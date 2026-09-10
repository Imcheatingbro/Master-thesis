# gemma4-12b-overfit20-step100 CNC SFT overfit20_train eval report

## 配置
```json
{
  "label": "gemma4-12b-overfit20-step100 CNC SFT overfit20_train",
  "model": "gemma4-12b-overfit20-step100",
  "dataset": "cnc_gemma12_overfit20_train",
  "sample_count": 20,
  "prompt_name": "cnc_gemma_v2",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 0,
  "temperature": 0.0,
  "max_tokens": 512,
  "primary_metric": "anchor_window",
  "progress_every": 10,
  "max_workers": 1,
  "llm_provider": "openai_compatible",
  "llm_base_url": "http://127.0.0.1:8001/v1",
  "context_length": null,
  "reasoning_effort": null,
  "llm_extra_body": null,
  "api_key_source": "local direct Unsloth API",
  "report_detail_limit": 200,
  "report_detail_mode": "errors",
  "report_error_metric": "anchor_window",
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ gemma4-12b-overfit20-step100 CNC SFT overfit20_train final report ================
样本总数: 20
  Gold 含因果: 10 | Pred 含因果: 10
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 1.000
  Precision: 1.000
  Recall   : 1.000
  F1       : 1.000
  (TP=10, TN=10, FP=0, FN=0)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 20
    Gold triples: 14 | Pred triples: 14
    Precision: 1.000
    Recall   : 1.000
    F1       : 1.000
    (TP=14, FP=0, FN=0)
  [anchor_window] (primary)
    样本数: 20
    Gold triples: 14 | Pred triples: 14
    Precision: 1.000
    Recall   : 1.000
    F1       : 1.000
    (TP=14, FP=0, FN=0)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 10
    Gold triples: 14 | Pred triples: 14
    Precision: 1.000
    Recall   : 1.000
    F1       : 1.000
    (TP=14, FP=0, FN=0)
  [anchor_window] (primary)
    样本数: 10
    Gold triples: 14 | Pred triples: 14
    Precision: 1.000
    Recall   : 1.000
    F1       : 1.000
    (TP=14, FP=0, FN=0)
================================================
```

## 生成失败统计
```json
{
  "total": 0,
  "by_type": {},
  "samples": []
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

Sample details shown: all 0 wrong samples from 20 total samples.
