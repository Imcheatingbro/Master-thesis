"""SPEC_04：串联 prompt 构造、LLM 调用、输出解析与兜底生成。"""

from __future__ import annotations

import json
import logging
import re
from typing import Any

from src.llm_client import LLMEmptyContentError
from src.prompt_builder import DEFAULT_PROMPT_NAME, RetrieverProtocol, build_messages


LOGGER = logging.getLogger(__name__)
DUPLICATE_EFFECT_CLOSING_BRACE_REPAIR = "duplicate_effect_closing_brace"


def call_llm(messages: list[dict[str, str]], client: Any) -> str:
    """调用 SPEC_02 的客户端并返回原始字符串。"""
    return str(client.chat(messages))


def parse_output(raw_str: str) -> dict[str, Any]:
    """将模型原始输出解析成 dict，兼容 markdown、前缀文本和 `<think>`。"""
    parsed, _ = parse_output_with_metadata(raw_str)
    return parsed


def parse_output_with_metadata(raw_str: str) -> tuple[dict[str, Any], str | None]:
    """解析模型输出，并返回实际应用的受限 JSON 修复类型。"""
    cleaned = re.sub(r"<think>.*?</think>", "", raw_str, flags=re.DOTALL | re.IGNORECASE).strip()
    json_text = _extract_json_from_markdown(cleaned) or _extract_first_json_object(cleaned)
    if json_text is None:
        raise ValueError("未找到 JSON 对象")

    parsed, repair_type = _parse_json_with_limited_repair(json_text)
    if not validate_minimal(parsed):
        missing = []
        if "has_causal" not in parsed:
            missing.append("has_causal")
        if "triples" not in parsed:
            missing.append("triples")
        if missing:
            raise ValueError(f"输出缺少字段：{', '.join(missing)}")
        raise ValueError("输出字段类型错误：has_causal 必须为 bool，triples 必须为 list")
    return parsed, repair_type


def validate_minimal(data: dict[str, Any]) -> bool:
    """检查 Demo1 允许的最小字段与类型。"""
    return isinstance(data.get("has_causal"), bool) and isinstance(data.get("triples"), list)


def generate(
    text: str,
    sample_id: int | None,
    client: Any,
    retriever: RetrieverProtocol | None,
    use_rag: bool,
    top_k: int,
    rag_mode: str = "pattern",
    prompt_name: str = DEFAULT_PROMPT_NAME,
    max_retry: int = 2,
) -> dict[str, Any]:
    """主入口：构造 prompt、调用 LLM、解析输出，失败后返回兜底结果。"""
    last_error: Exception | None = None
    failed_attempts: list[dict[str, Any]] = []
    for attempt in range(1, max_retry + 1):
        raw_output: str | None = None
        try:
            messages = build_messages(
                text,
                use_rag=use_rag,
                retriever=retriever,
                top_k=top_k,
                rag_mode=rag_mode,
                prompt_name=prompt_name,
            )
            raw_output = call_llm(messages, client)
            parsed, repair_type = parse_output_with_metadata(raw_output)
            result = {
                "id": sample_id,
                "has_causal": parsed["has_causal"],
                "triples": parsed["triples"],
            }
            if repair_type is not None:
                result["parse_repair_type"] = repair_type
                result["parse_repair_raw_output"] = raw_output
            return result
        except Exception as exc:
            last_error = exc
            failed_attempts.append(
                {
                    "attempt": attempt,
                    "raw_output": raw_output,
                    "error_type": classify_generation_error(exc),
                    "error_message": str(exc),
                }
            )
            LOGGER.warning("生成失败：sample_id=%s attempt=%s/%s error=%s", sample_id, attempt, max_retry, exc)
            if any(isinstance(item, LLMEmptyContentError) for item in _iter_error_chain(exc)):
                break

    LOGGER.error("生成兜底：sample_id=%s error=%s", sample_id, last_error)
    return {
        "id": sample_id,
        "has_causal": False,
        "triples": [],
        "error_type": classify_generation_error(last_error),
        "error_message": str(last_error) if last_error is not None else "",
        "generation_attempts": failed_attempts,
    }


def classify_generation_error(error: Exception | None) -> str:
    """把生成失败归类，便于 eval report 统计主要失败来源。"""
    if error is None:
        return "unknown_generation_error"

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
    if "缺少字段" in message or "字段类型" in message or "has_causal" in message or "triples" in message:
        return "invalid_output_schema"
    return "unknown_generation_error"


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


def _parse_json_with_limited_repair(json_text: str) -> tuple[dict[str, Any], str | None]:
    try:
        return json.loads(json_text), None
    except json.JSONDecodeError as original_error:
        repaired = _repair_duplicate_effect_closing_brace(json_text)
        if repaired == json_text:
            raise
        try:
            return json.loads(repaired), DUPLICATE_EFFECT_CLOSING_BRACE_REPAIR
        except json.JSONDecodeError:
            raise original_error


def _repair_duplicate_effect_closing_brace(json_text: str) -> str:
    """删除 effect 单行对象后、独立 triple 结束符前的重复右括号。"""
    lines = json_text.splitlines()
    changed = False
    for index, line in enumerate(lines):
        stripped = line.rstrip()
        if not re.match(r'^\s*"effect"\s*:\s*\{.*\}\}\s*$', stripped):
            continue
        next_index = index + 1
        while next_index < len(lines) and not lines[next_index].strip():
            next_index += 1
        if next_index >= len(lines) or lines[next_index].strip() not in {"}", "},"}:
            continue
        lines[index] = stripped[:-1]
        changed = True
    return "\n".join(lines) if changed else json_text
