"""SPEC_03：BGE embedding cache 构建与读取的单元测试。"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.retriever import build_embedding_cache, load_embedding_cache


class FakeEncoder:
    """测试用固定 embedding 编码器。"""

    def encode(
        self,
        sentences: list[str],
        batch_size: int,
        normalize_embeddings: bool,
        show_progress_bar: bool,
    ) -> np.ndarray:
        vectors = []
        for sentence in sentences:
            if "rain" in sentence.lower():
                vectors.append([1.0, 0.0])
            else:
                vectors.append([0.0, 1.0])
        return np.asarray(vectors, dtype=np.float32)


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
                "sentence": "<cause>Rain</cause> caused <effect>flooding</effect>.",
                "cause_t": "Rain",
                "effect_t": "flooding",
                "causality_phrase": "caused",
                "embedings": "[9, 9]",
            }
        )
        writer.writerow(
            {
                "sentence": "<cause>Heat</cause> led to <effect>drought</effect>.",
                "cause_t": "Heat",
                "effect_t": "drought",
                "causality_phrase": "led to",
                "embedings": "[8, 8]",
            }
        )


def test_build_embedding_cache_writes_metadata_and_numpy_matrix(tmp_path: Path) -> None:
    pattern_db_path = tmp_path / "patterns.csv"
    metadata_path = tmp_path / "examples.jsonl"
    embeddings_path = tmp_path / "embeddings.npy"
    write_pattern_db(pattern_db_path)

    count = build_embedding_cache(
        pattern_db_path=pattern_db_path,
        metadata_path=metadata_path,
        embeddings_path=embeddings_path,
        encoder=FakeEncoder(),
        batch_size=2,
    )

    examples, embeddings = load_embedding_cache(metadata_path, embeddings_path)
    assert count == 2
    assert examples[0]["sentence"] == "<cause>Rain</cause> caused <effect>flooding</effect>."
    assert examples[0]["cause"] == "Rain"
    assert examples[0]["effect"] == "flooding"
    assert examples[0]["causality_phrase"] == "caused"
    assert embeddings.dtype == np.float32
    assert embeddings.shape == (2, 2)
    assert embeddings.tolist() == [[1.0, 0.0], [0.0, 1.0]]
