"""Post-generation processing helpers for constructed causal KGs."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import re
from typing import Any, Iterable
import unicodedata
import uuid


NORMALIZATION_VERSION = "exact_surface_v1"
WITHIN_EXAMPLE_DEDUP_VERSION = "canonical_key_boundary_conditional_v2"
COLLECTION_CONSOLIDATION_VERSION = "canonical_key_boundary_conditional_collection_v2"

_SURFACE_TRANSLATION = str.maketrans(
    {
        "\u2018": "'",
        "\u2019": "'",
        "\u201b": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u201f": '"',
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
    }
)
_WHITESPACE_RE = re.compile(r"\s+")

# These words may be removed only from the outer boundary of a key, and only
# when the remaining strict key already occurs in the current comparison
# scope.  They are never removed from inside a phrase.  This keeps the rule
# deterministic and prevents an isolated phrase from being rewritten merely
# because it starts with a function word.
_BOUNDARY_FUNCTION_WORDS = frozenset(
    {
        "a",
        "an",
        "the",
        "at",
        "by",
        "for",
        "from",
        "in",
        "inside",
        "into",
        "near",
        "of",
        "on",
        "onto",
        "outside",
        "through",
        "to",
        "toward",
        "towards",
        "via",
        "within",
    }
)


def load_cached_kg_samples(
    source_path: str | Path,
    *,
    dataset: str,
    sample_ids: Iterable[int],
    prompt_version: str,
) -> dict[int, dict[str, Any]]:
    """Rebuild sample-level KG JSON objects from saved span-level extractions.

    Only construction fields are consumed. Saved Judge prompts, outputs, and
    scores are deliberately ignored.
    """

    path = Path(source_path)
    if not path.exists():
        raise FileNotFoundError(f"construction span cache not found: {path}")

    requested_ids = tuple(dict.fromkeys(int(sample_id) for sample_id in sample_ids))
    if not requested_ids:
        raise ValueError("sample_ids must not be empty")
    requested_set = set(requested_ids)

    grouped: dict[int, list[dict[str, Any]]] = {sample_id: [] for sample_id in requested_ids}
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"cache line {line_number} is not valid JSON") from exc
            if not isinstance(record, dict):
                continue

            try:
                sample_id = int(record.get("sample_id"))
            except (TypeError, ValueError):
                continue
            if sample_id not in requested_set:
                continue
            if str(record.get("dataset")) != dataset:
                continue
            if str(record.get("prompt_version")) != prompt_version:
                continue
            grouped[sample_id].append(record)

    missing = [sample_id for sample_id in requested_ids if not grouped[sample_id]]
    if missing:
        raise ValueError(
            f"cache contains no samples for dataset={dataset}, prompt={prompt_version}: {missing}"
        )

    return {
        sample_id: _rebuild_sample_kg(
            grouped[sample_id],
            sample_id=sample_id,
            dataset=dataset,
            prompt_version=prompt_version,
            source_path=path,
        )
        for sample_id in requested_ids
    }


def normalize_surface_value(value: str) -> str:
    """Apply conservative, deterministic normalization to one extracted value.

    The readable normalized value keeps lexical content and case. It only
    standardizes Unicode compatibility forms, common quote/dash variants and
    whitespace. This deliberately performs no stemming, article removal,
    synonym expansion or entity disambiguation.
    """

    if not isinstance(value, str):
        raise TypeError("KG value must be a string")
    normalized = unicodedata.normalize("NFKC", value).translate(_SURFACE_TRANSLATION)
    normalized = _WHITESPACE_RE.sub(" ", normalized).strip()
    if not normalized:
        raise ValueError("KG value must not be empty after normalization")
    return normalized


def canonical_surface_key(value: str) -> str:
    """Return the exact-match key used by later deterministic deduplication."""

    return normalize_surface_value(value).casefold()


def normalize_kg_samples(
    kg_samples: dict[int, dict[str, Any]],
) -> dict[int, dict[str, Any]]:
    """Normalize all value-bearing units without mutating the input KGs."""

    return {
        sample_id: normalize_kg_sample(kg, expected_sample_id=sample_id)
        for sample_id, kg in kg_samples.items()
    }


def normalize_kg_sample(
    kg: dict[str, Any],
    *,
    expected_sample_id: int | None = None,
) -> dict[str, Any]:
    """Annotate every component/attribute/child with exact surface keys."""

    if not isinstance(kg, dict):
        raise TypeError("KG sample must be an object")
    if expected_sample_id is not None and kg.get("id") != expected_sample_id:
        raise ValueError(
            f"KG sample ID mismatch: key={expected_sample_id}, kg.id={kg.get('id')}"
        )

    normalized_kg = deepcopy(kg)
    events = normalized_kg.get("events")
    if not isinstance(events, dict):
        raise ValueError("KG sample is missing the events object")

    normalized_unit_count = 0
    changed_surface_count = 0
    canonical_keys: set[str] = set()
    for event_id, event in events.items():
        if not isinstance(event, dict):
            raise ValueError(f"event={event_id} must be an object")
        components = event.get("components")
        if not isinstance(components, list):
            raise ValueError(f"event={event_id} is missing the components list")
        for index, component in enumerate(components):
            counts = _normalize_value_unit(
                component,
                location=f"events.{event_id}.components[{index}]",
                canonical_keys=canonical_keys,
            )
            normalized_unit_count += counts[0]
            changed_surface_count += counts[1]

    normalized_kg["normalization"] = {
        "version": NORMALIZATION_VERSION,
        "operations": [
            "Unicode NFKC",
            "quote and dash standardization",
            "whitespace collapse and trim",
            "casefold canonical key",
        ],
        "semantic_disambiguation": False,
        "normalized_unit_count": normalized_unit_count,
        "changed_surface_count": changed_surface_count,
        "unique_canonical_key_count": len(canonical_keys),
    }
    return normalized_kg


def deduplicate_kg_samples(
    normalized_kg_samples: dict[int, dict[str, Any]],
) -> dict[int, dict[str, Any]]:
    """Create sample-local resources by conservative canonical-key grouping.

    Original mention units and causal/event structure remain intact. Each value
    unit receives a mention id and a link to one sample-local canonical resource.
    Exact keys are grouped directly. A boundary-function-word variant is grouped
    only when its stripped strict key also occurs in the same sample. This is
    surface-form deduplication, not semantic entity resolution.
    """

    return {
        sample_id: deduplicate_kg_sample(kg, expected_sample_id=sample_id)
        for sample_id, kg in normalized_kg_samples.items()
    }


def deduplicate_kg_sample(
    normalized_kg: dict[str, Any],
    *,
    expected_sample_id: int | None = None,
) -> dict[str, Any]:
    """Link exact or conditionally stripped mentions within one sample."""

    if not isinstance(normalized_kg, dict):
        raise TypeError("normalized KG sample must be an object")
    sample_id = normalized_kg.get("id")
    if expected_sample_id is not None and sample_id != expected_sample_id:
        raise ValueError(
            f"KG sample ID mismatch: key={expected_sample_id}, kg.id={sample_id}"
        )
    normalization = normalized_kg.get("normalization")
    if not isinstance(normalization, dict) or normalization.get("version") != NORMALIZATION_VERSION:
        raise ValueError("generate canonical_key with the current exact normalization before deduplication")

    deduplicated_kg = deepcopy(normalized_kg)
    events = deduplicated_kg.get("events")
    if not isinstance(events, dict):
        raise ValueError("KG sample is missing the events object")

    unit_records: list[dict[str, Any]] = []
    preferred_labels_by_strict_key: dict[str, str] = {}
    for event_id, event in events.items():
        if not isinstance(event, dict):
            raise ValueError(f"event={event_id} must be an object")
        source_span_id = event.get("source_span_id")
        components = event.get("components")
        if not isinstance(components, list):
            raise ValueError(f"event={event_id} is missing the components list")

        for index, component in enumerate(components):
            for path, unit in _iter_value_units(component, path=f"components[{index}]"):
                canonical_key = unit.get("canonical_key")
                normalized_value = unit.get("normalized_value")
                role = unit.get("role")
                value = unit.get("value")
                if not all(
                    isinstance(item, str) and item
                    for item in (canonical_key, normalized_value, role, value)
                ):
                    raise ValueError(
                        f"events.{event_id}.{path} is missing a valid "
                        "role/value/normalized_value/canonical_key"
                    )

                preferred_labels_by_strict_key.setdefault(canonical_key, normalized_value)
                unit_records.append(
                    {
                        "event_id": event_id,
                        "source_span_id": source_span_id,
                        "path": path,
                        "unit": unit,
                        "canonical_key": canonical_key,
                        "normalized_value": normalized_value,
                        "role": role,
                        "value": value,
                    }
                )

    strict_keys = set(preferred_labels_by_strict_key)
    resources_by_key: dict[str, dict[str, Any]] = {}
    mention_ids: set[str] = set()
    conditional_match_count = 0
    for record in unit_records:
        event_id = record["event_id"]
        source_span_id = record["source_span_id"]
        path = record["path"]
        unit = record["unit"]
        canonical_key = record["canonical_key"]
        normalized_value = record["normalized_value"]
        role = record["role"]
        value = record["value"]
        deduplication_key, match_method = _resolve_conditional_boundary_key(
            canonical_key,
            available_strict_keys=strict_keys,
        )
        if match_method == "conditional_boundary_function_match":
            conditional_match_count += 1

        resource_id = _stable_uuid(
            "resource",
            f"sample={sample_id}\ndeduplication_key={deduplication_key}",
        )
        mention_id = _stable_uuid(
            "mention",
            f"sample={sample_id}\nevent={event_id}\npath={path}",
        )
        if mention_id in mention_ids:
            raise ValueError(f"sample_id={sample_id} has a duplicate mention path: {event_id}.{path}")
        mention_ids.add(mention_id)

        unit["deduplication_key"] = deduplication_key
        unit["deduplication_match_method"] = match_method
        unit["mention_id"] = mention_id
        unit["canonical_resource_id"] = resource_id

        resource = resources_by_key.setdefault(
            deduplication_key,
            {
                "resource_id": resource_id,
                "scope": "sample",
                "sample_id": sample_id,
                "canonical_key": deduplication_key,
                "preferred_label": preferred_labels_by_strict_key[deduplication_key],
                "surface_forms": [],
                "member_canonical_keys": [],
                "matching_methods": [],
                "mentions": [],
            },
        )
        if resource["resource_id"] != resource_id:
            raise RuntimeError("deterministic resource id collision")
        if value not in resource["surface_forms"]:
            resource["surface_forms"].append(value)
        if canonical_key not in resource["member_canonical_keys"]:
            resource["member_canonical_keys"].append(canonical_key)
        if match_method not in resource["matching_methods"]:
            resource["matching_methods"].append(match_method)
        resource["mentions"].append(
            {
                "mention_id": mention_id,
                "event_id": event_id,
                "source_span_id": source_span_id,
                "path": path,
                "role": role,
                "value": value,
                "normalized_value": normalized_value,
                "canonical_key": canonical_key,
                "deduplication_key": deduplication_key,
                "deduplication_match_method": match_method,
            }
        )

    resources = list(resources_by_key.values())
    for resource in resources:
        resource["mention_count"] = len(resource["mentions"])
        resource["resolution_method"] = (
            "conditional_boundary_function_match"
            if "conditional_boundary_function_match" in resource["matching_methods"]
            else "exact_surface_match"
        )
    duplicate_resources = [resource for resource in resources if resource["mention_count"] > 1]
    deduplicated_kg["canonical_resources"] = resources
    deduplicated_kg["within_example_deduplication"] = {
        "version": WITHIN_EXAMPLE_DEDUP_VERSION,
        "matching_rule": (
            "exact canonical-key equality, plus boundary-function-word stripping "
            "only when the remaining strict key exists within the same sample"
        ),
        "boundary_function_words": sorted(_BOUNDARY_FUNCTION_WORDS),
        "semantic_disambiguation": False,
        "mentions_preserved": True,
        "mention_count": len(mention_ids),
        "canonical_resource_count": len(resources),
        "duplicate_group_count": len(duplicate_resources),
        "duplicate_occurrence_count": sum(
            resource["mention_count"] - 1 for resource in duplicate_resources
        ),
        "conditional_boundary_match_count": conditional_match_count,
    }
    return deduplicated_kg


def consolidate_kg_collection(
    deduplicated_kg_samples: dict[int, dict[str, Any]],
    *,
    collection_id: str,
) -> dict[str, Any]:
    """Consolidate sample-local resources into one collection resource layer.

    Consolidation uses exact canonical-key equality plus the same conditional
    boundary-function-word rule used within samples. Source sample graphs,
    event nodes, causal links and mention provenance are retained. The resulting
    resources are surface-form clusters, not resolved identities.
    """

    if not isinstance(collection_id, str) or not collection_id.strip():
        raise ValueError("collection_id must be a non-empty string")
    collection_id = collection_id.strip()
    if not deduplicated_kg_samples:
        raise ValueError("deduplicated_kg_samples must not be empty")

    sample_graphs: list[dict[str, Any]] = []
    collection_resources_by_key: dict[str, dict[str, Any]] = {}
    all_mention_ids: set[str] = set()
    local_resource_count = 0
    datasets: set[str] = set()

    collection_strict_keys: set[str] = set()
    preferred_labels_by_strict_key: dict[str, str] = {}
    for sample_id in sorted(deduplicated_kg_samples):
        source_kg = deduplicated_kg_samples[sample_id]
        if not isinstance(source_kg, dict) or source_kg.get("id") != sample_id:
            raise ValueError(f"sample key={sample_id} does not match the KG ID")
        deduplication = source_kg.get("within_example_deduplication")
        if (
            not isinstance(deduplication, dict)
            or deduplication.get("version") != WITHIN_EXAMPLE_DEDUP_VERSION
        ):
            raise ValueError(f"sample_id={sample_id} has not completed the current section 2.4 deduplication")
        local_resources = source_kg.get("canonical_resources")
        if not isinstance(local_resources, list):
            raise ValueError(f"sample_id={sample_id} is missing the canonical_resources list")
        for local_resource in local_resources:
            if not isinstance(local_resource, dict):
                raise ValueError(f"sample_id={sample_id} local resource must be an object")
            canonical_key = local_resource.get("canonical_key")
            preferred_label = local_resource.get("preferred_label")
            if not all(
                isinstance(item, str) and item
                for item in (canonical_key, preferred_label)
            ):
                raise ValueError(f"sample_id={sample_id} contains an invalid local canonical resource")
            collection_strict_keys.add(canonical_key)
            preferred_labels_by_strict_key.setdefault(canonical_key, preferred_label)

    conditional_match_count = 0

    for sample_id in sorted(deduplicated_kg_samples):
        source_kg = deduplicated_kg_samples[sample_id]
        if not isinstance(source_kg, dict) or source_kg.get("id") != sample_id:
            raise ValueError(f"sample key={sample_id} does not match the KG ID")
        deduplication = source_kg.get("within_example_deduplication")
        if (
            not isinstance(deduplication, dict)
            or deduplication.get("version") != WITHIN_EXAMPLE_DEDUP_VERSION
        ):
            raise ValueError(f"sample_id={sample_id} has not completed the current section 2.4 deduplication")

        kg = deepcopy(source_kg)
        if isinstance(kg.get("dataset"), str) and kg["dataset"]:
            datasets.add(kg["dataset"])
        event_roles = _event_role_map(kg)
        local_resources = kg.get("canonical_resources")
        if not isinstance(local_resources, list):
            raise ValueError(f"sample_id={sample_id} is missing the canonical_resources list")

        local_to_collection: dict[str, tuple[str, str, str]] = {}
        local_mention_ids: set[str] = set()
        for local_resource in local_resources:
            if not isinstance(local_resource, dict):
                raise ValueError(f"sample_id={sample_id} local resource must be an object")
            local_resource_id = local_resource.get("resource_id")
            canonical_key = local_resource.get("canonical_key")
            preferred_label = local_resource.get("preferred_label")
            mentions = local_resource.get("mentions")
            if not all(
                isinstance(item, str) and item
                for item in (local_resource_id, canonical_key, preferred_label)
            ) or not isinstance(mentions, list):
                raise ValueError(f"sample_id={sample_id} contains an invalid local canonical resource")
            if local_resource_id in local_to_collection:
                raise ValueError(f"sample_id={sample_id} contains a duplicate local resource ID")

            collection_key, collection_match_method = _resolve_conditional_boundary_key(
                canonical_key,
                available_strict_keys=collection_strict_keys,
            )
            if collection_match_method == "conditional_boundary_function_match":
                conditional_match_count += 1

            collection_resource_id = _stable_uuid(
                "collection_resource",
                f"collection={collection_id}\ndeduplication_key={collection_key}",
            )
            local_to_collection[local_resource_id] = (
                collection_resource_id,
                canonical_key,
                collection_key,
            )
            local_resource["collection_resource_id"] = collection_resource_id
            local_resource["collection_deduplication_key"] = collection_key
            local_resource["collection_match_method"] = collection_match_method
            local_resource_count += 1

            collection_resource = collection_resources_by_key.setdefault(
                collection_key,
                {
                    "resource_id": collection_resource_id,
                    "scope": "collection",
                    "collection_id": collection_id,
                    "canonical_key": collection_key,
                    "preferred_label": preferred_labels_by_strict_key[collection_key],
                    "surface_forms": [],
                    "member_canonical_keys": [],
                    "matching_methods": [],
                    "sample_ids": [],
                    "local_resources": [],
                    "mentions": [],
                    "semantic_identity_confirmed": False,
                },
            )
            if collection_resource["resource_id"] != collection_resource_id:
                raise RuntimeError("deterministic collection resource id collision")
            if sample_id not in collection_resource["sample_ids"]:
                collection_resource["sample_ids"].append(sample_id)
            if canonical_key not in collection_resource["member_canonical_keys"]:
                collection_resource["member_canonical_keys"].append(canonical_key)
            effective_match_method = (
                "conditional_boundary_function_match"
                if collection_match_method == "conditional_boundary_function_match"
                or local_resource.get("resolution_method")
                == "conditional_boundary_function_match"
                else "exact_surface_match"
            )
            if effective_match_method not in collection_resource["matching_methods"]:
                collection_resource["matching_methods"].append(effective_match_method)
            collection_resource["local_resources"].append(
                {
                    "sample_id": sample_id,
                    "resource_id": local_resource_id,
                    "canonical_key": canonical_key,
                    "collection_match_method": collection_match_method,
                    "effective_match_method": effective_match_method,
                }
            )
            for surface_form in local_resource.get("surface_forms", []):
                if not isinstance(surface_form, str) or not surface_form:
                    raise ValueError(f"sample_id={sample_id} contains an invalid surface form")
                if surface_form not in collection_resource["surface_forms"]:
                    collection_resource["surface_forms"].append(surface_form)

            for mention in mentions:
                if not isinstance(mention, dict):
                    raise ValueError(f"sample_id={sample_id} mention must be an object")
                mention_id = mention.get("mention_id")
                event_id = mention.get("event_id")
                if not isinstance(mention_id, str) or not mention_id:
                    raise ValueError(f"sample_id={sample_id} contains an invalid mention_id")
                if mention_id in all_mention_ids:
                    raise ValueError(f"duplicate mention_id in collection: {mention_id}")
                all_mention_ids.add(mention_id)
                local_mention_ids.add(mention_id)
                collection_resource["mentions"].append(
                    {
                        "mention_id": mention_id,
                        "sample_id": sample_id,
                        "event_id": event_id,
                        "event_role": event_roles.get(event_id),
                        "source_span_id": mention.get("source_span_id"),
                        "path": mention.get("path"),
                        "component_role": mention.get("role"),
                        "value": mention.get("value"),
                        "normalized_value": mention.get("normalized_value"),
                        "canonical_key": mention.get("canonical_key"),
                        "local_deduplication_key": canonical_key,
                        "collection_deduplication_key": collection_key,
                        "collection_match_method": collection_match_method,
                        "local_resource_id": local_resource_id,
                    }
                )

        event_mention_ids: set[str] = set()
        events = kg.get("events")
        if not isinstance(events, dict):
            raise ValueError(f"sample_id={sample_id} is missing the events object")
        for event_id, event in events.items():
            components = event.get("components") if isinstance(event, dict) else None
            if not isinstance(components, list):
                raise ValueError(f"sample_id={sample_id} event={event_id} is missing the components list")
            for index, component in enumerate(components):
                for path, unit in _iter_value_units(component, path=f"components[{index}]"):
                    mention_id = unit.get("mention_id")
                    local_resource_id = unit.get("canonical_resource_id")
                    if not isinstance(mention_id, str) or not isinstance(local_resource_id, str):
                        raise ValueError(
                            f"sample_id={sample_id} event={event_id} {path} is missing section 2.4 linkage"
                        )
                    mapping = local_to_collection.get(local_resource_id)
                    if mapping is None or mapping[1] != unit.get("deduplication_key"):
                        raise ValueError(
                            f"sample_id={sample_id} event={event_id} {path} has inconsistent local-resource linkage"
                        )
                    unit["collection_resource_id"] = mapping[0]
                    unit["collection_deduplication_key"] = mapping[2]
                    unit["collection_match_method"] = (
                        "conditional_boundary_function_match"
                        if unit.get("deduplication_match_method")
                        == "conditional_boundary_function_match"
                        or mapping[2] != unit.get("canonical_key")
                        else "exact_surface_match"
                    )
                    event_mention_ids.add(mention_id)
        if event_mention_ids != local_mention_ids:
            raise ValueError(
                f"sample_id={sample_id} event mentions do not match canonical-resource provenance"
            )
        sample_graphs.append(kg)

    collection_resources = [
        collection_resources_by_key[key]
        for key in sorted(collection_resources_by_key)
    ]
    for resource in collection_resources:
        resource["sample_count"] = len(resource["sample_ids"])
        resource["mention_count"] = len(resource["mentions"])
        resource["resolution_method"] = (
            "conditional_boundary_function_match"
            if "conditional_boundary_function_match" in resource["matching_methods"]
            else "exact_surface_match"
        )
    cross_example_resources = [
        resource for resource in collection_resources if resource["sample_count"] > 1
    ]

    return {
        "collection_id": collection_id,
        "scope": "collection",
        "datasets": sorted(datasets),
        "sample_ids": [kg["id"] for kg in sample_graphs],
        "sample_graphs": sample_graphs,
        "canonical_resources": collection_resources,
        "collection_consolidation": {
            "version": COLLECTION_CONSOLIDATION_VERSION,
            "matching_rule": (
                "exact canonical-key equality, plus boundary-function-word stripping "
                "only when the remaining strict key exists across the input collection"
            ),
            "boundary_function_words": sorted(_BOUNDARY_FUNCTION_WORDS),
            "resolution_method": "deterministic_surface_match",
            "semantic_disambiguation": False,
            "semantic_identity_confirmed": False,
            "sample_count": len(sample_graphs),
            "mention_count": len(all_mention_ids),
            "local_resource_count": local_resource_count,
            "collection_resource_count": len(collection_resources),
            "cross_example_resource_count": len(cross_example_resources),
            "cross_example_mention_count": sum(
                resource["mention_count"] for resource in cross_example_resources
            ),
            "resource_reduction_count": local_resource_count - len(collection_resources),
            "conditional_boundary_match_count": conditional_match_count,
        },
    }


def _resolve_conditional_boundary_key(
    canonical_key: str,
    *,
    available_strict_keys: set[str],
) -> tuple[str, str]:
    """Resolve one key without guessing a target absent from the current scope."""

    tokens = canonical_key.split()
    start = 0
    end = len(tokens)
    while start < end and tokens[start] in _BOUNDARY_FUNCTION_WORDS:
        start += 1
    while end > start and tokens[end - 1] in _BOUNDARY_FUNCTION_WORDS:
        end -= 1

    candidate = " ".join(tokens[start:end])
    if candidate and candidate != canonical_key and candidate in available_strict_keys:
        return candidate, "conditional_boundary_function_match"
    return canonical_key, "exact_surface_match"


def _normalize_value_unit(
    unit: Any,
    *,
    location: str,
    canonical_keys: set[str],
) -> tuple[int, int]:
    if not isinstance(unit, dict):
        raise ValueError(f"{location} must be an object")
    if "value" not in unit:
        raise ValueError(f"{location} is missing value")

    original_value = unit["value"]
    normalized_value = normalize_surface_value(original_value)
    canonical_key = normalized_value.casefold()
    unit["normalized_value"] = normalized_value
    unit["canonical_key"] = canonical_key
    canonical_keys.add(canonical_key)

    unit_count = 1
    changed_count = int(normalized_value != original_value)
    for collection_name in ("attributes", "children"):
        nested_units = unit.get(collection_name, [])
        if nested_units is None:
            nested_units = []
        if not isinstance(nested_units, list):
            raise ValueError(f"{location}.{collection_name} must be a list")
        for index, nested_unit in enumerate(nested_units):
            nested_counts = _normalize_value_unit(
                nested_unit,
                location=f"{location}.{collection_name}[{index}]",
                canonical_keys=canonical_keys,
            )
            unit_count += nested_counts[0]
            changed_count += nested_counts[1]
    return unit_count, changed_count


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


def _stable_uuid(kind: str, identity: str) -> str:
    return f"{kind}_{uuid.uuid5(uuid.NAMESPACE_URL, f'causal-kg:{kind}:{identity}')}"


def _event_role_map(kg: dict[str, Any]) -> dict[str, str]:
    roles: dict[str, str] = {}
    causal_links = kg.get("causal_links")
    if not isinstance(causal_links, list):
        raise ValueError("KG sample is missing the causal_links list")
    for link in causal_links:
        if not isinstance(link, dict):
            raise ValueError("causal link must be an object")
        for field, role in (("cause_event", "cause"), ("effect_event", "effect")):
            event_id = link.get(field)
            if not isinstance(event_id, str) or not event_id:
                raise ValueError(f"causal link is missing {field}")
            existing_role = roles.setdefault(event_id, role)
            if existing_role != role:
                raise ValueError(f"event={event_id} is marked as both cause and effect")
    return roles


def _rebuild_sample_kg(
    records: list[dict[str, Any]],
    *,
    sample_id: int,
    dataset: str,
    prompt_version: str,
    source_path: Path,
) -> dict[str, Any]:
    sample_texts = {str(record.get("sample_text", "")) for record in records}
    if len(sample_texts) != 1:
        raise ValueError(f"sample_id={sample_id} cache contains inconsistent sample_text values")

    events: dict[str, dict[str, Any]] = {}
    roles_by_triple: dict[int, set[str]] = {}
    for record in records:
        if record.get("extraction_error_type"):
            raise ValueError(
                f"sample_id={sample_id} span={record.get('span_id')} has a construction error: "
                f"{record.get('extraction_error_type')}"
            )

        parsed = record.get("parsed_extraction")
        if not isinstance(parsed, dict) or not isinstance(parsed.get("components"), list):
            raise ValueError(
                f"sample_id={sample_id} span={record.get('span_id')} is missing parsed_extraction.components"
            )

        event_role = str(record.get("event_role", "")).strip().lower()
        if event_role not in {"cause", "effect"}:
            raise ValueError(f"sample_id={sample_id} contains unknown event_role={event_role!r}")
        try:
            triple_index = int(record.get("triple_index"))
        except (TypeError, ValueError) as exc:
            raise ValueError(f"sample_id={sample_id} contains an invalid triple_index") from exc

        expected_event_id = f"triple_{triple_index}_{event_role}"
        event_id = str(record.get("graph_event_id") or expected_event_id)
        if event_id != expected_event_id:
            raise ValueError(
                f"sample_id={sample_id} graph_event_id mismatch: {event_id} != {expected_event_id}"
            )
        if event_id in events:
            raise ValueError(f"sample_id={sample_id} contains a duplicate event: {event_id}")

        events[event_id] = {
            "span": str(record.get("span", "")),
            "components": parsed["components"],
            "source_span_id": record.get("span_id"),
        }
        roles_by_triple.setdefault(triple_index, set()).add(event_role)

    incomplete = {
        index: sorted(roles)
        for index, roles in roles_by_triple.items()
        if roles != {"cause", "effect"}
    }
    if incomplete:
        raise ValueError(f"sample_id={sample_id} has incomplete causal triples: {incomplete}")

    causal_links = [
        {
            "relation": "caused",
            "cause_event": f"triple_{index}_cause",
            "effect_event": f"triple_{index}_effect",
            "triple_index": index,
        }
        for index in sorted(roles_by_triple)
    ]
    return {
        "id": sample_id,
        "dataset": dataset,
        "text": sample_texts.pop(),
        "triple_source": "gold_cached",
        "construction_prompt_version": prompt_version,
        "construction_source": str(source_path),
        "causal_links": causal_links,
        "events": events,
    }
