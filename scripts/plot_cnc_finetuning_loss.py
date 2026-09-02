"""从 CNC 最终四个微调分支的训练日志生成 loss 数据与论文图表。"""

from __future__ import annotations

import csv
import json
import logging
import math
import sys
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Iterable


LOGGER = logging.getLogger("cnc-finetuning-loss")
PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "reports" / "assets"
CSV_PATH = OUTPUT_DIR / "cnc_finetuning_loss_points.csv"
TRAIN_SVG_PATH = OUTPUT_DIR / "cnc_finetuning_training_loss.svg"
VALIDATION_SVG_PATH = OUTPUT_DIR / "cnc_finetuning_validation_loss.svg"


@dataclass(frozen=True)
class LossPoint:
    """单个训练或验证 loss 观测点。"""

    model: str
    split: str
    step: int
    loss: float


@dataclass(frozen=True)
class ModelStyle:
    """模型日志来源及固定绘图样式。"""

    label: str
    color: str
    marker: str
    trainer_state: Path | None = None
    event_file: Path | None = None


MODELS = (
    ModelStyle(
        label="Qwen3-8B LoRA",
        color="#0f766e",
        marker="circle",
        trainer_state=PROJECT_ROOT
        / "outputs/finetuning/qwen3_8b_cnc_bf16_lora_unsloth_v1/trainer_state.json",
    ),
    ModelStyle(
        label="Qwen3-14B QLoRA",
        color="#2563eb",
        marker="square",
        trainer_state=PROJECT_ROOT
        / "outputs/finetuning/qwen3_14b_cnc_qlora_unsloth_v2_gemma12_profile/trainer_state.json",
    ),
    ModelStyle(
        label="Gemma 4 E4B LoRA",
        color="#d97706",
        marker="diamond",
        event_file=PROJECT_ROOT
        / (
            "outputs/finetuning/gemma4_e4b_cnc_bf16_lora_unsloth_v1/runs/"
            "Aug20_17-17-57_PC-202301311540/"
            "events.out.tfevents.1787239077.PC-202301311540.68164.0"
        ),
    ),
    ModelStyle(
        label="Gemma 4 12B QLoRA",
        color="#7c3aed",
        marker="triangle",
        trainer_state=PROJECT_ROOT
        / (
            "outputs/finetuning/gemma4_12b_cnc_qlora_unsloth_v1/"
            "checkpoint-291/trainer_state.json"
        ),
    ),
)


def load_trainer_state(model: ModelStyle) -> list[LossPoint]:
    """从 Hugging Face Trainer state 中读取训练与验证 loss。"""
    if model.trainer_state is None:
        raise ValueError(f"{model.label} 未配置 trainer_state")
    payload = json.loads(model.trainer_state.read_text(encoding="utf-8"))
    points: list[LossPoint] = []
    for record in payload["log_history"]:
        step = int(record["step"])
        if "loss" in record:
            points.append(LossPoint(model.label, "train", step, float(record["loss"])))
        if "eval_loss" in record:
            points.append(LossPoint(model.label, "validation", step, float(record["eval_loss"])))
    return points


def import_event_accumulator() -> type:
    """载入 TensorBoard event reader，并兼容本机训练环境的依赖位置。"""
    try:
        from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

        return EventAccumulator
    except ModuleNotFoundError:
        fallback = Path("D:/Anaconda3/envs/Gemma_finetune/Lib/site-packages")
        if not fallback.is_dir():
            raise
        sys.path.insert(0, str(fallback))
        from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

        return EventAccumulator


def load_tensorboard_event(model: ModelStyle) -> list[LossPoint]:
    """从 TensorBoard event 文件读取训练与验证 loss。"""
    if model.event_file is None:
        raise ValueError(f"{model.label} 未配置 event_file")
    event_accumulator = import_event_accumulator()
    accumulator = event_accumulator(str(model.event_file))
    accumulator.Reload()
    points = [
        LossPoint(model.label, "train", int(item.step), float(item.value))
        for item in accumulator.Scalars("train/loss")
    ]
    points.extend(
        LossPoint(model.label, "validation", int(item.step), float(item.value))
        for item in accumulator.Scalars("eval/loss")
    )
    return points


def load_all_points() -> list[LossPoint]:
    """读取并验证四个最终模型的全部 loss 点。"""
    points: list[LossPoint] = []
    for model in MODELS:
        model_points = (
            load_trainer_state(model)
            if model.trainer_state is not None
            else load_tensorboard_event(model)
        )
        splits = {point.split for point in model_points}
        if splits != {"train", "validation"}:
            raise ValueError(f"{model.label} 的 loss 数据不完整：{sorted(splits)}")
        points.extend(model_points)
    return sorted(points, key=lambda point: (point.model, point.split, point.step))


def write_csv(points: Iterable[LossPoint]) -> None:
    """保存可核查的绘图源数据。"""
    with CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("model", "split", "step", "loss"))
        writer.writeheader()
        for point in points:
            writer.writerow(
                {
                    "model": point.model,
                    "split": point.split,
                    "step": point.step,
                    "loss": f"{point.loss:.10f}",
                }
            )


def marker_svg(marker: str, x: float, y: float, color: str, size: float = 4.5) -> str:
    """返回同时使用颜色与形状编码的 SVG marker。"""
    if marker == "circle":
        return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{size}" fill="{color}"/>'
    if marker == "square":
        return (
            f'<rect x="{x - size:.2f}" y="{y - size:.2f}" width="{size * 2:.2f}" '
            f'height="{size * 2:.2f}" fill="{color}"/>'
        )
    if marker == "diamond":
        return (
            f'<polygon points="{x:.2f},{y - size - 0.8:.2f} {x + size + 0.8:.2f},{y:.2f} '
            f'{x:.2f},{y + size + 0.8:.2f} {x - size - 0.8:.2f},{y:.2f}" fill="{color}"/>'
        )
    if marker == "triangle":
        return (
            f'<polygon points="{x:.2f},{y - size - 1:.2f} {x + size + 1:.2f},{y + size:.2f} '
            f'{x - size - 1:.2f},{y + size:.2f}" fill="{color}"/>'
        )
    raise ValueError(f"未知 marker：{marker}")


def nice_axis(maximum: float) -> tuple[float, float]:
    """为线性 loss 轴返回易读的上限与刻度间隔。"""
    if maximum > 0.5:
        return 1.0, 0.2
    if maximum > 0.12:
        return 0.18, 0.03
    return 0.10, 0.02


def build_svg(points: list[LossPoint], split: str, title: str) -> str:
    """生成单个训练或验证 loss 折线图。"""
    width = 1200
    height = 720
    left = 105
    right = 1155
    top = 145
    bottom = 590
    plot_width = right - left
    plot_height = bottom - top
    split_points = [point for point in points if point.split == split]
    y_max, y_tick = nice_axis(max(point.loss for point in split_points))
    x_max = max(point.step for point in split_points)

    def x_position(step: int) -> float:
        return left + (step / x_max) * plot_width

    def y_position(loss: float) -> float:
        return bottom - (loss / y_max) * plot_height

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="description">Loss curves for four final CNC fine-tuning branches over training steps.</desc>',
        """<style>
          .title { font: 600 25px Arial, sans-serif; fill: #111827; }
          .axis { font: 16px Arial, sans-serif; fill: #374151; }
          .tick { font: 14px Arial, sans-serif; fill: #4b5563; }
          .legend { font: 15px Arial, sans-serif; fill: #374151; }
          .note { font: 13px Arial, sans-serif; fill: #64748b; }
          .epoch { font: 12px Arial, sans-serif; fill: #94a3b8; }
          .grid { stroke: #dbe2ea; stroke-width: 1; }
        </style>""",
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'<text x="{width / 2}" y="46" class="title" text-anchor="middle">{escape(title)}</text>',
        f'<rect x="{left}" y="{top}" width="{plot_width}" height="{plot_height}" '
        'fill="#fbfcfe" stroke="#cbd5e1" stroke-width="1"/>',
    ]

    tick_count = int(round(y_max / y_tick))
    for index in range(tick_count + 1):
        value = index * y_tick
        y = y_position(value)
        elements.append(f'<line x1="{left}" y1="{y:.2f}" x2="{right}" y2="{y:.2f}" class="grid"/>')
        elements.append(
            f'<text x="{left - 16}" y="{y + 5:.2f}" class="tick" text-anchor="end">{value:.2f}</text>'
        )

    x_ticks = [0, 50, 100, 150, 200, 250, x_max]
    for step in x_ticks:
        x = x_position(step)
        anchor = "end" if step == x_max else "middle"
        elements.append(
            f'<text x="{x:.2f}" y="{bottom + 31}" class="tick" text-anchor="{anchor}">{step}</text>'
        )

    for boundary in (97, 194):
        x = x_position(boundary)
        elements.append(
            f'<line x1="{x:.2f}" y1="{top}" x2="{x:.2f}" y2="{bottom}" '
            'stroke="#94a3b8" stroke-width="1" stroke-dasharray="5 6"/>'
        )
    for epoch, center_step in enumerate((48.5, 145.5, 242.5), start=1):
        elements.append(
            f'<text x="{x_position(int(center_step)):.2f}" y="{top + 20}" class="epoch" '
            f'text-anchor="middle">Epoch {epoch}</text>'
        )

    elements.extend(
        [
            f'<text x="{(left + right) / 2}" y="{bottom + 70}" class="axis" '
            'text-anchor="middle">Training step</text>',
            f'<text x="31" y="{(top + bottom) / 2}" class="axis" text-anchor="middle" '
            f'transform="rotate(-90 31 {(top + bottom) / 2})">Cross-entropy loss</text>',
        ]
    )

    legend_x = 122
    for model in MODELS:
        model_points = sorted(
            (point for point in split_points if point.model == model.label),
            key=lambda point: point.step,
        )
        coordinates = [(x_position(point.step), y_position(point.loss)) for point in model_points]
        path = " ".join(f"{x:.2f},{y:.2f}" for x, y in coordinates)
        elements.append(
            f'<polyline points="{path}" fill="none" stroke="{model.color}" stroke-width="2.6" '
            'stroke-linejoin="round" stroke-linecap="round"/>'
        )
        for x, y in coordinates:
            elements.append(marker_svg(model.marker, x, y, model.color, 3.8 if split == "train" else 5.0))

        elements.append(marker_svg(model.marker, legend_x, 91, model.color, 5.0))
        elements.append(
            f'<text x="{legend_x + 14}" y="96" class="legend" '
            f'text-anchor="start">{escape(model.label)}</text>'
        )
        legend_x += 263

    note = (
        "Training loss is logged every 10 steps; curves show interval loss, not the final run-average loss."
        if split == "train"
        else "Validation frequency differs: Qwen3-8B at steps 100/200/final; the other runs every 50 steps and final."
    )
    elements.append(
        f'<text x="{width / 2}" y="687" class="note" text-anchor="middle">{escape(note)}</text>'
    )
    elements.append("</svg>")
    return "\n".join(elements)


def main() -> None:
    """生成 CSV、训练 loss 图和验证 loss 图。"""
    logging.basicConfig(level=logging.INFO, format="[%(name)s|%(levelname)s] %(message)s")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    points = load_all_points()
    write_csv(points)
    TRAIN_SVG_PATH.write_text(
        build_svg(points, "train", "CNC Fine-tuning: Training Loss"),
        encoding="utf-8",
        newline="\n",
    )
    VALIDATION_SVG_PATH.write_text(
        build_svg(points, "validation", "CNC Fine-tuning: Validation Loss"),
        encoding="utf-8",
        newline="\n",
    )
    LOGGER.info("已生成 %s 个 loss 观测点。", len(points))


if __name__ == "__main__":
    main()
