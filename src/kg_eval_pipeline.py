"""KG construction evaluation 的批量运行编排。"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.data_io import load_dataset
from src.kg_evaluator import (
    DEFAULT_DEEPSEEK_MODEL,
    DeepSeekJudgeClient,
    aggregate_sample_results,
    build_judge_prompt,
    compute_span_metrics,
    flatten_judge_units,
    load_gold_span_records,
    run_eval_extraction,
    run_parallel_judge,
    save_eval_checkpoint,
    save_eval_outputs,
    validate_extraction,
)


@dataclass
class KGEvalConfig:
    """一次 KG construction evaluation 的配置。"""

    dataset: str
    event_prompt_version: str
    sample_n: int | None = 20
    max_spans: int | None = None
    schema: str = "auto"
    max_depth: str | int | None = "auto"
    extraction_retry_times: int = 1
    checkpoint_every: int = 100
    output_dir: Path | str = Path("results/kg_evaluation")
    run_judge: bool = True
    judge_prompt_version: str = "v1"
    judge_api_key_path: Path | str = Path("deepseek_api.txt")
    judge_model: str = DEFAULT_DEEPSEEK_MODEL
    judge_max_tokens: int = 2048
    judge_timeout: float = 60.0
    judge_max_workers: int = 5
    judge_retry_times: int = 3
    judge_retry_base_seconds: float = 2.0
    save_outputs: bool = True


@dataclass
class KGEvalResult:
    """KG construction evaluation 的完整返回结果。"""

    span_results: list[dict[str, Any]]
    sample_results: list[dict[str, Any]]
    method_metrics: dict[str, Any]
    output_paths: dict[str, Path] = field(default_factory=dict)
    checkpoint_paths: list[Path] = field(default_factory=list)
    eval_schema: str = ""
    eval_max_depth: int | None = None


def resolve_eval_schema(prompt_version: str, schema: str) -> str:
    """根据 prompt version 推断评估 schema。"""
    if schema != "auto":
        return schema
    return "nested" if "nested" in prompt_version else "two_layer"


def resolve_eval_max_depth(prompt_version: str, schema: str, max_depth: str | int | None) -> int | None:
    """根据 prompt version 和 schema 推断最大深度约束。"""
    if max_depth != "auto":
        return max_depth
    if schema == "two_layer":
        return 1
    if "depth3" in prompt_version:
        return 3
    return None


def run_kg_evaluation(
    config: KGEvalConfig,
    construction_client: Any,
    samples: list[dict[str, Any]] | None = None,
    judge_client: Any | None = None,
    progress_factory: Any | None = None,
) -> KGEvalResult:
    """运行一次完整 KG construction evaluation。"""
    eval_schema = resolve_eval_schema(config.event_prompt_version, config.schema)
    eval_max_depth = resolve_eval_max_depth(config.event_prompt_version, eval_schema, config.max_depth)
    eval_samples = samples if samples is not None else load_dataset(config.dataset)
    eval_span_records = load_gold_span_records(
        eval_samples,
        dataset=config.dataset,
        sample_n=config.sample_n,
        max_spans=config.max_spans,
    )

    records_by_sample: dict[Any, list[dict[str, Any]]] = defaultdict(list)
    for record in eval_span_records:
        records_by_sample[record["sample_id"]].append(record)

    active_judge_client = judge_client
    if config.run_judge and active_judge_client is None:
        active_judge_client = DeepSeekJudgeClient(
            api_key_path=config.judge_api_key_path,
            model=config.judge_model,
            max_tokens=config.judge_max_tokens,
            timeout=config.judge_timeout,
            retry_times=config.judge_retry_times,
            retry_base_seconds=config.judge_retry_base_seconds,
        )

    span_results: list[dict[str, Any]] = []
    checkpoint_paths: list[Path] = []
    sample_items = records_by_sample.items()
    sample_iterable = _progress_iter(
        sample_items,
        progress_factory=progress_factory,
        total=len(records_by_sample),
        desc="KG eval samples",
    )

    processed_samples = 0
    for sample_id, records in sample_iterable:
        processed_samples += 1
        for span_record in records:
            span_result = _prepare_span_result(
                span_record=span_record,
                construction_client=construction_client,
                prompt_version=config.event_prompt_version,
                extraction_retry_times=config.extraction_retry_times,
                eval_schema=eval_schema,
                eval_max_depth=eval_max_depth,
                judge_prompt_version=config.judge_prompt_version,
            )
            span_results.append(span_result)

        if config.checkpoint_every and processed_samples % config.checkpoint_every == 0:
            checkpoint_paths.append(
                save_eval_checkpoint(
                    span_results,
                    output_dir=config.output_dir,
                    dataset=config.dataset,
                    prompt_version=config.event_prompt_version,
                    processed_samples=processed_samples,
                )
            )

    if config.run_judge and active_judge_client is not None:
        judge_progress = _progress_bar(progress_factory, total=len(span_results), desc="DeepSeek judge spans")
        try:
            span_results = run_parallel_judge(
                span_results,
                active_judge_client,
                max_workers=config.judge_max_workers,
                progress_callback=(lambda _result: judge_progress.update(1)) if judge_progress is not None else None,
            )
        finally:
            if judge_progress is not None:
                judge_progress.close()

    sample_results, method_metrics = aggregate_sample_results(span_results)
    output_paths: dict[str, Path] = {}
    if config.save_outputs:
        output_paths = save_eval_outputs(
            span_results,
            sample_results,
            method_metrics,
            output_dir=config.output_dir,
            dataset=config.dataset,
            prompt_version=config.event_prompt_version,
            sample_n=config.sample_n,
        )

    return KGEvalResult(
        span_results=span_results,
        sample_results=sample_results,
        method_metrics=method_metrics,
        output_paths=output_paths,
        checkpoint_paths=checkpoint_paths,
        eval_schema=eval_schema,
        eval_max_depth=eval_max_depth,
    )


def _prepare_span_result(
    span_record: dict[str, Any],
    construction_client: Any,
    prompt_version: str,
    extraction_retry_times: int,
    eval_schema: str,
    eval_max_depth: int | None,
    judge_prompt_version: str,
) -> dict[str, Any]:
    span_result = run_eval_extraction(
        span_record,
        client=construction_client,
        prompt_version=prompt_version,
        max_retry=extraction_retry_times,
    )
    validation = validate_extraction(
        span_result.get("parsed_extraction"),
        span=str(span_result.get("span", "")),
        schema=eval_schema,
        max_depth=eval_max_depth,
    )
    judge_units = flatten_judge_units(
        span_result.get("parsed_extraction") or {"components": []},
        graph_event_id=str(span_result.get("graph_event_id") or ""),
    )
    judge_prompt = build_judge_prompt(
        span=str(span_result.get("span", "")),
        units=judge_units,
        judge_span_id="s0",
        prompt_version=judge_prompt_version,
    )
    span_result.update(
        {
            "validation": validation,
            "judge_units": judge_units,
            "judge_prompt": judge_prompt,
            "raw_judge_output": "",
            "judge_result": None,
            "judge_error": None,
            "span_metrics": compute_span_metrics(validation, judge_units, None),
        }
    )
    return span_result


def _progress_iter(iterable: Any, progress_factory: Any | None, total: int, desc: str) -> Any:
    if progress_factory is None:
        return iterable
    return progress_factory(iterable, total=total, desc=desc)


def _progress_bar(progress_factory: Any | None, total: int, desc: str) -> Any | None:
    if progress_factory is None:
        return None
    return progress_factory(total=total, desc=desc)
