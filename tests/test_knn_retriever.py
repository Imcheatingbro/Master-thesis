"""SPEC_03：KNN RAG 与 KNN+Pattern RAG 检索器的单元测试。"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.retriever import (
    DeterministicRandomRetriever,
    ExactCountHybridRetriever,
    HybridRetriever,
    KNNRetriever,
    load_examples_from_jsonl,
)


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


class StaticRetriever:
    """测试用固定顺序检索器。"""

    def __init__(self, sentences: list[str], source: str) -> None:
        self.examples = [
            {
                "dataset": "cnc",
                "sample_id": sentence,
                "sentence": sentence,
                "cause": f"{sentence} cause",
                "effect": f"{sentence} effect",
                "source": source,
            }
            for sentence in sentences
        ]

    def retrieve(self, text: str, top_k: int) -> list[dict[str, object]]:
        return self.examples[:top_k]


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


def test_exact_count_hybrid_retriever_fills_overlap_to_two_k() -> None:
    retriever = ExactCountHybridRetriever(
        pattern_retriever=StaticRetriever(["P1", "shared", "P3", "P4"], "pattern"),
        knn_retriever=StaticRetriever(["shared", "K2", "K3", "K4"], "knn"),
    )

    examples = retriever.retrieve("query", top_k=2)

    assert len(examples) == 4
    assert len({str(example["sentence"]) for example in examples}) == 4
    assert [example["sentence"] for example in examples] == ["P1", "shared", "K2", "P3"]


def test_deterministic_random_retriever_returns_stable_two_k(tmp_path: Path) -> None:
    metadata_path = tmp_path / "random_examples.jsonl"
    rows = [
        {
            "dataset": "cnc",
            "sample_id": index,
            "sentence": f"Sentence {index}.",
            "cause": f"Cause {index}",
            "effect": f"Effect {index}",
        }
        for index in range(10)
    ]
    metadata_path.write_text(
        "\n".join(json.dumps(row) for row in rows) + "\n",
        encoding="utf-8",
    )
    retriever = DeterministicRandomRetriever(metadata_path=metadata_path, seed=42)

    first = retriever.retrieve("query", top_k=3)
    second = retriever.retrieve("query", top_k=3)

    assert len(first) == 6
    assert [example["sample_id"] for example in first] == [example["sample_id"] for example in second]
    assert len({example["sample_id"] for example in first}) == 6
    assert all(example["source"] == "random" for example in first)


def test_load_examples_from_jsonl_preserves_multi_triples_and_signals(tmp_path: Path) -> None:
    metadata_path = tmp_path / "cnc_examples.jsonl"
    metadata_path.write_text(
        json.dumps(
            {
                "dataset": "cnc",
                "sample_id": 7,
                "sentence": "A caused B and led to C.",
                "triples": [
                    {"cause": "A", "effect": "B"},
                    {"cause": "A", "effect": "C"},
                ],
                "signals": ["caused", "led to"],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    examples = load_examples_from_jsonl(metadata_path)

    assert examples[0]["sample_id"] == 7
    assert len(examples[0]["triples"]) == 2
    assert examples[0]["signals"] == ["caused", "led to"]
    assert examples[0]["cause"] == "A"
