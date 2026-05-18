"""SPEC_03：构造因果抽取 prompt 与 OpenAI messages。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol


PROMPT_PATH = Path(__file__).resolve().parents[1] / "prompts" / "v1.txt"


class RetrieverProtocol(Protocol):
    """PatternRetriever 的最小接口。"""

    def retrieve(self, text: str, top_k: int) -> list[dict[str, object]]:
        """检索 top-k 个 few-shot examples。"""


def build_messages(
    text: str,
    use_rag: bool,
    retriever: RetrieverProtocol | None,
    top_k: int,
) -> list[dict[str, str]]:
    """根据 RAG 开关构造 OpenAI chat messages。"""
    template = PROMPT_PATH.read_text(encoding="utf-8")
    rag_examples = ""
    if use_rag:
        if retriever is None:
            raise ValueError("use_rag=True 时必须提供 retriever")
        examples = retriever.retrieve(text, top_k)
        rag_examples = format_rag_examples(examples)

    system_content = template.replace("{rag_examples}", rag_examples).replace("{input_text}", text)
    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": text},
    ]


def format_rag_examples(examples: list[dict[str, object]]) -> str:
    """将检索结果转换成 prompt 中的 JSON few-shot examples。"""
    if not examples:
        return ""

    blocks = ["Retrieved Pattern RAG examples:"]
    for index, example in enumerate(examples, start=1):
        output = {
            "has_causal": True,
            "triples": [
                {
                    "cause": {"span": str(example["cause"])},
                    "relation": "caused",
                    "effect": {"span": str(example["effect"])},
                }
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
