# LESSONS

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
