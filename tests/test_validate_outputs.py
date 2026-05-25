"""清洗产物验证脚本的回归测试。"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "Data" / "script" / "validate_outputs.py"


def test_validate_jsonl_handles_unicode_line_separator_inside_text(tmp_path: Path) -> None:
    module = _load_script_module()
    path = tmp_path / "Dataset_4_causenet_modified.jsonl"
    row = {
        "id": 1,
        "text": "Rain caused flooding.\u2028The source sentence keeps a unicode separator.",
        "has_causal": True,
        "relations": [{"cause": "Rain", "effect": "flooding"}],
    }
    with path.open("w", encoding="utf-8", newline="\n") as file:
        file.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    stats = {
        "causenet": {
            "output_samples": 1,
            "causal_samples": 1,
            "non_causal_samples": 0,
            "total_relations": 1,
            "relation_count_distribution": {"1": 1},
        }
    }

    summary = module.validate_jsonl("causenet", path, stats)

    assert summary == f"causenet: 1 samples, 1 relations, LF ok"


def test_validation_targets_skip_missing_causenet_extra(tmp_path: Path) -> None:
    module = _load_script_module()
    (tmp_path / "finetuning").mkdir()
    for path in [
        tmp_path / "Dataset_1_CNC_modified.jsonl",
        tmp_path / "Dataset_2_Li_modified.jsonl",
        tmp_path / "Dataset_3_ADE_modified.jsonl",
        tmp_path / "Dataset_4_causenet_modified.jsonl",
        tmp_path / "finetuning" / "Dataset_3_ADE_train.jsonl",
        tmp_path / "finetuning" / "Dataset_4_causenet_train.jsonl",
    ]:
        path.write_text("", encoding="utf-8")

    targets = module.validation_targets(tmp_path)

    assert [name for name, _ in targets] == ["cnc", "li", "ade_train", "ade", "causenet_train", "causenet"]


def test_validation_targets_include_existing_causenet_extra(tmp_path: Path) -> None:
    module = _load_script_module()
    (tmp_path / "Dataset_4_causenet_extra.jsonl").write_text("", encoding="utf-8")

    targets = module.validation_targets(tmp_path)

    assert targets[-1] == ("causenet_extra", tmp_path / "Dataset_4_causenet_extra.jsonl")


def _load_script_module() -> Any:
    spec = importlib.util.spec_from_file_location("validate_outputs", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
