"""ADE 数据清洗与 BGE overlap 剔除脚本的单元测试。"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "Data" / "script" / "clean_ade_data.py"


def test_build_ade_samples_merges_detection_and_relations_then_excludes_bge_texts() -> None:
    module = _load_script_module()
    classification_rows = [
        {"text": "Drug A caused rash.", "label": 1},
        {"text": "Drug A caused rash.", "label": 1},
        {"text": "No relation here.", "label": 0},
        {"text": "Overlap sentence.", "label": 1},
    ]
    relation_rows = [
        {"text": "Drug A caused rash.", "drug": "Drug A", "effect": "rash"},
        {"text": "Drug A caused rash.", "drug": "Drug A", "effect": "caused rash"},
        {"text": "Overlap sentence.", "drug": "Overlap", "effect": "sentence"},
    ]
    excluded_texts = {module.normalize_sentence("<cause>Overlap</cause> <effect>sentence</effect>.")}

    samples, stats = module.build_ade_samples(classification_rows, relation_rows, excluded_texts)

    assert samples == [
        {
            "id": 1,
            "text": "Drug A caused rash.",
            "has_causal": True,
            "relations": [
                {"cause": "Drug A", "effect": "rash"},
                {"cause": "Drug A", "effect": "caused rash"},
            ],
        },
        {"id": 2, "text": "No relation here.", "has_causal": False, "relations": []},
    ]
    assert stats["input_classification_rows"] == 4
    assert stats["unique_classification_texts"] == 3
    assert stats["input_relation_rows"] == 3
    assert stats["bge_excluded_samples"] == 1
    assert stats["output_samples"] == 2
    assert stats["causal_samples"] == 1
    assert stats["total_relations"] == 2


def test_load_bge_example_texts_strips_cause_effect_tags(tmp_path: Path) -> None:
    module = _load_script_module()
    bge_path = tmp_path / "bge.jsonl"
    bge_path.write_text(
        json.dumps({"sentence": "\"<cause>Drug A</cause>-induced <effect>rash</effect>.\""}) + "\n",
        encoding="utf-8",
    )

    texts = module.load_bge_example_texts(bge_path)

    assert texts == {module.normalize_sentence("Drug A-induced rash.")}


def test_split_samples_is_seeded_stratified_and_renumbered() -> None:
    module = _load_script_module()
    samples = [
        {"id": 1, "text": "c1", "has_causal": True, "relations": [{"cause": "a", "effect": "b"}]},
        {"id": 2, "text": "c2", "has_causal": True, "relations": [{"cause": "a", "effect": "b"}]},
        {"id": 3, "text": "c3", "has_causal": True, "relations": [{"cause": "a", "effect": "b"}]},
        {"id": 4, "text": "c4", "has_causal": True, "relations": [{"cause": "a", "effect": "b"}]},
        {"id": 5, "text": "n1", "has_causal": False, "relations": []},
        {"id": 6, "text": "n2", "has_causal": False, "relations": []},
        {"id": 7, "text": "n3", "has_causal": False, "relations": []},
        {"id": 8, "text": "n4", "has_causal": False, "relations": []},
        {"id": 9, "text": "n5", "has_causal": False, "relations": []},
        {"id": 10, "text": "n6", "has_causal": False, "relations": []},
    ]

    train, test, stats = module.split_samples(samples, train_ratio=0.5, seed=7)
    train_again, test_again, stats_again = module.split_samples(samples, train_ratio=0.5, seed=7)

    assert [sample["text"] for sample in train] == [sample["text"] for sample in train_again]
    assert [sample["text"] for sample in test] == [sample["text"] for sample in test_again]
    assert [sample["id"] for sample in train] == list(range(1, len(train) + 1))
    assert [sample["id"] for sample in test] == list(range(1, len(test) + 1))
    assert sum(1 for sample in train if sample["has_causal"]) == 2
    assert sum(1 for sample in test if sample["has_causal"]) == 2
    assert sum(1 for sample in train if not sample["has_causal"]) == 3
    assert sum(1 for sample in test if not sample["has_causal"]) == 3
    assert {sample["text"] for sample in train}.isdisjoint({sample["text"] for sample in test})
    assert stats == stats_again
    assert stats["seed"] == 7
    assert stats["train"]["output_samples"] == 5
    assert stats["test"]["output_samples"] == 5


def _load_script_module() -> Any:
    spec = importlib.util.spec_from_file_location("clean_ade_data", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
