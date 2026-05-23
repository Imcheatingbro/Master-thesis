"""ADE Hugging Face 下载脚本的单元测试。"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "Data" / "script" / "download_ade_hf_datasets.py"


def test_download_all_saves_both_ade_configs(tmp_path: Path) -> None:
    module = _load_script_module()
    calls: list[tuple[str, str]] = []

    def fake_load_dataset(repo: str, config_name: str) -> Any:
        calls.append((repo, config_name))
        return FakeDataset(config_name)

    saved_paths = module.download_all(output_dir=tmp_path, load_dataset_fn=fake_load_dataset)

    assert calls == [
        ("ade-benchmark-corpus/ade_corpus_v2", "Ade_corpus_v2_classification"),
        ("ade-benchmark-corpus/ade_corpus_v2", "Ade_corpus_v2_drug_ade_relation"),
    ]
    assert saved_paths == [
        tmp_path / "Ade_corpus_v2_classification",
        tmp_path / "Ade_corpus_v2_drug_ade_relation",
    ]
    assert (tmp_path / "Ade_corpus_v2_classification" / "marker.txt").read_text(encoding="utf-8") == (
        "Ade_corpus_v2_classification"
    )
    assert (tmp_path / "Ade_corpus_v2_drug_ade_relation" / "marker.txt").read_text(encoding="utf-8") == (
        "Ade_corpus_v2_drug_ade_relation"
    )


def _load_script_module() -> Any:
    spec = importlib.util.spec_from_file_location("download_ade_hf_datasets", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FakeDataset:
    """模拟 Hugging Face DatasetDict 的 save_to_disk 行为。"""

    def __init__(self, config_name: str) -> None:
        self.config_name = config_name

    def save_to_disk(self, path: str) -> None:
        output_path = Path(path)
        output_path.mkdir(parents=True, exist_ok=True)
        (output_path / "marker.txt").write_text(self.config_name, encoding="utf-8")
