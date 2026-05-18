"""SPEC_04：清洗后 JSONL 数据读取工具的单元测试。"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_io import load_dataset


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    """写入测试 JSONL。"""
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def test_load_dataset_reads_expected_file_and_limits_rows(tmp_path: Path) -> None:
    rows = [
        {"id": 1, "text": "A caused B.", "has_causal": True, "relations": []},
        {"id": 2, "text": "No relation.", "has_causal": False, "relations": []},
    ]
    write_jsonl(tmp_path / "Dataset_1_CNC_modified.jsonl", rows)

    samples = load_dataset("cnc", data_dir=tmp_path, n=1)

    assert samples == [rows[0]]


def test_load_dataset_supports_li_name(tmp_path: Path) -> None:
    rows = [{"id": 1, "text": "X caused Y.", "has_causal": True, "relations": []}]
    write_jsonl(tmp_path / "Dataset_2_Li_modified.jsonl", rows)

    samples = load_dataset("li", data_dir=tmp_path)

    assert samples == rows
