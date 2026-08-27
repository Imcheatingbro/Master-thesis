"""SPEC_03：Prompt 组装逻辑的单元测试。"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.prompt_builder import build_messages, format_rag_examples, load_prompt_template


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


def test_cnc_sft_v2_prompt_matches_training_message_format() -> None:
    text = "Heavy rain caused flooding."
    messages = build_messages(
        text,
        use_rag=False,
        retriever=None,
        top_k=0,
        prompt_name="cnc_sft_v2",
    )

    assert messages[0]["role"] == "system"
    assert messages[0]["content"] == load_prompt_template("cnc_sft_v2").strip()
    assert messages[1] == {"role": "user", "content": f"Input text:\n{text}"}
    assert "Extract all supported relations" in messages[0]["content"]
    assert "smallest complete event" in messages[0]["content"]
    assert "{rag_examples}" not in messages[0]["content"]
    assert "Example" not in messages[0]["content"]


def test_load_prompt_template_supports_dotted_prompt_names() -> None:
    prompt = load_prompt_template("v6.1")

    assert "adverse drug event extraction system" in prompt
    assert "known drug properties" in prompt


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


def test_format_rag_examples_labels_random_control() -> None:
    rendered = format_rag_examples(
        [
            {
                "sentence": "Rain caused flooding.",
                "cause": "Rain",
                "effect": "flooding",
            }
        ],
        rag_mode="random",
    )

    assert "Retrieved Random-control RAG examples:" in rendered


def test_format_rag_examples_preserves_all_cnc_triples() -> None:
    rendered = format_rag_examples(
        [
            {
                "sentence": "The outage stopped trains and caused delays.",
                "triples": [
                    {"cause": "The outage", "effect": "stopped trains"},
                    {"cause": "The outage", "effect": "delays"},
                ],
                "signals": ["caused"],
            }
        ],
        rag_mode="knn",
    )

    assert rendered.count('"relation": "caused"') == 2
    assert '"effect": {"span": "stopped trains"}' in rendered
    assert '"effect": {"span": "delays"}' in rendered


def test_v13_prompt_inserts_dynamic_rag_examples() -> None:
    messages = build_messages(
        "Heavy rain caused flooding.",
        use_rag=True,
        retriever=FakeRetriever(),
        top_k=1,
        rag_mode="knn",
        prompt_name="v13",
    )

    assert "Retrieved KNN RAG examples:" in messages[0]["content"]
    assert "<cause>Rain</cause> caused <effect>flooding</effect>." in messages[0]["content"]


def test_v14_prompt_is_compact_recall_oriented_and_rag_ready() -> None:
    prompt = load_prompt_template("v14")

    assert prompt.count("\nInput:\n") == 2
    assert "do not stop after finding the first relation" in prompt
    assert "Output all relations supported" in prompt
    assert "A missing speculative triple costs less" not in prompt
    assert prompt.count("{rag_examples}") == 1
    assert len(prompt) < 8000

    messages = build_messages(
        "Heavy rain caused flooding.",
        use_rag=True,
        retriever=FakeRetriever(),
        top_k=1,
        rag_mode="knn",
        prompt_name="v14",
    )
    assert "Retrieved KNN RAG examples:" in messages[0]["content"]


def test_v17_prompt_is_anchor_oriented_and_keeps_fixed_examples_bounded() -> None:
    prompt = load_prompt_template("v17")

    assert "HIGHEST PRIORITY: ANCHOR-SAFE SPAN BOUNDARIES" in prompt
    assert "prefer the WIDEST DEFENSIBLE CONTINUOUS CLAUSE" in prompt
    assert "Never use the whole sentence as both arguments" in prompt
    assert prompt.count("Fixed example ") == 10
    assert prompt.count("{rag_examples}") == 1
    assert "Jitin Das" not in prompt
    assert "Falcon Tyres" not in prompt

    messages = build_messages(
        "Heavy rain caused flooding.",
        use_rag=True,
        retriever=FakeRetriever(),
        top_k=1,
        rag_mode="knn",
        prompt_name="v17",
    )

    assert "{rag_examples}" not in messages[0]["content"]
    assert "Retrieved KNN RAG examples:" in messages[0]["content"]


def test_v98_prompt_preserves_mixed_cnc_detection_and_adds_anchor_boundaries() -> None:
    prompt = load_prompt_template("v9.8")

    assert "STAGE 1: CNC CAUSALITY DECISION" in prompt
    assert "STAGE 2: ANCHOR-SAFE SPAN BOUNDARIES" in prompt
    assert "prefer the WIDEST DEFENSIBLE CONTINUOUS VERSION OF THE SAME EVENT" in prompt
    assert '{"has_causal": false, "triples": []}' in prompt
    assert prompt.count("\nInput:\n") == 10
    assert prompt.count("{rag_examples}") == 1
    assert "Adhir Chowdhury" not in prompt
    assert "Chale was allegedly chased" not in prompt
    assert "All the 417 guards" not in prompt

    messages = build_messages(
        "Heavy rain caused flooding.",
        use_rag=True,
        retriever=FakeRetriever(),
        top_k=1,
        rag_mode="knn",
        prompt_name="v9.8",
    )

    assert "{rag_examples}" not in messages[0]["content"]
    assert "Retrieved KNN RAG examples:" in messages[0]["content"]


def test_v96_prompt_contains_ten_fixed_examples() -> None:
    prompt = load_prompt_template("v9.6")
    zero_shot_prompt = load_prompt_template("v9.6_zero_shot")
    v98_prompt = load_prompt_template("v9.8")
    v98_zero_shot_prompt = load_prompt_template("v9.8_zero_shot")

    assert prompt.count("\nInput:\n") == 10
    assert "Raman was chased by a crowd" in prompt
    assert "opposition legislator Mira Sen" in prompt
    assert "in which twelve people were injured" in prompt
    assert "Anchor-safe span boundaries:" in prompt
    assert "CNC non-causal checks:" in prompt
    assert "Neither span may contain the other argument in full" in prompt
    assert prompt.split("\nExamples:\n", 1)[0].strip() == zero_shot_prompt.split("\n{rag_examples}", 1)[0].strip()
    assert abs(len(prompt.split()) - len(v98_prompt.split())) <= 200
    assert abs(len(zero_shot_prompt.split()) - len(v98_zero_shot_prompt.split())) <= 200


def test_v102_adapts_gemma_staging_to_li_short_anchors() -> None:
    prompt = load_prompt_template("v10.2")
    v101_prompt = load_prompt_template("v10.1")

    assert "STAGE 1: LI EXPLICIT CAUSALITY DECISION" in prompt
    assert "STAGE 2: LI SHORT ENTITY ANCHORS" in prompt
    assert "STAGE 3: COMPLETE RELATION COVERAGE" in prompt
    assert "prefer the shortest defensible entity anchor" in prompt
    assert "Do not copy the CNC convention" in prompt
    assert "Do not create a Cartesian product across unrelated causal frames" in prompt
    assert prompt.count("\nInput:\n") == v101_prompt.count("\nInput:\n") == 11
    assert prompt.split("\nExamples:\n", 1)[1] == v101_prompt.split("\nExamples:\n", 1)[1]


def test_cnc_gemma_v1_preserves_v98_logic_without_repeated_sft_examples() -> None:
    prompt = load_prompt_template("cnc_gemma_v1")
    qwen_sft_prompt = load_prompt_template("cnc_sft_v2")

    assert "CNC causality decision:" in prompt
    assert "Anchor-oriented span boundaries:" in prompt
    assert "Prefer the WIDEST DEFENSIBLE CONTINUOUS VERSION OF THE SAME EVENT" in prompt
    assert "Thinking is disabled:" in prompt
    assert "Fictional examples" not in prompt
    assert "\nInput:\n" not in prompt
    assert "{rag_examples}" not in prompt
    assert len(prompt) < len(qwen_sft_prompt)

    messages = build_messages(
        "Heavy rain caused flooding.",
        use_rag=False,
        retriever=None,
        top_k=0,
        prompt_name="cnc_gemma_v1",
    )

    assert messages[0]["content"] == prompt.strip()
    assert messages[1]["content"] == "Input text:\nHeavy rain caused flooding."


def test_cnc_gemma_v2_matches_12b_training_message_format() -> None:
    prompt = load_prompt_template("cnc_gemma_v2")
    messages = build_messages(
        "Heavy rain caused flooding.",
        use_rag=False,
        retriever=None,
        top_k=0,
        prompt_name="cnc_gemma_v2",
    )

    assert messages[0]["content"] == prompt.strip()
    assert messages[1]["content"] == "Input text:\nHeavy rain caused flooding."
    assert "Anchor-safe span boundaries:" in prompt


def test_cnc_gemma_v4_triples_only_removes_redundant_decision_field() -> None:
    prompt = load_prompt_template("cnc_gemma_v4_triples_only")
    messages = build_messages(
        "Heavy rain caused flooding.",
        use_rag=False,
        retriever=None,
        top_k=0,
        prompt_name="cnc_gemma_v4_triples_only",
    )

    assert messages[0]["content"] == prompt.strip()
    assert messages[1]["content"] == "Input text:\nHeavy rain caused flooding."
    assert '"triples":[]' in prompt
    assert "has_causal" not in prompt


def test_v5_prompt_preserves_general_rules_and_adds_multi_causal_boundary_example() -> None:
    prompt = load_prompt_template("v5")

    assert "Output strict JSON object only." in prompt
    assert "Do not output reasoning" in prompt
    assert "Extract all causal triples in the input text." in prompt
    assert "complete event/state spans" in prompt
    assert "Treat purpose clauses" in prompt
    assert "Treat \"when\", \"after\", \"following\", or \"once\" as causal" in prompt
    assert "Do not merge the effect of one causal relation with another downstream event." in prompt
    assert "Critical span copying rule" in prompt
    assert "Never use ellipses" in prompt
    assert '"span": "..."' not in prompt
    assert "EXACT_ORIGINAL_CAUSE_SUBSTRING" in prompt
    assert "EXACT_ORIGINAL_EFFECT_SUBSTRING" in prompt
    assert "Video of the clashes emerged on Monday" in prompt
    assert "fuelling public anger" in prompt
    assert "failing to prevent the attack" in prompt
    assert "residents demanded explanations from officials" in prompt
    assert "the factory spill" in prompt
    assert "the tanker accident" in prompt
    assert "the river contamination" in prompt
    assert "Maya Chen , the lead researcher in the project related to repairs at the coastal observatory , could not appear before the review board on Thursday" in prompt
    assert "logistics staff in Northport failed to arrange transport for her" in prompt
    assert "Maya Chen ... could not appear" not in prompt
    assert "Anoop George" not in prompt
