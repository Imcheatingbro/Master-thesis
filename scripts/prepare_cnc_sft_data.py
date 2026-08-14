"""为 CNC 微调准备文档隔离、分层且可审计的数据划分。"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import math
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_PATH = PROJECT_ROOT / "Data" / "Dataset_1_CNC_modified.jsonl"
DEFAULT_RAW_PATH = PROJECT_ROOT / "Data" / "raw" / "Dataset_1_CNC_raw.csv"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "Data" / "CNC_sft"
DEFAULT_TRAIN_SIZE = 1537
DEFAULT_VALIDATION_SIZE = 500
DEFAULT_SEED = 42
SPLIT_NAMES = ("train", "validation", "test")
OUTPUT_FILES = (
    "train.jsonl",
    "validation.jsonl",
    "test.jsonl",
    "dataset_info.json",
    "split_manifest.json",
    "audit.json",
)
SYSTEM_PROMPT = (
    "You are a causal relation extraction system for the CNC dataset. "
    "Given one input sentence, identify all causal relations. Copy every cause and effect "
    "as an exact continuous span from the input. Return strict JSON only with keys "
    "has_causal and triples. Each triple must contain cause.span, relation=caused, and "
    "effect.span. If no causal relation is present, return "
    '{"has_causal":false,"triples":[]}.'
)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description="准备 CNC 的 LLaMA-Factory SFT 数据")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE_PATH)
    parser.add_argument("--raw-data", type=Path, default=DEFAULT_RAW_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--train-size", type=int, default=DEFAULT_TRAIN_SIZE)
    parser.add_argument("--validation-size", type=int, default=DEFAULT_VALIDATION_SIZE)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    """生成数据划分及审计文件。"""
    args = parse_args()
    manifest, audit = prepare_cnc_sft_data(
        source_path=args.source,
        raw_path=args.raw_data,
        output_dir=args.output_dir,
        train_size=args.train_size,
        validation_size=args.validation_size,
        seed=args.seed,
        overwrite=args.overwrite,
    )
    LOGGER.info("CNC SFT 数据已生成：%s", args.output_dir)
    LOGGER.info("划分数量：%s", manifest["actual_sizes"])
    LOGGER.info("审计检查全部通过：%s", all(audit["checks"].values()))


def prepare_cnc_sft_data(
    source_path: Path,
    raw_path: Path,
    output_dir: Path,
    train_size: int = DEFAULT_TRAIN_SIZE,
    validation_size: int = DEFAULT_VALIDATION_SIZE,
    seed: int = DEFAULT_SEED,
    overwrite: bool = False,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """读取 CNC，生成三份文档隔离数据以及 manifest、audit。"""
    samples = _read_jsonl(source_path)
    raw_rows = _read_csv(raw_path)
    enriched = _enrich_and_validate(samples, raw_rows)
    split_sizes = _split_sizes(len(enriched), train_size, validation_size)
    split_indices, target_strata = _assign_document_disjoint_splits(
        enriched,
        split_sizes=split_sizes,
        seed=seed,
    )
    output_rows = {
        split: [_sft_record(enriched[index]) for index in indices]
        for split, indices in split_indices.items()
    }
    audit = _build_audit(enriched, split_indices, split_sizes, target_strata)
    if not all(audit["checks"].values()):
        failed = [name for name, passed in audit["checks"].items() if not passed]
        raise RuntimeError(f"CNC SFT 数据审计失败：{', '.join(failed)}")

    _ensure_output_is_safe(output_dir, overwrite=overwrite)
    output_dir.mkdir(parents=True, exist_ok=True)
    for split in SPLIT_NAMES:
        _write_jsonl(output_dir / f"{split}.jsonl", output_rows[split])
    _write_json(output_dir / "dataset_info.json", _dataset_info())

    data_hashes = {
        f"{split}.jsonl": _sha256(output_dir / f"{split}.jsonl")
        for split in SPLIT_NAMES
    }
    manifest = _build_manifest(
        source_path=source_path,
        raw_path=raw_path,
        enriched=enriched,
        split_indices=split_indices,
        split_sizes=split_sizes,
        target_strata=target_strata,
        seed=seed,
        data_hashes=data_hashes,
    )
    _write_json(output_dir / "split_manifest.json", manifest)
    _write_json(output_dir / "audit.json", audit)
    return manifest, audit


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def _enrich_and_validate(
    samples: list[dict[str, Any]],
    raw_rows: list[dict[str, str]],
) -> list[dict[str, Any]]:
    raw_by_text: dict[str, dict[str, str]] = {}
    for raw in raw_rows:
        text = raw.get("text", "")
        if not text:
            raise ValueError("原始 CNC 中存在空文本")
        if text in raw_by_text:
            raise ValueError(f"原始 CNC 文本不唯一：{text[:100]}")
        raw_by_text[text] = raw

    seen_ids: set[Any] = set()
    seen_texts: set[str] = set()
    enriched: list[dict[str, Any]] = []
    for source_index, sample in enumerate(samples):
        sample_id = sample.get("id")
        text = sample.get("text")
        relations = sample.get("relations")
        has_causal = sample.get("has_causal")
        if sample_id in seen_ids:
            raise ValueError(f"CNC id 不唯一：{sample_id}")
        if not isinstance(text, str) or not text:
            raise ValueError(f"CNC id={sample_id} 的 text 无效")
        if text in seen_texts:
            raise ValueError(f"CNC text 不唯一：id={sample_id}")
        if not isinstance(has_causal, bool) or not isinstance(relations, list):
            raise ValueError(f"CNC id={sample_id} 的标签字段类型无效")
        if has_causal != bool(relations):
            raise ValueError(f"CNC id={sample_id} 的 has_causal 与 relations 不一致")
        for relation in relations:
            if not isinstance(relation, dict):
                raise ValueError(f"CNC id={sample_id} 的 relation 不是对象")
            cause = relation.get("cause")
            effect = relation.get("effect")
            if not isinstance(cause, str) or not cause or cause not in text:
                raise ValueError(f"CNC id={sample_id} 的 cause 不是原文连续 span：{cause}")
            if not isinstance(effect, str) or not effect or effect not in text:
                raise ValueError(f"CNC id={sample_id} 的 effect 不是原文连续 span：{effect}")

        raw = raw_by_text.get(text)
        if raw is None:
            raise ValueError(f"CNC id={sample_id} 无法映射回原始 CSV")
        doc_id = raw.get("doc_id", "")
        if not doc_id:
            raise ValueError(f"CNC id={sample_id} 缺少 doc_id")
        seen_ids.add(sample_id)
        seen_texts.add(text)
        enriched.append(
            {
                "sample": sample,
                "source_index": source_index,
                "sample_id": sample_id,
                "text": text,
                "doc_id": doc_id,
                "raw_index": raw.get("index", ""),
                "relations": relations,
                "has_causal": has_causal,
                "word_count": len(text.split()),
                "stratum": _stratum(text, relations),
            }
        )
    return enriched


def _split_sizes(total: int, train_size: int, validation_size: int) -> dict[str, int]:
    if train_size <= 0 or validation_size <= 0:
        raise ValueError("train-size 和 validation-size 必须大于 0")
    test_size = total - train_size - validation_size
    if test_size <= 0:
        raise ValueError("train-size 与 validation-size 必须为测试集保留样本")
    return {"train": train_size, "validation": validation_size, "test": test_size}


def _stratum(text: str, relations: list[dict[str, Any]]) -> tuple[str, str]:
    relation_count = len(relations)
    relation_bucket = (
        "0"
        if relation_count == 0
        else "1"
        if relation_count == 1
        else "2"
        if relation_count == 2
        else "3+"
    )
    word_count = len(text.split())
    length_bucket = "short" if word_count <= 20 else "medium" if word_count <= 40 else "long"
    return relation_bucket, length_bucket


def _assign_document_disjoint_splits(
    enriched: list[dict[str, Any]],
    split_sizes: dict[str, int],
    seed: int,
) -> tuple[dict[str, list[int]], dict[str, dict[tuple[str, str], int]]]:
    global_strata = Counter(item["stratum"] for item in enriched)
    train_targets = _largest_remainder(global_strata, len(enriched), split_sizes["train"])
    remaining = {key: global_strata[key] - train_targets[key] for key in global_strata}
    validation_targets = _largest_remainder(
        remaining,
        sum(remaining.values()),
        split_sizes["validation"],
    )
    test_targets = {
        key: global_strata[key] - train_targets[key] - validation_targets[key]
        for key in global_strata
    }
    target_strata = {
        "train": train_targets,
        "validation": validation_targets,
        "test": test_targets,
    }

    by_document: dict[str, list[int]] = defaultdict(list)
    for index, item in enumerate(enriched):
        by_document[item["doc_id"]].append(index)
    group_size_targets = _group_size_targets(by_document, split_sizes, len(enriched))
    split_indices = _allocate_documents(
        enriched,
        by_document=by_document,
        target_strata=target_strata,
        group_size_targets=group_size_targets,
        seed=seed,
    )
    return split_indices, target_strata


def _largest_remainder(
    counts: dict[tuple[str, str], int],
    total: int,
    target_size: int,
) -> dict[tuple[str, str], int]:
    raw = {key: count * target_size / total for key, count in counts.items()}
    quotas = {key: math.floor(value) for key, value in raw.items()}
    remaining = target_size - sum(quotas.values())
    ranked = sorted(counts, key=lambda key: (-(raw[key] - quotas[key]), str(key)))
    for key in ranked[:remaining]:
        quotas[key] += 1
    return quotas


def _group_size_targets(
    by_document: dict[str, list[int]],
    split_sizes: dict[str, int],
    total_samples: int,
) -> dict[str, dict[int, int]]:
    group_counts = Counter(len(indices) for indices in by_document.values())
    targets = {split: {} for split in SPLIT_NAMES}
    for group_size, count in group_counts.items():
        raw = {
            split: count * split_sizes[split] / total_samples
            for split in SPLIT_NAMES
        }
        quotas = {split: math.floor(raw[split]) for split in SPLIT_NAMES}
        remaining = count - sum(quotas.values())
        ranked = sorted(
            SPLIT_NAMES,
            key=lambda split: (-(raw[split] - quotas[split]), split),
        )
        for split in ranked[:remaining]:
            quotas[split] += 1
        for split in SPLIT_NAMES:
            targets[split][group_size] = quotas[split]
    return targets


def _allocate_documents(
    enriched: list[dict[str, Any]],
    by_document: dict[str, list[int]],
    target_strata: dict[str, dict[tuple[str, str], int]],
    group_size_targets: dict[str, dict[int, int]],
    seed: int,
) -> dict[str, list[int]]:
    rng = random.Random(seed)
    global_strata = Counter(item["stratum"] for item in enriched)
    singleton_docs: dict[tuple[str, str], list[tuple[str, int]]] = defaultdict(list)
    multi_docs: list[tuple[str, list[int], Counter[tuple[str, str]]]] = []
    for doc_id, indices in sorted(by_document.items()):
        if len(indices) == 1:
            singleton_docs[enriched[indices[0]]["stratum"]].append((doc_id, indices[0]))
        else:
            vector = Counter(enriched[index]["stratum"] for index in indices)
            multi_docs.append((doc_id, indices, vector))

    rng.shuffle(multi_docs)
    multi_docs.sort(
        key=lambda group: (
            -sum(group[2][key] / global_strata[key] for key in group[2]),
            -len(group[1]),
        )
    )
    assigned_strata = {split: Counter() for split in SPLIT_NAMES}
    assigned_group_sizes = {split: Counter() for split in SPLIT_NAMES}
    result = {split: [] for split in SPLIT_NAMES}

    for doc_id, indices, vector in multi_docs:
        split_rank = list(SPLIT_NAMES)
        rng.shuffle(split_rank)
        tie_order = {split: rank for rank, split in enumerate(split_rank)}
        choices: list[tuple[float, int, str]] = []
        for split in SPLIT_NAMES:
            group_size = len(indices)
            if assigned_group_sizes[split][group_size] >= group_size_targets[split][group_size]:
                continue
            if any(
                assigned_strata[split][key] + count > target_strata[split][key]
                for key, count in vector.items()
            ):
                continue
            score = sum(
                (
                    (target_strata[split][key] - assigned_strata[split][key] - vector[key])
                    / max(target_strata[split][key], 1)
                )
                ** 2
                for key in global_strata
            )
            choices.append((score, tie_order[split], split))
        if not choices:
            raise RuntimeError(f"无法在不破坏分层配额的情况下分配文档：{doc_id}")
        split = min(choices)[2]
        result[split].extend(indices)
        assigned_strata[split].update(vector)
        assigned_group_sizes[split][len(indices)] += 1

    for stratum in sorted(singleton_docs, key=str):
        documents = singleton_docs[stratum]
        rng.shuffle(documents)
        position = 0
        for split in SPLIT_NAMES:
            needed = target_strata[split][stratum] - assigned_strata[split][stratum]
            if needed < 0:
                raise RuntimeError(f"分层配额出现负缺口：{split} {stratum}")
            selected = documents[position : position + needed]
            result[split].extend(index for _doc_id, index in selected)
            assigned_strata[split][stratum] += len(selected)
            position += needed
        if position != len(documents):
            raise RuntimeError(f"单句文档未完全分配：{stratum}")

    for split in SPLIT_NAMES:
        rng.shuffle(result[split])
        if Counter(enriched[index]["stratum"] for index in result[split]) != Counter(
            target_strata[split]
        ):
            raise RuntimeError(f"{split} 的实际分层与目标不一致")
    return result


def _sft_record(item: dict[str, Any]) -> dict[str, Any]:
    sample = item["sample"]
    assistant = {
        "has_causal": item["has_causal"],
        "triples": [
            {
                "cause": {"span": relation["cause"]},
                "relation": "caused",
                "effect": {"span": relation["effect"]},
            }
            for relation in item["relations"]
        ],
    }
    return {
        "id": item["sample_id"],
        "doc_id": item["doc_id"],
        "raw_index": item["raw_index"],
        "text": item["text"],
        "has_causal": item["has_causal"],
        "relations": sample["relations"],
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Input text:\n{item['text']}"},
            {
                "role": "assistant",
                "content": json.dumps(assistant, ensure_ascii=False, separators=(",", ":")),
            },
        ],
    }


def _build_audit(
    enriched: list[dict[str, Any]],
    split_indices: dict[str, list[int]],
    split_sizes: dict[str, int],
    target_strata: dict[str, dict[tuple[str, str], int]],
) -> dict[str, Any]:
    id_sets = {
        split: {enriched[index]["sample_id"] for index in indices}
        for split, indices in split_indices.items()
    }
    text_sets = {
        split: {enriched[index]["text"] for index in indices}
        for split, indices in split_indices.items()
    }
    doc_sets = {
        split: {enriched[index]["doc_id"] for index in indices}
        for split, indices in split_indices.items()
    }
    all_indices = [index for indices in split_indices.values() for index in indices]
    source_ids = [item["sample_id"] for item in enriched]
    source_texts = [item["text"] for item in enriched]
    checks = {
        "exact_target_sizes": all(len(split_indices[split]) == split_sizes[split] for split in SPLIT_NAMES),
        "all_samples_assigned_once": len(all_indices) == len(enriched) and len(set(all_indices)) == len(enriched),
        "source_ids_unique": len(source_ids) == len(set(source_ids)),
        "source_texts_unique": len(source_texts) == len(set(source_texts)),
        "id_overlap_zero": _pairwise_overlap(id_sets) == 0,
        "text_overlap_zero": _pairwise_overlap(text_sets) == 0,
        "document_overlap_zero": _pairwise_overlap(doc_sets) == 0,
        "strata_match_targets": all(
            Counter(enriched[index]["stratum"] for index in split_indices[split])
            == Counter(target_strata[split])
            for split in SPLIT_NAMES
        ),
        "labels_consistent": all(item["has_causal"] == bool(item["relations"]) for item in enriched),
        "all_spans_are_exact_substrings": all(
            relation[role] in item["text"]
            for item in enriched
            for relation in item["relations"]
            for role in ("cause", "effect")
        ),
    }
    return {
        "source": _distribution(enriched, list(range(len(enriched)))),
        "splits": {
            split: _distribution(enriched, split_indices[split])
            for split in SPLIT_NAMES
        },
        "pairwise_overlap": {
            "ids": _overlap_details(id_sets),
            "texts": _overlap_details(text_sets),
            "documents": _overlap_details(doc_sets),
        },
        "checks": checks,
    }


def _distribution(enriched: list[dict[str, Any]], indices: list[int]) -> dict[str, Any]:
    selected = [enriched[index] for index in indices]
    relation_counts = Counter(len(item["relations"]) for item in selected)
    strata = Counter("|".join(item["stratum"]) for item in selected)
    return {
        "samples": len(selected),
        "documents": len({item["doc_id"] for item in selected}),
        "positive": sum(item["has_causal"] for item in selected),
        "negative": sum(not item["has_causal"] for item in selected),
        "relations": sum(len(item["relations"]) for item in selected),
        "relation_count": {str(key): value for key, value in sorted(relation_counts.items())},
        "length_bucket": dict(sorted(Counter(item["stratum"][1] for item in selected).items())),
        "strata": dict(sorted(strata.items())),
    }


def _pairwise_overlap(values: dict[str, set[Any]]) -> int:
    return sum(
        len(values[left] & values[right])
        for left_index, left in enumerate(SPLIT_NAMES)
        for right in SPLIT_NAMES[left_index + 1 :]
    )


def _overlap_details(values: dict[str, set[Any]]) -> dict[str, int]:
    return {
        f"{left}__{right}": len(values[left] & values[right])
        for left_index, left in enumerate(SPLIT_NAMES)
        for right in SPLIT_NAMES[left_index + 1 :]
    }


def _build_manifest(
    source_path: Path,
    raw_path: Path,
    enriched: list[dict[str, Any]],
    split_indices: dict[str, list[int]],
    split_sizes: dict[str, int],
    target_strata: dict[str, dict[tuple[str, str], int]],
    seed: int,
    data_hashes: dict[str, str],
) -> dict[str, Any]:
    return {
        "strategy": "document-disjoint stratification by relation-count and text-length buckets",
        "strategy_version": 1,
        "seed": seed,
        "source": {
            "path": _portable_path(source_path),
            "sha256": _sha256(source_path),
            "raw_path": _portable_path(raw_path),
            "raw_sha256": _sha256(raw_path),
            "samples": len(enriched),
        },
        "target_sizes": split_sizes,
        "actual_sizes": {split: len(split_indices[split]) for split in SPLIT_NAMES},
        "target_strata": {
            split: {
                "|".join(key): value
                for key, value in sorted(target_strata[split].items(), key=lambda item: str(item[0]))
            }
            for split in SPLIT_NAMES
        },
        "data_sha256": data_hashes,
        "split_ids": {
            split: [enriched[index]["sample_id"] for index in split_indices[split]]
            for split in SPLIT_NAMES
        },
        "split_doc_ids": {
            split: sorted({enriched[index]["doc_id"] for index in split_indices[split]})
            for split in SPLIT_NAMES
        },
        "evaluation_note": (
            "该测试集从此版本起与微调严格隔离；部分 CNC 样本此前可能用于 prompt/RAG 阶段实验，"
            "因此它适合相同测试集上的 base-vs-finetuned 对比，但不宣称是从未用于开发的隐藏测试集。"
        ),
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
        f"cnc_sft_{split}": {
            "file_name": f"{split}.jsonl",
            "formatting": "sharegpt",
            "columns": {"messages": "messages"},
            "tags": tags,
        }
        for split in SPLIT_NAMES
    }


def _ensure_output_is_safe(output_dir: Path, overwrite: bool) -> None:
    existing = [output_dir / name for name in OUTPUT_FILES if (output_dir / name).exists()]
    if existing and not overwrite:
        names = ", ".join(path.name for path in existing)
        raise FileExistsError(f"输出已存在（使用 --overwrite 才可覆盖）：{names}")


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
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    main()
