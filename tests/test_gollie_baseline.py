"""验证 GoLLIE prompt、Python 列表解析、断点续跑及统一评估接线。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.gollie_baseline import (
    DEFAULT_SOURCE_DIR,
    RunConfig,
    build_prompt,
    parse_gollie_output,
    prediction_from_gollie_output,
    run_gollie_baseline,
    source_hashes,
)


def test_author_source_and_fixed_prompt_use_only_text() -> None:
    hashes = source_hashes(DEFAULT_SOURCE_DIR)
    assert set(hashes) == {
        "README.md",
        "notebooks/Create Custom Task.ipynb",
        "notebooks/Relation Extraction.ipynb",
        "configs/model_configs/eval/GoLLIE-13B_CodeLLaMA.yaml",
    }
    sample = {
        "id": "hidden",
        "text": "Rain causes flooding.",
        "has_causal": True,
        "relations": [{"cause": "SECRET_GOLD", "effect": "SECRET_GOLD"}],
    }
    prompt = build_prompt(sample)
    assert "class CausalRelation(Relation)" in prompt
    assert "arg1: str" in prompt and "arg2: str" in prompt
    assert "text = 'Rain causes flooding.'" in prompt
    assert prompt.endswith("result = [")
    assert "SECRET_GOLD" not in prompt and "hidden" not in prompt


def test_parser_accepts_raw_completion_and_full_list_without_executing_code() -> None:
    raw = (
        'CausalRelation(arg1="heavy rain", arg2="flooding"),\n'
        "    CausalRelation('power failure', 'shutdown'),\n]"
    )
    pairs, errors = parse_gollie_output(raw)
    assert errors == []
    assert pairs == [
        {"cause": "heavy rain", "effect": "flooding"},
        {"cause": "power failure", "effect": "shutdown"},
    ]
    assert parse_gollie_output("[]") == ([], [])
    full = "result = [CausalRelation(arg1='A', arg2='B')]\n# trailing text"
    assert parse_gollie_output(full)[0] == [{"cause": "A", "effect": "B"}]


def test_parser_filters_unknown_or_invalid_annotations_and_never_evals() -> None:
    output = (
        "[OtherRelation(arg1='A', arg2='B'), "
        "CausalRelation(arg1=None, arg2='B'), "
        "CausalRelation(arg1=__import__('os').system('whoami'), arg2='B')]"
    )
    pairs, errors = parse_gollie_output(output)
    assert pairs == []
    assert len(errors) == 3
    assert parse_gollie_output("CausalRelation(arg1='A', arg2='B')")[1] == ["missing_or_unclosed_list"]


def test_prediction_derives_detection_from_joint_extraction() -> None:
    positive = prediction_from_gollie_output(1, "CausalRelation(arg1='Rain', arg2='flooding'),]")
    assert positive["has_causal"] is True
    assert positive["triples"] == [{"cause": {"span": "Rain"}, "effect": {"span": "flooding"}}]
    negative = prediction_from_gollie_output(2, "]")
    assert negative["has_causal"] is False and negative["triples"] == []


class FakeRunner:
    """以固定 completion 验证保存、续跑和 evaluator，不调用 LM Studio。"""

    def __init__(self, responses: list[str]) -> None:
        self.config = RunConfig(base_url="http://test.invalid/v1")
        self.source_sha256 = {"author": "test"}
        self.identity = {
            "provider": "fake",
            "model": self.config.model,
            "transport": "raw_completion_without_chat_template",
        }
        self.runtime: dict[str, Any] = {"request_count": 0}
        self.responses = list(responses)
        self.prompts: list[str] = []

    def generate(self, prompt: str) -> str:
        self.prompts.append(prompt)
        self.runtime["request_count"] += 1
        return self.responses.pop(0)


def _samples() -> list[dict[str, Any]]:
    return [
        {
            "id": 1,
            "text": "Rain causes flooding.",
            "has_causal": True,
            "relations": [{"cause": "Rain", "effect": "flooding"}],
        },
        {"id": 2, "text": "Birds are singing.", "has_causal": False, "relations": []},
    ]


def test_complete_run_saves_auditable_outputs_and_reuses_checkpoint(tmp_path: Path) -> None:
    runner = FakeRunner(["CausalRelation(arg1='Rain', arg2='flooding'),]", "]"])
    progress: list[tuple[int, int]] = []
    result = run_gollie_baseline(
        _samples(), runner, "cnc_sft_test", tmp_path, "smoke",
        primary_metric="anchor_window", progress_callback=lambda done, total: progress.append((done, total)),
    )
    assert len(runner.prompts) == 2
    assert progress == [(0, 2), (1, 2), (2, 2)]
    assert result["report"]["detection"]["f1"] == 1.0
    assert result["report"]["extraction"]["anchor_window"]["all_samples"]["f1"] == 1.0
    assert result["report"]["baseline"]["diagnostics"] == {
        "parse_error_samples": 0,
        "predicted_positive_samples": 1,
        "predicted_pairs": 1,
        "nonverbatim_pairs": 0,
    }
    assert all(path.is_file() for path in result["paths"].values())
    manifest = json.loads(result["paths"]["manifest"].read_text(encoding="utf-8"))
    assert manifest["task_mode"] == "single_stage_joint_detection_and_extraction"
    assert manifest["runner"]["transport"] == "raw_completion_without_chat_template"
    assert manifest["runtime"]["request_count"] == 2

    reused = FakeRunner([])
    second = run_gollie_baseline(
        _samples(), reused, "cnc_sft_test", tmp_path, "smoke", primary_metric="anchor_window"
    )
    assert reused.prompts == []
    assert second["predictions"] == result["predictions"]


def test_duplicate_ids_and_changed_same_name_run_are_rejected(tmp_path: Path) -> None:
    samples = _samples()
    samples[1]["id"] = 1
    try:
        run_gollie_baseline(samples, FakeRunner([]), "ade", tmp_path, "duplicate")
    except ValueError as exc:
        assert "id 不唯一" in str(exc)
    else:
        raise AssertionError("重复 id 应被拒绝")

    run_gollie_baseline(_samples(), FakeRunner(["]", "]"]), "ade", tmp_path, "stable")
    changed = _samples()
    changed[0]["text"] += " changed"
    try:
        run_gollie_baseline(changed, FakeRunner([]), "ade", tmp_path, "stable")
    except ValueError as exc:
        assert "同名运行" in str(exc)
    else:
        raise AssertionError("变化的同名运行应被拒绝")
