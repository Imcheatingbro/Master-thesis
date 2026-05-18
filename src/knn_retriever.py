"""SPEC_03：基于 BGE embedding cache 的 KNN RAG 与 KNN+Pattern RAG 检索器。"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Protocol

import numpy as np
from numpy.typing import NDArray

from src.embedding_cache import (
    DEFAULT_BGE_EMBEDDINGS_PATH,
    DEFAULT_BGE_METADATA_PATH,
    DEFAULT_BGE_MODEL_NAME,
    SentenceEncoderProtocol,
    load_embedding_cache,
)


LOGGER = logging.getLogger(__name__)


class RetrieverProtocol(Protocol):
    """PatternRetriever 与 KNNRetriever 共用的最小接口。"""

    def retrieve(self, text: str, top_k: int) -> list[dict[str, object]]:
        """检索 top-k 个 few-shot examples。"""


class KNNRetriever:
    """从 BGE embedding cache 中检索语义最相似的 examples。"""

    def __init__(
        self,
        metadata_path: Path | str = DEFAULT_BGE_METADATA_PATH,
        embeddings_path: Path | str = DEFAULT_BGE_EMBEDDINGS_PATH,
        model_name: str = DEFAULT_BGE_MODEL_NAME,
        encoder: SentenceEncoderProtocol | None = None,
    ) -> None:
        self.metadata_path = Path(metadata_path)
        self.embeddings_path = Path(embeddings_path)
        self.model_name = model_name
        self.examples, embeddings = load_embedding_cache(self.metadata_path, self.embeddings_path)
        self.embeddings = _normalize_matrix(embeddings)
        self.encoder = encoder
        LOGGER.info("KNN cache 已加载：examples=%s path=%s", len(self.examples), self.metadata_path)

    def retrieve(self, text: str, top_k: int = 3) -> list[dict[str, object]]:
        """返回与输入文本 embedding cosine similarity 最高的 top-k examples。"""
        if top_k <= 0:
            return []
        query_embedding = self._encode_query(text)
        scores = self.embeddings @ query_embedding
        top_indices = np.argsort(scores)[-top_k:][::-1]
        results: list[dict[str, object]] = []
        for index in top_indices:
            example = self.examples[int(index)]
            results.append(
                {
                    "sentence": example["sentence"],
                    "cause": example["cause"],
                    "effect": example["effect"],
                    "causality_phrase": example["causality_phrase"],
                    "score": round(float(scores[int(index)]), 4),
                    "source": "knn",
                }
            )
        return results

    def _encode_query(self, text: str) -> NDArray[np.float32]:
        if self.encoder is None:
            from sentence_transformers import SentenceTransformer

            self.encoder = SentenceTransformer(self.model_name)
        embedding = self.encoder.encode(
            [text],
            batch_size=1,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return _normalize_matrix(np.asarray(embedding, dtype=np.float32))[0]


class HybridRetriever:
    """拼接 Pattern RAG 与 KNN RAG examples，并按句子/标注去重。"""

    def __init__(self, pattern_retriever: RetrieverProtocol, knn_retriever: RetrieverProtocol) -> None:
        self.pattern_retriever = pattern_retriever
        self.knn_retriever = knn_retriever

    def retrieve(self, text: str, top_k: int = 3) -> list[dict[str, object]]:
        """返回 Pattern examples 后接 KNN examples 的去重结果。"""
        combined = self.pattern_retriever.retrieve(text, top_k) + self.knn_retriever.retrieve(text, top_k)
        seen: set[tuple[str, str, str]] = set()
        results: list[dict[str, object]] = []
        for example in combined:
            key = (str(example["sentence"]), str(example["cause"]), str(example["effect"]))
            if key in seen:
                continue
            seen.add(key)
            results.append(example)
        return results


def _normalize_matrix(matrix: NDArray[np.float32]) -> NDArray[np.float32]:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return (matrix / norms).astype(np.float32, copy=False)
