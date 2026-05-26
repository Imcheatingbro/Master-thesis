# 当前阶段工作总结

更新时间：2026-05-26

## 1. Proposal 原始目标

原 proposal 的主线是：从多领域文本中直接生成结构化因果三元组，再经过轻量后处理构建跨领域 causal knowledge graph。

核心研究目标可以拆成四层：

| 层级 | Proposal 中的设想 | 当前状态 |
|---|---|---|
| 因果三元组生成 | LLM 在一次生成中完成 cause/effect 边界识别、关系判断和结构化输出 | 已打通，当前输出采用 JSON triples，而不是 GoLLIE 风格 Python object |
| RAG 增强 | 基于 causal pattern database 做 retrieval-augmented few-shot generation | 已实现 Pattern、KNN、KNN+Pattern 三种模式 |
| 跨领域数据 | 使用 Li et al.、ADE、CauseNet 三类不同粒度/领域数据 | 已支持 Li、ADE、CauseNet，并额外加入 CNC 作为高质量 span benchmark |
| KG 构建与评估 | entity normalisation、Wikipedia linking、RDFS/OWL、ontology alignment、graph-level evaluation | 尚未开始，属于下一阶段 |

因此，目前项目完成的是 proposal 中第一阶段的核心能力：

```text
raw/cleaned text -> prompt/RAG -> local LLM -> JSON causal triples -> triple-level evaluation report
```

尚未进入完整 causal knowledge graph construction 阶段。

## 2. 当前阶段结论

截至目前，我们已经完成了一个可复现的本地因果三元组抽取与评估 pipeline。

它能够：

- 读取统一格式的数据集。
- 在 notebook 中切换数据集、模型、prompt、RAG 和评估规模。
- 调用 LM Studio 本地 OpenAI-compatible API。
- 使用 prompt v4 生成固定 JSON schema 的 causal triples。
- 可选启用 Pattern RAG、KNN RAG 或混合 RAG。
- 对 detection 和 extraction 分层评估。
- 把最终指标、生成失败类型和样本明细写入 Markdown report。

当前阶段最重要的边界是：

- 我们已经能评价“模型能否从句子中抽出因果三元组”。
- 我们还没有评价“这些三元组能否组成高质量 causal knowledge graph”。
- KG 构建、实体归一化、实体链接、RDFS/OWL 输出和 graph-level evaluation 是后续工作。

## 3. 按顺序已经完成的工作

### 3.1 项目基础与运行环境

- 建立了项目级约定：统一使用 conda 环境 `Master_thesis`，库代码不直接 `print`，经验和取舍记录到 `reports/LESSONS.md`。
- 主 notebook 使用 `PROJECT_ROOT` 解析路径，减少从不同目录启动 Jupyter 时路径错误的问题。
- 当前 notebook 作为主实验入口，顶部集中配置数据集、模型、prompt、RAG、token 参数和 report 保存策略。
- LM Studio 作为本地模型服务入口，项目通过 OpenAI-compatible API 调用本地模型。

### 3.2 数据清洗与统一 schema

最初 proposal 计划使用 Li et al.、ADE、CauseNet 三个数据集。实际实现中，我们额外加入 CNC，用来提供更接近完整 span/event 的高质量评估样本。

当前所有可评估数据都统一为：

```json
{
  "id": 1,
  "text": "sentence text",
  "has_causal": true,
  "relations": [
    {"cause": "gold cause span", "effect": "gold effect span"}
  ]
}
```

当前数据集状态：

| 数据集 | 文件 | 样本数 | causal | non-causal | gold relations | 当前主要用途 |
|---|---|---:|---:|---:|---:|---|
| CNC | `Data/Dataset_1_CNC_modified.jsonl` | 3,075 | 1,624 | 1,451 | 2,257 | 完整 span/event 抽取评估 |
| Li | `Data/Dataset_2_Li_modified.jsonl` | 786 | 191 | 595 | 296 | 多因果 pair 与细粒度 span 评估 |
| ADE test | `Data/Dataset_3_ADE_modified.jsonl` | 5,882 | 895 | 4,987 | 1,317 | 医学领域 drug -> adverse effect 评估 |
| ADE train | `Data/finetuning/Dataset_3_ADE_train.jsonl` | 13,727 | 2,090 | 11,637 | 3,238 | 后续微调候选数据 |
| CauseNet test | `Data/Dataset_4_causenet_modified.jsonl` | 5,000 | 5,000 | 0 | 5,908 | 大规模开放域弱监督 causal resource |
| CauseNet train | `Data/finetuning/Dataset_4_causenet_train.jsonl` | 10,000 | 10,000 | 0 | 11,653 | 后续微调候选数据 |

重要处理：

- CNC 从 `<ARG0>/<ARG1>` 中提取 cause/effect，并保留原句空格和标点风格。
- Li 从 XML 中的 `<eN>` 实体和 `Cause-Effect((eX,eY),...)` label 构建多因果 relations。
- ADE 合并 Hugging Face classification 与 drug-ADE relation 两份数据，且剔除了与 RAG few-shot example 重叠的句子，避免评估串样。
- CauseNet 只保留有 sentence provenance 的 source，并从大规模弱监督资源中抽样构建 train/test/extra。

### 3.3 LLM Client 与 notebook 配置

- 实现 `src/llm_client.py`，封装 LM Studio chat completion 调用。
- 支持从 `configs/llm.yaml` 读取默认配置，也支持 notebook 覆盖模型名、token、timeout、temperature 等参数。
- 支持 `MODEL_NAME="auto"`，从 LM Studio 当前 loaded models 中自动识别唯一聊天模型。
- 保留 `extra_body` 通用能力，但当前默认不再主动传入 thinking/reasoning 相关参数。
- 生成失败会带上错误类型和错误信息，便于在 report 中统计。

### 3.4 Prompt 迭代

Prompt 已从早期版本迭代到 `prompts/v4.txt`。

当前 v4 的目标更明确：

- 输出固定 JSON schema：`has_causal` + `triples`。
- 每个 triple 包含 `cause.span`、`relation="caused"`、`effect.span`。
- 强调 CNC-style span 边界，尽量抽完整 event/state span。
- 约束模型不要输出解释、markdown 或额外文本。
- 对无因果样本输出 `{"has_causal": false, "triples": []}`。

和 proposal 的差异：

- proposal 原计划借鉴 GoLLIE，使用 Python class/docstring 作为结构化 guideline，并输出 Python object。
- 当前为了本地 LM Studio、JSON parser 和 notebook evaluation 的稳定性，阶段性采用 JSON schema 输出。
- 这个调整降低了格式解析难度，也更适合当前批量 evaluation；是否回到 GoLLIE-style Python object 可留到模型/论文对比阶段再决定。

### 3.5 RAG 实现

参考 PatternRAG 原论文代码后，我们实现了三种检索模式：

| RAG 模式 | 当前实现 | 作用 |
|---|---|---|
| `pattern` | 基于 causal connective / pattern 的表面匹配 | 找因果表达结构相似的 examples |
| `knn` | 基于 BGE embedding 的语义近邻 | 找语义相似 examples |
| `knn_pattern` | 拼接 Pattern 与 KNN，再去重 | 同时利用结构相似和语义相似 |

当前 RAG 资源：

- Pattern DB：`RAG Database/comb_SCITEsemADE_CausalityPattern.csv`
- BGE examples：`RAG Database/bge-small-en-v1.5_examples.jsonl`
- BGE embeddings：`RAG Database/bge-small-en-v1.5_embeddings.npy`
- embedding 模型：`BAAI/bge-small-en-v1.5`

和 proposal 的关系：

- proposal 中提到借鉴 Pattern RAG，并探索改进 retrieval strategy。
- 当前已经超过最小目标：不仅实现了 pattern retrieval，也加入了 dense KNN 和 hybrid retrieval。

### 3.6 Generator 与解析策略

- 实现 `src/generator.py`，串联 prompt builder、LLM client、输出解析和最小 schema 校验。
- `parse_output()` 支持纯 JSON、markdown code block、前缀解释文本和完整 `<think>...</think>` 后的 JSON。
- 生成失败时不会中断整个 evaluation，而是返回兜底结构，并记录 `error_type` 与 `error_message`。
- 当前不强制检查模型输出 span 是否为原文子串；span 质量统一交给 evaluator 处理。

已经决定不做的解析策略：

- 不再从 `reasoning_content` 里兜底解析 JSON。
- 原因是 thinking 模型可能在 reasoning 中复述 prompt 示例 JSON，宽松解析容易把示例误判为最终答案。

### 3.7 Evaluation 设计与实现

当前 evaluator 已经从 notebook 抽到源码中：

- `src/evaluator.py`：负责 detection/extraction 指标计算。
- `src/eval_pipeline.py`：负责流式评估、进度快照、report 落盘和样本明细。
- report 输出目录：`results/eval_report/`

当前 evaluation 分两层：

| 层级 | 评价对象 | 指标 |
|---|---|---|
| Detection | `pred.has_causal` vs `gold.has_causal` | Accuracy / Precision / Recall / F1 / TP/TN/FP/FN |
| Extraction | `pred.triples` vs `gold.relations` | Precision / Recall / F1 / TP/FP/FN |

Extraction 有两种视角：

| 视角 | 含义 | 用途 |
|---|---|---|
| `all_samples` | 所有样本都参与，不管 detection 是否正确 | 当前主观察指标，反映端到端抽取效果 |
| `detected_only` | 只看 gold=True 且 pred=True 的样本 | 诊断 span 质量，排除 detection 错误影响 |

Extraction 有两种匹配方法：

| 方法 | 适合数据 | 解释 |
|---|---|---|
| `strict_token_f1` | CNC / Li | gold 更接近完整 span/event，需要惩罚边界不完整 |
| `anchor_window` | ADE / CauseNet | gold 更像 concept anchor，允许模型输出更长但包含 anchor 的合理 span |

当前主指标选择：

| 数据集 | 主 extraction metric |
|---|---|
| CNC | `strict_token_f1` |
| Li | `strict_token_f1` |
| ADE | `anchor_window` |
| CauseNet | `anchor_window` |

多因果匹配已经升级为全局最优 one-to-one matching：

- 一个预测 triple 最多匹配一个 gold relation。
- 一个 gold relation 最多被一个预测 triple 命中。
- 先最大化 TP 数；TP 相同再最大化总匹配分数。
- 这避免了 greedy 局部最优在多因果样本中少算 TP，也避免重复预测同一 gold 被多次计分。

### 3.8 模型与本地推理实验

当前主要围绕本地 4090 + LM Studio 运行。

已测试或处理过的模型/设置：

- `qwen/qwen3-14b`
- `Qwen3.5-9B` GGUF 系列
- `Manojb/Qwen3.5-9B-Q8_0-no-thinking` 虚拟模型

关键结论：

- Qwen3 14B 在 thinking 开启时可以正常产出 `content`，thinking 长度相对可控。
- Qwen3.5 9B 在 LM Studio 中容易出现 `content=""`、答案或 JSON 落入 `reasoning_content` 的问题。
- `reasoning="off"`、`chat_template_kwargs.enable_thinking=False`、`/no_think` 等方法对 Qwen3.5 9B 并不稳定。
- 最终通过 LM Studio `model.yaml` 创建 no-thinking 虚拟模型，暴露 `Enable Thinking` 开关，并在 UI 中关闭 thinking，才得到更稳定的批量 evaluation 行为。
- 当前代码层面不再传默认 thinking/reasoning 参数；优先依赖 LM Studio 模型配置解决。

## 4. 当前已有实验结果

以下结果主要用于阶段判断，还不能作为最终论文结论。当前这一组 report 的重点是检查 pipeline、prompt、RAG 和不同数据集主指标是否能稳定产出可比较结果。

### 4.1 当前本地 100 条结果

#### 4.1.1 Qwen3.5 9B no-thinking baseline

| 数据集/样本 | Gold causal / Gold triples | 主 extraction metric | Detection P/R/F1 | Extraction all_samples P/R/F1 | Extraction detected_only P/R/F1 | 生成失败 |
|---|---:|---|---|---|---|---:|
| CNC n=100 | 51 / 74 | `strict_token_f1` | 0.864 / 0.745 / 0.800 | 0.500 / 0.311 / 0.383 | 0.575 / 0.383 / 0.460 | 0 |
| ADE n=100 | 100 / 124 | `anchor_window` | 1.000 / 0.470 / 0.639 | 0.804 / 0.331 / 0.469 | 0.804 / 0.621 / 0.701 | 0 |

#### 4.1.2 Qwen3.5 35B-A3B n=100 对比

| 数据集/样本 | Prompt | RAG | Gold causal / Gold triples | 主 extraction metric | Detection P/R/F1 | Extraction all_samples P/R/F1 | Extraction detected_only P/R/F1 | 生成失败 |
|---|---|---|---:|---|---|---|---|---:|
| ADE n=100 | v4 | off | 100 / 124 | `anchor_window` | 1.000 / 0.430 / 0.601 | 0.894 / 0.339 / 0.491 | 0.894 / 0.778 / 0.832 | 0 |
| ADE n=100 | v3 | off | 100 / 124 | `anchor_window` | 1.000 / 0.690 / 0.817 | 0.929 / 0.524 / 0.670 | 0.929 / 0.747 / 0.828 | 0 |
| ADE n=100 | v3 | `knn_pattern-k3` | 100 / 124 | `anchor_window` | 1.000 / 0.910 / 0.953 | 0.968 / 0.734 / 0.835 | 0.968 / 0.812 / 0.883 | 0 |
| CNC n=100 | v3 | off | 51 / 74 | `strict_token_f1` | 0.841 / 0.725 / 0.779 | 0.447 / 0.284 / 0.347 | 0.525 / 0.356 / 0.424 | 0 |
| CNC n=100 | v3 | `knn_pattern-k3` | 51 / 74 | `strict_token_f1` | 0.871 / 0.529 / 0.659 | 0.486 / 0.230 / 0.312 | 0.548 / 0.378 / 0.447 | 0 |
| CauseNet n=100 | v3 | off | 100 / 121 | `anchor_window` | 1.000 / 0.880 / 0.936 | 0.589 / 0.545 / 0.567 | 0.589 / 0.611 / 0.600 | 0 |
| CauseNet n=100 | v3 | `knn_pattern-k3` | 100 / 121 | `anchor_window` | 1.000 / 0.900 / 0.947 | 0.600 / 0.595 / 0.598 | 0.600 / 0.667 / 0.632 | 0 |
| Li n=100 | v3 | off | 34 / 53 | `strict_token_f1` | 0.853 / 0.853 / 0.853 | 0.056 / 0.038 / 0.045 | 0.065 / 0.042 / 0.051 | 0 |
| Li n=100 | v3 | `knn_pattern-k3` | 34 / 53 | `strict_token_f1` | 0.892 / 0.971 / 0.930 | 0.256 / 0.189 / 0.217 | 0.286 / 0.192 / 0.230 | 0 |

阶段性观察：

- 当前更新后的 report 中 generation failure 全部为 0，说明这批实验至少没有再触发空 `content` 或 JSON 解析失败这类工程性阻塞。
- ADE 上 35B-A3B + v3 + `knn_pattern-k3` 明显优于 v3 RAG off，也优于 v4 RAG off。这个结果好的一部分原因是 ADE 多数样本接近单因果对：100 个 causal 样本对应 124 个 gold triples，平均每个 causal 样本约 1.24 个 causal triple。
- 当前模型对多因果提取仍然偏弱，可以从 `Gold causal / Gold triples` 的差距看出来。CNC 是 51 / 74，Li 是 34 / 53，说明不少 causal 样本含多个因果对；这两组的 strict extraction F1 明显低于 ADE。
- CauseNet 是 100 / 121，形式上也以接近单因果为主，但 extraction 分数仍不高。这里更主要的问题不是多因果，而是 CauseNet 来自自动抽取，标注和 provenance 噪声较大，gold span/anchor 本身的可靠性弱于 ADE/CNC/Li。
- CauseNet 上 RAG 有小幅提升，但 CauseNet test 基本是 causal 样本，detection 指标不能和 CNC/Li 这类含负例的数据集直接横比。
- CNC 上 `knn_pattern-k3` 在这次 35B-A3B 实验里降低了 detection recall 和 all_samples F1，说明 RAG 不是稳定增益，需要后续做更系统的 ablation。
- Li 上 RAG 提升明显，但 extraction F1 仍然很低，说明 Li 的完整 span、多因果和严格匹配仍是当前最难的部分。

## 5. 遇到的问题与解决/取舍

### 5.1 Proposal 模型计划与本地硬件现实不完全一致

Proposal 最初计划比较 GoLLIE-13B 和两个强 14B general-purpose 模型。实际推进时，我们优先选择了能在 LM Studio + 4090 上稳定运行的 Qwen 系列 GGUF 模型。

当前取舍：

- 先把 pipeline、数据和 evaluation 做稳。
- 模型对比暂时以本地可跑模型为主。
- GoLLIE-style guideline 或 GoLLIE 模型本身是否进入最终实验，需要后续单独评估可运行性和输出稳定性。

### 5.2 JSON schema 与 GoLLIE Python object 输出的取舍

Proposal 中 GoLLIE 范式偏向 Python class/object 输出。当前项目采用 JSON 输出。

原因：

- JSON 更容易和 LM Studio structured output、notebook、report 和 evaluator 集成。
- 当前任务核心是因果三元组抽取，JSON 足够表达 `has_causal` 和 `triples`。
- Python object 输出可能增加 parser 和安全处理成本，现阶段收益不明确。

当前决定：

- 保留 JSON 作为当前 pipeline 的正式输出。
- 是否增加 GoLLIE-style 输出作为对照实验，留到模型对比阶段再决定。

### 5.3 Qwen3.5 thinking 通道问题

问题现象：

```text
message.content = ""
message.reasoning_content = 很长，甚至包含 JSON
```

这导致 parser 在 `content` 中找不到 JSON。

尝试过但不稳定的方法：

- `reasoning="off"`
- `extra_body={"chat_template_kwargs": {"enable_thinking": False}}`
- `/no_think`
- structured output / JSON schema
- 从 `reasoning_content` 兜底解析 JSON

最终决定：

- 不从 `reasoning_content` 解析最终答案。
- 使用 LM Studio no-thinking 虚拟模型来控制 Qwen3.5 thinking。
- 如果模型仍只返回 reasoning，则按 `llm_reasoning_only_empty_content` 记入 generation failure。

### 5.4 Evaluation 指标不能照搬原 PatternRAG 论文

原 PatternRAG 作者对 SemEval/ADE 单因果数据使用句级 accuracy；对 Li et al. 多因果数据使用 triplet-level Precision/Recall/F1。

我们的数据更复杂：

- CNC/Li 更像完整 span/event 抽取。
- ADE/CauseNet 更像 concept anchor 匹配。
- 同一条样本可能有多个 gold relation。

当前决定：

- Detection 用句级 classification 指标。
- Extraction 统一用 triple-level P/R/F1。
- 同时保留 `strict_token_f1` 和 `anchor_window` 两套 span 匹配。
- 根据数据集标注粒度选择主指标。
- 多因果匹配使用全局最优 one-to-one matching。

### 5.5 RAG 的效果还没有系统验证

目前 RAG 已经实现，但还没有完整跑完跨模型、跨数据集、开/关 RAG 的对比实验。

当前已有小样本结果不足以证明：

- RAG 一定提升。
- Pattern RAG 比 KNN 更好。
- KNN+Pattern 一定优于单独检索。

当前判断：

- RAG 能力已经具备。
- 是否作为最终论文贡献点，需要后续系统 ablation。

### 5.6 CauseNet 噪声与评估解释问题

CauseNet 是 proposal 中计划使用的大规模开放域资源，但它来自自动抽取，天然有噪声、冗余和语义模糊。

当前处理：

- 只保留有 sentence provenance 的 causal source。
- 将 concept anchor 映射回原句 surface span。
- 抽样构建 train/test/extra。

仍需注意：

- CauseNet test 全部是 causal 样本，因此 detection accuracy 解释方式和 CNC/ADE/Li 不同。
- CauseNet 的 gold 更适合 `anchor_window`，不适合严格完整 span 评价。

## 6. 新增的内容

相对 proposal 和早期 spec，目前新增了：

- CNC 数据集作为额外 benchmark。
- ADE train/test 分层切分与 RAG overlap 剔除。
- CauseNet sentence provenance 过滤、清洗、抽样和 train/test/extra 切分。
- LM Studio loaded model 自动识别。
- `prompt=v4`，更强调完整 span/event 边界。
- BGE dense KNN 检索与本地 embedding cache。
- `knn_pattern` 混合 RAG。
- `run_stream_eval()`，支持进度快照、report 保存和样本明细。
- `generation_failures` 分类统计。
- `strict_token_f1` 与 `anchor_window` 双 evaluation 口径。
- 全局最优 one-to-one 多因果匹配。
- Qwen3.5 no-thinking LM Studio 虚拟模型方案。

## 7. 已决定去掉或暂时不做的内容

当前明确去掉：

- `/no_think` prompt 后缀。
- notebook 默认传入 `LLM_REASONING` 或 `chat_template_kwargs.enable_thinking`。
- 从 `reasoning_content` 中兜底解析 JSON。
- `original_like` evaluation 指标。
- notebook 中重复的旧批量生成入口。

当前暂时不做：

- 直接输出 GoLLIE-style Python object。
- KG 构建阶段的 entity normalisation、Wikipedia linking、RDFS/OWL 输出。
- graph-level human/LLM-assisted evaluation。
- 使用 `reasoning_content` 作为模型答案来源。
- 把 structured output 作为 thinking 模型问题的根治方案。

## 8. 下一阶段需要完成的工作

### 8.1 稳定 triple-level extraction 实验

- 固定一到两个稳定本地模型，优先使用 no-thinking 或非 thinking 模型。
- 对 CNC、Li、ADE、CauseNet 运行更系统的小规模到中规模评估。
- 对比 RAG off、pattern、knn、knn_pattern。
- 记录每组实验的 generation failure、detection、extraction all_samples 和 detected_only。
- 做样本级 error analysis：区分漏检、误检、边界过短、边界过长、多因果漏抽、非因果幻觉。

### 8.2 决定最终模型与 prompt 方案

- 比较 Qwen3 14B、Qwen3.5 9B no-thinking，以及可能的其他 9B/14B 模型。
- 决定是否重新引入 GoLLIE-style guideline 或 Python object 输出作为实验组。
- 基于 error analysis 继续调整 prompt v4，必要时形成 v5。

### 8.3 完成 proposal 中的 KG 构建阶段

后续需要从：

```text
JSON causal triples
```

推进到：

```text
normalised causal nodes -> linked entities/concepts -> ontology-aligned RDF/RDFS/OWL graph
```

具体任务：

- 节点归一化：合并同义/大小写/轻微变体表达。
- 去重：合并重复 triples 和重复 provenance。
- 实体或概念链接：至少评估 Wikipedia linking 是否可行。
- 设计或复用 causal ontology schema，对齐 Jaimini et al. 的 causal ODP。
- 输出 RDF/RDFS/OWL 或等价可查询图格式。

### 8.4 Graph-level evaluation

proposal 中计划 graph-level evaluation，目前还未开始。

后续需要设计：

- 多跳 causal chain 抽样方法。
- human evaluation 或 LLM-assisted judge 的评价 rubrics。
- 图结构一致性、事实忠实度、节点冗余、边可信度等指标。
- triple-level 指标与 graph-level 质量之间的关系分析。

### 8.5 论文写作与实验叙事

后续论文中需要清楚解释当前已经形成的几个关键取舍：

- 为什么当前采用 JSON triples，而不是 GoLLIE Python object。
- 为什么不同数据集使用不同主 extraction metric。
- 为什么不从 `reasoning_content` 解析答案。
- 为什么 Li/CNC 更适合 strict span 评价，ADE/CauseNet 更适合 anchor-style 评价。
- PatternRAG 原论文的 single/multi evaluation 口径与我们当前统一 triple-level evaluation 的差异。

## 9. 当前阶段一句话总结

当前项目已经完成 proposal 中“LLM-based causal triple generation and triple-level evaluation”的工程闭环，并发现和解决了本地模型 thinking、数据集标注粒度、RAG 实现、JSON 解析、多因果匹配等关键问题。下一阶段的重点应从“pipeline 是否能跑通”转向“系统实验是否稳定、RAG 是否有效、以及如何把高质量 triples 组织成 ontology-aligned causal knowledge graph”。
