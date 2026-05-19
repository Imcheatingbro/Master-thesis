# LESSONS

## SPEC_05 Evaluator 实现

- Evaluator 不直接打印，提供 `format_report()` 返回字符串；notebook 负责 `print`，避免违反模块内不使用 `print` 的项目约定。
- Extraction 同时输出两套指标：`all_samples` 忽略 `has_causal` 字段，在全部样本上匹配 triples；`detected_only` 只在 gold=True 且 pred=True 的样本上评估 span 质量，用于剥离 detection 错误后观察抽取边界。
- 增加 `original_like` 抽取指标，用原作者风格的字符窗口 fuzzy ratio 同时判断 cause/effect；该口径比 token F1 更严格，尤其是预测 span 短于 gold span 时会直接无法命中。
- notebook 的最终 eval cell 追加前 10 条样本明细，输出 gold/pred triples 以及 `token_f1`、`original_like` 的 TP/FP/FN，方便定位分数偏低来自 span 边界、漏抽还是误抽。
- SPEC_05 的 eval helper 不能隐式依赖前面 SPEC_03/04 cell 导入过 `load_dataset` 或 `generate`；Cell P 需要自带第五部分运行所需 imports，否则从第五部分开始跑会出现 `NameError`。
- 当 `USE_RAG=True` 时，SPEC_05 不能假设 Cell H 已创建 `retriever`；eval helper 需要在本 cell 内复用已有 retriever 或按 `RAG_MODE` 和 BGE cache 路径即时创建，否则从第五部分直接运行会报 `NameError`。
- notebook eval helper 使用 `tqdm.auto` 显示进度条，并按 `EVAL_PROGRESS_EVERY` 周期输出当前累计 report；完整数据集评估默认由 `RUN_FULL_EVAL=False` 关闭，避免误触发长时间 LM Studio 推理。

## SPEC_01 数据清洗实现

- 实际数据文件直接位于 `Data` 目录，未采用规范示例中的 `data/raw` 与 `data/modified` 分层；按项目作者要求，脚本位于 `Data/script`，新数据直接写回 `Data`。
- `relation_count_distribution` 使用实际关系数量动态生成 key；这是因为 CNC 原始数据存在 4 和 5 个 relation 的样本，规范示例只展示到 3。
- CNC 软错误统计：`{"num_rs_mismatch": 0, "substring_check_failed_relations": 0, "substring_check_failed_samples": 0}`。
- Li 软错误统计：`{"missing_entity_mapping": 0, "substring_check_failed_relations": 0, "substring_check_failed_samples": 0}`。
- 解析过程只剥离标签与首尾空白，保留原始文本内部空格和标点空格。

## SPEC_02 LLM Client 实现

- `LLMClient` 只封装 LM Studio 兼容 OpenAI API 的最小能力：`ping()` 和 `chat()`，不提前加入 prompt、解析、缓存或并发逻辑。
- 配置文件使用 `configs/llm.yaml`，notebook 可通过构造函数覆盖 `temperature` 与 `max_tokens` 等参数。
- 单元测试使用假 OpenAI 客户端验证连接状态和重试行为，避免 pytest 依赖本地 LM Studio 必须在线。
- `notebooks/main_pipeline.ipynb` 只追加 SPEC_02 验收 cells；真实模型连通性和示例输出留给项目作者在 LM Studio 启动后验收。

## SPEC_03 Prompt 与 Pattern RAG 实现

- Pattern DB 实际路径为 `RAG Database/comb_SCITEsemADE_CausalityPattern.csv`，不是早期规范中的 `DAGdatabase`。
- 论文与参考代码中的 Pattern RAG 主要依赖 causal connective 匹配；本实现使用 `rapidfuzz` 复刻相近逻辑，并用 token overlap 作为未命中时的稳定补齐策略。
- 未使用 CSV 中的 `embedings` 字段，因为 Demo1 只实现 Pattern RAG，不实现 kNN+Pattern RAG。
- 为保证 demo/eval 可复现，超过 `top_k` 的候选按分数与 CSV 原始顺序稳定排序，不使用参考 notebook 中的随机抽样。
- 真实 LM Studio 测试中，Qwen 仍会输出 `<think>` 推理文本；SPEC_04 的解析器需要处理 `<think>`、前缀解释文本和截断 JSON。

## SPEC_04 Generator 实现

- `parse_output` 支持纯 JSON、markdown 代码块、前缀解释文本和 `<think>...</think>` 后再解析首个 JSON 对象。
- `generate` 每次调用重新构造 prompt 并调用 LLM；解析或最小校验失败时按 `max_retry` 重试，耗尽后返回 `{"id": sample_id, "has_causal": false, "triples": []}` 兜底。
- Demo1 的最小校验只检查 `has_causal: bool` 与 `triples: list`，不在本阶段做 span 子串评估或 relation-level 指标，这些留给 SPEC_05。
- `load_dataset` 按实际路径读取 `data/Dataset_1_CNC_modified.jsonl` 与 `data/Dataset_2_Li_modified.jsonl`；sample 模式暂取前 N 条，保证 notebook 行为可复现。
- 真实 LM Studio smoke test 使用 `Heavy rain caused widespread flooding in the region.`，成功解析出 1 条 causal triple，未触发兜底。

## Notebook 内核与导入路径修正

- Jupyter 从 notebooks 目录或普通 Python 内核启动时，项目根目录不会自动进入 sys.path，因此 from src... 会报 ModuleNotFoundError；在 notebook 初始化 cell 中加入项目根目录兜底。
- Master_thesis 环境需要安装并注册 ipykernel 后，Jupyter 界面才会出现对应内核；notebook 元数据同步指向 Master_thesis，减少误选普通内核导致的依赖不一致。
- notebook 验收 cell 访问项目文件时不能直接使用相对路径；应复用初始化 cell 的 PROJECT_ROOT，否则从 notebooks 目录启动时会误查 notebooks 子目录。

## SPEC_03 KNN+Pattern RAG 扩展

- `Xenova/text-embedding-ada-002` 只是 OpenAI ada-002 tokenizer 的 Hugging Face 兼容版，不能替代真实 embedding encoder；本项目改用 `BAAI/bge-small-en-v1.5` 生成本地 sentence embeddings。
- 为后续大量 evaluation，BGE cache 使用 `RAG Database/bge-small-en-v1.5_examples.jsonl` 与 `RAG Database/bge-small-en-v1.5_embeddings.npy`，避免在 CSV 中反复解析长 float 字符串。
- 单独 Pattern RAG 仍保留；当 BGE metadata cache 存在时，PatternRetriever 默认使用同一份 jsonl metadata，实现 Pattern、KNN、KNN+Pattern 三种模式共享 example metadata。
- KNN+Pattern RAG 按参考代码习惯先拼接 Pattern examples，再拼接 KNN examples，并按 `(sentence, cause, effect)` 去重；因此最终 examples 数量最多为 `2 * RAG_TOP_K`。
- 原始 Pattern DB CSV 只作为重建 BGE cache 的输入，不再作为 notebook demo/eval 运行时验收项；运行时统一验证并读取 BGE jsonl/npy cache。
- 为降低 demo 阶段代码阅读成本，RAG 检索相关实现合并到 `src/retriever.py`，脚本与 notebook 统一从该模块导入。

- prompt 模板不再在 system message 末尾重复 {input_text}；输入文本只放在 user message，减少 prompt 冗余。
- LM Studio 已手动提升 context length 至 8192；configs/llm.yaml 增加 context_length: 8192，客户端通过 OpenAI 兼容接口的 extra_body 传递该值。

- notebook sample demo 的 Gold 输出改为完整 has_causal 与 	riples JSON，方便人工对照模型输出。
- 删除 notebook 中的 Cell N 批量生成预备逻辑；正式 evaluation 由后续 SPEC_05 单独实现，避免 demo notebook 出现半成品评估入口。
