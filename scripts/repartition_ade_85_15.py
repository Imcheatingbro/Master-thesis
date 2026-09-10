"""Repartition the canonical ADE pool into an 85/15 train-test split."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRAIN_PATH = PROJECT_ROOT / "Data/finetuning/Dataset_3_ADE_train.jsonl"
DEFAULT_TEST_PATH = PROJECT_ROOT / "Data/Dataset_3_ADE_modified.jsonl"
DEFAULT_STATS_PATH = PROJECT_ROOT / "Data/stats.json"
DEFAULT_SFT_MANIFEST_PATH = PROJECT_ROOT / "Data/ADE_sft_gemma_v1/split_manifest.json"
DEFAULT_OUTPUT_MANIFEST_PATH = PROJECT_ROOT / "Data/ADE_split_85_15_manifest.json"
DEFAULT_ARCHIVE_DIR = PROJECT_ROOT / "Data/ADE_split_archive_70_30"

TRAIN_RATIO = 0.85
PRESERVED_TEST_PREFIX = 2_000
TAIL_SAMPLE_SEED = 42
EXPECTED_SOURCE_TOTAL = 19_609


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train", type=Path, default=DEFAULT_TRAIN_PATH)
    parser.add_argument("--test", type=Path, default=DEFAULT_TEST_PATH)
    parser.add_argument("--stats", type=Path, default=DEFAULT_STATS_PATH)
    parser.add_argument("--sft-manifest", type=Path, default=DEFAULT_SFT_MANIFEST_PATH)
    parser.add_argument("--output-manifest", type=Path, default=DEFAULT_OUTPUT_MANIFEST_PATH)
    parser.add_argument("--archive-dir", type=Path, default=DEFAULT_ARCHIVE_DIR)
    parser.add_argument("--seed", type=int, default=TAIL_SAMPLE_SEED)
    parser.add_argument("--preserve-prefix", type=int, default=PRESERVED_TEST_PREFIX)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = repartition(
        train_path=args.train,
        test_path=args.test,
        stats_path=args.stats,
        sft_manifest_path=args.sft_manifest,
        output_manifest_path=args.output_manifest,
        archive_dir=args.archive_dir,
        seed=args.seed,
        preserve_prefix=args.preserve_prefix,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


def repartition(
    *,
    train_path: Path,
    test_path: Path,
    stats_path: Path,
    sft_manifest_path: Path,
    output_manifest_path: Path,
    archive_dir: Path,
    seed: int = TAIL_SAMPLE_SEED,
    preserve_prefix: int = PRESERVED_TEST_PREFIX,
) -> dict[str, Any]:
    if output_manifest_path.exists():
        existing = _read_json(output_manifest_path)
        expected_hash = existing.get("new_split", {}).get("test", {}).get("sha256")
        if expected_hash and test_path.exists() and _sha256(test_path) == expected_hash:
            return {
                "status": "already_applied",
                "train_samples": existing["new_split"]["train_pool"]["distribution"]["samples"],
                "test_samples": existing["new_split"]["test"]["distribution"]["samples"],
                "manifest": _portable_path(output_manifest_path),
            }
        raise RuntimeError(f"已有 manifest 但当前 test hash 不匹配：{output_manifest_path}")

    train_rows = _read_jsonl(train_path)
    test_rows = _read_jsonl(test_path)
    if len(train_rows) + len(test_rows) != EXPECTED_SOURCE_TOTAL:
        raise ValueError(
            f"ADE source total 应为 {EXPECTED_SOURCE_TOTAL}，实际为 "
            f"{len(train_rows) + len(test_rows)}"
        )
    if preserve_prefix <= 0 or preserve_prefix >= len(test_rows):
        raise ValueError("preserve_prefix 必须大于 0 且小于当前 test 数量")

    _validate_rows(train_rows, "train")
    _validate_rows(test_rows, "test")
    old_train_hash = _sha256(train_path)
    old_test_hash = _sha256(test_path)
    old_stats_hash = _sha256(stats_path)
    old_sft_manifest_hash = _sha256(sft_manifest_path)

    prefix_rows = test_rows[:preserve_prefix]
    tail_rows = test_rows[preserve_prefix:]
    combined_rows = train_rows + test_rows
    target_test_by_label = _target_test_by_label(combined_rows, train_ratio=TRAIN_RATIO)
    target_relation_counts = _target_relation_counts(
        test_rows=test_rows,
        prefix_rows=prefix_rows,
        target_positive=target_test_by_label[True],
        target_negative=target_test_by_label[False],
    )

    prefix_counts = Counter(len(row["relations"]) for row in prefix_rows)
    needed_counts = {
        relation_count: target_count - prefix_counts.get(relation_count, 0)
        for relation_count, target_count in target_relation_counts.items()
    }
    if any(count < 0 for count in needed_counts.values()):
        raise ValueError(f"保留前缀已经超过目标分层数量：{needed_counts}")

    candidates: dict[int, list[int]] = defaultdict(list)
    for tail_index, row in enumerate(tail_rows):
        candidates[len(row["relations"])].append(tail_index)

    rng = random.Random(seed)
    selected_tail_indices: set[int] = set()
    for relation_count in sorted(needed_counts):
        group = list(candidates.get(relation_count, []))
        rng.shuffle(group)
        needed = needed_counts[relation_count]
        if len(group) < needed:
            raise ValueError(
                f"relation_count={relation_count} 候选不足：need={needed} available={len(group)}"
            )
        selected_tail_indices.update(group[:needed])

    selected_tail_rows = [
        row for index, row in enumerate(tail_rows) if index in selected_tail_indices
    ]
    moved_rows = [
        row for index, row in enumerate(tail_rows) if index not in selected_tail_indices
    ]
    new_test_rows = prefix_rows + selected_tail_rows

    max_train_id = max(int(row["id"]) for row in train_rows)
    moved_id_map: list[dict[str, int]] = []
    appended_train_rows: list[dict[str, Any]] = []
    for offset, row in enumerate(moved_rows, start=1):
        new_id = max_train_id + offset
        appended = dict(row)
        appended["id"] = new_id
        appended_train_rows.append(appended)
        moved_id_map.append({"original_test_id": int(row["id"]), "new_train_id": new_id})
    new_train_rows = train_rows + appended_train_rows

    expected_test_size = sum(target_test_by_label.values())
    if len(new_test_rows) != expected_test_size:
        raise AssertionError(f"新 test 数量错误：{len(new_test_rows)} != {expected_test_size}")
    if len(new_train_rows) + len(new_test_rows) != EXPECTED_SOURCE_TOTAL:
        raise AssertionError("重新划分后样本总数发生变化")
    if new_test_rows[:preserve_prefix] != prefix_rows:
        raise AssertionError("历史 test 前缀未被逐条保留")
    actual_test_relation_counts = Counter(len(row["relations"]) for row in new_test_rows)
    if actual_test_relation_counts != Counter(target_relation_counts):
        raise AssertionError(
            f"新 test 分层错误：{dict(actual_test_relation_counts)} != {target_relation_counts}"
        )
    _assert_text_disjoint(new_train_rows, new_test_rows)

    archive_paths = {
        "train": archive_dir / train_path.name,
        "test": archive_dir / test_path.name,
        "stats": archive_dir / stats_path.name,
        "sft_manifest": archive_dir / "ADE_sft_gemma_v1_split_manifest.json",
    }
    _archive_file(train_path, archive_paths["train"], expected_hash=old_train_hash)
    _archive_file(test_path, archive_paths["test"], expected_hash=old_test_hash)
    _archive_file(stats_path, archive_paths["stats"], expected_hash=old_stats_hash)
    _archive_file(
        sft_manifest_path,
        archive_paths["sft_manifest"],
        expected_hash=old_sft_manifest_hash,
    )

    _write_jsonl_atomic(train_path, new_train_rows)
    _write_jsonl_atomic(test_path, new_test_rows)

    stats = _read_json(stats_path)
    parent_split_seed = stats.get("ade", {}).get("split_seed")
    stats["ade"] = _stats_entry(
        new_test_rows,
        split_role="test",
        parent_split_seed=parent_split_seed,
        seed=seed,
        preserve_prefix=preserve_prefix,
    )
    stats["ade_train"] = _stats_entry(
        new_train_rows,
        split_role="train",
        parent_split_seed=parent_split_seed,
        seed=seed,
        preserve_prefix=preserve_prefix,
    )
    _write_json_atomic(stats_path, stats)

    sft_manifest = _read_json(sft_manifest_path)
    used_train_ids = {
        int(sample_id)
        for split in ("train", "validation")
        for sample_id in sft_manifest["split_ids"][split]
    }
    original_train_ids = {int(row["id"]) for row in train_rows}
    if not used_train_ids <= original_train_ids:
        raise AssertionError("冻结的 SFT IDs 不完全属于原 train pool")
    if used_train_ids & {row["id"] for row in appended_train_rows}:
        raise AssertionError("迁入 train pool 的样本意外进入冻结 SFT 数据")

    sft_manifest["source"]["path"] = _portable_path(archive_paths["train"])
    sft_manifest["held_out_test"]["path"] = _portable_path(archive_paths["test"])
    sft_manifest["current_evaluation_split_manifest"] = _portable_path(output_manifest_path)
    sft_manifest["evaluation_note"] = (
        "The E4B SFT train/validation files remain frozen. Their historical 70/30 source and "
        "held-out test snapshots are stored under Data/ADE_split_archive_70_30. Current base-model "
        "evaluation uses the canonical 85/15 test recorded in Data/ADE_split_85_15_manifest.json."
    )
    _write_json_atomic(sft_manifest_path, sft_manifest)

    train_distribution = _distribution(new_train_rows)
    test_distribution = _distribution(new_test_rows)
    selected_tail_distribution = _distribution(selected_tail_rows)
    moved_distribution = _distribution(moved_rows)
    manifest = {
        "strategy": (
            "85/15 ADE repartition; preserve historical test rows 1-2000 exactly and sample "
            "the additional test rows from the old test tail by relation count"
        ),
        "strategy_version": 1,
        "train_ratio": TRAIN_RATIO,
        "test_ratio": 1.0 - TRAIN_RATIO,
        "tail_sample_seed": seed,
        "preserved_test_prefix_rows": preserve_prefix,
        "source_split": {
            "train": {
                "path": _portable_path(archive_paths["train"]),
                "sha256": old_train_hash,
                "distribution": _distribution(train_rows),
            },
            "test": {
                "path": _portable_path(archive_paths["test"]),
                "sha256": old_test_hash,
                "distribution": _distribution(test_rows),
            },
        },
        "test_construction": {
            "target_by_label": {
                "positive": target_test_by_label[True],
                "negative": target_test_by_label[False],
            },
            "target_relation_count": {
                str(key): value for key, value in sorted(target_relation_counts.items())
            },
            "preserved_prefix_distribution": _distribution(prefix_rows),
            "selected_tail_distribution": selected_tail_distribution,
            "selected_tail_original_test_ids": [int(row["id"]) for row in selected_tail_rows],
            "prefix_preserved_exactly": True,
        },
        "new_split": {
            "train_pool": {
                "path": _portable_path(train_path),
                "sha256": _sha256(train_path),
                "distribution": train_distribution,
            },
            "test": {
                "path": _portable_path(test_path),
                "sha256": _sha256(test_path),
                "distribution": test_distribution,
            },
        },
        "frozen_e4b_sft": {
            "manifest_path": _portable_path(sft_manifest_path),
            "train_rows": len(sft_manifest["split_ids"]["train"]),
            "validation_rows": len(sft_manifest["split_ids"]["validation"]),
            "used_rows": len(used_train_ids),
            "unused_rows_before_repartition": len(train_rows) - len(used_train_ids),
            "reallocated_old_test_rows": len(moved_rows),
            "reallocated_rows_used_by_existing_e4b": 0,
            "unused_rows_after_repartition": len(new_train_rows) - len(used_train_ids),
        },
        "reallocated_from_old_test": {
            "distribution": moved_distribution,
            "id_map": moved_id_map,
        },
        "checks": {
            "total_preserved": len(new_train_rows) + len(new_test_rows) == EXPECTED_SOURCE_TOTAL,
            "train_test_text_overlap_zero": True,
            "historical_first_2000_preserved": True,
            "existing_sft_rows_unchanged": True,
            "moved_rows_excluded_from_existing_e4b": True,
        },
    }
    _write_json_atomic(output_manifest_path, manifest)

    return {
        "status": "completed",
        "train_samples": len(new_train_rows),
        "test_samples": len(new_test_rows),
        "preserved_prefix": preserve_prefix,
        "selected_from_old_test_tail": len(selected_tail_rows),
        "moved_to_unused_train_pool": len(moved_rows),
        "frozen_e4b_used_rows": len(used_train_ids),
        "unused_train_pool_rows": len(new_train_rows) - len(used_train_ids),
        "manifest": _portable_path(output_manifest_path),
    }


def _target_test_by_label(
    rows: list[dict[str, Any]], *, train_ratio: float
) -> dict[bool, int]:
    counts = Counter(bool(row["has_causal"]) for row in rows)
    return {
        label: count - int(count * train_ratio + 0.5)
        for label, count in counts.items()
    }


def _target_relation_counts(
    *,
    test_rows: list[dict[str, Any]],
    prefix_rows: list[dict[str, Any]],
    target_positive: int,
    target_negative: int,
) -> dict[int, int]:
    full_counts = Counter(len(row["relations"]) for row in test_rows)
    prefix_counts = Counter(len(row["relations"]) for row in prefix_rows)
    positive_total = sum(count for key, count in full_counts.items() if key > 0)
    if positive_total == 0:
        raise ValueError("ADE test 没有正例")

    quotas = {
        key: full_counts[key] * target_positive / positive_total
        for key in full_counts
        if key > 0
    }
    targets = {
        key: max(prefix_counts.get(key, 0), math.floor(quota))
        for key, quota in quotas.items()
    }
    if sum(targets.values()) > target_positive:
        raise ValueError("保留前缀中的正例结构无法容纳进新的正例目标")
    while sum(targets.values()) < target_positive:
        candidates = [key for key in targets if targets[key] < full_counts[key]]
        if not candidates:
            raise ValueError("无法补足新的正例目标")
        selected_key = max(candidates, key=lambda key: (quotas[key] - targets[key], -key))
        targets[selected_key] += 1

    return {0: target_negative, **dict(sorted(targets.items()))}


def _distribution(rows: list[dict[str, Any]]) -> dict[str, Any]:
    relation_counts = Counter(len(row["relations"]) for row in rows)
    positive = sum(bool(row["has_causal"]) for row in rows)
    return {
        "samples": len(rows),
        "positive": positive,
        "negative": len(rows) - positive,
        "relations": sum(len(row["relations"]) for row in rows),
        "single_relation_samples": relation_counts.get(1, 0),
        "multi_relation_samples": sum(
            count for relation_count, count in relation_counts.items() if relation_count >= 2
        ),
        "max_relations_per_sample": max(relation_counts, default=0),
        "relation_count": {
            str(key): value for key, value in sorted(relation_counts.items())
        },
    }


def _stats_entry(
    rows: list[dict[str, Any]],
    *,
    split_role: str,
    parent_split_seed: int | None,
    seed: int,
    preserve_prefix: int,
) -> dict[str, Any]:
    distribution = _distribution(rows)
    return {
        "split_role": split_role,
        "split_strategy": "85/15_preserve_first_2000_test_then_relation_stratified_tail",
        "parent_split_seed": parent_split_seed,
        "repartition_seed": seed,
        "train_ratio": TRAIN_RATIO,
        "preserved_test_prefix_rows": preserve_prefix,
        "output_samples": distribution["samples"],
        "causal_samples": distribution["positive"],
        "non_causal_samples": distribution["negative"],
        "total_relations": distribution["relations"],
        "relation_count_distribution": distribution["relation_count"],
        "warnings": {},
    }


def _validate_rows(rows: list[dict[str, Any]], label: str) -> None:
    required = {"id", "text", "has_causal", "relations"}
    ids: set[int] = set()
    for index, row in enumerate(rows):
        missing = required - row.keys()
        if missing:
            raise ValueError(f"{label}[{index}] 缺少字段：{sorted(missing)}")
        sample_id = int(row["id"])
        if sample_id in ids:
            raise ValueError(f"{label} ID 重复：{sample_id}")
        ids.add(sample_id)
        if bool(row["has_causal"]) != bool(row["relations"]):
            raise ValueError(f"{label} 标签与 relations 不一致：id={sample_id}")


def _assert_text_disjoint(
    train_rows: list[dict[str, Any]], test_rows: list[dict[str, Any]]
) -> None:
    train_texts = {_normalize_text(row["text"]) for row in train_rows}
    test_texts = {_normalize_text(row["text"]) for row in test_rows}
    overlap = train_texts & test_texts
    if overlap:
        raise ValueError(f"新 train/test 存在 {len(overlap)} 条规范化文本重叠")


def _normalize_text(value: object) -> str:
    return " ".join(str(value).split()).casefold()


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_jsonl_atomic(path: Path, rows: list[dict[str, Any]]) -> None:
    text = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    _write_text_atomic(path, text)


def _write_json_atomic(path: Path, data: dict[str, Any]) -> None:
    _write_text_atomic(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def _write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def _archive_file(source: Path, destination: Path, *, expected_hash: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        if _sha256(destination) != expected_hash:
            raise RuntimeError(f"历史快照已存在但 hash 不匹配：{destination}")
        return
    shutil.copy2(source, destination)
    if _sha256(destination) != expected_hash:
        raise RuntimeError(f"历史快照复制校验失败：{destination}")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _portable_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


if __name__ == "__main__":
    main()
