"""Generate the unified twelve-run Qwen cross-dataset evaluation notebook."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "notebooks" / "lmstudio_qwen_family_three_datasets_12runs.ipynb"


class NotebookNode(dict[str, Any]):

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class _V4:
    @staticmethod
    def new_notebook() -> NotebookNode:
        return NotebookNode(cells=[], metadata={}, nbformat=4, nbformat_minor=5)

    @staticmethod
    def new_markdown_cell(source: str, *, id: str) -> NotebookNode:
        return NotebookNode(cell_type="markdown", id=id, metadata={}, source=source)

    @staticmethod
    def new_code_cell(source: str, *, id: str) -> NotebookNode:
        return NotebookNode(
            cell_type="code",
            execution_count=None,
            id=id,
            metadata={},
            outputs=[],
            source=source,
        )


class _NotebookFormat:
    v4 = _V4()
    NotebookNode = NotebookNode

    @staticmethod
    def write(notebook: NotebookNode, path: Path) -> None:
        path.write_text(
            json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )


nbf = _NotebookFormat()


def _source(text: str) -> str:
    return dedent(text).strip() + "\n"


def build_notebook() -> nbf.NotebookNode:
    notebook = nbf.v4.new_notebook()
    notebook.metadata = {
        "kernelspec": {
            "display_name": "Master_thesis",
            "language": "python",
            "name": "master_thesis",
        },
        "language_info": {"name": "python", "version": "3.11"},
    }
    notebook.cells = [
        nbf.v4.new_markdown_cell(
            _source(
                """
                # Qwen 双模型 × CNC/ADE/Li × Fixed/RAG：12 轮统一补跑

                本 notebook 在 Phase 2 完成并产出 `phase2_qwen27_v9.8_anchor_k_selection.csv` 后运行。
                它依次执行 3 个数据集 × 2 个 Qwen 模型 × 2 种条件，共 12 个逻辑实验：

                - Fixed：Gemma 边界风格的 10-shot Prompt，RAG 关闭；
                - Fixed + RAG：相同 Prompt，并使用 Phase 2 选出的 Qwen 家族 k；
                - CNC / ADE / Li 分别使用 `v9.8` / `v9.2` / `v10.2`；
                - CNC 使用 600 条 CNC train-only support；ADE 与 Li 使用原始 generic Pattern/BGE database；
                - 三个数据集统一以 `anchor_window` 为主指标，`strict_token_f1` 作为辅助指标。

                稳定性协议：每条预测立即写入带运行签名的 checkpoint；`cache_prompt=False`；
                每生成 500 条就卸载并重新加载当前模型；连接故障不会保存 False 兜底，而是停止整批。
                若检测到接近 `MAX_TOKENS` 的单字符/极低多样性循环输出，则不保存该失败结果，立即卸载模型，
                用全新实例从同一 sample 重试；单样本最多自动重载 3 次，之后才保存可审计失败并继续。
                重启 kernel 后重新运行即可从当前 run 的未完成 sample ID 继续。完成态 checkpoint 只离线重建报告，
                不重新调用模型。

                当前 `RUN_BATCH = True`，已经按最终配置锁定；从第一格开始顺序运行即可。
                """
            ),
            id="overview",
        ),
        nbf.v4.new_code_cell(
            _source(
                """
                # ===== 1. 全局配置 =====
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
                    raise RuntimeError('请切换到 Master_thesis kernel，重启 kernel 后从第一格重新运行。')

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
                LOGGER = logging.getLogger('lmstudio_qwen_family_three_datasets_12runs')
                logging.getLogger('src.llm_client').setLevel(logging.WARNING)


                def _notebook_progress(
                    iterable: Iterable[Any],
                    *,
                    total: int,
                    desc: str,
                ) -> Iterator[Any]:
                    safe_desc = escape(desc)
                    safe_total = max(total, 1)

                    def render(completed: int) -> HTML:
                        percent = min(completed / safe_total * 100, 100.0)
                        return HTML(
                            f"<div style='width:100%'>"
                            f"<div>{safe_desc}: {completed}/{total} ({percent:.1f}%)</div>"
                            f"<progress value='{completed}' max='{safe_total}' "
                            f"style='width:100%;height:18px'></progress></div>"
                        )

                    handle = display(render(0), display_id=True)
                    for completed, item in enumerate(iterable, 1):
                        yield item
                        if handle is not None:
                            handle.update(render(completed))


                LMSTUDIO_BASE_URL = 'http://127.0.0.1:1234/v1'
                LMSTUDIO_API_KEY = 'lm-studio'
                MODEL_LOAD_TIMEOUT = 1200
                LLM_TIMEOUT = 600
                LLM_RETRY_TIMES = 3
                CONTEXT_LENGTH = 8192
                MODEL_PARALLEL = 4
                OFFLOAD_KV_CACHE_TO_GPU = True
                MAX_TOKENS = 2048
                TEMPERATURE = 0.0
                CACHE_PROMPT = False

                PRIMARY_METRIC = 'anchor_window'
                EVAL_MAX_WORKERS = 1
                EVAL_PROGRESS_EVERY = 500
                MODEL_RELOAD_EVERY_SAMPLES = 500
                MAX_DEGENERATE_RELOADS_PER_SAMPLE = 3
                QWEN_RAG_TOP_K = 1
                RANDOM_SEED = 42
                RUN_BATCH = True

                REPORT_DIR = (
                    Path('results') / 'eval_report' / 'qwen_family_three_datasets_anchor_rerun'
                )
                CHECKPOINT_DIR = (
                    Path('results') / 'eval_checkpoints' / 'qwen_family_three_datasets_anchor_rerun'
                )
                SUMMARY_PATH = PROJECT_ROOT / REPORT_DIR / 'qwen_family_three_datasets_12runs_summary.csv'
                PHASE2_DIR = (
                    PROJECT_ROOT / 'results' / 'eval_report' / 'rag_ablation'
                    / 'phase2_qwen27_v9.8_anchor'
                )
                PHASE2_SUMMARY_PATH = PHASE2_DIR / 'phase2_qwen27_v9.8_anchor_summary.csv'
                PHASE2_K_SELECTION_PATH = PHASE2_DIR / 'phase2_qwen27_v9.8_anchor_k_selection.csv'

                DATASET_CONFIGS: list[dict[str, Any]] = [
                    {
                        'dataset_key': 'cnc',
                        'dataset_name': 'cnc_sft_test',
                        'split': 'test',
                        'expected': {
                            'samples': 1038, 'positive': 548, 'negative': 490,
                            'relations': 763, 'max_relations': 5,
                        },
                        'prompt_name': 'v9.8',
                        'rag_database': 'cnc',
                    },
                    {
                        'dataset_key': 'ade',
                        'dataset_name': 'ade',
                        'split': 'test',
                        'expected': {
                            'samples': 2942, 'positive': 448, 'negative': 2494,
                            'relations': 663, 'max_relations': 10,
                        },
                        'prompt_name': 'v9.2',
                        'rag_database': 'generic',
                    },
                    {
                        'dataset_key': 'li',
                        'dataset_name': 'li',
                        'split': 'full',
                        'expected': {
                            'samples': 786, 'positive': 191, 'negative': 595,
                            'relations': 296, 'max_relations': 12,
                        },
                        'prompt_name': 'v10.2',
                        'rag_database': 'generic',
                    },
                ]
                MODEL_CONFIGS: list[dict[str, str]] = [
                    {
                        'model_id': 'qwen35',
                        'display_name': 'Qwen3.6 35B A3B',
                        'model_key': 'qwen/qwen3.6-35b-a3b',
                    },
                    {
                        'model_id': 'qwen27',
                        'display_name': 'Qwen3.6 27B No Thinking',
                        'model_key': 'local/qwen3.6-27b-no-thinking',
                    },
                ]

                display(pd.DataFrame(DATASET_CONFIGS))
                display(pd.DataFrame(MODEL_CONFIGS))
                """
            ),
            id="global-config",
        ),
        nbf.v4.new_code_cell(
            _source(
                """
                # ===== 2. Phase 2、模型、数据、Prompt 与 RAG 隔离预检 =====
                EXPECTED_PHASE2_RUN_IDS = {
                    'fixed',
                    'rag_only_k1', 'rag_only_k3', 'rag_only_k5',
                    'fixed_random_k1', 'fixed_random_k3', 'fixed_random_k5',
                    'fixed_rag_k1', 'fixed_rag_k3', 'fixed_rag_k5',
                }
                if not PHASE2_SUMMARY_PATH.is_file():
                    raise FileNotFoundError(f'缺少 Phase 2 汇总：{PHASE2_SUMMARY_PATH}')
                if not PHASE2_K_SELECTION_PATH.is_file():
                    raise FileNotFoundError(
                        f'Phase 2 尚未完成或尚未生成 k-selection：{PHASE2_K_SELECTION_PATH}'
                    )

                phase2_df = pd.read_csv(PHASE2_SUMMARY_PATH)
                phase2_completed = phase2_df.loc[phase2_df['status'] == 'completed'].copy()
                phase2_completed = phase2_completed.drop_duplicates(subset='run_id', keep='last')
                completed_phase2_ids = set(phase2_completed['run_id'].astype(str))
                if completed_phase2_ids != EXPECTED_PHASE2_RUN_IDS:
                    missing = sorted(EXPECTED_PHASE2_RUN_IDS - completed_phase2_ids)
                    extra = sorted(completed_phase2_ids - EXPECTED_PHASE2_RUN_IDS)
                    raise RuntimeError(f'Phase 2 完成态 run 不完整：missing={missing}, extra={extra}')
                if set(phase2_completed['primary_metric'].astype(str)) != {PRIMARY_METRIC}:
                    raise RuntimeError('Phase 2 不是统一以 anchor_window 为主指标。')

                k_selection_df = pd.read_csv(PHASE2_K_SELECTION_PATH).sort_values('selection_rank')
                if len(k_selection_df) != 3 or set(k_selection_df['k'].astype(int)) != {1, 3, 5}:
                    raise RuntimeError('Phase 2 k-selection 必须完整包含 k=1/3/5。')
                phase2_selected_k = int(k_selection_df.iloc[0]['k'])
                if phase2_selected_k != QWEN_RAG_TOP_K:
                    raise RuntimeError(
                        f'最终配置固定为 Qwen k={QWEN_RAG_TOP_K}，但 Phase 2 选择文件为 '
                        f'k={phase2_selected_k}；拒绝静默漂移。'
                    )
                SELECTED_K = QWEN_RAG_TOP_K

                RUN_MATRIX: list[dict[str, Any]] = []
                for dataset_config in DATASET_CONFIGS:
                    for use_rag in (False, True):
                        for model_config in MODEL_CONFIGS:
                            condition = 'fixed_rag' if use_rag else 'fixed'
                            run = {
                                **dataset_config,
                                **model_config,
                                'condition': condition,
                                'configuration': 'Fixed + RAG' if use_rag else 'Fixed',
                                'use_rag': use_rag,
                                'rag_mode': 'knn_pattern' if use_rag else 'off',
                                'rag_top_k': SELECTED_K if use_rag else 0,
                                'total_examples': 10 + (2 * SELECTED_K if use_rag else 0),
                            }
                            run['run_id'] = (
                                f"{run['dataset_key']}_{run['model_id']}_{condition}"
                                + (f"_k{SELECTED_K}" if use_rag else '')
                            )
                            RUN_MATRIX.append(run)
                if len(RUN_MATRIX) != 12 or len({run['run_id'] for run in RUN_MATRIX}) != 12:
                    raise RuntimeError('统一运行矩阵必须包含 12 个唯一 run。')

                manager = LLMClient(
                    provider='lmstudio',
                    base_url=LMSTUDIO_BASE_URL,
                    model=MODEL_CONFIGS[0]['model_key'],
                    api_key=LMSTUDIO_API_KEY,
                    temperature=TEMPERATURE,
                    max_tokens=MAX_TOKENS,
                    context_length=CONTEXT_LENGTH,
                    reasoning='off',
                    extra_body={'cache_prompt': CACHE_PROMPT},
                    timeout=MODEL_LOAD_TIMEOUT,
                    retry_times=LLM_RETRY_TIMES,
                )
                inventory_by_key = {
                    str(item['key']): item
                    for item in manager.list_local_models()
                    if item.get('key')
                }
                missing_model_keys = [
                    model['model_key']
                    for model in MODEL_CONFIGS
                    if model['model_key'] not in inventory_by_key
                ]
                if missing_model_keys:
                    raise RuntimeError(f'LM Studio 缺少目标模型：{missing_model_keys}')
                for model in MODEL_CONFIGS:
                    reasoning = inventory_by_key[model['model_key']].get('capabilities', {}).get('reasoning', {})
                    allowed = reasoning.get('allowed_options', [])
                    if allowed and 'off' not in allowed:
                        raise RuntimeError(f"{model['model_key']} 不支持 reasoning=off。")

                DATASETS: dict[str, list[dict[str, Any]]] = {}
                dataset_audit_rows: list[dict[str, Any]] = []
                for config in DATASET_CONFIGS:
                    samples = load_dataset(config['dataset_name'])
                    stats = {
                        'samples': len(samples),
                        'positive': sum(bool(sample['has_causal']) for sample in samples),
                        'negative': sum(not bool(sample['has_causal']) for sample in samples),
                        'relations': sum(len(sample.get('relations', [])) for sample in samples),
                        'max_relations': max(len(sample.get('relations', [])) for sample in samples),
                    }
                    if stats != config['expected']:
                        raise RuntimeError(
                            f"{config['dataset_name']} 数据漂移：{stats} != {config['expected']}"
                        )
                    if len({str(sample['id']) for sample in samples}) != len(samples):
                        raise RuntimeError(f"{config['dataset_name']} 存在重复 sample id。")
                    prompt_text = load_prompt_template(config['prompt_name'])
                    if prompt_text.count('{rag_examples}') != 1:
                        raise RuntimeError(f"{config['prompt_name']} 必须包含一个 RAG 插槽。")
                    if prompt_text.count('\\nInput:\\n') != 10:
                        raise RuntimeError(f"{config['prompt_name']} 必须包含 10 个 fixed examples。")
                    DATASETS[config['dataset_key']] = samples
                    dataset_audit_rows.append({'dataset': config['dataset_name'], **stats})

                cnc_manifest = json.loads(
                    (PROJECT_ROOT / 'RAG Database' / 'cnc_split_manifest.json').read_text(encoding='utf-8')
                )
                if not cnc_manifest.get('train_only_support'):
                    raise RuntimeError('CNC RAG manifest 未声明 train_only_support。')
                cnc_test_ids = {str(sample['id']) for sample in DATASETS['cnc']}
                cnc_support_ids = {str(sample_id) for sample_id in cnc_manifest['support_ids']}
                if cnc_test_ids.intersection(cnc_support_ids):
                    raise RuntimeError('CNC RAG support 与 CNC test 存在精确 ID 重叠。')

                cleaning_stats = json.loads(
                    (PROJECT_ROOT / 'Data' / 'stats.json').read_text(encoding='utf-8')
                )
                if (
                    cleaning_stats['ade']['split_role'] != 'test'
                    or cleaning_stats['ade']['train_ratio'] != 0.85
                    or cleaning_stats['ade']['repartition_seed'] != 42
                    or cleaning_stats['ade_source']['bge_excluded_samples'] != 1286
                ):
                    raise RuntimeError('ADE test split 或 generic RAG overlap 排除记录不匹配。')

                def _normalize_overlap_text(value: Any) -> str:
                    without_tags = re.sub(
                        r'</?(?:cause|effect)>', '', str(value or ''), flags=re.IGNORECASE,
                    )
                    return ' '.join(without_tags.casefold().split())

                generic_metadata_path, _ = resolve_rag_cache_paths('generic')
                generic_support_texts = {
                    _normalize_overlap_text(json.loads(line).get('sentence', ''))
                    for line in generic_metadata_path.read_text(encoding='utf-8').splitlines()
                    if line.strip()
                }
                li_texts = {
                    _normalize_overlap_text(sample['text']) for sample in DATASETS['li']
                }
                li_generic_overlap = generic_support_texts & li_texts
                if li_generic_overlap:
                    raise RuntimeError(
                        f'Li 与 original generic RAG database 存在文本泄漏：'
                        f'{len(li_generic_overlap)} 条。'
                    )

                RAG_RETRIEVERS: dict[str, ExactCountHybridRetriever] = {}
                rag_audit_rows: list[dict[str, Any]] = []
                for database in sorted({config['rag_database'] for config in DATASET_CONFIGS}):
                    metadata_path, embeddings_path = resolve_rag_cache_paths(database)
                    if not metadata_path.is_file() or not embeddings_path.is_file():
                        raise FileNotFoundError(f'{database} RAG cache 不完整。')
                    retriever = ExactCountHybridRetriever(
                        pattern_retriever=PatternRetriever(metadata_path=metadata_path),
                        knn_retriever=KNNRetriever(
                            metadata_path=metadata_path,
                            embeddings_path=embeddings_path,
                            device='cpu',
                        ),
                    )
                    probe = retriever.retrieve('Heavy rain caused flooding in the region.', top_k=SELECTED_K)
                    if len(probe) != 2 * SELECTED_K:
                        raise RuntimeError(f'{database} RAG 未严格返回 2k examples。')
                    RAG_RETRIEVERS[database] = retriever
                    rag_audit_rows.append({
                        'database': database,
                        'selected_k': SELECTED_K,
                        'dynamic_examples': len(probe),
                        'metadata_path': str(metadata_path),
                        'embeddings_path': str(embeddings_path),
                    })

                display(pd.DataFrame(dataset_audit_rows))
                display(pd.DataFrame(rag_audit_rows))
                display(pd.DataFrame(RUN_MATRIX)[[
                    'run_id', 'dataset_name', 'split', 'display_name', 'configuration',
                    'prompt_name', 'rag_database', 'rag_top_k', 'total_examples',
                ]])
                LOGGER.info(
                    '预检通过：12 runs，selected_k=%s，cache_prompt=%s，reload_every=%s。',
                    SELECTED_K, CACHE_PROMPT, MODEL_RELOAD_EVERY_SAMPLES,
                )
                """
            ),
            id="preflight",
        ),
        nbf.v4.new_code_cell(
            _source(
                """
                # ===== 3. 逐样本 checkpoint、每 500 条重载、离线报告与汇总 =====
                def _is_lmstudio_transport_error(exc: BaseException) -> bool:
                    transport_names = {
                        'APIConnectionError', 'APITimeoutError', 'ConnectionError',
                        'ConnectionRefusedError', 'ConnectionResetError', 'TimeoutError', 'URLError',
                    }
                    transport_markers = (
                        'winerror 10054', 'winerror 10060', 'winerror 10061',
                        'connection refused', 'connection reset', 'unable to connect',
                        'actively refused', 'actively rejected', 'timed out',
                        '积极拒绝', '强迫关闭',
                    )
                    current: BaseException | None = exc
                    seen: set[int] = set()
                    while current is not None and id(current) not in seen:
                        seen.add(id(current))
                        if type(current).__name__ in transport_names:
                            return True
                        if any(marker in str(current).lower() for marker in transport_markers):
                            return True
                        current = current.__cause__ or current.__context__
                    return False


                def _require_lmstudio_service(stage: str) -> list[dict[str, Any]]:
                    try:
                        return manager.list_local_models()
                    except Exception as exc:
                        raise FatalGenerationError(
                            f'LM Studio 在{stage}不可用；已有预测已保存，可重启后续跑。'
                        ) from exc


                def _unload_all_models_checked(stage: str) -> None:
                    _require_lmstudio_service(f'{stage}前健康检查')
                    try:
                        manager.unload_all_models()
                        remaining = manager.list_loaded_instances()
                    except Exception as exc:
                        raise FatalGenerationError(f'LM Studio 在{stage}时卸载失败。') from exc
                    if remaining:
                        raise FatalGenerationError(f'LM Studio 在{stage}后仍有实例：{remaining}')


                def _load_eval_client(run: dict[str, Any]) -> tuple[LLMClient, str]:
                    _unload_all_models_checked(f"加载 {run['model_key']}")
                    try:
                        load_result = manager.load_model(
                            run['model_key'],
                            context_length=CONTEXT_LENGTH,
                            parallel=MODEL_PARALLEL,
                            offload_kv_cache_to_gpu=OFFLOAD_KV_CACHE_TO_GPU,
                        )
                    except Exception as exc:
                        raise FatalGenerationError(f"加载 {run['model_key']} 失败。") from exc
                    load_config = load_result.get('load_config', {})
                    actual = {
                        'context_length': int(load_config.get('context_length', 0)),
                        'parallel': int(load_config.get('parallel', 0)),
                        'offload_kv_cache_to_gpu': load_config.get('offload_kv_cache_to_gpu') is True,
                    }
                    expected = {
                        'context_length': CONTEXT_LENGTH,
                        'parallel': MODEL_PARALLEL,
                        'offload_kv_cache_to_gpu': OFFLOAD_KV_CACHE_TO_GPU,
                    }
                    if actual != expected:
                        manager.unload_all_models()
                        raise RuntimeError(f'模型实际加载配置不一致：{actual} != {expected}')
                    instance_id = str(load_result['instance_id'])
                    client = LLMClient(
                        provider='lmstudio',
                        base_url=LMSTUDIO_BASE_URL,
                        model=instance_id,
                        api_key=LMSTUDIO_API_KEY,
                        temperature=TEMPERATURE,
                        max_tokens=MAX_TOKENS,
                        context_length=CONTEXT_LENGTH,
                        reasoning='off',
                        extra_body={'cache_prompt': CACHE_PROMPT},
                        timeout=LLM_TIMEOUT,
                        retry_times=LLM_RETRY_TIMES,
                    )
                    LOGGER.info(
                        '模型已加载：%s instance=%s context=%s parallel=%s cache_prompt=%s',
                        run['model_key'], instance_id, CONTEXT_LENGTH, MODEL_PARALLEL, CACHE_PROMPT,
                    )
                    return client, instance_id


                def _checkpoint_signature(run: dict[str, Any], samples: list[dict[str, Any]]) -> dict[str, Any]:
                    dataset_text = json.dumps(
                        samples, ensure_ascii=False, sort_keys=True, separators=(',', ':'),
                    )
                    prompt_text = load_prompt_template(run['prompt_name'])
                    return {
                        'protocol': 'qwen_family_three_datasets_anchor_rerun_v1',
                        'parser_protocol': 'limited_json_repair_v2',
                        'dataset': run['dataset_name'],
                        'dataset_sha256': hashlib.sha256(dataset_text.encode('utf-8')).hexdigest(),
                        'sample_count': len(samples),
                        'run_id': run['run_id'],
                        'model_key': run['model_key'],
                        'prompt_name': run['prompt_name'],
                        'prompt_sha256': hashlib.sha256(prompt_text.encode('utf-8')).hexdigest(),
                        'use_rag': run['use_rag'],
                        'rag_database': run['rag_database'] if run['use_rag'] else None,
                        'rag_mode': run['rag_mode'],
                        'rag_top_k': run['rag_top_k'],
                        'phase2_selected_k': SELECTED_K,
                        'temperature': TEMPERATURE,
                        'context_length': CONTEXT_LENGTH,
                        'parallel': MODEL_PARALLEL,
                        'max_tokens': MAX_TOKENS,
                        'cache_prompt': CACHE_PROMPT,
                        'degenerate_loop_recovery': 'reload_same_sample_v1',
                        'max_degenerate_reloads_per_sample': MAX_DEGENERATE_RELOADS_PER_SAMPLE,
                        'primary_metric': PRIMARY_METRIC,
                    }


                def _open_checkpoint(
                    run: dict[str, Any],
                    samples: list[dict[str, Any]],
                ) -> PredictionCheckpoint:
                    checkpoint = PredictionCheckpoint(
                        directory=PROJECT_ROOT / CHECKPOINT_DIR,
                        run_name=run['run_id'],
                        signature_payload=_checkpoint_signature(run, samples),
                        sample_ids=[sample['id'] for sample in samples],
                    )
                    LOGGER.info(
                        '[checkpoint] %s：完成 %s/%s，剩余 %s；%s',
                        run['run_id'], len(checkpoint), len(samples),
                        checkpoint.remaining_count, checkpoint.predictions_path,
                    )
                    return checkpoint


                def _transport_failure_text(prediction: dict[str, Any]) -> str:
                    parts = [str(prediction.get('error_message', ''))]
                    parts.extend(
                        str(attempt.get('error_message', ''))
                        for attempt in prediction.get('generation_attempts', [])
                        if isinstance(attempt, dict)
                    )
                    return ' '.join(part for part in parts if part).strip()


                class DegenerateGenerationLoop(RuntimeError):
                    def __init__(self, sample_id: Any, prediction: dict[str, Any]) -> None:
                        super().__init__(f'id={sample_id!r} 生成了跑满长度的循环输出')
                        self.sample_id = sample_id
                        self.prediction = prediction


                def _is_repetitive_max_length_output(raw_output: Any) -> bool:
                    text = str(raw_output or '').strip()
                    minimum_chars = max(256, MAX_TOKENS // 2)
                    if len(text) < minimum_chars:
                        return False

                    unique_chars = set(text)
                    if len(unique_chars) <= 4:
                        return True
                    dominant_count = max(text.count(char) for char in unique_chars)
                    if dominant_count / len(text) >= 0.98:
                        return True

                    # 捕获诸如 ``abcabc...`` 或短语反复直到 token 上限的周期循环。
                    tail = text[-min(len(text), 1024):]
                    for period in range(1, min(64, len(tail) // 4) + 1):
                        unit = tail[:period]
                        if (unit * ((len(tail) + period - 1) // period))[:len(tail)] == tail:
                            return True
                    return False


                def _degenerate_attempts(prediction: dict[str, Any]) -> list[dict[str, Any]]:
                    if not prediction.get('error_type'):
                        return []
                    return [
                        attempt
                        for attempt in prediction.get('generation_attempts', [])
                        if isinstance(attempt, dict)
                        and _is_repetitive_max_length_output(attempt.get('raw_output'))
                    ]


                def _degenerate_attempt_audit(prediction: dict[str, Any]) -> list[dict[str, Any]]:
                    audit: list[dict[str, Any]] = []
                    for attempt in _degenerate_attempts(prediction):
                        raw_output = str(attempt.get('raw_output') or '')
                        audit.append({
                            'attempt': attempt.get('attempt'),
                            'output_chars': len(raw_output),
                            'unique_chars': len(set(raw_output)),
                            'raw_output_sha256': hashlib.sha256(
                                raw_output.encode('utf-8')
                            ).hexdigest(),
                        })
                    return audit


                def _generate_chunk(
                    run: dict[str, Any],
                    chunk: list[dict[str, Any]],
                    checkpoint: PredictionCheckpoint,
                    client: LLMClient,
                    retriever: Any,
                    degenerate_reload_counts: dict[str, int],
                    degenerate_history: dict[str, list[dict[str, Any]]],
                ) -> None:
                    for completed, sample in enumerate(
                        _notebook_progress(chunk, total=len(chunk), desc=f"{run['run_id']} chunk"),
                        1,
                    ):
                        sample_id = sample['id']
                        if checkpoint.get(sample_id) is not None:
                            continue
                        try:
                            prediction = generate(
                                text=sample['text'],
                                sample_id=sample_id,
                                client=client,
                                retriever=retriever,
                                use_rag=run['use_rag'],
                                top_k=run['rag_top_k'],
                                rag_mode=run['rag_mode'],
                                prompt_name=run['prompt_name'],
                            )
                        except Exception as exc:
                            if _is_lmstudio_transport_error(exc):
                                checkpoint.mark_status(
                                    'interrupted',
                                    error=f"{run['run_id']} id={sample_id!r}: {type(exc).__name__}: {exc}",
                                )
                                raise FatalGenerationError(
                                    f"{run['run_id']} id={sample_id!r} 发生连接故障；该样本未保存。"
                                ) from exc
                            prediction = {
                                'id': sample_id,
                                'has_causal': False,
                                'triples': [],
                                'error_type': type(exc).__name__,
                                'error_message': str(exc),
                            }
                        if _degenerate_attempts(prediction):
                            raise DegenerateGenerationLoop(sample_id, prediction)

                        sample_key = json.dumps(
                            sample_id, ensure_ascii=False, sort_keys=True, separators=(',', ':'),
                        )
                        recovery_count = degenerate_reload_counts.get(sample_key, 0)
                        if recovery_count:
                            prediction['generation_recovery_type'] = (
                                'fresh_model_reload_after_degenerate_max_length_loop'
                            )
                            prediction['generation_recovery_reload_count'] = recovery_count
                            prediction['generation_recovery_failures'] = degenerate_history.get(
                                sample_key, []
                            )
                        if prediction.get('error_type'):
                            failure_text = _transport_failure_text(prediction)
                            if _is_lmstudio_transport_error(RuntimeError(failure_text)):
                                checkpoint.mark_status(
                                    'interrupted',
                                    error=f"{run['run_id']} id={sample_id!r}: {failure_text}",
                                )
                                raise FatalGenerationError(
                                    f"{run['run_id']} id={sample_id!r} 返回连接故障兜底；该样本未保存。"
                                )
                            LOGGER.warning(
                                '%s id=%r 为非连接生成失败；保存可审计兜底并继续。',
                                run['run_id'], sample_id,
                            )
                        checkpoint.append(sample_id, prediction)
                        if completed % 100 == 0:
                            LOGGER.info(
                                '%s 当前 checkpoint=%s/%s',
                                run['run_id'], len(checkpoint),
                                len(checkpoint.sample_id_keys),
                            )


                def _complete_predictions(
                    run: dict[str, Any],
                    samples: list[dict[str, Any]],
                    checkpoint: PredictionCheckpoint,
                ) -> None:
                    retriever = RAG_RETRIEVERS[run['rag_database']] if run['use_rag'] else None
                    degenerate_reload_counts: dict[str, int] = {}
                    degenerate_history: dict[str, list[dict[str, Any]]] = {}
                    while checkpoint.remaining_count > 0:
                        pending = [
                            sample for sample in samples
                            if checkpoint.get(sample['id']) is None
                        ]
                        chunk = pending[:MODEL_RELOAD_EVERY_SAMPLES]
                        client: LLMClient | None = None
                        degenerate_exc: DegenerateGenerationLoop | None = None
                        try:
                            client, _instance_id = _load_eval_client(run)
                            _generate_chunk(
                                run,
                                chunk,
                                checkpoint,
                                client,
                                retriever,
                                degenerate_reload_counts,
                                degenerate_history,
                            )
                        except DegenerateGenerationLoop as exc:
                            degenerate_exc = exc
                        finally:
                            if client is not None:
                                _unload_all_models_checked(f"{run['run_id']} chunk 后卸载")

                        if degenerate_exc is not None:
                            sample_key = json.dumps(
                                degenerate_exc.sample_id,
                                ensure_ascii=False,
                                sort_keys=True,
                                separators=(',', ':'),
                            )
                            reload_count = degenerate_reload_counts.get(sample_key, 0) + 1
                            degenerate_reload_counts[sample_key] = reload_count
                            degenerate_history.setdefault(sample_key, []).append({
                                'failed_instance_number': reload_count,
                                'attempts': _degenerate_attempt_audit(degenerate_exc.prediction),
                            })
                            if reload_count <= MAX_DEGENERATE_RELOADS_PER_SAMPLE:
                                checkpoint.mark_status(
                                    'reload_required',
                                    error=(
                                        f"{run['run_id']} id={degenerate_exc.sample_id!r} "
                                        f"检测到跑满长度的循环输出；准备第 {reload_count}/"
                                        f"{MAX_DEGENERATE_RELOADS_PER_SAMPLE} 次全新实例重试。"
                                    ),
                                )
                                LOGGER.warning(
                                    '%s id=%r 检测到循环输出；模型已卸载，将用全新实例重试同一样本（%s/%s）。',
                                    run['run_id'], degenerate_exc.sample_id, reload_count,
                                    MAX_DEGENERATE_RELOADS_PER_SAMPLE,
                                )
                                continue

                            exhausted_prediction = dict(degenerate_exc.prediction)
                            exhausted_prediction['error_type'] = 'degenerate_generation_loop_exhausted'
                            exhausted_prediction['error_message'] = (
                                f'初始实例及 {MAX_DEGENERATE_RELOADS_PER_SAMPLE} 次全新实例均产生循环输出'
                            )
                            exhausted_prediction['generation_recovery_reload_count'] = (
                                MAX_DEGENERATE_RELOADS_PER_SAMPLE
                            )
                            exhausted_prediction['generation_recovery_failures'] = (
                                degenerate_history[sample_key]
                            )
                            checkpoint.append(degenerate_exc.sample_id, exhausted_prediction)
                            LOGGER.error(
                                '%s id=%r 连续循环输出；达到自动重载上限，保存可审计失败并继续。',
                                run['run_id'], degenerate_exc.sample_id,
                            )
                            continue
                        LOGGER.info(
                            '%s chunk 完成：checkpoint=%s/%s，remaining=%s',
                            run['run_id'], len(checkpoint), len(samples), checkpoint.remaining_count,
                        )


                def _build_report_from_checkpoint(
                    run: dict[str, Any],
                    samples: list[dict[str, Any]],
                    checkpoint: PredictionCheckpoint,
                    resumed_samples: int,
                ) -> dict[str, Any]:
                    if checkpoint.remaining_count != 0:
                        raise RuntimeError(f"{run['run_id']} checkpoint 尚未完成，不能生成最终报告。")

                    def cached_generator(**kwargs: Any) -> dict[str, Any]:
                        prediction = checkpoint.get(kwargs.get('sample_id'))
                        if prediction is None:
                            raise RuntimeError(f"Checkpoint 缺少 id={kwargs.get('sample_id')!r}")
                        return prediction

                    metadata_path = None
                    embeddings_path = None
                    retriever = None
                    if run['use_rag']:
                        metadata_path, embeddings_path = resolve_rag_cache_paths(run['rag_database'])
                        retriever = RAG_RETRIEVERS[run['rag_database']]
                    config = EvalRunConfig(
                        project_root=PROJECT_ROOT,
                        model=run['model_key'],
                        dataset=run['dataset_name'],
                        prompt_name=run['prompt_name'],
                        use_rag=run['use_rag'],
                        rag_mode=run['rag_mode'],
                        rag_top_k=run['rag_top_k'],
                        temperature=TEMPERATURE,
                        max_tokens=MAX_TOKENS,
                        primary_metric=PRIMARY_METRIC,
                        progress_every=EVAL_PROGRESS_EVERY,
                        max_workers=EVAL_MAX_WORKERS,
                        llm_provider='lmstudio',
                        llm_base_url=LMSTUDIO_BASE_URL,
                        context_length=CONTEXT_LENGTH,
                        reasoning_effort=None,
                        llm_extra_body={'cache_prompt': CACHE_PROMPT},
                        api_key_source='lmstudio-default',
                        save_report=True,
                        report_dir=REPORT_DIR,
                        report_detail_limit=200,
                        report_detail_mode='errors',
                        report_error_metric=PRIMARY_METRIC,
                        metadata_path=metadata_path,
                        embeddings_path=embeddings_path,
                    )
                    report = run_stream_eval(
                        samples=samples,
                        label=f"{run['display_name']} {run['dataset_name']} {run['configuration']}",
                        client=object(),
                        config=config,
                        generator=cached_generator,
                        existing_retriever=retriever,
                        progress_factory=_notebook_progress,
                        emit=LOGGER.info,
                    )
                    report['checkpoint_path'] = str(checkpoint.predictions_path)
                    report['checkpoint_resumed_samples'] = resumed_samples
                    checkpoint.mark_status('complete', report_path=str(report['report_path']))
                    return report


                def _summary_row(
                    run: dict[str, Any],
                    report: dict[str, Any],
                ) -> dict[str, Any]:
                    detection = report['detection']
                    strict = report['extraction']['strict_token_f1']
                    anchor = report['extraction']['anchor_window']
                    return {
                        'status': 'completed',
                        'protocol': 'qwen_family_three_datasets_anchor_rerun_v1',
                        'run_id': run['run_id'],
                        'dataset': run['dataset_name'],
                        'split': run['split'],
                        'model': run['display_name'],
                        'model_key': run['model_key'],
                        'configuration': run['configuration'],
                        'prompt': run['prompt_name'],
                        'primary_metric': report['extraction']['primary_metric'],
                        'use_rag': run['use_rag'],
                        'rag_database': run['rag_database'] if run['use_rag'] else '',
                        'rag_mode': run['rag_mode'],
                        'rag_top_k': run['rag_top_k'],
                        'phase2_selected_k': SELECTED_K,
                        'total_examples': run['total_examples'],
                        'temperature': TEMPERATURE,
                        'context_length': CONTEXT_LENGTH,
                        'max_tokens': MAX_TOKENS,
                        'parallel': MODEL_PARALLEL,
                        'cache_prompt': CACHE_PROMPT,
                        'reload_every_samples': MODEL_RELOAD_EVERY_SAMPLES,
                        'max_degenerate_reloads_per_sample': MAX_DEGENERATE_RELOADS_PER_SAMPLE,
                        'detection_accuracy': detection['accuracy'],
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


                def _failed_row(
                    run: dict[str, Any],
                    exc: BaseException,
                    checkpoint: PredictionCheckpoint | None,
                ) -> dict[str, Any]:
                    return {
                        'status': 'interrupted' if isinstance(exc, (FatalGenerationError, KeyboardInterrupt)) else 'failed',
                        'protocol': 'qwen_family_three_datasets_anchor_rerun_v1',
                        'run_id': run['run_id'],
                        'dataset': run['dataset_name'],
                        'split': run['split'],
                        'model': run['display_name'],
                        'model_key': run['model_key'],
                        'configuration': run['configuration'],
                        'prompt': run['prompt_name'],
                        'primary_metric': PRIMARY_METRIC,
                        'use_rag': run['use_rag'],
                        'rag_database': run['rag_database'] if run['use_rag'] else '',
                        'rag_mode': run['rag_mode'],
                        'rag_top_k': run['rag_top_k'],
                        'phase2_selected_k': SELECTED_K,
                        'cache_prompt': CACHE_PROMPT,
                        'reload_every_samples': MODEL_RELOAD_EVERY_SAMPLES,
                        'max_degenerate_reloads_per_sample': MAX_DEGENERATE_RELOADS_PER_SAMPLE,
                        'checkpoint_path': str(checkpoint.predictions_path) if checkpoint else '',
                        'checkpoint_completed_samples': len(checkpoint) if checkpoint else 0,
                        'error': f'{type(exc).__name__}: {exc}',
                    }


                def _save_summary(rows: list[dict[str, Any]]) -> None:
                    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    order = [run['run_id'] for run in RUN_MATRIX]
                    frame = pd.DataFrame(rows)
                    if not frame.empty:
                        frame['_order'] = pd.Categorical(frame['run_id'], categories=order, ordered=True)
                        frame = frame.sort_values('_order').drop(columns='_order')
                    frame.to_csv(SUMMARY_PATH, index=False, encoding='utf-8-sig')
                    LOGGER.info('增量汇总已保存：%s', SUMMARY_PATH)


                def _load_completed_rows() -> list[dict[str, Any]]:
                    if not SUMMARY_PATH.is_file():
                        return []
                    frame = pd.read_csv(SUMMARY_PATH)
                    if frame.empty:
                        return []
                    completed = frame.loc[frame['status'] == 'completed'].copy()
                    if completed.empty:
                        return []
                    if set(completed['protocol'].astype(str)) != {
                        'qwen_family_three_datasets_anchor_rerun_v1'
                    }:
                        raise RuntimeError('现有 summary 混入其他协议。')
                    if set(completed['phase2_selected_k'].astype(int)) != {SELECTED_K}:
                        raise RuntimeError('现有 summary 的 selected k 与当前 Phase 2 结果不一致。')
                    valid_ids = {run['run_id'] for run in RUN_MATRIX}
                    completed = completed.loc[completed['run_id'].isin(valid_ids)]
                    return completed.drop_duplicates(subset='run_id', keep='last').to_dict(orient='records')


                def run_all_12() -> list[dict[str, Any]]:
                    rows = _load_completed_rows()
                    completed_ids = {row['run_id'] for row in rows}
                    pending_runs = [run for run in RUN_MATRIX if run['run_id'] not in completed_ids]
                    LOGGER.info('12-run 状态：completed=%s pending=%s', len(completed_ids), len(pending_runs))

                    for position, run in enumerate(pending_runs, 1):
                        checkpoint: PredictionCheckpoint | None = None
                        try:
                            samples = DATASETS[run['dataset_key']]
                            LOGGER.info(
                                '[run %s/%s] %s：samples=%s',
                                position, len(pending_runs), run['run_id'], len(samples),
                            )
                            checkpoint = _open_checkpoint(run, samples)
                            resumed_samples = len(checkpoint)
                            _complete_predictions(run, samples, checkpoint)
                            report = _build_report_from_checkpoint(
                                run, samples, checkpoint, resumed_samples,
                            )
                            rows = [row for row in rows if row.get('run_id') != run['run_id']]
                            rows.append(_summary_row(run, report))
                        except KeyboardInterrupt as exc:
                            if checkpoint is not None:
                                checkpoint.mark_status('interrupted', error='KeyboardInterrupt')
                            rows = [row for row in rows if row.get('run_id') != run['run_id']]
                            rows.append(_failed_row(run, exc, checkpoint))
                            _save_summary(rows)
                            LOGGER.warning('用户中断；当前 sample 之前的预测已保存。')
                            raise
                        except FatalGenerationError as exc:
                            rows = [row for row in rows if row.get('run_id') != run['run_id']]
                            rows.append(_failed_row(run, exc, checkpoint))
                            _save_summary(rows)
                            LOGGER.error('基础设施故障，整批停止：%s', exc)
                            break
                        except Exception as exc:
                            if checkpoint is not None:
                                checkpoint.mark_status(
                                    'interrupted', error=f'{type(exc).__name__}: {exc}',
                                )
                            rows = [row for row in rows if row.get('run_id') != run['run_id']]
                            rows.append(_failed_row(run, exc, checkpoint))
                            LOGGER.exception('%s 失败；记录后继续下一 run。', run['run_id'])
                        _save_summary(rows)
                    return rows
                """
            ),
            id="run-helpers",
        ),
        nbf.v4.new_code_cell(
            _source(
                """
                # ===== 4. 执行 12 轮；相同 summary/checkpoint 自动续跑 =====
                if not RUN_BATCH:
                    LOGGER.warning(
                        'RUN_BATCH=False：当前只完成配置与预检。确认矩阵后改为 True，重启 kernel 并从第一格运行。'
                    )
                    display(pd.DataFrame(RUN_MATRIX)[[
                        'run_id', 'dataset_name', 'display_name', 'configuration',
                        'prompt_name', 'rag_top_k', 'total_examples',
                    ]])
                else:
                    ALL_RESULTS = run_all_12()
                    results_df = pd.DataFrame(ALL_RESULTS)
                    display(results_df)
                    completed_df = results_df.loc[results_df['status'] == 'completed'].copy()
                    completed_ids = set(completed_df['run_id'].astype(str))
                    expected_ids = {run['run_id'] for run in RUN_MATRIX}
                    if completed_ids != expected_ids:
                        missing = sorted(expected_ids - completed_ids)
                        raise RuntimeError(
                            f'12 轮尚未全部完成：missing={missing}。已有 checkpoint 可直接续跑。'
                        )

                    comparison = completed_df[[
                        'dataset', 'model', 'configuration', 'rag_top_k',
                        'detection_f1', 'anchor_all_f1', 'strict_all_f1',
                        'generation_failures', 'parse_repairs',
                    ]].sort_values(['dataset', 'model', 'configuration'])
                    display(comparison)
                    LOGGER.info('12 轮全部完成：%s', SUMMARY_PATH)
                """
            ),
            id="run-all-12",
        ),
    ]
    for cell in notebook.cells:
        if cell.cell_type == "code":
            cell.execution_count = None
            cell.outputs = []
    return notebook


def main() -> None:
    notebook = build_notebook()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(notebook, OUTPUT_PATH)
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
