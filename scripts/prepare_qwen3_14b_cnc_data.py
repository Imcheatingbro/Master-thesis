"""Create the audited CNC training dataset used by the Qwen3-14B run."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import random
from collections import Counter
from pathlib import Path
from typing import Any

from prepare_cnc_hard_sft_data import (
    _rank_candidates,
    _score_hard_negative,
    _validate_source_splits,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = PROJECT_ROOT / "Data" / "CNC_sft"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "Data" / "CNC_sft_qwen3_14b_v1"
DEFAULT_PROMPT_PATH = PROJECT_ROOT / "prompts" / "cnc_eval_v2.txt"
DEFAULT_HARD_NEGATIVE_COUNT = 200
DEFAULT_SEED = 42
SPLITS = ("train", "validation", "test")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare the Qwen3-14B CNC SFT dataset")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--system-prompt", type=Path, default=DEFAULT_PROMPT_PATH)
    parser.add_argument("--hard-negative-count", type=int, default=DEFAULT_HARD_NEGATIVE_COUNT)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    audit = prepare_qwen3_14b_data(
        source_dir=args.source_dir,
        output_dir=args.output_dir,
        system_prompt_path=args.system_prompt,
        hard_negative_count=args.hard_negative_count,
        seed=args.seed,
        overwrite=args.overwrite,
    )
    print(f"Qwen3-14B CNC data created: {args.output_dir}")
    print(json.dumps(audit["effective_distribution"], ensure_ascii=False, indent=2))
    print(f"Audit checks passed: {all(audit['checks'].values())}")


def prepare_qwen3_14b_data(
    source_dir: Path = DEFAULT_SOURCE_DIR,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    system_prompt_path: Path = DEFAULT_PROMPT_PATH,
    hard_negative_count: int = DEFAULT_HARD_NEGATIVE_COUNT,
    seed: int = DEFAULT_SEED,
    overwrite: bool = False,
) -> dict[str, Any]:
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    system_prompt_path = system_prompt_path.resolve()
    if output_dir == source_dir:
        raise ValueError("Output directory must differ from the source directory")
    if hard_negative_count <= 0:
        raise ValueError("hard_negative_count must be positive")
    if not system_prompt_path.is_file():
        raise FileNotFoundError(system_prompt_path)

    source_paths = {split: source_dir / f"{split}.jsonl" for split in SPLITS}
    for path in source_paths.values():
        if not path.is_file():
            raise FileNotFoundError(path)
    source_rows = {split: _read_jsonl(path) for split, path in source_paths.items()}
    _validate_source_splits(
        source_rows["train"], source_rows["validation"], source_rows["test"]
    )

    prompt = system_prompt_path.read_text(encoding="utf-8").strip()
    train_rows = source_rows["train"]
    multi_rows = [row for row in train_rows if len(row["relations"]) >= 2]
    negative_rows = [row for row in train_rows if not row["relations"]]
    if hard_negative_count > len(negative_rows):
        raise ValueError("hard_negative_count exceeds the available negative rows")
    ranked_negatives = _rank_candidates(negative_rows, _score_hard_negative)
    hard_negatives = ranked_negatives[:hard_negative_count]

    derived_train: list[dict[str, Any]] = []
    for row in train_rows:
        derived_train.append(_training_instance(row, prompt, "base"))
    for row in multi_rows:
        derived_train.append(
            _training_instance(
                row,
                prompt,
                "multi_causal_oversample",
                score=len(row["relations"]),
                reasons=[f"gold_relations={len(row['relations'])}"],
            )
        )
    for score, _source_id, reasons, row in hard_negatives:
        derived_train.append(
            _training_instance(
                row,
                prompt,
                "hard_negative_oversample",
                score=score,
                reasons=reasons,
            )
        )
    random.Random(seed).shuffle(derived_train)

    output_rows = {
        "train": derived_train,
        "validation": [_replace_prompt(row, prompt) for row in source_rows["validation"]],
        "test": [_replace_prompt(row, prompt) for row in source_rows["test"]],
    }
    _ensure_output_is_safe(output_dir, overwrite)
    output_dir.mkdir(parents=True, exist_ok=True)
    for split, rows in output_rows.items():
        _write_jsonl(output_dir / f"{split}.jsonl", rows)
    _write_json(output_dir / "dataset_info.json", _dataset_info())

    selection = {
        "multi_causal_oversample": [
            {"source_id": row["id"], "gold_relations": len(row["relations"])}
            for row in multi_rows
        ],
        "hard_negative_oversample": [
            {"source_id": source_id, "score": score, "reasons": reasons}
            for score, source_id, reasons, _row in hard_negatives
        ],
    }
    _write_json(output_dir / "selection_manifest.json", selection)
    audit = _build_audit(
        source_dir=source_dir,
        output_dir=output_dir,
        system_prompt_path=system_prompt_path,
        prompt=prompt,
        source_rows=source_rows,
        output_rows=output_rows,
        selection=selection,
        seed=seed,
        hard_negative_count=hard_negative_count,
    )
    if not all(audit["checks"].values()):
        failed = [name for name, passed in audit["checks"].items() if not passed]
        raise RuntimeError(f"Qwen3-14B data audit failed: {', '.join(failed)}")
    _write_json(output_dir / "audit.json", audit)
    return audit


def _training_instance(
    row: dict[str, Any],
    prompt: str,
    kind: str,
    score: int | None = None,
    reasons: list[str] | None = None,
) -> dict[str, Any]:
    copied = _replace_prompt(row, prompt)
    copied["sampling"] = {
        "source_id": row["id"],
        "kind": kind,
        "score": score,
        "reasons": reasons or [],
    }
    return copied


def _replace_prompt(row: dict[str, Any], prompt: str) -> dict[str, Any]:
    messages = row.get("messages")
    if not isinstance(messages, list) or len(messages) != 3:
        raise ValueError(f"Invalid messages for id={row.get('id')}")
    if [message.get("role") for message in messages] != ["system", "user", "assistant"]:
        raise ValueError(f"Unexpected message roles for id={row.get('id')}")
    copied = copy.deepcopy(row)
    copied["messages"][0] = {"role": "system", "content": prompt}
    return copied


def _build_audit(
    *,
    source_dir: Path,
    output_dir: Path,
    system_prompt_path: Path,
    prompt: str,
    source_rows: dict[str, list[dict[str, Any]]],
    output_rows: dict[str, list[dict[str, Any]]],
    selection: dict[str, list[dict[str, Any]]],
    seed: int,
    hard_negative_count: int,
) -> dict[str, Any]:
    source_train = source_rows["train"]
    derived_train = output_rows["train"]
    source_by_id = {row["id"]: row for row in source_train}
    derived_counts = Counter(row["id"] for row in derived_train)
    selected_ids = {
        kind: {item["source_id"] for item in items} for kind, items in selection.items()
    }
    duplicated_ids = set().union(*selected_ids.values())
    actual_duplicated = {source_id for source_id, count in derived_counts.items() if count == 2}
    source_ids = set(source_by_id)
    eval_ids = {row["id"] for row in source_rows["validation"] + source_rows["test"]}
    kind_counts = Counter(row["sampling"]["kind"] for row in derived_train)

    checks = {
        "source_train_ids_unique": len(source_ids) == len(source_train),
        "base_train_covered": set(derived_counts) == source_ids,
        "selection_categories_disjoint": sum(len(ids) for ids in selected_ids.values())
        == len(duplicated_ids),
        "only_selected_rows_duplicated": actual_duplicated == duplicated_ids,
        "each_selected_row_occurs_twice": all(
            derived_counts[source_id] == 2 for source_id in duplicated_ids
        ),
        "each_unselected_row_occurs_once": all(
            derived_counts[source_id] == 1 for source_id in source_ids - duplicated_ids
        ),
        "multi_selection_complete": len(selected_ids["multi_causal_oversample"])
        == sum(len(row["relations"]) >= 2 for row in source_train),
        "hard_negative_target_met": len(selected_ids["hard_negative_oversample"])
        == hard_negative_count,
        "no_validation_or_test_ids_used": not (set(derived_counts) & eval_ids),
        "train_payload_preserved_except_system_and_sampling": all(
            _matches_source(row, source_by_id[row["id"]]) for row in derived_train
        ),
        "validation_and_test_payload_preserved_except_system": all(
            _matches_split(source_rows[split], output_rows[split])
            for split in ("validation", "test")
        ),
        "system_prompt_aligned_exactly": all(
            row["messages"][0] == {"role": "system", "content": prompt}
            for rows in output_rows.values()
            for row in rows
        ),
        "labels_consistent": all(
            bool(row.get("relations")) == bool(row.get("has_causal"))
            for rows in output_rows.values()
            for row in rows
        ),
    }
    return {
        "strategy": (
            "retain every source training row once; duplicate every multi-relation row and "
            "the 200 highest-scoring causal-looking negatives; do not oversample single-positive rows"
        ),
        "strategy_version": 1,
        "seed": seed,
        "source_dir": _portable_path(source_dir),
        "output_dir": _portable_path(output_dir),
        "system_prompt": {
            "path": _portable_path(system_prompt_path),
            "sha256": _sha256(system_prompt_path),
            "characters": len(prompt),
        },
        "source_hashes": {
            f"{split}.jsonl": _sha256(source_dir / f"{split}.jsonl") for split in SPLITS
        },
        "output_hashes": {
            f"{split}.jsonl": _sha256(output_dir / f"{split}.jsonl") for split in SPLITS
        },
        "selection_targets": {
            "multi_causal": len(selected_ids["multi_causal_oversample"]),
            "hard_negative": hard_negative_count,
            "hard_single_positive": 0,
        },
        "sampling_kind_counts": dict(sorted(kind_counts.items())),
        "unique_source_distribution": _distribution(source_train),
        "effective_distribution": _distribution(derived_train),
        "validation_distribution": _distribution(output_rows["validation"]),
        "test_distribution": _distribution(output_rows["test"]),
        "checks": checks,
        "notes": [
            "No validation or test example is included in training.",
            "IDs, text, Gold labels/spans, user messages, and assistant answers are unchanged.",
            "Only the system prompt and training sampling metadata are changed.",
            "Training and evaluation use the exact same cnc_eval_v2 system prompt.",
        ],
    }


def _matches_source(derived: dict[str, Any], source: dict[str, Any]) -> bool:
    derived_without_sampling = {key: value for key, value in derived.items() if key != "sampling"}
    return (
        _without_system_message(derived_without_sampling) == _without_system_message(source)
        and derived["messages"][1:] == source["messages"][1:]
    )


def _matches_split(source_rows: list[dict[str, Any]], output_rows: list[dict[str, Any]]) -> bool:
    return len(source_rows) == len(output_rows) and all(
        _without_system_message(source) == _without_system_message(output)
        and source["messages"][1:] == output["messages"][1:]
        for source, output in zip(source_rows, output_rows)
    )


def _without_system_message(row: dict[str, Any]) -> dict[str, Any]:
    copied = copy.deepcopy(row)
    copied["messages"] = copied["messages"][1:]
    return copied


def _distribution(rows: list[dict[str, Any]]) -> dict[str, Any]:
    relation_counts = Counter(len(row["relations"]) for row in rows)
    return {
        "samples": len(rows),
        "unique_source_ids": len({row["id"] for row in rows}),
        "positive": sum(bool(row["relations"]) for row in rows),
        "negative": sum(not row["relations"] for row in rows),
        "relations": sum(len(row["relations"]) for row in rows),
        "relation_count": {str(key): value for key, value in sorted(relation_counts.items())},
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
        f"cnc_qwen3_14b_{split}": {
            "file_name": f"{split}.jsonl",
            "formatting": "sharegpt",
            "columns": {"messages": "messages"},
            "tags": tags,
        }
        for split in SPLITS
    }


def _ensure_output_is_safe(output_dir: Path, overwrite: bool) -> None:
    if not output_dir.exists():
        return
    existing = list(output_dir.iterdir())
    if existing and not overwrite:
        raise FileExistsError(f"Output directory already contains files: {output_dir}")
    if overwrite:
        allowed_names = {
            "train.jsonl",
            "validation.jsonl",
            "test.jsonl",
            "dataset_info.json",
            "selection_manifest.json",
            "audit.json",
        }
        unexpected = [path for path in existing if path.name not in allowed_names or not path.is_file()]
        if unexpected:
            raise RuntimeError(f"Refusing to overwrite unexpected paths: {unexpected}")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


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
    try:
        return path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


if __name__ == "__main__":
    main()
