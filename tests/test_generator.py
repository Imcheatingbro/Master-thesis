"""SPEC_04：Generator 输出解析与重试逻辑的单元测试。"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.generator import (
    DUPLICATE_EFFECT_CLOSING_BRACE_REPAIR,
    generate,
    parse_output,
    parse_output_with_metadata,
    validate_minimal,
)
from src.llm_client import LLMEmptyContentError


class FakeClient:
    """按顺序返回预设输出或抛出异常的测试客户端。"""

    def __init__(self, outputs: list[str | Exception]) -> None:
        self.outputs = outputs
        self.calls = 0
        self.messages: list[list[dict[str, str]]] = []

    def chat(self, messages: list[dict[str, str]]) -> str:
        self.calls += 1
        self.messages.append(messages)
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


def test_parse_output_repairs_duplicate_effect_closing_brace() -> None:
    raw = """```json
{
  "has_causal": true,
  "triples": [
    {
      "cause": {"span": "Rain"},
      "relation": "caused",
      "effect": {"span": "flooding"}}
    }
  ]
}
```"""

    parsed, repair_type = parse_output_with_metadata(raw)

    assert parsed["triples"][0]["effect"]["span"] == "flooding"
    assert repair_type == DUPLICATE_EFFECT_CLOSING_BRACE_REPAIR


def test_parse_output_does_not_repair_unrelated_json_error() -> None:
    raw = """```json
{
  "has_causal": true,
  "triples": [
    {
      "cause": {"span": "Rain"}}
      "relation": "caused",
      "effect": {"span": "flooding"}
    }
  ]
}
```"""

    with pytest.raises(ValueError):
        parse_output(raw)


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


def test_generate_accepts_non_substring_span_for_evaluator_to_score() -> None:
    client = FakeClient(
        [
            (
                '{"has_causal": true, "triples": ['
                '{"cause": {"span": "jail authorities failed to arrange escort"}, '
                '"relation": "caused", '
                '"effect": {"span": "Anoop George ... could not be produced"}}]}'
            ),
        ]
    )

    result = generate(
        text="Anoop George could not be produced after jail authorities failed to arrange escort.",
        sample_id=15,
        client=client,
        retriever=None,
        use_rag=False,
        top_k=0,
        max_retry=2,
    )

    assert client.calls == 1
    assert result["id"] == 15
    assert result["has_causal"] is True
    assert result["triples"][0]["effect"]["span"] == "Anoop George ... could not be produced"


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
    assert result["id"] is None
    assert result["has_causal"] is False
    assert result["triples"] == []
    assert result["error_type"] == "unknown_generation_error"
    assert result["error_message"] == "坏输出"
    assert result["generation_attempts"] == [
        {
            "attempt": 1,
            "raw_output": "not json",
            "error_type": "no_json_object",
            "error_message": "未找到 JSON 对象",
        },
        {
            "attempt": 2,
            "raw_output": None,
            "error_type": "unknown_generation_error",
            "error_message": "坏输出",
        },
    ]


def test_generate_preserves_every_invalid_json_output() -> None:
    first_output = '{"has_causal": true "triples": []}'
    second_output = '{"has_causal": true, "triples": [}'
    client = FakeClient([first_output, second_output])

    result = generate(
        text="Rain caused flooding.",
        sample_id=21,
        client=client,
        retriever=None,
        use_rag=False,
        top_k=0,
        max_retry=2,
    )

    assert result["error_type"] == "invalid_json_syntax"
    assert [row["raw_output"] for row in result["generation_attempts"]] == [first_output, second_output]
    assert [row["attempt"] for row in result["generation_attempts"]] == [1, 2]


def test_generate_records_successful_limited_parse_repair() -> None:
    raw = """```json
{
  "has_causal": true,
  "triples": [
    {
      "cause": {"span": "Rain"},
      "relation": "caused",
      "effect": {"span": "flooding"}}
    }
  ]
}
```"""
    client = FakeClient([raw])

    result = generate(
        text="Rain caused flooding.",
        sample_id=22,
        client=client,
        retriever=None,
        use_rag=False,
        top_k=0,
        max_retry=2,
    )

    assert client.calls == 1
    assert result["has_causal"] is True
    assert result["parse_repair_type"] == DUPLICATE_EFFECT_CLOSING_BRACE_REPAIR
    assert result["parse_repair_raw_output"] == raw


def test_generate_classifies_reasoning_only_empty_content() -> None:
    client = FakeClient([LLMEmptyContentError("模型只返回 reasoning_content，content 为空")])

    result = generate(
        text="Difficult sample.",
        sample_id=8,
        client=client,
        retriever=None,
        use_rag=False,
        top_k=0,
        max_retry=2,
    )

    assert client.calls == 1
    assert result["error_type"] == "llm_reasoning_only_empty_content"
    assert "reasoning_content" in result["error_message"]


def test_generate_classifies_missing_json_object() -> None:
    client = FakeClient(["not json"])

    result = generate(
        text="Difficult sample.",
        sample_id=9,
        client=client,
        retriever=None,
        use_rag=False,
        top_k=0,
        max_retry=1,
    )

    assert result["error_type"] == "no_json_object"
    assert "JSON" in result["error_message"]


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


def test_generate_accepts_prompt_name() -> None:
    client = FakeClient(['{"has_causal": false, "triples": []}'])

    result = generate(
        text="The talks collapsed when the offer was rejected.",
        sample_id=4,
        client=client,
        retriever=None,
        use_rag=False,
        top_k=0,
        prompt_name="v1",
        max_retry=1,
    )

    assert result == {"id": 4, "has_causal": False, "triples": []}
    assert "triggers, enables, or explains the main event" in client.messages[0][0]["content"]
