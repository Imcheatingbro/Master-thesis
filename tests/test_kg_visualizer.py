"""SPEC_07：pyvis 可视化输出的单元测试。"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.kg_visualizer import _prepare_pyvis_graph, visualize


def test_visualize_writes_utf8_html(tmp_path: Path) -> None:
    graph = nx.DiGraph()
    graph.add_node("cause", type="event", event_role="cause", label="rain", title="cause event")
    graph.add_node("effect", type="event", event_role="effect", label="flooding", title="effect event")
    graph.add_edge("cause", "effect", type="causal", label="Caused")

    output_path = Path(visualize(graph, str(tmp_path / "kg.html")))
    html = output_path.read_text(encoding="utf-8")

    assert output_path.exists()
    assert "rain" in html
    assert "flooding" in html
    assert "vis-network" in html or "vis.js" in html


def test_prepare_pyvis_graph_keeps_action_label_visible_without_reserved_value() -> None:
    graph = nx.DiGraph()
    graph.add_node(
        "effect/action",
        type="component",
        subtype="action",
        label="hacked",
        value="hacked",
        title="type: action<br>role: Action<br>value: hacked",
    )

    styled_graph = _prepare_pyvis_graph(graph)
    action_node = styled_graph.nodes["effect/action"]

    assert action_node["label"] == "hacked"
    assert action_node["shape"] == "box"
    assert action_node["kg_value"] == "hacked"
    assert "value" not in action_node
    assert action_node["font"]["size"] == 14


def test_action_component_uses_same_visual_style_as_other_components() -> None:
    graph = nx.DiGraph()
    graph.add_node("event/action", type="component", subtype="action", label="hacked")
    graph.add_node("event/theme", type="component", subtype="component", label="Chale")

    styled_graph = _prepare_pyvis_graph(graph)
    action_node = styled_graph.nodes["event/action"]
    theme_node = styled_graph.nodes["event/theme"]

    assert action_node["shape"] == theme_node["shape"] == "box"
    assert action_node["color"] == theme_node["color"]
    assert action_node["font"] == theme_node["font"]
    assert "borderWidth" not in action_node


def test_event_node_uses_wrapped_box_label_for_long_span() -> None:
    graph = nx.DiGraph()
    span = "they hacked Sabata Petros Chale , 39 , to death in Marikana West , on December 8 , 2016"
    graph.add_node("event", type="event", event_role="effect", label=span, title="effect event")

    styled_graph = _prepare_pyvis_graph(graph)
    event_node = styled_graph.nodes["event"]

    assert event_node["shape"] == "box"
    assert "\n" in event_node["label"]
    assert event_node["title"] == "effect event"


def test_visualize_uses_free_layout_then_freezes_physics(tmp_path: Path) -> None:
    graph = nx.DiGraph()
    graph.add_node("cause", type="event", event_role="cause", label="rain")
    graph.add_node("effect", type="event", event_role="effect", label="flooding")
    graph.add_edge("cause", "effect", type="causal", label="Caused")

    output_path = Path(visualize(graph, str(tmp_path / "kg.html")))
    html = output_path.read_text(encoding="utf-8")

    assert 'var options = {"layout": {"hierarchical"' not in html
    assert '"direction": "LR"' not in html
    assert '"barnesHut"' in html
    assert '"physics"' in html
    assert '"enabled": true' in html
    assert "stabilizationIterationsDone" in html
    assert "physics: { enabled: false }" in html
