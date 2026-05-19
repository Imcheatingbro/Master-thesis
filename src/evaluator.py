"""SPEC_05：Demo1 的 detection 与 extraction 评估模块。"""

from __future__ import annotations

import re
import string
from dataclasses import dataclass
from typing import Any


FUZZY_THRESHOLD = 0.8
ARTICLES = {"a", "an", "the"}


@dataclass
class Counts:
    """保存 TP/FP/FN 计数并计算指标。"""

    tp: int = 0
    fp: int = 0
    fn: int = 0

    def add(self, tp: int, fp: int, fn: int) -> None:
        self.tp += tp
        self.fp += fp
        self.fn += fn

    def metrics(self) -> dict[str, float | int]:
        precision = _safe_div(self.tp, self.tp + self.fp)
        recall = _safe_div(self.tp, self.tp + self.fn)
        return {
            "tp": self.tp,
            "fp": self.fp,
            "fn": self.fn,
            "precision": precision,
            "recall": recall,
            "f1": _f1(precision, recall),
        }


class Evaluator:
    """流式累计 Demo1 的 detection 与 extraction 评估指标。"""

    def __init__(self, threshold: float = FUZZY_THRESHOLD) -> None:
        self.threshold = threshold
        self.reset()

    def reset(self) -> None:
        """清空所有累计指标。"""
        self.n_samples = 0
        self.n_causal_gold = 0
        self.n_causal_pred = 0
        self.det_tp = 0
        self.det_tn = 0
        self.det_fp = 0
        self.det_fn = 0
        self.all_samples_counts = Counts()
        self.detected_only_counts = Counts()
        self.all_samples_n_eval = 0
        self.all_samples_gold_triples = 0
        self.all_samples_pred_triples = 0
        self.detected_only_n_eval = 0
        self.detected_only_gold_triples = 0
        self.detected_only_pred_triples = 0

    def update(self, prediction: dict[str, Any], gold: dict[str, Any]) -> None:
        """用单条 prediction 与 gold 更新累计指标。"""
        pred_has_causal = bool(prediction.get("has_causal", False))
        gold_has_causal = bool(gold.get("has_causal", False))
        pred_triples = _as_list(prediction.get("triples"))
        gold_relations = _as_list(gold.get("relations"))

        self.n_samples += 1
        self.n_causal_gold += int(gold_has_causal)
        self.n_causal_pred += int(pred_has_causal)
        self._update_detection(pred_has_causal=pred_has_causal, gold_has_causal=gold_has_causal)
        self._update_all_samples(pred_triples=pred_triples, gold_relations=gold_relations)

        if pred_has_causal and gold_has_causal:
            self._update_detected_only(pred_triples=pred_triples, gold_relations=gold_relations)

    def report(self) -> dict[str, Any]:
        """返回完整评估报告。"""
        det_precision = _safe_div(self.det_tp, self.det_tp + self.det_fp)
        det_recall = _safe_div(self.det_tp, self.det_tp + self.det_fn)
        return {
            "n_samples": self.n_samples,
            "n_causal_gold": self.n_causal_gold,
            "n_causal_pred": self.n_causal_pred,
            "detection": {
                "tp": self.det_tp,
                "tn": self.det_tn,
                "fp": self.det_fp,
                "fn": self.det_fn,
                "accuracy": _safe_div(self.det_tp + self.det_tn, self.n_samples),
                "precision": det_precision,
                "recall": det_recall,
                "f1": _f1(det_precision, det_recall),
            },
            "extraction": {
                "all_samples": self._extraction_report(
                    self.all_samples_counts,
                    n_eval_samples=self.all_samples_n_eval,
                    n_gold_triples=self.all_samples_gold_triples,
                    n_pred_triples=self.all_samples_pred_triples,
                ),
                "detected_only": self._extraction_report(
                    self.detected_only_counts,
                    n_eval_samples=self.detected_only_n_eval,
                    n_gold_triples=self.detected_only_gold_triples,
                    n_pred_triples=self.detected_only_pred_triples,
                ),
            },
            "fuzzy_threshold": self.threshold,
        }

    def format_report(self, title: str = "Demo1 评估报告") -> str:
        """返回可读的多行文本报告；由 notebook 负责 print。"""
        report = self.report()
        detection = report["detection"]
        all_samples = report["extraction"]["all_samples"]
        detected_only = report["extraction"]["detected_only"]
        lines = [
            f"================ {title} ================",
            f"样本总数: {report['n_samples']}",
            f"  Gold 含因果: {report['n_causal_gold']} | Pred 含因果: {report['n_causal_pred']}",
            f"  模糊匹配阈值: {report['fuzzy_threshold']:.3f}",
            "",
            "[Layer 1] Detection",
            f"  Accuracy : {detection['accuracy']:.3f}",
            f"  Precision: {detection['precision']:.3f}",
            f"  Recall   : {detection['recall']:.3f}",
            f"  F1       : {detection['f1']:.3f}",
            f"  (TP={detection['tp']}, TN={detection['tn']}, FP={detection['fp']}, FN={detection['fn']})",
            "",
            "[Layer 2A] Extraction all_samples",
            "  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。",
            _format_extraction_block(all_samples),
            "",
            "[Layer 2B] Extraction detected_only",
            "  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量。",
            _format_extraction_block(detected_only),
            "================================================",
        ]
        return "\n".join(lines)

    def _update_detection(self, pred_has_causal: bool, gold_has_causal: bool) -> None:
        if gold_has_causal and pred_has_causal:
            self.det_tp += 1
        elif not gold_has_causal and not pred_has_causal:
            self.det_tn += 1
        elif not gold_has_causal and pred_has_causal:
            self.det_fp += 1
        else:
            self.det_fn += 1

    def _update_all_samples(self, pred_triples: list[Any], gold_relations: list[Any]) -> None:
        tp, fp, fn = match_triples(pred_triples, gold_relations, threshold=self.threshold)
        self.all_samples_counts.add(tp, fp, fn)
        self.all_samples_n_eval += 1
        self.all_samples_gold_triples += len(gold_relations)
        self.all_samples_pred_triples += len(pred_triples)

    def _update_detected_only(self, pred_triples: list[Any], gold_relations: list[Any]) -> None:
        tp, fp, fn = match_triples(pred_triples, gold_relations, threshold=self.threshold)
        self.detected_only_counts.add(tp, fp, fn)
        self.detected_only_n_eval += 1
        self.detected_only_gold_triples += len(gold_relations)
        self.detected_only_pred_triples += len(pred_triples)

    @staticmethod
    def _extraction_report(
        counts: Counts,
        n_eval_samples: int,
        n_gold_triples: int,
        n_pred_triples: int,
    ) -> dict[str, float | int]:
        report = counts.metrics()
        report.update(
            {
                "n_eval_samples": n_eval_samples,
                "n_gold_triples": n_gold_triples,
                "n_pred_triples": n_pred_triples,
            }
        )
        return report


def preprocess_span(text: str) -> str:
    """清洗 span：小写、去冠词、去标点、合并空格。"""
    lowered = text.lower()
    punctuation_table = str.maketrans({char: " " for char in string.punctuation})
    without_punctuation = lowered.translate(punctuation_table)
    tokens = [token for token in without_punctuation.split() if token not in ARTICLES]
    return re.sub(r"\s+", " ", " ".join(tokens)).strip()


def token_f1(pred_span: str, gold_span: str) -> float:
    """计算两个 span 的 token-level F1。"""
    pred_tokens = set(preprocess_span(pred_span).split())
    gold_tokens = set(preprocess_span(gold_span).split())
    if not pred_tokens or not gold_tokens:
        return 0.0

    overlap = pred_tokens & gold_tokens
    precision = len(overlap) / len(pred_tokens)
    recall = len(overlap) / len(gold_tokens)
    return _f1(precision, recall)


def match_triples(
    pred_triples: list[Any],
    gold_relations: list[Any],
    threshold: float = FUZZY_THRESHOLD,
) -> tuple[int, int, int]:
    """用 greedy one-to-one matching 统计 triple 级 TP/FP/FN。"""
    pair_scores = []
    for pred_index, pred_triple in enumerate(pred_triples):
        pred_cause = _pred_span(pred_triple, "cause")
        pred_effect = _pred_span(pred_triple, "effect")
        for gold_index, gold_relation in enumerate(gold_relations):
            gold_cause = str(gold_relation.get("cause", "")) if isinstance(gold_relation, dict) else ""
            gold_effect = str(gold_relation.get("effect", "")) if isinstance(gold_relation, dict) else ""
            cause_f1 = token_f1(pred_cause, gold_cause)
            effect_f1 = token_f1(pred_effect, gold_effect)
            pair_scores.append((min(cause_f1, effect_f1), pred_index, gold_index))

    matched_preds: set[int] = set()
    matched_golds: set[int] = set()
    for score, pred_index, gold_index in sorted(pair_scores, key=lambda item: item[0], reverse=True):
        if score < threshold:
            break
        if pred_index in matched_preds or gold_index in matched_golds:
            continue
        matched_preds.add(pred_index)
        matched_golds.add(gold_index)

    tp = len(matched_preds)
    fp = len(pred_triples) - tp
    fn = len(gold_relations) - tp
    return tp, fp, fn


def _pred_span(pred_triple: Any, key: str) -> str:
    if not isinstance(pred_triple, dict):
        return ""
    value = pred_triple.get(key, "")
    if isinstance(value, dict):
        return str(value.get("span", ""))
    return str(value)


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _safe_div(numerator: int, denominator: int) -> float:
    return 0.0 if denominator == 0 else numerator / denominator


def _f1(precision: float, recall: float) -> float:
    return 0.0 if precision + recall == 0 else 2 * precision * recall / (precision + recall)


def _format_extraction_block(metrics: dict[str, float | int]) -> str:
    return "\n".join(
        [
            f"  样本数: {metrics['n_eval_samples']}",
            f"  Gold triples: {metrics['n_gold_triples']} | Pred triples: {metrics['n_pred_triples']}",
            f"  Precision: {metrics['precision']:.3f}",
            f"  Recall   : {metrics['recall']:.3f}",
            f"  F1       : {metrics['f1']:.3f}",
            f"  (TP={metrics['tp']}, FP={metrics['fp']}, FN={metrics['fn']})",
        ]
    )
