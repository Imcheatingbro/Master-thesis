"""KG evaluation pipeline 的单元测试。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.kg_eval_pipeline import KGEvalConfig, resolve_eval_max_depth, resolve_eval_schema, run_kg_evaluation


class FakeConstructionClient:
    """记录本地 construction extraction 调用顺序。"""

    def __init__(self) -> None:
        self.spans: list[str] = []

    def chat(self, messages: list[dict[str, str]]) -> str:
        user_content = messages[1]["content"]
        span = user_content.split("Span: ", 1)[1].splitlines()[0]
        self.spans.append(span)
        return json.dumps({"components": [{"role": "Theme", "value": span, "attributes": []}]})


class FakeJudgeClient:
    """返回紧凑 judge JSON。"""

    def __init__(self) -> None:
        self.prompts: list[str] = []

    def chat(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return json.dumps(
            {
                "span_id": "s0",
                "units": [{"id": "n0", "s": 1, "r": 1, "m": 1, "a": None, "t": 1, "e": None}],
            }
        )


class FakeProgress:
    """兼容 tqdm 的最小 progress object。"""

    def __init__(self, iterable: Any = None, **kwargs: Any) -> None:
        self.iterable = iterable
        self.kwargs = kwargs
        self.updates = 0
        self.closed = False

    def __iter__(self):
        return iter(self.iterable)

    def update(self, value: int) -> None:
        self.updates += value

    def close(self) -> None:
        self.closed = True


def test_resolve_eval_schema_and_depth_follow_prompt_version() -> None:
    assert resolve_eval_schema("nested_v1", "auto") == "nested"
    assert resolve_eval_schema("v2", "auto") == "two_layer"
    assert resolve_eval_schema("nested_v1", "two_layer") == "two_layer"
    assert resolve_eval_max_depth("v2", "two_layer", "auto") == 1
    assert resolve_eval_max_depth("nested_depth3", "nested", "auto") == 3
    assert resolve_eval_max_depth("nested_v1", "nested", "auto") is None
    assert resolve_eval_max_depth("nested_v1", "nested", 2) == 2


def test_run_kg_evaluation_extracts_then_judges_and_saves_outputs(tmp_path: Path) -> None:
    samples = [
        {
            "id": 1,
            "text": "rain caused flooding",
            "has_causal": True,
            "relations": [{"cause": "rain", "effect": "flooding"}],
        }
    ]
    construction_client = FakeConstructionClient()
    judge_client = FakeJudgeClient()
    progress_objects: list[FakeProgress] = []

    def progress_factory(iterable: Any = None, **kwargs: Any) -> FakeProgress:
        progress = FakeProgress(iterable, **kwargs)
        progress_objects.append(progress)
        return progress

    result = run_kg_evaluation(
        config=KGEvalConfig(
            dataset="cnc",
            event_prompt_version="v2",
            sample_n=1,
            checkpoint_every=1,
            output_dir=tmp_path,
            run_judge=True,
            save_outputs=True,
        ),
        construction_client=construction_client,
        samples=samples,
        judge_client=judge_client,
        progress_factory=progress_factory,
    )

    assert construction_client.spans == ["rain", "flooding"]
    assert len(judge_client.prompts) == 2
    assert [span["span_id"] for span in result.span_results] == ["cnc_1_t0_cause", "cnc_1_t0_effect"]
    assert result.span_results[0]["judge_result"]["units"][0]["id"] == "n0"
    assert result.method_metrics["sample_count"] == 1
    assert result.method_metrics["span_count"] == 2
    assert result.method_metrics["judge_success"] == 1
    assert result.output_paths["spans"].exists()
    assert result.output_paths["samples"].exists()
    assert result.output_paths["metrics"].exists()
    assert result.checkpoint_paths[0].exists()
    assert {progress.kwargs.get("desc") for progress in progress_objects} == {"KG eval samples", "DeepSeek judge spans"}


def test_run_kg_evaluation_can_skip_judge_and_output_files(tmp_path: Path) -> None:
    samples = [
        {
            "id": 2,
            "text": "wind caused delays",
            "has_causal": True,
            "relations": [{"cause": "wind", "effect": "delays"}],
        }
    ]

    result = run_kg_evaluation(
        config=KGEvalConfig(
            dataset="cnc",
            event_prompt_version="nested_v1",
            sample_n=1,
            output_dir=tmp_path,
            run_judge=False,
            save_outputs=False,
        ),
        construction_client=FakeConstructionClient(),
        samples=samples,
    )

    assert result.eval_schema == "nested"
    assert result.eval_max_depth is None
    assert result.output_paths == {}
    assert result.checkpoint_paths == []
    assert result.span_results[0]["judge_result"] is None
    assert result.span_results[0]["span_metrics"]["judge_success"] == 0
    assert result.method_metrics["judge_success"] == 0
    assert not list(tmp_path.glob("*_spans.jsonl"))
