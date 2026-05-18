"""SPEC_03：Prompt 组装逻辑的单元测试。"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.prompt_builder import build_messages


class FakeRetriever:
    """测试用固定检索器。"""

    def retrieve(self, text: str, top_k: int) -> list[dict[str, object]]:
        return [
            {
                "sentence": "<cause>Rain</cause> caused <effect>flooding</effect>.",
                "cause": "Rain",
                "effect": "flooding",
                "causality_phrase": "caused",
                "score": 99.0,
            }
        ][:top_k]


def test_build_messages_without_rag_omits_retrieved_examples() -> None:
    messages = build_messages("Smoking causes lung cancer.", use_rag=False, retriever=None, top_k=0)

    assert [message["role"] for message in messages] == ["system", "user"]
    assert "Smoking causes lung cancer." in messages[1]["content"]
    assert "Retrieved Pattern RAG examples" not in messages[0]["content"]
    assert "weak or implicit causal relations" in messages[0]["content"]


def test_build_messages_with_rag_includes_retrieved_examples() -> None:
    messages = build_messages(
        "Heavy rain caused flooding.",
        use_rag=True,
        retriever=FakeRetriever(),
        top_k=1,
    )

    system_content = messages[0]["content"]
    assert "Retrieved Pattern RAG examples" in system_content
    assert '"cause": {"span": "Rain"}' in system_content
    assert '"effect": {"span": "flooding"}' in system_content
