# Script Reference

The selected notebooks do not invoke these scripts directly; they are retained as supplementary utilities for data preparation, experiment execution, recovery, diagnostics, and figure generation.

- `add_li_gemma_generic_rerun_cells.py`: Appends two Gemma generic-RAG rerun sections to the Li batch notebook.
- `build_cnc_rag_database.py`: Builds a document-disjoint CNC RAG support database and complementary evaluation set.
- `build_embedding_cache.py`: Encodes RAG examples with BGE and saves the metadata and embedding cache.
- `build_politicause_rag_database.py`: Builds a train-only PolitiCAUSE RAG database without validation or test leakage.
- `build_politicause_test_batch_notebook.py`: Generates the frozen eight-run PolitiCAUSE test notebook.
- `build_qwen_family_three_dataset_notebook.py`: Generates the unified twelve-run Qwen cross-dataset evaluation notebook.
- `diagnose_gemma_relation_continuation.py`: Analyzes Gemma continuation and stopping behavior at gold triple boundaries.
- `plot_cnc_finetuning_loss.py`: Converts CNC training logs into loss data and a publication-ready SVG figure.
- `plot_cnc_positive_vs_joint_extraction.py`: Renders the CNC positive-only versus joint-extraction F1 comparison.
- `plot_model_family_selection.py`: Renders the benchmark figure used to compare candidate model families.
- `prepare_ade_sft_data.py`: Creates compact, relation-stratified ADE splits for supervised fine-tuning.
- `prepare_cnc_hard_sft_data.py`: Resamples difficult CNC examples for second-stage LoRA training.
- `prepare_cnc_prompt_variant_data.py`: Copies CNC fine-tuning splits while replacing only the system prompt.
- `prepare_cnc_sft_data.py`: Creates document-disjoint, stratified, and auditable CNC fine-tuning splits.
- `prepare_cnc_triples_only_data.py`: Converts CNC fine-tuning targets to the triples-only output schema.
- `prepare_gemma12_overfit20.py`: Selects a fixed twenty-example dataset for the Gemma overfitting diagnostic.
- `prepare_qwen3_14b_cnc_data.py`: Creates the audited CNC training dataset used by the Qwen3-14B run.
- `rejudge_kg_saved_results.py`: Applies a new knowledge-graph judge rubric to saved extraction spans.
- `repair_cnc_rag_database.py`: Repairs the CNC RAG support split and completes missing causal patterns.
- `repair_kg_global_diagnostics.py`: Reparses saved knowledge-graph global diagnostics without model calls.
- `repair_phase2_qwen27_missing_triple.py`: Repairs the defined Qwen missing-brace failure and rebuilds affected reports offline.
- `repartition_ade_85_15.py`: Repartitions the canonical ADE pool into an 85/15 train-test split.
- `repartition_causenet.py`: Repartitions the retained CauseNet pool into train, validation, and test splits.
- `rerun_phase2_degenerate_failures.py`: Reruns eligible repetitive-output failures with a freshly loaded model and rebuilds summaries.
- `run_cnc_bf16_lora_unsloth.ps1`: Launches the configured CNC BF16 LoRA training workflow with Unsloth.
- `run_cnc_qlora.ps1`: Launches the configured CNC QLoRA training workflow.
- `run_kg_judge_calibration.py`: Runs the fixed ten-case calibration for knowledge-graph judge versions 2 and 3.
- `run_qwen3_cnc_inference_api.ps1`: Starts the local inference endpoint for a selected Qwen CNC model variant.
- `serve_cnc_unsloth_api.py`: Serves a fine-tuned CNC model through a local OpenAI-compatible API.
- `train_qwen3_14b_cnc_unsloth.py`: Trains the Qwen3-14B CNC adapter directly with Unsloth and TRL.
