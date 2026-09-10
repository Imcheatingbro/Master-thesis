"""Reparse saved knowledge-graph global diagnostics without model calls."""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.kg_global_diagnostics import (
    aggregate_global_diagnostics,
    reparse_saved_global_diagnostics,
    save_global_diagnostic_outputs,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("diagnostics_jsonl")
    parser.add_argument("--output-dir", default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_path = Path(args.diagnostics_jsonl)
    records = [json.loads(line) for line in source_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    before_failures = sum(record.get("global_result") is None for record in records)
    records = reparse_saved_global_diagnostics(records)
    after_failures = sum(record.get("global_result") is None for record in records)

    warning_counts: Counter[str] = Counter()
    for record in records:
        result = record.get("global_result")
        if isinstance(result, dict):
            warning_counts.update(str(warning.get("type")) for warning in result.get("warnings", []))

    metrics = aggregate_global_diagnostics(records)
    first = records[0]
    dataset = str(first.get("dataset", "unknown"))
    event_prompt_version = str(first.get("event_prompt_version", "unknown"))
    global_prompt_version = str(first.get("global_prompt_version", "v1"))
    sample_count = len({(record.get("dataset"), record.get("sample_id")) for record in records})
    output_dir = Path(args.output_dir) if args.output_dir else source_path.parent
    paths = save_global_diagnostic_outputs(
        records,
        metrics,
        output_dir=output_dir,
        dataset=dataset,
        event_prompt_version=event_prompt_version,
        sample_count=sample_count,
        prompt_version=global_prompt_version,
        run_id=f"{time.strftime('%Y%m%d_%H%M%S')}_repaired",
    )

    print(f"before_failures={before_failures}")
    print(f"after_failures={after_failures}")
    print(json.dumps({"warnings": warning_counts, "metrics": metrics}, ensure_ascii=False, indent=2))
    for name, path in paths.items():
        print(f"{name}={path}")


if __name__ == "__main__":
    main()
