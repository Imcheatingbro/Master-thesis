# Fine-tuning Configurations

This directory contains the configurations associated with the five archived PEFT adapters. Model references use Hugging Face repository IDs, while dataset, prompt, adapter, cache, and output paths are relative to the repository root. The original Qwen3-8B QLoRA train/smoke pair is also retained because it is the target of `scripts/run_cnc_qlora.ps1` and provides the reported comparison baseline; its adapter is not part of the selected checkpoint archive.

| Configuration | Purpose | Dataset directory | Output or adapter directory |
| --- | --- | --- | --- |
| `qwen3_8b_cnc_bf16_lora_unsloth_v1.yaml` | Qwen3-8B CNC BF16 LoRA training | `Data/CNC_sft/` | `outputs/finetuning/qwen3_8b_cnc_bf16_lora_unsloth_v1/` |
| `qwen3_8b_cnc_bf16_lora_hard_v2_e3.yaml` | Qwen3-8B hard-example three-epoch LoRA training | `Data/CNC_sft_hard_v2/` | `outputs/finetuning/qwen3_8b_cnc_bf16_lora_hard_v2_e3/` |
| `qwen3_14b_cnc_qlora_unsloth_v2_gemma12_profile.yaml` | Qwen3-14B final CNC QLoRA training | `Data/CNC_sft_qwen3_14b_original_v1/` | `outputs/finetuning/qwen3_14b_cnc_qlora_unsloth_v2_gemma12_profile/` |
| `gemma4_e4b_cnc_bf16_lora_unsloth_v1.yaml` | Gemma 4 E4B CNC BF16 LoRA training | `Data/CNC_sft_gemma_v1/` | `outputs/finetuning/gemma4_e4b_cnc_bf16_lora_unsloth_v1/` |
| `gemma4_12b_cnc_qlora_unsloth_v1.yaml` | Gemma 4 12B CNC QLoRA training | `Data/CNC_sft_gemma_v2/` | `outputs/finetuning/gemma4_12b_cnc_qlora_unsloth_v1/` |

`qwen3_8b_cnc_bf16_lora_unsloth_smoke.yaml` is the bounded preflight configuration for the selected Qwen3-8B BF16 run. The `qwen3_8b_cnc_qlora_{smoke,v1}.yaml` pair supports the separate QLoRA launcher. The three `*_api.yaml` files serve the corresponding archived Qwen adapters from their repository-relative paths. Run LLaMA-Factory commands from the repository root so these relative paths resolve consistently. A local base-model directory may replace a Hugging Face model ID when an offline copy is preferred.
