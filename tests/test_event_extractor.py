"""SPEC_06：Event 分层结构提取与 KG JSON 组装的单元测试。"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.event_extractor import (
    PROMPT_DIR,
    _build_event_messages,
    build_kg_json,
    build_nuextract_depth2_template,
    extract_event,
    parse_event_output,
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


def test_parse_event_output_accepts_plain_json() -> None:
    result = parse_event_output(
        '{"components": [{"role": "Action", "value": "killed", "attributes": []}]}'
    )

    assert result == {"components": [{"role": "Action", "value": "killed", "attributes": []}]}


def test_parse_event_output_accepts_markdown_and_prefix_text() -> None:
    raw = """
Here is the result:
```json
{
  "components": [
    {
      "role": "Theme",
      "value": "rain",
      "attributes": [
        {"role": "Attribute", "value": "heavy"}
      ]
    }
  ]
}
```
"""

    result = parse_event_output(raw)

    assert result["components"][0]["value"] == "rain"
    assert result["components"][0]["attributes"] == [{"role": "Attribute", "value": "heavy"}]


def test_parse_event_output_rejects_missing_components() -> None:
    try:
        parse_event_output('{"items": []}')
    except ValueError as exc:
        assert "components" in str(exc)
    else:
        raise AssertionError("parse_event_output 应拒绝缺少 components 的输出")


def test_parse_event_output_preserves_nested_children() -> None:
    result = parse_event_output(
        """
{
  "components": [
    {
      "role": "Theme",
      "value": "Daniel Rao",
      "children": [
        {
          "role": "Description",
          "value": "the visiting engineer",
          "children": [
            {"role": "Case", "value": "the case", "children": []}
          ]
        }
      ]
    }
  ]
}
"""
    )

    assert result["components"][0]["children"][0]["role"] == "Description"
    assert result["components"][0]["children"][0]["children"][0]["value"] == "the case"


def test_parse_event_output_drops_nuextract_null_values() -> None:
    result = parse_event_output(
        """
{
  "components": [
    {
      "role": "Actor",
      "value": "Afghan troops",
      "attributes": [
        {"role": "Nationality", "value": "Afghan"},
        {"role": "Age", "value": null}
      ]
    },
    {
      "role": "Object",
      "value": null,
      "attributes": [
        {"role": "Quantifier", "value": "5"}
      ]
    }
  ]
}
"""
    )

    assert result == {
        "components": [
            {
                "role": "Actor",
                "value": "Afghan troops",
                "attributes": [{"role": "Nationality", "value": "Afghan"}],
            }
        ]
    }


def test_extract_event_filters_values_not_contained_in_span_but_allows_substrings() -> None:
    client = FakeClient(
        [
            """
{
  "components": [
    {
      "role": "Theme",
      "value": "apple",
      "attributes": [
        {"role": "Attribute", "value": "red"},
        {"role": "Attribute", "value": "green"}
      ]
    },
    {
      "role": "Action",
      "value": "fall",
      "attributes": []
    }
  ]
}
"""
        ]
    )

    event = extract_event("green apples", role="cause", client=client, max_retry=1)

    assert event["span"] == "green apples"
    assert event["components"] == [
        {
            "role": "Theme",
            "value": "apple",
            "attributes": [{"role": "Attribute", "value": "green"}],
        }
    ]
    assert event["warnings"] == [
        {"type": "attribute_value_not_in_span", "role": "Attribute", "value": "red"},
        {"type": "component_value_not_in_span", "role": "Action", "value": "fall"},
    ]


def test_extract_event_filters_nested_children_not_contained_in_span() -> None:
    client = FakeClient(
        [
            """
{
  "components": [
    {
      "role": "Theme",
      "value": "Daniel Rao",
      "children": [
        {"role": "Description", "value": "visiting engineer", "children": []},
        {"role": "Case", "value": "missing case", "children": []}
      ]
    }
  ]
}
"""
        ]
    )

    event = extract_event("Daniel Rao visiting engineer", role="effect", client=client, max_retry=1)

    assert event["components"][0]["children"] == [
        {"role": "Description", "value": "visiting engineer", "attributes": []}
    ]
    assert event["warnings"] == [
        {"type": "component_value_not_in_span", "role": "Case", "value": "missing case"}
    ]


def test_build_kg_json_puts_multiple_triples_into_one_sample_graph_json() -> None:
    client = FakeClient(
        [
            _event_json("Theme", "rain"),
            _event_json("Theme", "flooding"),
            _event_json("Theme", "wind"),
            _event_json("Theme", "damage"),
        ]
    )
    triples = [
        {"cause": {"span": "rain"}, "relation": "caused", "effect": {"span": "flooding"}},
        {"cause": "wind", "effect": "damage"},
    ]

    kg_json = build_kg_json(
        sample_id=12,
        text="rain caused flooding and wind caused damage.",
        triples=triples,
        client=client,
        triple_source="pred",
        max_retry=1,
    )

    assert client.calls == 4
    assert kg_json["id"] == 12
    assert kg_json["text"] == "rain caused flooding and wind caused damage."
    assert kg_json["triple_source"] == "pred"
    assert kg_json["causal_links"] == [
        {
            "relation": "caused",
            "cause_event": "triple_0_cause",
            "effect_event": "triple_0_effect",
            "triple_index": 0,
        },
        {
            "relation": "caused",
            "cause_event": "triple_1_cause",
            "effect_event": "triple_1_effect",
            "triple_index": 1,
        },
    ]
    assert set(kg_json["events"]) == {
        "triple_0_cause",
        "triple_0_effect",
        "triple_1_cause",
        "triple_1_effect",
    }


def test_build_kg_json_handles_samples_without_causal_triples() -> None:
    client = FakeClient([])

    kg_json = build_kg_json(
        sample_id=2,
        text="No causal relation here.",
        triples=[],
        client=client,
        triple_source="gold",
        max_retry=1,
    )

    assert client.calls == 0
    assert kg_json == {
        "id": 2,
        "text": "No causal relation here.",
        "triple_source": "gold",
        "causal_links": [],
        "events": {},
    }


def test_extract_event_returns_fallback_on_reasoning_only_error() -> None:
    client = FakeClient([LLMEmptyContentError("模型只返回 reasoning_content，content 为空")])

    event = extract_event("hard span", role="effect", client=client, max_retry=2)

    assert client.calls == 1
    assert event["span"] == "hard span"
    assert event["components"] == []
    assert event["error_type"] == "llm_reasoning_only_empty_content"
    assert "reasoning_content" in event["error_message"]


def test_event_prompt_v2_guides_content_attribute_without_nested_events() -> None:
    prompt = (PROMPT_DIR / "event_extraction_v2.txt").read_text(encoding="utf-8")

    assert "Content" in prompt
    assert "Topic" in prompt
    assert "Description" in prompt
    assert "which included" in prompt
    assert "Do not recursively decompose the content into nested events" in prompt
    assert "Report about the workshop" in prompt
    assert '"role": "Topic", "value": "about the workshop"' in prompt
    assert "which included a keynote talk , two poster sessions , and a panel discussion with students" in prompt
    assert "Footage of the attack" not in prompt
    assert '"role": "Content"' in prompt


def test_event_prompt_v3_keeps_pre_content_behavior_for_demo_comparison() -> None:
    prompt = (PROMPT_DIR / "event_extraction_v3.txt").read_text(encoding="utf-8")

    assert "Do not extract causality in this stage." in prompt
    assert 'Never output a component with role "Cause" or "Effect".' in prompt
    assert "their demands were not met" in prompt
    assert "Report about the workshop" not in prompt
    assert "which included" not in prompt
    assert "Content" not in prompt


def test_nuextract_depth2_template_matches_v2_two_layer_schema() -> None:
    template = build_nuextract_depth2_template()

    component_template = template["components"][0]
    attribute_template = component_template["attributes"][0]
    assert set(template) == {"components"}
    assert component_template["value"] == "verbatim-string"
    assert attribute_template["value"] == "verbatim-string"
    assert isinstance(component_template["role"], list)
    assert isinstance(attribute_template["role"], list)
    assert "Action" in component_template["role"]
    assert "Theme" in component_template["role"]
    assert "Negation" in attribute_template["role"]
    assert "children" not in component_template


def test_nuextract_v2_messages_embed_template_and_span_context() -> None:
    messages = _build_event_messages(
        span="5 Afghan troops killed",
        role="cause",
        prompt_version="nuextract_v2",
    )

    assert len(messages) == 1
    assert messages[0]["role"] == "user"
    content = messages[0]["content"]
    assert content.startswith("# Template:\n")
    assert "\n# Context:\n5 Afghan troops killed" in content
    assert '"components"' in content
    assert '"attributes"' in content
    assert '"verbatim-string"' in content
    assert "Role: cause" not in content


def test_event_prompt_nested_v1_directly_generates_nested_event_structure() -> None:
    prompt = (PROMPT_DIR / "event_extraction_nested_v1.txt").read_text(encoding="utf-8")

    assert "nested event structure extraction system" in prompt
    assert "This is not a second-stage enrichment prompt" in prompt
    assert '"components"' in prompt
    assert '"children"' in prompt
    assert '"nodes"' not in prompt
    assert '"edges"' not in prompt
    assert "continuous original substring" in prompt
    assert "Do not extract or revise the outer causal relation" in prompt
    assert "Prefer minimal head values for ordinary nodes" in prompt
    assert "Attach attributes and children to the nearest semantic parent" in prompt
    assert 'use `value`: "troops" with Quantifier "5"' in prompt
    assert "Daniel Rao" in prompt
    assert "the visiting engineer" in prompt
    assert "the case" in prompt
    assert "the office" in prompt
    assert "the northern rail depot" in prompt


def _event_json(role: str, value: str) -> str:
    return (
        '{"components": ['
        f'{{"role": "{role}", "value": "{value}", "attributes": []}}'
        "]}"
    )
