"""构造用于验证 DeepSeek 裁判能力的 RAMS 二分类测试集。"""

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
DEFAULT_SEED = 20260723
NEGATIVE_TYPES = ("role_corruption", "span_swap")

JsonObject = dict[str, Any]
Span = tuple[int, int]
CandidateKey = tuple[int, int, str]


def short_role(raw_role: str) -> str:
    """将 RAMS 原始角色编码转换为官方评分器使用的短角色名。"""
    return re.split(r"\d+", raw_role)[-1]


def load_jsonlines(path: Path) -> list[JsonObject]:
    """读取 JSON Lines 文件。"""
    with path.open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def load_ontology(path: Path) -> dict[str, list[str]]:
    """读取 RAMS 事件类型与允许角色的对应关系。"""
    ontology: dict[str, list[str]] = {}
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            fields = line.split()
            if not fields:
                continue
            ontology[fields[0]] = fields[1::2]
    return ontology


def locate_span(sentences: list[list[str]], span: Span) -> JsonObject:
    """返回全局 token span 对应的文本和句内位置。"""
    start, end = span
    offset = 0
    for sentence_id, sentence in enumerate(sentences):
        sentence_end = offset + len(sentence)
        if offset <= start and end < sentence_end:
            local_start = start - offset
            local_end = end - offset
            return {
                "text": " ".join(sentence[local_start : local_end + 1]),
                "start": start,
                "end": end,
                "sentence_id": sentence_id,
                "sentence_start": local_start,
                "sentence_end": local_end,
            }
        offset = sentence_end
    raise ValueError(f"span 超出文档范围或跨越句子边界: {span}")


def unique_gold_links(document: JsonObject) -> list[tuple[Span, str]]:
    """按原始顺序返回去重后的 gold argument span-role 对。"""
    links: list[tuple[Span, str]] = []
    seen: set[tuple[Span, str]] = set()
    for link in document["gold_evt_links"]:
        item = (tuple(link[1]), short_role(link[2]))
        if item not in seen:
            seen.add(item)
            links.append(item)
    return links


def candidate_key(span: Span, role: str) -> CandidateKey:
    """生成候选论元在单个事件中的唯一键。"""
    return span[0], span[1], role


def negative_options(
    gold_links: list[tuple[Span, str]],
    allowed_roles: list[str],
    source_span: Span,
    source_role: str,
) -> dict[str, list[tuple[Span, str]]]:
    """为一个 gold link 生成角色扰动和论元交换反例候选。"""
    gold_keys = {candidate_key(span, role) for span, role in gold_links}
    observed_roles = [role for _, role in gold_links if role != source_role]
    role_order = list(dict.fromkeys(observed_roles + allowed_roles))

    role_corruptions = [
        (source_span, role)
        for role in role_order
        if role != source_role and candidate_key(source_span, role) not in gold_keys
    ]
    span_swaps = [
        (span, source_role)
        for span, _ in gold_links
        if span != source_span and candidate_key(span, source_role) not in gold_keys
    ]
    return {
        "role_corruption": list(dict.fromkeys(role_corruptions)),
        "span_swap": list(dict.fromkeys(span_swaps)),
    }


def build_record(
    document: JsonObject,
    event_type: str,
    allowed_roles: list[str],
    pair_id: str,
    span: Span,
    role: str,
    label: bool,
    negative_type: str | None,
) -> JsonObject:
    """构造一条可直接转换为裁判 prompt 的候选记录。"""
    trigger_span = tuple(document["evt_triggers"][0][:2])
    return {
        "pair_id": pair_id,
        "doc_key": document["doc_key"],
        "source_split": "test",
        "sentences": [" ".join(sentence) for sentence in document["sentences"]],
        "event": {
            "type": event_type,
            "trigger": locate_span(document["sentences"], trigger_span),
            "allowed_roles": allowed_roles,
        },
        "candidate": {
            "role": role,
            "span": locate_span(document["sentences"], span),
        },
        "label": label,
        "case_type": "positive" if label else negative_type,
    }


def build_dataset(
    documents: list[JsonObject],
    ontology: dict[str, list[str]],
    seed: int = DEFAULT_SEED,
) -> tuple[list[JsonObject], JsonObject]:
    """构造标签均衡、候选唯一且可复现的 RAMS judge 数据集。"""
    records: list[JsonObject] = []
    negative_counts: Counter[str] = Counter()
    raw_gold_links = 0
    duplicate_gold_links = 0
    documents_with_gold_links = 0
    used_document_keys: set[str] = set()
    omitted_gold_links = 0

    for document in documents:
        raw_gold_links += len(document["gold_evt_links"])
        gold_links = unique_gold_links(document)
        duplicate_gold_links += len(document["gold_evt_links"]) - len(gold_links)
        if not gold_links:
            continue

        documents_with_gold_links += 1
        event_type = document["evt_triggers"][0][2][0][0]
        allowed_roles = ontology[event_type]
        gold_keys = {candidate_key(span, role) for span, role in gold_links}
        used_negative_keys: set[CandidateKey] = set()

        for argument_index, (gold_span, gold_role) in enumerate(gold_links):
            pair_id = f"{document['doc_key']}::arg{argument_index:02d}"
            options = negative_options(
                gold_links,
                allowed_roles,
                gold_span,
                gold_role,
            )
            type_order = sorted(
                NEGATIVE_TYPES,
                key=lambda name: (negative_counts[name], NEGATIVE_TYPES.index(name)),
            )
            selected: tuple[str, Span, str] | None = None
            for negative_type in type_order:
                for candidate_span, candidate_role in options[negative_type]:
                    key = candidate_key(candidate_span, candidate_role)
                    if key not in gold_keys and key not in used_negative_keys:
                        selected = negative_type, candidate_span, candidate_role
                        break
                if selected is not None:
                    break

            if selected is None:
                omitted_gold_links += 1
                continue

            negative_type, negative_span, negative_role = selected
            used_negative_keys.add(candidate_key(negative_span, negative_role))
            negative_counts[negative_type] += 1
            used_document_keys.add(document["doc_key"])
            records.append(
                build_record(
                    document,
                    event_type,
                    allowed_roles,
                    pair_id,
                    gold_span,
                    gold_role,
                    True,
                    None,
                )
            )
            records.append(
                build_record(
                    document,
                    event_type,
                    allowed_roles,
                    pair_id,
                    negative_span,
                    negative_role,
                    False,
                    negative_type,
                )
            )

    random.Random(seed).shuffle(records)
    records = [
        {"id": f"rams-judge-{index:05d}", **record}
        for index, record in enumerate(records, start=1)
    ]
    metadata = {
        "source_documents": len(documents),
        "documents_with_gold_links": documents_with_gold_links,
        "used_documents": len(used_document_keys),
        "documents_without_gold_links": len(documents) - documents_with_gold_links,
        "raw_gold_links": raw_gold_links,
        "unique_gold_links": raw_gold_links - duplicate_gold_links,
        "duplicate_gold_links_removed": duplicate_gold_links,
        "gold_links_used_as_positive": len(records) // 2,
        "gold_links_omitted_without_unique_semantic_negative": omitted_gold_links,
        "negative_type_counts": dict(sorted(negative_counts.items())),
    }
    return records, metadata


def validate_dataset(records: list[JsonObject]) -> JsonObject:
    """校验标签、配对、候选唯一性、span 文本和角色集合。"""
    ids = [record["id"] for record in records]
    pair_labels: dict[str, list[bool]] = {}
    candidate_keys: set[tuple[str, int, int, str]] = set()

    for record in records:
        pair_labels.setdefault(record["pair_id"], []).append(record["label"])
        span = record["candidate"]["span"]
        key = (
            record["doc_key"],
            span["start"],
            span["end"],
            record["candidate"]["role"],
        )
        if key in candidate_keys:
            raise ValueError(f"发现重复候选: {key}")
        candidate_keys.add(key)

        sentence_tokens = record["sentences"][span["sentence_id"]].split()
        recovered_text = " ".join(
            sentence_tokens[span["sentence_start"] : span["sentence_end"] + 1]
        )
        if recovered_text != span["text"]:
            raise ValueError(f"span 文本校验失败: {record['id']}")
        if record["candidate"]["role"] not in record["event"]["allowed_roles"]:
            raise ValueError(f"候选角色不属于事件本体: {record['id']}")

    invalid_pairs = {
        pair_id: labels
        for pair_id, labels in pair_labels.items()
        if sorted(labels) != [False, True]
    }
    if len(ids) != len(set(ids)):
        raise ValueError("记录 id 不唯一")
    if invalid_pairs:
        raise ValueError(f"正负例配对失败: {len(invalid_pairs)}")

    label_counts = Counter(str(record["label"]).lower() for record in records)
    if label_counts["true"] != label_counts["false"]:
        raise ValueError("正负标签数量不平衡")

    return {
        "record_ids_unique": True,
        "candidate_assertions_unique": True,
        "each_pair_has_one_positive_and_one_negative": True,
        "labels_balanced": True,
        "candidate_spans_valid": True,
        "candidate_roles_allowed": True,
    }


def file_sha256(path: Path) -> str:
    """计算文件 SHA-256。"""
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_jsonlines(path: Path, records: list[JsonObject]) -> None:
    """写出 JSON Lines 数据集。"""
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_statistics(
    records: list[JsonObject],
    metadata: JsonObject,
    validation: JsonObject,
    source_path: Path,
    output_path: Path,
    seed: int,
) -> JsonObject:
    """汇总数据来源、标签、反例类型及质量校验统计。"""
    positive_records = [record for record in records if record["label"]]
    event_counts = Counter(record["event"]["type"] for record in positive_records)
    role_counts = Counter(record["candidate"]["role"] for record in positive_records)
    span_length_counts = Counter(
        record["candidate"]["span"]["end"] - record["candidate"]["span"]["start"] + 1
        for record in positive_records
    )
    label_counts = Counter(str(record["label"]).lower() for record in records)
    case_type_counts = Counter(record["case_type"] for record in records)

    return {
        "dataset": "RAMS judge binary evaluation set",
        "source": {
            "split": "test",
            "path": str(source_path),
            **metadata,
        },
        "construction": {
            "unit": "event-argument candidate assertion",
            "positive_definition": "去重后的 RAMS gold_evt_links",
            "negative_definition": "不与同一事件任何 gold link 重合的受控扰动",
            "positive_to_negative_ratio": "1:1",
            "negative_type_priority": list(NEGATIVE_TYPES),
            "shuffle_seed": seed,
        },
        "records": {
            "total": len(records),
            "label_counts": dict(sorted(label_counts.items())),
            "case_type_counts": dict(sorted(case_type_counts.items())),
            "unique_event_types": len(event_counts),
            "unique_positive_roles": len(role_counts),
            "positive_span_length_counts": {
                str(key): value for key, value in sorted(span_length_counts.items())
            },
            "positive_role_counts": dict(sorted(role_counts.items())),
            "positive_event_type_counts": dict(sorted(event_counts.items())),
        },
        "quality_checks": validation,
        "artifacts": {
            "dataset_path": str(output_path),
            "dataset_sha256": file_sha256(output_path),
        },
    }


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    project_root = Path(__file__).resolve().parents[2]
    rams_root = project_root / "Data" / "RAMS_1.0c" / "RAMS_1.0c"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=rams_root / "data" / "test.jsonlines",
    )
    parser.add_argument(
        "--ontology",
        type=Path,
        default=rams_root / "scorer" / "event_role_multiplicities.txt",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=project_root / "Data" / "RAMS_judge",
    )
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def main() -> None:
    """生成 RAMS judge 数据集及统计文件。"""
    args = parse_args()
    documents = load_jsonlines(args.input)
    ontology = load_ontology(args.ontology)
    records, metadata = build_dataset(documents, ontology, args.seed)
    validation = validate_dataset(records)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    dataset_path = args.output_dir / "rams_judge_test.jsonl"
    stats_path = args.output_dir / "stats.json"
    write_jsonlines(dataset_path, records)
    statistics = build_statistics(
        records,
        metadata,
        validation,
        args.input,
        dataset_path,
        args.seed,
    )
    with stats_path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(statistics, file, ensure_ascii=False, indent=2)
        file.write("\n")

    LOGGER.info("已生成 %s 条记录: %s", len(records), dataset_path)
    LOGGER.info("统计文件: %s", stats_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
