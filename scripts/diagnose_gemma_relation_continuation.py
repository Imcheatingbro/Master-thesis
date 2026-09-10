"""Analyze Gemma continuation and stopping behavior at gold triple boundaries."""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from statistics import median
from typing import Any


LOGGER = logging.getLogger(__name__)
CONTINUE_SUFFIX = ","
STOP_SUFFIX = "]"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="诊断 Gemma triple continuation logits")
    parser.add_argument(
        "--model-path",
        type=Path,
        default=Path("outputs/finetuning/gemma4_12b_cnc_qlora_unsloth_v1"),
    )
    parser.add_argument("--dataset-dir", type=Path, default=Path("Data/CNC_sft_gemma_v2"))
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("results/diagnostics/gemma4_12b_relation_continuation_v1"),
    )
    parser.add_argument("--splits", nargs="+", default=["train", "validation"])
    parser.add_argument("--max-seq-length", type=int, default=2048)
    parser.add_argument("--progress-every", type=int, default=50)
    return parser.parse_args()


def build_boundary_specs(record: dict[str, Any]) -> list[dict[str, Any]]:
    messages = record.get("messages")
    if not isinstance(messages, list) or len(messages) < 3:
        raise ValueError(f"样本 {record.get('id')} 缺少完整 messages")
    target_text = str(messages[2].get("content", ""))
    target = json.loads(target_text)
    triples = target.get("triples")
    if not bool(target.get("has_causal")):
        return []
    if not isinstance(triples, list) or not triples:
        raise ValueError(f"正例 {record.get('id')} 没有 triples")

    compact_target = json.dumps(target, ensure_ascii=False, separators=(",", ":"))
    if compact_target != target_text:
        raise ValueError(f"样本 {record.get('id')} 的 target 不是训练使用的 compact JSON")

    serialized_triples = [
        json.dumps(triple, ensure_ascii=False, separators=(",", ":")) for triple in triples
    ]
    specs: list[dict[str, Any]] = []
    for boundary_index in range(1, len(serialized_triples) + 1):
        assistant_prefix = '{"has_causal":true,"triples":[' + ",".join(
            serialized_triples[:boundary_index]
        )
        expected_continue = boundary_index < len(serialized_triples)
        expected_character = CONTINUE_SUFFIX if expected_continue else STOP_SUFFIX
        actual_character = target_text[len(assistant_prefix) : len(assistant_prefix) + 1]
        if actual_character != expected_character:
            raise ValueError(
                f"样本 {record.get('id')} 边界 {boundary_index} 不符合 compact target："
                f"expected={expected_character!r}, actual={actual_character!r}"
            )
        specs.append(
            {
                "id": record.get("id"),
                "relation_count": len(serialized_triples),
                "boundary_index": boundary_index,
                "expected_continue": expected_continue,
                "continue_answer": (
                    target_text
                    if expected_continue
                    else assistant_prefix + "," + serialized_triples[0] + "]}"
                ),
                "stop_answer": assistant_prefix + "]}",
            }
        )
    return specs


def find_branch_tokens(continue_ids: list[int], stop_ids: list[int]) -> tuple[int, int, int]:
    common_length = 0
    for continue_id, stop_id in zip(continue_ids, stop_ids):
        if continue_id != stop_id:
            break
        common_length += 1
    if common_length >= len(continue_ids) or common_length >= len(stop_ids):
        raise ValueError("continue/stop token 序列没有可比较的首个分叉 token")
    return common_length, continue_ids[common_length], stop_ids[common_length]


def summarize_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    continue_rows = [row for row in rows if bool(row["expected_continue"])]
    stop_rows = [row for row in rows if not bool(row["expected_continue"])]
    pairwise_continue_correct = sum(float(row["margin"]) > 0 for row in continue_rows)
    pairwise_stop_correct = sum(float(row["margin"]) < 0 for row in stop_rows)
    ties = sum(float(row["margin"]) == 0 for row in rows)
    top_candidate = sum(bool(row["top_is_candidate"]) for row in rows)
    top_correct = sum(bool(row["top_is_expected"]) for row in rows)
    return {
        "boundaries": len(rows),
        "expected_continue": len(continue_rows),
        "expected_stop": len(stop_rows),
        "pairwise_continue_correct": pairwise_continue_correct,
        "pairwise_continue_accuracy": _safe_div(pairwise_continue_correct, len(continue_rows)),
        "pairwise_stop_correct": pairwise_stop_correct,
        "pairwise_stop_accuracy": _safe_div(pairwise_stop_correct, len(stop_rows)),
        "pairwise_overall_accuracy": _safe_div(
            pairwise_continue_correct + pairwise_stop_correct,
            len(rows),
        ),
        "margin_median_continue": _median_or_none(continue_rows),
        "margin_median_stop": _median_or_none(stop_rows),
        "margin_ties": ties,
        "top_token_candidate_rate": _safe_div(top_candidate, len(rows)),
        "top_token_expected_rate": _safe_div(top_correct, len(rows)),
        "pairwise_auc": _pairwise_auc(continue_rows, stop_rows),
    }


def _median_or_none(rows: list[dict[str, Any]]) -> float | None:
    if not rows:
        return None
    return float(median(float(row["margin"]) for row in rows))


def _pairwise_auc(
    continue_rows: list[dict[str, Any]],
    stop_rows: list[dict[str, Any]],
) -> float | None:
    if not continue_rows or not stop_rows:
        return None
    continue_margins = [float(row["margin"]) for row in continue_rows]
    stop_margins = [float(row["margin"]) for row in stop_rows]
    wins = sum(left > right for left in continue_margins for right in stop_margins)
    ties = sum(left == right for left in continue_margins for right in stop_margins)
    return (wins + 0.5 * ties) / (len(continue_margins) * len(stop_margins))


def _safe_div(numerator: int, denominator: int) -> float:
    return 0.0 if denominator == 0 else numerator / denominator


def _render_training_answer(
    text_tokenizer: Any,
    messages: list[dict[str, str]],
    assistant_answer: str,
) -> str:
    variant_messages = [*messages[:2], {"role": "assistant", "content": assistant_answer}]
    rendered = text_tokenizer.apply_chat_template(
        variant_messages,
        add_generation_prompt=False,
        tokenize=False,
        enable_thinking=False,
    )
    return rendered.removeprefix(text_tokenizer.bos_token or "")


def _truncate_processor_inputs(batch: Any, common_length: int, torch: Any) -> dict[str, Any]:
    full_length = int(batch["input_ids"].shape[-1])
    truncated: dict[str, Any] = {}
    for key, value in batch.items():
        if isinstance(value, torch.Tensor) and value.ndim >= 2 and value.shape[-1] == full_length:
            truncated[key] = value[..., :common_length].to("cuda")
        elif isinstance(value, torch.Tensor):
            truncated[key] = value.to("cuda")
        else:
            truncated[key] = value
    return truncated


def _score_boundary(
    model: Any,
    processor: Any,
    text_tokenizer: Any,
    torch: Any,
    messages: list[dict[str, str]],
    spec: dict[str, Any],
) -> dict[str, Any]:
    continue_text = _render_training_answer(
        text_tokenizer,
        messages,
        str(spec["continue_answer"]),
    )
    stop_text = _render_training_answer(
        text_tokenizer,
        messages,
        str(spec["stop_answer"]),
    )
    continue_batch = processor(
        text=[continue_text],
        return_tensors="pt",
        add_special_tokens=False,
    )
    stop_batch = processor(
        text=[stop_text],
        return_tensors="pt",
        add_special_tokens=False,
    )
    continue_ids = continue_batch["input_ids"][0].tolist()
    stop_ids = stop_batch["input_ids"][0].tolist()
    common_length, continue_token_id, stop_token_id = find_branch_tokens(continue_ids, stop_ids)
    inputs = _truncate_processor_inputs(continue_batch, common_length, torch)
    with torch.inference_mode():
        outputs = model(**inputs, logits_to_keep=1)
    logits = outputs.logits[0, -1].float()
    continue_logit = float(logits[continue_token_id].item())
    stop_logit = float(logits[stop_token_id].item())
    top_token_id = int(logits.argmax().item())
    expected_token_id = continue_token_id if bool(spec["expected_continue"]) else stop_token_id
    return {
        **{
            key: value
            for key, value in spec.items()
            if key not in {"continue_answer", "stop_answer"}
        },
        "context_tokens": common_length,
        "continue_token_id": continue_token_id,
        "continue_token": text_tokenizer.decode([continue_token_id], skip_special_tokens=False),
        "stop_token_id": stop_token_id,
        "stop_token": text_tokenizer.decode([stop_token_id], skip_special_tokens=False),
        "continue_logit": continue_logit,
        "stop_logit": stop_logit,
        "margin": continue_logit - stop_logit,
        "top_token_id": top_token_id,
        "top_token": text_tokenizer.decode([top_token_id], skip_special_tokens=False),
        "top_is_candidate": top_token_id in {continue_token_id, stop_token_id},
        "top_is_expected": top_token_id == expected_token_id,
    }


def _load_records(dataset_dir: Path, split: str) -> list[dict[str, Any]]:
    path = dataset_dir / f"{split}.jsonl"
    if not path.is_file():
        raise FileNotFoundError(path)
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def main() -> None:
    args = _parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    model_path = args.model_path.resolve()
    dataset_dir = args.dataset_dir.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    import unsloth
    import torch
    from unsloth import FastModel
    from unsloth.chat_templates import get_chat_template

    model, processor = FastModel.from_pretrained(
        model_name=str(model_path),
        max_seq_length=args.max_seq_length,
        dtype=torch.bfloat16,
        load_in_4bit=True,
        full_finetuning=False,
        trust_remote_code=False,
    )
    processor = get_chat_template(processor, chat_template="gemma-4")
    FastModel.for_inference(model)
    text_tokenizer = processor.tokenizer if hasattr(processor, "tokenizer") else processor

    all_scored: list[dict[str, Any]] = []
    split_summaries: dict[str, Any] = {}
    for split in args.splits:
        records = _load_records(dataset_dir, split)
        positive_records = [record for record in records if bool(record.get("has_causal"))]
        output_path = output_dir / f"{split}_boundary_scores.jsonl"
        split_scored: list[dict[str, Any]] = []
        completed = 0
        with output_path.open("w", encoding="utf-8") as handle:
            for record in positive_records:
                for spec in build_boundary_specs(record):
                    scored = _score_boundary(
                        model=model,
                        processor=processor,
                        text_tokenizer=text_tokenizer,
                        torch=torch,
                        messages=record["messages"],
                        spec=spec,
                    )
                    scored["split"] = split
                    handle.write(json.dumps(scored, ensure_ascii=False) + "\n")
                    split_scored.append(scored)
                    all_scored.append(scored)
                    completed += 1
                    if completed % args.progress_every == 0:
                        handle.flush()
                        LOGGER.info("%s scored %s boundaries", split, completed)
        split_summaries[split] = {
            "samples": len(records),
            "positive_samples": len(positive_records),
            **summarize_rows(split_scored),
        }
        LOGGER.info("%s summary: %s", split, json.dumps(split_summaries[split], ensure_ascii=False))

    summary = {
        "model_path": str(model_path),
        "dataset_dir": str(dataset_dir),
        "batch_size": 1,
        "splits": split_summaries,
        "overall": summarize_rows(all_scored),
    }
    summary_path = output_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    LOGGER.info("RESULT %s", json.dumps(summary, ensure_ascii=False))
    LOGGER.info("summary saved: %s", summary_path)


if __name__ == "__main__":
    main()
