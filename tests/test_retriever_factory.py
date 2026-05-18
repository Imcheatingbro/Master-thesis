"""SPEC_03：RAG 模式检索器工厂的单元测试。"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.retriever import HybridRetriever, KNNRetriever, PatternRetriever, create_retriever


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
    metadata_path = tmp_path / "examples.jsonl"
    embeddings_path = tmp_path / "embeddings.npy"
    write_cache(metadata_path, embeddings_path)

    assert isinstance(create_retriever("pattern", metadata_path=metadata_path), PatternRetriever)
    assert isinstance(
        create_retriever("knn", metadata_path=metadata_path, embeddings_path=embeddings_path),
        KNNRetriever,
    )
    assert isinstance(
        create_retriever(
            "knn_pattern",
            metadata_path=metadata_path,
            embeddings_path=embeddings_path,
        ),
        HybridRetriever,
    )


def test_create_retriever_rejects_unknown_mode() -> None:
    with pytest.raises(ValueError, match="rag_mode"):
        create_retriever("unknown")
