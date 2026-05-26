# ade first 100 eval report

## 配置
```json
{
  "label": "ade first 100",
  "model": "qwen/qwen3.5-35b-a3b",
  "dataset": "ade",
  "sample_count": 100,
  "prompt_name": "v3",
  "use_rag": true,
  "rag_mode": "knn_pattern",
  "rag_top_k": 3,
  "temperature": 0.0,
  "max_tokens": 2048,
  "progress_every": 50,
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ ade first 100 final report ================
样本总数: 100
  Gold 含因果: 100 | Pred 含因果: 91
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.910
  Precision: 1.000
  Recall   : 0.910
  F1       : 0.953
  (TP=91, TN=0, FP=0, FN=9)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 100
    Gold triples: 124 | Pred triples: 94
    Precision: 0.543
    Recall   : 0.411
    F1       : 0.468
    (TP=51, FP=43, FN=73)
  [anchor_window] (primary)
    样本数: 100
    Gold triples: 124 | Pred triples: 94
    Precision: 0.968
    Recall   : 0.734
    F1       : 0.835
    (TP=91, FP=3, FN=33)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 91
    Gold triples: 112 | Pred triples: 94
    Precision: 0.543
    Recall   : 0.455
    F1       : 0.495
    (TP=51, FP=43, FN=61)
  [anchor_window] (primary)
    样本数: 91
    Gold triples: 112 | Pred triples: 94
    Precision: 0.968
    Recall   : 0.812
    F1       : 0.883
    (TP=91, FP=3, FN=21)
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

## 样本明细

### --- id=1 ---

输入文本: Fixed drug eruption in hands caused by omeprazole.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "omeprazole",
      "effect": "eruption"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "omeprazole"
      },
      "relation": "caused",
      "effect": {
        "span": "Fixed drug eruption in hands"
      }
    }
  ]
}
```

### --- id=2 ---

输入文本: These findings suggest that bicytopenia in this patient was caused by D-Pen and may be due to different sensitivities in the hematopoietic lineage.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "D-Pen",
      "effect": "bicytopenia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "D-Pen"
      },
      "relation": "caused",
      "effect": {
        "span": "bicytopenia"
      }
    }
  ]
}
```

### --- id=3 ---

输入文本: Postoperative hypocalcemic tetany caused by fleet phospho-soda preparation in a patient taking alendronate sodium: report of a case.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "alendronate sodium",
      "effect": "hypocalcemic tetany"
    },
    {
      "cause": "fleet phospho-soda",
      "effect": "hypocalcemic tetany"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "fleet phospho-soda preparation"
      },
      "relation": "caused",
      "effect": {
        "span": "Postoperative hypocalcemic tetany"
      }
    }
  ]
}
```

### --- id=4 ---

输入文本: Bronchiolitis obliterans organising pneumonia associated with the use of nitrofurantoin.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "nitrofurantoin",
      "effect": "Bronchiolitis obliterans organising pneumonia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "nitrofurantoin"
      },
      "relation": "caused",
      "effect": {
        "span": "Bronchiolitis obliterans organising pneumonia"
      }
    }
  ]
}
```

### --- id=5 ---

输入文本: Acute erythroid leukemia after cyclophosphamide therapy for multiple myeloma: report of two cases.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "cyclophosphamide",
      "effect": "Acute erythroid leukemia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cyclophosphamide therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "Acute erythroid leukemia"
      }
    }
  ]
}
```

### --- id=6 ---

输入文本: It remains to be seen whether the hepatotoxicity associated with troglitazone is a drug-class effect or specific to troglitazone.

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
      "cause": "troglitazone",
      "effect": "hepatotoxicity"
    }
  ],
  "pred_triples": []
}
```

### --- id=7 ---

输入文本: Case 3: A 29-year-old female alcoholic complained of general fatigue and a slight fever after 1.5 years of abstinence with cyanamide treatment.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "cyanamide",
      "effect": "fatigue"
    },
    {
      "cause": "cyanamide",
      "effect": "fever"
    }
  ],
  "pred_triples": []
}
```

### --- id=8 ---

输入文本: Cyanamide-induced liver dysfunction after abstinence in alcoholics: a long-term follow-up study on four cases.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Cyanamide",
      "effect": "liver dysfunction"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Cyanamide"
      },
      "relation": "caused",
      "effect": {
        "span": "liver dysfunction"
      }
    }
  ]
}
```

### --- id=9 ---

输入文本: A case of normotensive scleroderma renal crisis after high-dose methylprednisolone treatment.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "methylprednisolone",
      "effect": "normotensive scleroderma renal crisis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "high-dose methylprednisolone treatment"
      },
      "relation": "caused",
      "effect": {
        "span": "normotensive scleroderma renal crisis"
      }
    }
  ]
}
```

### --- id=10 ---

输入文本: When the acute manic state is characterized by marked psychotic symptoms and intense anxiety, it may be associated with increased vulnerability to the development of severe lithium neurotoxicity.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "lithium",
      "effect": "intense anxiety"
    },
    {
      "cause": "lithium",
      "effect": "neurotoxicity"
    },
    {
      "cause": "lithium",
      "effect": "psychotic symptoms"
    }
  ],
  "pred_triples": []
}
```

### --- id=11 ---

输入文本: While for ribavirin antidepressant effects are not known, we suppose that antidepressants may prevent changes in serotonergic or noradrenergic neurotransmission caused by IFN-alpha.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "IFN-alpha",
      "effect": "changes in serotonergic or noradrenergic neurotransmission"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "IFN-alpha"
      },
      "relation": "caused",
      "effect": {
        "span": "changes in serotonergic or noradrenergic neurotransmission"
      }
    }
  ]
}
```

### --- id=12 ---

输入文本: Case studies in heparin-induced thrombocytopenia.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "heparin",
      "effect": "thrombocytopenia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "heparin"
      },
      "relation": "caused",
      "effect": {
        "span": "thrombocytopenia"
      }
    }
  ]
}
```

### --- id=13 ---

输入文本: We propose that cyclophosphamide be added to the list of exposures potentially associated with hepatic angiosarcoma.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "cyclophosphamide",
      "effect": "hepatic angiosarcoma"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cyclophosphamide"
      },
      "relation": "caused",
      "effect": {
        "span": "hepatic angiosarcoma"
      }
    }
  ]
}
```

### --- id=14 ---

输入文本: Possible serotonin syndrome associated with clomipramine after withdrawal of clozapine.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "clomipramine",
      "effect": "serotonin syndrome"
    },
    {
      "cause": "clozapine",
      "effect": "serotonin syndrome"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "withdrawal of clozapine"
      },
      "relation": "caused",
      "effect": {
        "span": "Possible serotonin syndrome"
      }
    }
  ]
}
```

### --- id=15 ---

输入文本: We describe a patient who presented with bloody diarrhoea after 15 mg meloxicam daily for 10 days for osteoarthritis.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "meloxicam",
      "effect": "bloody diarrhoea"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "15 mg meloxicam daily for 10 days"
      },
      "relation": "caused",
      "effect": {
        "span": "bloody diarrhoea"
      }
    }
  ]
}
```

### --- id=16 ---

输入文本: We cared for a patient with progressive renal impairment who presented with blurred vision, QRS broadening and cardiac failure due to chronic cibenzoline intoxication.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 4
  },
  "gold_relations": [
    {
      "cause": "cibenzoline",
      "effect": "blurred vision"
    },
    {
      "cause": "cibenzoline",
      "effect": "cardiac failure"
    },
    {
      "cause": "cibenzoline",
      "effect": "cibenzoline intoxication"
    },
    {
      "cause": "cibenzoline",
      "effect": "QRS broadening"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "chronic cibenzoline intoxication"
      },
      "relation": "caused",
      "effect": {
        "span": "progressive renal impairment who presented with blurred vision, QRS broadening and cardiac failure"
      }
    }
  ]
}
```

### --- id=17 ---

输入文本: Successful treatment of visceral leishmaniasis with allopurinol plus ketoconazole in an infant who developed pancreatitis caused by meglumine antimoniate.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "meglumine antimoniate",
      "effect": "pancreatitis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "meglumine antimoniate"
      },
      "relation": "caused",
      "effect": {
        "span": "pancreatitis"
      }
    }
  ]
}
```

### --- id=18 ---

输入文本: CONCLUSIONS: This case report showed that the clinical appearance of Hashimoto's disease after IFN-alpha therapy for chronic C hepatitis in our patient was associated with a specific genetic predisposition (DR5) for this pathology.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "IFN-alpha",
      "effect": "Hashimoto's disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "IFN-alpha therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "clinical appearance of Hashimoto's disease"
      }
    },
    {
      "cause": {
        "span": "specific genetic predisposition (DR5)"
      },
      "relation": "caused",
      "effect": {
        "span": "Hashimoto's disease"
      }
    }
  ]
}
```

### --- id=19 ---

输入文本: Avascular necrosis of the femoral head in patients with prostate cancer treated with cyproterone acetate and radiotherapy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "cyproterone acetate",
      "effect": "Avascular necrosis of the femoral head"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "treated with cyproterone acetate and radiotherapy"
      },
      "relation": "caused",
      "effect": {
        "span": "Avascular necrosis of the femoral head"
      }
    }
  ]
}
```

### --- id=20 ---

输入文本: Ticlopidine-induced interstitial pulmonary disease: a case report.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Ticlopidine",
      "effect": "interstitial pulmonary disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Ticlopidine"
      },
      "relation": "caused",
      "effect": {
        "span": "interstitial pulmonary disease"
      }
    }
  ]
}
```

### --- id=21 ---

输入文本: We describe a case of needle-track cutaneous seeding of hepatocellular carcinoma (HCC) after sonographically guided percutaneous ethanol injection (PEI).

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "ethanol injection",
      "effect": "cutaneous seeding"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "sonographically guided percutaneous ethanol injection"
      },
      "relation": "caused",
      "effect": {
        "span": "needle-track cutaneous seeding of hepatocellular carcinoma"
      }
    }
  ]
}
```

### --- id=22 ---

输入文本: Adenosine-induced ventricular fibrillation.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Adenosine",
      "effect": "ventricular fibrillation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Adenosine"
      },
      "relation": "caused",
      "effect": {
        "span": "ventricular fibrillation"
      }
    }
  ]
}
```

### --- id=23 ---

输入文本: An obese patient, not diabetic, treated with metformin for some weeks, was referred to us with severe inferior digestive hemorrhage, diagnosed with Meckel's diverticulum.

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
      "cause": "metformin",
      "effect": "severe inferior digestive hemorrhage"
    }
  ],
  "pred_triples": []
}
```

### --- id=24 ---

输入文本: CONCLUSIONS: We report the first case of gemcitabine-induced LABD.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "gemcitabine",
      "effect": "LABD"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "gemcitabine"
      },
      "relation": "caused",
      "effect": {
        "span": "LABD"
      }
    }
  ]
}
```

### --- id=25 ---

输入文本: Acute lung injury associated with 5-fluorouracil and oxaliplatinum combined chemotherapy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "5-fluorouracil",
      "effect": "Acute lung injury"
    },
    {
      "cause": "oxaliplatinum",
      "effect": "Acute lung injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "5-fluorouracil and oxaliplatinum combined chemotherapy"
      },
      "relation": "caused",
      "effect": {
        "span": "Acute lung injury"
      }
    }
  ]
}
```

### --- id=26 ---

输入文本: Papillary necrosis associated with the HIV protease inhibitor indinavir.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "indinavir",
      "effect": "Papillary necrosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the HIV protease inhibitor indinavir"
      },
      "relation": "caused",
      "effect": {
        "span": "Papillary necrosis"
      }
    }
  ]
}
```

### --- id=27 ---

输入文本: Stupor from lamotrigine toxicity.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "lamotrigine",
      "effect": "Stupor"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "lamotrigine toxicity"
      },
      "relation": "caused",
      "effect": {
        "span": "Stupor"
      }
    }
  ]
}
```

### --- id=28 ---

输入文本: Amphotericin B-induced seizures in a patient with AIDS.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Amphotericin B",
      "effect": "seizures"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Amphotericin B"
      },
      "relation": "caused",
      "effect": {
        "span": "seizures"
      }
    }
  ]
}
```

### --- id=29 ---

输入文本: CASE SUMMARY: A 46-year-old African-American man experienced recurrent grand mal seizures during intravenous infusion of amphotericin B, then petit mal seizures as the infusion was stopped and the drug concentrations decreased with time.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "amphotericin B",
      "effect": "grand mal seizures"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "intravenous infusion of amphotericin B"
      },
      "relation": "caused",
      "effect": {
        "span": "recurrent grand mal seizures"
      }
    },
    {
      "cause": {
        "span": "the infusion was stopped and the drug concentrations decreased with time"
      },
      "relation": "caused",
      "effect": {
        "span": "petit mal seizures"
      }
    }
  ]
}
```

### --- id=30 ---

输入文本: To date, only three cases of seizures associated with amphotericin B have been reported in the literature, but healthcare providers should be aware of the potential for this rare adverse effect.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "amphotericin B",
      "effect": "seizures"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "amphotericin B"
      },
      "relation": "caused",
      "effect": {
        "span": "seizures"
      }
    }
  ]
}
```

### --- id=31 ---

输入文本: Carbamazepine induced right bundle branch block in a Greenlandic patient.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Carbamazepine",
      "effect": "right bundle branch block"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Carbamazepine"
      },
      "relation": "caused",
      "effect": {
        "span": "right bundle branch block"
      }
    }
  ]
}
```

### --- id=32 ---

输入文本: Cicatricial entropion associated with chronic dipivefrin application.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "dipivefrin",
      "effect": "Cicatricial entropion"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "chronic dipivefrin application"
      },
      "relation": "caused",
      "effect": {
        "span": "Cicatricial entropion"
      }
    }
  ]
}
```

### --- id=33 ---

输入文本: Triiodothyronine-induced thyrotoxicosis in ophthalmic Graves disease.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Triiodothyronine",
      "effect": "thyrotoxicosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Triiodothyronine"
      },
      "relation": "caused",
      "effect": {
        "span": "thyrotoxicosis"
      }
    }
  ]
}
```

### --- id=34 ---

输入文本: Such anagen effluvium with lichenoid eruption following INH therapy has not been observed previously.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "INH",
      "effect": "anagen effluvium"
    },
    {
      "cause": "INH",
      "effect": "lichenoid eruption"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "INH therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "anagen effluvium with lichenoid eruption"
      }
    }
  ]
}
```

### --- id=35 ---

输入文本: We presented the case of a patient who developed a cutaneous reaction induced by captopril with positive patch test.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "captopril",
      "effect": "cutaneous reaction"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "captopril"
      },
      "relation": "caused",
      "effect": {
        "span": "a cutaneous reaction"
      }
    }
  ]
}
```

### --- id=36 ---

输入文本: We describe a case of subcutaneous metastasis along the needle track after percutaneous ethanol injection (PEI) for treatment of hepatocellular carcinoma.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "ethanol",
      "effect": "subcutaneous metastasis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "percutaneous ethanol injection"
      },
      "relation": "caused",
      "effect": {
        "span": "subcutaneous metastasis along the needle track"
      }
    }
  ]
}
```

### --- id=37 ---

输入文本: METHODS: Three patients with apparent itraconazole-induced liver injury were studied.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "itraconazole",
      "effect": "liver injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "itraconazole"
      },
      "relation": "caused",
      "effect": {
        "span": "liver injury"
      }
    }
  ]
}
```

### --- id=38 ---

输入文本: Lansoprazole-induced thrombocytopenia.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Lansoprazole",
      "effect": "thrombocytopenia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Lansoprazole"
      },
      "relation": "caused",
      "effect": {
        "span": "thrombocytopenia"
      }
    }
  ]
}
```

### --- id=39 ---

输入文本: The most common side effects associated with amifostine are nausea, vomiting, hypotension, hypocalcemia and allergic reactions.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 5
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 5
  },
  "gold_relations": [
    {
      "cause": "amifostine",
      "effect": "allergic reactions"
    },
    {
      "cause": "amifostine",
      "effect": "hypocalcemia"
    },
    {
      "cause": "amifostine",
      "effect": "hypotension"
    },
    {
      "cause": "amifostine",
      "effect": "nausea"
    },
    {
      "cause": "amifostine",
      "effect": "vomiting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "amifostine"
      },
      "relation": "caused",
      "effect": {
        "span": "nausea, vomiting, hypotension, hypocalcemia and allergic reactions"
      }
    }
  ]
}
```

### --- id=40 ---

输入文本: The female patient received clozapine in a daily dose of 400 mg, which induced agranulocytosis after 2 months.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "clozapine",
      "effect": "agranulocytosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "clozapine in a daily dose of 400 mg"
      },
      "relation": "caused",
      "effect": {
        "span": "agranulocytosis"
      }
    }
  ]
}
```

### --- id=41 ---

输入文本: The male patient was treated with 225-mg/day clozapine and the time to the diagnosis of agranulocytosis was 6 weeks.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "clozapine",
      "effect": "agranulocytosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "treated with 225-mg/day clozapine"
      },
      "relation": "caused",
      "effect": {
        "span": "diagnosis of agranulocytosis"
      }
    }
  ]
}
```

### --- id=42 ---

输入文本: Atypical neuroleptic malignant syndrome associated with olanzapine.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "olanzapine",
      "effect": "neuroleptic malignant syndrome"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "olanzapine"
      },
      "relation": "caused",
      "effect": {
        "span": "Atypical neuroleptic malignant syndrome"
      }
    }
  ]
}
```

### --- id=43 ---

输入文本: OBJECTIVE: To present a single case of zuclopenthixol-induced priapism and a literature review.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "zuclopenthixol",
      "effect": "priapism"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "zuclopenthixol"
      },
      "relation": "caused",
      "effect": {
        "span": "priapism"
      }
    }
  ]
}
```

### --- id=44 ---

输入文本: After identification of the index patient, additional inquiry revealed that the patient's mother was hospitalized previously for overwhelming sepsis associated with metamizole use.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "metamizole",
      "effect": "sepsis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "metamizole use"
      },
      "relation": "caused",
      "effect": {
        "span": "overwhelming sepsis"
      }
    }
  ]
}
```

### --- id=45 ---

输入文本: Posterior leukoencephalopathy following cisplatin, bleomycin and vinblastine therapy for germ cell tumor of the ovary.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "bleomycin",
      "effect": "Posterior leukoencephalopathy"
    },
    {
      "cause": "cisplatin",
      "effect": "Posterior leukoencephalopathy"
    },
    {
      "cause": "vinblastine",
      "effect": "Posterior leukoencephalopathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cisplatin, bleomycin and vinblastine therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "Posterior leukoencephalopathy"
      }
    }
  ]
}
```

### --- id=46 ---

输入文本: A 50-year-old diabetic and hypertensive male patient is reported who had ticlopidine-induced marrow aplasia partially responsive to colony-stimulating factors and corticosteroids, but experienced complete recovery with cyclosporine.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "ticlopidine",
      "effect": "marrow aplasia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "ticlopidine"
      },
      "relation": "caused",
      "effect": {
        "span": "marrow aplasia"
      }
    }
  ]
}
```

### --- id=47 ---

输入文本: Two cases of polymorphic ventricular tachycardia induced by the administration of verapamil against paroxysmal supraventricular tachycardia.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "verapamil",
      "effect": "polymorphic ventricular tachycardia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "administration of verapamil"
      },
      "relation": "caused",
      "effect": {
        "span": "polymorphic ventricular tachycardia"
      }
    }
  ]
}
```

### --- id=48 ---

输入文本: The authors report the first case of bucillamine-induced giant mammary hyperplasia.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "bucillamine",
      "effect": "giant mammary hyperplasia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "bucillamine"
      },
      "relation": "caused",
      "effect": {
        "span": "giant mammary hyperplasia"
      }
    }
  ]
}
```

### --- id=49 ---

输入文本: Ticlopidine-induced aplastic anemia: two new case reports, review, and meta-analysis of 55 additional cases.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Ticlopidine",
      "effect": "aplastic anemia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Ticlopidine"
      },
      "relation": "caused",
      "effect": {
        "span": "aplastic anemia"
      }
    }
  ]
}
```

### --- id=50 ---

输入文本: Acute onset of nephrotic syndrome during interferon-alpha retreatment for chronic active hepatitis C.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "interferon-alpha",
      "effect": "nephrotic syndrome"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "interferon-alpha retreatment"
      },
      "relation": "caused",
      "effect": {
        "span": "Acute onset of nephrotic syndrome"
      }
    }
  ]
}
```

### --- id=51 ---

输入文本: Recurrent palmar-plantar erythrodysaesthesia following high-dose cytarabine treatment for acute lymphoblastic leukemia.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "cytarabine",
      "effect": "palmar-plantar erythrodysaesthesia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "high-dose cytarabine treatment"
      },
      "relation": "caused",
      "effect": {
        "span": "Recurrent palmar-plantar erythrodysaesthesia"
      }
    }
  ]
}
```

### --- id=52 ---

输入文本: Anaphylaxis to cisplatin following nine previous uncomplicated cycles.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "cisplatin",
      "effect": "Anaphylaxis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cisplatin"
      },
      "relation": "caused",
      "effect": {
        "span": "Anaphylaxis"
      }
    }
  ]
}
```

### --- id=53 ---

输入文本: Anaphylaxis to cisplatin is an infrequent life-threatening complication which may occur even in patients who have received prior treatment with cisplatin.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "cisplatin",
      "effect": "Anaphylaxis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cisplatin"
      },
      "relation": "caused",
      "effect": {
        "span": "Anaphylaxis"
      }
    }
  ]
}
```

### --- id=54 ---

输入文本: Although isradipine has been associated with hepatocellular injury, there are no reports of fulminant liver failure with this agent, and our patient had been treated for >2 years without signs of toxicity.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "isradipine",
      "effect": "hepatocellular injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "isradipine"
      },
      "relation": "caused",
      "effect": {
        "span": "hepatocellular injury"
      }
    }
  ]
}
```

### --- id=55 ---

输入文本: Fulminant liver failure associated with clarithromycin.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "clarithromycin",
      "effect": "Fulminant liver failure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "clarithromycin"
      },
      "relation": "caused",
      "effect": {
        "span": "Fulminant liver failure"
      }
    }
  ]
}
```

### --- id=56 ---

输入文本: Doxycycline-induced hypoglycemia in a nondiabetic young man.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Doxycycline",
      "effect": "hypoglycemia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Doxycycline"
      },
      "relation": "caused",
      "effect": {
        "span": "hypoglycemia"
      }
    }
  ]
}
```

### --- id=57 ---

输入文本: For patients who suffer from osteogenic sarcoma and have anaphylactic reactions to MTX, this desensitization protocol will allow these patients to continue with needed therapeutic or palliative chemotherapy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "MTX",
      "effect": "anaphylactic reactions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "anaphylactic reactions to MTX"
      },
      "relation": "caused",
      "effect": {
        "span": "this desensitization protocol will allow these patients to continue with needed therapeutic or palliative chemotherapy"
      }
    }
  ]
}
```

### --- id=58 ---

输入文本: Successful desensitization to high-dose methotrexate after systemic anaphylaxis.

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
      "cause": "methotrexate",
      "effect": "systemic anaphylaxis"
    }
  ],
  "pred_triples": []
}
```

### --- id=59 ---

输入文本: Interstitial pneumonitis associated with sirolimus: a dilemma for lung transplantation.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "sirolimus",
      "effect": "Interstitial pneumonitis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "sirolimus"
      },
      "relation": "caused",
      "effect": {
        "span": "Interstitial pneumonitis"
      }
    }
  ]
}
```

### --- id=60 ---

输入文本: This case highlights the need to monitor liver enzymes in patients treated with 6-TG and identifies the need for additional research focused on the mechanism of thiopurine-induced hepatic injury.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "thiopurine",
      "effect": "hepatic injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "thiopurine"
      },
      "relation": "caused",
      "effect": {
        "span": "hepatic injury"
      }
    }
  ]
}
```

### --- id=61 ---

输入文本: Fulminant hepatic failure developed in a 24-year-old black woman who had been treated with propylthiouracil and propranolol for hyperthyroidism.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "propranolol",
      "effect": "Fulminant hepatic failure"
    },
    {
      "cause": "propylthiouracil",
      "effect": "Fulminant hepatic failure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "treated with propylthiouracil and propranolol"
      },
      "relation": "caused",
      "effect": {
        "span": "Fulminant hepatic failure"
      }
    }
  ]
}
```

### --- id=62 ---

输入文本: Fulminant hepatitis and lymphocyte sensitization due to propylthiouracil.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "propylthiouracil",
      "effect": "Fulminant hepatitis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "propylthiouracil"
      },
      "relation": "caused",
      "effect": {
        "span": "Fulminant hepatitis and lymphocyte sensitization"
      }
    }
  ]
}
```

### --- id=63 ---

输入文本: Two cases of childhood-onset schizophrenia associated with clozapine-induced akathisia responsive to beta-blocker treatment are described.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "clozapine",
      "effect": "akathisia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "clozapine"
      },
      "relation": "caused",
      "effect": {
        "span": "akathisia"
      }
    }
  ]
}
```

### --- id=64 ---

输入文本: Antithyroid treatment with propylthiouracil (PTU) resulted in elevated hepatic enzymes and after the 12th week of pregnancy treatment was changed to carbimazole (CBZ).

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "propylthiouracil",
      "effect": "elevated hepatic enzymes"
    },
    {
      "cause": "PTU",
      "effect": "elevated hepatic enzymes"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Antithyroid treatment with propylthiouracil (PTU)"
      },
      "relation": "caused",
      "effect": {
        "span": "elevated hepatic enzymes"
      }
    }
  ]
}
```

### --- id=65 ---

输入文本: Successful treatment with carbimazole of a hyperthyroid pregnancy with hepatic impairment after propylthiouracil administration: a case report.

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
      "cause": "propylthiouracil",
      "effect": "hepatic impairment"
    }
  ],
  "pred_triples": []
}
```

### --- id=66 ---

输入文本: Treatment of carbimazole-induced agranulocytosis and sepsis with granulocyte colony stimulating factor.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "carbimazole",
      "effect": "agranulocytosis"
    },
    {
      "cause": "carbimazole",
      "effect": "sepsis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "carbimazole"
      },
      "relation": "caused",
      "effect": {
        "span": "agranulocytosis"
      }
    }
  ]
}
```

### --- id=67 ---

输入文本: Tacrolimus (FK506)-induced mutism after liver transplant.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "FK506",
      "effect": "mutism"
    },
    {
      "cause": "Tacrolimus",
      "effect": "mutism"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Tacrolimus (FK506)"
      },
      "relation": "caused",
      "effect": {
        "span": "mutism"
      }
    }
  ]
}
```

### --- id=68 ---

输入文本: Intrathecal methotrexate-induced acute cerebellar syndrome.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "methotrexate",
      "effect": "acute cerebellar syndrome"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Intrathecal methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "acute cerebellar syndrome"
      }
    }
  ]
}
```

### --- id=69 ---

输入文本: We describe a patient who developed acute cerebellar syndrome after prophylactic intrathecal methotrexate administration and recovered spontaneously.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "methotrexate",
      "effect": "acute cerebellar syndrome"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "prophylactic intrathecal methotrexate administration"
      },
      "relation": "caused",
      "effect": {
        "span": "acute cerebellar syndrome"
      }
    }
  ]
}
```

### --- id=70 ---

输入文本: Angioimmunoblastic lymphadenopathy with dysproteinemia following doxycycline administration.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "doxycycline",
      "effect": "Angioimmunoblastic lymphadenopathy with dysproteinemia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "doxycycline"
      },
      "relation": "caused",
      "effect": {
        "span": "Angioimmunoblastic lymphadenopathy with dysproteinemia"
      }
    }
  ]
}
```

### --- id=71 ---

输入文本: We report a case of AILD in an 80-year-old male who presented with a generalized pruritic maculopapular eruption and fever following doxycycline administration.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "doxycycline",
      "effect": "AILD"
    },
    {
      "cause": "doxycycline",
      "effect": "fever"
    },
    {
      "cause": "doxycycline",
      "effect": "generalized pruritic maculopapular eruption"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "doxycycline administration"
      },
      "relation": "caused",
      "effect": {
        "span": "generalized pruritic maculopapular eruption and fever"
      }
    }
  ]
}
```

### --- id=72 ---

输入文本: The renal biopsy showed focal segmental glomerulosclerosis, which has only been previously reported in two cases of CML treated with IFNalpha.

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
      "cause": "IFNalpha",
      "effect": "focal segmental glomerulosclerosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=73 ---

输入文本: Severe autoimmune hemolytic anemia following rituximab therapy in a patient with a lymphoproliferative disorder.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "rituximab",
      "effect": "autoimmune hemolytic anemia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "rituximab therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "Severe autoimmune hemolytic anemia"
      }
    }
  ]
}
```

### --- id=74 ---

输入文本: Stevens-Johnson syndrome in a boy with nephrotic syndrome during prednisolone therapy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "prednisolone",
      "effect": "Stevens-Johnson syndrome"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "prednisolone therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "Stevens-Johnson syndrome"
      }
    }
  ]
}
```

### --- id=75 ---

输入文本: We describe a premenopausal woman who, while having tamoxifen due to a diagnosis of in situ ductal carcinoma, developed endometriosis requiring surgery.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "tamoxifen",
      "effect": "endometriosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "tamoxifen"
      },
      "relation": "caused",
      "effect": {
        "span": "endometriosis"
      }
    }
  ]
}
```

### --- id=76 ---

输入文本: Enoxaparin-induced generalized exanthem.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Enoxaparin",
      "effect": "generalized exanthem"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Enoxaparin"
      },
      "relation": "caused",
      "effect": {
        "span": "generalized exanthem"
      }
    }
  ]
}
```

### --- id=77 ---

输入文本: Cefuroxime-induced immune hemolysis.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Cefuroxime",
      "effect": "immune hemolysis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Cefuroxime"
      },
      "relation": "caused",
      "effect": {
        "span": "immune hemolysis"
      }
    }
  ]
}
```

### --- id=78 ---

输入文本: Hyperpigmentation during interferon-alpha therapy for chronic hepatitis C virus infection.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "interferon-alpha",
      "effect": "Hyperpigmentation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "interferon-alpha therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "Hyperpigmentation"
      }
    }
  ]
}
```

### --- id=79 ---

输入文本: Hemodynamic collapse following labetalol administration in preeclampsia.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "labetalol",
      "effect": "Hemodynamic collapse"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "labetalol administration"
      },
      "relation": "caused",
      "effect": {
        "span": "Hemodynamic collapse"
      }
    }
  ]
}
```

### --- id=80 ---

输入文本: Dilated cardiomyopathy associated with chronic overuse of an adrenaline inhaler.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "adrenaline",
      "effect": "Dilated cardiomyopathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "chronic overuse of an adrenaline inhaler"
      },
      "relation": "caused",
      "effect": {
        "span": "Dilated cardiomyopathy"
      }
    }
  ]
}
```

### --- id=81 ---

输入文本: This case report describes a 38-year-old male in whom SIADH was strongly suspected secondary to Tegretol therapy to control a seizure disorder.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "Tegretol",
      "effect": "SIADH"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Tegretol therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "SIADH"
      }
    }
  ]
}
```

### --- id=82 ---

输入文本: Gestational diabetes was no less severe (degree of hyperglycaemia, need for insulin therapy) when associated with norethisterone.

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
      "cause": "norethisterone",
      "effect": "Gestational diabetes"
    }
  ],
  "pred_triples": []
}
```

### --- id=83 ---

输入文本: Skin rash and splinter hemorrhages from ganciclovir.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "ganciclovir",
      "effect": "Skin rash"
    },
    {
      "cause": "ganciclovir",
      "effect": "splinter hemorrhages"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "ganciclovir"
      },
      "relation": "caused",
      "effect": {
        "span": "Skin rash and splinter hemorrhages"
      }
    }
  ]
}
```

### --- id=84 ---

输入文本: Colchicine-induced myopathy in a teenager with familial Mediterranean fever.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Colchicine",
      "effect": "myopathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Colchicine"
      },
      "relation": "caused",
      "effect": {
        "span": "myopathy"
      }
    }
  ]
}
```

### --- id=85 ---

输入文本: A diagnosis of infliximab-induced lupus was made and the drug treatment was withdrawn.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "infliximab",
      "effect": "lupus"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "infliximab"
      },
      "relation": "caused",
      "effect": {
        "span": "lupus"
      }
    }
  ]
}
```

### --- id=86 ---

输入文本: This is the first case, to our knowledge, of onset of prolonged infliximab-induced lupus.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "infliximab",
      "effect": "lupus"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "infliximab"
      },
      "relation": "caused",
      "effect": {
        "span": "lupus"
      }
    }
  ]
}
```

### --- id=87 ---

输入文本: Erythema multiforme associated with phenytoin and cranial radiation therapy: a report of three patients and review of the literature.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "phenytoin",
      "effect": "Erythema multiforme"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "phenytoin and cranial radiation therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "Erythema multiforme"
      }
    }
  ]
}
```

### --- id=88 ---

输入文本: We now present four cases of RSDS in kidney transplant recipients treated with tacrolimus.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "tacrolimus",
      "effect": "RSDS"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "treated with tacrolimus"
      },
      "relation": "caused",
      "effect": {
        "span": "RSDS"
      }
    }
  ]
}
```

### --- id=89 ---

输入文本: Mechanism of topiramate-induced acute-onset myopia and angle closure glaucoma.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "topiramate",
      "effect": "acute-onset myopia"
    },
    {
      "cause": "topiramate",
      "effect": "angle closure glaucoma"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "topiramate"
      },
      "relation": "caused",
      "effect": {
        "span": "acute-onset myopia"
      }
    },
    {
      "cause": {
        "span": "topiramate"
      },
      "relation": "caused",
      "effect": {
        "span": "angle closure glaucoma"
      }
    }
  ]
}
```

### --- id=90 ---

输入文本: Doxycycline-induced photo-onycholysis.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Doxycycline",
      "effect": "photo-onycholysis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Doxycycline"
      },
      "relation": "caused",
      "effect": {
        "span": "photo-onycholysis"
      }
    }
  ]
}
```

### --- id=91 ---

输入文本: Three distinct types of minocycline-induced cutaneous pigmentation have been described.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "minocycline",
      "effect": "cutaneous pigmentation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "minocycline"
      },
      "relation": "caused",
      "effect": {
        "span": "cutaneous pigmentation"
      }
    }
  ]
}
```

### --- id=92 ---

输入文本: We report here a case of TEN after administration of ciprofloxacin.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "ciprofloxacin",
      "effect": "TEN"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "administration of ciprofloxacin"
      },
      "relation": "caused",
      "effect": {
        "span": "TEN"
      }
    }
  ]
}
```

### --- id=93 ---

输入文本: Amifostine-induced fever: case report and review of the literature.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Amifostine",
      "effect": "fever"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Amifostine"
      },
      "relation": "caused",
      "effect": {
        "span": "fever"
      }
    }
  ]
}
```

### --- id=94 ---

输入文本: There have been several reported cases of omeprazole-induced AIN.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "omeprazole",
      "effect": "AIN"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "omeprazole"
      },
      "relation": "caused",
      "effect": {
        "span": "AIN"
      }
    }
  ]
}
```

### --- id=95 ---

输入文本: Fixed drug eruption of the scrotum due to methylphenidate.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "methylphenidate",
      "effect": "Fixed drug eruption of the scrotum"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methylphenidate"
      },
      "relation": "caused",
      "effect": {
        "span": "Fixed drug eruption of the scrotum"
      }
    }
  ]
}
```

### --- id=96 ---

输入文本: Cerebral infarcts in a pediatric patient secondary to phenylpropanolamine, a recalled medication.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "phenylpropanolamine",
      "effect": "Cerebral infarcts"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "phenylpropanolamine"
      },
      "relation": "caused",
      "effect": {
        "span": "Cerebral infarcts"
      }
    }
  ]
}
```

### --- id=97 ---

输入文本: OBJECTIVE: To report a case of ciprofloxacin-induced psychosis and to discuss occurrence rates, risk factors, possible etiologies, preventive measures, and treatment courses for this adverse reaction.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "ciprofloxacin",
      "effect": "psychosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "ciprofloxacin"
      },
      "relation": "caused",
      "effect": {
        "span": "psychosis"
      }
    }
  ]
}
```

### --- id=98 ---

输入文本: Agranulocytosis induced by vancomycin in an ESRD patient on CAPD.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "vancomycin",
      "effect": "Agranulocytosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "vancomycin"
      },
      "relation": "caused",
      "effect": {
        "span": "Agranulocytosis"
      }
    }
  ]
}
```

### --- id=99 ---

输入文本: Heat stroke in schizophrenia during clozapine treatment: rapid recognition and management.

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
      "cause": "clozapine",
      "effect": "Heat stroke"
    }
  ],
  "pred_triples": []
}
```

### --- id=100 ---

输入文本: The literature search found 12 cases of radiation recall caused by gemcitabine.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "gemcitabine",
      "effect": "radiation recall"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "gemcitabine"
      },
      "relation": "caused",
      "effect": {
        "span": "radiation recall"
      }
    }
  ]
}
```
