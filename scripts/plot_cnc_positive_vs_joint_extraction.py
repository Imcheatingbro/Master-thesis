"""Render the CNC positive-only versus joint-extraction F1 comparison."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reports" / "assets" / "cnc_positive_vs_joint_extraction_f1.png"

WIDTH, HEIGHT = 1600, 1000
PLOT_LEFT, PLOT_TOP, PLOT_RIGHT, PLOT_BOTTOM = 135, 180, 1530, 735
Y_MAX = 1.0

GROUPS = [
    {
        "model": "Qwen3.6 27B Dense",
        "positive_only": 0.586,
        "joint": 0.589,
    },
    {
        "model": "Qwen3.6 35B-A3B",
        "positive_only": 0.600,
        "joint": 0.542,
    },
    {
        "model": "Gemma 4 31B QAT",
        "positive_only": 0.746,
        "joint": 0.732,
    },
]

POSITIVE_COLOR = "#D4A72C"
JOINT_COLOR = "#256D85"


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(name, size=size)
    except OSError:
        return ImageFont.truetype("DejaVuSans.ttf", size=size)


def centered_text(
    draw: ImageDraw.ImageDraw,
    center_x: float,
    y: float,
    value: str,
    typeface: ImageFont.FreeTypeFont,
    fill: str,
) -> None:
    box = draw.textbbox((0, 0), value, font=typeface)
    draw.text((center_x - (box[2] - box[0]) / 2, y), value, font=typeface, fill=fill)


def value_to_y(value: float) -> float:
    plot_height = PLOT_BOTTOM - PLOT_TOP
    return PLOT_BOTTOM - (value / Y_MAX) * plot_height


def main() -> None:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), "#FFFFFF")
    draw = ImageDraw.Draw(canvas)

    title_font = font("seguisb.ttf", 46)
    axis_font = font("segoeui.ttf", 22)
    label_font = font("segoeui.ttf", 20)
    label_bold = font("seguisb.ttf", 21)
    value_font = font("seguisb.ttf", 28)
    note_font = font("segoeui.ttf", 19)

    centered_text(
        draw,
        WIDTH / 2,
        48,
        "Extraction F1 by model and task setup",
        title_font,
        "#172033",
    )


    legend_y = 151
    draw.rounded_rectangle((900, legend_y, 926, legend_y + 22), radius=4, fill=POSITIVE_COLOR)
    draw.text((938, legend_y - 4), "Positive-only extraction", font=note_font, fill="#172033")
    draw.rounded_rectangle((1222, legend_y, 1248, legend_y + 22), radius=4, fill=JOINT_COLOR)
    draw.text((1260, legend_y - 4), "Joint task (detected-only)", font=note_font, fill="#172033")


    for step in range(0, 11):
        tick = step / 10
        y = value_to_y(tick)
        draw.line((PLOT_LEFT, y, PLOT_RIGHT, y), fill="#DCE1E6", width=2)
        tick_text = f"{tick:.1f}"
        tick_box = draw.textbbox((0, 0), tick_text, font=axis_font)
        draw.text(
            (PLOT_LEFT - 18 - (tick_box[2] - tick_box[0]), y - 14),
            tick_text,
            font=axis_font,
            fill="#5B6573",
        )

    draw.line((PLOT_LEFT, PLOT_TOP, PLOT_LEFT, PLOT_BOTTOM), fill="#7B8794", width=3)
    draw.line((PLOT_LEFT, PLOT_BOTTOM, PLOT_RIGHT, PLOT_BOTTOM), fill="#7B8794", width=3)
    draw.text((42, PLOT_TOP - 6), "F1", font=label_bold, fill="#172033")

    group_centers = [365, 820, 1275]
    bar_width = 150
    bar_offset = 92
    for group_center, item in zip(group_centers, GROUPS):
        for center_x, value, color in (
            (group_center - bar_offset, item["positive_only"], POSITIVE_COLOR),
            (group_center + bar_offset, item["joint"], JOINT_COLOR),
        ):
            top = value_to_y(value)
            draw.rounded_rectangle(
                (center_x - bar_width / 2, top, center_x + bar_width / 2, PLOT_BOTTOM),
                radius=8,
                fill=color,
            )
            centered_text(
                draw,
                center_x,
                top - 44,
                f"{value:.3f}",
                value_font,
                "#172033",
            )

        centered_text(draw, group_center, PLOT_BOTTOM + 30, item["model"], label_bold, "#172033")
        delta = item["joint"] - item["positive_only"]
        centered_text(
            draw,
            group_center,
            PLOT_BOTTOM + 66,
            f"Joint - positive-only: {delta:+.3f}",
            label_font,
            "#5B6573",
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT, format="PNG", optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
