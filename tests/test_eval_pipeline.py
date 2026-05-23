"""SPEC_05：eval 运行流程与报告落盘 helper 的单元测试。"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from src.eval_pipeline import (
    EvalRunConfig,
    build_eval_report_filename,
    format_eval_report_text,
    run_stream_eval,
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
                "token_f1": {"counts": {"tp": 1, "fp": 0, "fn": 0}},
            },
            {
                "id": 2,
                "text": "No relation.",
                "gold_has_causal": False,
                "pred_has_causal": False,
                "gold_relations": [],
                "pred_triples": [],
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
    assert report_path.name == "qwen-qwen3-14b_cnc-n2_prompt-v2_rag-off_20260524-110000.md"
    assert "--- id=1 ---" in report_text
    assert any("前 10 条样本判定" in message for message in emitted)


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
