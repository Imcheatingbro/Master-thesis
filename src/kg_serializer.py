"""RDF/RDFS/OWL serialization for the post-processed causal KG.

The serializer uses a small fixed vocabulary for roles named by the
``nested_v1`` extraction prompt. A concise role invented by the LLM is not
discarded: it receives a deterministic custom predicate URI, keeps its exact
label, and is declared as a sub-property of ``hasFactorRelation``.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re
from typing import Any, Iterable
from urllib.parse import quote
import unicodedata

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, PROV, RDF, RDFS, XSD

from src.kg_postprocess_visualizer import build_integrated_postprocess_graph


RDF_SERIALIZATION_VERSION = "rdflib_open_role_registry_v1"
DEFAULT_BASE_NAMESPACE = "https://example.org/master-thesis/causal-kg/"

# Common roles and roles explicitly demonstrated by nested_v1. Other valid
# output roles are handled by the deterministic open-role branch below.
KNOWN_ROLE_PREDICATES: dict[str, str] = {
    "action": "hasAction",
    "actor": "hasActor",
    "theme": "hasTheme",
    "location": "hasLocation",
    "time": "hasTime",
    "instrument": "hasInstrument",
    "manner": "hasManner",
    "state": "hasState",
    "description": "hasDescription",
    "case": "hasCase",
    "organization": "hasOrganization",
    "event": "hasEvent",
    "object": "hasObject",
    "quantifier": "hasQuantifier",
    "attribute": "hasAttribute",
    "nationality": "hasNationality",
    "age": "hasAge",
    "type": "hasType",
    "cost": "hasCost",
    "name": "hasName",
    "modifier": "hasModifier",
    "negation": "hasNegation",
    "possessor": "hasPossessor",
    "result": "hasResult",
    "topic": "hasTopic",
    "content": "hasContent",
    "participant": "hasParticipant",
}


def to_rdf(
    integrated_kg: dict[str, Any],
    *,
    base_namespace: str = DEFAULT_BASE_NAMESPACE,
) -> Graph:
    """Convert one linked, consolidated KG collection to an RDF graph."""

    _validate_base_namespace(base_namespace)
    view = build_integrated_postprocess_graph(integrated_kg)
    graph = Graph()
    ex = Namespace(base_namespace)
    role_ns = Namespace(f"{base_namespace}relation/")
    graph.bind("ex", ex)
    graph.bind("role", role_ns)
    graph.bind("rdf", RDF)
    graph.bind("rdfs", RDFS)
    graph.bind("owl", OWL)
    graph.bind("prov", PROV)
    graph.bind("dcterms", DCTERMS)

    ontology_uri = URIRef(f"{base_namespace}ontology")
    graph.add((ontology_uri, RDF.type, OWL.Ontology))
    graph.add((ontology_uri, RDFS.label, Literal("Causal KG lightweight schema", lang="en")))
    graph.add((ontology_uri, ex.serializationVersion, Literal(RDF_SERIALIZATION_VERSION)))

    _declare_schema(graph, ex)
    collection_uri = _collection_uri(ex, integrated_kg)
    graph.add((collection_uri, RDF.type, ex.KnowledgeGraphCollection))
    graph.add((collection_uri, RDFS.label, Literal(str(integrated_kg.get("collection_id", "collection")))))
    graph.add(
        (
            collection_uri,
            ex.openRolePolicy,
            Literal(
                "Prompt-defined roles use fixed predicates; other concise LLM roles use deterministic custom predicates."
            ),
        )
    )

    sample_graphs = integrated_kg.get("sample_graphs")
    resources = integrated_kg.get("canonical_resources")
    if not isinstance(sample_graphs, list) or not isinstance(resources, list):
        raise ValueError("integrated_kg is missing the sample_graphs or canonical_resources list")

    for sample in sample_graphs:
        _add_sample_and_events(graph, ex, collection_uri, sample)
    for resource in resources:
        _add_resource_and_mentions(graph, ex, collection_uri, resource)
    _add_reused_ner_annotations(graph, ex, sample_graphs)
    _add_ner_mentions(graph, ex, integrated_kg)

    node_uris = {
        node_id: _node_uri_from_id(ex, node_id, data)
        for node_id, data in view.nodes(data=True)
    }
    role_registry: dict[str, tuple[URIRef, bool, str]] = {}
    for source, target, edge in view.edges(data=True):
        source_uri = node_uris[source]
        target_uri = node_uris[target]
        edge_type = str(edge.get("type", ""))
        if edge_type == "causal":
            predicate = ex.causes
            graph.add((source_uri, predicate, target_uri))
            _add_relation_assertion(
                graph,
                ex,
                collection_uri=collection_uri,
                source=source_uri,
                predicate=predicate,
                target=target_uri,
                role_label="caused",
                edge_type=edge_type,
                provenance={"sample_id": view.nodes[source].get("sample_id")},
            )
            continue

        provenance = edge.get("provenance")
        if not isinstance(provenance, list) or not provenance:
            provenance = [{}]
        roles = edge.get("roles")
        if not isinstance(roles, list) or not roles:
            roles = [edge.get("role") or edge.get("label") or edge_type]

        for item in provenance:
            if not isinstance(item, dict):
                item = {}
            role_label = str(item.get("role") or roles[0]).strip()
            if edge_type == "has_ner_mention":
                predicate = ex.hasNerEntity
                graph.add((source_uri, predicate, target_uri))
                _add_relation_assertion(
                    graph,
                    ex,
                    collection_uri=collection_uri,
                    source=source_uri,
                    predicate=predicate,
                    target=target_uri,
                    role_label=role_label,
                    edge_type=edge_type,
                    provenance=item,
                )
                continue
            predicate, is_open, normalized_role = _role_predicate(ex, role_ns, role_label)
            _declare_role_predicate(
                graph,
                ex,
                predicate,
                role_label=role_label,
                normalized_role=normalized_role,
                is_open=is_open,
            )
            role_registry[str(predicate)] = (predicate, is_open, role_label)
            graph.add((source_uri, predicate, target_uri))
            _add_relation_assertion(
                graph,
                ex,
                collection_uri=collection_uri,
                source=source_uri,
                predicate=predicate,
                target=target_uri,
                role_label=role_label,
                edge_type=edge_type,
                provenance=item,
            )

    known_count = sum(not record[1] for record in role_registry.values())
    open_count = sum(record[1] for record in role_registry.values())
    graph.add((collection_uri, ex.usedKnownRolePredicateCount, Literal(known_count, datatype=XSD.integer)))
    graph.add((collection_uri, ex.usedOpenRolePredicateCount, Literal(open_count, datatype=XSD.integer)))
    return graph


def serialize_integrated_kg(
    integrated_kg: dict[str, Any],
    *,
    turtle_path: str | Path,
    jsonld_path: str | Path,
    base_namespace: str = DEFAULT_BASE_NAMESPACE,
) -> dict[str, Any]:
    """Write Turtle and JSON-LD, parse both back, and return a QC summary."""

    ttl_path = Path(turtle_path)
    json_path = Path(jsonld_path)
    ttl_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    graph = to_rdf(integrated_kg, base_namespace=base_namespace)
    ex = Namespace(base_namespace)

    graph.serialize(destination=str(ttl_path), format="turtle", encoding="utf-8")
    context = {
        "ex": base_namespace,
        "role": f"{base_namespace}relation/",
        "rdf": str(RDF),
        "rdfs": str(RDFS),
        "owl": str(OWL),
        "prov": str(PROV),
        "dcterms": str(DCTERMS),
    }
    graph.serialize(
        destination=str(json_path),
        format="json-ld",
        context=context,
        auto_compact=True,
        indent=2,
        encoding="utf-8",
    )

    ttl_graph = Graph().parse(str(ttl_path), format="turtle")
    jsonld_graph = Graph().parse(str(json_path), format="json-ld")
    if len(ttl_graph) != len(graph) or len(jsonld_graph) != len(graph):
        raise ValueError("RDF round-trip triple count mismatch")

    expected_event_count = sum(
        len(sample.get("events", {}))
        for sample in integrated_kg.get("sample_graphs", [])
        if isinstance(sample, dict) and isinstance(sample.get("events"), dict)
    )
    expected_resource_count = len(integrated_kg.get("canonical_resources", []))
    event_count = len(set(graph.subjects(RDF.type, ex.CausalEvent)))
    resource_count = len(set(graph.subjects(RDF.type, ex.CanonicalFactor)))
    if event_count != expected_event_count or resource_count != expected_resource_count:
        raise ValueError(
            "RDF entity count mismatch: "
            f"events={event_count}/{expected_event_count}, "
            f"resources={resource_count}/{expected_resource_count}"
        )

    open_roles = sorted(
        {
            str(label)
            for predicate in graph.subjects(ex.roleKind, Literal("open"))
            for label in graph.objects(predicate, RDFS.label)
        }
    )
    known_roles = sorted(
        {
            str(label)
            for predicate in graph.subjects(ex.roleKind, Literal("prompt-defined"))
            for label in graph.objects(predicate, RDFS.label)
        }
    )
    wikipedia_link_count = len(set(graph.subjects(RDFS.seeAlso, None)))
    return {
        "version": RDF_SERIALIZATION_VERSION,
        "base_namespace": base_namespace,
        "turtle_path": str(ttl_path),
        "jsonld_path": str(json_path),
        "triple_count": len(graph),
        "turtle_roundtrip_triple_count": len(ttl_graph),
        "jsonld_roundtrip_triple_count": len(jsonld_graph),
        "event_count": event_count,
        "canonical_resource_count": resource_count,
        "wikipedia_link_count": wikipedia_link_count,
        "used_prompt_defined_roles": known_roles,
        "used_open_roles": open_roles,
        "roundtrip_valid": True,
        "uses_owl_same_as": any(True for _ in graph.triples((None, OWL.sameAs, None))),
    }


def _declare_schema(graph: Graph, ex: Namespace) -> None:
    classes = {
        ex.KnowledgeGraphCollection: "Knowledge graph collection",
        ex.Sample: "Source sample",
        ex.CausalEvent: "Causal event",
        ex.CauseEvent: "Cause event",
        ex.EffectEvent: "Effect event",
        ex.CanonicalFactor: "Canonical factor",
        ex.NerDerivedFactor: "NER-derived canonical factor",
        ex.FactorMention: "Extracted factor mention",
        ex.NerMention: "NER mention",
        ex.RelationAssertion: "Relation assertion",
    }
    for class_uri, label in classes.items():
        graph.add((class_uri, RDF.type, OWL.Class))
        graph.add((class_uri, RDFS.label, Literal(label, lang="en")))
    graph.add((ex.CauseEvent, RDFS.subClassOf, ex.CausalEvent))
    graph.add((ex.EffectEvent, RDFS.subClassOf, ex.CausalEvent))
    graph.add((ex.NerDerivedFactor, RDFS.subClassOf, ex.CanonicalFactor))
    graph.add((ex.NerMention, RDFS.subClassOf, ex.FactorMention))
    graph.add((ex.RelationAssertion, RDFS.subClassOf, RDF.Statement))

    properties = {
        ex.causes: "causes",
        ex.hasFactorRelation: "has factor relation",
        ex.hasNerEntity: "has NER-detected entity",
        ex.denotes: "denotes canonical factor",
        ex.inEvent: "occurs in event",
    }
    for property_uri, label in properties.items():
        graph.add((property_uri, RDF.type, OWL.ObjectProperty))
        graph.add((property_uri, RDFS.label, Literal(label, lang="en")))
    graph.add((ex.hasNerEntity, RDFS.subPropertyOf, ex.hasFactorRelation))


def _add_sample_and_events(
    graph: Graph,
    ex: Namespace,
    collection_uri: URIRef,
    sample: Any,
) -> None:
    if not isinstance(sample, dict) or not isinstance(sample.get("id"), int):
        raise ValueError("sample graph is missing an integer ID")
    sample_id = sample["id"]
    sample_uri = _sample_uri(ex, sample_id)
    graph.add((sample_uri, RDF.type, ex.Sample))
    graph.add((sample_uri, RDFS.label, Literal(f"Sample {sample_id}")))
    graph.add((sample_uri, ex.sampleId, Literal(sample_id, datatype=XSD.integer)))
    if sample.get("dataset"):
        graph.add((sample_uri, ex.dataset, Literal(str(sample["dataset"]))))
    if sample.get("text"):
        graph.add((sample_uri, RDF.value, Literal(str(sample["text"]))))
    graph.add((collection_uri, DCTERMS.hasPart, sample_uri))

    roles = _event_roles(sample)
    events = sample.get("events")
    if not isinstance(events, dict):
        raise ValueError(f"sample_id={sample_id} is missing the events object")
    for event_id, event in events.items():
        if not isinstance(event_id, str) or not isinstance(event, dict):
            raise ValueError(f"sample_id={sample_id} contains an invalid event")
        event_uri = _event_uri(ex, sample_id, event_id)
        graph.add((event_uri, RDF.type, ex.CausalEvent))
        event_role = roles.get(event_id, "event")
        if event_role in {"cause", "both"}:
            graph.add((event_uri, RDF.type, ex.CauseEvent))
        if event_role in {"effect", "both"}:
            graph.add((event_uri, RDF.type, ex.EffectEvent))
        span = str(event.get("span", "") or event_id)
        graph.add((event_uri, RDFS.label, Literal(span)))
        graph.add((event_uri, ex.eventId, Literal(event_id)))
        graph.add((event_uri, ex.eventRole, Literal(event_role)))
        if event.get("source_span_id") is not None:
            graph.add((event_uri, ex.sourceSpanId, Literal(str(event["source_span_id"]))))
        graph.add((event_uri, PROV.wasDerivedFrom, sample_uri))
        graph.add((collection_uri, DCTERMS.hasPart, event_uri))


def _add_resource_and_mentions(
    graph: Graph,
    ex: Namespace,
    collection_uri: URIRef,
    resource: Any,
) -> None:
    if not isinstance(resource, dict):
        raise ValueError("canonical resource must be an object")
    resource_id = _required_string(resource, "resource_id", "canonical resource")
    resource_uri = _resource_uri(ex, resource_id)
    graph.add((resource_uri, RDF.type, ex.CanonicalFactor))
    if resource.get("origin") == "postprocess_ner":
        graph.add((resource_uri, RDF.type, ex.NerDerivedFactor))
    graph.add((resource_uri, RDFS.label, Literal(_required_string(resource, "preferred_label", "resource"))))
    graph.add((resource_uri, ex.canonicalKey, Literal(_required_string(resource, "canonical_key", "resource"))))
    graph.add((resource_uri, ex.mentionCount, Literal(int(resource.get("mention_count", 0)), datatype=XSD.integer)))
    graph.add((resource_uri, ex.sampleCount, Literal(int(resource.get("sample_count", 0)), datatype=XSD.integer)))
    graph.add((resource_uri, ex.isCrossExample, Literal(int(resource.get("sample_count", 0)) > 1, datatype=XSD.boolean)))
    graph.add((resource_uri, ex.semanticIdentityConfirmed, Literal(bool(resource.get("semantic_identity_confirmed", False)), datatype=XSD.boolean)))
    for value in _strings(resource.get("surface_forms")):
        graph.add((resource_uri, ex.surfaceForm, Literal(value)))
    for sample_id in resource.get("sample_ids", []):
        if isinstance(sample_id, int):
            graph.add((resource_uri, PROV.wasDerivedFrom, _sample_uri(ex, sample_id)))
    graph.add((collection_uri, DCTERMS.hasPart, resource_uri))

    wikipedia = resource.get("wikipedia_link")
    if isinstance(wikipedia, dict):
        status = str(wikipedia.get("status", "not_checked"))
        graph.add((resource_uri, ex.wikipediaStatus, Literal(status)))
        page = wikipedia.get("selected_page")
        if status == "linked" and isinstance(page, dict) and page.get("url"):
            graph.add((resource_uri, RDFS.seeAlso, URIRef(str(page["url"]))))
            if page.get("title"):
                graph.add((resource_uri, ex.wikipediaTitle, Literal(str(page["title"]))))

    mentions = resource.get("mentions", [])
    if not isinstance(mentions, list):
        raise ValueError("resource.mentions must be a list")
    for mention in mentions:
        if not isinstance(mention, dict):
            raise ValueError("factor mention must be an object")
        mention_id = _required_string(mention, "mention_id", "factor mention")
        mention_uri = _mention_uri(ex, mention_id)
        graph.add((mention_uri, RDF.type, ex.FactorMention))
        graph.add((mention_uri, ex.denotes, resource_uri))
        if mention.get("value") is not None:
            graph.add((mention_uri, RDF.value, Literal(str(mention["value"]))))
        if mention.get("component_role") is not None:
            graph.add((mention_uri, ex.roleLabel, Literal(str(mention["component_role"]))))
        if mention.get("path") is not None:
            graph.add((mention_uri, ex.extractionPath, Literal(str(mention["path"]))))
        sample_id = mention.get("sample_id")
        event_id = mention.get("event_id")
        if isinstance(sample_id, int):
            graph.add((mention_uri, PROV.wasDerivedFrom, _sample_uri(ex, sample_id)))
            if isinstance(event_id, str) and event_id:
                graph.add((mention_uri, ex.inEvent, _event_uri(ex, sample_id, event_id)))


def _add_reused_ner_annotations(
    graph: Graph,
    ex: Namespace,
    sample_graphs: list[dict[str, Any]],
) -> None:
    for sample in sample_graphs:
        events = sample.get("events", {}) if isinstance(sample, dict) else {}
        for event in events.values() if isinstance(events, dict) else []:
            components = event.get("components", []) if isinstance(event, dict) else []
            for unit in _iter_units(components):
                mention_id = unit.get("mention_id")
                annotations = unit.get("ner_annotations", [])
                if not isinstance(mention_id, str) or not isinstance(annotations, list):
                    continue
                mention_uri = _mention_uri(ex, mention_id)
                for annotation in annotations:
                    if not isinstance(annotation, dict):
                        continue
                    if annotation.get("ner_label"):
                        graph.add((mention_uri, ex.nerLabel, Literal(str(annotation["ner_label"]))))
                    if annotation.get("match_method"):
                        graph.add((mention_uri, ex.nerMatchMethod, Literal(str(annotation["match_method"]))))


def _add_ner_mentions(graph: Graph, ex: Namespace, integrated_kg: dict[str, Any]) -> None:
    mentions = integrated_kg.get("ner_mentions", [])
    if not isinstance(mentions, list):
        raise ValueError("ner_mentions must be a list")
    for mention in mentions:
        if not isinstance(mention, dict):
            raise ValueError("NER mention must be an object")
        mention_id = _required_string(mention, "ner_mention_id", "NER mention")
        resource_id = _required_string(mention, "collection_resource_id", "NER mention")
        mention_uri = _mention_uri(ex, mention_id)
        graph.add((mention_uri, RDF.type, ex.NerMention))
        graph.add((mention_uri, ex.denotes, _resource_uri(ex, resource_id)))
        if mention.get("value"):
            graph.add((mention_uri, RDF.value, Literal(str(mention["value"]))))
        if mention.get("ner_label"):
            graph.add((mention_uri, ex.nerLabel, Literal(str(mention["ner_label"]))))
        if mention.get("sample_id") is not None:
            graph.add((mention_uri, PROV.wasDerivedFrom, _sample_uri(ex, int(mention["sample_id"]))))
        source_id = mention.get("source_factor_mention_id")
        if isinstance(source_id, str) and source_id:
            graph.add((mention_uri, ex.detectedWithin, _mention_uri(ex, source_id)))


def _declare_role_predicate(
    graph: Graph,
    ex: Namespace,
    predicate: URIRef,
    *,
    role_label: str,
    normalized_role: str,
    is_open: bool,
) -> None:
    graph.add((predicate, RDF.type, OWL.ObjectProperty))
    graph.add((predicate, RDFS.subPropertyOf, ex.hasFactorRelation))
    graph.add((predicate, RDFS.label, Literal(role_label)))
    graph.add((predicate, ex.normalizedRole, Literal(normalized_role)))
    graph.add((predicate, ex.roleKind, Literal("open" if is_open else "prompt-defined")))


def _role_predicate(
    ex: Namespace,
    role_ns: Namespace,
    role_label: str,
) -> tuple[URIRef, bool, str]:
    normalized = unicodedata.normalize("NFKC", role_label).strip().casefold()
    known_local_name = KNOWN_ROLE_PREDICATES.get(normalized)
    if known_local_name is not None:
        return ex[known_local_name], False, normalized
    slug = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-") or "role"
    digest = sha256(normalized.encode("utf-8")).hexdigest()[:8]
    return role_ns[f"custom/{slug}-{digest}"], True, normalized


def _add_relation_assertion(
    graph: Graph,
    ex: Namespace,
    *,
    collection_uri: URIRef,
    source: URIRef,
    predicate: URIRef,
    target: URIRef,
    role_label: str,
    edge_type: str,
    provenance: dict[str, Any],
) -> None:
    identity = "\n".join(
        [
            str(source),
            str(predicate),
            str(target),
            str(provenance.get("mention_id", "")),
            str(provenance.get("source_factor_mention_id", "")),
            str(provenance.get("path", "")),
            str(provenance.get("sample_id", "")),
        ]
    )
    assertion_uri = ex[f"assertion/{sha256(identity.encode('utf-8')).hexdigest()[:20]}"]
    graph.add((assertion_uri, RDF.type, ex.RelationAssertion))
    graph.add((assertion_uri, RDF.type, RDF.Statement))
    graph.add((assertion_uri, RDF.subject, source))
    graph.add((assertion_uri, RDF.predicate, predicate))
    graph.add((assertion_uri, RDF.object, target))
    graph.add((assertion_uri, ex.roleLabel, Literal(role_label)))
    graph.add((assertion_uri, ex.edgeType, Literal(edge_type)))
    graph.add((collection_uri, DCTERMS.hasPart, assertion_uri))
    sample_id = provenance.get("sample_id")
    if isinstance(sample_id, int):
        graph.add((assertion_uri, PROV.wasDerivedFrom, _sample_uri(ex, sample_id)))
    mention_id = provenance.get("mention_id")
    if isinstance(mention_id, str) and mention_id:
        graph.add((assertion_uri, PROV.wasDerivedFrom, _mention_uri(ex, mention_id)))
    for field, property_uri in (
        ("event_id", ex.sourceEventId),
        ("path", ex.extractionPath),
        ("value", ex.sourceValue),
        ("source_factor_mention_id", ex.sourceFactorMentionId),
        ("target_ner_mention_id", ex.targetNerMentionId),
    ):
        if provenance.get(field) is not None:
            graph.add((assertion_uri, property_uri, Literal(str(provenance[field]))))


def _node_uri_from_id(ex: Namespace, node_id: str, data: dict[str, Any]) -> URIRef:
    if data.get("type") == "event":
        return _event_uri(ex, int(data["sample_id"]), str(data["event_id"]))
    if data.get("type") == "canonical_resource" and node_id.startswith("resource:"):
        return _resource_uri(ex, node_id.removeprefix("resource:"))
    raise ValueError(f"cannot generate a URI from view node: {node_id}")


def _collection_uri(ex: Namespace, integrated_kg: dict[str, Any]) -> URIRef:
    return ex[f"collection/{_uri_component(str(integrated_kg.get('collection_id', 'collection')))}"]


def _sample_uri(ex: Namespace, sample_id: int) -> URIRef:
    return ex[f"sample/{sample_id}"]


def _event_uri(ex: Namespace, sample_id: int, event_id: str) -> URIRef:
    return ex[f"event/{sample_id}/{_uri_component(event_id)}"]


def _resource_uri(ex: Namespace, resource_id: str) -> URIRef:
    return ex[f"resource/{_uri_component(resource_id)}"]


def _mention_uri(ex: Namespace, mention_id: str) -> URIRef:
    return ex[f"mention/{_uri_component(mention_id)}"]


def _uri_component(value: str) -> str:
    return quote(value, safe="-._~")


def _event_roles(sample: dict[str, Any]) -> dict[str, str]:
    role_sets: dict[str, set[str]] = {}
    for link in sample.get("causal_links", []):
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


def _iter_units(units: Any) -> Iterable[dict[str, Any]]:
    if not isinstance(units, list):
        return
    for unit in units:
        if not isinstance(unit, dict):
            continue
        yield unit
        yield from _iter_units(unit.get("attributes", []))
        yield from _iter_units(unit.get("children", []))


def _strings(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str) and item]


def _required_string(record: dict[str, Any], field: str, context: str) -> str:
    value = record.get(field)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{context} is missing {field}")
    return value


def _validate_base_namespace(base_namespace: str) -> None:
    if not isinstance(base_namespace, str) or not base_namespace.startswith(("https://", "http://")):
        raise ValueError("base_namespace must be an HTTP(S) namespace")
    if not base_namespace.endswith(("/", "#")):
        raise ValueError("base_namespace must end with / or #")
