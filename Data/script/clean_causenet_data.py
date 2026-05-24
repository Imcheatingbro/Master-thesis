"""将 CauseNet raw 数据转换为项目统一 JSONL 格式并抽样切分。"""

from __future__ import annotations

import json
import logging
import random
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "Data"
FINETUNING_DIR_NAME = "finetuning"
CAUSENET_RAW_NAME = "Dataset_4_causenet_raw.jsonl"
CAUSENET_OUTPUT_NAME = "Dataset_4_causenet_modified.jsonl"
CAUSENET_TRAIN_OUTPUT_NAME = "Dataset_4_causenet_train.jsonl"
CAUSENET_EXTRA_OUTPUT_NAME = "Dataset_4_causenet_extra.jsonl"
STATS_NAME = "stats.json"
DEFAULT_TRAIN_SIZE = 10000
DEFAULT_TEST_SIZE = 5000
DEFAULT_SPLIT_SEED = 20260524

Sample = dict[str, Any]


def normalize_sentence(text: str) -> str:
    """合并空白但保留大小写，用于句子级合并。"""
    return re.sub(r"\s+", " ", text).strip()


def build_causenet_samples(rows: Iterable[dict[str, Any]]) -> tuple[list[Sample], dict[str, Any]]:
    """从 CauseNet relation rows 构造句子级样本，并合并同一句子的多条因果关系。"""
    grouped: dict[str, Sample] = {}
    seen_relations: dict[str, set[tuple[str, str]]] = {}
    warnings = {
        "missing_concept_rows": 0,
        "sources_without_sentence": 0,
        "substring_check_failed_relations": 0,
        "duplicate_relations": 0,
    }
    input_rows = 0
    input_sources = 0
    sentence_sources = 0

    for row in rows:
        input_rows += 1
        cause_concept, effect_concept = _extract_concepts(row)
        if not cause_concept or not effect_concept:
            warnings["missing_concept_rows"] += 1
            continue

        for source in row.get("sources") or []:
            input_sources += 1
            sentence = _extract_sentence(source)
            if not sentence:
                warnings["sources_without_sentence"] += 1
                continue
            sentence_sources += 1

            cause_span = _find_surface_span(sentence, cause_concept)
            effect_span = _find_surface_span(sentence, effect_concept)
            if cause_span is None or effect_span is None:
                warnings["substring_check_failed_relations"] += 1
                continue

            sentence_key = normalize_sentence(sentence)
            if sentence_key not in grouped:
                grouped[sentence_key] = {"id": 0, "text": sentence, "has_causal": True, "relations": []}
                seen_relations[sentence_key] = set()

            relation_key = (_normalize_relation_span(cause_span), _normalize_relation_span(effect_span))
            if relation_key in seen_relations[sentence_key]:
                warnings["duplicate_relations"] += 1
                continue

            grouped[sentence_key]["relations"].append({"cause": cause_span, "effect": effect_span})
            seen_relations[sentence_key].add(relation_key)

    samples = _renumber_samples(list(grouped.values()))
    stats = _build_source_stats(
        samples=samples,
        input_rows=input_rows,
        input_sources=input_sources,
        sentence_sources=sentence_sources,
        warnings=warnings,
    )
    return samples, stats


def split_samples(
    samples: list[Sample],
    train_size: int = DEFAULT_TRAIN_SIZE,
    test_size: int = DEFAULT_TEST_SIZE,
    seed: int = DEFAULT_SPLIT_SEED,
) -> tuple[list[Sample], list[Sample], list[Sample], dict[str, Any]]:
    """按固定随机种子打乱后切分 train/test/extra，并分别重新编号。"""
    required = train_size + test_size
    if len(samples) < required:
        raise ValueError(f"CauseNet 样本不足：需要至少 {required} 条，实际 {len(samples)} 条")

    shuffled = list(samples)
    random.Random(seed).shuffle(shuffled)
    train = _renumber_samples(shuffled[:train_size])
    test = _renumber_samples(shuffled[train_size:required])
    extra = _renumber_samples(shuffled[required:])
    stats = {
        "seed": seed,
        "train_size": train_size,
        "test_size": test_size,
        "source_samples": len(samples),
        "train": _build_file_stats(train, "train", seed, train_size, test_size),
        "test": _build_file_stats(test, "test", seed, train_size, test_size),
        "extra": _build_file_stats(extra, "extra", seed, train_size, test_size),
    }
    return train, test, extra, stats


def write_jsonl(path: Path, samples: list[Sample]) -> None:
    """以 UTF-8 与 LF 换行写出 JSONL。"""
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for sample in samples:
            file.write(json.dumps(sample, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_stats(path: Path, stats: dict[str, Any]) -> None:
    """写出稳定格式的 stats.json。"""
    with path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(stats, file, ensure_ascii=False, indent=2)
        file.write("\n")


def run_cleaning(
    data_dir: Path | str = DATA_DIR,
    train_size: int = DEFAULT_TRAIN_SIZE,
    test_size: int = DEFAULT_TEST_SIZE,
    seed: int = DEFAULT_SPLIT_SEED,
) -> dict[str, Any]:
    """读取 CauseNet raw，生成 train/test/extra 三份统一格式 JSONL 并更新 stats。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    target_dir = Path(data_dir)
    LOGGER.info("开始清洗 CauseNet 数据目录：%s", target_dir)

    samples, source_stats = build_causenet_samples(_iter_jsonl(target_dir / CAUSENET_RAW_NAME))
    train_samples, test_samples, extra_samples, split_stats = split_samples(
        samples,
        train_size=train_size,
        test_size=test_size,
        seed=seed,
    )

    finetuning_dir = target_dir / FINETUNING_DIR_NAME
    finetuning_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(finetuning_dir / CAUSENET_TRAIN_OUTPUT_NAME, train_samples)
    write_jsonl(target_dir / CAUSENET_OUTPUT_NAME, test_samples)
    write_jsonl(target_dir / CAUSENET_EXTRA_OUTPUT_NAME, extra_samples)

    stats_path = target_dir / STATS_NAME
    all_stats = json.loads(stats_path.read_text(encoding="utf-8")) if stats_path.exists() else {}
    all_stats["causenet_source"] = source_stats
    all_stats["causenet_train"] = split_stats["train"]
    all_stats["causenet"] = split_stats["test"]
    all_stats["causenet_extra"] = split_stats["extra"]
    write_stats(stats_path, all_stats)

    LOGGER.info(
        "CauseNet 清洗完成：source=%s train=%s test=%s extra=%s",
        source_stats["output_samples"],
        split_stats["train"]["output_samples"],
        split_stats["test"]["output_samples"],
        split_stats["extra"]["output_samples"],
    )
    return {"source": source_stats, "split": split_stats}


def main() -> None:
    """命令行入口。"""
    run_cleaning()


def _iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                yield json.loads(line)


def _extract_concepts(row: dict[str, Any]) -> tuple[str, str]:
    relation = row.get("causal_relation")
    if not isinstance(relation, dict):
        return "", ""
    cause = relation.get("cause")
    effect = relation.get("effect")
    cause_concept = cause.get("concept") if isinstance(cause, dict) else ""
    effect_concept = effect.get("concept") if isinstance(effect, dict) else ""
    return str(cause_concept or "").strip(), str(effect_concept or "").strip()


def _extract_sentence(source: Any) -> str:
    if not isinstance(source, dict):
        return ""
    payload = source.get("payload")
    if not isinstance(payload, dict):
        return ""
    return str(payload.get("sentence", "")).strip()


def _find_surface_span(sentence: str, concept: str) -> str | None:
    for candidate in _concept_candidates(concept):
        pattern = re.compile(re.escape(candidate).replace(r"\ ", r"\s+"), flags=re.IGNORECASE)
        match = pattern.search(sentence)
        if match is not None:
            return sentence[match.start() : match.end()]
    return None


def _concept_candidates(concept: str) -> list[str]:
    phrase = re.sub(r"\s+", " ", concept.replace("_", " ")).strip()
    literal = concept.strip()
    candidates: list[str] = []
    for candidate in (phrase, literal):
        if candidate and candidate not in candidates:
            candidates.append(candidate)
    return candidates


def _normalize_relation_span(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def _build_source_stats(
    samples: list[Sample],
    input_rows: int,
    input_sources: int,
    sentence_sources: int,
    warnings: dict[str, int],
) -> dict[str, Any]:
    stats = _build_counts(samples)
    return {
        "input_rows": input_rows,
        "input_sources": input_sources,
        "sentence_sources": sentence_sources,
        "output_samples": stats["output_samples"],
        "causal_samples": stats["causal_samples"],
        "non_causal_samples": stats["non_causal_samples"],
        "total_relations": stats["total_relations"],
        "relation_count_distribution": stats["relation_count_distribution"],
        "warnings": warnings,
    }


def _build_file_stats(
    samples: list[Sample],
    split_role: str,
    seed: int,
    train_size: int,
    test_size: int,
) -> dict[str, Any]:
    stats = _build_counts(samples)
    return {
        "split_role": split_role,
        "split_seed": seed,
        "train_size": train_size,
        "test_size": test_size,
        "output_samples": stats["output_samples"],
        "causal_samples": stats["causal_samples"],
        "non_causal_samples": stats["non_causal_samples"],
        "total_relations": stats["total_relations"],
        "relation_count_distribution": stats["relation_count_distribution"],
        "warnings": {},
    }


def _build_counts(samples: list[Sample]) -> dict[str, Any]:
    distribution = Counter(str(len(sample["relations"])) for sample in samples)
    causal_samples = sum(1 for sample in samples if sample["has_causal"])
    return {
        "output_samples": len(samples),
        "causal_samples": causal_samples,
        "non_causal_samples": len(samples) - causal_samples,
        "total_relations": sum(len(sample["relations"]) for sample in samples),
        "relation_count_distribution": dict(sorted(distribution.items(), key=lambda item: int(item[0]))),
    }


def _renumber_samples(samples: list[Sample]) -> list[Sample]:
    renumbered = []
    for new_id, sample in enumerate(samples, start=1):
        row = dict(sample)
        row["id"] = new_id
        renumbered.append(row)
    return renumbered


if __name__ == "__main__":
    main()
