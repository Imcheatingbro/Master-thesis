"""SPEC_06：从因果 span 中提取两层 Event 结构并组装 KG JSON。"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any

from src.llm_client import LLMEmptyContentError


LOGGER = logging.getLogger(__name__)
PROMPT_DIR = Path(__file__).resolve().parents[1] / "prompts"
DEFAULT_EVENT_PROMPT_VERSION = "v1"
NUEXTRACT_DEPTH2_PROMPT_VERSION = "nuextract_v2"

NUEXTRACT_COMPONENT_ROLES = [
    "Action",
    "Actor",
    "Theme",
    "Object",
    "Location",
    "Time",
    "Instrument",
    "Manner",
    "State",
    "Description",
    "Event",
    "Organization",
    "Case",
    "Other",
]
NUEXTRACT_ATTRIBUTE_ROLES = [
    "Quantifier",
    "Attribute",
    "Description",
    "Nationality",
    "Age",
    "Type",
    "Cost",
    "Name",
    "Modifier",
    "Negation",
    "Possessor",
    "Result",
    "Topic",
    "Time",
    "Location",
    "Other",
]


def extract_event(
    span: str,
    role: str,
    client: Any,
    prompt_version: str = DEFAULT_EVENT_PROMPT_VERSION,
    max_retry: int = 2,
) -> dict[str, Any]:
    """对单个 cause/effect span 提取两层 Event 结构。"""
    last_error: Exception | None = None
    for attempt in range(1, max_retry + 1):
        try:
            raw_output = str(client.chat(_build_event_messages(span, role, prompt_version)))
            parsed = parse_event_output(raw_output)
            event = {"span": span, "components": parsed["components"]}
            _filter_to_span_substrings(event)
            return event
        except Exception as exc:
            last_error = exc
            LOGGER.warning(
                "Event 提取失败：role=%s attempt=%s/%s error=%s",
                role,
                attempt,
                max_retry,
                exc,
            )
            if any(isinstance(item, LLMEmptyContentError) for item in _iter_error_chain(exc)):
                break

    LOGGER.error("Event 提取兜底：role=%s span=%s error=%s", role, span, last_error)
    return {
        "span": span,
        "components": [],
        "error_type": classify_event_error(last_error),
        "error_message": str(last_error) if last_error is not None else "",
    }


def parse_event_output(raw_str: str) -> dict[str, Any]:
    """解析 LLM 输出为 `{"components": [...]}`，兼容 markdown 与前缀文本。"""
    cleaned = re.sub(r"<think>.*?</think>", "", raw_str, flags=re.DOTALL | re.IGNORECASE).strip()
    json_text = _extract_json_from_markdown(cleaned) or _extract_first_json_object(cleaned)
    if json_text is None:
        raise ValueError("未找到 JSON 对象")

    parsed = json.loads(json_text)
    if not isinstance(parsed, dict):
        raise ValueError("Event 输出必须是 JSON object")
    components = parsed.get("components")
    if not isinstance(components, list):
        raise ValueError("Event 输出缺少 components 列表")
    normalized_components = [_normalize_component(component) for component in components]
    return {"components": [component for component in normalized_components if component is not None]}


def build_nuextract_depth2_template() -> dict[str, Any]:
    """构造 NuExtract 2.0 的两层 component/attribute 抽取模板。"""
    return {
        "components": [
            {
                "role": list(NUEXTRACT_COMPONENT_ROLES),
                "value": "verbatim-string",
                "attributes": [
                    {
                        "role": list(NUEXTRACT_ATTRIBUTE_ROLES),
                        "value": "verbatim-string",
                    }
                ],
            }
        ]
    }


def build_kg_json(
    sample_id: int | None,
    text: str,
    triples: list[dict[str, Any]],
    client: Any,
    prompt_version: str = DEFAULT_EVENT_PROMPT_VERSION,
    triple_source: str = "pred",
    max_retry: int = 2,
) -> dict[str, Any]:
    """把一个样本内的多条 causal triples 组装成同一份 KG JSON。"""
    events: dict[str, dict[str, Any]] = {}
    causal_links: list[dict[str, Any]] = []

    for index, triple in enumerate(triples):
        cause_span = _triple_span(triple, "cause")
        effect_span = _triple_span(triple, "effect")
        if not cause_span or not effect_span:
            LOGGER.warning("跳过缺少 cause/effect span 的 triple：sample_id=%s index=%s", sample_id, index)
            continue

        cause_event_id = f"triple_{index}_cause"
        effect_event_id = f"triple_{index}_effect"
        events[cause_event_id] = extract_event(
            span=cause_span,
            role="cause",
            client=client,
            prompt_version=prompt_version,
            max_retry=max_retry,
        )
        events[effect_event_id] = extract_event(
            span=effect_span,
            role="effect",
            client=client,
            prompt_version=prompt_version,
            max_retry=max_retry,
        )
        causal_links.append(
            {
                "relation": str(triple.get("relation", "caused")),
                "cause_event": cause_event_id,
                "effect_event": effect_event_id,
                "triple_index": index,
            }
        )

    return {
        "id": sample_id,
        "text": text,
        "triple_source": triple_source,
        "causal_links": causal_links,
        "events": events,
    }


def classify_event_error(error: Exception | None) -> str:
    """把 Event 提取失败归类，便于 notebook 展示和后续统计。"""
    if error is None:
        return "unknown_event_extraction_error"

    chain = list(_iter_error_chain(error))
    message = " ".join(str(item) for item in chain)
    lower_message = message.lower()
    if any(isinstance(item, LLMEmptyContentError) for item in chain):
        if "reasoning_content" in lower_message:
            return "llm_reasoning_only_empty_content"
        return "llm_empty_content"
    if any(isinstance(item, json.JSONDecodeError) for item in chain):
        return "invalid_json_syntax"
    if "json" in lower_message and ("未找到" in message or "not found" in lower_message):
        return "no_json_object"
    if "components" in lower_message or "component" in lower_message:
        return "invalid_event_schema"
    return "unknown_event_extraction_error"


def _build_event_messages(span: str, role: str, prompt_version: str) -> list[dict[str, str]]:
    if Path(prompt_version).stem == NUEXTRACT_DEPTH2_PROMPT_VERSION:
        return _build_nuextract_depth2_messages(span)

    prompt = _load_event_prompt(prompt_version)
    user_content = "\n".join(
        [
            f"Role: {role}",
            f"Span: {span}",
            "Output the event JSON object now.",
        ]
    )
    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_content},
    ]


def _build_nuextract_depth2_messages(span: str) -> list[dict[str, str]]:
    template_text = json.dumps(build_nuextract_depth2_template(), ensure_ascii=False, indent=2)
    return [
        {
            "role": "user",
            "content": f"# Template:\n{template_text}\n# Context:\n{span}",
        }
    ]


def _load_event_prompt(prompt_version: str) -> str:
    safe_version = Path(prompt_version).stem
    if safe_version.startswith("event_extraction_"):
        prompt_name = f"{safe_version}.txt"
    else:
        prompt_name = f"event_extraction_{safe_version}.txt"
    prompt_path = PROMPT_DIR / prompt_name
    if not prompt_path.exists():
        raise FileNotFoundError(f"Event prompt 模板不存在: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")


def _normalize_component(component: Any) -> dict[str, Any] | None:
    if not isinstance(component, dict):
        raise ValueError("component 必须是 object")
    role = component.get("role")
    value = component.get("value")
    attributes = component.get("attributes", [])
    if not isinstance(role, str) or not role.strip():
        raise ValueError("component.role 必须是非空字符串")
    if value is None or value == "":
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError("component.value 必须是非空字符串")
    if not isinstance(attributes, list):
        raise ValueError("component.attributes 必须是列表")
    normalized_attributes = [_normalize_attribute(attribute) for attribute in attributes]
    normalized = {
        "role": role.strip(),
        "value": value.strip(),
        "attributes": [attribute for attribute in normalized_attributes if attribute is not None],
    }
    children = component.get("children", [])
    if children:
        if not isinstance(children, list):
            raise ValueError("component.children 必须是列表")
        normalized_children = [_normalize_component(child) for child in children]
        normalized["children"] = [child for child in normalized_children if child is not None]
    return normalized


def _normalize_attribute(attribute: Any) -> dict[str, str] | None:
    if not isinstance(attribute, dict):
        raise ValueError("attribute 必须是 object")
    role = attribute.get("role")
    value = attribute.get("value")
    if not isinstance(role, str) or not role.strip():
        raise ValueError("attribute.role 必须是非空字符串")
    if value is None or value == "":
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError("attribute.value 必须是非空字符串")
    return {"role": role.strip(), "value": value.strip()}


def _filter_to_span_substrings(event: dict[str, Any]) -> None:
    span = str(event.get("span", ""))
    warnings: list[dict[str, str]] = []
    event["components"] = _filter_components_to_span(event.get("components", []), span, warnings)
    if warnings:
        event["warnings"] = warnings


def _filter_components_to_span(
    components: list[dict[str, Any]],
    span: str,
    warnings: list[dict[str, str]],
) -> list[dict[str, Any]]:
    kept_components: list[dict[str, Any]] = []
    for component in components:
        component_value = str(component.get("value", ""))
        if component_value not in span:
            warnings.append(
                {
                    "type": "component_value_not_in_span",
                    "role": str(component.get("role", "")),
                    "value": component_value,
                }
            )
            continue

        component["attributes"] = _filter_attributes_to_span(component.get("attributes", []), span, warnings)
        if "children" in component:
            component["children"] = _filter_components_to_span(component.get("children", []), span, warnings)
        kept_components.append(component)
    return kept_components


def _filter_attributes_to_span(
    attributes: list[dict[str, str]],
    span: str,
    warnings: list[dict[str, str]],
) -> list[dict[str, str]]:
    kept_attributes = []
    for attribute in attributes:
        attribute_value = str(attribute.get("value", ""))
        if attribute_value in span:
            kept_attributes.append(attribute)
        else:
            warnings.append(
                {
                    "type": "attribute_value_not_in_span",
                    "role": str(attribute.get("role", "")),
                    "value": attribute_value,
                }
            )
    return kept_attributes


def _triple_span(triple: dict[str, Any], key: str) -> str:
    value = triple.get(key, "")
    if isinstance(value, dict):
        return str(value.get("span", "")).strip()
    return str(value).strip()


def _iter_error_chain(error: Exception) -> list[Exception]:
    chain: list[Exception] = []
    current: BaseException | None = error
    while isinstance(current, Exception) and current not in chain:
        chain.append(current)
        current = current.__cause__ or current.__context__
    return chain


def _extract_json_from_markdown(text: str) -> str | None:
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL | re.IGNORECASE)
    return match.group(1) if match else None


def _extract_first_json_object(text: str) -> str | None:
    start = text.find("{")
    if start < 0:
        return None

    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return None
