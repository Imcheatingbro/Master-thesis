"""SPEC_03：基于 causal pattern 的 few-shot example 检索器。"""

from __future__ import annotations

import csv
import logging
import re
from pathlib import Path
from typing import Any

from rapidfuzz import fuzz


LOGGER = logging.getLogger(__name__)
DEFAULT_PATTERN_DB_PATH = (
    Path(__file__).resolve().parents[1] / "RAG Database" / "comb_SCITEsemADE_CausalityPattern.csv"
)


class PatternRetriever:
    """从 causal pattern database 中检索与输入文本相似的 examples。"""

    def __init__(self, pattern_db_path: Path | str = DEFAULT_PATTERN_DB_PATH) -> None:
        self.pattern_db_path = Path(pattern_db_path)
        self.examples = self._load_examples(self.pattern_db_path)

    @staticmethod
    def _load_examples(pattern_db_path: Path) -> list[dict[str, str]]:
        examples: list[dict[str, str]] = []
        with pattern_db_path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                phrase = (row.get("causality_phrase") or "").strip()
                if not phrase:
                    continue
                examples.append(
                    {
                        "sentence": row.get("sentence", ""),
                        "cause": row.get("cause_t", ""),
                        "effect": row.get("effect_t", ""),
                        "causality_phrase": phrase,
                    }
                )
        LOGGER.info("Pattern DB 已加载：path=%s examples=%s", pattern_db_path, len(examples))
        return examples

    def retrieve(self, text: str, top_k: int = 3) -> list[dict[str, Any]]:
        """返回 top-k 个 Pattern RAG examples。"""
        if top_k <= 0:
            return []

        scored = []
        for index, example in enumerate(self.examples):
            phrase_score = self._phrase_score(text, example["causality_phrase"])
            overlap_score = self._token_overlap_score(text, example)
            score = phrase_score + overlap_score
            if score > 0:
                scored.append((score, phrase_score, overlap_score, index, example))

        scored.sort(key=lambda item: (-item[0], -item[1], -item[2], item[3]))
        return [
            {
                "sentence": example["sentence"],
                "cause": example["cause"],
                "effect": example["effect"],
                "causality_phrase": example["causality_phrase"],
                "score": round(score, 4),
            }
            for score, _phrase_score, _overlap_score, _index, example in scored[:top_k]
        ]

    @staticmethod
    def _phrase_score(text: str, phrase: str) -> float:
        normalized_text = text.lower()
        normalized_phrase = phrase.lower().strip()
        if not normalized_phrase:
            return 0.0
        if normalized_phrase in normalized_text:
            return 100.0
        if len(normalized_text) < len(normalized_phrase):
            return 0.0

        scores = []
        window_size = len(normalized_phrase)
        for start in range(len(normalized_text) - window_size + 1):
            window = normalized_text[start : start + window_size]
            score = float(fuzz.ratio(window, normalized_phrase))
            if score > 90:
                scores.append(score)
        return max(scores, default=0.0)

    @staticmethod
    def _token_overlap_score(text: str, example: dict[str, str]) -> float:
        text_tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
        example_tokens = set(
            re.findall(
                r"[a-z0-9]+",
                " ".join([example["sentence"], example["cause"], example["effect"]]).lower(),
            )
        )
        if not text_tokens or not example_tokens:
            return 0.0
        overlap = len(text_tokens & example_tokens) / len(text_tokens)
        return overlap * 10.0
