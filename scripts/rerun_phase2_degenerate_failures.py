"""Rerun eligible repetitive-output failures with a freshly loaded model and rebuild summaries."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.repair_phase2_qwen27_missing_triple import _rebuild_report, _update_summary_rows
from src.data_io import load_dataset
from src.generator import classify_generation_error, parse_output_with_metadata
from src.llm_client import LLMClient
from src.prompt_builder import build_messages
from src.retriever import (
    ExactCountHybridRetriever,
    KNNRetriever,
    PatternRetriever,
    resolve_rag_cache_paths,
)


CHECKPOINT_DIR = (
    PROJECT_ROOT / "results" / "eval_checkpoints" / "rag_ablation"
    / "phase2_qwen27_v9.8_anchor"
)
REPORT_DIR = (
    PROJECT_ROOT / "results" / "eval_report" / "rag_ablation"
    / "phase2_qwen27_v9.8_anchor"
)
SUMMARY_PATH = REPORT_DIR / "phase2_qwen27_v9.8_anchor_summary.csv"
K_SELECTION_PATH = REPORT_DIR / "phase2_qwen27_v9.8_anchor_k_selection.csv"
MODEL_KEY = "local/qwen3.6-27b-no-thinking"
MODEL_DISPLAY_NAME = "Qwen3.6 27B No Thinking"
BASE_URL = "http://127.0.0.1:1234/v1"
API_KEY = "lm-studio"
CONTEXT_LENGTH = 8192
PARALLEL = 4
OFFLOAD_KV_CACHE_TO_GPU = True
MAX_TOKENS = 2048
TEMPERATURE = 0.0
CACHE_PROMPT = False
MODEL_LOAD_TIMEOUT = 1200
LLM_TIMEOUT = 600
RETRY_TIMES = 3
RECOVERY_TYPE = "fresh_model_rerun_after_degenerate_max_length_loop"


def _is_degenerate_loop(raw_output: str) -> bool:
    text = str(raw_output or "").strip()
    if len(text) < MAX_TOKENS:
        return False
    if len(set(text)) <= 4:
        return True
    dominant_count = max(text.count(char) for char in set(text))
    return dominant_count / len(text) >= 0.98


def _eligible_prediction(prediction: dict[str, Any]) -> bool:
    attempts = prediction.get("generation_attempts", [])
    return bool(attempts) and all(
        isinstance(attempt, dict)
        and isinstance(attempt.get("raw_output"), str)
        and _is_degenerate_loop(attempt["raw_output"])
        for attempt in attempts
    )


def _load_targets() -> list[dict[str, Any]]:
    targets: list[dict[str, Any]] = []
    for checkpoint_path in sorted(CHECKPOINT_DIR.glob("fixed_rag_k*.jsonl")):
        manifest_path = checkpoint_path.with_suffix(".manifest.json")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("status") != "complete":
            continue
        k = int(manifest["signature_payload"]["rag_top_k"])
        rows = [
            json.loads(line)
            for line in checkpoint_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        for row_index, row in enumerate(rows):
            prediction = row.get("prediction", {})
            if _eligible_prediction(prediction):
                targets.append(
                    {
                        "checkpoint_path": checkpoint_path,
                        "manifest_path": manifest_path,
                        "manifest": manifest,
                        "rows": rows,
                        "row_index": row_index,
                        "sample_id": row["sample_id"],
                        "k": k,
                        "original_prediction": prediction,
                    }
                )
    return targets


def _unload_all(manager: LLMClient, stage: str) -> None:
    manager.unload_all_models()
    remaining = manager.list_loaded_instances()
    if remaining:
        raise RuntimeError(f"{stage}后仍有已加载模型：{remaining}")


def _load_fresh_client(manager: LLMClient) -> tuple[LLMClient, str]:
    _unload_all(manager, "fresh rerun 加载前卸载")
    result = manager.load_model(
        MODEL_KEY,
        context_length=CONTEXT_LENGTH,
        parallel=PARALLEL,
        offload_kv_cache_to_gpu=OFFLOAD_KV_CACHE_TO_GPU,
    )
    load_config = result.get("load_config", {})
    actual = {
        "context_length": int(load_config.get("context_length", 0)),
        "parallel": int(load_config.get("parallel", 0)),
        "offload_kv_cache_to_gpu": load_config.get("offload_kv_cache_to_gpu") is True,
    }
    expected = {
        "context_length": CONTEXT_LENGTH,
        "parallel": PARALLEL,
        "offload_kv_cache_to_gpu": OFFLOAD_KV_CACHE_TO_GPU,
    }
    if actual != expected:
        manager.unload_all_models()
        raise RuntimeError(f"模型加载配置不一致：{actual} != {expected}")
    instance_id = str(result["instance_id"])
    return (
        LLMClient(
            provider="lmstudio",
            base_url=BASE_URL,
            model=instance_id,
            api_key=API_KEY,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            context_length=CONTEXT_LENGTH,
            reasoning="off",
            extra_body={"cache_prompt": CACHE_PROMPT},
            timeout=LLM_TIMEOUT,
            retry_times=RETRY_TIMES,
        ),
        instance_id,
    )


def _attempt_target(
    *,
    manager: LLMClient,
    retriever: ExactCountHybridRetriever,
    sample: dict[str, Any],
    k: int,
    max_fresh_attempts: int,
) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    messages = build_messages(
        sample["text"],
        use_rag=True,
        retriever=retriever,
        top_k=k,
        rag_mode="knn_pattern",
        prompt_name="v9.8",
    )
    attempts: list[dict[str, Any]] = []
    for fresh_attempt in range(1, max_fresh_attempts + 1):
        client: LLMClient | None = None
        instance_id = ""
        raw_output = ""
        try:
            client, instance_id = _load_fresh_client(manager)
            raw_output = client.chat(messages)
            parsed, repair_type = parse_output_with_metadata(raw_output)
            prediction: dict[str, Any] = {
                "id": sample["id"],
                "has_causal": parsed["has_causal"],
                "triples": parsed["triples"],
                "generation_recovery_type": RECOVERY_TYPE,
                "generation_recovery_fresh_attempt": fresh_attempt,
            }
            if repair_type is not None:
                prediction["parse_repair_type"] = repair_type
                prediction["parse_repair_raw_output"] = raw_output
            attempts.append(
                {
                    "fresh_attempt": fresh_attempt,
                    "instance_id": instance_id,
                    "success": True,
                    "repair_type": repair_type,
                    "raw_output": raw_output,
                }
            )
            return prediction, attempts
        except Exception as exc:
            attempts.append(
                {
                    "fresh_attempt": fresh_attempt,
                    "instance_id": instance_id,
                    "success": False,
                    "error_type": classify_generation_error(exc),
                    "error_message": str(exc),
                    "degenerate_loop": _is_degenerate_loop(str(raw_output)),
                    "raw_output": str(raw_output),
                }
            )
        finally:
            if client is not None:
                _unload_all(manager, f"fresh attempt {fresh_attempt} 卸载")
    return None, attempts


def _atomic_write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    temporary = path.with_suffix(path.suffix + ".fresh-rerun.tmp")
    temporary.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )
    temporary.replace(path)


def _backup(path: Path, backup_dir: Path) -> None:
    if path.exists():
        backup_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, backup_dir / path.name)


def _rebuild_k_selection() -> None:
    import pandas as pd

    frame = pd.read_csv(SUMMARY_PATH)
    completed = frame.loc[frame["status"] == "completed"].drop_duplicates("run_id", keep="last")
    fixed_row = completed.loc[completed["run_id"] == "fixed"].iloc[0]
    rows: list[dict[str, Any]] = []
    for k in (1, 3, 5):
        rag_row = completed.loc[completed["run_id"] == f"fixed_rag_k{k}"].iloc[0]
        random_row = completed.loc[completed["run_id"] == f"fixed_random_k{k}"].iloc[0]
        rows.append(
            {
                "k": k,
                "anchor_all_precision": rag_row["anchor_all_precision"],
                "anchor_all_recall": rag_row["anchor_all_recall"],
                "anchor_all_f1": rag_row["anchor_all_f1"],
                "delta_anchor_vs_fixed": rag_row["anchor_all_f1"] - fixed_row["anchor_all_f1"],
                "delta_anchor_vs_random_same_k": (
                    rag_row["anchor_all_f1"] - random_row["anchor_all_f1"]
                ),
                "detection_f1": rag_row["detection_f1"],
                "strict_all_f1_auxiliary": rag_row["strict_all_f1"],
                "anchor_detected_only_f1": rag_row["anchor_detected_only_f1"],
            }
        )
    selection = pd.DataFrame(rows).sort_values(
        ["anchor_all_f1", "k"], ascending=[False, True]
    ).reset_index(drop=True)
    selection.insert(0, "selection_rank", range(1, len(selection) + 1))
    temporary = K_SELECTION_PATH.with_suffix(K_SELECTION_PATH.suffix + ".fresh-rerun.tmp")
    selection.to_csv(temporary, index=False, encoding="utf-8-sig")
    temporary.replace(K_SELECTION_PATH)


def run(*, apply: bool, max_fresh_attempts: int) -> dict[str, Any]:
    targets = _load_targets()
    result: dict[str, Any] = {
        "mode": "apply" if apply else "dry_run",
        "recovery_type": RECOVERY_TYPE,
        "target_count": len(targets),
        "targets": [
            {"run_name": target["manifest"]["run_name"], "k": target["k"], "sample_id": target["sample_id"]}
            for target in targets
        ],
    }
    if not apply or not targets:
        return result

    manager = LLMClient(
        provider="lmstudio",
        base_url=BASE_URL,
        model=MODEL_KEY,
        api_key=API_KEY,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        context_length=CONTEXT_LENGTH,
        reasoning="off",
        extra_body={"cache_prompt": CACHE_PROMPT},
        timeout=MODEL_LOAD_TIMEOUT,
        retry_times=RETRY_TIMES,
    )
    inventory_keys = {
        str(item["key"])
        for item in manager.list_local_models()
        if item.get("key")
    }
    if MODEL_KEY not in inventory_keys:
        raise RuntimeError(f"LM Studio 中找不到 {MODEL_KEY}")

    metadata_path, embeddings_path = resolve_rag_cache_paths("cnc")
    retriever = ExactCountHybridRetriever(
        pattern_retriever=PatternRetriever(metadata_path=metadata_path),
        knn_retriever=KNNRetriever(
            metadata_path=metadata_path,
            embeddings_path=embeddings_path,
            device="cpu",
        ),
    )
    samples = {sample["id"]: sample for sample in load_dataset("cnc_sft_validation")}
    outcomes: list[dict[str, Any]] = []
    for target in targets:
        prediction, fresh_attempts = _attempt_target(
            manager=manager,
            retriever=retriever,
            sample=samples[target["sample_id"]],
            k=target["k"],
            max_fresh_attempts=max_fresh_attempts,
        )
        outcomes.append(
            {
                "run_name": target["manifest"]["run_name"],
                "k": target["k"],
                "sample_id": target["sample_id"],
                "success": prediction is not None,
                "prediction": prediction,
                "fresh_attempts": fresh_attempts,
                "original_prediction_sha256": hashlib.sha256(
                    json.dumps(
                        target["original_prediction"],
                        ensure_ascii=False,
                        sort_keys=True,
                    ).encode("utf-8")
                ).hexdigest(),
            }
        )
        target["new_prediction"] = prediction

    successful_targets = [target for target in targets if target.get("new_prediction") is not None]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    result["outcomes"] = outcomes
    result["success_count"] = len(successful_targets)
    if not successful_targets:
        audit_path = REPORT_DIR / f"degenerate_fresh_rerun_audit_{timestamp}.json"
        result["audit_path"] = str(audit_path)
        audit_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return result

    backup_dir = PROJECT_ROOT / "results" / "repair_backups" / f"degenerate-{timestamp}"
    _backup(SUMMARY_PATH, backup_dir)
    _backup(K_SELECTION_PATH, backup_dir)
    changed_checkpoints: dict[Path, dict[str, Any]] = {}
    for target in successful_targets:
        checkpoint_path = target["checkpoint_path"]
        changed = changed_checkpoints.setdefault(
            checkpoint_path,
            {
                "rows": target["rows"],
                "manifest": target["manifest"],
                "manifest_path": target["manifest_path"],
            },
        )
        changed["rows"][target["row_index"]]["prediction"] = target["new_prediction"]

    for checkpoint_path, changed in changed_checkpoints.items():
        _backup(checkpoint_path, backup_dir)
        _backup(changed["manifest_path"], backup_dir)
        report_path = Path(changed["manifest"]["report_path"])
        _backup(report_path, backup_dir)
        _backup(report_path.with_name(f"{report_path.stem}_generation_failures.jsonl"), backup_dir)
        _backup(report_path.with_name(f"{report_path.stem}_parse_repairs.jsonl"), backup_dir)
        _atomic_write_jsonl(checkpoint_path, changed["rows"])

    reports: dict[str, dict[str, Any]] = {}
    all_samples = load_dataset("cnc_sft_validation")
    for checkpoint_path, changed in changed_checkpoints.items():
        report = _rebuild_report(changed["manifest"], checkpoint_path, all_samples)
        run_name = str(changed["manifest"]["run_name"])
        reports[run_name] = report
        failure_path = Path(report["report_path"]).with_name(
            f"{Path(report['report_path']).stem}_generation_failures.jsonl"
        )
        if report["generation_failures"]["total"] == 0 and failure_path.exists():
            failure_path.unlink()
    _update_summary_rows(reports)
    _rebuild_k_selection()

    result["backup_dir"] = str(backup_dir)
    result["rebuilt_reports"] = {
        run_name: {
            "report_path": report["report_path"],
            "generation_failures": report["generation_failures"]["total"],
            "detection_f1": report["detection"]["f1"],
            "anchor_all_f1": report["extraction"]["anchor_window"]["all_samples"]["f1"],
        }
        for run_name, report in reports.items()
    }
    audit_path = REPORT_DIR / f"degenerate_fresh_rerun_audit_{timestamp}.json"
    result["audit_path"] = str(audit_path)
    audit_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--max-fresh-attempts", type=int, default=3)
    args = parser.parse_args()
    if args.max_fresh_attempts < 1:
        raise ValueError("--max-fresh-attempts 必须 >= 1")
    print(
        json.dumps(
            run(apply=args.apply, max_fresh_attempts=args.max_fresh_attempts),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
