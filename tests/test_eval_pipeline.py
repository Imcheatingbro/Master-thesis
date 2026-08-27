"""SPEC_05：eval 运行流程与报告落盘 helper 的单元测试。"""

from __future__ import annotations

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any

from src.eval_pipeline import (
    EvalRunConfig,
    build_eval_report_filename,
    format_detection_diff_examples,
    format_eval_diff_examples,
    format_eval_report_text,
    load_sample_judgements_from_report,
    load_sample_judgements_from_report_text,
    run_stream_eval,
    select_detection_diff_examples,
    select_eval_diff_examples,
    write_eval_report,
)


def test_build_eval_report_filename_contains_required_metadata() -> None:
    filename = build_eval_report_filename(
        model="qwen/qwen3-14b",
        dataset="cnc",
        sample_count=40,
        prompt_name="v2",
        use_rag=False,
        rag_mode="knn_pattern",
        top_k=5,
        generated_at=datetime(2026, 5, 24, 9, 30, 15),
    )

    assert filename == "qwen-qwen3-14b_cnc-n40_prompt-v2_rag-off_20260524-093015.md"


def test_format_eval_report_text_includes_metrics_and_all_sample_judgements() -> None:
    text = format_eval_report_text(
        title="cnc first 2 eval report",
        metrics_text="metrics block",
        sample_judgements=[
            {
                "id": 1,
                "text": "Rain caused flooding.",
                "gold_has_causal": True,
                "pred_has_causal": True,
                "gold_relations": [{"cause": "Rain", "effect": "flooding"}],
                "pred_triples": [{"cause": {"span": "Rain"}, "effect": {"span": "flooding"}}],
                "primary_metric": "strict_token_f1",
                "strict_token_f1": {"counts": {"tp": 1, "fp": 0, "fn": 0}},
                "anchor_window": {"counts": {"tp": 1, "fp": 0, "fn": 0}},
                "token_f1": {"counts": {"tp": 1, "fp": 0, "fn": 0}},
            },
            {
                "id": 2,
                "text": "No relation.",
                "gold_has_causal": False,
                "pred_has_causal": False,
                "gold_relations": [],
                "pred_triples": [],
                "primary_metric": "strict_token_f1",
                "strict_token_f1": {"counts": {"tp": 0, "fp": 0, "fn": 0}},
                "anchor_window": {"counts": {"tp": 0, "fp": 0, "fn": 0}},
                "token_f1": {"counts": {"tp": 0, "fp": 0, "fn": 0}},
            },
        ],
        config={"prompt_name": "v2", "rag": "off"},
    )

    assert "metrics block" in text
    assert "## 样本明细" in text
    assert "--- id=1 ---" in text
    assert "--- id=2 ---" in text
    assert '"gold_relations"' in text
    assert "original_like" not in text


def test_format_eval_report_text_limits_sample_details_when_above_threshold() -> None:
    sample_judgements = [
        {
            "id": sample_id,
            "text": f"Sample {sample_id}.",
            "gold_has_causal": False,
            "pred_has_causal": False,
            "gold_relations": [],
            "pred_triples": [],
            "primary_metric": "anchor_window",
            "strict_token_f1": {"counts": {"tp": 0, "fp": 0, "fn": 0}},
            "anchor_window": {"counts": {"tp": 0, "fp": 0, "fn": 0}},
            "token_f1": {"counts": {"tp": 0, "fp": 0, "fn": 0}},
        }
        for sample_id in range(1, 202)
    ]

    text = format_eval_report_text(
        title="ade first 201 eval report",
        metrics_text="样本总数: 201",
        sample_judgements=sample_judgements,
        config={"prompt_name": "v7.2"},
    )

    assert "样本总数: 201" in text
    assert "Sample details shown: first 200 of 201." in text
    assert "--- id=200 ---" in text
    assert "--- id=201 ---" not in text


def test_format_eval_report_text_can_save_first_wrong_samples_only() -> None:
    sample_judgements = [
        _sample_judgement(1, gold=True, pred=True, counts={"tp": 1, "fp": 0, "fn": 0}),
        *[
            _sample_judgement(
                sample_id,
                gold=True,
                pred=True,
                counts={"tp": 0, "fp": 1, "fn": 1},
            )
            for sample_id in range(2, 204)
        ],
    ]

    text = format_eval_report_text(
        title="cnc wrong sample report",
        metrics_text="样本总数: 203",
        sample_judgements=sample_judgements,
        config={"prompt_name": "v16"},
        sample_detail_limit=200,
        sample_detail_mode="errors",
    )

    assert "Sample details shown: first 200 of 202 wrong samples from 203 total samples." in text
    assert "--- id=1 ---" not in text
    assert "--- id=2 ---" in text
    assert "--- id=201 ---" in text
    assert "--- id=202 ---" not in text
    assert "--- id=203 ---" not in text


def test_format_eval_report_text_saves_all_wrong_samples_when_below_limit() -> None:
    generation_failure = _sample_judgement(
        4,
        gold=False,
        pred=False,
        counts={"tp": 0, "fp": 0, "fn": 0},
    )
    generation_failure["generation_error_type"] = "invalid_json_syntax"
    sample_judgements = [
        _sample_judgement(1, gold=True, pred=True, counts={"tp": 1, "fp": 0, "fn": 0}),
        _sample_judgement(2, gold=True, pred=True, counts={"tp": 0, "fp": 1, "fn": 1}),
        _sample_judgement(3, gold=True, pred=False, counts={"tp": 0, "fp": 0, "fn": 1}),
        generation_failure,
    ]

    text = format_eval_report_text(
        title="cnc wrong sample report",
        metrics_text="样本总数: 4",
        sample_judgements=sample_judgements,
        config={"prompt_name": "v16"},
        sample_detail_limit=200,
        sample_detail_mode="errors",
    )

    assert "Sample details shown: all 3 wrong samples from 4 total samples." in text
    assert "--- id=1 ---" not in text
    assert "--- id=2 ---" in text
    assert "--- id=3 ---" in text
    assert "--- id=4 ---" in text


def test_format_eval_report_text_uses_selected_error_metric() -> None:
    strict_only_error = _sample_judgement(
        2,
        gold=True,
        pred=True,
        counts={"tp": 0, "fp": 1, "fn": 1},
    )
    strict_only_error["anchor_window"]["counts"] = {"tp": 1, "fp": 0, "fn": 0}
    anchor_only_error = _sample_judgement(
        3,
        gold=True,
        pred=True,
        counts={"tp": 1, "fp": 0, "fn": 0},
    )
    anchor_only_error["anchor_window"]["counts"] = {"tp": 0, "fp": 1, "fn": 1}
    sample_judgements = [strict_only_error, anchor_only_error]

    anchor_text = format_eval_report_text(
        title="anchor wrong sample report",
        metrics_text="样本总数: 2",
        sample_judgements=sample_judgements,
        config={"dataset": "li"},
        sample_detail_limit=200,
        sample_detail_mode="errors",
        sample_detail_error_metric="anchor_window",
    )
    strict_text = format_eval_report_text(
        title="strict wrong sample report",
        metrics_text="样本总数: 2",
        sample_judgements=sample_judgements,
        config={"dataset": "cnc"},
        sample_detail_limit=200,
        sample_detail_mode="errors",
        sample_detail_error_metric="strict_token_f1",
    )

    assert "--- id=2 ---" not in anchor_text
    assert "--- id=3 ---" in anchor_text
    assert "--- id=2 ---" in strict_text
    assert "--- id=3 ---" not in strict_text


def test_select_eval_diff_examples_filters_detected_only_fn() -> None:
    sample_judgements = [
        _sample_judgement(1, gold=True, pred=True, counts={"tp": 1, "fp": 0, "fn": 0}),
        _sample_judgement(2, gold=True, pred=True, counts={"tp": 0, "fp": 1, "fn": 1}),
        _sample_judgement(3, gold=True, pred=False, counts={"tp": 0, "fp": 0, "fn": 1}),
        _sample_judgement(4, gold=False, pred=True, counts={"tp": 0, "fp": 1, "fn": 0}),
    ]

    examples = select_eval_diff_examples(
        sample_judgements,
        layer="detected_only",
        metric="strict_token_f1",
        bucket="FN",
        limit=20,
    )

    assert [example["id"] for example in examples] == [2]
    assert examples[0]["count"] == 1
    assert examples[0]["gold_relations"] == [{"cause": "gold cause 2", "effect": "gold effect 2"}]
    assert examples[0]["pred_triples"] == [
        {"cause": {"span": "pred cause 2"}, "effect": {"span": "pred effect 2"}}
    ]


def test_format_eval_diff_examples_groups_limited_gold_vs_pred_rows() -> None:
    sample_judgements = [
        _sample_judgement(1, gold=True, pred=True, counts={"tp": 0, "fp": 1, "fn": 1}),
        _sample_judgement(2, gold=True, pred=True, counts={"tp": 0, "fp": 1, "fn": 2}),
    ]

    text = format_eval_diff_examples(
        sample_judgements,
        layer="detected_only",
        metric="strict_token_f1",
        bucket="fn",
        limit=1,
    )

    assert "Layer: detected_only | metric: strict_token_f1 | bucket: FN" in text
    assert "showing 1 of 2 matching samples" in text
    assert "--- id=1 | FN count=1 ---" in text
    assert "--- id=2" not in text
    assert "gold_relations:" in text
    assert "pred_triples:" in text


def test_select_detection_diff_examples_filters_fn() -> None:
    sample_judgements = [
        _sample_judgement(1, gold=True, pred=True, counts={"tp": 1, "fp": 0, "fn": 0}),
        _sample_judgement(2, gold=True, pred=False, counts={"tp": 0, "fp": 0, "fn": 1}),
        _sample_judgement(3, gold=False, pred=True, counts={"tp": 0, "fp": 1, "fn": 0}),
        _sample_judgement(4, gold=False, pred=False, counts={"tp": 0, "fp": 0, "fn": 0}),
    ]

    examples = select_detection_diff_examples(sample_judgements, bucket="FN", limit=20)

    assert [example["id"] for example in examples] == [2]
    assert examples[0]["gold_relations"] == [{"cause": "gold cause 2", "effect": "gold effect 2"}]
    assert examples[0]["pred_triples"] == []


def test_format_detection_diff_examples_groups_limited_rows() -> None:
    sample_judgements = [
        _sample_judgement(1, gold=True, pred=False, counts={"tp": 0, "fp": 0, "fn": 1}),
        _sample_judgement(2, gold=True, pred=False, counts={"tp": 0, "fp": 0, "fn": 1}),
    ]

    text = format_detection_diff_examples(sample_judgements, bucket="fn", limit=1)

    assert "Layer: detection | bucket: FN" in text
    assert "showing 1 of 2 matching samples" in text
    assert "--- id=1 | detection=FN ---" in text
    assert "--- id=2" not in text
    assert "gold_relations:" in text
    assert "pred_triples:" in text


def test_load_sample_judgements_from_report_text_rehydrates_visible_details() -> None:
    report_text = format_eval_report_text(
        title="cnc first 1 eval report",
        metrics_text="metrics block",
        sample_judgements=[
            _sample_judgement(7, gold=True, pred=True, counts={"tp": 0, "fp": 1, "fn": 1}),
        ],
        config={"prompt_name": "v7.6"},
    )

    sample_judgements = load_sample_judgements_from_report_text(report_text)

    assert len(sample_judgements) == 1
    assert sample_judgements[0]["id"] == 7
    assert sample_judgements[0]["text"] == "Sample 7."
    assert sample_judgements[0]["strict_token_f1"]["counts"] == {"tp": 0, "fp": 1, "fn": 1}
    assert sample_judgements[0]["gold_relations"] == [{"cause": "gold cause 7", "effect": "gold effect 7"}]


def test_load_sample_judgements_from_report_text_uses_li_anchor_primary_from_config() -> None:
    judgement = _sample_judgement(2, gold=True, pred=True, counts={"tp": 0, "fp": 1, "fn": 1})
    judgement["primary_metric"] = "strict_token_f1"
    judgement["anchor_window"] = {"counts": {"tp": 0, "fp": 0, "fn": 1}}
    report_text = format_eval_report_text(
        title="li first 1 eval report",
        metrics_text="metrics block",
        sample_judgements=[judgement],
        config={"dataset": "li", "prompt_name": "v8.2"},
    )

    sample_judgements = load_sample_judgements_from_report_text(report_text)
    diff_text = format_eval_diff_examples(
        sample_judgements,
        layer="detected_only",
        metric="primary",
        bucket="fn",
        limit=1,
    )

    assert sample_judgements[0]["primary_metric"] == "anchor_window"
    assert "anchor_window counts: {'tp': 0, 'fp': 0, 'fn': 1}" in diff_text
    assert "strict_token_f1 counts:" not in diff_text


def test_load_sample_judgements_from_report_resolves_report_name(tmp_path: Path) -> None:
    report_text = format_eval_report_text(
        title="cnc first 1 eval report",
        metrics_text="metrics block",
        sample_judgements=[
            _sample_judgement(8, gold=True, pred=True, counts={"tp": 0, "fp": 1, "fn": 1}),
        ],
        config={"prompt_name": "v7.6"},
    )
    report_path = tmp_path / "deepseek-v4-pro_cnc-n300_prompt-v7.6_rag-off_20260707-033431.md"
    report_path.write_text(report_text, encoding="utf-8")

    sample_judgements = load_sample_judgements_from_report(
        "deepseek-v4-pro_cnc-n300_prompt-v7.6_rag-off_20260707-033431",
        report_dir=tmp_path,
    )

    assert [row["id"] for row in sample_judgements] == [8]


def test_write_eval_report_creates_target_directory_and_file(tmp_path: Path) -> None:
    path = write_eval_report(
        output_dir=tmp_path / "results" / "eval_report",
        model="qwen/qwen3-14b",
        dataset="li",
        sample_count=3,
        prompt_name="v1",
        use_rag=True,
        rag_mode="pattern",
        top_k=2,
        generated_at=datetime(2026, 5, 24, 10, 0, 0),
        metrics_text="metrics",
        sample_judgements=[],
        config={"dataset": "li"},
    )

    assert path.name == "qwen-qwen3-14b_li-n3_prompt-v1_rag-pattern-k2_20260524-100000.md"
    assert path.exists()
    assert "metrics" in path.read_text(encoding="utf-8")


def test_eval_run_config_reports_llm_runtime_metadata_without_api_key(tmp_path: Path) -> None:
    config = EvalRunConfig(
        project_root=tmp_path,
        model="deepseek-v4-pro",
        dataset="ade",
        prompt_name="v6.2",
        use_rag=False,
        rag_mode="knn_pattern",
        rag_top_k=2,
        temperature=0.0,
        max_tokens=8192,
        progress_every=50,
        max_workers=3,
        llm_provider="deepseek",
        llm_base_url="https://api.deepseek.com",
        context_length=8196,
        reasoning_effort="high",
        llm_extra_body={"thinking": {"type": "enabled"}},
        api_key_source="file:deepseek_api.txt",
        save_report=True,
        report_dir="results/eval_report",
        report_detail_limit=75,
        report_detail_mode="errors",
        report_error_metric="anchor_window",
    )

    report_config = config.to_report_config(sample_count=100, label="ade first 100")

    assert report_config["llm_provider"] == "deepseek"
    assert report_config["llm_base_url"] == "https://api.deepseek.com"
    assert report_config["context_length"] == 8196
    assert report_config["reasoning_effort"] == "high"
    assert report_config["llm_extra_body"] == {"thinking": {"type": "enabled"}}
    assert report_config["api_key_source"] == "file:deepseek_api.txt"
    assert report_config["report_detail_limit"] == 75
    assert report_config["report_detail_mode"] == "errors"
    assert report_config["report_error_metric"] == "anchor_window"
    assert "api_key" not in report_config


def test_run_stream_eval_saves_report_and_emits_debug_rows(tmp_path: Path) -> None:
    samples = [
        {
            "id": 1,
            "text": "Rain caused flooding.",
            "has_causal": True,
            "relations": [{"cause": "Rain", "effect": "flooding"}],
        },
        {"id": 2, "text": "No relation.", "has_causal": False, "relations": []},
    ]
    config = EvalRunConfig(
        project_root=tmp_path,
        model="qwen/qwen3-14b",
        dataset="cnc",
        prompt_name="v2",
        use_rag=False,
        rag_mode="pattern",
        rag_top_k=3,
        temperature=0.1,
        max_tokens=512,
        progress_every=1,
        save_report=True,
        report_dir="results/eval_report",
    )
    emitted: list[str] = []

    report = run_stream_eval(
        samples,
        label="cnc first 2",
        client=object(),
        config=config,
        generator=_fake_generator,
        emit=emitted.append,
        generated_at=datetime(2026, 5, 24, 11, 0, 0),
    )

    report_path = Path(str(report["report_path"]))
    report_text = report_path.read_text(encoding="utf-8")
    assert report["n_samples"] == 2
    assert report["extraction"]["all_samples"]["tp"] == 1
    assert [row["id"] for row in report["sample_judgements"]] == [1, 2]
    assert report_path.name == "qwen-qwen3-14b_cnc-n2_prompt-v2_rag-off_20260524-110000.md"
    assert "--- id=1 ---" in report_text
    assert any("前 10 条样本判定" in message for message in emitted)
    assert "generation_failures_path" not in report
    assert "parse_repairs_path" not in report
    assert not list(report_path.parent.glob("*_generation_failures.jsonl"))
    assert not list(report_path.parent.glob("*_parse_repairs.jsonl"))


def test_run_stream_eval_passes_explicit_triples_only_schema(tmp_path: Path) -> None:
    samples = [
        {
            "id": 1,
            "text": "Rain caused flooding.",
            "has_causal": True,
            "relations": [{"cause": "Rain", "effect": "flooding"}],
        }
    ]
    config = EvalRunConfig(
        project_root=tmp_path,
        model="gemma-triples-only",
        dataset="cnc",
        prompt_name="cnc_gemma_v4_triples_only",
        use_rag=False,
        rag_mode="knn",
        rag_top_k=0,
        temperature=0.0,
        max_tokens=512,
        output_schema="triples_only",
        progress_every=1,
    )

    report = run_stream_eval(
        samples,
        label="triples-only check",
        client=object(),
        config=config,
        generator=_fake_triples_only_generator,
    )

    assert report["detection"]["f1"] == 1.0
    assert report["extraction"]["strict_token_f1"]["all_samples"]["f1"] == 1.0


def test_run_stream_eval_records_generation_failure_summary(tmp_path: Path) -> None:
    samples = [
        {
            "id": 1,
            "text": "Rain caused flooding.",
            "has_causal": True,
            "relations": [{"cause": "Rain", "effect": "flooding"}],
        },
        {"id": 8, "text": "Hard sample.", "has_causal": False, "relations": []},
    ]
    config = EvalRunConfig(
        project_root=tmp_path,
        model="qwen3.5-9b.gguf",
        dataset="cnc",
        prompt_name="v2",
        use_rag=False,
        rag_mode="pattern",
        rag_top_k=0,
        temperature=0.0,
        max_tokens=800,
        save_report=True,
        report_dir="results/eval_report",
    )

    report = run_stream_eval(
        samples,
        label="cnc failure check",
        client=object(),
        config=config,
        generator=_fake_generator_with_failure,
        generated_at=datetime(2026, 5, 25, 12, 0, 0),
    )

    failure_summary = report["generation_failures"]
    assert failure_summary["total"] == 1
    assert failure_summary["by_type"] == {"llm_reasoning_only_empty_content": 1}
    assert failure_summary["samples"][0]["id"] == 8

    report_text = Path(str(report["report_path"])).read_text(encoding="utf-8")
    assert "## 生成失败统计" in report_text
    assert "llm_reasoning_only_empty_content" in report_text
    assert "reasoning_content" in report_text
    failure_path = Path(str(report["generation_failures_path"]))
    assert failure_path.name.endswith("_generation_failures.jsonl")
    failure_records = [
        json.loads(line) for line in failure_path.read_text(encoding="utf-8").splitlines() if line.strip()
    ]
    assert failure_records == [
        {
            "id": 8,
            "text": "Hard sample.",
            "error_type": "llm_reasoning_only_empty_content",
            "error_message": "模型只返回 reasoning_content，content 为空",
            "attempts": [
                {
                    "attempt": 1,
                    "raw_output": None,
                    "error_type": "llm_reasoning_only_empty_content",
                    "error_message": "模型只返回 reasoning_content，content 为空",
                }
            ],
        }
    ]


def test_run_stream_eval_records_parse_repair_summary_and_raw_output(tmp_path: Path) -> None:
    samples = [
        {
            "id": 23,
            "text": "Rain caused flooding.",
            "has_causal": True,
            "relations": [{"cause": "Rain", "effect": "flooding"}],
        }
    ]
    config = EvalRunConfig(
        project_root=tmp_path,
        model="gemma-4-31b",
        dataset="cnc",
        prompt_name="v16",
        use_rag=False,
        rag_mode="knn",
        rag_top_k=0,
        temperature=0.0,
        max_tokens=2048,
        save_report=True,
        report_dir="results/eval_report",
    )

    report = run_stream_eval(
        samples,
        label="cnc repair check",
        client=object(),
        config=config,
        generator=_fake_generator_with_repair,
        generated_at=datetime(2026, 7, 25, 1, 0, 0),
    )

    assert report["parse_repairs"] == {
        "total": 1,
        "by_type": {"duplicate_effect_closing_brace": 1},
        "samples": [{"id": 23, "repair_type": "duplicate_effect_closing_brace"}],
    }
    repair_path = Path(str(report["parse_repairs_path"]))
    records = [json.loads(line) for line in repair_path.read_text(encoding="utf-8").splitlines()]
    assert records == [
        {
            "id": 23,
            "text": "Rain caused flooding.",
            "repair_type": "duplicate_effect_closing_brace",
            "raw_output": "RAW_OUTPUT_WITH_DUPLICATE_BRACE",
        }
    ]
    report_text = Path(str(report["report_path"])).read_text(encoding="utf-8")
    assert "## 解析修复统计" in report_text
    assert "duplicate_effect_closing_brace" in report_text
    assert "RAW_OUTPUT_WITH_DUPLICATE_BRACE" not in report_text


def test_run_stream_eval_parallel_preserves_report_order(tmp_path: Path) -> None:
    samples = [
        {
            "id": 1,
            "text": "Rain caused flooding.",
            "has_causal": True,
            "relations": [{"cause": "Rain", "effect": "flooding"}],
        },
        {"id": 2, "text": "No relation.", "has_causal": False, "relations": []},
        {
            "id": 3,
            "text": "Fire caused smoke.",
            "has_causal": True,
            "relations": [{"cause": "Fire", "effect": "smoke"}],
        },
    ]
    config = EvalRunConfig(
        project_root=tmp_path,
        model="deepseek-v4-pro",
        dataset="cnc",
        prompt_name="v2",
        use_rag=False,
        rag_mode="pattern",
        rag_top_k=0,
        temperature=0.0,
        max_tokens=800,
        progress_every=1,
        max_workers=3,
        save_report=True,
        report_dir="results/eval_report",
    )

    report = run_stream_eval(
        samples,
        label="cnc parallel check",
        client=object(),
        config=config,
        generator=_fake_generator_out_of_order,
        generated_at=datetime(2026, 5, 25, 13, 0, 0),
    )

    report_text = Path(str(report["report_path"])).read_text(encoding="utf-8")
    assert report["n_samples"] == 3
    assert report_text.index("--- id=1 ---") < report_text.index("--- id=2 ---") < report_text.index("--- id=3 ---")


def _fake_generator(
    text: str,
    sample_id: int | None,
    client: Any,
    retriever: Any,
    use_rag: bool,
    top_k: int,
    rag_mode: str,
    prompt_name: str,
) -> dict[str, Any]:
    if sample_id == 1:
        return {
            "id": sample_id,
            "has_causal": True,
            "triples": [{"cause": {"span": "Rain"}, "effect": {"span": "flooding"}}],
        }
    return {"id": sample_id, "has_causal": False, "triples": []}


def _fake_triples_only_generator(
    text: str,
    sample_id: int | None,
    client: Any,
    retriever: Any,
    use_rag: bool,
    top_k: int,
    rag_mode: str,
    prompt_name: str,
    output_schema: str,
) -> dict[str, Any]:
    assert output_schema == "triples_only"
    return {
        "id": sample_id,
        "has_causal": True,
        "triples": [
            {
                "cause": {"span": "Rain"},
                "relation": "caused",
                "effect": {"span": "flooding"},
            }
        ],
    }


def _sample_judgement(sample_id: int, gold: bool, pred: bool, counts: dict[str, int]) -> dict[str, Any]:
    return {
        "id": sample_id,
        "text": f"Sample {sample_id}.",
        "gold_has_causal": gold,
        "pred_has_causal": pred,
        "gold_relations": [{"cause": f"gold cause {sample_id}", "effect": f"gold effect {sample_id}"}]
        if gold
        else [],
        "pred_triples": [
            {"cause": {"span": f"pred cause {sample_id}"}, "effect": {"span": f"pred effect {sample_id}"}}
        ]
        if pred
        else [],
        "primary_metric": "strict_token_f1",
        "strict_token_f1": {"counts": counts},
        "anchor_window": {"counts": counts},
        "token_f1": {"counts": counts},
    }


def _fake_generator_with_failure(
    text: str,
    sample_id: int | None,
    client: Any,
    retriever: Any,
    use_rag: bool,
    top_k: int,
    rag_mode: str,
    prompt_name: str,
) -> dict[str, Any]:
    if sample_id == 8:
        return {
            "id": sample_id,
            "has_causal": False,
            "triples": [],
            "error_type": "llm_reasoning_only_empty_content",
            "error_message": "模型只返回 reasoning_content，content 为空",
            "generation_attempts": [
                {
                    "attempt": 1,
                    "raw_output": None,
                    "error_type": "llm_reasoning_only_empty_content",
                    "error_message": "模型只返回 reasoning_content，content 为空",
                }
            ],
        }
    return {
        "id": sample_id,
        "has_causal": True,
        "triples": [{"cause": {"span": "Rain"}, "effect": {"span": "flooding"}}],
    }


def _fake_generator_with_repair(
    text: str,
    sample_id: int | None,
    client: Any,
    retriever: Any,
    use_rag: bool,
    top_k: int,
    rag_mode: str,
    prompt_name: str,
) -> dict[str, Any]:
    return {
        "id": sample_id,
        "has_causal": True,
        "triples": [{"cause": {"span": "Rain"}, "effect": {"span": "flooding"}}],
        "parse_repair_type": "duplicate_effect_closing_brace",
        "parse_repair_raw_output": "RAW_OUTPUT_WITH_DUPLICATE_BRACE",
    }


def _fake_generator_out_of_order(
    text: str,
    sample_id: int | None,
    client: Any,
    retriever: Any,
    use_rag: bool,
    top_k: int,
    rag_mode: str,
    prompt_name: str,
) -> dict[str, Any]:
    delays = {1: 0.03, 2: 0.01, 3: 0.0}
    time.sleep(delays.get(sample_id, 0.0))
    if sample_id == 2:
        return {"id": sample_id, "has_causal": False, "triples": []}
    cause = "Rain" if sample_id == 1 else "Fire"
    effect = "flooding" if sample_id == 1 else "smoke"
    return {
        "id": sample_id,
        "has_causal": True,
        "triples": [{"cause": {"span": cause}, "effect": {"span": effect}}],
    }
