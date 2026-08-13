"""SPEC_07：将 SPEC_06 KG JSON 映射为 NetworkX 有向图。"""

from __future__ import annotations

from typing import Any

import networkx as nx


def build_graph(kg_json: dict[str, Any]) -> nx.DiGraph:
    """按 Event → Component → Attribute 与 causal links 构建有向图。"""
    graph = nx.DiGraph()
    events = kg_json.get("events", {})
    if not isinstance(events, dict):
        raise ValueError("kg_json.events 必须是 dict")

    event_roles = _collect_event_roles(kg_json.get("causal_links", []))
    for event_id, event in events.items():
        _add_event_node(graph, str(event_id), event, event_roles.get(str(event_id), "event"))
        _add_component_nodes(graph, str(event_id), event)

    for link in _as_list(kg_json.get("causal_links")):
        cause_event = str(link.get("cause_event", ""))
        effect_event = str(link.get("effect_event", ""))
        if cause_event not in graph or effect_event not in graph:
            raise ValueError(f"causal_link 引用了不存在的 event：{cause_event} -> {effect_event}")
        graph.add_edge(
            cause_event,
            effect_event,
            label="Caused",
            type="causal",
            relation=str(link.get("relation", "caused")),
            triple_index=link.get("triple_index"),
            color="#d94841",
            width=4,
            arrows="to",
        )

    graph.graph["sample_id"] = kg_json.get("id")
    graph.graph["text"] = kg_json.get("text", "")
    graph.graph["triple_source"] = kg_json.get("triple_source", "")
    return graph


def _add_event_node(graph: nx.DiGraph, event_id: str, event: Any, event_role: str) -> None:
    if not isinstance(event, dict):
        event = {}
    span = str(event.get("span", ""))
    graph.add_node(
        event_id,
        type="event",
        event_role=event_role,
        label=span or event_id,
        span=span,
        title=_node_title("event", event_role, span or event_id),
    )


def _add_component_nodes(graph: nx.DiGraph, event_id: str, event: Any) -> None:
    components = _as_list(event.get("components") if isinstance(event, dict) else [])
    for component_index, component in enumerate(components):
        if not isinstance(component, dict):
            continue
        component_role = str(component.get("role", "")).strip() or "Component"
        component_value = str(component.get("value", "")).strip()
        if not component_value:
            continue
        component_id = f"{event_id}/component_{component_index}"
        component_subtype = "action" if component_role.lower() == "action" else "component"
        graph.add_node(
            component_id,
            type="component",
            subtype=component_subtype,
            role=component_role,
            label=component_value,
            value=component_value,
            title=_node_title(component_subtype, component_role, component_value),
        )
        graph.add_edge(
            event_id,
            component_id,
            label=component_role,
            type="has_component",
            role=component_role,
            arrows="to",
        )
        _add_attribute_nodes(graph, component_id, component)
        _add_child_nodes(graph, component_id, component)


def _add_attribute_nodes(graph: nx.DiGraph, component_id: str, component: dict[str, Any]) -> None:
    for attribute_index, attribute in enumerate(_as_list(component.get("attributes"))):
        if not isinstance(attribute, dict):
            continue
        attribute_role = str(attribute.get("role", "")).strip() or "Attribute"
        attribute_value = str(attribute.get("value", "")).strip()
        if not attribute_value:
            continue
        attribute_id = f"{component_id}/attribute_{attribute_index}"
        graph.add_node(
            attribute_id,
            type="attribute",
            role=attribute_role,
            label=attribute_value,
            value=attribute_value,
            title=_node_title("attribute", attribute_role, attribute_value),
        )
        graph.add_edge(
            component_id,
            attribute_id,
            label=attribute_role,
            type="has_attribute",
            role=attribute_role,
            arrows="to",
        )


def _add_child_nodes(graph: nx.DiGraph, parent_id: str, component: dict[str, Any]) -> None:
    for child_index, child in enumerate(_as_list(component.get("children"))):
        if not isinstance(child, dict):
            continue
        child_role = str(child.get("role", "")).strip() or "Component"
        child_value = str(child.get("value", "")).strip()
        if not child_value:
            continue
        child_id = f"{parent_id}/child_{child_index}"
        child_subtype = "action" if child_role.lower() == "action" else "component"
        graph.add_node(
            child_id,
            type="component",
            subtype=child_subtype,
            role=child_role,
            label=child_value,
            value=child_value,
            title=_node_title(child_subtype, child_role, child_value),
        )
        graph.add_edge(
            parent_id,
            child_id,
            label=child_role,
            type="has_child",
            role=child_role,
            arrows="to",
        )
        _add_attribute_nodes(graph, child_id, child)
        _add_child_nodes(graph, child_id, child)


def _collect_event_roles(causal_links: Any) -> dict[str, str]:
    role_sets: dict[str, set[str]] = {}
    for link in _as_list(causal_links):
        if not isinstance(link, dict):
            continue
        cause_event = str(link.get("cause_event", ""))
        effect_event = str(link.get("effect_event", ""))
        if cause_event:
            role_sets.setdefault(cause_event, set()).add("cause")
        if effect_event:
            role_sets.setdefault(effect_event, set()).add("effect")

    roles = {}
    for event_id, values in role_sets.items():
        roles[event_id] = "both" if len(values) > 1 else next(iter(values))
    return roles


def _node_title(node_type: str, role: str, value: str) -> str:
    return f"type: {node_type}<br>role: {role}<br>value: {value}"


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []
