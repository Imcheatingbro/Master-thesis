"""Global diagnostics for redundancy and unsupported hierarchy."""

from __future__ import annotations

import csv
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from src.kg_evaluator import flatten_judge_units


PROMPT_DIR = Path(__file__).resolve().parents[1] / "prompts"
ALLOWED_GLOBAL_ISSUES = {"semantic_redundancy", "unsupported_hierarchy"}


def build_global_diagnostic_prompt(
    span: str,
    extraction: dict[str, Any] | None,
    indexed_units: list[dict[str, Any]],
    span_id: str,
    prompt_version: str = "v1",
) -> str:
    template = _load_prompt(prompt_version)
    payload = {
        "span_id": span_id,
        "span": span,
        "structure": extraction if isinstance(extraction, dict) else {"components": []},
        "indexed_units": [_strip_graph_metadata(unit) for unit in indexed_units],
    }
    return template.replace("{input_json}", json.dumps(payload, ensure_ascii=False, indent=2))


def parse_global_diagnostic_output(
    raw_output: str,
    indexed_units: list[dict[str, Any]],
    expected_span_id: str,
) -> dict[str, Any]:
    cleaned = re.sub(r"<think>.*?</think>", "", raw_output, flags=re.DOTALL | re.IGNORECASE).strip()
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", cleaned, flags=re.DOTALL | re.IGNORECASE)
    text = fenced.group(1) if fenced else _first_json_object(cleaned)
    if text is None:
        raise ValueError("Global diagnostic output contains no JSON object")
    parsed = json.loads(text)
    if not isinstance(parsed, dict) or not isinstance(parsed.get("issues"), list):
        raise ValueError("Global diagnostic output must contain an issues list")
    warnings: list[dict[str, str]] = []
    if str(parsed.get("span_id")) != str(expected_span_id):
        warnings.append(
            {
                "type": "span_id_normalized",
                "message": f"Returned {parsed.get('span_id')!r}; used expected input span_id",
            }
        )

    unit_by_id = {str(unit.get("id")): unit for unit in indexed_units if isinstance(unit, dict)}
    normalized: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for issue_index, issue in enumerate(parsed["issues"]):
        if not isinstance(issue, dict):
            warnings.append({"type": "invalid_issue_dropped", "message": f"Issue {issue_index} is not an object"})
            continue
        issue_type = str(issue.get("type", ""))
        anchor_id = str(issue.get("anchor_id", ""))
        if issue_type not in ALLOWED_GLOBAL_ISSUES:
            warnings.append(
                {"type": "invalid_issue_dropped", "message": f"Issue {issue_index} has unsupported type {issue_type!r}"}
            )
            continue
        if anchor_id not in unit_by_id:
            warnings.append(
                {"type": "invalid_issue_dropped", "message": f"Issue {issue_index} has unknown anchor {anchor_id!r}"}
            )
            continue
        anchor_kind = str(unit_by_id[anchor_id].get("kind", ""))
        if issue_type == "semantic_redundancy" and anchor_kind not in {"node", "attribute"}:
            warnings.append(
                {"type": "invalid_issue_dropped", "message": f"Issue {issue_index} redundancy anchor is {anchor_kind!r}"}
            )
            continue
        if issue_type == "unsupported_hierarchy" and anchor_kind != "child_link":
            warnings.append(
                {"type": "invalid_issue_dropped", "message": f"Issue {issue_index} hierarchy anchor is {anchor_kind!r}"}
            )
            continue

        related_raw = issue.get("related_ids", [])
        if not isinstance(related_raw, list):
            warnings.append(
                {"type": "invalid_issue_dropped", "message": f"Issue {issue_index} related_ids is not a list"}
            )
            continue
        related_ids = sorted({str(item) for item in related_raw if str(item) and str(item) != anchor_id})
        if any(item not in unit_by_id for item in related_ids):
            warnings.append(
                {"type": "invalid_issue_dropped", "message": f"Issue {issue_index} has an unknown related id"}
            )
            continue

        key = (str(expected_span_id), issue_type, anchor_id)
        if key in seen:
            continue
        seen.add(key)
        normalized.append(
            {
                "type": issue_type,
                "anchor_id": anchor_id,
                "related_ids": related_ids,
                "reason": str(issue.get("reason", "")).strip(),
            }
        )
    return {"span_id": str(expected_span_id), "issues": normalized, "warnings": warnings}


def reparse_saved_global_diagnostics(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for record in records:
        raw_output = str(record.get("raw_global_output", ""))
        if not raw_output.strip():
            continue
        try:
            record["global_result"] = parse_global_diagnostic_output(
                raw_output,
                indexed_units=record.get("indexed_units", []),
                expected_span_id=str(record.get("span_id", "")),
            )
            record["global_error"] = None
        except Exception as exc:
            record["global_result"] = None
            record["global_error"] = {"type": type(exc).__name__, "message": str(exc)}
    return records


def prepare_global_diagnostic_records(
    saved_span_results: list[dict[str, Any]],
    prompt_version: str = "v1",
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for source in saved_span_results:
        extraction = source.get("parsed_extraction")
        units = flatten_judge_units(
            extraction if isinstance(extraction, dict) else {"components": []},
            graph_event_id=str(source.get("graph_event_id") or ""),
        )
        span_id = str(source.get("span_id", ""))
        records.append(
            {
                "dataset": source.get("dataset"),
                "sample_id": source.get("sample_id"),
                "span_id": span_id,
                "event_prompt_version": source.get("prompt_version"),
                "span": str(source.get("span", "")),
                "parsed_extraction": extraction,
                "indexed_units": units,
                "global_prompt_version": prompt_version,
                "global_prompt": build_global_diagnostic_prompt(
                    span=str(source.get("span", "")),
                    extraction=extraction if isinstance(extraction, dict) else None,
                    indexed_units=units,
                    span_id=span_id,
                    prompt_version=prompt_version,
                ),
                "raw_global_output": "",
                "global_result": None,
                "global_error": None,
            }
        )
    return records


def run_parallel_global_diagnostics(
    records: list[dict[str, Any]],
    client: Any,
    max_workers: int = 5,
    progress_callback: Any | None = None,
) -> list[dict[str, Any]]:
    def run_one(index: int, record: dict[str, Any]) -> tuple[int, str, dict[str, Any] | None, dict[str, str] | None]:
        raw_output = ""
        result = None
        error = None
        try:
            raw_output = str(client.chat(str(record.get("global_prompt", ""))))
            result = parse_global_diagnostic_output(
                raw_output,
                indexed_units=record.get("indexed_units", []),
                expected_span_id=str(record.get("span_id", "")),
            )
        except Exception as exc:  # pragma: no cover - behavior is tested through fake clients
            error = {"type": type(exc).__name__, "message": str(exc)}
        return index, raw_output, result, error

    worker_count = max(1, int(max_workers or 1))
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = {executor.submit(run_one, index, record): index for index, record in enumerate(records)}
        for future in as_completed(futures):
            index, raw_output, result, error = future.result()
            records[index].update(
                {
                    "raw_global_output": raw_output,
                    "global_result": result,
                    "global_error": error,
                }
            )
            if progress_callback is not None:
                progress_callback(records[index])
    return records


def aggregate_global_diagnostics(records: list[dict[str, Any]]) -> dict[str, Any]:
    successful = [record for record in records if isinstance(record.get("global_result"), dict)]
    redundancy_issues = 0
    redundancy_spans = 0
    hierarchy_issues = 0
    hierarchy_spans = 0
    hierarchy_eligible = 0

    for record in successful:
        issues = record["global_result"].get("issues", [])
        redundancy = [issue for issue in issues if issue.get("type") == "semantic_redundancy"]
        hierarchy = [issue for issue in issues if issue.get("type") == "unsupported_hierarchy"]
        redundancy_issues += len(redundancy)
        hierarchy_issues += len(hierarchy)
        redundancy_spans += int(bool(redundancy))
        hierarchy_spans += int(bool(hierarchy))
        has_child_link = any(unit.get("kind") == "child_link" for unit in record.get("indexed_units", []))
        hierarchy_eligible += int(has_child_link)

    diagnosed_count = len(successful)
    return {
        "diagnostic_span_count": len(records),
        "diagnostic_coverage": _rate(diagnosed_count, len(records)),
        "semantic_redundancy_issue_count": redundancy_issues,
        "semantic_redundancy_affected_span_count": redundancy_spans,
        "semantic_redundancy_span_rate": _rate(redundancy_spans, diagnosed_count),
        "unsupported_hierarchy_issue_count": hierarchy_issues,
        "unsupported_hierarchy_eligible_span_count": hierarchy_eligible,
        "unsupported_hierarchy_affected_span_count": hierarchy_spans,
        "unsupported_hierarchy_span_rate": _rate(hierarchy_spans, hierarchy_eligible) if hierarchy_eligible else None,
    }


def save_global_diagnostic_outputs(
    records: list[dict[str, Any]],
    metrics: dict[str, Any],
    output_dir: Path | str,
    dataset: str,
    event_prompt_version: str,
    sample_count: int,
    prompt_version: str = "v1",
    run_id: str | None = None,
) -> dict[str, Path]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    timestamp = run_id or time.strftime("%Y%m%d_%H%M%S")
    prefix = f"{dataset}_{event_prompt_version}_global-{prompt_version}_n{sample_count}_{timestamp}"

    details_path = output_path / f"{prefix}_diagnostics.jsonl"
    with details_path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")

    metrics_path = output_path / f"{prefix}_metrics.csv"
    with metrics_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["metric", "value"])
        writer.writeheader()
        for key, value in metrics.items():
            writer.writerow({"metric": key, "value": value})
    return {"diagnostics": details_path, "metrics": metrics_path}


def _load_prompt(prompt_version: str) -> str:
    safe_version = Path(prompt_version).stem
    prompt_path = PROMPT_DIR / f"kg_eval_global_diagnostics_{safe_version}.txt"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Global diagnostic prompt does not exist: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")


def _strip_graph_metadata(unit: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in unit.items() if key != "graph_path"}


def _first_json_object(text: str) -> str | None:
    start = text.find("{")
    if start < 0:
        return None
    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return None


def _rate(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 6) if denominator else 0.0
