# 当前阶段工作总结

更新时间：2026-05-25

## 已完成的主要工作

- 数据集已经整理为统一的 `id/text/has_causal/relations` 格式，当前 pipeline 支持 `cnc`、`li`、`ade`、`causenet` 四个数据集。
- notebook 顶部配置已集中管理数据集、prompt、RAG、模型、生成参数和 eval 参数，`MODEL_NAME="auto"` 时会从 LM Studio 当前 loaded 模型中自动识别唯一聊天模型。
- Prompt 已迭代到 `v4`，当前实验主要围绕 CNC-style 因果三元组抽取，并要求模型输出固定 JSON schema。
- RAG 已实现三种模式：`pattern`、`knn`、`knn_pattern`。其中 `knn_pattern` 会拼接 Pattern RAG 与 BGE KNN 检索结果，并按 `(sentence, cause, effect)` 去重。
- BGE 检索使用本地缓存：`RAG Database/bge-small-en-v1.5_examples.jsonl` 与 `RAG Database/bge-small-en-v1.5_embeddings.npy`。
- evaluation 已从 notebook 中抽出到 `src/eval_pipeline.py`，报告会落盘到 `results/eval_report`，并保存配置、最终指标、生成失败统计和样本明细。

## 数据结构与当前数据文件

当前四个可评估数据集都被统一成 JSONL，每一行是一条句子级样本：

```json
{
  "id": 1,
  "text": "原始句子文本",
  "has_causal": true,
  "relations": [
    {
      "cause": "gold cause span",
      "effect": "gold effect span"
    }
  ]
}
```

- `id`：当前文件内重新编号的样本 ID，不保证跨 train/test 或跨数据集唯一。
- `text`：模型实际输入的句子文本。
- `has_causal`：句子级 detection gold label。
- `relations`：gold 因果关系列表；非因果样本为空列表。一个句子可以对应多个因果关系，例如同一句中有两个原因、两个结果或多个独立因果事件。
- 生成端模型输出字段叫 `triples`，其中每条 triple 使用 `cause.span / relation / effect.span`；evaluation 时会把 `pred.triples` 与 `gold.relations` 做匹配。

当前 `src.data_io.load_dataset()` 支持四个名称：

| dataset 名称 | 文件 | 当前用途 | 主 evaluation 匹配方式 |
|---|---|---|---|
| `cnc` | `Data/Dataset_1_CNC_modified.jsonl` | eval/test | `strict_token_f1` |
| `li` | `Data/Dataset_2_Li_modified.jsonl` | eval/test | `strict_token_f1` |
| `ade` | `Data/Dataset_3_ADE_modified.jsonl` | eval/test | `anchor_window` |
| `causenet` | `Data/Dataset_4_causenet_modified.jsonl` | eval/test | `anchor_window` |

当前统计来自 `Data/stats.json`：

| 数据集 | 样本数 | causal | non-causal | gold relations | 备注 |
|---|---:|---:|---:|---:|---|
| CNC | 3,075 | 1,624 | 1,451 | 2,257 | 原始 CSV 的 `<ARG0>/<ARG1>` span 被解析为较完整的事件/短语 span。 |
| Li | 786 | 191 | 595 | 296 | 原始 XML 中实体标签映射为 cause/effect span。 |
| ADE test | 5,882 | 895 | 4,987 | 1,317 | 从 Hugging Face classification + relation 两份数据合并；BGE example 中出现过的句子已剔除。 |
| ADE train | 13,727 | 2,090 | 11,637 | 3,238 | 位于 `Data/finetuning/Dataset_3_ADE_train.jsonl`，按 causal/non-causal 分层随机切分，seed=`20260524`。 |
| CauseNet test | 5,000 | 5,000 | 0 | 5,908 | 从 CauseNet sentence sources 清洗后随机抽样；全部为 causal 样本。 |
| CauseNet train | 10,000 | 10,000 | 0 | 11,653 | 位于 `Data/finetuning/Dataset_4_causenet_train.jsonl`，seed=`20260524`。 |

各数据集的标注粒度并不完全一致，这是后面采用两种 extraction 匹配方式的根本原因：

- CNC/Li 更接近“文本 span 抽取”任务，gold 往往是较完整的短语或事件片段。例如 CNC 中：

```json
{
  "text": "The State alleged they hacked Sabata Petros Chale , 39 , to death in Marikana West , on December 8 , 2016 , allegedly over the allocation of low cost ( RDP ) houses at Marikana West Extension 2 .",
  "relations": [
    {
      "cause": "the allocation of low cost ( RDP ) houses at Marikana West Extension 2",
      "effect": "they hacked Sabata Petros Chale , 39 , to death in Marikana West , on December 8 , 2016"
    }
  ]
}
```

如果模型只输出 `hacked Sabata Petros Chale`，就漏掉了主语、时间、地点等成分。对 CNC/Li 来说，这类缺失应该被评价指标惩罚。

- ADE/CauseNet 更接近“concept anchor 标注”，gold 往往比自然语言中的合理抽取 span 短。例如 ADE 中：

```json
{
  "text": "Fixed drug eruption in hands caused by omeprazole.",
  "relations": [
    {
      "cause": "omeprazole",
      "effect": "eruption"
    }
  ]
}
```

模型如果输出 `Fixed drug eruption in hands` 或 `drug eruption in hands` 作为 effect，并不一定是错误；只是它比 gold concept anchor 更长。再例如 CauseNet 中：

```json
{
  "text": "Drug users also may become involved in risky sexual behaviors, which could lead to the spread of HIV, the virus that causes AIDS.",
  "relations": [
    {
      "cause": "virus",
      "effect": "AIDS"
    }
  ]
}
```

模型可能抽到更自然的 `the virus`，甚至更长的局部短语。若用 CNC/Li 的严格 span 标准，会把大量“包含 gold anchor 的合理长 span”误判为错。

## 模型与 thinking 问题

- 已测试 `qwen/qwen3-14b` 与 `Qwen3.5-9B` 系列模型。14B 在 4090 上速度可接受，并且 thinking 行为相对稳定。
- 为 Qwen3.5 9B 创建过 LM Studio no-thinking 虚拟模型，通过 `model.yaml` 暴露 `Enable Thinking` 开关，并验证过小规模 eval 不再出现 reasoning-only 空正文失败。
- 也测试过 structured output。它能约束输出格式，但在 thinking 模型上可能出现 `content=""`、JSON 被放进 `reasoning_content` 的边界行为。
- 曾尝试从 `reasoning_content` 兜底解析 JSON，但发现风险较高：普通 `Thinking Process` 里可能复述 prompt 中的 JSON 示例，宽松解析会把示例误判为最终答案。
- 当前最终决策：不从 `reasoning_content` 解析答案。程序只解析 `content`；如果模型只返回 `reasoning_content` 且 `content=""`，记录为 `llm_reasoning_only_empty_content`。这个问题目前没有代码层面的可靠解决方案，优先通过模型选择或关闭 thinking 来规避。

## Evaluation 定义

- Detection 是句子级二分类，直接比较 `pred.has_causal` 与 `gold.has_causal`，统计 Accuracy、Precision、Recall、F1 以及 TP/TN/FP/FN。
- Extraction 分两种统计视角：
  - `all_samples`：忽略 `has_causal` 字段，直接在全部样本上匹配 `pred.triples` 与 `gold.relations`。这是当前主要观察指标，因为它把 detection 漏检也计入 extraction 的总体损失：如果 gold 有因果但模型说没有因果，就会产生 FN。
  - `detected_only`：只在 `gold.has_causal=True` 且 `pred.has_causal=True` 的样本上观察 span 抽取质量。它不作为主要结论指标，主要用于诊断：当 `all_samples` 很低时，可以区分问题来自 detection 漏检，还是来自已经检测到因果之后 span 抽得不好。
- Extraction 同时保留两种 span 匹配方法：
  - `strict_token_f1`：先对 cause span 和 effect span 分别做 token-level F1，再取二者较小值作为一个 triple pair 的分数；分数达到 `0.8` 才算匹配成功。它适合 CNC/Li，因为这两个数据集的 gold 更像完整文本 span。例子：gold effect 是 `they hacked Sabata Petros Chale , 39 , to death in Marikana West , on December 8 , 2016`，如果模型只输出 `hacked Sabata Petros Chale`，应当被视为不完整抽取。
  - `anchor_window`：把 gold cause/effect 当作较短的 concept anchor，只要 gold anchor 能在更长的 prediction span 中被窗口匹配到，且分数达到 `0.9`，就算匹配成功。它适合 ADE/CauseNet，因为这两个数据集的 gold 常常只是药物、疾病、概念词，而模型输出更长的自然语言 span 往往仍然合理。例子：gold 是 `azithromycin -> ototoxicity`，prediction 是 `Intravenous azithromycin -> severe ototoxicity`，`strict_token_f1` 会判失败，但 `anchor_window` 会判成功。
- 主指标按数据集自动选择：`cnc/li` 使用 `strict_token_f1`，`ade/causenet` 使用 `anchor_window`。报告里仍同时输出两种方法，方便排查不同标注粒度带来的差异。
- 本文下方三份结果表都是 `cnc` 前 20 条，因此表内 extraction 数值使用 `Extraction all_samples / strict_token_f1`。

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
