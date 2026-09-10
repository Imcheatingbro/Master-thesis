# Causal Relation Extraction Thesis Archive

This repository contains the reviewed implementation, processed evaluation data, retrieval resources, selected experiment outputs, and representative notebooks used in the thesis. The archive is organized around a configurable causal-relation extraction pipeline and its knowledge-graph and semantic-evaluation extensions.

## Repository structure

- `src/` contains the reusable Python implementation. It includes dataset loading, prompt construction, local and hosted model clients, structured-output parsing, retrieval, checkpointing, evaluation metrics, knowledge-graph construction and serialization, graph diagnostics, RAMS judging, the KAPipe adapter, and supervised-training utilities.
- `notebooks/` contains the four representative interactive workflows. `main_pipeline_demo1.ipynb` is the general extraction and evaluation entry point; `kg_construction.ipynb` covers knowledge-graph construction and evaluation; `rams_judge_evaluation.ipynb` evaluates semantic role-span judgements; and `kapipe_cdr_baseline.ipynb` runs the KAPipe CDR baseline.
- `configs/` contains `llm.yaml` for an OpenAI-compatible model service and `configs/finetuning/` for the five archived PEFT adapters, bounded smoke runs, the retained Qwen3-8B QLoRA comparison, and the matching Qwen inference services. All repository paths in these configurations are relative to the repository root.
- `prompts/` contains the complete versioned prompt collection for causal extraction, dataset-specific evaluation, knowledge-graph judging, event extraction, RAMS judging, and fine-tuned model variants. Notebook parameters refer to these files by stem, for example `PROMPT_NAME = "v8.7"` loads `prompts/v8.7.txt`.
- `Data/` contains the processed CNC, Li, ADE, PolitiCAUSE, and retained CauseNet evaluation splits; the fine-tuning datasets required by the five archived adapters; the CNC positive-only and RAG evaluation sets; the document-isolated RAMS judge splits; and the relevant manifests, audits, and summary statistics. Raw source downloads remain external.
- `RAG Database/` contains the generic, CNC, and PolitiCAUSE retrieval examples and their BGE embedding matrices. It also contains pattern-completion records, split manifests, the causality-pattern table, ontology resources, and archived CNC database variants used during retrieval development.
- `results/` contains the selected experiment artifacts last modified on or after 2026-07-10. These include evaluation reports, resumable checkpoints, knowledge-graph evaluations, RAMS judge runs, diagnostics, and offline repair backups. Older exploratory outputs are excluded.
- `scripts/` contains supplementary utilities for preparing data, building retrieval databases, creating experiment notebooks, launching training or inference, repairing saved results, running diagnostics, and plotting figures. A one-line description of every script is provided in `scripts/README.md`.
- `outputs/finetuning/` contains the five PEFT adapters reported in the thesis draft: three Qwen CNC variants and two Gemma CNC variants. This path matches the training-output location used by the project scripts. Intermediate checkpoints, smoke outputs, unreported exploratory runs, trainer state, and base-model weights are excluded; the large adapter files are tracked with Git LFS.
- `environment.yml` defines the cross-platform `Master_thesis` Conda environment used by the main pipeline, evaluation, retrieval, and graph workflows. The GPU fine-tuning environments are intentionally kept separate and are described below.
- `environments/` contains the Windows/NVIDIA reference environments used to serve the Qwen and Gemma fine-tuned checkpoints. They are server environments and do not replace the main `environment.yml`.

Base-model weights, API keys, local caches, raw source downloads, and temporary runtime files are not part of the repository.

## Fine-tuning configurations and data paths

The selected training configurations use Hugging Face model IDs and repository-relative data and output paths. Run training or serving commands from the repository root. Replace a model ID with an absolute local model directory only when using an offline copy.

| Archived adapter | Training configuration | Training data |
| --- | --- | --- |
| Qwen3-8B BF16 LoRA | `configs/finetuning/qwen3_8b_cnc_bf16_lora_unsloth_v1.yaml` | `Data/CNC_sft/` |
| Qwen3-8B hard-v2 BF16 LoRA | `configs/finetuning/qwen3_8b_cnc_bf16_lora_hard_v2_e3.yaml` | `Data/CNC_sft_hard_v2/` |
| Qwen3-14B QLoRA | `configs/finetuning/qwen3_14b_cnc_qlora_unsloth_v2_gemma12_profile.yaml` | `Data/CNC_sft_qwen3_14b_original_v1/` |
| Gemma 4 E4B BF16 LoRA | `configs/finetuning/gemma4_e4b_cnc_bf16_lora_unsloth_v1.yaml` | `Data/CNC_sft_gemma_v1/` |
| Gemma 4 12B QLoRA | `configs/finetuning/gemma4_12b_cnc_qlora_unsloth_v1.yaml` | `Data/CNC_sft_gemma_v2/` |

The Qwen service configurations point to the same directories under `outputs/finetuning/` that are stored in Git LFS. Gemma checkpoints are served with `scripts/serve_cnc_unsloth_api.py`, using an explicit base-model path and the corresponding repository-relative adapter path.

## General environment setup

The selected adapter weights are stored with Git LFS. Install Git LFS before cloning, or initialize it and retrieve the weights in an existing checkout:

```bash
git lfs install
git lfs pull
```

If only the source code and non-fine-tuned model workflows are needed, the LFS download may be skipped. Create the general environment and register its Jupyter kernel from the repository root:

```bash
conda env create -f environment.yml
conda activate Master_thesis
python -m ipykernel install --user --name Master_thesis --display-name Master_thesis
jupyter notebook
```

This environment runs the repository code and notebook kernels. It is sufficient for LM Studio and hosted-API experiments, but it does not load the included PEFT adapters directly. Select the `Master_thesis` kernel before running the notebooks. The notebooks resolve paths from either the repository root or the `notebooks/` directory; outputs, execution counts, and machine-specific cell metadata are intentionally removed from the archive.

## External model downloads and recorded identifiers

Large third-party model files are not stored in this repository. This includes the LM Studio GGUF files, KAPipe pretrained snapshots, the base models required by the included PEFT adapters, and the BGE encoder used to build or query the retrieval databases. The identifiers and download sources below match the archived experiment configuration.

### LM Studio models used in the experiments

The table distinguishes the model key sent to the OpenAI-compatible API from the underlying repository and quantized file. Use the exact API key when reproducing a saved run, because that value is also written into report metadata and checkpoint manifests.

| Experiment model | Exact LM Studio API key | Installed variant or file | Download source |
| --- | --- | --- | --- |
| Qwen3.6-35B-A3B | `qwen/qwen3.6-35b-a3b` | `qwen/qwen3.6-35b-a3b@q4_k_m`; `Qwen3.6-35B-A3B-Q4_K_M.gguf` | [`lmstudio-community/Qwen3.6-35B-A3B-GGUF`](https://huggingface.co/lmstudio-community/Qwen3.6-35B-A3B-GGUF) |
| Qwen3.6-27B, non-thinking | `local/qwen3.6-27b-no-thinking` | `local/qwen3.6-27b-no-thinking@q4_k_m`; `Qwen3.6-27B-Q4_K_M.gguf` | [`lmstudio-community/Qwen3.6-27B-GGUF`](https://huggingface.co/lmstudio-community/Qwen3.6-27B-GGUF) |
| Gemma 4 26B-A4B QAT | `google/gemma-4-26b-a4b-qat` | `google/gemma-4-26b-a4b-qat@q4_0`; `gemma-4-26B-A4B-it-QAT-Q4_0.gguf` | [`lmstudio-community/gemma-4-26B-A4B-it-QAT-GGUF`](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-QAT-GGUF) |
| Gemma 4 31B QAT | `google/gemma-4-31b-qat` | `google/gemma-4-31b-qat@q4_0`; `gemma-4-31B-it-QAT-Q4_0.gguf` | [`lmstudio-community/gemma-4-31B-it-QAT-GGUF`](https://huggingface.co/lmstudio-community/gemma-4-31B-it-QAT-GGUF) |
| NuExtract3 KG baseline | `nuextract3` | `NuExtract3-Q4_K_M.gguf` | [`numind/NuExtract3-GGUF`](https://huggingface.co/numind/NuExtract3-GGUF) |

The GGUF files can be downloaded through LM Studio's Discover page by opening the linked repository and selecting the listed quantization. For catalogued models, the equivalent CLI pattern is `lms get <model-key>@<quantization>`; the local Qwen 27B alias is defined separately after its base GGUF has been downloaded. Run `lms ls --json` to confirm the installed API keys and selected variants. Load exactly one chat model and start the server on port `1234` before using `MODEL_NAME = "auto"` in a notebook.

`local/qwen3.6-27b-no-thinking` is a local LM Studio `model.yaml` alias over `Qwen3.6-27B-Q4_K_M.gguf`, with the `enable_thinking` template variable disabled by default. It is not a separate Hugging Face model. One early archived report used the older alias `lmstudio-community/Qwen3.6-27B-GGUF-no-thinking`; the final cross-dataset and RAG runs use `local/qwen3.6-27b-no-thinking`. Reproduction should use the latter label and keep thinking disabled. LM Studio's [`model.yaml` documentation](https://lmstudio.ai/docs/app/modelyaml) describes how to define a local alias over an existing GGUF file.

The local LM Studio inventory also contained `google/gemma-4-12b-qat`, `zai-org/glm-4.7-flash`, and the generic `qwen3.6-27b` entry. These identifiers do not occur as model keys in the archived evaluation reports and are therefore not required to reproduce the reported comparison tables.

### KAPipe source and CDR snapshots

The KAPipe source and pretrained weights are third-party files and are not included. From the repository root, place the upstream source at the path expected by the notebook:

```powershell
New-Item -ItemType Directory -Force "reference code from related work/kapipe-main"
git clone https://github.com/norikinishida/kapipe.git "reference code from related work/kapipe-main/kapipe-main"
```

Download the latest archive from the official [KAPipe Release Files](https://drive.google.com/drive/folders/16ypMCoLYf5kDxglDD_NYoCNAfhTy4Qwp), extract it, and copy the following four CDR snapshot directories into `reference code from related work/kapipe-model/` while preserving this directory structure:

| Component | Required snapshot directory |
| --- | --- |
| Named-entity recognition | `ner/biaffine_ner/biaffine_ner_model_scibertuncased_cdr/raiden163a/` |
| Entity retrieval | `ed_retrieval/blink_bi_encoder/blink_bi_encoder_model_scibertuncased_cdr/raiden512a/` |
| Entity reranking | `ed_reranking/blink_cross_encoder/blink_cross_encoder_model_scibertuncased_cdr/raiden907a/` |
| Document-level relation extraction | `docre/atlop/atlop_model_scibertcased_cdr_overlap/raiden158a/` |

The included notebook uses this repository-local snapshot root rather than KAPipe's default `~/.kapipe` resource directory. If the extracted release is kept elsewhere, update `KAPIPE_MODEL_ROOT` in the notebook. Its preflight cell checks all four paths and their required `model.pt`, configuration, vocabulary, and entity-index files before loading a model. The snapshots also reference [`allenai/scibert_scivocab_uncased`](https://huggingface.co/allenai/scibert_scivocab_uncased) and [`allenai/scibert_scivocab_cased`](https://huggingface.co/allenai/scibert_scivocab_cased); Transformers downloads these backbones automatically when they are not already cached.

### Adapter base models and retrieval encoder

The repository contains PEFT adapters, not their base-model weights. The Qwen adapters use [`Qwen/Qwen3-8B`](https://huggingface.co/Qwen/Qwen3-8B) and [`Qwen/Qwen3-14B`](https://huggingface.co/Qwen/Qwen3-14B); the Gemma adapters use [`google/gemma-4-E4B-it`](https://huggingface.co/google/gemma-4-E4B-it) and [`google/gemma-4-12B-it`](https://huggingface.co/google/gemma-4-12B-it). The model IDs are recorded in each `adapter_config.json`, so the matching serving environment downloads them through Hugging Face when needed. Gemma downloads may require accepting the model licence and authenticating with a Hugging Face account.

Retrieval uses [`BAAI/bge-small-en-v1.5`](https://huggingface.co/BAAI/bge-small-en-v1.5). `sentence-transformers` downloads and caches it automatically on the first run. The committed `.npy` files already contain the embeddings used in the archived retrieval databases, but the encoder is still required to embed new queries or rebuild a database.

## Runtime environments and model backends

The experiments used three Conda environments. They are separated because the evaluation code and the two fine-tuning stacks have different dependency and model-serving requirements.

| Environment | Main use | Validated training or serving path |
| --- | --- | --- |
| `Master_thesis` | Data preparation, extraction and evaluation, RAG, knowledge-graph workflows, RAMS judging, the KAPipe adapter, and the client side of model evaluation | Created from `environment.yml`; calls LM Studio, DeepSeek, LLaMA-Factory, or the direct Unsloth service through an OpenAI-compatible API |
| `Model_finetune` / `Qwen_checkpoint` | Qwen3-8B and Qwen3-14B LoRA/QLoRA training and local serving | LLaMA-Factory CLI with Unsloth enabled; validated with Python 3.11, PyTorch 2.11.0 with CUDA 12.8, Transformers 5.5.0, and Unsloth 2026.8.18 |
| `Gemma_finetune` / `Gemma_checkpoint` | Gemma 4 E4B and Gemma 4 12B Unified LoRA/QLoRA training and local serving | Direct Unsloth `FastModel` API; validated with Python 3.11, PyTorch 2.11.0 with CUDA 12.8, Transformers 5.10.4, and Unsloth 2026.8.19 |

`Master_thesis` is the only environment needed for the notebook kernels included in this archive and for models reached through LM Studio or a hosted API. Loading the original PEFT checkpoints is different: the model server must run in the matching Qwen or Gemma checkpoint environment, while the evaluation notebook remains in `Master_thesis`. The corresponding training notebooks are among the temporarily omitted experiment notebooks described at the end of this README.

The two fine-tuning environments are not interchangeable. Qwen training was stable through LLaMA-Factory's CLI while retaining Unsloth's optimized model loading and training path. The tested Gemma 4 stack instead required Unsloth's direct `FastModel.from_pretrained()` and `FastModel.get_peft_model()` API. In the combined LLaMA-Factory/Unsloth path, LLaMA-Factory expanded the Gemma LoRA targets to full module paths before Unsloth applied its language-layer filter, leaving no matching trainable layers. Direct Unsloth loading allowed the language attention and MLP targets to be selected explicitly without modifying either installed package.

The serving path must also match the training template. LLaMA-Factory's tested `gemma4` inference template added thinking and channel markers, whereas the Gemma adapters were trained with Unsloth's non-thinking `gemma-4` template. Serving those adapters through LLaMA-Factory produced a prompt mismatch and input echoing. Gemma evaluation therefore used a small OpenAI-compatible FastAPI service built directly on Unsloth, with the same `gemma-4` template and thinking disabled. Qwen evaluation continued to use the LLaMA-Factory API. The services used separate ports (`8000` for Qwen and `8001` for Gemma), while the evaluation notebooks themselves remained in `Master_thesis`.

Gemma 4 12B Unified also required Transformers 5.10.4 for its `gemma4_unified` configuration, while the validated Qwen/LLaMA-Factory environment used Transformers 5.5.0. Keeping the environments separate preserves the working Qwen stack, isolates the newer Gemma model support, and prevents CUDA, Triton, trainer, and template dependencies from affecting the general evaluation environment.

### Create a checkpoint-serving environment

The supplied checkpoint environments reproduce the Windows setup used with an NVIDIA RTX 4090 and CUDA 12.8 PyTorch wheels. The final adapters are included under `outputs/finetuning/`; the much larger base-model weights are not included and must be downloaded separately.

For Qwen checkpoints, create the complete LLaMA-Factory/Unsloth service environment with:

```powershell
conda env create -f environments/qwen-checkpoint-windows.yml
conda activate Qwen_checkpoint
```

This environment serves Qwen checkpoints through `llamafactory-cli api`. Its package set also includes Unsloth because the adapters were trained and validated through LLaMA-Factory with Unsloth enabled.

For Gemma checkpoints, first create the direct-Unsloth base environment:

```powershell
conda env create -f environments/gemma-checkpoint-windows.yml
conda activate Gemma_checkpoint
python -m pip install --no-deps --upgrade transformers==5.10.4
```

The final command is mandatory for the archived Gemma 4 12B Unified checkpoints. Transformers 5.5.0 satisfies the dependency metadata declared by the recorded Unsloth release, but it does not contain the required `gemma4_unified` model registration. Transformers 5.10.4 loads that architecture and was used with Unsloth 2026.8.19 for the archived Gemma runs. Because that version is newer than the upper bound declared in the historical Unsloth metadata, `pip check` reports a known Transformers constraint warning after the override; the direct `FastModel` import and all service dependencies were rechecked in a fresh process. LLaMA-Factory is intentionally absent from the Gemma checkpoint environment because the Gemma server does not import or use it.

Both environment files describe the model-server side only. Data loading, prompt construction, metric computation, and report generation continue to run in `Master_thesis`. A Linux or Docker deployment must replace `triton-windows` and the Windows-specific CUDA wheel selection with the corresponding Linux CUDA stack.

## Main extraction and evaluation notebook

Open `notebooks/main_pipeline_demo1.ipynb` for the most complete, configurable workflow. It supports prompt inspection, optional retrieval, short demonstrations, evaluation subsets, full-dataset runs, report generation, and saved-error analysis.

### 1. Select the model service

The default configuration expects LM Studio at `http://127.0.0.1:1234/v1`.

- For LM Studio, load exactly one chat model when `MODEL_NAME = "auto"`, start the local server, and keep `LLM_PROVIDER = "lmstudio"`.
- For a hosted DeepSeek run, set `LLM_PROVIDER = "deepseek"`, choose the explicit model name, change `LLM_BASE_URL` to `https://api.deepseek.com`, and provide the key through the `DEEPSEEK_API_KEY` environment variable or the ignored local file `deepseek_api.txt`.
- Keep `TEMPERATURE = 0.0` for reproducible comparisons. Increase token or context limits only when the selected model truncates long structured outputs.

The initialization cell checks the active kernel, verifies that imports resolve to this checkout, locates the selected dataset, resolves the API key without printing it, and confirms the loaded model.

### 2. Choose the task configuration

The main parameters are defined in the first cell:

| Parameter | Purpose |
| --- | --- |
| `MODE` | Use `"eval"` for dataset evaluation or `"demo"` for the manual and sample demonstration cells. |
| `DATASET` | Selects a registered dataset. The distributed evaluation files support `cnc`, `li`, `ade`, `politicause_train`, `politicause_validation`, `politicause_validation_prompt300`, and `politicause`. |
| `PROMPT_NAME` | Selects a template from `prompts/` without the `.txt` suffix. The prompt must match the target dataset and expected output schema. |
| `PRIMARY_METRIC` | `anchor_window` is the principal thesis extraction metric; strict token F1 is retained as an auxiliary measure. |
| `EVAL_SAMPLE_N` | Limits the development evaluation. The default value of 300 corresponds to the frozen PolitiCAUSE prompt-development subset. |
| `RUN_FULL_EVAL` | Enables a separate full-dataset pass after the bounded evaluation has been inspected. It is `False` by default to prevent an accidental long run. |

For a quick manual check, set `MODE = "demo"`, choose `DEMO_INPUT = "manual"`, and edit `DEMO_TEXT`. To preview real dataset examples instead, use `DEMO_INPUT = "sample"` and set `DEMO_SAMPLE_N`.

### 3. Configure retrieval

Set `USE_RAG = False` for the no-retrieval baseline or `True` for a retrieval condition.

- `RAG_DATABASE = "generic"` uses the general causality database and is suitable for broad cross-domain experiments.
- `RAG_DATABASE = "cnc"` uses the document-disjoint CNC support database.
- `RAG_DATABASE = "politicause"` uses the train-only PolitiCAUSE support database and avoids validation or test leakage.
- `RAG_MODE = "pattern"` retrieves by causal-pattern similarity, `"knn"` uses BGE semantic similarity, and `"knn_pattern"` combines the two rankings.
- `RAG_TOP_K` controls the number of demonstrations inserted into the prompt. The default `1` matches the final single-example comparison; change it only for a stated retrieval-depth experiment.
- `RAG_EMBEDDING_DEVICE = "cpu"` keeps the embedding model from competing with a locally served language model for GPU memory.

Run the cache check and prompt-preview cells before evaluation. They show the resolved database paths, the exact zero-shot and retrieval-augmented prompts, and the retrieved examples without making a model call.

### 4. Validate and run

Run the notebook from top to bottom. The fixed parser and evaluator checks should pass before any dataset evaluation begins. They cover common JSON wrappers, span normalization, token overlap, relation matching, and aggregate error accounting.

In evaluation mode, the bounded run uses `EVAL_SAMPLE_N`. Progress, predictions, and run metadata are handled by the shared evaluation pipeline. If `RUN_FULL_EVAL = True`, the following cell evaluates the complete selected dataset. Local LM Studio runs should normally keep `EVAL_MAX_WORKERS = 1`; hosted services may use controlled concurrency within their rate limits.

Reports are written under `results/eval_report/`, and resumable prediction checkpoints are stored under `results/eval_checkpoints/`. `REPORT_DETAIL_MODE = "errors"` records misclassified samples, while `REPORT_DETAIL_LIMIT` bounds report size. The final two cells can reload a saved report and inspect extraction or detection errors by metric and error bucket.

## Knowledge-graph construction notebook

Open `notebooks/kg_construction.ipynb` and select one workflow with `RUN_MODE` in the first cell. The default `"postprocess"` mode loads the included cached CNC `nested_v1` constructions for samples 370 and 371, then demonstrates deterministic normalization, within-example deduplication, collection-level canonical-resource consolidation, provenance retention, Stanza NER reconciliation, Wikipedia linking, visualization, and RDF serialization. It does not require LM Studio.

- `"visualize"` runs a single-sample construction using gold causal spans or Demo1 predictions and requires the LM Studio service.
- `"postprocess"` reuses `results/kg_evaluation/cnc_nested_v1_n300_20260901_132127_spans.jsonl`; disable `POSTPROCESS_ENABLE_NER` or `POSTPROCESS_ENABLE_WIKIPEDIA` when those optional stages are not required.
- `"rejudge"` reuses saved constructions and reruns the DeepSeek unit Judge and optional global diagnostics without LM Studio.
- `"evaluation"` performs batch construction over gold causal spans and optionally calls the DeepSeek Judge.

The general environment includes Stanza, but its English NER resources are an external model download. Install them once in the default `~/stanza_resources` directory:

```bash
python -c "import stanza; stanza.download('en', processors='tokenize,ner', package={'ner': 'ontonotes-ww-multi_charlm'})"
```

If the resources are stored elsewhere, set `STANZA_MODEL_DIR` in the first cell. Rejudge, global-diagnostic, and judged-evaluation runs require a DeepSeek key in the ignored root-level file `deepseek_api.txt`. Post-processing artifacts are written under `outputs/kg_postprocessing/`; new evaluation results are written under `results/kg_evaluation/`.

## RAMS semantic-judge notebook

Open `notebooks/rams_judge_evaluation.ipynb`. Place the DeepSeek key in the ignored root-level file `deepseek_api.txt`, or update the key path locally. Use `SAMPLE_LIMIT` for a small smoke run or leave it as `None` for all 998 document-isolated test records. Set `RUN_EVALUATION = False` to inspect the dataset summary and prompt without API calls; set it to `True` to run or resume the evaluation.

The notebook saves the validated configuration, dataset and prompt hashes, prompt snapshot, incremental predictions, aggregate metrics, comparisons, and mistakes under `results/rams_judge_evaluation/`. Reusing the same run name is allowed only when the invariant settings and input hashes still match.

## KAPipe CDR baseline notebook

Open `notebooks/kapipe_cdr_baseline.ipynb` after completing the KAPipe setup under **External model downloads and recorded identifiers**. Install the dependencies reported by the preflight cell using the upstream KAPipe instructions.

Enable `RUN_SMOKE` to validate the adapter on the first 100 ADE samples. After checking that result, enable `RUN_FULL_EVAL` and leave `FULL_EVAL_SAMPLE_N = None` for the complete ADE test set. The notebook preserves KAPipe's cross-encoder reranking stage and writes the converted documents, predictions, and evaluation report under `results/eval_report/kapipe_cdr_baseline/`.

## Temporarily omitted notebooks

The remaining experiment notebooks are not included yet because they are largely repeated batch-evaluation copies. Separate notebooks were created during experimentation for convenience, even though they reuse the same execution logic and differ mainly in model, dataset, prompt, or retrieval settings.

Before they are added to the public archive, these copies should be consolidated into one configurable batch-evaluation notebook. Omitting them for now avoids publishing a large set of redundant workflows and makes the intended reusable structure clearer.
