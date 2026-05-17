# SPEC_01 ｜ 数据清洗规范 v0.2

> **版本说明**：本版本基于 v0.1 全面重写。v0.1 中关于 Li (SCITE) 数据集、char_span、source/split 字段、signal 保留等设计**全部作废**，以本文档为准。
> **适用范围**：Causal KG Demo 项目，数据准备阶段
> **目标读者**：Codex agent（实现） + 项目作者（验收）
> **输入**：`Dataset_1_CNC_raw.csv`、`Dataset_2_Li_raw.xml`
> **输出**：`Dataset_1_CNC_modified.jsonl`、`Dataset_2_Li_modified.jsonl`

---

## 0. 阅读须知（给 Codex）

1. 本规范只定义"输入是什么、输出是什么、怎么转换"，**不规定使用哪些依赖库**，自行选择即可。
2. **所有操作必须在 conda 虚拟环境 `Master_thesis` 中完成**。开工前先检查该环境是否存在（`conda env list`），不存在则创建（`conda create -n Master_thesis python=3.11 -y`）。所有 `pip install` / `pytest` / `python` 命令均在该环境激活状态下执行。
3. **GitHub 仓库**：`https://github.com/Imcheatingbro/Master-thesis.git`（public）。完成后推送到此仓库。
4. 所有文件读写一律 UTF-8，写入 JSONL 时 LF 换行（`newline='\n'`），无 BOM。
5. 全文沟通、commit message、注释、docstring 统一中文。
6. 实现过程中遇到的任何边界、踩坑、与本规范不一致的判断，全部写进 `reports/LESSONS.md`。
7. 完成后按第 6 节验收清单逐项自检，全部通过才推 GitHub。
8. 有任何疑问直接问项目作者，不要自行猜测。

---

## 1. 统一目标格式（Unified Schema）

### 1.1 设计原则

- **极简优先**：只保留下游 LLM pipeline 真正需要的字段。
- **数据集分离**：CNC 和 Li 各自输出独立 jsonl 文件，文件名即来源标识，schema 内**不**带 source 字段。
- **无 split 字段**：是否划分 train/dev/test 由后续流程决定，本阶段处理完整文件。
- **无字符位置信息**：下游是自然语言输入输出的 LLM 任务，char_span 无评估价值。
- **无 signal 字段**：保持两个数据集字段一致，CNC 原始数据中的 `<SIG>` 标记在清洗时丢弃。

### 1.2 字段定义

每个样本一行 JSON，仅包含 **4 个顶层字段**：

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | `int` | 样本唯一编号，从 `1` 开始按原文件顺序递增。每个 jsonl 文件内独立编号，CNC 和 Li 不共享 id 空间。 |
| `text` | `str` | 纯净的句子文本，**不含任何标注标签**（无 `<ARG>` `<SIG>` `<e1>` 等）。 |
| `has_causal` | `bool` | 该句是否包含至少一对因果关系。 |
| `relations` | `list[object]` | 因果对列表。`has_causal=false` 时必须为 `[]`；`has_causal=true` 时长度必须 ≥ 1。 |

`relations` 中的每个对象包含 **2 个字段**：

| 字段 | 类型 | 说明 |
|---|---|---|
| `cause` | `str` | 原因部分的文本，**必须是 `text` 字段的子串**。 |
| `effect` | `str` | 结果部分的文本，**必须是 `text` 字段的子串**。 |

### 1.3 样例

**含因果（单对）**：
```json
{"id": 1, "text": "The farmworkers ' strike resumed on Tuesday when their demands were not met .", "has_causal": true, "relations": [{"cause": "their demands were not met", "effect": "The farmworkers ' strike resumed on Tuesday"}]}
```

**含因果（多对，CNC 多关系合并 / Li 多对共果，表示方式一致）**：
```json
{"id": 2, "text": "Cutler ended up with a bleeding stomach ulcer caused by the stress and hard work supervising their tours twenty-four hours a day.", "has_causal": true, "relations": [{"cause": "the stress", "effect": "a bleeding stomach ulcer"}, {"cause": "hard work", "effect": "a bleeding stomach ulcer"}]}
```

**非因果**：
```json
{"id": 3, "text": "Chale was allegedly chased by a group of about 30 people and was hacked to death with pangas , axes and spears .", "has_causal": false, "relations": []}
```

---

## 2. 数据集 1：CNC

### 2.1 原始格式（`Dataset_1_CNC_raw.csv`）

CSV 文件，UTF-8 编码，**首行可能含 BOM**（`\ufeff`），解析时需要剥离。

字段清单：

| 列名 | 含义 | 本规范是否使用 |
|---|---|---|
| `corpus` | 数据集名（恒为 `cnc`） | 否 |
| `doc_id` | 文档标识 | 否 |
| `sent_id` | 文档内句子标识 | 否 |
| `eg_id` | 同一句子的标注版本编号 | **是**（用于多关系合并） |
| `index` | 全局唯一标识，格式 `cnc_{doc_id}_{sent_id}_{eg_id}` | **是**（用于分组与去重） |
| `text` | 原句纯文本，**不含**任何 ARG/SIG 标签 | **是** |
| `causal_text_w_pairs` | 带标注的句子，**Python list 字面量字符串**，每个元素是一份只标一对因果的标注版本 | **是** |
| `num_rs` | 该原句包含的因果对数量；`0` 表示非因果 | **是**（用于一致性校验） |

### 2.2 标注语义

CNC 在 `causal_text_w_pairs` 中用 3 类成对 XML 风格标签包围 span：

| 标签对 | 含义 | 本规范如何处理 |
|---|---|---|
| `<ARG0>...</ARG0>` | **Cause** 原因 | 抽取为 `relations[i].cause` |
| `<ARG1>...</ARG1>` | **Effect** 结果 | 抽取为 `relations[i].effect` |
| `<SIG0>...</SIG0>` | Signal 触发词（可选，可能不存在） | **丢弃**，仅去除标签保留内部文本 |

**重要约束**：
- 同一份标注版本（list 中的一个元素）有且仅有 1 个 `<ARG0>` 和 1 个 `<ARG1>`。
- `<SIG0>` 可能**嵌套在 `<ARG0>` 或 `<ARG1>` 内部**（例：`<ARG0><SIG0>to</SIG0> hold a rally</ARG0>`）。剥离时要正确处理嵌套。
- 标签外的所有字符（包括空格、标点）属于句子上下文，不归任何角色。

### 2.3 解析规则

**Step 1：按 `index` 字段分组**

> 注：CNC 原始数据每一行的 `index` 字段已经唯一（一行一句），`causal_text_w_pairs` 列已经把同一原句的多对标注合并成一个 list。**无需跨行分组**，按行直接处理即可。`eg_id` 字段在本规范的清洗流程中不参与逻辑判断，仅作为元数据存在于原 CSV 中。

**Step 2：对每行处理**

1. 取 `text` 列作为统一格式的 `text` 字段。**不做任何文本清洗**（不去多余空格、不去标点空格），保留原样。
2. 将 `causal_text_w_pairs` 字段（字符串）用 `ast.literal_eval` 解析为 Python list。**禁止用 `eval`**。
3. 判断 `has_causal`：
   - 列表为空 `[]` → `has_causal = false`，`relations = []`
   - 列表非空 → `has_causal = true`，继续 Step 3
4. 一致性校验：`len(causal_text_w_pairs) == num_rs`。不一致时**记入 LESSONS.md** 并以 `len(causal_text_w_pairs)` 为准。

**Step 3：从每份标注版本提取 1 个 relation**

对 list 中每个标注字符串：
1. 先剥离 `<SIG0>` 和 `</SIG0>` 标签（但保留标签内文本）。剥离后字符串中应只剩 `<ARG0>` / `</ARG0>` / `<ARG1>` / `</ARG1>` 标签。
2. 用正则提取 `<ARG0>(.+?)</ARG0>` 内的文本作为 `cause`。
3. 用正则提取 `<ARG1>(.+?)</ARG1>` 内的文本作为 `effect`。
4. 对提取出的 `cause` / `effect` 做**首尾 strip**（去除前后空格），但**内部空格保留原样**。
5. 组装为 `{"cause": ..., "effect": ...}`，追加到 `relations` 数组。

**Step 4：子串校验（必须做）**

对每个 relation，断言 `cause` 和 `effect` 都是 `text` 字段的子串。
- 若不是子串 → 这是一个解析错误，**记入 LESSONS.md**，并将该 relation 跳过（不写入输出，但样本本身仍写入，relations 数组可能因此变短）。
- 若该样本所有 relation 都失败 → `has_causal` 仍保持原值 `true`、`relations = []`（这种异常状态必须在 stats 中体现，便于回查）。

### 2.4 输出顺序与编号

按 CSV 文件中原始行的出现顺序处理。`id` 从 `1` 开始递增，**不跳号**。

---

## 3. 数据集 2：Li

### 3.1 原始格式（`Dataset_2_Li_raw.xml`）

XML 文件，UTF-8 编码。根元素为 `<test-corpus>`（**即使 version 属性显示 2018 也不代表只有 test，按整个文件处理，不做 split 划分**）。每个样本对应一个 `<item>` 元素，结构如下：

```xml
<item id="2" label="Cause-Effect((e2,e1),(e3,e1))">
    <sentence>Cutler ended up with &lt;e1&gt;a bleeding stomach ulcer&lt;/e1&gt; caused by &lt;e2&gt;the stress&lt;/e2&gt; and &lt;e3&gt;hard work&lt;/e3&gt; supervising their tours twenty-four hours a day.</sentence>
</item>
```

**关键点**：
- `<sentence>` 内容中的 `<e1>` `<e2>` `<eN>` 标签在 XML 源文件中被**实体转义**为 `&lt;e1&gt;`、`&lt;/e1&gt;` 等。用标准 XML 解析器读取后会自动反转义为字面尖括号。这些尖括号是**句子文本的一部分**，**不是 XML 子元素**。
- `<item>` 的 `id` 属性是该数据集内的原始编号，本规范不直接使用，输出时按文件顺序重新编号。
- `<item>` 的 `label` 属性决定因果状态。

### 3.2 标注语义

#### 3.2.1 `<eN>` 实体标记

`<sentence>` 文本内用 `<e1>...</e1>`、`<e2>...</e2>`、`<e3>...</e3>` 包围**所有候选实体**（可能有 2 个或 3 个，按数据集惯例 e1/e2 是必有，e3 可选）。

**重要**：非因果句子里也会有 `<e1>` `<e2>`，这些实体跟因果无关，但仍需正确剥离标签。

#### 3.2.2 `label` 属性的两种取值

| label 形态 | 含义 | 解析动作 |
|---|---|---|
| `"Non-Causal"` | 非因果 | `has_causal = false` |
| `"Cause-Effect((eX,eY),(eX',eY'),...)"` | 因果 | `has_causal = true`，按括号对解析 |

**`Cause-Effect(...)` 字符串语法**：
- 最外层 `Cause-Effect( ... )` 包裹所有因果对。
- 内部是 1 个或多个 `(eX,eY)` 元组，逗号分隔。
- **每个 `(eX,eY)` 中 eX 是 cause、eY 是 effect**（与 SemEval-2010 Task 8 原约定一致）。
- 例：
  - `Cause-Effect((e2,e1))` → 1 对：e2 → e1
  - `Cause-Effect((e2,e1),(e3,e1))` → 2 对：e2 → e1，e3 → e1（"两因共果"，effect 文本会在 relations 中出现 2 次）

### 3.3 解析规则

**Step 1：用标准 XML 解析器读取整个文件**

推荐 `xml.etree.ElementTree`。遍历所有 `<item>` 元素。

**Step 2：对每个 `<item>` 处理**

1. 读取 `label` 属性。
2. 读取 `<sentence>` 子元素的文本内容（XML 解析器自动处理 `&lt;`/`&gt;` 反转义）。
3. 在剥离 `<eN>` 标签**之前**，先建立 `eN → 实体文本` 的映射表：
   - 用正则 `<e(\d+)>(.+?)</e\1>` 扫描句子文本（注意这里的尖括号是字面字符）。
   - 例：从 `<e1>a bleeding stomach ulcer</e1>` 提取出映射 `"e1" → "a bleeding stomach ulcer"`。
4. 剥离所有 `<eN>` 和 `</eN>` 标签，得到干净的 `text` 字段。剥离方式：用正则 `</?e\d+>` 替换为空字符串。**不做其他清洗**（不调整空格）。
5. 判断 label：
   - `label == "Non-Causal"` → `has_causal = false`，`relations = []`
   - 其他 → 继续 Step 3

**Step 3：解析 `Cause-Effect(...)` 字符串**

1. 用正则 `\((e\d+),(e\d+)\)` 抓取所有 `(eX,eY)` 元组。**不要尝试 ast.literal_eval**，因为这不是合法的 Python 字面量。
2. 对每个 `(eX, eY)` 元组：
   - 从 Step 2 的映射表查出 eX 对应文本作为 `cause`。
   - 从映射表查出 eY 对应文本作为 `effect`。
   - 若映射表中找不到对应 eN → 这是数据本身的错误，**记入 LESSONS.md**，跳过该 relation。
3. 组装为 `{"cause": ..., "effect": ...}`，按解析顺序追加到 `relations` 数组。

**Step 4：子串校验**

与 CNC 规则 §2.3 Step 4 完全一致：每个 relation 的 cause / effect 必须是清洗后 `text` 字段的子串，否则跳过并记入 LESSONS.md。

### 3.4 输出顺序与编号

按 XML 文件中 `<item>` 出现顺序处理。`id` 从 `1` 开始递增，**与 Li 原始 `id` 属性无关**。

---

## 4. 输出规范

### 4.1 文件位置

```
data/
├── raw/
│   ├── Dataset_1_CNC_raw.csv
│   └── Dataset_2_Li_raw.xml
└── modified/
    ├── Dataset_1_CNC_modified.jsonl
    ├── Dataset_2_Li_modified.jsonl
    └── stats.json
```

> 命名约定：以 `_raw` 结尾的是原始数据，以 `_modified` 结尾的是清洗后的统一格式。两个文件独立、互不混合。

### 4.2 JSONL 格式

- 每行一个完整 JSON 对象，**不换行、不缩进**。
- 字段顺序固定：`id` → `text` → `has_causal` → `relations`（便于人眼审阅 diff）。
- `relations` 内对象的字段顺序固定：`cause` → `effect`。
- 文件末尾**有**最后一行的换行符。
- UTF-8 编码，无 BOM，LF 换行。

### 4.3 stats.json 内容

每个数据集一个统计对象，聚合在同一份 `stats.json` 中：

```json
{
  "cnc": {
    "input_rows": <int>,
    "output_samples": <int>,
    "causal_samples": <int>,
    "non_causal_samples": <int>,
    "total_relations": <int>,
    "relation_count_distribution": {"0": <int>, "1": <int>, "2": <int>, "3": <int>},
    "warnings": {
      "num_rs_mismatch": <int>,
      "substring_check_failed_relations": <int>,
      "substring_check_failed_samples": <int>
    }
  },
  "li": {
    "input_items": <int>,
    "output_samples": <int>,
    "causal_samples": <int>,
    "non_causal_samples": <int>,
    "total_relations": <int>,
    "relation_count_distribution": {"0": <int>, "1": <int>, "2": <int>, "3": <int>},
    "warnings": {
      "missing_entity_mapping": <int>,
      "substring_check_failed_relations": <int>,
      "substring_check_failed_samples": <int>
    }
  }
}
```

---

## 5. 通用规则

### 5.1 编码与换行
- 读取 / 写入一律 UTF-8。
- 写入文件统一 LF 换行（`open(..., 'w', encoding='utf-8', newline='\n')`）。
- Windows 环境下尤其要注意：默认 CRLF 会污染 jsonl 解析。

### 5.2 文本完整性原则
- **不修改任何原始文本**。原始数据中 token 之间的空格（如 `" , "`、`" ."`）保留原样。
- 仅做两类操作：①标签剥离；②首尾 strip。

### 5.3 异常处理
- 禁止 `except: pass`。所有异常必须 log + 计入 stats。
- 子串校验失败、num_rs 不一致、实体映射缺失等"软错误"：跳过该 relation / 样本，**继续处理后续数据**。
- 文件不存在、XML 格式损坏等"硬错误"：抛异常并终止。

### 5.4 日志
- 使用 `logging` 模块，禁止 `print`。
- 日志级别：处理流程信息 → `INFO`；软错误 → `WARNING`；硬错误 → `ERROR`。

### 5.5 可复现性
- 处理流程必须**幂等**：对同一份 raw 数据多次运行，输出 jsonl 字节级一致。
- `id` 编号策略稳定：仅依赖文件原始顺序，不依赖文件系统遍历顺序或哈希随机性。

---

## 6. 验收清单

实现完成后逐项自检，**全部通过才能 commit**。

### 6.1 文件产物
- [ ] `data/modified/Dataset_1_CNC_modified.jsonl` 存在，UTF-8 + LF 换行
- [ ] `data/modified/Dataset_2_Li_modified.jsonl` 存在，UTF-8 + LF 换行
- [ ] `data/modified/stats.json` 存在，包含 cnc 和 li 两个顶层 key

### 6.2 schema 合规
- [ ] 每行 jsonl 都能被 `json.loads` 解析
- [ ] 每个样本恰好 4 个顶层字段：`id` `text` `has_causal` `relations`
- [ ] `id` 是从 1 开始连续递增的整数
- [ ] `has_causal=false` 时 `relations` 必为 `[]`
- [ ] `has_causal=true` 时 `relations` 长度 ≥ 1（若全部 relation 因软错误跳过，按 §2.3 Step 4 末段规则处理并记 stats）
- [ ] 每个 relation 仅含 `cause` `effect` 两个字段，均为非空字符串

### 6.3 内容正确性（抽样人工检查）
- [ ] CNC 输出抽样 5 条因果样本，对照原 CSV 的 `causal_text_w_pairs`，cause/effect 文本完全吻合（无残留 `<SIG>` 标签）
- [ ] Li 输出抽样 5 条因果样本，对照原 XML 的 label 和 `<eN>` 标记，cause/effect 与实体文本吻合
- [ ] Li 输出抽样 3 条非因果样本，text 中无残留 `<e1>` `<e2>` 标签
- [ ] 抽 1 条 Li 的多对因果样本（如原 id=2），确认 `relations` 数组长度等于 label 中括号对数量

### 6.4 子串约束
- [ ] 对每个文件全量遍历，验证所有 relation 的 cause/effect 都是同样本 text 的子串（**这是硬性约束，下游 LLM 评估依赖此性质**）

### 6.5 stats 合理性
- [ ] stats.json 中 `causal_samples + non_causal_samples == output_samples`
- [ ] `relation_count_distribution` 中 `key=0` 的数量等于 `non_causal_samples`
- [ ] `total_relations` 等于所有 relation 的总和

### 6.6 文档
- [ ] `reports/LESSONS.md` 有本次实现的记录段落（含踩坑、设计取舍、遗留问题、与本规范的任何偏差）

### 6.7 Git
- [ ] commit message 格式 `[data] <简述>`
- [ ] 已推送至 GitHub private repo

---

**规范结束。**
