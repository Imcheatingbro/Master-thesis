"""Calibration utilities for semantic graph judges."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.kg_evaluator import build_judge_prompt, run_parallel_judge


APPLICABLE_FIELDS = {
    "node": ("s", "r", "m"),
    "attribute": ("s", "r", "a"),
    "child_link": ("a",),
}


def load_calibration_cases(path: Path | str, expected_count: int | None = 10) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            case = json.loads(line)
            if not isinstance(case, dict):
                raise ValueError(f"Calibration line {line_number} must be an object")
            _validate_case(case, line_number)
            cases.append(case)
    if expected_count is not None and len(cases) != expected_count:
        raise ValueError(f"Expected {expected_count} calibration cases, found {len(cases)}")
    case_ids = [str(case["case_id"]) for case in cases]
    if len(case_ids) != len(set(case_ids)):
        raise ValueError("Calibration case_id values must be unique")
    return cases


def run_calibration_version(
    cases: list[dict[str, Any]],
    prompt_version: str,
    judge_client: Any,
    max_workers: int = 5,
) -> dict[str, Any]:
    span_results = []
    for case in cases:
        units = case["units"]
        span_results.append(
            {
                "case_id": case["case_id"],
                "pair_id": case["pair_id"],
                "variant": case["variant"],
                "span_id": case["case_id"],
                "span": case["span"],
                "expected": case["expected"],
                "judge_prompt_version": prompt_version,
                "judge_units": units,
                "judge_prompt": build_judge_prompt(
                    span=str(case["span"]),
                    units=units,
                    judge_span_id=str(case["case_id"]),
                    prompt_version=prompt_version,
                ),
                "validation": {
                    "json_parse_success": True,
                    "schema_valid": True,
                    "substring_valid": True,
                    "depth_compliant": True,
                    "forbidden_role_count": 0,
                    "max_depth": 0,
                    "node_count": sum(unit.get("kind") == "node" for unit in units),
                    "attribute_count": sum(unit.get("kind") == "attribute" for unit in units),
                    "child_link_count": sum(unit.get("kind") == "child_link" for unit in units),
                },
            }
        )

    judged = run_parallel_judge(span_results, judge_client, max_workers=max_workers)
    return {
        "prompt_version": prompt_version,
        "summary": score_calibration_results(judged),
        "cases": judged,
    }


def score_calibration_results(judged_cases: list[dict[str, Any]]) -> dict[str, Any]:
    successful_cases = 0
    error_targets = 0
    detected_targets = 0
    protected_units = 0
    retained_units = 0
    clean_cases = 0
    clean_cases_passed = 0
    error_cases = 0
    error_cases_detected = 0

    for case in judged_cases:
        expected = case.get("expected", {})
        targets = expected.get("error_targets", []) if isinstance(expected, dict) else []
        protected_ids = expected.get("protected_unit_ids", []) if isinstance(expected, dict) else []
        units = case.get("judge_units", [])
        result = case.get("judge_result")
        result_units = result.get("units", []) if isinstance(result, dict) else []
        scores_by_id = {str(item.get("id")): item for item in result_units if isinstance(item, dict)}
        input_ids = {str(item.get("id")) for item in units if isinstance(item, dict)}
        complete = bool(result is not None and input_ids == set(scores_by_id))
        case["calibration_complete"] = complete
        if complete:
            successful_cases += 1

        target_flags: list[bool] = []
        for target in targets:
            error_targets += 1
            score = scores_by_id.get(str(target.get("unit_id")), {})
            detected = complete and any(_is_below_one(score.get(field)) for field in target.get("fields", []))
            target_flags.append(detected)
            if detected:
                detected_targets += 1

        protected_flags: list[bool] = []
        units_by_id = {str(item.get("id")): item for item in units if isinstance(item, dict)}
        for unit_id in protected_ids:
            protected_units += 1
            unit = units_by_id.get(str(unit_id), {})
            score = scores_by_id.get(str(unit_id), {})
            applicable = APPLICABLE_FIELDS.get(str(unit.get("kind")), ())
            retained = complete and bool(applicable) and all(_is_one(score.get(field)) for field in applicable)
            protected_flags.append(retained)
            if retained:
                retained_units += 1

        case["detected_expected_targets"] = target_flags
        case["retained_protected_units"] = protected_flags
        if case.get("variant") == "clean":
            clean_cases += 1
            if complete and protected_flags and all(protected_flags):
                clean_cases_passed += 1
        elif case.get("variant") == "error":
            error_cases += 1
            if complete and target_flags and all(target_flags):
                error_cases_detected += 1

    retention_rate = (retained_units / protected_units) if protected_units else 0.0
    return {
        "case_count": len(judged_cases),
        "judge_success_rate": _rate(successful_cases, len(judged_cases)),
        "error_target_count": error_targets,
        "detected_error_target_count": detected_targets,
        "error_detection_rate": _rate(detected_targets, error_targets),
        "protected_unit_count": protected_units,
        "retained_protected_unit_count": retained_units,
        "clean_retention_rate": retention_rate,
        "false_positive_rate": 1.0 - retention_rate if protected_units else 0.0,
        "clean_case_pass_rate": _rate(clean_cases_passed, clean_cases),
        "error_case_detection_rate": _rate(error_cases_detected, error_cases),
    }


def calibration_gate(summary: dict[str, Any]) -> dict[str, Any]:
    checks = {
        "all_calls_succeeded": float(summary.get("judge_success_rate", 0)) == 1.0,
        "error_detection_at_least_80pct": float(summary.get("error_detection_rate", 0)) >= 0.8,
        "clean_retention_at_least_80pct": float(summary.get("clean_retention_rate", 0)) >= 0.8,
        "false_positive_at_most_20pct": float(summary.get("false_positive_rate", 1)) <= 0.2,
    }
    return {"passed": all(checks.values()), "checks": checks}


def _validate_case(case: dict[str, Any], line_number: int) -> None:
    required = {"case_id", "pair_id", "variant", "span", "units", "expected"}
    missing = required - set(case)
    if missing:
        raise ValueError(f"Calibration line {line_number} missing: {sorted(missing)}")
    if case["variant"] not in {"clean", "error"}:
        raise ValueError(f"Calibration line {line_number} has invalid variant")
    if not isinstance(case["units"], list) or not case["units"]:
        raise ValueError(f"Calibration line {line_number} must contain units")
    unit_ids = [str(unit.get("id")) for unit in case["units"] if isinstance(unit, dict)]
    if len(unit_ids) != len(case["units"]) or len(unit_ids) != len(set(unit_ids)):
        raise ValueError(f"Calibration line {line_number} has invalid or duplicate unit ids")
    expected = case["expected"]
    if not isinstance(expected, dict):
        raise ValueError(f"Calibration line {line_number} expected must be an object")
    referenced = set(expected.get("protected_unit_ids", []))
    referenced.update(target.get("unit_id") for target in expected.get("error_targets", []))
    if not referenced.issubset(set(unit_ids)):
        raise ValueError(f"Calibration line {line_number} references unknown unit ids")
    if case["variant"] == "clean" and expected.get("error_targets"):
        raise ValueError(f"Calibration line {line_number} clean case cannot have error targets")
    if case["variant"] == "error" and not expected.get("error_targets"):
        raise ValueError(f"Calibration line {line_number} error case needs an error target")


def _is_one(value: Any) -> bool:
    return value in {1, 1.0, "1"}


def _is_below_one(value: Any) -> bool:
    return value in {0, 0.0, 0.5, "0", "0.5"}


def _rate(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 6) if denominator else 0.0
