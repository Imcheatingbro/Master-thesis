================ KAPipe CDR baseline: ade ================
样本总数: 100
  Gold 含因果: 10 | Pred 含因果: 8
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.920
  Precision: 0.625
  Recall   : 0.500
  F1       : 0.556
  (TP=5, TN=87, FP=3, FN=5)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 100
    Gold triples: 17 | Pred triples: 9
    Precision: 0.667
    Recall   : 0.353
    F1       : 0.462
    (TP=6, FP=3, FN=11)
  [anchor_window] (primary)
    样本数: 100
    Gold triples: 17 | Pred triples: 9
    Precision: 0.556
    Recall   : 0.294
    F1       : 0.385
    (TP=5, FP=4, FN=12)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 5
    Gold triples: 10 | Pred triples: 6
    Precision: 1.000
    Recall   : 0.600
    F1       : 0.750
    (TP=6, FP=0, FN=4)
  [anchor_window] (primary)
    样本数: 5
    Gold triples: 10 | Pred triples: 6
    Precision: 0.833
    Recall   : 0.500
    F1       : 0.625
    (TP=5, FP=1, FN=5)
================================================