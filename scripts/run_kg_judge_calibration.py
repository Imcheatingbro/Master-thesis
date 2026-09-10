"""Run the fixed ten-case calibration for knowledge-graph judge versions 2 and 3."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.kg_evaluator import DeepSeekJudgeClient
from src.kg_judge_calibration import calibration_gate, load_calibration_cases, run_calibration_version


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", default="Data/KG_eval/judge_v3_calibration_10.jsonl")
    parser.add_argument("--api-key", default="deepseek_api.txt")
    parser.add_argument("--model", default="deepseek-v4-pro")
    parser.add_argument("--versions", nargs="+", default=["v2", "v3"])
    parser.add_argument("--workers", type=int, default=5)
    parser.add_argument("--max-tokens", type=int, default=2048)
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--output-dir", default="results/kg_evaluation/judge_calibration")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cases = load_calibration_cases(args.cases, expected_count=10)
    client = DeepSeekJudgeClient(
        api_key_path=args.api_key,
        model=args.model,
        max_tokens=args.max_tokens,
        timeout=args.timeout,
    )

    results = {}
    for version in args.versions:
        version_result = run_calibration_version(
            cases,
            prompt_version=version,
            judge_client=client,
            max_workers=args.workers,
        )
        version_result["gate"] = calibration_gate(version_result["summary"])
        results[version] = version_result

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    run_id = time.strftime("%Y%m%d_%H%M%S")
    details_path = output_dir / f"judge_v2_v3_calibration_{run_id}.json"
    details_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    summary_path = output_dir / f"judge_v2_v3_calibration_{run_id}.csv"
    summary_keys = list(next(iter(results.values()))["summary"])
    with summary_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["prompt_version", "gate_passed", *summary_keys])
        writer.writeheader()
        for version, result in results.items():
            writer.writerow(
                {
                    "prompt_version": version,
                    "gate_passed": result["gate"]["passed"],
                    **result["summary"],
                }
            )

    compact = {
        version: {"summary": result["summary"], "gate": result["gate"]}
        for version, result in results.items()
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2))
    print(f"details={details_path}")
    print(f"summary={summary_path}")


if __name__ == "__main__":
    main()
