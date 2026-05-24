"""CauseNet raw 过滤脚本的单元测试。"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "Data" / "script" / "filter_causenet_raw.py"


def test_filter_rows_keeps_sentence_sources_and_drops_non_sentence_sources() -> None:
    module = _load_script_module()
    rows = [
        {
            "causal_relation": {"cause": {"concept": "smoking"}, "effect": {"concept": "death"}},
            "sources": [
                {"type": "wikipedia_sentence", "payload": {"sentence": "Smoking caused death."}},
                {"type": "wikipedia_list", "payload": {"list_toc_section_heading": "Causes"}},
            ],
        },
        {
            "causal_relation": {"cause": {"concept": "alcohol"}, "effect": {"concept": "cirrhosis"}},
            "sources": [{"type": "wikipedia_infobox", "payload": {"infobox_argument": "causes"}}],
        },
    ]

    kept_rows, stats = module.filter_rows(rows)

    assert kept_rows == [
        {
            "causal_relation": {"cause": {"concept": "smoking"}, "effect": {"concept": "death"}},
            "sources": [{"type": "wikipedia_sentence", "payload": {"sentence": "Smoking caused death."}}],
        }
    ]
    assert stats.rows_read == 2
    assert stats.rows_kept == 1
    assert stats.rows_removed == 1
    assert stats.sources_kept == 1
    assert stats.sources_removed == 2


def test_filter_file_replaces_input_with_filtered_jsonl(tmp_path: Path) -> None:
    module = _load_script_module()
    path = tmp_path / "Dataset_4_causenet_raw.jsonl"
    rows = [
        {
            "causal_relation": {"cause": {"concept": "human_activity"}, "effect": {"concept": "climate_change"}},
            "sources": [{"type": "wikipedia_sentence", "payload": {"sentence": "Climate change is caused by human activity."}}],
        },
        {
            "causal_relation": {"cause": {"concept": "separation"}, "effect": {"concept": "stress"}},
            "sources": [{"type": "wikipedia_list", "payload": {"list_toc_section_heading": "Causes"}}],
        },
    ]
    path.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")

    stats = module.filter_file(path)

    output_rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    assert output_rows == [rows[0]]
    assert stats.rows_read == 2
    assert stats.rows_kept == 1
    assert not (tmp_path / "Dataset_4_causenet_raw.jsonl.tmp").exists()


def _load_script_module() -> Any:
    spec = importlib.util.spec_from_file_location("filter_causenet_raw", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
