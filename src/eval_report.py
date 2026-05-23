"""SPEC_05：Demo1 evaluation 报告落盘工具。"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


def build_eval_report_filename(
    model: str,
    dataset: str,
    sample_count: int,
    prompt_name: str,
    use_rag: bool,
    rag_mode: str,
    top_k: int,
    generated_at: datetime,
) -> str:
    """按模型、数据集、样本数、prompt、RAG 配置和时间生成报告文件名。"""
    rag_part = f"rag-{rag_mode}-k{top_k}" if use_rag else "rag-off"
    parts = [
        _safe_filename_part(model),
        f"{_safe_filename_part(dataset)}-n{sample_count}",
        f"prompt-{_safe_filename_part(prompt_name)}",
        _safe_filename_part(rag_part),
        generated_at.strftime("%Y%m%d-%H%M%S"),
    ]
    return "_".join(parts) + ".md"


def format_eval_report_text(
    title: str,
    metrics_text: str,
    sample_judgements: list[dict[str, Any]],
    config: dict[str, Any],
) -> str:
    """生成包含统计指标和全部样本 gold/pred 对照的 Markdown 报告。"""
    lines = [
        f"# {title}",
        "",
        "## 配置",
        "```json",
        json.dumps(config, indent=2, ensure_ascii=False),
        "```",
        "",
        "## 统计指标",
        "```text",
        metrics_text,
        "```",
        "",
        "## 样本明细",
    ]
    for row in sample_judgements:
        lines.extend(_format_sample_judgement(row))
    return "\n".join(lines) + "\n"


def write_eval_report(
    output_dir: Path | str,
    model: str,
    dataset: str,
    sample_count: int,
    prompt_name: str,
    use_rag: bool,
    rag_mode: str,
    top_k: int,
    generated_at: datetime,
    metrics_text: str,
    sample_judgements: list[dict[str, Any]],
    config: dict[str, Any],
    title: str | None = None,
) -> Path:
    """写入 eval Markdown 报告并返回路径。"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    filename = build_eval_report_filename(
        model=model,
        dataset=dataset,
        sample_count=sample_count,
        prompt_name=prompt_name,
        use_rag=use_rag,
        rag_mode=rag_mode,
        top_k=top_k,
        generated_at=generated_at,
    )
    report_path = output_path / filename
    report_path.write_text(
        format_eval_report_text(
            title=title or f"{dataset} first {sample_count} eval report",
            metrics_text=metrics_text,
            sample_judgements=sample_judgements,
            config=config,
        ),
        encoding="utf-8",
    )
    return report_path


def _safe_filename_part(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    return normalized.strip("-._") or "unknown"


def _format_sample_judgement(row: dict[str, Any]) -> list[str]:
    payload = {
        "gold_has_causal": row.get("gold_has_causal", False),
        "pred_has_causal": row.get("pred_has_causal", False),
        "token_f1_counts": row.get("token_f1", {}).get("counts", {}),
        "gold_relations": row.get("gold_relations", []),
        "pred_triples": row.get("pred_triples", []),
    }
    return [
        "",
        f"### --- id={row.get('id')} ---",
        "",
        f"输入文本: {row.get('text', '')}",
        "",
        "```json",
        json.dumps(payload, indent=2, ensure_ascii=False),
        "```",
    ]
