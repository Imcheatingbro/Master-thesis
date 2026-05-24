# LESSONS

本文件只记录已经在当前代码、数据或 notebook 中落地的经验、取舍和风险；过期结论不要保留。

## 全局项目约定

- 所有 Python 运行、测试和 notebook kernel 都应使用 conda 环境 `Master_thesis`；notebook 初始化 cell 会检查 `sys.executable`，避免误用 base 或其他环境。
- 源码模块保持无交互输出：库代码使用 `logging`，展示型输出放在 notebook 或脚本入口中。
- 文件路径在 Windows 上大小写不敏感，但项目里真实数据目录是 `Data`；`src/data_io.py` 的默认数据目录已统一为 `Data`，避免迁移到大小写敏感文件系统后找不到文件。
- 当前工作流依赖本地 LM Studio OpenAI-compatible API；单元测试用 fake client 避免 pytest 依赖真实服务在线。

## SPEC_01 数据清洗实现

- ADE benchmark 只作为 Hugging Face 原始快照下载到 `Data/Ade_corpus_v2_classification` 和 `Data/Ade_corpus_v2_drug_ade_relation`；脚本位于 `Data/script/download_ade_hf_datasets.py`，使用 `datasets.load_dataset(...).save_to_disk(...)`，不做清洗或字段重构。
- `Data/script/clean_ade_data.py` 将 ADE classification 与 drug-ADE relation 合并成 `Dataset_3_ADE_modified.jsonl`：classification 负责句子级 `has_causal`，relation 的 `drug` 作为 cause、`effect` 作为 effect，同一句子多条关系合并到一个样本。
- ADE 输出前会把 `RAG Database/bge-small-en-v1.5_examples.jsonl` 中出现过的句子剔除；比较时会去掉 `<cause>/<effect>` 标签、外层引号并合并空白，避免 RAG few-shot 库与 evaluation 数据串样。
- 当前 ADE 清洗统计：classification `23516` 行、规范化后唯一句子 `20895` 条、BGE overlap 剔除 `1286` 条，切分前 source pool 为 `19609` 条样本、`4555` 条 relation，软错误统计均为 `0`。
- ADE 清洗后会按 `has_causal` 分层随机切分，固定 `split_seed=20260524`，每个类别内分别打乱后按 7:3 切分；train 写入 `Data/finetuning/Dataset_3_ADE_train.jsonl`，test 覆盖保留为 `Data/Dataset_3_ADE_modified.jsonl`。
- 当前 ADE split 结果：train `13727` 条（causal `2090`、non-causal `11637`、relations `3238`），test `5882` 条（causal `895`、non-causal `4987`、relations `1317`）；train/test 与 BGE examples 的规范化句子 overlap 均为 `0`。
- 实际数据文件直接位于 `Data` 目录，未采用规范示例中的 `data/raw` 与 `data/modified` 分层；清洗脚本位于 `Data/script`，清洗产物也写回 `Data`。
- CNC 清洗按 `causal_text_w_pairs` 解析 `<ARG0>` 和 `<ARG1>`，先剥离 `<SIGn>` 标签，再做 cause/effect 子串校验；Li 清洗先从句内 `<eN>` 标签建立实体映射，再按 label 中的 `(eX,eY)` 提取多对因果关系。
- 清洗过程只剥离标注标签与首尾空白，保留原始文本内部空格和标点空格；这是下游 span 子串校验和评估可复现的基础。
- `relation_count_distribution` 使用实际关系数量动态生成 key；CNC 存在 4、5 个 relation 的样本，Li 存在最多 12 个 relation 的样本，不能把分布写死到 0-3。
- 当前清洗统计为：CNC `3075` 条样本、`1624` 条因果样本、`2257` 条 relation；Li `786` 条样本、`191` 条因果样本、`296` 条 relation。
- 当前清洗软错误统计均为 0：CNC `num_rs_mismatch`、`substring_check_failed_relations`、`substring_check_failed_samples`；Li `missing_entity_mapping`、`substring_check_failed_relations`、`substring_check_failed_samples`。
- `Data/script/validate_outputs.py` 会验证 JSONL LF 换行、字段顺序、连续 id、非因果样本空 relations、relation 子串约束和 stats 一致性；这是 SPEC_01 的关键验收入口。
- 需要注意：`Data/script/clean_data.py` 中的 `write_lessons()` 会重写整个 `reports/LESSONS.md`，如果重新运行清洗脚本，可能覆盖后续 SPEC 的经验记录；后续最好改为追加或移除该副作用。

## SPEC_02 LLM Client 实现

- `LLMClient` 只封装 LM Studio 兼容 OpenAI API 的最小能力：`ping()` 和 `chat()`；prompt 构造、输出解析、缓存和并发都不放在客户端层。
- 配置集中在 `configs/llm.yaml`，构造 `LLMClient` 时可覆盖 `model`、`temperature`、`max_tokens` 等参数，便于 notebook 在不同实验配置间切换。
- `chat()` 会把 `context_length` 通过 OpenAI 兼容接口的 `extra_body` 传给 LM Studio；当前配置为 `8192`，与本地模型上下文设置保持一致。
- 重试逻辑只处理调用异常：按 `retry_times` 指数退避重试，最终失败时抛出 `RuntimeError`；模型输出格式问题交给 SPEC_04 处理。
- 单元测试使用 fake OpenAI client 验证配置读取、参数覆盖、`ping()` 成功/失败和 transient failure 重试，避免测试依赖本地 LM Studio。

## SPEC_03 Prompt 与 RAG 实现

- Prompt 模板从 `prompts/{name}.txt` 读取，当前默认 `v1`；notebook 当前配置使用未跟踪的 `v2`，若要复现实验，需要确认 `prompts/v2.txt` 被纳入版本控制或显式切回 `v1`。
- `build_messages()` 只把输入文本放在 user message；system message 不再重复 `{input_text}`，减少 prompt 冗余并降低长输入时的上下文占用。
- `v1` prompt 同时覆盖显式因果、purpose/motivation 弱因果、以及 `when/after/following/once` 条件触发类因果；要求输出严格 JSON，且不得输出 `<think>`。
- `v2` prompt 更偏 CNC-style span 边界：强调完整 event/state span、保留修饰语、避免把事件缩短成 noun phrase，并对合并/拆分 cause-effect 给出更具体约束。
- Pattern DB 实际路径为 `RAG Database/comb_SCITEsemADE_CausalityPattern.csv`，不是早期规范中的 `DAGdatabase`。
- 当前 RAG 相关实现统一在 `src/retriever.py`，没有单独的 `src/rag_retriever.py`；notebook、脚本和测试都从该模块导入。
- Pattern RAG 主要依赖 causal connective 匹配：先匹配 `causality_phrase`，再用 token overlap 作为兜底补齐；排序按总分、phrase 分、overlap 分和原始顺序稳定排序，保证可复现。
- 原始 CSV 中的 `embedings` 字段不再作为运行时检索输入；KNN 检索使用本地 BGE cache：`RAG Database/bge-small-en-v1.5_examples.jsonl` 与 `RAG Database/bge-small-en-v1.5_embeddings.npy`。
- BGE cache 当前为 `2365` 条 example、embedding 维度 `384`，模型名为 `BAAI/bge-small-en-v1.5`；脚本 `scripts/build_embedding_cache.py` 可从 Pattern DB 重建 jsonl/npy cache。
- `create_retriever()` 当前支持 `pattern`、`knn`、`knn_pattern` 三种模式；`knn_pattern` 先拼接 Pattern examples，再拼接 KNN examples，并按 `(sentence, cause, effect)` 去重。
- 混合模式下每个 retriever 各取 `RAG_TOP_K` 条，因此最终 examples 数量最多为 `2 * RAG_TOP_K`，prompt 长度会随 K 增长明显变长。

## SPEC_04 Generator 与数据读取实现

- `generate()` 串联 `build_messages()`、`client.chat()`、`parse_output()` 和最小字段校验；解析或校验失败时重新调用 LLM，耗尽重试后返回 `{"id": sample_id, "has_causal": false, "triples": []}`。
- `parse_output()` 支持纯 JSON、markdown fenced code block、前缀解释文本和完整 `<think>...</think>` 包裹后的 JSON；如果模型输出未闭合 `<think>`，仍可能无法提取 JSON，需要通过关闭 thinking 或更强 prompt 约束规避。
- Demo1 的最小校验只检查 `has_causal: bool` 与 `triples: list`，不在生成阶段强制检查 span 是否为原文子串；span 质量留给 SPEC_05 evaluator 统一评估。
- `generate()` 会把 `rag_mode` 和 `prompt_name` 继续传给 prompt builder，因此同一套生成入口可以覆盖 Pattern、KNN、KNN+Pattern 和不同 prompt 版本。
- `src/data_io.py` 的 `load_dataset()` 支持 `cnc`、`li`、`ade` 和前 n 条样本读取；当前实现按前 N 条取样，不做随机抽样，便于 notebook demo/eval 可复现。
- 真实 LM Studio smoke test 曾用 `Heavy rain caused widespread flooding in the region.` 成功解析出 causal triple，未触发兜底；这只能说明链路可跑通，不代表评估质量。

## Notebook 集成与运行经验

- `notebooks/main_pipeline.ipynb` 负责把 SPEC_02-05 串起来：环境检查、LM Studio 连通性、prompt/RAG 渲染、generator demo、evaluator 小规模/完整评估。
- notebook 初始化 cell 会根据 `Path.cwd()` 推断 `PROJECT_ROOT`，解决从 `notebooks` 目录启动时 `from src...` 找不到项目根目录的问题。
- notebook 元数据指向 `Master_thesis` kernel；如果 Jupyter 中看不到该 kernel，需要先在该 conda 环境中安装并注册 ipykernel。
- notebook 中访问项目文件时应使用 `PROJECT_ROOT / ...`，不要依赖裸相对路径；否则从不同启动目录运行会误查 `notebooks` 子目录。
- SPEC_03/04 cell 会通过 `importlib.reload()` 重载 prompt_builder 和 retriever，方便修改 prompt 或检索实现后不用重启 kernel 就能看到新逻辑。
- SPEC_04 中原先的批量生成预备逻辑已不再作为正式入口；正式 evaluation 集中到 SPEC_05 的 `run_stream_eval()`，避免 demo 与评估入口重复。
- demo sample 输出 Gold 时展示完整 `has_causal` 与 `relations` JSON，便于人工对照模型输出，而不是只看 relation 数量。
- notebook 顶部配置可切换 `MODE`、`PROMPT_NAME`、`USE_RAG` 和 `EVAL_SAMPLE_N`；如果使用未跟踪的 prompt 版本（例如本地 `v2`），需要先确认该 prompt 文件已保存并在需要复现实验时纳入版本控制。

## SPEC_05 Evaluator 实现

- SPEC_05 的运行编排已从 notebook 抽到 `src/eval_pipeline.py`：该文件负责循环生成、进度快照、报告落盘和前 10 条样本展示；`src/evaluator.py` 继续只负责匹配算法与指标累计，Cell P 只构造 `EvalRunConfig`。
- `Evaluator` 流式累计指标，不直接打印；`format_report()` 返回字符串，notebook 负责展示，这样既适合长评估过程，也符合模块内不使用 `print` 的约定。
- Detection 是句子级二分类，按 `has_causal` 统计 TP/TN/FP/FN、accuracy、precision、recall、F1。
- 当前主评估流程分两层：第一层 detection 按 `has_causal` 做句子级二分类；第二层 extraction 不依赖 `has_causal`，直接比较模型输出的 `triples` 与 gold `relations`。
- Extraction 保留两套视角：`all_samples` 在全部样本上评估 triple 抽取，是当前 prompt 调优时最主要看的指标；`detected_only` 只在 gold=True 且 pred=True 的样本上观察 span 质量，用来排除 detection 错误后分析边界抽取。
- token-F1 匹配会小写、去标点、去冠词、合并空格，再对 cause/effect 分别计算 token F1，并用二者最小值作为 triple pair 分数；默认阈值为 `0.8`。
- triple 匹配使用 greedy one-to-one matching：先计算所有 pred/gold triple pair 分数，再从高到低匹配；一个预测和一个 gold 都最多只能被命中一次，最后累计 TP/FP/FN。
- 曾实现过 `original_like` 指标来近似原作者 evaluation：对每个 span 先小写，如果预测 span 短于 gold span 就直接得 0；否则在预测 span 中用 gold span 长度滑动窗口，逐窗口用字符级 fuzzy ratio 取最高分；cause 和 effect 都必须大于 90，triple 才算命中。
- 删除 `original_like` 的原因是它对 Demo1 的 prompt 调优过于严格：模型只要少输出一个主语、时间地点修饰、冠词或边界稍短，就可能整条 triple 变成 FN/FP；这种口径更适合复现原论文表格，不适合当前阶段判断 prompt 是否在语义上抽对了因果事件。
- `build_sample_judgement()` 输出单条样本的 text、gold/pred has_causal、gold/pred triples，以及 token-F1 的 TP/FP/FN，便于定位分数偏低来自漏抽、误抽还是 span 边界。
- SPEC_05 notebook 的 Cell P 不再定义运行函数，只负责导入 `load_dataset`、`EvalRunConfig`、`run_stream_eval` 并构造 `eval_config`；RAG retriever 的复用或即时创建放在 `eval_pipeline.py`，避免 notebook cell 之间隐藏函数依赖。
- notebook eval helper 使用 `tqdm.auto` 展示进度，并按 `EVAL_PROGRESS_EVERY` 输出累计指标快照；完整数据集评估由 `RUN_FULL_EVAL=False` 默认关闭，避免误触发长时间 LM Studio 推理。
- `SAVE_EVAL_REPORT=True` 时，Cell Q/Cell R 会把最终统计指标和本次评估的全部样本明细写入 `results/eval_report`；文件名包含模型、数据集、样本数量、prompt 名、RAG 配置和生成时间，便于对比不同 prompt 实验。
