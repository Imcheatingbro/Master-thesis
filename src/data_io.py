"""Dataset loading utilities for normalized JSONL inputs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).resolve().parents[1] / "Data"
DATASET_FILES = {
    "cnc": "Dataset_1_CNC_modified.jsonl",
    "cnc_positive": "Dataset_1_CNC_positive_only.jsonl",
    "cnc_positive_rag_eval": "Dataset_1_CNC_positive_rag_eval.jsonl",
    "cnc_sft_validation": "CNC_sft/validation.jsonl",
    "cnc_sft_test": "CNC_sft/test.jsonl",
    "cnc_gemma12_overfit20_train": "CNC_sft_gemma12_overfit20_v1/train.jsonl",
    "li": "Dataset_2_Li_modified.jsonl",
    "ade": "Dataset_3_ADE_modified.jsonl",
    "ade_sft_train": "ADE_sft_gemma_v1/train.jsonl",
    "ade_sft_validation": "ADE_sft_gemma_v1/validation.jsonl",
    "causenet_train": "finetuning/Dataset_4_causenet_train.jsonl",
    "causenet_validation": "finetuning/Dataset_4_causenet_validation.jsonl",
    "causenet": "Dataset_4_causenet_modified.jsonl",
    "politicause_train": "PolitiCAUSE/train.jsonl",
    "politicause_validation": "PolitiCAUSE/validation.jsonl",
    "politicause_validation_prompt300": "PolitiCAUSE/validation_prompt300.jsonl",
    "politicause": "PolitiCAUSE/test.jsonl",
}


def load_dataset(dataset: str, data_dir: Path | str = DATA_DIR, n: int | None = None) -> list[dict[str, Any]]:
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
