"""Demo1：LM Studio 四模型 Li 批量评测 notebook 的结构测试。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "lmstudio_batch_li_test.ipynb"


def _load_notebook() -> dict[str, Any]:
    return json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))


def _cells_by_id(notebook: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(cell["id"]): cell for cell in notebook["cells"]}


def test_li_batch_notebook_code_cells_compile() -> None:
    notebook = _load_notebook()

    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            compile("".join(cell["source"]), f"{NOTEBOOK_PATH.name}:cell{index}", "exec")


def test_li_batch_notebook_uses_family_prompts_and_selected_rag_config() -> None:
    cells = _cells_by_id(_load_notebook())
    config_source = "".join(cells["global-config"]["source"])
    preflight_source = "".join(cells["lmstudio-preflight"]["source"])
    eval_source = "".join(cells["eval-helper"]["source"])
    run_source = "".join(cells["run-formal-batch"]["source"])

    expected_order = [
        "qwen/qwen3.6-35b-a3b",
        "local/qwen3.6-27b-no-thinking",
        "google/gemma-4-26b-a4b-qat",
        "google/gemma-4-31b-qat",
    ]
    positions = [config_source.index(model_key) for model_key in expected_order]

    assert positions == sorted(positions)
    assert "DATASET_NAME = 'li'" in config_source
    assert "EVAL_SAMPLE_N = None" in config_source
    assert "ENABLE_RAG = False" in config_source or "ENABLE_RAG = True" in config_source
    assert config_source.count("'use_rag': ENABLE_RAG") == 4
    assert config_source.count("'prompt_name': 'v10.1'") == 2
    assert config_source.count("'prompt_name': 'v10.2'") == 2
    assert "LI_RAG_DATABASE = 'cnc'" in config_source
    assert "LI_RAG_MODE = 'knn_pattern'" in config_source
    assert "QWEN_RAG_TOP_K = 3" in config_source
    assert "GEMMA_RAG_TOP_K = 1" in config_source
    assert config_source.count("'rag_top_k': QWEN_RAG_TOP_K") == 2
    assert config_source.count("'rag_top_k': GEMMA_RAG_TOP_K") == 2
    assert "Path('results') / 'eval_report' / 'lmstudio_batch_li'" in config_source
    assert "load_prompt_template(prompt_name).count('{rag_examples}')" in preflight_source
    assert "Li full dataset" in eval_source
    assert "if not RUN_BATCH_EVAL" in run_source
    assert "li_full_{batch_mode}_summary.csv" in run_source
    assert "family-rag-qwen-k3-gemma-k1" in run_source
    assert "batch_summary_df.to_csv" in run_source


def test_li_family_prompts_each_have_one_rag_slot() -> None:
    for prompt_name in ("v10.1", "v10.2"):
        prompt_path = PROJECT_ROOT / "prompts" / f"{prompt_name}.txt"
        assert prompt_path.read_text(encoding="utf-8").count("{rag_examples}") == 1


def test_li_batch_notebook_reruns_last_three_with_reload50() -> None:
    cells = _cells_by_id(_load_notebook())
    config_source = "".join(cells["last-three-reload50-config"]["source"])
    run_source = "".join(cells["run-last-three-reload50"]["source"])

    assert "MODEL_RUNS[1:]" in config_source
    assert "'reload_every_samples': 50" in config_source
    assert "local/qwen3.6-27b-no-thinking" in config_source
    assert "google/gemma-4-26b-a4b-qat" in config_source
    assert "google/gemma-4-31b-qat" in config_source
    assert "qwen/qwen3.6-35b-a3b" not in config_source
    assert "str(run['rag_database']) != 'cnc'" in config_source
    assert "str(run['rag_mode']) != 'knn_pattern'" in config_source
    assert "run_formal_batch(" in run_source
    assert "LAST_THREE_RELOAD50_RUNS" in run_source
    assert "require_all_smoke=False" in run_source
    assert "li_full_family_rag_last3_reload50_summary.csv" in run_source
