"""验证 SPEC_01 清洗产物的 schema、统计与换行格式。"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).resolve().parent.parent
LOGGER = logging.getLogger(__name__)


def validate_jsonl(name: str, path: Path, stats: dict[str, Any]) -> str:
    """验证单个 JSONL 文件并返回摘要。"""
    data = path.read_bytes()
    if not data.endswith(b"\n") or b"\r\n" in data:
        raise AssertionError(f"{path} 不是 LF 结尾格式")

    lines = path.read_text(encoding="utf-8").splitlines()
    ids: list[int] = []
    relation_sum = 0
    causal_samples = 0
    non_causal_samples = 0
    distribution: dict[str, int] = {}

    for line_no, line in enumerate(lines, start=1):
        sample = json.loads(line)
        if list(sample.keys()) != ["id", "text", "has_causal", "relations"]:
            raise AssertionError(f"{path}:{line_no} 顶层字段顺序错误")
        if re.search(r"</?(ARG|SIG|e)\d*>", sample["text"]):
            raise AssertionError(f"{path}:{line_no} text 残留标注标签")

        ids.append(sample["id"])
        if sample["has_causal"]:
            causal_samples += 1
        else:
            non_causal_samples += 1
            if sample["relations"] != []:
                raise AssertionError(f"{path}:{line_no} 非因果样本 relations 非空")

        for relation in sample["relations"]:
            if list(relation.keys()) != ["cause", "effect"]:
                raise AssertionError(f"{path}:{line_no} relation 字段错误")
            if not relation["cause"] or not relation["effect"]:
                raise AssertionError(f"{path}:{line_no} relation 存在空字符串")
            if relation["cause"] not in sample["text"] or relation["effect"] not in sample["text"]:
                raise AssertionError(f"{path}:{line_no} relation 未通过子串校验")

        relation_count = len(sample["relations"])
        relation_sum += relation_count
        distribution[str(relation_count)] = distribution.get(str(relation_count), 0) + 1

    if ids != list(range(1, len(lines) + 1)):
        raise AssertionError(f"{path} id 不连续")
    if stats[name]["output_samples"] != len(lines):
        raise AssertionError(f"{name} output_samples 不一致")
    if stats[name]["causal_samples"] != causal_samples:
        raise AssertionError(f"{name} causal_samples 不一致")
    if stats[name]["non_causal_samples"] != non_causal_samples:
        raise AssertionError(f"{name} non_causal_samples 不一致")
    if stats[name]["total_relations"] != relation_sum:
        raise AssertionError(f"{name} total_relations 不一致")
    if stats[name]["relation_count_distribution"] != distribution:
        raise AssertionError(f"{name} relation_count_distribution 不一致")
    if distribution.get("0", 0) != non_causal_samples:
        raise AssertionError(f"{name} 0 关系分布与非因果样本数不一致")

    return f"{name}: {len(lines)} samples, {relation_sum} relations, LF ok"


def main() -> None:
    """执行完整产物验收。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    stats = json.loads((DATA_DIR / "stats.json").read_text(encoding="utf-8"))
    summaries = [
        validate_jsonl("cnc", DATA_DIR / "Dataset_1_CNC_modified.jsonl", stats),
        validate_jsonl("li", DATA_DIR / "Dataset_2_Li_modified.jsonl", stats),
    ]
    for summary in summaries:
        LOGGER.info(summary)
    LOGGER.info("validation ok")


if __name__ == "__main__":
    main()
