# SPEC_05 ｜ Evaluator（Demo1 评估模块）

> **适用范围**：Causal KG Demo 项目，Demo1 阶段的评估
> **依赖文档**：`AGENT.md`（全局规则）、`SPEC_01_data_cleaning_v0.2.md`（数据 schema）、`SPEC_02_03_04_demo1_pipeline.md`（生成模块）
> **前置条件**：SPEC_02 / SPEC_03 / SPEC_04 已全部完成并通过验收
> **执行方式**：完成后在主 notebook 中追加验收 cells，**停下来等待项目作者验收**

---

## 0. 阅读须知（给 Codex）

1. 本 SPEC 是独立模块，**不要修改 SPEC_02 / SPEC_03 / SPEC_04 产生的任何文件**（除 notebook 追加 cells 之外）。
2. 完成后：
   - 在 `notebooks/main_pipeline.ipynb` 中追加 SPEC_05 验收 cells
   - 在 `reports/LESSONS.md` 中追加本 SPEC 的踩坑记录
   - 推送 Git（commit message: `[evaluator] 完成 Demo1 评估模块`）
   - **停下来，明确告诉项目作者"SPEC_05 已完成，请验收"**
3. 全局规则遵守 `AGENT.md`。

---

## 1. 任务边界

**做**：
- 实现两层评估：Detection（句子级二分类）+ Extraction（triple 级模糊匹配）
- 提供**流式累加**接口：边生成边评估，每条样本生成完立即比对 ground truth，不需要存中间 prediction.jsonl 文件
- 在评估结束时输出可读的报告

**不做**：
- 不评估 properties 字段（demo1 阶段不输出 properties）
- 不评估 relation type（固定为 `"caused"`）
- 不做 embedding 相似度（用最简单的 token-level F1）
- 不评估 demo 模式（demo 模式没有 ground truth）

---

## 2. 评估方法

### 2.1 Layer 1 - Detection（句子级二分类）

**目标**：判断模型识别"句子是否含因果"的能力。

**方法**：
- 对每条样本，比较 `pred["has_causal"]` 和 `gold["has_causal"]`
- 直接相等判断，无需模糊匹配
- 累加 TP / TN / FP / FN：
  - TP：gold=True, pred=True
  - TN：gold=False, pred=False
  - FP：gold=False, pred=True
  - FN：gold=True, pred=False

**指标**：Accuracy、Precision、Recall、F1（按 `has_causal=True` 为正类计算）。

### 2.2 Layer 2 - Extraction（triple 级模糊匹配）

**目标**：当模型识别有因果时，评估其抽取的 cause/effect span 是否正确。

**计算范围**：
- **只在 `gold["has_causal"]=True` 且 `pred["has_causal"]=True` 的样本上计算**
- 其他样本（任一方 has_causal=False）不参与 Layer 2

**Span 预处理（评估前对每个 span 做的清洗）**：
1. 转小写（lowercase）
2. 去掉冠词：`a` / `an` / `the`（作为独立单词出现时）
3. 去掉所有标点（保留字母数字和空格）
4. 合并连续空格为单个空格
5. 首尾 strip

例：`"A super heavy rain ."` → `"super heavy rain"`

**Token-level F1 计算**：
```
pred_tokens = set(预处理后的 pred_span.split())
gold_tokens = set(预处理后的 gold_span.split())
overlap = pred_tokens & gold_tokens

如果 |pred_tokens| == 0 或 |gold_tokens| == 0:
    f1 = 0.0
else:
    precision = |overlap| / |pred_tokens|
    recall = |overlap| / |gold_tokens|
    f1 = 0.0 if (precision + recall == 0) else 2 * precision * recall / (precision + recall)
```

**Triple 配对（一句话内多 triple 的匹配）**：

每条样本有一组 gold relations 和一组 pred triples。配对规则：

1. 对每对 (pred_triple, gold_relation)，计算 triple-level 相似度：
   - `cause_f1 = token_f1(pred.cause.span, gold.cause)`
   - `effect_f1 = token_f1(pred.effect.span, gold.effect)`
   - `triple_score = min(cause_f1, effect_f1)`（cause 和 effect 都要对得上才算匹配）

2. **贪心匹配**：
   - 把所有 (pred, gold) 配对按 `triple_score` 降序排列
   - 从高到低遍历，若 pred 和 gold 都未被占用且 `triple_score >= 0.8`，则配对成功，标记两者已占用
   - 直到遍历完或所有 pred/gold 都被占用

3. 统计：
   - TP = 成功配对数
   - FP = 未被配对的 pred triple 数
   - FN = 未被配对的 gold relation 数

**指标**：Precision、Recall、F1（基于 Layer 2 的 TP / FP / FN）。

### 2.3 模糊匹配阈值

阈值固定为 **0.8**，不需要可配置。

---

## 3. 模块文件

新建 `src/evaluator.py`，至少包含：

```
preprocess_span(text: str) -> str
    span 预处理（lowercase + 去冠词 + 去标点 + 去多余空格）

token_f1(pred_span: str, gold_span: str) -> float
    计算两个 span 的 token-level F1（内部先调 preprocess_span）

match_triples(pred_triples: list, gold_relations: list, threshold: float = 0.8) -> tuple
    贪心配对，返回 (tp, fp, fn) 三个整数

class Evaluator:
    def __init__(self): ...
        初始化累加器（Detection 的 TP/TN/FP/FN，Extraction 的 TP/FP/FN）

    def update(self, prediction: dict, gold: dict) -> None:
        对单条样本累加统计

    def report(self) -> dict:
        返回完整指标报告（dict 结构见 §4）

    def reset(self) -> None:
        清空累加器

    def print_report(self) -> None:
        以人类可读格式打印报告（表格或多行文本）
```

---

## 4. Report 输出格式

`Evaluator.report()` 返回的 dict 结构：

```python
{
    "n_samples": 100,              # 总评估样本数
    "n_causal_gold": 60,           # gold 中含因果的样本数
    "n_causal_pred": 55,           # pred 中含因果的样本数
    "detection": {
        "tp": 50,
        "tn": 35,
        "fp": 5,
        "fn": 10,
        "accuracy": 0.85,
        "precision": 0.909,
        "recall": 0.833,
        "f1": 0.870,
    },
    "extraction": {
        "n_eval_samples": 45,      # gold=T 且 pred=T 的样本数
        "n_gold_triples": 78,      # 这些样本上的 gold relations 总数
        "n_pred_triples": 72,      # 这些样本上的 pred triples 总数
        "tp": 55,
        "fp": 17,
        "fn": 23,
        "precision": 0.764,
        "recall": 0.705,
        "f1": 0.733,
    },
    "fuzzy_threshold": 0.8,
}
```

`print_report()` 应输出类似：

```
================ Demo1 评估报告 ================
样本总数: 100
  Gold 含因果: 60 | Pred 含因果: 55
  模糊匹配阈值: 0.8

[Layer 1] Detection (句子级二分类)
  Accuracy : 0.850
  Precision: 0.909
  Recall   : 0.833
  F1       : 0.870
  (TP=50, TN=35, FP=5, FN=10)

[Layer 2] Extraction (triple 级，gold=T & pred=T 子集上)
  样本数: 45
  Gold triples: 78 | Pred triples: 72
  Precision: 0.764
  Recall   : 0.705
  F1       : 0.733
  (TP=55, FP=17, FN=23)
================================================
```

---

## 5. 与 Generator 的集成方式

**关键设计**：评估是**流式累加**的，不需要先把 predictions 全存下来再读。

Notebook 中 eval 模式的主循环结构：

```python
from src.evaluator import Evaluator
from src.generator import generate
from src.data_io import load_dataset

samples = load_dataset(DATASET)
evaluator = Evaluator()

for s in samples:
    pred = generate(
        text=s["text"],
        sample_id=s["id"],
        client=client,
        retriever=retriever if USE_RAG else None,
        use_rag=USE_RAG,
        top_k=RAG_TOP_K,
    )
    # gold 字段命名见 SPEC_01：has_causal + relations
    evaluator.update(prediction=pred, gold=s)

evaluator.print_report()
```

**关于 gold 的字段名映射**：
- gold（来自 modified jsonl）：`has_causal` (bool) + `relations` (list[{"cause": str, "effect": str}])
- pred（来自 generator）：`has_causal` (bool) + `triples` (list[{"cause": {"span": str}, "effect": {"span": str}}])
- evaluator 内部要正确处理这两套不同字段名

---

## 6. 测试

新建 `tests/test_evaluator.py`，至少覆盖：

- `preprocess_span` 的各种 case：冠词、标点、大小写、多余空格
- `token_f1` 的边界：完全相同（1.0）、完全不同（0.0）、空字符串（0.0）、部分重叠
- `match_triples` 的贪心配对：单对、多对、阈值边界（恰好 0.8、刚好 0.79）
- `Evaluator.update` + `report` 的端到端流程：构造几组人工 prediction + gold，验证最终指标计算正确

测试 fixture 直接在测试文件里硬编码 dict 即可，不需要外部文件。

---

## 7. 文件产出

```
src/evaluator.py
tests/test_evaluator.py
```

---

## 8. Notebook 验收 cells（追加到 main_pipeline.ipynb）

```python
# ===== SPEC_05 验收 =====
from src.evaluator import Evaluator, preprocess_span, token_f1, match_triples

# Cell O：span 预处理快速验证
test_pairs = [
    ("A super heavy rain", "super heavy rain"),
    ("The strike resumed on Tuesday.", "strike resumed on tuesday"),
    ("  Multiple   spaces  ", "multiple spaces"),
]
for raw, expected in test_pairs:
    got = preprocess_span(raw)
    mark = "✓" if got == expected else "✗"
    print(f"{mark} {raw!r} -> {got!r} (expected {expected!r})")

# Cell P：token_f1 快速验证
print(f"完全相同: {token_f1('heavy rain', 'heavy rain'):.3f}")
print(f"完全不同: {token_f1('apple pie', 'rocket science'):.3f}")
print(f"a/the 差异: {token_f1('a super heavy rain', 'the super heavy rain'):.3f}")
print(f"部分重叠: {token_f1('heavy rain caused flooding', 'heavy rain'):.3f}")

# Cell Q：构造小批量 prediction + gold 跑评估器（不依赖 LLM）
mock_preds = [
    {"id": 1, "has_causal": True, "triples": [
        {"cause": {"span": "heavy rain"}, "relation": "caused", "effect": {"span": "flooding"}}
    ]},
    {"id": 2, "has_causal": False, "triples": []},
    {"id": 3, "has_causal": True, "triples": [
        {"cause": {"span": "the strike"}, "relation": "caused", "effect": {"span": "delays"}}
    ]},
]
mock_golds = [
    {"id": 1, "has_causal": True, "relations": [{"cause": "heavy rain", "effect": "the flooding"}]},
    {"id": 2, "has_causal": False, "relations": []},
    {"id": 3, "has_causal": False, "relations": []},  # 这条 pred FP
]
ev = Evaluator()
for p, g in zip(mock_preds, mock_golds):
    ev.update(prediction=p, gold=g)
ev.print_report()

# Cell R：用真实数据集小规模跑通完整 eval pipeline（前 20 条）
from src.generator import generate
from src.data_io import load_dataset

if MODE == "eval":
    samples = load_dataset(DATASET)
    evaluator = Evaluator()
    n = min(20, len(samples))
    for i, s in enumerate(samples[:n], 1):
        pred = generate(
            text=s["text"],
            sample_id=s["id"],
            client=client,
            retriever=retriever if USE_RAG else None,
            use_rag=USE_RAG,
            top_k=RAG_TOP_K,
        )
        evaluator.update(prediction=pred, gold=s)
        if i % 5 == 0:
            print(f"已处理 {i}/{n} 条")
    print()
    evaluator.print_report()

# Cell S：完整数据集评估（耗时较长，按需运行）
if MODE == "eval":
    samples = load_dataset(DATASET)
    evaluator = Evaluator()
    for i, s in enumerate(samples, 1):
        pred = generate(
            text=s["text"],
            sample_id=s["id"],
            client=client,
            retriever=retriever if USE_RAG else None,
            use_rag=USE_RAG,
            top_k=RAG_TOP_K,
        )
        evaluator.update(prediction=pred, gold=s)
        if i % 50 == 0:
            print(f"已处理 {i}/{len(samples)} 条")
    print()
    evaluator.print_report()
```

---

## 9. SPEC_05 完成后的动作

1. 跑通所有验收 cells（O / P / Q 必须有输出；R 可选；S 可选）
2. 在 `reports/LESSONS.md` 追加 SPEC_05 的记录
   - 特别说明：贪心匹配是否符合预期？模糊阈值 0.8 在真实数据上效果如何？是否有大量边界 case 卡在阈值附近？
3. Git push（commit: `[evaluator] 完成 Demo1 评估模块`）
4. **停下来，告知项目作者"SPEC_05 已完成，Demo1 全线打通，请验收"**

---

# 总验收清单（项目作者用）

## 文件结构
- [ ] `src/evaluator.py` 存在
- [ ] `tests/test_evaluator.py` 存在且 `pytest` 全绿
- [ ] `notebooks/main_pipeline.ipynb` 末尾有 SPEC_05 验收 cells（O / P / Q / R / S）

## 功能正确性
- [ ] `preprocess_span` 正确处理冠词、标点、大小写、多余空格
- [ ] `token_f1` 对完全相同的 span 返回 1.0，对完全不相干 span 返回 0.0
- [ ] 模糊匹配阈值 0.8 生效，"a super heavy rain" vs "the super heavy rain" 算配对成功
- [ ] Layer 1 Detection 指标基于 has_causal 字段直接计算
- [ ] Layer 2 Extraction 只在 gold=True & pred=True 的样本上计算
- [ ] 贪心配对：每个 pred 和 gold 最多被配一次，未配上的算 FP / FN
- [ ] `print_report` 输出可读、字段齐全

## 集成性
- [ ] 在真实数据集小规模评估（前 20 条）跑通无错
- [ ] 评估器与 generator 流式集成无错（不需要中间 prediction.jsonl 文件）

## 文档
- [ ] `reports/LESSONS.md` 有 SPEC_05 段落
- [ ] 任何与本规范的偏离都明确说明

## Git
- [ ] commit message 符合 `[evaluator] 简述` 格式
- [ ] 已推送至 GitHub

---

**规范结束。**
