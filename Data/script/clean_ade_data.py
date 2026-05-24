"""将 ADE Hugging Face 原始快照合并为项目统一 JSONL 格式。"""

from __future__ import annotations

import json
import logging
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "Data"
CLASSIFICATION_DIR_NAME = "Ade_corpus_v2_classification"
RELATION_DIR_NAME = "Ade_corpus_v2_drug_ade_relation"
ADE_OUTPUT_NAME = "Dataset_3_ADE_modified.jsonl"
STATS_NAME = "stats.json"
BGE_EXAMPLES_PATH = PROJECT_ROOT / "RAG Database" / "bge-small-en-v1.5_examples.jsonl"
TAG_PATTERN = re.compile(r"</?(?:cause|effect)>", flags=re.IGNORECASE)
Sample = dict[str, Any]


def normalize_sentence(text: str) -> str:
    """去掉 BGE example 标注标签并规范化空白，用于句子级去重。"""
    cleaned = TAG_PATTERN.sub("", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = _strip_outer_quotes(cleaned)
    return cleaned.casefold()


def load_bge_example_texts(path: Path | str) -> set[str]:
    """读取 BGE metadata 中的 sentence 字段，返回规范化后的句子集合。"""
    texts: set[str] = set()
    with Path(path).open("r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            row = json.loads(line)
            sentence = str(row.get("sentence", "")).strip()
            if sentence:
                texts.add(normalize_sentence(sentence))
    return texts


def build_ade_samples(
    classification_rows: Iterable[dict[str, Any]],
    relation_rows: Iterable[dict[str, Any]],
    excluded_texts: set[str],
) -> tuple[list[Sample], dict[str, Any]]:
    """合并 ADE classification 与 relation 数据，并剔除 BGE 已出现句子。"""
    relation_map, relation_stats = _build_relation_map(relation_rows)
    classification_map: dict[str, dict[str, Any]] = {}
    samples: list[Sample] = []
    input_classification_rows = 0
    bge_excluded_samples = 0
    positive_without_relation = 0

    for row in classification_rows:
        input_classification_rows += 1
        text = str(row.get("text", ""))
        text_key = normalize_sentence(text)
        has_causal = _is_related_label(row.get("label"))
        if text_key not in classification_map:
            classification_map[text_key] = {"text": text, "has_causal": has_causal}
        else:
            classification_map[text_key]["has_causal"] = bool(classification_map[text_key]["has_causal"] or has_causal)

    for text_key, row in classification_map.items():
        if text_key in excluded_texts:
            bge_excluded_samples += 1
            continue

        text = str(row["text"])
        has_causal = bool(row["has_causal"])
        relations = relation_map.get(text_key, []) if has_causal else []
        if has_causal and not relations:
            positive_without_relation += 1

        samples.append(
            {
                "id": len(samples) + 1,
                "text": text,
                "has_causal": has_causal,
                "relations": relations,
            }
        )

    stats = _build_stats(
        samples=samples,
        input_classification_rows=input_classification_rows,
        unique_classification_texts=len(classification_map),
        input_relation_rows=relation_stats["input_relation_rows"],
        bge_excluded_samples=bge_excluded_samples,
        bge_example_sentences=len(excluded_texts),
        warnings={
            "substring_check_failed_relations": relation_stats["substring_check_failed_relations"],
            "positive_without_relation": positive_without_relation,
        },
    )
    return samples, stats


def write_jsonl(path: Path, samples: list[Sample]) -> None:
    """以 UTF-8 与 LF 换行写出 JSONL。"""
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for sample in samples:
            file.write(json.dumps(sample, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_stats(path: Path, stats: dict[str, Any]) -> None:
    """写出统一 stats.json。"""
    with path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(stats, file, ensure_ascii=False, indent=2)
        file.write("\n")


def run_cleaning(
    data_dir: Path | str = DATA_DIR,
    bge_examples_path: Path | str = BGE_EXAMPLES_PATH,
) -> dict[str, Any]:
    """读取 ADE 原始快照，生成 Dataset_3_ADE_modified.jsonl 并更新 stats.json。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    target_dir = Path(data_dir)
    LOGGER.info("开始清洗 ADE 数据目录：%s", target_dir)

    classification_rows = _load_hf_train_split(target_dir / CLASSIFICATION_DIR_NAME)
    relation_rows = _load_hf_train_split(target_dir / RELATION_DIR_NAME)
    excluded_texts = load_bge_example_texts(bge_examples_path)
    samples, ade_stats = build_ade_samples(classification_rows, relation_rows, excluded_texts)

    write_jsonl(target_dir / ADE_OUTPUT_NAME, samples)
    stats_path = target_dir / STATS_NAME
    all_stats = json.loads(stats_path.read_text(encoding="utf-8")) if stats_path.exists() else {}
    all_stats["ade"] = ade_stats
    write_stats(stats_path, all_stats)

    LOGGER.info("ADE 数据清洗完成：samples=%s relations=%s", ade_stats["output_samples"], ade_stats["total_relations"])
    return ade_stats


def main() -> None:
    """命令行入口。"""
    run_cleaning()


def _build_relation_map(relation_rows: Iterable[dict[str, Any]]) -> tuple[dict[str, list[dict[str, str]]], dict[str, int]]:
    relation_map: dict[str, list[dict[str, str]]] = {}
    seen_relations: dict[str, set[tuple[str, str]]] = {}
    input_relation_rows = 0
    substring_check_failed_relations = 0

    for row in relation_rows:
        input_relation_rows += 1
        text = str(row.get("text", ""))
        cause = str(row.get("drug", "")).strip()
        effect = str(row.get("effect", "")).strip()
        if not cause or not effect or cause not in text or effect not in text:
            substring_check_failed_relations += 1
            continue

        text_key = normalize_sentence(text)
        relation_key = (cause, effect)
        seen_relations.setdefault(text_key, set())
        if relation_key in seen_relations[text_key]:
            continue
        seen_relations[text_key].add(relation_key)
        relation_map.setdefault(text_key, []).append({"cause": cause, "effect": effect})

    return relation_map, {
        "input_relation_rows": input_relation_rows,
        "substring_check_failed_relations": substring_check_failed_relations,
    }


def _build_stats(
    samples: list[Sample],
    input_classification_rows: int,
    unique_classification_texts: int,
    input_relation_rows: int,
    bge_excluded_samples: int,
    bge_example_sentences: int,
    warnings: dict[str, int],
) -> dict[str, Any]:
    distribution = Counter(str(len(sample["relations"])) for sample in samples)
    causal_samples = sum(1 for sample in samples if sample["has_causal"])
    return {
        "input_classification_rows": input_classification_rows,
        "unique_classification_texts": unique_classification_texts,
        "input_relation_rows": input_relation_rows,
        "bge_example_sentences": bge_example_sentences,
        "bge_excluded_samples": bge_excluded_samples,
        "output_samples": len(samples),
        "causal_samples": causal_samples,
        "non_causal_samples": len(samples) - causal_samples,
        "total_relations": sum(len(sample["relations"]) for sample in samples),
        "relation_count_distribution": dict(sorted(distribution.items(), key=lambda item: int(item[0]))),
        "warnings": warnings,
    }


def _is_related_label(label: Any) -> bool:
    if isinstance(label, str):
        return label.strip().lower() in {"1", "related", "true"}
    return bool(label)


def _load_hf_train_split(path: Path) -> Any:
    try:
        from datasets import load_from_disk
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "缺少依赖 datasets，请先在 Master_thesis 环境中运行：python -m pip install datasets"
        ) from exc
    return load_from_disk(str(path))["train"]


def _strip_outer_quotes(text: str) -> str:
    quote_pairs = {('"', '"'), ("'", "'"), ("“", "”"), ("‘", "’")}
    cleaned = text
    while len(cleaned) >= 2 and (cleaned[0], cleaned[-1]) in quote_pairs:
        cleaned = cleaned[1:-1].strip()
    return cleaned


if __name__ == "__main__":
    main()
