"""Build auditable NetworkX views for the KG post-processing demo.

The integrated view keeps the original event/factor structure and adds a
separate canonical-resource layer.  Visual flags are stored as graph
attributes so that rendering remains a presentation concern:

* ``is_cross_example`` marks resources reused by more than one example;
* ``wikipedia_linked`` marks resources with an accepted Wikipedia page;
* NER-created resources remain explicit, but their transient mention records
  are folded into the same resource node rather than drawn twice.
"""

from __future__ import annotations

from html import escape
from typing import Any

import networkx as nx

from src.kg_builder import build_graph


POSTPROCESS_LEGEND_HTML = """
<div class="kg-postprocess-legend" role="note" aria-label="KG visualization legend">
  <strong>Legend</strong>
  <span><i class="legend-box cause"></i>Cause event</span>
  <span><i class="legend-box effect"></i>Effect event</span>
  <span><i class="legend-ellipse canonical"></i>Canonical factor node</span>
  <span><i class="legend-diamond shared"></i>Shared canonical node (across examples)</span>
  <span><i class="legend-ellipse wiki"></i>Wikipedia-linked canonical node</span>
  <span><i class="legend-triangle ner"></i>NER-added canonical node</span>
</div>
""".strip()


def build_postprocess_graphs(
    raw_demo_kgs: dict[int, dict[str, Any]],
    linked_integrated_kg: dict[str, Any],
) -> tuple[dict[int, nx.DiGraph], nx.DiGraph]:
    """Return per-example raw graphs and one integrated post-process graph."""

    if not isinstance(raw_demo_kgs, dict) or not raw_demo_kgs:
        raise ValueError("raw_demo_kgs must be a non-empty dictionary")
    raw_graphs: dict[int, nx.DiGraph] = {}
    for sample_id, kg in raw_demo_kgs.items():
        if not isinstance(sample_id, int) or not isinstance(kg, dict):
            raise ValueError("raw_demo_kgs must map integer sample IDs to KG objects")
        raw_graphs[sample_id] = build_graph(kg)

    integrated_graph = build_integrated_postprocess_graph(linked_integrated_kg)
    return raw_graphs, integrated_graph


def build_integrated_postprocess_graph(
    linked_integrated_kg: dict[str, Any],
) -> nx.DiGraph:
    """Map the full post-processed collection to an inspectable directed graph."""

    if not isinstance(linked_integrated_kg, dict):
        raise TypeError("linked_integrated_kg must be an object")
    sample_graphs = linked_integrated_kg.get("sample_graphs")
    resources = linked_integrated_kg.get("canonical_resources")
    if not isinstance(sample_graphs, list) or not isinstance(resources, list):
        raise ValueError("linked_integrated_kg is missing the sample_graphs or canonical_resources list")

    graph = nx.DiGraph()
    resource_node_ids: dict[str, str] = {}
    for resource in resources:
        if not isinstance(resource, dict):
            raise ValueError("each canonical resource must be an object")
        resource_id = _required_string(resource, "resource_id", "canonical resource")
        if resource_id in resource_node_ids:
            raise ValueError(f"duplicate canonical resource ID: {resource_id}")
        node_id = f"resource:{resource_id}"
        resource_node_ids[resource_id] = node_id
        _add_resource_node(graph, node_id, resource)

    # Each original factor mention resolves directly to its canonical resource
    # node. The mention remains available in provenance, but it is deliberately
    # not rendered as a second node in the integrated KG.
    factor_node_ids: dict[str, str] = {}
    sample_ids: list[int] = []
    for sample_graph in sample_graphs:
        if not isinstance(sample_graph, dict):
            raise ValueError("sample graph must be an object")
        sample_id = sample_graph.get("id")
        if not isinstance(sample_id, int):
            raise ValueError("sample graph is missing an integer ID")
        sample_ids.append(sample_id)
        events = sample_graph.get("events")
        if not isinstance(events, dict):
            raise ValueError(f"sample_id={sample_id} is missing the events object")
        event_roles = _event_role_map(sample_graph)

        for event_id, event in events.items():
            if not isinstance(event_id, str) or not isinstance(event, dict):
                raise ValueError(f"sample_id={sample_id} contains an invalid event")
            event_node_id = _event_node_id(sample_id, event_id)
            span = str(event.get("span", "") or event_id)
            event_role = event_roles.get(event_id, "event")
            graph.add_node(
                event_node_id,
                type="event",
                event_role=event_role,
                label=f"S{sample_id} {event_role.upper()}\n{span}",
                span=span,
                sample_id=sample_id,
                event_id=event_id,
                title=(
                    f"type: event<br>sample: {sample_id}<br>"
                    f"event role: {escape(event_role)}<br>span: {escape(span)}"
                ),
            )
            components = event.get("components")
            if not isinstance(components, list):
                raise ValueError(f"sample_id={sample_id} event={event_id} is missing the components list")
            for index, component in enumerate(components):
                _add_factor_unit(
                    graph,
                    component,
                    parent_node_id=event_node_id,
                    edge_type="has_component",
                    sample_id=sample_id,
                    event_id=event_id,
                    path=f"components[{index}]",
                    node_type="component",
                    resource_node_ids=resource_node_ids,
                    factor_node_ids=factor_node_ids,
                )

        for link in _as_list(sample_graph.get("causal_links")):
            if not isinstance(link, dict):
                raise ValueError(f"sample_id={sample_id} causal link must be an object")
            cause_event = _required_string(link, "cause_event", "causal link")
            effect_event = _required_string(link, "effect_event", "causal link")
            source = _event_node_id(sample_id, cause_event)
            target = _event_node_id(sample_id, effect_event)
            if source not in graph or target not in graph:
                raise ValueError(f"causal link references a missing event: {source} -> {target}")
            graph.add_edge(
                source,
                target,
                type="causal",
                label="Caused",
                relation=str(link.get("relation", "caused")),
                arrows="to",
            )

    _add_ner_mentions(
        graph,
        linked_integrated_kg,
        factor_node_ids=factor_node_ids,
        resource_node_ids=resource_node_ids,
    )

    shared_count = sum(bool(data.get("is_cross_example")) for _, data in graph.nodes(data=True))
    linked_count = sum(bool(data.get("wikipedia_linked")) for _, data in graph.nodes(data=True))
    graph.graph.update(
        {
            "collection_id": linked_integrated_kg.get("collection_id"),
            "sample_ids": sample_ids,
            "view": "postprocess_integrated",
            "shared_resource_count": shared_count,
            "wikipedia_linked_resource_count": linked_count,
        }
    )
    return graph


def _add_resource_node(
    graph: nx.DiGraph,
    node_id: str,
    resource: dict[str, Any],
) -> None:
    label = _required_string(resource, "preferred_label", "canonical resource")
    sample_count = int(resource.get("sample_count", 0) or 0)
    mention_count = int(resource.get("mention_count", 0) or 0)
    is_cross_example = sample_count > 1
    is_deduplicated = mention_count > 1

    wikipedia_link = resource.get("wikipedia_link")
    if not isinstance(wikipedia_link, dict):
        wikipedia_link = {}
    wikipedia_status = str(wikipedia_link.get("status", "not_checked"))
    selected_page = wikipedia_link.get("selected_page")
    if not isinstance(selected_page, dict):
        selected_page = {}
    wikipedia_linked = wikipedia_status == "linked" and bool(selected_page.get("url"))

    tags: list[str] = []
    if is_cross_example:
        tags.append("SHARED")
    elif is_deduplicated:
        tags.append("DEDUP")
    if wikipedia_linked:
        tags.append("WIKI")
    display_label = f"[{' + '.join(tags)}]\n{label}" if tags else label

    surfaces = ", ".join(str(item) for item in _as_list(resource.get("surface_forms")))
    sample_ids = ", ".join(str(item) for item in _as_list(resource.get("sample_ids")))
    title_lines = [
        "type: canonical resource",
        f"preferred label: {escape(label)}",
        f"surface forms: {escape(surfaces or label)}",
        f"mentions: {mention_count}",
        f"samples: {escape(sample_ids or '-')}",
        f"Wikipedia status: {escape(wikipedia_status)}",
    ]
    if wikipedia_linked:
        title_lines.extend(
            [
                f"Wikipedia title: {escape(str(selected_page.get('title', '')))}",
                f"Wikipedia URL: {escape(str(selected_page.get('url', '')))}",
            ]
        )
    graph.add_node(
        node_id,
        type="canonical_resource",
        label=display_label,
        canonical_key=resource.get("canonical_key"),
        preferred_label=label,
        mention_count=mention_count,
        sample_count=sample_count,
        is_deduplicated=is_deduplicated,
        is_cross_example=is_cross_example,
        is_ner_created=resource.get("origin") == "postprocess_ner",
        wikipedia_status=wikipedia_status,
        wikipedia_linked=wikipedia_linked,
        wikipedia_title=selected_page.get("title"),
        wikipedia_url=selected_page.get("url"),
        title="<br>".join(title_lines),
    )


def _add_factor_unit(
    graph: nx.DiGraph,
    unit: Any,
    *,
    parent_node_id: str,
    edge_type: str,
    sample_id: int,
    event_id: str,
    path: str,
    node_type: str,
    resource_node_ids: dict[str, str],
    factor_node_ids: dict[str, str],
) -> None:
    if not isinstance(unit, dict):
        raise ValueError(f"sample_id={sample_id} event={event_id} {path} must be an object")
    mention_id = _required_string(unit, "mention_id", path)
    role = _required_string(unit, "role", path)
    value = _required_string(unit, "value", path)
    resource_id = _required_string(unit, "collection_resource_id", path)
    if mention_id in factor_node_ids:
        raise ValueError(f"duplicate factor mention_id: {mention_id}")
    resource_node_id = resource_node_ids.get(resource_id)
    if resource_node_id is None:
        raise ValueError(f"{path} references a missing collection resource: {resource_id}")

    node_id = resource_node_id
    factor_node_ids[mention_id] = node_id
    ner_annotations = unit.get("ner_annotations")
    if not isinstance(ner_annotations, list):
        ner_annotations = []
    ner_labels = sorted(
        {
            str(annotation.get("ner_label"))
            for annotation in ner_annotations
            if isinstance(annotation, dict) and annotation.get("ner_label")
        }
    )
    resource_data = graph.nodes[node_id]
    _append_unique(resource_data, "observed_roles", role)
    _append_unique(resource_data, "observed_values", value)
    for ner_label in ner_labels:
        _append_unique(resource_data, "ner_labels", ner_label)
    if ner_labels:
        resource_data["title"] += f"<br>NER evidence: {escape(', '.join(ner_labels))}"

    provenance = {
        "sample_id": sample_id,
        "event_id": event_id,
        "path": path,
        "mention_id": mention_id,
        "role": role,
        "value": value,
    }
    if parent_node_id == node_id:
        # Collapsing a wrapper and its exact canonical child can otherwise
        # create a meaningless self-loop. Retain the occurrence for auditing.
        resource_data.setdefault("collapsed_self_relations", []).append(
            {"edge_type": edge_type, **provenance}
        )
    else:
        _add_or_merge_edge(
            graph,
            parent_node_id,
            node_id,
            edge_type=edge_type,
            role=role,
            provenance=provenance,
        )

    for index, attribute in enumerate(_as_list(unit.get("attributes"))):
        _add_factor_unit(
            graph,
            attribute,
            parent_node_id=node_id,
            edge_type="has_attribute",
            sample_id=sample_id,
            event_id=event_id,
            path=f"{path}.attributes[{index}]",
            node_type="attribute",
            resource_node_ids=resource_node_ids,
            factor_node_ids=factor_node_ids,
        )
    for index, child in enumerate(_as_list(unit.get("children"))):
        _add_factor_unit(
            graph,
            child,
            parent_node_id=node_id,
            edge_type="has_child",
            sample_id=sample_id,
            event_id=event_id,
            path=f"{path}.children[{index}]",
            node_type="component",
            resource_node_ids=resource_node_ids,
            factor_node_ids=factor_node_ids,
        )


def _add_ner_mentions(
    graph: nx.DiGraph,
    integrated_kg: dict[str, Any],
    *,
    factor_node_ids: dict[str, str],
    resource_node_ids: dict[str, str],
) -> None:
    mentions = integrated_kg.get("ner_mentions", [])
    edges = integrated_kg.get("ner_edges", [])
    if not isinstance(mentions, list) or not isinstance(edges, list):
        raise ValueError("ner_mentions and ner_edges must be lists")

    ner_node_ids: dict[str, str] = {}
    for mention in mentions:
        if not isinstance(mention, dict):
            raise ValueError("NER mention must be an object")
        mention_id = _required_string(mention, "ner_mention_id", "NER mention")
        value = _required_string(mention, "value", "NER mention")
        ner_label = _required_string(mention, "ner_label", "NER mention")
        resource_id = _required_string(mention, "collection_resource_id", "NER mention")
        resource_node_id = resource_node_ids.get(resource_id)
        if resource_node_id is None:
            raise ValueError(f"NER mention references a missing resource: {resource_id}")
        # The NER mention is provenance for the canonical node, not an extra KG
        # node. This keeps one visible node per resolved canonical resource.
        node_id = resource_node_id
        ner_node_ids[mention_id] = node_id
        resource_data = graph.nodes[node_id]
        resource_data["is_ner_created"] = True
        _append_unique(resource_data, "ner_labels", ner_label)
        resource_data["title"] += (
            f"<br>NER-added surface: {escape(value)}"
            f"<br>NER type: {escape(ner_label)}"
        )

    for edge in edges:
        if not isinstance(edge, dict):
            raise ValueError("NER edge must be an object")
        source_mention_id = _required_string(edge, "source_factor_mention_id", "NER edge")
        target_mention_id = _required_string(edge, "target_ner_mention_id", "NER edge")
        source = factor_node_ids.get(source_mention_id)
        target = ner_node_ids.get(target_mention_id)
        if source is None or target is None:
            raise ValueError("NER edge references a missing factor or NER mention")
        if source == target:
            graph.nodes[target].setdefault("collapsed_ner_relations", []).append(
                {"source_factor_mention_id": source_mention_id, "target_ner_mention_id": target_mention_id}
            )
        else:
            _add_or_merge_edge(
                graph,
                source,
                target,
                edge_type="has_ner_mention",
                role=str(edge.get("relation", "has_ner_mention")),
                provenance={
                    "source_factor_mention_id": source_mention_id,
                    "target_ner_mention_id": target_mention_id,
                },
            )


def _add_or_merge_edge(
    graph: nx.DiGraph,
    source: str,
    target: str,
    *,
    edge_type: str,
    role: str,
    provenance: dict[str, Any],
) -> None:
    """Add one semantic edge and aggregate duplicate mention occurrences."""

    if graph.has_edge(source, target):
        data = graph.edges[source, target]
        data.setdefault("provenance", []).append(provenance)
        data["occurrence_count"] = len(data["provenance"])
        _append_unique(data, "roles", role)
        data["label"] = " / ".join(data["roles"])
        return
    graph.add_edge(
        source,
        target,
        type=edge_type,
        label=role,
        role=role,
        roles=[role],
        provenance=[provenance],
        occurrence_count=1,
        arrows="to",
    )


def _append_unique(record: dict[str, Any], field: str, value: str) -> None:
    values = record.setdefault(field, [])
    if value not in values:
        values.append(value)


def _event_role_map(sample_graph: dict[str, Any]) -> dict[str, str]:
    role_sets: dict[str, set[str]] = {}
    for link in _as_list(sample_graph.get("causal_links")):
        if not isinstance(link, dict):
            continue
        for field, role in (("cause_event", "cause"), ("effect_event", "effect")):
            event_id = link.get(field)
            if isinstance(event_id, str) and event_id:
                role_sets.setdefault(event_id, set()).add(role)
    return {
        event_id: "both" if len(roles) > 1 else next(iter(roles))
        for event_id, roles in role_sets.items()
    }


def _event_node_id(sample_id: int, event_id: str) -> str:
    return f"sample:{sample_id}:event:{event_id}"


def _required_string(record: dict[str, Any], field: str, context: str) -> str:
    value = record.get(field)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{context} is missing {field}")
    return value


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []
