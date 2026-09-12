"""SPEC_05：验证 notebook 可执行、模型调用开关及四数据集评估接线。"""

from pathlib import Path
from typing import Any

import nbformat
import pytest

import src.causal_discovery_baseline as baseline


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "causal_discovery_baseline.ipynb"


def _notebook() -> Any:
    if not baseline.DEFAULT_SOURCE_DIR.is_dir():
        pytest.skip("未下载作者仓库，跳过依赖该仓库的 notebook 执行检查")
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    nbformat.validate(notebook)
    for cell in notebook.cells:
        if cell.cell_type == "code":
            assert cell.execution_count is None and not cell.outputs
            compile(cell.source, str(NOTEBOOK), "exec")
    return notebook


def test_notebook_preflight_and_data_work_without_inference(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    import IPython.display
    import subprocess
    import torch
    import sys

    monkeypatch.chdir(ROOT / "notebooks")
    monkeypatch.setattr(sys, "prefix", str(tmp_path / "CausalDiscovery"))
    monkeypatch.setattr(IPython.display, "display", lambda *args: None)
    monkeypatch.setattr(torch.cuda, "is_available", lambda: False)

    def forbidden(*args: Any, **kwargs: Any) -> None:
        pytest.fail("仅检查数据时不应安装软件、下载模型或开始推理")

    monkeypatch.setattr(subprocess, "run", forbidden)
    monkeypatch.setattr(baseline.AuthorRunner, "prepare", forbidden)
    namespace: dict[str, Any] = {}
    for cell in _notebook().cells:
        if cell.cell_type != "code":
            continue
        exec(compile(cell.source, str(NOTEBOOK), "exec"), namespace)
        if "configuration" in cell.metadata.tags:
            assert namespace["RUN_SMOKE"] is True and namespace["RUN_FULL_EVAL"] is False
            assert namespace["RUN_ID"] == "mistral7b_bf16_ficl_cot_adapted_v2"
            namespace["RUN_SMOKE"] = False
    assert namespace["ROOT"] == ROOT
    assert set(namespace["DATASETS"]) == {"cnc_sft_test", "li", "ade", "politicause"}
    assert all(namespace["DATASETS"].values())
    assert namespace["MODEL_NAME_OR_PATH"] == str(
        ROOT / "reference code from related work" / "CausalDiscovery-model" / "Mistral-7B-Instruct-v0.3"
    )
    assert not namespace["recent_results"]
    with pytest.raises(RuntimeError, match="推理环境未就绪"):
        namespace["require_inference_environment"]()
    notebook_source = "\n".join(cell.source for cell in _notebook().cells)
    assert "MODEL_REPO_ID" not in notebook_source and "HF_HOME" not in notebook_source
    assert "INSTALL_DEPENDENCIES" not in notebook_source and "DOWNLOAD_MODEL" not in notebook_source
    assert "不启用独立 reasoning/thinking 开关" in notebook_source
    assert "profile=ADAPTED_PROFILE" in notebook_source
    assert "precision=BF16" in notebook_source
    assert "do_sample=False" in notebook_source
    assert namespace["CONFIG"].profile == baseline.ADAPTED_PROFILE
    assert namespace["CONFIG"].precision == baseline.BF16
    assert namespace["CONFIG"].extraction_max_new_tokens == 1024


def test_notebook_smoke_and_full_use_actual_evaluator_with_stubbed_model(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> None:
    import IPython.display
    import sys

    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(sys, "prefix", str(tmp_path / "CausalDiscovery"))
    monkeypatch.setattr(IPython.display, "display", lambda *args: None)
    prepared: list[str] = []

    class NoCausalRunner:
        """所有样本返回负例，仅代替昂贵模型，数据、prompt、输出保存与 evaluator 均真实执行。"""

        def __init__(self, source_dir: Path, config: baseline.RunConfig) -> None:
            self.templates = baseline.load_author_templates(source_dir)
            self.config = config
            self.runtime: dict[str, Any] = {}

        def prepare(self, stage: str) -> None:
            prepared.append(stage)

        def generate(self, prompts: list[str]) -> list[str]:
            return ['{"answer":"noncausal"}'] * len(prompts)

        def close(self) -> None:
            self.runtime.clear()

    monkeypatch.setattr(baseline, "AuthorRunner", NoCausalRunner)
    namespace: dict[str, Any] = {}
    for cell in _notebook().cells:
        if cell.cell_type != "code":
            continue
        exec(compile(cell.source, str(NOTEBOOK), "exec"), namespace)
        if "configuration" in cell.metadata.tags:
            namespace.update(RUN_SMOKE=True, RUN_FULL_EVAL=True, EVAL_SAMPLE_N=2,
                             FULL_EVAL_SAMPLE_N=3, OUTPUT_DIR=tmp_path / "results")
        if "preflight" in cell.metadata.tags:
            namespace["require_inference_environment"] = lambda: None
    assert prepared == ["detection"] * 8
    assert len(namespace["smoke_results"]) == len(namespace["full_results"]) == 4
    for phase, count in (("smoke", 2), ("full", 3)):
        for result in namespace[f"{phase}_results"]:
            assert result["report"]["n_samples"] == count
            assert len(result["predictions"]) == count
            assert result["paths"]["report_json"].is_file()
            row = namespace["result_row"](result)
            assert "Extraction F1 (all)" in row and "Extraction F1 (detected-only)" in row
            assert row["Detection parse errors"] == 0
            assert row["Normalized detection outputs"] == 0
