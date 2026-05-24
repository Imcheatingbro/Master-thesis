"""SPEC_05：Demo1 的 detection 与 extraction 评估模块。"""

from __future__ import annotations

import difflib
import re
import string
from dataclasses import dataclass
from typing import Any, Callable


FUZZY_THRESHOLD = 0.8
ANCHOR_WINDOW_THRESHOLD = 0.9
STRICT_TOKEN_F1 = "strict_token_f1"
ANCHOR_WINDOW = "anchor_window"
PRIMARY_METRIC_BY_DATASET = {
    "cnc": STRICT_TOKEN_F1,
    "li": STRICT_TOKEN_F1,
    "ade": ANCHOR_WINDOW,
    "causenet": ANCHOR_WINDOW,
}
VALID_EXTRACTION_METRICS = {STRICT_TOKEN_F1, ANCHOR_WINDOW}
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

    def __init__(
        self,
        threshold: float = FUZZY_THRESHOLD,
        anchor_threshold: float = ANCHOR_WINDOW_THRESHOLD,
        dataset: str | None = None,
        primary_metric: str | None = None,
    ) -> None:
        self.threshold = threshold
        self.anchor_threshold = anchor_threshold
        self.dataset = dataset
        self.primary_metric = _resolve_primary_metric(dataset=dataset, primary_metric=primary_metric)
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
        self.strict_all_samples_counts = Counts()
        self.strict_detected_only_counts = Counts()
        self.anchor_all_samples_counts = Counts()
        self.anchor_detected_only_counts = Counts()
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
            "extraction": self._build_extraction_report(),
            "fuzzy_threshold": self.threshold,
            "anchor_window_threshold": self.anchor_threshold,
        }

    def format_report(self, title: str = "Demo1 评估报告") -> str:
        """返回可读的多行文本报告；由 notebook 负责 print。"""
        report = self.report()
        detection = report["detection"]
        extraction = report["extraction"]
        strict = extraction[STRICT_TOKEN_F1]
        anchor = extraction[ANCHOR_WINDOW]
        primary_metric = str(extraction["primary_metric"])
        lines = [
            f"================ {title} ================",
            f"样本总数: {report['n_samples']}",
            f"  Gold 含因果: {report['n_causal_gold']} | Pred 含因果: {report['n_causal_pred']}",
            f"  Primary extraction metric: {primary_metric}",
            f"  strict_token_f1 阈值: {report['fuzzy_threshold']:.3f}",
            f"  anchor_window 阈值: {report['anchor_window_threshold']:.3f}",
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
            _format_metric_block(STRICT_TOKEN_F1, strict["all_samples"], primary_metric == STRICT_TOKEN_F1),
            _format_metric_block(ANCHOR_WINDOW, anchor["all_samples"], primary_metric == ANCHOR_WINDOW),
            "",
            "[Layer 2B] Extraction detected_only",
            "  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。",
            _format_metric_block(STRICT_TOKEN_F1, strict["detected_only"], primary_metric == STRICT_TOKEN_F1),
            _format_metric_block(ANCHOR_WINDOW, anchor["detected_only"], primary_metric == ANCHOR_WINDOW),
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
        strict_counts = match_triples(pred_triples, gold_relations, threshold=self.threshold)
        anchor_counts = match_triples_anchor_window(pred_triples, gold_relations, threshold=self.anchor_threshold)
        self.strict_all_samples_counts.add(*strict_counts)
        self.anchor_all_samples_counts.add(*anchor_counts)
        self.all_samples_n_eval += 1
        self.all_samples_gold_triples += len(gold_relations)
        self.all_samples_pred_triples += len(pred_triples)

    def _update_detected_only(self, pred_triples: list[Any], gold_relations: list[Any]) -> None:
        strict_counts = match_triples(pred_triples, gold_relations, threshold=self.threshold)
        anchor_counts = match_triples_anchor_window(pred_triples, gold_relations, threshold=self.anchor_threshold)
        self.strict_detected_only_counts.add(*strict_counts)
        self.anchor_detected_only_counts.add(*anchor_counts)
        self.detected_only_n_eval += 1
        self.detected_only_gold_triples += len(gold_relations)
        self.detected_only_pred_triples += len(pred_triples)

    def _build_extraction_report(self) -> dict[str, Any]:
        strict = {
            "all_samples": self._extraction_report(
                self.strict_all_samples_counts,
                n_eval_samples=self.all_samples_n_eval,
                n_gold_triples=self.all_samples_gold_triples,
                n_pred_triples=self.all_samples_pred_triples,
            ),
            "detected_only": self._extraction_report(
                self.strict_detected_only_counts,
                n_eval_samples=self.detected_only_n_eval,
                n_gold_triples=self.detected_only_gold_triples,
                n_pred_triples=self.detected_only_pred_triples,
            ),
        }
        anchor = {
            "all_samples": self._extraction_report(
                self.anchor_all_samples_counts,
                n_eval_samples=self.all_samples_n_eval,
                n_gold_triples=self.all_samples_gold_triples,
                n_pred_triples=self.all_samples_pred_triples,
            ),
            "detected_only": self._extraction_report(
                self.anchor_detected_only_counts,
                n_eval_samples=self.detected_only_n_eval,
                n_gold_triples=self.detected_only_gold_triples,
                n_pred_triples=self.detected_only_pred_triples,
            ),
        }
        primary = strict if self.primary_metric == STRICT_TOKEN_F1 else anchor
        return {
            "primary_metric": self.primary_metric,
            STRICT_TOKEN_F1: strict,
            ANCHOR_WINDOW: anchor,
            "all_samples": primary["all_samples"],
            "detected_only": primary["detected_only"],
        }

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


def anchor_window_score(pred_span: str, gold_span: str) -> float:
    """计算 gold anchor 是否可在更长 prediction span 中被 fuzzy window 匹配。"""
    pred = _normalize_anchor_window_text(pred_span)
    gold = _normalize_anchor_window_text(gold_span)
    if not pred or not gold or len(pred) < len(gold):
        return 0.0
    if gold in pred:
        return 1.0
    return max(
        difflib.SequenceMatcher(None, pred[index : index + len(gold)], gold).ratio()
        for index in range(len(pred) - len(gold) + 1)
    )


def match_triples(
    pred_triples: list[Any],
    gold_relations: list[Any],
    threshold: float = FUZZY_THRESHOLD,
) -> tuple[int, int, int]:
    """用 strict token-F1 与 greedy one-to-one matching 统计 TP/FP/FN。"""
    return _match_triples_by_span_score(pred_triples, gold_relations, threshold=threshold, span_score=token_f1)


def match_triples_anchor_window(
    pred_triples: list[Any],
    gold_relations: list[Any],
    threshold: float = ANCHOR_WINDOW_THRESHOLD,
) -> tuple[int, int, int]:
    """用 anchor-window matching 统计 concept-anchor 标注的 TP/FP/FN。"""
    return _match_triples_by_span_score(
        pred_triples,
        gold_relations,
        threshold=threshold,
        span_score=anchor_window_score,
    )


def primary_metric_for_dataset(dataset: str | None) -> str:
    """根据数据集的标注粒度返回默认主指标。"""
    return PRIMARY_METRIC_BY_DATASET.get(str(dataset or "").lower(), STRICT_TOKEN_F1)


def build_sample_judgement(
    prediction: dict[str, Any],
    gold: dict[str, Any],
    dataset: str | None = None,
    primary_metric: str | None = None,
) -> dict[str, Any]:
    """构造单条样本的调试判定，供 notebook 展示或写入报告。"""
    pred_triples = _as_list(prediction.get("triples"))
    gold_relations = _as_list(gold.get("relations"))
    metric = _resolve_primary_metric(dataset=dataset, primary_metric=primary_metric)
    strict_counts = match_triples(pred_triples, gold_relations)
    anchor_counts = match_triples_anchor_window(pred_triples, gold_relations)
    return {
        "id": gold.get("id", prediction.get("id")),
        "text": gold.get("text", ""),
        "gold_has_causal": bool(gold.get("has_causal", False)),
        "pred_has_causal": bool(prediction.get("has_causal", False)),
        "gold_relations": gold_relations,
        "pred_triples": pred_triples,
        "primary_metric": metric,
        STRICT_TOKEN_F1: {"counts": _counts_dict(strict_counts)},
        ANCHOR_WINDOW: {"counts": _counts_dict(anchor_counts)},
        "token_f1": {"counts": _counts_dict(strict_counts)},
    }


def _match_triples_by_span_score(
    pred_triples: list[Any],
    gold_relations: list[Any],
    threshold: float,
    span_score: Callable[[str, str], float],
) -> tuple[int, int, int]:
    pair_scores = []
    for pred_index, pred_triple in enumerate(pred_triples):
        pred_cause = _pred_span(pred_triple, "cause")
        pred_effect = _pred_span(pred_triple, "effect")
        for gold_index, gold_relation in enumerate(gold_relations):
            gold_cause = str(gold_relation.get("cause", "")) if isinstance(gold_relation, dict) else ""
            gold_effect = str(gold_relation.get("effect", "")) if isinstance(gold_relation, dict) else ""
            cause_score = span_score(pred_cause, gold_cause)
            effect_score = span_score(pred_effect, gold_effect)
            pair_scores.append((min(cause_score, effect_score), pred_index, gold_index))

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


def _resolve_primary_metric(dataset: str | None, primary_metric: str | None) -> str:
    metric = primary_metric or primary_metric_for_dataset(dataset)
    if metric not in VALID_EXTRACTION_METRICS:
        raise ValueError(f"未知 extraction metric：{metric}")
    return metric


def _normalize_anchor_window_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def _pred_span(pred_triple: Any, key: str) -> str:
    if not isinstance(pred_triple, dict):
        return ""
    value = pred_triple.get(key, "")
    if isinstance(value, dict):
        return str(value.get("span", ""))
    return str(value)


def _counts_dict(counts: tuple[int, int, int]) -> dict[str, int]:
    tp, fp, fn = counts
    return {"tp": tp, "fp": fp, "fn": fn}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _safe_div(numerator: int, denominator: int) -> float:
    return 0.0 if denominator == 0 else numerator / denominator


def _f1(precision: float, recall: float) -> float:
    return 0.0 if precision + recall == 0 else 2 * precision * recall / (precision + recall)


def _format_metric_block(metric_name: str, metrics: dict[str, float | int], is_primary: bool) -> str:
    marker = " (primary)" if is_primary else ""
    return "\n".join(
        [
            f"  [{metric_name}]{marker}",
            f"    样本数: {metrics['n_eval_samples']}",
            f"    Gold triples: {metrics['n_gold_triples']} | Pred triples: {metrics['n_pred_triples']}",
            f"    Precision: {metrics['precision']:.3f}",
            f"    Recall   : {metrics['recall']:.3f}",
            f"    F1       : {metrics['f1']:.3f}",
            f"    (TP={metrics['tp']}, FP={metrics['fp']}, FN={metrics['fn']})",
        ]
    )
