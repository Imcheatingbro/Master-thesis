# Gemma 4 12B 多关系继续/结束偏置诊断

> **口径说明：** 本目录用于解释模型的提前结束偏置。文中的 continuation pipeline 属于探索性多阶段解码，已从主评估 API 撤回；它不符合“一条样本一次完整 `model.generate()`”的论文主实验约束，不能作为主结果。

## 结论

当前 adapter 存在明确的“过早结束 triples 数组”偏置。它在需要继续输出下一条关系时，通常仍更偏好结束；但 continue/stop margin 仍有较好的排序能力，因此应先验证边界感知解码，不必立刻重训。

这项诊断只回答“给定正确的前一条 Gold triple，模型是否知道后面还应继续”，不等同于端到端 relation F1，也没有使用 test 数据。

## 方法

- 模型：`outputs/finetuning/gemma4_12b_cnc_qlora_unsloth_v1`
- 数据：`Data/CNC_sft_gemma_v2` 的 train 与 validation
- 推理格式：训练时的 `gemma-4` chat template、`enable_thinking=False`、移除额外 BOS、batch=1
- 对每个 Gold triple 结束位置构造两条完整且合法的 assistant 答案：一条继续下一条 triple，一条立即关闭数组
- 对两条完整 token 序列取最长公共前缀，再比较首个真实分叉 token 的 logit
- margin 定义：`continue_logit - stop_logit`；大于等于阈值判为继续

不能只在上下文后分别拼接孤立的 `,` 和 `]`。Gemma tokenizer 有 look-ahead/合并标点行为，孤立字符的 tokenization 与完整 JSON 中的真实分叉不同。本次 1,494 个边界中，1,485 个边界的真实首分叉 token 对是 `"` 与 `"}}`，不是两个孤立标点 token。

## 结果

| Split | Continue 边界 | Stop 边界 | Continue 正确率（阈值 0） | Stop 正确率（阈值 0） | Margin AUC |
|---|---:|---:|---:|---:|---:|
| Train | 316 | 812 | 0.206 | 0.982 | 0.804 |
| Validation | 102 | 264 | 0.225 | 0.985 | 0.854 |

Validation 中：

- 表中的 pairwise 正确率按严格 argmax 统计（margin 必须大于 0；tie 不算正确）；下面的可部署阈值策略统一按 `margin >= threshold`，所以阈值 0 会把 8 个 validation ties 判为 continue。
- 默认阈值 0 只找回 31/102 个应继续边界，continue recall 为 0.304；却正确结束 260/264 个 stop 边界。
- 第一条 triple 后，84 个应继续边界中只有 28 个被默认阈值找回（0.333）。这直接支持“经常只输出第一条关系”的观察。
- continue margin 中位数为 -0.6875，stop margin 中位数为 -2.375。两类都偏负，但仍能相对区分，这说明问题是决策基线偏向结束，而不是完全没有学到多关系信号。

## Validation 内部校准检查

为了只验证 margin 是否可救，将 264 个 validation 正例按单关系/多关系分层、固定 seed=42 后，按 sample ID 分成 132 条 calibration 与 132 条 held-out。calibration 半集选择的观测 cutoff 为 -1.25；使用相邻 margin 的中点表示时等价为 -1.3125。

在 held-out 的 183 个边界上：

| 设置 | Continue P | Continue R | Continue F1 | Stop R | Balanced accuracy |
|---|---:|---:|---:|---:|---:|
| 默认阈值 0 | 0.864 | 0.373 | 0.521 | 0.977 | 0.675 |
| 校准阈值 -1.3125 | 0.694 | 0.667 | 0.680 | 0.886 | 0.777 |

该提升只证明“边界 margin 值得用于解码实验”。是否能提高最终 anchor F1，必须在同一 validation 上跑完整生成后确认。

## 探索性处理（已撤出主评估入口）

1. 曾实现过顶层因果判定、初始关系抽取、最终 triple 边界复核、必要时续抽取、JSON 校验与安全回退的内部 pipeline；它虽然只返回一个 JSON，却包含多次模型计算，因此已从主 API 删除。
2. 边界复核按当前完整上下文重新构造 tokenizer-safe 的 continue/stop 候选，不对固定逗号 token 做全局 bias。
3. continuation 阈值设为 `-1.3125`，最多续抽取 4 轮；新结果必须保留全部旧 triples、增加关系且保持合法 JSON，否则回退到上一版合法输出。
4. 这些结果只用于定位训练问题。主实验下一步应保持严格 single-pass，在训练侧修复多关系学习能力，并只用 validation 选择配置。

原始逐边界分数见 `train_boundary_scores.jsonl` 与 `validation_boundary_scores.jsonl`，总体统计见 `summary.json`。复现入口为 `scripts/diagnose_gemma_relation_continuation.py`。
