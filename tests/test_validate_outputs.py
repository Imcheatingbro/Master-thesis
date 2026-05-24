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


def _load_script_module() -> Any:
    spec = importlib.util.spec_from_file_location("validate_outputs", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
