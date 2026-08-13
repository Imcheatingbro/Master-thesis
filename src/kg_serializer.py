"""SPEC_06：预留 KG JSON 到 RDF/OWL 的序列化接口。"""

from __future__ import annotations

from typing import Any


def to_rdf(kg_json: dict[str, Any]) -> Any:
    """将 KG JSON 转为 RDF 图；当前阶段仅预留接口。"""
    raise NotImplementedError("RDF 序列化将在后续阶段实现")
