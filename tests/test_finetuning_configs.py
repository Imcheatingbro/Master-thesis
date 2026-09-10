"""验证 CNC QLoRA 配置的模型、数据隔离和关键训练参数。"""

from __future__ import annotations

import json
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = PROJECT_ROOT / "configs" / "finetuning"
DATA_DIR = PROJECT_ROOT / "Data" / "CNC_sft"
MODEL_REVISION = "b968826d9c46dd6066d109eabc6255188de91218"


def _load_yaml(name: str) -> dict[str, object]:
    return yaml.safe_load((CONFIG_DIR / name).read_text(encoding="utf-8"))


def _read_ids(name: str) -> set[int]:
    return {
        json.loads(line)["id"]
        for line in (DATA_DIR / name).read_text(encoding="utf-8").splitlines()
    }


def test_full_qlora_config_uses_frozen_cnc_splits() -> None:
    config = _load_yaml("qwen3_8b_cnc_qlora_v1.yaml")

    assert config["model_name_or_path"] == "Qwen/Qwen3-8B"
    assert config["model_revision"] == MODEL_REVISION
    assert config["dataset"] == "cnc_sft_train"
    assert config["eval_dataset"] == "cnc_sft_validation"
    assert config["template"] == "qwen3"
    assert config["enable_thinking"] is False
    assert config["train_on_prompt"] is False
    assert config["quantization_bit"] == 4
    assert config["quantization_method"] == "bnb"
    assert config["quantization_type"] == "nf4"
    assert config["double_quantization"] is True
    assert config["use_unsloth"] is False
    assert config["upcast_layernorm"] is True
    assert config["cutoff_len"] == 1024
    assert config["dataloader_num_workers"] == 0
    assert config["eval_strategy"] == "epoch"

    train_ids = _read_ids("train.jsonl")
    validation_ids = _read_ids("validation.jsonl")
    test_ids = _read_ids("test.jsonl")
    assert len(train_ids) == 1537
    assert len(validation_ids) == 500
    assert len(test_ids) == 1038
    assert train_ids.isdisjoint(validation_ids)
    assert train_ids.isdisjoint(test_ids)
    assert validation_ids.isdisjoint(test_ids)


def test_smoke_config_matches_full_model_and_uses_bounded_training() -> None:
    full = _load_yaml("qwen3_8b_cnc_qlora_v1.yaml")
    smoke = _load_yaml("qwen3_8b_cnc_qlora_smoke.yaml")

    for key in (
        "model_name_or_path",
        "model_revision",
        "template",
        "enable_thinking",
        "quantization_bit",
        "quantization_method",
        "quantization_type",
        "double_quantization",
        "lora_rank",
        "lora_alpha",
        "upcast_layernorm",
        "cutoff_len",
    ):
        assert smoke[key] == full[key]
    assert smoke["max_samples"] == 64
    assert smoke["max_steps"] == 5
    assert smoke["save_strategy"] == "no"
    assert smoke["eval_strategy"] == "no"


def test_download_notebook_pins_training_weights_and_kernel() -> None:
    notebook_path = PROJECT_ROOT / "notebooks" / "download_qwen3_8b_for_finetuning.ipynb"
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    source = "\n".join(
        "".join(cell.get("source", []))
        for cell in notebook["cells"]
    )

    assert notebook["nbformat"] == 4
    assert notebook["metadata"]["kernelspec"]["name"] == "model_finetune"
    assert "Qwen/Qwen3-8B" in source
    assert MODEL_REVISION in source
    assert r"D:\huggingface_cache" in source
    assert "snapshot_download" in source
    assert "model-*.safetensors" in source
    assert "max_workers=4" in source
