"""SPEC_03：Pattern RAG 检索器的单元测试。"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.retriever import PatternRetriever


def write_pattern_db(path: Path) -> None:
    """写入测试用 pattern database。"""
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["sentence", "cause_t", "effect_t", "causality_phrase", "embedings"],
        )
        writer.writeheader()
        writer.writerow(
            {
                "sentence": "<cause>Heavy rain</cause> caused <effect>widespread flooding</effect>.",
                "cause_t": "Heavy rain",
                "effect_t": "widespread flooding",
                "causality_phrase": "caused",
                "embedings": "[]",
            }
        )
        writer.writerow(
            {
                "sentence": "<effect>Chaos</effect> happened because of <cause>the outage</cause>.",
                "cause_t": "the outage",
                "effect_t": "Chaos",
                "causality_phrase": "because of",
                "embedings": "[]",
            }
        )
        writer.writerow(
            {
                "sentence": "<cause>Medication</cause>-associated <effect>rash</effect>.",
                "cause_t": "Medication",
                "effect_t": "rash",
                "causality_phrase": "-associated",
                "embedings": "[]",
            }
        )


def test_retrieve_prefers_matching_causality_phrase(tmp_path: Path) -> None:
    db_path = tmp_path / "patterns.csv"
    write_pattern_db(db_path)
    retriever = PatternRetriever(pattern_db_path=db_path)

    examples = retriever.retrieve("The outage caused delays across the city.", top_k=2)

    assert len(examples) == 2
    assert examples[0]["causality_phrase"] == "caused"
    assert examples[0]["cause"] == "Heavy rain"
    assert examples[0]["effect"] == "widespread flooding"
    assert examples[0]["score"] >= examples[1]["score"]


def test_retrieve_uses_token_overlap_fallback_when_no_phrase_matches(tmp_path: Path) -> None:
    db_path = tmp_path / "patterns.csv"
    write_pattern_db(db_path)
    retriever = PatternRetriever(pattern_db_path=db_path)

    examples = retriever.retrieve("Doctors discussed a medication reaction.", top_k=1)

    assert len(examples) == 1
    assert examples[0]["cause"] == "Medication"
    assert examples[0]["effect"] == "rash"
