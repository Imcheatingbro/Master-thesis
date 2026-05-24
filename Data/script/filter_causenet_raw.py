"""过滤 CauseNet raw JSONL，只保留带 sentence 的 provenance。"""

from __future__ import annotations

import json
import logging
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


LOGGER = logging.getLogger(__name__)
DATA_DIR = Path(__file__).resolve().parent.parent
CAUSENET_RAW_NAME = "Dataset_4_causenet_raw.jsonl"


@dataclass
class FilterStats:
    """记录 CauseNet raw 过滤统计。"""

    rows_read: int = 0
    rows_kept: int = 0
    rows_removed: int = 0
    sources_kept: int = 0
    sources_removed: int = 0
    kept_source_types: Counter[str] = field(default_factory=Counter)
    removed_source_types: Counter[str] = field(default_factory=Counter)

    def as_dict(self) -> dict[str, Any]:
        """转换为可写入日志或统计文件的 dict。"""
        return {
            "rows_read": self.rows_read,
            "rows_kept": self.rows_kept,
            "rows_removed": self.rows_removed,
            "sources_kept": self.sources_kept,
            "sources_removed": self.sources_removed,
            "kept_source_types": dict(self.kept_source_types),
            "removed_source_types": dict(self.removed_source_types),
        }


def filter_rows(rows: Iterable[dict[str, Any]]) -> tuple[list[dict[str, Any]], FilterStats]:
    """过滤内存中的 CauseNet rows，主要供单元测试使用。"""
    stats = FilterStats()
    kept_rows = []
    for row in rows:
        filtered_row = _filter_row(row, stats)
        if filtered_row is not None:
            kept_rows.append(filtered_row)
    return kept_rows, stats


def filter_file(path: Path | str = DATA_DIR / CAUSENET_RAW_NAME) -> FilterStats:
    """流式过滤 CauseNet JSONL，并用过滤后的文件替换原文件。"""
    input_path = Path(path)
    temp_path = input_path.with_name(input_path.name + ".tmp")
    stats = FilterStats()
    with input_path.open("r", encoding="utf-8") as input_file, temp_path.open(
        "w", encoding="utf-8", newline="\n"
    ) as output_file:
        for line in input_file:
            if not line.strip():
                continue
            row = json.loads(line)
            filtered_row = _filter_row(row, stats)
            if filtered_row is not None:
                output_file.write(json.dumps(filtered_row, ensure_ascii=False, separators=(",", ":")) + "\n")

    temp_path.replace(input_path)
    return stats


def main() -> None:
    """命令行入口。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    stats = filter_file()
    LOGGER.info("CauseNet raw 过滤完成：%s", stats.as_dict())


def _filter_row(row: dict[str, Any], stats: FilterStats) -> dict[str, Any] | None:
    stats.rows_read += 1
    sources = row.get("sources") or []
    kept_sources = []
    for source in sources:
        source_type = str(source.get("type", "")) if isinstance(source, dict) else ""
        if _has_sentence(source):
            kept_sources.append(source)
            stats.sources_kept += 1
            stats.kept_source_types[source_type] += 1
        else:
            stats.sources_removed += 1
            stats.removed_source_types[source_type] += 1

    if not kept_sources:
        stats.rows_removed += 1
        return None

    filtered_row = dict(row)
    filtered_row["sources"] = kept_sources
    stats.rows_kept += 1
    return filtered_row


def _has_sentence(source: Any) -> bool:
    if not isinstance(source, dict):
        return False
    payload = source.get("payload")
    if not isinstance(payload, dict):
        return False
    return bool(str(payload.get("sentence", "")).strip())


if __name__ == "__main__":
    main()
