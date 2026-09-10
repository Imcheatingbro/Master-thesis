"""RAMS judge evaluation 流程的单元测试。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rams_judge_evaluator import (
    build_comparison_records,
    build_judge_prompt,
    build_prompt_input,
    compute_metrics,
    parse_judge_output,
    run_evaluation,
    save_comparison_outputs,
    select_records,
    summarize_selection,
)


class FakeClient:
    """按顺序返回预设 judge 输出。"""

    def __init__(self, outputs: list[str]) -> None:
        self.outputs = outputs
        self.prompts: list[str] = []

    def chat(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return self.outputs.pop(0)


def sample_record(
    record_id: str = "rams-judge-00001",
    label: bool = True,
    case_type: str = "positive",
) -> dict[str, Any]:
    """创建最小可用 RAMS judge 记录。"""
    return {
        "id": record_id,
        "pair_id": "doc-1::arg00",
        "doc_key": "doc-1",
        "source_split": "test",
        "sentences": [
            "A public execution happened in Tehran .",
            "The report was published later .",
        ],
        "event": {
            "type": "justice.judicialconsequences.execute",
            "trigger": {
                "text": "execution",
                "sentence_id": 0,
                "sentence_start": 2,
                "sentence_end": 2,
            },
            "allowed_roles": ["executioner", "defendant", "crime", "place"],
        },
        "candidate": {
            "role": "place",
            "span": {
                "text": "Tehran",
                "sentence_id": 0,
                "sentence_start": 5,
                "sentence_end": 5,
            },
        },
        "label": label,
        "case_type": case_type,
    }


def test_select_records_uses_fixed_dataset_order_and_limit() -> None:
    records = [
        sample_record(f"rams-judge-{index:05d}", label=index % 2 == 0)
        for index in range(1, 6)
    ]

    selected = select_records(records, sample_limit=3)

    assert [record["id"] for record in selected] == [
        "rams-judge-00001",
        "rams-judge-00002",
        "rams-judge-00003",
    ]
    assert len(select_records(records, sample_limit=None)) == 5
    with pytest.raises(ValueError):
        select_records(records, sample_limit=0)


def test_prompt_input_excludes_labels_and_local_metadata() -> None:
    record = sample_record(label=False, case_type="role_corruption")

    prompt_input = build_prompt_input(record)
    rendered = json.dumps(prompt_input)

    assert "label" not in prompt_input
    assert "case_type" not in prompt_input
    assert "pair_id" not in prompt_input
    assert "role_corruption" not in rendered
    assert prompt_input["candidate"]["span"]["text"] == "Tehran"


def test_build_prompt_and_parse_strict_boolean() -> None:
    template = "Judge this candidate.\n{input_json}"
    prompt = build_judge_prompt(sample_record(), template)

    assert "justice.judicialconsequences.execute" in prompt
    assert parse_judge_output('```json\n{"valid": true}\n```') is True
    assert parse_judge_output('<think>hidden</think>{"valid": false}') is False
    with pytest.raises(ValueError):
        parse_judge_output('{"valid": "true"}')


def test_compute_metrics_penalizes_invalid_outputs() -> None:
    results = [
        {
            "gold_label": True,
            "predicted_label": True,
            "case_type": "positive",
        },
        {
            "gold_label": False,
            "predicted_label": False,
            "case_type": "role_corruption",
        },
        {
            "gold_label": True,
            "predicted_label": None,
            "case_type": "positive",
        },
        {
            "gold_label": False,
            "predicted_label": None,
            "case_type": "span_swap",
        },
    ]

    metrics = compute_metrics(results)

    assert metrics["coverage"] == 0.5
    assert metrics["accuracy"] == 0.5
    assert metrics["f1"] == 0.5
    assert metrics["macro_f1"] == 0.5
    assert metrics["confusion_matrix"] == {
        "tp": 1,
        "tn": 1,
        "fp": 1,
        "fn": 1,
    }


def test_run_evaluation_checkpoints_and_resumes(tmp_path: Path) -> None:
    records = [
        sample_record("rams-judge-00001", label=True, case_type="positive"),
        sample_record(
            "rams-judge-00002",
            label=False,
            case_type="role_corruption",
        ),
    ]
    results_path = tmp_path / "predictions.jsonl"
    first_client = FakeClient(['{"valid": true}', '{"valid": false}'])

    first_results = run_evaluation(
        records,
        client=first_client,
        prompt_template="{input_json}",
        results_path=results_path,
        max_workers=1,
    )
    second_client = FakeClient([])
    resumed_results = run_evaluation(
        records,
        client=second_client,
        prompt_template="{input_json}",
        results_path=results_path,
        max_workers=1,
    )

    assert [result["correct"] for result in first_results] == [True, True]
    assert resumed_results == first_results
    assert len(first_client.prompts) == 2
    assert second_client.prompts == []
    assert len(results_path.read_text(encoding="utf-8").splitlines()) == 2


def test_summarize_selection_reports_current_prefix_distribution() -> None:
    records = [
        sample_record("rams-judge-00001", label=True, case_type="positive"),
        sample_record(
            "rams-judge-00002",
            label=False,
            case_type="span_swap",
        ),
    ]

    summary = summarize_selection(records)

    assert summary == {
        "total": 2,
        "labels": {"false": 1, "true": 1},
        "case_types": {"positive": 1, "span_swap": 1},
    }


def test_comparison_outputs_keep_input_gold_and_raw_model_output(
    tmp_path: Path,
) -> None:
    record = sample_record()
    result = {
        "id": record["id"],
        "pair_id": record["pair_id"],
        "doc_key": record["doc_key"],
        "case_type": record["case_type"],
        "gold_label": True,
        "predicted_label": False,
        "correct": False,
        "raw_output": '{"valid": false}',
        "error": None,
        "elapsed_seconds": 0.2,
    }

    comparisons = build_comparison_records([record], [result])
    paths = save_comparison_outputs([record], [result], tmp_path)

    assert comparisons[0]["gold"] == {"valid": True}
    assert comparisons[0]["model_output"]["raw"] == '{"valid": false}'
    assert comparisons[0]["model_output"]["parsed_valid"] is False
    assert "label" not in comparisons[0]["model_input"]
    assert paths["mistakes_jsonl"].exists()
    assert paths["comparison_csv"].exists()
    assert len(paths["mistakes_jsonl"].read_text(encoding="utf-8").splitlines()) == 1
