"""Apply a new knowledge-graph judge rubric to saved extraction spans."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.kg_eval_pipeline import KGRejudgeConfig, run_saved_kg_judging


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_spans_path")
    parser.add_argument("--judge-version", default="v3")
    parser.add_argument("--api-key", default="deepseek_api.txt")
    parser.add_argument("--model", default="deepseek-v4-pro")
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--max-tokens", type=int, default=2048)
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--output-dir", default="results/kg_evaluation/rejudged")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        from tqdm.auto import tqdm
    except ImportError:
        tqdm = None

    result = run_saved_kg_judging(
        KGRejudgeConfig(
            source_spans_path=args.source_spans_path,
            judge_prompt_version=args.judge_version,
            output_dir=args.output_dir,
            judge_api_key_path=args.api_key,
            judge_model=args.model,
            judge_max_tokens=args.max_tokens,
            judge_timeout=args.timeout,
            judge_max_workers=args.workers,
        ),
        progress_factory=tqdm,
    )
    print(json.dumps(result.method_metrics, ensure_ascii=False, indent=2))
    for label, path in result.output_paths.items():
        print(f"{label}={path}")


if __name__ == "__main__":
    main()
