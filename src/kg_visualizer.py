"""SPEC_07：使用 pyvis 将 NetworkX KG 图渲染为交互式 HTML。"""

from __future__ import annotations

import textwrap
from pathlib import Path

import networkx as nx
from pyvis.network import Network


def visualize(graph: nx.DiGraph, output_path: str) -> str:
    """用 pyvis 渲染 NetworkX 有向图，写出 HTML 并返回路径。"""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    styled_graph = _prepare_pyvis_graph(graph)

    network = Network(
        height="600px",
        width="100%",
        directed=True,
        notebook=True,
        cdn_resources="in_line",
        bgcolor="#ffffff",
    )
    network.from_nx(styled_graph)
    network.toggle_physics(True)
    network.set_options(
        """
{
  "interaction": {
    "hover": true,
    "dragNodes": true,
    "navigationButtons": true,
    "keyboard": true
  },
  "physics": {
    "enabled": true,
    "stabilization": {
      "enabled": true,
      "iterations": 500,
      "updateInterval": 50,
      "fit": true
    },
    "barnesHut": {
      "gravitationalConstant": -3500,
      "springLength": 140,
      "springConstant": 0.04
    }
  }
}
"""
    )
    html = _freeze_physics_after_stabilization(network.generate_html(notebook=False))
    output.write_text(html, encoding="utf-8")
    return str(output)


def _prepare_pyvis_graph(graph: nx.DiGraph) -> nx.DiGraph:
    """生成仅供 pyvis 使用的图副本，避免 KG 字段与 vis.js 保留字段冲突。"""
    styled_graph = graph.copy()
    for node_id, data in styled_graph.nodes(data=True):
        if "value" in data:
            data.setdefault("kg_value", data.pop("value"))
        if data.get("type") == "event":
            data["label"] = _wrap_label(str(data.get("label", "")))
        data.update(_node_style(data))
        data.setdefault("title", str(node_id))
    for _source, _target, data in styled_graph.edges(data=True):
        data.update(_edge_style(data))
    return styled_graph


def _node_style(data: dict[str, object]) -> dict[str, object]:
    node_type = str(data.get("type", ""))
    subtype = str(data.get("subtype", ""))
    event_role = str(data.get("event_role", ""))

    if node_type == "event":
        if event_role == "cause":
            color = "#8fd19e"
        elif event_role == "effect":
            color = "#8ec5ff"
        elif event_role == "both":
            color = "#b7a7ff"
        else:
            color = "#d5dde5"
        return {
            "shape": "box",
            "color": color,
            "margin": 12,
            "widthConstraint": {"maximum": 340},
            "font": _font(14),
        }

    if node_type == "component" and subtype == "action":
        return {"shape": "box", "color": "#f4a261", "size": 20, "font": _font(14)}

    if node_type == "component":
        return {"shape": "box", "color": "#f4a261", "size": 20, "font": _font(14)}

    if node_type == "attribute":
        return {"shape": "box", "color": "#e9ecef", "size": 14, "font": _font(12)}

    return {"shape": "dot", "color": "#d5dde5", "size": 12, "font": _font(12)}


def _edge_style(data: dict[str, object]) -> dict[str, object]:
    if data.get("type") == "causal":
        return {"color": "#d94841", "width": 4, "arrows": "to"}
    return {"color": "#7b8794", "width": 1.5, "arrows": "to"}


def _font(size: int) -> dict[str, object]:
    return {"size": size, "color": "#1f2933"}


def _wrap_label(label: str, width: int = 38) -> str:
    if len(label) <= width:
        return label
    return "\n".join(textwrap.wrap(label, width=width, break_long_words=False, break_on_hyphens=False))


def _freeze_physics_after_stabilization(html: str) -> str:
    script = """
              if (network) {
                  network.once("stabilizationIterationsDone", function () {
                      network.setOptions({ physics: { enabled: false } });
                  });
              }
"""
    marker = "              drawGraph();"
    if marker in html:
        return html.replace(marker, marker + script, 1)
    return html
