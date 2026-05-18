"""SPEC_03：构建和读取 BGE embedding cache。"""

from __future__ import annotations

import csv
import json
import logging
from pathlib import Path
from typing import Protocol

import numpy as np
from numpy.typing import NDArray


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATTERN_DB_PATH = PROJECT_ROOT / "RAG Database" / "comb_SCITEsemADE_CausalityPattern.csv"
DEFAULT_BGE_MODEL_NAME = "BAAI/bge-small-en-v1.5"
DEFAULT_BGE_METADATA_PATH = PROJECT_ROOT / "RAG Database" / "bge-small-en-v1.5_examples.jsonl"
DEFAULT_BGE_EMBEDDINGS_PATH = PROJECT_ROOT / "RAG Database" / "bge-small-en-v1.5_embeddings.npy"


class SentenceEncoderProtocol(Protocol):
    """SentenceTransformer 与测试编码器共用的最小接口。"""

    def encode(
        self,
        sentences: list[str],
        batch_size: int,
        normalize_embeddings: bool,
        show_progress_bar: bool,
    ) -> NDArray[np.float32]:
        """将文本列表编码为 embedding 矩阵。"""


def load_examples_from_csv(pattern_db_path: Path | str) -> list[dict[str, str]]:
    """从原始 Pattern DB CSV 读取 few-shot examples。"""
    examples: list[dict[str, str]] = []
    with Path(pattern_db_path).open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            phrase = (row.get("causality_phrase") or "").strip()
            if not phrase:
                continue
            examples.append(
                {
                    "sentence": row.get("sentence", ""),
                    "cause": row.get("cause_t", ""),
                    "effect": row.get("effect_t", ""),
                    "causality_phrase": phrase,
                }
            )
    return examples


def build_embedding_cache(
    pattern_db_path: Path | str = DEFAULT_PATTERN_DB_PATH,
    metadata_path: Path | str = DEFAULT_BGE_METADATA_PATH,
    embeddings_path: Path | str = DEFAULT_BGE_EMBEDDINGS_PATH,
    model_name: str = DEFAULT_BGE_MODEL_NAME,
    batch_size: int = 64,
    encoder: SentenceEncoderProtocol | None = None,
) -> int:
    """用 BGE 模型构建 jsonl metadata 与 npy embedding cache。"""
    examples = load_examples_from_csv(pattern_db_path)
    if encoder is None:
        from sentence_transformers import SentenceTransformer

        encoder = SentenceTransformer(model_name)

    sentences = [example["sentence"] for example in examples]
    embeddings = encoder.encode(
        sentences,
        batch_size=batch_size,
        normalize_embeddings=True,
        show_progress_bar=True,
    )
    embeddings_array = np.asarray(embeddings, dtype=np.float32)

    metadata_file = Path(metadata_path)
    embeddings_file = Path(embeddings_path)
    metadata_file.parent.mkdir(parents=True, exist_ok=True)
    embeddings_file.parent.mkdir(parents=True, exist_ok=True)

    with metadata_file.open("w", encoding="utf-8", newline="\n") as file:
        for example in examples:
            file.write(json.dumps(example, ensure_ascii=False) + "\n")
    np.save(embeddings_file, embeddings_array)
    LOGGER.info(
        "BGE embedding cache 已构建：examples=%s metadata=%s embeddings=%s",
        len(examples),
        metadata_file,
        embeddings_file,
    )
    return len(examples)


def load_embedding_cache(
    metadata_path: Path | str = DEFAULT_BGE_METADATA_PATH,
    embeddings_path: Path | str = DEFAULT_BGE_EMBEDDINGS_PATH,
) -> tuple[list[dict[str, str]], NDArray[np.float32]]:
    """读取 jsonl metadata 与 npy embedding cache，并校验行数一致。"""
    metadata_file = Path(metadata_path)
    embeddings_file = Path(embeddings_path)
    examples: list[dict[str, str]] = []
    with metadata_file.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                examples.append(json.loads(line))

    embeddings = np.load(embeddings_file).astype(np.float32, copy=False)
    if len(examples) != embeddings.shape[0]:
        raise ValueError(
            f"metadata 与 embeddings 行数不一致：metadata={len(examples)} embeddings={embeddings.shape[0]}"
        )
    return examples, embeddings
