# SPEC_02-04 ｜ Demo1 生成 Pipeline 实现规范

> **适用范围**：Causal KG Demo 项目，Demo1 阶段（text → JSON triples）
> **依赖文档**：`AGENT.md`（全局规则）、`SPEC_01_data_cleaning_v0.2.md`（数据格式）
> **输入**：`data/modified/Dataset_1_CNC_modified.jsonl` 和 `data/modified/Dataset_2_Li_modified.jsonl`
> **本规范覆盖三个模块**：SPEC_02 (LLM Client)、SPEC_03 (Prompt + Pattern RAG)、SPEC_04 (Generator)
> **执行方式**：**逐 SPEC 顺序完成**，每完成一个 SPEC 立刻在主 notebook 中追加验收 cells，然后**停下来等待项目作者验收**，验收通过才能开始下一个 SPEC。

---

## 0. 阅读须知（给 Codex）

1. 本规范包含 3 个 SPEC，**必须按 SPEC_02 → SPEC_03 → SPEC_04 顺序实现**。
2. 每完成一个 SPEC：
   - 在 `notebooks/main_pipeline.ipynb` 中追加该 SPEC 对应的验收 cells（见各 SPEC 末尾）
   - 在 `reports/LESSONS.md` 中追加本 SPEC 的踩坑记录
   - 推送 Git（commit message: `[spec_0X] 模块名简述`）
   - **停下来。明确告诉项目作者"SPEC_0X 已完成，请验收"。在收到验收通过的回复之前，不要开始下一个 SPEC。**
3. 全局规则遵守 `AGENT.md`（conda env `Master_thesis`、中文沟通、Simplicity First、Surgical Changes 等）。
4. 数据集是 SPEC_01 已完成的产物，路径：`data/modified/Dataset_1_CNC_modified.jsonl` 和 `Dataset_2_Li_modified.jsonl`，schema 见 SPEC_01。

---

## 1. 公共设计：主 notebook 与全局参数

实现 SPEC_02 时第一步就是建立 `notebooks/main_pipeline.ipynb` 的骨架。Notebook 顶部第一个 cell 是**全局参数配置**：

```python
# ===== 全局运行配置 =====
MODE = "demo"          # "eval" 或 "demo"
DATASET = "cnc"        # "cnc" 或 "li"（eval 模式 + demo sample 模式使用）

# demo 模式专用
DEMO_INPUT = "manual"     # "manual"（手动输入单条）或 "sample"（数据集抽样）
DEMO_TEXT = "Heavy rain caused widespread flooding in the region."  # manual 时使用
DEMO_SAMPLE_N = 10        # sample 时使用：从数据集随机抽 N 条

# RAG 开关
USE_RAG = False
RAG_TOP_K = 3

# LLM 参数
TEMPERATURE = 0.0      # eval 用 0 保证可复现；demo 可以调高看多样性
MAX_TOKENS = 2048
```

后续每个 SPEC 完成时只在 notebook 中**追加 cells**，不要修改这个全局配置 cell 的结构。

---

# SPEC_02 ｜ LLM Client

## 2.1 任务边界

**只做**：把 LM Studio 的 chat completion HTTP API 封装成 Python 函数。

**不做**：prompt 构造（SPEC_03）、输出解析（SPEC_04）、streaming、并发、缓存。

## 2.2 配置文件

新建 `configs/llm.yaml`：

```yaml
llm:
  base_url: "http://127.0.0.1:1234/v1"
  model: "qwen/qwen3-14b"
  api_key: "lm-studio"
  temperature: 0.0
  max_tokens: 2048
  timeout: 120
  retry_times: 3
```

**重要**：base_url 末尾必须有 `/v1`，OpenAI SDK 会自动拼 `/chat/completions` 等子路径。

## 2.3 模块文件

新建 `src/llm_client.py`：

- 类 `LLMClient`，构造函数读 `configs/llm.yaml`，支持 notebook 中覆盖参数
- 方法 `chat(messages: list[dict]) -> str`：接 OpenAI 格式的 message list，返回 LLM 输出的纯字符串
- 方法 `ping() -> bool`：测试连接，调用 `GET /v1/models` 验证服务可达
- 支持 `role: "system"` 和 `role: "user"`（SPEC_03 会用到）
- 失败重试：网络错误 / 超时时重试 `retry_times` 次，间隔指数退避
- 完整 logging：每次调用记录耗时、输入 message 总字符数、输出字符数

## 2.4 依赖

用官方 `openai` Python 包（`pip install openai`）。LM Studio 完全兼容 OpenAI chat API，初始化时把 `base_url` 指向本地即可。

## 2.5 文件产出

```
configs/llm.yaml
src/llm_client.py
tests/test_llm_client.py        # 至少测 ping() 和异常重试逻辑（用 mock）
```

## 2.6 Notebook 验收 cells（追加到 main_pipeline.ipynb）

```python
# ===== SPEC_02 验收 =====
# Cell A：导入与初始化
from src.llm_client import LLMClient
client = LLMClient()
print(f"Base URL: {client.base_url}")
print(f"Model: {client.model}")

# Cell B：连通性测试
assert client.ping(), "LM Studio server 未启动或无法访问"
print("✓ LM Studio 连接正常")

# Cell C：最简单的 hello 测试
resp = client.chat([{"role": "user", "content": "Reply with exactly the word 'hello' and nothing else."}])
print(f"模型回复: {resp}")

# Cell D：System message 测试
resp = client.chat([
    {"role": "system", "content": "You are a translator. Translate user input to French."},
    {"role": "user", "content": "Good morning"}
])
print(f"翻译结果: {resp}")

# Cell E：真实因果抽取试探（只是测 client，不评估输出质量）
resp = client.chat([
    {"role": "user", "content": "Extract cause and effect from this sentence: 'Smoking causes lung cancer.' Output in JSON format."}
])
print(f"因果输出: {resp}")
```

## 2.7 SPEC_02 完成后的动作

1. 跑通所有验收 cells（每个都有输出）
2. 在 `reports/LESSONS.md` 追加 SPEC_02 的记录
3. Git push（commit: `[llm_client] 完成 LM Studio 客户端封装`）
4. **停下来，告知项目作者"SPEC_02 已完成，请验收"。等待验收通过再开始 SPEC_03。**

---

# SPEC_03 ｜ Prompt + Pattern RAG

## 3.1 任务边界

**做**：
- 设计 prompt 模板（明确 explicit + implicit 因果定义、输出 schema、few-shot 示例）
- 实现 Pattern RAG 检索器（基于已清洗的数据集构建 pattern database）
- 实现 prompt 组装逻辑（根据 `USE_RAG` 开关，组装最终发给 LLM 的 messages）

**不做**：调 LLM（SPEC_02 的事）、解析输出（SPEC_04 的事）。

## 3.2 Prompt 设计要点

新建 `prompts/v1.txt`，作为 prompt 模板文件（带占位符）。Prompt 必须明确以下内容：

### 3.2.1 任务定义
让 LLM 从输入文本中抽取因果关系，输出严格 JSON 格式。

### 3.2.2 输出 schema（必须严格遵守）

```json
{
  "has_causal": true,
  "triples": [
    {
      "cause": {"span": "..."},
      "relation": "caused",
      "effect": {"span": "..."}
    }
  ]
}
```

约束：
- `has_causal` 必填，bool 类型
- `triples` 必填，数组，无因果时为 `[]`
- `relation` 固定值 `"caused"`
- `cause.span` 和 `effect.span` 必须是**输入文本的原始子串**（不要改写、不要总结）

### 3.2.3 因果判断标准

Prompt 中必须明确告诉模型识别**两类因果**：

**(1) 显式因果**：由因果连接词直接标示（"because"、"caused by"、"due to"、"therefore"、"as a result"、"leads to" 等）。

**(2) 隐式 / 弱因果**：以下定义必须**逐字写入 prompt**：

> In addition to explicit causal relations, you should also extract weak or implicit causal relations when the sentence expresses a purpose, motivation, or reason for an action.
>
> A purpose/motivation relation should be treated as a causal span pair if:
> 1. one span describes an action/event performed by an agent;
> 2. another span describes the purpose, motivation, or reason for that action;
> 3. the meaning can be paraphrased as: "Because the agent wanted/intended to [purpose], the agent did [action]."
>
> For such cases, output:
> - Cause span: the purpose/motivation/reason span
> - Effect span: the action/event span
>
> Common linguistic cues include: "to", "in order to", "so as to", "for the purpose of", "aimed at", "intended to", "meant to", "not to X but to Y".
>
> Do not exclude a relation only because it is not introduced by explicit causal markers such as "because", "therefore", or "as a result".

### 3.2.4 Few-shot 示例

Prompt 中至少包含 3 个 in-context examples，覆盖：
- 显式因果（1 对）
- 隐式因果（purpose/motivation 类）
- 无因果

例子的格式与输出 schema 一致，让 LLM 模仿。

### 3.2.5 占位符

Prompt 模板使用以下占位符：
- `{rag_examples}`：Pattern RAG 检索到的 few-shot examples（USE_RAG=False 时为空字符串）
- `{input_text}`：当前要抽取的句子

## 3.3 Pattern RAG 设计

### 3.3.1 参考资料

`reference code from related work/PatternRAG/` 文件夹中有原论文的参考代码。**Agent 自行阅读理解源代码中 RAG 是如何工作的，把这套机制迁移到本项目**：每条输入文本都要经过 RAG 流程，匹配到若干个相似的 example，作为 few-shot 注入 prompt。

**核心要求**：
- 匹配的 example 数量可配置（通过 `top_k` 参数控制，默认 3）
- 检索的具体相似度策略、连接词提取方式、索引结构等技术细节，由 agent 阅读参考代码后自行决定，并在 `LESSONS.md` 中说明选择理由

### 3.3.2 Pattern Database

**数据库已就绪，无需构建**：

- 路径：`DAGdatabase/comb_SCITEsemADE_CausalityPattern.csv`
- 这是 SCITE / SemEval / ADE 三个数据集合并的 causal pattern 库
- Agent 自行查看 csv 表结构后决定如何加载与索引

### 3.3.3 检索逻辑

新建 `src/rag_retriever.py`：

- 类 `PatternRetriever`，构造时加载 `DAGdatabase/comb_SCITEsemADE_CausalityPattern.csv`
- 方法 `retrieve(text: str, top_k: int) -> list[dict]`：对输入文本，返回 top-k 个最相似的 pattern example
- 具体的检索算法、相似度度量、example 字段返回格式等细节，agent 参考源代码自行实现

## 3.4 Prompt 组装

新建 `src/prompt_builder.py`：

- 方法 `build_messages(text: str, use_rag: bool, retriever: Optional[PatternRetriever], top_k: int) -> list[dict]`
- 返回 OpenAI 格式的 messages 列表（含 system + user）
- 若 `use_rag=True`，调用 retriever 拿到 top-k examples，填入 `{rag_examples}` 占位符
- 若 `use_rag=False`，`{rag_examples}` 部分留空（或不出现）

## 3.5 文件产出

```
prompts/v1.txt
src/rag_retriever.py
src/prompt_builder.py
tests/test_prompt_builder.py     # 测试 build_messages 在 use_rag True/False 下的行为
tests/test_rag_retriever.py      # 测试检索返回格式与数量
```

> Pattern Database 文件 `DAGdatabase/comb_SCITEsemADE_CausalityPattern.csv` 已由项目作者提供，不在本 SPEC 产出列表中。

## 3.6 Notebook 验收 cells（追加到 main_pipeline.ipynb）

```python
# ===== SPEC_03 验收 =====
# Cell F：验证 Pattern Database 文件存在
from pathlib import Path
pattern_db_path = Path("DAGdatabase/comb_SCITEsemADE_CausalityPattern.csv")
assert pattern_db_path.exists(), f"Pattern DB 不存在: {pattern_db_path}"
print(f"✓ Pattern Database 已就绪: {pattern_db_path}")
print(f"  文件大小: {pattern_db_path.stat().st_size / 1024:.1f} KB")

# Cell G：检验 Prompt 模板渲染（不调 LLM）
from src.prompt_builder import build_messages
from src.rag_retriever import PatternRetriever

# 不带 RAG
messages = build_messages(DEMO_TEXT, use_rag=False, retriever=None, top_k=0)
for m in messages:
    print(f"--- {m['role']} ---")
    print(m['content'])
    print()

# Cell H：带 RAG 的 prompt 渲染
retriever = PatternRetriever()
messages_rag = build_messages(DEMO_TEXT, use_rag=True, retriever=retriever, top_k=3)
for m in messages_rag:
    print(f"--- {m['role']} ---")
    print(m['content'])
    print()

# Cell I：观察 RAG 检索到的 examples
examples = retriever.retrieve(DEMO_TEXT, top_k=3)
print(f"检索到 {len(examples)} 个 examples:")
for i, ex in enumerate(examples, 1):
    print(f"\n--- Example {i} ---")
    print(ex)

# Cell J：用 SPEC_02 的 client 真正调一次 LLM（只看输出，不解析）
resp = client.chat(messages_rag if USE_RAG else messages)
print("=== LLM 原始输出 ===")
print(resp)
```

## 3.7 SPEC_03 完成后的动作

1. 跑通所有验收 cells
2. 在 `LESSONS.md` 追加记录（特别说明 RAG 相似度策略的选择理由）
3. Git push（commit: `[prompt_rag] 完成 prompt 模板与 Pattern RAG`）
4. **停下来，告知项目作者"SPEC_03 已完成，请验收"。等待验收通过再开始 SPEC_04。**

---

# SPEC_04 ｜ Generator

## 4.1 任务边界

**做**：
- 把 SPEC_02（LLM 调用）和 SPEC_03（prompt 构造）串起来
- 解析 LLM 的字符串输出为 Python dict
- 处理各种解析异常（markdown 包裹、前缀解释、破损 JSON）
- 必要时重试（解析失败、字段缺失）

**不做**：schema 校验（DAY2）、RDF 序列化（DAY2）、评估（SPEC_05）。

## 4.2 输出格式

最终 generate 函数返回的 dict 严格遵守以下 schema：

```json
{
  "id": 42,
  "has_causal": true,
  "triples": [
    {
      "cause": {"span": "their demands were not met"},
      "relation": "caused",
      "effect": {"span": "The farmworkers ' strike resumed on Tuesday"}
    }
  ]
}
```

- `id`：eval 模式从 ground truth 取；demo manual 模式填 `null`；demo sample 模式从原样本取
- 无因果样本：`has_causal=false`, `triples=[]`
- **不输出 `text` 字段**

## 4.3 模块文件

新建 `src/generator.py`，内部至少包含以下函数：

```
call_llm(messages, client) -> str
    调 SPEC_02 的 client，返回原始字符串

parse_output(raw_str) -> dict
    字符串 → dict。要处理：
    - 直接 json.loads 成功的情况
    - markdown 代码块包裹（```json ... ```）
    - 前后有解释文本（用正则提取首个 { ... } 块）
    - 字段缺失时报清晰错误

validate_minimal(d) -> bool
    检查 dict 是否含有 has_causal 和 triples 两个顶层字段，类型正确
    （这是 demo1 唯一允许的"轻校验"，不是 SPEC_05 的评估校验）

generate(text, sample_id, client, retriever, use_rag, top_k, max_retry=2) -> dict
    主入口：build_messages → call_llm → parse_output → validate_minimal
    解析或校验失败时重试 max_retry 次
    全部失败时返回兜底结果：{"id": sample_id, "has_causal": false, "triples": []}
    并在 LESSONS 风格的日志中记录失败样本
```

## 4.4 错误处理策略

- 解析失败 → 重试（重新调 LLM，保持 temperature）
- 重试耗尽 → 写日志 + 返回兜底（`has_causal=false, triples=[]`）+ **不抛异常中断流程**（评估时需要继续跑其他样本）
- 兜底次数记入运行日志，最终在评估报告中可见

## 4.5 集成到 notebook：实际跑通生成

SPEC_04 完成时，notebook 已具备完整生成能力。需要追加：
- 数据加载函数（读 modified jsonl）
- 根据 MODE 分支：
  - eval 模式：循环跑所有样本（或 N 条样本），收集预测结果到内存（先不评估，评估留给 SPEC_05）
  - demo manual：跑单条 DEMO_TEXT，pretty-print 输出
  - demo sample：从数据集抽 DEMO_SAMPLE_N 条，逐条跑，pretty-print 输出

## 4.6 文件产出

```
src/generator.py
src/data_io.py                   # 读 modified jsonl 的工具函数（小模块）
tests/test_generator.py          # 重点测 parse_output 的各种异常情况
```

## 4.7 Notebook 验收 cells（追加到 main_pipeline.ipynb）

```python
# ===== SPEC_04 验收 =====
import json
from src.generator import generate, parse_output
from src.data_io import load_dataset

# Cell K：parse_output 鲁棒性快速测试（不调 LLM，用构造字符串）
test_cases = [
    '{"has_causal": true, "triples": []}',                                          # 纯 JSON
    'Here is the result:\n{"has_causal": false, "triples": []}',                   # 带前缀
    '```json\n{"has_causal": true, "triples": []}\n```',                           # markdown 包裹
    'Sure!\n```\n{"has_causal": false, "triples": []}\n```\nDone.',                # 无 json 标记的 markdown
]
for i, tc in enumerate(test_cases, 1):
    try:
        result = parse_output(tc)
        print(f"✓ 用例 {i}: {result}")
    except Exception as e:
        print(f"✗ 用例 {i} 解析失败: {e}")

# Cell L：单条 demo（manual 模式）
if MODE == "demo" and DEMO_INPUT == "manual":
    result = generate(
        text=DEMO_TEXT,
        sample_id=None,
        client=client,
        retriever=retriever if USE_RAG else None,
        use_rag=USE_RAG,
        top_k=RAG_TOP_K,
    )
    print("=== Demo 单条输出 ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))

# Cell M：数据集抽样 demo（sample 模式）
if MODE == "demo" and DEMO_INPUT == "sample":
    samples = load_dataset(DEMO_DATASET, n=DEMO_SAMPLE_N)
    for s in samples:
        result = generate(
            text=s["text"],
            sample_id=s["id"],
            client=client,
            retriever=retriever if USE_RAG else None,
            use_rag=USE_RAG,
            top_k=RAG_TOP_K,
        )
        print(f"\n--- id={s['id']} ---")
        print(f"输入: {s['text']}")
        print(f"Gold: has_causal={s['has_causal']}, relations={len(s['relations'])}")
        print(f"Pred: {json.dumps(result, indent=2, ensure_ascii=False)}")

# Cell N：批量生成（eval 模式预备，但本 SPEC 不做评估）
if MODE == "eval":
    samples = load_dataset(DATASET)
    predictions = []
    for s in samples[:20]:  # 先跑前 20 条验证 pipeline 通畅
        result = generate(
            text=s["text"],
            sample_id=s["id"],
            client=client,
            retriever=retriever if USE_RAG else None,
            use_rag=USE_RAG,
            top_k=RAG_TOP_K,
        )
        predictions.append({"pred": result, "gold": s})
    print(f"成功生成 {len(predictions)} 条预测，留待 SPEC_05 评估")
    # 简单看看前 3 条对比
    for p in predictions[:3]:
        print(f"\nid={p['gold']['id']}")
        print(f"  Gold has_causal={p['gold']['has_causal']}, relations={p['gold']['relations']}")
        print(f"  Pred has_causal={p['pred']['has_causal']}, triples={p['pred']['triples']}")
```

## 4.8 SPEC_04 完成后的动作

1. 跑通所有验收 cells
2. 在 `LESSONS.md` 追加记录（特别说明：解析兜底触发率、常见解析失败模式、重试是否有效）
3. Git push（commit: `[generator] 完成 Demo1 生成 pipeline`）
4. **停下来，告知项目作者"SPEC_04 已完成，Demo1 生成 pipeline 全线打通，请验收。SPEC_05 评估模块将作为下一份独立规范发布。"**

---

# 总验收清单（项目作者用）

Demo1 全部完成时，项目作者按以下清单验收：

## 文件结构
- [ ] `configs/llm.yaml` 存在且字段完整
- [ ] `src/llm_client.py`、`src/prompt_builder.py`、`src/rag_retriever.py`、`src/generator.py`、`src/data_io.py` 全部存在
- [ ] `prompts/v1.txt` 存在，包含 explicit + implicit 定义、few-shot examples、输出 schema 说明
- [ ] `DAGdatabase/comb_SCITEsemADE_CausalityPattern.csv` 已就位（由项目作者提供）
- [ ] `tests/` 下对应每个模块都有测试文件，`pytest` 全绿
- [ ] `notebooks/main_pipeline.ipynb` 顶部有全局参数 cell，下方有 SPEC_02/03/04 的验收 cells

## 功能正确性
- [ ] LM Studio 启动后，`client.ping()` 返回 True
- [ ] System message 能正确传递（不被忽略）
- [ ] RAG 关闭时 prompt 中不出现 examples 段
- [ ] RAG 开启时能检索到合理的相似 examples
- [ ] generate 函数在 demo manual / demo sample / eval 三种模式下都能正常工作
- [ ] 输出 JSON 严格符合 schema：含 `id` / `has_causal` / `triples` 三个顶层字段，relation 固定为 `"caused"`

## 文档
- [ ] `reports/LESSONS.md` 有 SPEC_02、SPEC_03、SPEC_04 三段记录
- [ ] 任何与本规范的偏离都在 LESSONS 中明确说明

## Git
- [ ] 三次独立 commit，message 符合 `[模块] 简述` 格式
- [ ] 已推送至 GitHub

---

**规范结束。**
