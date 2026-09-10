"""Build a train-only PolitiCAUSE RAG database without validation or test leakage."""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import logging
import sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from Data.script.clean_politicause_data import (
    select_consensus_one_to_one_annotation,
)
from scripts.build_cnc_rag_database import (
    _select_cluster_representatives,
    _target_quotas,
)
from scripts.repair_cnc_rag_database import (
    append_jsonl,
    apply_implicit_patterns,
    apply_patterns,
    build_implicit_pattern_prompt,
    build_pattern_prompt,
    find_original_substring,
    load_terminal_audit,
    load_pattern_prompt_examples,
    parse_implicit_pattern_response,
    parse_pattern_response,
    write_json_atomic,
    write_jsonl_atomic,
    write_npy_atomic,
)
from src.kg_evaluator import (
    DEFAULT_DEEPSEEK_BASE_URL,
    DEFAULT_DEEPSEEK_MODEL,
    DeepSeekJudgeClient,
)


LOGGER = logging.getLogger(__name__)
DEFAULT_DATA_DIR = PROJECT_ROOT / "Data" / "PolitiCAUSE"
DEFAULT_RAW_ANNOTATIONS_PATH = (
    PROJECT_ROOT / "Data" / "raw" / "PolitiCAUSE" / "span_annotations.csv"
)
DEFAULT_METADATA_PATH = PROJECT_ROOT / "RAG Database" / "politicause_examples.jsonl"
DEFAULT_EMBEDDINGS_PATH = PROJECT_ROOT / "RAG Database" / "politicause_embeddings.npy"
DEFAULT_MANIFEST_PATH = PROJECT_ROOT / "RAG Database" / "politicause_split_manifest.json"
DEFAULT_PATTERN_AUDIT_PATH = (
    PROJECT_ROOT / "RAG Database" / "politicause_pattern_completion.jsonl"
)
DEFAULT_IMPLICIT_AUDIT_PATH = (
    PROJECT_ROOT / "RAG Database" / "politicause_implicit_pattern_completion.jsonl"
)
DEFAULT_PATTERN_EXAMPLES_PATH = (
    PROJECT_ROOT / "RAG Database" / "comb_SCITEsemADE_CausalityPattern.csv"
)
DEFAULT_API_KEY_PATH = PROJECT_ROOT / "deepseek_api.txt"
DEFAULT_EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
DEFAULT_SUPPORT_SIZE = 1000
DEFAULT_SEED = 20260829


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="构建 PolitiCAUSE train-only RAG 数据库")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--raw-annotations", type=Path, default=DEFAULT_RAW_ANNOTATIONS_PATH)
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA_PATH)
    parser.add_argument("--embeddings", type=Path, default=DEFAULT_EMBEDDINGS_PATH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--pattern-audit", type=Path, default=DEFAULT_PATTERN_AUDIT_PATH)
    parser.add_argument("--implicit-audit", type=Path, default=DEFAULT_IMPLICIT_AUDIT_PATH)
    parser.add_argument("--pattern-examples", type=Path, default=DEFAULT_PATTERN_EXAMPLES_PATH)
    parser.add_argument("--api-key", type=Path, default=DEFAULT_API_KEY_PATH)
    parser.add_argument("--embedding-model", default=DEFAULT_EMBEDDING_MODEL)
    parser.add_argument("--embedding-device", default="cpu")
    parser.add_argument("--deepseek-model", default=DEFAULT_DEEPSEEK_MODEL)
    parser.add_argument("--deepseek-base-url", default=DEFAULT_DEEPSEEK_BASE_URL)
    parser.add_argument("--support-size", type=int, default=DEFAULT_SUPPORT_SIZE)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--pattern-workers", type=int, default=8)
    parser.add_argument("--skip-pattern-completion", action="store_true")
    parser.add_argument("--force-implicit-patterns", action="store_true")
    parser.add_argument("--max-completions", type=int)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    train = _read_jsonl(args.data_dir / "train.jsonl")
    validation = _read_jsonl(args.data_dir / "validation.jsonl")
    test = _read_jsonl(args.data_dir / "test.jsonl")
    audit = _read_jsonl(args.data_dir / "audit.jsonl")
    annotations = _read_annotations(args.raw_annotations)
    all_enriched = enrich_train_positives(train, audit, annotations)
    held_out_texts = {
        _normalize_text(str(row["text"])) for row in validation + test
    }
    enriched = [
        item
        for item in all_enriched
        if _normalize_text(str(item["sentence"])) not in held_out_texts
    ]
    LOGGER.info(
        "剔除 validation/test 重复文本：train_positives=%s excluded=%s candidates=%s",
        len(all_enriched),
        len(all_enriched) - len(enriched),
        len(enriched),
    )
    if not 0 < args.support_size <= len(enriched):
        raise ValueError("support-size 必须大于 0 且不超过训练正例数")

    from sentence_transformers import SentenceTransformer

    LOGGER.info(
        "编码 PolitiCAUSE 训练正例：samples=%s model=%s device=%s",
        len(enriched),
        args.embedding_model,
        args.embedding_device,
    )
    encoder = SentenceTransformer(args.embedding_model, device=args.embedding_device)
    all_embeddings = np.asarray(
        encoder.encode(
            [item["sentence"] for item in enriched],
            batch_size=args.batch_size,
            normalize_embeddings=True,
            show_progress_bar=True,
        ),
        dtype=np.float32,
    )
    quotas = _target_quotas(enriched, args.support_size)
    support_indices = sorted(
        _select_cluster_representatives(enriched, all_embeddings, quotas, seed=args.seed)
    )
    metadata = [_metadata_record(enriched[index]) for index in support_indices]
    support_embeddings = all_embeddings[support_indices].astype(np.float32, copy=False)
    validate_train_only_database(metadata, support_embeddings, train, validation, test)

    completion_summary: dict[str, Any] = {}
    client: DeepSeekJudgeClient | None = None
    if not args.skip_pattern_completion:
        client = DeepSeekJudgeClient(
            api_key_path=args.api_key,
            model=args.deepseek_model,
            base_url=args.deepseek_base_url,
            max_tokens=1024,
            thinking="disabled",
        )
        completion_summary["explicit_connective"] = complete_patterns_parallel(
            metadata=metadata,
            client=client,
            prompt_examples=load_pattern_prompt_examples(args.pattern_examples, limit=14),
            audit_path=args.pattern_audit,
            model=args.deepseek_model,
            workers=args.pattern_workers,
            max_completions=args.max_completions,
        )
    if args.force_implicit_patterns:
        if client is None:
            client = DeepSeekJudgeClient(
                api_key_path=args.api_key,
                model=args.deepseek_model,
                base_url=args.deepseek_base_url,
                max_tokens=1024,
                thinking="disabled",
            )
        completion_summary["implicit_lexical_proxy"] = complete_patterns_parallel(
            metadata=metadata,
            client=client,
            audit_path=args.implicit_audit,
            model=args.deepseek_model,
            workers=args.pattern_workers,
            implicit=True,
            max_completions=args.max_completions,
        )

    support_ids = {int(row["sample_id"]) for row in metadata}
    completion_summary["pattern_audit_retained_rows"] = compact_pattern_audit(
        args.pattern_audit,
        support_ids,
    )
    completion_summary["implicit_audit_retained_rows"] = compact_pattern_audit(
        args.implicit_audit,
        support_ids,
    )

    validate_train_only_database(metadata, support_embeddings, train, validation, test)
    write_jsonl_atomic(args.metadata, metadata)
    write_npy_atomic(args.embeddings, support_embeddings)
    manifest = build_manifest(
        enriched=enriched,
        train_positive_rows=len(all_enriched),
        metadata=metadata,
        quotas=quotas,
        train=train,
        validation=validation,
        test=test,
        embedding_model=args.embedding_model,
        deepseek_model=args.deepseek_model,
        seed=args.seed,
        completion_summary=completion_summary,
        paths={
            "metadata": args.metadata,
            "embeddings": args.embeddings,
            "pattern_audit": args.pattern_audit,
            "implicit_pattern_audit": args.implicit_audit,
        },
    )
    write_json_atomic(args.manifest, manifest)
    LOGGER.info("PolitiCAUSE RAG 数据库完成：%s", manifest["summary"])


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _read_annotations(path: Path) -> dict[str, list[dict[str, str]]]:
    by_text: dict[str, list[dict[str, str]]] = defaultdict(list)
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            by_text[str(row.get("text", ""))].append(row)
    return by_text


def enrich_train_positives(
    train: list[dict[str, Any]],
    audit: list[dict[str, Any]],
    annotations: dict[str, list[dict[str, str]]],
) -> list[dict[str, Any]]:
    audit_by_id = {
        int(row["id"]): row
        for row in audit
        if row.get("split") == "train"
        and row.get("status") == "included_positive_consensus_one_to_one"
    }
    enriched: list[dict[str, Any]] = []
    for sample in train:
        if not sample.get("has_causal"):
            continue
        sample_id = int(sample["id"])
        text = str(sample["text"])
        relations = list(sample.get("relations", []))
        selected, _diagnostics, exclusion_reason = select_consensus_one_to_one_annotation(
            annotations[text],
            text,
        )
        if selected is None or exclusion_reason is not None or selected["relations"] != relations:
            raise ValueError(f"训练正例 id={sample_id} 无法复现所选 span bundle")
        if len(relations) != 1 or selected["pairing_kind"] != "one_to_one":
            raise ValueError(f"训练正例 id={sample_id} 不是共识单关系样本")
        selected_row = annotations[text][int(selected["row_index"])]
        signals = _extract_connectors(selected_row.get("spans", "[]"), text)
        word_count = len(text.split())
        audit_row = audit_by_id[sample_id]
        enriched.append(
            {
                "sample_id": sample_id,
                "sentence": text,
                "relations": relations,
                "signals": signals,
                "has_gold_signal": bool(signals),
                "relation_bucket": "single",
                "length_bucket": _length_bucket(word_count),
                "word_count": word_count,
                "pairing_kind": audit_row["pairing_kind"],
                "agreement_score": audit_row["agreement_score"],
            }
        )
    return enriched


def _extract_connectors(raw_spans: str, sentence: str) -> list[str]:
    parsed = ast.literal_eval(raw_spans)
    signals: list[str] = []
    for item in parsed:
        if not isinstance(item, dict) or not str(item.get("Connector", "")).strip():
            continue
        original = find_original_substring(sentence, str(item["Connector"]))
        if original and original.casefold() not in {signal.casefold() for signal in signals}:
            signals.append(original)
    return signals


def _length_bucket(word_count: int) -> str:
    if word_count <= 20:
        return "short"
    if word_count <= 40:
        return "medium"
    return "long"


def _metadata_record(item: dict[str, Any]) -> dict[str, Any]:
    if len(item["relations"]) != 1 or item["pairing_kind"] != "one_to_one":
        raise ValueError("PolitiCAUSE RAG 仅允许共识 1C+1E 训练正例")
    return {
        "dataset": "politicause",
        "sample_id": item["sample_id"],
        "source_split": "train",
        "sentence": item["sentence"],
        "triples": [
            {"cause": relation["cause"], "effect": relation["effect"]}
            for relation in item["relations"]
        ],
        "signals": item["signals"],
        "signal_source": "gold_connector" if item["signals"] else "none",
        "relation_count": len(item["relations"]),
        "pairing_kind": item["pairing_kind"],
        "word_count": item["word_count"],
    }


def complete_patterns_parallel(
    *,
    metadata: list[dict[str, Any]],
    client: Any,
    audit_path: Path,
    model: str,
    workers: int,
    prompt_examples: list[dict[str, str]] | None = None,
    implicit: bool = False,
    max_completions: int | None = None,
) -> dict[str, int]:
    if workers <= 0:
        raise ValueError("pattern-workers 必须大于 0")
    if not implicit and prompt_examples is None:
        raise ValueError("显式 pattern 补齐需要 prompt examples")

    cached = load_terminal_audit(audit_path)
    targets = [row for row in metadata if not row.get("signals")]
    if max_completions is not None:
        targets = targets[:max_completions]
    counts: Counter[str] = Counter()
    pending: list[dict[str, Any]] = []
    for row in targets:
        sample_id = int(row["sample_id"])
        sentence_hash = hashlib.sha256(str(row["sentence"]).encode("utf-8")).hexdigest()
        audit = cached.get(sample_id)
        if audit and audit.get("sentence_sha256") == sentence_hash:
            patterns = [str(value) for value in audit.get("patterns", [])]
            _apply_completed_patterns(row, patterns, model, implicit)
            counts[f"cached_{audit['status']}"] += 1
        else:
            pending.append(row)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                _request_patterns,
                row,
                client,
                prompt_examples,
                implicit,
                model,
            ): row
            for row in pending
        }
        for offset, future in enumerate(as_completed(futures), start=1):
            row = futures[future]
            audit = future.result()
            patterns = [str(value) for value in audit["patterns"]]
            if audit["status"] == "updated":
                _apply_completed_patterns(row, patterns, model, implicit)
            elif not implicit:
                apply_patterns(row, [], model)
            append_jsonl(audit_path, audit)
            counts[str(audit["status"])] += 1
            LOGGER.info(
                "DeepSeek %s pattern progress：%s/%s sample_id=%s status=%s patterns=%s",
                "implicit" if implicit else "explicit",
                offset,
                len(pending),
                row["sample_id"],
                audit["status"],
                patterns,
            )
    counts["targets"] = len(targets)
    counts["api_requests"] = len(pending)
    return dict(sorted(counts.items()))


def _request_patterns(
    row: dict[str, Any],
    client: Any,
    prompt_examples: list[dict[str, str]] | None,
    implicit: bool,
    model: str,
) -> dict[str, Any]:
    sentence = str(row["sentence"])
    prompt = (
        build_implicit_pattern_prompt(row)
        if implicit
        else build_pattern_prompt(row, prompt_examples or [])
    )
    status = "failed"
    patterns: list[str] = []
    raw_response = ""
    error = ""
    for attempt in range(2):
        try:
            raw_response = client.chat(prompt)
            patterns = (
                parse_implicit_pattern_response(raw_response, sentence)
                if implicit
                else parse_pattern_response(raw_response, sentence)
            )
            status = "updated" if patterns else "no_explicit_pattern"
            error = ""
            break
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"
            if attempt == 0:
                prompt += (
                    "\n\nYour previous response was invalid. "
                    f"Validation error: {error}. Previous response: {raw_response}. "
                    "Return a corrected JSON object only."
                )
    return {
        "sample_id": int(row["sample_id"]),
        "sentence_sha256": hashlib.sha256(sentence.encode("utf-8")).hexdigest(),
        "model": model,
        "status": status,
        "patterns": patterns,
        "raw_response": raw_response,
        "error": error,
    }


def _apply_completed_patterns(
    row: dict[str, Any],
    patterns: list[str],
    model: str,
    implicit: bool,
) -> None:
    if implicit:
        apply_implicit_patterns(row, patterns, model)
    else:
        apply_patterns(row, patterns, model)


def compact_pattern_audit(path: Path, support_ids: set[int]) -> int:
    if not path.exists():
        return 0
    latest: dict[int, dict[str, Any]] = {}
    for row in _read_jsonl(path):
        sample_id = int(row["sample_id"])
        if sample_id in support_ids:
            latest[sample_id] = row
    retained = [latest[sample_id] for sample_id in sorted(latest)]
    write_jsonl_atomic(path, retained)
    return len(retained)


def validate_train_only_database(
    metadata: list[dict[str, Any]],
    embeddings: np.ndarray,
    train: list[dict[str, Any]],
    validation: list[dict[str, Any]],
    test: list[dict[str, Any]],
) -> None:
    if len(metadata) != embeddings.shape[0]:
        raise ValueError("metadata 与 embeddings 行数不一致")
    if not np.isfinite(embeddings).all():
        raise ValueError("embeddings 含 NaN 或 Inf")
    sample_ids = [int(row["sample_id"]) for row in metadata]
    train_positive_ids = {int(row["id"]) for row in train if row.get("has_causal")}
    held_out_ids = {int(row["id"]) for row in validation + test}
    held_out_texts = {_normalize_text(str(row["text"])) for row in validation + test}
    if len(sample_ids) != len(set(sample_ids)):
        raise ValueError("support 存在重复 sample_id")
    if set(sample_ids) - train_positive_ids:
        raise ValueError("support 含非训练正例")
    if set(sample_ids) & held_out_ids:
        raise ValueError("support 与 validation/test ID 重叠")
    if {_normalize_text(str(row["sentence"])) for row in metadata} & held_out_texts:
        raise ValueError("support 与 validation/test 文本重叠")
    if any(int(row.get("relation_count", 0)) != 1 for row in metadata):
        raise ValueError("support 含非单关系样本")
    if any(str(row.get("pairing_kind", "")) != "one_to_one" for row in metadata):
        raise ValueError("support 含非 1C+1E 配对样本")


def build_manifest(
    *,
    enriched: list[dict[str, Any]],
    train_positive_rows: int,
    metadata: list[dict[str, Any]],
    quotas: dict[tuple[str, bool, str], int],
    train: list[dict[str, Any]],
    validation: list[dict[str, Any]],
    test: list[dict[str, Any]],
    embedding_model: str,
    deepseek_model: str,
    seed: int,
    completion_summary: dict[str, Any],
    paths: dict[str, Path],
) -> dict[str, Any]:
    support_ids = {int(row["sample_id"]) for row in metadata}
    held_out_ids = {int(row["id"]) for row in validation + test}
    held_out_texts = {_normalize_text(str(row["text"])) for row in validation + test}
    support_texts = {_normalize_text(str(row["sentence"])) for row in metadata}
    relation_counts = Counter(int(row["relation_count"]) for row in metadata)
    source_counts = Counter(str(row["signal_source"]) for row in metadata)
    return {
        "strategy": (
            "从 PolitiCAUSE 清洗后 train 的共识 1C+1E 正例中，按原标注 Connector 与"
            "文本长度加权分层，再用 BGE k-means medoid 选择语义代表；显式 pattern 采用"
            "原标注 Connector 或 CNC 同款 14-shot DeepSeek prompt，剩余项可标为隐式检索代理"
        ),
        "seed": seed,
        "embedding_model": embedding_model,
        "pattern_completion_model": deepseek_model,
        "paths": {key: str(value) for key, value in paths.items()},
        "target_quotas": {
            "|".join(map(str, key)): value
            for key, value in sorted(quotas.items(), key=lambda item: str(item[0]))
        },
        "summary": {
            "train_positive_rows": train_positive_rows,
            "train_positive_candidates": len(enriched),
            "held_out_duplicate_texts_excluded": train_positive_rows - len(enriched),
            "support_samples": len(metadata),
            "support_relations": sum(int(row["relation_count"]) for row in metadata),
            "relation_count": dict(sorted(relation_counts.items())),
            "relation_bucket": dict(
                sorted(Counter("single" if count == 1 else "multi" for count in relation_counts.elements()).items())
            ),
            "length_bucket": dict(
                sorted(Counter(_length_bucket(int(row["word_count"])) for row in metadata).items())
            ),
            "signal_source": dict(sorted(source_counts.items())),
            "rows_without_pattern": sum(not row.get("signals") for row in metadata),
            "unique_patterns": len(
                {
                    str(signal).casefold()
                    for row in metadata
                    for signal in row.get("signals", [])
                    if str(signal).strip()
                }
            ),
            "validation_test_id_overlap": len(support_ids & held_out_ids),
            "validation_test_text_overlap": len(support_texts & held_out_texts),
            "train_rows": len(train),
            "validation_rows": len(validation),
            "test_rows": len(test),
            "completion_run": completion_summary,
        },
        "support_ids": sorted(support_ids),
    }


def _normalize_text(value: str) -> str:
    return " ".join(value.casefold().split())


if __name__ == "__main__":
    main()
