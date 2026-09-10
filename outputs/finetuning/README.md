# Fine-tuned adapters

This directory contains the five PEFT adapters reported in the Stage I fine-tuning results of the thesis draft. Intermediate `checkpoint-*` directories, smoke runs, unreported exploratory variants, optimizer states, scheduler states, and training caches are intentionally excluded.

| Adapter directory | Base model | Dataset or purpose | Server environment |
| --- | --- | --- | --- |
| `qwen3_8b_cnc_bf16_lora_unsloth_v1` | `Qwen/Qwen3-8B` | CNC, BF16 LoRA | `Qwen_checkpoint` |
| `qwen3_8b_cnc_bf16_lora_hard_v2_e3` | `Qwen/Qwen3-8B` | CNC, hard-example BF16 LoRA | `Qwen_checkpoint` |
| `qwen3_14b_cnc_qlora_unsloth_v2_gemma12_profile` | `Qwen/Qwen3-14B` | CNC, final 14B QLoRA run | `Qwen_checkpoint` |
| `gemma4_e4b_cnc_bf16_lora_unsloth_v1` | `google/gemma-4-E4B-it` | CNC, BF16 LoRA | `Gemma_checkpoint` |
| `gemma4_12b_cnc_qlora_unsloth_v1` | `google/gemma-4-12B-it` | CNC, standard rank-16 QLoRA | `Gemma_checkpoint` |

Each directory contains the adapter weights and the tokenizer, processor, and chat-template files needed by the recorded serving path. The Gemma 4 12B adapter is retained as the exploratory raw baseline reported in the table; the draft documents its output-collapse limitation and does not treat it as the selected best model. Base-model weights are not duplicated in this repository. Access to gated base models, where applicable, must be arranged with the original model provider.

Use `environments/qwen-checkpoint-windows.yml` for Qwen adapters and `environments/gemma-checkpoint-windows.yml` plus the documented Transformers override for Gemma adapters. The model service and the `Master_thesis` evaluation client run in separate processes.

The adapter weights are stored with Git LFS. Clone the repository with Git LFS enabled or run `git lfs pull` after cloning.
