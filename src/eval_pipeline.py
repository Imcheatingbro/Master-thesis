"""SPEC_05：Demo1 evaluation 运行流程与报告落盘工具。"""

from __future__ import annotations

import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from src.evaluator import (
    VALID_EXTRACTION_METRICS,
    Evaluator,
    build_sample_judgement,
    primary_metric_for_dataset,
)
from src.generator import generate
from src.retriever import RetrieverProtocol, create_retriever


DEFAULT_REPORT_DETAIL_LIMIT = 200
DEFAULT_REPORT_DETAIL_MODE = "first"
REPORT_DETAIL_MODES = {"first", "errors"}


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
    max_workers: int = 1
    llm_provider: str | None = None
    llm_base_url: str | None = None
    context_length: int | None = None
    reasoning_effort: str | None = None
    llm_extra_body: dict[str, Any] | None = None
    api_key_source: str | None = None
    save_report: bool = False
    report_dir: Path | str = Path("results") / "eval_report"
    report_detail_limit: int | None = DEFAULT_REPORT_DETAIL_LIMIT
    report_detail_mode: str = DEFAULT_REPORT_DETAIL_MODE
    report_error_metric: str | None = None
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
            "max_workers": self.max_workers,
            "llm_provider": self.llm_provider,
            "llm_base_url": self.llm_base_url,
            "context_length": self.context_length,
            "reasoning_effort": self.reasoning_effort,
            "llm_extra_body": self.llm_extra_body,
            "api_key_source": self.api_key_source,
            "report_detail_limit": self.report_detail_limit,
            "report_detail_mode": self.report_detail_mode,
            "report_error_metric": self.report_error_metric,
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
    indexed_judgements: list[tuple[int, dict[str, Any]]] = []
    total = len(samples)

    for completed_count, sample_index, sample, prediction in _iter_predictions(
        samples=samples,
        label=label,
        client=client,
        retriever=eval_retriever,
        config=config,
        generator=generator,
        progress_factory=progress_factory,
    ):
        evaluator.update(prediction=prediction, gold=sample)
        judgement = build_sample_judgement(prediction=prediction, gold=sample, dataset=config.dataset)
        _attach_generation_error(judgement, prediction)
        _attach_parse_repair(judgement, prediction)
        indexed_judgements.append((sample_index, judgement))
        if emit is not None and config.progress_every > 0 and completed_count % config.progress_every == 0:
            emit("")
            emit(evaluator.format_report(title=f"{label} progress {completed_count}/{total}"))

    final_metrics_text = evaluator.format_report(title=f"{label} final report")
    sample_judgements = [judgement for _, judgement in sorted(indexed_judgements, key=lambda item: item[0])]
    if emit is not None:
        emit("")
        emit(final_metrics_text)
        emit(format_sample_judgements(sample_judgements[:10]))

    generation_failures = summarize_generation_failures(sample_judgements)
    parse_repairs = summarize_parse_repairs(sample_judgements)
    report = evaluator.report()
    report["sample_judgements"] = sample_judgements
    report["generation_failures"] = generation_failures
    report["parse_repairs"] = parse_repairs
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
            generation_failures=generation_failures,
            parse_repairs=parse_repairs,
            sample_detail_limit=config.report_detail_limit,
            sample_detail_mode=config.report_detail_mode,
            sample_detail_error_metric=config.report_error_metric,
            title=f"{label} eval report",
        )
        report["report_path"] = str(report_path)
        generation_failures_path = write_generation_failure_outputs(
            report_path=report_path,
            sample_judgements=sample_judgements,
        )
        if generation_failures_path is not None:
            report["generation_failures_path"] = str(generation_failures_path)
        parse_repairs_path = write_parse_repair_outputs(
            report_path=report_path,
            sample_judgements=sample_judgements,
        )
        if parse_repairs_path is not None:
            report["parse_repairs_path"] = str(parse_repairs_path)
        if emit is not None:
            emit(f"Eval report saved: {report_path}")
            if generation_failures_path is not None:
                emit(f"Generation failure outputs saved: {generation_failures_path}")
            if parse_repairs_path is not None:
                emit(f"Parse repair outputs saved: {parse_repairs_path}")
    return report


def _iter_predictions(
    samples: list[dict[str, Any]],
    label: str,
    client: Any,
    retriever: RetrieverProtocol | None,
    config: EvalRunConfig,
    generator: Callable[..., dict[str, Any]],
    progress_factory: Callable[..., Iterable[Any]] | None,
) -> Iterable[tuple[int, int, dict[str, Any], dict[str, Any]]]:
    worker_count = max(1, int(config.max_workers or 1))
    if worker_count == 1:
        iterator = _build_progress_iterator(samples, label, progress_factory)
        for completed_count, sample in enumerate(iterator, 1):
            sample_index = completed_count - 1
            prediction = _generate_prediction(
                sample=sample,
                client=client,
                retriever=retriever,
                config=config,
                generator=generator,
            )
            yield completed_count, sample_index, sample, prediction
        return

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = {
            executor.submit(
                _generate_prediction,
                sample=sample,
                client=client,
                retriever=retriever,
                config=config,
                generator=generator,
            ): (sample_index, sample)
            for sample_index, sample in enumerate(samples)
        }
        future_iterator = as_completed(futures)
        if progress_factory is not None:
            future_iterator = progress_factory(future_iterator, total=len(futures), desc=label)
        for completed_count, future in enumerate(future_iterator, 1):
            sample_index, sample = futures[future]
            prediction = future.result()
            yield completed_count, sample_index, sample, prediction


def _generate_prediction(
    sample: dict[str, Any],
    client: Any,
    retriever: RetrieverProtocol | None,
    config: EvalRunConfig,
    generator: Callable[..., dict[str, Any]],
) -> dict[str, Any]:
    try:
        return generator(
            text=sample["text"],
            sample_id=sample["id"],
            client=client,
            retriever=retriever,
            use_rag=config.use_rag,
            top_k=config.rag_top_k,
            rag_mode=config.rag_mode,
            prompt_name=config.prompt_name,
        )
    except Exception as exc:
        return {
            "id": sample.get("id"),
            "has_causal": False,
            "triples": [],
            "error_type": type(exc).__name__,
            "error_message": str(exc),
        }


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
    generation_failures: dict[str, Any] | None = None,
    parse_repairs: dict[str, Any] | None = None,
    sample_detail_limit: int | None = DEFAULT_REPORT_DETAIL_LIMIT,
    sample_detail_mode: str = DEFAULT_REPORT_DETAIL_MODE,
    sample_detail_error_metric: str | None = None,
) -> str:
    """生成包含统计指标和所选样本 gold/pred 对照的 Markdown 报告。"""
    failure_summary = generation_failures or {"total": 0, "by_type": {}, "samples": []}
    repair_summary = parse_repairs or {"total": 0, "by_type": {}, "samples": []}
    visible_sample_judgements, sample_detail_note = _select_report_sample_details(
        sample_judgements=sample_judgements,
        sample_detail_limit=sample_detail_limit,
        sample_detail_mode=sample_detail_mode,
        sample_detail_error_metric=sample_detail_error_metric,
    )
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
        "## 生成失败统计",
        "```json",
        json.dumps(failure_summary, indent=2, ensure_ascii=False),
        "```",
        "",
        "## 解析修复统计",
        "```json",
        json.dumps(repair_summary, indent=2, ensure_ascii=False),
        "```",
        "",
        "## 样本明细",
    ]
    if sample_detail_note is not None:
        lines.extend(["", sample_detail_note])
    for row in visible_sample_judgements:
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
    generation_failures: dict[str, Any] | None = None,
    parse_repairs: dict[str, Any] | None = None,
    sample_detail_limit: int | None = DEFAULT_REPORT_DETAIL_LIMIT,
    sample_detail_mode: str = DEFAULT_REPORT_DETAIL_MODE,
    sample_detail_error_metric: str | None = None,
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
            generation_failures=generation_failures,
            parse_repairs=parse_repairs,
            sample_detail_limit=sample_detail_limit,
            sample_detail_mode=sample_detail_mode,
            sample_detail_error_metric=sample_detail_error_metric,
        ),
        encoding="utf-8",
    )
    return report_path


def _select_report_sample_details(
    sample_judgements: list[dict[str, Any]],
    sample_detail_limit: int | None,
    sample_detail_mode: str,
    sample_detail_error_metric: str | None,
) -> tuple[list[dict[str, Any]], str | None]:
    """按原始顺序选择报告明细；errors 模式只保留主指标判错的样本。"""
    mode = str(sample_detail_mode or DEFAULT_REPORT_DETAIL_MODE).strip().lower()
    if mode not in REPORT_DETAIL_MODES:
        valid_modes = ", ".join(sorted(REPORT_DETAIL_MODES))
        raise ValueError(f"Unsupported sample_detail_mode={sample_detail_mode!r}; expected one of: {valid_modes}")

    if mode == "errors":
        error_metric = _validate_report_error_metric(sample_detail_error_metric)
        candidate_rows = [
            row
            for row in sample_judgements
            if _is_wrong_sample_judgement(row, error_metric=error_metric)
        ]
        total_wrong = len(candidate_rows)
        if sample_detail_limit is None:
            return (
                candidate_rows,
                f"Sample details shown: all {total_wrong} wrong samples "
                f"from {len(sample_judgements)} total samples.",
            )
        limit = max(0, int(sample_detail_limit))
        visible_rows = candidate_rows[:limit]
        if total_wrong > limit:
            note = (
                f"Sample details shown: first {limit} of {total_wrong} wrong samples "
                f"from {len(sample_judgements)} total samples."
            )
        else:
            note = (
                f"Sample details shown: all {total_wrong} wrong samples "
                f"from {len(sample_judgements)} total samples."
            )
        return visible_rows, note

    if sample_detail_limit is None:
        return sample_judgements, None
    limit = max(0, int(sample_detail_limit))
    if len(sample_judgements) > limit:
        return (
            sample_judgements[:limit],
            f"Sample details shown: first {limit} of {len(sample_judgements)}.",
        )
    return sample_judgements, None


def _is_wrong_sample_judgement(row: dict[str, Any], error_metric: str | None = None) -> bool:
    """判断样本是否在生成、因果判定或主抽取指标上出错。"""
    if row.get("generation_error_type"):
        return True
    if bool(row.get("gold_has_causal", False)) != bool(row.get("pred_has_causal", False)):
        return True

    metric = error_metric or str(row.get("primary_metric") or "strict_token_f1")
    metric_payload = row.get(metric, {})
    if not isinstance(metric_payload, dict):
        return True
    counts = metric_payload.get("counts", {})
    if not isinstance(counts, dict):
        return True
    return _nonzero_count(counts.get("fp")) or _nonzero_count(counts.get("fn"))


def _validate_report_error_metric(error_metric: str | None) -> str | None:
    if error_metric is None:
        return None
    metric = str(error_metric).strip().lower()
    if metric not in VALID_EXTRACTION_METRICS:
        valid_metrics = ", ".join(sorted(VALID_EXTRACTION_METRICS))
        raise ValueError(
            f"Unsupported sample_detail_error_metric={error_metric!r}; expected one of: {valid_metrics}"
        )
    return metric


def _nonzero_count(value: Any) -> bool:
    try:
        return int(value or 0) != 0
    except (TypeError, ValueError):
        return True


def write_generation_failure_outputs(
    report_path: Path | str,
    sample_judgements: list[dict[str, Any]],
) -> Path | None:
    """把最终兜底样本的逐次原始输出写入独立 JSONL 文件。"""
    failures: list[dict[str, Any]] = []
    for row in sample_judgements:
        error_type = row.get("generation_error_type")
        if not error_type:
            continue
        attempts = row.get("generation_attempts", [])
        failures.append(
            {
                "id": row.get("id"),
                "text": row.get("text", ""),
                "error_type": str(error_type),
                "error_message": str(row.get("generation_error_message", "")),
                "attempts": attempts if isinstance(attempts, list) else [],
            }
        )
    if not failures:
        return None

    markdown_path = Path(report_path)
    output_path = markdown_path.with_name(f"{markdown_path.stem}_generation_failures.jsonl")
    output_path.write_text(
        "".join(f"{json.dumps(row, ensure_ascii=False)}\n" for row in failures),
        encoding="utf-8",
    )
    return output_path


def write_parse_repair_outputs(
    report_path: Path | str,
    sample_judgements: list[dict[str, Any]],
) -> Path | None:
    """把自动修复成功样本的修复前原始输出写入独立 JSONL 文件。"""
    repairs: list[dict[str, Any]] = []
    for row in sample_judgements:
        repair_type = row.get("parse_repair_type")
        if not repair_type:
            continue
        repairs.append(
            {
                "id": row.get("id"),
                "text": row.get("text", ""),
                "repair_type": str(repair_type),
                "raw_output": str(row.get("parse_repair_raw_output", "")),
            }
        )
    if not repairs:
        return None

    markdown_path = Path(report_path)
    output_path = markdown_path.with_name(f"{markdown_path.stem}_parse_repairs.jsonl")
    output_path.write_text(
        "".join(f"{json.dumps(row, ensure_ascii=False)}\n" for row in repairs),
        encoding="utf-8",
    )
    return output_path


def summarize_generation_failures(sample_judgements: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总 generator 兜底时记录的失败类型。"""
    failures: list[dict[str, Any]] = []
    by_type: dict[str, int] = {}
    for row in sample_judgements:
        error_type = row.get("generation_error_type")
        if not error_type:
            continue
        error_key = str(error_type)
        by_type[error_key] = by_type.get(error_key, 0) + 1
        failures.append(
            {
                "id": row.get("id"),
                "error_type": error_key,
                "error_message": row.get("generation_error_message", ""),
            }
        )
    return {"total": len(failures), "by_type": by_type, "samples": failures}


def summarize_parse_repairs(sample_judgements: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总成功解析前应用的受限 JSON 修复。"""
    repairs: list[dict[str, Any]] = []
    by_type: dict[str, int] = {}
    for row in sample_judgements:
        repair_type = row.get("parse_repair_type")
        if not repair_type:
            continue
        repair_key = str(repair_type)
        by_type[repair_key] = by_type.get(repair_key, 0) + 1
        repairs.append({"id": row.get("id"), "repair_type": repair_key})
    return {"total": len(repairs), "by_type": by_type, "samples": repairs}


def load_sample_judgements_from_report(
    report_name: str | Path,
    report_dir: Path | str = Path("results") / "eval_report",
) -> list[dict[str, Any]]:
    """Load visible sample judgements from a saved Markdown eval report."""
    report_path = _resolve_eval_report_path(report_name=report_name, report_dir=report_dir)
    return load_sample_judgements_from_report_text(report_path.read_text(encoding="utf-8"))


def load_sample_judgements_from_report_text(report_text: str) -> list[dict[str, Any]]:
    """Parse sample details written by format_eval_report_text back into judgement rows."""
    rows: list[dict[str, Any]] = []
    report_primary_metric = _primary_metric_from_report_text(report_text)
    pattern = re.compile(
        r"### --- id=(?P<id>.*?) ---\s*\n\s*(?P<text_line>.*?)\s*\n\s*```json\s*\n"
        r"(?P<payload>\{.*?\})\s*\n```",
        re.DOTALL,
    )
    for match in pattern.finditer(report_text):
        payload = json.loads(match.group("payload"))
        text_line = match.group("text_line").strip()
        _, separator, text = text_line.partition(": ")
        rows.append(
            {
                "id": _parse_report_sample_id(match.group("id")),
                "text": text if separator else text_line,
                "gold_has_causal": bool(payload.get("gold_has_causal", False)),
                "pred_has_causal": bool(payload.get("pred_has_causal", False)),
                "gold_relations": payload.get("gold_relations", []),
                "pred_triples": payload.get("pred_triples", []),
                "primary_metric": report_primary_metric or payload.get("primary_metric", "strict_token_f1"),
                "strict_token_f1": {"counts": payload.get("strict_token_f1_counts", {})},
                "anchor_window": {"counts": payload.get("anchor_window_counts", {})},
                "token_f1": {"counts": payload.get("token_f1_counts", {})},
            }
        )
        if payload.get("generation_error_type"):
            rows[-1]["generation_error_type"] = payload.get("generation_error_type")
            rows[-1]["generation_error_message"] = payload.get("generation_error_message", "")
    return rows


def select_eval_diff_examples(
    sample_judgements: list[dict[str, Any]],
    layer: str = "detected_only",
    metric: str = "strict_token_f1",
    bucket: str = "fn",
    limit: int | None = 20,
) -> list[dict[str, Any]]:
    """Select sample-level TP/FP/FN examples for notebook diagnostics."""
    examples = _collect_eval_diff_examples(
        sample_judgements=sample_judgements,
        layer=layer,
        metric=metric,
        bucket=bucket,
    )
    if limit is None:
        return examples
    return examples[: max(0, int(limit))]


def format_eval_diff_examples(
    sample_judgements: list[dict[str, Any]],
    layer: str = "detected_only",
    metric: str = "strict_token_f1",
    bucket: str = "fn",
    limit: int | None = 20,
    title: str = "Eval diff examples",
) -> str:
    """Format sample-level gold-vs-pred examples for notebook inspection."""
    layer_key = _normalize_diff_layer(layer)
    metric_key = _normalize_diff_metric(metric)
    bucket_key = _normalize_diff_bucket(bucket)
    all_examples = _collect_eval_diff_examples(
        sample_judgements=sample_judgements,
        layer=layer_key,
        metric=metric_key,
        bucket=bucket_key,
    )
    visible_examples = all_examples if limit is None else all_examples[: max(0, int(limit))]
    lines = [
        f"================ {title} ================",
        f"Layer: {layer_key} | metric: {metric_key} | bucket: {bucket_key.upper()}",
        f"showing {len(visible_examples)} of {len(all_examples)} matching samples",
    ]
    if not visible_examples:
        lines.append("No matching samples.")
        return "\n".join(lines)

    for example in visible_examples:
        lines.extend(
            [
                "",
                f"--- id={example.get('id')} | {bucket_key.upper()} count={example.get('count', 0)} ---",
                f"text: {example.get('text', '')}",
                f"gold_has_causal={example.get('gold_has_causal', False)} | "
                f"pred_has_causal={example.get('pred_has_causal', False)}",
                f"{example.get('metric', metric_key)} counts: {example.get('counts', {})}",
                "gold_relations:",
                json.dumps(example.get("gold_relations", []), indent=2, ensure_ascii=False),
                "pred_triples:",
                json.dumps(example.get("pred_triples", []), indent=2, ensure_ascii=False),
            ]
        )
        if example.get("generation_error_type"):
            lines.extend(
                [
                    "generation_error:",
                    json.dumps(
                        {
                            "type": example.get("generation_error_type"),
                            "message": example.get("generation_error_message", ""),
                        },
                        indent=2,
                        ensure_ascii=False,
                    ),
                ]
            )
    return "\n".join(lines)


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


def select_detection_diff_examples(
    sample_judgements: list[dict[str, Any]],
    bucket: str = "fn",
    limit: int | None = 20,
) -> list[dict[str, Any]]:
    """Select sentence-level detection TP/TN/FP/FN examples."""
    examples = _collect_detection_diff_examples(sample_judgements=sample_judgements, bucket=bucket)
    if limit is None:
        return examples
    return examples[: max(0, int(limit))]


def format_detection_diff_examples(
    sample_judgements: list[dict[str, Any]],
    bucket: str = "fn",
    limit: int | None = 20,
    title: str = "Detection diff examples",
) -> str:
    """Format sentence-level detection examples for notebook inspection."""
    bucket_key = _normalize_detection_bucket(bucket)
    all_examples = _collect_detection_diff_examples(sample_judgements=sample_judgements, bucket=bucket_key)
    visible_examples = all_examples if limit is None else all_examples[: max(0, int(limit))]
    lines = [
        f"================ {title} ================",
        f"Layer: detection | bucket: {bucket_key.upper()}",
        f"showing {len(visible_examples)} of {len(all_examples)} matching samples",
    ]
    if not visible_examples:
        lines.append("No matching samples.")
        return "\n".join(lines)

    for example in visible_examples:
        lines.extend(
            [
                "",
                f"--- id={example.get('id')} | detection={bucket_key.upper()} ---",
                f"text: {example.get('text', '')}",
                f"gold_has_causal={example.get('gold_has_causal', False)} | "
                f"pred_has_causal={example.get('pred_has_causal', False)}",
                f"primary_metric: {example.get('primary_metric', 'strict_token_f1')}",
                f"strict_token_f1 counts: {example.get('strict_token_f1_counts', {})}",
                f"anchor_window counts: {example.get('anchor_window_counts', {})}",
                "gold_relations:",
                json.dumps(example.get("gold_relations", []), indent=2, ensure_ascii=False),
                "pred_triples:",
                json.dumps(example.get("pred_triples", []), indent=2, ensure_ascii=False),
            ]
        )
        if example.get("generation_error_type"):
            lines.extend(
                [
                    "generation_error:",
                    json.dumps(
                        {
                            "type": example.get("generation_error_type"),
                            "message": example.get("generation_error_message", ""),
                        },
                        indent=2,
                        ensure_ascii=False,
                    ),
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


def _attach_generation_error(judgement: dict[str, Any], prediction: dict[str, Any]) -> None:
    error_type = prediction.get("error_type")
    if not error_type:
        return
    judgement["generation_error_type"] = str(error_type)
    judgement["generation_error_message"] = str(prediction.get("error_message", ""))
    attempts = prediction.get("generation_attempts")
    if isinstance(attempts, list):
        judgement["generation_attempts"] = attempts


def _attach_parse_repair(judgement: dict[str, Any], prediction: dict[str, Any]) -> None:
    repair_type = prediction.get("parse_repair_type")
    if not repair_type:
        return
    judgement["parse_repair_type"] = str(repair_type)
    judgement["parse_repair_raw_output"] = str(prediction.get("parse_repair_raw_output", ""))


def _collect_eval_diff_examples(
    sample_judgements: list[dict[str, Any]],
    layer: str,
    metric: str,
    bucket: str,
) -> list[dict[str, Any]]:
    layer_key = _normalize_diff_layer(layer)
    metric_key = _normalize_diff_metric(metric)
    bucket_key = _normalize_diff_bucket(bucket)
    examples: list[dict[str, Any]] = []
    for row in sample_judgements:
        if layer_key == "detected_only" and not (
            bool(row.get("gold_has_causal", False)) and bool(row.get("pred_has_causal", False))
        ):
            continue
        row_metric = row.get("primary_metric", "strict_token_f1") if metric_key == "primary" else metric_key
        counts = row.get(str(row_metric), {}).get("counts", {})
        count = int(counts.get(bucket_key, 0) or 0)
        if count <= 0:
            continue
        examples.append(
            {
                "id": row.get("id"),
                "text": row.get("text", ""),
                "gold_has_causal": bool(row.get("gold_has_causal", False)),
                "pred_has_causal": bool(row.get("pred_has_causal", False)),
                "count": count,
                "counts": counts,
                "metric": str(row_metric),
                "gold_relations": row.get("gold_relations", []),
                "pred_triples": row.get("pred_triples", []),
                "generation_error_type": row.get("generation_error_type"),
                "generation_error_message": row.get("generation_error_message", ""),
            }
        )
    return examples


def _collect_detection_diff_examples(
    sample_judgements: list[dict[str, Any]],
    bucket: str,
) -> list[dict[str, Any]]:
    bucket_key = _normalize_detection_bucket(bucket)
    examples: list[dict[str, Any]] = []
    for row in sample_judgements:
        gold_has_causal = bool(row.get("gold_has_causal", False))
        pred_has_causal = bool(row.get("pred_has_causal", False))
        if _detection_bucket(gold_has_causal=gold_has_causal, pred_has_causal=pred_has_causal) != bucket_key:
            continue
        examples.append(
            {
                "id": row.get("id"),
                "text": row.get("text", ""),
                "gold_has_causal": gold_has_causal,
                "pred_has_causal": pred_has_causal,
                "primary_metric": row.get("primary_metric", "strict_token_f1"),
                "strict_token_f1_counts": row.get("strict_token_f1", {}).get("counts", {}),
                "anchor_window_counts": row.get("anchor_window", {}).get("counts", {}),
                "gold_relations": row.get("gold_relations", []),
                "pred_triples": row.get("pred_triples", []),
                "generation_error_type": row.get("generation_error_type"),
                "generation_error_message": row.get("generation_error_message", ""),
            }
        )
    return examples


def _detection_bucket(gold_has_causal: bool, pred_has_causal: bool) -> str:
    if gold_has_causal and pred_has_causal:
        return "tp"
    if not gold_has_causal and not pred_has_causal:
        return "tn"
    if not gold_has_causal and pred_has_causal:
        return "fp"
    return "fn"


def _normalize_diff_layer(layer: str) -> str:
    layer_key = str(layer).lower()
    if layer_key not in {"all_samples", "detected_only"}:
        raise ValueError("layer must be 'all_samples' or 'detected_only'")
    return layer_key


def _normalize_diff_metric(metric: str) -> str:
    metric_key = str(metric).lower()
    if metric_key not in {"strict_token_f1", "anchor_window", "token_f1", "primary"}:
        raise ValueError("metric must be 'strict_token_f1', 'anchor_window', 'token_f1', or 'primary'")
    return metric_key


def _normalize_diff_bucket(bucket: str) -> str:
    bucket_key = str(bucket).lower()
    if bucket_key not in {"tp", "fp", "fn"}:
        raise ValueError("bucket must be 'tp', 'fp', or 'fn'")
    return bucket_key


def _normalize_detection_bucket(bucket: str) -> str:
    bucket_key = str(bucket).lower()
    if bucket_key not in {"tp", "tn", "fp", "fn"}:
        raise ValueError("bucket must be 'tp', 'tn', 'fp', or 'fn'")
    return bucket_key


def _resolve_eval_report_path(report_name: str | Path, report_dir: Path | str) -> Path:
    raw_path = Path(report_name)
    candidates = [raw_path]
    if not str(raw_path).lower().endswith(".md"):
        candidates.append(Path(f"{raw_path}.md"))

    for candidate in candidates:
        paths_to_try = [candidate] if candidate.is_absolute() else [candidate, Path(report_dir) / candidate]
        for path in paths_to_try:
            if path.exists():
                return path
    fallback = Path(report_dir) / candidates[-1]
    raise FileNotFoundError(f"Eval report not found: {fallback}")


def _parse_report_sample_id(raw_id: str) -> int | str:
    value = raw_id.strip()
    try:
        return int(value)
    except ValueError:
        return value


def _primary_metric_from_report_text(report_text: str) -> str | None:
    config_match = re.search(r"```json\s*\n(?P<config>\{.*?\})\s*\n```", report_text, re.DOTALL)
    if config_match is None:
        return None
    try:
        config = json.loads(config_match.group("config"))
    except json.JSONDecodeError:
        return None
    dataset = config.get("dataset") if isinstance(config, dict) else None
    if not dataset:
        return None
    return primary_metric_for_dataset(str(dataset))


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
    if row.get("generation_error_type"):
        payload["generation_error_type"] = row.get("generation_error_type")
        payload["generation_error_message"] = row.get("generation_error_message", "")
    if row.get("parse_repair_type"):
        payload["parse_repair_type"] = row.get("parse_repair_type")
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
