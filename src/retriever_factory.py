"""SPEC_03：按 notebook 配置创建 Pattern、KNN 或 KNN+Pattern 检索器。"""

from __future__ import annotations

from pathlib import Path

from src.embedding_cache import DEFAULT_BGE_EMBEDDINGS_PATH, DEFAULT_BGE_METADATA_PATH
from src.knn_retriever import HybridRetriever, KNNRetriever, RetrieverProtocol
from src.rag_retriever import PatternRetriever


def create_retriever(
    rag_mode: str,
    pattern_db_path: Path | str | None = None,
    metadata_path: Path | str = DEFAULT_BGE_METADATA_PATH,
    embeddings_path: Path | str = DEFAULT_BGE_EMBEDDINGS_PATH,
) -> RetrieverProtocol:
    """根据 rag_mode 创建检索器，支持 pattern、knn、knn_pattern。"""
    normalized_mode = rag_mode.strip().lower()
    if normalized_mode == "pattern":
        return PatternRetriever(pattern_db_path=pattern_db_path)
    if normalized_mode == "knn":
        return KNNRetriever(metadata_path=metadata_path, embeddings_path=embeddings_path)
    if normalized_mode == "knn_pattern":
        return HybridRetriever(
            pattern_retriever=PatternRetriever(pattern_db_path=pattern_db_path),
            knn_retriever=KNNRetriever(metadata_path=metadata_path, embeddings_path=embeddings_path),
        )
    raise ValueError("rag_mode 必须是 pattern、knn 或 knn_pattern")
