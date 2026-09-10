"""Serialization interfaces for generated knowledge graphs."""

from __future__ import annotations

from typing import Any


def to_rdf(kg_json: dict[str, Any]) -> Any:
    raise NotImplementedError("RDF 序列化将在后续阶段实现")
