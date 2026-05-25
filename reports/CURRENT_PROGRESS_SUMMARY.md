# 当前阶段工作总结

更新时间：2026-05-25

## 已完成的主要工作

- 数据集已经整理为统一的 `id/text/has_causal/relations` 格式，当前 pipeline 支持 `cnc`、`li`、`ade`、`causenet` 四个数据集。
- notebook 顶部配置已集中管理数据集、prompt、RAG、模型、生成参数和 eval 参数，`MODEL_NAME="auto"` 时会从 LM Studio 当前 loaded 模型中自动识别唯一聊天模型。
- Prompt 已迭代到 `v4`，当前实验主要围绕 CNC-style 因果三元组抽取，并要求模型输出固定 JSON schema。
- RAG 已实现三种模式：`pattern`、`knn`、`knn_pattern`。其中 `knn_pattern` 会拼接 Pattern RAG 与 BGE KNN 检索结果，并按 `(sentence, cause, effect)` 去重。
- BGE 检索使用本地缓存：`RAG Database/bge-small-en-v1.5_examples.jsonl` 与 `RAG Database/bge-small-en-v1.5_embeddings.npy`。
- evaluation 已从 notebook 中抽出到 `src/eval_pipeline.py`，报告会落盘到 `results/eval_report`，并保存配置、最终指标、生成失败统计和样本明细。

## 模型与 thinking 问题

- 已测试 `qwen/qwen3-14b` 与 `Qwen3.5-9B` 系列模型。14B 在 4090 上速度可接受，并且 thinking 行为相对稳定。
- 为 Qwen3.5 9B 创建过 LM Studio no-thinking 虚拟模型，通过 `model.yaml` 暴露 `Enable Thinking` 开关，并验证过小规模 eval 不再出现 reasoning-only 空正文失败。
- 也测试过 structured output。它能约束输出格式，但在 thinking 模型上可能出现 `content=""`、JSON 被放进 `reasoning_content` 的边界行为。
- 曾尝试从 `reasoning_content` 兜底解析 JSON，但发现风险较高：普通 `Thinking Process` 里可能复述 prompt 中的 JSON 示例，宽松解析会把示例误判为最终答案。
- 当前最终决策：不从 `reasoning_content` 解析答案。程序只解析 `content`；如果模型只返回 `reasoning_content` 且 `content=""`，记录为 `llm_reasoning_only_empty_content`。这个问题目前没有代码层面的可靠解决方案，优先通过模型选择或关闭 thinking 来规避。

## Evaluation 定义

- Detection 是句子级二分类，直接比较 `pred.has_causal` 与 `gold.has_causal`，统计 Accuracy、Precision、Recall、F1 以及 TP/TN/FP/FN。
- Extraction 分两种视角：
- `all_samples`：忽略 `has_causal`，在全部样本上匹配 pred triples 与 gold relations，是当前主要观察指标。
- `detected_only`：只在 gold=True 且 pred=True 的样本上观察 span 抽取质量，主要用于诊断。
- Extraction 当前保留两种匹配方法：
- `strict_token_f1`：对 cause/effect 分别做 token F1，并取二者较小值作为 triple pair 分数；CNC/Li 的主指标。
- `anchor_window`：用于 ADE/CauseNet 这类 gold 更接近 concept anchor 的数据集。
- 本文下方结果表使用 `Extraction all_samples` 的第一种方法，即 `strict_token_f1`。

## 当前三份结果对比

三份 report 都是 `cnc` 前 20 条、`prompt=v4`、`temperature=0.0`、`max_tokens=2048`，并且 `generation_failures.total=0`。

| 实验 | Report | RAG | Thinking 状态 | Detection Acc | Detection P | Detection R | Detection F1 | Detection TP/TN/FP/FN | Extraction all_samples strict P | Extraction all_samples strict R | Extraction all_samples strict F1 | Gold/Pred triples |
|---|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---|
| Qwen3 14B，较早结果 | `qwen-qwen3-14b_cnc-n20_prompt-v4_rag-knn_pattern-k2_20260525-211730.md` | `knn_pattern-k2` | 未开 thinking | 0.700 | 0.833 | 0.500 | 0.625 | 5/9/1/5 | 0.500 | 0.333 | 0.400 | 15/10 |
| Qwen3 14B，较晚结果 | `qwen-qwen3-14b_cnc-n20_prompt-v4_rag-knn_pattern-k2_20260525-211814.md` | `knn_pattern-k2` | 开 thinking | 0.800 | 0.750 | 0.900 | 0.818 | 9/7/3/1 | 0.600 | 0.600 | 0.600 | 15/15 |
| Qwen3.5 9B no-thinking | `Manojb-Qwen3.5-9B-Q8_0-no-thinking_cnc-n20_prompt-v4_rag-off_20260525-221803.md` | `off` | 虚拟模型关闭 thinking | 0.950 | 0.909 | 1.000 | 0.952 | 10/9/1/0 | 0.833 | 0.667 | 0.741 | 15/12 |

## 当前判断

- 在这三份小样本结果中，`Qwen3.5-9B-Q8_0-no-thinking` 的 detection 与 extraction all_samples strict F1 都最高，但它没有启用 RAG，因此不能直接和两个 14B RAG 实验做严格模型能力对比。
- 14B 开 thinking 的结果明显好于 14B 未开 thinking 的结果，尤其 recall 和 extraction F1 提升明显。
- structured output + thinking 的通道分离问题暂时不作为主线继续硬修；后续更稳的方向是使用非 thinking / no-thinking 模型，或确认 LM Studio 侧能真正把最终答案写入 `content`。
