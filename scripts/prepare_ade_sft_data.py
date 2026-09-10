"""Create compact, relation-stratified ADE splits for supervised fine-tuning."""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import random
import re
from collections import Counter
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]


DEFAULT_SOURCE_PATH = (
    PROJECT_ROOT / "Data" / "ADE_split_archive_70_30" / "Dataset_3_ADE_train.jsonl"
)
DEFAULT_TEST_PATH = PROJECT_ROOT / "Data" / "Dataset_3_ADE_modified.jsonl"
DEFAULT_PROMPT_PATH = PROJECT_ROOT / "prompts" / "ade_sft_v1.txt"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "Data" / "ADE_sft_gemma_v1"
DEFAULT_NEGATIVE_COUNT = 4_180

CNC_TRAIN_SIZE = 1_537
CNC_VALIDATION_SIZE = 500
DEFAULT_VALIDATION_RATIO = CNC_VALIDATION_SIZE / (CNC_TRAIN_SIZE + CNC_VALIDATION_SIZE)
DEFAULT_SEED = 42
SPLITS = ("train", "validation")
OUTPUT_FILES = (
    "train.jsonl",
    "validation.jsonl",
    "dataset_info.json",
    "split_manifest.json",
    "audit.json",
)
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare relation-stratified ADE SFT data")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE_PATH)
    parser.add_argument("--test", type=Path, default=DEFAULT_TEST_PATH)
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--negative-count", type=int, default=DEFAULT_NEGATIVE_COUNT)
    parser.add_argument("--validation-ratio", type=float, default=DEFAULT_VALIDATION_RATIO)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    args = parse_args()
    manifest, audit = prepare_ade_sft_data(
        source_path=args.source,
        test_path=args.test,
        prompt_path=args.prompt,
        output_dir=args.output_dir,
        negative_count=args.negative_count,
        validation_ratio=args.validation_ratio,
        seed=args.seed,
        overwrite=args.overwrite,
    )
    LOGGER.info("ADE SFT data written to %s", args.output_dir)
    LOGGER.info("Split sizes: %s", manifest["actual_sizes"])
    LOGGER.info("All audit checks passed: %s", all(audit["checks"].values()))


def prepare_ade_sft_data(
    source_path: Path,
    test_path: Path,
    prompt_path: Path,
    output_dir: Path,
    negative_count: int = DEFAULT_NEGATIVE_COUNT,
    validation_ratio: float = DEFAULT_VALIDATION_RATIO,
    seed: int = DEFAULT_SEED,
    overwrite: bool = False,
) -> tuple[dict[str, Any], dict[str, Any]]:
    if negative_count <= 0:
        raise ValueError("negative_count must be positive")
    if not 0.0 < validation_ratio < 1.0:
        raise ValueError("validation_ratio must be between 0 and 1")

    source_rows = _read_jsonl(source_path)
    test_rows = _read_jsonl(test_path)
    _validate_rows(source_rows, "ADE train pool")
    _validate_rows(test_rows, "ADE held-out test")
    system_prompt = _read_training_prompt(prompt_path)

    buckets = _bucket_rows(source_rows)
    if negative_count > len(buckets["negative"]):
        raise ValueError(
            f"Requested {negative_count} negatives but source has only {len(buckets['negative'])}"
        )

    rng = random.Random(seed)
    selected_buckets = {
        "negative": rng.sample(buckets["negative"], negative_count),
        "single_relation": list(buckets["single_relation"]),
        "multi_relation": list(buckets["multi_relation"]),
    }
    split_rows: dict[str, list[dict[str, Any]]] = {split: [] for split in SPLITS}
    split_bucket_targets: dict[str, dict[str, int]] = {split: {} for split in SPLITS}

    for bucket_name, rows in selected_buckets.items():
        shuffled = list(rows)
        rng.shuffle(shuffled)
        train_count = _train_count(len(shuffled), validation_ratio)
        assigned = {
            "train": shuffled[:train_count],
            "validation": shuffled[train_count:],
        }
        for split in SPLITS:
            split_rows[split].extend(assigned[split])
            split_bucket_targets[split][bucket_name] = len(assigned[split])

    for split in SPLITS:
        rng.shuffle(split_rows[split])

    output_rows = {
        split: [_to_sft_record(row, system_prompt) for row in split_rows[split]]
        for split in SPLITS
    }
    audit = _build_audit(
        source_rows=source_rows,
        test_rows=test_rows,
        selected_buckets=selected_buckets,
        split_rows=split_rows,
        split_bucket_targets=split_bucket_targets,
        system_prompt=system_prompt,
        negative_count=negative_count,
    )
    if not all(audit["checks"].values()):
        failed = [name for name, passed in audit["checks"].items() if not passed]
        raise RuntimeError(f"ADE SFT audit failed: {', '.join(failed)}")

    _ensure_output_is_safe(output_dir, overwrite=overwrite)
    output_dir.mkdir(parents=True, exist_ok=True)
    for split in SPLITS:
        _write_jsonl(output_dir / f"{split}.jsonl", output_rows[split])
    _write_json(output_dir / "dataset_info.json", _dataset_info())

    data_hashes = {
        f"{split}.jsonl": _sha256(output_dir / f"{split}.jsonl") for split in SPLITS
    }
    manifest = {
        "strategy": "retain all positives, sample negatives 1:2, then stratify by 0/1/2+ relations",
        "strategy_version": 2,
        "seed": seed,
        "validation_ratio": validation_ratio,
        "reference_split": {
            "dataset": "CNC_sft_gemma_v1",
            "train": CNC_TRAIN_SIZE,
            "validation": CNC_VALIDATION_SIZE,
            "train_to_validation_ratio": CNC_TRAIN_SIZE / CNC_VALIDATION_SIZE,
        },
        "negative_count": negative_count,
        "source": {
            "path": _portable_path(source_path),
            "sha256": _sha256(source_path),
            "samples": len(source_rows),
            "distribution": _distribution(source_rows),
        },
        "held_out_test": {
            "path": _portable_path(test_path),
            "sha256": _sha256(test_path),
            "samples": len(test_rows),
            "distribution": _distribution(test_rows),
            "included_in_sft_files": False,
        },
        "prompt": {
            "source_path": _portable_path(prompt_path),
            "source_sha256": _sha256(prompt_path),
            "derivation": "compressed zero-shot ADE rules aligned to the CNC SFT prompt budget",
            "few_shot_examples": 0,
            "rag_placeholder": False,
        },
        "selected_distribution": _distribution(
            [row for rows in selected_buckets.values() for row in rows]
        ),
        "target_bucket_sizes": split_bucket_targets,
        "actual_sizes": {split: len(split_rows[split]) for split in SPLITS},
        "actual_distribution": {
            split: _distribution(split_rows[split]) for split in SPLITS
        },
        "split_ids": {
            split: [row["id"] for row in split_rows[split]] for split in SPLITS
        },
        "data_sha256": data_hashes,
        "evaluation_note": (
            "Data/Dataset_3_ADE_modified.jsonl remains the held-out test set and is not copied "
            "into this SFT directory."
        ),
    }
    _write_json(output_dir / "split_manifest.json", manifest)
    _write_json(output_dir / "audit.json", audit)
    return manifest, audit


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _read_training_prompt(path: Path) -> str:
    prompt = path.read_text(encoding="utf-8").strip()
    forbidden_markers = (
        "{rag_examples}",
        "retrieved examples",
        "Fixed examples",
        "\nInput:\n",
    )
    if not prompt or any(marker.lower() in prompt.lower() for marker in forbidden_markers):
        raise ValueError("ADE SFT prompt must be the frozen v9.1 pure-rule prompt")
    return prompt


def _validate_rows(rows: list[dict[str, Any]], label: str) -> None:
    if not rows:
        raise ValueError(f"{label} is empty")
    ids: set[Any] = set()
    texts: set[str] = set()
    for row in rows:
        sample_id = row.get("id")
        text = row.get("text")
        has_causal = row.get("has_causal")
        relations = row.get("relations")
        normalized = _normalize_text(text) if isinstance(text, str) else ""
        if sample_id in ids:
            raise ValueError(f"{label} has duplicate id={sample_id}")
        if not normalized or normalized in texts:
            raise ValueError(f"{label} has empty or duplicate normalized text at id={sample_id}")
        if not isinstance(has_causal, bool) or not isinstance(relations, list):
            raise ValueError(f"{label} has invalid labels at id={sample_id}")
        if has_causal != bool(relations):
            raise ValueError(f"{label} has inconsistent has_causal at id={sample_id}")
        for relation in relations:
            if not isinstance(relation, dict):
                raise ValueError(f"{label} has a non-object relation at id={sample_id}")
            for role in ("cause", "effect"):
                span = relation.get(role)
                if not isinstance(span, str) or not span or span not in text:
                    raise ValueError(f"{label} has an invalid {role} span at id={sample_id}")
        ids.add(sample_id)
        texts.add(normalized)


def _bucket_rows(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    buckets = {"negative": [], "single_relation": [], "multi_relation": []}
    for row in rows:
        count = len(row["relations"])
        bucket = "negative" if count == 0 else "single_relation" if count == 1 else "multi_relation"
        buckets[bucket].append(row)
    return buckets


def _train_count(size: int, validation_ratio: float) -> int:
    count = int(size * (1.0 - validation_ratio) + 0.5)
    if size >= 2:
        return min(size - 1, max(1, count))
    return size


def _to_sft_record(row: dict[str, Any], system_prompt: str) -> dict[str, Any]:
    triples = [
        {
            "cause": {"span": relation["cause"]},
            "relation": "caused",
            "effect": {"span": relation["effect"]},
        }
        for relation in row["relations"]
    ]
    target = {"has_causal": row["has_causal"], "triples": triples}
    return {
        "id": row["id"],
        "text": row["text"],
        "has_causal": row["has_causal"],
        "relations": row["relations"],
        "relation_count": len(row["relations"]),
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Input text:\n{row['text']}"},
            {
                "role": "assistant",
                "content": json.dumps(target, ensure_ascii=False, separators=(",", ":")),
            },
        ],
    }


def _build_audit(
    source_rows: list[dict[str, Any]],
    test_rows: list[dict[str, Any]],
    selected_buckets: dict[str, list[dict[str, Any]]],
    split_rows: dict[str, list[dict[str, Any]]],
    split_bucket_targets: dict[str, dict[str, int]],
    system_prompt: str,
    negative_count: int,
) -> dict[str, Any]:
    source_positive_ids = {row["id"] for row in source_rows if row["has_causal"]}
    selected_rows = [row for rows in selected_buckets.values() for row in rows]
    selected_ids = {row["id"] for row in selected_rows}
    split_ids = {split: {row["id"] for row in split_rows[split]} for split in SPLITS}
    split_texts = {
        split: {_normalize_text(row["text"]) for row in split_rows[split]} for split in SPLITS
    }
    test_texts = {_normalize_text(row["text"]) for row in test_rows}
    actual_bucket_sizes = {
        split: {name: len(rows) for name, rows in _bucket_rows(split_rows[split]).items()}
        for split in SPLITS
    }
    checks = {
        "all_source_positives_retained": source_positive_ids <= selected_ids,
        "selected_negative_count_exact": len(selected_buckets["negative"]) == negative_count,
        "selected_rows_assigned_once": (
            len(split_rows["train"]) + len(split_rows["validation"]) == len(selected_rows)
            and not (split_ids["train"] & split_ids["validation"])
        ),
        "train_validation_text_overlap_zero": not (
            split_texts["train"] & split_texts["validation"]
        ),
        "held_out_test_text_overlap_zero": not (
            (split_texts["train"] | split_texts["validation"]) & test_texts
        ),
        "bucket_sizes_match_targets": actual_bucket_sizes == split_bucket_targets,
        "multi_relation_present_in_train": actual_bucket_sizes["train"]["multi_relation"] > 0,
        "multi_relation_present_in_validation": actual_bucket_sizes["validation"]["multi_relation"] > 0,
        "labels_consistent": all(row["has_causal"] == bool(row["relations"]) for row in selected_rows),
        "all_spans_are_exact_substrings": all(
            relation[role] in row["text"]
            for row in selected_rows
            for relation in row["relations"]
            for role in ("cause", "effect")
        ),
        "prompt_is_zero_shot": "{rag_examples}" not in system_prompt,
    }
    return {
        "checks": checks,
        "source_distribution": _distribution(source_rows),
        "selected_distribution": _distribution(selected_rows),
        "split_distribution": {
            split: _distribution(split_rows[split]) for split in SPLITS
        },
        "bucket_targets": split_bucket_targets,
        "bucket_actual": actual_bucket_sizes,
        "overlap": {
            "train_validation_ids": len(split_ids["train"] & split_ids["validation"]),
            "train_validation_texts": len(split_texts["train"] & split_texts["validation"]),
            "sft_held_out_test_texts": len(
                (split_texts["train"] | split_texts["validation"]) & test_texts
            ),
        },
    }


def _distribution(rows: list[dict[str, Any]]) -> dict[str, Any]:
    counts = Counter(len(row["relations"]) for row in rows)
    return {
        "samples": len(rows),
        "positive": sum(row["has_causal"] for row in rows),
        "negative": sum(not row["has_causal"] for row in rows),
        "relations": sum(len(row["relations"]) for row in rows),
        "single_relation_samples": counts[1],
        "multi_relation_samples": sum(value for key, value in counts.items() if key >= 2),
        "max_relations_per_sample": max(counts, default=0),
        "relation_count": {str(key): value for key, value in sorted(counts.items())},
    }


def _dataset_info() -> dict[str, Any]:
    tags = {
        "role_tag": "role",
        "content_tag": "content",
        "user_tag": "user",
        "assistant_tag": "assistant",
        "system_tag": "system",
    }
    return {
        f"ade_sft_{split}": {
            "file_name": f"{split}.jsonl",
            "formatting": "sharegpt",
            "columns": {"messages": "messages"},
            "tags": tags,
        }
        for split in SPLITS
    }


def _normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def _ensure_output_is_safe(output_dir: Path, overwrite: bool) -> None:
    existing = [output_dir / name for name in OUTPUT_FILES if (output_dir / name).exists()]
    if existing and not overwrite:
        raise FileExistsError(
            "Output exists; pass --overwrite to replace: " + ", ".join(path.name for path in existing)
        )


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _portable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


if __name__ == "__main__":
    main()
