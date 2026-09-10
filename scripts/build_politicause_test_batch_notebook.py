"""Generate the frozen eight-run PolitiCAUSE test notebook."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from textwrap import dedent
from types import ModuleType


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BASE_BUILDER_PATH = PROJECT_ROOT / "scripts" / "build_qwen_family_three_dataset_notebook.py"
OUTPUT_PATH = PROJECT_ROOT / "notebooks" / "lmstudio_batch_politicause_test.ipynb"


def _source(text: str) -> str:
    return dedent(text).strip() + "\n"


def _load_base_builder() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "build_qwen_family_three_dataset_notebook",
        BASE_BUILDER_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load notebook builder: {BASE_BUILDER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _overview_source() -> str:
    return _source(
        """
        # PolitiCAUSE Test：四模型 × Fixed/RAG k=1（8 轮冻结评测）

        本 notebook 只用于冻结后的 PolitiCAUSE Test。它依次执行 4 个模型 × 2 种条件，
        共 8 个逻辑实验：

        - Fixed：冻结的 10-shot `politicause_v1_final` Prompt，RAG 关闭；
        - Fixed + RAG：同一 Prompt，PolitiCAUSE train-only KNN+Pattern RAG，k=1；
        - Qwen 与 Gemma 两个家族均使用已经确定的 k=1；
        - 主指标为 `anchor_window`，`strict_token_f1` 作为辅助指标；
        - Test 固定为 860 条（245 正、615 负），运行后不得依据 Test 修改 Prompt。

        冻结保护：启动时校验 Prompt、Test 数据、RAG metadata 和 embedding 的 SHA-256，
        并检查 RAG support 全部来自 train 且与 Test 无 ID/文本重叠。任何漂移都会拒绝运行。

        稳定性协议：每条预测立即写入带运行签名的 checkpoint；`cache_prompt=False`；
        生成进度条始终以完整 Test 的 860 条为分母；每生成 500 条卸载并重新加载当前模型，
        但进度条不会归零。连接故障不保存 False 兜底，而是停止整批。
        若检测到接近 `MAX_TOKENS` 的循环输出，则立即重载模型并从同一 sample 重试；
        单样本最多自动重载 3 次。中断后重启 kernel，从第一格顺序运行即可按 sample ID 续跑。

        `RUN_BATCH=True` 已按最终协议锁定。运行全部单元格即可开始正式 Test。
        """
    )


def _config_source() -> str:
    return _source(
        """
        # ===== 1. 冻结协议与全局配置 =====
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
        from src.prompt_builder import USER_PREFIX_BY_PROMPT, load_prompt_template
        from src.retriever import (
            ExactCountHybridRetriever,
            KNNRetriever,
            PatternRetriever,
            resolve_rag_cache_paths,
        )

        logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
        LOGGER = logging.getLogger('lmstudio_batch_politicause_test')
        logging.getLogger('src.llm_client').setLevel(logging.WARNING)


        class _NotebookProgress:
            def __init__(self, *, total: int, desc: str, initial: int = 0) -> None:
                self.total = total
                self.safe_total = max(total, 1)
                self.safe_desc = escape(desc)
                self.handle = display(self._render(initial), display_id=True)

            def _render(self, completed: int) -> HTML:
                bounded = min(max(completed, 0), self.total)
                percent = min(bounded / self.safe_total * 100, 100.0)
                return HTML(
                    f"<div style='width:100%'>"
                    f"<div>{self.safe_desc}: {bounded}/{self.total} ({percent:.1f}%)</div>"
                    f"<progress value='{bounded}' max='{self.safe_total}' "
                    f"style='width:100%;height:18px'></progress></div>"
                )

            def update(self, completed: int) -> None:
                if self.handle is not None:
                    self.handle.update(self._render(completed))


        def _notebook_progress(
            iterable: Iterable[Any],
            *,
            total: int,
            desc: str,
        ) -> Iterator[Any]:
            progress = _NotebookProgress(total=total, desc=desc)
            for completed, item in enumerate(iterable, 1):
                yield item
                progress.update(completed)


        PROTOCOL = 'politicause_test_frozen_v1'
        DATASET_KEY = 'politicause'
        DATASET_NAME = 'politicause'
        SPLIT = 'test'
        PROMPT_NAME = 'politicause_v1_final'
        RAG_DATABASE = 'politicause'
        SELECTED_K = 1
        FIXED_EXAMPLE_COUNT = 10

        FROZEN_PROMPT_SHA256 = '94c51591193869e0026230836213c843557e2bcc0eb78be40f7c1ec873575272'
        FROZEN_DATASET_SHA256 = '2edf4dcf76cb269572c9cc69dae8774b88a58168f1e9849f1df584b226ff0001'
        FROZEN_RAG_METADATA_SHA256 = '2b0b7c577f62fa54456432c6ce57cc4f48c31b38dcd7f0ffacced0c051516983'
        FROZEN_RAG_EMBEDDINGS_SHA256 = 'e1b4ffd8c0511459ba0a19a9f9ddfbcdf1cd4f77869d75be9a734b21a5183aca'
        EXPECTED_DATASET_STATS = {
            'samples': 860,
            'positive': 245,
            'negative': 615,
            'relations': 245,
            'max_relations': 1,
        }

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
        RUN_BATCH = True

        REPORT_DIR = Path('results') / 'eval_report' / 'politicause_test_final_v1'
        CHECKPOINT_DIR = Path('results') / 'eval_checkpoints' / 'politicause_test_final_v1'
        SUMMARY_PATH = PROJECT_ROOT / REPORT_DIR / 'politicause_test_8runs_summary.csv'

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
            {
                'model_id': 'gemma26',
                'display_name': 'Gemma 4 26B A4B QAT',
                'model_key': 'google/gemma-4-26b-a4b-qat',
            },
            {
                'model_id': 'gemma31',
                'display_name': 'Gemma 4 31B QAT',
                'model_key': 'google/gemma-4-31b-qat',
            },
        ]

        RUN_MATRIX: list[dict[str, Any]] = []
        for model_config in MODEL_CONFIGS:
            for use_rag in (False, True):
                condition = 'fixed_rag' if use_rag else 'fixed'
                run = {
                    **model_config,
                    'dataset_key': DATASET_KEY,
                    'dataset_name': DATASET_NAME,
                    'split': SPLIT,
                    'prompt_name': PROMPT_NAME,
                    'condition': condition,
                    'configuration': 'Fixed + RAG' if use_rag else 'Fixed',
                    'use_rag': use_rag,
                    'rag_database': RAG_DATABASE,
                    'rag_mode': 'knn_pattern' if use_rag else 'off',
                    'rag_top_k': SELECTED_K if use_rag else 0,
                    'total_examples': FIXED_EXAMPLE_COUNT + (2 * SELECTED_K if use_rag else 0),
                }
                run['run_id'] = (
                    f"politicause_{run['model_id']}_{condition}"
                    + (f"_k{SELECTED_K}" if use_rag else '')
                )
                RUN_MATRIX.append(run)

        if len(RUN_MATRIX) != 8 or len({run['run_id'] for run in RUN_MATRIX}) != 8:
            raise RuntimeError('冻结运行矩阵必须包含 8 个唯一 run。')

        display(pd.DataFrame(MODEL_CONFIGS))
        display(pd.DataFrame(RUN_MATRIX)[[
            'run_id', 'display_name', 'configuration', 'prompt_name',
            'rag_database', 'rag_top_k', 'total_examples',
        ]])
        """
    )


def _preflight_source() -> str:
    return _source(
        """
        # ===== 2. Prompt、Test、RAG 隔离与四模型预检 =====
        def _sha256_bytes(path: Path) -> str:
            return hashlib.sha256(path.read_bytes()).hexdigest()


        def _canonical_dataset_sha256(samples: list[dict[str, Any]]) -> str:
            payload = json.dumps(
                samples, ensure_ascii=False, sort_keys=True, separators=(',', ':'),
            )
            return hashlib.sha256(payload.encode('utf-8')).hexdigest()


        def _normalize_overlap_text(value: Any) -> str:
            without_tags = re.sub(
                r'</?(?:cause|effect)>', '', str(value or ''), flags=re.IGNORECASE,
            )
            return ' '.join(without_tags.casefold().split())


        prompt_path = PROJECT_ROOT / 'prompts' / f'{PROMPT_NAME}.txt'
        prompt_text = load_prompt_template(PROMPT_NAME)
        actual_prompt_sha256 = hashlib.sha256(prompt_text.encode('utf-8')).hexdigest()
        if actual_prompt_sha256 != FROZEN_PROMPT_SHA256:
            raise RuntimeError(
                f'冻结 Prompt 漂移：{actual_prompt_sha256} != {FROZEN_PROMPT_SHA256}'
            )
        if _sha256_bytes(prompt_path) != FROZEN_PROMPT_SHA256:
            raise RuntimeError('冻结 Prompt 文件字节哈希不匹配。')
        if prompt_text.count('{rag_examples}') != 1:
            raise RuntimeError('冻结 Prompt 必须恰好包含一个 RAG 插槽。')
        if len(re.findall(r'(?m)^Example [0-9]+$', prompt_text)) != FIXED_EXAMPLE_COUNT:
            raise RuntimeError('冻结 Prompt 的 fixed example 数量不是 10。')
        if PROMPT_NAME in USER_PREFIX_BY_PROMPT:
            raise RuntimeError(
                '冻结验证协议使用原始 user text；不能为该 Prompt 静默加入 Input text 前缀。'
            )

        samples = load_dataset(DATASET_NAME)
        dataset_stats = {
            'samples': len(samples),
            'positive': sum(bool(sample['has_causal']) for sample in samples),
            'negative': sum(not bool(sample['has_causal']) for sample in samples),
            'relations': sum(len(sample.get('relations', [])) for sample in samples),
            'max_relations': max(len(sample.get('relations', [])) for sample in samples),
        }
        if dataset_stats != EXPECTED_DATASET_STATS:
            raise RuntimeError(
                f'PolitiCAUSE Test 数据规模漂移：{dataset_stats} != {EXPECTED_DATASET_STATS}'
            )
        actual_dataset_sha256 = _canonical_dataset_sha256(samples)
        if actual_dataset_sha256 != FROZEN_DATASET_SHA256:
            raise RuntimeError(
                f'PolitiCAUSE Test 内容漂移：{actual_dataset_sha256} != {FROZEN_DATASET_SHA256}'
            )
        if len({str(sample['id']) for sample in samples}) != len(samples):
            raise RuntimeError('PolitiCAUSE Test 存在重复 sample id。')
        if any(
            len(sample.get('relations', [])) != (1 if sample['has_causal'] else 0)
            for sample in samples
        ):
            raise RuntimeError('PolitiCAUSE Test 不再满足负例 0 关系、正例严格 1C+1E。')

        metadata_path, embeddings_path = resolve_rag_cache_paths(RAG_DATABASE)
        if _sha256_bytes(metadata_path) != FROZEN_RAG_METADATA_SHA256:
            raise RuntimeError('PolitiCAUSE RAG metadata 漂移。')
        if _sha256_bytes(embeddings_path) != FROZEN_RAG_EMBEDDINGS_SHA256:
            raise RuntimeError('PolitiCAUSE RAG embeddings 漂移。')
        metadata_rows = [
            json.loads(line)
            for line in metadata_path.read_text(encoding='utf-8').splitlines()
            if line.strip()
        ]
        if len(metadata_rows) != 1000:
            raise RuntimeError(f'PolitiCAUSE RAG support 不是 1000 条：{len(metadata_rows)}')
        if any(
            row.get('source_split') != 'train'
            or int(row.get('relation_count', 0)) != 1
            or len(row.get('triples', [])) != 1
            for row in metadata_rows
        ):
            raise RuntimeError('PolitiCAUSE RAG support 混入非 train 或非单关系样本。')

        manifest_path = PROJECT_ROOT / 'RAG Database' / 'politicause_split_manifest.json'
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        manifest_summary = manifest.get('summary', {})
        if (
            int(manifest_summary.get('support_samples', -1)) != 1000
            or int(manifest_summary.get('validation_test_id_overlap', -1)) != 0
            or int(manifest_summary.get('validation_test_text_overlap', -1)) != 0
            or int(manifest_summary.get('rows_without_pattern', -1)) != 0
        ):
            raise RuntimeError('PolitiCAUSE RAG manifest 未通过 train-only/held-out 隔离检查。')

        test_ids = {str(sample['id']) for sample in samples}
        support_ids = {str(row['sample_id']) for row in metadata_rows}
        if test_ids & support_ids:
            raise RuntimeError('PolitiCAUSE RAG support 与 Test 存在 sample id 重叠。')
        test_texts = {_normalize_overlap_text(sample['text']) for sample in samples}
        support_texts = {_normalize_overlap_text(row['sentence']) for row in metadata_rows}
        if test_texts & support_texts:
            raise RuntimeError('PolitiCAUSE RAG support 与 Test 存在规范化文本重叠。')

        retriever = ExactCountHybridRetriever(
            pattern_retriever=PatternRetriever(metadata_path=metadata_path),
            knn_retriever=KNNRetriever(
                metadata_path=metadata_path,
                embeddings_path=embeddings_path,
                device='cpu',
            ),
        )
        probe = retriever.retrieve(
            'Heavy rain caused flooding in the region.',
            top_k=SELECTED_K,
        )
        if len(probe) != 2 * SELECTED_K:
            raise RuntimeError('KNN+Pattern RAG 未严格返回 2k 个动态 examples。')

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
            reasoning = inventory_by_key[model['model_key']].get('capabilities', {}).get(
                'reasoning', {}
            )
            allowed = reasoning.get('allowed_options', [])
            if allowed and 'off' not in allowed:
                raise RuntimeError(f"{model['model_key']} 不支持 reasoning=off。")

        DATASETS = {DATASET_KEY: samples}
        RAG_RETRIEVERS = {RAG_DATABASE: retriever}

        display(pd.DataFrame([{'dataset': DATASET_NAME, **dataset_stats}]))
        display(pd.DataFrame([{
            'prompt': PROMPT_NAME,
            'prompt_sha256': actual_prompt_sha256,
            'raw_user_text_protocol': True,
            'fixed_examples': FIXED_EXAMPLE_COUNT,
        }]))
        display(pd.DataFrame([{
            'database': RAG_DATABASE,
            'support_samples': len(metadata_rows),
            'selected_k': SELECTED_K,
            'dynamic_examples': len(probe),
            'test_id_overlap': 0,
            'test_text_overlap': 0,
        }]))
        LOGGER.info(
            '冻结预检通过：8 runs，Test=%s（%s 正/%s 负），RAG k=%s，cache_prompt=%s。',
            dataset_stats['samples'], dataset_stats['positive'], dataset_stats['negative'],
            SELECTED_K, CACHE_PROMPT,
        )
        """
    )


def _helper_source(base_source: str) -> str:
    source = base_source
    replacements = {
        '# ===== 3. 逐样本 checkpoint、每 500 条重载、离线报告与汇总 =====':
            '# ===== 3. 逐样本 checkpoint、每 500 条重载、循环恢复与离线报告 =====',
        'qwen_family_three_datasets_anchor_rerun_v1': 'politicause_test_frozen_v1',
        'phase2_selected_k': 'selected_k',
        'run_all_12': 'run_all_8',
        '12-run 状态': '8-run 状态',
    }
    for old, new in replacements.items():
        if old not in source:
            raise RuntimeError(f'Base helper drifted; missing marker: {old}')
        source = source.replace(old, new)

    old_save = """    frame.to_csv(SUMMARY_PATH, index=False, encoding='utf-8-sig')
    LOGGER.info('增量汇总已保存：%s', SUMMARY_PATH)
"""
    new_save = """    temporary_summary = SUMMARY_PATH.with_suffix(SUMMARY_PATH.suffix + '.tmp')
    frame.to_csv(temporary_summary, index=False, encoding='utf-8-sig')
    temporary_summary.replace(SUMMARY_PATH)
    LOGGER.info('增量汇总已原子保存：%s', SUMMARY_PATH)
"""
    if old_save not in source:
        raise RuntimeError('Base helper summary writer drifted.')
    source = source.replace(old_save, new_save)

    old_read = """    frame = pd.read_csv(SUMMARY_PATH)
    if frame.empty:
        return []
"""
    new_read = """    try:
        frame = pd.read_csv(SUMMARY_PATH)
    except pd.errors.EmptyDataError:
        LOGGER.warning('发现历史空 summary；按无已完成 run 处理：%s', SUMMARY_PATH)
        return []
    if frame.empty:
        return []
"""
    if old_read not in source:
        raise RuntimeError('Base helper summary reader drifted.')
    source = source.replace(old_read, new_read)

    old_generate_header = """def _generate_chunk(
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
"""
    new_generate_header = """def _generate_chunk(
    run: dict[str, Any],
    chunk: list[dict[str, Any]],
    checkpoint: PredictionCheckpoint,
    client: LLMClient,
    retriever: Any,
    degenerate_reload_counts: dict[str, int],
    degenerate_history: dict[str, list[dict[str, Any]]],
    overall_progress: _NotebookProgress,
) -> None:
    for sample in chunk:
"""
    if old_generate_header not in source:
        raise RuntimeError('Base helper chunk progress header drifted.')
    source = source.replace(old_generate_header, new_generate_header)

    old_checkpoint_update = """        checkpoint.append(sample_id, prediction)
        if completed % 100 == 0:
"""
    new_checkpoint_update = """        checkpoint.append(sample_id, prediction)
        overall_progress.update(len(checkpoint))
        if len(checkpoint) % 100 == 0:
"""
    if old_checkpoint_update not in source:
        raise RuntimeError('Base helper checkpoint progress update drifted.')
    source = source.replace(old_checkpoint_update, new_checkpoint_update)

    old_progress_setup = """    degenerate_reload_counts: dict[str, int] = {}
    degenerate_history: dict[str, list[dict[str, Any]]] = {}
    while checkpoint.remaining_count > 0:
"""
    new_progress_setup = """    degenerate_reload_counts: dict[str, int] = {}
    degenerate_history: dict[str, list[dict[str, Any]]] = {}
    overall_progress = _NotebookProgress(
        total=len(samples),
        desc=f"{run['run_id']} generation",
        initial=len(checkpoint),
    )
    while checkpoint.remaining_count > 0:
"""
    if old_progress_setup not in source:
        raise RuntimeError('Base helper overall progress setup drifted.')
    source = source.replace(old_progress_setup, new_progress_setup)

    old_generate_call = """                degenerate_reload_counts,
                degenerate_history,
            )
"""
    new_generate_call = """                degenerate_reload_counts,
                degenerate_history,
                overall_progress,
            )
"""
    if old_generate_call not in source:
        raise RuntimeError('Base helper chunk call drifted.')
    source = source.replace(old_generate_call, new_generate_call)
    return source


def _execute_source() -> str:
    return _source(
        """
        # ===== 4. 执行 8 轮；相同 summary/checkpoint 自动续跑 =====
        if not RUN_BATCH:
            LOGGER.warning(
                'RUN_BATCH=False：当前只完成冻结预检。确认矩阵后改为 True，重启 kernel 并从第一格运行。'
            )
            display(pd.DataFrame(RUN_MATRIX)[[
                'run_id', 'display_name', 'configuration', 'prompt_name',
                'rag_top_k', 'total_examples',
            ]])
        else:
            ALL_RESULTS = run_all_8()
            results_df = pd.DataFrame(ALL_RESULTS)
            display(results_df)
            completed_df = results_df.loc[results_df['status'] == 'completed'].copy()
            completed_ids = set(completed_df['run_id'].astype(str))
            expected_ids = {run['run_id'] for run in RUN_MATRIX}
            if completed_ids != expected_ids:
                missing = sorted(expected_ids - completed_ids)
                raise RuntimeError(
                    f'8 轮尚未全部完成：missing={missing}。已有 checkpoint 可直接续跑。'
                )

            comparison = completed_df[[
                'model', 'configuration', 'rag_top_k',
                'detection_f1', 'anchor_all_f1', 'strict_all_f1',
                'anchor_detected_only_f1', 'generation_failures', 'parse_repairs',
            ]].sort_values(['model', 'configuration'])
            display(comparison)
            LOGGER.info('8 轮全部完成：%s', SUMMARY_PATH)
        """
    )


def build_notebook():
    base_builder = _load_base_builder()
    notebook = base_builder.build_notebook()
    if len(notebook.cells) != 5:
        raise RuntimeError(f"Unexpected base notebook cell count: {len(notebook.cells)}")

    notebook.cells[0].source = _overview_source()
    notebook.cells[0].id = 'overview'
    notebook.cells[1].source = _config_source()
    notebook.cells[1].id = 'frozen-config'
    notebook.cells[2].source = _preflight_source()
    notebook.cells[2].id = 'frozen-preflight'
    notebook.cells[3].source = _helper_source(notebook.cells[3].source)
    notebook.cells[3].id = 'checkpoint-runner'
    notebook.cells[4].source = _execute_source()
    notebook.cells[4].id = 'execute-eight-runs'

    for cell in notebook.cells:
        if cell.get('cell_type') == 'code':
            cell.execution_count = None
            cell.outputs = []
    return notebook, base_builder


def main() -> None:
    notebook, base_builder = build_notebook()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    base_builder.nbf.write(notebook, OUTPUT_PATH)
    print(OUTPUT_PATH)


if __name__ == '__main__':
    main()
