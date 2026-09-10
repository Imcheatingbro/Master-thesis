"""CauseNet 数据清洗与固定规模切分脚本的单元测试。"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "Data" / "script" / "clean_causenet_data.py"


def test_build_causenet_samples_merges_same_sentence_relations() -> None:
    module = _load_script_module()
    rows = [
        _raw_row(
            "human_activity",
            "climate_change",
            "Climate change is caused by greenhouse gases and human activity.",
        ),
        _raw_row(
            "greenhouse_gases",
            "climate_change",
            "Climate change is caused by greenhouse gases and human activity.",
        ),
        _raw_row("missing_concept", "climate_change", "Climate change is caused by human activity."),
    ]

    samples, stats = module.build_causenet_samples(rows)

    assert samples == [
        {
            "id": 1,
            "text": "Climate change is caused by greenhouse gases and human activity.",
            "has_causal": True,
            "relations": [
                {"cause": "human activity", "effect": "Climate change"},
                {"cause": "greenhouse gases", "effect": "Climate change"},
            ],
        }
    ]
    assert stats["input_rows"] == 3
    assert stats["input_sources"] == 3
    assert stats["output_samples"] == 1
    assert stats["causal_samples"] == 1
    assert stats["non_causal_samples"] == 0
    assert stats["total_relations"] == 2
    assert stats["warnings"]["substring_check_failed_relations"] == 1


def test_split_samples_uses_seeded_fixed_sizes_and_keeps_extra() -> None:
    module = _load_script_module()
    samples = [
        {"id": index, "text": f"sample {index}", "has_causal": True, "relations": [{"cause": "a", "effect": "b"}]}
        for index in range(1, 7)
    ]

    train, test, extra, stats = module.split_samples(samples, train_size=2, test_size=2, seed=7)
    train_again, test_again, extra_again, stats_again = module.split_samples(samples, train_size=2, test_size=2, seed=7)

    assert [sample["text"] for sample in train] == [sample["text"] for sample in train_again]
    assert [sample["text"] for sample in test] == [sample["text"] for sample in test_again]
    assert [sample["text"] for sample in extra] == [sample["text"] for sample in extra_again]
    assert [sample["id"] for sample in train] == [1, 2]
    assert [sample["id"] for sample in test] == [1, 2]
    assert [sample["id"] for sample in extra] == [1, 2]
    assert {sample["text"] for sample in train}.isdisjoint({sample["text"] for sample in test})
    assert {sample["text"] for sample in train}.isdisjoint({sample["text"] for sample in extra})
    assert {sample["text"] for sample in test}.isdisjoint({sample["text"] for sample in extra})
    assert stats == stats_again
    assert stats["train"]["output_samples"] == 2
    assert stats["test"]["output_samples"] == 2
    assert stats["extra"]["output_samples"] == 2


def test_run_cleaning_writes_train_test_extra_and_stats(tmp_path: Path) -> None:
    module = _load_script_module()
    rows = [
        _raw_row("rain", "flooding", "Heavy rain caused flooding."),
        _raw_row("wind", "damage", "Strong wind caused damage."),
        _raw_row("heat", "illness", "Heat caused illness."),
        _raw_row("stress", "insomnia", "Stress caused insomnia."),
    ]
    raw_path = tmp_path / "Dataset_4_causenet_raw.jsonl"
    raw_path.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")

    result = module.run_cleaning(tmp_path, train_size=2, test_size=1, seed=11)

    train_rows = _read_jsonl(tmp_path / "finetuning" / "Dataset_4_causenet_train.jsonl")
    test_rows = _read_jsonl(tmp_path / "Dataset_4_causenet_modified.jsonl")
    extra_rows = _read_jsonl(tmp_path / "Dataset_4_causenet_extra.jsonl")
    stats = json.loads((tmp_path / "stats.json").read_text(encoding="utf-8"))

    assert len(train_rows) == 2
    assert len(test_rows) == 1
    assert len(extra_rows) == 1
    assert all(row["has_causal"] for row in train_rows + test_rows + extra_rows)
    assert result["source"]["output_samples"] == 4
    assert stats["causenet_train"]["output_samples"] == 2
    assert stats["causenet"]["output_samples"] == 1
    assert stats["causenet_extra"]["output_samples"] == 1


def _raw_row(cause: str, effect: str, sentence: str) -> dict[str, Any]:
    return {
        "causal_relation": {"cause": {"concept": cause}, "effect": {"concept": effect}},
        "sources": [{"type": "wikipedia_sentence", "payload": {"sentence": sentence}}],
    }


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def _load_script_module() -> Any:
    spec = importlib.util.spec_from_file_location("clean_causenet_data", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
