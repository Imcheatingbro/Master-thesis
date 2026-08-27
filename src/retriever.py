"""SPEC_03：Pattern、KNN 与 KNN+Pattern RAG 检索及 BGE cache 构建。"""

from __future__ import annotations

import csv
import hashlib
import json
import logging
import random
import re
from pathlib import Path
from typing import Any, Protocol

import numpy as np
from numpy.typing import NDArray
from rapidfuzz import fuzz


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATTERN_DB_PATH = PROJECT_ROOT / "RAG Database" / "comb_SCITEsemADE_CausalityPattern.csv"
DEFAULT_BGE_MODEL_NAME = "BAAI/bge-small-en-v1.5"
DEFAULT_BGE_METADATA_PATH = PROJECT_ROOT / "RAG Database" / "bge-small-en-v1.5_examples.jsonl"
DEFAULT_BGE_EMBEDDINGS_PATH = PROJECT_ROOT / "RAG Database" / "bge-small-en-v1.5_embeddings.npy"
DEFAULT_CNC_METADATA_PATH = PROJECT_ROOT / "RAG Database" / "cnc_examples.jsonl"
DEFAULT_CNC_EMBEDDINGS_PATH = PROJECT_ROOT / "RAG Database" / "cnc_embeddings.npy"

RAG_CACHE_PATHS = {
    "generic": (DEFAULT_BGE_METADATA_PATH, DEFAULT_BGE_EMBEDDINGS_PATH),
    "cnc": (DEFAULT_CNC_METADATA_PATH, DEFAULT_CNC_EMBEDDINGS_PATH),
}


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


class RetrieverProtocol(Protocol):
    """RAG 检索器的最小接口。"""

    def retrieve(self, text: str, top_k: int) -> list[dict[str, object]]:
        """检索 top-k 个 few-shot examples。"""


def load_examples_from_csv(pattern_db_path: Path | str) -> list[dict[str, Any]]:
    """从原始 Pattern DB CSV 读取 few-shot examples，用于重建 cache。"""
    examples: list[dict[str, Any]] = []
    with Path(pattern_db_path).open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            phrase = (row.get("causality_phrase") or "").strip()
            if not phrase:
                continue
            examples.append(
                _normalize_example(
                    {
                        "sentence": row.get("sentence", ""),
                        "cause": row.get("cause_t", ""),
                        "effect": row.get("effect_t", ""),
                        "causality_phrase": phrase,
                    }
                )
            )
    return examples


def load_examples_from_jsonl(metadata_path: Path | str) -> list[dict[str, Any]]:
    """从 BGE metadata jsonl 读取 few-shot examples。"""
    examples: list[dict[str, Any]] = []
    with Path(metadata_path).open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                examples.append(_normalize_example(json.loads(line)))
    return examples


def _normalize_example(row: dict[str, Any]) -> dict[str, Any]:
    """Normalize legacy single-pair and CNC multi-triple metadata."""
    triples: list[dict[str, str]] = []
    raw_triples = row.get("triples")
    if isinstance(raw_triples, list):
        for triple in raw_triples:
            if not isinstance(triple, dict):
                continue
            cause = _span_text(triple.get("cause"))
            effect = _span_text(triple.get("effect"))
            if cause and effect:
                triples.append({"cause": cause, "effect": effect})

    legacy_cause = _span_text(row.get("cause"))
    legacy_effect = _span_text(row.get("effect"))
    if not triples and legacy_cause and legacy_effect:
        triples.append({"cause": legacy_cause, "effect": legacy_effect})

    raw_signals = row.get("signals")
    if isinstance(raw_signals, list):
        signals = [str(signal).strip() for signal in raw_signals if str(signal).strip()]
    else:
        phrase = str(row.get("causality_phrase") or "").strip()
        signals = [phrase] if phrase else []

    normalized = dict(row)
    normalized.update(
        {
            "sentence": str(row.get("sentence") or ""),
            "triples": triples,
            "signals": list(dict.fromkeys(signals)),
            # Legacy aliases keep the existing retrievers and downstream callers compatible.
            "cause": triples[0]["cause"] if triples else legacy_cause,
            "effect": triples[0]["effect"] if triples else legacy_effect,
            "causality_phrase": signals[0] if signals else "",
        }
    )
    return normalized


def _span_text(value: Any) -> str:
    if isinstance(value, dict):
        value = value.get("span", "")
    return str(value or "").strip()


def resolve_rag_cache_paths(database: str = "generic") -> tuple[Path, Path]:
    """Return metadata and embedding cache paths for a named RAG database."""
    normalized = database.strip().lower()
    if normalized not in RAG_CACHE_PATHS:
        raise ValueError(f"rag_database must be one of: {', '.join(sorted(RAG_CACHE_PATHS))}")
    return RAG_CACHE_PATHS[normalized]


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
) -> tuple[list[dict[str, Any]], NDArray[np.float32]]:
    """读取 jsonl metadata 与 npy embedding cache，并校验行数一致。"""
    examples = load_examples_from_jsonl(metadata_path)
    embeddings = np.load(embeddings_path).astype(np.float32, copy=False)
    if len(examples) != embeddings.shape[0]:
        raise ValueError(
            f"metadata 与 embeddings 行数不一致：metadata={len(examples)} embeddings={embeddings.shape[0]}"
        )
    return examples, embeddings


class PatternRetriever:
    """从 BGE metadata 或 CSV 中检索与输入 causal pattern 相似的 examples。"""

    def __init__(
        self,
        metadata_path: Path | str = DEFAULT_BGE_METADATA_PATH,
        pattern_db_path: Path | str | None = None,
    ) -> None:
        if pattern_db_path is not None:
            metadata_path = pattern_db_path
        self.metadata_path = Path(metadata_path)
        self.examples = self._load_examples(self.metadata_path)

    @staticmethod
    def _load_examples(metadata_path: Path) -> list[dict[str, Any]]:
        if metadata_path.suffix.lower() == ".csv":
            examples = load_examples_from_csv(metadata_path)
        else:
            examples = load_examples_from_jsonl(metadata_path)
        LOGGER.info("Pattern examples 已加载：path=%s examples=%s", metadata_path, len(examples))
        return examples

    def retrieve(self, text: str, top_k: int = 3) -> list[dict[str, Any]]:
        """返回 top-k 个 Pattern RAG examples。"""
        if top_k <= 0:
            return []

        scored = []
        for index, example in enumerate(self.examples):
            phrase_score = max(
                (self._phrase_score(text, signal) for signal in example.get("signals", [])),
                default=0.0,
            )
            overlap_score = self._token_overlap_score(text, example)
            score = phrase_score + overlap_score
            if score > 0:
                scored.append((score, phrase_score, overlap_score, index, example))

        scored.sort(key=lambda item: (-item[0], -item[1], -item[2], item[3]))
        return [
            _retrieval_result(example, score=score, source="pattern")
            for score, _phrase_score, _overlap_score, _index, example in scored[:top_k]
        ]

    @staticmethod
    def _phrase_score(text: str, phrase: str) -> float:
        normalized_text = text.lower()
        normalized_phrase = phrase.lower().strip()
        if not normalized_phrase:
            return 0.0
        if normalized_phrase in normalized_text:
            return 100.0
        if len(normalized_text) < len(normalized_phrase):
            return 0.0

        scores = []
        window_size = len(normalized_phrase)
        for start in range(len(normalized_text) - window_size + 1):
            window = normalized_text[start : start + window_size]
            score = float(fuzz.ratio(window, normalized_phrase))
            if score > 90:
                scores.append(score)
        return max(scores, default=0.0)

    @staticmethod
    def _token_overlap_score(text: str, example: dict[str, Any]) -> float:
        text_tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
        triple_text = " ".join(
            part
            for triple in example.get("triples", [])
            for part in (str(triple.get("cause", "")), str(triple.get("effect", "")))
        )
        example_tokens = set(
            re.findall(
                r"[a-z0-9]+",
                " ".join([str(example["sentence"]), triple_text]).lower(),
            )
        )
        if not text_tokens or not example_tokens:
            return 0.0
        overlap = len(text_tokens & example_tokens) / len(text_tokens)
        return overlap * 10.0


class KNNRetriever:
    """从 BGE embedding cache 中检索语义最相似的 examples。"""

    def __init__(
        self,
        metadata_path: Path | str = DEFAULT_BGE_METADATA_PATH,
        embeddings_path: Path | str = DEFAULT_BGE_EMBEDDINGS_PATH,
        model_name: str = DEFAULT_BGE_MODEL_NAME,
        encoder: SentenceEncoderProtocol | None = None,
        device: str | None = "cpu",
    ) -> None:
        self.metadata_path = Path(metadata_path)
        self.embeddings_path = Path(embeddings_path)
        self.model_name = model_name
        self.examples, embeddings = load_embedding_cache(self.metadata_path, self.embeddings_path)
        self.embeddings = _normalize_matrix(embeddings)
        self.encoder = encoder
        self.device = device
        LOGGER.info(
            "KNN cache 已加载：examples=%s path=%s embedding_device=%s",
            len(self.examples),
            self.metadata_path,
            self.device,
        )

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
            results.append(_retrieval_result(example, score=float(scores[int(index)]), source="knn"))
        return results

    def _encode_query(self, text: str) -> NDArray[np.float32]:
        if self.encoder is None:
            from sentence_transformers import SentenceTransformer

            self.encoder = SentenceTransformer(self.model_name, device=self.device)
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
        seen: set[tuple[str, ...]] = set()
        results: list[dict[str, object]] = []
        for example in combined:
            sample_id = example.get("sample_id")
            if sample_id is not None:
                key = ("sample_id", str(example.get("dataset", "")), str(sample_id))
            else:
                key = (
                    "content",
                    str(example["sentence"]),
                )
            if key in seen:
                continue
            seen.add(key)
            results.append(example)
        return results


class ExactCountHybridRetriever(HybridRetriever):
    """为消融实验返回严格 2k 个去重的 Pattern+KNN examples。"""

    def retrieve(self, text: str, top_k: int = 3) -> list[dict[str, object]]:
        """优先各取 k 个 Pattern/KNN 结果，重叠时从后续候选补足至 2k。"""
        if top_k <= 0:
            return []

        target_count = 2 * top_k
        pattern_examples = self.pattern_retriever.retrieve(text, target_count)
        knn_examples = self.knn_retriever.retrieve(text, target_count)
        candidates = pattern_examples[:top_k] + knn_examples[:top_k]
        for offset in range(top_k, target_count):
            if offset < len(pattern_examples):
                candidates.append(pattern_examples[offset])
            if offset < len(knn_examples):
                candidates.append(knn_examples[offset])

        results = _deduplicate_retrieval_results(candidates, limit=target_count)
        if len(results) != target_count:
            raise ValueError(
                f"Pattern+KNN 无法补足严格 2k examples：k={top_k} actual={len(results)}"
            )
        return results


class DeterministicRandomRetriever:
    """从同一 support pool 为每个 query 确定性随机抽取严格 2k 个 examples。"""

    def __init__(
        self,
        metadata_path: Path | str = DEFAULT_CNC_METADATA_PATH,
        seed: int = 42,
    ) -> None:
        self.metadata_path = Path(metadata_path)
        self.examples = load_examples_from_jsonl(self.metadata_path)
        self.seed = int(seed)

    def retrieve(self, text: str, top_k: int = 3) -> list[dict[str, object]]:
        """按 seed 与 query 文本稳定抽取 2k 个不重复 examples。"""
        if top_k <= 0:
            return []

        target_count = 2 * top_k
        if target_count > len(self.examples):
            raise ValueError(
                f"Random support 不足：requested={target_count} available={len(self.examples)}"
            )
        digest = hashlib.sha256(f"{self.seed}\0{text}".encode("utf-8")).digest()
        query_seed = int.from_bytes(digest[:8], byteorder="big", signed=False)
        indices = random.Random(query_seed).sample(range(len(self.examples)), target_count)
        return [
            _retrieval_result(self.examples[index], score=0.0, source="random")
            for index in indices
        ]


def _deduplicate_retrieval_results(
    examples: list[dict[str, object]],
    limit: int,
) -> list[dict[str, object]]:
    """按 sample ID 或句子内容去重并截断检索结果。"""
    seen: set[tuple[str, ...]] = set()
    results: list[dict[str, object]] = []
    for example in examples:
        sample_id = example.get("sample_id")
        if sample_id is not None:
            key = ("sample_id", str(example.get("dataset", "")), str(sample_id))
        else:
            key = ("content", str(example["sentence"]))
        if key in seen:
            continue
        seen.add(key)
        results.append(example)
        if len(results) == limit:
            break
    return results


def create_retriever(
    rag_mode: str,
    metadata_path: Path | str = DEFAULT_BGE_METADATA_PATH,
    embeddings_path: Path | str = DEFAULT_BGE_EMBEDDINGS_PATH,
    embedding_device: str | None = "cpu",
) -> RetrieverProtocol:
    """根据 rag_mode 创建检索器，支持 pattern、knn、knn_pattern。"""
    normalized_mode = rag_mode.strip().lower()
    if normalized_mode == "pattern":
        return PatternRetriever(metadata_path=metadata_path)
    if normalized_mode == "knn":
        return KNNRetriever(
            metadata_path=metadata_path,
            embeddings_path=embeddings_path,
            device=embedding_device,
        )
    if normalized_mode == "knn_pattern":
        return HybridRetriever(
            pattern_retriever=PatternRetriever(metadata_path=metadata_path),
            knn_retriever=KNNRetriever(
                metadata_path=metadata_path,
                embeddings_path=embeddings_path,
                device=embedding_device,
            ),
        )
    raise ValueError("rag_mode 必须是 pattern、knn 或 knn_pattern")


def _normalize_matrix(matrix: NDArray[np.float32]) -> NDArray[np.float32]:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return (matrix / norms).astype(np.float32, copy=False)


def _retrieval_result(example: dict[str, Any], score: float, source: str) -> dict[str, object]:
    result: dict[str, object] = dict(example)
    result["score"] = round(float(score), 4)
    result["source"] = source
    return result
