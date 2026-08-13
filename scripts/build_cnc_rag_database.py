"""Build a document-disjoint CNC RAG support DB and complementary eval set."""

from __future__ import annotations

import argparse
import ast
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np
from sklearn.cluster import KMeans


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

DEFAULT_POSITIVE_PATH = PROJECT_ROOT / "Data" / "Dataset_1_CNC_positive_only.jsonl"
DEFAULT_RAW_PATH = PROJECT_ROOT / "Data" / "raw" / "Dataset_1_CNC_raw.csv"
DEFAULT_METADATA_PATH = PROJECT_ROOT / "RAG Database" / "cnc_examples.jsonl"
DEFAULT_EMBEDDINGS_PATH = PROJECT_ROOT / "RAG Database" / "cnc_embeddings.npy"
DEFAULT_EVAL_PATH = PROJECT_ROOT / "Data" / "Dataset_1_CNC_positive_rag_eval.jsonl"
DEFAULT_MANIFEST_PATH = PROJECT_ROOT / "RAG Database" / "cnc_split_manifest.json"
DEFAULT_MODEL_NAME = "BAAI/bge-small-en-v1.5"
SIGNAL_RE = re.compile(r"<SIG\d+>(.*?)</SIG\d+>", re.IGNORECASE | re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the CNC multi-triple RAG database")
    parser.add_argument("--positive-data", type=Path, default=DEFAULT_POSITIVE_PATH)
    parser.add_argument("--raw-data", type=Path, default=DEFAULT_RAW_PATH)
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA_PATH)
    parser.add_argument("--embeddings", type=Path, default=DEFAULT_EMBEDDINGS_PATH)
    parser.add_argument("--eval-data", type=Path, default=DEFAULT_EVAL_PATH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--model", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--support-size", type=int, default=600)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--batch-size", type=int, default=64)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    samples = _read_jsonl(args.positive_data)
    raw_rows = _read_raw_rows(args.raw_data)
    enriched = _enrich_samples(samples, raw_rows)
    if not 0 < args.support_size < len(enriched):
        raise ValueError("support-size must be between 1 and the number of positive samples minus 1")

    from sentence_transformers import SentenceTransformer

    print(f"Loading embedding model: {args.model} on {args.device}", flush=True)
    encoder = SentenceTransformer(args.model, device=args.device)
    print(f"Encoding {len(enriched)} CNC positive sentences...", flush=True)
    embeddings = np.asarray(
        encoder.encode(
            [item["sentence"] for item in enriched],
            batch_size=args.batch_size,
            normalize_embeddings=True,
            show_progress_bar=True,
        ),
        dtype=np.float32,
    )
    print(f"Encoding complete: shape={embeddings.shape}", flush=True)

    target_quotas = _target_quotas(enriched, args.support_size)
    print(f"Selecting {args.support_size} stratified semantic representatives...", flush=True)
    support_indices = _select_cluster_representatives(
        enriched,
        embeddings,
        target_quotas,
        seed=args.seed,
    )
    support_indices = _make_document_disjoint(
        enriched,
        embeddings,
        support_indices,
        target_quotas,
        support_size=args.support_size,
    )
    print("Selection and document-level split complete.", flush=True)

    eval_indices = sorted(set(range(len(enriched))) - support_indices)
    support_indices = sorted(support_indices)
    _validate_split(enriched, support_indices, eval_indices, args.support_size)
    np.random.default_rng(args.seed).shuffle(eval_indices)

    metadata_rows = [_metadata_record(enriched[index]) for index in support_indices]
    eval_rows = [samples[index] for index in eval_indices]
    support_embeddings = embeddings[support_indices].astype(np.float32, copy=False)

    _write_jsonl(args.metadata, metadata_rows)
    args.embeddings.parent.mkdir(parents=True, exist_ok=True)
    np.save(args.embeddings, support_embeddings)
    _write_jsonl(args.eval_data, eval_rows)

    manifest = _build_manifest(
        enriched=enriched,
        support_indices=support_indices,
        eval_indices=eval_indices,
        target_quotas=target_quotas,
        model_name=args.model,
        seed=args.seed,
        metadata_path=args.metadata,
        embeddings_path=args.embeddings,
        eval_path=args.eval_data,
    )
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(manifest["summary"], ensure_ascii=False, indent=2))


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _read_raw_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def _enrich_samples(
    samples: list[dict[str, Any]],
    raw_rows: list[dict[str, str]],
) -> list[dict[str, Any]]:
    raw_by_text: dict[str, dict[str, str]] = {}
    for row in raw_rows:
        text = row.get("text", "")
        if text in raw_by_text:
            raise ValueError(f"Raw CNC text is not unique: {text[:100]}")
        raw_by_text[text] = row

    enriched: list[dict[str, Any]] = []
    for sample in samples:
        text = str(sample["text"])
        raw = raw_by_text.get(text)
        if raw is None:
            raise ValueError(f"Cannot map cleaned CNC sample id={sample.get('id')} back to raw CSV")
        relations = sample.get("relations", [])
        _validate_relation_spans(text, relations, sample.get("id"))
        signals = _extract_signals(raw.get("causal_text_w_pairs", ""))
        enriched.append(
            {
                "sample": sample,
                "sample_id": sample.get("id"),
                "sentence": text,
                "relations": relations,
                "signals": signals,
                "has_gold_signal": bool(signals),
                "doc_id": raw.get("doc_id", ""),
                "raw_index": raw.get("index", ""),
                "relation_bucket": "single" if len(relations) == 1 else "multi",
                "length_bucket": _length_bucket(text),
                "word_count": len(text.split()),
            }
        )
    return enriched


def _extract_signals(value: str) -> list[str]:
    try:
        tagged_relations = ast.literal_eval(value)
    except (SyntaxError, ValueError):
        tagged_relations = [value]
    if not isinstance(tagged_relations, list):
        tagged_relations = [str(tagged_relations)]
    signals = [" ".join(signal.split()) for relation in tagged_relations for signal in SIGNAL_RE.findall(relation)]
    return list(dict.fromkeys(signal for signal in signals if signal))


def _validate_relation_spans(text: str, relations: list[dict[str, Any]], sample_id: Any) -> None:
    normalized_text = " ".join(text.lower().split())
    if not relations:
        raise ValueError(f"Positive CNC sample id={sample_id} has no relations")
    for relation in relations:
        cause = " ".join(str(relation.get("cause", "")).lower().split())
        effect = " ".join(str(relation.get("effect", "")).lower().split())
        if not cause or not effect or cause not in normalized_text or effect not in normalized_text:
            raise ValueError(f"Relation span does not occur in CNC sample id={sample_id}: {relation}")


def _length_bucket(text: str) -> str:
    word_count = len(text.split())
    if word_count <= 20:
        return "short"
    if word_count <= 40:
        return "medium"
    return "long"


def _stratum(item: dict[str, Any]) -> tuple[str, bool, str]:
    return item["relation_bucket"], item["has_gold_signal"], item["length_bucket"]


def _target_quotas(enriched: list[dict[str, Any]], support_size: int) -> dict[tuple[str, bool, str], int]:
    counts = Counter(_stratum(item) for item in enriched)
    weighted: dict[tuple[str, bool, str], float] = {}
    length_weights = {"short": 0.9, "medium": 1.0, "long": 1.25}
    for key, count in counts.items():
        relation_bucket, _has_signal, length_bucket = key
        relation_weight = 1.35 if relation_bucket == "multi" else 1.0
        weighted[key] = count * relation_weight * length_weights[length_bucket]

    total_weight = sum(weighted.values())
    raw_quotas = {key: support_size * value / total_weight for key, value in weighted.items()}
    quotas = {key: min(counts[key], int(raw_quotas[key])) for key in counts}
    remaining = support_size - sum(quotas.values())
    candidates = sorted(
        counts,
        key=lambda key: (raw_quotas[key] - quotas[key], str(key)),
        reverse=True,
    )
    while remaining:
        changed = False
        for key in candidates:
            if quotas[key] < counts[key]:
                quotas[key] += 1
                remaining -= 1
                changed = True
                if remaining == 0:
                    break
        if not changed:
            raise RuntimeError("Unable to allocate CNC support quotas")
    return quotas


def _select_cluster_representatives(
    enriched: list[dict[str, Any]],
    embeddings: np.ndarray,
    quotas: dict[tuple[str, bool, str], int],
    seed: int,
) -> set[int]:
    grouped: dict[tuple[str, bool, str], list[int]] = defaultdict(list)
    for index, item in enumerate(enriched):
        grouped[_stratum(item)].append(index)

    selected: set[int] = set()
    for offset, key in enumerate(sorted(grouped, key=str)):
        indices = grouped[key]
        quota = quotas[key]
        if quota >= len(indices):
            selected.update(indices)
            continue
        matrix = embeddings[indices]
        model = KMeans(n_clusters=quota, random_state=seed + offset, n_init=10)
        labels = model.fit_predict(matrix)
        for cluster_id in range(quota):
            member_positions = np.flatnonzero(labels == cluster_id)
            center = model.cluster_centers_[cluster_id]
            distances = np.linalg.norm(matrix[member_positions] - center, axis=1)
            selected.add(indices[int(member_positions[int(np.argmin(distances))])])
    if len(selected) != sum(quotas.values()):
        raise RuntimeError(f"Cluster selection produced {len(selected)} rows, expected {sum(quotas.values())}")
    return selected


def _make_document_disjoint(
    enriched: list[dict[str, Any]],
    embeddings: np.ndarray,
    selected: set[int],
    target_quotas: dict[tuple[str, bool, str], int],
    support_size: int,
) -> set[int]:
    by_doc: dict[str, list[int]] = defaultdict(list)
    for index, item in enumerate(enriched):
        by_doc[str(item["doc_id"])].append(index)

    for indices in by_doc.values():
        if any(index in selected for index in indices):
            selected.update(indices)

    singleton_selected = [
        indices[0]
        for indices in by_doc.values()
        if len(indices) == 1 and indices[0] in selected
    ]
    while len(selected) > support_size:
        selected_list = sorted(selected)
        selected_matrix = embeddings[selected_list]
        similarities = embeddings[singleton_selected] @ selected_matrix.T
        current_counts = Counter(_stratum(enriched[index]) for index in selected)
        removable: list[tuple[int, float, int]] = []
        for row_index, index in enumerate(singleton_selected):
            if index not in selected:
                continue
            own_position = selected_list.index(index)
            row = similarities[row_index].copy()
            row[own_position] = -1.0
            redundancy = float(np.max(row))
            surplus = current_counts[_stratum(enriched[index])] - target_quotas[_stratum(enriched[index])]
            removable.append((surplus, redundancy, index))
        if not removable:
            raise RuntimeError("Cannot reduce document-disjoint support split to requested size")
        _surplus, _redundancy, remove_index = max(removable)
        selected.remove(remove_index)
    return selected


def _validate_split(
    enriched: list[dict[str, Any]],
    support_indices: list[int],
    eval_indices: list[int],
    support_size: int,
) -> None:
    if len(support_indices) != support_size:
        raise RuntimeError(f"Support split has {len(support_indices)} rows, expected {support_size}")
    if set(support_indices) & set(eval_indices):
        raise RuntimeError("CNC support and eval indices overlap")
    support_docs = {enriched[index]["doc_id"] for index in support_indices}
    eval_docs = {enriched[index]["doc_id"] for index in eval_indices}
    if support_docs & eval_docs:
        raise RuntimeError("CNC support and eval documents overlap")
    support_texts = {enriched[index]["sentence"] for index in support_indices}
    eval_texts = {enriched[index]["sentence"] for index in eval_indices}
    if support_texts & eval_texts:
        raise RuntimeError("CNC support and eval texts overlap")


def _metadata_record(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "dataset": "cnc",
        "sample_id": item["sample_id"],
        "doc_id": item["doc_id"],
        "raw_index": item["raw_index"],
        "sentence": item["sentence"],
        "triples": [
            {"cause": relation["cause"], "effect": relation["effect"]}
            for relation in item["relations"]
        ],
        "signals": item["signals"],
        "signal_source": "gold" if item["signals"] else "none",
        "relation_count": len(item["relations"]),
        "word_count": item["word_count"],
    }


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def _distribution(enriched: list[dict[str, Any]], indices: list[int]) -> dict[str, Any]:
    selected = [enriched[index] for index in indices]
    return {
        "samples": len(selected),
        "relations": sum(len(item["relations"]) for item in selected),
        "relation_count": dict(sorted(Counter(len(item["relations"]) for item in selected).items())),
        "relation_bucket": dict(sorted(Counter(item["relation_bucket"] for item in selected).items())),
        "length_bucket": dict(sorted(Counter(item["length_bucket"] for item in selected).items())),
        "gold_signal": dict(sorted(Counter(str(item["has_gold_signal"]).lower() for item in selected).items())),
        "documents": len({item["doc_id"] for item in selected}),
    }


def _build_manifest(
    enriched: list[dict[str, Any]],
    support_indices: list[int],
    eval_indices: list[int],
    target_quotas: dict[tuple[str, bool, str], int],
    model_name: str,
    seed: int,
    metadata_path: Path,
    embeddings_path: Path,
    eval_path: Path,
) -> dict[str, Any]:
    support_distribution = _distribution(enriched, support_indices)
    eval_distribution = _distribution(enriched, eval_indices)
    summary = {
        "source_samples": len(enriched),
        "support": support_distribution,
        "evaluation": eval_distribution,
        "sample_overlap": 0,
        "document_overlap": 0,
    }
    return {
        "strategy": "weighted relation/signal/length strata with BGE k-means medoids; document-disjoint",
        "seed": seed,
        "embedding_model": model_name,
        "paths": {
            "metadata": str(metadata_path),
            "embeddings": str(embeddings_path),
            "evaluation": str(eval_path),
        },
        "target_quotas": {"|".join(map(str, key)): value for key, value in sorted(target_quotas.items(), key=lambda item: str(item[0]))},
        "summary": summary,
        "support_ids": [enriched[index]["sample_id"] for index in support_indices],
        "evaluation_ids": [enriched[index]["sample_id"] for index in eval_indices],
    }


if __name__ == "__main__":
    main()
