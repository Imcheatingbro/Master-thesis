"""Demo1：Qwen3.6 27B CNC RAG 消融 Phase 2 notebook 的结构测试。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "lmstudio_rag_ablation_phase2_qwen27.ipynb"
FIXED_PROMPT_PATH = PROJECT_ROOT / "prompts" / "v9.6.txt"


def _load_notebook() -> dict[str, Any]:
    return json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))


def _cells_by_id(notebook: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(cell["id"]): cell for cell in notebook["cells"]}


def test_qwen27_phase2_notebook_code_cells_compile() -> None:
    notebook = _load_notebook()

    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            compile("".join(cell["source"]), f"{NOTEBOOK_PATH.name}:cell{index}", "exec")


def test_qwen27_phase2_notebook_uses_matching_ablation_grid() -> None:
    cells = _cells_by_id(_load_notebook())
    config_source = "".join(cells["global-config"]["source"])
    preflight_source = "".join(cells["preflight"]["source"])
    helper_source = "".join(cells["phase2-helper"]["source"])
    run_source = "".join(cells["run-phase2"]["source"])

    assert "MODEL_KEY = 'local/qwen3.6-27b-no-thinking'" in config_source
    assert "MODEL_DISPLAY_NAME = 'Qwen3.6 27B No Thinking'" in config_source
    assert "FIXED_PROMPT = 'v9.6'" in config_source
    assert "ZERO_SHOT_PROMPT = 'v9.6_zero_shot'" in config_source
    assert "DATASET_NAME = 'cnc_sft_validation'" in config_source
    assert "K_VALUES = (1, 3, 5)" in config_source
    assert "MODEL_PARALLEL = 1" in config_source
    assert "OFFLOAD_KV_CACHE_TO_GPU = True" in config_source
    assert "'configuration': 'fixed'" in config_source
    assert "'configuration': 'RAG only'" in config_source
    assert "'configuration': 'fixed + random'" in config_source
    assert "'configuration': 'fixed + RAG'" in config_source
    assert "'dynamic_examples': 2 * k" in config_source
    assert "'total_examples': 10 + 2 * k" in config_source
    assert "RUN_PHASE2 = False" in config_source
    assert "gemma-4-31b" not in config_source.lower()

    assert "validation_ids.intersection(support_ids)" in preflight_source
    assert "fixed_template.count('\\nInput:\\n') != 10" in preflight_source
    assert "zero_template.count('\\nInput:\\n') != 0" in preflight_source
    assert "fixed_template.count('{rag_examples}') != 1" in preflight_source
    assert "messages = build_messages(" in preflight_source
    assert "inserted_examples != 2 * k" in preflight_source

    assert "parallel=parallel" in helper_source
    assert "offload_kv_cache_to_gpu=OFFLOAD_KV_CACHE_TO_GPU" in helper_source
    assert "context_length: int = CONTEXT_LENGTH" in helper_source
    assert "parallel: int = MODEL_PARALLEL" in helper_source
    assert "actual_parallel != parallel" in helper_source
    assert "actual_context != context_length" in helper_source
    assert "inventory_context != context_length" in helper_source
    assert "inventory_parallel != parallel" in helper_source
    assert "primary_metric='strict_token_f1'" in helper_source
    assert "report_error_metric='strict_token_f1'" in helper_source
    assert "phase2_qwen27_summary.csv" in helper_source
    assert "run_phase2(EXPERIMENT_RUNS)" in run_source


def test_qwen27_fixed_prompt_has_one_dynamic_example_slot() -> None:
    prompt = FIXED_PROMPT_PATH.read_text(encoding="utf-8")

    assert prompt.count("\nInput:\n") == 10
    assert prompt.count("{rag_examples}") == 1


def test_qwen27_phase2_notebook_has_scoped_six_run_rerun() -> None:
    cells = _cells_by_id(_load_notebook())
    config_source = "".join(cells["global-config"]["source"])
    helper_source = "".join(cells["phase2-helper"]["source"])
    rerun_config_source = "".join(cells["rerun-config"]["source"])
    rerun_source = "".join(cells["run-phase2-reruns"]["source"])
    rerun_ids_source = rerun_config_source.split("RERUN_SUMMARY_PATH", maxsplit=1)[0]

    assert "RUN_PHASE2 = False" in config_source
    assert "summary_path: Path = SUMMARY_PATH" in helper_source
    assert "_save_summary(rows, summary_path)" in helper_source
    assert "RERUN_RUN_IDS = (" in rerun_config_source
    assert rerun_ids_source.count("'fixed_random_k") == 3
    assert rerun_ids_source.count("'fixed_rag_k") == 3
    assert "'fixed'" not in rerun_ids_source
    assert "'rag_only_k" not in rerun_ids_source
    assert "phase2_qwen27_rerun_summary.csv" in rerun_config_source
    assert "phase2_qwen27_corrected_summary.csv" in rerun_config_source
    assert "RUN_PHASE2_RERUN = False" in rerun_config_source
    assert "run_phase2(" in rerun_source
    assert "RERUN_EXPERIMENT_RUNS" in rerun_source
    assert "summary_path=RERUN_SUMMARY_PATH" in rerun_source
    assert "original_summary_df['run_id'].isin(VALID_ORIGINAL_RUN_IDS)" in rerun_source
    assert "corrected_summary_df.to_csv(" in rerun_source


def test_qwen27_phase2_notebook_has_fixed_rag_k5_only_rerun() -> None:
    cells = _cells_by_id(_load_notebook())
    config_source = "".join(cells["fixed-rag-k5-rerun-config"]["source"])
    run_source = "".join(cells["run-fixed-rag-k5-rerun"]["source"])

    assert "FIXED_RAG_K5_CONTEXT_LENGTH = 8192" in config_source
    assert "FIXED_RAG_K5_PARALLEL = 4" in config_source
    assert "runs_by_id['fixed_rag_k5'].copy()" in config_source
    assert "RUN_FIXED_RAG_K5_RERUN = False" in config_source
    assert "phase2_qwen27_fixed_rag_k5_rerun_summary.csv" in config_source

    assert "[FIXED_RAG_K5_RUN]" in run_source
    assert "context_length=FIXED_RAG_K5_CONTEXT_LENGTH" in run_source
    assert "parallel=FIXED_RAG_K5_PARALLEL" in run_source
    assert "fixed_rag_k5_df.iloc[0]['status'] != 'completed'" in run_source
    assert "previous_rerun_df['run_id'] != 'fixed_rag_k5'" in run_source
    assert "set(phase2_rerun_summary_df['run_id']) != set(RERUN_RUN_IDS)" in run_source
    assert "RERUN_SUMMARY_PATH" in run_source
    assert "CORRECTED_SUMMARY_PATH" in run_source
