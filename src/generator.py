"""SPEC_04：串联 prompt 构造、LLM 调用、输出解析与兜底生成。"""

from __future__ import annotations

import json
import logging
import re
from typing import Any

from src.prompt_builder import RetrieverProtocol, build_messages


LOGGER = logging.getLogger(__name__)


def call_llm(messages: list[dict[str, str]], client: Any) -> str:
    """调用 SPEC_02 的客户端并返回原始字符串。"""
    return str(client.chat(messages))


def parse_output(raw_str: str) -> dict[str, Any]:
    """将模型原始输出解析成 dict，兼容 markdown、前缀文本和 `<think>`。"""
    cleaned = re.sub(r"<think>.*?</think>", "", raw_str, flags=re.DOTALL | re.IGNORECASE).strip()
    json_text = _extract_json_from_markdown(cleaned) or _extract_first_json_object(cleaned)
    if json_text is None:
        raise ValueError("未找到 JSON 对象")

    parsed = json.loads(json_text)
    if not validate_minimal(parsed):
        missing = []
        if "has_causal" not in parsed:
            missing.append("has_causal")
        if "triples" not in parsed:
            missing.append("triples")
        if missing:
            raise ValueError(f"输出缺少字段：{', '.join(missing)}")
        raise ValueError("输出字段类型错误：has_causal 必须为 bool，triples 必须为 list")
    return parsed


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
    max_retry: int = 2,
) -> dict[str, Any]:
    """主入口：构造 prompt、调用 LLM、解析输出，失败后返回兜底结果。"""
    last_error: Exception | None = None
    for attempt in range(1, max_retry + 1):
        try:
            messages = build_messages(
                text,
                use_rag=use_rag,
                retriever=retriever,
                top_k=top_k,
                rag_mode=rag_mode,
            )
            raw_output = call_llm(messages, client)
            parsed = parse_output(raw_output)
            return {
                "id": sample_id,
                "has_causal": parsed["has_causal"],
                "triples": parsed["triples"],
            }
        except Exception as exc:
            last_error = exc
            LOGGER.warning("生成失败：sample_id=%s attempt=%s/%s error=%s", sample_id, attempt, max_retry, exc)

    LOGGER.error("生成兜底：sample_id=%s error=%s", sample_id, last_error)
    return {"id": sample_id, "has_causal": False, "triples": []}


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
