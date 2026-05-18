"""SPEC_03：KNN RAG 与 KNN+Pattern RAG 检索器的单元测试。"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.knn_retriever import HybridRetriever, KNNRetriever


class FakeEncoder:
    """测试用查询 embedding 编码器。"""

    def encode(
        self,
        sentences: list[str],
        batch_size: int,
        normalize_embeddings: bool,
        show_progress_bar: bool,
    ) -> np.ndarray:
        return np.asarray([[1.0, 0.0] for _sentence in sentences], dtype=np.float32)


class FakePatternRetriever:
    """测试用 Pattern 检索器。"""

    def retrieve(self, text: str, top_k: int) -> list[dict[str, object]]:
        return [
            {
                "sentence": "Pattern sentence.",
                "cause": "pattern cause",
                "effect": "pattern effect",
                "causality_phrase": "because",
                "score": 100.0,
                "source": "pattern",
            },
            {
                "sentence": "KNN first.",
                "cause": "A",
                "effect": "B",
                "causality_phrase": "caused",
                "score": 90.0,
                "source": "pattern",
            },
        ][:top_k]


def write_cache(metadata_path: Path, embeddings_path: Path) -> None:
    """写入测试用 embedding cache。"""
    examples = [
        {"sentence": "KNN first.", "cause": "A", "effect": "B", "causality_phrase": "caused"},
        {"sentence": "KNN second.", "cause": "C", "effect": "D", "causality_phrase": "led to"},
    ]
    with metadata_path.open("w", encoding="utf-8") as file:
        for example in examples:
            file.write(json.dumps(example, ensure_ascii=False) + "\n")
    np.save(embeddings_path, np.asarray([[1.0, 0.0], [0.0, 1.0]], dtype=np.float32))


def test_knn_retriever_returns_examples_by_cosine_similarity(tmp_path: Path) -> None:
    metadata_path = tmp_path / "examples.jsonl"
    embeddings_path = tmp_path / "embeddings.npy"
    write_cache(metadata_path, embeddings_path)
    retriever = KNNRetriever(
        metadata_path=metadata_path,
        embeddings_path=embeddings_path,
        encoder=FakeEncoder(),
    )

    examples = retriever.retrieve("Rain caused flooding.", top_k=2)

    assert [example["sentence"] for example in examples] == ["KNN first.", "KNN second."]
    assert examples[0]["source"] == "knn"
    assert examples[0]["score"] > examples[1]["score"]


def test_hybrid_retriever_concatenates_pattern_and_knn_with_dedup(tmp_path: Path) -> None:
    metadata_path = tmp_path / "examples.jsonl"
    embeddings_path = tmp_path / "embeddings.npy"
    write_cache(metadata_path, embeddings_path)
    knn_retriever = KNNRetriever(
        metadata_path=metadata_path,
        embeddings_path=embeddings_path,
        encoder=FakeEncoder(),
    )
    retriever = HybridRetriever(pattern_retriever=FakePatternRetriever(), knn_retriever=knn_retriever)

    examples = retriever.retrieve("Rain caused flooding.", top_k=2)

    assert [example["sentence"] for example in examples] == [
        "Pattern sentence.",
        "KNN first.",
        "KNN second.",
    ]
    assert [example["source"] for example in examples] == ["pattern", "pattern", "knn"]
