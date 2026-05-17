# LESSONS

## SPEC_01 数据清洗实现

- 实际数据文件直接位于 `Data` 目录，未采用规范示例中的 `data/raw` 与 `data/modified` 分层；按项目作者要求，脚本位于 `Data/script`，新数据直接写回 `Data`。
- `relation_count_distribution` 使用实际关系数量动态生成 key；这是因为 CNC 原始数据存在 4 和 5 个 relation 的样本，规范示例只展示到 3。
- CNC 软错误统计：`{"num_rs_mismatch": 0, "substring_check_failed_relations": 0, "substring_check_failed_samples": 0}`。
- Li 软错误统计：`{"missing_entity_mapping": 0, "substring_check_failed_relations": 0, "substring_check_failed_samples": 0}`。
- 解析过程只剥离标签与首尾空白，保留原始文本内部空格和标点空格。
