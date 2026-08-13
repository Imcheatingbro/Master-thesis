"""SPEC_03：构造因果抽取 prompt 与 OpenAI messages。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol


PROMPT_DIR = Path(__file__).resolve().parents[1] / "prompts"
DEFAULT_PROMPT_NAME = "v1"


class RetrieverProtocol(Protocol):
    """RAG 检索器的最小接口。"""

    def retrieve(self, text: str, top_k: int) -> list[dict[str, object]]:
        """检索 top-k 个 few-shot examples。"""


def build_messages(
    text: str,
    use_rag: bool,
    retriever: RetrieverProtocol | None,
    top_k: int,
    rag_mode: str = "pattern",
    prompt_name: str = DEFAULT_PROMPT_NAME,
) -> list[dict[str, str]]:
    """根据 RAG 开关与模式构造 OpenAI chat messages。"""
    template = load_prompt_template(prompt_name)
    rag_examples = ""
    if use_rag:
        if retriever is None:
            raise ValueError("use_rag=True 时必须提供 retriever")
        examples = retriever.retrieve(text, top_k)
        rag_examples = format_rag_examples(examples, rag_mode=rag_mode)

    system_content = template.replace("{rag_examples}", rag_examples)
    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": text},
    ]


def load_prompt_template(prompt_name: str = DEFAULT_PROMPT_NAME) -> str:
    """按 prompt 名称读取模板文件。"""
    safe_name = Path(prompt_name).name
    prompt_filename = safe_name if safe_name.endswith(".txt") else f"{safe_name}.txt"
    prompt_path = PROMPT_DIR / prompt_filename
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt 模板不存在: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")


def format_rag_examples(examples: list[dict[str, object]], rag_mode: str = "pattern") -> str:
    """将检索结果转换成 prompt 中的 JSON few-shot examples。"""
    if not examples:
        return ""

    blocks = [f"Retrieved {_rag_mode_label(rag_mode)} examples:"]
    for index, example in enumerate(examples, start=1):
        triples = _example_triples(example)
        output = {
            "has_causal": True,
            "triples": [
                {
                    "cause": {"span": triple["cause"]},
                    "relation": "caused",
                    "effect": {"span": triple["effect"]},
                }
                for triple in triples
            ],
        }
        blocks.append(
            "\n".join(
                [
                    f"Example {index}:",
                    f"Input: {example['sentence']}",
                    "Output:",
                    json.dumps(output, ensure_ascii=False, separators=(",", ": ")),
                ]
            )
        )
    return "\n\n".join(blocks)


def _example_triples(example: dict[str, object]) -> list[dict[str, str]]:
    raw_triples = example.get("triples")
    triples: list[dict[str, str]] = []
    if isinstance(raw_triples, list):
        for raw_triple in raw_triples:
            if not isinstance(raw_triple, dict):
                continue
            cause = _span_text(raw_triple.get("cause"))
            effect = _span_text(raw_triple.get("effect"))
            if cause and effect:
                triples.append({"cause": cause, "effect": effect})
    if triples:
        return triples

    cause = _span_text(example.get("cause"))
    effect = _span_text(example.get("effect"))
    return [{"cause": cause, "effect": effect}] if cause and effect else []


def _span_text(value: object) -> str:
    if isinstance(value, dict):
        value = value.get("span", "")
    return str(value or "").strip()


def _rag_mode_label(rag_mode: str) -> str:
    labels = {
        "pattern": "Pattern RAG",
        "knn": "KNN RAG",
        "knn_pattern": "KNN+Pattern RAG",
    }
    return labels.get(rag_mode.strip().lower(), "RAG")
