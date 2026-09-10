"""Resample difficult CNC examples for second-stage LoRA training."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import shutil
from collections import Counter
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = PROJECT_ROOT / "Data" / "CNC_sft"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "Data" / "CNC_sft_hard_v2"
DEFAULT_HARD_SINGLE_COUNT = 200
DEFAULT_HARD_NEGATIVE_COUNT = 200
DEFAULT_SEED = 42

STRONG_CAUSAL_PATTERNS = {
    "because": r"\bbecause\b",
    "due_to": r"\bdue\s+to\b",
    "result": r"\b(?:resulted|resulting|results?)\b",
    "cause": r"\b(?:cause|caused|causing)\b",
    "lead": r"\b(?:lead|leads|led)\s+to\b",
    "force": r"\b(?:force|forced|forcing)\b",
    "leave": r"\b(?:leave|leaves|left|leaving)\b",
    "kill_injure": r"\b(?:kill(?:ed|ing)?|injur(?:ed|ing))\b",
}
REACTION_PURPOSE_PATTERNS = {
    "protest_opposition": r"\b(?:protest(?:ed|ing|s)?|oppose[ds]?|opposition)\b",
    "support": r"\bsupport(?:ed|ing|s)?\b",
    "demand_urge": r"\b(?:demand(?:ed|ing|s)?|urg(?:e|ed|es|ing))\b",
    "blame_accuse": r"\b(?:blam(?:e|ed|es|ing)|accus(?:e|ed|es|ing|ation))\b",
    "concern_condemn": r"\b(?:concern(?:ed|s)?|condemn(?:ed|ing|s|ation)?)\b",
    "seek_prevent": r"\b(?:seek(?:ing|s)?|sought|prevent(?:ed|ing|s)?)\b",
    "commemorate": r"\bcommemorat(?:e|ed|es|ing|ion)\b",
}
TEMPORAL_AMBIGUITY_PATTERNS = {
    "after_following": r"\b(?:after|following)\b",
    "when_once": r"\b(?:when|once)\b",
    "since": r"\bsince\b",
}
WEAK_ARGUMENT_PATTERNS = {
    "to": r"\bto\b",
    "for": r"\bfor\b",
    "over": r"\bover\b",
    "against": r"\bagainst\b",
}
LEADING_FUNCTION_WORDS = re.compile(
    r"^(?:if|to|for|because|since|following|after|when|once|who|which)\b",
    flags=re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="准备 CNC 困难样本第二阶段 SFT 数据")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--hard-single-count", type=int, default=DEFAULT_HARD_SINGLE_COUNT)
    parser.add_argument("--hard-negative-count", type=int, default=DEFAULT_HARD_NEGATIVE_COUNT)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    audit = prepare_cnc_hard_sft_data(
        source_dir=args.source_dir,
        output_dir=args.output_dir,
        hard_single_count=args.hard_single_count,
        hard_negative_count=args.hard_negative_count,
        seed=args.seed,
        overwrite=args.overwrite,
    )
    print(f"CNC 困难样本数据已生成：{args.output_dir}")
    print(json.dumps(audit["effective_distribution"], ensure_ascii=False, indent=2))
    print(f"审计检查全部通过：{all(audit['checks'].values())}")


def prepare_cnc_hard_sft_data(
    source_dir: Path = DEFAULT_SOURCE_DIR,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    hard_single_count: int = DEFAULT_HARD_SINGLE_COUNT,
    hard_negative_count: int = DEFAULT_HARD_NEGATIVE_COUNT,
    seed: int = DEFAULT_SEED,
    overwrite: bool = False,
) -> dict[str, Any]:
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    source_train = source_dir / "train.jsonl"
    source_validation = source_dir / "validation.jsonl"
    source_test = source_dir / "test.jsonl"
    for path in (source_train, source_validation, source_test):
        if not path.is_file():
            raise FileNotFoundError(f"缺少 CNC SFT 源数据：{path}")
    if hard_single_count <= 0 or hard_negative_count <= 0:
        raise ValueError("困难单因果和困难负样本数量必须大于 0")

    train_rows = _read_jsonl(source_train)
    validation_rows = _read_jsonl(source_validation)
    test_rows = _read_jsonl(source_test)
    _validate_source_splits(train_rows, validation_rows, test_rows)

    multi_rows = [row for row in train_rows if len(row["relations"]) >= 2]
    single_candidates = [row for row in train_rows if len(row["relations"]) == 1]
    negative_candidates = [row for row in train_rows if not row["relations"]]
    if hard_single_count > len(single_candidates):
        raise ValueError("困难单因果目标数量超过训练集单因果样本数")
    if hard_negative_count > len(negative_candidates):
        raise ValueError("困难负样本目标数量超过训练集负样本数")

    hard_single_ranked = _rank_candidates(single_candidates, _score_hard_single_positive)
    hard_negative_ranked = _rank_candidates(negative_candidates, _score_hard_negative)
    hard_single = hard_single_ranked[:hard_single_count]
    hard_negative = hard_negative_ranked[:hard_negative_count]

    derived_rows: list[dict[str, Any]] = []
    for row in train_rows:
        derived_rows.append(_training_instance(row, kind="base"))
    for row in multi_rows:
        derived_rows.append(
            _training_instance(
                row,
                kind="multi_causal_oversample",
                score=len(row["relations"]),
                reasons=[f"gold_relations={len(row['relations'])}"],
            )
        )
    for score, source_id, reasons, row in hard_single:
        derived_rows.append(
            _training_instance(
                row,
                kind="hard_single_positive_oversample",
                score=score,
                reasons=reasons,
            )
        )
    for score, source_id, reasons, row in hard_negative:
        derived_rows.append(
            _training_instance(
                row,
                kind="hard_negative_oversample",
                score=score,
                reasons=reasons,
            )
        )

    random.Random(seed).shuffle(derived_rows)
    _ensure_output_is_safe(output_dir, overwrite=overwrite)
    output_dir.mkdir(parents=True, exist_ok=True)
    _write_jsonl(output_dir / "train.jsonl", derived_rows)
    shutil.copyfile(source_validation, output_dir / "validation.jsonl")
    shutil.copyfile(source_test, output_dir / "test.jsonl")
    _write_json(output_dir / "dataset_info.json", _dataset_info())

    selection = {
        "multi_causal_oversample": [
            {
                "source_id": row["id"],
                "gold_relations": len(row["relations"]),
            }
            for row in multi_rows
        ],
        "hard_single_positive_oversample": [
            {"source_id": source_id, "score": score, "reasons": reasons}
            for score, source_id, reasons, _row in hard_single
        ],
        "hard_negative_oversample": [
            {"source_id": source_id, "score": score, "reasons": reasons}
            for score, source_id, reasons, _row in hard_negative
        ],
    }
    audit = _build_audit(
        train_rows=train_rows,
        validation_rows=validation_rows,
        test_rows=test_rows,
        derived_rows=derived_rows,
        selection=selection,
        source_dir=source_dir,
        output_dir=output_dir,
        seed=seed,
        hard_single_count=hard_single_count,
        hard_negative_count=hard_negative_count,
    )
    if not all(audit["checks"].values()):
        failed = [name for name, passed in audit["checks"].items() if not passed]
        raise RuntimeError(f"CNC 困难样本数据审计失败：{', '.join(failed)}")
    _write_json(output_dir / "selection_manifest.json", selection)
    _write_json(output_dir / "audit.json", audit)
    return audit


def _score_hard_single_positive(row: dict[str, Any]) -> tuple[int, list[str]]:
    text = row["text"]
    score = 0
    reasons: list[str] = []
    strong = _matched_patterns(text, STRONG_CAUSAL_PATTERNS)
    reaction = _matched_patterns(text, REACTION_PURPOSE_PATTERNS)
    temporal = _matched_patterns(text, TEMPORAL_AMBIGUITY_PATTERNS)
    weak = _matched_patterns(text, WEAK_ARGUMENT_PATTERNS)
    score += 4 * len(strong)
    score += 3 * len(reaction)
    score += 2 * len(temporal)
    score += len(weak)
    reasons.extend(f"strong:{name}" for name in strong)
    reasons.extend(f"reaction_or_purpose:{name}" for name in reaction)
    reasons.extend(f"temporal_ambiguity:{name}" for name in temporal)
    reasons.extend(f"weak_argument_marker:{name}" for name in weak)

    relation = row["relations"][0]
    leading_roles = [role for role in ("cause", "effect") if LEADING_FUNCTION_WORDS.search(relation[role])]
    if leading_roles:
        score += 3 * len(leading_roles)
        reasons.extend(f"leading_function_word:{role}" for role in leading_roles)
    word_count = len(text.split())
    if word_count >= 40:
        score += 2
        reasons.append("long_context")
    if word_count <= 20:
        score += 1
        reasons.append("compact_or_headline_like")
    if not text.rstrip().endswith((".", "?", "!", '"', "'")):
        score += 2
        reasons.append("fragment_or_headline_ending")
    if "��" in text or re.search(r"\w\s+'\s*s\b", text, flags=re.IGNORECASE):
        score += 2
        reasons.append("tokenization_or_apostrophe_noise")
    if min(len(relation["cause"].split()), len(relation["effect"].split())) <= 4:
        score += 1
        reasons.append("short_causal_argument")
    return score, reasons or ["single_positive_fallback"]


def _score_hard_negative(row: dict[str, Any]) -> tuple[int, list[str]]:
    text = row["text"]
    score = 0
    reasons: list[str] = []
    strong = _matched_patterns(text, STRONG_CAUSAL_PATTERNS)
    reaction = _matched_patterns(text, REACTION_PURPOSE_PATTERNS)
    temporal = _matched_patterns(text, TEMPORAL_AMBIGUITY_PATTERNS)
    weak = _matched_patterns(text, WEAK_ARGUMENT_PATTERNS)
    score += 5 * len(strong)
    score += 3 * len(reaction)
    score += 3 * len(temporal)
    score += len(weak)
    reasons.extend(f"strong_causal_surface_form:{name}" for name in strong)
    reasons.extend(f"reaction_or_purpose_surface_form:{name}" for name in reaction)
    reasons.extend(f"temporal_surface_form:{name}" for name in temporal)
    reasons.extend(f"weak_surface_form:{name}" for name in weak)
    word_count = len(text.split())
    if word_count >= 40:
        score += 2
        reasons.append("long_distractor_context")
    if word_count <= 20:
        score += 1
        reasons.append("compact_negative")
    if not text.rstrip().endswith((".", "?", "!", '"', "'")):
        score += 1
        reasons.append("fragment_or_headline_ending")
    if "��" in text or re.search(r"\w\s+'\s*s\b", text, flags=re.IGNORECASE):
        score += 1
        reasons.append("tokenization_or_apostrophe_noise")
    return score, reasons or ["negative_fallback"]


def _matched_patterns(text: str, patterns: dict[str, str]) -> list[str]:
    return [name for name, pattern in patterns.items() if re.search(pattern, text, flags=re.IGNORECASE)]


def _rank_candidates(
    rows: list[dict[str, Any]],
    scorer: Any,
) -> list[tuple[int, Any, list[str], dict[str, Any]]]:
    ranked = []
    for row in rows:
        score, reasons = scorer(row)
        ranked.append((score, row["id"], reasons, row))
    ranked.sort(key=lambda item: (-item[0], _stable_id(item[1])))
    return ranked


def _stable_id(value: Any) -> tuple[int, Any]:
    if isinstance(value, int):
        return 0, value
    return 1, str(value)


def _training_instance(
    row: dict[str, Any],
    kind: str,
    score: int | None = None,
    reasons: list[str] | None = None,
) -> dict[str, Any]:
    copied = dict(row)
    copied["sampling"] = {
        "source_id": row["id"],
        "kind": kind,
        "score": score,
        "reasons": reasons or [],
    }
    return copied


def _validate_source_splits(
    train_rows: list[dict[str, Any]],
    validation_rows: list[dict[str, Any]],
    test_rows: list[dict[str, Any]],
) -> None:
    all_splits = {
        "train": train_rows,
        "validation": validation_rows,
        "test": test_rows,
    }
    for split, rows in all_splits.items():
        if not rows:
            raise ValueError(f"{split} 数据为空")
        for row in rows:
            if bool(row.get("relations")) != bool(row.get("has_causal")):
                raise ValueError(f"{split} id={row.get('id')} 标签不一致")
            if not isinstance(row.get("messages"), list) or len(row["messages"]) != 3:
                raise ValueError(f"{split} id={row.get('id')} messages 格式无效")
    id_sets = {split: {row["id"] for row in rows} for split, rows in all_splits.items()}
    doc_sets = {split: {row["doc_id"] for row in rows} for split, rows in all_splits.items()}
    for left, right in (("train", "validation"), ("train", "test"), ("validation", "test")):
        if id_sets[left] & id_sets[right]:
            raise ValueError(f"{left} 与 {right} 存在 id 泄漏")
        if doc_sets[left] & doc_sets[right]:
            raise ValueError(f"{left} 与 {right} 存在文档泄漏")


def _build_audit(
    train_rows: list[dict[str, Any]],
    validation_rows: list[dict[str, Any]],
    test_rows: list[dict[str, Any]],
    derived_rows: list[dict[str, Any]],
    selection: dict[str, list[dict[str, Any]]],
    source_dir: Path,
    output_dir: Path,
    seed: int,
    hard_single_count: int,
    hard_negative_count: int,
) -> dict[str, Any]:
    source_counts = Counter(row["id"] for row in train_rows)
    derived_counts = Counter(row["id"] for row in derived_rows)
    selected_ids = {
        kind: {item["source_id"] for item in items}
        for kind, items in selection.items()
    }
    expected_duplicated = set().union(*selected_ids.values())
    actual_duplicated = {source_id for source_id, count in derived_counts.items() if count == 2}
    all_source_ids = set(source_counts)
    all_eval_ids = {row["id"] for row in validation_rows + test_rows}
    kind_counts = Counter(row["sampling"]["kind"] for row in derived_rows)
    output_validation = output_dir / "validation.jsonl"
    output_test = output_dir / "test.jsonl"
    checks = {
        "source_train_ids_unique": all(count == 1 for count in source_counts.values()),
        "base_train_covered": set(derived_counts) == all_source_ids,
        "only_selected_rows_duplicated": actual_duplicated == expected_duplicated,
        "each_selected_row_occurs_twice": all(derived_counts[source_id] == 2 for source_id in expected_duplicated),
        "each_unselected_row_occurs_once": all(
            derived_counts[source_id] == 1 for source_id in all_source_ids - expected_duplicated
        ),
        "selection_categories_disjoint": sum(len(ids) for ids in selected_ids.values())
        == len(expected_duplicated),
        "multi_selection_complete": len(selected_ids["multi_causal_oversample"])
        == sum(len(row["relations"]) >= 2 for row in train_rows),
        "hard_single_target_met": len(selected_ids["hard_single_positive_oversample"])
        == hard_single_count,
        "hard_negative_target_met": len(selected_ids["hard_negative_oversample"])
        == hard_negative_count,
        "no_validation_or_test_ids_used": not (set(derived_counts) & all_eval_ids),
        "validation_byte_identical": _sha256(source_dir / "validation.jsonl")
        == _sha256(output_validation),
        "test_byte_identical": _sha256(source_dir / "test.jsonl") == _sha256(output_test),
        "messages_preserved": all(_messages_match_source(row, train_rows) for row in derived_rows),
    }
    return {
        "strategy": (
            "retain every original training row once; add one extra occurrence for every multi-causal row, "
            "the highest-scoring hard single-positive rows, and the highest-scoring causal-looking negative rows"
        ),
        "strategy_version": 1,
        "seed": seed,
        "source_dir": _portable_path(source_dir),
        "output_dir": _portable_path(output_dir),
        "source_hashes": {
            name: _sha256(source_dir / name)
            for name in ("train.jsonl", "validation.jsonl", "test.jsonl")
        },
        "output_hashes": {
            name: _sha256(output_dir / name)
            for name in ("train.jsonl", "validation.jsonl", "test.jsonl")
        },
        "selection_targets": {
            "multi_causal": len(selected_ids["multi_causal_oversample"]),
            "hard_single_positive": hard_single_count,
            "hard_negative": hard_negative_count,
        },
        "sampling_kind_counts": dict(sorted(kind_counts.items())),
        "unique_source_distribution": _distribution(train_rows),
        "effective_distribution": _distribution(derived_rows),
        "validation_distribution": _distribution(validation_rows),
        "test_distribution": _distribution(test_rows),
        "checks": checks,
        "notes": [
            "No validation or test row is included in the derived training data.",
            "Gold labels, spans, messages, and the training prompt are unchanged.",
            "Oversampling is implemented as deterministic duplicate training occurrences, not synthetic data.",
        ],
    }


def _messages_match_source(row: dict[str, Any], source_rows: list[dict[str, Any]]) -> bool:
    source_by_id = {source["id"]: source for source in source_rows}
    source = source_by_id.get(row["id"])
    return bool(
        source
        and row.get("messages") == source.get("messages")
        and row.get("relations") == source.get("relations")
        and row.get("text") == source.get("text")
    )


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
        f"cnc_sft_hard_{split}": {
            "file_name": f"{split}.jsonl",
            "formatting": "sharegpt",
            "columns": {"messages": "messages"},
            "tags": tags,
        }
        for split in ("train", "validation", "test")
    }


def _ensure_output_is_safe(output_dir: Path, overwrite: bool) -> None:
    if not output_dir.exists():
        return
    existing = list(output_dir.iterdir())
    if existing and not overwrite:
        raise FileExistsError(f"输出目录已有文件，请使用 --overwrite：{output_dir}")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


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
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.resolve().as_posix()


if __name__ == "__main__":
    main()
