# causenet first 100 eval report

## 配置
```json
{
  "label": "causenet first 100",
  "model": "qwen/qwen3.5-35b-a3b",
  "dataset": "causenet",
  "sample_count": 100,
  "prompt_name": "v3",
  "use_rag": false,
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
================ causenet first 100 final report ================
样本总数: 100
  Gold 含因果: 100 | Pred 含因果: 88
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.880
  Precision: 1.000
  Recall   : 0.880
  F1       : 0.936
  (TP=88, TN=0, FP=0, FN=12)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 100
    Gold triples: 121 | Pred triples: 112
    Precision: 0.098
    Recall   : 0.091
    F1       : 0.094
    (TP=11, FP=101, FN=110)
  [anchor_window] (primary)
    样本数: 100
    Gold triples: 121 | Pred triples: 112
    Precision: 0.589
    Recall   : 0.545
    F1       : 0.567
    (TP=66, FP=46, FN=55)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 88
    Gold triples: 108 | Pred triples: 112
    Precision: 0.098
    Recall   : 0.102
    F1       : 0.100
    (TP=11, FP=101, FN=97)
  [anchor_window] (primary)
    样本数: 88
    Gold triples: 108 | Pred triples: 112
    Precision: 0.589
    Recall   : 0.611
    F1       : 0.600
    (TP=66, FP=46, FN=42)
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

输入文本: Drug users also may become involved in risky sexual behaviors, which could lead to the spread of HIV, the virus that causes AIDS.

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
      "cause": "virus",
      "effect": "AIDS"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "risky sexual behaviors"
      },
      "relation": "caused",
      "effect": {
        "span": "the spread of HIV"
      }
    }
  ]
}
```

### --- id=2 ---

输入文本: Stress associated with training, racing, barking and travelling will also cause electrolytes to become depleted, particularly during the warmer months of the year.

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
      "cause": "training",
      "effect": "Stress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Stress associated with training, racing, barking and travelling"
      },
      "relation": "caused",
      "effect": {
        "span": "electrolytes to become depleted"
      }
    }
  ]
}
```

### --- id=3 ---

输入文本: However, the use of such medications has been associated with side effects such as weight gain that may increase the likelihood of diabetes and cardiovascular disease, sedation and movement disorders.

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
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "use of such medications",
      "effect": "side effects"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the use of such medications has been associated with side effects such as weight gain"
      },
      "relation": "caused",
      "effect": {
        "span": "that may increase the likelihood of diabetes and cardiovascular disease"
      }
    },
    {
      "cause": {
        "span": "the use of such medications has been associated with side effects such as sedation and movement disorders"
      },
      "relation": "caused",
      "effect": {
        "span": ""
      }
    }
  ]
}
```

### --- id=4 ---

输入文本: In ancient Rome, Galen, the physician to the gladiators, observed that bereavement and depression from the death of a spouse could itself lead to an early death.

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
      "cause": "depression",
      "effect": "early death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "bereavement and depression from the death of a spouse"
      },
      "relation": "caused",
      "effect": {
        "span": "lead to an early death"
      }
    }
  ]
}
```

### --- id=5 ---

输入文本: Photographer: Daniel Acker/Bloomberg ]According to a recent report, Johnson & Johnson sold their Gynecare Prolift mesh for several years before obtaining FDA approval, and the manufacturer now faces a number of product liability lawsuits brought by women who suffered complications allegedly caused by design defects with the vaginal surgical mesh.

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
      "cause": "design defects",
      "effect": "complications"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "design defects with the vaginal surgical mesh"
      },
      "relation": "caused",
      "effect": {
        "span": "women who suffered complications"
      }
    }
  ]
}
```

### --- id=6 ---

输入文本: If a return is due to our error, we will reimburse reasonable freight charges.

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
      "cause": "error",
      "effect": "return"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a return is due to our error"
      },
      "relation": "caused",
      "effect": {
        "span": "we will reimburse reasonable freight charges"
      }
    }
  ]
}
```

### --- id=7 ---

输入文本: According to reports by Livingston and various other researchers, cancer is caused by pleomorphic, cell wall deficient bacteria.

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
      "cause": "cell wall deficient bacteria",
      "effect": "cancer"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "pleomorphic, cell wall deficient bacteria"
      },
      "relation": "caused",
      "effect": {
        "span": "cancer"
      }
    }
  ]
}
```

### --- id=8 ---

输入文本: Many criminal justice career law enforcement officers witness death and suffering resulting from accidents and criminal behavior.

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
      "cause": "accidents",
      "effect": "death"
    },
    {
      "cause": "criminal behavior",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "accidents and criminal behavior"
      },
      "relation": "caused",
      "effect": {
        "span": "death and suffering"
      }
    }
  ]
}
```

### --- id=9 ---

输入文本: FINDINGS: UCLA scientists have devised a novel way to correct abnormal gene splicing – a common mutation that often leads to disease.

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
      "cause": "mutation",
      "effect": "disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "abnormal gene splicing"
      },
      "relation": "caused",
      "effect": {
        "span": "often leads to disease"
      }
    }
  ]
}
```

### --- id=10 ---

输入文本: The conclusion remains that whether the hazard, if one exists, is due to exposure to electromagnetic fields or to some chemical associated with the work is impossible to decide at the present."

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
      "cause": "chemical",
      "effect": "hazard"
    }
  ],
  "pred_triples": []
}
```

### --- id=11 ---

输入文本: Lead poisoning can cause damage to the brain or nervous system, interfere with growth, and can cause hearing loss and learning disabilities.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Lead poisoning",
      "effect": "hearing loss"
    },
    {
      "cause": "Lead poisoning",
      "effect": "damage to the brain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Lead poisoning"
      },
      "relation": "caused",
      "effect": {
        "span": "damage to the brain or nervous system"
      }
    },
    {
      "cause": {
        "span": "Lead poisoning"
      },
      "relation": "caused",
      "effect": {
        "span": "interfere with growth"
      }
    },
    {
      "cause": {
        "span": "Lead poisoning"
      },
      "relation": "caused",
      "effect": {
        "span": "hearing loss and learning disabilities"
      }
    }
  ]
}
```

### --- id=12 ---

输入文本: BJ Hardick teaches in his Maximized Living Makeover that high cholesterol is NOT the cause of heart disease or heart attacks.

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
      "cause": "high cholesterol",
      "effect": "heart disease"
    },
    {
      "cause": "high cholesterol",
      "effect": "heart attacks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "high cholesterol"
      },
      "relation": "caused",
      "effect": {
        "span": "heart disease or heart attacks"
      }
    }
  ]
}
```

### --- id=13 ---

输入文本: Diagnosis was largely the result of observation and deduction, and treatment was empirical.

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
      "cause": "observation",
      "effect": "Diagnosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "observation and deduction"
      },
      "relation": "caused",
      "effect": {
        "span": "Diagnosis was largely"
      }
    }
  ]
}
```

### --- id=14 ---

输入文本: - Not if the weight loss caused the problem.

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
      "cause": "weight loss",
      "effect": "problem"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the weight loss"
      },
      "relation": "caused",
      "effect": {
        "span": "the problem"
      }
    }
  ]
}
```

### --- id=15 ---

输入文本: No woman was transfered to a higher level of care due to symptoms associated with misoprostol.

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
      "cause": "misoprostol",
      "effect": "symptoms"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "symptoms associated with misoprostol"
      },
      "relation": "caused",
      "effect": {
        "span": "No woman was transfered to a higher level of care"
      }
    }
  ]
}
```

### --- id=16 ---

输入文本: Many diseases and health problems today are caused by lack of exercise.

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
      "cause": "lack of exercise",
      "effect": "health problems"
    },
    {
      "cause": "lack of exercise",
      "effect": "diseases"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "lack of exercise"
      },
      "relation": "caused",
      "effect": {
        "span": "Many diseases and health problems today are caused"
      }
    }
  ]
}
```

### --- id=17 ---

输入文本: Hyperinsulinemia resulting from insulin resistance increases the synthesis of fatty acids in hepatocytes by increasing glycolysis and favors the accumulation of triglycerides within hepatocytes by decreasing hepatic production of apolipoprotein B-10017.

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
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "insulin resistance",
      "effect": "Hyperinsulinemia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Hyperinsulinemia resulting from insulin resistance"
      },
      "relation": "caused",
      "effect": {
        "span": "increases the synthesis of fatty acids in hepatocytes by increasing glycolysis"
      }
    },
    {
      "cause": {
        "span": "Hyperinsulinemia resulting from insulin resistance"
      },
      "relation": "caused",
      "effect": {
        "span": "favors the accumulation of triglycerides within hepatocytes by decreasing hepatic production of apolipoprotein B-10017"
      }
    }
  ]
}
```

### --- id=18 ---

输入文本: The Emphysema may cause chronic bronchitis and the strain can lead to heart and lung failure.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Emphysema",
      "effect": "chronic bronchitis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Emphysema"
      },
      "relation": "caused",
      "effect": {
        "span": "chronic bronchitis"
      }
    },
    {
      "cause": {
        "span": "the strain"
      },
      "relation": "caused",
      "effect": {
        "span": "heart and lung failure"
      }
    }
  ]
}
```

### --- id=19 ---

输入文本: This virus is the cause of African swine fever.

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
      "cause": "virus",
      "effect": "African swine fever"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "This virus"
      },
      "relation": "caused",
      "effect": {
        "span": "African swine fever"
      }
    }
  ]
}
```

### --- id=20 ---

输入文本: Iron overload can cause deterioration of the gut lining, vomiting and diarrhoea, abdominal and joint pain, liver damage, loss of weight, and intense fatigue.343 Acute doses as low as 3 g can cause death in children.

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
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "liver damage",
      "effect": "death in children"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Iron overload"
      },
      "relation": "caused",
      "effect": {
        "span": "deterioration of the gut lining, vomiting and diarrhoea, abdominal and joint pain, liver damage, loss of weight, and intense fatigue"
      }
    },
    {
      "cause": {
        "span": "Acute doses as low as 3 g"
      },
      "relation": "caused",
      "effect": {
        "span": "death in children"
      }
    }
  ]
}
```

### --- id=21 ---

输入文本: Accidental or deliberate application or ingestion by a child or adolescent will cause respiratory depression that could result in death.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "respiratory depression",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Accidental or deliberate application or ingestion by a child or adolescent"
      },
      "relation": "caused",
      "effect": {
        "span": "respiratory depression"
      }
    },
    {
      "cause": {
        "span": "respiratory depression"
      },
      "relation": "caused",
      "effect": {
        "span": "death"
      }
    }
  ]
}
```

### --- id=22 ---

输入文本: Depression can cause sleeplessness and excessive energy, high school students.

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
      "cause": "Depression",
      "effect": "sleeplessness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Depression"
      },
      "relation": "caused",
      "effect": {
        "span": "sleeplessness and excessive energy"
      }
    }
  ]
}
```

### --- id=23 ---

输入文本: Various studies have examined distress associated with tinnitus (e.g., symptom distress, sleep loss [4], hearing difficulties, and psychological problems [5]).

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
      "cause": "tinnitus",
      "effect": "distress"
    }
  ],
  "pred_triples": []
}
```

### --- id=24 ---

输入文本: Higher concentrations can lead to unconsciousness and coma after prolonged exposure.

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
      "cause": "Higher concentrations",
      "effect": "unconsciousness"
    },
    {
      "cause": "Higher concentrations",
      "effect": "coma"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Higher concentrations"
      },
      "relation": "caused",
      "effect": {
        "span": "unconsciousness and coma after prolonged exposure"
      }
    }
  ]
}
```

### --- id=25 ---

输入文本: In men, urethritis is caused by gonorrhea and chlamydia.

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
      "cause": "chlamydia",
      "effect": "urethritis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "gonorrhea and chlamydia"
      },
      "relation": "caused",
      "effect": {
        "span": "urethritis"
      }
    }
  ]
}
```

### --- id=26 ---

输入文本: The subject policy was applicable only to claims for bodily injury and property damage caused by an "occurrence", which was defined as "an accident, including continuous or repeated exposure to substantially the same general harmful conditions".

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
      "cause": "occurrence",
      "effect": "bodily injury"
    }
  ],
  "pred_triples": []
}
```

### --- id=27 ---

输入文本: Prohibition of photography seemed an act worthy of the closed societies which cultivated the hatred that brought forth the attack.

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
      "cause": "hatred",
      "effect": "attack"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the closed societies which cultivated the hatred"
      },
      "relation": "caused",
      "effect": {
        "span": "brought forth the attack"
      }
    }
  ]
}
```

### --- id=28 ---

输入文本: Fiji, it says, has problems with typhoid and other diseases caused by a lack of clean drinking water.

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
      "cause": "lack of clean drinking water",
      "effect": "diseases"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a lack of clean drinking water"
      },
      "relation": "caused",
      "effect": {
        "span": "typhoid and other diseases"
      }
    }
  ]
}
```

### --- id=29 ---

输入文本: Evidence suggests that delirium is associated with long-term poor outcome but delirium often occurs in individuals with more severe underlying disease.

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
      "cause": "delirium",
      "effect": "delirium"
    }
  ],
  "pred_triples": []
}
```

### --- id=30 ---

输入文本: Viral infections can lead to diarrhea and gastroenteritis for which specific anti-diarrhea dietary treatment may be urgently required.

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
      "cause": "Viral infections",
      "effect": "diarrhea"
    },
    {
      "cause": "Viral infections",
      "effect": "gastroenteritis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Viral infections"
      },
      "relation": "caused",
      "effect": {
        "span": "diarrhea and gastroenteritis"
      }
    }
  ]
}
```

### --- id=31 ---

输入文本: Diabetes: Diabetes is associated with high blood pressure and interferes with the ability to break down clots, increasing the risk of ischemic stroke Alli 90 Pills X 120 Mg: 198.81 $.

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
      "cause": "Diabetes",
      "effect": "high blood pressure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Diabetes is associated with high blood pressure and interferes with the ability to break down clots"
      },
      "relation": "caused",
      "effect": {
        "span": "increasing the risk of ischemic stroke"
      }
    }
  ]
}
```

### --- id=32 ---

输入文本: In 1840, a devastating fire caused a panic that led to many deaths, and Israeli officials became especially concerned about the danger with the expected crush of tourists arriving for the year 2000 celebrations.

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
      "cause": "panic",
      "effect": "deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a devastating fire"
      },
      "relation": "caused",
      "effect": {
        "span": "a panic"
      }
    },
    {
      "cause": {
        "span": "a panic"
      },
      "relation": "caused",
      "effect": {
        "span": "many deaths"
      }
    }
  ]
}
```

### --- id=33 ---

输入文本: But the pain caused by a heartbreak is so extreme at times that it makes us give them a false sense of having a 'higher power' than they actually deserve or possess.

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
      "cause": "heartbreak",
      "effect": "pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the pain caused by a heartbreak"
      },
      "relation": "caused",
      "effect": {
        "span": "it makes us give them a false sense of having a 'higher power' than they actually deserve or possess"
      }
    }
  ]
}
```

### --- id=34 ---

输入文本: Other thing is that mesothelioma is generally caused by the inhalation of dust from asbestos, which is a extremely dangerous material.

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
      "cause": "inhalation of dust from asbestos",
      "effect": "mesothelioma"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the inhalation of dust from asbestos"
      },
      "relation": "caused",
      "effect": {
        "span": "mesothelioma is generally caused"
      }
    }
  ]
}
```

### --- id=35 ---

输入文本: Diseases associated with this genus include cutaneous lesions.

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
      "cause": "genus",
      "effect": "Diseases"
    }
  ],
  "pred_triples": []
}
```

### --- id=36 ---

输入文本: This pay was used to assist with costs associated with the cleaning and replacing of clothes that were damaged while fighting fires.

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
      "cause": "cleaning",
      "effect": "costs"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "fighting fires"
      },
      "relation": "caused",
      "effect": {
        "span": "clothes that were damaged"
      }
    },
    {
      "cause": {
        "span": "This pay was used to assist with costs associated with the cleaning and replacing of clothes that were damaged while fighting fires"
      },
      "relation": "caused",
      "effect": {
        "span": "assist with costs associated with the cleaning and replacing of clothes"
      }
    }
  ]
}
```

### --- id=37 ---

输入文本: Muscle weakness, fatigue and, in particular, spasm and spasticity are cardinal features of MS and, as already noted, can be associated with pain.

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
      "cause": "fatigue",
      "effect": "pain"
    },
    {
      "cause": "Muscle weakness",
      "effect": "pain"
    }
  ],
  "pred_triples": []
}
```

### --- id=38 ---

输入文本: chronic fatigue syndrome: a disorder that causes extreme fatigue.

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
      "cause": "disorder",
      "effect": "extreme fatigue"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a disorder"
      },
      "relation": "caused",
      "effect": {
        "span": "extreme fatigue"
      }
    }
  ]
}
```

### --- id=39 ---

输入文本: On a pack of Kool menthol the sergeon Generals warning states that "smoking causes lung cancer, heart disease, emphysema, and may complicate pregnancy".

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
      "cause": "smoking",
      "effect": "lung cancer"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "smoking"
      },
      "relation": "caused",
      "effect": {
        "span": "lung cancer, heart disease, emphysema, and may complicate pregnancy"
      }
    }
  ]
}
```

### --- id=40 ---

输入文本: Often the sharp pain and lumps are caused by cysts or clogged glands.

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
      "cause": "cysts",
      "effect": "lumps"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cysts or clogged glands"
      },
      "relation": "caused",
      "effect": {
        "span": "the sharp pain and lumps"
      }
    }
  ]
}
```

### --- id=41 ---

输入文本: Both conditions tend to cause confusion and this disorientation often permits the subject to experience vivid, ethereal out of body experiences.

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
      "cause": "conditions",
      "effect": "confusion"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Both conditions"
      },
      "relation": "caused",
      "effect": {
        "span": "confusion"
      }
    },
    {
      "cause": {
        "span": "this disorientation often permits the subject to experience vivid, ethereal out of body experiences"
      },
      "relation": "caused",
      "effect": {
        "span": "vivid, ethereal out of body experiences"
      }
    }
  ]
}
```

### --- id=42 ---

输入文本: The mutation which causes the disease is an expansion in the number of repetitions of three nucleotides, C, A, and G in exon 1 of the huntingtin gene.

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
      "cause": "mutation",
      "effect": "disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an expansion in the number of repetitions of three nucleotides, C, A, and G in exon 1 of the huntingtin gene"
      },
      "relation": "caused",
      "effect": {
        "span": "the disease"
      }
    }
  ]
}
```

### --- id=43 ---

输入文本: The includes loss of data resulting from delays, nondeliveries, wrong delivery, and any and all service interruptions caused by 123easyhost and its employees.

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
      "cause": "delays",
      "effect": "loss of data"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "delays, nondeliveries, wrong delivery, and any and all service interruptions caused by 123easyhost and its employees"
      },
      "relation": "caused",
      "effect": {
        "span": "loss of data"
      }
    }
  ]
}
```

### --- id=44 ---

输入文本: A large earthquake will certainly cause much more damage.

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
      "cause": "large earthquake",
      "effect": "damage"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "A large earthquake"
      },
      "relation": "caused",
      "effect": {
        "span": "will certainly cause much more damage"
      }
    }
  ]
}
```

### --- id=45 ---

输入文本: Before the 1850s, balance and vertigo were attributed to the central nervous system, and disorders of balance were often considered psychiatric illnesses, sometimes called “apoplectic cerebral congestion.”

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
      "cause": "central nervous system",
      "effect": "vertigo"
    }
  ],
  "pred_triples": []
}
```

### --- id=46 ---

输入文本: This is one of the best alternatives to prescription medications that can sometimes be very addictive and can cause harmful side effects as well.

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
      "cause": "prescription medications",
      "effect": "harmful side effects"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "very addictive"
      },
      "relation": "caused",
      "effect": {
        "span": "harmful side effects"
      }
    }
  ]
}
```

### --- id=47 ---

输入文本: It is a frank compendium of survival in a state of dwindling expectations for, while migration is sometimes a result of war or natural disasters, it is most often the condition of economics.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "war",
      "effect": "migration"
    },
    {
      "cause": "natural disasters",
      "effect": "migration"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "war or natural disasters"
      },
      "relation": "caused",
      "effect": {
        "span": "migration is sometimes a result"
      }
    },
    {
      "cause": {
        "span": "the condition of economics"
      },
      "relation": "caused",
      "effect": {
        "span": "it is most often the [result]"
      }
    }
  ]
}
```

### --- id=48 ---

输入文本: Even someone who has developed chest pain caused by narrowed coronary arteries (known as angina) can enroll in a cardiac rehab program.

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
      "cause": "narrowed coronary arteries",
      "effect": "chest pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "narrowed coronary arteries"
      },
      "relation": "caused",
      "effect": {
        "span": "chest pain"
      }
    }
  ]
}
```

### --- id=49 ---

输入文本: Improper caring for teeth leads to development of cavities and defective teeth.

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
      "cause": "Improper caring for teeth",
      "effect": "development of cavities"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Improper caring for teeth"
      },
      "relation": "caused",
      "effect": {
        "span": "development of cavities and defective teeth"
      }
    }
  ]
}
```

### --- id=50 ---

输入文本: Acne scars caused by loss of tissue are more common than marks resulting from increased tissue formation.

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
      "cause": "loss of tissue",
      "effect": "Acne scars"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "loss of tissue"
      },
      "relation": "caused",
      "effect": {
        "span": "Acne scars caused by loss of tissue are more common than marks resulting from increased tissue formation"
      }
    },
    {
      "cause": {
        "span": "increased tissue formation"
      },
      "relation": "caused",
      "effect": {
        "span": "marks resulting from increased tissue formation"
      }
    }
  ]
}
```

### --- id=51 ---

输入文本: Scarce adverse reactions out of Alprazolam side effects government contain shivers, slurred talk, unreadable perspective, abdominal aches, hallucinations, urination complications, loss of memory, dilemma, unnatural monthly periods, withdrawal leading to convulsions, sore chests and also milk products release.

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
      "cause": "withdrawal",
      "effect": "convulsions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "withdrawal"
      },
      "relation": "caused",
      "effect": {
        "span": "convulsions"
      }
    }
  ]
}
```

### --- id=52 ---

输入文本: During these weeks, posters and brochures on breast cancer knowledge, the harm caused by bad habits, and the benefit of healthy life styles will be distributed as target objectives by volunteers.

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
      "cause": "bad habits",
      "effect": "harm"
    }
  ],
  "pred_triples": []
}
```

### --- id=53 ---

输入文本: Auto accidents are consistently a leading cause of injury and death in the United States.

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
      "cause": "Auto accidents",
      "effect": "death"
    },
    {
      "cause": "Auto accidents",
      "effect": "injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Auto accidents"
      },
      "relation": "caused",
      "effect": {
        "span": "a leading cause of injury and death in the United States"
      }
    }
  ]
}
```

### --- id=54 ---

输入文本: In addition to these eight deaths associated directly with the October 1 earthquake, a man was reportedly killed when he jumped, from fear, out of the window on the second floor of a building.

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
      "cause": "October 1 earthquake",
      "effect": "eight deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he jumped, from fear"
      },
      "relation": "caused",
      "effect": {
        "span": "a man was reportedly killed"
      }
    }
  ]
}
```

### --- id=55 ---

输入文本: Most of unexplained deaths (73) were classified as Sudden Infant Death Syndrome, while out of 44 deaths with identified cause 22 were caused by infections, 13 by pre- and antenatal conditions, and 8 by seizures.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "infections",
      "effect": "deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "infections"
      },
      "relation": "caused",
      "effect": {
        "span": "22 were caused by infections"
      }
    },
    {
      "cause": {
        "span": "pre- and antenatal conditions"
      },
      "relation": "caused",
      "effect": {
        "span": "13 [were caused] by pre- and antenatal conditions"
      }
    },
    {
      "cause": {
        "span": "seizures"
      },
      "relation": "caused",
      "effect": {
        "span": "8 [were caused] by seizures"
      }
    }
  ]
}
```

### --- id=56 ---

输入文本: Vertigo caused by migraine can often be treated with medication.

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
      "cause": "migraine",
      "effect": "Vertigo"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "migraine"
      },
      "relation": "caused",
      "effect": {
        "span": "Vertigo"
      }
    }
  ]
}
```

### --- id=57 ---

输入文本: Modern life that tends to cause stress is one of the suspected causes of the high cold cough disease cases in large cities.

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
      "cause": "Modern life",
      "effect": "stress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Modern life that tends to cause stress"
      },
      "relation": "caused",
      "effect": {
        "span": "the high cold cough disease cases in large cities"
      }
    }
  ]
}
```

### --- id=58 ---

输入文本: At the nephrotic syndrome caused by an amyloidosis, a diabetic glomerulosclerosis, a clottage of renal veins, paraneoplastic and paratubercular processes, immunodepressants are contraindicative, therefore the specified conditions should be excluded before the beginning of such treatment.

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
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "amyloidosis",
      "effect": "nephrotic syndrome"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "At the nephrotic syndrome caused by an amyloidosis, a diabetic glomerulosclerosis, a clottage of renal veins, paraneoplastic and paratubercular processes"
      },
      "relation": "caused",
      "effect": {
        "span": "immunodepressants are contraindicative"
      }
    },
    {
      "cause": {
        "span": "immunodepressants are contraindicative"
      },
      "relation": "caused",
      "effect": {
        "span": "the specified conditions should be excluded before the beginning of such treatment"
      }
    }
  ]
}
```

### --- id=59 ---

输入文本: TLR1 is associated with infections caused by bacteria in both humans and mice, and this gene is of interest to researchers because genetic variation in it is associated with increased Gram-positive bacterial infections, organ failure, and death.

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
      "cause": "bacteria",
      "effect": "infections"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "genetic variation in it"
      },
      "relation": "caused",
      "effect": {
        "span": "increased Gram-positive bacterial infections, organ failure, and death"
      }
    }
  ]
}
```

### --- id=60 ---

输入文本: … Autism is caused by too many vaccines given too soon.”

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
      "cause": "vaccines",
      "effect": "Autism"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "too many vaccines given too soon"
      },
      "relation": "caused",
      "effect": {
        "span": "Autism"
      }
    }
  ]
}
```

### --- id=61 ---

输入文本: She had a really hard life and I think her death was probably caused by drugs.

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
      "cause": "drugs",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "her death"
      }
    }
  ]
}
```

### --- id=62 ---

输入文本: The thinking that a mom can’t breastfeed while pregnant comes from the fact that the uterus contracts during breastfeeding, and the possibility exists that contractions can cause early labor or miscarriage.

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
      "cause": "contractions",
      "effect": "miscarriage"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the uterus contracts during breastfeeding"
      },
      "relation": "caused",
      "effect": {
        "span": "contractions can cause early labor or miscarriage"
      }
    }
  ]
}
```

### --- id=63 ---

输入文本: Later, in graduate school, I often experienced shoulder and neck pain, which I attributed to the long hours of studying, hunched over books in the library.

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
      "cause": "long hours",
      "effect": "neck pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the long hours of studying, hunched over books in the library"
      },
      "relation": "caused",
      "effect": {
        "span": "I often experienced shoulder and neck pain"
      }
    }
  ]
}
```

### --- id=64 ---

输入文本: Heartburn often causes discomfort in the later months of pregnancy.

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
      "cause": "Heartburn",
      "effect": "discomfort"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Heartburn"
      },
      "relation": "caused",
      "effect": {
        "span": "discomfort in the later months of pregnancy"
      }
    }
  ]
}
```

### --- id=65 ---

输入文本: In this patch of woodland near Grafton, Mass., Telford counts how many of the deer ticks clinging to his bug-catcher are likely carrying the bacterium that causes Lyme disease.

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
      "cause": "bacterium",
      "effect": "Lyme disease"
    }
  ],
  "pred_triples": []
}
```

### --- id=66 ---

输入文本: An attack on 24 November in downtown Phnom Penh, Cambodia, resulted in deaths and injuries.

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
      "cause": "attack",
      "effect": "injuries"
    },
    {
      "cause": "attack",
      "effect": "deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "An attack on 24 November in downtown Phnom Penh, Cambodia"
      },
      "relation": "caused",
      "effect": {
        "span": "resulted in deaths and injuries"
      }
    }
  ]
}
```

### --- id=67 ---

输入文本: The data from China suggest that deaths from ischemic heart disease make up a much smaller proportion of the total number of deaths caused by tobacco than in the West, while respiratory diseases and cancers account for most of the deaths.

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
      "cause": "tobacco",
      "effect": "deaths"
    }
  ],
  "pred_triples": []
}
```

### --- id=68 ---

输入文本: In general the consequences of the fall was that sin entered man and therefore death, which is the result of sin.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "sin",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the fall"
      },
      "relation": "caused",
      "effect": {
        "span": "sin entered man and therefore death"
      }
    },
    {
      "cause": {
        "span": "sin"
      },
      "relation": "caused",
      "effect": {
        "span": "death"
      }
    }
  ]
}
```

### --- id=69 ---

输入文本: Fractures can result in serious complications including pain, loss of mobility, and death.

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
      "cause": "Fractures",
      "effect": "serious complications"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Fractures"
      },
      "relation": "caused",
      "effect": {
        "span": "result in serious complications including pain, loss of mobility, and death"
      }
    }
  ]
}
```

### --- id=70 ---

输入文本: Smoking is the leading preventable cause of disease and death in the United States.

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
      "cause": "Smoking",
      "effect": "death"
    },
    {
      "cause": "Smoking",
      "effect": "disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Smoking"
      },
      "relation": "caused",
      "effect": {
        "span": "the leading preventable cause of disease and death in the United States"
      }
    }
  ]
}
```

### --- id=71 ---

输入文本: For example, if you are stressed, and people who have a very serious illness usually are stressed, or if you are depressed, we know depression is also associated with memory problems and cognitive problems.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "depression",
      "effect": "memory problems"
    },
    {
      "cause": "depression",
      "effect": "cognitive problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "people who have a very serious illness usually are stressed"
      },
      "relation": "caused",
      "effect": {
        "span": "you are stressed"
      }
    },
    {
      "cause": {
        "span": "depression"
      },
      "relation": "caused",
      "effect": {
        "span": "memory problems and cognitive problems"
      }
    }
  ]
}
```

### --- id=72 ---

输入文本: METRONIDAZOLE will cause vomiting, diarrhea and other related problems.

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
      "cause": "METRONIDAZOLE",
      "effect": "vomiting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "METRONIDAZOLE"
      },
      "relation": "caused",
      "effect": {
        "span": "will cause vomiting, diarrhea and other related problems"
      }
    }
  ]
}
```

### --- id=73 ---

输入文本: Complications of surgery Both surgical procedures can result in complications.

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
      "cause": "surgical procedures",
      "effect": "Complications"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Both surgical procedures"
      },
      "relation": "caused",
      "effect": {
        "span": "result in complications"
      }
    }
  ]
}
```

### --- id=74 ---

输入文本: The bacteria that cause scarlet fever make a toxin that results in a skin rash.

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
      "cause": "toxin",
      "effect": "skin rash"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The bacteria that cause scarlet fever make a toxin"
      },
      "relation": "caused",
      "effect": {
        "span": "a skin rash"
      }
    }
  ]
}
```

### --- id=75 ---

输入文本: In additional studies it was documented that EPO may be effective in patients with severe anemia with normal renal function, e.g. in the treatment of anemia associated with multiple myeloma, neoplastic bone marrow infiltration, in AIDS patients treaed with zidovudine (AZT), in chronic rheumatoid arthritis, in correcting chemiotherapy-induced anemia or anemia associated with cancer.

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
      "cause": "multiple myeloma",
      "effect": "anemia"
    }
  ],
  "pred_triples": []
}
```

### --- id=76 ---

输入文本: INTRODUCTION: Exposure to secondhand smoke causes disease and premature death.

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
      "cause": "Exposure to secondhand smoke",
      "effect": "premature death"
    },
    {
      "cause": "Exposure to secondhand smoke",
      "effect": "disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Exposure to secondhand smoke"
      },
      "relation": "caused",
      "effect": {
        "span": "disease and premature death"
      }
    }
  ]
}
```

### --- id=77 ---

输入文本: Religion has been the cause of so many wars, so many deaths.

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
      "cause": "Religion",
      "effect": "wars"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Religion"
      },
      "relation": "caused",
      "effect": {
        "span": "so many wars, so many deaths"
      }
    }
  ]
}
```

### --- id=78 ---

输入文本: An itchy scalp may result in hair loss, therefore you should find a remedy as soon as possible.

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
      "cause": "itchy scalp",
      "effect": "hair loss"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "An itchy scalp"
      },
      "relation": "caused",
      "effect": {
        "span": "hair loss"
      }
    }
  ]
}
```

### --- id=79 ---

输入文本: Skin allergies caused by some products or due to environmental aggressors may cause sensitivity in your skin.

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
      "cause": "products",
      "effect": "Skin allergies"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Skin allergies caused by some products or due to environmental aggressors"
      },
      "relation": "caused",
      "effect": {
        "span": "may cause sensitivity in your skin"
      }
    }
  ]
}
```

### --- id=80 ---

输入文本: Plaintiff’s late husband died of injuries resulting from his exposure to asbestos aboard the USS Hornet.

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
      "cause": "exposure to asbestos",
      "effect": "injuries"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "his exposure to asbestos aboard the USS Hornet"
      },
      "relation": "caused",
      "effect": {
        "span": "Plaintiff's late husband died of injuries"
      }
    }
  ]
}
```

### --- id=81 ---

输入文本: This disease can cause similar symptoms and is diagnosed in breeds that are also predisposed to portosystemic shunts.

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
      "cause": "disease",
      "effect": "similar symptoms"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "This disease"
      },
      "relation": "caused",
      "effect": {
        "span": "similar symptoms"
      }
    }
  ]
}
```

### --- id=82 ---

输入文本: Heart disease is the leading cause of death for men and women in the US.

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
      "cause": "Heart disease",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Heart disease"
      },
      "relation": "caused",
      "effect": {
        "span": "the leading cause of death for men and women in the US"
      }
    }
  ]
}
```

### --- id=83 ---

输入文本: This might be interpreted, perhaps naively, as simply that the state is open alike to all religions, that �each is permitted to worship his maker after his own judgment�, in the eloquent words of John Tyler, tenth President of the United States.9 Such separation has been interpreted less benignly as hostility to religion and all morality associated with religion.

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
      "cause": "religion",
      "effect": "morality"
    }
  ],
  "pred_triples": []
}
```

### --- id=84 ---

输入文本: He was in good health, until about 3 months ago, when he was stricken down with a complication of diseases causing his death.

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
      "cause": "complication of diseases",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he was stricken down with a complication of diseases"
      },
      "relation": "caused",
      "effect": {
        "span": "his death"
      }
    }
  ]
}
```

### --- id=85 ---

输入文本: There is so much fear surrounding birth in our country and it is my opinion that most problems are caused by these fears and interventions.

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
      "cause": "fears",
      "effect": "problems"
    },
    {
      "cause": "interventions",
      "effect": "problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "most problems are caused by these fears and interventions"
      },
      "relation": "caused",
      "effect": {
        "span": "most problems"
      }
    }
  ]
}
```

### --- id=86 ---

输入文本: HSV1 can be reactivated later in life by stress, immunosuppression, fever or ultraviolet light exposure; HSV1 is the virus that causes cold sores.

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
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "virus",
      "effect": "cold sores"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "stress, immunosuppression, fever or ultraviolet light exposure"
      },
      "relation": "caused",
      "effect": {
        "span": "HSV1 can be reactivated later in life"
      }
    },
    {
      "cause": {
        "span": "HSV1"
      },
      "relation": "caused",
      "effect": {
        "span": "cold sores"
      }
    }
  ]
}
```

### --- id=87 ---

输入文本: Giardiasis causes diarrhea, bloating and flatuence that may last more than a week.

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
      "cause": "Giardiasis",
      "effect": "diarrhea"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Giardiasis"
      },
      "relation": "caused",
      "effect": {
        "span": "diarrhea, bloating and flatuence that may last more than a week"
      }
    }
  ]
}
```

### --- id=88 ---

输入文本: Hepatitis is caused by a virus that attacks the liver, triggering painful inflammation and often leading to more serious conditions like liver failure and even death.

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
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "virus",
      "effect": "Hepatitis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Hepatitis is caused by a virus that attacks the liver"
      },
      "relation": "caused",
      "effect": {
        "span": "triggering painful inflammation"
      }
    },
    {
      "cause": {
        "span": "painful inflammation"
      },
      "relation": "caused",
      "effect": {
        "span": "leading to more serious conditions like liver failure and even death"
      }
    }
  ]
}
```

### --- id=89 ---

输入文本: High doses can cause severe breathing or brain problems, coma, or even death.

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
      "cause": "High doses",
      "effect": "death"
    },
    {
      "cause": "High doses",
      "effect": "coma"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "High doses"
      },
      "relation": "caused",
      "effect": {
        "span": "severe breathing or brain problems, coma, or even death"
      }
    }
  ]
}
```

### --- id=90 ---

输入文本: The increase in services revenue was primarily a result of our acquisition of Perot Systems in Fiscal 2010.

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
      "cause": "acquisition of Perot Systems",
      "effect": "increase in services revenue"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "our acquisition of Perot Systems in Fiscal 2010"
      },
      "relation": "caused",
      "effect": {
        "span": "The increase in services revenue"
      }
    }
  ]
}
```

### --- id=91 ---

输入文本: There is always some danger that when the gates are open to the greater spiritual realm of the mind, that also the unconscious: feelings, longings, wishes, can rush up as well, and cause some confusion.

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
      "cause": "feelings",
      "effect": "confusion"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the unconscious: feelings, longings, wishes, can rush up"
      },
      "relation": "caused",
      "effect": {
        "span": "some confusion"
      }
    }
  ]
}
```

### --- id=92 ---

输入文本: Excessive govt spending can and does cause inflation and malinvestment which can lead to imbalances and recession.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "inflation",
      "effect": "recession"
    },
    {
      "cause": "malinvestment",
      "effect": "recession"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Excessive govt spending"
      },
      "relation": "caused",
      "effect": {
        "span": "inflation and malinvestment"
      }
    },
    {
      "cause": {
        "span": "inflation and malinvestment"
      },
      "relation": "caused",
      "effect": {
        "span": "imbalances and recession"
      }
    }
  ]
}
```

### --- id=93 ---

输入文本: Drugs used to treat RA may cause death, disability, and diseases, especially if the treatment continues in the setting of undetected toxicity.

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
    "tp": 0,
    "fp": 1,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "Drugs",
      "effect": "death"
    },
    {
      "cause": "Drugs",
      "effect": "diseases"
    },
    {
      "cause": "Drugs",
      "effect": "disability"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "treatment continues in the setting of undetected toxicity"
      },
      "relation": "caused",
      "effect": {
        "span": "death, disability, and diseases"
      }
    }
  ]
}
```

### --- id=94 ---

输入文本: And apparently economic growth has a lot to do with the greenhouse gases that might lead to climate change.

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
      "cause": "greenhouse gases",
      "effect": "climate change"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "economic growth"
      },
      "relation": "caused",
      "effect": {
        "span": "the greenhouse gases"
      }
    },
    {
      "cause": {
        "span": "the greenhouse gases that might lead to climate change"
      },
      "relation": "caused",
      "effect": {
        "span": "climate change"
      }
    }
  ]
}
```

### --- id=95 ---

输入文本: In the United States, injury is the leading cause of death for persons aged 1--44 years, and the approximately 800,000 emergency medical services (EMS) providers have a substantial impact on the care of injured persons and on public health.

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
      "cause": "injury",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "injury"
      },
      "relation": "caused",
      "effect": {
        "span": "the leading cause of death for persons aged 1--44 years"
      }
    }
  ]
}
```

### --- id=96 ---

输入文本: Among other death which resulted from these riots, was Mr. Robert Dillon, a pious man, who had officiated at the Roman Catholic chapel, in Moorfields, for thirty-six years.

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
      "cause": "riots",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "these riots"
      },
      "relation": "caused",
      "effect": {
        "span": "Among other death which resulted from these riots"
      }
    }
  ]
}
```

### --- id=97 ---

输入文本: He explains on the PBS special that "HIV, the virus that causes AIDS, attacks the human immune system, by infecting the white blood cells sent to destroy it.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "virus",
      "effect": "AIDS"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "HIV"
      },
      "relation": "caused",
      "effect": {
        "span": "the virus that causes AIDS"
      }
    },
    {
      "cause": {
        "span": "HIV, the virus that causes AIDS"
      },
      "relation": "caused",
      "effect": {
        "span": "attacks the human immune system"
      }
    },
    {
      "cause": {
        "span": "infecting the white blood cells sent to destroy it"
      },
      "relation": "caused",
      "effect": {
        "span": "attacks the human immune system"
      }
    }
  ]
}
```

### --- id=98 ---

输入文本: Thus, I think it is this idea that “choices and actions lead to consequences”  is central to Rowling’s choice of a scar.

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
      "cause": "actions",
      "effect": "consequences"
    },
    {
      "cause": "choices",
      "effect": "consequences"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "choices and actions"
      },
      "relation": "caused",
      "effect": {
        "span": "consequences"
      }
    }
  ]
}
```

### --- id=99 ---

输入文本: For example, acute exposure to carbon monoxide may cause headache, nausea or death while chronic exposure may initiate or exacerbate heart and circulatory system problems.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "acute exposure",
      "effect": "nausea"
    },
    {
      "cause": "acute exposure",
      "effect": "death"
    },
    {
      "cause": "acute exposure",
      "effect": "headache"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "acute exposure to carbon monoxide"
      },
      "relation": "caused",
      "effect": {
        "span": "may cause headache, nausea or death"
      }
    },
    {
      "cause": {
        "span": "chronic exposure"
      },
      "relation": "caused",
      "effect": {
        "span": "may initiate or exacerbate heart and circulatory system problems"
      }
    }
  ]
}
```

### --- id=100 ---

输入文本: The primary cause of hypocalcemia is hypoparathyroidism.

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
      "cause": "hypoparathyroidism",
      "effect": "hypocalcemia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "hypoparathyroidism"
      },
      "relation": "caused",
      "effect": {
        "span": "hypocalcemia"
      }
    }
  ]
}
```
