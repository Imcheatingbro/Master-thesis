# LESSONS

本文件只记录已经在当前代码、数据或 notebook 中落地的经验、取舍和风险；过期结论不要保留。

## 全局项目约定

- 所有 Python 运行、测试和 notebook kernel 都应使用 conda 环境 `Master_thesis`；notebook 初始化 cell 会检查 `sys.executable`，避免误用 base 或其他环境。
- 源码模块保持无交互输出：库代码使用 `logging`，展示型输出放在 notebook 或脚本入口中。
- 文件路径在 Windows 上大小写不敏感，但项目里真实数据目录是 `Data`；`src/data_io.py` 的默认数据目录已统一为 `Data`，避免迁移到大小写敏感文件系统后找不到文件。
- 当前工作流依赖本地 LM Studio OpenAI-compatible API；单元测试用 fake client 避免 pytest 依赖真实服务在线。
- 跨电脑复现环境使用根目录 `environment.yml`，避免使用 `conda list --export` 生成的 Windows 构建号锁文件；macOS 上应先安装 Miniforge/Miniconda，再运行 `conda env create -f environment.yml`，随后用 `python -m ipykernel install --user --name Master_thesis --display-name Master_thesis` 注册 notebook kernel。

## SPEC_01 数据清洗实现

- ADE benchmark 只作为 Hugging Face 原始快照下载到 `Data/Ade_corpus_v2_classification` 和 `Data/Ade_corpus_v2_drug_ade_relation`；脚本位于 `Data/script/download_ade_hf_datasets.py`，使用 `datasets.load_dataset(...).save_to_disk(...)`，不做清洗或字段重构。
- `Data/script/clean_ade_data.py` 将 ADE classification 与 drug-ADE relation 合并成 `Dataset_3_ADE_modified.jsonl`：classification 负责句子级 `has_causal`，relation 的 `drug` 作为 cause、`effect` 作为 effect，同一句子多条关系合并到一个样本。
- ADE 输出前会把 `RAG Database/bge-small-en-v1.5_examples.jsonl` 中出现过的句子剔除；比较时会去掉 `<cause>/<effect>` 标签、外层引号并合并空白，避免 RAG few-shot 库与 evaluation 数据串样。
- 当前 ADE 清洗统计：classification `23516` 行、规范化后唯一句子 `20895` 条、BGE overlap 剔除 `1286` 条，切分前 source pool 为 `19609` 条样本、`4555` 条 relation，软错误统计均为 `0`。
- ADE 清洗后会按 `has_causal` 分层随机切分，固定 `split_seed=20260524`，每个类别内分别打乱后按 7:3 切分；train 写入 `Data/finetuning/Dataset_3_ADE_train.jsonl`，test 覆盖保留为 `Data/Dataset_3_ADE_modified.jsonl`。
- 当前 ADE split 结果：train `13727` 条（causal `2090`、non-causal `11637`、relations `3238`），test `5882` 条（causal `895`、non-causal `4987`、relations `1317`）；train/test 与 BGE examples 的规范化句子 overlap 均为 `0`。
- CauseNet raw 使用 `Data/script/filter_causenet_raw.py` 流式过滤并原地替换 `Data/Dataset_4_causenet_raw.jsonl`；保留标准不是固定 source type 名称，而是 source 的 `payload.sentence` 非空，以免后续遇到新的 sentence source type 被误删。
- CauseNet 中纯 `wikipedia_list` / `wikipedia_infobox` 等无句子 provenance 的 row 会被删除；若同一 row 混有 sentence 和非 sentence source，则保留该 row 及其 sentence source，并剔除无句子的 source，保证后续 text-to-triples demo 只面对有原句的证据。
- 当前 CauseNet raw 过滤结果：原始 `197806` 行，保留 `180885` 行，删除 `16921` 行；保留 source `1941181` 个（`clueweb12_sentence` `1904792`、`wikipedia_sentence` `36389`），删除无句子 source `20307` 个（`wikipedia_list` `12391`、`wikipedia_infobox` `7916`）。复核结果为 invalid JSON `0`，无句子 source `0`。
- `Data/script/clean_causenet_data.py` 将 CauseNet raw 转为项目统一 `id/text/has_causal/relations` 格式：每个 sentence source 生成候选样本，`causal_relation` 中的 concept 下划线转为空格后在原句中大小写不敏感匹配，最终写出原句里的表面 span；同一句子的多条因果关系会合并到一个样本。
- CauseNet 句子合并只合并空白差异，不做大小写折叠；这是因为同一句大小写变体合并后，relation span 可能来自另一个大小写版本，无法通过项目现有的严格子串校验。
- CauseNet 二阶段清洗统计：输入 `180885` 行、`1941181` 个 sentence source，合并后 `786249` 个全因果句子样本、`918495` 条 relation；`substring_check_failed_relations` 为 `16630`，主要来自 concept 无法作为表面字符串在句中匹配，`duplicate_relations` 为 `1006056`，主要来自同一句同一因果关系被多个 provenance source 重复支持。
- CauseNet 固定随机种子 `split_seed=20260524` 后抽样切分：train 写入 `Data/finetuning/Dataset_4_causenet_train.jsonl`，共 `10000` 条、`11653` 条 relation；test 写入 `Data/Dataset_4_causenet_modified.jsonl`，共 `5000` 条、`5908` 条 relation；剩余 `771249` 条、`900934` 条 relation 写入 `Data/Dataset_4_causenet_extra.jsonl`。三份文件之间句子 overlap 为 `0`。
- CauseNet 真实句子里存在 Unicode 行分隔符等 `str.splitlines()` 会识别的字符；`Data/script/validate_outputs.py` 必须按文件对象逐行读取 JSONL，而不是对整文件 `read_text().splitlines()`，否则会把合法 JSON 字符串内部字符误当作记录边界。
- `Data/Dataset_4_causenet_extra.jsonl` 属于大型剩余样本池，可移动到 `Data/raw/` 并不纳入 Git；`validate_outputs.py` 对 `causenet_extra` 采用“文件存在才验证”的可选逻辑，确保新电脑 clone 后只凭已提交数据也能完成验收。
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
- Extraction 保留两套视角：`all_samples` 在全部样本上评估 triple 抽取，是当前 prompt 调优时最主要看的指标；`detected_only` 只在 gold=True 且 pred=True 的样本上观察 span 质量，用来排除 detection 错误后分析边界抽取，当前定位为诊断视图而不是主结果。
- Extraction 也保留两套匹配指标：`strict_token_f1` 会小写、去标点、去冠词、合并空格，再对 cause/effect 分别计算 token F1，并用二者最小值作为 triple pair 分数；默认阈值为 `0.8`。`anchor_window` 会检查较短的 gold concept anchor 是否能在较长的 prediction span 中通过滑动窗口 fuzzy matching 命中；默认阈值为 `0.9`。
- 不同数据集的主 extraction 指标按标注粒度选择：CNC/Li 的 gold 更接近完整 event/span，因此主指标为 `strict_token_f1`；ADE/CauseNet 的 gold 更接近 drug/disease/concept anchor，因此主指标为 `anchor_window`。报告会同时输出两套指标，避免隐藏不同口径带来的差异。
- triple 匹配使用 greedy one-to-one matching：先计算所有 pred/gold triple pair 分数，再从高到低匹配；一个预测和一个 gold 都最多只能被命中一次，最后累计 TP/FP/FN。
- 曾删除过近似原作者 evaluation 的 `original_like` 指标，因为它不适合 CNC/Li 这类完整 span 标注；加入 ADE/CauseNet 后重新发现其“gold 较短、prediction 合理更长”的场景，因此以更明确的 `anchor_window` 名称回归，并只作为 concept-anchor 数据集的主指标。
- `build_sample_judgement()` 输出单条样本的 text、gold/pred has_causal、gold/pred triples，以及 `strict_token_f1` 和 `anchor_window` 两套 TP/FP/FN，便于定位分数偏低来自漏抽、误抽、span 边界还是数据集标注粒度差异。
- SPEC_05 notebook 的 Cell P 不再定义运行函数，只负责导入 `load_dataset`、`EvalRunConfig`、`run_stream_eval` 并构造 `eval_config`；RAG retriever 的复用或即时创建放在 `eval_pipeline.py`，避免 notebook cell 之间隐藏函数依赖。
- notebook eval helper 使用 `tqdm.auto` 展示进度，并按 `EVAL_PROGRESS_EVERY` 输出累计指标快照；完整数据集评估由 `RUN_FULL_EVAL=False` 默认关闭，避免误触发长时间 LM Studio 推理。
- `SAVE_EVAL_REPORT=True` 时，Cell Q/Cell R 会把最终统计指标和本次评估的全部样本明细写入 `results/eval_report`；文件名包含模型、数据集、样本数量、prompt 名、RAG 配置和生成时间，便于对比不同 prompt 实验。
- notebook 顶部集中控制 LM Studio 连接与生成参数：`LLM_BASE_URL`、`LLM_API_KEY`、`MODEL_NAME`、`TEMPERATURE`、`MAX_TOKENS`、`CONTEXT_LENGTH`、`LLM_TIMEOUT` 和 `LLM_RETRY_TIMES`。这些变量填 `None` 时会回退读取 `configs/llm.yaml`；填入具体值时由 Cell A 覆盖 config 并创建新的 `LLMClient`。`MODEL_NAME="auto"` 时，Cell A 会调用 LM Studio `/api/v0/models` 并只读取 `state=loaded` 且 `type` 为 `llm` 或 `vlm` 的聊天模型；仅当返回刚好一个模型 ID 时自动替换 `client.model`，若返回 0 个或多个模型，会要求手动指定，避免 report 文件名和真实模型不一致。修改模型或连接参数后必须重跑 Cell A，修改 prompt/dataset/RAG 后必须至少重跑顶部配置 cell；Cell Q/Cell R 会在运行前重建 `EvalRunConfig`，避免报告文件名继续沿用旧的 `prompt_name` 或 RAG 配置。
- LM Studio 0.4.0 之后可能在 Server Settings 中开启 API Token 鉴权；开启后 `LLM_API_KEY="lm-studio"` 这种占位值会返回 401，需要在 LM Studio Developer 页面创建真实 token，并把 notebook 顶部 `LLM_API_KEY` 或 `configs/llm.yaml` 中的 `api_key` 改成该 token。`LLMClient.list_loaded_models()` 会把该 key 作为 `Authorization: Bearer ...` 发送给 `/api/v0/models`。
- 为减少 notebook cell 顺序依赖，SPEC_05 的 `make_eval_config()` 与 `tqdm` 导入已前移到 Cell A；Cell P 只展示当前 eval/report metadata，因此重启 kernel 后按“顶部配置 cell -> Cell A -> Cell Q”运行即可，不必先运行 Cell P。
- `LLMClient` 支持从 `configs/llm.yaml` 或 notebook 覆盖传入额外 OpenAI-compatible 请求体参数；当前默认不再传 `chat_template_kwargs.enable_thinking`，只固定传入 `context_length`。若后续模型没有通过 `model.yaml` 暴露 `Enable Thinking`，仍可临时用 `extra_body` 做兼容测试。
- `qwen3.5-9b.gguf` 在复杂样本上可能只返回 `reasoning_content` 且 `content=""`；这不是 JSON parser 格式兼容问题，而是模型没有进入最终答案阶段。`LLMClient.chat()` 会把这类返回分类为“模型只返回 reasoning_content，content 为空”，避免在 generator 层误报为“未找到 JSON 对象”。
- `reasoning="off"` 是 LM Studio `/api/v1/chat` 文档中的 reasoning 控制参数；Qwen 官方 OpenAI-compatible API 使用 `extra_body={"enable_thinking": False}`；llama.cpp/GGUF chat template 使用 `extra_body={"chat_template_kwargs": {"enable_thinking": False}}`。本项目当前走 LM Studio OpenAI-compatible chat completions + GGUF，因此优先测试 `chat_template_kwargs.enable_thinking=False`。
- `/no_think` 在当前 LM Studio + `qwen3.5-9b.gguf` 批量 eval 中已验证不可靠，已从 `LLMClient` 和 notebook 配置中移除；若仍出现 `reasoning_content`，应在 report 的生成失败统计里观察比例，而不是继续依赖 prompt 后缀。
- `generate()` 兜底结果会记录 `error_type` 与 `error_message`；`run_stream_eval()` 会在返回结果和 Markdown report 中写入 `generation_failures`，用于区分 `llm_reasoning_only_empty_content`、`no_json_object`、`invalid_json_syntax`、`invalid_output_schema` 和未知生成错误。
- 2026-05-25 通过 LM Studio `/api/v0/models` 只读检查发现，当前加载的 `qwen3.5-9b.gguf` 返回 `capabilities=["tool_use"]`，没有 `reasoning` 能力标记；因此 `chat_template_kwargs.enable_thinking=False` 仍可能不生效，根因更可能是 LM Studio 没把该 GGUF/模板识别为可控 thinking 模型，而不是 Python 客户端未传参。
- reasoning-only 且 `content=""` 属于确定性模型输出失败，不是网络瞬断；`LLMClient.chat()` 和 `generate()` 不再对此类错误重复重试，避免每个失败样本浪费多轮完整 reasoning token。
- 2026-05-25 在 `D:\LMstudio_models\Manojb\Qwen3.5-9B-Q8_0-no-thinking\model.yaml` 创建虚拟模型，`base` 指向原始 `Manojb/Qwen3.5-9B-Q8_0.gguf/Qwen3.5-9B-Q8_0.gguf`，基础 GGUF 目录保持不动；LM Studio 重新索引后出现 `Enable Thinking` 按钮，说明 `customFields -> setJinjaVariable -> enable_thinking` 映射生效。
- `Qwen3.5-9B-Q8_0.gguf` 的内置 chat template 已包含 `enable_thinking` 分支：变量为 `false` 时模板会插入空 `<think>\n\n</think>` 并直接进入最终回答；变量未定义或为 true 时会打开 `<think>`，容易把 token 全耗在 `reasoning_content`。因此修复重点是让 LM Studio UI/模型元信息把 `enableThinking=false` 传给 `enable_thinking`，而不是继续依赖 `/no_think`。
- 虚拟模型 `Manojb/Qwen3.5-9B-Q8_0-no-thinking` 的小规模 eval 已生成 report，`generation_failures.total=0`，未再出现 `llm_reasoning_only_empty_content`；后续运行应优先加载该虚拟模型，并新开会话确认 `Enable Thinking=Off`，避免旧会话状态覆盖模型默认值。
- 虚拟模型默认关闭 thinking 后，notebook 层的 `LLM_REASONING=None` 与 `LLM_EXTRA_BODY={"chat_template_kwargs": {"enable_thinking": False}}` 都属于多余默认参数，已清理为不传；`LLMClient.extra_body` 通用能力保留，便于将来测试没有正确暴露 `enableThinking` 的模型。
- 不再从 `reasoning_content` 里兜底解析 JSON；structured output 与 thinking 模型叠加时虽然可能把 JSON 放入 reasoning 通道，但这种行为依赖 LM Studio/模型模板边界状态，且容易把 `Thinking Process` 中复述的示例 JSON 误判为最终答案。当前规则恢复为只解析 `content`，`content=""` 继续按 `llm_reasoning_only_empty_content` 记录失败。
