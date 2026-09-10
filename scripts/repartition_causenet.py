"""Repartition the retained CauseNet pool into train, validation, and test splits."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "Data"
TRAIN_PATH = DATA_DIR / "finetuning" / "Dataset_4_causenet_train.jsonl"
VALIDATION_PATH = DATA_DIR / "finetuning" / "Dataset_4_causenet_validation.jsonl"
TEST_PATH = DATA_DIR / "Dataset_4_causenet_modified.jsonl"
UNUSED_PATH = DATA_DIR / "finetuning" / "Dataset_4_causenet_unused.jsonl"
MANIFEST_PATH = DATA_DIR / "CauseNet_split_manifest.json"
STATS_PATH = DATA_DIR / "stats.json"

DEFAULT_TEST_SIZE = 2_000
DEFAULT_SEED = 20260524
TARGET_RATIOS = {"train": 0.5136, "validation": 0.1671, "test": 0.3194}

Row = dict[str, Any]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Repartition the existing CauseNet pool")
    parser.add_argument("--data-dir", type=Path, default=DATA_DIR)
    parser.add_argument("--test-size", type=int, default=DEFAULT_TEST_SIZE)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def derive_split_sizes(test_size: int = DEFAULT_TEST_SIZE) -> dict[str, int]:
    if test_size <= 0:
        raise ValueError("test_size must be positive")
    test_ratio = TARGET_RATIOS["test"]
    return {
        "train": round(test_size * TARGET_RATIOS["train"] / test_ratio),
        "validation": round(test_size * TARGET_RATIOS["validation"] / test_ratio),
        "test": test_size,
    }


def repartition_rows(
    rows: Iterable[Row],
    split_sizes: dict[str, int],
    seed: int = DEFAULT_SEED,
) -> dict[str, list[Row]]:
    canonical_rows = [_canonicalize_row(row) for row in rows]
    _validate_source_pool(canonical_rows)
    requested = sum(split_sizes.values())
    if requested > len(canonical_rows):
        raise ValueError(
            f"CauseNet pool is too small: requested={requested}, available={len(canonical_rows)}"
        )

    buckets: dict[str, list[Row]] = {}
    for row in canonical_rows:
        buckets.setdefault(_relation_bucket(row), []).append(row)

    rng = random.Random(seed)
    for bucket_name in sorted(buckets):
        buckets[bucket_name].sort(key=_stable_row_key)
        rng.shuffle(buckets[bucket_name])

    offsets = {bucket_name: 0 for bucket_name in buckets}
    result: dict[str, list[Row]] = {}
    source_counts = {bucket_name: len(bucket) for bucket_name, bucket in buckets.items()}
    for split_name in ("train", "validation", "test"):
        quotas = _proportional_quotas(source_counts, split_sizes[split_name])
        selected: list[Row] = []
        for bucket_name in sorted(buckets):
            start = offsets[bucket_name]
            end = start + quotas[bucket_name]
            if end > len(buckets[bucket_name]):
                raise RuntimeError(f"Stratum {bucket_name} was over-allocated")
            selected.extend(buckets[bucket_name][start:end])
            offsets[bucket_name] = end
        rng.shuffle(selected)
        result[split_name] = _renumber(selected)

    unused: list[Row] = []
    for bucket_name in sorted(buckets):
        unused.extend(buckets[bucket_name][offsets[bucket_name] :])
    rng.shuffle(unused)
    result["unused"] = _renumber(unused)
    _validate_output_splits(result, split_sizes, len(canonical_rows))
    return result


def run_repartition(
    data_dir: Path | str = DATA_DIR,
    test_size: int = DEFAULT_TEST_SIZE,
    seed: int = DEFAULT_SEED,
) -> dict[str, Any]:
    target_dir = Path(data_dir)
    train_path = target_dir / "finetuning" / "Dataset_4_causenet_train.jsonl"
    validation_path = target_dir / "finetuning" / "Dataset_4_causenet_validation.jsonl"
    test_path = target_dir / "Dataset_4_causenet_modified.jsonl"
    unused_path = target_dir / "finetuning" / "Dataset_4_causenet_unused.jsonl"
    manifest_path = target_dir / "CauseNet_split_manifest.json"
    stats_path = target_dir / "stats.json"

    source_paths = [train_path, test_path]
    if validation_path.exists() and unused_path.exists():
        source_paths.extend([validation_path, unused_path])
    rows = [row for path in source_paths for row in _read_jsonl(path)]
    split_sizes = derive_split_sizes(test_size)
    splits = repartition_rows(rows, split_sizes=split_sizes, seed=seed)

    output_paths = {
        "train": train_path,
        "validation": validation_path,
        "test": test_path,
        "unused": unused_path,
    }
    for split_name, path in output_paths.items():
        _write_jsonl(path, splits[split_name])

    selected_total = sum(split_sizes.values())
    manifest = {
        "strategy": "deterministic relation-count-stratified repartition of existing CauseNet train/test pool",
        "seed": seed,
        "requested_ratios_percent": {
            "train": 51.36,
            "validation": 16.71,
            "test": 31.94,
        },
        "source_files": [str(path.relative_to(target_dir)) for path in source_paths],
        "source_samples": len(rows),
        "selected_samples": selected_total,
        "target_sizes": split_sizes,
        "actual_ratios_percent": {
            name: round(len(splits[name]) / selected_total * 100, 6)
            for name in ("train", "validation", "test")
        },
        "splits": {
            name: {
                **_split_stats(splits[name], name, seed),
                "path": str(output_paths[name].relative_to(target_dir)),
                "sha256": _sha256(output_paths[name]),
            }
            for name in ("train", "validation", "test", "unused")
        },
        "overlap": _overlap_audit(splits),
    }
    _write_json(manifest_path, manifest)
    _update_stats(stats_path, splits, seed)
    return manifest


def _proportional_quotas(source_counts: dict[str, int], target_size: int) -> dict[str, int]:
    total = sum(source_counts.values())
    raw = {name: target_size * count / total for name, count in source_counts.items()}
    quotas = {name: int(value) for name, value in raw.items()}
    remaining = target_size - sum(quotas.values())
    order = sorted(source_counts, key=lambda name: (-(raw[name] - quotas[name]), name))
    for name in order[:remaining]:
        quotas[name] += 1
    return quotas


def _relation_bucket(row: Row) -> str:
    count = len(row["relations"])
    if count == 1:
        return "1"
    if count == 2:
        return "2"
    return "3+"


def _canonicalize_row(row: Row) -> Row:
    return {
        "id": 0,
        "text": str(row.get("text", "")),
        "has_causal": bool(row.get("has_causal")),
        "relations": list(row.get("relations") or []),
    }


def _validate_source_pool(rows: list[Row]) -> None:
    if not rows:
        raise ValueError("CauseNet source pool is empty")
    texts = [row["text"] for row in rows]
    if any(not text.strip() for text in texts):
        raise ValueError("CauseNet contains an empty text")
    if len(texts) != len(set(texts)):
        raise ValueError("CauseNet source files contain overlapping or duplicate texts")
    for row in rows:
        if not row["has_causal"] or not row["relations"]:
            raise ValueError("The retained CauseNet pool is expected to contain positive examples only")


def _validate_output_splits(
    splits: dict[str, list[Row]], split_sizes: dict[str, int], source_size: int
) -> None:
    for name, expected in split_sizes.items():
        if len(splits[name]) != expected:
            raise RuntimeError(f"Unexpected {name} size: {len(splits[name])} != {expected}")
    if sum(len(rows) for rows in splits.values()) != source_size:
        raise RuntimeError("Repartition did not preserve the complete source pool")
    if any(value for value in _overlap_audit(splits).values()):
        raise RuntimeError("CauseNet output splits overlap")


def _overlap_audit(splits: dict[str, list[Row]]) -> dict[str, int]:
    names = list(splits)
    text_sets = {name: {row["text"] for row in rows} for name, rows in splits.items()}
    return {
        f"{left}_{right}": len(text_sets[left] & text_sets[right])
        for index, left in enumerate(names)
        for right in names[index + 1 :]
    }


def _renumber(rows: list[Row]) -> list[Row]:
    return [{**row, "id": index} for index, row in enumerate(rows, start=1)]


def _stable_row_key(row: Row) -> str:
    payload = json.dumps(
        {"text": row["text"], "relations": row["relations"]},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _split_stats(rows: list[Row], split_role: str, seed: int) -> dict[str, Any]:
    distribution = Counter(str(len(row["relations"])) for row in rows)
    bucket_distribution = Counter(_relation_bucket(row) for row in rows)
    return {
        "split_role": split_role,
        "split_seed": seed,
        "output_samples": len(rows),
        "causal_samples": sum(bool(row["has_causal"]) for row in rows),
        "non_causal_samples": sum(not row["has_causal"] for row in rows),
        "total_relations": sum(len(row["relations"]) for row in rows),
        "relation_count_distribution": dict(
            sorted(distribution.items(), key=lambda item: int(item[0]))
        ),
        "stratification_bucket_distribution": dict(sorted(bucket_distribution.items())),
        "warnings": {},
    }


def _update_stats(path: Path, splits: dict[str, list[Row]], seed: int) -> None:
    stats = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    stats["causenet_train"] = _split_stats(splits["train"], "train", seed)
    stats["causenet_validation"] = _split_stats(splits["validation"], "validation", seed)
    stats["causenet"] = _split_stats(splits["test"], "test", seed)
    stats["causenet_unused"] = _split_stats(splits["unused"], "unused", seed)
    stats.pop("causenet_extra", None)
    _write_json(path, stats)


def _read_jsonl(path: Path) -> list[Row]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def _write_jsonl(path: Path, rows: list[Row]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        file.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    args = parse_args()
    manifest = run_repartition(args.data_dir, test_size=args.test_size, seed=args.seed)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
