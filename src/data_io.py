"""SPEC_04：读取 SPEC_01 清洗后的 JSONL 数据。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).resolve().parents[1] / "Data"
DATASET_FILES = {
    "cnc": "Dataset_1_CNC_modified.jsonl",
    "li": "Dataset_2_Li_modified.jsonl",
    "ade": "Dataset_3_ADE_modified.jsonl",
}


def load_dataset(dataset: str, data_dir: Path | str = DATA_DIR, n: int | None = None) -> list[dict[str, Any]]:
    """读取指定数据集；`n` 不为空时返回前 n 条样本。"""
    if dataset not in DATASET_FILES:
        raise ValueError(f"未知数据集：{dataset}")

    path = Path(data_dir) / DATASET_FILES[dataset]
    samples: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            samples.append(json.loads(line))
            if n is not None and len(samples) >= n:
                break
    return samples
