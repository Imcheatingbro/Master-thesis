"""Render a NetworkX knowledge graph as interactive HTML with pyvis."""

from __future__ import annotations

import textwrap
from pathlib import Path

import networkx as nx
from pyvis.network import Network


def visualize(
    graph: nx.DiGraph,
    output_path: str,
    *,
    height: str = "600px",
    legend_html: str | None = None,
) -> str:
    """Render a directed NetworkX graph with pyvis and return the HTML path."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    styled_graph = _prepare_pyvis_graph(graph)

    network = Network(
        height=height,
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
    if legend_html:
        html = _inject_legend(html, legend_html)
    output.write_text(html, encoding="utf-8")
    return str(output)


def _prepare_pyvis_graph(graph: nx.DiGraph) -> nx.DiGraph:
    """Build a pyvis-only graph copy to avoid clashes with reserved vis.js fields."""
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

    if node_type == "canonical_resource":
        shared = bool(data.get("is_cross_example"))
        deduplicated = bool(data.get("is_deduplicated"))
        ner_created = bool(data.get("is_ner_created"))
        wikipedia_linked = bool(data.get("wikipedia_linked"))
        if wikipedia_linked:
            color: object = {
                "background": "#fff0a8",
                "border": "#16803c",
                "highlight": {"background": "#ffe16a", "border": "#0f6a31"},
                "hover": {"background": "#ffe991", "border": "#0f6a31"},
            }
        elif shared:
            color = {
                "background": "#eee7ff",
                "border": "#6d3fc0",
                "highlight": {"background": "#ddd0ff", "border": "#5529a5"},
                "hover": {"background": "#e5d9ff", "border": "#5529a5"},
            }
        elif deduplicated:
            color = {"background": "#f3efff", "border": "#8b63c7"}
        else:
            color = {"background": "#f8fafc", "border": "#64748b"}
        return {
            "shape": "diamond" if shared else ("triangle" if ner_created else "ellipse"),
            "color": color,
            "borderWidth": 4 if wikipedia_linked else (3 if shared or deduplicated else 2),
            "margin": 10,
            "widthConstraint": {"maximum": 210},
            "font": _font(13),
        }

    if node_type == "ner_mention":
        return {
            "shape": "triangle",
            "color": {"background": "#bdeff2", "border": "#087f8c"},
            "borderWidth": 2,
            "size": 22,
            "font": _font(12),
        }

    return {"shape": "dot", "color": "#d5dde5", "size": 12, "font": _font(12)}


def _edge_style(data: dict[str, object]) -> dict[str, object]:
    if data.get("type") == "causal":
        return {"color": "#d94841", "width": 4, "arrows": "to"}
    if data.get("type") == "canonicalizes_to":
        return {
            "color": "#6d3fc0" if data.get("target_shared") else "#94a3b8",
            "width": 2.2 if data.get("target_shared") else 1.2,
            "dashes": True,
            "arrows": "to",
        }
    if data.get("type") == "has_ner_mention":
        return {"color": "#087f8c", "width": 2, "dashes": [4, 4], "arrows": "to"}
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


def _inject_legend(html: str, legend_html: str) -> str:
    style = """
<style>
.kg-postprocess-legend { font-family: Arial, sans-serif; display: flex; flex-wrap: wrap;
  align-items: center; gap: 10px 18px; padding: 10px 14px; margin: 8px;
  border: 1px solid #d7dde5; border-radius: 8px; background: #fbfcfe; color: #1f2933; }
.kg-postprocess-legend span { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; }
.kg-postprocess-legend i { display: inline-block; width: 18px; height: 14px; border: 2px solid #64748b; }
.kg-postprocess-legend .cause { background: #8fd19e; }
.kg-postprocess-legend .effect { background: #8ec5ff; }
.kg-postprocess-legend .canonical { background: #f8fafc; border-radius: 50%; }
.kg-postprocess-legend .shared { background: #eee7ff; border-color: #6d3fc0; transform: rotate(45deg); width: 13px; height: 13px; margin: 2px; }
.kg-postprocess-legend .wiki { background: #fff0a8; border: 4px solid #16803c; border-radius: 50%; }
.kg-postprocess-legend .ner { width: 0; height: 0; border-left: 10px solid transparent;
  border-right: 10px solid transparent; border-bottom: 18px solid #087f8c; border-top: 0; }
</style>
"""
    insertion = f"{style}\n{legend_html}\n"
    if "<body>" in html:
        return html.replace("<body>", f"<body>\n{insertion}", 1)
    return insertion + html
