"""生成论文模型家族选择章节的公开基准 SVG 对比图。"""

from html import escape
from pathlib import Path


OUTPUT_PATH = (
    Path(__file__).resolve().parents[1]
    / "reports"
    / "assets"
    / "model_family_selection_qwen36_gemma4.svg"
)


def svg_text(x: float, y: float, content: str, css_class: str, anchor: str = "middle") -> str:
    """返回转义后的 SVG 文本元素。"""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" class="{css_class}" '
        f'text-anchor="{anchor}">{escape(content)}</text>'
    )


def build_svg() -> str:
    """构建 Qwen 3.6 与 Gemma 4 的公开通用基准柱状图。"""
    width = 1200
    height = 700
    plot_left = 110
    plot_right = 1140
    plot_top = 135
    plot_bottom = 565
    plot_height = plot_bottom - plot_top
    benchmarks = ["MMLU-Pro", "GPQA Diamond", "LiveCodeBench v6", "AIME 2026"]
    qwen_scores = [85.2, 86.0, 80.4, 92.7]
    gemma_scores = [85.2, 84.3, 80.0, 89.2]
    group_centers = [235, 500, 765, 1030]
    bar_width = 76
    gap = 10

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        'aria-labelledby="title description">',
        '<title id="title">Published General-Capability Evidence for Model-Family Selection</title>',
        '<desc id="description">Grouped bar chart comparing representative Qwen 3.6 and Gemma 4 checkpoints on four public benchmarks.</desc>',
        """<style>
          .title { font: 600 25px Arial, sans-serif; fill: #111827; }
          .axis { font: 16px Arial, sans-serif; fill: #374151; }
          .tick { font: 14px Arial, sans-serif; fill: #4b5563; }
          .label { font: 600 15px Arial, sans-serif; fill: #1f2937; }
          .legend { font: 15px Arial, sans-serif; fill: #374151; }
          .note { font: 13px Arial, sans-serif; fill: #64748b; }
          .grid { stroke: #dbe2ea; stroke-width: 1; }
        </style>""",
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'<rect x="{plot_left}" y="{plot_top}" width="{plot_right - plot_left}" '
        f'height="{plot_height}" rx="8" fill="#fbfcfe"/>',
        svg_text(width / 2, 52, "Published General-Capability Evidence for Model-Family Selection", "title"),
    ]

    for tick in range(0, 101, 20):
        y = plot_bottom - (tick / 100) * plot_height
        elements.append(f'<line x1="{plot_left}" y1="{y:.1f}" x2="{plot_right}" y2="{y:.1f}" class="grid"/>')
        elements.append(svg_text(plot_left - 18, y + 5, str(tick), "tick", "end"))

    elements.append(
        f'<text x="32" y="{(plot_top + plot_bottom) / 2:.1f}" class="axis" '
        'text-anchor="middle" transform="rotate(-90 32 350)">Score (%)</text>'
    )

    for center, benchmark, qwen_score, gemma_score in zip(
        group_centers, benchmarks, qwen_scores, gemma_scores, strict=True
    ):
        qwen_x = center - gap / 2 - bar_width
        gemma_x = center + gap / 2
        for x, score, color in (
            (qwen_x, qwen_score, "#0f766e"),
            (gemma_x, gemma_score, "#4f6bed"),
        ):
            bar_height = score / 100 * plot_height
            y = plot_bottom - bar_height
            elements.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_width}" height="{bar_height:.1f}" '
                f'rx="5" fill="{color}"/>'
            )
            elements.append(svg_text(x + bar_width / 2, y - 10, f"{score:.1f}", "label"))
        elements.append(svg_text(center, plot_bottom + 36, benchmark, "tick"))

    elements.extend(
        [
            '<rect x="118" y="84" width="18" height="18" rx="3" fill="#0f766e"/>',
            svg_text(146, 98, "Qwen 3.6", "legend", "start"),
            '<rect x="245" y="84" width="18" height="18" rx="3" fill="#4f6bed"/>',
            svg_text(273, 98, "Gemma 4", "legend", "start"),
            svg_text(
                width / 2,
                645,
                "Representative published checkpoints; vendor-reported results from the Qwen 3.6 model card.",
                "note",
            ),
            svg_text(
                width / 2,
                668,
                "Scores are evidence of comparable capability, not family-wide guarantees.",
                "note",
            ),
            "</svg>",
        ]
    )
    return "\n".join(elements)


def main() -> None:
    """保存论文插图。"""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_svg(), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
