"""NER enrichment for collection-level causal knowledge graphs."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable
import uuid

from src.kg_postprocessor import canonical_surface_key, normalize_surface_value


NER_ENRICHMENT_VERSION = "mention_reconciliation_v1"
NER_RELATION = "has_ner_mention"


def enrich_collection_with_ner(
    integrated_kg: dict[str, Any],
    *,
    ner_pipeline: Any,
    detector_name: str,
    detector_model: str,
    detector_version: str | None = None,
) -> dict[str, Any]:
    """Detect entities in every factor and reconcile them with existing nodes.

    A full-factor match, or a unique same-event factor match, reuses the
    existing LLM-extracted mention. A previously unrepresented strict subspan
    becomes a new NER mention connected through ``has_ner_mention``. This step
    performs no Wikipedia lookup and never mutates ``integrated_kg``.
    """

    if not isinstance(integrated_kg, dict):
        raise TypeError("integrated_kg must be an object")
    collection_id = integrated_kg.get("collection_id")
    if not isinstance(collection_id, str) or not collection_id:
        raise ValueError("integrated_kg is missing collection_id")
    if not callable(ner_pipeline):
        raise TypeError("ner_pipeline must be callable")
    if not isinstance(detector_name, str) or not detector_name.strip():
        raise ValueError("detector_name must be a non-empty string")
    if not isinstance(detector_model, str) or not detector_model.strip():
        raise ValueError("detector_model must be a non-empty string")

    enriched = deepcopy(integrated_kg)
    sample_graphs = enriched.get("sample_graphs")
    resources = enriched.get("canonical_resources")
    if not isinstance(sample_graphs, list):
        raise ValueError("integrated_kg is missing the sample_graphs list")
    if not isinstance(resources, list):
        raise ValueError("integrated_kg is missing the canonical_resources list")

    resources_by_key: dict[str, dict[str, Any]] = {}
    resources_by_id: dict[str, dict[str, Any]] = {}
    for resource in resources:
        if not isinstance(resource, dict):
            raise ValueError("each canonical resource must be an object")
        canonical_key = resource.get("canonical_key")
        resource_id = resource.get("resource_id")
        if not isinstance(canonical_key, str) or not canonical_key:
            raise ValueError("canonical resource is missing canonical_key")
        if not isinstance(resource_id, str) or not resource_id:
            raise ValueError("canonical resource is missing resource_id")
        if canonical_key in resources_by_key or resource_id in resources_by_id:
            raise ValueError("integrated_kg contains a duplicate canonical resource")
        resource.setdefault("ner_detection_ids", [])
        resource.setdefault("ner_mention_ids", [])
        resource.setdefault("ner_mention_count", len(resource["ner_mention_ids"]))
        resources_by_key[canonical_key] = resource
        resources_by_id[resource_id] = resource

    factor_records = _collect_factor_records(sample_graphs)
    inference_cache: dict[str, list[dict[str, Any]]] = {}
    detections: list[dict[str, Any]] = []
    ner_mentions: list[dict[str, Any]] = []
    ner_edges: list[dict[str, Any]] = []
    detection_ids: set[str] = set()
    created_resource_count = 0
    reused_existing_count = 0

    for source_record in factor_records:
        factor_value = source_record["unit"]["value"]
        if factor_value not in inference_cache:
            inference_cache[factor_value] = _run_ner(ner_pipeline, factor_value)

        for entity in inference_cache[factor_value]:
            entity_text = entity["text"]
            entity_key = canonical_surface_key(entity_text)
            detection_id = _stable_uuid(
                "ner_detection",
                (
                    f"collection={collection_id}\n"
                    f"source_mention={source_record['mention_id']}\n"
                    f"start={entity['start_char']}\nend={entity['end_char']}\n"
                    f"label={entity['label']}\nkey={entity_key}"
                ),
            )
            if detection_id in detection_ids:
                raise ValueError(f"duplicate NER detection: {detection_id}")
            detection_ids.add(detection_id)

            target_record, match_method = _match_existing_factor(
                source_record,
                factor_records,
                entity_key=entity_key,
                start_char=entity["start_char"],
                end_char=entity["end_char"],
            )
            base_detection = {
                "detection_id": detection_id,
                "text": entity_text,
                "ner_label": entity["label"],
                "start_char": entity["start_char"],
                "end_char": entity["end_char"],
                "source_sample_id": source_record["sample_id"],
                "source_event_id": source_record["event_id"],
                "source_event_role": source_record["event_role"],
                "source_factor_mention_id": source_record["mention_id"],
                "source_factor_path": source_record["path"],
                "source_factor_value": factor_value,
                "detected_by": detector_name.strip(),
                "detector_model": detector_model.strip(),
                "detector_version": detector_version,
            }

            if target_record is not None:
                target_unit = target_record["unit"]
                annotation = {
                    "detection_id": detection_id,
                    "ner_label": entity["label"],
                    "detected_text": entity_text,
                    "detected_by": detector_name.strip(),
                    "detector_model": detector_model.strip(),
                    "detector_version": detector_version,
                    "match_method": match_method,
                    "source_factor_mention_id": source_record["mention_id"],
                    "start_char": entity["start_char"],
                    "end_char": entity["end_char"],
                }
                target_unit.setdefault("ner_annotations", []).append(annotation)
                target_resource = resources_by_id.get(target_unit["collection_resource_id"])
                if target_resource is None:
                    raise ValueError("existing factor references an unknown collection resource")
                target_resource["ner_detection_ids"].append(detection_id)
                detections.append(
                    {
                        **base_detection,
                        "action": "reused_existing_factor",
                        "match_method": match_method,
                        "target_factor_mention_id": target_record["mention_id"],
                        "target_collection_resource_id": target_resource["resource_id"],
                    }
                )
                reused_existing_count += 1
                continue

            normalized_entity = normalize_surface_value(entity_text)
            resource = resources_by_key.get(entity_key)
            if resource is None:
                resource_id = _stable_uuid(
                    "collection_resource",
                    f"collection={collection_id}\ncanonical_key={entity_key}",
                )
                resource = {
                    "resource_id": resource_id,
                    "scope": "collection",
                    "collection_id": collection_id,
                    "canonical_key": entity_key,
                    "preferred_label": normalized_entity,
                    "surface_forms": [entity_text],
                    "sample_ids": [],
                    "local_resources": [],
                    "mentions": [],
                    "resolution_method": "ner_surface_normalization",
                    "semantic_identity_confirmed": False,
                    "sample_count": 0,
                    "mention_count": 0,
                    "ner_detection_ids": [],
                    "ner_mention_ids": [],
                    "ner_mention_count": 0,
                    "origin": "postprocess_ner",
                }
                resources_by_key[entity_key] = resource
                resources_by_id[resource_id] = resource
                resources.append(resource)
                created_resource_count += 1
            if entity_text not in resource["surface_forms"]:
                resource["surface_forms"].append(entity_text)
            if source_record["sample_id"] not in resource["sample_ids"]:
                resource["sample_ids"].append(source_record["sample_id"])

            ner_mention_id = _stable_uuid(
                "ner_mention",
                f"collection={collection_id}\ndetection={detection_id}",
            )
            ner_mention = {
                "ner_mention_id": ner_mention_id,
                "node_type": "ner_mention",
                "value": entity_text,
                "normalized_value": normalized_entity,
                "canonical_key": entity_key,
                "ner_label": entity["label"],
                "origin": "postprocess_ner",
                "detected_by": detector_name.strip(),
                "detector_model": detector_model.strip(),
                "detector_version": detector_version,
                "source_sample_id": source_record["sample_id"],
                "source_event_id": source_record["event_id"],
                "source_event_role": source_record["event_role"],
                "source_span_id": source_record["source_span_id"],
                "source_factor_mention_id": source_record["mention_id"],
                "source_factor_path": source_record["path"],
                "start_char": entity["start_char"],
                "end_char": entity["end_char"],
                "collection_resource_id": resource["resource_id"],
            }
            edge = {
                "source_factor_mention_id": source_record["mention_id"],
                "relation": NER_RELATION,
                "target_ner_mention_id": ner_mention_id,
                "origin": "postprocess_ner",
                "detection_id": detection_id,
            }
            ner_mentions.append(ner_mention)
            ner_edges.append(edge)
            resource["ner_detection_ids"].append(detection_id)
            resource["ner_mention_ids"].append(ner_mention_id)
            resource["ner_mention_count"] = len(resource["ner_mention_ids"])
            resource["sample_count"] = len(resource["sample_ids"])
            detections.append(
                {
                    **base_detection,
                    "action": "created_ner_mention",
                    "match_method": "new_subspan_mention",
                    "target_ner_mention_id": ner_mention_id,
                    "target_collection_resource_id": resource["resource_id"],
                }
            )

    resources.sort(key=lambda resource: resource["canonical_key"])
    enriched["ner_detections"] = detections
    enriched["ner_mentions"] = ner_mentions
    enriched["ner_edges"] = ner_edges
    enriched["ner_enrichment"] = {
        "version": NER_ENRICHMENT_VERSION,
        "detector_name": detector_name.strip(),
        "detector_model": detector_model.strip(),
        "detector_version": detector_version,
        "relation_for_new_nodes": NER_RELATION,
        "factor_mention_count": len(factor_records),
        "unique_factor_text_inference_count": len(inference_cache),
        "ner_detection_count": len(detections),
        "reused_existing_factor_count": reused_existing_count,
        "created_ner_mention_count": len(ner_mentions),
        "created_canonical_resource_count": created_resource_count,
        "collection_resource_count_before": len(resources) - created_resource_count,
        "collection_resource_count_after": len(resources),
        "wikipedia_linking_performed": False,
    }
    return enriched


def _run_ner(ner_pipeline: Any, text: str) -> list[dict[str, Any]]:
    document = ner_pipeline(text)
    entities = getattr(document, "ents", None)
    if entities is None:
        raise ValueError("NER pipeline output is missing ents")

    output: list[dict[str, Any]] = []
    for entity in entities:
        entity_text = getattr(entity, "text", None)
        entity_label = getattr(entity, "type", None)
        start_char = getattr(entity, "start_char", None)
        end_char = getattr(entity, "end_char", None)
        if not isinstance(entity_text, str) or not entity_text:
            raise ValueError("NER entity is missing text")
        if not isinstance(entity_label, str) or not entity_label:
            raise ValueError("NER entity is missing type")
        if (
            not isinstance(start_char, int)
            or not isinstance(end_char, int)
            or start_char < 0
            or end_char <= start_char
            or end_char > len(text)
        ):
            raise ValueError("NER entity contains invalid character offsets")
        surface_text = text[start_char:end_char]
        if canonical_surface_key(surface_text) != canonical_surface_key(entity_text):
            raise ValueError("NER entity.text does not match its character offsets")
        output.append(
            {
                "text": surface_text,
                "label": entity_label,
                "start_char": start_char,
                "end_char": end_char,
            }
        )
    return output


def _collect_factor_records(sample_graphs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    mention_ids: set[str] = set()
    for sample_graph in sample_graphs:
        if not isinstance(sample_graph, dict):
            raise ValueError("sample graph must be an object")
        sample_id = sample_graph.get("id")
        event_roles = _event_role_map(sample_graph)
        events = sample_graph.get("events")
        if not isinstance(events, dict):
            raise ValueError(f"sample_id={sample_id} is missing the events object")
        for event_id, event in events.items():
            components = event.get("components") if isinstance(event, dict) else None
            if not isinstance(components, list):
                raise ValueError(f"sample_id={sample_id} event={event_id} is missing the components list")
            for index, component in enumerate(components):
                for path, unit in _iter_value_units(component, path=f"components[{index}]"):
                    mention_id = unit.get("mention_id")
                    value = unit.get("value")
                    canonical_key = unit.get("canonical_key")
                    collection_deduplication_key = unit.get("collection_deduplication_key")
                    collection_resource_id = unit.get("collection_resource_id")
                    if not all(
                        isinstance(item, str) and item
                        for item in (
                            mention_id,
                            value,
                            canonical_key,
                            collection_deduplication_key,
                            collection_resource_id,
                        )
                    ):
                        raise ValueError(
                            f"sample_id={sample_id} event={event_id} {path} is missing linkage from sections 2.3-2.5"
                        )
                    if mention_id in mention_ids:
                        raise ValueError(f"duplicate factor mention_id: {mention_id}")
                    mention_ids.add(mention_id)
                    records.append(
                        {
                            "sample_id": sample_id,
                            "event_id": event_id,
                            "event_role": event_roles.get(event_id),
                            "source_span_id": event.get("source_span_id"),
                            "path": path,
                            "mention_id": mention_id,
                            "canonical_key": canonical_key,
                            "collection_deduplication_key": collection_deduplication_key,
                            "collection_resource_id": collection_resource_id,
                            "unit": unit,
                        }
                    )
    return records


def _match_existing_factor(
    source_record: dict[str, Any],
    factor_records: list[dict[str, Any]],
    *,
    entity_key: str,
    start_char: int,
    end_char: int,
) -> tuple[dict[str, Any] | None, str | None]:
    source_value = source_record["unit"]["value"]
    if (
        not source_value[:start_char].strip()
        and not source_value[end_char:].strip()
        and source_record["canonical_key"] == entity_key
    ):
        return source_record, "full_factor_exact"

    # 2.4/2.5 may already have established that a boundary-wrapped surface
    # form (for example, "in Kunming") belongs to the same deterministic
    # resource as the strict form "Kunming". Reuse that factor/resource and
    # attach NER evidence instead of creating a redundant NER mention node.
    if source_record["collection_deduplication_key"] == entity_key:
        return source_record, "existing_canonical_resource_exact"

    same_event_matches = [
        record
        for record in factor_records
        if record["sample_id"] == source_record["sample_id"]
        and record["event_id"] == source_record["event_id"]
        and record["canonical_key"] == entity_key
        and record["mention_id"] != source_record["mention_id"]
    ]
    descendants = [
        record
        for record in same_event_matches
        if record["path"].startswith(f"{source_record['path']}.")
    ]
    if len(descendants) == 1:
        return descendants[0], "existing_descendant_exact"
    if len(same_event_matches) == 1:
        return same_event_matches[0], "existing_same_event_exact"
    return None, None


def _iter_value_units(
    unit: Any,
    *,
    path: str,
) -> Iterable[tuple[str, dict[str, Any]]]:
    if not isinstance(unit, dict):
        raise ValueError(f"{path} must be an object")
    yield path, unit
    for collection_name in ("attributes", "children"):
        nested_units = unit.get(collection_name, [])
        if nested_units is None:
            nested_units = []
        if not isinstance(nested_units, list):
            raise ValueError(f"{path}.{collection_name} must be a list")
        for index, nested_unit in enumerate(nested_units):
            yield from _iter_value_units(
                nested_unit,
                path=f"{path}.{collection_name}[{index}]",
            )


def _event_role_map(sample_graph: dict[str, Any]) -> dict[str, str]:
    roles: dict[str, str] = {}
    links = sample_graph.get("causal_links")
    if not isinstance(links, list):
        raise ValueError("sample graph is missing the causal_links list")
    for link in links:
        if not isinstance(link, dict):
            raise ValueError("causal link must be an object")
        for field, role in (("cause_event", "cause"), ("effect_event", "effect")):
            event_id = link.get(field)
            if not isinstance(event_id, str) or not event_id:
                raise ValueError(f"causal link is missing {field}")
            existing = roles.setdefault(event_id, role)
            if existing != role:
                raise ValueError(f"event={event_id} is marked as both cause and effect")
    return roles


def _stable_uuid(kind: str, identity: str) -> str:
    return f"{kind}_{uuid.uuid5(uuid.NAMESPACE_URL, f'causal-kg:{kind}:{identity}')}"
