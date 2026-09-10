"""Conservative Wikipedia linking for post-processed causal KGs."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import re
from typing import Any, Iterable
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from rapidfuzz import fuzz
from urllib3.util.retry import Retry

from src.kg_postprocessor import canonical_surface_key


WIKIPEDIA_LINKING_VERSION = "wikipedia_action_api_role_guarded_v3"
WIKIPEDIA_STATUSES = frozenset({"linked", "ambiguous", "unlinked", "request_failed"})
DEFAULT_ENDPOINT = "https://en.wikipedia.org/w/api.php"
DEFAULT_USER_AGENT = "MasterThesisCausalKG/1.0 (academic research; local execution)"

_NON_ALNUM_RE = re.compile(r"[^\w\s]+", flags=re.UNICODE)
_WHITESPACE_RE = re.compile(r"\s+")
_NON_ENTITY_NER_LABELS = frozenset(
    {"CARDINAL", "DATE", "MONEY", "ORDINAL", "PERCENT", "QUANTITY", "TIME"}
)
_NAMED_ENTITY_NER_LABELS = frozenset(
    {"EVENT", "FAC", "GPE", "LANGUAGE", "LAW", "LOC", "NORP", "ORG", "PERSON", "PRODUCT", "WORK_OF_ART"}
)
_GUARDED_COMPONENT_ROLES = frozenset(
    {"Action", "Location", "Modifier", "Quantifier", "Time"}
)


def link_collection_to_wikipedia(
    integrated_kg: dict[str, Any],
    *,
    cache_path: str | Path | None = None,
    endpoint: str = DEFAULT_ENDPOINT,
    language: str = "en",
    timeout: float = 20.0,
    max_candidates: int = 5,
    fuzzy_threshold: float = 95.0,
    fuzzy_margin: float = 5.0,
    user_agent: str = DEFAULT_USER_AGENT,
    session: Any | None = None,
) -> dict[str, Any]:
    """Link every collection resource to Wikipedia using auditable rules.

    Every canonical resource is checked exactly once per call. A direct title
    or redirect is accepted unless it is a disambiguation page. Otherwise the
    top search result must pass both a strict title-similarity threshold and a
    margin over the runner-up. This is lightweight surface linking, not full
    context-sensitive entity disambiguation.
    """

    if not isinstance(integrated_kg, dict):
        raise TypeError("integrated_kg must be an object")
    if not isinstance(endpoint, str) or not endpoint.startswith("https://"):
        raise ValueError("Wikipedia endpoint must be an HTTPS URL")
    if not isinstance(language, str) or not language.strip():
        raise ValueError("language must be a non-empty string")
    if timeout <= 0:
        raise ValueError("timeout must be greater than zero")
    if not 1 <= max_candidates <= 50:
        raise ValueError("max_candidates must be between 1 and 50")
    if not 0 <= fuzzy_threshold <= 100 or not 0 <= fuzzy_margin <= 100:
        raise ValueError("fuzzy threshold and margin must be between 0 and 100")
    if not isinstance(user_agent, str) or not user_agent.strip():
        raise ValueError("user_agent must be a non-empty string")

    linked_kg = deepcopy(integrated_kg)
    resources = linked_kg.get("canonical_resources")
    if not isinstance(resources, list):
        raise ValueError("integrated_kg is missing the canonical_resources list")

    resources_by_id: dict[str, dict[str, Any]] = {}
    resource_keys: set[str] = set()
    for resource in resources:
        if not isinstance(resource, dict):
            raise ValueError("each canonical resource must be an object")
        resource_id = resource.get("resource_id")
        canonical_key = resource.get("canonical_key")
        if not all(isinstance(item, str) and item for item in (resource_id, canonical_key)):
            raise ValueError("canonical resource is missing resource_id or canonical_key")
        if resource_id in resources_by_id or canonical_key in resource_keys:
            raise ValueError("integrated_kg contains a duplicate canonical resource")
        resources_by_id[resource_id] = resource
        resource_keys.add(canonical_key)

    evidence_by_resource_id = _collect_resource_evidence(linked_kg, resources_by_id)

    cache_file = Path(cache_path) if cache_path is not None else None
    cached_entries = _load_cache(cache_file, endpoint=endpoint, language=language)
    http = session if session is not None else _build_session(user_agent)

    status_counts = {status: 0 for status in sorted(WIKIPEDIA_STATUSES)}
    cache_hit_count = 0
    api_request_count = 0
    cache_changed = False

    for resource in resources:
        canonical_key = resource["canonical_key"]
        evidence = evidence_by_resource_id[resource["resource_id"]]
        cached = cached_entries.get(canonical_key)
        if _valid_cached_result(cached, evidence_signature=evidence["signature"]):
            result = deepcopy(cached)
            result["cache_hit"] = True
            cache_hit_count += 1
        else:
            result = _lookup_resource(
                canonical_key,
                http=http,
                endpoint=endpoint,
                language=language,
                timeout=timeout,
                max_candidates=max_candidates,
                fuzzy_threshold=fuzzy_threshold,
                fuzzy_margin=fuzzy_margin,
                evidence=evidence,
            )
            api_request_count += result.pop("_api_request_count")
            result["cache_hit"] = False
            if result["status"] != "request_failed":
                cached_entries[canonical_key] = {
                    key: deepcopy(value)
                    for key, value in result.items()
                    if key != "cache_hit"
                }
                cache_changed = True

        resource["wikipedia_link"] = result
        status_counts[result["status"]] += 1

    _propagate_resource_links(linked_kg, resources_by_id)

    if cache_file is not None and (cache_changed or not cache_file.exists()):
        _write_cache(
            cache_file,
            endpoint=endpoint,
            language=language,
            entries=cached_entries,
        )

    if isinstance(linked_kg.get("ner_enrichment"), dict):
        linked_kg["ner_enrichment"]["wikipedia_linking_performed"] = True
    linked_kg["wikipedia_linking"] = {
        "version": WIKIPEDIA_LINKING_VERSION,
        "endpoint": endpoint,
        "language": language,
        "scope": "all_collection_canonical_resources",
        "semantic_disambiguation": False,
        "semantic_identity_confirmed": False,
        "selection_policy": (
            "non-disambiguation direct title/redirect or strict fuzzy title match, "
            "subject to NER/role consistency guards"
        ),
        "fuzzy_threshold": float(fuzzy_threshold),
        "fuzzy_margin": float(fuzzy_margin),
        "max_candidates": max_candidates,
        "resource_count": len(resources),
        "query_count": len(resources),
        "api_request_count": api_request_count,
        "cache_hit_count": cache_hit_count,
        "linked_count": status_counts["linked"],
        "ambiguous_count": status_counts["ambiguous"],
        "unlinked_count": status_counts["unlinked"],
        "request_failed_count": status_counts["request_failed"],
        "cache_path": str(cache_file) if cache_file is not None else None,
    }
    return linked_kg


def _lookup_resource(
    query: str,
    *,
    http: Any,
    endpoint: str,
    language: str,
    timeout: float,
    max_candidates: int,
    fuzzy_threshold: float,
    fuzzy_margin: float,
    evidence: dict[str, Any],
) -> dict[str, Any]:
    request_count = 0
    try:
        direct_data = _request_json(
            http,
            endpoint,
            {
                **_base_params(),
                "titles": query,
                "redirects": 1,
            },
            timeout=timeout,
        )
        request_count += 1
    except Exception as exc:
        return _request_failure(
            query,
            exc,
            language=language,
            evidence=evidence,
            request_count=1,
        )

    direct_page = _first_existing_page(direct_data)
    redirect = _redirect_record(direct_data, query)
    if direct_page is not None:
        candidate = _page_candidate(direct_page, query=query, language=language, rank=1)
        if candidate["is_disambiguation"]:
            return {
                **_base_result(query, language, evidence),
                "status": "ambiguous",
                "match_method": "direct_disambiguation_page",
                "confidence": None,
                "selected_page": None,
                "candidates": [candidate],
                "reason": "The direct Wikipedia title is a disambiguation page.",
                "_api_request_count": request_count,
            }
        match_method = "redirect" if redirect is not None else "direct_title"
        allowed, guard_reason = _automatic_link_allowed(
            candidate,
            match_method=match_method,
            evidence=evidence,
            fuzzy_threshold=fuzzy_threshold,
        )
        if not allowed:
            return {
                **_base_result(query, language, evidence),
                "status": "ambiguous",
                "match_method": "direct_candidate_rejected_by_role_ner_guard",
                "confidence": None,
                "selected_page": None,
                "candidates": [candidate],
                "redirect": redirect,
                "reason": guard_reason,
                "_api_request_count": request_count,
            }
        return {
            **_base_result(query, language, evidence),
            "status": "linked",
            "match_method": match_method,
            "confidence": 1.0,
            "selected_page": candidate,
            "candidates": [candidate],
            "redirect": redirect,
            "reason": "A non-disambiguation direct title or redirect was found.",
            "_api_request_count": request_count,
        }

    try:
        search_data = _request_json(
            http,
            endpoint,
            {
                **_base_params(),
                "generator": "search",
                "gsrsearch": query,
                "gsrnamespace": 0,
                "gsrlimit": max_candidates,
            },
            timeout=timeout,
        )
        request_count += 1
    except Exception as exc:
        return _request_failure(
            query,
            exc,
            language=language,
            evidence=evidence,
            request_count=request_count + 1,
        )

    pages = _existing_pages(search_data)
    pages.sort(key=lambda page: int(page.get("index", 10**9)))
    candidates = [
        _page_candidate(page, query=query, language=language, rank=index)
        for index, page in enumerate(pages[:max_candidates], start=1)
    ]
    eligible = [candidate for candidate in candidates if not candidate["is_disambiguation"]]
    eligible.sort(key=lambda item: (-item["title_similarity"], item["rank"]))

    if eligible:
        best = eligible[0]
        runner_up_score = eligible[1]["title_similarity"] if len(eligible) > 1 else 0.0
        margin = best["title_similarity"] - runner_up_score
        allowed, guard_reason = _automatic_link_allowed(
            best,
            match_method="search_title_fuzzy",
            evidence=evidence,
            fuzzy_threshold=fuzzy_threshold,
        )
        if (
            best["title_similarity"] >= fuzzy_threshold
            and margin >= fuzzy_margin
            and allowed
        ):
            return {
                **_base_result(query, language, evidence),
                "status": "linked",
                "match_method": "search_title_fuzzy",
                "confidence": round(best["title_similarity"] / 100.0, 4),
                "selected_page": best,
                "candidates": candidates,
                "runner_up_margin": round(margin, 2),
                "reason": "The top non-disambiguation title passed the threshold and margin.",
                "_api_request_count": request_count,
            }

    if candidates:
        return {
            **_base_result(query, language, evidence),
            "status": "ambiguous",
            "match_method": "search_candidates_below_threshold_or_margin",
            "confidence": None,
            "selected_page": None,
            "candidates": candidates,
            "reason": (
                guard_reason
                if eligible and not allowed
                else "Candidates exist, but deterministic selection confidence is insufficient."
            ),
            "_api_request_count": request_count,
        }
    return {
        **_base_result(query, language, evidence),
        "status": "unlinked",
        "match_method": "no_candidate",
        "confidence": None,
        "selected_page": None,
        "candidates": [],
        "reason": "Wikipedia returned no page candidate.",
        "_api_request_count": request_count,
    }


def _base_params() -> dict[str, Any]:
    return {
        "action": "query",
        "format": "json",
        "formatversion": 2,
        "prop": "info|pageprops|extracts",
        "inprop": "url",
        "ppprop": "disambiguation",
        "exintro": 1,
        "explaintext": 1,
        "exsentences": 2,
    }


def _request_json(
    http: Any,
    endpoint: str,
    params: dict[str, Any],
    *,
    timeout: float,
) -> dict[str, Any]:
    response = http.get(endpoint, params=params, timeout=timeout)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict):
        raise ValueError("Wikipedia API response is not a JSON object")
    if "error" in payload:
        raise RuntimeError(f"Wikipedia API error: {payload['error']}")
    return payload


def _first_existing_page(payload: dict[str, Any]) -> dict[str, Any] | None:
    pages = _existing_pages(payload)
    return pages[0] if pages else None


def _existing_pages(payload: dict[str, Any]) -> list[dict[str, Any]]:
    query = payload.get("query")
    pages = query.get("pages") if isinstance(query, dict) else None
    if not isinstance(pages, list):
        return []
    return [
        page
        for page in pages
        if isinstance(page, dict)
        and not page.get("missing")
        and int(page.get("ns", 0)) == 0
        and isinstance(page.get("pageid"), int)
    ]


def _redirect_record(payload: dict[str, Any], query_text: str) -> dict[str, str] | None:
    query = payload.get("query")
    redirects = query.get("redirects") if isinstance(query, dict) else None
    if not isinstance(redirects, list):
        return None
    query_key = canonical_surface_key(query_text)
    for redirect in redirects:
        if not isinstance(redirect, dict):
            continue
        source = redirect.get("from")
        target = redirect.get("to")
        if (
            isinstance(source, str)
            and isinstance(target, str)
            and canonical_surface_key(source) == query_key
        ):
            return {"from": source, "to": target}
    return None


def _page_candidate(
    page: dict[str, Any],
    *,
    query: str,
    language: str,
    rank: int,
) -> dict[str, Any]:
    title = str(page.get("title", "")).strip()
    pageprops = page.get("pageprops")
    is_disambiguation = isinstance(pageprops, dict) and "disambiguation" in pageprops
    url = page.get("canonicalurl") or page.get("fullurl")
    if not isinstance(url, str) or not url:
        url = f"https://{language}.wikipedia.org/wiki/{quote(title.replace(' ', '_'))}"
    extract = page.get("extract")
    if not isinstance(extract, str):
        extract = ""
    extract = _WHITESPACE_RE.sub(" ", extract).strip()
    return {
        "rank": rank,
        "page_id": page["pageid"],
        "title": title,
        "url": url,
        "extract": extract[:500],
        "is_disambiguation": is_disambiguation,
        "title_similarity": round(float(fuzz.ratio(_title_key(query), _title_key(title))), 2),
    }


def _title_key(value: str) -> str:
    normalized = canonical_surface_key(value).replace("_", " ").replace("-", " ")
    normalized = _NON_ALNUM_RE.sub(" ", normalized)
    return _WHITESPACE_RE.sub(" ", normalized).strip()


def _base_result(
    query: str,
    language: str,
    evidence: dict[str, Any],
) -> dict[str, Any]:
    return {
        "version": WIKIPEDIA_LINKING_VERSION,
        "query": query,
        "language": language,
        "component_roles": evidence["component_roles"],
        "ner_labels": evidence["ner_labels"],
        "evidence_signature": evidence["signature"],
        "semantic_identity_confirmed": False,
    }


def _request_failure(
    query: str,
    exc: Exception,
    *,
    language: str,
    evidence: dict[str, Any],
    request_count: int,
) -> dict[str, Any]:
    return {
        **_base_result(query, language, evidence),
        "status": "request_failed",
        "match_method": None,
        "confidence": None,
        "selected_page": None,
        "candidates": [],
        "reason": "Wikipedia request failed; this is not evidence that no page exists.",
        "error_type": type(exc).__name__,
        "error_message": str(exc)[:300],
        "_api_request_count": request_count,
    }


def _automatic_link_allowed(
    candidate: dict[str, Any],
    *,
    match_method: str,
    evidence: dict[str, Any],
    fuzzy_threshold: float,
) -> tuple[bool, str]:
    """Reject obvious surface-title false positives without hiding candidates."""

    ner_labels = set(evidence["ner_labels"])
    component_roles = set(evidence["component_roles"])
    if ner_labels & _NON_ENTITY_NER_LABELS:
        return (
            False,
            "NER marks the mention as numeric/temporal rather than a named entity or concept.",
        )
    if ner_labels & _NAMED_ENTITY_NER_LABELS:
        return True, "A named-entity NER label supports automatic linking."
    if component_roles and component_roles.issubset(_GUARDED_COMPONENT_ROLES):
        return (
            False,
            "The extraction role is prone to title homonyms and has no named-entity evidence.",
        )
    if match_method == "redirect" and candidate["title_similarity"] < fuzzy_threshold:
        return (
            False,
            "The redirect target is lexically different from the extracted factor.",
        )
    return True, "The title match passed the conservative acceptance guards."


def _collect_resource_evidence(
    linked_kg: dict[str, Any],
    resources_by_id: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    roles_by_id = {resource_id: set() for resource_id in resources_by_id}
    ner_labels_by_id = {resource_id: set() for resource_id in resources_by_id}

    for resource_id, resource in resources_by_id.items():
        mentions = resource.get("mentions", [])
        if not isinstance(mentions, list):
            raise ValueError("collection resource mentions must be a list")
        for mention in mentions:
            role = mention.get("component_role") if isinstance(mention, dict) else None
            if isinstance(role, str) and role:
                roles_by_id[resource_id].add(role)

    sample_graphs = linked_kg.get("sample_graphs", [])
    if not isinstance(sample_graphs, list):
        raise ValueError("sample_graphs must be a list")
    for sample_graph in sample_graphs:
        events = sample_graph.get("events") if isinstance(sample_graph, dict) else None
        if not isinstance(events, dict):
            raise ValueError("sample graph is missing the events object")
        for event in events.values():
            components = event.get("components") if isinstance(event, dict) else None
            if not isinstance(components, list):
                raise ValueError("event is missing the components list")
            for component in components:
                for unit in _iter_units(component):
                    resource_id = unit.get("collection_resource_id")
                    if resource_id not in resources_by_id:
                        raise ValueError("factor mention references an unknown collection resource")
                    annotations = unit.get("ner_annotations", [])
                    if not isinstance(annotations, list):
                        raise ValueError("factor ner_annotations must be a list")
                    for annotation in annotations:
                        label = annotation.get("ner_label") if isinstance(annotation, dict) else None
                        if isinstance(label, str) and label:
                            ner_labels_by_id[resource_id].add(label)

    ner_mentions = linked_kg.get("ner_mentions", [])
    if not isinstance(ner_mentions, list):
        raise ValueError("ner_mentions must be a list")
    for mention in ner_mentions:
        resource_id = mention.get("collection_resource_id") if isinstance(mention, dict) else None
        label = mention.get("ner_label") if isinstance(mention, dict) else None
        if resource_id not in resources_by_id:
            raise ValueError("NER mention references an unknown collection resource")
        if isinstance(label, str) and label:
            ner_labels_by_id[resource_id].add(label)

    evidence: dict[str, dict[str, Any]] = {}
    for resource_id in resources_by_id:
        roles = sorted(roles_by_id[resource_id])
        labels = sorted(ner_labels_by_id[resource_id])
        evidence[resource_id] = {
            "component_roles": roles,
            "ner_labels": labels,
            "signature": f"roles={','.join(roles)};ner={','.join(labels)}",
        }
    return evidence


def _compact_link(link: dict[str, Any]) -> dict[str, Any]:
    selected = link.get("selected_page")
    return {
        "status": link["status"],
        "query": link["query"],
        "match_method": link.get("match_method"),
        "page_id": selected.get("page_id") if isinstance(selected, dict) else None,
        "title": selected.get("title") if isinstance(selected, dict) else None,
        "url": selected.get("url") if isinstance(selected, dict) else None,
    }


def _propagate_resource_links(
    linked_kg: dict[str, Any],
    resources_by_id: dict[str, dict[str, Any]],
) -> None:
    links_by_id = {
        resource_id: _compact_link(resource["wikipedia_link"])
        for resource_id, resource in resources_by_id.items()
    }
    for resource_id, resource in resources_by_id.items():
        compact = links_by_id[resource_id]
        mentions = resource.get("mentions", [])
        if not isinstance(mentions, list):
            raise ValueError("collection resource mentions must be a list")
        for mention in mentions:
            if isinstance(mention, dict):
                mention["wikipedia_link"] = deepcopy(compact)

    sample_graphs = linked_kg.get("sample_graphs", [])
    if not isinstance(sample_graphs, list):
        raise ValueError("sample_graphs must be a list")
    for sample_graph in sample_graphs:
        local_resources = sample_graph.get("canonical_resources", [])
        if not isinstance(local_resources, list):
            raise ValueError("sample canonical_resources must be a list")
        for local_resource in local_resources:
            resource_id = local_resource.get("collection_resource_id")
            if resource_id not in links_by_id:
                raise ValueError("sample-local resource references an unknown collection resource")
            local_resource["wikipedia_link"] = deepcopy(links_by_id[resource_id])

        events = sample_graph.get("events")
        if not isinstance(events, dict):
            raise ValueError("sample graph is missing the events object")
        for event in events.values():
            components = event.get("components") if isinstance(event, dict) else None
            if not isinstance(components, list):
                raise ValueError("event is missing the components list")
            for component in components:
                for unit in _iter_units(component):
                    resource_id = unit.get("collection_resource_id")
                    if resource_id not in links_by_id:
                        raise ValueError("factor mention references an unknown collection resource")
                    unit["wikipedia_link"] = deepcopy(links_by_id[resource_id])

    ner_mentions = linked_kg.get("ner_mentions", [])
    if not isinstance(ner_mentions, list):
        raise ValueError("ner_mentions must be a list")
    for mention in ner_mentions:
        resource_id = mention.get("collection_resource_id") if isinstance(mention, dict) else None
        if resource_id not in links_by_id:
            raise ValueError("NER mention references an unknown collection resource")
        mention["wikipedia_link"] = deepcopy(links_by_id[resource_id])


def _iter_units(unit: Any) -> Iterable[dict[str, Any]]:
    if not isinstance(unit, dict):
        raise ValueError("KG unit must be an object")
    yield unit
    for field in ("attributes", "children"):
        nested = unit.get(field, [])
        if nested is None:
            nested = []
        if not isinstance(nested, list):
            raise ValueError(f"KG unit {field} must be a list")
        for child in nested:
            yield from _iter_units(child)


def _build_session(user_agent: str) -> requests.Session:
    retry = Retry(
        total=2,
        connect=2,
        read=2,
        status=2,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=True,
    )
    session = requests.Session()
    session.headers.update({"User-Agent": user_agent})
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


def _valid_cached_result(
    value: Any,
    *,
    evidence_signature: str | None = None,
) -> bool:
    valid = (
        isinstance(value, dict)
        and value.get("version") == WIKIPEDIA_LINKING_VERSION
        and value.get("status") in WIKIPEDIA_STATUSES - {"request_failed"}
        and isinstance(value.get("query"), str)
    )
    if not valid:
        return False
    return evidence_signature is None or value.get("evidence_signature") == evidence_signature


def _load_cache(
    cache_path: Path | None,
    *,
    endpoint: str,
    language: str,
) -> dict[str, dict[str, Any]]:
    if cache_path is None or not cache_path.exists():
        return {}
    try:
        payload = json.loads(cache_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if (
        not isinstance(payload, dict)
        or payload.get("version") != WIKIPEDIA_LINKING_VERSION
        or payload.get("endpoint") != endpoint
        or payload.get("language") != language
        or not isinstance(payload.get("entries"), dict)
    ):
        return {}
    return {
        key: value
        for key, value in payload["entries"].items()
        if isinstance(key, str) and _valid_cached_result(value)
    }


def _write_cache(
    cache_path: Path,
    *,
    endpoint: str,
    language: str,
    entries: dict[str, dict[str, Any]],
) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": WIKIPEDIA_LINKING_VERSION,
        "endpoint": endpoint,
        "language": language,
        "entries": {key: entries[key] for key in sorted(entries)},
    }
    temporary = cache_path.with_suffix(f"{cache_path.suffix}.tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(cache_path)
