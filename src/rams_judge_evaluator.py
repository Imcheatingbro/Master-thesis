"""RAMS 二分类 judge 实验的数据选择、调用、断点续跑与指标计算。"""

from __future__ import annotations

import csv
import json
import re
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATASET_PATH = PROJECT_ROOT / "Data" / "RAMS_judge" / "rams_judge_test.jsonl"
DEFAULT_PROMPT_PATH = PROJECT_ROOT / "prompts" / "rams_judge_v1.txt"

JsonObject = dict[str, Any]


def load_jsonlines(path: Path | str) -> list[JsonObject]:
    """读取 JSON Lines 文件。"""
    with Path(path).open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def select_records(
    records: list[JsonObject],
    sample_limit: int | None,
) -> list[JsonObject]:
    """从已固定打乱的数据顺序中选择全量或前 N 条。"""
    if sample_limit is None:
        return list(records)
    if sample_limit <= 0:
        raise ValueError("sample_limit 必须为正整数或 None")
    return list(records[:sample_limit])


def summarize_selection(records: list[JsonObject]) -> JsonObject:
    """统计运行前所选子集的标签和 case type 分布。"""
    return {
        "total": len(records),
        "labels": dict(
            sorted(Counter(str(record["label"]).lower() for record in records).items())
        ),
        "case_types": dict(
            sorted(Counter(str(record["case_type"]) for record in records).items())
        ),
    }


def load_prompt_template(path: Path | str = DEFAULT_PROMPT_PATH) -> str:
    """读取 RAMS judge prompt 模板。"""
    template = Path(path).read_text(encoding="utf-8")
    if "{input_json}" not in template:
        raise ValueError("prompt 模板缺少 {input_json} 占位符")
    return template


def build_prompt_input(record: JsonObject) -> JsonObject:
    """提取允许发送给模型的字段，避免标签和反例类型泄露。"""
    trigger = record["event"]["trigger"]
    candidate_span = record["candidate"]["span"]
    return {
        "document": [
            {"sentence_id": index, "text": sentence}
            for index, sentence in enumerate(record["sentences"])
        ],
        "event": {
            "type": record["event"]["type"],
            "trigger": {
                "text": trigger["text"],
                "sentence_id": trigger["sentence_id"],
                "token_start": trigger["sentence_start"],
                "token_end": trigger["sentence_end"],
            },
            "allowed_roles": record["event"]["allowed_roles"],
        },
        "candidate": {
            "role": record["candidate"]["role"],
            "span": {
                "text": candidate_span["text"],
                "sentence_id": candidate_span["sentence_id"],
                "token_start": candidate_span["sentence_start"],
                "token_end": candidate_span["sentence_end"],
            },
        },
    }


def build_judge_prompt(record: JsonObject, template: str) -> str:
    """将单条 RAMS 候选渲染为 judge prompt。"""
    input_json = json.dumps(build_prompt_input(record), ensure_ascii=False, indent=2)
    return template.replace("{input_json}", input_json)


def parse_judge_output(raw_output: str) -> bool:
    """从 DeepSeek 输出中解析严格 JSON boolean。"""
    cleaned = re.sub(
        r"<think>.*?</think>",
        "",
        raw_output,
        flags=re.DOTALL | re.IGNORECASE,
    ).strip()
    decoder = json.JSONDecoder()
    parsed: Any | None = None
    for index, character in enumerate(cleaned):
        if character != "{":
            continue
        try:
            parsed, _ = decoder.raw_decode(cleaned[index:])
            break
        except json.JSONDecodeError:
            continue

    if not isinstance(parsed, dict):
        raise ValueError("judge 输出中没有 JSON object")
    if not isinstance(parsed.get("valid"), bool):
        raise ValueError("judge 输出的 valid 必须是 JSON boolean")
    return parsed["valid"]


def evaluate_record(
    record: JsonObject,
    client: Any,
    prompt_template: str,
) -> JsonObject:
    """调用一次 judge，并保留原始输出、错误和耗时。"""
    raw_output = ""
    predicted_label: bool | None = None
    error: JsonObject | None = None
    started_at = time.perf_counter()

    try:
        prompt = build_judge_prompt(record, prompt_template)
        raw_output = str(client.chat(prompt))
        predicted_label = parse_judge_output(raw_output)
    except Exception as exc:
        error = {"type": type(exc).__name__, "message": str(exc)}

    gold_label = bool(record["label"])
    return {
        "id": record["id"],
        "pair_id": record["pair_id"],
        "doc_key": record["doc_key"],
        "case_type": record["case_type"],
        "gold_label": gold_label,
        "predicted_label": predicted_label,
        "correct": predicted_label is not None and predicted_label == gold_label,
        "raw_output": raw_output,
        "error": error,
        "elapsed_seconds": round(time.perf_counter() - started_at, 6),
    }


def load_latest_results(path: Path | str) -> dict[str, JsonObject]:
    """读取 checkpoint JSONL；同一 ID 多次出现时保留最后一次结果。"""
    result_path = Path(path)
    if not result_path.exists():
        return {}
    return {
        str(result["id"]): result
        for result in load_jsonlines(result_path)
        if isinstance(result.get("id"), str)
    }


def run_evaluation(
    records: list[JsonObject],
    client: Any,
    prompt_template: str,
    results_path: Path | str,
    max_workers: int = 5,
    retry_failed: bool = True,
    progress_callback: Any | None = None,
) -> list[JsonObject]:
    """并发运行 judge，每完成一条即追加 checkpoint，并支持断点续跑。"""
    output_path = Path(results_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    latest = load_latest_results(output_path)
    selected_ids = {str(record["id"]) for record in records}
    results_by_id = {
        record_id: result
        for record_id, result in latest.items()
        if record_id in selected_ids
    }

    pending = [
        record
        for record in records
        if str(record["id"]) not in results_by_id
        or (
            retry_failed
            and results_by_id[str(record["id"])].get("predicted_label") is None
        )
    ]

    if pending:
        with output_path.open("a", encoding="utf-8", newline="\n") as file:
            with ThreadPoolExecutor(max_workers=max(1, int(max_workers))) as executor:
                futures = {
                    executor.submit(
                        evaluate_record,
                        record,
                        client,
                        prompt_template,
                    ): record["id"]
                    for record in pending
                }
                for future in as_completed(futures):
                    result = future.result()
                    results_by_id[str(result["id"])] = result
                    file.write(json.dumps(result, ensure_ascii=False) + "\n")
                    file.flush()
                    if progress_callback is not None:
                        progress_callback(result)

    return [
        results_by_id[str(record["id"])]
        for record in records
        if str(record["id"]) in results_by_id
    ]


def compute_metrics(results: list[JsonObject]) -> JsonObject:
    """计算严格二分类指标；无有效 boolean 的结果按最坏情况计错。"""
    total = len(results)
    if total == 0:
        raise ValueError("没有可计算指标的结果")

    tp = tn = fp = fn = 0
    valid_count = 0
    valid_correct = 0
    case_total: Counter[str] = Counter()
    case_correct: Counter[str] = Counter()

    for result in results:
        gold = bool(result["gold_label"])
        predicted = result.get("predicted_label")
        case_type = str(result["case_type"])
        case_total[case_type] += 1

        if isinstance(predicted, bool):
            valid_count += 1
            is_correct = predicted == gold
            if is_correct:
                valid_correct += 1
                case_correct[case_type] += 1
            if gold and predicted:
                tp += 1
            elif not gold and not predicted:
                tn += 1
            elif not gold and predicted:
                fp += 1
            else:
                fn += 1
        elif gold:
            fn += 1
        else:
            fp += 1

    positive_precision = _safe_divide(tp, tp + fp)
    positive_recall = _safe_divide(tp, tp + fn)
    positive_f1 = _f1(positive_precision, positive_recall)
    negative_precision = _safe_divide(tn, tn + fn)
    negative_recall = _safe_divide(tn, tn + fp)
    negative_f1 = _f1(negative_precision, negative_recall)

    return {
        "total": total,
        "valid_responses": valid_count,
        "invalid_responses": total - valid_count,
        "coverage": _safe_divide(valid_count, total),
        "accuracy": _safe_divide(tp + tn, total),
        "precision": positive_precision,
        "recall": positive_recall,
        "f1": positive_f1,
        "macro_f1": (positive_f1 + negative_f1) / 2,
        "valid_response_accuracy": _safe_divide(valid_correct, valid_count),
        "confusion_matrix": {
            "tp": tp,
            "tn": tn,
            "fp": fp,
            "fn": fn,
        },
        "per_case_accuracy": {
            case_type: _safe_divide(case_correct[case_type], count)
            for case_type, count in sorted(case_total.items())
        },
        "invalid_response_policy": (
            "无有效 JSON boolean 时严格计错：gold=True 计 FN，gold=False 计 FP"
        ),
    }


def build_comparison_records(
    records: list[JsonObject],
    results: list[JsonObject],
) -> list[JsonObject]:
    """将模型输入、gold 和真实输出整理为逐条可审计对比记录。"""
    source_by_id = {str(record["id"]): record for record in records}
    comparisons: list[JsonObject] = []

    for result in results:
        record_id = str(result["id"])
        if record_id not in source_by_id:
            raise ValueError(f"结果缺少对应的源记录: {record_id}")
        source = source_by_id[record_id]
        gold_label = bool(source["label"])
        if bool(result["gold_label"]) != gold_label:
            raise ValueError(f"结果中的 gold label 与源数据不一致: {record_id}")

        comparisons.append(
            {
                "id": record_id,
                "pair_id": source["pair_id"],
                "doc_key": source["doc_key"],
                "case_type": source["case_type"],
                "model_input": build_prompt_input(source),
                "gold": {"valid": gold_label},
                "model_output": {
                    "raw": result.get("raw_output", ""),
                    "parsed_valid": result.get("predicted_label"),
                    "correct": bool(result.get("correct")),
                    "error": result.get("error"),
                    "elapsed_seconds": result.get("elapsed_seconds"),
                },
            }
        )
    return comparisons


def save_comparison_outputs(
    records: list[JsonObject],
    results: list[JsonObject],
    output_dir: Path | str,
) -> dict[str, Path]:
    """保存错误详情和包含全量对比的扁平 CSV。"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    comparisons = build_comparison_records(records, results)
    mistakes = [
        comparison
        for comparison in comparisons
        if not comparison["model_output"]["correct"]
    ]

    mistakes_path = output_path / "mistakes.jsonl"
    csv_path = output_path / "comparison.csv"
    _write_jsonlines(mistakes_path, mistakes)

    fieldnames = [
        "id",
        "pair_id",
        "doc_key",
        "case_type",
        "event_type",
        "trigger",
        "candidate_role",
        "candidate_span",
        "gold_valid",
        "predicted_valid",
        "correct",
        "error_type",
        "error_message",
        "raw_output",
        "document",
    ]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for comparison in comparisons:
            model_input = comparison["model_input"]
            model_output = comparison["model_output"]
            error = model_output.get("error") or {}
            writer.writerow(
                {
                    "id": comparison["id"],
                    "pair_id": comparison["pair_id"],
                    "doc_key": comparison["doc_key"],
                    "case_type": comparison["case_type"],
                    "event_type": model_input["event"]["type"],
                    "trigger": model_input["event"]["trigger"]["text"],
                    "candidate_role": model_input["candidate"]["role"],
                    "candidate_span": model_input["candidate"]["span"]["text"],
                    "gold_valid": comparison["gold"]["valid"],
                    "predicted_valid": model_output["parsed_valid"],
                    "correct": model_output["correct"],
                    "error_type": error.get("type", ""),
                    "error_message": error.get("message", ""),
                    "raw_output": model_output["raw"],
                    "document": "\n".join(
                        sentence["text"] for sentence in model_input["document"]
                    ),
                }
            )

    return {
        "mistakes_jsonl": mistakes_path,
        "comparison_csv": csv_path,
    }


def save_json(path: Path | str, payload: JsonObject) -> Path:
    """将配置或指标保存为 UTF-8 JSON。"""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output_path


def _write_jsonlines(path: Path, records: list[JsonObject]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")


def _safe_divide(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 0.0


def _f1(precision: float, recall: float) -> float:
    return 2 * precision * recall / (precision + recall) if precision + recall else 0.0
