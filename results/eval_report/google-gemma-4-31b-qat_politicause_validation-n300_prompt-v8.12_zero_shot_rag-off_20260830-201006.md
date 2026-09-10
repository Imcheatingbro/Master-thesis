# politicause_validation first 300 eval report

## 配置
```json
{
  "label": "politicause_validation first 300",
  "model": "google/gemma-4-31b-qat",
  "dataset": "politicause_validation",
  "sample_count": 300,
  "prompt_name": "v8.12_zero_shot",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 1,
  "temperature": 0.0,
  "max_tokens": 8192,
  "output_schema": "standard",
  "primary_metric": "anchor_window",
  "progress_every": 100,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 8192,
  "reasoning_effort": "none",
  "llm_extra_body": {
    "cache_prompt": false
  },
  "api_key_source": "file:deepseek_api.txt",
  "report_detail_limit": 200,
  "report_detail_mode": "errors",
  "report_error_metric": "anchor_window",
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ politicause_validation first 300 final report ================
样本总数: 300
  Gold 含因果: 85 | Pred 含因果: 0
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.717
  Precision: 0.000
  Recall   : 0.000
  F1       : 0.000
  (TP=0, TN=215, FP=0, FN=85)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 300
    Gold triples: 85 | Pred triples: 0
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=0, FN=85)
  [anchor_window] (primary)
    样本数: 300
    Gold triples: 85 | Pred triples: 0
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=0, FN=85)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 0
    Gold triples: 0 | Pred triples: 0
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=0, FN=0)
  [anchor_window] (primary)
    样本数: 0
    Gold triples: 0 | Pred triples: 0
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=0, FN=0)
================================================
```

## 生成失败统计
```json
{
  "total": 300,
  "by_type": {
    "unknown_generation_error": 300
  },
  "samples": [
    {
      "id": 12959,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1508,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14471,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4482,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15348,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5612,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5582,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 779,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 17107,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9241,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 17125,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3695,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11157,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13401,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15147,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13972,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15577,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13902,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7292,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16586,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12348,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1865,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14831,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2595,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9886,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1486,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11022,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7745,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5221,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12781,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6334,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2955,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1224,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7592,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10938,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15544,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11802,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10919,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15061,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13901,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6964,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15855,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5414,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15776,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13980,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6758,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13779,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15448,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1587,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9518,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 867,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5262,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13195,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14081,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13583,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 17076,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9493,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6165,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16809,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15208,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12742,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13141,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6025,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5434,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8026,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11986,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10117,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6032,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13587,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15152,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11364,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12299,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 917,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2286,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7769,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13844,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7509,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15428,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9901,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14057,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15742,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7788,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16563,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15618,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11504,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 216,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 647,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14009,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9197,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15330,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13856,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1967,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6986,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8868,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3554,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15895,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1214,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3824,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 939,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1983,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12764,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11946,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9960,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1065,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11799,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9047,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9787,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10751,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7291,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14520,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9059,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5651,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16045,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14212,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9698,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1532,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10886,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 433,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11213,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5683,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8377,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13624,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10445,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6942,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 17553,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16356,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6591,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9897,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11987,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5300,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9916,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8534,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3635,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12133,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 17523,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 936,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 698,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16743,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3577,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7055,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10899,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8926,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7235,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5064,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 946,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4565,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7522,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13539,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16071,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4567,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2885,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14752,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16580,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6978,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3651,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15004,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10489,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2234,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14787,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5236,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13276,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9104,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13269,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10048,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11717,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12408,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7709,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14441,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9343,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14050,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6094,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1127,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12465,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14058,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9918,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14614,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2699,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5364,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2276,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14512,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 811,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 17630,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16535,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8813,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12185,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10841,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16652,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4433,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16651,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16817,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4815,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1404,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3687,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10582,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9052,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9439,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 17298,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8652,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5142,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12744,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4182,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14432,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15266,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16619,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4849,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16470,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1246,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6948,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16035,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3864,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10803,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1403,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15671,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3014,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5421,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14962,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14488,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16593,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9278,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8389,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11945,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3569,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13529,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3421,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16750,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7733,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3785,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 10270,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 680,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6628,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4674,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8002,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4235,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8506,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14909,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5483,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9193,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15621,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13034,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11401,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3134,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7677,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9677,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3437,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8254,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7547,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16384,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1245,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 15391,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8990,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13888,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2592,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16991,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 17042,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16270,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6568,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8655,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12379,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9086,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16675,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 389,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13373,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13791,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2706,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8176,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1499,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16958,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7126,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 5803,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 7574,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6607,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14997,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11719,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16988,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12237,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13521,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16186,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4261,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12969,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3839,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 12717,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 1377,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2365,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 9964,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16534,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 6330,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 11130,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13225,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16379,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 2700,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 14809,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 4793,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3027,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13126,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 3759,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 13971,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 438,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 16904,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 8949,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    },
    {
      "id": 218,
      "error_type": "unknown_generation_error",
      "error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
    }
  ]
}
```

## 解析修复统计
```json
{
  "total": 0,
  "by_type": {},
  "samples": []
}
```

## 样本明细

Sample details shown: first 200 of 300 wrong samples from 300 total samples.

### --- id=12959 ---

输入文本: I have no doubt that his extensive experience and leadership will enable him to successfully conduct our deliberations.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "his extensive experience and leadership",
      "effect": "enable him to successfully conduct our deliberations"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1508 ---

输入文本: The world’s economic centre of gravity is shifting decisively towards Asia, centred on the economic growth of China and India.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14471 ---

输入文本: We must avoid any incident liable to trigger ever worse consequences.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=4482 ---

输入文本: Further investigations are being undertaken.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15348 ---

输入文本: At the same time, to help us recover from the economic devastation caused by this pandemic, the starting point is three words: Cancel the Debts.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "this pandemic",
      "effect": "the economic devastation"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5612 ---

输入文本: That means that by 15 April we will be able to offer a first dose to all of you who are over 50, as well as those under 50 who are clinically vulnerable.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5582 ---

输入文本: Today, we are also reminded about the vital importance of fighting this virus to protect our economy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "fighting this virus",
      "effect": "protect our economy"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=779 ---

输入文本: The hospital admission rate for week 12 was 19.48 per 100,000 population, in the previous week it was 18.55 per 100,000 population.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=17107 ---

输入文本: As a small island developing State, and with all the constraints that come with that status, the Democratic Republic of Sao Tome and Principe pursues policies adapted to our reality, with full respect for multicultural diversity and human rights.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9241 ---

输入文本: Especially at a time when we already had a shortage of workers and near full employment across the economy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=17125 ---

输入文本: The cost of poverty, the cost of radicalized youth and the cost of children bred by ignorance will always outstrip any investment we can make today.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=3695 ---

输入文本: Dr Yvonne Doyle, Medical Director at Public Health England, said: Case rates in people aged 20 to 29 are at the highest across any age group recorded since the pandemic began.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11157 ---

输入文本: It also provided an opportunity to mobilize the energy of different stakeholders in the climate change arena and to recognize that our undertaking is of a global nature.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13401 ---

输入文本: We are profoundly thankful for all the attention and support from the Organization and its Member States and specialized agencies in the aftermath of the massive devastation inflicted on us by the category 5 Hurricane Maria in September 2017.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15147 ---

输入文本: Today around 60,000 Cuban agents control and interfere with every area of Venezuelan society, especially intelligence and defence.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13972 ---

输入文本: In 2017, 2018 and 2019, in order to properly ensure accountability, my country submitted voluntary reports that take stock of the significant progress we have made in each of the 17 Goals.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "submitted voluntary reports that take stock of the significant progress we have made in each of the 17 Goals",
      "effect": "in order to properly ensure accountability"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15577 ---

输入文本: It also inflicted collective punishment on people, deliberately and repeatedly cutting off the water supply of more than 1 million Syrians in Al-Hasakah and its surrounding residential areas.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13902 ---

输入文本: Faced with the immediate and lofty task of charting the future of the Union of the Comoros, I decided to work harder than ever to strengthen national unity and social cohesion, without which efforts for harmonious development would be in vain.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "work",
      "effect": "strengthen"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7292 ---

输入文本: We restored the balance of power by strengthening democratic dialogue and governance among the various levels of the State.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "strengthening democratic dialogue and governance",
      "effect": "restored the balance"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16586 ---

输入文本: Despite the violations by the Houthis, my country will continue its efforts to achieve peace.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12348 ---

输入文本: While there should be no doubt about the goodwill of President Kiir and the Government he leads to secure peace and the establishment of a just, peaceful, inclusive and prosperous South Sudan, we need to identify and address the objective reasons for those failures.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1865 ---

输入文本: As a candidate with a realistic chance of becoming a member of the Human Rights Council, we will advocate for streamlined agendas and better synergy between Geneva and New York.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14831 ---

输入文本: To continue to do so has been and remains the very essence of what Japan can contribute to the rest of the world.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=2595 ---

输入文本: Only a global response facilitating access for all to vaccines can put an end to this global scourge.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "facilitating access for all to vaccines",
      "effect": "put an end to this global scourge"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9886 ---

输入文本: First, we must all reaffirm the fundamental importance of international law and the Charter of the United Nations in international relations and multilateral cooperation.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1486 ---

输入文本: A challenge which has been made easier as a result of this grant.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "this grant",
      "effect": "has been made easier"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11022 ---

输入文本: We will continue to support the call for removing the economic and financial embargo on it, which has caused untold suffering for Cuba’s citizens.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "the economic and financial embargo",
      "effect": "untold suffering"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7745 ---

输入文本: Flu is another winter virus.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5221 ---

输入文本: Minister for Care Gillian Keegan said: Protecting care staff and people who use social care services continues to be a priority, especially as cases surge and Omicron spreads rapidly around the country.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12781 ---

输入文本: This session is being held at a time when the international community faces the adverse socioeconomic impact of the COVID-19 pandemic.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6334 ---

输入文本: We have a dedicated chapter on environment in our Constitution, which mandates 60 per cent forest coverage and maintain inter-generational equity of our natural resources.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=2955 ---

输入文本: Armenia appealed to ODKB (Collective Security Treaty Organization) for military assistance, thus admitting its defeat.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "appealed to ODKB (Collective Security Treaty Organization) for military assistance",
      "effect": "admitting its defeat"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1224 ---

输入文本: It is never too late to come forward for your first dose and it’s vital that everyone comes forward to get boosted now as we head into the new year.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7592 ---

输入文本: Last week, clinical guidance was updated to enable COVID-19 boosters to be given slightly earlier to those at highest risk, where this makes operational sense to do so.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10938 ---

输入文本: In recent years, Prime Minister Netanyahu and I developed the Tracks for Regional Peace initiative, which will connect the Arab Gulf States by rail through Jordan to the Israeli ports in Haifa.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15544 ---

输入文本: Across the African continent, revenues have fallen by as much as $150 billion as economies are still reeling from the impact of the pandemic.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "reeling from the impact of the pandemic",
      "effect": "revenues have fallen by as much as $150 billion"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11802 ---

输入文本: Is it reasonable and acceptable for the United Nations to emerge from the greatest threat to human security since the Organization was established in the same state it was in at the beginning of 2020?

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10919 ---

输入文本: In that context, the Horn of Africa and Middle East regions have been immensely and inordinately afflicted in the past 25 years by externally instigated, intractable, internecine ethnic and clan conflicts, as well as discord and wars among neighbouring countries.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "externally instigated, intractable, internecine ethnic and clan conflicts",
      "effect": "have been immensely and inordinately afflicted"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15061 ---

输入文本: We continue to cooperate strategically with the United States and to work together to root out the remnants of terrorism, wherever they are.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13901 ---

输入文本: I therefore again call on our partners in the international community to support us in this process so that it is transparent and credible.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6964 ---

输入文本: It is necessary to struggle so that solidarity, cooperation and mutual respect prevail if we are to provide an effective response to the needs and aspirations of all peoples and preserve what is most valuable: human life and dignity.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15855 ---

输入文本: But the international law we have accepted and adhered to and the peace for which we strive are now in severe jeopardy, as a result of Israel’s policies and practices in our occupied land and the fact that it has reneged on agreements it has signed, since the Oslo Accords in 1993 to date.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "Israel’s policies and practices in our occupied land",
      "effect": "severe jeopardy"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5414 ---

输入文本: Those who leave self-isolation on or after day 7 are strongly advised to limit close contact with other people in crowded or poorly ventilated spaces, work from home and minimise contact with anyone who is at higher risk of severe illness if infected with COVID- 19.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15776 ---

输入文本: We need a stronger United Nations to respond more effectively to protracted conflicts and humanitarian crises in the Middle East, sub-Saharan Africa and other regions.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13980 ---

输入文本: In addition, our country opted for decent work, providing more guarantees and rights to workers, including the right to social security and free medical care for rural and domestic workers, who have historically been neglected.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6758 ---

输入文本: Developed countries account for the largest share of the world’s production of vaccines.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13779 ---

输入文本: Today, the mobile and instantaneous nature of communications have brought us closer to the misfortunes of all in a much more direct way.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15448 ---

输入文本: International financing to stop COVID, and to deal with its impact both on health and economies, is still too little.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1587 ---

输入文本: We have signed a pact with the youth to make a genuine change in the policies that will benefit them.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "have signed a pact with the youth",
      "effect": "make a genuine change in the policies that will benefit them"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9518 ---

输入文本: Today I would like to reiterate once again that the world is greater than five countries.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=867 ---

输入文本: The hospital admission rate for week 5 was 13.22 per 100,000 population, in the previous week it was 16.40 per 100,000 population.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5262 ---

输入文本: Appointments continue to be available over the festive period.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13195 ---

输入文本: That leads us to our current dedicated efforts, which we are undertaking together with other ASEAN members, to push for partnership and turn conflicts into cooperation so that development and progress can be sustainable.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "current dedicated efforts, which we are undertaking together with other ASEAN members",
      "effect": "development and progress can be sustainable"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14081 ---

输入文本: In Iceland, our experience shows that both individuals’ rights and human rights are essential to positive economic and social development.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13583 ---

输入文本: We see the United Nations as a forum that has been provided to give a voice to the voiceless, the marginalized and those lacking power and wealth.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=17076 ---

输入文本: Nevertheless, the approach based on the security-development nexus may not be enough to overcome security challenges as they may have roots going beyond development per se.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9493 ---

输入文本: The Nile River Basin Cooperative Framework Agreement, signed in May 2010 after 13 years of negotiations, was our first and only truly inclusive multilateral treaty in this area.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6165 ---

输入文本: To save lives.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16809 ---

输入文本: This is already reflected in efforts to establish a strategic hub of excellence and a first-class business centre in the West African subregion and to develop centres to transform agriculture, manufacturing and the extractive industry while strengthening social development and inclusion mechanisms.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15208 ---

输入文本: The monopoly of tribal chief Raoni is over. The United Nations has played a key role in overcoming colonialism and cannot possibly accept that this type of mindset be allowed to return to its halls and corridors under any pretext.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12742 ---

输入文本: We are now embarking on reviving our tourism sector, which was badly affected because of the travel restrictions imposed in many countries in order to curb the spread of COVID-19.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "travel restrictions imposed in many countries in order to curb the spread of COVID-19",
      "effect": "was badly affected"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13141 ---

输入文本: As they work to achieve sustainable development, landlocked developing countries face specific challenges that require special attention.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6025 ---

输入文本: On this note, the Lao PDR continues its economic infrastructure development in order to efficiently facilitate the regional and subregional integration through various cooperation frameworks.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "economic infrastructure development",
      "effect": "efficiently facilitate the regional and subregional integration through various cooperation frameworks"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5434 ---

输入文本: This is a mammoth deal for the UK government and for patients across the country that are set to benefit from these antivirals over the coming months.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=8026 ---

输入文本: Prevalence rates were uncertain for those whose second dose was more than 6 months previously.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11986 ---

输入文本: We reiterate the call on all parties to commit to updated and more ambitious NDCs in order to meet the Paris Agreement promise.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "commit to updated and more ambitious NDCs",
      "effect": "meet the Paris Agreement promise"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10117 ---

输入文本: On the three principles of action — namely, emancipate, protect and ensure real equality — we will act in view of the Generation Equality Forum, to be held in Paris in July 2020, 25 years after the Beijing Declaration, which marked the history of our Organization.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6032 ---

输入文本: I think that it is a very wise choice, as today we hear more news that makes despair and lose hope nowadays.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "hear more news",
      "effect": "makes despair and lose hope nowadays"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13587 ---

输入文本: To reject the norms of collective, mutually respectful action taken together in favour of aggressive individual action, or to retreat to an old, false rhetoric of war, promises misery in the form of a continuity of instability, imbalance, social inequality and exploitation in every aspect of a potential shared life.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15152 ---

输入文本: We have done our part to assist them, through Operation Welcome — an operation conducted by the Brazilian army that has earned praise worldwide.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11364 ---

输入文本: Precisely because it was Germany that 80 years ago unleashed fire and destruction in Europe and the world, we must assume a special responsibility today for an order that secures peace.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "80 years ago unleashed fire and destruction in Europe and the world",
      "effect": "we must assume a special responsibility today for an order that secures peace"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12299 ---

输入文本: We urge the United Nations to increase its collaboration and partnerships with those bodies and Governments in order to usher in a more peaceful subregion.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "increase its collaboration and partnerships",
      "effect": "usher in a more peaceful subregion"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=917 ---

输入文本: Weekly case rates per 100,000 population were highest in the North East at 2,350.8.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=2286 ---

输入文本: One of the main challenges developing countries such as ours are faced with relate to access to essential medicines and vaccines.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7769 ---

输入文本: This is now easier than ever before as vaccinations are now available both through school or a walk-in centre.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13844 ---

输入文本: The constant bullying by ruffians — and the original meaning of the word ruffians is bully boys — particularly the ruffians who are the bureaucrats of the European Union, has revealed that the unambiguous objective of the European Union is not well-regulated Caribbean financial centres but a decimated and discredited sector, while it panders to the thriving centres that exist within its own borders or in other more powerful locales.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7509 ---

输入文本: Let all the difficulties we have overcome lay the firm foundation for a new understanding among peoples.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15428 ---

输入文本: We know that isolationism also contributes to growing authoritarianism.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "isolationism",
      "effect": "growing authoritarianism"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9901 ---

输入文本: In the South-East Asia region, ASEAN is a regional institution that is based on shared commitments and collective responsibility in enhancing regional peace, security and prosperity.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14057 ---

输入文本: Those days gave Afghans tremendous belief that peace is possible and proved that the Government has the ability to directly negotiate peace with our enemies.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15742 ---

输入文本: The United in Science report details the degree of acidification and deoxygenation affecting our oceans and killing marine life.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7788 ---

输入文本: Red list and quarantine hotels will continue to operate as the UK’s first defence against incoming variants of concern (VOC), with reviews taking place every 3 weeks.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16563 ---

输入文本: The United Arab Emirates has participated in regional and international efforts aimed at easing tensions and reaching political solutions to the crises in the Middle East, including in Libya, Yemen, the Sudan, Syria and Palestine.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15618 ---

输入文本: That is what will make democracy attractive to our people in our individual countries.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11504 ---

输入文本: It should serve as a clarion call to Member States to work collaboratively, in good faith, toward early reform of the Security Council to effectively respond to the urgent needs and challenges facing the diverse membership of the United Nations.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "work collaboratively, in good faith, toward early reform of the Security Council",
      "effect": "effectively respond to the urgent needs and challenges"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=216 ---

输入文本: Genomes have now been uploaded from South Africa, Botswana and Hong Kong but the extent of spread is not yet determined.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=647 ---

输入文本: The regulations will be published shortly.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14009 ---

输入文本: In Uruguay, we are absolutely convinced that the key to facing those challenges lies in the universalization of education.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "universalization of education",
      "effect": "facing"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9197 ---

输入文本: The government has been clear that it keeps all COVID-19 measures under review.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15330 ---

输入文本: We, all together, have the will and capacity to make it better.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13856 ---

输入文本: Immense progress has been made towards macroeconomic and fiscal stabilization as well as high-impact projects that pave the way for private-sector-led growth.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "macroeconomic and fiscal stabilization as well as high-impact projects",
      "effect": "pave the way for private-sector-led growth"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1967 ---

输入文本: That is precisely why my country, the Republic of the Congo, has very deep faith and trust in the Organization, which has such a unique historical trajectory.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6986 ---

输入文本: Apart from posing a significant threat to health, the pandemic is also a serious threat to development.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=8868 ---

输入文本: Vaccine effectiveness for Pfizer, where the second dose was administered 6 weeks or more after the first dose, stood at 85% from 14 to 73 days after, falling to 51% after 6 months.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=3554 ---

输入文本: Lithuania welcomes Ukraine’s efforts to negotiate an end to the war and calls on Russia to move closer to a sustainable political resolution.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15895 ---

输入文本: In that context, Peru reaffirms its commitment to a rules-based multilateral trading system, as reflected in the World Trade Organization, and encourages everyone to work towards strengthening and improving that organization in order to guarantee the stability, predictability and transparency of the multilateral trading system, for the benefit of all.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "strengthening and improving",
      "effect": "guarantee"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1214 ---

输入文本: The latest data confirmed that among those who had received 2 doses of AstraZeneca, there was no effect against Omicron from 20 weeks after the second dose.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "received 2 doses of AstraZeneca",
      "effect": "no effect against Omicron from 20 weeks after the second dose"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=3824 ---

输入文本: The hospital admission rate for COVID-19 has fallen – it was 0.73 per 100,000 in week 19, compared to 1.02 per 100,000 in the previous week.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=939 ---

输入文本: The lowest case rates were in those aged 80 and above, with a weekly rate of 69.5 per 100,000 population.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1983 ---

输入文本: A fairer world is one in which we are all protected from COVID-19.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12764 ---

输入文本: And because it’s logistically straightforward, it can be practically deployed in the poorest parts of the world too.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "it’s logistically straightforward",
      "effect": "can be practically deployed in the poorest parts of the world too"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11946 ---

输入文本: Designed to further the cause of peace, stability and security in the Indo- Pacific region for the benefit of all who live within that region.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9960 ---

输入文本: We firmly condemn the unjustified political and diplomatic aggression against Burundi and its people by foreign Governments, some of which were known to have attempted regime change in 2015 through unconstitutional means.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1065 ---

输入文本: We are immensely proud of what NVAP has achieved so far and look forward to expanding its reach even further over the coming months and years.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11799 ---

输入文本: Even more so, the path to membership serves to secure the higher standards all peoples aspire to.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "membership",
      "effect": "secure"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9047 ---

输入文本: Note this data will be updated later today, Thursday 10 February.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9787 ---

输入文本: Palau has some of the most well-preserved coral reef ecosystems in the world.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10751 ---

输入文本: Without unity, the struggle will only drain our energy and will never be won.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7291 ---

输入文本: For Nauru, and our small population of 12,000, with limited health infrastructure, our best defence against the virus is our closed borders and a capture and contain policy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14520 ---

输入文本: That was a major achievement of the Armenian people’s non-violent velvet revolution of 2018.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9059 ---

输入文本: This includes responsibility for developing and expanding pathogen genomic surveillance in partnership with scientific organisations including the Wellcome Sanger Institute, NHS, public health agencies from all 4 countries of the UK, academic institutions and the COVID-19 Genomics UK (COG-UK) consortium.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5651 ---

输入文本: So, when the call comes, please do get a jab and, in the meantime, stay at home, protect the NHS and save lives.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "stay at home",
      "effect": "protect the NHS and save"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16045 ---

输入文本: It should also be very clear that new conflicts should not cause us to forget older ones, for that would be a destructive message and peace is not divisible.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14212 ---

输入文本: The United States and its regional satellites are preparing an act of aggression against Venezuela from Colombia, putting the security and stability of the continent at risk.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "are preparing an act of aggression against Venezuela from Colombia",
      "effect": "putting the security and stability of the continent at risk"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9698 ---

输入文本: As Micronesia is addressing the existential threat of climate change, we want to point out that it is impossible to tackle it without protecting the ocean, the world’s largest carbon sink.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1532 ---

输入文本: Surely such a world — which now looms on the horizon — is one that all leaders should work to prevent, focusing their attention instead on advancing the progress of our one humankind through cooperation and mutual benefit.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10886 ---

输入文本: I urge the international community to mobilize resources in order to provide assistance.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "mobilize resources",
      "effect": "provide assistance"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=433 ---

输入文本: Our white paper on integration, which we’ll be bringing forward shortly, will go even further.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11213 ---

输入文本: In Kenya we have invested heavily in education and health in an effort to achieve social inclusion, develop knowledge and competencies and secure the future by not leaving anyone behind.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "invested heavily in education and health",
      "effect": "achieve social inclusion, develop knowledge and competencies and secure the future"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5683 ---

输入文本: If we can catch more asymptomatic people before they unknowingly pass on the disease to the vulnerable, we can help to stop the virus’ vicious spread.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "catch more asymptomatic people before they unknowingly pass on the disease",
      "effect": "help to stop the virus’ vicious spread"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=8377 ---

输入文本: However, children under 2 can be at greater risk of severe illness, especially those born prematurely, with a heart condition or who have a chronic lung disease.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13624 ---

输入文本: I hope that it sets a level of ambition for the total elimination of nuclear weapons, the only guarantee of our safety.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10445 ---

输入文本: We want the United Nations to be ready to lead in the twenty-first century, fully benefiting from the technological advances of humankind that have made it much easier for those who are not big and powerful — the majority of United Nations Member States — to follow and contribute to the Organization’s various bodies and numerous discussions.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "technological advances",
      "effect": "made it much easier for those who are not big and powerful — the majority of United Nations Member States — to follow and contribute to the Organization’s various bodies"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6942 ---

输入文本: Azerbaijan ratified the Paris Climate Agreement, with a voluntary commitment to achieve a 35 percent reduction in greenhouse gas emissions by 2030 compared to the base year 1990.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=17553 ---

输入文本: The Government of Ethiopia took the necessary measures to avert the grave danger imposed on us.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "took",
      "effect": "avert"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16356 ---

输入文本: Collaboration with development partners, financial institutions and the private sector, among others, is critical.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6591 ---

输入文本: In order to prevent high-handedness and arbitrariness in the Security Council, we should increase its representation of developing countries, which make up a majority of the United Nations.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "increase its representation of developing",
      "effect": "prevent"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9897 ---

输入文本: Secondly, it is important to enhance global and regional synergies.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11987 ---

输入文本: Fundamentally, it must be about improving lives and empowering people, especially the poorest and most vulnerable.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5300 ---

输入文本: BA.1 (Omicron) accounted for 1.69% (11 of 650) of the recorded COVID-19 infections where the sequencing was determined in this round (up to 11 December).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9916 ---

输入文本: Finally, the political commitment of world leaders is indispensable to any efforts aimed at revitalizing multilateralism.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=8534 ---

输入文本: Over 109,000 volunteers in England took part in the study to examine the levels of COVID-19 in the general population between 8 March and 31 March.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=3635 ---

输入文本: The assistance provided to us by the WHO, the United Nations and its swiftly established Fund, as well as international donors, was essential.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12133 ---

输入文本: We’re going to be throwing everything at it, in order to ensure that everyone eligible is offered that booster in just over two months.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "going to be throwing everything at it",
      "effect": "to ensure that everyone eligible is offered that booster in just over two months"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=17523 ---

输入文本: We have also seen that a lack of in-person communication among family members, friends, children, colleagues, States and nations has a negative impact on businesses, education, social behaviour and relations and mental health.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "a lack of in-person communication among family members, friends, children, colleagues, States and nations",
      "effect": "negative impact on businesses, education, social behaviour and relations and mental health"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=936 ---

输入文本: Thursday 16 December The main points from this week’s national influenza and COVID-19 surveillance report are: Surveillance indicators suggest that at a national level COVID-19 activity has increased in most indicators in week 49 of 2021.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=698 ---

输入文本: Remember to observe good hand and respiratory hygiene.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16743 ---

输入文本: As a nation, we see human capital as a critical enabler for achieving the SDGs.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "human capital",
      "effect": "achieving"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=3577 ---

输入文本: Mr. President, With regards to the Renaissance Dam matter, I wish to seize this opportunity to convey to you the mounting concerns of the Egyptian nation regarding this project, currently being constructed by a neighboring and friendly Country, which shares a river that has provided life to millions of people for thousands of years.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7055 ---

输入文本: At the outset, I would like to convey a message of solidarity from the Malagasy people with every nation and family that has been hard hit by the coronavirus disease (COVID-19) pandemic.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10899 ---

输入文本: Those actions constitute a serious threat to regional peace and security and a direct attack on the Venezuelan people, in an attempt to break them in the cruellest of ways.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=8926 ---

输入文本: Fiona Sandford, CEO for Visionary, said: More visually impaired people are able to test for COVID-19 at home, which is a significant step forward.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7235 ---

输入文本: It must be able to work effectively, efficiently and independently of any political or other influence.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5064 ---

输入文本: As Children’s Commissioner and having run schools all my life, I’m always excited about the start of a new term and the return to school.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=946 ---

输入文本: We need everyone to take action to stop the spread.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "take action",
      "effect": "stop the spread"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=4565 ---

输入文本: This is so that expert scientists can understand more about how to deploy these treatments in the NHS more widely later in the year – including who would benefit most from receiving antiviral treatments for COVID-19.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7522 ---

输入文本: The reality today is that our world is far from being a safe place to live in.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13539 ---

输入文本: For my part, I am fully cognizant of our responsibility and I can assure the Assembly that the Niger will assume it with commitment and conviction and with a view to helping to find solutions to the various challenges facing the international community.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16071 ---

输入文本: What is more, by helping local communities to understand and reduce disaster risk, Georgia is strengthening a culture of resilience that is a core value of democracy and self-government.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "helping local communities to understand and reduce disaster risk",
      "effect": "is strengthening a culture of resilience"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=4567 ---

输入文本: Anyone over the age of 50 or between 18 to 49 with an underlying health condition can sign up to the study as soon as they receive a positive PCR or lateral flow test result.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=2885 ---

输入文本: Today I would like to focus on three critical developments — three crises, in fact — that have dominated our attention this summer.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14752 ---

输入文本: According to that report, Africa is losing more than $50 billion annually through illicit financial outflows.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "illicit financial outflows",
      "effect": "is losing"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16580 ---

输入文本: This year our sister nation of Saudi Arabia hosted Gulf, Arab and Islamic summits, in a successful example of coordinating regional and international positions to address the critical security situation in the region.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6978 ---

输入文本: They even doubted Syria’s cooperation with the OPCW, in addition to taking advantage of reports that lack credibility and professionalism.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=3651 ---

输入文本: We must show respect to the international law, effectively protect human rights and fundamental freedoms, and promote economic and social cohesion on a global scale.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=15004 ---

输入文本: Up to 200 species become extinct every day.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10489 ---

输入文本: That is why we have taken the decision to implement a plan for a long-term low-emission strategy that will enable us to take the necessary steps to achieve more ambitious targets, such as carbon neutrality by the year 2050.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "taken the decision to implement a plan for a long-term low-emission strategy",
      "effect": "take the necessary steps to achieve more ambitious targets"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=2234 ---

输入文本: We place great hope in the regional C5 dialogue frameworks with major extraregional actors.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14787 ---

输入文本: The transformational potential of universal health coverage is now at the top of the global health agenda, thanks to the outstanding leadership of the World Health Organization and many other stakeholders.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "thanks to the outstanding leadership of the World Health Organization and many other stakeholders",
      "effect": "is now at the top of the global health agenda"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5236 ---

输入文本: As friends, families and loved ones gather for the festive season, the public is reminded that vaccines remain the best way to protect people against COVID-19.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13276 ---

输入文本: We must reflect those messages in our policies if we are to respond bravely and with determination.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9104 ---

输入文本: It forms part of wide-ranging plans to tackle the backlog of elective care caused by the COVID-19 pandemic, which also includes the rollout of more than 100 community diagnostic centres across the country and extra surgical hubs, all backed by a billion pounds of additional investment.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "the COVID-19 pandemic",
      "effect": "the backlog of elective care"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=13269 ---

输入文本: Speaking of international solidarity and inclusion, I would once again like to call from this rostrum for the total lifting of the decades-long embargo imposed on the Government and people of Cuba, in order to remove the obstacles to their achievement of the Sustainable Development Goals, which is a legitimate aspiration for all the peoples of the world.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "lifting of the decades-long embargo imposed on the Government and people of Cuba",
      "effect": "remove the obstacles to their achievement of the Sustainable Development Goals"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10048 ---

输入文本: With regard to Syria, I would like to welcome the encouraging announcements made yesterday by the Special Representative of the Secretary-General, and a decisive step forward with respect to the constitution, at last, by the long-awaited Constitutional Committee.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=11717 ---

输入文本: The European Union and its Member States must strengthen the dialogue on migration issues with the countries of origin and transit of migrants, in order to achieve joint responsibility in the management of flows.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "strengthen the dialogue on migration issues with the countries of origin and transit",
      "effect": "achieve joint responsibility in the management of flows"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12408 ---

输入文本: Namibia, however, aims to deploy innovative approaches to ensure sustainable economic development in this volatile period of pandemic and climate change.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "deploy innovative approaches",
      "effect": "ensure sustainable economic development"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=7709 ---

输入文本: Hundreds of thousands of people continue to book in for their vital boosters with a further 1.7 million invites due to land this week and the NHS has now opened up hundreds of walk-in sites across the country so people can get their top-up protection without delay.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "has now opened up hundreds of walk-in sites across the country",
      "effect": "people can get their top-up protection without delay"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14441 ---

输入文本: The gains are real, but we know we still have an extremely long way to go.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9343 ---

输入文本: So, if you haven’t already, please come forward for your first, second or booster jab.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14050 ---

输入文本: I am very confident that such an effort, with the support of the Russian Federation and the West, could radically change the profile of my country, about which I spoke with such great concern at the beginning of my address.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "effort, with the support of the Russian Federation",
      "effect": "could radically change"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=6094 ---

输入文本: We must therefore maintain our regional and international solidarity in a relentless effort to combat it and ensure our regional security.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "maintain our regional and international solidarity in",
      "effect": "to combat it and ensure our regional security."
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1127 ---

输入文本: Data by variant related to intensive care unit admissions is presented and an analysis into the effect of the recent surge of Omicron cases in care homes is also available in the latest technical briefing.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12465 ---

输入文本: We urge migrant-receiving countries to treat them fairly and protect their jobs, health and well-being during these trying times.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14058 ---

输入文本: Each of these has been a significant step in an ongoing Afghan-led process that is geared toward an inclusive, sustainable and dignified peace for all Afghans.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9918 ---

输入文本: Only when such commitment is guaranteed can we enter a new, brighter chapter in the history of humankind — a chapter of cooperation and dialogue; a chapter of sustainable peace and development.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14614 ---

输入文本: To address this global challenge, we have been working to develop an innovative climate-finance mechanism, which is part of Armenia’s national pledge for the United Nations Climate Action Summit.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=2699 ---

输入文本: Samoa is confident that despite all the challenges, even existential threats for some of us; there is still hope if there is Unity amongst our UN family.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5364 ---

输入文本: Boosters Separately, in response to the threat from the Omicron variant, the JCVI has advised that booster vaccinations should be offered to persons aged: 16 to 17 years 12 to 15 who are in a clinical risk group or who are a household contact of someone (of any age) who is immunosuppressed 12 to 15 years who are severely immunocompromised and who have had a third primary dose The booster vaccination for these age groups should be with 30 micrograms of the PfizerBioNTech COVID-19 vaccine, given no sooner than 3 months after completion of the primary course.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=2276 ---

输入文本: Addressing those inequalities and fostering a more robust spirit of global solidarity in the face of daunting challenges reflects the values and interests of the entire United Nations, not just those of Canada.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=14512 ---

输入文本: At the outset, I would like to congratulate His Excellency Mr. Tijjani Muhammad-Bande on his election as President of the General Assembly at its seventy-fourth session.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=811 ---

输入文本: Please help reduce transmission by wearing a face covering in crowded or enclosed spaces, washing hands regularly, keeping rooms well ventilated.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=17630 ---

输入文本: I would like to thank the Secretariat and the host country’s services for the enormous effort they have invested to ensure that the general debate is not only a demonstration of hope and belief that the world will deal with the pandemic but also a secure and safe event for all participants.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "enormous effort",
      "effect": "ensure"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16535 ---

输入文本: As we all know, migration is the result of deep-rooted causes that require immediate action, together with medium- to long-term perspectives.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "deep-rooted causes",
      "effect": "migration"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=8813 ---

输入文本: However, staying at home and avoiding contact with others is still the most effective way to avoid passing on COVID-19 if you are infected.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12185 ---

输入文本: That is the conceptual cornerstone of human security, but we are struggling to comprehend this reality, and above all, take action to safeguard us all.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10841 ---

输入文本: Despite everything, I believe that the agreement between Serbs and Albanians is of the utmost importance to the stability of the Balkans and that those two nations have a role in our region that Winston Churchill intended for France and Germany when he spoke of uniting Europe.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16652 ---

输入文本: We are currently working on an ambitious low-carbon development strategy that will enable Latvia to reach climate neutrality by 2050.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "an ambitious low-carbon development strategy",
      "effect": "reach climate neutrality"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=4433 ---

输入文本: Conducting the final regular traffic light review before the switch to the new two-tiered system, several additional countries and territories will move off the red list – Turkey, Pakistan, the Maldives, Egypt, Sri Lanka, Oman, Bangladesh and Kenya.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16651 ---

输入文本: In Latvia, we have reduced our greenhouse-gas emissions by almost 60 per cent compared to our 1990 levels, but we understand that it is not enough, and we therefore support climate neutrality as a goal for the future.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=16817 ---

输入文本: We therefore welcome the Addis Ababa Action Agenda of the Third International Conference on Financing for Development, which remains a key framework for mobilizing financial resources likely to lead to tangible progress in achieving the SDGs.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=4815 ---

输入文本: So I’m sure the whole house would want to join me in wishing Professor Sir Jonathan Van-Tam the very best.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=1404 ---

输入文本: One case is located in Camden, London, and one case is located in Wandsworth, London.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=3687 ---

输入文本: Yet, they try in vain to deprive Iran of its minimum defense requirements, and disregard international law and global consensus in order to extend arms restrictions against Iran in contravention of the letter of UNSCR 2231.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "try in vain to deprive Iran of its minimum defense requirements, and disregard international law and global consensus",
      "effect": "in order to extend arms restrictions against Iran in contravention of the letter of UNSCR 2231"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=10582 ---

输入文本: Where is the constructive action by the countries responsible for carbon emissions that believe that it is okay to continue to build coal-power plants and not decommission them, and that do not understand that the world is providing us with prospects of new industries and new jobs while enabling us to save the world for our young people?

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9052 ---

输入文本: Hinge – Hinge is encouraging users to share their vaccination status on their profiles.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=9439 ---

输入文本: We have enlarged the political space, releasing jailed political prisoners and journalists; inviting exiled political parties to return home and pursue their peaceful struggle; revising electoral, counter-terrorism and civil society laws; and ending the 20-year conflict with Eritrea.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=17298 ---

输入文本: That requires securing peace and stability and resolving existing conflicts.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=8652 ---

输入文本: One dose has been found to provide long-lasting protection against this disease for up to 6 months.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=5142 ---

输入文本: With COVID-19 cases continuing to rise rapidly, the best resolution you can make this new year is to protect yourself and those around you, so I urge you to come forward for your booster as soon as you can, and with hundreds of thousands of appointments available in the coming days, it has never been easier to grab your jab.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```

### --- id=12744 ---

输入文本: After all, we are living in an era in which humankind can irreversibly destroy the living conditions on our planet.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "Prompt 模板不存在: D:\\Master thesis\\prompts\\v8.12_zero_shot.txt"
}
```
