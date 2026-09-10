================ KAPipe CDR baseline: ade ================
样本总数: 10
  Gold 含因果: 3 | Pred 含因果: 2
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.900
  Precision: 1.000
  Recall   : 0.667
  F1       : 0.800
  (TP=2, TN=7, FP=0, FN=1)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 10
    Gold triples: 8 | Pred triples: 3
    Precision: 1.000
    Recall   : 0.375
    F1       : 0.545
    (TP=3, FP=0, FN=5)
  [anchor_window] (primary)
    样本数: 10
    Gold triples: 8 | Pred triples: 3
    Precision: 0.667
    Recall   : 0.250
    F1       : 0.364
    (TP=2, FP=1, FN=6)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 2
    Gold triples: 7 | Pred triples: 3
    Precision: 1.000
    Recall   : 0.429
    F1       : 0.600
    (TP=3, FP=0, FN=4)
  [anchor_window] (primary)
    样本数: 2
    Gold triples: 7 | Pred triples: 3
    Precision: 0.667
    Recall   : 0.286
    F1       : 0.400
    (TP=2, FP=1, FN=5)
================================================