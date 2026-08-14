"""验证 CNC 微调数据划分、格式与泄漏审计。"""

from __future__ import annotations

import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.prepare_cnc_sft_data import prepare_cnc_sft_data


def _read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def test_prepare_cnc_sft_data_is_document_disjoint_and_llamafactory_ready(tmp_path: Path) -> None:
    output_dir = tmp_path / "cnc_sft"
    manifest, audit = prepare_cnc_sft_data(
        source_path=PROJECT_ROOT / "Data" / "Dataset_1_CNC_modified.jsonl",
        raw_path=PROJECT_ROOT / "Data" / "raw" / "Dataset_1_CNC_raw.csv",
        output_dir=output_dir,
    )

    rows = {
        split: _read_jsonl(output_dir / f"{split}.jsonl")
        for split in ("train", "validation", "test")
    }
    assert {split: len(items) for split, items in rows.items()} == {
        "train": 1537,
        "validation": 500,
        "test": 1038,
    }
    assert all(audit["checks"].values())
    assert manifest["actual_sizes"] == manifest["target_sizes"]

    document_sets = {
        split: {row["doc_id"] for row in items}
        for split, items in rows.items()
    }
    assert document_sets["train"].isdisjoint(document_sets["validation"])
    assert document_sets["train"].isdisjoint(document_sets["test"])
    assert document_sets["validation"].isdisjoint(document_sets["test"])

    positive = next(row for row in rows["train"] if row["has_causal"])
    negative = next(row for row in rows["train"] if not row["has_causal"])
    positive_answer = json.loads(positive["messages"][2]["content"])
    negative_answer = json.loads(negative["messages"][2]["content"])
    assert positive_answer["has_causal"] is True
    assert positive_answer["triples"][0]["relation"] == "caused"
    assert positive_answer["triples"][0]["cause"]["span"] in positive["text"]
    assert positive_answer["triples"][0]["effect"]["span"] in positive["text"]
    assert negative_answer == {"has_causal": False, "triples": []}

    dataset_info = json.loads((output_dir / "dataset_info.json").read_text(encoding="utf-8"))
    assert dataset_info["cnc_sft_train"]["formatting"] == "sharegpt"
    assert dataset_info["cnc_sft_train"]["columns"] == {"messages": "messages"}


def test_prepare_cnc_sft_data_is_reproducible(tmp_path: Path) -> None:
    first_dir = tmp_path / "first"
    second_dir = tmp_path / "second"
    first, _audit = prepare_cnc_sft_data(
        source_path=PROJECT_ROOT / "Data" / "Dataset_1_CNC_modified.jsonl",
        raw_path=PROJECT_ROOT / "Data" / "raw" / "Dataset_1_CNC_raw.csv",
        output_dir=first_dir,
    )
    second, _audit = prepare_cnc_sft_data(
        source_path=PROJECT_ROOT / "Data" / "Dataset_1_CNC_modified.jsonl",
        raw_path=PROJECT_ROOT / "Data" / "raw" / "Dataset_1_CNC_raw.csv",
        output_dir=second_dir,
    )

    assert first["data_sha256"] == second["data_sha256"]
    assert first["split_ids"] == second["split_ids"]
