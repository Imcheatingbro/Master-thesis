"""Select a fixed twenty-example dataset for the Gemma overfitting diagnostic."""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import random
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = PROJECT_ROOT / "Data" / "CNC_sft_gemma_v2"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "Data" / "CNC_sft_gemma12_overfit20_v1"
DEFAULT_SEED = 20260823
CATEGORY_SPECS = (
    ("negative", 0, 10),
    ("single_positive", 1, 6),
    ("multi_positive", 2, 4),
)


def main(args: argparse.Namespace) -> None:
    audit = prepare_overfit20(args.source_dir, args.output_dir, args.seed)
    LOGGER.info("Gemma 12B overfit-20 数据已生成：%s", args.output_dir.resolve())
    LOGGER.info("样本分布：%s", audit["distribution"])
    LOGGER.info("固定样本 ID：%s", audit["selected_ids"])


def prepare_overfit20(source_dir: Path, output_dir: Path, seed: int) -> dict[str, Any]:
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    if output_dir.exists():
        raise FileExistsError(f"拒绝覆盖已有诊断数据：{output_dir}")

    split_paths = {
        split: source_dir / f"{split}.jsonl"
        for split in ("train", "validation", "test")
    }
    for path in split_paths.values():
        if not path.is_file():
            raise FileNotFoundError(path)
    source_rows = {split: _read_jsonl(path) for split, path in split_paths.items()}

    selected = _select_rows(source_rows["train"], seed)
    random.Random(seed + 1).shuffle(selected)
    rows = [row for _category, row in selected]
    categories = {int(row["id"]): category for category, row in selected}
    checks = _validate_selection(source_rows, rows, categories)
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise RuntimeError(f"overfit-20 数据审计失败：{', '.join(failed)}")

    output_dir.mkdir(parents=True)
    _write_jsonl(output_dir / "train.jsonl", rows)
    distribution = {
        "samples": len(rows),
        "positive": sum(bool(row["relations"]) for row in rows),
        "negative": sum(not row["relations"] for row in rows),
        "single_positive": sum(len(row["relations"]) == 1 for row in rows),
        "multi_positive": sum(len(row["relations"]) >= 2 for row in rows),
        "relations": sum(len(row["relations"]) for row in rows),
        "distinct_documents": len({row["doc_id"] for row in rows}),
    }
    selection = [
        {
            "order": index,
            "category": categories[int(row["id"])],
            "id": row["id"],
            "doc_id": row["doc_id"],
            "gold_relations": len(row["relations"]),
        }
        for index, row in enumerate(rows)
    ]
    _write_json(
        output_dir / "selection_manifest.json",
        {
            "purpose": "Gemma 4 12B 当前 schema 的 20 条样本记忆诊断",
            "seed": seed,
            "source_dir": str(source_dir),
            "source_train_sha256": _sha256(split_paths["train"]),
            "selection": selection,
        },
    )
    audit = {
        "purpose": "训练管线记忆测试，不是泛化评测集",
        "seed": seed,
        "source_dir": str(source_dir),
        "output_dir": str(output_dir),
        "distribution": distribution,
        "selected_ids": [row["id"] for row in rows],
        "checks": checks,
        "output_train_sha256": _sha256(output_dir / "train.jsonl"),
    }
    _write_json(output_dir / "audit.json", audit)
    return audit


def _select_rows(
    train_rows: list[dict[str, Any]], seed: int
) -> list[tuple[str, dict[str, Any]]]:
    rng = random.Random(seed)
    selected: list[tuple[str, dict[str, Any]]] = []
    used_documents: set[str] = set()
    for category, relation_count, target_count in CATEGORY_SPECS:
        if category == "multi_positive":
            candidates = [row for row in train_rows if len(row["relations"]) >= relation_count]
        else:
            candidates = [row for row in train_rows if len(row["relations"]) == relation_count]
        candidates.sort(key=lambda row: int(row["id"]))
        rng.shuffle(candidates)
        category_rows = []
        for row in candidates:
            document = str(row["doc_id"])
            if document in used_documents:
                continue
            category_rows.append(row)
            used_documents.add(document)
            if len(category_rows) == target_count:
                break
        if len(category_rows) != target_count:
            raise RuntimeError(f"{category} 无法抽取 {target_count} 个不同文档样本")
        selected.extend((category, row) for row in category_rows)
    return selected


def _validate_selection(
    source_rows: dict[str, list[dict[str, Any]]],
    rows: list[dict[str, Any]],
    categories: dict[int, str],
) -> dict[str, bool]:
    train_by_id = {int(row["id"]): row for row in source_rows["train"]}
    ids = [int(row["id"]) for row in rows]
    documents = [str(row["doc_id"]) for row in rows]
    held_out_ids = {
        int(row["id"])
        for split in ("validation", "test")
        for row in source_rows[split]
    }
    held_out_documents = {
        str(row["doc_id"])
        for split in ("validation", "test")
        for row in source_rows[split]
    }
    return {
        "exactly_20_rows": len(rows) == 20,
        "unique_ids": len(set(ids)) == 20,
        "distinct_documents": len(set(documents)) == 20,
        "all_rows_exactly_preserved": all(train_by_id[int(row["id"])] == row for row in rows),
        "ten_negative": sum(value == "negative" for value in categories.values()) == 10,
        "six_single_positive": sum(value == "single_positive" for value in categories.values()) == 6,
        "four_multi_positive": sum(value == "multi_positive" for value in categories.values()) == 4,
        "labels_and_messages_consistent": all(_row_is_consistent(row) for row in rows),
        "no_validation_or_test_ids": set(ids).isdisjoint(held_out_ids),
        "no_validation_or_test_documents": set(documents).isdisjoint(held_out_documents),
    }


def _row_is_consistent(row: dict[str, Any]) -> bool:
    messages = row["messages"]
    if [message["role"] for message in messages] != ["system", "user", "assistant"]:
        return False
    target = json.loads(messages[-1]["content"])
    expected = [
        {
            "cause": {"span": relation["cause"]},
            "relation": "caused",
            "effect": {"span": relation["effect"]},
        }
        for relation in row["relations"]
    ]
    return (
        bool(row["has_causal"]) == bool(expected)
        and bool(target["has_causal"]) == bool(expected)
        and target["triples"] == expected
    )


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="准备 Gemma 12B 过拟合诊断的固定 20 条训练样本")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    main(parser.parse_args())
