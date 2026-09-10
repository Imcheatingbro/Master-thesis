# causenet_validation first 300 eval report

## 配置
```json
{
  "label": "causenet_validation first 300",
  "model": "google/gemma-4-31b-qat",
  "dataset": "causenet_validation",
  "sample_count": 300,
  "prompt_name": "v3",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 5,
  "temperature": 0.0,
  "max_tokens": 8192,
  "output_schema": "standard",
  "primary_metric": null,
  "progress_every": 100,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 2048,
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
================ causenet_validation first 300 final report ================
样本总数: 300
  Gold 含因果: 300 | Pred 含因果: 277
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.923
  Precision: 1.000
  Recall   : 0.923
  F1       : 0.960
  (TP=277, TN=0, FP=0, FN=23)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 300
    Gold triples: 354 | Pred triples: 347
    Precision: 0.170
    Recall   : 0.167
    F1       : 0.168
    (TP=59, FP=288, FN=295)
  [anchor_window] (primary)
    样本数: 300
    Gold triples: 354 | Pred triples: 347
    Precision: 0.660
    Recall   : 0.647
    F1       : 0.653
    (TP=229, FP=118, FN=125)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 277
    Gold triples: 327 | Pred triples: 347
    Precision: 0.170
    Recall   : 0.180
    F1       : 0.175
    (TP=59, FP=288, FN=268)
  [anchor_window] (primary)
    样本数: 277
    Gold triples: 327 | Pred triples: 347
    Precision: 0.660
    Recall   : 0.700
    F1       : 0.680
    (TP=229, FP=118, FN=98)
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

Sample details shown: all 143 wrong samples from 300 total samples.

### --- id=1 ---

输入文本: Hyperhomocysteinemia is associated with an increased risk of atherosclerotic and thromboembolic disorders, as well as hyperinsulinemia and may partially account for increased risk of cardiovascular disease associated with insulin resistance.

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
      "effect": "cardiovascular disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Hyperhomocysteinemia"
      },
      "relation": "caused",
      "effect": {
        "span": "an increased risk of atherosclerotic and thromboembolic disorders, as well as hyperinsulinemia"
      }
    },
    {
      "cause": {
        "span": "Hyperhomocysteinemia"
      },
      "relation": "caused",
      "effect": {
        "span": "increased risk of cardiovascular disease associated with insulin resistance"
      }
    }
  ]
}
```

### --- id=3 ---

输入文本: More than likely the pain is caused by the pressure on the nerve and it is best to lie on the opposite side to relieve the pressure.

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
      "cause": "pressure on the nerve",
      "effect": "pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the pressure on the nerve"
      },
      "relation": "caused",
      "effect": {
        "span": "the pain"
      }
    },
    {
      "cause": {
        "span": "lie on the opposite side"
      },
      "relation": "caused",
      "effect": {
        "span": "relieve the pressure"
      }
    }
  ]
}
```

### --- id=5 ---

输入文本: Over consumption of sugar makes children vulnerable to yeast overgrowth, which can lead to chronic nasal congestion, eczema, and ear infections.

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
      "cause": "yeast overgrowth",
      "effect": "ear infections"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Over consumption of sugar"
      },
      "relation": "caused",
      "effect": {
        "span": "makes children vulnerable to yeast overgrowth"
      }
    },
    {
      "cause": {
        "span": "yeast overgrowth"
      },
      "relation": "caused",
      "effect": {
        "span": "chronic nasal congestion, eczema, and ear infections"
      }
    }
  ]
}
```

### --- id=7 ---

输入文本: His doctor suggested a sleep study, which determined he was suffering from obstructive sleep apnea, a sleep disorder that can lead to serious health problems.

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
      "cause": "sleep disorder",
      "effect": "serious health problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "obstructive sleep apnea"
      },
      "relation": "caused",
      "effect": {
        "span": "serious health problems"
      }
    }
  ]
}
```

### --- id=8 ---

输入文本: The term includes impairments caused by congenital anomaly (e.g., clubfoot, absence of some member, etc.), impairments caused by disease (e.g., poliomyelitis, bone tuberculosis, etc.) and impairments from other causes (e.g., cerebral palsy, amputations, and fractures or burns that cause contractions).

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
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "disease",
      "effect": "impairments"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "congenital anomaly (e.g., clubfoot, absence of some member, etc.)"
      },
      "relation": "caused",
      "effect": {
        "span": "impairments"
      }
    },
    {
      "cause": {
        "span": "disease (e.g., poliomyelitis, bone tuberculosis, etc.)"
      },
      "relation": "caused",
      "effect": {
        "span": "impairments"
      }
    },
    {
      "cause": {
        "span": "fractures or burns"
      },
      "relation": "caused",
      "effect": {
        "span": "contractions"
      }
    }
  ]
}
```

### --- id=9 ---

输入文本: By the late 1930s, respected medical journals already contained articles describing how asbestos could cause asbestosis and cancer, indicating that the disease took 15 years or more to develop (latency period); that the diseases were often progressive; and that asbestos disease could be fatal.

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
      "cause": "asbestos",
      "effect": "cancer"
    },
    {
      "cause": "asbestos",
      "effect": "asbestosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "asbestos"
      },
      "relation": "caused",
      "effect": {
        "span": "asbestosis and cancer"
      }
    }
  ]
}
```

### --- id=17 ---

输入文本: The most reasonable approach to determine whether any tax policy change directly causes a "net tax revenue gain to any district" would be to analyze the fiscal impact of such change.

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
      "cause": "tax policy change",
      "effect": "net tax revenue gain to any district"
    }
  ],
  "pred_triples": []
}
```

### --- id=19 ---

输入文本: A one metre rise in sea level could permanently flood 21% of Bangladesh, including its best agricultural land, pushing 15 million people out of their homes.1 Ethiopia has suffered successive years of drought since 2004 caused by failure of the spring rains that may well be linked to climate change.2 The droughts caused crop failures that have left millions at risk of starvation.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 3,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "droughts",
      "effect": "crop failures"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "A one metre rise in sea level"
      },
      "relation": "caused",
      "effect": {
        "span": "permanently flood 21% of Bangladesh, including its best agricultural land, pushing 15 million people out of their homes"
      }
    },
    {
      "cause": {
        "span": "failure of the spring rains"
      },
      "relation": "caused",
      "effect": {
        "span": "Ethiopia has suffered successive years of drought since 2004"
      }
    },
    {
      "cause": {
        "span": "climate change"
      },
      "relation": "caused",
      "effect": {
        "span": "failure of the spring rains"
      }
    },
    {
      "cause": {
        "span": "The droughts"
      },
      "relation": "caused",
      "effect": {
        "span": "crop failures that have left millions at risk of starvation"
      }
    }
  ]
}
```

### --- id=20 ---

输入文本: Some storms have been known to cause floods which seem to affect the greatest number of people in Austria, doing serious economic damage.

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
      "cause": "storms",
      "effect": "floods"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Some storms"
      },
      "relation": "caused",
      "effect": {
        "span": "floods which seem to affect the greatest number of people in Austria"
      }
    },
    {
      "cause": {
        "span": "floods which seem to affect the greatest number of people in Austria"
      },
      "relation": "caused",
      "effect": {
        "span": "doing serious economic damage"
      }
    }
  ]
}
```

### --- id=21 ---

输入文本: Three distinct audiences are addressed: biochemists and pharmacologists studying the processes in which magnesium has a pivotal role; clinicians who recognize that magnesium deficiency, as well as that of potassium, is associated with several conditions; and researchers investigating the role of metal ions in the regulation of biological processes, or the role of biomolecular interactions in cellular signalling and This volume contains the Proceeding of the 8th International Symposium on Magnesium.

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
      "cause": "magnesium deficiency",
      "effect": "conditions"
    }
  ],
  "pred_triples": []
}
```

### --- id=23 ---

输入文本: Less commonly the distress and disablement caused by anxiety may cause periods of depression or drug and alcohol problems.

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
      "cause": "anxiety",
      "effect": "distress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "anxiety"
      },
      "relation": "caused",
      "effect": {
        "span": "the distress and disablement"
      }
    },
    {
      "cause": {
        "span": "the distress and disablement caused by anxiety"
      },
      "relation": "caused",
      "effect": {
        "span": "periods of depression or drug and alcohol problems"
      }
    }
  ]
}
```

### --- id=25 ---

输入文本: [ 10] The string attached to the door would lead to a lever or button inside the box.

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
      "cause": "string attached to the door",
      "effect": "lever or button inside the box"
    }
  ],
  "pred_triples": []
}
```

### --- id=27 ---

输入文本: Their product, Diabeta, used along with diet to lower the sugar level in the blood for non-insulin-dependent diabetics, shows increased risk of death from heart disease.

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
      "cause": "heart disease",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Their product, Diabeta, used along with diet to lower the sugar level in the blood for non-insulin-dependent diabetics"
      },
      "relation": "caused",
      "effect": {
        "span": "increased risk of death from heart disease"
      }
    }
  ]
}
```

### --- id=28 ---

输入文本: The emergence of reduced vancomycin susceptibility in S. aureus increases the possibility that some strains will become fully resistant and that currently available antimicrobial agents will become ineffective for treating infections caused by such strains.

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
      "cause": "strains",
      "effect": "infections"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The emergence of reduced vancomycin susceptibility in S. aureus"
      },
      "relation": "caused",
      "effect": {
        "span": "increases the possibility that some strains will become fully resistant and that currently available antimicrobial agents will become ineffective for treating infections caused by such strains"
      }
    }
  ]
}
```

### --- id=30 ---

输入文本: The current tour is intended to educate people about the suffering caused by Agent Orange, build solidarity between the U.S. and Vietnam, as well as achieve justice for the Vietnamese victims of the chemical by promoting and supporting their lawsuit.

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
      "cause": "Agent Orange",
      "effect": "suffering"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Agent Orange"
      },
      "relation": "caused",
      "effect": {
        "span": "the suffering"
      }
    },
    {
      "cause": {
        "span": "The current tour"
      },
      "relation": "caused",
      "effect": {
        "span": "educate people about the suffering caused by Agent Orange, build solidarity between the U.S. and Vietnam, as well as achieve justice for the Vietnamese victims of the chemical by promoting and supporting their lawsuit"
      }
    }
  ]
}
```

### --- id=32 ---

输入文本: Researchers believe this may be caused by the chronic pain and sleeplessness associated with the disease, which tends to depress HPA activity—including growth hormone, androgens, and cortisol levels (Calis M et al 2004; Geenen R et al 2002; Okifuji A et al 2002).

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
      "cause": "disease",
      "effect": "chronic pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the chronic pain and sleeplessness associated with the disease"
      },
      "relation": "caused",
      "effect": {
        "span": "this"
      }
    },
    {
      "cause": {
        "span": "the chronic pain and sleeplessness associated with the disease"
      },
      "relation": "caused",
      "effect": {
        "span": "depress HPA activity—including growth hormone, androgens, and cortisol levels"
      }
    }
  ]
}
```

### --- id=34 ---

输入文本: It will also help our body repair the damage caused by infection, radiation treatments, stress, injury, bad diet, and even burns and trauma .

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
      "cause": "injury",
      "effect": "damage"
    },
    {
      "cause": "infection",
      "effect": "damage"
    },
    {
      "cause": "stress",
      "effect": "damage"
    },
    {
      "cause": "radiation treatments",
      "effect": "damage"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "infection, radiation treatments, stress, injury, bad diet, and even burns and trauma"
      },
      "relation": "caused",
      "effect": {
        "span": "the damage"
      }
    }
  ]
}
```

### --- id=35 ---

输入文本: According to the American Stroke Foundation, stroke is the 3rd leading cause of death in the U.S. With over 700,000 strokes occurring annually, 4 of 5 families in the United States alone will endure the heartbreak associated with this disease.

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
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Stroke",
      "effect": "death"
    },
    {
      "cause": "disease",
      "effect": "heartbreak"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over 700,000 strokes occurring annually"
      },
      "relation": "caused",
      "effect": {
        "span": "4 of 5 families in the United States alone will endure the heartbreak associated with this disease"
      }
    }
  ]
}
```

### --- id=36 ---

输入文本: CONCLUSIONS: Cardiovascular disease, diabetes, future coronary risk, and increasing fasting glucose levels are independently associated with ED.

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
      "cause": "diabetes",
      "effect": "ed"
    },
    {
      "cause": "Cardiovascular disease",
      "effect": "ed"
    }
  ],
  "pred_triples": []
}
```

### --- id=38 ---

输入文本: Diabetic retinopathy is a potentially blinding condition in which the blood vessels inside the eye become damaged from the high blood sugar levels associated with diabetes.

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
      "cause": "diabetes",
      "effect": "high blood sugar levels"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the high blood sugar levels associated with diabetes"
      },
      "relation": "caused",
      "effect": {
        "span": "the blood vessels inside the eye become damaged"
      }
    }
  ]
}
```

### --- id=39 ---

输入文本: A person licensed or certified pursuant to section 17a-114 shall be liable for any act or omission resulting in personal injury to a child placed in his care by the Commissioner of Children and Families to the same extent as a biological parent is liable for any act or omission resulting in personal injury to a biological child in his care.

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
      "cause": "omission",
      "effect": "personal injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "any act or omission"
      },
      "relation": "caused",
      "effect": {
        "span": "personal injury to a child placed in his care by the Commissioner of Children and Families"
      }
    },
    {
      "cause": {
        "span": "any act or omission"
      },
      "relation": "caused",
      "effect": {
        "span": "personal injury to a biological child in his care"
      }
    }
  ]
}
```

### --- id=40 ---

输入文本: The serious side effects which can lead to death include intra-articular or pericardial bleeding, hemorrhagic stroke, bleeding in the brain or other subdural bleeds.

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
      "cause": "serious side effects",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "intra-articular or pericardial bleeding, hemorrhagic stroke, bleeding in the brain or other subdural bleeds"
      },
      "relation": "caused",
      "effect": {
        "span": "death"
      }
    }
  ]
}
```

### --- id=41 ---

输入文本: Some of the side effects associated with anabolic steroids include - premature balding or hair loss, dizziness, mood swings (anger, depression and aggression), hallucinations, extreme feelings of mistrust or fear, sleeping problems, vomiting and nausea, trembling, high blood pressure, aching joints, jaundice, liver damage, urinary problems, shortening of the final adult height, increased risk of developing heart disease, and strokes Abilify.

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
      "cause": "anabolic steroids",
      "effect": "side effects"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "anabolic steroids"
      },
      "relation": "caused",
      "effect": {
        "span": "premature balding or hair loss, dizziness, mood swings (anger, depression and aggression), hallucinations, extreme feelings of mistrust or fear, sleeping problems, vomiting and nausea, trembling, high blood pressure, aching joints, jaundice, liver damage, urinary problems, shortening of the final adult height, increased risk of developing heart disease, and strokes Abilify"
      }
    }
  ]
}
```

### --- id=42 ---

输入文本: From car repairs to financial loss resulting from damage or theft, auto insurance is an essential for all Cumberland, Perry, Franklin and Dauphin County drivers.

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
      "cause": "theft",
      "effect": "financial loss"
    },
    {
      "cause": "damage",
      "effect": "financial loss"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "damage or theft"
      },
      "relation": "caused",
      "effect": {
        "span": "financial loss"
      }
    }
  ]
}
```

### --- id=44 ---

输入文本: The Physical Health section asked about self assessed health and ratings with peers, accidents, diseases, limitations due to health, both traditional and modern medications, and medical consultations.

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
      "cause": "Health",
      "effect": "limitations"
    }
  ],
  "pred_triples": []
}
```

### --- id=47 ---

输入文本: It therefore appeared unlikely that Dr Musbahi's response would have been different if he had thought that the breathlessness was due to heart failure rather than COPD.

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
      "cause": "heart failure",
      "effect": "breathlessness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the breathlessness was due to heart failure rather than COPD"
      },
      "relation": "caused",
      "effect": {
        "span": "Dr Musbahi's response would have been different"
      }
    }
  ]
}
```

### --- id=48 ---

输入文本: The Endoscopy Center of Southern Nevada routinely reused syringes on multiple patients, a negligent practice which exposed thousands of patients to blood borne diseases, including Hepatitis C, Hepatitis B and HIV, the virus that causes AIDS.

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
      "effect": "AIDS"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The Endoscopy Center of Southern Nevada routinely reused syringes on multiple patients"
      },
      "relation": "caused",
      "effect": {
        "span": "exposed thousands of patients to blood borne diseases, including Hepatitis C, Hepatitis B and HIV"
      }
    },
    {
      "cause": {
        "span": "HIV"
      },
      "relation": "caused",
      "effect": {
        "span": "AIDS"
      }
    }
  ]
}
```

### --- id=49 ---

输入文本: Again because of recent improvements with regards to the kinds of materials used and the doping & die structure of the lights means that now they're able to emit light in all visible frequencies which results in white light being produced.

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
      "cause": "light in all visible frequencies",
      "effect": "white light being produced"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "recent improvements with regards to the kinds of materials used and the doping & die structure of the lights"
      },
      "relation": "caused",
      "effect": {
        "span": "now they're able to emit light in all visible frequencies"
      }
    },
    {
      "cause": {
        "span": "now they're able to emit light in all visible frequencies"
      },
      "relation": "caused",
      "effect": {
        "span": "white light being produced"
      }
    }
  ]
}
```

### --- id=50 ---

输入文本: Avoid alcohol and caffeine, which can cause dehydration, and cigarette smoke, which can aggravate your symptoms.

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
      "cause": "alcohol",
      "effect": "dehydration"
    },
    {
      "cause": "caffeine",
      "effect": "dehydration"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "alcohol and caffeine"
      },
      "relation": "caused",
      "effect": {
        "span": "dehydration"
      }
    },
    {
      "cause": {
        "span": "cigarette smoke"
      },
      "relation": "caused",
      "effect": {
        "span": "aggravate your symptoms"
      }
    }
  ]
}
```

### --- id=51 ---

输入文本: Smoking can even cause strokes and heart disease.

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
      "effect": "heart disease"
    },
    {
      "cause": "Smoking",
      "effect": "strokes"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Smoking"
      },
      "relation": "caused",
      "effect": {
        "span": "strokes and heart disease"
      }
    }
  ]
}
```

### --- id=55 ---

输入文本: The opinion, the first round in the closely followed Association for Molecular Pathology v. United States Patent and Trademark Office (widely known as the ACLU v. Myriad Genetics case), invalidates several patents with claims covering genes associated with breast cancer.

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
      "cause": "breast cancer",
      "effect": "genes"
    }
  ],
  "pred_triples": []
}
```

### --- id=57 ---

输入文本: Robert S. Wilson, PhD, from the Rush Alzheimer's Disease Center at Rush University in Chicago, Illinois suggests in his study that "a rich cognitive life" does "square the curve" of decline leading to Dementia by significantly delaying the onset.

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
      "cause": "decline",
      "effect": "Dementia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "\"a rich cognitive life\""
      },
      "relation": "caused",
      "effect": {
        "span": "\"square the curve\" of decline leading to Dementia by significantly delaying the onset"
      }
    }
  ]
}
```

### --- id=60 ---

输入文本: It can lead to situations such as the heart getting larger, which can lead to its failure.

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
      "cause": "situations",
      "effect": "failure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "It"
      },
      "relation": "caused",
      "effect": {
        "span": "the heart getting larger"
      }
    },
    {
      "cause": {
        "span": "the heart getting larger"
      },
      "relation": "caused",
      "effect": {
        "span": "its failure"
      }
    }
  ]
}
```

### --- id=61 ---

输入文本: This immune reaction is the result of a problem in the MHC or perhaps the controller of the immune system which causes a release of histamines that trigger a gluten sensitivity rash.

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
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "problem in the MHC",
      "effect": "immune reaction"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a problem in the MHC or perhaps the controller of the immune system"
      },
      "relation": "caused",
      "effect": {
        "span": "This immune reaction"
      }
    },
    {
      "cause": {
        "span": "a problem in the MHC or perhaps the controller of the immune system"
      },
      "relation": "caused",
      "effect": {
        "span": "a release of histamines"
      }
    },
    {
      "cause": {
        "span": "a release of histamines"
      },
      "relation": "caused",
      "effect": {
        "span": "a gluten sensitivity rash"
      }
    }
  ]
}
```

### --- id=65 ---

输入文本: Establishing activity in clinical trials with either APOPTONE or TRIOLEX will go a long way to validate our approach that our new class of adrenal steroid hormones may play a fundamental role in preventing or treating diseases associated with aging.”

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
      "cause": "aging",
      "effect": "treating diseases"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Establishing activity in clinical trials with either APOPTONE or TRIOLEX"
      },
      "relation": "caused",
      "effect": {
        "span": "validate our approach that our new class of adrenal steroid hormones may play a fundamental role in preventing or treating diseases associated with aging"
      }
    }
  ]
}
```

### --- id=68 ---

输入文本: Drug abuse causes changes in the brain, which then leads to certain behaviour, like taking the drug compulsively, but drug addicts can learn to change their behaviour.

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
      "cause": "Drug abuse",
      "effect": "changes in the brain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Drug abuse"
      },
      "relation": "caused",
      "effect": {
        "span": "changes in the brain"
      }
    },
    {
      "cause": {
        "span": "changes in the brain"
      },
      "relation": "caused",
      "effect": {
        "span": "certain behaviour, like taking the drug compulsively"
      }
    }
  ]
}
```

### --- id=70 ---

输入文本: In addition, cytokines modify eating behaviour and metabolism, producing 'cachexia' which is the loss of appetite and tissue wasting often associated with trauma, cancer and other serious diseases.

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
      "cause": "cancer",
      "effect": "loss of appetite"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cytokines modify eating behaviour and metabolism"
      },
      "relation": "caused",
      "effect": {
        "span": "producing 'cachexia' which is the loss of appetite and tissue wasting"
      }
    }
  ]
}
```

### --- id=75 ---

输入文本: The warranty is void if it is established that the failure is due to customer's gross abuse, neglect, or misuse.

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
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "neglect",
      "effect": "failure"
    },
    {
      "cause": "misuse",
      "effect": "failure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the failure is due to customer's gross abuse, neglect, or misuse"
      },
      "relation": "caused",
      "effect": {
        "span": "The warranty is void"
      }
    }
  ]
}
```

### --- id=76 ---

输入文本: Chronic obstructive pulmonary disease is the fourth leading cause of death in the United States, with 80-90 percent of COPD cases being caused by smoking.

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
      "cause": "Chronic obstructive pulmonary disease",
      "effect": "death in the United States"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "smoking"
      },
      "relation": "caused",
      "effect": {
        "span": "80-90 percent of COPD cases"
      }
    }
  ]
}
```

### --- id=77 ---

输入文本: In addition to exploring the ways in which sex differences affect body fluid regulation and cardiovascular function, this research may lead to the development of preventative and therapeutic treatments for pregnancy disorders as well as diseases associated with aging.

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
      "cause": "aging",
      "effect": "diseases"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "this research"
      },
      "relation": "caused",
      "effect": {
        "span": "the development of preventative and therapeutic treatments for pregnancy disorders as well as diseases associated with aging"
      }
    }
  ]
}
```

### --- id=78 ---

输入文本: Infertility can lead to depression, anxiety, and a host of other physical and emotional issues.

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
      "cause": "Infertility",
      "effect": "depression"
    },
    {
      "cause": "Infertility",
      "effect": "anxiety"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Infertility"
      },
      "relation": "caused",
      "effect": {
        "span": "depression, anxiety, and a host of other physical and emotional issues"
      }
    }
  ]
}
```

### --- id=79 ---

输入文本: Like "the virus that causes AIDS" itself, AIDS denialism can infect even the most faithful "HIV=AIDS" promoters, which is why I guess they say AIDS denialism it is so insidious.

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
      "cause": "virus",
      "effect": "AIDS"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the virus"
      },
      "relation": "caused",
      "effect": {
        "span": "AIDS"
      }
    },
    {
      "cause": {
        "span": "AIDS denialism can infect even the most faithful \"HIV=AIDS\" promoters"
      },
      "relation": "caused",
      "effect": {
        "span": "AIDS denialism it is so insidious"
      }
    }
  ]
}
```

### --- id=81 ---

输入文本: It is expected that there will come a time when the costs associated with the purchase, maintenance, and disposal of cutting fluids will exceed that of the metalcutting benefits gained by their use.

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
      "cause": "maintenance",
      "effect": "costs"
    },
    {
      "cause": "purchase",
      "effect": "costs"
    }
  ],
  "pred_triples": []
}
```

### --- id=85 ---

输入文本: Stress that is out of control makes pain worse, interferes with mental clarity and mood, and causes numerous health problems, especially digestive and heart problems, along with high blood pressure.

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
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Stress",
      "effect": "heart problems"
    },
    {
      "cause": "Stress",
      "effect": "numerous health problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Stress that is out of control"
      },
      "relation": "caused",
      "effect": {
        "span": "makes pain worse"
      }
    },
    {
      "cause": {
        "span": "Stress that is out of control"
      },
      "relation": "caused",
      "effect": {
        "span": "interferes with mental clarity and mood"
      }
    },
    {
      "cause": {
        "span": "Stress that is out of control"
      },
      "relation": "caused",
      "effect": {
        "span": "causes numerous health problems, especially digestive and heart problems, along with high blood pressure"
      }
    }
  ]
}
```

### --- id=87 ---

输入文本: Furosemide is indicated in adults and pediatric patients for the treatment of edema associated with congestive heart failure, cirrhosis of the liver, and renal disease, including the nephrotic syndrome.Furosemide is particularly useful when an agent with greater diuretic potential is desired.

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
      "cause": "congestive heart failure",
      "effect": "edema"
    }
  ],
  "pred_triples": []
}
```

### --- id=89 ---

输入文本: Explaining why alcohol has such an effect on us, Dr Rupert See, senior physician at Raffles Medical explains, “Consuming alcohol causes your body to lose fluids, leading to dehydration, which causes headaches and fatigue.”

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
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "dehydration",
      "effect": "headaches"
    },
    {
      "cause": "dehydration",
      "effect": "fatigue"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Consuming alcohol"
      },
      "relation": "caused",
      "effect": {
        "span": "your body to lose fluids"
      }
    },
    {
      "cause": {
        "span": "your body to lose fluids"
      },
      "relation": "caused",
      "effect": {
        "span": "dehydration"
      }
    },
    {
      "cause": {
        "span": "dehydration"
      },
      "relation": "caused",
      "effect": {
        "span": "headaches and fatigue"
      }
    }
  ]
}
```

### --- id=91 ---

输入文本: Loss of hair can also be caused by medications and drugs that you could be taking.

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
      "cause": "medications",
      "effect": "Loss of hair"
    },
    {
      "cause": "drugs",
      "effect": "Loss of hair"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "medications and drugs that you could be taking"
      },
      "relation": "caused",
      "effect": {
        "span": "Loss of hair"
      }
    }
  ]
}
```

### --- id=92 ---

输入文本: Infections are never caused by dirt.

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
      "cause": "dirt",
      "effect": "Infections"
    }
  ],
  "pred_triples": []
}
```

### --- id=98 ---

输入文本: The creation of EMI, the Great Depression which followed the Crash of 1929, and the rise of Fascism, completely changed the landscape for recordings in Europe.

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
      "cause": "Crash of 1929",
      "effect": "Great Depression"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The creation of EMI, the Great Depression which followed the Crash of 1929, and the rise of Fascism"
      },
      "relation": "caused",
      "effect": {
        "span": "completely changed the landscape for recordings in Europe"
      }
    }
  ]
}
```

### --- id=101 ---

输入文本: Taunton Daily Gazette, 24 Feb 2012 - As a cancer survivor, I have personally witnessed the pain and suffering associated with chronic and terminal illness.

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
      "cause": "terminal illness",
      "effect": "pain"
    }
  ],
  "pred_triples": []
}
```

### --- id=102 ---

输入文本: No one reaction requiring discontinuation accounted for &#62;0.03% of the total patient population, however, of those reactions resulting in discontinuation, gastrointestinal events (diarrhea... The goal of treatment is to reduce inflammation.

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
      "cause": "reactions",
      "effect": "discontinuation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "gastrointestinal events (diarrhea"
      },
      "relation": "caused",
      "effect": {
        "span": "reactions resulting in discontinuation"
      }
    }
  ]
}
```

### --- id=103 ---

输入文本: The end result: The closer these adults stuck to a Mediterranean-style diet, the lower their risk of death from both heart attack and cancer.

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
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "cancer",
      "effect": "death"
    },
    {
      "cause": "heart attack",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The closer these adults stuck to a Mediterranean-style diet"
      },
      "relation": "caused",
      "effect": {
        "span": "the lower their risk of death from both heart attack and cancer"
      }
    }
  ]
}
```

### --- id=104 ---

输入文本: Reducing energy use of PC networks also helps reduce CO2 emissions, which is a leading cause of global warming.

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
      "cause": "CO2 emissions",
      "effect": "global warming"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Reducing energy use of PC networks"
      },
      "relation": "caused",
      "effect": {
        "span": "reduce CO2 emissions"
      }
    },
    {
      "cause": {
        "span": "CO2 emissions"
      },
      "relation": "caused",
      "effect": {
        "span": "global warming"
      }
    }
  ]
}
```

### --- id=105 ---

输入文本: Cirrhosis can be caused by viruses, bacteria, alcohol, chemicals or drugs.

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
      "cause": "alcohol",
      "effect": "Cirrhosis"
    },
    {
      "cause": "viruses",
      "effect": "Cirrhosis"
    },
    {
      "cause": "drugs",
      "effect": "Cirrhosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "viruses, bacteria, alcohol, chemicals or drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "Cirrhosis"
      }
    }
  ]
}
```

### --- id=106 ---

输入文本: These things can also result in guilt, anxiety, stress, frustrations and other negative feelings.

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
      "cause": "things",
      "effect": "stress"
    },
    {
      "cause": "things",
      "effect": "anxiety"
    },
    {
      "cause": "things",
      "effect": "frustrations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "These things"
      },
      "relation": "caused",
      "effect": {
        "span": "guilt, anxiety, stress, frustrations and other negative feelings"
      }
    }
  ]
}
```

### --- id=107 ---

输入文本: Arthritis is an inflammatory disease that can cause stiffness, pain, and swelling in the joints throughout the body; any joint in the body may be affected.

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
      "cause": "inflammatory disease",
      "effect": "pain"
    },
    {
      "cause": "inflammatory disease",
      "effect": "stiffness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Arthritis is an inflammatory disease"
      },
      "relation": "caused",
      "effect": {
        "span": "stiffness, pain, and swelling in the joints throughout the body"
      }
    }
  ]
}
```

### --- id=108 ---

输入文本: The fines associated with these deficiencies are significant.

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
      "cause": "deficiencies",
      "effect": "fines"
    }
  ],
  "pred_triples": []
}
```

### --- id=111 ---

输入文本: After all, there have been many famous people to file bankruptcy before you, so, if you determine you are in need of relief from the stress associated with debt and you live in or around the metropolitan area of Dallas, Texas, contact us today.

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
      "cause": "debt",
      "effect": "stress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "you determine you are in need of relief from the stress associated with debt and you live in or around the metropolitan area of Dallas, Texas"
      },
      "relation": "caused",
      "effect": {
        "span": "contact us today"
      }
    }
  ]
}
```

### --- id=112 ---

输入文本: The bad or LDL is like a one way bus, it carries cholesterol from the liver where it is made and recycled, and deposits it in the arteries where it can cause blockages that lead to heart disease and other problems.

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
      "cause": "blockages",
      "effect": "problems"
    },
    {
      "cause": "blockages",
      "effect": "heart disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "deposits it in the arteries"
      },
      "relation": "caused",
      "effect": {
        "span": "cause blockages"
      }
    },
    {
      "cause": {
        "span": "blockages"
      },
      "relation": "caused",
      "effect": {
        "span": "lead to heart disease and other problems"
      }
    }
  ]
}
```

### --- id=115 ---

输入文本: Rapid weight gain or weight loss due to pregnancy or diet is the cause of stretch marks.

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
      "cause": "Rapid weight gain",
      "effect": "stretch marks"
    },
    {
      "cause": "weight loss",
      "effect": "stretch marks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Rapid weight gain or weight loss due to pregnancy or diet"
      },
      "relation": "caused",
      "effect": {
        "span": "stretch marks"
      }
    }
  ]
}
```

### --- id=119 ---

输入文本: Insomnia and other sleep problems are often caused by stress, anxiety and a busy mind at bedtime.

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
      "cause": "stress",
      "effect": "Insomnia"
    },
    {
      "cause": "anxiety",
      "effect": "Insomnia"
    },
    {
      "cause": "stress",
      "effect": "sleep problems"
    },
    {
      "cause": "anxiety",
      "effect": "sleep problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "stress, anxiety and a busy mind at bedtime"
      },
      "relation": "caused",
      "effect": {
        "span": "Insomnia and other sleep problems"
      }
    }
  ]
}
```

### --- id=122 ---

输入文本: There are other conditions that can cause shoulder pain with throwing, and therefore, before any treatment you should obtain a proper diagnosis.

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
      "cause": "conditions",
      "effect": "shoulder pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "other conditions that can cause shoulder pain with throwing"
      },
      "relation": "caused",
      "effect": {
        "span": "before any treatment you should obtain a proper diagnosis"
      }
    }
  ]
}
```

### --- id=123 ---

输入文本: For one thing, it's recently been discovered that very low frequency sound waves, or "standing waves," trapped in a building can cause many of the phenomena associated with ghosts.

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
      "cause": "ghosts",
      "effect": "phenomena"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "very low frequency sound waves, or \"standing waves,\" trapped in a building"
      },
      "relation": "caused",
      "effect": {
        "span": "many of the phenomena associated with ghosts"
      }
    }
  ]
}
```

### --- id=125 ---

输入文本: With those two sets of data, NTSB investigators can usually piece together the events that led to a crash.

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
      "cause": "events",
      "effect": "crash"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "those two sets of data"
      },
      "relation": "caused",
      "effect": {
        "span": "NTSB investigators can usually piece together the events that led to a crash"
      }
    }
  ]
}
```

### --- id=127 ---

输入文本: The result of this prolonged exposure or overexposure is called Cushing's Disease, which can result in high blood pressure, bone loss, diabetes and other physical symptoms.

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
      "cause": "diabetes",
      "effect": "high blood pressure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "this prolonged exposure or overexposure"
      },
      "relation": "caused",
      "effect": {
        "span": "Cushing's Disease"
      }
    },
    {
      "cause": {
        "span": "Cushing's Disease"
      },
      "relation": "caused",
      "effect": {
        "span": "high blood pressure, bone loss, diabetes and other physical symptoms"
      }
    }
  ]
}
```

### --- id=129 ---

输入文本: Well, this may be my own — first of all, the comic industry was under fire because of an old crank who claimed that comic books led to juvenile delinquency and the comic companies pulled their horns in and tried to defend themselves and stammered their way through the congressional hearings and it looked very bleak for comics.

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
      "cause": "comic books",
      "effect": "juvenile delinquency"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an old crank who claimed that comic books led to juvenile delinquency"
      },
      "relation": "caused",
      "effect": {
        "span": "the comic industry was under fire"
      }
    },
    {
      "cause": {
        "span": "comic books"
      },
      "relation": "caused",
      "effect": {
        "span": "juvenile delinquency"
      }
    }
  ]
}
```

### --- id=132 ---

输入文本: On initial impact an injury causes pain and resultant impairment and disability.

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
      "cause": "injury",
      "effect": "pain"
    },
    {
      "cause": "injury",
      "effect": "disability"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an injury"
      },
      "relation": "caused",
      "effect": {
        "span": "pain and resultant impairment and disability"
      }
    }
  ]
}
```

### --- id=133 ---

输入文本: Obesity is associated with many health risks including increased risk of diabetes, high blood pressure, heart attack, stroke, cancer and decreased quality of life.

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
      "cause": "Obesity",
      "effect": "health risks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Obesity"
      },
      "relation": "caused",
      "effect": {
        "span": "increased risk of diabetes, high blood pressure, heart attack, stroke, cancer and decreased quality of life"
      }
    }
  ]
}
```

### --- id=134 ---

输入文本: Ancient medical and literary writings have indicated that heavy metal poisoning was widespread in the history of China and was probably a chronic disease leading to premature death.

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
      "cause": "chronic disease",
      "effect": "premature death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "heavy metal poisoning"
      },
      "relation": "caused",
      "effect": {
        "span": "premature death"
      }
    }
  ]
}
```

### --- id=135 ---

输入文本: Accidents caused by faulty or defective automobiles and auto parts can cause serious injuries, including burns, broken bones, brain or spinal cord injuries, other disabling injuries, or death.

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
      "cause": "Accidents",
      "effect": "serious injuries"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "faulty or defective automobiles and auto parts"
      },
      "relation": "caused",
      "effect": {
        "span": "Accidents"
      }
    },
    {
      "cause": {
        "span": "Accidents caused by faulty or defective automobiles and auto parts"
      },
      "relation": "caused",
      "effect": {
        "span": "serious injuries, including burns, broken bones, brain or spinal cord injuries, other disabling injuries, or death"
      }
    }
  ]
}
```

### --- id=137 ---

输入文本: Although pathogens are still a primary cause of disease in developing countries, chemical pollution from industries is a major cause for concern.

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
      "cause": "pathogens",
      "effect": "disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "pathogens"
      },
      "relation": "caused",
      "effect": {
        "span": "disease in developing countries"
      }
    },
    {
      "cause": {
        "span": "chemical pollution from industries"
      },
      "relation": "caused",
      "effect": {
        "span": "concern"
      }
    }
  ]
}
```

### --- id=140 ---

输入文本: gJapan is facing a crisis caused by the earthquake, tsunami and the damaged nuclear power plant in Fukushima.

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
      "cause": "earthquake",
      "effect": "crisis"
    },
    {
      "cause": "tsunami",
      "effect": "crisis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the earthquake, tsunami and the damaged nuclear power plant in Fukushima"
      },
      "relation": "caused",
      "effect": {
        "span": "Japan is facing a crisis"
      }
    }
  ]
}
```

### --- id=143 ---

输入文本: You will be amazed how quickly this will help, particularly if your sleepless nights is as a result of anxiety, constant worry or depression as Qi Gong will help you relax your mind as well as your body.

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
      "cause": "anxiety",
      "effect": "sleepless nights"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "anxiety, constant worry or depression"
      },
      "relation": "caused",
      "effect": {
        "span": "your sleepless nights"
      }
    },
    {
      "cause": {
        "span": "Qi Gong"
      },
      "relation": "caused",
      "effect": {
        "span": "help you relax your mind as well as your body"
      }
    }
  ]
}
```

### --- id=145 ---

输入文本: Another consideration is that taking growth hormone and other hormones may cause sometimes-serious side effects, including carpal tunnel syndrome, worsening of diabetes, and fluid retention leading to congestive heart failure.

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
      "cause": "fluid retention",
      "effect": "congestive heart failure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "taking growth hormone and other hormones"
      },
      "relation": "caused",
      "effect": {
        "span": "sometimes-serious side effects, including carpal tunnel syndrome, worsening of diabetes, and fluid retention"
      }
    },
    {
      "cause": {
        "span": "fluid retention"
      },
      "relation": "caused",
      "effect": {
        "span": "congestive heart failure"
      }
    }
  ]
}
```

### --- id=151 ---

输入文本: Consistent high blood pressure also increases your risk for congestive heart failure and can lead to other problems such as <abbr title="A process in which fatty substances build up inside the walls of blood vessels.

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
      "cause": "high blood pressure",
      "effect": "problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Consistent high blood pressure"
      },
      "relation": "caused",
      "effect": {
        "span": "increases your risk for congestive heart failure"
      }
    },
    {
      "cause": {
        "span": "Consistent high blood pressure"
      },
      "relation": "caused",
      "effect": {
        "span": "can lead to other problems such as <abbr title=\"A process in which fatty substances build up inside the walls of blood vessels."
      }
    }
  ]
}
```

### --- id=154 ---

输入文本: It describes emotions as ‘the flesh of time’ and explores how emotions are attributed to objects, such that objects become sticky, or full of affective value.

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
      "cause": "objects",
      "effect": "emotions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "emotions are attributed to objects"
      },
      "relation": "caused",
      "effect": {
        "span": "objects become sticky, or full of affective value"
      }
    }
  ]
}
```

### --- id=158 ---

输入文本: The following is a list of symptoms that can be caused or made worse by estrogen dominance: acceleration of the ageing process, allergies, breast tenderness, decreased sex-drive, depression, fatigue, hair thinning, excessive facial hair, fibrocystic breasts, foggy thinking, headaches, hypoglycemia, increased blood-clotting, increased risk of stroke, infertility, irritability, memory loss, miscarriage, osteoporosis, pre-menopausal bone-loss, PMS, thyroid dysfunction mimicking hypothyroidism, uterine cancer, uterine fibroids, water retention, bloating, fat gain (especially around the abdomen, hips and thighs), gall bladder disease and auto-immune disorders such as lupus and thyroiditis.3 Not long ago in Lake Apopka in Florida, wildlife biologists discovered that strange biological effects were happening in the alligators living there.

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
      "cause": "estrogen dominance",
      "effect": "symptoms"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "estrogen dominance"
      },
      "relation": "caused",
      "effect": {
        "span": "acceleration of the ageing process, allergies, breast tenderness, decreased sex-drive, depression, fatigue, hair thinning, excessive facial hair, fibrocystic breasts, foggy thinking, headaches, hypoglycemia, increased blood-clotting, increased risk of stroke, infertility, irritability, memory loss, miscarriage, osteoporosis, pre-menopausal bone-loss, PMS, thyroid dysfunction mimicking hypothyroidism, uterine cancer, uterine fibroids, water retention, bloating, fat gain (especially around the abdomen, hips and thighs), gall bladder disease and auto-immune disorders such as lupus and thyroiditis"
      }
    }
  ]
}
```

### --- id=159 ---

输入文本: Some medical problems and medications can lead to depression.

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
      "cause": "medications",
      "effect": "depression"
    },
    {
      "cause": "medical problems",
      "effect": "depression"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Some medical problems and medications"
      },
      "relation": "caused",
      "effect": {
        "span": "depression"
      }
    }
  ]
}
```

### --- id=160 ---

输入文本: These drugs can cause liver injury when the drug is taken in a dosage that exceeds the recommended dosage.

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
      "cause": "drugs",
      "effect": "liver injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the drug is taken in a dosage that exceeds the recommended dosage"
      },
      "relation": "caused",
      "effect": {
        "span": "These drugs can cause liver injury"
      }
    }
  ]
}
```

### --- id=161 ---

输入文本: In addition, the Casio Keitai C53CA offers image stabilization technology to enhance the image quality by eliminating blur caused by camera movement.

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
      "cause": "camera movement",
      "effect": "blur"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "camera movement"
      },
      "relation": "caused",
      "effect": {
        "span": "blur"
      }
    },
    {
      "cause": {
        "span": "eliminating blur caused by camera movement"
      },
      "relation": "caused",
      "effect": {
        "span": "enhance the image quality"
      }
    }
  ]
}
```

### --- id=165 ---

输入文本: Chewing helps reduce plaque and bacterial build-up that may cause tooth decay.

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
      "cause": "plaque",
      "effect": "tooth decay"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Chewing"
      },
      "relation": "caused",
      "effect": {
        "span": "reduce plaque and bacterial build-up"
      }
    },
    {
      "cause": {
        "span": "plaque and bacterial build-up"
      },
      "relation": "caused",
      "effect": {
        "span": "tooth decay"
      }
    }
  ]
}
```

### --- id=166 ---

输入文本: The report also suggested that excessive calcium intake could lead to heart disease and kidney stones, while excessive vitamin D might lead to heart disease and kidney problems.

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
      "cause": "excessive calcium intake",
      "effect": "kidney stones"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "excessive calcium intake"
      },
      "relation": "caused",
      "effect": {
        "span": "heart disease and kidney stones"
      }
    },
    {
      "cause": {
        "span": "excessive vitamin D"
      },
      "relation": "caused",
      "effect": {
        "span": "heart disease and kidney problems"
      }
    }
  ]
}
```

### --- id=167 ---

输入文本: The Cakkavattisihanada Sutta states that poverty is the cause of immoral behavior, such as theft, falsehood, violence, hatred and cruelty, behavior which often results in crime.

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
      "cause": "behavior",
      "effect": "crime"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "poverty"
      },
      "relation": "caused",
      "effect": {
        "span": "immoral behavior, such as theft, falsehood, violence, hatred and cruelty"
      }
    },
    {
      "cause": {
        "span": "immoral behavior, such as theft, falsehood, violence, hatred and cruelty"
      },
      "relation": "caused",
      "effect": {
        "span": "crime"
      }
    }
  ]
}
```

### --- id=171 ---

输入文本: The higher operation and maintenance expense at Power Delivery was primarily due to increased pension expense, and the higher interest expense was primarily due to the debt financing completed in the fall of 2008.

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
      "cause": "debt financing",
      "effect": "higher interest expense"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "increased pension expense"
      },
      "relation": "caused",
      "effect": {
        "span": "The higher operation and maintenance expense at Power Delivery"
      }
    },
    {
      "cause": {
        "span": "the debt financing completed in the fall of 2008"
      },
      "relation": "caused",
      "effect": {
        "span": "the higher interest expense"
      }
    }
  ]
}
```

### --- id=174 ---

输入文本: This can prevent "Optimum Health" and can cause degenerative changes leading to stiffness, pain, and other problems.

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
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "degenerative changes",
      "effect": "pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "This"
      },
      "relation": "caused",
      "effect": {
        "span": "prevent \"Optimum Health\""
      }
    },
    {
      "cause": {
        "span": "This"
      },
      "relation": "caused",
      "effect": {
        "span": "degenerative changes"
      }
    },
    {
      "cause": {
        "span": "degenerative changes"
      },
      "relation": "caused",
      "effect": {
        "span": "stiffness, pain, and other problems"
      }
    }
  ]
}
```

### --- id=175 ---

输入文本: The causes of extinction were hunting, a narrowing of habitat due to the development of farming, climatic changes, and diseases transmitted by domestic cattle.

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
      "cause": "hunting",
      "effect": "extinction"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "hunting, a narrowing of habitat due to the development of farming, climatic changes, and diseases transmitted by domestic cattle"
      },
      "relation": "caused",
      "effect": {
        "span": "extinction"
      }
    },
    {
      "cause": {
        "span": "the development of farming"
      },
      "relation": "caused",
      "effect": {
        "span": "a narrowing of habitat"
      }
    }
  ]
}
```

### --- id=177 ---

输入文本: Back pain is due to muscle strain, stress, and poor posture.

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
      "cause": "poor posture",
      "effect": "Back pain"
    },
    {
      "cause": "stress",
      "effect": "Back pain"
    },
    {
      "cause": "muscle strain",
      "effect": "Back pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "muscle strain, stress, and poor posture"
      },
      "relation": "caused",
      "effect": {
        "span": "Back pain"
      }
    }
  ]
}
```

### --- id=178 ---

输入文本: The damage caused by irritants causes the same symptoms as associated with “allergens”.

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
      "cause": "irritants",
      "effect": "damage"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "damage caused by irritants"
      },
      "relation": "caused",
      "effect": {
        "span": "the same symptoms as associated with “allergens”"
      }
    }
  ]
}
```

### --- id=180 ---

输入文本: These women claim that the oral contraceptive pill they took to prevent pregnancy has caused them severe medical damage.The pharmaceutical company manufacturing this contraceptive pill claimed to reduce acne, stress and problems associated with premenstrual syndrome in women.

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
      "cause": "premenstrual syndrome",
      "effect": "acne"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the oral contraceptive pill they took to prevent pregnancy"
      },
      "relation": "caused",
      "effect": {
        "span": "severe medical damage"
      }
    }
  ]
}
```

### --- id=181 ---

输入文本: recent large scale epidemiological studies demonstrate that used in moderation, it might protect against morbidity and mortality associated with coronary artery disease and perhaps thrombotic strokes.

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
      "cause": "coronary artery disease",
      "effect": "morbidity"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "used in moderation"
      },
      "relation": "caused",
      "effect": {
        "span": "it might protect against morbidity and mortality associated with coronary artery disease and perhaps thrombotic strokes"
      }
    }
  ]
}
```

### --- id=188 ---

输入文本: See the Federal Trade Commissions Consumer Web site located at www.ftc.gov/bcp/conline/ pubs/alerts/nigeralrt.htm, which offers a short history and details A bogus press release stated that Uniprime Capital claimed to have documentation from the government of Spain indicating that the Plasma Plus was a breakthrough treatment for the virus that causes AIDS.

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
      "cause": "virus",
      "effect": "AIDS"
    }
  ],
  "pred_triples": []
}
```

### --- id=189 ---

输入文本: Rarely, kyphosis may cause neurologic damage, such as spastic paraparesis secondary to spinal cord compression and herniated nucleus pulposus.

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
      "cause": "kyphosis",
      "effect": "neurologic damage"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "kyphosis"
      },
      "relation": "caused",
      "effect": {
        "span": "neurologic damage, such as spastic paraparesis"
      }
    },
    {
      "cause": {
        "span": "spinal cord compression and herniated nucleus pulposus"
      },
      "relation": "caused",
      "effect": {
        "span": "spastic paraparesis"
      }
    }
  ]
}
```

### --- id=192 ---

输入文本: Anxiety is also associated with PTSD or post traumatic stress disorders and conditions like panic attacks and nervous stomach.

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
      "cause": "Anxiety",
      "effect": "conditions"
    },
    {
      "cause": "Anxiety",
      "effect": "PTSD"
    }
  ],
  "pred_triples": []
}
```

### --- id=193 ---

输入文本: In the next few weeks, we will be focusing our financial support efforts on the stabilization of the temporary shelters and temporary housing being created for the victims; the mental health needs of the elderly, children and challenged individuals; and trying to prevent the death toll from rising due to the stress, hygiene and health conditions caused by the disaster, freezing weather conditions, aftershocks, and the threat of radiation exposure.

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
      "cause": "disaster",
      "effect": "stress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the disaster, freezing weather conditions, aftershocks, and the threat of radiation exposure"
      },
      "relation": "caused",
      "effect": {
        "span": "the stress, hygiene and health conditions"
      }
    },
    {
      "cause": {
        "span": "the stress, hygiene and health conditions caused by the disaster, freezing weather conditions, aftershocks, and the threat of radiation exposure"
      },
      "relation": "caused",
      "effect": {
        "span": "the death toll from rising"
      }
    }
  ]
}
```

### --- id=195 ---

输入文本: The U.S. government has long recognized the need to provide disability compensation to veterans for health problems associated with military service.

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
      "cause": "military service",
      "effect": "health problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "health problems associated with military service"
      },
      "relation": "caused",
      "effect": {
        "span": "the need to provide disability compensation to veterans"
      }
    }
  ]
}
```

### --- id=197 ---

输入文本: Love is the very cause of life; on the other hand, separation brings death.

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
      "cause": "Love",
      "effect": "life"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Love"
      },
      "relation": "caused",
      "effect": {
        "span": "life"
      }
    },
    {
      "cause": {
        "span": "separation"
      },
      "relation": "caused",
      "effect": {
        "span": "death"
      }
    }
  ]
}
```

### --- id=204 ---

输入文本: The disease is accompanied by remarkably few systemic symptoms, but occasionally secondary infections resulting in sepsis or tetanus cause severe systemic disease and death .

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
      "cause": "secondary infections",
      "effect": "sepsis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "secondary infections resulting in sepsis or tetanus"
      },
      "relation": "caused",
      "effect": {
        "span": "severe systemic disease and death"
      }
    }
  ]
}
```

### --- id=206 ---

输入文本: In third grade, Warhol had St. Vitus' dance, a nervous system disease that causes involuntary movements of the extremities, which is believed to be a complication of scarlet fever and causes skin pigmentation blotchiness.

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
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "nervous system disease",
      "effect": "involuntary movements of the extremities"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "St. Vitus' dance, a nervous system disease"
      },
      "relation": "caused",
      "effect": {
        "span": "involuntary movements of the extremities"
      }
    },
    {
      "cause": {
        "span": "scarlet fever"
      },
      "relation": "caused",
      "effect": {
        "span": "St. Vitus' dance, a nervous system disease"
      }
    },
    {
      "cause": {
        "span": "St. Vitus' dance, a nervous system disease"
      },
      "relation": "caused",
      "effect": {
        "span": "skin pigmentation blotchiness"
      }
    }
  ]
}
```

### --- id=208 ---

输入文本: Stock Market Crash [1929] http://www.pbs.org/fmc/timeline/estockmktcrash.htm Concise summary of the U.S. stock market crash of 1929, including the events leading up to the crash and the effect of the crash on the economy.

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
      "cause": "events",
      "effect": "Crash"
    }
  ],
  "pred_triples": []
}
```

### --- id=209 ---

输入文本: (Read about "Depressive Illnesses" "Allergies") But with planning, you and your family can avoid many of the problems associated with holidays, and enjoy them in good health.

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
      "cause": "holidays",
      "effect": "problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "with planning"
      },
      "relation": "caused",
      "effect": {
        "span": "you and your family can avoid many of the problems associated with holidays, and enjoy them in good health"
      }
    }
  ]
}
```

### --- id=211 ---

输入文本: Only by looking within can Truth be found, and that Truth leads to God.

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
      "cause": "Truth",
      "effect": "God"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "looking within"
      },
      "relation": "caused",
      "effect": {
        "span": "Truth be found"
      }
    },
    {
      "cause": {
        "span": "Truth"
      },
      "relation": "caused",
      "effect": {
        "span": "leads to God"
      }
    }
  ]
}
```

### --- id=212 ---

输入文本: Islam is frequently and wrongly associated with human rights violations and terrorism."

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
      "cause": "Islam",
      "effect": "terrorism"
    }
  ],
  "pred_triples": []
}
```

### --- id=214 ---

输入文本: From the data I saw, if I were asked, is that accurate, is that an accurate statement, that Accutane, and I think the label reads, Accutane, and I don't know if it's "may cause" or "Accutane causes depression, psychosis, and in rare cases suicide attempts and suicide."

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
      "cause": "Accutane",
      "effect": "depression"
    },
    {
      "cause": "Accutane",
      "effect": "psychosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Accutane"
      },
      "relation": "caused",
      "effect": {
        "span": "depression, psychosis, and in rare cases suicide attempts and suicide"
      }
    }
  ]
}
```

### --- id=216 ---

输入文本: Even with good game handling habits, however, your favorite games will eventually stop working simply from the damage caused by normal wear and tear over a long period of time.

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
      "cause": "normal wear and tear",
      "effect": "damage"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "normal wear and tear over a long period of time"
      },
      "relation": "caused",
      "effect": {
        "span": "your favorite games will eventually stop working"
      }
    }
  ]
}
```

### --- id=217 ---

输入文本: The anxiety must cause clinically significant distress or impairment.

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
      "cause": "anxiety",
      "effect": "impairment"
    },
    {
      "cause": "anxiety",
      "effect": "clinically significant distress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The anxiety"
      },
      "relation": "caused",
      "effect": {
        "span": "clinically significant distress or impairment"
      }
    }
  ]
}
```

### --- id=219 ---

输入文本: That is particularly the case because the stimulant drugs routinely used to treat ADHD may cause side effects, and the most commonly used drug, methylphenidate (Ritalin), increased the incidence of liver cancer in a study on mice.

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
      "cause": "stimulant drugs",
      "effect": "side effects"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the stimulant drugs routinely used to treat ADHD"
      },
      "relation": "caused",
      "effect": {
        "span": "may cause side effects"
      }
    },
    {
      "cause": {
        "span": "the most commonly used drug, methylphenidate (Ritalin)"
      },
      "relation": "caused",
      "effect": {
        "span": "increased the incidence of liver cancer in a study on mice"
      }
    }
  ]
}
```

### --- id=221 ---

输入文本: Studies of pain severity have shown that the pain of postherpetic neuralgia exceeds that of pain associated with childbirth, musculoskeletal pain, osteoarthritis, or chronic cancer pain.

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
      "cause": "osteoarthritis",
      "effect": "pain"
    },
    {
      "cause": "childbirth",
      "effect": "pain"
    }
  ],
  "pred_triples": []
}
```

### --- id=224 ---

输入文本: Although lymphedema may be temporary in some cases, chronic lymphedema is an irreversible, debilitating, and lifelong condition that can cause pain and discomfort, disfigurement, skin damage, limb impairments, fibrosis, and recurring risk of infection in the affected tissue.

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
      "cause": "lifelong condition",
      "effect": "pain"
    },
    {
      "cause": "lifelong condition",
      "effect": "discomfort"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "chronic lymphedema is an irreversible, debilitating, and lifelong condition"
      },
      "relation": "caused",
      "effect": {
        "span": "pain and discomfort, disfigurement, skin damage, limb impairments, fibrosis, and recurring risk of infection in the affected tissue"
      }
    }
  ]
}
```

### --- id=225 ---

输入文本: Most violence associated with drugs is because they're illegal.

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
      "cause": "drugs",
      "effect": "violence"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they're illegal"
      },
      "relation": "caused",
      "effect": {
        "span": "Most violence associated with drugs"
      }
    }
  ]
}
```

### --- id=229 ---

输入文本: Under Texas law, assault is a misdemeanor; however, assault becomes the more serious crime of aggravated assault if the offender uses a firearm or other deadly weapon, the assault causes serious bodily injury, the assault is in retaliation against a witness or informant, or the assault is against a government employee acting in his or her official capacity.

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
      "cause": "assault",
      "effect": "serious bodily injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the offender uses a firearm or other deadly weapon, the assault causes serious bodily injury, the assault is in retaliation against a witness or informant, or the assault is against a government employee acting in his or her official capacity"
      },
      "relation": "caused",
      "effect": {
        "span": "assault becomes the more serious crime of aggravated assault"
      }
    }
  ]
}
```

### --- id=231 ---

输入文本: Two major types of impacts resulting from these activities are estuarine habitat destruction and hydrologic alteration.

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
      "cause": "activities",
      "effect": "impacts"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "these activities"
      },
      "relation": "caused",
      "effect": {
        "span": "estuarine habitat destruction and hydrologic alteration"
      }
    }
  ]
}
```

### --- id=235 ---

输入文本: There are many reasons as to why a relationship might cause more pain than happiness and the most common one is incompatibility.

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
      "cause": "relationship",
      "effect": "pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "incompatibility"
      },
      "relation": "caused",
      "effect": {
        "span": "a relationship might cause more pain than happiness"
      }
    }
  ]
}
```

### --- id=236 ---

输入文本: It has been noted that if it is left untreated then it becomes chronic and leads to scarring which further leads to blindness also.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "scarring",
      "effect": "blindness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "it is left untreated"
      },
      "relation": "caused",
      "effect": {
        "span": "it becomes chronic"
      }
    },
    {
      "cause": {
        "span": "it becomes chronic"
      },
      "relation": "caused",
      "effect": {
        "span": "leads to scarring"
      }
    },
    {
      "cause": {
        "span": "scarring"
      },
      "relation": "caused",
      "effect": {
        "span": "blindness"
      }
    }
  ]
}
```

### --- id=239 ---

输入文本: The costs associated with crime are increasing rapidly with the current survey showing the costs incurred per single incident of crime ranging from €50 to €50,000, with the average cost per incident being €2,920.

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
      "cause": "crime",
      "effect": "costs"
    }
  ],
  "pred_triples": []
}
```

### --- id=242 ---

输入文本: The report also states that tobacco, which causes 5.4 million deaths a year, will be responsible for 10% of all deaths globally, killing 6.5 million in 2015 and 8.3 million in 2030.

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
      "cause": "tobacco",
      "effect": "deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "tobacco"
      },
      "relation": "caused",
      "effect": {
        "span": "5.4 million deaths a year"
      }
    },
    {
      "cause": {
        "span": "tobacco"
      },
      "relation": "caused",
      "effect": {
        "span": "10% of all deaths globally, killing 6.5 million in 2015 and 8.3 million in 2030"
      }
    }
  ]
}
```

### --- id=243 ---

输入文本: They are also evaluating hydrogen sulfide as a means to locally reduce overall tissue oxygen needs during surgery, thereby reducing complications resulting from ischemia and reperfusion.

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
      "cause": "ischemia",
      "effect": "complications"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "evaluating hydrogen sulfide as a means to locally reduce overall tissue oxygen needs during surgery"
      },
      "relation": "caused",
      "effect": {
        "span": "reducing complications resulting from ischemia and reperfusion"
      }
    },
    {
      "cause": {
        "span": "ischemia and reperfusion"
      },
      "relation": "caused",
      "effect": {
        "span": "complications"
      }
    }
  ]
}
```

### --- id=244 ---

输入文本: Social support from friends and family can have similar benefits, but interpersonal relationships often cause stress as well, whereas pets may be less likely to cause stress.

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
      "cause": "pets",
      "effect": "stress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "interpersonal relationships"
      },
      "relation": "caused",
      "effect": {
        "span": "stress"
      }
    }
  ]
}
```

### --- id=247 ---

输入文本: Several types of drugs have been reported to cause different forms of anemia, including aplastic anemia, megaloblastic anemia, hemolytic anemia, and anemia caused by blood loss, chronic inflammation or suppression of red blood cell production.1 This article profiles a range of medications which can lead to these types of anemia and describes the mechanisms at work so that you may be able to prevent or minimize drug-induced cases of anemia.

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
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "blood loss",
      "effect": "anemia"
    },
    {
      "cause": "chronic inflammation",
      "effect": "anemia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Several types of drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "different forms of anemia, including aplastic anemia, megaloblastic anemia, hemolytic anemia, and anemia"
      }
    },
    {
      "cause": {
        "span": "blood loss, chronic inflammation or suppression of red blood cell production"
      },
      "relation": "caused",
      "effect": {
        "span": "anemia"
      }
    },
    {
      "cause": {
        "span": "a range of medications"
      },
      "relation": "caused",
      "effect": {
        "span": "these types of anemia"
      }
    }
  ]
}
```

### --- id=248 ---

输入文本: Malaise can be associated with depression and fatigue.

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
      "cause": "Malaise",
      "effect": "fatigue"
    }
  ],
  "pred_triples": []
}
```

### --- id=250 ---

输入文本: A wet basement will lead to many issues within your house; you can find annoyances ranging from simply losing living space to risking the structural stability of the entire home.

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
      "cause": "wet basement",
      "effect": "issues within your house"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "A wet basement"
      },
      "relation": "caused",
      "effect": {
        "span": "many issues within your house"
      }
    },
    {
      "cause": {
        "span": "A wet basement"
      },
      "relation": "caused",
      "effect": {
        "span": "annoyances ranging from simply losing living space to risking the structural stability of the entire home"
      }
    }
  ]
}
```

### --- id=253 ---

输入文本: Carcinogens, harmful substances in air, water and foods, may damage the body's cells, triggering changes that may lead to cancer.

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
      "cause": "changes",
      "effect": "cancer"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Carcinogens, harmful substances in air, water and foods, may damage the body's cells"
      },
      "relation": "caused",
      "effect": {
        "span": "triggering changes"
      }
    },
    {
      "cause": {
        "span": "triggering changes"
      },
      "relation": "caused",
      "effect": {
        "span": "may lead to cancer"
      }
    }
  ]
}
```

### --- id=258 ---

输入文本: Older adults face many obstacles to getting healthy food, and those challenges can lead to malnutrition.

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
      "cause": "challenges",
      "effect": "malnutrition"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Older adults face many obstacles to getting healthy food"
      },
      "relation": "caused",
      "effect": {
        "span": "those challenges can lead to malnutrition"
      }
    }
  ]
}
```

### --- id=260 ---

输入文本: One independent scientist has called it “one of the most toxic chemicals on earth,” citing research that methyl iodide causes cancer, late-term miscarriages and contaminates groundwater.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "methyl iodide",
      "effect": "cancer"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methyl iodide"
      },
      "relation": "caused",
      "effect": {
        "span": "cancer"
      }
    },
    {
      "cause": {
        "span": "methyl iodide"
      },
      "relation": "caused",
      "effect": {
        "span": "late-term miscarriages"
      }
    },
    {
      "cause": {
        "span": "methyl iodide"
      },
      "relation": "caused",
      "effect": {
        "span": "contaminates groundwater"
      }
    }
  ]
}
```

### --- id=262 ---

输入文本: Most Americans recognize the harmful effects of smoking, and tend to blame smokers, rather than tobacco companies, for the health problems associated with the habit.

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
      "cause": "habit",
      "effect": "health problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "smoking"
      },
      "relation": "caused",
      "effect": {
        "span": "the harmful effects of smoking"
      }
    },
    {
      "cause": {
        "span": "the habit"
      },
      "relation": "caused",
      "effect": {
        "span": "the health problems associated with the habit"
      }
    }
  ]
}
```

### --- id=264 ---

输入文本: If the disability is due to an illness or pregnancy, you will collect beginning on the sixth work day.

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
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "illness",
      "effect": "disability"
    },
    {
      "cause": "pregnancy",
      "effect": "disability"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the disability is due to an illness or pregnancy"
      },
      "relation": "caused",
      "effect": {
        "span": "you will collect beginning on the sixth work day"
      }
    }
  ]
}
```

### --- id=265 ---

输入文本: His first trial resulted in a hung jury because of the question of the legitimacy of murder during wartime; the jury of twelve voted ten in favor, two opposed to conviction.

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
      "cause": "first trial",
      "effect": "hung jury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the question of the legitimacy of murder during wartime"
      },
      "relation": "caused",
      "effect": {
        "span": "His first trial resulted in a hung jury"
      }
    }
  ]
}
```

### --- id=266 ---

输入文本: After suffering declining health caused by multiple heart attacks and AIDS related complications, Carter died of pneumonia in Manhattan in 1985.

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
      "cause": "complications",
      "effect": "declining health"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "multiple heart attacks and AIDS related complications"
      },
      "relation": "caused",
      "effect": {
        "span": "suffering declining health"
      }
    },
    {
      "cause": {
        "span": "pneumonia"
      },
      "relation": "caused",
      "effect": {
        "span": "Carter died of pneumonia in Manhattan in 1985"
      }
    }
  ]
}
```

### --- id=267 ---

输入文本: AstraZeneca today announced that the U.S. Food and Drug Administration (FDA) has approved SEROQUEL® (quetiapine fumarate) for the treatment of patients with depressive episodes associated with bipolar disorder.

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
      "cause": "bipolar disorder",
      "effect": "depressive episodes"
    }
  ],
  "pred_triples": []
}
```

### --- id=269 ---

输入文本: Because HIV, the virus that causes AIDS, can take 10 or more years to produce signs of the disease, most of these young AIDS patients were infected as teenagers.

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
      "cause": "virus",
      "effect": "AIDS"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "HIV, the virus that causes AIDS, can take 10 or more years to produce signs of the disease"
      },
      "relation": "caused",
      "effect": {
        "span": "most of these young AIDS patients were infected as teenagers"
      }
    },
    {
      "cause": {
        "span": "HIV"
      },
      "relation": "caused",
      "effect": {
        "span": "AIDS"
      }
    }
  ]
}
```

### --- id=273 ---

输入文本: On a background of strong conservation, probably controlled by selective constraints, the lineage leading to humans showed a ratio increased to 0.42.

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
      "cause": "lineage",
      "effect": "humans"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "strong conservation, probably controlled by selective constraints"
      },
      "relation": "caused",
      "effect": {
        "span": "the lineage leading to humans showed a ratio increased to 0.42"
      }
    }
  ]
}
```

### --- id=278 ---

输入文本: Watching locusts watching Star Wars, wondering why woodpeckers don't get headaches, pondering if catfish are the real cause of earthquakes... It's all in a day's work for some of the world's leading scientists.

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
      "cause": "catfish",
      "effect": "earthquakes"
    }
  ],
  "pred_triples": []
}
```

### --- id=279 ---

输入文本: Occasionally other rashes give rise to this appearance which may be caused by infection for example so do seek advice soon.

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
      "cause": "infection",
      "effect": "appearance"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "other rashes"
      },
      "relation": "caused",
      "effect": {
        "span": "give rise to this appearance"
      }
    },
    {
      "cause": {
        "span": "infection"
      },
      "relation": "caused",
      "effect": {
        "span": "this appearance"
      }
    }
  ]
}
```

### --- id=282 ---

输入文本: Categories:Acute Care, Animal Models, Basic Science, Cardiology , Cardiovascular, Chronic Diseases, Clinical Research, Clinical Trials, Diabetes , Disease-Specific Research, Epidemiological Studies, Epidemiology , Gender and Health, Health Promotion, Heart, Heart Disease, Heart Failure, Hypertension, Inflammation , Minority Health, Nicotine, Nutrition, Obesity, Pathophysiology, Pediatrics, Physical Fitness/Sports, Preventive Medicine, Public Health, Thrombosis Cardiovascular disorders are the main cause of morbidity and mortality in many countries around the world including Latin American countries.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 16
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 16
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 16
  },
  "gold_relations": [
    {
      "cause": "Chronic Diseases",
      "effect": "morbidity"
    },
    {
      "cause": "Obesity",
      "effect": "mortality"
    },
    {
      "cause": "Diabetes",
      "effect": "mortality"
    },
    {
      "cause": "Heart Failure",
      "effect": "mortality"
    },
    {
      "cause": "Diabetes",
      "effect": "morbidity"
    },
    {
      "cause": "Heart Disease",
      "effect": "mortality"
    },
    {
      "cause": "Obesity",
      "effect": "morbidity"
    },
    {
      "cause": "Hypertension",
      "effect": "mortality"
    },
    {
      "cause": "Heart Failure",
      "effect": "morbidity"
    },
    {
      "cause": "Chronic Diseases",
      "effect": "mortality"
    },
    {
      "cause": "Heart Disease",
      "effect": "morbidity"
    },
    {
      "cause": "Hypertension",
      "effect": "morbidity"
    },
    {
      "cause": "Heart",
      "effect": "mortality"
    },
    {
      "cause": "Nutrition",
      "effect": "mortality"
    },
    {
      "cause": "Heart",
      "effect": "morbidity"
    },
    {
      "cause": "Gender",
      "effect": "morbidity"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Cardiovascular disorders"
      },
      "relation": "caused",
      "effect": {
        "span": "morbidity and mortality in many countries around the world including Latin American countries"
      }
    }
  ]
}
```

### --- id=283 ---

输入文本: (Healingtalks) We know that smoking can cause some major illnesses, including heart disease, cancer, and certainly respiratory disease that all lead to untimely or premature death.

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
      "cause": "smoking",
      "effect": "major illnesses"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "smoking"
      },
      "relation": "caused",
      "effect": {
        "span": "some major illnesses, including heart disease, cancer, and certainly respiratory disease"
      }
    },
    {
      "cause": {
        "span": "some major illnesses, including heart disease, cancer, and certainly respiratory disease"
      },
      "relation": "caused",
      "effect": {
        "span": "untimely or premature death"
      }
    }
  ]
}
```

### --- id=284 ---

输入文本: The employee was dismissed due to a long period of illness, but the illness was a result of severe stress attributable to the employer’s failure to adequately deal with her complaints of bullying.

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
      "cause": "severe stress",
      "effect": "illness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a long period of illness"
      },
      "relation": "caused",
      "effect": {
        "span": "The employee was dismissed"
      }
    },
    {
      "cause": {
        "span": "severe stress attributable to the employer’s failure to adequately deal with her complaints of bullying"
      },
      "relation": "caused",
      "effect": {
        "span": "the illness"
      }
    }
  ]
}
```

### --- id=285 ---

输入文本: Many characteristics are attributed to Down syndrome but any one person will only have some of them - each person is an individual, with a unique appearance, personality and set of abilities.

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
      "cause": "Down syndrome",
      "effect": "characteristics"
    }
  ],
  "pred_triples": []
}
```

### --- id=286 ---

输入文本: According to Law, I attest that I have read and understand the three (3) pages presented here, and have been informed as to the complications associated with Ventral (or Spigelian) Hernia Repair.

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
      "cause": "Hernia Repair",
      "effect": "complications"
    }
  ],
  "pred_triples": []
}
```

### --- id=287 ---

输入文本: Due to harsh weather conditions during winter months many trains and flights can be delayed with snow and ice causing road accidents.

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
      "cause": "snow",
      "effect": "road accidents"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "harsh weather conditions during winter months"
      },
      "relation": "caused",
      "effect": {
        "span": "many trains and flights can be delayed"
      }
    },
    {
      "cause": {
        "span": "snow and ice"
      },
      "relation": "caused",
      "effect": {
        "span": "road accidents"
      }
    }
  ]
}
```

### --- id=290 ---

输入文本: Recovery will probably be slower in people whose injuries resulted in long periods of unconsciousness or amnesia.

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
      "cause": "injuries",
      "effect": "long periods"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "injuries resulted in long periods of unconsciousness or amnesia"
      },
      "relation": "caused",
      "effect": {
        "span": "Recovery will probably be slower in people"
      }
    }
  ]
}
```

### --- id=293 ---

输入文本: However, several carefully constructed research studies disproved the idea that the pertussis vaccine is the cause of neurologic damage.

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
      "cause": "pertussis vaccine",
      "effect": "neurologic damage"
    }
  ],
  "pred_triples": []
}
```

### --- id=294 ---

输入文本: Its sting may cause pain, swelling, redness, and numbness in the area of the sting and may be followed by difficulty speaking, blurred vision, paralysis of muscles, respiratory failure, and cardiac arrest.

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
      "cause": "sting",
      "effect": "pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Its sting"
      },
      "relation": "caused",
      "effect": {
        "span": "pain, swelling, redness, and numbness in the area of the sting"
      }
    },
    {
      "cause": {
        "span": "Its sting"
      },
      "relation": "caused",
      "effect": {
        "span": "difficulty speaking, blurred vision, paralysis of muscles, respiratory failure, and cardiac arrest"
      }
    }
  ]
}
```

### --- id=297 ---

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
      "cause": "use of such medications",
      "effect": "side effects"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the use of such medications"
      },
      "relation": "caused",
      "effect": {
        "span": "side effects such as weight gain that may increase the likelihood of diabetes and cardiovascular disease, sedation and movement disorders"
      }
    },
    {
      "cause": {
        "span": "weight gain"
      },
      "relation": "caused",
      "effect": {
        "span": "increase the likelihood of diabetes and cardiovascular disease"
      }
    }
  ]
}
```

### --- id=299 ---

输入文本: Death was as a result of head injuries resulting from a fractured skull.

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
      "cause": "head injuries",
      "effect": "Death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "head injuries resulting from a fractured skull"
      },
      "relation": "caused",
      "effect": {
        "span": "Death"
      }
    },
    {
      "cause": {
        "span": "a fractured skull"
      },
      "relation": "caused",
      "effect": {
        "span": "head injuries"
      }
    }
  ]
}
```
