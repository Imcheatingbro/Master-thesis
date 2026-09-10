================ KAPipe CDR baseline: ade ================
样本总数: 2942
  Gold 含因果: 448 | Pred 含因果: 365
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.928
  Precision: 0.822
  Recall   : 0.670
  F1       : 0.738
  (TP=300, TN=2429, FP=65, FN=148)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 2942
    Gold triples: 663 | Pred triples: 469
    Precision: 0.657
    Recall   : 0.465
    F1       : 0.544
    (TP=308, FP=161, FN=355)
  [anchor_window] (primary)
    样本数: 2942
    Gold triples: 663 | Pred triples: 469
    Precision: 0.580
    Recall   : 0.410
    F1       : 0.481
    (TP=272, FP=197, FN=391)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 300
    Gold triples: 469 | Pred triples: 394
    Precision: 0.782
    Recall   : 0.657
    F1       : 0.714
    (TP=308, FP=86, FN=161)
  [anchor_window] (primary)
    样本数: 300
    Gold triples: 469 | Pred triples: 394
    Precision: 0.690
    Recall   : 0.580
    F1       : 0.630
    (TP=272, FP=122, FN=197)
================================================