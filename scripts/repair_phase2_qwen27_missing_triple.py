"""Repair the defined Qwen missing-brace failure and rebuild affected reports offline."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data_io import load_dataset
from src.eval_pipeline import EvalRunConfig, run_stream_eval
from src.generator import MISSING_TRIPLE_CLOSING_BRACE_REPAIR, parse_output_with_metadata
from src.retriever import resolve_rag_cache_paths


CHECKPOINT_DIR = (
    PROJECT_ROOT
    / "results"
    / "eval_checkpoints"
    / "rag_ablation"
    / "phase2_qwen27_v9.8_anchor"
)
REPORT_DIR = (
    PROJECT_ROOT
    / "results"
    / "eval_report"
    / "rag_ablation"
    / "phase2_qwen27_v9.8_anchor"
)
SUMMARY_PATH = REPORT_DIR / "phase2_qwen27_v9.8_anchor_summary.csv"
MODEL_DISPLAY_NAME = "Qwen3.6 27B No Thinking"


class _OfflineRetriever:

    def retrieve(self, text: str, top_k: int) -> list[dict[str, Any]]:
        raise RuntimeError("Offline report rebuild must not perform retrieval.")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _json_key(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _atomic_write_text(path: Path, text: str, *, encoding: str = "utf-8") -> None:
    temporary_path = path.with_suffix(path.suffix + ".offline-repair.tmp")
    temporary_path.write_text(text, encoding=encoding)
    temporary_path.replace(path)


def _repair_prediction(sample_id: Any, prediction: dict[str, Any]) -> tuple[dict[str, Any], str] | None:
    if prediction.get("error_type") != "no_json_object":
        return None
    repaired_attempts: list[tuple[dict[str, Any], str]] = []
    for attempt in prediction.get("generation_attempts", []):
        if not isinstance(attempt, dict) or not isinstance(attempt.get("raw_output"), str):
            continue
        raw_output = attempt["raw_output"]
        try:
            parsed, repair_type = parse_output_with_metadata(raw_output)
        except (TypeError, ValueError, json.JSONDecodeError):
            continue
        if repair_type == MISSING_TRIPLE_CLOSING_BRACE_REPAIR:
            repaired_attempts.append((parsed, raw_output))
    if not repaired_attempts:
        return None

    normalized_outputs = {
        json.dumps(parsed, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        for parsed, _ in repaired_attempts
    }
    if len(normalized_outputs) != 1:
        raise RuntimeError(f"Sample id={sample_id!r} 的多次可修复输出语义不一致，拒绝自动选择。")
    parsed, raw_output = repaired_attempts[0]
    return (
        {
            "id": prediction.get("id", sample_id),
            "has_causal": parsed["has_causal"],
            "triples": parsed["triples"],
            "parse_repair_type": MISSING_TRIPLE_CLOSING_BRACE_REPAIR,
            "parse_repair_raw_output": raw_output,
        },
        raw_output,
    )


def _scan_checkpoint(path: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    repairs: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if "sample_id" not in row or not isinstance(row.get("prediction"), dict):
            raise RuntimeError(f"{path.name} 第 {line_number} 行不是有效 checkpoint row。")
        repaired = _repair_prediction(row["sample_id"], row["prediction"])
        if repaired is not None:
            new_prediction, raw_output = repaired
            repairs.append(
                {
                    "sample_id": row["sample_id"],
                    "old_error_type": row["prediction"].get("error_type"),
                    "repair_type": MISSING_TRIPLE_CLOSING_BRACE_REPAIR,
                    "raw_output_sha256": hashlib.sha256(raw_output.encode("utf-8")).hexdigest(),
                }
            )
            row["prediction"] = new_prediction
        rows.append(row)
    return rows, repairs


def _serialize_checkpoint(rows: list[dict[str, Any]]) -> str:
    return "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
        for row in rows
    )


def _load_prediction_map(path: Path) -> dict[str, dict[str, Any]]:
    predictions: dict[str, dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        predictions[_json_key(row["sample_id"])] = row["prediction"]
    return predictions


def _report_timestamp(report_path: Path) -> datetime:
    match = re.search(r"_(\d{8}-\d{6})\.md$", report_path.name)
    if match is None:
        raise RuntimeError(f"无法从报告文件名恢复时间：{report_path.name}")
    return datetime.strptime(match.group(1), "%Y%m%d-%H%M%S")


def _rebuild_report(
    manifest: dict[str, Any],
    checkpoint_path: Path,
    samples: list[dict[str, Any]],
) -> dict[str, Any]:
    signature = manifest["signature_payload"]
    predictions = _load_prediction_map(checkpoint_path)
    if len(predictions) != len(samples):
        raise RuntimeError(
            f"完成态 checkpoint {checkpoint_path.name} 只有 {len(predictions)}/{len(samples)} 条。"
        )

    def cached_generator(**kwargs: Any) -> dict[str, Any]:
        sample_id = kwargs.get("sample_id")
        prediction = predictions.get(_json_key(sample_id))
        if prediction is None:
            raise RuntimeError(f"Checkpoint 缺少 sample id={sample_id!r}。")
        return prediction

    report_path = Path(manifest["report_path"])
    metadata_path, embeddings_path = resolve_rag_cache_paths("cnc")
    config = EvalRunConfig(
        project_root=PROJECT_ROOT,
        model=str(signature["model_key"]),
        dataset=str(signature["dataset"]),
        prompt_name=str(signature["prompt_name"]),
        use_rag=str(signature["retriever_kind"]) != "none",
        rag_mode=str(signature["rag_mode"]),
        rag_top_k=int(signature["rag_top_k"]),
        temperature=float(signature["temperature"]),
        max_tokens=int(signature["max_tokens"]),
        primary_metric=str(signature["primary_metric"]),
        progress_every=0,
        max_workers=1,
        llm_provider="lmstudio",
        llm_base_url="http://127.0.0.1:1234/v1",
        context_length=int(signature["context_length"]),
        reasoning_effort=None,
        llm_extra_body={"cache_prompt": bool(signature["cache_prompt"])},
        api_key_source="lmstudio-default",
        save_report=True,
        report_dir=REPORT_DIR,
        report_detail_limit=200,
        report_detail_mode="errors",
        report_error_metric=str(signature["primary_metric"]),
        metadata_path=metadata_path,
        embeddings_path=embeddings_path,
    )
    report = run_stream_eval(
        samples=samples,
        label=f"{MODEL_DISPLAY_NAME} CNC validation {manifest['run_name']}",
        client=object(),
        config=config,
        generator=cached_generator,
        existing_retriever=_OfflineRetriever(),
        generated_at=_report_timestamp(report_path),
    )
    rebuilt_path = Path(report["report_path"])
    if rebuilt_path.resolve() != report_path.resolve():
        raise RuntimeError(f"重建报告路径变化：{report_path} -> {rebuilt_path}")
    return report


def _update_summary_rows(reports: dict[str, dict[str, Any]]) -> None:
    with SUMMARY_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    for row in rows:
        report = reports.get(str(row.get("run_id")))
        if report is None:
            continue
        detection = report["detection"]
        strict = report["extraction"]["strict_token_f1"]
        anchor = report["extraction"]["anchor_window"]
        updates = {
            "detection_accuracy": detection["accuracy"],
            "detection_precision": detection["precision"],
            "detection_recall": detection["recall"],
            "detection_f1": detection["f1"],
            "strict_all_precision": strict["all_samples"]["precision"],
            "strict_all_recall": strict["all_samples"]["recall"],
            "strict_all_f1": strict["all_samples"]["f1"],
            "anchor_all_precision": anchor["all_samples"]["precision"],
            "anchor_all_recall": anchor["all_samples"]["recall"],
            "anchor_all_f1": anchor["all_samples"]["f1"],
            "strict_detected_only_f1": strict["detected_only"]["f1"],
            "anchor_detected_only_f1": anchor["detected_only"]["f1"],
            "report_path": report["report_path"],
        }
        row.update({key: str(value) for key, value in updates.items()})

    temporary_path = SUMMARY_PATH.with_suffix(SUMMARY_PATH.suffix + ".offline-repair.tmp")
    with temporary_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    temporary_path.replace(SUMMARY_PATH)


def _backup(path: Path, backup_dir: Path) -> None:
    if path.exists():
        backup_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, backup_dir / path.name)


def run(*, apply: bool) -> dict[str, Any]:
    if not CHECKPOINT_DIR.is_dir() or not REPORT_DIR.is_dir():
        raise RuntimeError("Phase 2 checkpoint/report 目录不存在。")
    checkpoint_results: list[dict[str, Any]] = []
    scanned: list[tuple[Path, Path, dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]] = []
    for checkpoint_path in sorted(CHECKPOINT_DIR.glob("rag_only_k*.jsonl")):
        manifest_path = checkpoint_path.with_suffix(".manifest.json")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        rows, repairs = _scan_checkpoint(checkpoint_path)
        scanned.append((checkpoint_path, manifest_path, manifest, rows, repairs))
        checkpoint_results.append(
            {
                "checkpoint": str(checkpoint_path),
                "status": manifest.get("status"),
                "completed_samples": manifest.get("completed_samples"),
                "repair_count": len(repairs),
                "sample_ids": [item["sample_id"] for item in repairs],
                "repairs": repairs,
            }
        )

    total_repairs = sum(item["repair_count"] for item in checkpoint_results)
    result: dict[str, Any] = {
        "repair_type": MISSING_TRIPLE_CLOSING_BRACE_REPAIR,
        "mode": "apply" if apply else "dry_run",
        "total_repairs": total_repairs,
        "checkpoints": checkpoint_results,
    }
    if not apply or total_repairs == 0:
        return result

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")


    backup_dir = PROJECT_ROOT / "results" / "repair_backups" / timestamp
    _backup(SUMMARY_PATH, backup_dir)
    reports_to_rebuild: list[tuple[dict[str, Any], Path]] = []
    for checkpoint_path, manifest_path, manifest, rows, repairs in scanned:
        if not repairs:
            continue
        _backup(checkpoint_path, backup_dir)
        _backup(manifest_path, backup_dir)
        before_sha256 = _sha256(checkpoint_path)
        _atomic_write_text(checkpoint_path, _serialize_checkpoint(rows))
        checkpoint_record = next(
            item for item in checkpoint_results if item["checkpoint"] == str(checkpoint_path)
        )
        checkpoint_record["before_sha256"] = before_sha256
        checkpoint_record["after_sha256"] = _sha256(checkpoint_path)
        if manifest.get("status") == "complete":
            report_path = Path(manifest["report_path"])
            _backup(report_path, backup_dir)
            _backup(report_path.with_name(f"{report_path.stem}_generation_failures.jsonl"), backup_dir)
            _backup(report_path.with_name(f"{report_path.stem}_parse_repairs.jsonl"), backup_dir)
            reports_to_rebuild.append((manifest, checkpoint_path))

    samples = load_dataset("cnc_sft_validation")
    rebuilt_reports: dict[str, dict[str, Any]] = {}
    for manifest, checkpoint_path in reports_to_rebuild:
        report = _rebuild_report(manifest, checkpoint_path, samples)
        run_name = str(manifest["run_name"])
        rebuilt_reports[run_name] = report
        stale_failure_path = Path(report["report_path"]).with_name(
            f"{Path(report['report_path']).stem}_generation_failures.jsonl"
        )
        if report["generation_failures"]["total"] == 0 and stale_failure_path.exists():
            stale_failure_path.unlink()
    if rebuilt_reports:
        _update_summary_rows(rebuilt_reports)

    result["backup_dir"] = str(backup_dir)
    result["rebuilt_reports"] = {
        run_name: {
            "report_path": report["report_path"],
            "generation_failures": report["generation_failures"]["total"],
            "parse_repairs": report["parse_repairs"],
            "detection_f1": report["detection"]["f1"],
            "anchor_all_f1": report["extraction"]["anchor_window"]["all_samples"]["f1"],
        }
        for run_name, report in rebuilt_reports.items()
    }
    audit_path = REPORT_DIR / f"offline_missing_triple_repair_audit_{timestamp}.json"
    result["audit_path"] = str(audit_path)
    _atomic_write_text(
        audit_path,
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply atomic checkpoint changes and rebuild completed reports; otherwise dry-run.",
    )
    args = parser.parse_args()
    print(json.dumps(run(apply=args.apply), ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
