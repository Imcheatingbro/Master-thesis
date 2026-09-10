"""Train the Qwen3-14B CNC adapter directly with Unsloth and TRL."""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any

import yaml

import unsloth
import torch
from datasets import load_dataset
from trl import SFTConfig, SFTTrainer
from unsloth import FastLanguageModel
from unsloth.chat_templates import train_on_responses_only


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TARGET_MODULES = [
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
]
LOGGER = logging.getLogger("qwen3-14b-cnc-training")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Direct Unsloth Qwen3-14B CNC training")
    parser.add_argument("config", type=Path)
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = parse_args()
    config_path = args.config.resolve()
    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    _validate_config(cfg, config_path)
    _validate_windows_cpu_microcode()

    model_path = Path(cfg["model_name_or_path"])
    dataset_dir = PROJECT_ROOT / cfg["dataset_dir"]
    output_dir = PROJECT_ROOT / cfg["output_dir"]
    _validate_paths(model_path, dataset_dir, output_dir)

    free_bytes, total_bytes = torch.cuda.mem_get_info()
    LOGGER.info(
        "GPU=%s | free=%.2f/%.2f GiB | mode=%s",
        torch.cuda.get_device_name(0),
        free_bytes / 2**30,
        total_bytes / 2**30,
        "smoke" if "max_steps" in cfg else "train",
    )

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=str(model_path),
        max_seq_length=int(cfg["cutoff_len"]),
        dtype=torch.bfloat16,
        load_in_4bit=True,
        full_finetuning=False,
        trust_remote_code=bool(cfg["trust_remote_code"]),
        use_gradient_checkpointing="unsloth",
        random_state=int(cfg["seed"]),
        max_lora_rank=int(cfg["lora_rank"]),
        text_only=True,
    )
    if getattr(tokenizer, "bos_token_id", None) is not None and getattr(
        tokenizer, "add_bos_token", False
    ):
        raise RuntimeError("Qwen3 training must not manually prepend BOS")
    if not getattr(tokenizer, "chat_template", None):
        raise RuntimeError("The local Qwen3 tokenizer has no native chat template")

    linear4bit_modules = sum(
        module.__class__.__name__ == "Linear4bit" for module in model.modules()
    )
    if linear4bit_modules <= 0:
        raise RuntimeError("NF4 load failed: no Linear4bit modules found")
    LOGGER.info("NF4 model load verified: %s Linear4bit modules", linear4bit_modules)

    model = FastLanguageModel.get_peft_model(
        model,
        r=int(cfg["lora_rank"]),
        target_modules=TARGET_MODULES,
        lora_alpha=int(cfg["lora_alpha"]),
        lora_dropout=float(cfg["lora_dropout"]),
        bias="none",
        use_gradient_checkpointing="unsloth",
        random_state=int(cfg["seed"]),
        max_seq_length=int(cfg["cutoff_len"]),
        use_rslora=False,
    )
    trainable, total = model.get_nb_trainable_parameters()
    LOGGER.info(
        "Trainable params: %s / %s (%.4f%%)",
        f"{trainable:,}",
        f"{total:,}",
        trainable / total * 100,
    )

    train_dataset = load_dataset(
        "json", data_files=str(dataset_dir / "train.jsonl"), split="train"
    )
    eval_dataset = None
    if cfg["eval_strategy"] != "no":
        eval_dataset = load_dataset(
            "json", data_files=str(dataset_dir / "validation.jsonl"), split="train"
        )

    def format_batch(examples: dict[str, list[Any]]) -> dict[str, list[str]]:
        return {
            "text": [
                tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=False,
                    enable_thinking=False,
                )
                for messages in examples["messages"]
            ]
        }

    map_workers = max(1, int(cfg.get("preprocessing_num_workers", 1)))
    train_dataset = train_dataset.map(
        format_batch,
        batched=True,
        num_proc=map_workers,
        remove_columns=train_dataset.column_names,
        desc="Render Qwen3 non-thinking training messages",
    )
    if eval_dataset is not None:
        eval_dataset = eval_dataset.map(
            format_batch,
            batched=True,
            num_proc=map_workers,
            remove_columns=eval_dataset.column_names,
            desc="Render Qwen3 non-thinking validation messages",
        )
    LOGGER.info(
        "Dataset rows: train=%s validation=%s",
        len(train_dataset),
        len(eval_dataset) if eval_dataset is not None else 0,
    )

    training_args: dict[str, Any] = {
        "output_dir": str(output_dir),
        "per_device_train_batch_size": int(cfg["per_device_train_batch_size"]),
        "gradient_accumulation_steps": int(cfg["gradient_accumulation_steps"]),
        "learning_rate": float(cfg["learning_rate"]),
        "lr_scheduler_type": cfg["lr_scheduler_type"],
        "weight_decay": float(cfg["weight_decay"]),
        "max_grad_norm": float(cfg["max_grad_norm"]),
        "bf16": bool(cfg["bf16"]),
        "fp16": bool(cfg.get("fp16", False)),
        "gradient_checkpointing": bool(cfg["gradient_checkpointing"]),
        "optim": cfg["optim"],
        "max_length": int(cfg["cutoff_len"]),
        "packing": bool(cfg["packing"]),
        "dataset_text_field": "text",
        "dataset_num_proc": map_workers,
        "dataloader_num_workers": int(cfg["dataloader_num_workers"]),
        "dataloader_pin_memory": bool(cfg.get("dataloader_pin_memory", True)),
        "train_sampling_strategy": cfg["train_sampling_strategy"],
        "logging_steps": int(cfg["logging_steps"]),
        "eval_strategy": cfg["eval_strategy"],
        "save_strategy": cfg["save_strategy"],
        "report_to": cfg["report_to"],
        "seed": int(cfg["seed"]),
        "data_seed": int(cfg["data_seed"]),
        "do_train": True,
    }
    if "warmup_steps" in cfg:
        training_args["warmup_steps"] = int(cfg["warmup_steps"])
    else:
        training_args["warmup_ratio"] = float(cfg["warmup_ratio"])
    if "max_steps" in cfg:
        training_args["max_steps"] = int(cfg["max_steps"])
    else:
        training_args.update(
            {
                "num_train_epochs": float(cfg["num_train_epochs"]),
                "per_device_eval_batch_size": int(cfg["per_device_eval_batch_size"]),
                "eval_steps": int(cfg["eval_steps"]),
                "save_steps": int(cfg["save_steps"]),
                "save_total_limit": int(cfg["save_total_limit"]),
                "load_best_model_at_end": bool(cfg["load_best_model_at_end"]),
                "save_only_model": bool(cfg["save_only_model"]),
            }
        )

    trainer = SFTTrainer(
        model=model,
        processing_class=tokenizer,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        args=SFTConfig(**training_args),
    )
    trainer = train_on_responses_only(
        trainer,
        instruction_part="<|im_start|>user\n",
        response_part="<|im_start|>assistant\n",
    )
    _audit_answer_mask(trainer.train_dataset, tokenizer)

    torch.cuda.reset_peak_memory_stats()
    result = trainer.train()
    peak_allocated = torch.cuda.max_memory_allocated() / 2**30
    peak_reserved = torch.cuda.max_memory_reserved() / 2**30
    LOGGER.info(
        "Training complete: step=%s peak_allocated=%.2f GiB peak_reserved=%.2f GiB",
        result.global_step,
        peak_allocated,
        peak_reserved,
    )
    if "max_steps" not in cfg:
        trainer.save_model(str(output_dir))
        tokenizer.save_pretrained(str(output_dir))
        LOGGER.info("Final adapter saved: %s", output_dir)


def _audit_answer_mask(dataset: Any, tokenizer: Any) -> None:
    saw_true = False
    saw_false = False
    for index in range(min(128, len(dataset))):
        feature = dataset[index]
        input_ids = feature["input_ids"]
        labels = feature["labels"]
        supervised_ids = [token_id for token_id, label in zip(input_ids, labels) if label != -100]
        if not supervised_ids or len(supervised_ids) >= len(input_ids):
            raise RuntimeError(f"Invalid answer-only mask at dataset index {index}")
        decoded = tokenizer.decode(supervised_ids, skip_special_tokens=False)
        saw_true = saw_true or '"has_causal":true' in decoded.replace(" ", "")
        saw_false = saw_false or '"has_causal":false' in decoded.replace(" ", "")
        if saw_true and saw_false:
            LOGGER.info("Answer-only mask verified for both true and false decision targets")
            return
    raise RuntimeError(
        f"Decision target mask audit failed: saw_true={saw_true}, saw_false={saw_false}"
    )


def _validate_config(cfg: dict[str, Any], config_path: Path) -> None:
    expected = {
        "template": "qwen3",
        "use_unsloth": True,
        "quantization_bit": 4,
        "quantization_method": "bnb",
        "quantization_type": "nf4",
        "double_quantization": True,
        "finetuning_type": "lora",
        "lora_rank": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.0,
        "lora_target": "all",
        "dataset_dir": "Data/CNC_sft_qwen3_14b_original_v1",
        "dataset": "cnc_sft_train",
        "enable_thinking": False,
        "train_on_prompt": False,
        "cutoff_len": 1536,
        "packing": False,
        "train_sampling_strategy": "group_by_length",
        "learning_rate": 5.0e-5,
        "max_grad_norm": 0.5,
        "bf16": True,
        "gradient_checkpointing": True,
        "optim": "adamw_8bit",
    }
    mismatches = {
        key: (cfg.get(key), value) for key, value in expected.items() if cfg.get(key) != value
    }
    if mismatches:
        raise RuntimeError(f"Unexpected Qwen3-14B config values in {config_path}: {mismatches}")
    if not cfg.get("model_name_or_path"):
        raise RuntimeError("model_name_or_path must identify the base model")
    if "adapter_name_or_path" in cfg:
        raise RuntimeError("Training must initialize a fresh adapter from the base model")
    if cfg["eval_strategy"] == "no":
        if cfg.get("max_steps") != 2:
            raise RuntimeError("Smoke config must run exactly two optimizer steps")
        if cfg.get("per_device_train_batch_size") != 4 or cfg.get("gradient_accumulation_steps") != 1:
            raise RuntimeError("Gemma-profile smoke must use batch=4 and accumulation=1")
    else:
        if cfg.get("num_train_epochs") != 3.0 or "max_steps" in cfg:
            raise RuntimeError("Formal config must run exactly three epochs without max_steps")
        if cfg.get("eval_dataset") != "cnc_sft_validation":
            raise RuntimeError("Formal config uses the wrong validation split")
        if cfg.get("per_device_train_batch_size") != 4 or cfg.get("gradient_accumulation_steps") != 4:
            raise RuntimeError("Gemma-profile formal config must keep effective batch 4 x 4")
        if cfg.get("warmup_steps") != 30 or "warmup_ratio" in cfg:
            raise RuntimeError("Gemma-profile formal config must use 30 warmup steps")
    if cfg.get("preprocessing_num_workers") != 1:
        raise RuntimeError("Gemma-profile preprocessing must stay single-process")
    if cfg.get("dataloader_num_workers") != 0 or cfg.get("dataloader_pin_memory") is not True:
        raise RuntimeError("Gemma-profile data loading requires worker=0 and pin_memory=true")


def _validate_windows_cpu_microcode() -> None:
    if sys.platform != "win32":
        return
    import winreg

    key_path = r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
        processor = str(winreg.QueryValueEx(key, "ProcessorNameString")[0])
        raw_revision = winreg.QueryValueEx(key, "Update Revision")[0]
    if "13th Gen Intel(R) Core(TM) i9-13900K" not in processor:
        return
    if not isinstance(raw_revision, bytes) or len(raw_revision) < 4:
        raise RuntimeError("Cannot verify the current Intel CPU microcode revision")
    revision = int.from_bytes(raw_revision[:4], byteorder="little")
    if revision < 0x12B:
        raise RuntimeError(
            f"Unsafe Intel CPU microcode 0x{revision:X}; update the MSI motherboard BIOS "
            "to a current stable release containing microcode 0x12B or newer before training"
        )


def _validate_paths(model_path: Path, dataset_dir: Path, output_dir: Path) -> None:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is unavailable")
    for path in (model_path, dataset_dir):
        if not path.exists():
            raise FileNotFoundError(path)
    model_config = json.loads((model_path / "config.json").read_text(encoding="utf-8"))
    if model_config.get("model_type") != "qwen3" or model_config.get("num_hidden_layers") != 40:
        raise RuntimeError(f"Unexpected local model architecture: {model_config}")
    audit = json.loads((dataset_dir / "audit.json").read_text(encoding="utf-8"))
    if not all(audit["checks"].values()):
        raise RuntimeError("Dataset audit contains failed checks")
    if audit["distribution"]["train"] != {
        "samples": 1537,
        "positive": 812,
        "negative": 725,
        "relations": 1128,
    }:
        raise RuntimeError("Dataset distribution differs from the locked training design")
    prompt = (PROJECT_ROOT / "prompts" / "cnc_eval_v2.txt").read_text(
        encoding="utf-8"
    ).strip()
    with (dataset_dir / "train.jsonl").open(encoding="utf-8") as file:
        first_row = json.loads(next(file))
    if first_row["messages"][0] != {"role": "system", "content": prompt}:
        raise RuntimeError("Training data and cnc_eval_v2 prompt are no longer identical")
    if output_dir.exists():
        entries = list(output_dir.iterdir())
        unexpected = [entry for entry in entries if entry.name != "runs"]
        if unexpected:
            raise RuntimeError(f"Output directory is not empty: {unexpected}")


if __name__ == "__main__":
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    if str(PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(PROJECT_ROOT))
    main()
