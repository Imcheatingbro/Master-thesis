"""SPEC_03：为 KNN RAG 构建 BGE embedding cache 的命令行脚本。"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.embedding_cache import (
    DEFAULT_BGE_EMBEDDINGS_PATH,
    DEFAULT_BGE_METADATA_PATH,
    DEFAULT_BGE_MODEL_NAME,
    DEFAULT_PATTERN_DB_PATH,
    build_embedding_cache,
)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description="构建 BGE embedding cache")
    parser.add_argument("--pattern-db", type=Path, default=DEFAULT_PATTERN_DB_PATH)
    parser.add_argument("--metadata", type=Path, default=DEFAULT_BGE_METADATA_PATH)
    parser.add_argument("--embeddings", type=Path, default=DEFAULT_BGE_EMBEDDINGS_PATH)
    parser.add_argument("--model", default=DEFAULT_BGE_MODEL_NAME)
    parser.add_argument("--batch-size", type=int, default=64)
    return parser.parse_args()


def main() -> None:
    """脚本入口。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    args = parse_args()
    count = build_embedding_cache(
        pattern_db_path=args.pattern_db,
        metadata_path=args.metadata,
        embeddings_path=args.embeddings,
        model_name=args.model,
        batch_size=args.batch_size,
    )
    logging.info("完成 BGE embedding cache 构建：examples=%s", count)


if __name__ == "__main__":
    main()
