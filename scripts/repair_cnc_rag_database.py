"""Repair the CNC RAG support split and complete missing causal patterns."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Protocol

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import linear_sum_assignment


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.build_cnc_rag_database import (
    _enrich_samples,
    _metadata_record,
    _read_jsonl,
    _read_raw_rows,
    _stratum,
)
from src.kg_evaluator import (
    DEFAULT_DEEPSEEK_BASE_URL,
    DEFAULT_DEEPSEEK_MODEL,
    DeepSeekJudgeClient,
)


LOGGER = logging.getLogger(__name__)
DEFAULT_POSITIVE_PATH = PROJECT_ROOT / "Data" / "Dataset_1_CNC_positive_only.jsonl"
DEFAULT_RAW_PATH = PROJECT_ROOT / "Data" / "raw" / "Dataset_1_CNC_raw.csv"
DEFAULT_SPLIT_DIR = PROJECT_ROOT / "Data" / "CNC_sft_gemma_v2"
DEFAULT_METADATA_PATH = PROJECT_ROOT / "RAG Database" / "cnc_examples.jsonl"
DEFAULT_EMBEDDINGS_PATH = PROJECT_ROOT / "RAG Database" / "cnc_embeddings.npy"
DEFAULT_MANIFEST_PATH = PROJECT_ROOT / "RAG Database" / "cnc_split_manifest.json"
DEFAULT_AUDIT_PATH = PROJECT_ROOT / "RAG Database" / "cnc_pattern_completion.jsonl"
DEFAULT_IMPLICIT_AUDIT_PATH = PROJECT_ROOT / "RAG Database" / "cnc_implicit_pattern_completion.jsonl"
DEFAULT_PATTERN_EXAMPLES_PATH = (
    PROJECT_ROOT / "RAG Database" / "comb_SCITEsemADE_CausalityPattern.csv"
)
DEFAULT_API_KEY_PATH = PROJECT_ROOT / "deepseek_api.txt"
DEFAULT_EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
TERMINAL_AUDIT_STATUSES = {"updated", "no_explicit_pattern"}


class EncoderProtocol(Protocol):

    def encode(
        self,
        sentences: list[str],
        batch_size: int,
        normalize_embeddings: bool,
        show_progress_bar: bool,
    ) -> NDArray[np.float32]:
        pass


class PatternClientProtocol(Protocol):

    def chat(self, prompt: str) -> str:
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replace CNC test examples with train/validation examples and complete missing patterns"
    )
    parser.add_argument("--positive-data", type=Path, default=DEFAULT_POSITIVE_PATH)
    parser.add_argument("--raw-data", type=Path, default=DEFAULT_RAW_PATH)
    parser.add_argument("--split-dir", type=Path, default=DEFAULT_SPLIT_DIR)
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA_PATH)
    parser.add_argument("--embeddings", type=Path, default=DEFAULT_EMBEDDINGS_PATH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT_PATH)
    parser.add_argument("--implicit-audit", type=Path, default=DEFAULT_IMPLICIT_AUDIT_PATH)
    parser.add_argument("--pattern-examples", type=Path, default=DEFAULT_PATTERN_EXAMPLES_PATH)
    parser.add_argument("--api-key", type=Path, default=DEFAULT_API_KEY_PATH)
    parser.add_argument("--deepseek-model", default=DEFAULT_DEEPSEEK_MODEL)
    parser.add_argument("--deepseek-base-url", default=DEFAULT_DEEPSEEK_BASE_URL)
    parser.add_argument("--embedding-model", default=DEFAULT_EMBEDDING_MODEL)
    parser.add_argument("--embedding-device", default="cpu")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--skip-replacement", action="store_true")
    parser.add_argument(
        "--train-only-support",
        action="store_true",
        help="用未使用的 train 正例替换全部 validation support",
    )
    parser.add_argument("--skip-completion", action="store_true")
    parser.add_argument("--force-implicit-patterns", action="store_true")
    parser.add_argument("--max-completions", type=int)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    previous_manifest = (
        json.loads(args.manifest.read_text(encoding="utf-8")) if args.manifest.exists() else {}
    )
    metadata = _read_jsonl(args.metadata)
    embeddings = np.load(args.embeddings).astype(np.float32, copy=False)
    if len(metadata) != embeddings.shape[0]:
        raise ValueError(
            f"metadata 与 embeddings 行数不一致：metadata={len(metadata)} embeddings={embeddings.shape[0]}"
        )

    enriched = _enrich_samples(
        _read_jsonl(args.positive_data),
        _read_raw_rows(args.raw_data),
    )
    split_ids = load_split_ids(args.split_dir)
    run_replacements: list[dict[str, Any]] = []

    if not args.skip_replacement:
        from sentence_transformers import SentenceTransformer

        encoder = SentenceTransformer(args.embedding_model, device=args.embedding_device)
        metadata, embeddings, test_replacements = replace_test_examples(
            metadata=metadata,
            embeddings=embeddings,
            enriched=enriched,
            split_ids=split_ids,
            encoder=encoder,
            batch_size=args.batch_size,
        )
        run_replacements.extend(test_replacements)
        LOGGER.info("test 泄漏替换完成：replacements=%s", len(test_replacements))
        if args.train_only_support:
            metadata, embeddings, validation_replacements = replace_validation_examples_with_train(
                metadata=metadata,
                embeddings=embeddings,
                enriched=enriched,
                split_ids=split_ids,
                encoder=encoder,
                batch_size=args.batch_size,
            )
            run_replacements.extend(validation_replacements)
            LOGGER.info(
                "validation support 替换完成：replacements=%s",
                len(validation_replacements),
            )

    completion_summary: dict[str, Any] = {}
    client: PatternClientProtocol | None = None
    if not args.skip_completion:
        prompt_examples = load_pattern_prompt_examples(args.pattern_examples, limit=14)
        client = DeepSeekJudgeClient(
            api_key_path=args.api_key,
            model=args.deepseek_model,
            base_url=args.deepseek_base_url,
            max_tokens=1024,
            thinking="disabled",
        )
        completion_summary["explicit_connective"] = complete_missing_patterns(
            metadata=metadata,
            client=client,
            prompt_examples=prompt_examples,
            audit_path=args.audit,
            model=args.deepseek_model,
            max_completions=args.max_completions,
        )
        LOGGER.info("pattern 补齐完成：%s", completion_summary)

    if args.force_implicit_patterns:
        if client is None:
            client = DeepSeekJudgeClient(
                api_key_path=args.api_key,
                model=args.deepseek_model,
                base_url=args.deepseek_base_url,
                max_tokens=1024,
                thinking="disabled",
            )
        completion_summary["implicit_lexical_proxy"] = complete_implicit_patterns(
            metadata=metadata,
            client=client,
            audit_path=args.implicit_audit,
            model=args.deepseek_model,
            max_completions=args.max_completions,
        )
        LOGGER.info("隐式 pattern 词语补齐完成：%s", completion_summary)

    validate_database(
        metadata,
        embeddings,
        split_ids,
        require_train_only=args.train_only_support,
    )
    replacement_history = list(previous_manifest.get("replacements", []))
    replacement_history.extend(run_replacements)
    manifest = build_manifest(
        metadata=metadata,
        split_ids=split_ids,
        replacements=replacement_history,
        current_replacement_count=len(run_replacements),
        completion_summary=completion_summary,
        embedding_model=args.embedding_model,
        deepseek_model=args.deepseek_model,
        audit_path=args.audit,
        implicit_audit_path=args.implicit_audit,
        train_only_support=args.train_only_support,
    )
    write_jsonl_atomic(args.metadata, metadata)
    write_npy_atomic(args.embeddings, embeddings)
    write_json_atomic(args.manifest, manifest)
    LOGGER.info("CNC RAG 数据库已写入：metadata=%s embeddings=%s", args.metadata, args.embeddings)


def load_split_ids(split_dir: Path) -> dict[str, set[int]]:
    split_ids: dict[str, set[int]] = {}
    for split in ("train", "validation", "test"):
        rows = _read_jsonl(split_dir / f"{split}.jsonl")
        split_ids[split] = {int(row["id"]) for row in rows}
    overlaps = (
        split_ids["train"] & split_ids["validation"]
        | split_ids["train"] & split_ids["test"]
        | split_ids["validation"] & split_ids["test"]
    )
    if overlaps:
        raise ValueError(f"CNC SFT split ID 重叠：{sorted(overlaps)[:10]}")
    return split_ids


def replace_test_examples(
    *,
    metadata: list[dict[str, Any]],
    embeddings: NDArray[np.float32],
    enriched: list[dict[str, Any]],
    split_ids: dict[str, set[int]],
    encoder: EncoderProtocol,
    batch_size: int = 64,
) -> tuple[list[dict[str, Any]], NDArray[np.float32], list[dict[str, Any]]]:
    allowed_ids = split_ids["train"] | split_ids["validation"]
    test_ids = split_ids["test"]
    enriched_by_id = {int(item["sample_id"]): item for item in enriched}
    current_ids = {int(row["sample_id"]) for row in metadata}
    leaked_positions = [
        index for index, row in enumerate(metadata) if int(row["sample_id"]) in test_ids
    ]
    unknown_ids = current_ids - allowed_ids - test_ids
    if unknown_ids:
        raise ValueError(f"数据库存在不属于 CNC SFT splits 的 ID：{sorted(unknown_ids)[:10]}")
    if not leaked_positions:
        return metadata, embeddings, []

    candidates = [
        item
        for item in enriched
        if int(item["sample_id"]) in allowed_ids and int(item["sample_id"]) not in current_ids
    ]
    candidate_vectors = np.asarray(
        encoder.encode(
            [item["sentence"] for item in candidates],
            batch_size=batch_size,
            normalize_embeddings=True,
            show_progress_bar=True,
        ),
        dtype=np.float32,
    )
    if candidate_vectors.shape[0] != len(candidates):
        raise ValueError("候选 embedding 行数与候选 metadata 不一致")

    leaked_by_stratum: dict[tuple[str, bool, str], list[int]] = defaultdict(list)
    candidate_by_stratum: dict[tuple[str, bool, str], list[int]] = defaultdict(list)
    for position in leaked_positions:
        sample_id = int(metadata[position]["sample_id"])
        leaked_by_stratum[_stratum(enriched_by_id[sample_id])].append(position)
    for index, item in enumerate(candidates):
        candidate_by_stratum[_stratum(item)].append(index)

    output_metadata = [dict(row) for row in metadata]
    output_embeddings = embeddings.copy()
    replacements: list[dict[str, Any]] = []
    for stratum, positions in sorted(leaked_by_stratum.items(), key=lambda item: str(item[0])):
        candidate_indices = candidate_by_stratum.get(stratum, [])
        if len(candidate_indices) < len(positions):
            raise ValueError(
                f"分层 {stratum} 的替换候选不足：need={len(positions)} available={len(candidate_indices)}"
            )
        old_vectors = normalize_matrix(output_embeddings[positions])
        new_vectors = normalize_matrix(candidate_vectors[candidate_indices])
        row_indices, column_indices = linear_sum_assignment(-(old_vectors @ new_vectors.T))
        if len(row_indices) != len(positions):
            raise RuntimeError(f"分层 {stratum} 未完成一对一替换")
        for row_index, column_index in zip(row_indices, column_indices, strict=True):
            position = positions[int(row_index)]
            candidate_index = candidate_indices[int(column_index)]
            old_id = int(output_metadata[position]["sample_id"])
            candidate = candidates[candidate_index]
            new_id = int(candidate["sample_id"])
            similarity = float(old_vectors[int(row_index)] @ new_vectors[int(column_index)])
            output_metadata[position] = _metadata_record(candidate)
            output_embeddings[position] = candidate_vectors[candidate_index]
            replacements.append(
                {
                    "position": position,
                    "old_test_id": old_id,
                    "new_support_id": new_id,
                    "new_split": "train" if new_id in split_ids["train"] else "validation",
                    "stratum": list(stratum),
                    "cosine_similarity": round(similarity, 6),
                }
            )

    replacements.sort(key=lambda item: int(item["position"]))
    return output_metadata, output_embeddings, replacements


def replace_validation_examples_with_train(
    *,
    metadata: list[dict[str, Any]],
    embeddings: NDArray[np.float32],
    enriched: list[dict[str, Any]],
    split_ids: dict[str, set[int]],
    encoder: EncoderProtocol,
    batch_size: int = 64,
) -> tuple[list[dict[str, Any]], NDArray[np.float32], list[dict[str, Any]]]:
    train_ids = split_ids["train"]
    validation_ids = split_ids["validation"]
    test_ids = split_ids["test"]
    enriched_by_id = {int(item["sample_id"]): item for item in enriched}
    current_ids = {int(row["sample_id"]) for row in metadata}
    validation_positions = [
        index for index, row in enumerate(metadata) if int(row["sample_id"]) in validation_ids
    ]
    unknown_ids = current_ids - train_ids - validation_ids - test_ids
    if unknown_ids:
        raise ValueError(f"数据库存在不属于 CNC SFT splits 的 ID：{sorted(unknown_ids)[:10]}")
    if not validation_positions:
        return metadata, embeddings, []

    current_texts = {normalize_text(str(row["sentence"])) for row in metadata}
    held_out_texts = {
        normalize_text(str(item["sentence"]))
        for item in enriched
        if int(item["sample_id"]) in validation_ids | test_ids
    }
    held_out_docs = {
        str(item["doc_id"])
        for item in enriched
        if int(item["sample_id"]) in validation_ids | test_ids
    }
    candidates = [
        item
        for item in enriched
        if int(item["sample_id"]) in train_ids
        and int(item["sample_id"]) not in current_ids
        and normalize_text(str(item["sentence"])) not in current_texts
        and normalize_text(str(item["sentence"])) not in held_out_texts
        and str(item["doc_id"]) not in held_out_docs
    ]
    candidate_vectors = np.asarray(
        encoder.encode(
            [item["sentence"] for item in candidates],
            batch_size=batch_size,
            normalize_embeddings=True,
            show_progress_bar=True,
        ),
        dtype=np.float32,
    )
    if candidate_vectors.shape[0] != len(candidates):
        raise ValueError("候选 embedding 行数与候选 metadata 不一致")


    position_groups: dict[tuple[str, bool], list[int]] = defaultdict(list)
    candidate_groups: dict[tuple[str, bool], list[int]] = defaultdict(list)
    for position in validation_positions:
        item = enriched_by_id[int(metadata[position]["sample_id"])]
        relation_bucket, has_gold_signal, _length_bucket = _stratum(item)
        position_groups[(relation_bucket, has_gold_signal)].append(position)
    for index, item in enumerate(candidates):
        relation_bucket, has_gold_signal, _length_bucket = _stratum(item)
        candidate_groups[(relation_bucket, has_gold_signal)].append(index)

    length_rank = {"short": 0, "medium": 1, "long": 2}
    output_metadata = [dict(row) for row in metadata]
    output_embeddings = embeddings.copy()
    replacements: list[dict[str, Any]] = []
    for group, positions in sorted(position_groups.items(), key=lambda item: str(item[0])):
        candidate_indices = candidate_groups.get(group, [])
        if len(candidate_indices) < len(positions):
            raise ValueError(
                f"分组 {group} 的 train 替换候选不足："
                f"need={len(positions)} available={len(candidate_indices)}"
            )
        old_vectors = normalize_matrix(output_embeddings[positions])
        new_vectors = normalize_matrix(candidate_vectors[candidate_indices])
        similarities = old_vectors @ new_vectors.T
        length_cost = np.empty_like(similarities)
        for row_index, position in enumerate(positions):
            old_item = enriched_by_id[int(output_metadata[position]["sample_id"])]
            old_length = _stratum(old_item)[2]
            for column_index, candidate_index in enumerate(candidate_indices):
                new_length = _stratum(candidates[candidate_index])[2]
                length_cost[row_index, column_index] = abs(
                    length_rank[old_length] - length_rank[new_length]
                )

        assignment_cost = 3.0 * length_cost - similarities
        row_indices, column_indices = linear_sum_assignment(assignment_cost)
        if len(row_indices) != len(positions):
            raise RuntimeError(f"分组 {group} 未完成一对一 train 替换")
        for row_index, column_index in zip(row_indices, column_indices, strict=True):
            position = positions[int(row_index)]
            candidate_index = candidate_indices[int(column_index)]
            old_id = int(output_metadata[position]["sample_id"])
            old_item = enriched_by_id[old_id]
            candidate = candidates[candidate_index]
            new_id = int(candidate["sample_id"])
            old_stratum = _stratum(old_item)
            new_stratum = _stratum(candidate)
            output_metadata[position] = _metadata_record(candidate)
            output_embeddings[position] = candidate_vectors[candidate_index]
            replacements.append(
                {
                    "position": position,
                    "replacement_type": "validation_to_train",
                    "old_validation_id": old_id,
                    "new_support_id": new_id,
                    "new_split": "train",
                    "old_stratum": list(old_stratum),
                    "new_stratum": list(new_stratum),
                    "length_bucket_relaxed": old_stratum[2] != new_stratum[2],
                    "cosine_similarity": round(
                        float(similarities[int(row_index), int(column_index)]), 6
                    ),
                }
            )

    replacements.sort(key=lambda item: int(item["position"]))
    return output_metadata, output_embeddings, replacements


def load_pattern_prompt_examples(path: Path, limit: int = 14) -> list[dict[str, str]]:
    examples: list[dict[str, str]] = []
    seen_patterns: set[str] = set()
    with path.open("r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            pattern = str(row.get("causality_phrase") or "").strip()
            if not pattern or pattern.casefold() in seen_patterns:
                continue
            sentence = re.sub(r"</?(?:cause|effect)>", "", str(row.get("sentence") or ""))
            cause = str(row.get("cause_t") or "").strip()
            effect = str(row.get("effect_t") or "").strip()
            if not sentence or not cause or not effect:
                continue
            examples.append(
                {
                    "sentence": sentence,
                    "cause": cause,
                    "effect": effect,
                    "causal_connective": pattern,
                }
            )
            seen_patterns.add(pattern.casefold())
            if len(examples) == limit:
                break
    if len(examples) != limit:
        raise ValueError(f"无法从 Pattern DB 读取 {limit} 个不同 connective examples")
    return examples


def complete_missing_patterns(
    *,
    metadata: list[dict[str, Any]],
    client: PatternClientProtocol,
    prompt_examples: list[dict[str, str]],
    audit_path: Path,
    model: str,
    max_completions: int | None = None,
) -> dict[str, int]:
    cached = load_terminal_audit(audit_path)
    targets = [row for row in metadata if not row.get("signals")]
    if max_completions is not None:
        targets = targets[:max_completions]

    counts: Counter[str] = Counter()
    for offset, row in enumerate(targets, start=1):
        sample_id = int(row["sample_id"])
        sentence_hash = hashlib.sha256(str(row["sentence"]).encode("utf-8")).hexdigest()
        audit = cached.get(sample_id)
        if audit and audit.get("sentence_sha256") == sentence_hash:
            patterns = [str(value) for value in audit.get("patterns", [])]
            apply_patterns(row, patterns, model)
            counts[f"cached_{audit['status']}"] += 1
            continue

        prompt = build_pattern_prompt(row, prompt_examples)
        status = "failed"
        patterns: list[str] = []
        raw_response = ""
        error = ""
        for attempt in range(2):
            raw_response = client.chat(prompt)
            try:
                patterns = parse_pattern_response(raw_response, str(row["sentence"]))
                status = "updated" if patterns else "no_explicit_pattern"
                apply_patterns(row, patterns, model)
                error = ""
                break
            except (json.JSONDecodeError, TypeError, ValueError) as exc:
                error = str(exc)
                if attempt == 0:
                    prompt += (
                        "\n\nYour previous response was invalid. "
                        f"Validation error: {error}. Previous response: {raw_response}. "
                        "Return a corrected JSON object only."
                    )

        audit = {
            "sample_id": sample_id,
            "sentence_sha256": sentence_hash,
            "model": model,
            "status": status,
            "patterns": patterns,
            "raw_response": raw_response,
            "error": error,
        }
        append_jsonl(audit_path, audit)
        counts[status] += 1
        LOGGER.info(
            "DeepSeek pattern progress：%s/%s sample_id=%s status=%s patterns=%s",
            offset,
            len(targets),
            sample_id,
            status,
            patterns,
        )
    counts["targets"] = len(targets)
    return dict(sorted(counts.items()))


def build_pattern_prompt(
    row: dict[str, Any],
    prompt_examples: list[dict[str, str]],
) -> str:
    target = {
        "sentence": row["sentence"],
        "relations": [
            {
                "relation_index": index,
                "cause": triple["cause"],
                "effect": triple["effect"],
            }
            for index, triple in enumerate(row.get("triples", []))
        ],
    }
    examples = [
        {
            "sentence": example["sentence"],
            "relations": [
                {
                    "relation_index": 0,
                    "cause": example["cause"],
                    "effect": example["effect"],
                }
            ],
            "output": {
                "patterns": [
                    {
                        "relation_index": 0,
                        "causal_connective": example["causal_connective"],
                    }
                ]
            },
        }
        for example in prompt_examples
    ]
    return (
        "A sentence known to express causality and its gold cause-effect relations are provided. "
        "Following the causal-connective extraction method in the supplied Pattern RAG paper, "
        "identify the shortest explicit phrase in the original sentence that linguistically signals "
        "each relation. The connective must be a verbatim contiguous substring of the sentence. "
        "Do not invent or paraphrase a connective. If a relation is implicit and has no explicit "
        "connective, use an empty string. Return exactly one JSON object in this schema: "
        '{"patterns":[{"relation_index":0,"causal_connective":"..."}]}. '
        "Return one item for every relation_index and no other text.\n\n"
        f"Paper-style examples:\n{json.dumps(examples, ensure_ascii=False)}\n\n"
        f"Target:\n{json.dumps(target, ensure_ascii=False)}"
    )


def complete_implicit_patterns(
    *,
    metadata: list[dict[str, Any]],
    client: PatternClientProtocol,
    audit_path: Path,
    model: str,
    max_completions: int | None = None,
) -> dict[str, int]:
    cached = load_terminal_audit(audit_path)
    targets = [row for row in metadata if not row.get("signals")]
    if max_completions is not None:
        targets = targets[:max_completions]

    counts: Counter[str] = Counter()
    for offset, row in enumerate(targets, start=1):
        sample_id = int(row["sample_id"])
        sentence_hash = hashlib.sha256(str(row["sentence"]).encode("utf-8")).hexdigest()
        audit = cached.get(sample_id)
        if audit and audit.get("sentence_sha256") == sentence_hash:
            patterns = [str(value) for value in audit.get("patterns", [])]
            apply_implicit_patterns(row, patterns, model)
            counts["cached_updated"] += 1
            continue

        prompt = build_implicit_pattern_prompt(row)
        status = "failed"
        patterns: list[str] = []
        raw_response = ""
        error = ""
        for attempt in range(2):
            raw_response = client.chat(prompt)
            try:
                patterns = parse_implicit_pattern_response(raw_response, str(row["sentence"]))
                apply_implicit_patterns(row, patterns, model)
                status = "updated"
                error = ""
                break
            except (json.JSONDecodeError, TypeError, ValueError) as exc:
                error = str(exc)
                if attempt == 0:
                    prompt += (
                        "\n\nYour previous response was invalid. "
                        f"Validation error: {error}. Previous response: {raw_response}. "
                        "Return a corrected JSON object containing at least one word pattern only."
                    )

        audit = {
            "sample_id": sample_id,
            "sentence_sha256": sentence_hash,
            "model": model,
            "status": status,
            "patterns": patterns,
            "raw_response": raw_response,
            "error": error,
        }
        append_jsonl(audit_path, audit)
        counts[status] += 1
        LOGGER.info(
            "DeepSeek implicit pattern progress：%s/%s sample_id=%s status=%s patterns=%s",
            offset,
            len(targets),
            sample_id,
            status,
            patterns,
        )
    counts["targets"] = len(targets)
    return dict(sorted(counts.items()))


def build_implicit_pattern_prompt(row: dict[str, Any]) -> str:
    target = {
        "sentence": row["sentence"],
        "relations": [
            {
                "relation_index": index,
                "cause": triple["cause"],
                "effect": triple["effect"],
            }
            for index, triple in enumerate(row.get("triples", []))
        ],
    }
    return (
        "The sentence has an annotated causal relation but no standalone explicit causal connective. "
        "Select one or more lexical proxy patterns so the existing surface-form Pattern RAG matcher "
        "can index this example without adding a new schema field. Each pattern must be a verbatim "
        "contiguous word or multiword phrase from the original sentence. Do not use a comma, colon, "
        "semicolon, dash, or any punctuation-only pattern. Prefer an action, reaction, causal event, "
        "or result word such as protesting, blocked, attack, quit, or crisis. If no informative event "
        "word is available, a grammatical linker such as and or in is allowed. These are retrieval "
        "proxies, not claims that the words are explicit causal connectives. Return exactly one JSON "
        'object in this schema: {"patterns":[{"relation_index":0,"causal_connective":"word or phrase"}]}. '
        "Return at least one non-empty pattern and no other text.\n\n"
        f"Target:\n{json.dumps(target, ensure_ascii=False)}"
    )


def parse_implicit_pattern_response(response: str, sentence: str) -> list[str]:
    patterns = parse_pattern_response(response, sentence)
    if not patterns:
        raise ValueError("隐式 pattern 必须至少包含一个原句词语")
    for pattern in patterns:
        if not re.fullmatch(r"[A-Za-z0-9]+(?:[A-Za-z0-9'’ -]*[A-Za-z0-9])?", pattern):
            raise ValueError(f"隐式 pattern 必须是词语且不能含标点：{pattern!r}")
    return patterns


def apply_implicit_patterns(row: dict[str, Any], patterns: list[str], model: str) -> None:
    if not patterns:
        raise ValueError("不能写入空的隐式 pattern")
    row["signals"] = patterns
    row["signal_source"] = f"{model}_implicit_lexical_proxy"


def parse_pattern_response(response: str, sentence: str) -> list[str]:
    cleaned = response.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", cleaned, flags=re.IGNORECASE)
    payload = json.loads(cleaned)
    if not isinstance(payload, dict) or not isinstance(payload.get("patterns"), list):
        raise TypeError("DeepSeek 输出必须包含 patterns list")

    patterns: list[str] = []
    for item in payload["patterns"]:
        if not isinstance(item, dict):
            raise TypeError("patterns 中每一项必须是 object")
        value = str(item.get("causal_connective") or "").strip()
        if not value:
            continue
        original = find_original_substring(sentence, value)
        if original is None:
            raise ValueError(f"pattern 不是原句连续子串：{value!r}")
        if not re.search(r"[A-Za-z0-9]", original):
            raise ValueError(f"pattern 不能只有标点：{value!r}")
        if original.casefold() not in {pattern.casefold() for pattern in patterns}:
            patterns.append(original)
    return patterns


def find_original_substring(sentence: str, value: str) -> str | None:
    parts = value.split()
    if not parts:
        return None
    match = re.search(r"\s+".join(re.escape(part) for part in parts), sentence, re.IGNORECASE)
    return match.group(0) if match else None


def apply_patterns(row: dict[str, Any], patterns: list[str], model: str) -> None:
    row["signals"] = patterns
    row["signal_source"] = model if patterns else "none_explicit_after_deepseek"


def load_terminal_audit(path: Path) -> dict[int, dict[str, Any]]:
    if not path.exists():
        return {}
    cached: dict[int, dict[str, Any]] = {}
    for row in _read_jsonl(path):
        if row.get("status") in TERMINAL_AUDIT_STATUSES:
            cached[int(row["sample_id"])] = row
    return cached


def validate_database(
    metadata: list[dict[str, Any]],
    embeddings: NDArray[np.float32],
    split_ids: dict[str, set[int]],
    *,
    require_train_only: bool = False,
) -> None:
    if len(metadata) != embeddings.shape[0]:
        raise ValueError("最终 metadata 与 embeddings 行数不一致")
    sample_ids = [int(row["sample_id"]) for row in metadata]
    if len(sample_ids) != len(set(sample_ids)):
        raise ValueError("最终数据库存在重复 sample_id")
    allowed_ids = split_ids["train"] | split_ids["validation"]
    invalid_ids = set(sample_ids) - allowed_ids
    if invalid_ids:
        raise ValueError(f"最终数据库仍包含非 train/validation ID：{sorted(invalid_ids)[:10]}")
    if set(sample_ids) & split_ids["test"]:
        raise ValueError("最终数据库与 test split 重叠")
    if require_train_only and set(sample_ids) - split_ids["train"]:
        raise ValueError("最终数据库仍包含非 train support")
    if not np.isfinite(embeddings).all():
        raise ValueError("最终 embeddings 含 NaN 或 Inf")


def build_manifest(
    *,
    metadata: list[dict[str, Any]],
    split_ids: dict[str, set[int]],
    replacements: list[dict[str, Any]],
    current_replacement_count: int,
    completion_summary: dict[str, Any],
    embedding_model: str,
    deepseek_model: str,
    audit_path: Path,
    implicit_audit_path: Path,
    train_only_support: bool,
) -> dict[str, Any]:
    sample_ids = [int(row["sample_id"]) for row in metadata]
    source_counts = Counter(
        "train" if sample_id in split_ids["train"] else "validation" for sample_id in sample_ids
    )
    signal_sources = Counter(str(row.get("signal_source", "unknown")) for row in metadata)
    return {
        "strategy": (
            "retain eligible support rows; replace test rows with globally matched nearest "
            "train/validation positives; optionally replace validation support with unused train "
            "positives while preserving relation/signal strata and minimizing length relaxation; complete "
            "empty causal-connective patterns with the paper-style 14-shot DeepSeek prompt; "
            "assign original-sentence lexical proxy words to the remaining implicit cases"
        ),
        "train_only_support": train_only_support,
        "embedding_model": embedding_model,
        "pattern_completion_model": deepseek_model,
        "pattern_completion_audit": str(audit_path),
        "implicit_pattern_completion_audit": str(implicit_audit_path),
        "summary": {
            "support_samples": len(metadata),
            "support_relations": sum(int(row.get("relation_count", 0)) for row in metadata),
            "support_split": dict(sorted(source_counts.items())),
            "test_sample_overlap": len(set(sample_ids) & split_ids["test"]),
            "validation_sample_overlap": len(set(sample_ids) & split_ids["validation"]),
            "replacement_count": len(replacements),
            "current_replacement_count": current_replacement_count,
            "signal_source": dict(sorted(signal_sources.items())),
            "rows_without_pattern": sum(not row.get("signals") for row in metadata),
            "unique_patterns": len(
                {
                    str(signal).casefold()
                    for row in metadata
                    for signal in row.get("signals", [])
                    if str(signal).strip()
                }
            ),
            "completion_run": completion_summary,
        },
        "support_ids": sample_ids,
        "replacements": replacements,
    }


def normalize_matrix(matrix: NDArray[np.float32]) -> NDArray[np.float32]:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return (matrix / norms).astype(np.float32, copy=False)


def normalize_text(value: str) -> str:
    return " ".join(value.casefold().split())


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as file:
        file.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_jsonl_atomic(path: Path, rows: list[dict[str, Any]]) -> None:
    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.parent.mkdir(parents=True, exist_ok=True)
    with temp_path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")
    temp_path.replace(path)


def write_npy_atomic(path: Path, matrix: NDArray[np.float32]) -> None:
    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.parent.mkdir(parents=True, exist_ok=True)
    with temp_path.open("wb") as file:
        np.save(file, matrix)
    temp_path.replace(path)


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temp_path.replace(path)


if __name__ == "__main__":
    main()
