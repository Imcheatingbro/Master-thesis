"""KG construction evaluation 的单元测试。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.kg_evaluator import (
    DeepSeekJudgeClient,
    aggregate_sample_results,
    build_judge_prompt,
    compute_span_metrics,
    flatten_judge_units,
    load_gold_span_records,
    parse_judge_output,
    run_parallel_judge,
    run_eval_extraction,
    save_eval_outputs,
    validate_extraction,
)


class FakeClient:
    """记录 messages 并返回预设 construction 输出。"""

    def __init__(self, outputs: list[str]) -> None:
        self.outputs = outputs
        self.messages: list[list[dict[str, str]]] = []

    def chat(self, messages: list[dict[str, str]]) -> str:
        self.messages.append(messages)
        return self.outputs.pop(0)


class FakeResponse:
    """模拟 urllib response context manager。"""

    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *_args: object) -> None:
        return None

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


def test_load_gold_span_records_limits_by_causal_sample_and_keeps_sample_id() -> None:
    samples = [
        {"id": 1, "text": "Rain caused flooding.", "has_causal": True, "relations": [{"cause": "Rain", "effect": "flooding"}]},
        {"id": 2, "text": "No relation.", "has_causal": False, "relations": []},
        {
            "id": 3,
            "text": "Wind and rain caused delays.",
            "has_causal": True,
            "relations": [
                {"cause": "Wind", "effect": "delays"},
                {"cause": "rain", "effect": "delays"},
            ],
        },
    ]

    records = load_gold_span_records(samples, dataset="cnc", sample_n=2)

    assert [record["sample_id"] for record in records] == [1, 1, 3, 3, 3, 3]
    assert records[0]["span_id"] == "cnc_1_t0_cause"
    assert records[1]["event_role"] == "effect"
    assert records[-1]["span"] == "delays"


def test_run_eval_extraction_preserves_raw_output_without_substring_filtering() -> None:
    raw = """
{
  "components": [
    {
      "role": "Theme",
      "value": "invented value",
      "attributes": [
        {"role": "Attribute", "value": "green"}
      ]
    }
  ]
}
"""
    client = FakeClient([raw])
    span_record = {
        "dataset": "cnc",
        "sample_id": 1,
        "span_id": "cnc_1_t0_cause",
        "event_role": "cause",
        "span": "green apples",
        "sample_text": "green apples caused illness.",
        "triple_index": 0,
    }

    result = run_eval_extraction(span_record, client=client, prompt_version="v2")

    assert result["sample_id"] == 1
    assert result["raw_extraction_output"] == raw
    assert result["parsed_extraction"]["components"][0]["value"] == "invented value"
    assert client.messages[0][1]["content"].startswith("Role: cause\nSpan: green apples")


def test_validate_extraction_reports_substring_depth_and_forbidden_roles() -> None:
    extraction = {
        "components": [
            {
                "role": "Cause",
                "value": "rain",
                "attributes": [{"role": "Location", "value": "sky"}],
                "children": [
                    {
                        "role": "Theme",
                        "value": "storm",
                        "children": [
                            {"role": "Action", "value": "fell", "attributes": []}
                        ],
                    }
                ],
            }
        ]
    }

    validation = validate_extraction(
        extraction,
        span="rain fell",
        schema="nested",
        max_depth=2,
    )

    assert validation["json_parse_success"] is True
    assert validation["schema_valid"] is True
    assert validation["substring_valid"] is False
    assert validation["depth_compliant"] is False
    assert validation["max_depth"] == 3
    assert validation["node_count"] == 3
    assert validation["attribute_count"] == 1
    assert validation["child_link_count"] == 2
    assert validation["forbidden_role_count"] == 1
    assert validation["invalid_values"] == [
        {"path": "c0.attr0", "role": "Location", "value": "sky"},
        {"path": "c0.ch0", "role": "Theme", "value": "storm"},
    ]


def test_validate_two_layer_treats_non_empty_children_as_schema_and_depth_violation() -> None:
    extraction = {
        "components": [
            {"role": "Theme", "value": "rain", "attributes": [], "children": []},
            {"role": "Action", "value": "fell", "attributes": [], "children": [{"role": "Location", "value": "field"}]},
        ]
    }

    validation = validate_extraction(extraction, span="rain fell in field", schema="two_layer", max_depth=1)

    assert validation["schema_valid"] is False
    assert validation["depth_compliant"] is False
    assert validation["node_count"] == 3


def test_flatten_judge_units_uses_short_ids_and_keeps_graph_path_metadata() -> None:
    extraction = {
        "components": [
            {
                "role": "Theme",
                "value": "Anoop George",
                "attributes": [{"role": "Name", "value": "Anoop"}],
                "children": [
                    {
                        "role": "Description",
                        "value": "the main accused",
                        "attributes": [],
                    }
                ],
            }
        ]
    }

    units = flatten_judge_units(extraction, graph_event_id="triple_0_effect")

    assert [unit["id"] for unit in units] == ["n0", "a0", "n1", "l0"]
    assert units[0]["path"] == "c0"
    assert units[0]["graph_path"] == "triple_0_effect/component_0"
    assert units[1]["parent"] == {"id": "n0", "role": "Theme", "value": "Anoop George"}
    assert units[2]["path"] == "c0.ch0"
    assert units[3]["parent"]["id"] == "n0"
    assert units[3]["child"]["id"] == "n1"


def test_build_judge_prompt_hides_graph_paths_and_uses_compact_unit_ids() -> None:
    units = [
        {
            "id": "n0",
            "kind": "node",
            "path": "c0",
            "graph_path": "triple_0_cause/component_0",
            "role": "Theme",
            "value": "rain",
        }
    ]

    prompt = build_judge_prompt(span="heavy rain", units=units, judge_span_id="s0")

    assert "strict semantic judge" in prompt
    assert "Do not evaluate JSON validity" in prompt
    assert '"span_id": "s0"' in prompt
    assert '"id": "n0"' in prompt
    assert "graph_path" not in prompt
    assert "triple_0_cause" not in prompt


def test_parse_judge_output_accepts_markdown_and_numeric_scores() -> None:
    parsed = parse_judge_output(
        """
```json
{"span_id": "s0", "units": [{"id": "n0", "s": 1, "r": 0.5, "m": 1, "a": null, "t": 1, "e": null}]}
```
"""
    )

    assert parsed["units"][0]["r"] == 0.5


def test_aggregate_sample_results_uses_sample_level_macro_average() -> None:
    span_results = [
        {
            "dataset": "cnc",
            "sample_id": 5,
            "prompt_version": "v2",
            "triple_index": 0,
            "span_metrics": {"unit_precision": 1.0, "supported_information_yield": 3},
        },
        {
            "dataset": "cnc",
            "sample_id": 5,
            "prompt_version": "v2",
            "triple_index": 0,
            "span_metrics": {"unit_precision": 0.5, "supported_information_yield": 1},
        },
        {
            "dataset": "cnc",
            "sample_id": 7,
            "prompt_version": "v2",
            "triple_index": 0,
            "span_metrics": {"unit_precision": 0.25, "supported_information_yield": 2},
        },
    ]

    samples, method_metrics = aggregate_sample_results(span_results)

    assert samples[0]["sample_id"] == 5
    assert samples[0]["evaluated_span_count"] == 2
    assert samples[0]["sample_metrics"]["unit_precision"] == 0.75
    assert samples[0]["sample_metrics"]["supported_information_yield"] == 4
    assert method_metrics["sample_count"] == 2
    assert method_metrics["unit_precision"] == 0.5
    assert method_metrics["supported_information_yield"] == 3


def test_aggregate_sample_results_renames_aggregated_depth_and_tracks_observed_max() -> None:
    span_results = [
        {
            "dataset": "cnc",
            "sample_id": 5,
            "prompt_version": "nested_v1",
            "triple_index": 0,
            "span_metrics": {"max_depth": 1},
        },
        {
            "dataset": "cnc",
            "sample_id": 5,
            "prompt_version": "nested_v1",
            "triple_index": 0,
            "span_metrics": {"max_depth": 3},
        },
        {
            "dataset": "cnc",
            "sample_id": 7,
            "prompt_version": "nested_v1",
            "triple_index": 0,
            "span_metrics": {"max_depth": 4},
        },
    ]

    samples, method_metrics = aggregate_sample_results(span_results)

    sample_5 = next(sample for sample in samples if sample["sample_id"] == 5)
    sample_7 = next(sample for sample in samples if sample["sample_id"] == 7)
    assert sample_5["sample_metrics"]["avg_max_depth"] == 2
    assert sample_5["sample_metrics"]["max_observed_depth"] == 3
    assert "max_depth" not in sample_5["sample_metrics"]
    assert sample_7["sample_metrics"]["avg_max_depth"] == 4
    assert sample_7["sample_metrics"]["max_observed_depth"] == 4
    assert method_metrics["avg_max_depth"] == 3
    assert method_metrics["max_observed_depth"] == 4
    assert "max_depth" not in method_metrics


def test_compute_span_metrics_uses_none_for_judge_failure_instead_of_zero() -> None:
    validation = {
        "json_parse_success": True,
        "schema_valid": True,
        "substring_valid": True,
        "depth_compliant": True,
        "forbidden_role_count": 0,
        "max_depth": 1,
        "node_count": 1,
        "attribute_count": 1,
        "child_link_count": 0,
    }
    judge_units = [
        {
            "id": "a0",
            "kind": "attribute",
            "parent": {"id": "n0", "role": "Theme", "value": "troops"},
            "role": "Quantifier",
            "value": "5",
        }
    ]

    metrics = compute_span_metrics(validation, judge_units, judge_result=None)

    assert metrics["judge_success"] == 0
    assert metrics["attribute_precision"] is None
    assert metrics["unit_precision"] is None
    assert metrics["supported_information_yield"] is None


def test_compute_span_metrics_treats_missing_attribute_units_as_not_applicable() -> None:
    validation = {
        "json_parse_success": True,
        "schema_valid": True,
        "substring_valid": True,
        "depth_compliant": True,
        "forbidden_role_count": 0,
        "max_depth": 1,
        "node_count": 1,
        "attribute_count": 0,
        "child_link_count": 0,
    }
    judge_units = [{"id": "n0", "kind": "node", "role": "Theme", "value": "rain"}]
    judge_result = {"span_id": "s0", "units": [{"id": "n0", "s": 1, "r": 1, "m": 1, "a": None, "t": 1, "e": None}]}

    metrics = compute_span_metrics(validation, judge_units, judge_result)

    assert metrics["judge_success"] == 1
    assert metrics["unit_precision"] == 1
    assert metrics["supported_information_yield"] == 1
    assert metrics["attribute_precision"] is None
    assert metrics["attachment_precision"] is None


def test_aggregate_sample_results_skips_not_applicable_metric_values() -> None:
    span_results = [
        {
            "dataset": "cnc",
            "sample_id": 5,
            "prompt_version": "nested_v1",
            "triple_index": 0,
            "span_metrics": {"attribute_precision": None, "unit_precision": 1.0},
        },
        {
            "dataset": "cnc",
            "sample_id": 5,
            "prompt_version": "nested_v1",
            "triple_index": 0,
            "span_metrics": {"attribute_precision": 1.0, "unit_precision": 0.5},
        },
        {
            "dataset": "cnc",
            "sample_id": 7,
            "prompt_version": "nested_v1",
            "triple_index": 0,
            "span_metrics": {"attribute_precision": None, "unit_precision": 0.25},
        },
    ]

    samples, method_metrics = aggregate_sample_results(span_results)

    sample_5 = next(sample for sample in samples if sample["sample_id"] == 5)
    sample_7 = next(sample for sample in samples if sample["sample_id"] == 7)
    assert sample_5["sample_metrics"]["attribute_precision"] == 1
    assert "attribute_precision" not in sample_7["sample_metrics"]
    assert method_metrics["attribute_precision"] == 1
    assert method_metrics["unit_precision"] == 0.5


def test_save_eval_outputs_writes_spans_samples_and_metrics_without_summary(tmp_path: Path) -> None:
    paths = save_eval_outputs(
        span_results=[{"sample_id": 1}],
        sample_results=[{"sample_id": 1, "sample_metrics": {"unit_precision": 1.0}}],
        method_metrics={"sample_count": 1, "unit_precision": 1.0},
        output_dir=tmp_path,
        dataset="cnc",
        prompt_version="v2",
        sample_n=20,
        run_id="20260101_000000",
    )

    assert set(paths) == {"spans", "samples", "metrics"}
    assert paths["spans"].name == "cnc_v2_n20_20260101_000000_spans.jsonl"
    assert paths["samples"].exists()
    assert paths["metrics"].read_text(encoding="utf-8").splitlines()[0] == "metric,value"
    assert not list(tmp_path.glob("*summary.md"))


def test_deepseek_judge_client_sends_v4_pro_with_thinking_disabled(tmp_path: Path) -> None:
    key_path = tmp_path / "deepseek_api.txt"
    key_path.write_text("sk-test", encoding="utf-8")
    captured: dict[str, Any] = {}

    def fake_urlopen(request: Any, timeout: float) -> FakeResponse:
        captured["url"] = request.full_url
        captured["headers"] = dict(request.header_items())
        captured["timeout"] = timeout
        captured["body"] = json.loads(request.data.decode("utf-8"))
        return FakeResponse({"choices": [{"message": {"content": "{\"span_id\":\"s0\",\"units\":[]}"}}]})

    client = DeepSeekJudgeClient(api_key_path=key_path, urlopen_func=fake_urlopen)
    result = client.chat("judge prompt")

    assert result == '{"span_id":"s0","units":[]}'
    assert captured["url"] == "https://api.deepseek.com/chat/completions"
    assert captured["body"]["model"] == "deepseek-v4-pro"
    assert captured["body"]["thinking"] == {"type": "disabled"}
    assert captured["body"]["temperature"] == 0
    assert "reasoning_effort" not in captured["body"]
    assert captured["body"]["messages"][0]["role"] == "system"
    assert captured["body"]["messages"][1]["content"] == "judge prompt"


def test_deepseek_judge_client_sends_configured_thinking_options(tmp_path: Path) -> None:
    key_path = tmp_path / "deepseek_api.txt"
    key_path.write_text("sk-test", encoding="utf-8")
    captured: dict[str, Any] = {}

    def fake_urlopen(request: Any, timeout: float) -> FakeResponse:
        captured["body"] = json.loads(request.data.decode("utf-8"))
        return FakeResponse({"choices": [{"message": {"content": "{\"valid\":true}"}}]})

    client = DeepSeekJudgeClient(
        api_key_path=key_path,
        thinking="enabled",
        reasoning_effort="high",
        max_tokens=4096,
        urlopen_func=fake_urlopen,
    )

    assert client.chat("judge prompt") == '{"valid":true}'
    assert captured["body"]["thinking"] == {"type": "enabled"}
    assert captured["body"]["reasoning_effort"] == "high"
    assert captured["body"]["max_tokens"] == 4096
    assert "temperature" not in captured["body"]


def test_deepseek_judge_client_rejects_inconsistent_thinking_options(tmp_path: Path) -> None:
    key_path = tmp_path / "deepseek_api.txt"
    key_path.write_text("sk-test", encoding="utf-8")

    try:
        DeepSeekJudgeClient(
            api_key_path=key_path,
            thinking="disabled",
            reasoning_effort="high",
        )
    except ValueError as exc:
        assert "reasoning_effort" in str(exc)
    else:
        raise AssertionError("disabled thinking should reject reasoning_effort")


def test_deepseek_judge_client_retries_retryable_http_errors(tmp_path: Path) -> None:
    key_path = tmp_path / "deepseek_api.txt"
    key_path.write_text("sk-test", encoding="utf-8")
    calls = 0
    sleeps: list[float] = []

    def fake_urlopen(_request: Any, timeout: float) -> FakeResponse:
        nonlocal calls
        calls += 1
        if calls == 1:
            raise HTTPError("https://api.deepseek.com/chat/completions", 429, "Too Many Requests", {}, None)
        assert timeout == 30
        return FakeResponse({"choices": [{"message": {"content": "{\"span_id\":\"s0\",\"units\":[]}"}}]})

    client = DeepSeekJudgeClient(
        api_key_path=key_path,
        timeout=30,
        retry_times=3,
        retry_base_seconds=2,
        sleep_func=sleeps.append,
        urlopen_func=fake_urlopen,
    )

    assert client.chat("judge prompt") == '{"span_id":"s0","units":[]}'
    assert calls == 2
    assert sleeps == [2]


def test_deepseek_judge_client_does_not_retry_non_retryable_http_errors(tmp_path: Path) -> None:
    key_path = tmp_path / "deepseek_api.txt"
    key_path.write_text("sk-test", encoding="utf-8")
    calls = 0

    def fake_urlopen(_request: Any, timeout: float) -> FakeResponse:
        nonlocal calls
        assert timeout == 60.0
        calls += 1
        raise HTTPError("https://api.deepseek.com/chat/completions", 400, "Bad Request", {}, None)

    client = DeepSeekJudgeClient(
        api_key_path=key_path,
        retry_times=3,
        sleep_func=lambda _seconds: None,
        urlopen_func=fake_urlopen,
    )

    try:
        client.chat("judge prompt")
    except HTTPError as exc:
        assert exc.code == 400
    else:
        raise AssertionError("400 HTTPError should be raised")
    assert calls == 1


def test_run_parallel_judge_updates_results_without_reordering() -> None:
    class FakeJudgeClient:
        def __init__(self) -> None:
            self.prompts: list[str] = []

        def chat(self, prompt: str) -> str:
            self.prompts.append(prompt)
            if "bad-span" in prompt:
                raise RuntimeError("temporary judge failure")
            unit_id = "a0" if "attribute-span" in prompt else "n0"
            return json.dumps(
                {
                    "span_id": "s0",
                    "units": [
                        {"id": unit_id, "s": 1, "r": 1, "m": 1, "a": 1 if unit_id == "a0" else None, "t": 1, "e": None}
                    ],
                }
            )

    validation = {
        "json_parse_success": True,
        "schema_valid": True,
        "substring_valid": True,
        "depth_compliant": True,
        "forbidden_role_count": 0,
        "max_depth": 1,
        "node_count": 1,
        "attribute_count": 0,
        "child_link_count": 0,
    }
    span_results = [
        {
            "sample_id": 2,
            "span_id": "second",
            "judge_prompt": "node-span",
            "validation": validation,
            "judge_units": [{"id": "n0", "kind": "node", "role": "Theme", "value": "rain"}],
        },
        {
            "sample_id": 1,
            "span_id": "first",
            "judge_prompt": "attribute-span",
            "validation": {**validation, "attribute_count": 1},
            "judge_units": [
                {
                    "id": "a0",
                    "kind": "attribute",
                    "parent": {"id": "n0", "role": "Theme", "value": "troops"},
                    "role": "Quantifier",
                    "value": "5",
                }
            ],
        },
        {
            "sample_id": 3,
            "span_id": "third",
            "judge_prompt": "bad-span",
            "validation": validation,
            "judge_units": [{"id": "n0", "kind": "node", "role": "Theme", "value": "wind"}],
        },
    ]

    progressed: list[str] = []

    judged = run_parallel_judge(
        span_results,
        FakeJudgeClient(),
        max_workers=2,
        progress_callback=lambda result: progressed.append(str(result["span_id"])),
    )

    assert [result["span_id"] for result in judged] == ["second", "first", "third"]
    assert sorted(progressed) == ["first", "second", "third"]
    assert judged[0]["judge_result"]["units"][0]["id"] == "n0"
    assert judged[1]["span_metrics"]["attribute_precision"] == 1
    assert judged[2]["judge_result"] is None
    assert judged[2]["judge_error"]["type"] == "RuntimeError"
    assert judged[2]["span_metrics"]["judge_success"] == 0
