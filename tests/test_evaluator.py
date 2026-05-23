"""SPEC_05：Demo1 evaluator 的单元测试。"""

from __future__ import annotations

import pytest

from src.evaluator import (
    Evaluator,
    build_sample_judgement,
    match_triples,
    preprocess_span,
    token_f1,
)


def test_preprocess_span_normalizes_articles_punctuation_case_and_spaces() -> None:
    assert preprocess_span("A super heavy rain.") == "super heavy rain"
    assert preprocess_span("The strike resumed on Tuesday.") == "strike resumed on tuesday"
    assert preprocess_span("  Multiple   spaces  ") == "multiple spaces"
    assert preprocess_span("An apple, the pear!") == "apple pear"


def test_token_f1_handles_exact_empty_different_and_partial_overlap() -> None:
    assert token_f1("heavy rain", "heavy rain") == pytest.approx(1.0)
    assert token_f1("", "heavy rain") == pytest.approx(0.0)
    assert token_f1("apple pie", "rocket science") == pytest.approx(0.0)
    assert token_f1("heavy rain caused flooding", "heavy rain") == pytest.approx(2 / 3)


def test_match_triples_uses_greedy_one_to_one_matching_and_threshold() -> None:
    pred_triples = [
        {
            "cause": {"span": "a heavy rain damage"},
            "relation": "caused",
            "effect": {"span": "the flooding"},
        },
        {
            "cause": {"span": "unrelated cause"},
            "relation": "caused",
            "effect": {"span": "unrelated effect"},
        },
    ]
    gold_relations = [{"cause": "heavy rain", "effect": "flooding"}]

    assert match_triples(pred_triples, gold_relations, threshold=0.8) == (1, 1, 0)
    assert match_triples(pred_triples, gold_relations, threshold=0.81) == (0, 2, 1)


def test_evaluator_reports_detection_and_two_extraction_views() -> None:
    evaluator = Evaluator()
    cases = [
        (
            {
                "id": 1,
                "has_causal": True,
                "triples": [
                    {
                        "cause": {"span": "heavy rain"},
                        "relation": "caused",
                        "effect": {"span": "flooding"},
                    }
                ],
            },
            {"id": 1, "has_causal": True, "relations": [{"cause": "heavy rain", "effect": "the flooding"}]},
        ),
        ({"id": 2, "has_causal": False, "triples": []}, {"id": 2, "has_causal": False, "relations": []}),
        (
            {"id": 3, "has_causal": False, "triples": []},
            {"id": 3, "has_causal": True, "relations": [{"cause": "stress", "effect": "ulcer"}]},
        ),
        (
            {
                "id": 4,
                "has_causal": True,
                "triples": [
                    {
                        "cause": {"span": "rumor"},
                        "relation": "caused",
                        "effect": {"span": "panic"},
                    }
                ],
            },
            {"id": 4, "has_causal": False, "relations": []},
        ),
        (
            {
                "id": 5,
                "has_causal": True,
                "triples": [
                    {
                        "cause": {"span": "fire"},
                        "relation": "caused",
                        "effect": {"span": "evacuation"},
                    },
                    {
                        "cause": {"span": "extra"},
                        "relation": "caused",
                        "effect": {"span": "noise"},
                    },
                ],
            },
            {
                "id": 5,
                "has_causal": True,
                "relations": [
                    {"cause": "the fire", "effect": "the evacuation"},
                    {"cause": "smoke", "effect": "alarm"},
                ],
            },
        ),
    ]

    for prediction, gold in cases:
        evaluator.update(prediction=prediction, gold=gold)

    report = evaluator.report()

    assert report["n_samples"] == 5
    assert report["n_causal_gold"] == 3
    assert report["n_causal_pred"] == 3
    assert report["detection"]["tp"] == 2
    assert report["detection"]["tn"] == 1
    assert report["detection"]["fp"] == 1
    assert report["detection"]["fn"] == 1
    assert report["detection"]["accuracy"] == pytest.approx(0.6)

    all_samples = report["extraction"]["all_samples"]
    assert all_samples["n_eval_samples"] == 5
    assert all_samples["n_gold_triples"] == 4
    assert all_samples["n_pred_triples"] == 4
    assert all_samples["tp"] == 2
    assert all_samples["fp"] == 2
    assert all_samples["fn"] == 2
    assert all_samples["f1"] == pytest.approx(0.5)

    detected_only = report["extraction"]["detected_only"]
    assert detected_only["n_eval_samples"] == 2
    assert detected_only["n_gold_triples"] == 3
    assert detected_only["n_pred_triples"] == 3
    assert detected_only["tp"] == 2
    assert detected_only["fp"] == 1
    assert detected_only["fn"] == 1
    assert detected_only["f1"] == pytest.approx(2 / 3)

    assert "original_like" not in report["extraction"]


def test_format_report_contains_progress_snapshot_fields() -> None:
    evaluator = Evaluator()
    evaluator.update(
        prediction={
            "id": 1,
            "has_causal": True,
            "triples": [{"cause": {"span": "rain"}, "relation": "caused", "effect": {"span": "flooding"}}],
        },
        gold={"id": 1, "has_causal": True, "relations": [{"cause": "rain", "effect": "flooding"}]},
    )

    formatted = evaluator.format_report(title="进度快照")

    assert "进度快照" in formatted
    assert "[Layer 1] Detection" in formatted
    assert "[Layer 2A] Extraction all_samples" in formatted
    assert "[Layer 2B] Extraction detected_only" in formatted
    assert "original_like" not in formatted


def test_build_sample_judgement_exposes_first_ten_debug_fields() -> None:
    judgement = build_sample_judgement(
        prediction={
            "id": 7,
            "has_causal": True,
            "triples": [
                {
                    "cause": {"span": "a heavy rain"},
                    "relation": "caused",
                    "effect": {"span": "serious street flooding"},
                }
            ],
        },
        gold={"id": 7, "text": "Heavy rain caused street flooding.", "has_causal": True, "relations": [
            {"cause": "heavy rain", "effect": "street flooding"}
        ]},
    )

    assert judgement["id"] == 7
    assert judgement["text"] == "Heavy rain caused street flooding."
    assert judgement["token_f1"]["counts"] == {"tp": 1, "fp": 0, "fn": 0}
    assert judgement["gold_relations"] == [{"cause": "heavy rain", "effect": "street flooding"}]
    assert judgement["pred_triples"][0]["cause"]["span"] == "a heavy rain"
