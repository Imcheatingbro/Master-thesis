"""SPEC_07：KG JSON 到 NetworkX 图映射的单元测试。"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.kg_builder import build_graph


def test_build_graph_maps_events_components_attributes_and_causal_edge() -> None:
    graph = build_graph(_sample_kg_json())

    assert graph.number_of_nodes() == 11
    assert graph.number_of_edges() == 10

    assert graph.nodes["triple_0_cause"]["type"] == "event"
    assert graph.nodes["triple_0_cause"]["event_role"] == "cause"
    assert graph.nodes["triple_0_effect"]["event_role"] == "effect"

    action_node = "triple_0_cause/component_0"
    theme_node = "triple_0_effect/component_1"
    attribute_node = "triple_0_effect/component_1/attribute_0"

    assert graph.nodes[action_node]["type"] == "component"
    assert graph.nodes[action_node]["subtype"] == "action"
    assert graph.nodes[action_node]["label"] == "bombards"
    assert graph.nodes[theme_node]["label"] == "troops"
    assert graph.nodes[attribute_node]["type"] == "attribute"
    assert graph.nodes[attribute_node]["label"] == "5"

    assert graph.edges["triple_0_cause", "triple_0_effect"]["label"] == "Caused"
    assert graph.edges["triple_0_cause", action_node]["label"] == "Action"
    assert graph.edges[theme_node, attribute_node]["label"] == "Quantifier"


def test_build_graph_keeps_same_surface_span_as_separate_event_nodes() -> None:
    kg_json = _sample_kg_json()
    kg_json["events"]["triple_1_cause"] = {
        "span": "strong wind",
        "components": [{"role": "Theme", "value": "wind", "attributes": [{"role": "Attribute", "value": "strong"}]}],
    }
    kg_json["events"]["triple_1_effect"] = {
        "span": "5 Afghan troops killed",
        "components": [{"role": "Theme", "value": "troops", "attributes": []}],
    }
    kg_json["causal_links"].append(
        {
            "relation": "caused",
            "cause_event": "triple_1_cause",
            "effect_event": "triple_1_effect",
            "triple_index": 1,
        }
    )

    graph = build_graph(kg_json)

    assert "triple_0_effect" in graph
    assert "triple_1_effect" in graph
    assert graph.nodes["triple_0_effect"]["label"] == graph.nodes["triple_1_effect"]["label"]
    assert graph.number_of_edges() == 14


def test_build_graph_rejects_causal_link_to_missing_event() -> None:
    kg_json = _sample_kg_json()
    kg_json["causal_links"][0]["effect_event"] = "missing_event"

    with pytest.raises(ValueError, match="不存在"):
        build_graph(kg_json)


def test_build_graph_maps_nested_children_recursively_without_changing_two_layer_counts() -> None:
    kg_json = _sample_kg_json()
    kg_json["events"]["triple_0_effect"]["components"][1]["children"] = [
        {
            "role": "Description",
            "value": "visiting engineer",
            "attributes": [{"role": "Modifier", "value": "visiting"}],
            "children": [
                {
                    "role": "Case",
                    "value": "inspection",
                    "attributes": [],
                    "children": [{"role": "Location", "value": "Kabul", "attributes": []}],
                }
            ],
        }
    ]

    graph = build_graph(kg_json)

    child_node = "triple_0_effect/component_1/child_0"
    child_attribute = "triple_0_effect/component_1/child_0/attribute_0"
    grandchild_node = "triple_0_effect/component_1/child_0/child_0"
    great_grandchild_node = "triple_0_effect/component_1/child_0/child_0/child_0"

    assert graph.number_of_nodes() == 15
    assert graph.number_of_edges() == 14
    assert graph.nodes[child_node]["type"] == "component"
    assert graph.nodes[child_node]["role"] == "Description"
    assert graph.nodes[child_node]["label"] == "visiting engineer"
    assert graph.nodes[child_attribute]["type"] == "attribute"
    assert graph.nodes[grandchild_node]["label"] == "inspection"
    assert graph.nodes[great_grandchild_node]["role"] == "Location"
    assert graph.edges["triple_0_effect/component_1", child_node]["type"] == "has_child"
    assert graph.edges["triple_0_effect/component_1", child_node]["label"] == "Description"
    assert graph.edges[grandchild_node, great_grandchild_node]["label"] == "Location"


def _sample_kg_json() -> dict:
    return {
        "id": None,
        "text": "5 Afghan troops killed after US army bombards warehouse in Kabul",
        "triple_source": "manual",
        "causal_links": [
            {
                "relation": "caused",
                "cause_event": "triple_0_cause",
                "effect_event": "triple_0_effect",
                "triple_index": 0,
            }
        ],
        "events": {
            "triple_0_cause": {
                "span": "US army bombards warehouse in Kabul",
                "components": [
                    {"role": "Action", "value": "bombards", "attributes": []},
                    {"role": "Actor", "value": "army", "attributes": [{"role": "Nationality", "value": "US"}]},
                    {"role": "Theme", "value": "warehouse", "attributes": []},
                    {"role": "Location", "value": "Kabul", "attributes": []},
                ],
            },
            "triple_0_effect": {
                "span": "5 Afghan troops killed",
                "components": [
                    {"role": "Action", "value": "killed", "attributes": []},
                    {
                        "role": "Theme",
                        "value": "troops",
                        "attributes": [
                            {"role": "Quantifier", "value": "5"},
                            {"role": "Attribute", "value": "Afghan"},
                        ],
                    },
                ],
            },
        },
    }
