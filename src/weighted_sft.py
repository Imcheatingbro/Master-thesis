"""Structure-aware token weighting for supervised fine-tuning."""

from __future__ import annotations

import json
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any

import torch


MessageEncoder = Callable[[Sequence[Mapping[str, str]]], list[int]]


@dataclass(frozen=True)
class StructuralWeightResult:

    loss_weights: list[float]
    decision_true: int
    decision_false: int
    continuation: int
    stop: int


def _compact_json(value: Mapping[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _replace_assistant(
    messages: Sequence[Mapping[str, str]], assistant_content: str
) -> list[dict[str, str]]:
    replaced = [dict(message) for message in messages]
    assistant_indices = [
        index for index, message in enumerate(replaced) if message.get("role") == "assistant"
    ]
    if assistant_indices != [len(replaced) - 1]:
        raise ValueError("训练消息必须且只能以一个 assistant answer 结束。")
    replaced[-1]["content"] = assistant_content
    return replaced


def _first_divergence(left: Sequence[int], right: Sequence[int]) -> int:
    limit = min(len(left), len(right))
    for index in range(limit):
        if left[index] != right[index]:
            return index
    raise ValueError("两条候选 token 序列没有真实分叉。")


def build_structural_loss_weights(
    *,
    input_ids: Sequence[int],
    labels: Sequence[int],
    messages: Sequence[Mapping[str, str]],
    encode_messages: MessageEncoder,
    ordinary_weight: float,
    decision_true_weight: float,
    decision_false_weight: float,
    continuation_weight: float,
    stop_weight: float,
) -> StructuralWeightResult:

    if len(input_ids) != len(labels):
        raise ValueError("input_ids 与 labels 长度不一致。")
    if min(
        ordinary_weight,
        decision_true_weight,
        decision_false_weight,
        continuation_weight,
        stop_weight,
    ) <= 0:
        raise ValueError("所有 loss 权重都必须大于 0。")

    assistant_content = str(messages[-1].get("content", ""))
    try:
        target = json.loads(assistant_content)
    except json.JSONDecodeError as exc:
        raise ValueError("assistant answer 不是合法 JSON。") from exc
    if _compact_json(target) != assistant_content:
        raise ValueError("assistant answer 必须使用训练集的紧凑规范 JSON 格式。")

    has_causal = target.get("has_causal")
    triples = target.get("triples")
    if not isinstance(has_causal, bool) or not isinstance(triples, list):
        raise ValueError("assistant answer 缺少合法 has_causal/triples。")
    if has_causal != bool(triples):
        raise ValueError("has_causal 与 triples 是否为空不一致。")

    actual_ids = list(encode_messages(messages))
    observed_ids = list(input_ids)
    if observed_ids != actual_ids[: len(observed_ids)]:
        raise ValueError("权重编码与 SFTTrainer 的实际 input_ids 不一致。")

    weights = [float(ordinary_weight)] * len(observed_ids)
    occupied_positions: set[int] = set()

    def assign(position: int, weight: float, branch_name: str) -> None:
        if position >= len(observed_ids):
            raise ValueError(f"{branch_name} 分叉位置被 cutoff 截断。")
        if labels[position] == -100:
            raise ValueError(f"{branch_name} 分叉位置被 answer-only mask 屏蔽。")
        if position in occupied_positions:
            raise ValueError(f"多个结构分叉落在同一个 token 位置：{position}。")
        weights[position] = float(weight)
        occupied_positions.add(position)

    dummy_triple = {
        "cause": {"span": "DUMMY_CAUSE"},
        "relation": "caused",
        "effect": {"span": "DUMMY_EFFECT"},
    }
    true_target = {"has_causal": True, "triples": triples or [dummy_triple]}
    false_target = {"has_causal": False, "triples": []}
    true_ids = encode_messages(_replace_assistant(messages, _compact_json(true_target)))
    false_ids = encode_messages(_replace_assistant(messages, _compact_json(false_target)))
    decision_position = _first_divergence(true_ids, false_ids)
    expected_decision_ids = true_ids if has_causal else false_ids
    if observed_ids[decision_position] != expected_decision_ids[decision_position]:
        raise ValueError("实际 decision token 与候选分叉不一致。")
    assign(
        decision_position,
        decision_true_weight if has_causal else decision_false_weight,
        "decision_true" if has_causal else "decision_false",
    )

    continuation_count = 0
    stop_count = 0
    for boundary_index in range(1, len(triples) + 1):
        prefix = triples[:boundary_index]
        stop_target = {"has_causal": True, "triples": prefix}
        next_triple = triples[boundary_index] if boundary_index < len(triples) else triples[-1]
        continue_target = {"has_causal": True, "triples": [*prefix, next_triple]}
        stop_ids = encode_messages(_replace_assistant(messages, _compact_json(stop_target)))
        continue_ids = encode_messages(
            _replace_assistant(messages, _compact_json(continue_target))
        )
        boundary_position = _first_divergence(continue_ids, stop_ids)
        should_continue = boundary_index < len(triples)
        expected_boundary_ids = continue_ids if should_continue else stop_ids
        if observed_ids[boundary_position] != expected_boundary_ids[boundary_position]:
            raise ValueError("实际 continuation/stop token 与候选分叉不一致。")
        assign(
            boundary_position,
            continuation_weight if should_continue else stop_weight,
            "continuation" if should_continue else "stop",
        )
        continuation_count += int(should_continue)
        stop_count += int(not should_continue)

    return StructuralWeightResult(
        loss_weights=weights,
        decision_true=int(has_causal),
        decision_false=int(not has_causal),
        continuation=continuation_count,
        stop=stop_count,
    )


class WeightedDataCollator:

    def __init__(self, base_collator: Callable[..., dict[str, Any]], padding_side: str) -> None:
        if padding_side not in {"left", "right"}:
            raise ValueError(f"未知 padding_side：{padding_side}")
        self.base_collator = base_collator
        self.padding_side = padding_side

    def __call__(self, features: list[dict[str, Any]]) -> dict[str, Any]:
        copied_features = [dict(feature) for feature in features]
        weight_rows = [list(feature.pop("loss_weights")) for feature in copied_features]
        for feature, weights in zip(copied_features, weight_rows, strict=True):
            if len(feature["input_ids"]) != len(weights):
                raise ValueError("collator 收到的 input_ids 与 loss_weights 长度不一致。")

        batch = self.base_collator(copied_features)
        sequence_length = int(batch["input_ids"].shape[1])
        padded_rows: list[list[float]] = []
        for weights in weight_rows:
            padding = [0.0] * (sequence_length - len(weights))
            padded_rows.append(
                [*padding, *weights] if self.padding_side == "left" else [*weights, *padding]
            )
        batch["loss_weights"] = torch.tensor(padded_rows, dtype=torch.float32)
        return batch


def reduce_weighted_token_losses(
    token_losses: torch.Tensor,
    shifted_labels: torch.Tensor,
    shifted_weights: torch.Tensor,
) -> torch.Tensor:

    if token_losses.shape != shifted_labels.shape or token_losses.shape != shifted_weights.shape:
        raise ValueError("token loss、shifted labels 与 shifted weights 形状不一致。")
    valid_mask = shifted_labels.ne(-100)
    effective_weights = shifted_weights.to(token_losses.device) * valid_mask
    denominator = effective_weights.sum().clamp_min(torch.finfo(token_losses.dtype).eps)
    return (token_losses * effective_weights).sum() / denominator


def make_weighted_sft_trainer_class(base_trainer_class: type[Any]) -> type[Any]:

    class WeightedSFTTrainer(base_trainer_class):  # type: ignore[misc, valid-type]
        def compute_loss(
            self,
            model: torch.nn.Module,
            inputs: dict[str, Any],
            return_outputs: bool = False,
            num_items_in_batch: torch.Tensor | int | None = None,
        ) -> torch.Tensor | tuple[torch.Tensor, dict[str, torch.Tensor]]:
            del num_items_in_batch
            model_inputs = dict(inputs)
            loss_weights = model_inputs.pop("loss_weights", None)
            labels = model_inputs.pop("labels", None)
            if loss_weights is None or labels is None:
                raise ValueError("加权训练 batch 缺少 labels 或 loss_weights。")

            base_model = model.get_base_model() if hasattr(model, "get_base_model") else model
            backbone = getattr(base_model, "model", None)
            lm_head = base_model.get_output_embeddings()
            if backbone is None or lm_head is None or getattr(lm_head, "bias", None) is not None:
                raise TypeError("当前加权 loss 只支持无 bias lm_head 的 Gemma 4 模型。")

            backbone_outputs = backbone(
                **model_inputs,
                use_cache=False,
                return_dict=True,
            )
            hidden_states = backbone_outputs.last_hidden_state
            text_config = (
                base_model.config.get_text_config()
                if hasattr(base_model.config, "get_text_config")
                else base_model.config
            )
            softcap = getattr(text_config, "final_logit_softcapping", None)

            from cut_cross_entropy import linear_cross_entropy

            token_losses = linear_cross_entropy(
                hidden_states,
                lm_head.weight,
                targets=labels,
                ignore_index=-100,
                softcap=softcap,
                reduction="none",
                shift=True,
                filter_eps="auto",
            )
            loss = reduce_weighted_token_losses(
                token_losses,
                labels[..., 1:],
                loss_weights[..., 1:],
            )
            if return_outputs:
                return loss, {"loss": loss.detach()}
            return loss

    WeightedSFTTrainer.__name__ = "WeightedSFTTrainer"
    return WeightedSFTTrainer
