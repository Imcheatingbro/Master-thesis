"""Deterministic and semantic evaluation of generated graph structures."""

from __future__ import annotations

import csv
import json
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from src.event_extractor import _build_event_messages, classify_event_error, parse_event_output


PROMPT_DIR = Path(__file__).resolve().parents[1] / "prompts"
DEFAULT_JUDGE_PROMPT_VERSION = "v3"
DEFAULT_DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_DEEPSEEK_MODEL = "deepseek-v4-pro"
FORBIDDEN_ROLES = {"cause", "effect", "reason", "consequence", "causaltrigger", "resultof"}
SUM_WITHIN_SAMPLE_METRICS = {"correct_unit_yield"}
RETRYABLE_DEEPSEEK_STATUS_CODES = {429, 500, 502, 503, 504}
MAIN_METRIC_ORDER = (
    "deterministic_compliance_rate",
    "forbidden_role_affected_rate",
    "content_token_coverage",
    "node_count",
    "attribute_count",
    "child_link_count",
    "avg_max_depth",
    "p95_max_depth",
    "strict_unit_precision",
    "correct_unit_yield",
    "role_correctness",
    "attachment_correctness",
    "judge_coverage",
    "sample_count",
    "span_count",
)

# A deliberately small, fixed function-word list makes ``content_token_coverage``
# deterministic without introducing a POS tagger or another model dependency.
FUNCTION_WORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}


def load_gold_span_records(
    samples: list[dict[str, Any]],
    dataset: str,
    sample_n: int | None = None,
    max_spans: int | None = None,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    causal_sample_count = 0

    for sample in samples:
        relations = sample.get("relations", [])
        if not isinstance(relations, list) or not relations:
            continue
        if sample_n is not None and causal_sample_count >= sample_n:
            break

        causal_sample_count += 1
        sample_id = sample.get("id")
        text = str(sample.get("text", ""))
        for triple_index, relation in enumerate(relations):
            if not isinstance(relation, dict):
                continue
            for event_role in ("cause", "effect"):
                span = str(relation.get(event_role, "")).strip()
                if not span:
                    continue
                records.append(
                    {
                        "dataset": dataset,
                        "sample_id": sample_id,
                        "sample_text": text,
                        "triple_index": triple_index,
                        "event_role": event_role,
                        "span_id": f"{dataset}_{sample_id}_t{triple_index}_{event_role}",
                        "graph_event_id": f"triple_{triple_index}_{event_role}",
                        "span": span,
                    }
                )
                if max_spans is not None and len(records) >= max_spans:
                    return records
    return records


def run_eval_extraction(
    span_record: dict[str, Any],
    client: Any,
    prompt_version: str,
    max_retry: int = 1,
) -> dict[str, Any]:
    raw_output = ""
    parsed: dict[str, Any] | None = None
    last_error: Exception | None = None

    for _attempt in range(1, max_retry + 1):
        try:
            raw_output = str(
                client.chat(
                    _build_event_messages(
                        str(span_record["span"]),
                        str(span_record["event_role"]),
                        prompt_version,
                    )
                )
            )
            parsed = parse_event_output(raw_output)
            last_error = None
            break
        except Exception as exc:  # pragma: no cover - returned state is tested indirectly
            last_error = exc

    result = {
        "dataset": span_record.get("dataset"),
        "sample_id": span_record.get("sample_id"),
        "sample_text": span_record.get("sample_text", ""),
        "span_id": span_record.get("span_id"),
        "graph_event_id": span_record.get("graph_event_id"),
        "triple_index": span_record.get("triple_index"),
        "event_role": span_record.get("event_role"),
        "span": span_record.get("span", ""),
        "prompt_version": prompt_version,
        "raw_extraction_output": raw_output,
        "parsed_extraction": parsed,
        "extraction_error_type": None,
        "extraction_error_message": "",
    }
    if last_error is not None:
        result["extraction_error_type"] = classify_event_error(last_error)
        result["extraction_error_message"] = str(last_error)
    return result


def validate_extraction(
    extraction: dict[str, Any] | None,
    span: str,
    schema: str,
    max_depth: int | None,
) -> dict[str, Any]:
    validation: dict[str, Any] = {
        "json_parse_success": isinstance(extraction, dict),
        "schema_valid": isinstance(extraction, dict),
        "substring_valid": True,
        "depth_compliant": True,
        "forbidden_role_count": 0,
        "max_depth": 0,
        "node_count": 0,
        "attribute_count": 0,
        "child_link_count": 0,
        "invalid_values": [],
        "schema_errors": [],
    }
    if not isinstance(extraction, dict):
        validation["schema_valid"] = False
        validation["substring_valid"] = False
        validation["depth_compliant"] = False
        validation["schema_errors"].append("extraction_not_object")
        return validation

    components = extraction.get("components")
    if not isinstance(components, list):
        validation["schema_valid"] = False
        validation["schema_errors"].append("components_not_list")
        return validation

    for index, component in enumerate(components):
        _validate_node(component, span, schema, 1, f"c{index}", validation)

    if max_depth is not None and validation["max_depth"] > max_depth:
        validation["depth_compliant"] = False
    if validation["invalid_values"]:
        validation["substring_valid"] = False
    if validation["schema_errors"]:
        validation["schema_valid"] = False
    return validation


def flatten_judge_units(extraction: dict[str, Any], graph_event_id: str | None = None) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []
    counters = {"node": 0, "attribute": 0, "link": 0}
    components = extraction.get("components", []) if isinstance(extraction, dict) else []
    for index, component in enumerate(_as_list(components)):
        if not isinstance(component, dict):
            continue
        graph_path = f"{graph_event_id}/component_{index}" if graph_event_id else f"component_{index}"
        _flatten_node(component, f"c{index}", graph_path, units, counters)
    return units


def build_judge_prompt(
    span: str,
    units: list[dict[str, Any]],
    judge_span_id: str = "s0",
    prompt_version: str = DEFAULT_JUDGE_PROMPT_VERSION,
) -> str:
    template = _load_judge_prompt(prompt_version)
    judge_units = [_strip_local_metadata(unit) for unit in units]
    input_json = json.dumps({"span_id": judge_span_id, "span": span, "units": judge_units}, ensure_ascii=False, indent=2)
    return template.replace("{input_json}", input_json)


def parse_judge_output(raw_str: str) -> dict[str, Any]:
    cleaned = re.sub(r"<think>.*?</think>", "", raw_str, flags=re.DOTALL | re.IGNORECASE).strip()
    json_text = _extract_json_from_markdown(cleaned) or _extract_first_json_object(cleaned)
    if json_text is None:
        raise ValueError("Judge JSON object not found")
    parsed = json.loads(json_text)
    if not isinstance(parsed, dict):
        raise ValueError("Judge output must be a JSON object")
    if not isinstance(parsed.get("units"), list):
        raise ValueError("Judge output is missing the units list")
    return parsed


def compute_span_metrics(
    validation: dict[str, Any],
    judge_units: list[dict[str, Any]],
    judge_result: dict[str, Any] | None,
    descriptors: dict[str, Any] | None = None,
) -> dict[str, Any]:
    metrics: dict[str, Any] = {
        "json_parse_success": int(bool(validation.get("json_parse_success"))),
        "schema_valid": int(bool(validation.get("schema_valid"))),
        "substring_valid": int(bool(validation.get("substring_valid"))),
        "depth_compliant": int(bool(validation.get("depth_compliant"))),
        "forbidden_role_count": int(validation.get("forbidden_role_count", 0)),
        "max_depth": int(validation.get("max_depth", 0)),
        "node_count": int(validation.get("node_count", 0)),
        "attribute_count": int(validation.get("attribute_count", 0)),
        "child_link_count": int(validation.get("child_link_count", 0)),
        "judge_unit_count": len(judge_units),
        "judge_coverage": int(is_complete_judge_result(judge_units, judge_result)),
        "correct_unit_yield": None,
    }
    metrics.update(descriptors or {})
    if not is_complete_judge_result(judge_units, judge_result):
        metrics.update(
            {
                "strict_unit_precision": None,
                "role_correctness": None,
                "attachment_correctness": None,
            }
        )
        return metrics

    correct_unit_yield = 0
    score_by_id = {str(item.get("id")): item for item in judge_result.get("units", []) if isinstance(item, dict)}
    strict_scores: list[float] = []
    role_scores: list[float] = []
    attachment_scores: list[float] = []

    for unit in judge_units:
        score = score_by_id.get(str(unit.get("id")), {})
        applicable = [_numeric_score(score.get(field)) for field in ("s", "r", "m", "a") if score.get(field) is not None]
        if applicable:
            is_strict = all(value == 1.0 for value in applicable)
            strict_scores.append(1.0 if is_strict else 0.0)
            if is_strict:
                correct_unit_yield += 1
        if score.get("r") is not None:
            role_scores.append(_numeric_score(score.get("r")))
        if unit.get("kind") in {"attribute", "child_link"} and score.get("a") is not None:
            attachment_scores.append(_numeric_score(score.get("a")))

    metrics["correct_unit_yield"] = correct_unit_yield
    metrics["strict_unit_precision"] = _mean_or_none(strict_scores)
    metrics["role_correctness"] = _mean_or_none(role_scores)
    metrics["attachment_correctness"] = _mean_or_none(attachment_scores)
    return metrics


def is_complete_judge_result(
    judge_units: list[dict[str, Any]],
    judge_result: dict[str, Any] | None,
) -> bool:
    if not isinstance(judge_result, dict) or not isinstance(judge_result.get("units"), list):
        return False
    returned_items = [item for item in judge_result["units"] if isinstance(item, dict)]
    expected_ids = [str(unit.get("id")) for unit in judge_units]
    returned_ids = [str(item.get("id")) for item in returned_items]
    if len(returned_ids) != len(set(returned_ids)) or set(returned_ids) != set(expected_ids):
        return False

    score_by_id = {str(item.get("id")): item for item in returned_items}
    applicable_by_kind = {
        "node": ("s", "r", "m"),
        "attribute": ("s", "r", "a"),
        "child_link": ("a",),
    }
    for unit in judge_units:
        score = score_by_id[str(unit.get("id"))]
        applicable = applicable_by_kind.get(str(unit.get("kind")), ())
        if not applicable or any(not _valid_judge_score(score.get(field)) for field in applicable):
            return False
    return True


def compute_deterministic_descriptors(
    span: str,
    judge_units: list[dict[str, Any]],
    validation: dict[str, Any],
) -> dict[str, Any]:
    value_units = [
        unit
        for unit in judge_units
        if unit.get("kind") in {"node", "attribute"} and str(unit.get("value", "")).strip()
    ]
    normalized_values = [_normalize_text(str(unit.get("value", ""))) for unit in value_units]

    signatures = [
        (str(unit.get("role", "")).strip().casefold(), normalized_values[index])
        for index, unit in enumerate(value_units)
    ]
    duplicate_count = len(signatures) - len(set(signatures))

    contained_indices: set[int] = set()
    for small_index, small in enumerate(normalized_values):
        if not small:
            continue
        for large_index, large in enumerate(normalized_values):
            if small_index == large_index or small == large:
                continue
            if _is_token_bounded_substring(small, large):
                contained_indices.add(small_index)
                break

    node_count = int(validation.get("node_count", 0))
    max_depth = int(validation.get("max_depth", 0))
    return {
        "deterministic_compliance_rate": int(
            bool(validation.get("json_parse_success"))
            and bool(validation.get("schema_valid"))
            and bool(validation.get("substring_valid"))
        ),
        "forbidden_role_affected_rate": int(int(validation.get("forbidden_role_count", 0)) > 0),
        "content_token_coverage": _content_token_coverage(span, value_units),
        "exact_duplicate_rate": (duplicate_count / len(value_units)) if value_units else 0.0,
        "containment_rate": (len(contained_indices) / len(value_units)) if value_units else 0.0,
        "normalized_chain_depth": (max_depth / node_count) if node_count else 0.0,
    }


def run_parallel_judge(
    span_results: list[dict[str, Any]],
    judge_client: Any,
    max_workers: int = 5,
    progress_callback: Any | None = None,
) -> list[dict[str, Any]]:
    if not span_results:
        return span_results

    worker_count = max(1, int(max_workers or 1))

    def judge_one(index: int, span_result: dict[str, Any]) -> tuple[int, str, dict[str, Any] | None, dict[str, str] | None, dict[str, Any]]:
        raw_judge_output = ""
        judge_result = None
        judge_error = None
        validation = span_result.get("validation") if isinstance(span_result.get("validation"), dict) else {}
        judge_units = span_result.get("judge_units") if isinstance(span_result.get("judge_units"), list) else []
        descriptors = (
            span_result.get("deterministic_descriptors")
            if isinstance(span_result.get("deterministic_descriptors"), dict)
            else {}
        )
        try:
            raw_judge_output = judge_client.chat(str(span_result.get("judge_prompt", "")))
            judge_result = parse_judge_output(raw_judge_output)
            if not is_complete_judge_result(judge_units, judge_result):
                judge_error = {
                    "type": "IncompleteJudgeOutput",
                    "message": "Judge output omitted a unit or an applicable s/r/m/a score",
                }
        except Exception as exc:  # pragma: no cover - concrete branches are covered by behavior tests
            judge_error = {"type": type(exc).__name__, "message": str(exc)}
        span_metrics = compute_span_metrics(validation, judge_units, judge_result, descriptors)
        return index, raw_judge_output, judge_result, judge_error, span_metrics

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = {executor.submit(judge_one, index, span_result): index for index, span_result in enumerate(span_results)}
        for future in as_completed(futures):
            index, raw_judge_output, judge_result, judge_error, span_metrics = future.result()
            span_results[index].update(
                {
                    "raw_judge_output": raw_judge_output,
                    "judge_result": judge_result,
                    "judge_error": judge_error,
                    "span_metrics": span_metrics,
                }
            )
            if progress_callback is not None:
                progress_callback(span_results[index])
    return span_results


def aggregate_sample_results(span_results: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    grouped: dict[tuple[str, Any, str], list[dict[str, Any]]] = defaultdict(list)
    for result in span_results:
        grouped[(str(result.get("dataset")), result.get("sample_id"), str(result.get("prompt_version")))].append(result)

    sample_results: list[dict[str, Any]] = []
    for (dataset, sample_id, prompt_version), items in sorted(grouped.items(), key=lambda item: (item[0][0], str(item[0][1]), item[0][2])):
        sample_metrics = _aggregate_metrics([item.get("span_metrics", {}) for item in items], within_sample=True)
        triple_indices = {item.get("triple_index") for item in items if item.get("triple_index") is not None}
        sample_results.append(
            {
                "dataset": dataset,
                "sample_id": sample_id,
                "prompt_version": prompt_version,
                "gold_relation_count": len(triple_indices),
                "evaluated_span_count": len(items),
                "sample_metrics": sample_metrics,
                "span_results": items,
            }
        )

    method_metrics = _aggregate_metrics([sample["sample_metrics"] for sample in sample_results], within_sample=False)
    span_depths = [
        float(result.get("span_metrics", {}).get("max_depth"))
        for result in span_results
        if isinstance(result.get("span_metrics", {}).get("max_depth"), int | float)
    ]
    if span_depths:
        method_metrics["p95_max_depth"] = _clean_number(_nearest_rank_percentile(span_depths, 0.95))
    method_metrics.update({"sample_count": len(sample_results), "span_count": sum(sample["evaluated_span_count"] for sample in sample_results)})
    return sample_results, method_metrics


def select_main_metrics(method_metrics: dict[str, Any]) -> dict[str, Any]:
    return {key: method_metrics[key] for key in MAIN_METRIC_ORDER if key in method_metrics}


def save_eval_checkpoint(
    span_results: list[dict[str, Any]],
    output_dir: Path | str,
    dataset: str,
    prompt_version: str,
    processed_samples: int,
) -> Path:
    checkpoint_dir = Path(output_dir) / "checkpoints"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    path = checkpoint_dir / f"{dataset}_{prompt_version}_checkpoint_{processed_samples:04d}.json"
    path.write_text(json.dumps(span_results, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def save_eval_outputs(
    span_results: list[dict[str, Any]],
    sample_results: list[dict[str, Any]],
    method_metrics: dict[str, Any],
    output_dir: Path | str,
    dataset: str,
    prompt_version: str,
    sample_n: int | None,
    run_id: str | None = None,
    output_tag: str | None = None,
) -> dict[str, Path]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    timestamp = run_id or time.strftime("%Y%m%d_%H%M%S")
    n_label = "all" if sample_n is None else f"n{sample_n}"
    tag = f"_{output_tag}" if output_tag else ""
    prefix = f"{dataset}_{prompt_version}{tag}_{n_label}_{timestamp}"

    spans_path = output_path / f"{prefix}_spans.jsonl"
    with spans_path.open("w", encoding="utf-8") as file:
        for result in span_results:
            file.write(json.dumps(result, ensure_ascii=False) + "\n")

    samples_path = output_path / f"{prefix}_samples.json"
    samples_path.write_text(json.dumps(sample_results, ensure_ascii=False, indent=2), encoding="utf-8")

    metrics_path = output_path / f"{prefix}_metrics.csv"
    with metrics_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["metric", "value"])
        writer.writeheader()
        for key, value in method_metrics.items():
            writer.writerow({"metric": key, "value": value})

    main_metrics_path = output_path / f"{prefix}_main_metrics.csv"
    with main_metrics_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["metric", "value"])
        writer.writeheader()
        for key, value in select_main_metrics(method_metrics).items():
            writer.writerow({"metric": key, "value": value})

    return {
        "spans": spans_path,
        "samples": samples_path,
        "metrics": metrics_path,
        "main_metrics": main_metrics_path,
    }


class DeepSeekJudgeClient:

    def __init__(
        self,
        api_key_path: Path | str,
        model: str = DEFAULT_DEEPSEEK_MODEL,
        base_url: str = DEFAULT_DEEPSEEK_BASE_URL,
        max_tokens: int = 1024,
        thinking: str = "disabled",
        reasoning_effort: str | None = None,
        timeout: float = 60.0,
        retry_times: int = 3,
        retry_base_seconds: float = 2.0,
        sleep_func: Any | None = None,
        urlopen_func: Any | None = None,
    ) -> None:
        if thinking not in {"enabled", "disabled"}:
            raise ValueError("thinking must be either 'enabled' or 'disabled'")
        if reasoning_effort not in {None, "high", "max"}:
            raise ValueError("reasoning_effort must be None, 'high', or 'max'")
        if thinking == "disabled" and reasoning_effort is not None:
            raise ValueError("reasoning_effort must be None when thinking='disabled'")

        self.api_key = _read_api_key(Path(api_key_path))
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.max_tokens = max_tokens
        self.thinking = thinking
        self.reasoning_effort = reasoning_effort
        self.timeout = timeout
        self.retry_times = max(1, int(retry_times))
        self.retry_base_seconds = float(retry_base_seconds)
        self._sleep = sleep_func or time.sleep
        self._urlopen = urlopen_func or urlopen

    def chat(self, prompt: str) -> str:
        body = {
            "model": self.model,
            "thinking": {"type": self.thinking},
            "messages": [
                {"role": "system", "content": "Return strict JSON only."},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": self.max_tokens,
        }
        if self.thinking == "enabled":
            if self.reasoning_effort is not None:
                body["reasoning_effort"] = self.reasoning_effort
        else:
            body["temperature"] = 0

        payload: dict[str, Any] | None = None
        for attempt in range(1, self.retry_times + 1):
            request = Request(
                f"{self.base_url}/chat/completions",
                data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
                headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
                method="POST",
            )
            try:
                with self._urlopen(request, timeout=self.timeout) as response:
                    payload = json.loads(response.read().decode("utf-8"))
                break
            except HTTPError as exc:
                if not self._should_retry_http_error(exc, attempt):
                    raise
                self._sleep(self.retry_base_seconds * (2 ** (attempt - 1)))
            except (URLError, TimeoutError):
                if attempt >= self.retry_times:
                    raise
                self._sleep(self.retry_base_seconds * (2 ** (attempt - 1)))

        if payload is None:
            raise RuntimeError("DeepSeek judge request failed without response payload")
        content = payload["choices"][0]["message"].get("content") or ""
        if not content:
            raise ValueError("DeepSeek Judge returned empty content")
        return str(content)
    def _should_retry_http_error(self, exc: HTTPError, attempt: int) -> bool:
        return exc.code in RETRYABLE_DEEPSEEK_STATUS_CODES and attempt < self.retry_times


def _validate_node(node: Any, span: str, schema: str, depth: int, path: str, validation: dict[str, Any]) -> None:
    if not isinstance(node, dict):
        validation["schema_errors"].append(f"{path}:node_not_object")
        return

    role = node.get("role")
    value = node.get("value")
    if not isinstance(role, str) or not role.strip():
        validation["schema_errors"].append(f"{path}:missing_role")
    if not isinstance(value, str) or not value.strip():
        validation["schema_errors"].append(f"{path}:missing_value")
    else:
        validation["node_count"] += 1
        validation["max_depth"] = max(int(validation["max_depth"]), depth)
        if value not in span:
            validation["invalid_values"].append({"path": path, "role": str(role or ""), "value": value})

    if isinstance(role, str) and role.strip().casefold() in FORBIDDEN_ROLES:
        validation["forbidden_role_count"] += 1

    attributes = node.get("attributes", [])
    if not isinstance(attributes, list):
        validation["schema_errors"].append(f"{path}:attributes_not_list")
        attributes = []
    for index, attribute in enumerate(attributes):
        _validate_attribute(attribute, span, f"{path}.attr{index}", validation)

    children = node.get("children", [])
    if children is None:
        children = []
    if not isinstance(children, list):
        validation["schema_errors"].append(f"{path}:children_not_list")
        return
    if schema == "two_layer" and children:
        validation["schema_errors"].append(f"{path}:two_layer_has_children")
        validation["depth_compliant"] = False
    for index, child in enumerate(children):
        validation["child_link_count"] += 1
        _validate_node(child, span, schema, depth + 1, f"{path}.ch{index}", validation)


def _validate_attribute(attribute: Any, span: str, path: str, validation: dict[str, Any]) -> None:
    if not isinstance(attribute, dict):
        validation["schema_errors"].append(f"{path}:attribute_not_object")
        return
    role = attribute.get("role")
    value = attribute.get("value")
    if not isinstance(role, str) or not role.strip():
        validation["schema_errors"].append(f"{path}:missing_role")
    if not isinstance(value, str) or not value.strip():
        validation["schema_errors"].append(f"{path}:missing_value")
        return
    validation["attribute_count"] += 1
    if role.strip().casefold() in FORBIDDEN_ROLES:
        validation["forbidden_role_count"] += 1
    if value not in span:
        validation["invalid_values"].append({"path": path, "role": str(role or ""), "value": value})


def _flatten_node(
    node: dict[str, Any],
    path: str,
    graph_path: str,
    units: list[dict[str, Any]],
    counters: dict[str, int],
) -> dict[str, str]:
    node_id = f"n{counters['node']}"
    counters["node"] += 1
    node_ref = {"id": node_id, "role": str(node.get("role", "")), "value": str(node.get("value", ""))}
    units.append(
        {
            "id": node_id,
            "kind": "node",
            "path": path,
            "graph_path": graph_path,
            "role": node_ref["role"],
            "value": node_ref["value"],
        }
    )

    for index, attribute in enumerate(_as_list(node.get("attributes"))):
        if not isinstance(attribute, dict):
            continue
        attribute_id = f"a{counters['attribute']}"
        counters["attribute"] += 1
        units.append(
            {
                "id": attribute_id,
                "kind": "attribute",
                "path": f"{path}.attr{index}",
                "graph_path": f"{graph_path}/attribute_{index}",
                "parent": node_ref,
                "role": str(attribute.get("role", "")),
                "value": str(attribute.get("value", "")),
            }
        )

    for index, child in enumerate(_as_list(node.get("children"))):
        if not isinstance(child, dict):
            continue
        child_path = f"{path}.ch{index}"
        child_graph_path = f"{graph_path}/child_{index}"
        child_ref = _flatten_node(child, child_path, child_graph_path, units, counters)
        link_id = f"l{counters['link']}"
        counters["link"] += 1
        units.append(
            {
                "id": link_id,
                "kind": "child_link",
                "path": f"{path}->{child_path}",
                "graph_path": f"{graph_path}->{child_graph_path}",
                "parent": node_ref,
                "child": child_ref,
            }
        )
    return node_ref


def _strip_local_metadata(unit: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in unit.items() if key != "graph_path"}


def _load_judge_prompt(prompt_version: str) -> str:
    safe_version = Path(prompt_version).stem
    prompt_name = f"{safe_version}.txt" if safe_version.startswith("kg_eval_judge_") else f"kg_eval_judge_{safe_version}.txt"
    prompt_path = PROMPT_DIR / prompt_name
    if not prompt_path.exists():
        raise FileNotFoundError(f"Judge prompt template not found: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")


def _extract_json_from_markdown(text: str) -> str | None:
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL | re.IGNORECASE)
    return match.group(1) if match else None


def _extract_first_json_object(text: str) -> str | None:
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


def _aggregate_metrics(metrics_list: list[dict[str, Any]], within_sample: bool) -> dict[str, Any]:
    values_by_key: dict[str, list[float]] = defaultdict(list)
    for metrics in metrics_list:
        for key, value in metrics.items():
            if isinstance(value, bool):
                values_by_key[key].append(float(int(value)))
            elif isinstance(value, int | float):
                values_by_key[key].append(float(value))

    aggregated: dict[str, Any] = {}
    depth_values = values_by_key.pop("max_depth", [])
    observed_depth_values = values_by_key.pop("max_observed_depth", [])
    if depth_values:
        aggregated["avg_max_depth"] = _clean_number(_mean(depth_values))
    if depth_values or observed_depth_values:
        aggregated["max_observed_depth"] = _clean_number(max([*depth_values, *observed_depth_values]))

    for key, values in values_by_key.items():
        if within_sample and key in SUM_WITHIN_SAMPLE_METRICS:
            value = sum(values)
        else:
            value = _mean(values)
        aggregated[key] = _clean_number(value)
    return aggregated


def _numeric_score(value: Any) -> float:
    if value in {1, 1.0, "1"}:
        return 1.0
    if value in {0.5, "0.5"}:
        return 0.5
    return 0.0


def _valid_judge_score(value: Any) -> bool:
    return value in {0, 0.0, 0.5, 1, 1.0, "0", "0.5", "1"}


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _mean_or_none(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def _nearest_rank_percentile(values: list[float], percentile: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    rank = max(1, int((len(ordered) * percentile) + 0.999999999))
    return ordered[min(rank - 1, len(ordered) - 1)]


def _normalize_text(value: str) -> str:
    return " ".join(value.casefold().split())


def _is_token_bounded_substring(small: str, large: str) -> bool:
    return re.search(rf"(?<!\w){re.escape(small)}(?!\w)", large, flags=re.UNICODE) is not None


def _content_token_coverage(span: str, value_units: list[dict[str, Any]]) -> float | None:
    token_matches = [
        match
        for match in re.finditer(r"[^\W_]+(?:[-'][^\W_]+)*|\d+(?:[.,]\d+)*", span, flags=re.UNICODE)
        if match.group(0).casefold() not in FUNCTION_WORDS
    ]
    if not token_matches:
        return None

    covered_chars: set[int] = set()
    folded_span = span.casefold()
    for unit in value_units:
        value = str(unit.get("value", "")).strip()
        if not value:
            continue
        folded_value = value.casefold()
        start = 0
        while True:
            found = folded_span.find(folded_value, start)
            if found < 0:
                break
            covered_chars.update(range(found, found + len(value)))
            start = found + max(1, len(value))

    covered_tokens = sum(
        1
        for match in token_matches
        if all(index in covered_chars for index in range(match.start(), match.end()))
    )
    return covered_tokens / len(token_matches)


def _clean_number(value: float) -> int | float:
    if float(value).is_integer():
        return int(value)
    return round(value, 6)


def _read_api_key(api_key_path: Path) -> str:
    raw = api_key_path.read_text(encoding="utf-8").strip()
    if not raw:
        raise ValueError(f"DeepSeek API key file is empty: {api_key_path}")
    match = re.search(r"DEEPSEEK_API_KEY\s*=\s*(.+)", raw)
    key = match.group(1).strip() if match else raw
    key = key.strip('"').strip("'")
    if not key:
        raise ValueError(f"DeepSeek API key file is empty: {api_key_path}")
    return key


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []
