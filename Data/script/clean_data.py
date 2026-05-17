"""实现 SPEC_01 数据清洗规范 v0.2 的 CNC 与 Li 数据转换。"""

from __future__ import annotations

import ast
import csv
import json
import logging
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger(__name__)

CNC_RAW_NAME = "Dataset_1_CNC_raw.csv"
LI_RAW_NAME = "Dataset_2_Li_raw.xml"
CNC_OUTPUT_NAME = "Dataset_1_CNC_modified.jsonl"
LI_OUTPUT_NAME = "Dataset_2_Li_modified.jsonl"
STATS_NAME = "stats.json"


Sample = dict[str, Any]
WarningCounts = dict[str, int]


def empty_cnc_warnings() -> WarningCounts:
    """创建 CNC 软错误计数器。"""
    return {
        "num_rs_mismatch": 0,
        "substring_check_failed_relations": 0,
        "substring_check_failed_samples": 0,
    }


def empty_li_warnings() -> WarningCounts:
    """创建 Li 软错误计数器。"""
    return {
        "missing_entity_mapping": 0,
        "substring_check_failed_relations": 0,
        "substring_check_failed_samples": 0,
    }


def add_warnings(total: WarningCounts, current: WarningCounts) -> None:
    """将单条样本的软错误累加到总计数器。"""
    for key, value in current.items():
        total[key] += value


def parse_cnc_row(row: dict[str, str], sample_id: int) -> tuple[Sample, WarningCounts]:
    """按规范第 2 节解析一行 CNC CSV 数据。"""
    warnings = empty_cnc_warnings()
    text = row["text"]
    raw_pairs = ast.literal_eval(row["causal_text_w_pairs"])
    expected_relations = int(row["num_rs"])

    if len(raw_pairs) != expected_relations:
        warnings["num_rs_mismatch"] += 1
        LOGGER.warning("CNC 样本 %s 的 num_rs 与标注列表长度不一致", sample_id)

    relations: list[dict[str, str]] = []
    for raw_pair in raw_pairs:
        cleaned_pair = re.sub(r"</?SIG\d*>", "", raw_pair)
        cause_match = re.search(r"<ARG0>(.+?)</ARG0>", cleaned_pair, flags=re.DOTALL)
        effect_match = re.search(r"<ARG1>(.+?)</ARG1>", cleaned_pair, flags=re.DOTALL)
        if cause_match is None or effect_match is None:
            warnings["substring_check_failed_relations"] += 1
            LOGGER.warning("CNC 样本 %s 缺少 ARG0 或 ARG1 标记", sample_id)
            continue

        relation = {
            "cause": cause_match.group(1).strip(),
            "effect": effect_match.group(1).strip(),
        }
        if relation["cause"] in text and relation["effect"] in text:
            relations.append(relation)
        else:
            warnings["substring_check_failed_relations"] += 1
            LOGGER.warning("CNC 样本 %s 的 relation 未通过子串校验", sample_id)

    if raw_pairs and warnings["substring_check_failed_relations"] > 0 and len(relations) < len(raw_pairs):
        warnings["substring_check_failed_samples"] += 1

    return {
        "id": sample_id,
        "text": text,
        "has_causal": bool(raw_pairs),
        "relations": relations,
    }, warnings


def parse_li_item(label: str, sentence: str, sample_id: int) -> tuple[Sample, WarningCounts]:
    """按规范第 3 节解析一个 Li XML item。"""
    warnings = empty_li_warnings()
    entity_map = {
        f"e{match.group(1)}": match.group(2)
        for match in re.finditer(r"<e(\d+)>(.+?)</e\1>", sentence, flags=re.DOTALL)
    }
    text = re.sub(r"</?e\d+>", "", sentence)
    has_causal = label != "Non-Causal"
    relations: list[dict[str, str]] = []
    failed_relations = 0

    if has_causal:
        for cause_id, effect_id in re.findall(r"\((e\d+),(e\d+)\)", label):
            cause = entity_map.get(cause_id)
            effect = entity_map.get(effect_id)
            if cause is None or effect is None:
                warnings["missing_entity_mapping"] += 1
                failed_relations += 1
                LOGGER.warning("Li 样本 %s 缺少实体映射：%s 或 %s", sample_id, cause_id, effect_id)
                continue

            relation = {"cause": cause.strip(), "effect": effect.strip()}
            if relation["cause"] in text and relation["effect"] in text:
                relations.append(relation)
            else:
                warnings["substring_check_failed_relations"] += 1
                failed_relations += 1
                LOGGER.warning("Li 样本 %s 的 relation 未通过子串校验", sample_id)

    if failed_relations > 0:
        warnings["substring_check_failed_samples"] += 1

    return {
        "id": sample_id,
        "text": text,
        "has_causal": has_causal,
        "relations": relations,
    }, warnings


def build_stats(
    samples: list[Sample],
    warnings: WarningCounts,
    input_count_key: str,
    input_count: int,
) -> dict[str, Any]:
    """根据输出样本构造 stats.json 中的单数据集统计对象。"""
    distribution = Counter(str(len(sample["relations"])) for sample in samples)
    causal_samples = sum(1 for sample in samples if sample["has_causal"])
    return {
        input_count_key: input_count,
        "output_samples": len(samples),
        "causal_samples": causal_samples,
        "non_causal_samples": len(samples) - causal_samples,
        "total_relations": sum(len(sample["relations"]) for sample in samples),
        "relation_count_distribution": dict(sorted(distribution.items(), key=lambda item: int(item[0]))),
        "warnings": warnings,
    }


def write_jsonl(path: Path, samples: list[Sample]) -> None:
    """以 UTF-8 与 LF 换行写出 JSONL。"""
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for sample in samples:
            file.write(json.dumps(sample, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_stats(path: Path, stats: dict[str, Any]) -> None:
    """以稳定格式写出统计文件。"""
    with path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(stats, file, ensure_ascii=False, indent=2)
        file.write("\n")


def write_lessons(data_dir: Path, stats: dict[str, Any]) -> None:
    """记录本次实现的路径差异、设计取舍与软错误统计。"""
    reports_dir = data_dir.parent / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    lessons_path = reports_dir / "LESSONS.md"
    content = (
        "# LESSONS\n\n"
        "## SPEC_01 数据清洗实现\n\n"
        "- 实际数据文件直接位于 `Data` 目录，未采用规范示例中的 `data/raw` 与 `data/modified` 分层；"
        "按项目作者要求，脚本位于 `Data/script`，新数据直接写回 `Data`。\n"
        "- `relation_count_distribution` 使用实际关系数量动态生成 key；"
        "这是因为 CNC 原始数据存在 4 和 5 个 relation 的样本，规范示例只展示到 3。\n"
        f"- CNC 软错误统计：`{json.dumps(stats['cnc']['warnings'], ensure_ascii=False)}`。\n"
        f"- Li 软错误统计：`{json.dumps(stats['li']['warnings'], ensure_ascii=False)}`。\n"
        "- 解析过程只剥离标签与首尾空白，保留原始文本内部空格和标点空格。\n"
    )
    with lessons_path.open("w", encoding="utf-8", newline="\n") as file:
        file.write(content)


def load_cnc_samples(data_dir: Path) -> tuple[list[Sample], dict[str, Any]]:
    """读取并转换 CNC 原始 CSV。"""
    input_path = data_dir / CNC_RAW_NAME
    warnings = empty_cnc_warnings()
    samples: list[Sample] = []

    with input_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for sample_id, row in enumerate(reader, start=1):
            sample, current_warnings = parse_cnc_row(row, sample_id)
            samples.append(sample)
            add_warnings(warnings, current_warnings)

    stats = build_stats(samples, warnings, "input_rows", len(samples))
    return samples, stats


def load_li_samples(data_dir: Path) -> tuple[list[Sample], dict[str, Any]]:
    """读取并转换 Li 原始 XML。"""
    input_path = data_dir / LI_RAW_NAME
    root = ET.parse(input_path).getroot()
    warnings = empty_li_warnings()
    samples: list[Sample] = []

    for sample_id, item in enumerate(root.findall("item"), start=1):
        label = item.attrib["label"]
        sentence_element = item.find("sentence")
        if sentence_element is None or sentence_element.text is None:
            raise ValueError(f"Li 样本 {sample_id} 缺少 sentence 文本")
        sample, current_warnings = parse_li_item(label, sentence_element.text, sample_id)
        samples.append(sample)
        add_warnings(warnings, current_warnings)

    stats = build_stats(samples, warnings, "input_items", len(samples))
    return samples, stats


def run_cleaning(data_dir: Path) -> dict[str, Any]:
    """执行完整清洗流程，并将新数据写入 Data 目录。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    LOGGER.info("开始清洗数据目录：%s", data_dir)

    cnc_samples, cnc_stats = load_cnc_samples(data_dir)
    li_samples, li_stats = load_li_samples(data_dir)
    stats = {"cnc": cnc_stats, "li": li_stats}

    write_jsonl(data_dir / CNC_OUTPUT_NAME, cnc_samples)
    write_jsonl(data_dir / LI_OUTPUT_NAME, li_samples)
    write_stats(data_dir / STATS_NAME, stats)
    write_lessons(data_dir, stats)

    LOGGER.info("数据清洗完成")
    return stats


def main() -> None:
    """命令行入口：默认处理脚本上一级 Data 目录。"""
    run_cleaning(Path(__file__).resolve().parent.parent)


if __name__ == "__main__":
    main()
