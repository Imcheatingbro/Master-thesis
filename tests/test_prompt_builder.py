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
    assert "Input text:" not in messages[0]["content"]
    assert "Retrieved Pattern RAG examples" not in messages[0]["content"]
    assert "weak or implicit causal relations" in messages[0]["content"]
    assert "include its subject" in messages[0]["content"]
    assert "including time, location, dates, quantities, numbers, ages" in messages[0]["content"]
    assert '"effect": {"span": "the guards to evacuate the building"}' in messages[0]["content"]


def test_build_messages_supports_prompt_name_selection() -> None:
    messages = build_messages(
        "Smoking causes lung cancer.",
        use_rag=False,
        retriever=None,
        top_k=0,
        prompt_name="v1",
    )

    assert "Smoking causes lung cancer." in messages[1]["content"]
    assert "causality extraction system" in messages[0]["content"]


def test_v1_prompt_includes_condition_trigger_guidance() -> None:
    messages = build_messages("The talks collapsed when the offer was rejected.", use_rag=False, retriever=None, top_k=0)

    assert '"when", "after", "following", or "once"' in messages[0]["content"]
    assert "triggers, enables, or explains the main event" in messages[0]["content"]


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


def test_build_messages_labels_knn_pattern_mode() -> None:
    messages = build_messages(
        "Heavy rain caused flooding.",
        use_rag=True,
        retriever=FakeRetriever(),
        top_k=1,
        rag_mode="knn_pattern",
    )

    assert "Retrieved KNN+Pattern RAG examples" in messages[0]["content"]
