"""下载 Hugging Face ADE benchmark 数据集原始快照到 Data 目录。"""

from __future__ import annotations

import logging
from collections.abc import Callable
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "Data"
HF_REPO = "ade-benchmark-corpus/ade_corpus_v2"
DATASET_CONFIGS = (
    "Ade_corpus_v2_classification",
    "Ade_corpus_v2_drug_ade_relation",
)
LoadDatasetFn = Callable[[str, str], Any]


def download_all(output_dir: Path | str = DATA_DIR, load_dataset_fn: LoadDatasetFn | None = None) -> list[Path]:
    """下载两个 ADE config，并用 Hugging Face 原生格式保存到 output_dir。"""
    target_root = Path(output_dir)
    target_root.mkdir(parents=True, exist_ok=True)
    loader = load_dataset_fn or _default_load_dataset

    saved_paths = []
    for config_name in DATASET_CONFIGS:
        target_path = target_root / config_name
        if target_path.exists():
            LOGGER.info("已存在，跳过下载：%s", target_path)
            saved_paths.append(target_path)
            continue

        LOGGER.info("开始下载：repo=%s config=%s", HF_REPO, config_name)
        dataset = loader(HF_REPO, config_name)
        dataset.save_to_disk(str(target_path))
        LOGGER.info("已保存：%s", target_path)
        saved_paths.append(target_path)
    return saved_paths


def main() -> None:
    """命令行入口。"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    download_all()


def _default_load_dataset(repo: str, config_name: str) -> Any:
    try:
        from datasets import load_dataset
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "缺少依赖 datasets，请先在 Master_thesis 环境中运行：python -m pip install datasets"
        ) from exc
    return load_dataset(repo, config_name)


if __name__ == "__main__":
    main()
