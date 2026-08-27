"""Demo1：LM Studio 四模型批量 smoke 与固定 test notebook 的结构测试。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "lmstudio_batch_cnc_test.ipynb"


def _load_notebook() -> dict[str, Any]:
    return json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))


def _cells_by_id(notebook: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(cell["id"]): cell for cell in notebook["cells"]}


def test_batch_notebook_code_cells_compile() -> None:
    notebook = _load_notebook()

    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            compile("".join(cell["source"]), f"{NOTEBOOK_PATH.name}:cell{index}", "exec")


def test_batch_notebook_separates_smoke_switching_from_guarded_formal_eval() -> None:
    cells = _cells_by_id(_load_notebook())
    config_source = "".join(cells["global-config"]["source"])
    smoke_source = "".join(cells["run-smoke-batch"]["source"])
    formal_source = "".join(cells["run-formal-batch"]["source"])
    smoke_helper_source = "".join(cells["smoke-helper"]["source"])
    eval_helper_source = "".join(cells["eval-helper"]["source"])

    expected_model_keys = {
        "google/gemma-4-31b-qat",
        "qwen/qwen3.6-35b-a3b",
        "google/gemma-4-26b-a4b-qat",
        "local/qwen3.6-27b-no-thinking",
    }
    assert all(model_key in config_source for model_key in expected_model_keys)
    expected_order = [
        "qwen/qwen3.6-35b-a3b",
        "local/qwen3.6-27b-no-thinking",
        "google/gemma-4-26b-a4b-qat",
        "google/gemma-4-31b-qat",
    ]
    positions = [config_source.index(model_key) for model_key in expected_order]
    assert positions == sorted(positions)
    assert "DATASET_NAME = 'cnc_sft_test'" in config_source
    assert "RUN_BATCH_EVAL =" in config_source
    assert "logging.getLogger('src.llm_client').setLevel(logging.WARNING)" in config_source
    assert "def _notebook_progress(" in config_source
    assert "from tqdm.auto import tqdm" not in config_source
    assert "run_smoke_batch(MODEL_RUNS, manager)" in smoke_source
    assert "reasoning='off'" in smoke_helper_source
    assert "lmstudio.unload_all_models()" in smoke_helper_source
    assert "reasoning='off'" not in eval_helper_source
    assert "llm_extra_body=None" in eval_helper_source
    assert "progress_factory=_notebook_progress" in eval_helper_source
    assert "if not RUN_BATCH_EVAL" in formal_source
    assert "run_formal_batch(MODEL_RUNS)" in formal_source


def test_batch_notebook_blocks_overlapping_cnc_rag_on_fixed_test() -> None:
    cells = _cells_by_id(_load_notebook())
    eval_helper_source = "".join(cells["eval-helper"]["source"])

    assert "Data/CNC_sft/split_manifest.json" in eval_helper_source
    assert "RAG Database/cnc_split_manifest.json" in eval_helper_source
    assert "support 与 test" in eval_helper_source


def test_batch_notebook_appends_qwen_family_validation_selected_rag3_test() -> None:
    cells = _cells_by_id(_load_notebook())
    config_source = "".join(cells["global-config"]["source"])
    eval_helper_source = "".join(cells["eval-helper"]["source"])
    rag3_config_source = "".join(cells["qwen-rag3-test-config"]["source"])
    rag3_run_source = "".join(cells["run-qwen-rag3-test"]["source"])

    assert "RUN_BATCH_EVAL = False" in config_source
    assert "existing_retrievers: dict[str, Any] | None = None" in eval_helper_source
    assert "primary_metric=str(run.get('primary_metric', 'anchor_window'))" in eval_helper_source
    assert "existing_retriever=(existing_retrievers or {}).get(run_id)" in eval_helper_source
    assert "parallel=None if run_parallel is None else int(run_parallel)" in eval_helper_source
    assert "def generate_with_periodic_reload(" in eval_helper_source
    assert "completed_samples % reload_every_samples == 0" in eval_helper_source
    assert "manager.unload_all_models()" in eval_helper_source

    assert "QWEN_FAMILY_RAG3_TEST_RUNS" in rag3_config_source
    assert "qwen/qwen3.6-35b-a3b" in rag3_config_source
    assert "local/qwen3.6-27b-no-thinking" in rag3_config_source
    assert rag3_config_source.count("'rag_top_k': 3") == 2
    assert rag3_config_source.count("'primary_metric': 'strict_token_f1'") == 2
    assert rag3_config_source.count("'context_length': 8192") == 2
    assert rag3_config_source.count("'parallel': 1") == 2
    assert rag3_config_source.count("'reload_every_samples': 200") == 2
    assert "ExactCountHybridRetriever(" in rag3_config_source
    assert "PatternRetriever(" in rag3_config_source
    assert "KNNRetriever(" in rag3_config_source
    assert "train_only_support" in rag3_config_source
    assert "len(qwen_rag3_examples) != 6" in rag3_config_source

    assert "run_formal_batch(" in rag3_run_source
    assert "QWEN_FAMILY_RAG3_TEST_RUNS" in rag3_run_source
    assert "require_all_smoke=False" in rag3_run_source
    assert "qwen_family_fixed_rag_k3_test_summary.csv" in rag3_config_source
