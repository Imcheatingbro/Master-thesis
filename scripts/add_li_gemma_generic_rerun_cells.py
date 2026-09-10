"""Append two Gemma generic-RAG rerun sections to the Li batch notebook."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "lmstudio_batch_li_test.ipynb"
CELL_IDS = {
    "li-gemma-generic-rerun-note",
    "li-gemma-generic-rerun-config",
    "li-gemma-generic-rerun-helpers",
    "run-li-gemma-generic-rerun",
}


def _source(value: str) -> list[str]:
    return dedent(value).strip("\n").splitlines(keepends=True)


def _markdown(cell_id: str, value: str) -> dict[str, Any]:
    return {
        "cell_type": "markdown",
        "id": cell_id,
        "metadata": {},
        "source": _source(value),
    }


def _code(cell_id: str, value: str) -> dict[str, Any]:
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": cell_id,
        "metadata": {},
        "outputs": [],
        "source": _source(value),
    }


def build_cells() -> list[dict[str, Any]]:
    return [
        _markdown(
            "li-gemma-generic-rerun-note",
            r"""
            ## 阶段 4：Gemma × Li × 正确 original generic database 补跑

            旧阶段 2/3 的 Gemma RAG 报告使用了 CNC train-only support，它们作为跨数据集迁移记录保留，
            不覆盖、不冒充本次正式结果。本阶段只补跑 Gemma 4 26B A4B QAT 与 Gemma 4 31B QAT：

            - Li 全部 786 条；Prompt `v10.2`；
            - original generic Pattern/BGE database；`KNN+Pattern k=1`（1 KNN + 1 Pattern）；
            - `temperature=0`、`context=8192`、`max_tokens=2048`、`cache_prompt=False`；
            - 每 500 条常规卸载并重新加载模型；逐样本 checkpoint；
            - 若出现跑满长度的循环输出，不保存该失败，卸载模型后从同一 sample 重试。

            这一阶段独立初始化所需对象。只需依次运行下面三个代码格，不需要重新运行旧阶段。
            """,
        ),
        _code(
            "li-gemma-generic-rerun-config",
            r"""
            # ===== 阶段 4 配置与预检：两款 Gemma + Li original generic RAG =====
            import hashlib
            import json
            import logging
            import re
            import sys
            from collections.abc import Iterable, Iterator
            from html import escape
            from pathlib import Path
            from typing import Any

            import pandas as pd
            from IPython.display import HTML, display

            PROJECT_ROOT = Path.cwd()
            if PROJECT_ROOT.name == 'notebooks':
                PROJECT_ROOT = PROJECT_ROOT.parent
            if str(PROJECT_ROOT) not in sys.path:
                sys.path.insert(0, str(PROJECT_ROOT))
            if 'master_thesis' not in sys.executable.lower():
                raise RuntimeError('请切换到 Master_thesis kernel，重启 kernel 后重新运行阶段 4。')

            from src.data_io import load_dataset
            from src.eval_pipeline import EvalRunConfig, FatalGenerationError, run_stream_eval
            from src.generator import generate
            from src.llm_client import LLMClient
            from src.prediction_checkpoint import PredictionCheckpoint
            from src.prompt_builder import load_prompt_template
            from src.retriever import (
                ExactCountHybridRetriever,
                KNNRetriever,
                PatternRetriever,
                resolve_rag_cache_paths,
            )

            logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
            LI_GENERIC_LOGGER = logging.getLogger('li_gemma_generic_rag_k1_rerun')
            logging.getLogger('src.llm_client').setLevel(logging.WARNING)
            LI_GENERIC_PROGRESS_HANDLES: dict[str, Any] = {}


            def _li_generic_progress(
                iterable: Iterable[Any],
                *,
                total: int,
                desc: str,
                initial: int = 0,
                progress_key: str | None = None,
            ) -> Iterator[Any]:
                safe_desc = escape(desc)
                safe_total = max(total, 1)
                safe_initial = min(max(int(initial), 0), safe_total)

                def render(completed: int) -> HTML:
                    percent = min(completed / safe_total * 100, 100.0)
                    return HTML(
                        f"<div style='width:100%'><div>{safe_desc}: {completed}/{total} "
                        f"({percent:.1f}%)</div><progress value='{completed}' max='{safe_total}' "
                        f"style='width:100%;height:18px'></progress></div>"
                    )

                handle = LI_GENERIC_PROGRESS_HANDLES.get(progress_key or '')
                if handle is None:
                    handle = display(render(safe_initial), display_id=True)
                    if progress_key and handle is not None:
                        LI_GENERIC_PROGRESS_HANDLES[progress_key] = handle
                elif handle is not None:
                    handle.update(render(safe_initial))
                for completed, item in enumerate(iterable, safe_initial + 1):
                    yield item
                    if handle is not None:
                        handle.update(render(completed))


            LI_GENERIC_BASE_URL = 'http://127.0.0.1:1234/v1'
            LI_GENERIC_API_KEY = 'lm-studio'
            LI_GENERIC_MODEL_LOAD_TIMEOUT = 1200
            LI_GENERIC_LLM_TIMEOUT = 600
            LI_GENERIC_RETRY_TIMES = 3
            LI_GENERIC_CONTEXT_LENGTH = 8192
            LI_GENERIC_MAX_TOKENS = 2048
            LI_GENERIC_TEMPERATURE = 0.0
            LI_GENERIC_CACHE_PROMPT = False
            LI_GENERIC_RELOAD_EVERY = 500
            LI_GENERIC_MAX_LOOP_RELOADS = 3
            LI_GENERIC_PRIMARY_METRIC = 'anchor_window'
            RUN_LI_GEMMA_GENERIC_RAG_RERUN = True

            LI_GENERIC_REPORT_DIR = (
                Path('results') / 'eval_report' / 'lmstudio_batch_li'
                / 'gemma_generic_rag_k1_rerun'
            )
            LI_GENERIC_CHECKPOINT_DIR = (
                Path('results') / 'eval_checkpoints' / 'lmstudio_batch_li'
                / 'gemma_generic_rag_k1_rerun'
            )
            LI_GENERIC_SUMMARY_PATH = (
                PROJECT_ROOT / LI_GENERIC_REPORT_DIR
                / 'li_gemma_generic_rag_k1_rerun_summary.csv'
            )

            LI_GEMMA_GENERIC_RUNS: list[dict[str, Any]] = [
                {
                    'run_id': 'li_gemma26_generic_rag_k1',
                    'display_name': 'Gemma 4 26B A4B QAT',
                    'model_key': 'google/gemma-4-26b-a4b-qat',
                    'prompt_name': 'v10.2',
                    'use_rag': True,
                    'rag_database': 'generic',
                    'rag_mode': 'knn_pattern',
                    'rag_top_k': 1,
                },
                {
                    'run_id': 'li_gemma31_generic_rag_k1',
                    'display_name': 'Gemma 4 31B QAT',
                    'model_key': 'google/gemma-4-31b-qat',
                    'prompt_name': 'v10.2',
                    'use_rag': True,
                    'rag_database': 'generic',
                    'rag_mode': 'knn_pattern',
                    'rag_top_k': 1,
                },
            ]

            LI_GENERIC_SAMPLES = load_dataset('li')
            li_generic_stats = {
                'samples': len(LI_GENERIC_SAMPLES),
                'positive': sum(bool(sample['has_causal']) for sample in LI_GENERIC_SAMPLES),
                'negative': sum(not bool(sample['has_causal']) for sample in LI_GENERIC_SAMPLES),
                'relations': sum(len(sample.get('relations', [])) for sample in LI_GENERIC_SAMPLES),
                'max_relations': max(len(sample.get('relations', [])) for sample in LI_GENERIC_SAMPLES),
            }
            expected_li_generic_stats = {
                'samples': 786, 'positive': 191, 'negative': 595,
                'relations': 296, 'max_relations': 12,
            }
            if li_generic_stats != expected_li_generic_stats:
                raise RuntimeError(
                    f'Li 数据漂移：{li_generic_stats} != {expected_li_generic_stats}'
                )
            if len({str(sample['id']) for sample in LI_GENERIC_SAMPLES}) != 786:
                raise RuntimeError('Li sample id 不唯一。')

            LI_GENERIC_METADATA_PATH, LI_GENERIC_EMBEDDINGS_PATH = resolve_rag_cache_paths('generic')
            if (
                LI_GENERIC_METADATA_PATH.name != 'bge-small-en-v1.5_examples.jsonl'
                or LI_GENERIC_EMBEDDINGS_PATH.name != 'bge-small-en-v1.5_embeddings.npy'
            ):
                raise RuntimeError('generic database 没有解析到原始 Pattern/BGE cache。')
            if not LI_GENERIC_METADATA_PATH.is_file() or not LI_GENERIC_EMBEDDINGS_PATH.is_file():
                raise FileNotFoundError('Li original generic RAG cache 不完整。')


            def _li_generic_normalize_text(value: Any) -> str:
                without_tags = re.sub(
                    r'</?(?:cause|effect)>', '', str(value or ''), flags=re.IGNORECASE,
                )
                return ' '.join(without_tags.casefold().split())


            li_generic_support_rows = [
                json.loads(line)
                for line in LI_GENERIC_METADATA_PATH.read_text(encoding='utf-8').splitlines()
                if line.strip()
            ]
            li_generic_support_texts = {
                _li_generic_normalize_text(row.get('sentence', ''))
                for row in li_generic_support_rows
            }
            li_generic_eval_texts = {
                _li_generic_normalize_text(sample['text']) for sample in LI_GENERIC_SAMPLES
            }
            LI_GENERIC_TEXT_OVERLAP = li_generic_support_texts & li_generic_eval_texts
            if LI_GENERIC_TEXT_OVERLAP:
                raise RuntimeError(
                    f'Li 与 original generic database 存在文本泄漏：'
                    f'{len(LI_GENERIC_TEXT_OVERLAP)} 条。'
                )

            li_generic_prompt = load_prompt_template('v10.2')
            if li_generic_prompt.count('{rag_examples}') != 1:
                raise RuntimeError('v10.2 必须恰好包含一个 RAG 插槽。')
            if li_generic_prompt.count('\nInput:\n') != 10:
                raise RuntimeError('v10.2 必须保留 10 个 fixed examples。')

            LI_GENERIC_MANAGER = LLMClient(
                provider='lmstudio',
                base_url=LI_GENERIC_BASE_URL,
                model=LI_GEMMA_GENERIC_RUNS[0]['model_key'],
                api_key=LI_GENERIC_API_KEY,
                temperature=LI_GENERIC_TEMPERATURE,
                max_tokens=LI_GENERIC_MAX_TOKENS,
                context_length=LI_GENERIC_CONTEXT_LENGTH,
                reasoning='off',
                timeout=LI_GENERIC_MODEL_LOAD_TIMEOUT,
                retry_times=LI_GENERIC_RETRY_TIMES,
            )
            li_generic_inventory = {
                str(item['key']): item
                for item in LI_GENERIC_MANAGER.list_local_models()
                if item.get('key')
            }
            li_generic_missing_models = [
                run['model_key'] for run in LI_GEMMA_GENERIC_RUNS
                if run['model_key'] not in li_generic_inventory
            ]
            if li_generic_missing_models:
                raise RuntimeError(f'LM Studio 缺少 Gemma 模型：{li_generic_missing_models}')
            for run in LI_GEMMA_GENERIC_RUNS:
                reasoning = li_generic_inventory[run['model_key']].get(
                    'capabilities', {}
                ).get('reasoning', {})
                allowed = reasoning.get('allowed_options', [])
                if allowed and 'off' not in allowed:
                    raise RuntimeError(f"{run['model_key']} 不支持 reasoning=off。")

            LI_GENERIC_RETRIEVER = ExactCountHybridRetriever(
                pattern_retriever=PatternRetriever(metadata_path=LI_GENERIC_METADATA_PATH),
                knn_retriever=KNNRetriever(
                    metadata_path=LI_GENERIC_METADATA_PATH,
                    embeddings_path=LI_GENERIC_EMBEDDINGS_PATH,
                    device='cpu',
                ),
            )
            li_generic_probe = LI_GENERIC_RETRIEVER.retrieve(
                'Heavy rain caused flooding in the region.', top_k=1,
            )
            if len(li_generic_probe) != 2:
                raise RuntimeError('Li generic KNN+Pattern k=1 必须严格返回 2 条动态示例。')

            display(pd.DataFrame([li_generic_stats]))
            display(pd.DataFrame(LI_GEMMA_GENERIC_RUNS))
            display(pd.DataFrame([{
                'database': 'generic',
                'metadata': str(LI_GENERIC_METADATA_PATH),
                'embeddings': str(LI_GENERIC_EMBEDDINGS_PATH),
                'support_examples': len(li_generic_support_rows),
                'li_text_overlap': len(LI_GENERIC_TEXT_OVERLAP),
                'rag_mode': 'knn_pattern',
                'k': 1,
                'dynamic_examples': len(li_generic_probe),
            }]))
            LI_GENERIC_LOGGER.info('阶段 4 预检通过：2 Gemma runs，generic KNN+Pattern k=1。')
            """,
        ),
        _code(
            "li-gemma-generic-rerun-helpers",
            r"""
            # ===== 阶段 4：checkpoint、每 500 条重载、循环输出恢复与离线报告 =====
            def _li_generic_sample_key(sample_id: Any) -> str:
                return json.dumps(
                    sample_id, ensure_ascii=False, sort_keys=True, separators=(',', ':'),
                )


            def _li_generic_file_sha256(path: Path) -> str:
                digest = hashlib.sha256()
                with path.open('rb') as handle:
                    for chunk in iter(lambda: handle.read(1024 * 1024), b''):
                        digest.update(chunk)
                return digest.hexdigest()


            def _li_generic_transport_error(exc: BaseException) -> bool:
                names = {
                    'APIConnectionError', 'APITimeoutError', 'ConnectionError',
                    'ConnectionRefusedError', 'ConnectionResetError', 'TimeoutError', 'URLError',
                }
                markers = (
                    'winerror 10054', 'winerror 10060', 'winerror 10061',
                    'connection refused', 'connection reset', 'unable to connect',
                    'actively refused', 'actively rejected', 'timed out',
                    '积极拒绝', '强迫关闭',
                )
                current: BaseException | None = exc
                seen: set[int] = set()
                while current is not None and id(current) not in seen:
                    seen.add(id(current))
                    if type(current).__name__ in names:
                        return True
                    if any(marker in str(current).lower() for marker in markers):
                        return True
                    current = current.__cause__ or current.__context__
                return False


            def _li_generic_unload_checked(stage: str) -> None:
                try:
                    LI_GENERIC_MANAGER.unload_all_models()
                    remaining = LI_GENERIC_MANAGER.list_loaded_instances()
                except Exception as exc:
                    raise FatalGenerationError(f'LM Studio 在{stage}时卸载失败。') from exc
                if remaining:
                    raise FatalGenerationError(f'LM Studio 在{stage}后仍有实例：{remaining}')


            def _li_generic_load_client(run: dict[str, Any]) -> LLMClient:
                _li_generic_unload_checked(f"加载 {run['model_key']} 前")
                try:
                    load_result = LI_GENERIC_MANAGER.load_model(
                        run['model_key'],
                        context_length=LI_GENERIC_CONTEXT_LENGTH,
                        parallel=None,
                        offload_kv_cache_to_gpu=True,
                    )
                except Exception as exc:
                    raise FatalGenerationError(f"加载 {run['model_key']} 失败。") from exc
                load_config = load_result.get('load_config', {})
                if int(load_config.get('context_length', 0)) != LI_GENERIC_CONTEXT_LENGTH:
                    LI_GENERIC_MANAGER.unload_all_models()
                    raise RuntimeError(f'模型 context 加载不一致：{load_config}')
                if load_config.get('offload_kv_cache_to_gpu') is not True:
                    LI_GENERIC_MANAGER.unload_all_models()
                    raise RuntimeError(f'模型 KV cache 加载不一致：{load_config}')
                instance_id = str(load_result['instance_id'])
                LI_GENERIC_LOGGER.info(
                    '模型已加载：%s instance=%s parallel=%s',
                    run['model_key'], instance_id, load_config.get('parallel'),
                )
                return LLMClient(
                    provider='lmstudio',
                    base_url=LI_GENERIC_BASE_URL,
                    model=instance_id,
                    api_key=LI_GENERIC_API_KEY,
                    temperature=LI_GENERIC_TEMPERATURE,
                    max_tokens=LI_GENERIC_MAX_TOKENS,
                    context_length=LI_GENERIC_CONTEXT_LENGTH,
                    reasoning='off',
                    extra_body={'cache_prompt': LI_GENERIC_CACHE_PROMPT},
                    timeout=LI_GENERIC_LLM_TIMEOUT,
                    retry_times=LI_GENERIC_RETRY_TIMES,
                )


            def _li_generic_checkpoint_signature(run: dict[str, Any]) -> dict[str, Any]:
                dataset_text = json.dumps(
                    LI_GENERIC_SAMPLES,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(',', ':'),
                )
                prompt_text = load_prompt_template(run['prompt_name'])
                return {
                    'protocol': 'li_gemma_generic_rag_k1_checkpoint_v1',
                    'parser_protocol': 'limited_json_repair_v2',
                    'dataset': 'li',
                    'dataset_sha256': hashlib.sha256(dataset_text.encode('utf-8')).hexdigest(),
                    'sample_count': len(LI_GENERIC_SAMPLES),
                    'run_id': run['run_id'],
                    'model_key': run['model_key'],
                    'prompt_name': run['prompt_name'],
                    'prompt_sha256': hashlib.sha256(prompt_text.encode('utf-8')).hexdigest(),
                    'use_rag': True,
                    'rag_database': 'generic',
                    'rag_mode': 'knn_pattern',
                    'rag_top_k': 1,
                    'metadata_sha256': _li_generic_file_sha256(LI_GENERIC_METADATA_PATH),
                    'embeddings_sha256': _li_generic_file_sha256(LI_GENERIC_EMBEDDINGS_PATH),
                    'temperature': LI_GENERIC_TEMPERATURE,
                    'context_length': LI_GENERIC_CONTEXT_LENGTH,
                    'max_tokens': LI_GENERIC_MAX_TOKENS,
                    'parallel': 'model_default',
                    'cache_prompt': LI_GENERIC_CACHE_PROMPT,
                    'reload_every_samples': LI_GENERIC_RELOAD_EVERY,
                    'degenerate_loop_recovery': 'reload_same_sample_v1',
                    'max_degenerate_reloads_per_sample': LI_GENERIC_MAX_LOOP_RELOADS,
                    'primary_metric': LI_GENERIC_PRIMARY_METRIC,
                }


            def _li_generic_open_checkpoint(run: dict[str, Any]) -> PredictionCheckpoint:
                checkpoint = PredictionCheckpoint(
                    directory=PROJECT_ROOT / LI_GENERIC_CHECKPOINT_DIR,
                    run_name=run['run_id'],
                    signature_payload=_li_generic_checkpoint_signature(run),
                    sample_ids=[sample['id'] for sample in LI_GENERIC_SAMPLES],
                )
                LI_GENERIC_LOGGER.info(
                    '[checkpoint] %s：完成 %s/%s，剩余 %s；%s',
                    run['run_id'], len(checkpoint), len(LI_GENERIC_SAMPLES),
                    checkpoint.remaining_count, checkpoint.predictions_path,
                )
                return checkpoint


            class LiGenericDegenerateGenerationLoop(RuntimeError):
                def __init__(self, sample_id: Any, prediction: dict[str, Any]) -> None:
                    super().__init__(f'id={sample_id!r} 生成了跑满长度的循环输出')
                    self.sample_id = sample_id
                    self.prediction = prediction


            def _li_generic_is_loop_output(raw_output: Any) -> bool:
                text = str(raw_output or '').strip()
                if len(text) < max(256, LI_GENERIC_MAX_TOKENS // 2):
                    return False
                unique_chars = set(text)
                if len(unique_chars) <= 4:
                    return True
                if max(text.count(char) for char in unique_chars) / len(text) >= 0.98:
                    return True
                tail = text[-min(len(text), 1024):]
                for period in range(1, min(64, len(tail) // 4) + 1):
                    unit = tail[:period]
                    repeated = (unit * ((len(tail) + period - 1) // period))[:len(tail)]
                    if repeated == tail:
                        return True
                return False


            def _li_generic_loop_attempts(prediction: dict[str, Any]) -> list[dict[str, Any]]:
                if not prediction.get('error_type'):
                    return []
                return [
                    attempt
                    for attempt in prediction.get('generation_attempts', [])
                    if isinstance(attempt, dict)
                    and _li_generic_is_loop_output(attempt.get('raw_output'))
                ]


            def _li_generic_loop_audit(prediction: dict[str, Any]) -> list[dict[str, Any]]:
                rows: list[dict[str, Any]] = []
                for attempt in _li_generic_loop_attempts(prediction):
                    raw = str(attempt.get('raw_output') or '')
                    rows.append({
                        'attempt': attempt.get('attempt'),
                        'output_chars': len(raw),
                        'unique_chars': len(set(raw)),
                        'raw_output_sha256': hashlib.sha256(raw.encode('utf-8')).hexdigest(),
                    })
                return rows


            def _li_generic_failure_text(prediction: dict[str, Any]) -> str:
                parts = [str(prediction.get('error_message', ''))]
                parts.extend(
                    str(attempt.get('error_message', ''))
                    for attempt in prediction.get('generation_attempts', [])
                    if isinstance(attempt, dict)
                )
                return ' '.join(part for part in parts if part).strip()


            def _li_generic_generate_chunk(
                run: dict[str, Any],
                chunk: list[dict[str, Any]],
                checkpoint: PredictionCheckpoint,
                client: LLMClient,
                reload_counts: dict[str, int],
                loop_history: dict[str, list[dict[str, Any]]],
            ) -> None:
                for sample in _li_generic_progress(
                    chunk,
                    total=len(LI_GENERIC_SAMPLES),
                    desc=f"{run['run_id']} total",
                    initial=len(checkpoint),
                    progress_key=run['run_id'],
                ):
                    sample_id = sample['id']
                    if checkpoint.get(sample_id) is not None:
                        continue
                    try:
                        prediction = generate(
                            text=sample['text'],
                            sample_id=sample_id,
                            client=client,
                            retriever=LI_GENERIC_RETRIEVER,
                            use_rag=True,
                            top_k=1,
                            rag_mode='knn_pattern',
                            prompt_name='v10.2',
                        )
                    except Exception as exc:
                        if _li_generic_transport_error(exc):
                            checkpoint.mark_status(
                                'interrupted',
                                error=f"{run['run_id']} id={sample_id!r}: {type(exc).__name__}: {exc}",
                            )
                            raise FatalGenerationError(
                                f"{run['run_id']} id={sample_id!r} 连接故障；该样本未保存。"
                            ) from exc
                        prediction = {
                            'id': sample_id,
                            'has_causal': False,
                            'triples': [],
                            'error_type': type(exc).__name__,
                            'error_message': str(exc),
                        }

                    if _li_generic_loop_attempts(prediction):
                        raise LiGenericDegenerateGenerationLoop(sample_id, prediction)

                    sample_key = _li_generic_sample_key(sample_id)
                    recovery_count = reload_counts.get(sample_key, 0)
                    if recovery_count:
                        prediction['generation_recovery_type'] = (
                            'fresh_model_reload_after_degenerate_max_length_loop'
                        )
                        prediction['generation_recovery_reload_count'] = recovery_count
                        prediction['generation_recovery_failures'] = loop_history.get(
                            sample_key, []
                        )
                    if prediction.get('error_type'):
                        failure_text = _li_generic_failure_text(prediction)
                        if _li_generic_transport_error(RuntimeError(failure_text)):
                            checkpoint.mark_status(
                                'interrupted',
                                error=f"{run['run_id']} id={sample_id!r}: {failure_text}",
                            )
                            raise FatalGenerationError(
                                f"{run['run_id']} id={sample_id!r} 返回连接故障；该样本未保存。"
                            )
                        LI_GENERIC_LOGGER.warning(
                            '%s id=%r 非连接生成失败；保存可审计兜底。',
                            run['run_id'], sample_id,
                        )
                    checkpoint.append(sample_id, prediction)


            def _li_generic_complete_predictions(
                run: dict[str, Any], checkpoint: PredictionCheckpoint,
            ) -> None:
                reload_counts: dict[str, int] = {}
                loop_history: dict[str, list[dict[str, Any]]] = {}
                while checkpoint.remaining_count > 0:
                    pending = [
                        sample for sample in LI_GENERIC_SAMPLES
                        if checkpoint.get(sample['id']) is None
                    ]
                    chunk = pending[:LI_GENERIC_RELOAD_EVERY]
                    client: LLMClient | None = None
                    loop_exc: LiGenericDegenerateGenerationLoop | None = None
                    try:
                        client = _li_generic_load_client(run)
                        _li_generic_generate_chunk(
                            run, chunk, checkpoint, client, reload_counts, loop_history,
                        )
                    except LiGenericDegenerateGenerationLoop as exc:
                        loop_exc = exc
                    finally:
                        if client is not None:
                            _li_generic_unload_checked(f"{run['run_id']} chunk 后")

                    if loop_exc is not None:
                        sample_key = _li_generic_sample_key(loop_exc.sample_id)
                        reload_count = reload_counts.get(sample_key, 0) + 1
                        reload_counts[sample_key] = reload_count
                        loop_history.setdefault(sample_key, []).append({
                            'failed_instance_number': reload_count,
                            'attempts': _li_generic_loop_audit(loop_exc.prediction),
                        })
                        if reload_count <= LI_GENERIC_MAX_LOOP_RELOADS:
                            checkpoint.mark_status(
                                'reload_required',
                                error=(
                                    f"{run['run_id']} id={loop_exc.sample_id!r} 循环输出；"
                                    f"准备全新实例重试 {reload_count}/"
                                    f"{LI_GENERIC_MAX_LOOP_RELOADS}。"
                                ),
                            )
                            LI_GENERIC_LOGGER.warning(
                                '%s id=%r 循环输出；模型已卸载，将从同一样本重试（%s/%s）。',
                                run['run_id'], loop_exc.sample_id, reload_count,
                                LI_GENERIC_MAX_LOOP_RELOADS,
                            )
                            continue

                        exhausted = dict(loop_exc.prediction)
                        exhausted['error_type'] = 'degenerate_generation_loop_exhausted'
                        exhausted['error_message'] = (
                            f'初始实例及 {LI_GENERIC_MAX_LOOP_RELOADS} 次全新实例均循环输出'
                        )
                        exhausted['generation_recovery_reload_count'] = LI_GENERIC_MAX_LOOP_RELOADS
                        exhausted['generation_recovery_failures'] = loop_history[sample_key]
                        checkpoint.append(loop_exc.sample_id, exhausted)
                        LI_GENERIC_LOGGER.error(
                            '%s id=%r 达到循环输出重载上限；保存失败并继续。',
                            run['run_id'], loop_exc.sample_id,
                        )
                        continue

                    LI_GENERIC_LOGGER.info(
                        '%s chunk 完成：checkpoint=%s/%s，remaining=%s',
                        run['run_id'], len(checkpoint), len(LI_GENERIC_SAMPLES),
                        checkpoint.remaining_count,
                    )


            def _li_generic_build_report(
                run: dict[str, Any],
                checkpoint: PredictionCheckpoint,
                resumed_samples: int,
            ) -> dict[str, Any]:
                if checkpoint.remaining_count:
                    raise RuntimeError(f"{run['run_id']} checkpoint 未完成，不能生成报告。")

                def cached_generator(**kwargs: Any) -> dict[str, Any]:
                    prediction = checkpoint.get(kwargs.get('sample_id'))
                    if prediction is None:
                        raise RuntimeError(f"Checkpoint 缺少 id={kwargs.get('sample_id')!r}")
                    return prediction

                config = EvalRunConfig(
                    project_root=PROJECT_ROOT,
                    model=run['model_key'],
                    dataset='li',
                    prompt_name='v10.2',
                    use_rag=True,
                    rag_mode='knn_pattern',
                    rag_top_k=1,
                    temperature=LI_GENERIC_TEMPERATURE,
                    max_tokens=LI_GENERIC_MAX_TOKENS,
                    primary_metric=LI_GENERIC_PRIMARY_METRIC,
                    progress_every=1000,
                    max_workers=1,
                    llm_provider='lmstudio',
                    llm_base_url=LI_GENERIC_BASE_URL,
                    context_length=LI_GENERIC_CONTEXT_LENGTH,
                    reasoning_effort=None,
                    llm_extra_body={'cache_prompt': LI_GENERIC_CACHE_PROMPT},
                    api_key_source='lmstudio-default',
                    save_report=True,
                    report_dir=LI_GENERIC_REPORT_DIR,
                    report_detail_limit=200,
                    report_detail_mode='errors',
                    report_error_metric=LI_GENERIC_PRIMARY_METRIC,
                    metadata_path=LI_GENERIC_METADATA_PATH,
                    embeddings_path=LI_GENERIC_EMBEDDINGS_PATH,
                )
                report = run_stream_eval(
                    samples=LI_GENERIC_SAMPLES,
                    label=f"{run['display_name']} Li original generic RAG k1 rerun",
                    client=object(),
                    config=config,
                    generator=cached_generator,
                    existing_retriever=LI_GENERIC_RETRIEVER,
                    progress_factory=_li_generic_progress,
                    emit=LI_GENERIC_LOGGER.info,
                )
                report['checkpoint_path'] = str(checkpoint.predictions_path)
                report['checkpoint_resumed_samples'] = resumed_samples
                checkpoint.mark_status('complete', report_path=str(report['report_path']))
                return report


            def _li_generic_summary_row(
                run: dict[str, Any], report: dict[str, Any],
            ) -> dict[str, Any]:
                detection = report['detection']
                strict = report['extraction']['strict_token_f1']
                anchor = report['extraction']['anchor_window']
                return {
                    'status': 'completed',
                    'protocol': 'li_gemma_generic_rag_k1_checkpoint_v1',
                    'run_id': run['run_id'],
                    'model': run['display_name'],
                    'model_key': run['model_key'],
                    'dataset': 'li',
                    'prompt': 'v10.2',
                    'rag_database': 'generic',
                    'rag_mode': 'knn_pattern',
                    'rag_top_k': 1,
                    'temperature': LI_GENERIC_TEMPERATURE,
                    'context_length': LI_GENERIC_CONTEXT_LENGTH,
                    'max_tokens': LI_GENERIC_MAX_TOKENS,
                    'parallel': 'model_default',
                    'reload_every_samples': LI_GENERIC_RELOAD_EVERY,
                    'cache_prompt': LI_GENERIC_CACHE_PROMPT,
                    'n_samples': report['n_samples'],
                    'detection_precision': detection['precision'],
                    'detection_recall': detection['recall'],
                    'detection_f1': detection['f1'],
                    'strict_all_precision': strict['all_samples']['precision'],
                    'strict_all_recall': strict['all_samples']['recall'],
                    'strict_all_f1': strict['all_samples']['f1'],
                    'anchor_all_precision': anchor['all_samples']['precision'],
                    'anchor_all_recall': anchor['all_samples']['recall'],
                    'anchor_all_f1': anchor['all_samples']['f1'],
                    'strict_detected_only_f1': strict['detected_only']['f1'],
                    'anchor_detected_only_f1': anchor['detected_only']['f1'],
                    'generation_failures': report['generation_failures']['total'],
                    'parse_repairs': report['parse_repairs']['total'],
                    'checkpoint_path': report['checkpoint_path'],
                    'checkpoint_resumed_samples': report['checkpoint_resumed_samples'],
                    'report_path': report['report_path'],
                    'error': '',
                }


            def _li_generic_save_summary(rows: list[dict[str, Any]]) -> None:
                LI_GENERIC_SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
                order = [run['run_id'] for run in LI_GEMMA_GENERIC_RUNS]
                frame = pd.DataFrame(rows)
                if frame.empty:
                    frame = pd.DataFrame(columns=['status', 'protocol', 'run_id'])
                else:
                    frame['_order'] = pd.Categorical(
                        frame['run_id'], categories=order, ordered=True,
                    )
                    frame = frame.sort_values('_order').drop(columns='_order')
                frame.to_csv(LI_GENERIC_SUMMARY_PATH, index=False, encoding='utf-8-sig')


            def run_li_gemma_generic_rerun() -> list[dict[str, Any]]:
                rows: list[dict[str, Any]] = []
                if LI_GENERIC_SUMMARY_PATH.is_file():
                    try:
                        old = pd.read_csv(LI_GENERIC_SUMMARY_PATH)
                    except pd.errors.EmptyDataError:
                        LI_GENERIC_LOGGER.warning(
                            '检测到首次中断留下的空 summary；忽略并从 checkpoint 恢复。'
                        )
                        old = pd.DataFrame()
                    if not old.empty:
                        completed = old.loc[old['status'] == 'completed'].copy()
                        if not completed.empty and set(completed['protocol'].astype(str)) != {
                            'li_gemma_generic_rag_k1_checkpoint_v1'
                        }:
                            raise RuntimeError('阶段 4 summary 混入其他协议。')
                        rows = completed.drop_duplicates('run_id', keep='last').to_dict('records')

                completed_ids = {str(row['run_id']) for row in rows}
                pending = [
                    run for run in LI_GEMMA_GENERIC_RUNS
                    if run['run_id'] not in completed_ids
                ]
                for run in pending:
                    checkpoint: PredictionCheckpoint | None = None
                    try:
                        checkpoint = _li_generic_open_checkpoint(run)
                        resumed_samples = len(checkpoint)
                        _li_generic_complete_predictions(run, checkpoint)
                        report = _li_generic_build_report(
                            run, checkpoint, resumed_samples,
                        )
                        rows = [row for row in rows if row.get('run_id') != run['run_id']]
                        rows.append(_li_generic_summary_row(run, report))
                    except KeyboardInterrupt:
                        if checkpoint is not None:
                            checkpoint.mark_status('interrupted', error='KeyboardInterrupt')
                        _li_generic_save_summary(rows)
                        raise
                    except FatalGenerationError as exc:
                        if checkpoint is not None:
                            checkpoint.mark_status('interrupted', error=str(exc))
                        rows = [row for row in rows if row.get('run_id') != run['run_id']]
                        rows.append({
                            'status': 'interrupted',
                            'protocol': 'li_gemma_generic_rag_k1_checkpoint_v1',
                            'run_id': run['run_id'],
                            'model': run['display_name'],
                            'model_key': run['model_key'],
                            'rag_database': 'generic',
                            'rag_mode': 'knn_pattern',
                            'rag_top_k': 1,
                            'checkpoint_path': (
                                str(checkpoint.predictions_path) if checkpoint else ''
                            ),
                            'error': f'{type(exc).__name__}: {exc}',
                        })
                        _li_generic_save_summary(rows)
                        LI_GENERIC_LOGGER.error('基础设施故障，阶段 4 停止：%s', exc)
                        break
                    except Exception as exc:
                        if checkpoint is not None:
                            checkpoint.mark_status(
                                'interrupted', error=f'{type(exc).__name__}: {exc}',
                            )
                        LI_GENERIC_LOGGER.exception('%s 失败。', run['run_id'])
                        rows = [row for row in rows if row.get('run_id') != run['run_id']]
                        rows.append({
                            'status': 'failed',
                            'protocol': 'li_gemma_generic_rag_k1_checkpoint_v1',
                            'run_id': run['run_id'],
                            'model': run['display_name'],
                            'model_key': run['model_key'],
                            'rag_database': 'generic',
                            'rag_mode': 'knn_pattern',
                            'rag_top_k': 1,
                            'checkpoint_path': (
                                str(checkpoint.predictions_path) if checkpoint else ''
                            ),
                            'error': f'{type(exc).__name__}: {exc}',
                        })
                    _li_generic_save_summary(rows)
                return rows
            """,
        ),
        _code(
            "run-li-gemma-generic-rerun",
            r"""
            # ===== 阶段 4：执行两个 Gemma 的 Li original generic RAG k=1 补跑 =====
            if not RUN_LI_GEMMA_GENERIC_RAG_RERUN:
                LI_GENERIC_LOGGER.warning('阶段 4 Gemma generic RAG 补跑未启动。')
            else:
                LI_GEMMA_GENERIC_RESULTS = run_li_gemma_generic_rerun()
                li_gemma_generic_df = pd.DataFrame(LI_GEMMA_GENERIC_RESULTS)
                display(li_gemma_generic_df)
                completed_ids = set(
                    li_gemma_generic_df.loc[
                        li_gemma_generic_df['status'] == 'completed', 'run_id'
                    ].astype(str)
                )
                expected_ids = {run['run_id'] for run in LI_GEMMA_GENERIC_RUNS}
                if completed_ids != expected_ids:
                    missing = sorted(expected_ids - completed_ids)
                    raise RuntimeError(
                        f'阶段 4 尚未完成：missing={missing}。checkpoint 已保存，可直接续跑。'
                    )
                display(li_gemma_generic_df[[
                    'model', 'rag_database', 'rag_mode', 'rag_top_k',
                    'detection_f1', 'anchor_all_f1', 'strict_all_f1',
                    'generation_failures', 'parse_repairs',
                ]])
                LI_GENERIC_LOGGER.info('阶段 4 两个 Gemma 补跑完成：%s', LI_GENERIC_SUMMARY_PATH)
            """,
        ),
    ]


def main() -> None:
    notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    notebook["cells"] = [
        cell
        for cell in notebook["cells"]
        if str(cell.get("id", "")) not in CELL_IDS
        and not (
            cell.get("cell_type") == "code"
            and not "".join(cell.get("source", [])).strip()
        )
    ]
    notebook["cells"].extend(build_cells())
    NOTEBOOK_PATH.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    print(NOTEBOOK_PATH)


if __name__ == "__main__":
    main()
