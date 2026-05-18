"""SPEC_04：Generator 输出解析与重试逻辑的单元测试。"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.generator import generate, parse_output, validate_minimal


class FakeClient:
    """按顺序返回预设输出或抛出异常的测试客户端。"""

    def __init__(self, outputs: list[str | Exception]) -> None:
        self.outputs = outputs
        self.calls = 0

    def chat(self, messages: list[dict[str, str]]) -> str:
        self.calls += 1
        output = self.outputs.pop(0)
        if isinstance(output, Exception):
            raise output
        return output


class RecordingRetriever:
    """记录被调用参数的测试检索器。"""

    def __init__(self) -> None:
        self.calls: list[tuple[str, int]] = []

    def retrieve(self, text: str, top_k: int) -> list[dict[str, object]]:
        self.calls.append((text, top_k))
        return [
            {
                "sentence": "<cause>Rain</cause> caused <effect>flooding</effect>.",
                "cause": "Rain",
                "effect": "flooding",
                "causality_phrase": "caused",
                "score": 99.0,
            }
        ]


def test_parse_output_accepts_plain_json() -> None:
    result = parse_output('{"has_causal": true, "triples": []}')

    assert result == {"has_causal": True, "triples": []}


def test_parse_output_accepts_markdown_code_block() -> None:
    result = parse_output('```json\n{"has_causal": false, "triples": []}\n```')

    assert result == {"has_causal": False, "triples": []}


def test_parse_output_accepts_prefix_and_think_text() -> None:
    raw = """
<think>模型推理文本，不能进入结果。</think>
Here is the result:
{
  "has_causal": true,
  "triples": [
    {
      "cause": {"span": "Heavy rain"},
      "relation": "caused",
      "effect": {"span": "flooding"}
    }
  ]
}
"""

    result = parse_output(raw)

    assert result["has_causal"] is True
    assert result["triples"][0]["cause"]["span"] == "Heavy rain"


def test_parse_output_raises_clear_error_when_fields_are_missing() -> None:
    with pytest.raises(ValueError, match="has_causal"):
        parse_output('{"triples": []}')


def test_validate_minimal_rejects_wrong_types() -> None:
    assert validate_minimal({"has_causal": True, "triples": []}) is True
    assert validate_minimal({"has_causal": "true", "triples": []}) is False
    assert validate_minimal({"has_causal": True, "triples": {}}) is False


def test_generate_retries_after_parse_failure_and_sets_id() -> None:
    client = FakeClient(
        [
            "not json",
            '{"has_causal": true, "triples": [{"cause": {"span": "Rain"}, "relation": "caused", "effect": {"span": "flooding"}}]}',
        ]
    )

    result = generate(
        text="Rain caused flooding.",
        sample_id=12,
        client=client,
        retriever=None,
        use_rag=False,
        top_k=0,
        max_retry=2,
    )

    assert client.calls == 2
    assert result["id"] == 12
    assert result["has_causal"] is True
    assert result["triples"][0]["effect"]["span"] == "flooding"


def test_generate_returns_fallback_after_retries_are_exhausted() -> None:
    client = FakeClient(["not json", ValueError("坏输出")])

    result = generate(
        text="No reliable output.",
        sample_id=None,
        client=client,
        retriever=None,
        use_rag=False,
        top_k=0,
        max_retry=2,
    )

    assert client.calls == 2
    assert result == {"id": None, "has_causal": False, "triples": []}


def test_generate_passes_rag_mode_to_prompt_builder() -> None:
    client = FakeClient(['{"has_causal": true, "triples": []}'])
    retriever = RecordingRetriever()

    result = generate(
        text="Rain caused flooding.",
        sample_id=3,
        client=client,
        retriever=retriever,
        use_rag=True,
        top_k=1,
        rag_mode="knn_pattern",
        max_retry=1,
    )

    assert result == {"id": 3, "has_causal": True, "triples": []}
    assert retriever.calls == [("Rain caused flooding.", 1)]
