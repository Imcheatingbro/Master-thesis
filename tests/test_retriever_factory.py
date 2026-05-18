"""SPEC_03：RAG 模式检索器工厂的单元测试。"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.knn_retriever import HybridRetriever, KNNRetriever
from src.rag_retriever import PatternRetriever
from src.retriever_factory import create_retriever


def write_pattern_db(path: Path) -> None:
    """写入测试用 pattern database。"""
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["sentence", "cause_t", "effect_t", "causality_phrase"])
        writer.writeheader()
        writer.writerow(
            {
                "sentence": "<cause>Rain</cause> caused <effect>flooding</effect>.",
                "cause_t": "Rain",
                "effect_t": "flooding",
                "causality_phrase": "caused",
            }
        )


def write_cache(metadata_path: Path, embeddings_path: Path) -> None:
    """写入测试用 embedding cache。"""
    with metadata_path.open("w", encoding="utf-8") as file:
        file.write(
            json.dumps(
                {
                    "sentence": "<cause>Rain</cause> caused <effect>flooding</effect>.",
                    "cause": "Rain",
                    "effect": "flooding",
                    "causality_phrase": "caused",
                }
            )
            + "\n"
        )
    np.save(embeddings_path, np.asarray([[1.0, 0.0]], dtype=np.float32))


def test_create_retriever_returns_expected_mode_types(tmp_path: Path) -> None:
    pattern_db_path = tmp_path / "patterns.csv"
    metadata_path = tmp_path / "examples.jsonl"
    embeddings_path = tmp_path / "embeddings.npy"
    write_pattern_db(pattern_db_path)
    write_cache(metadata_path, embeddings_path)

    assert isinstance(create_retriever("pattern", pattern_db_path=pattern_db_path), PatternRetriever)
    assert isinstance(
        create_retriever("knn", metadata_path=metadata_path, embeddings_path=embeddings_path),
        KNNRetriever,
    )
    assert isinstance(
        create_retriever(
            "knn_pattern",
            pattern_db_path=pattern_db_path,
            metadata_path=metadata_path,
            embeddings_path=embeddings_path,
        ),
        HybridRetriever,
    )


def test_create_retriever_rejects_unknown_mode() -> None:
    with pytest.raises(ValueError, match="rag_mode"):
        create_retriever("unknown")
