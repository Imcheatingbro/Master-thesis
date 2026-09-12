"""验证 GoLLIE baseline notebook 的固定模型、数据和运行开关。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "gollie_baseline.ipynb"


def _notebook() -> dict[str, Any]:
    return json.loads(NOTEBOOK.read_text(encoding="utf-8"))


def _cells() -> dict[str, dict[str, Any]]:
    return {str(cell["id"]): cell for cell in _notebook()["cells"]}


def test_notebook_code_compiles_and_contains_no_saved_outputs() -> None:
    notebook = _notebook()
    assert notebook["metadata"]["kernelspec"]["name"] == "master_thesis"
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            compile("".join(cell["source"]), f"{NOTEBOOK.name}:cell{index}", "exec")
            assert cell.get("execution_count") is None
            assert cell.get("outputs", []) == []


def test_notebook_locks_gollie_q8_raw_completion_and_four_datasets() -> None:
    cells = _cells()
    config = "".join(cells["global-config"]["source"])
    preflight = "".join(cells["preflight"]["source"])
    runner = "".join(cells["runner-functions"]["source"])
    assert 'MODEL_ID = "hitz-gollie-13b-assafetensors"' in config
    assert 'DATASET_NAMES = ["cnc_sft_test", "li", "ade", "politicause"]' in config
    assert 'PRIMARY_METRIC = "anchor_window"' in config
    assert "RUN_SMOKE = True" in config and "RUN_FULL_EVAL = False" in config
    assert "max_tokens=1024" in preflight
    assert "temperature=0.0" in preflight and "cache_prompt=False" in preflight
    assert "runner.require_model()" in runner
    assert "run_gollie_baseline(" in runner
    assert 'run_selected_datasets("full", FULL_EVAL_SAMPLE_N)' in "".join(cells["run-full"]["source"])
