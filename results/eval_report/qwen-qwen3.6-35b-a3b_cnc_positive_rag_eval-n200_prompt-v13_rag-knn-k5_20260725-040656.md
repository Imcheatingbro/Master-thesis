# cnc_positive_rag_eval first 200 eval report

## 配置
```json
{
  "label": "cnc_positive_rag_eval first 200",
  "model": "qwen/qwen3.6-35b-a3b",
  "dataset": "cnc_positive_rag_eval",
  "sample_count": 200,
  "prompt_name": "v13",
  "use_rag": true,
  "rag_mode": "knn",
  "rag_top_k": 5,
  "temperature": 0.0,
  "max_tokens": 16384,
  "progress_every": 500,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 16384,
  "reasoning_effort": null,
  "llm_extra_body": {},
  "api_key_source": "file:deepseek_api.txt",
  "report_detail_limit": 200,
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ cnc_positive_rag_eval first 200 final report ================
样本总数: 200
  Gold 含因果: 200 | Pred 含因果: 0
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.000
  Precision: 0.000
  Recall   : 0.000
  F1       : 0.000
  (TP=0, TN=0, FP=0, FN=200)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 200
    Gold triples: 267 | Pred triples: 0
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=0, FN=267)
  [anchor_window]
    样本数: 200
    Gold triples: 267 | Pred triples: 0
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=0, FN=267)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 0
    Gold triples: 0 | Pred triples: 0
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=0, FN=0)
  [anchor_window]
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
  "total": 200,
  "by_type": {
    "unknown_generation_error": 200
  },
  "samples": [
    {
      "id": 197,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1855,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1427,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 823,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 3053,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2332,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2609,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1204,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 453,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2465,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 848,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2271,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1444,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 347,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 7,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 473,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 471,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 100,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 669,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1707,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1290,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2447,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 958,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2035,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 308,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1442,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1059,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1163,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 353,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 722,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 443,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2450,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 512,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 886,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1720,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1778,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1369,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2790,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1216,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 612,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 488,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2643,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2746,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2127,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 179,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 150,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1322,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2402,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2838,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2563,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 986,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 3071,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2067,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 572,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2056,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2647,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 434,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1998,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1621,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2367,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1056,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2557,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2763,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1512,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1536,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 27,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1826,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 355,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2241,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1253,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2017,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2567,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 207,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1654,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 230,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2878,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1625,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2999,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2724,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1351,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 518,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1357,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 975,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1893,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 3018,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2751,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1920,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2611,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 499,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1988,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1367,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2455,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2377,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 676,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 406,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2712,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2718,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1575,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1817,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 302,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2594,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1062,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2384,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1281,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2341,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1189,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1517,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1093,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1551,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1967,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 3045,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1860,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1460,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 3013,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1905,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2626,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2503,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1570,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 181,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2539,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2726,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 962,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2076,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1080,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2147,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2577,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1835,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2658,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2624,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1653,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 902,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1560,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1953,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 148,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 924,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 783,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1535,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 617,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 487,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2302,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 3061,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1072,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2948,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2233,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 594,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 513,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2569,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 858,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 339,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 296,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2369,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2900,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2351,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2925,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 1038,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2124,
      "error_type": "unknown_generation_error",
      "error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
    },
    {
      "id": 2632,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1238,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1555,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 3038,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 462,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1836,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 117,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2771,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2578,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2736,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2051,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1461,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2281,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2985,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1450,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1970,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1302,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1926,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1138,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1761,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1172,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 905,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1928,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 892,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2575,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 3000,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 809,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 246,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1100,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1943,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2216,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2540,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2665,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1131,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 790,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1177,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 3010,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2386,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1162,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1446,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 1435,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 2487,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 456,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
    },
    {
      "id": 708,
      "error_type": "unknown_generation_error",
      "error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
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

### --- id=197 ---

输入文本: His arrest has sparked widespread protests by students , teachers as well as opposition parties .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "His arrest",
      "effect": "widespread protests by students , teachers as well as opposition parties"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1855 ---

输入文本: The petitioner Rohan Mohanty has submitted that junior doctors ’ strike has affected hundreds of patients and thus , they should be directed to join duty immediately .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "junior doctors ’ strike",
      "effect": "has affected hundreds of patients"
    },
    {
      "cause": "has affected hundreds of patients",
      "effect": "they should be directed to join duty immediately"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1427 ---

输入文本: 12th March 2009 03:09 AM HYDERABAD : Expressing sympathy to the family members of Special Police Officer ( SPO ) K Subrahmanyam Raju who died in the attack on Gandhi Bhavan by MRPS activists recently , Pradesh Congress Committee president D Srinivas today announced an ex gratia of Rs 10 lakh to the bereaved family .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the attack on Gandhi Bhavan by MRPS activists recently",
      "effect": "Special Police Officer ( SPO ) K Subrahmanyam Raju who died"
    },
    {
      "cause": "Expressing sympathy to the family members of Special Police Officer ( SPO ) K Subrahmanyam Raju who died in the attack on Gandhi Bhavan by MRPS activists recently",
      "effect": "Pradesh Congress Committee president D Srinivas today announced an ex gratia of Rs 10 lakh to the bereaved family"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=823 ---

输入文本: Thousands of heavily armed troops have paraded through cities in China ’ s troubled far west with officials there vowing a “ thunderous ” anti-terror crackdown after an apparent upsurge in deadly ethnic violence .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "an apparent upsurge in deadly ethnic violence",
      "effect": "Thousands of heavily armed troops have paraded through cities in China ’ s troubled far west with officials there vowing a “ thunderous ” anti-terror crackdown"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=3053 ---

输入文本: Later in the day , vans transporting the students to the Tiruchi airport from Thanjavur were pelted with stones resulting in damage to windshields .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "vans transporting the students to the Tiruchi airport from Thanjavur were pelted with stones",
      "effect": "damage to windshields"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2332 ---

输入文本: This resulted into a clash between the members of the two communities .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "This",
      "effect": "a clash between the members of the two communities"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2609 ---

输入文本: Jitin Das , among them , resorted to fast unto death and died on the 63rd day of his fast ( September 13 ) , he said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Jitin Das , among them , resorted to fast unto death",
      "effect": "died on the 63rd day of his fast ( September 13 )"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1204 ---

输入文本: A large crowd of men holding umbrellas gathered at Freedom Park sports grounds to wait for him to arrive .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to wait for him to arrive",
      "effect": "A large crowd of men holding umbrellas gathered at Freedom Park sports grounds"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=453 ---

输入文本: The driver of the JCB ( earth-mover machine ) has been injured in the clashes , " a police officer said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the clashes",
      "effect": "The driver of the JCB ( earth-mover machine ) has been injured"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2465 ---

输入文本: Association leader Benny said that their members who availed themselves of casual leave on Wednesday as a mark of protest , would continue to boycott duties and organise a 24 - hour satyagraha before the Secretariat on February 20 .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "a mark of protest",
      "effect": "their members who availed themselves of casual leave on Wednesday"
    },
    {
      "cause": "would continue to boycott duties and organise a 24 - hour satyagraha before the Secretariat on February 20",
      "effect": "a mark of protest"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=848 ---

输入文本: Members of the Mamelodi community staged a protest at the High Court Thursday , complaining that he should have been in jail and that his bail should not have been extended .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "complaining that he should have been in jail and that his bail should not have been extended",
      "effect": "Members of the Mamelodi community staged a protest at the High Court Thursday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2271 ---

输入文本: 23rd August 2016 08:17 PM PHULBANI : The communally sensitive Kandhamal district was today put under high security blanket as the members of the VHP assembled there to observe the death anniversary of Swami Laxamananda Saraswati , whose killing had sparked a large scale riot in the area in 2008 .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "the members of the VHP assembled there",
      "effect": "The communally sensitive Kandhamal district was today put under high security blanket"
    },
    {
      "cause": "to observe the death anniversary of Swami Laxamananda Saraswati",
      "effect": "the members of the VHP assembled there"
    },
    {
      "cause": "whose killing",
      "effect": "had sparked a large scale riot in the area in 2008"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1444 ---

输入文本: He said incidents of protest affected voting stations in areas including Mahikeng and Marikana in North West ; Malamulelele , Musina , Mogalakwena , and Northhampton , in Limpopo ; Bushbuckridge in Mpumalanaga ; Khayelitsha in the Western Cape ; Denver , George Koch , and Orange Farm in Gauteng ; Ethekwini and Jozini in KwaZulu-Natal ; Nelson Mandela Bay , Butterworth , and OR Tambo in the Eastern Cape ; Pampierstad in the Northern Cape ; and Maluti-a-Phofung in the Free State .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "incidents of protest",
      "effect": "affected voting stations in areas"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=347 ---

输入文本: But the caste violence that wrecked the lives of over a thousand Dalits earlier this month has forever tainted the image of Dharmapuri district as a former Naxal stronghold that , even a decade ago , had no place for caste or class differences .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the caste violence",
      "effect": "wrecked the lives of over a thousand Dalits earlier this month"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=7 ---

输入文本: Protesters are angry at the police ’ s slow response to the attack in Yuen Long and their pursuit of the case .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the police ’ s slow response to the attack in Yuen Long and their pursuit of the case",
      "effect": "Protesters are angry"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=473 ---

输入文本: The police claimed they were killed while trying to blow up the local bus station .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "trying to blow up the local bus station",
      "effect": "The police claimed they were killed"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=471 ---

输入文本: Police statistics say 16 extremists died in 18 exchanges of fire in just the six weeks from 14 December 2004 .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "18 exchanges of fire in just the six weeks from 14 December 2004",
      "effect": "16 extremists died"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=100 ---

输入文本: All the 417 guards in the suburban section refused to work extra hours in protest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "in protest",
      "effect": "All the 417 guards in the suburban section refused to work extra hours"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=669 ---

输入文本: Stating that the Telangana agitation had spread to the nook and corner of the region because of the fast taken up by TRS president K. Chandrasekhar Rao last year , Mr. Kodandaram said that change of guard in the government would not help in stalling the ongoing agitation for separate State .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the fast taken up by TRS president K. Chandrasekhar Rao last year",
      "effect": "the Telangana agitation had spread to the nook and corner of the region"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1707 ---

输入文本: According to police , one person was arrested for public violence on Saturday after about 70 protesting residents stoned a car and attempted to blockade roads in Goedgevonden .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "about 70 protesting residents stoned a car and attempted to blockade roads in Goedgevonden",
      "effect": "one person was arrested for public violence on Saturday"
    },
    {
      "cause": "public violence",
      "effect": "one person was arrested"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1290 ---

输入文本: The 1966 riots , which were prompted by a 50 per cent increase in cross-harbour ferry fares , took place against the backdrop of a bad economy and widening gap between the government and the people .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "a 50 per cent increase in cross-harbour ferry fares",
      "effect": "The 1966 riots"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2447 ---

输入文本: Party Vice-President Ram Kishore Singh threatened to “ put him ( Modi ) behind bars ” , because following the Muzaffarnagar riots , the state government had received IB alerts on possible communal unrest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the state government had received IB alerts on possible communal unrest",
      "effect": "Party Vice-President Ram Kishore Singh threatened to “ put him ( Modi ) behind bars"
    },
    {
      "cause": "the Muzaffarnagar riots",
      "effect": "the state government had received IB alerts on possible communal unrest"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=958 ---

输入文本: It claimed that during the attack a five-vehicle convoy of 6th Dogra Regiment was " assaulted " at Tengnoupal-New Somtal Road in Chandel district of Manipur .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the attack",
      "effect": "a five-vehicle convoy of 6th Dogra Regiment was \" assaulted \" at Tengnoupal-New Somtal Road in Chandel district of Manipur"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2035 ---

输入文本: Anantapur : Accused ‘ paraded ' half-naked by CI September 17 , 2010 00:00 IST Eight members of handloom weavers ' community including local councillor Pola Venkatanarayana were paraded half-naked by Circle Inspector Venugopala Reddy for allegedly beating up and threatening one B. Ramana , member of the local weavers enforcement committee .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "allegedly beating up and threatening one B. Ramana , member of the local weavers enforcement committee",
      "effect": "Eight members of handloom weavers ' community including local councillor Pola Venkatanarayana were paraded half-naked by Circle Inspector Venugopala Reddy"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=308 ---

输入文本: Some police personnel intervened and urged them to give up their protest - but to no avail .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Some police personnel intervened",
      "effect": "urged them to give up their protest"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1442 ---

输入文本: While the Congress members walked out in protest , the BJP members continued the dharna in the Well till the House was adjourned for the day after the presentation of the Budget .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "in protest",
      "effect": "the Congress members walked out"
    },
    {
      "cause": "the House was adjourned for the day after the presentation of the Budget",
      "effect": "the BJP members continued the dharna in the Well"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1059 ---

输入文本: MYSURU : Tension prevails as Falcon Tyres employees block KRS Road March 03 , 2016 00:00 IST Tension prevailed on the KRS Road for sometime on Wednesday after scores of Falcon Tyres employees staged a demonstration against the factory management demanding immediate settlement of their pending wages .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "Falcon Tyres employees block KRS Road",
      "effect": "Tension prevails"
    },
    {
      "cause": "scores of Falcon Tyres employees staged a demonstration against the factory management",
      "effect": "Tension prevailed on the KRS Road for sometime on Wednesday"
    },
    {
      "cause": "demanding immediate settlement of their pending wages",
      "effect": "scores of Falcon Tyres employees staged a demonstration against the factory management"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1163 ---

输入文本: The party was protesting the arrest of its president N. Chandrababu Naidu and other leaders by Maharashtra police when they tried to visit Babli project .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the arrest of its president N. Chandrababu Naidu and other leaders by Maharashtra police",
      "effect": "The party was protesting"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=353 ---

输入文本: In 2009 , riots broke out in the capital , Urumqui , and in their wake , mass arrests were made and many Uyghurs were imprisoned or “ disappeared ” .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "riots broke out in the capital",
      "effect": "mass arrests were made and many Uyghurs were imprisoned or “ disappeared ”"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=722 ---

输入文本: By noon , veteran BJP leader O. Rajagopal took over the fast as Krishnadas had to go for campaigning .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Krishnadas had to go for campaigning",
      "effect": "veteran BJP leader O. Rajagopal took over the fast"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=443 ---

输入文本: The bombing created panic among villagers .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "The bombing",
      "effect": "created panic among villagers"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2450 ---

输入文本: They alleged that the police tried to intimidate religious leaders and pressured them to withdraw the bandh call and had issued notices to them saying that if there was any untoward incident during the bandh they would be held responsible for it .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "there was any untoward incident during the bandh",
      "effect": "they would be held responsible for it"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=512 ---

输入文本: " An elaborate security arrangement have been made for the CPI ( M-L ) rally in Patna following three more bombs recovered in and around Gandhi Maidan Tuesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "three more bombs recovered in and around Gandhi Maidan Tuesday",
      "effect": "An elaborate security arrangement have been made for the CPI ( M-L ) rally in Patna"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=886 ---

输入文本: Police took into custody fifteen activists for blocking the traffic in Visakhapatnam .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "blocking the traffic in Visakhapatnam",
      "effect": "Police took into custody fifteen activists"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1720 ---

输入文本: The wife of the house owner , Taja , died in the shootout between the militants and the police .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "in the shootout between the militants and the police",
      "effect": "The wife of the house owner , Taja , died"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1778 ---

输入文本: Addressing a rally here to protest against the offensive , he said , " Tamils should be given equal rights and powers in the affairs of Sri Lanka .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to protest against the offensive",
      "effect": "a rally here"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1369 ---

输入文本: On New Year 's Day , seven days after Qian 's death , thousands of residents of surrounding villages gathered to mourn but were stopped by hundreds of police .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to mourn",
      "effect": "thousands of residents of surrounding villages gathered"
    },
    {
      "cause": "On New Year 's Day , seven days after Qian 's death",
      "effect": "to mourn"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2790 ---

输入文本: `` In recent weeks , residents invaded land in the area and to curb the mushrooming of structures on the land , the municipality obtained a court order to remove the land invaders .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to curb the mushrooming of structures on the land",
      "effect": "the municipality obtained a court order to remove the land invaders"
    },
    {
      "cause": "to remove the land invaders",
      "effect": "the municipality obtained a court order"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1216 ---

输入文本: Subsequently , more constituents , in a show of solidarity , joined and thus the protest was postponed to February 28 , said P .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "more constituents , in a show of solidarity , joined",
      "effect": "the protest was postponed to February 28"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=612 ---

输入文本: Maruti 's Manesar plant closed for 2nd day - Indian Express Agencies , Agencies : Manesar , Fri Jul 20 2012 , 11:11 hrs Maruti Suzuki India Friday said its plant was remain closed for the second day after the violence on Wednesday in which one senior company official was killed .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the violence on Wednesday in which one senior company official was killed",
      "effect": "its plant was remain closed for the second day"
    },
    {
      "cause": "the violence on Wednesday",
      "effect": "one senior company official was killed"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=488 ---

输入文本: ANDHRA PRADESH Congress office in Vidyut Bhavan flayed June 17 , 2007 00:00 IST KADAPA : Members of the United Electricity Employees Union staged dharna before the Collectorate on Saturday decrying allotment of one acre of land on Vidyut Bhavan premises to the Congress office .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "decrying allotment of one acre of land on Vidyut Bhavan premises to the Congress office",
      "effect": "Members of the United Electricity Employees Union staged dharna before the Collectorate on Saturday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2643 ---

输入文本: Militants also killed two members of a policeman 's family and wounded two others when they barged into a house in the border district of Poonch and opened fire .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "they barged into a house in the border district of Poonch and opened fire",
      "effect": "Militants also killed two members of a policeman 's family and wounded two others"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2746 ---

输入文本: For instance , a few years ago , MNS workers disrupted a railway recruitment examination because some candidates were non-Marathis .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "some candidates were non-Marathis",
      "effect": "MNS workers disrupted a railway recruitment examination"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2127 ---

输入文本: When we got up to go home the police acted violently towards us even though our protest was peaceful .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "to go home",
      "effect": "we got up"
    },
    {
      "cause": "we got up",
      "effect": "the police acted violently towards us"
    },
    {
      "cause": "our protest was peaceful",
      "effect": "the police acted violently towards us"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=179 ---

输入文本: SANGAREDDY : Shortage of urea : farmers protest in Sangareddy

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Shortage of urea",
      "effect": "farmers protest in Sangareddy"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=150 ---

输入文本: “ If peaceful marches that disrupt the road for an afternoon or so don ’ t work , maybe it spills over to blockading more roads , maybe for long .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "peaceful marches",
      "effect": "that disrupt the road for an afternoon or so"
    },
    {
      "cause": "peaceful marches that disrupt the road for an afternoon or so don ’ t work",
      "effect": "maybe it spills over to blockading more roads , maybe for long"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1322 ---

输入文本: Posted : Tue Apr 21 1998 IST KARIMNAGAR , April 20 : Armed reserve and civil policemen revolted and unleashed a reign of terror in the town last night to protest against the transfer of superintendent of police Umesh Chandra , further eroding the image of the police which touched an all-time low due to several incidents recently .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "to protest against the transfer of superintendent of police Umesh Chandra",
      "effect": "Armed reserve and civil policemen revolted and unleashed a reign of terror in the town last night"
    },
    {
      "cause": "Armed reserve and civil policemen revolted and unleashed a reign of terror in the town last night to protest against the transfer of superintendent of police Umesh Chandra",
      "effect": "further eroding the image of the police"
    },
    {
      "cause": "several incidents recently",
      "effect": "image of the police which touched an all-time low"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2402 ---

输入文本: KARNATAKA Action sought March 12 , 2009 00:00 IST Bijapur : Members of Mahila Jana Sangha and Dalit Sangharsha Samiti picketed the office of the Superintendent of Police demanding action against women police officials who allegedly harassed Savitri Chalwadi in Manguli village of the district on Tuesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "demanding action against women police officials",
      "effect": "Members of Mahila Jana Sangha and Dalit Sangharsha Samiti picketed the office of the Superintendent of Police"
    },
    {
      "cause": "who allegedly harassed Savitri Chalwadi in Manguli village of the district on Tuesday",
      "effect": "demanding action against women police officials"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2838 ---

输入文本: India stalled cricketing ties in the aftermath of 2008 Mumbai terrorist attack .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "2008 Mumbai terrorist attack",
      "effect": "India stalled cricketing ties"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2563 ---

输入文本: Will the unprecedented protests embolden them to fight for their beliefs in future , or convince them that resistance to Beijing ’ s will is futile ?

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the unprecedented protests",
      "effect": "embolden them to fight for their beliefs in future , or convince them that resistance to Beijing ’ s will is futile"
    },
    {
      "cause": "their beliefs in future",
      "effect": "embolden them to fight"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=986 ---

输入文本: KOLLAM : Neglect of Kollam alleged August 06 , 2011 00:00 IST UDF government has declared war on people : Chandrappan The district unit of the Left Democratic Front ( LDF ) staged a dharna at the Press Club Maidan here on Friday to register its protest against the alleged neglect of the district in the revised Budget presented by Finance Minister K.M. Mani .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to register its protest against the alleged neglect of the district in the revised Budget presented by Finance Minister K.M. Mani",
      "effect": "The district unit of the Left Democratic Front ( LDF ) staged a dharna at the Press Club Maidan here on Friday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=3071 ---

输入文本: She said the group had to be dispersed after the local police station was attacked by high school pupils , injuring three police officers , on Monday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the local police station was attacked by high school pupils",
      "effect": "the group had to be dispersed"
    },
    {
      "cause": "the local police station was attacked by high school pupils",
      "effect": "injuring three police officers"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2067 ---

输入文本: On January 23 , Amcu members at Lonmin , Amplats , and Implats downed tools , demanding a monthly basic salary of R12,500 .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding a monthly basic salary of R12,500",
      "effect": "On January 23 , Amcu members at Lonmin , Amplats , and Implats downed tools"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=572 ---

输入文本: VP takes his protest to Kalam - Indian Express Express News Service , Express News Service : New Delhi , September 19 , Wed Sep 20 2006 , 01:07 hrs Former prime minister VP Singh today met President APJ Kalam to plead for his intervention in what he called a case of ' land grabbing ' in Uttar Pradesh .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to plead for his intervention in what he called a case of ' land grabbing ' in Uttar Pradesh",
      "effect": "Former prime minister VP Singh today met President APJ Kalam"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2056 ---

输入文本: " The militants fired indiscriminately on at least three locations , killing one army soldier and injuring two more , " police spokesperson A. Das told IANS .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "The militants fired indiscriminately on at least three locations",
      "effect": "killing one army soldier and injuring two more"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2647 ---

输入文本: The station house officer of the Farah police station Santosh Yadav and the Superintendent of Police ( City ) Mathura Mukul Dwivedi were killed when activists of Swadheen Bharat Subhash Sena ( SBSS ) opened fire at the police party that attempted to evict it from Jawahar Park late on Thursday evening .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "activists of Swadheen Bharat Subhash Sena ( SBSS ) opened fire at the police party that attempted to evict it from Jawahar Park late on Thursday evening",
      "effect": "The station house officer of the Farah police station Santosh Yadav and the Superintendent of Police ( City ) Mathura Mukul Dwivedi were killed"
    },
    {
      "cause": "that attempted to evict it from Jawahar Park late on Thursday evening",
      "effect": "activists of Swadheen Bharat Subhash Sena ( SBSS ) opened fire at the police party"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=434 ---

输入文本: The traffic on Rohtak-Jhajjar highway remained disrupted prompting police to divert vehicles to other routes .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "The traffic on Rohtak-Jhajjar highway remained disrupted",
      "effect": "prompting police to divert vehicles to other routes"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1998 ---

输入文本: The ANC in KwaZulu-Natal strongly condemns the misbehaviour of IFP members who interrupted our campaign trail led by ANC Deputy President Jacob Zuma at Dokodweni and Mandeni on the north coast today .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "who interrupted our campaign trail led by ANC Deputy President Jacob Zuma at Dokodweni and Mandeni on the north coast today",
      "effect": "The ANC in KwaZulu-Natal strongly condemns the misbehaviour of IFP members"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1621 ---

输入文本: Feb 15 , 2010 : Around 100 Maoists storm a police camp in Silda , West Bengal , killing 24 policemen and looting arms .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Around 100 Maoists storm a police camp in Silda , West Bengal",
      "effect": "killing 24 policemen and looting arms ."
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2367 ---

输入文本: The Maoists have abducted the TDP men demanding that the Andhra Pradesh government stop bauxite mining in the agency areas of the district .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding that the Andhra Pradesh government stop bauxite mining in the agency areas of the district",
      "effect": "The Maoists have abducted the TDP men"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1056 ---

输入文本: Tirupur : Telecom employees stage protest June 22 , 2015 00:00 IST Alleging that the deficiencies in operational infrastructure and staff shortage in telephone exchanges in Tirupur and nearby areas are not getting addressed , the BSNL Employees Union members staged an agitation here .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Alleging that the deficiencies in operational infrastructure and staff shortage in telephone exchanges in Tirupur and nearby areas are not getting addressed",
      "effect": "the BSNL Employees Union members staged an agitation here"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2557 ---

输入文本: Fasting Jagan denied mulakats 27th August 2013 11:23 AM The indefinite fast of YSR Congress chief YS Jaganmohan Reddy in protest against state division continued on the second day on Monday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "against state division",
      "effect": "The indefinite fast of YSR Congress chief YS Jaganmohan Reddy in protest"
    },
    {
      "cause": "protest against state division",
      "effect": "The indefinite fast of YSR Congress chief YS Jaganmohan Reddy"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2763 ---

输入文本: She claimed that the police showed maximum restraint but lost temper when some of their colleagues got hurt during the stone-pelting and rataliated .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "and rataliated",
      "effect": "She claimed that the police showed maximum restraint but lost temper when some of their colleagues got hurt during the stone-pelting"
    },
    {
      "cause": "some of their colleagues got hurt",
      "effect": "lost temper"
    },
    {
      "cause": "the stone-pelting",
      "effect": "some of their colleagues got hurt"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1512 ---

输入文本: " I had to walk half the distance after some people forcibly stopped the auto I was travelling in , " said a commuter .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "some people forcibly stopped the auto I was travelling in",
      "effect": "I had to walk half the distance"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1536 ---

输入文本: On Tuesday , 29 truckers were arrested in the Johannesburg city centre after violent clashes with the police .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "violent clashes with the police",
      "effect": "On Tuesday , 29 truckers were arrested in the Johannesburg city centre"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=27 ---

输入文本: Akram was on the radar of the National Investigation Agency ( NIA ) as he is believed to have arranged explosives and planter for the blast .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "he is believed to have arranged explosives and planter for the blast",
      "effect": "Akram was on the radar of the National Investigation Agency ( NIA )"
    },
    {
      "cause": "the blast",
      "effect": "arranged explosives and planter"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1826 ---

输入文本: Simon Blore , director , Leadarchitects Limited Angered by anti-Occupy Central march I have followed with dismay the all-too apparent manipulation of gullible people being fed propaganda by pro-Beijing loyalists about the Occupy Central initiative for a freer election process .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "anti-Occupy Central march",
      "effect": "Angered"
    },
    {
      "cause": "Angered by anti-Occupy Central march",
      "effect": "I have followed with dismay the all-too apparent manipulation of gullible people being fed propaganda by pro-Beijing loyalists about the Occupy Central initiative for a freer election process"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=355 ---

输入文本: Four students were injured when police fired rubber bullets during a protest on the campus of the University of the North West in Mafikeng on Monday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "police fired rubber bullets during a protest on the campus of the University of the North West in Mafikeng on Monday",
      "effect": "Four students were injured"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2241 ---

输入文本: “ The JAC has decided to go on work to rule in any given month if the salaries were not paid on first day of that month .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the salaries were not paid on first day of that month",
      "effect": "The JAC has decided to go on work to rule in any given month"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1253 ---

输入文本: Militants fired a rocket at the headquarters of 84th battalion of BSF in Sopore in North Kashmir late last night which missed its target and caused no loss of life or damage to property , police said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Militants fired a rocket at the headquarters of 84th battalion of BSF in Sopore in North Kashmir late last night which missed its target",
      "effect": "no loss of life or damage to property"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2017 ---

输入文本: Scuffles broke out around noon when police attempted to seize their banners .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "police attempted to seize their banners",
      "effect": "Scuffles broke out around noon"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2567 ---

输入文本: Millions on the mainland took part in the pro-reform protests of 1989 which began in Tiananmen Square , but after the bloody crackdown , fear and economic inducements ensured they turned away from politics .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "fear and economic inducements",
      "effect": "they turned away from politics"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=207 ---

输入文本: The employees also served an ultimatum to the government that unless they shelved the decision on privatisation , they would go ahead with their indefinite strike plan and intensify their ongoing agitation .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "they shelved the decision on privatisation",
      "effect": "they would go ahead with their indefinite strike plan and intensify their ongoing agitation"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1654 ---

输入文本: Hong Kong police have fired teargas at demonstrators and moved to disperse crowds after protesters stormed the legislative council building and raised the territory ’ s former colonial flag on the 22nd anniversary of its handover to China .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "protesters stormed the legislative council building and raised the territory ’ s former colonial flag on the 22nd anniversary of its handover to China",
      "effect": "Hong Kong police have fired teargas at demonstrators and moved to disperse crowds"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=230 ---

输入文本: TIRUCHI : Residents raise black flag atop their houses May 06 , 2016 00:00 IST Residents of Quaide Milleth Nagar near Ariyamangalam on Thursday hoisted black flags atop their houses demanding basic amenities and threatened to boycott the Assembly election if their demands were not conceded .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "demanding basic amenities",
      "effect": "Residents of Quaide Milleth Nagar near Ariyamangalam on Thursday hoisted black flags atop their houses"
    },
    {
      "cause": "their demands were not conceded",
      "effect": "threatened to boycott the Assembly election"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2878 ---

输入文本: Sena Flays CM for Keeping Mum While Vidarbha Flag Was Hoisted 03rd May 2016 04:32 PM MUMBAI : Ruling alliance partner Shiv Sena today flayed Maharashtra Chief Minister Devendra Fadnavis for keeping mum when a flag of a separate Vidarbha state was recently hoisted in Nagpur on Maharashtra Day .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Keeping Mum While Vidarbha Flag Was Hoisted",
      "effect": "Sena Flays CM"
    },
    {
      "cause": "keeping mum when a flag of a separate Vidarbha state was recently hoisted in Nagpur on Maharashtra Day",
      "effect": "Ruling alliance partner Shiv Sena today flayed Maharashtra Chief Minister Devendra Fadnavis"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1625 ---

输入文本: June 23 , 2009 : A group of motorcycle-borne armed Maoists open fire on Lakhisarai district court premises in Bihar to free four of their men .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to free four of their men",
      "effect": "A group of motorcycle-borne armed Maoists open fire on Lakhisarai district court premises in Bihar"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2999 ---

输入文本: Wild , irresponsible and most unfounded allegations , by certain sections of the Sikh community , about my involvement in the inciting of violence against them during the most unfortunate Sikh riots of 1984 , soon after the death of Shrimati Indira Gandhi , the then prime minister of India , has caused me acute agony .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Wild , irresponsible and most unfounded allegations , by certain sections of the Sikh community , about my involvement in the inciting of violence against them during the most unfortunate Sikh riots of 1984 , soon after the death of Shrimati Indira Gandhi , the then prime minister of India",
      "effect": "has caused me acute agony"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2724 ---

输入文本: May 08 , 2010 00:00 IST Over 470 pourakarmikas are agitating for release of wages

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "release of wages",
      "effect": "Over 470 pourakarmikas are agitating"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1351 ---

输入文本: KARNATAKA Protest July 06 , 2007 00:00 IST Gulbarga : Dalit Sena activists laid siege to the zilla panchayat office in Gulbarga on Thursday in protest against the decision to close down some hostels for Scheduled Caste / Scheduled Tribe students in the district .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "in protest against the decision to close down some hostels for Scheduled Caste / Scheduled Tribe students in the district",
      "effect": "Dalit Sena activists laid siege to the zilla panchayat office in Gulbarga on Thursday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=518 ---

输入文本: One of the journalists overheard the group saying they would necklace one of the reporters to get media coverage .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to get media coverage",
      "effect": "they would necklace one of the reporters"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1357 ---

输入文本: With little option but to obey the Supreme Court directive , Karnataka started releasing water from September 29 , which has led to daily protests in Bangalore and in the Cauvery basin districts .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to obey the Supreme Court directive",
      "effect": "Karnataka started releasing water from September 29"
    },
    {
      "cause": "Karnataka started releasing water from September 29",
      "effect": "daily protests in Bangalore and in the Cauvery basin districts"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=975 ---

输入文本: If an agreement was not reached the protests would continue , Gumede said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "an agreement was not reached",
      "effect": "the protests would continue"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1893 ---

输入文本: The Left , the BJP and a few other parties have been disrupting Parliament proceedings for the past two days over the alleged involvement of the Maoists in organising Trinamool Congress rally at Lalgarh in West Bengal .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the alleged involvement of the Maoists in organising Trinamool Congress rally at Lalgarh in West Bengal",
      "effect": "The Left , the BJP and a few other parties have been disrupting Parliament proceedings for the past two days"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=3018 ---

输入文本: A group , comprising leaders of the Communist Party of India ( Marxist ) and the Democratic Youth Federation of India , had roughed up a journalist who had put out a report to that effect .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "had put out a report to that effect",
      "effect": "A group , comprising leaders of the Communist Party of India ( Marxist ) and the Democratic Youth Federation of India , had roughed up a journalist"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2751 ---

输入文本: Striking workers will not return to work unless health workers who were fired for taking part in salary protest actions are reinstated , the National Education , Health and Allied Workers Union ( Nehawu ) said in Bloemfontein on Wednesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "health workers who were fired for taking part in salary protest actions are reinstated",
      "effect": "Striking workers will not return to work"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1920 ---

输入文本: Freezing weather conditions at ANC PE Siyanqoba Rally Raahil Sain PORT ELIZABETH , July 23 ( ANA ) - African National Congress supporters streamed into the Dan Qeqe Stadium in Zwide , Port Elizabeth , in freezing weather conditions and rain for the ANC 's August 3 municipal elections Siyanqoba rally on Saturday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "for the ANC 's August 3 municipal elections Siyanqoba rally on Saturday",
      "effect": "African National Congress supporters streamed into the Dan Qeqe Stadium in Zwide , Port Elizabeth , in freezing weather conditions and rain"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2611 ---

输入文本: " Based on specific inputs , security forces cordoned off a house and that resulted in an encounter with the militant first opening fire on the security team , " Kokrajhar police chief P.K. Dutta said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "security forces cordoned off a house",
      "effect": "an encounter with the militant first opening fire on the security team"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=499 ---

输入文本: On August 16 , 2012 , police shot dead 34 people , almost all striking mineworkers , while trying to disperse and disarm them .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "trying to disperse and disarm them",
      "effect": "police shot dead 34 people , almost all striking mineworkers"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1988 ---

输入文本: KERALA Private bus strike total in city August 14 , 2008 00:00 IST DIFFICULT RIDE : Commuters had a hard time on the first day of the private bus strike in the city on Wednesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the private bus strike in the city on Wednesday",
      "effect": "Commuters had a hard time on the first day"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1367 ---

输入文本: ' He refused a two million ( HK $ 2.34 million ) yuan bribe and pretty girls offered by authorities who wanted him to stop petitioning , ' said another villager .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "who wanted him to stop petitioning",
      "effect": "a two million ( HK $ 2.34 million ) yuan bribe and pretty girls offered by authorities"
    },
    {
      "cause": "authorities who wanted him to stop petitioning",
      "effect": "a two million ( HK $ 2.34 million ) yuan bribe and pretty girls offered"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2455 ---

输入文本: In reply to the argument of the defence counsel that the UDF used the murder of Chandrasekharan for political gain by blaming CPM for the killing , Rema told the court that this was not right .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "political gain by blaming CPM for the killing",
      "effect": "the UDF used the murder of Chandrasekharan"
    },
    {
      "cause": "the UDF used the murder of Chandrasekharan for political gain",
      "effect": "blaming CPM for the killing"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2377 ---

输入文本: The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday to condemn what it called a “ concerted attack on Hindu leaders in the state . ” Ramesh , the state BJP unit ’ s general secretary and a charted accountant by profession , was murdered by assailants in Salem while he was on his way back home after visiting the party office on Friday evening .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to condemn what it called a “ concerted attack on Hindu leaders in the state",
      "effect": "The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday"
    },
    {
      "cause": "visiting the party office on Friday evening",
      "effect": "he was on his way back home"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=676 ---

输入文本: The enthusiastic plans of the freedom fighters , satyagrahis , revolutionaries and soldiers for grand celebrations began to ebb right after the Mumbai attacks , with Subhash Chandra Bose and Bhagat Singh leading the agitation to boycott the celebrations .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Subhash Chandra Bose and Bhagat Singh leading the agitation to boycott the celebrations",
      "effect": "The enthusiastic plans of the freedom fighters , satyagrahis , revolutionaries and soldiers for grand celebrations began to ebb right after the Mumbai attacks"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=406 ---

输入文本: Dissatisfied with the package , workers staged an all-nigh sit-in .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Dissatisfied with the package",
      "effect": "workers staged an all-nigh sit-in"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2712 ---

输入文本: The protesters – many of whom were wearing black T-shirts and hard hats and were armed with shields made from boards of wood and surfboards , as well as hiking sticks and rods – retaliated by throwing umbrellas and water bottles .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "throwing umbrellas and water bottles",
      "effect": "The protesters – many of whom were wearing black T-shirts and hard hats and were armed with shields made from boards of wood and surfboards , as well as hiking sticks and rods – retaliated"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2718 ---

输入文本: Hong Kong ’ s hospital authority said 17 people had been hospitalised following the clashes , including two who were in serious condition .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the clashes",
      "effect": "17 people had been hospitalised"
    },
    {
      "cause": "the clashes",
      "effect": "including two who were in serious condition"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1575 ---

输入文本: Addressing a massive gathering of party workers and sympathisers from in and around the city at the ‘ maha dharna ' organised in the vicinity of the Collector 's office here on Monday , Mr. Naidu said the Rosaiah Government has failed on all fronts and neglected agriculture as reflected in the acute shortage of fertilizer faced by the farmers .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the Rosaiah Government has failed on all fronts and neglected agriculture",
      "effect": "the acute shortage of fertilizer faced by the farmers"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1817 ---

输入文本: Five people died on the spot in the second blast and over 50 were injured , several critically .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the second blast",
      "effect": "Five people died on the spot"
    },
    {
      "cause": "the second blast",
      "effect": "and over 50 were injured , several critically"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=302 ---

输入文本: More violence in TN district Posted : Wed Jun 25 1997 IST RAJAPALAYAM , June 23 : In continuing violence in TN 's Kamarajar district , one person was stabbed and buses being attacked .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "In continuing violence in TN 's Kamarajar district",
      "effect": "one person was stabbed and buses being attacked"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2594 ---

输入文本: The dawn-to-dusk shutdown evoked total response in Bihar , upsetting Lalu-Rabri rival Nitish Kumar as well as the Bharatiya Janata Party ( BJP ) and the Congress , which is trying for a revival in the state .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "The dawn-to-dusk shutdown",
      "effect": "total response in Bihar"
    },
    {
      "cause": "total response in Bihar",
      "effect": "upsetting Lalu-Rabri rival Nitish Kumar as well as the Bharatiya Janata Party ( BJP ) and the Congress"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1062 ---

输入文本: Later in the day , the entire opposition - TDP , CPI , CPI(M) and PDF staged a walk out when government turned down their demand to adopt a resolution urging Centre to withdraw recent hike in fuel prices and the decision on deregulation of petrol .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "government turned down their demand to adopt a resolution urging Centre to withdraw recent hike in fuel prices and the decision on deregulation of petrol",
      "effect": "the entire opposition - TDP , CPI , CPI(M) and PDF staged a walk out"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2384 ---

输入文本: These attacks and killings may be aimed at instilling fear in the minds of the people in general and of our party workers in particular , ” the statement read and demanded a Special Investigation Team to go into each of the incidents .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "may be aimed at instilling fear in the minds of the people in general and of our party workers in particular",
      "effect": "These attacks and killings"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1281 ---

输入文本: Truckers put govt on notice 08th January 2009 03:57 AM CHENNAI : With the national-level truckers ’ strike called by the All-India Motor Transport Congress ( AIMTC ) demanding immediate reduction of diesel prices entering the third day on Wednesday , representatives of the striking truckers have issued an ultimatum to the government to act before Thursday midnight to resolve the issue or face severe consequences .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "demanding immediate reduction of diesel prices",
      "effect": "the national-level truckers ’ strike called by the All-India Motor Transport Congress ( AIMTC )"
    },
    {
      "cause": "the national-level truckers ’ strike called by the All-India Motor Transport Congress ( AIMTC ) demanding immediate reduction of diesel prices entering the third day on Wednesday",
      "effect": "representatives of the striking truckers have issued an ultimatum to the government to act before Thursday midnight to resolve the issue or face severe consequences"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2341 ---

输入文本: KARIMNAGAR : TDP rasta roko against fuel price hike June 28 , 2010 00:00 IST The TDP district unit leaders staged a rasta roko in front of the RTC bus station complex here on Sunday in protest against the fuel price hike .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "against the fuel price hike",
      "effect": "The TDP district unit leaders staged a rasta roko in front of the RTC bus station complex here on Sunday in protest"
    },
    {
      "cause": "in protest against the fuel price hike",
      "effect": "The TDP district unit leaders staged a rasta roko in front of the RTC bus station complex here on Sunday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1189 ---

输入文本: About 120 PG students are on strike demanding payment of their stipend arrears .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding payment of their stipend arrears",
      "effect": "About 120 PG students are on strike"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1517 ---

输入文本: The participating unions called off the daylong token strike after 5 pm but Kshirsagar said that they would enforce it again on Monday if the traffic police did not ease pressure on drivers .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the traffic police did not ease pressure on drivers",
      "effect": "they would enforce it again on Monday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1093 ---

输入文本: Hundreds arrested for blocking Hyderabad-Bangalore highway 21st March 2013 05:43 PM Police arrested hundreds of pro-Telangana protestors for blocking traffic on the Hyderabad-Bangalore national highway in Telangana region of Andhra Pradesh Thursday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "blocking traffic on the Hyderabad-Bangalore national highway in Telangana region of Andhra Pradesh Thursday",
      "effect": "Police arrested hundreds of pro-Telangana protestors"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1551 ---

输入文本: Upset with Probe into AIADMK Man 's Murder , Wife Stages Stir

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Probe into AIADMK Man 's Murder",
      "effect": "Upset"
    },
    {
      "cause": "Upset with Probe into AIADMK Man 's Murder",
      "effect": "Wife Stages Stir"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1967 ---

输入文本: There was also allegation that some of the Congress workers , who came to interrupt the fest , were in an inebriated state .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "were in an inebriated state",
      "effect": "some of the Congress workers , who came to interrupt the fest"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=3045 ---

输入文本: Muslims across the city of lakes , still haunted by memories of the 2002 Gujarat riots , say they will not vote for someone who was unable to stop a massacre of ‘ innocent people ’ in his state .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Muslims across the city of lakes , still haunted by memories of the 2002 Gujarat riots",
      "effect": "they will not vote for someone who was unable to stop a massacre of ‘ innocent people ’ in his state"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1860 ---

输入文本: The DGP said steps have been taken to prevent the escalation of violence .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to prevent the escalation of violence",
      "effect": "steps have been taken"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1460 ---

输入文本: The Bhim Army and other Dalit groups were refused permission to organise a rally against atrocities on May 9 sparking off violence and vandalism , with several vehicles and buses burnt .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "against atrocities on May 9",
      "effect": "organise a rally"
    },
    {
      "cause": "The Bhim Army and other Dalit groups were refused permission to organise a rally against atrocities on May 9",
      "effect": "violence and vandalism , with several vehicles and buses burnt"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=3013 ---

输入文本: Led by former Minister Mandava Venkateswar Rao , MLA ( Nizamabad Urban ) MLAs Annapoornamma and Hanmanth Shinde and MLCs V.G. Goud and A. Narsa Reddy held protest demonstration in front of the office of Superintending Engineer demanding rectification of the situation within two days .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding rectification of the situation within two days",
      "effect": "MLA ( Nizamabad Urban ) MLAs Annapoornamma and Hanmanth Shinde and MLCs V.G. Goud and A. Narsa Reddy held protest demonstration in front of the office of Superintending Engineer"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1905 ---

输入文本: April 26 : Three policemen and two CPI-Maoist cadres were killed in an encounter in Dumka , Jharkhand .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "an encounter in Dumka , Jharkhand .",
      "effect": "Three policemen and two CPI-Maoist cadres were killed"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2626 ---

输入文本: Twin Bomb Blasts Injures Four in Guwahati 's Fancy Bazar Area : Police 05th December 2015 04:37 PM A screen grab of the fancy Bazaar area from Google Maps GUWAHATI : Two low intensity blasts rocked the busy commercial Fancy Bazaar area in Guwahati Saturday afternoon , injuring four persons .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Twin Bomb Blasts",
      "effect": "Injures Four in Guwahati 's Fancy Bazar Area"
    },
    {
      "cause": "Two low intensity blasts rocked the busy commercial Fancy Bazaar area in Guwahati Saturday afternoon",
      "effect": "injuring four persons"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2503 ---

输入文本: They then took the workers , who were sleeping there , including the JCB and tractor drivers , to about one km , fearing police retaliation .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "fearing police retaliation",
      "effect": "They then took the workers , who were sleeping there , including the JCB and tractor drivers , to about one km"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1570 ---

输入文本: The protests started on Tuesday , with residents demanding better service delivery and housing .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "residents demanding better service delivery and housing",
      "effect": "The protests started on Tuesday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=181 ---

输入文本: While earlier it was the turn of Telangana Rashtra Samithi ( TRS ) to participate in protests in support to farmers , on Monday it was the Telugu Desam .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "in support to farmers",
      "effect": "Telangana Rashtra Samithi ( TRS ) to participate in protests"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2539 ---

输入文本: City police have now constituted teams to carry out regular inspection at malls following the blasts .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to carry out regular inspection at malls",
      "effect": "City police have now constituted teams"
    },
    {
      "cause": "the blasts",
      "effect": "to carry out regular inspection at malls"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2726 ---

输入文本: The protests , which began over a controversial extradition bill , have evolved to take in other demands , including a police inquiry into the violence in Yuen Long last week .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to take in other demands",
      "effect": "The protests , which began over a controversial extradition bill , have evolved"
    },
    {
      "cause": "a controversial extradition bill",
      "effect": "The protests , which began"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=962 ---

输入文本: Christians flay Commission ’ s report 21st February 2011 04:25 AM MANGALORE : Thousands of Christians took out a silent march from Ambedkar ( Jyothi ) Circle to Nehru Maidan on Sunday by wrapping their mouth with black cloth and holding black flags to oppose Justice Somasekhara Commission ’ s report on church attacks .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to oppose Justice Somasekhara Commission ’ s report on church attacks",
      "effect": "Thousands of Christians took out a silent march from Ambedkar ( Jyothi ) Circle to Nehru Maidan on Sunday by wrapping their mouth with black cloth and holding black flags"
    },
    {
      "cause": "Thousands of Christians took out a silent march from Ambedkar ( Jyothi ) Circle to Nehru Maidan on Sunday",
      "effect": "wrapping their mouth with black cloth and holding black flags"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2076 ---

输入文本: “ They blocked access to the villages by cutting down trees .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "cutting down trees",
      "effect": "They blocked access to the villages"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1080 ---

输入文本: OPINION India ’ s Pakistan problem is Pakistan ’ s problem too December 03 , 2008 00:00 IST Siddharth Varadarajan If politics and emotion do not dictate India ’ s response , the terrorist strikes in Mumbai could be a catalyst for ending the Pakistani military ’ s fatal patronage of jihadi groups .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "politics and emotion do not dictate India ’ s response",
      "effect": "the terrorist strikes in Mumbai could be a catalyst for ending the Pakistani military ’ s fatal patronage of jihadi groups"
    },
    {
      "cause": "the terrorist strikes in Mumbai",
      "effect": "ending the Pakistani military ’ s fatal patronage of jihadi groups"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2147 ---

输入文本: In all , 58 persons were arrested for indulging in violence .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "indulging in violence",
      "effect": "58 persons were arrested"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2577 ---

输入文本: THRISSUR : Hike in toll rate withdrawn October 03 , 2013 00:00 IST A hike in toll on the Mannuthy-Edappally stretch , effected from Tuesday , was withdrawn on Wednesday following protests .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "protests",
      "effect": "A hike in toll on the Mannuthy-Edappally stretch , effected from Tuesday , was withdrawn on Wednesday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1835 ---

输入文本: Two men have been arrested for the murder of two ANC branch leaders on the KwaZulu-Natal south coast , police said on Tuesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the murder of two ANC branch leaders on the KwaZulu-Natal south coast",
      "effect": "Two men have been arrested"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2658 ---

输入文本: TDP members were probing irregularities in wage payment under NRLEGP when they were mobbed

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "TDP members were probing irregularities in wage payment under NRLEGP",
      "effect": "they were mobbed"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2624 ---

输入文本: " Rebels opened fire on the IAF chopper when it tried to land in a conflict zone in Sukma district to rescue a few troopers who had received gunshots in an encounter .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "it tried to land in a conflict zone in Sukma district",
      "effect": "Rebels opened fire on the IAF chopper"
    },
    {
      "cause": "to rescue a few troopers who had received gunshots in an encounter",
      "effect": "it tried to land in a conflict zone in Sukma district"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1653 ---

输入文本: On August 16 , 34 striking mineworkers were shot dead and 78 were injured when the police opened fire while trying to disperse a group which had gathered on a hill near the mine .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the police opened fire while trying to disperse a group which had gathered on a hill near the mine",
      "effect": "On August 16 , 34 striking mineworkers were shot dead and 78 were injured"
    },
    {
      "cause": "trying to disperse a group which had gathered on a hill near the mine",
      "effect": "the police opened fire"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=902 ---

输入文本: The memorandum given to Chief Minister Harish Rawat , on Saturday , read : “ The stone crushers working in the area will [ be the cause of dust and health problems which will ] result in migration of the population … here most of the people are completely dependent on the earnings from the agricultural produce [ and the dust from the stone crushers would destroy agriculture ] . ”

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "The stone crushers working in the area",
      "effect": "dust and health problems"
    },
    {
      "cause": "dust and health problems",
      "effect": "migration of the population"
    },
    {
      "cause": "the dust from the stone crushers",
      "effect": "would destroy agriculture"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1560 ---

输入文本: Police officers arrived on the spot and promised action and convinced Jaya to stop the protest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Police officers arrived on the spot and promised action",
      "effect": "convinced Jaya to stop the protest"
    },
    {
      "cause": "to stop the protest",
      "effect": "convinced Jaya"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1953 ---

输入文本: Three months back , when the garbage transport vehicle drivers went for a flash strike , the city stank for four days .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the garbage transport vehicle drivers went for a flash strike",
      "effect": "the city stank for four days"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=148 ---

输入文本: Hong Kong police on Thursday also charged 44 people linked to the protests with “ rioting ” , a crime that carries a maximum penalty of 10 years in prison .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "“ rioting ”",
      "effect": "Hong Kong police on Thursday also charged 44 people linked to the protests"
    },
    {
      "cause": "linked to the protests with “ rioting ”",
      "effect": "Hong Kong police on Thursday also charged 44 people"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=924 ---

输入文本: They reacted angrily when mayor James Nxumalo was not available to accept their memorandum .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "mayor James Nxumalo was not available to accept their memorandum",
      "effect": "They reacted angrily"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=783 ---

输入文本: The company had further offered a once-off hardship allowance of R2000 to help workers deal with financial difficulties arising from the no-work , no-pay principle in place while they were striking .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to help workers deal with financial difficulties arising from the no-work , no-pay principle in place while they were striking",
      "effect": "The company had further offered a once-off hardship allowance of R2000"
    },
    {
      "cause": "the no-work , no-pay principle in place",
      "effect": "financial difficulties"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1535 ---

输入文本: RFEA chief executive Nico Badenhorst said the strike was costing the country R100 million a day .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the strike",
      "effect": "costing the country R100 million a day"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=617 ---

输入文本: Agri SA calls for calm in Coligny Molaole Montsho COLIGNY , May 8 ( ANA ) - Agricultural body Agri SA on Monday , slammed the violence that flared up in Coligny , in the North West , after two farmers accused of the murder of Matlhomola Jonas Mosweu were granted bail .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "two farmers accused of the murder of Matlhomola Jonas Mosweu were granted bail",
      "effect": "the violence that flared up in Coligny , in the North West"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=487 ---

输入文本: When a security guard tried to intervene , he was brutally assaulted .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "a security guard tried to intervene",
      "effect": "he was brutally assaulted"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2302 ---

输入文本: On Wednesday , a crowd , made up of mainly young people from various civil community organisations and students from universities and schools across the city , gathered outside the CTICC , chanting struggle songs and holding posters on which was written `` enough is enough '' and `` stop killing women and children '' .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "chanting struggle songs and holding posters on which was written `` enough is enough '' and `` stop killing women and children ''",
      "effect": "On Wednesday , a crowd , made up of mainly young people from various civil community organisations and students from universities and schools across the city , gathered outside the CTICC"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=3061 ---

输入文本: In 2001 , he allegedly hatched a conspiracy to murder his political opponent Javed Iqbal in Allahabad .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to murder his political opponent Javed Iqbal in Allahabad",
      "effect": "he allegedly hatched a conspiracy"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1072 ---

输入文本: In India , actions around the Copenhagen talks are being organised by Climate Satyagraha Camp , a civil society coalition to give Indians a voice to the Climate Summit in Copenhagen .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to give Indians a voice to the Climate Summit in Copenhagen",
      "effect": "In India , actions around the Copenhagen talks are being organised by Climate Satyagraha Camp , a civil society coalition"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2948 ---

输入文本: Of the five flat occupants , Atif Ameen and Mohd Sajid were killed during the encounter .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the encounter",
      "effect": "Atif Ameen and Mohd Sajid were killed"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2233 ---

输入文本: Other explosions cut railway lines between the sprawling township and Johannesburg .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Other explosions",
      "effect": "cut railway lines between the sprawling township and Johannesburg"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=594 ---

输入文本: CPI activists staged a road blockade in Mahbubnagar district , demanding the legislator 's arrest and a compensation of Rs .1 million to the family of the deceased .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding the legislator 's arrest and a compensation of Rs .1 million to the family of the deceased",
      "effect": "CPI activists staged a road blockade in Mahbubnagar district"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=513 ---

输入文本: A series of blasts took place Sunday before Modi was to address the BJP rally , leaving six dead and over 80 injured .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "A series of blasts took place Sunday",
      "effect": "leaving six dead and over 80 injured"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2569 ---

输入文本: Earlier in the day , the hotel premises saw party workers waving Trinamool flags and shouting slogans demanding justice from the management .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding justice from the management",
      "effect": "the hotel premises saw party workers waving Trinamool flags and shouting slogans"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=858 ---

输入文本: As the information was spread in the area , the public started gathering in front of the check-post demanding the arrest of the policeman .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the information was spread in the area",
      "effect": "the public started gathering in front of the check-post"
    },
    {
      "cause": "demanding the arrest of the policeman",
      "effect": "the public started gathering in front of the check-post"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=339 ---

输入文本: Distributing medals and trophies to winners of the five-day event in which 702 personnel from 22 State police teams and eight Central police organisations participated , the chief minister recalled the 26/11 incidents in Mumbai to stress her point .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to stress her point",
      "effect": "the chief minister recalled the 26/11 incidents in Mumbai"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=296 ---

输入文本: The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma to probe into the violence and the deaths of 44 people in wage-related protests .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to probe into the violence and the deaths of 44 people in wage-related protests",
      "effect": "The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma"
    },
    {
      "cause": "wage-related protests",
      "effect": "the violence and the deaths of 44 people"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2369 ---

输入文本: Tension prevailed in the dense forest , especially in and around GK Veedhi , Chintapalle and other Maoist strongholds following the incident .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the incident",
      "effect": "Tension prevailed in the dense forest , especially in and around GK Veedhi , Chintapalle and other Maoist strongholds"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2900 ---

输入文本: However , the absence of senior Trinamool Congress leaders during the agitation prompted opposition parties to raise fingers at " TMC 's internal feud that led to the incident " .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the absence of senior Trinamool Congress leaders during the agitation",
      "effect": "opposition parties to raise fingers at \" TMC 's internal feud that led to the incident \""
    },
    {
      "cause": "TMC 's internal feud",
      "effect": "the incident"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2351 ---

输入文本: PTI BANGALORE : All courts will be shut on Saturday after Friday 's violence the city 's civil court premises .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Friday 's violence the city 's civil court premises",
      "effect": "All courts will be shut on Saturday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2925 ---

输入文本: Sub-Inspector Murlidhar Bastia of Raghunathpur area was killed in Maoist attack while working in Keonjhar district .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Maoist attack while working in Keonjhar district",
      "effect": "Sub-Inspector Murlidhar Bastia of Raghunathpur area was killed"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=1038 ---

输入文本: Farmers Block NH 7 , Say Government Blind to Their Plight 21st June 2015 06:00 AM CHIKBALLAPUR : Farmers on Saturday blocked the busy National Highway 7 on the outskirts of the city for nearly five hours and shouted slogans against the Union and state governments .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "against the Union and state governments",
      "effect": "Farmers on Saturday blocked the busy National Highway 7 on the outskirts of the city for nearly five hours and shouted slogans"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2124 ---

输入文本: On Tuesday we went to picket at the Western Cape Provincial Legislature after we had gone over a month without teachers .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "we had gone over a month without teachers",
      "effect": "On Tuesday we went to picket at the Western Cape Provincial Legislature"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "cannot import name 'package' from partially initialized module 'torch' (most likely due to a circular import) (D:\\Anaconda3\\envs\\Master_thesis\\Lib\\site-packages\\torch\\__init__.py)"
}
```

### --- id=2632 ---

输入文本: He has been on indefinite hunger strike since August 25 in support of united Andhra Pradesh .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "in support of united Andhra Pradesh",
      "effect": "He has been on indefinite hunger strike since August 25"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1238 ---

输入文本: Till the filing of this report , all protesters were squatting outside Vikas Bhawan and said would call off their stir only after getting formal orders regarding regularisation of all retrenched staffers .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the filing of this report",
      "effect": "all protesters were squatting outside Vikas Bhawan"
    },
    {
      "cause": "getting formal orders regarding regularisation of all retrenched staffers",
      "effect": "would call off their stir"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1555 ---

输入文本: Subsequently , the police arrested six persons in connection with the murder and eight others turned themselves in .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "in connection with the murder and eight others turned themselves in",
      "effect": "the police arrested six persons"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=3038 ---

输入文本: April 13 , 2013 00:00 IST Police step up security Several hundred shops in Podanur , Sundarapuram , Kuniamuthur , Kovaipudur , Milekal , Machampalayam , Idayarpalayam , Kulathupalayam and Sungapuram areas remained closed on Friday in protest against the damage caused to an idol at a temple on Monday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "in protest against the damage caused to an idol at a temple on Monday",
      "effect": "Several hundred shops in Podanur , Sundarapuram , Kuniamuthur , Kovaipudur , Milekal , Machampalayam , Idayarpalayam , Kulathupalayam and Sungapuram areas remained closed on Friday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=462 ---

输入文本: Avelino de Sa , president DRAG said the dharna was held to highlight the neglect of the differently-abled persons by the State government from four years .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to highlight the neglect of the differently-abled persons by the State government from four years",
      "effect": "the dharna was held"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1836 ---

输入文本: Similar banners were also found between Sunki and Ampavalli where Maoists also blocked road by felling trees .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "felling trees",
      "effect": "blocked road"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=117 ---

输入文本: Another Congress worker , Repon Sheikh , was killed at Bharatpur in the same district during a clash between rival party supporters , the police said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "a clash between rival party supporters",
      "effect": "Another Congress worker , Repon Sheikh , was killed at Bharatpur in the same district"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2771 ---

输入文本: On July 28 , an argument between two shopkeepers had led to a communal flare-up .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "an argument between two shopkeepers",
      "effect": "a communal flare-up"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2578 ---

输入文本: The hike was withdrawn on Wednesday following protests by activists of the Youth Congress , the BJP and the DYFI .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "protests by activists of the Youth Congress , the BJP and the DYFI",
      "effect": "The hike was withdrawn on Wednesday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2736 ---

输入文本: Eyewitness said three rebels armed with sophisticated weapons arrived near the Shiva temple in a motorcycle and fired point blank at 38 - year-old contractor Budra Dhangda Majhi , killing him on the spot .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "three rebels armed with sophisticated weapons arrived near the Shiva temple in a motorcycle and fired point blank at 38 - year-old contractor Budra Dhangda Majhi",
      "effect": "killing him on the spot"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2051 ---

输入文本: Meanwhile , the Salem Range DIG , Sanjay Kumar , said that a special team has been formed to nab the assailants who murdered Ramesh .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to nab the assailants who murdered Ramesh",
      "effect": "a special team has been formed"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1461 ---

输入文本: The police charged Mr. Chandrashekhar with instigating violence on May 9 under various IPC sections .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "instigating violence on May 9 under various IPC sections",
      "effect": "The police charged Mr. Chandrashekhar"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2281 ---

输入文本: While an official ceremony took place at the Hong Kong Convention and Exhibition Centre to mark the 22nd anniversary of the return of sovereignty from Britain to China , tensions spiked once more in the financial hub after hundreds of mainly young , masked protesters mostly in black wearing hard hats and goggles seized three key thoroughfares , some deploying metal and plastic barriers to block the way .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "to mark the 22nd anniversary of the return of sovereignty from Britain to China",
      "effect": "an official ceremony took place at the Hong Kong Convention and Exhibition Centre"
    },
    {
      "cause": "hundreds of mainly young , masked protesters mostly in black wearing hard hats and goggles seized three key thoroughfares",
      "effect": "tensions spiked once more in the financial hub"
    },
    {
      "cause": "to block the way",
      "effect": "some deploying metal and plastic barriers"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2985 ---

输入文本: Official sources said the firing was done in " self defence " when a group of villagers resisted combing operations and tried to snatch the weapons of the police and Army personnel .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "a group of villagers resisted combing operations and tried to snatch the weapons of the police and Army personnel",
      "effect": "the firing was done in \" self defence"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1450 ---

输入文本: The incident took place around noon in Gaya district 's Uchla village near Sherghati , about 100 km from here , when Maoists blew up a patrolling vehicle of the Roshanganj police station .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Maoists blew up a patrolling vehicle of the Roshanganj police station",
      "effect": "The incident took place around noon in Gaya district 's Uchla village near Sherghati , about 100 km from here"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1970 ---

输入文本: Police teargassing was answered with a few gunshots in the air from one of the houses .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Police teargassing",
      "effect": "a few gunshots in the air from one of the houses"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1302 ---

输入文本: Protests were held over the weekend as displaced families and relatives of missing firefighters demanded compensation and answers about the whereabouts of their loved ones .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "displaced families and relatives of missing firefighters demanded compensation and answers about the whereabouts of their loved ones",
      "effect": "Protests were held over the weekend"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1926 ---

输入文本: The police fired seven rounds in the air and lobbed nine teargas shells to bring the mob which fired from country-made guns and pelted stones under control .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to bring the mob which fired from country-made guns and pelted stones under control",
      "effect": "The police fired seven rounds in the air and lobbed nine teargas shells"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1138 ---

输入文本: Senior teachers , concerned about the future of students , agreed that the university administration had made a smart move to conduct classes even as the exams were boycotted to ensure that the mandatory instruction days were met with .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to ensure that the mandatory instruction days were met with",
      "effect": "the university administration had made a smart move to conduct classes even as the exams were boycotted"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1761 ---

输入文本: Students Lay Siege to CHSE Office over + 2 Results

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "+ 2 Results",
      "effect": "Students Lay Siege to CHSE Office"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1172 ---

输入文本: On July 16 , one person identified as Mintu Deori was killed during a protest while 20 others , including two Additional SPs , were injured in clashes between police and protesters demanding shifting of proposed AIIMS in Assam from Changsari to Raha .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "a protest",
      "effect": "one person identified as Mintu Deori was killed"
    },
    {
      "cause": "clashes between police and protesters",
      "effect": "20 others , including two Additional SPs , were injured"
    },
    {
      "cause": "demanding shifting of proposed AIIMS in Assam from Changsari to Raha",
      "effect": "clashes between police and protesters"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=905 ---

输入文本: The incident triggered outrage across the country and was condemned as despicable and shameful stirring memories of a similar attack last December in New Delhi that sparked nationwide protests .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "The incident",
      "effect": "triggered outrage across the country and was condemned as despicable and shameful stirring memories of a similar attack last December in New Delhi that sparked nationwide protests"
    },
    {
      "cause": "a similar attack last December in New Delhi",
      "effect": "nationwide protests"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1928 ---

输入文本: The municipality witnessed protests by residents in Boitumelong in the beginning of April , when a number of houses , including a councillor 's , were burnt down .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "The municipality witnessed protests by residents in Boitumelong in the beginning of April",
      "effect": "a number of houses , including a councillor 's , were burnt down"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=892 ---

输入文本: Campaign against Negligence of Girl Child , a non-governmental organisation , and the District Legal Services Authority jointly organised the human chain as part of the worldwide campaign on violence against women from November 25 to December 12 .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "as part of the worldwide campaign on violence against women from November 25 to December 12",
      "effect": "Campaign against Negligence of Girl Child , a non-governmental organisation , and the District Legal Services Authority jointly organised the human chain"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2575 ---

输入文本: In case the government does not change its stand , we will further intensify our stir .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the government does not change its stand",
      "effect": "we will further intensify our stir"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=3000 ---

输入文本: We have been together in each other 's hour of grief and joy , but to allege that I was a part of the crowd that incited them to raise anti-Sikh slogans is a preposterous and blatant lie .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to raise anti-Sikh slogans",
      "effect": "the crowd that incited them"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=809 ---

输入文本: “ We are here to fight for democracy and universal suffrage. ”

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "for democracy and universal suffrage",
      "effect": "We are here to fight"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=246 ---

输入文本: Spokesman Keith Khoza said they had decided to March to Prime Media because the cartoon had raised various concerns .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the cartoon had raised various concerns",
      "effect": "they had decided to March to Prime Media"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1100 ---

输入文本: Students and lawyers also joined the protests , focusing on Mahabubnagar district to stop vehicles entering Telangana coming from Kurnool district , which is a part of the Rayalaseema region .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to stop vehicles entering Telangana coming from Kurnool district , which is a part of the Rayalaseema region",
      "effect": "Students and lawyers also joined the protests , focusing on Mahabubnagar district"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1943 ---

输入文本: Speakers at the rally , orgainsed by the Peoples Union for Civil Liberties ( PUCL ) , CPI , CPM , and Chhattisgarh Mukti Morcha ( CMM ) , accused the Raman Singh government of having implicated Sen in a false case .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "having implicated Sen in a false case",
      "effect": "Speakers at the rally , orgainsed by the Peoples Union for Civil Liberties ( PUCL ) , CPI , CPM , and Chhattisgarh Mukti Morcha ( CMM ) , accused the Raman Singh government of"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2216 ---

输入文本: Protesters pushed through police barriers in an attempt to enter the buildings , but to no avail .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to enter the buildings",
      "effect": "Protesters pushed through police barriers"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2540 ---

输入文本: Soon after the heat and dust of the twin blasts settled , city policemen worked overtime to step up security arrangements all over the city and schools were among the most important establishments under the scanner .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "step up security arrangements all over the city",
      "effect": "city policemen worked overtime"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2665 ---

输入文本: Saying that the attack was planned and motivated , she demanded Dr. Venkateswara Rao to resign his Assembly membership and sought an apology from Ms. Purandeswari .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "Saying that the attack was planned and motivated",
      "effect": "she demanded Dr. Venkateswara Rao to resign his Assembly membership and sought an apology from Ms. Purandeswari"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1131 ---

输入文本: Though none were injured , it shook the entire State machinery , as the blast had occurred just a few days ahead of the classical Tamil conference in June last year .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the blast had occurred just a few days ahead of the classical Tamil conference in June last year",
      "effect": "it shook the entire State machinery"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=790 ---

输入文本: The youth 's murder took political overtones this morning with the Leader of Opposition ( LoP ) Prem Kumar meeting the family members of the victim to express sorrow and later addressed a large number of people who had blocked road near Mahabir bridge to protest against the murder .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 4
  },
  "gold_relations": [
    {
      "cause": "the Leader of Opposition ( LoP ) Prem Kumar meeting the family members of the victim to express sorrow and later addressed a large number of people who had blocked road near Mahabir bridge to protest against the murder",
      "effect": "The youth 's murder took political overtones this morning"
    },
    {
      "cause": "to express sorrow",
      "effect": "the Leader of Opposition ( LoP ) Prem Kumar meeting the family members of the victim"
    },
    {
      "cause": "against the murder",
      "effect": "a large number of people who had blocked road near Mahabir bridge to protest"
    },
    {
      "cause": "to protest",
      "effect": "a large number of people who had blocked road near Mahabir bridge"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1177 ---

输入文本: Violence broke out when DYFI members protested against a Youth Congress meeting being held at the junction .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "DYFI members protested",
      "effect": "Violence broke out"
    },
    {
      "cause": "against a Youth Congress meeting being held at the junction",
      "effect": "DYFI members protested"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=3010 ---

输入文本: March 03 , 2013 00:00 IST Holds demonstration in front of SE office in Nizamabad The TDP Legislators on Saturday , seriously warned the electricity authorities against the frequent cuts in power supply to the farm sector resulting in damage to the crop which is in its last stage for harvest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the frequent cuts in power supply to the farm sector",
      "effect": "damage to the crop which is in its last stage for harvest"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2386 ---

输入文本: Meanwhile , Tamil Nadu BJP president Pon Radhakrishnan said the party has called for a statewide bandh on Monday to condemn the murder .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "to condemn the murder",
      "effect": "the party has called for a statewide bandh on Monday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1162 ---

输入文本: HYDERABAD : Schools , colleges closed today July 19 , 2010 00:00 IST Managements of several educational institutions , especially schools have announced a holiday on Monday due to the State-wide bandh called by Telugu Desam on Monday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the State-wide bandh called by Telugu Desam on Monday",
      "effect": "Managements of several educational institutions , especially schools have announced a holiday on Monday"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1446 ---

输入文本: KERALA Bishops express concern December 27 , 2007 00:00 IST Kochi : The Kerala Catholic Bishops ’ Council ( KCBC ) has expressed concern over the attack on Christian churches , orphanages and the Bishop ’ s House at Kandhamal in Orissa .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the attack on Christian churches , orphanages and the Bishop ’ s House at Kandhamal in Orissa .",
      "effect": "The Kerala Catholic Bishops ’ Council ( KCBC ) has expressed concern"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=1435 ---

输入文本: A sudden deviation from it carries ominous implications , not least because the scale of the outbreak in the UP village was not large enough to warrant such a departure from the norm .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the scale of the outbreak in the UP village was not large enough to warrant such a departure from the norm",
      "effect": "A sudden deviation from it carries ominous implications"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=2487 ---

输入文本: IN SCHOOL Meghalaya June 02 , 2014 00:00 IST 13 Curfew was on Saturday relaxed for eight hours in Meghalaya ’ s West Garo Hills district , two days after it was imposed following mob violence over the death of a suspected militant in police custody , officials said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "mob violence",
      "effect": "it was imposed"
    },
    {
      "cause": "the death of a suspected militant in police custody",
      "effect": "mob violence"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=456 ---

输入文本: ALIGARH : AMU shut down following violence May 01 , 2011 00:00 IST Aligarh Muslim University has been closed indefinitely in the wake of violence among students late on Friday evening .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "violence among students late on Friday evening",
      "effect": "Aligarh Muslim University has been closed indefinitely"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```

### --- id=708 ---

输入文本: September 04 , 2014 00:00 IST Officials promise to supply water in tankers Women took to streets carrying pots in protest against erratic supply of drinking water at Kelamagalam in Udhanapalli on Wednesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "against erratic supply of drinking water at Kelamagalam in Udhanapalli on Wednesday",
      "effect": "Women took to streets carrying pots in protest"
    },
    {
      "cause": "in protest against erratic supply of drinking water at Kelamagalam in Udhanapalli on Wednesday",
      "effect": "Women took to streets carrying pots"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "unknown_generation_error",
  "generation_error_message": "[WinError 206] 文件名或扩展名太长。: 'D:\\\\Anaconda3\\\\envs\\\\Master_thesis\\\\Lib\\\\site-packages\\\\torch\\\\lib'"
}
```
