"""SPEC_05：Demo1 evaluation 运行流程与报告落盘工具。"""

from __future__ import annotations

import json
import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from src.evaluator import Evaluator, build_sample_judgement
from src.generator import generate
from src.retriever import RetrieverProtocol, create_retriever


@dataclass(frozen=True)
class EvalRunConfig:
    """保存一次 notebook eval 运行所需的非交互配置。"""

    project_root: Path | str
    model: str
    dataset: str
    prompt_name: str
    use_rag: bool
    rag_mode: str
    rag_top_k: int
    temperature: float
    max_tokens: int
    progress_every: int = 50
    save_report: bool = False
    report_dir: Path | str = Path("results") / "eval_report"
    metadata_path: Path | str | None = None
    embeddings_path: Path | str | None = None

    @property
    def report_output_dir(self) -> Path:
        """返回报告输出目录，支持相对项目根目录的路径。"""
        output_dir = Path(self.report_dir)
        if output_dir.is_absolute():
            return output_dir
        return Path(self.project_root) / output_dir

    def to_report_config(self, sample_count: int, label: str) -> dict[str, Any]:
        """生成可写入 Markdown 报告的 JSON 配置块。"""
        return {
            "label": label,
            "model": self.model,
            "dataset": self.dataset,
            "sample_count": sample_count,
            "prompt_name": self.prompt_name,
            "use_rag": self.use_rag,
            "rag_mode": self.rag_mode,
            "rag_top_k": self.rag_top_k,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "progress_every": self.progress_every,
            "metadata_path": str(self.metadata_path) if self.metadata_path is not None else None,
            "embeddings_path": str(self.embeddings_path) if self.embeddings_path is not None else None,
        }


def run_stream_eval(
    samples: list[dict[str, Any]],
    label: str,
    client: Any,
    config: EvalRunConfig,
    existing_retriever: RetrieverProtocol | None = None,
    generator: Callable[..., dict[str, Any]] = generate,
    progress_factory: Callable[..., Iterable[dict[str, Any]]] | None = None,
    emit: Callable[[str], None] | None = None,
    generated_at: datetime | None = None,
) -> dict[str, Any]:
    """流式运行 eval，按需输出进度快照并保存完整 Markdown 报告。"""
    evaluator = Evaluator(dataset=config.dataset)
    eval_retriever = _get_eval_retriever(config, existing_retriever)
    sample_judgements: list[dict[str, Any]] = []
    total = len(samples)
    iterator = _build_progress_iterator(samples, label, progress_factory)

    for index, sample in enumerate(iterator, 1):
        prediction = generator(
            text=sample["text"],
            sample_id=sample["id"],
            client=client,
            retriever=eval_retriever,
            use_rag=config.use_rag,
            top_k=config.rag_top_k,
            rag_mode=config.rag_mode,
            prompt_name=config.prompt_name,
        )
        evaluator.update(prediction=prediction, gold=sample)
        sample_judgements.append(build_sample_judgement(prediction=prediction, gold=sample, dataset=config.dataset))
        if emit is not None and config.progress_every > 0 and index % config.progress_every == 0:
            emit("")
            emit(evaluator.format_report(title=f"{label} progress {index}/{total}"))

    final_metrics_text = evaluator.format_report(title=f"{label} final report")
    if emit is not None:
        emit("")
        emit(final_metrics_text)
        emit(format_sample_judgements(sample_judgements[:10]))

    report = evaluator.report()
    if config.save_report:
        report_path = write_eval_report(
            output_dir=config.report_output_dir,
            model=config.model,
            dataset=config.dataset,
            sample_count=total,
            prompt_name=config.prompt_name,
            use_rag=config.use_rag,
            rag_mode=config.rag_mode,
            top_k=config.rag_top_k,
            generated_at=generated_at or datetime.now(),
            metrics_text=final_metrics_text,
            sample_judgements=sample_judgements,
            config=config.to_report_config(total, label),
            title=f"{label} eval report",
        )
        report["report_path"] = str(report_path)
        if emit is not None:
            emit(f"Eval report saved: {report_path}")
    return report


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


def format_sample_judgements(records: list[dict[str, Any]], title: str = "前 10 条样本判定") -> str:
    """把若干条样本判定格式化成 notebook 可直接展示的文本。"""
    lines = [f"================ {title} ================"]
    for row in records:
        lines.extend(
            [
                "",
                f"--- id={row.get('id')} ---",
                f"text: {row.get('text', '')}",
                f"gold_has_causal={row.get('gold_has_causal', False)} | "
                f"pred_has_causal={row.get('pred_has_causal', False)}",
                f"token_f1 counts: {row.get('token_f1', {}).get('counts', {})}",
                f"primary_metric: {row.get('primary_metric', 'strict_token_f1')}",
                f"strict_token_f1 counts: {row.get('strict_token_f1', {}).get('counts', {})}",
                f"anchor_window counts: {row.get('anchor_window', {}).get('counts', {})}",
                "gold_relations:",
                json.dumps(row.get("gold_relations", []), indent=2, ensure_ascii=False),
                "pred_triples:",
                json.dumps(row.get("pred_triples", []), indent=2, ensure_ascii=False),
            ]
        )
    return "\n".join(lines)


def _get_eval_retriever(
    config: EvalRunConfig,
    existing_retriever: RetrieverProtocol | None,
) -> RetrieverProtocol | None:
    if not config.use_rag:
        return None
    if existing_retriever is not None:
        return existing_retriever

    kwargs: dict[str, Path | str] = {}
    if config.metadata_path is not None:
        kwargs["metadata_path"] = config.metadata_path
    if config.embeddings_path is not None:
        kwargs["embeddings_path"] = config.embeddings_path
    return create_retriever(config.rag_mode, **kwargs)


def _build_progress_iterator(
    samples: list[dict[str, Any]],
    label: str,
    progress_factory: Callable[..., Iterable[dict[str, Any]]] | None,
) -> Iterable[dict[str, Any]]:
    if progress_factory is None:
        return samples
    return progress_factory(samples, total=len(samples), desc=label)


def _safe_filename_part(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    return normalized.strip("-._") or "unknown"


def _format_sample_judgement(row: dict[str, Any]) -> list[str]:
    payload = {
        "gold_has_causal": row.get("gold_has_causal", False),
        "pred_has_causal": row.get("pred_has_causal", False),
        "primary_metric": row.get("primary_metric", "strict_token_f1"),
        "strict_token_f1_counts": row.get("strict_token_f1", {}).get("counts", {}),
        "anchor_window_counts": row.get("anchor_window", {}).get("counts", {}),
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
