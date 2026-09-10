# Qwen3.6 35B A3B ade Fixed eval report

## 配置
```json
{
  "label": "Qwen3.6 35B A3B ade Fixed",
  "model": "qwen/qwen3.6-35b-a3b",
  "dataset": "ade",
  "sample_count": 2942,
  "prompt_name": "v9.2",
  "use_rag": false,
  "rag_mode": "off",
  "rag_top_k": 0,
  "temperature": 0.0,
  "max_tokens": 2048,
  "output_schema": "standard",
  "primary_metric": "anchor_window",
  "progress_every": 500,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 8192,
  "reasoning_effort": null,
  "llm_extra_body": {
    "cache_prompt": false
  },
  "api_key_source": "lmstudio-default",
  "report_detail_limit": 200,
  "report_detail_mode": "errors",
  "report_error_metric": "anchor_window",
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ Qwen3.6 35B A3B ade Fixed final report ================
样本总数: 2942
  Gold 含因果: 448 | Pred 含因果: 414
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.937
  Precision: 0.819
  Recall   : 0.757
  F1       : 0.787
  (TP=339, TN=2419, FP=75, FN=109)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 2942
    Gold triples: 663 | Pred triples: 584
    Precision: 0.580
    Recall   : 0.511
    F1       : 0.544
    (TP=339, FP=245, FN=324)
  [anchor_window] (primary)
    样本数: 2942
    Gold triples: 663 | Pred triples: 584
    Precision: 0.774
    Recall   : 0.682
    F1       : 0.725
    (TP=452, FP=132, FN=211)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 339
    Gold triples: 512 | Pred triples: 474
    Precision: 0.715
    Recall   : 0.662
    F1       : 0.688
    (TP=339, FP=135, FN=173)
  [anchor_window] (primary)
    样本数: 339
    Gold triples: 512 | Pred triples: 474
    Precision: 0.954
    Recall   : 0.883
    F1       : 0.917
    (TP=452, FP=22, FN=60)
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

Sample details shown: first 200 of 240 wrong samples from 2942 total samples.

### --- id=9 ---

输入文本: We present a fatal case of subacute methanol toxicity with associated diffuse brain involvement, including bilateral putaminal necrosis and cerebral edema with ventricular compression.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 5,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 5,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 5,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "methanol",
      "effect": "bilateral putaminal necrosis"
    },
    {
      "cause": "methanol",
      "effect": "cerebral edema"
    },
    {
      "cause": "methanol",
      "effect": "diffuse brain involvement"
    },
    {
      "cause": "methanol",
      "effect": "fatal"
    },
    {
      "cause": "methanol",
      "effect": "methanol toxicity"
    },
    {
      "cause": "methanol",
      "effect": "ventricular compression"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methanol"
      },
      "effect": {
        "span": "subacute methanol toxicity"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "methanol"
      },
      "effect": {
        "span": "diffuse brain involvement"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "methanol"
      },
      "effect": {
        "span": "bilateral putaminal necrosis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "methanol"
      },
      "effect": {
        "span": "cerebral edema"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "methanol"
      },
      "effect": {
        "span": "ventricular compression"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=17 ---

输入文本: Attempts were made to stop and then restart the theophylline therapy at progressively lower doses; however, with each attempt, the patient's reaction to the drug became more toxic, with serum theophylline levels ranging between 99.9 and 149.9 micromol/L (18 and 27 microg/mL).

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
      "cause": "theophylline",
      "effect": "reaction to the drug became more toxic"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "theophylline"
      },
      "effect": {
        "span": "toxic"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=31 ---

输入文本: The course of this patient's renal disease contrasts sharply with diffuse proliferative glomerulonephritis of idiopathic systemic lupus, and suggests that this rare complication of procainamide therapy may have a favorable course.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "procainamide therapy"
      },
      "effect": {
        "span": "diffuse proliferative glomerulonephritis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=61 ---

输入文本: We report the case of a 14-year-old female with acute promyelocytic leukemia who developed symptomatic cardiomyopathy only 4 months into treatment with a combination of daunomycin and all-trans retinoic acid (ATRA).

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "all-trans retinoic acid",
      "effect": "symptomatic cardiomyopathy"
    },
    {
      "cause": "ATRA",
      "effect": "symptomatic cardiomyopathy"
    },
    {
      "cause": "daunomycin",
      "effect": "symptomatic cardiomyopathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "daunomycin"
      },
      "effect": {
        "span": "symptomatic cardiomyopathy"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "all-trans retinoic acid"
      },
      "effect": {
        "span": "symptomatic cardiomyopathy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=116 ---

输入文本: We report a 5-year-old boy with CF who had a stricture of the hepatic flexure region with associated narrowing due to submucosal fibrosis of the transverse colon, secondary to high-lipase pancreatin therapy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "high-lipase pancreatin",
      "effect": "stricture of the hepatic flexure region with associated narrowing"
    },
    {
      "cause": "high-lipase pancreatin",
      "effect": "submucosal fibrosis of the transverse colon"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "high-lipase pancreatin therapy"
      },
      "effect": {
        "span": "stricture of the hepatic flexure region"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "high-lipase pancreatin therapy"
      },
      "effect": {
        "span": "narrowing"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "high-lipase pancreatin therapy"
      },
      "effect": {
        "span": "submucosal fibrosis of the transverse colon"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=140 ---

输入文本: The potential for progressive brain injury and subsequent disability related to intraventricular IL-2 therapy is discussed.

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
      "cause": "IL-2",
      "effect": "brain injury"
    },
    {
      "cause": "IL-2",
      "effect": "disability"
    }
  ],
  "pred_triples": []
}
```

### --- id=151 ---

输入文本: One woman received ifosfamide 1000 mg/m2 (1 h infusion on days 1-5); confusion, lethargy, and speech deterioration developed on day 3.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "ifosfamide"
      },
      "effect": {
        "span": "confusion"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "ifosfamide"
      },
      "effect": {
        "span": "lethargy"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "ifosfamide"
      },
      "effect": {
        "span": "speech deterioration"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=154 ---

输入文本: The use of beclomethasone diproprionate inhaler complicated by the development of an eosinophilic pneumonia reaction.

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
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "beclomethasone diproprionate",
      "effect": "eosinophilic pneumonia reaction"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "beclomethasone diproprionate inhaler"
      },
      "effect": {
        "span": "eosinophilic pneumonia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=175 ---

输入文本: FINDINGS: Six children with growth retardation noted after treatment with high-dose fluticasone propionate were found to have adrenal suppression.

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
      "cause": "fluticasone propionate",
      "effect": "adrenal suppression"
    },
    {
      "cause": "fluticasone propionate",
      "effect": "growth retardation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "high-dose fluticasone propionate"
      },
      "effect": {
        "span": "adrenal suppression"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=200 ---

输入文本: In the absence of other causes, we suspected an adverse reaction to amiodarone, not least because of the similarity with histologic findings of cases previously reported.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "amiodarone"
      },
      "effect": {
        "span": "adverse reaction"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=211 ---

输入文本: Administration of intravenous nitroglycerin in a patient with idiopathic pulmonary hypertension resulted in an increase in pulmonary artery pressure associated with a decrease in blood flow that is best explained by an increase in pulmonary vascular resistance.

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
      "cause": "nitroglycerin",
      "effect": "decrease in blood flow"
    },
    {
      "cause": "nitroglycerin",
      "effect": "increase in pulmonary artery pressure"
    },
    {
      "cause": "nitroglycerin",
      "effect": "increase in pulmonary vascular resistance"
    }
  ],
  "pred_triples": []
}
```

### --- id=228 ---

输入文本: Both patients experienced problems due to side effects from the anti-MAC regimen and from an immune-reconstitution syndrome related to HAART.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "anti-MAC regimen"
      },
      "effect": {
        "span": "problems"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "HAART"
      },
      "effect": {
        "span": "immune-reconstitution syndrome"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=240 ---

输入文本: Three children presented with adrenal crises, manifested by vomiting and hypoglycaemia, after protracted courses of high-dose inhaled corticosteroids for asthma.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "high-dose inhaled corticosteroids"
      },
      "effect": {
        "span": "adrenal crises"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "high-dose inhaled corticosteroids"
      },
      "effect": {
        "span": "vomiting"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "high-dose inhaled corticosteroids"
      },
      "effect": {
        "span": "hypoglycaemia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=244 ---

输入文本: We describe a 35-year-old woman who developed severe thrombotic complications due to heparinization and unrecognized HDAs.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "heparinization"
      },
      "effect": {
        "span": "severe thrombotic complications"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=257 ---

输入文本: To optimize future management of this problem we studied 2 poorly recognized factors in the pathogenesis and prognosis of genitourinary malacoplakia in transplant recipients: 1) the probable role of azathioprine as the specific immunosuppressive agent responsible for the pathogenesis of malacoplakia, and 2) the importance of the localization of the disease and its impact on the ultimate prognosis.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "azathioprine"
      },
      "effect": {
        "span": "malacoplakia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=271 ---

输入文本: Ferrous sulfate-induced increase in requirement for thyroxine in a patient with primary hypothyroidism.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Ferrous sulfate"
      },
      "effect": {
        "span": "increase in requirement for thyroxine"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=273 ---

输入文本: Myoglobinuria and acute renal failure associated with intravenous vasopressin infusion.

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
      "cause": "vasopressin",
      "effect": "acute renal failure"
    },
    {
      "cause": "vasopressin",
      "effect": "Myoglobinuria"
    }
  ],
  "pred_triples": []
}
```

### --- id=274 ---

输入文本: Although they had only a few nodules at diagnosis, the nodules increased in number and size 3 to 4 months after the start of methotrexate therapy in both patients.

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
      "effect": "nodules"
    }
  ],
  "pred_triples": []
}
```

### --- id=277 ---

输入文本: These evolutional changes in both proteinuria and glomerular histology suggest a close linkage between the M-CSF treatment and macrophage-related glomerular injury.

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
      "cause": "M-CSF",
      "effect": "macrophage-related glomerular injury"
    }
  ],
  "pred_triples": []
}
```

### --- id=286 ---

输入文本: A retrospective review of TTP patients with quinine-associated thrombotic microangiopathy (TMA) for whom ADAMTS13 was measured before plasma exchange was performed.

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
      "cause": "quinine",
      "effect": "thrombotic microangiopathy"
    },
    {
      "cause": "quinine",
      "effect": "TMA"
    }
  ],
  "pred_triples": []
}
```

### --- id=291 ---

输入文本: We report a cae of paranoid psychosis following use of a decongestant containing PPA and summarize the case report literature of psychiatric adverse effects to PPA in which doses were known and stated to be within recommended guidelines.

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
      "cause": "PPA",
      "effect": "paranoid psychosis"
    },
    {
      "cause": "PPA",
      "effect": "psychiatric adverse effects"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "PPA"
      },
      "effect": {
        "span": "paranoid psychosis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=292 ---

输入文本: Pentavalent antimonial drugs used for the treatment of leishmaniasis have been associated with sudden deaths, probably due to the development of ventricular tachyarrhythmias.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Pentavalent antimonial drugs"
      },
      "effect": {
        "span": "sudden deaths"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Pentavalent antimonial drugs"
      },
      "effect": {
        "span": "ventricular tachyarrhythmias"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=301 ---

输入文本: We report four cases of severe corneal ulceration in methamphetamine abusers.

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
      "cause": "methamphetamine",
      "effect": "severe corneal ulceration"
    }
  ],
  "pred_triples": []
}
```

### --- id=329 ---

输入文本: A clinically atypical, neuropathologically verified case of Creutzfeldt-Jakob disease is described in a 32-year-old New Zealand woman with idiopathic hypopituitarism who had been treated in late adolescence (1970 to 1973) with human growth hormone processed from pooled cadaveric pituitary glands.

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
      "cause": "human growth hormone",
      "effect": "Creutzfeldt-Jakob disease"
    }
  ],
  "pred_triples": []
}
```

### --- id=365 ---

输入文本: Severe adenovirus pneumonia (AVP) following infliximab infusion for the treatment of Crohn's disease.

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
      "cause": "infliximab",
      "effect": "AVP"
    },
    {
      "cause": "infliximab",
      "effect": "Severe adenovirus pneumonia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "infliximab"
      },
      "effect": {
        "span": "Severe adenovirus pneumonia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=399 ---

输入文本: Therefore, although garenoxacin reportedly causes fewer adverse reactions for cardiac rhythms than third-generation quinolone antibiotics, one must be cautious of the interference of other drugs during hypokalemia in order to prevent TdP.

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
      "cause": "garenoxacin",
      "effect": "cardiac rhythms"
    },
    {
      "cause": "garenoxacin",
      "effect": "hypokalemia"
    }
  ],
  "pred_triples": []
}
```

### --- id=400 ---

输入文本: Danazol and multiple hepatic adenomas: peculiar clinical findings in an acromegalic patient.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Danazol"
      },
      "effect": {
        "span": "multiple hepatic adenomas"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=408 ---

输入文本: In addition to disease refractoriness, rare instances of disease progression from chronic phase to blast crisis during imatinib therapy have recently been anecdotally reported.

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
      "cause": "imatinib",
      "effect": "blast crisis"
    }
  ],
  "pred_triples": []
}
```

### --- id=410 ---

输入文本: Graft versus host-like illness in a child with phenobarbital hypersensitivity.

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
      "cause": "phenobarbital",
      "effect": "Graft versus host-like illness"
    },
    {
      "cause": "phenobarbital",
      "effect": "hypersensitivity"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "Graft versus host-like illness"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=419 ---

输入文本: CONCLUSIONS: Clinicians should be aware that Crohn's disease is a potential novel adverse drug effect of Copaxone.

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
      "cause": "Copaxone",
      "effect": "Crohn's disease"
    }
  ],
  "pred_triples": []
}
```

### --- id=420 ---

输入文本: Report of two cases of male breast cancer after prolonged estrogen treatment for prostatic carcinoma.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "estrogen"
      },
      "effect": {
        "span": "male breast cancer"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=436 ---

输入文本: Methanol toxicity can cause severe central nervous system insult in which a characteristic pattern of bilateral putaminal injury is noted on brain imaging studies.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Methanol",
      "effect": "bilateral putaminal injury"
    },
    {
      "cause": "Methanol",
      "effect": "Methanol toxicity"
    },
    {
      "cause": "Methanol",
      "effect": "severe central nervous system insult"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Methanol"
      },
      "effect": {
        "span": "severe central nervous system insult"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=452 ---

输入文本: DISCUSSION: Cough induced by ACE inhibitors is a frequently documented adverse effect.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "ACE inhibitors"
      },
      "effect": {
        "span": "Cough"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=461 ---

输入文本: Transdermal scopolamine delivery system (TRANSDERM-V) and acute angle-closure glaucoma.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Transdermal scopolamine delivery system"
      },
      "effect": {
        "span": "acute angle-closure glaucoma"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=493 ---

输入文本: Hepatocellular carcinoma in a young woman with prolonged exposure to oral contraceptives.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "oral contraceptives"
      },
      "effect": {
        "span": "Hepatocellular carcinoma"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=499 ---

输入文本: A 3-year-old boy developed alopecia areata (AA) universalis in the convalescent status of phenobarbital-induced AHS, compatible to the evidences of increased lymphocyte proliferation and increased dead cells percentages while his peripheral blood mononuclear cells were incubated with phenobarbital.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "AHS"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "alopecia areata (AA) universalis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=501 ---

输入文本: A 40-year-old man who developed acute myelomonoblastic leukemia (M4) after 7 years of treatment for multiple myeloma with the alkylating agent melphalan and steroids is presented.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "melphalan"
      },
      "effect": {
        "span": "acute myelomonoblastic leukemia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=534 ---

输入文本: We report a case of a 35-year old female who developed new onset type II diabetes mellitus with hyperosmolar hyperglycaemic coma and acute renal failure following treatment with a SGA for a first manic episode.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "SGA"
      },
      "effect": {
        "span": "new onset type II diabetes mellitus"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "SGA"
      },
      "effect": {
        "span": "hyperosmolar hyperglycaemic coma"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "SGA"
      },
      "effect": {
        "span": "acute renal failure"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=547 ---

输入文本: The probable proarrhythmic action of amiodarone, although rare, is reviewed along with a discussion of the novel use of intravenous magnesium sulfate therapy.

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
      "cause": "amiodarone",
      "effect": "proarrhythmic"
    }
  ],
  "pred_triples": []
}
```

### --- id=549 ---

输入文本: The case of a patient with apparent cocaine toxicity and drug-mediated hypertension and tachycardia is presented.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "cocaine"
      },
      "effect": {
        "span": "cocaine toxicity"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "cocaine"
      },
      "effect": {
        "span": "hypertension"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "cocaine"
      },
      "effect": {
        "span": "tachycardia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=563 ---

输入文本: Ocular toxicity by latex of Calotropis procera (Sodom apple).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "latex of Calotropis procera"
      },
      "effect": {
        "span": "Ocular toxicity"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=590 ---

输入文本: Leukaemoid monocytosis in M4 AML following chemotherapy and G-CSF.

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
      "cause": "G-CSF",
      "effect": "Leukaemoid monocytosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=591 ---

输入文本: We describe longitudinal diffusion-weighted MRI findings of sub-acute leukoencephalopathy following methotrexate therapy in a 24-year-old man diagnosed with pre-B-cell acute lymphoblastic leukemia (ALL), presenting with right-sided paralysis and aphasia after second consolidation with intrathecal triple-drug therapy given intrathecally.

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
      "cause": "methotrexate",
      "effect": "sub-acute leukoencephalopathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methotrexate therapy"
      },
      "effect": {
        "span": "sub-acute leukoencephalopathy"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "intrathecal triple-drug therapy"
      },
      "effect": {
        "span": "right-sided paralysis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "intrathecal triple-drug therapy"
      },
      "effect": {
        "span": "aphasia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=597 ---

输入文本: Administration of cation-exchange resin such as sodium polystyrene sulphonate (Kayexalate) is effective in lowering plasma potassium, although complications following oral or rectal administration are reported in newborns.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "sodium polystyrene sulphonate"
      },
      "effect": {
        "span": "complications"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Kayexalate"
      },
      "effect": {
        "span": "complications"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=652 ---

输入文本: Reversible leukopenia was documented in an 81-year-old woman treated with adjunctive ibopamine 100 mg t.i.d. for chronic congestive heart failure.

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
      "cause": "ibopamine",
      "effect": "Reversible leukopenia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "ibopamine"
      },
      "effect": {
        "span": "leukopenia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=668 ---

输入文本: Reviewing data on these patients and recent literature indicate that fatal marrow aplasia seems to occur more frequently in sero-negative women who respond well to therapy with gold salts.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "gold salts"
      },
      "effect": {
        "span": "fatal marrow aplasia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=682 ---

输入文本: The symptoms were attributed to hepatitis B vaccination.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "hepatitis B vaccination"
      },
      "effect": {
        "span": "symptoms"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=716 ---

输入文本: Genetic defects of sertraline demethylation and/or Pglycoprotein binding or concurrent circumstances may explain the onset of rhabdomyolysis in this particular patient.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "sertraline"
      },
      "effect": {
        "span": "rhabdomyolysis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=719 ---

输入文本: Possible serotonin syndrome associated with clomipramine after withdrawal of clozapine.

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
        "span": "clomipramine"
      },
      "effect": {
        "span": "serotonin syndrome"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=761 ---

输入文本: A few recent individual case reports have suggested that a myasthenic syndrome may be associated with statin treatment, but this association is not well described.

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
      "cause": "statin",
      "effect": "myasthenic syndrome"
    }
  ],
  "pred_triples": []
}
```

### --- id=777 ---

输入文本: These findings support previous studies that showed that the use of aspirin during the antecedent illness may be a risk factor for the development of RS.

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
      "cause": "aspirin",
      "effect": "RS"
    }
  ],
  "pred_triples": []
}
```

### --- id=794 ---

输入文本: Intravenous sodium bicarbonate appears to be indicated prophylactically in combating the associated metabolic acidosis due to absorbed formic acid.

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
      "cause": "formic acid",
      "effect": "metabolic acidosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=804 ---

输入文本: Panic anxiety after abrupt discontinuation of mianserin.

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
      "cause": "mianserin",
      "effect": "Panic anxiety"
    }
  ],
  "pred_triples": []
}
```

### --- id=816 ---

输入文本: We report a case of successful surgical management of arterial thrombosis after percutaneous thrombin injection of a femoral artery pseudoaneurysm in a 69-year-old woman.

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
      "cause": "thrombin",
      "effect": "arterial thrombosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=827 ---

输入文本: Sulfasalazine has been associated with bronchopulmonary complications of inflammatory bowel disease (IBD) in adults.

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
      "cause": "Sulfasalazine",
      "effect": "bronchopulmonary complications of inflammatory bowel disease"
    },
    {
      "cause": "Sulfasalazine",
      "effect": "IBD"
    }
  ],
  "pred_triples": []
}
```

### --- id=841 ---

输入文本: After calling the salon and consulting Poisindex, the substance was found to be Mar-V-cide, containing 20% Hyamine 3500, 50% cationic detergents, 20% isopropyl alcohol, and 1% sodium nitrite, which caused the methemoglobinemia in this case.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Mar-V-cide"
      },
      "effect": {
        "span": "methemoglobinemia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Hyamine 3500"
      },
      "effect": {
        "span": "methemoglobinemia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "cationic detergents"
      },
      "effect": {
        "span": "methemoglobinemia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "isopropyl alcohol"
      },
      "effect": {
        "span": "methemoglobinemia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "sodium nitrite"
      },
      "effect": {
        "span": "methemoglobinemia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=842 ---

输入文本: CASE SUMMARIES: In each case, the patients were treated over 5 years with lovastatin and developed rhabdomyolysis that coincided with the completion of a prescribed regimen of a newer macrolide antibiotic.

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
      "cause": "lovastatin",
      "effect": "rhabdomyolysis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "lovastatin"
      },
      "effect": {
        "span": "rhabdomyolysis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "macrolide antibiotic"
      },
      "effect": {
        "span": "rhabdomyolysis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=854 ---

输入文本: Vaccine-associated herpes zoster ophthalmicus [correction of opthalmicus] and encephalitis in an immunocompetent child.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Vaccine"
      },
      "effect": {
        "span": "herpes zoster ophthalmicus"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Vaccine"
      },
      "effect": {
        "span": "encephalitis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=859 ---

输入文本: We report the use of pamidronate for acute, severe hypercalcemia secondary to iatrogenic vitamin D poisoning.

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
      "cause": "vitamin D",
      "effect": "severe hypercalcemia"
    },
    {
      "cause": "vitamin D",
      "effect": "vitamin D poisoning"
    }
  ],
  "pred_triples": []
}
```

### --- id=880 ---

输入文本: Cerebrovascular complications of L-asparaginase therapy in children with leukemia: aphasia and other neuropsychological deficits.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "L-asparaginase",
      "effect": "aphasia"
    },
    {
      "cause": "L-asparaginase",
      "effect": "Cerebrovascular complications"
    },
    {
      "cause": "L-asparaginase",
      "effect": "neuropsychological deficits"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "L-asparaginase"
      },
      "effect": {
        "span": "aphasia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "L-asparaginase"
      },
      "effect": {
        "span": "neuropsychological deficits"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=883 ---

输入文本: Atrioventricular block complicating amiodarone-induced hypothyroidism in a patient with pre-excitation and rate-dependent bilateral bundle branch block.

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
      "cause": "amiodarone",
      "effect": "Atrioventricular block"
    },
    {
      "cause": "amiodarone",
      "effect": "hypothyroidism"
    }
  ],
  "pred_triples": []
}
```

### --- id=893 ---

输入文本: It is likely that the selective nephrotoxicity in these 3 patients with SIADH was induced by tetracycline.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "tetracycline"
      },
      "effect": {
        "span": "selective nephrotoxicity"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=903 ---

输入文本: Escape atrial complexes, which occurred following junctional premature complexes, failed to initiate tachycardia in the control state but tachycardia was always reinitiated by an identical escape sequence after procainamide.

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
      "cause": "procainamide",
      "effect": "tachycardia"
    }
  ],
  "pred_triples": []
}
```

### --- id=916 ---

输入文本: This is a unique autopsy case of hepatocellular carcinoma closely related to diethylstilbestrol (DES) therapy for prostatic cancer.

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
      "cause": "DES",
      "effect": "hepatocellular carcinoma"
    },
    {
      "cause": "diethylstilbestrol",
      "effect": "hepatocellular carcinoma"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "diethylstilbestrol"
      },
      "effect": {
        "span": "hepatocellular carcinoma"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=930 ---

输入文本: The present study describes a patient who had unusual weight fluctuation under corticosteroid and psychotropic treatment such as mianserin and aripiprazole.

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
      "cause": "aripiprazole",
      "effect": "unusual weight fluctuation"
    },
    {
      "cause": "mianserin",
      "effect": "unusual weight fluctuation"
    }
  ],
  "pred_triples": []
}
```

### --- id=943 ---

输入文本: This report describes the sudden appearance of mixed mania in three children with delusional depression soon after the commencement of tricyclic antidepressant therapy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "tricyclic antidepressant therapy"
      },
      "effect": {
        "span": "mixed mania"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=949 ---

输入文本: Severe lidocaine intoxication by cutaneous absorption.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "lidocaine"
      },
      "effect": {
        "span": "Severe lidocaine intoxication"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=955 ---

输入文本: Preliminary results suggest that the higher concentrations of dextrose induce increased histamine release from blood cells, and that this phenomenon is more marked in diabetic, and particularly diabetic-allergic, individuals.

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
      "cause": "dextrose",
      "effect": "increased histamine release"
    }
  ],
  "pred_triples": []
}
```

### --- id=956 ---

输入文本: We wish to call for cautious approach at time of cessation of prolonged ACTH therapy because of possible unexpected and only partially understood hazardous side effects such as hyperkalemia.

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
      "cause": "ACTH",
      "effect": "hyperkalemia"
    }
  ],
  "pred_triples": []
}
```

### --- id=957 ---

输入文本: Lithium neurotoxicity should be considered in Creutzfeldt-Jakob disease differential diagnosis, serial electroencephalograms being the most valuable.

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
      "cause": "Lithium",
      "effect": "Creutzfeldt-Jakob disease"
    },
    {
      "cause": "Lithium",
      "effect": "Lithium neurotoxicity"
    }
  ],
  "pred_triples": []
}
```

### --- id=971 ---

输入文本: The induction of hypoglycaemia with PAS in this patient suggests a potential role for PAS in the treatment of diabetes mellitus.

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
      "cause": "PAS",
      "effect": "hypoglycaemia"
    }
  ],
  "pred_triples": []
}
```

### --- id=1010 ---

输入文本: After discontinuation of danazol the diabetes completely resolved.

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
      "cause": "danazol",
      "effect": "diabetes"
    }
  ],
  "pred_triples": []
}
```

### --- id=1030 ---

输入文本: This case had radiation fibrosis, so we suggest that radiation fibrosis may be another contributor of the occurrence of ILD in patients taking erlotinib.

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
      "cause": "erlotinib",
      "effect": "ILD"
    }
  ],
  "pred_triples": []
}
```

### --- id=1031 ---

输入文本: To develop information on the relative rarity or frequency of neurologic worsening with the initiation of penicillamine therapy, we conducted a retrospective survey of 25 additional patients with Wilson's disease who met the criteria of presenting with neurologic disease and having been treated with penicillamine.

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
      "cause": "penicillamine",
      "effect": "neurologic disease"
    },
    {
      "cause": "penicillamine",
      "effect": "neurologic worsening"
    }
  ],
  "pred_triples": []
}
```

### --- id=1059 ---

输入文本: Correction of serum electrolyte imbalance prevents cardiac arrhythmia during amphotericin B administration.

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
      "cause": "amphotericin B",
      "effect": "cardiac arrhythmia"
    }
  ],
  "pred_triples": []
}
```

### --- id=1063 ---

输入文本: In the second case, five cardiac arrests due to ventricular tachycardia and fibrillation occurred during several hours after beginning a trial of bretylium maintenance therapy for complex ventricular ectopy.

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
      "cause": "bretylium",
      "effect": "cardiac arrests"
    },
    {
      "cause": "bretylium",
      "effect": "fibrillation"
    },
    {
      "cause": "bretylium",
      "effect": "ventricular tachycardia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "bretylium maintenance therapy"
      },
      "effect": {
        "span": "cardiac arrests"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1083 ---

输入文本: Rifampin (RFP) increases hepatic microsomal enzyme activity, and there are case reports of RFP-induced hypothyroidism, all associated with Hashimoto's thyroiditis.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "RFP",
      "effect": "Hashimoto's thyroiditis"
    },
    {
      "cause": "Rifampin",
      "effect": "Hashimoto's thyroiditis"
    },
    {
      "cause": "RFP",
      "effect": "hypothyroidism"
    },
    {
      "cause": "Rifampin",
      "effect": "hypothyroidism"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "RFP"
      },
      "effect": {
        "span": "hypothyroidism"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1102 ---

输入文本: Systemic lupus erythematosus (SLE) developed in as 23-year-old woman with psoriasis during treatment with psoralen-ultraviolet-A (PUVA).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "psoralen-ultraviolet-A"
      },
      "effect": {
        "span": "Systemic lupus erythematosus"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1104 ---

输入文本: Although heparin-dependent antibodies (HDAs) typically manifest with thrombocytopenia as in heparin-induced thrombocytopenia (HIT), they may also manifest with preserved platelet counts.

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
      "cause": "heparin",
      "effect": "thrombocytopenia"
    }
  ],
  "pred_triples": []
}
```

### --- id=1108 ---

输入文本: Alprazolam withdrawal delirium unresponsive to diazepam: case report.

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
      "cause": "Alprazolam",
      "effect": "delirium"
    }
  ],
  "pred_triples": []
}
```

### --- id=1117 ---

输入文本: All patients experienced severe anaemia after induction chemotherapy despite erythropoietin.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "induction chemotherapy"
      },
      "effect": {
        "span": "severe anaemia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1165 ---

输入文本: Visual system side effects caused by parasympathetic dysfunction after botulinum toxin type B injections.

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
      "cause": "botulinum toxin type B",
      "effect": "parasympathetic dysfunction"
    },
    {
      "cause": "botulinum toxin type B",
      "effect": "Visual system side effects"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "botulinum toxin type B"
      },
      "effect": {
        "span": "Visual system side effects"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1182 ---

输入文本: The incidence and clinical features of allergic contact and/or photocontact dermatitis due to psoralens were examined in 371 patients with psoriasis treated with topical PUVA.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "psoralens"
      },
      "effect": {
        "span": "allergic contact and/or photocontact dermatitis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1186 ---

输入文本: While for ribavirin antidepressant effects are not known, we suppose that antidepressants may prevent changes in serotonergic or noradrenergic neurotransmission caused by IFN-alpha.

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
      "cause": "IFN-alpha",
      "effect": "changes in serotonergic or noradrenergic neurotransmission"
    }
  ],
  "pred_triples": []
}
```

### --- id=1187 ---

输入文本: A potential role for renal and hepatic impairment in the observed protracted course of amiodarone-induced thyrotoxicosis is suggested.

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
      "cause": "amiodarone",
      "effect": "thyrotoxicosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=1193 ---

输入文本: Myoglobinuria and acute renal failure were observed in two patients with vasopressin-treated gastrointestinal hemorrhage.

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
      "cause": "vasopressin",
      "effect": "acute renal failure"
    },
    {
      "cause": "vasopressin",
      "effect": "Myoglobinuria"
    }
  ],
  "pred_triples": []
}
```

### --- id=1220 ---

输入文本: We report a patient with inoperable pancreatic cancer who developed gastrointestinal bleeding secondary to radiation-recall related to gemcitabine and review literature.

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
      "cause": "gemcitabine",
      "effect": "gastrointestinal bleeding"
    },
    {
      "cause": "gemcitabine",
      "effect": "radiation-recall"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "gemcitabine"
      },
      "effect": {
        "span": "gastrointestinal bleeding"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1246 ---

输入文本: We report an additional case of isotretinoin teratogenicity in which the patient had agenesis of the cerebellar vermis, multiple leptomeningeal neuroglial heterotopias, hydrocephalus, and abnormalities of the corticospinal tracts.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "isotretinoin",
      "effect": "abnormalities of the corticospinal tracts"
    },
    {
      "cause": "isotretinoin",
      "effect": "agenesis of the cerebellar vermis"
    },
    {
      "cause": "isotretinoin",
      "effect": "hydrocephalus"
    },
    {
      "cause": "isotretinoin",
      "effect": "multiple leptomeningeal neuroglial heterotopias"
    },
    {
      "cause": "isotretinoin",
      "effect": "teratogenicity"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "isotretinoin"
      },
      "effect": {
        "span": "agenesis of the cerebellar vermis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "isotretinoin"
      },
      "effect": {
        "span": "multiple leptomeningeal neuroglial heterotopias"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "isotretinoin"
      },
      "effect": {
        "span": "hydrocephalus"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "isotretinoin"
      },
      "effect": {
        "span": "abnormalities of the corticospinal tracts"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1252 ---

输入文本: Pulmonary hemorrhage is an uncommon feature in the HUS, and seems to appear especially in the HUS associated with MMC therapy.

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
      "cause": "MMC",
      "effect": "HUS"
    },
    {
      "cause": "MMC",
      "effect": "Pulmonary hemorrhage"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "MMC therapy"
      },
      "effect": {
        "span": "Pulmonary hemorrhage"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1266 ---

输入文本: This paper reports an autopsy case of a 78-year-old male with multiple nodules in the liver developed after long-termed administration of phosphate diethylstilbestrol (PDES) for prostatic cancer.

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
      "cause": "PDES",
      "effect": "multiple nodules in the liver"
    },
    {
      "cause": "phosphate diethylstilbestrol",
      "effect": "multiple nodules in the liver"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "phosphate diethylstilbestrol"
      },
      "effect": {
        "span": "multiple nodules in the liver"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1267 ---

输入文本: A case of acute subdural haematoma originating spontaneously from an angiomatous meningioma in a patient receiving prophylactic aspirin therapy is presented.

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
      "cause": "aspirin",
      "effect": "acute subdural haematoma"
    }
  ],
  "pred_triples": []
}
```

### --- id=1271 ---

输入文本: The other patient required a further course of treatment with lithium and the nephrotic syndrome returned.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "lithium"
      },
      "effect": {
        "span": "nephrotic syndrome"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1290 ---

输入文本: Reactivation histoplasmosis after treatment with anti-tumor necrosis factor alpha in a patient from a nonendemic area.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "anti-tumor necrosis factor alpha"
      },
      "effect": {
        "span": "Reactivation histoplasmosis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1335 ---

输入文本: Common adverse events (frequency 10%) of lacosamide doses up to 600 mg/day include nonspecific central nervous system effects (e.g., dizziness, ataxia, diplopia, and somnolence).

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "lacosamide",
      "effect": "ataxia"
    },
    {
      "cause": "lacosamide",
      "effect": "diplopia"
    },
    {
      "cause": "lacosamide",
      "effect": "dizziness"
    },
    {
      "cause": "lacosamide",
      "effect": "somnolence"
    }
  ],
  "pred_triples": []
}
```

### --- id=1381 ---

输入文本: We describe a 15-year-old female patient diagnosed with acute lymphoblastic leukemia presenting with status epilepticus after receiving intrathecal methotrexate.

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
      "cause": "methotrexate",
      "effect": "acute lymphoblastic leukemia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "intrathecal methotrexate"
      },
      "effect": {
        "span": "status epilepticus"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1393 ---

输入文本: Flare of Kaposi's sarcoma (KS) is well described in immunosuppressed patients treated with corticosteroids and rituximab, but has not yet been reported during treatment with imatinib.

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
      "cause": "rituximab",
      "effect": "Kaposi's sarcoma"
    },
    {
      "cause": "rituximab",
      "effect": "KS"
    }
  ],
  "pred_triples": []
}
```

### --- id=1402 ---

输入文本: Both patients were then treated with a carboplatin alternative to cisplatin in the following courses, which resulted in neither a relapse of the colitis nor a recurrence of the malignancies up to this time.

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
      "cause": "cisplatin",
      "effect": "colitis"
    }
  ],
  "pred_triples": []
}
```

### --- id=1406 ---

输入文本: A dapsone hypersensitivity syndrome, consisting of fever, headache, nausea, vomiting, lymphadenopathy, hepatitis, hemolysis, leukopenia, and mononucleosis, has been described in patients treated with the drug for leprosy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 9,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 9,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 9,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "dapsone",
      "effect": "fever"
    },
    {
      "cause": "dapsone",
      "effect": "headache"
    },
    {
      "cause": "dapsone",
      "effect": "hemolysis"
    },
    {
      "cause": "dapsone",
      "effect": "hepatitis"
    },
    {
      "cause": "dapsone",
      "effect": "hypersensitivity syndrome"
    },
    {
      "cause": "dapsone",
      "effect": "leukopenia"
    },
    {
      "cause": "dapsone",
      "effect": "lymphadenopathy"
    },
    {
      "cause": "dapsone",
      "effect": "mononucleosis"
    },
    {
      "cause": "dapsone",
      "effect": "nausea"
    },
    {
      "cause": "dapsone",
      "effect": "vomiting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "dapsone"
      },
      "effect": {
        "span": "fever"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dapsone"
      },
      "effect": {
        "span": "headache"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dapsone"
      },
      "effect": {
        "span": "nausea"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dapsone"
      },
      "effect": {
        "span": "vomiting"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dapsone"
      },
      "effect": {
        "span": "lymphadenopathy"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dapsone"
      },
      "effect": {
        "span": "hepatitis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dapsone"
      },
      "effect": {
        "span": "hemolysis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dapsone"
      },
      "effect": {
        "span": "leukopenia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dapsone"
      },
      "effect": {
        "span": "mononucleosis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1424 ---

输入文本: Cesium-induced QT-interval prolongation in an adolescent.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Cesium"
      },
      "effect": {
        "span": "QT-interval prolongation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1439 ---

输入文本: In this case, discontinuing piroxicam, a nonsteroidal anti-inflammatory drug, and starting a palliative treatment plan helped resolve a patient's ulcers.

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
      "cause": "piroxicam",
      "effect": "ulcers"
    }
  ],
  "pred_triples": []
}
```

### --- id=1443 ---

输入文本: We describe a case of poisoning with 3,4-methylenedioxymet-amphetamine Ecstasy that presented with all the features suggestive of a fatal outcome, including a creatinine phosphokinase level markedly higher than any previously reported.

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
      "cause": "3,4-methylenedioxymet-amphetamine Ecstasy",
      "effect": "poisoning"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "3,4-methylenedioxymet-amphetamine Ecstasy"
      },
      "effect": {
        "span": "fatal outcome"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1472 ---

输入文本: This case demonstrates the association of selective IgA deficiency with remission in rheumatoid arthritis induced by fenclofenac as well as aurothiomalate and sulphasalazine.

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
      "cause": "aurothiomalate",
      "effect": "IgA deficiency"
    },
    {
      "cause": "fenclofenac",
      "effect": "IgA deficiency"
    },
    {
      "cause": "sulphasalazine",
      "effect": "IgA deficiency"
    }
  ],
  "pred_triples": []
}
```

### --- id=1501 ---

输入文本: Theoretical basal ganglia toxicologic mechanisms of methanol poisoning are reviewed, and the role of brain imaging studies will regard to diagnosis, prognosis and impact on management is discussed.

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
      "cause": "methanol",
      "effect": "methanol poisoning"
    }
  ],
  "pred_triples": []
}
```

### --- id=1510 ---

输入文本: Conversely, diffuse interstitial pulmonary fibrosis should be considered in the differential diagnosis of patients receiving methotrexate who develop bilateral pulmonary infiltrates seen on chest roentgenograms.

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
      "cause": "methotrexate",
      "effect": "bilateral pulmonary infiltrates"
    },
    {
      "cause": "methotrexate",
      "effect": "diffuse interstitial pulmonary fibrosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=1524 ---

输入文本: RESULTS: SD-OCT images demonstrated loss of photoreceptor inner segment/outer segment (IS/OS) junction and a downward "sink-hole" displacement of inner retinal structures in areas of hydroxychloroquine toxicity corresponding to HVF 10-2 defects and ophthalmoscopic clinical examination findings.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "hydroxychloroquine toxicity"
      },
      "effect": {
        "span": "loss of photoreceptor inner segment/outer segment (IS/OS) junction"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "hydroxychloroquine toxicity"
      },
      "effect": {
        "span": "downward \"sink-hole\" displacement of inner retinal structures"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1537 ---

输入文本: A case of high-grade endometrial stromal sarcoma, confined into an intrauterine polypoid growth, in a woman with a history of breast cancer who was treated with adjuvant tamoxifen.

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
      "cause": "tamoxifen",
      "effect": "high-grade endometrial stromal sarcoma"
    },
    {
      "cause": "tamoxifen",
      "effect": "intrauterine polypoid growth"
    }
  ],
  "pred_triples": []
}
```

### --- id=1538 ---

输入文本: We describe two patients with rheumatoid arthritis who developed chronic inflammatory demyelinating polyneuropathy (CIDP) during their course of therapy with TNF-alpha antagonists.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "TNF-alpha antagonists"
      },
      "effect": {
        "span": "chronic inflammatory demyelinating polyneuropopathy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1559 ---

输入文本: We present the case of a 19-year-old male athlete with protein C deficiency who developed proximal deep venous thrombosis and pulmonary embolism while abusing anabolic-androgenic steroids.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "anabolic-androgenic steroids"
      },
      "effect": {
        "span": "proximal deep venous thrombosis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "anabolic-androgenic steroids"
      },
      "effect": {
        "span": "pulmonary embolism"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1588 ---

输入文本: DATA SYNTHESIS: Genetic deficiencies in DPD, the rate-limiting enzyme responsible for 5-FU catabolism, may occur in 3% or more of patients with cancer putting them at increased risk for unusually severe adverse reactions (e.g., diarrhea, stomatitis, mucositis, myelosuppression, neurotoxicity) to standard doses of 5-FU.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 5
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 5
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 5
  },
  "gold_relations": [
    {
      "cause": "5-FU",
      "effect": "diarrhea"
    },
    {
      "cause": "5-FU",
      "effect": "mucositis"
    },
    {
      "cause": "5-FU",
      "effect": "myelosuppression"
    },
    {
      "cause": "5-FU",
      "effect": "neurotoxicity"
    },
    {
      "cause": "5-FU",
      "effect": "stomatitis"
    }
  ],
  "pred_triples": []
}
```

### --- id=1589 ---

输入文本: Itch and skin rash from chocolate during fluoxetine and sertraline treatment: case report.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "fluoxetine",
      "effect": "Itch"
    },
    {
      "cause": "sertraline",
      "effect": "Itch"
    },
    {
      "cause": "fluoxetine",
      "effect": "skin rash"
    },
    {
      "cause": "sertraline",
      "effect": "skin rash"
    }
  ],
  "pred_triples": []
}
```

### --- id=1593 ---

输入文本: Worsening of neurologic syndrome in patients with Wilson's disease with initial penicillamine therapy.

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
      "cause": "penicillamine",
      "effect": "Worsening of neurologic syndrome"
    }
  ],
  "pred_triples": []
}
```

### --- id=1596 ---

输入文本: A 61-year-old man developed clinical lupus syndrome with positive antinuclear antibody, positive lupus erythematosus (LE) cell preparation, and diffuse proliferative glomerulonephritis following 26 months of procainamide therapy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 3,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "procainamide",
      "effect": "clinical lupus syndrome"
    },
    {
      "cause": "procainamide",
      "effect": "diffuse proliferative glomerulonephritis"
    },
    {
      "cause": "procainamide",
      "effect": "lupus erythematosus"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "procainamide therapy"
      },
      "effect": {
        "span": "clinical lupus syndrome"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "procainamide therapy"
      },
      "effect": {
        "span": "positive antinuclear antibody"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "procainamide therapy"
      },
      "effect": {
        "span": "positive lupus erythematosus (LE) cell preparation"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "procainamide therapy"
      },
      "effect": {
        "span": "diffuse proliferative glomerulonephritis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1616 ---

输入文本: Multiple complications of propylthiouracil treatment: granulocytopenia, eosinophilia, skin reaction and hepatitis with lymphocyte sensitization.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 3,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 3,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "propylthiouracil",
      "effect": "eosinophilia"
    },
    {
      "cause": "propylthiouracil",
      "effect": "granulocytopenia"
    },
    {
      "cause": "propylthiouracil",
      "effect": "hepatitis"
    },
    {
      "cause": "propylthiouracil",
      "effect": "lymphocyte sensitization"
    },
    {
      "cause": "propylthiouracil",
      "effect": "skin reaction"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "propylthiouracil"
      },
      "effect": {
        "span": "granulocytopenia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "propylthiouracil"
      },
      "effect": {
        "span": "eosinophilia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "propylthiouracil"
      },
      "effect": {
        "span": "skin reaction"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "propylthiouracil"
      },
      "effect": {
        "span": "hepatitis with lymphocyte sensitization"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1627 ---

输入文本: We report two children with HC pneumonitis and pneumatoceles as a reversible complication after ingestion and aspiration of lamp oil with very low viscosity.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "lamp oil"
      },
      "effect": {
        "span": "HC pneumonitis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "lamp oil"
      },
      "effect": {
        "span": "pneumatoceles"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1628 ---

输入文本: We present a 49-year-old woman with refractory myofascial pain of many years duration who developed subacromial impingement syndrome (SIS) following a series of botulinum toxin injections to the bilateral upper trapezii.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "botulinum toxin"
      },
      "effect": {
        "span": "subacromial impingement syndrome"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1647 ---

输入文本: We also describe a new, noninvasive method to assess magnesium-induced neuromuscular block when curariform muscle relaxant was given simultaneously.

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
      "cause": "magnesium",
      "effect": "neuromuscular block"
    }
  ],
  "pred_triples": []
}
```

### --- id=1654 ---

输入文本: While acute toxicity is not infrequently reported, a recent experience in an adult who received five consecutive daily doses of VCR (1.0 mg/m2) in conjunction with two other drugs led to a sequence of life-threatening toxicities which were not obviously ameliorated by folinic acid rescue as has been recently advocated.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "VCR"
      },
      "effect": {
        "span": "life-threatening toxicities"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1698 ---

输入文本: A severe form of exophthalmos resulting from lithium therapy has not been described in the literature.

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
      "cause": "lithium",
      "effect": "exophthalmos"
    }
  ],
  "pred_triples": []
}
```

### --- id=1703 ---

输入文本: In deciding if tamoxifen therapy is warranted, all potentially life-threatening adverse events associated with tamoxifen should be considered, including endometrial adenocarcinoma or uterine sarcoma.

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
      "cause": "tamoxifen",
      "effect": "endometrial adenocarcinoma"
    },
    {
      "cause": "tamoxifen",
      "effect": "uterine sarcoma"
    }
  ],
  "pred_triples": []
}
```

### --- id=1733 ---

输入文本: In the latter cases, it is commonly attributed to azathioprine and/or tacrolimus.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "azathioprine"
      },
      "effect": {
        "span": "it"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "tacrolimus"
      },
      "effect": {
        "span": "it"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1735 ---

输入文本: The syndrome of irreversible lithium-effectuated neurotoxicity (SILENT).

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
      "cause": "lithium",
      "effect": "neurotoxicity"
    }
  ],
  "pred_triples": []
}
```

### --- id=1745 ---

输入文本: Prick tests and intradermal tests with a series of dilutions of carboplatin and cisplatin were performed on three patients who had exhibited medium and severe hypersensitivity reactions to carboplatin.

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
      "cause": "carboplatin",
      "effect": "severe hypersensitivity"
    }
  ],
  "pred_triples": []
}
```

### --- id=1767 ---

输入文本: During her third cycle, she again received cisplatin 100 mg/m2 over 30 minutes and developed palmar pruritus, urticaria, and edema.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 3,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 3,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 3,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "cisplatin",
      "effect": "100 mg/m2"
    },
    {
      "cause": "cisplatin",
      "effect": "edema"
    },
    {
      "cause": "cisplatin",
      "effect": "palmar pruritus"
    },
    {
      "cause": "cisplatin",
      "effect": "urticaria"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cisplatin"
      },
      "effect": {
        "span": "palmar pruritus"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "cisplatin"
      },
      "effect": {
        "span": "urticaria"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "cisplatin"
      },
      "effect": {
        "span": "edema"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1782 ---

输入文本: Possible mechanisms for damage to the urothelium by ketamine are suggested.

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
      "cause": "ketamine",
      "effect": "damage to the urothelium"
    }
  ],
  "pred_triples": []
}
```

### --- id=1786 ---

输入文本: Only two case reports of adults with allergic contact dermatitis to this chemical exist in the literature, and we describe three more cases of children with recalcitrant atopic dermatitis found to have potential allergic contact dermatitis to bisabolol- a component of the Aquaphor emollient they were using to treat their atopic dermatitis.

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
      "cause": "bisabolol",
      "effect": "allergic contact dermatitis"
    }
  ],
  "pred_triples": []
}
```

### --- id=1797 ---

输入文本: Hyperglycemia induced by the first product improved after the substitution, suggesting that the Erwinia enzyme may be less diabetogenic than the E. coli enzyme.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the first product"
      },
      "effect": {
        "span": "Hyperglycemia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1804 ---

输入文本: Although isradipine has been associated with hepatocellular injury, there are no reports of fulminant liver failure with this agent, and our patient had been treated for >2 years without signs of toxicity.

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
      "cause": "isradipine",
      "effect": "hepatocellular injury"
    }
  ],
  "pred_triples": []
}
```

### --- id=1805 ---

输入文本: Idiosyncratic pulmonary reactions to nitrofurantoin are not unusual, often presenting as eosinophilic pneumonia.

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
      "cause": "nitrofurantoin",
      "effect": "eosinophilic pneumonia"
    },
    {
      "cause": "nitrofurantoin",
      "effect": "Idiosyncratic pulmonary reactions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "nitrofurantoin"
      },
      "effect": {
        "span": "eosinophilic pneumonia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1829 ---

输入文本: Zidovudine use in pregnancy: a report on 104 cases and the occurrence of birth defects.

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
      "cause": "Zidovudine",
      "effect": "birth defects"
    }
  ],
  "pred_triples": []
}
```

### --- id=1847 ---

输入文本: To our knowledge, this is the first case of polymyositis associated with dilated cardiomyopathy after the administration of interferon in a patient with hepatitis B.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "interferon"
      },
      "effect": {
        "span": "polymyositis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "interferon"
      },
      "effect": {
        "span": "dilated cardiomyopathy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1856 ---

输入文本: The allopurinol hypersensitivity syndrome is a rare adverse drug reaction.

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
      "cause": "allopurinol",
      "effect": "hypersensitivity syndrome"
    }
  ],
  "pred_triples": []
}
```

### --- id=1865 ---

输入文本: Reversible valproate hepatotoxicity due to mutations in mitochondrial DNA polymerase gamma (POLG1).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "valproate"
      },
      "effect": {
        "span": "valproate hepatotoxicity"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1869 ---

输入文本: Skin prick testing several weeks later identified diamorphine as the likely causative agent, a drug overlooked initially as a potential cause.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "diamorphine"
      },
      "effect": {
        "span": "Skin prick testing several weeks later identified diamorphine as the likely causative agent"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1872 ---

输入文本: This unique syndrome should be identified as a direct causal effect of paclitaxel.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "paclitaxel"
      },
      "effect": {
        "span": "This unique syndrome"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1874 ---

输入文本: Case studies in heparin-induced thrombocytopenia.

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
      "cause": "heparin",
      "effect": "thrombocytopenia"
    }
  ],
  "pred_triples": []
}
```

### --- id=1899 ---

输入文本: Lipoid pneumonia: a silent complication of mineral oil aspiration.

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
      "cause": "mineral oil",
      "effect": "Lipoid pneumonia"
    }
  ],
  "pred_triples": []
}
```

### --- id=1909 ---

输入文本: Rapid development of keratoacanthoma and accelerated transformation into squamous cell carcinoma of the skin: a mutagenic effect of polychemotherapy in a patient with Hodgkin's disease?

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "polychemotherapy"
      },
      "effect": {
        "span": "keratoacanthoma"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "polychemotherapy"
      },
      "effect": {
        "span": "accelerated transformation into squamous cell carcinoma"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1920 ---

输入文本: Since amiodarone was first marketed in 1992 in Japan, the incidence of amiodarone-induced thyrotoxicosis (AIT) has been increasing.

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
      "cause": "amiodarone",
      "effect": "AIT"
    },
    {
      "cause": "amiodarone",
      "effect": "thyrotoxicosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "amiodarone"
      },
      "effect": {
        "span": "amiodarone-induced thyrotoxicosis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1922 ---

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

### --- id=1933 ---

输入文本: This patient developed severe lipoatrophy with the use of a premixed insulin containing the analogue insulin aspart.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "insulin aspart"
      },
      "effect": {
        "span": "severe lipoatrophy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1935 ---

输入文本: A case of a 53-year-old man who developed acute pneumonitis after bleomycin and moderate oxygen administration is presented.

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
      "cause": "bleomycin",
      "effect": "acute pneumonitis"
    },
    {
      "cause": "oxygen",
      "effect": "acute pneumonitis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "bleomycin"
      },
      "effect": {
        "span": "acute pneumonitis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1967 ---

输入文本: We report a case of a patient with rheumatoid arthritis treated with low-dose methotrexate (15 mg/week) who developed infection with both M. tuberculosis and M. chelonae after the revision of a prosthetic hip.

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
      "effect": "infection with both M. tuberculosis and M. chelonae"
    }
  ],
  "pred_triples": []
}
```

### --- id=1983 ---

输入文本: CONCLUSION: Atovaquone should be added to the list of agents causing vortex keratopathy involving the corneal epithelium.

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
      "cause": "Atovaquone",
      "effect": "vortex keratopathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Atovaquone"
      },
      "effect": {
        "span": "vortex keratopathy"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Atovaquone"
      },
      "effect": {
        "span": "vortex keratopathy involving the corneal epithelium"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2044 ---

输入文本: This report describes a case of fatal haemolytic uraemic syndrome (HUS) developing in a child with acute lymphoblastic leukaemia (ALL) during induction chemotherapy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "induction chemotherapy"
      },
      "effect": {
        "span": "fatal haemolytic uraemic syndrome"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2047 ---

输入文本: Radiation recall from gemcitabine is rare, but can potentially arise in any site that has been previously irradiated.

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
      "cause": "gemcitabine",
      "effect": "Radiation recall"
    }
  ],
  "pred_triples": []
}
```

### --- id=2178 ---

输入文本: INTRODUCTION: Although gefitinib used for the treatment of non-small-cell lung cancer is a well-known cause of interstitial lung disease (ILD), few case reports on erlotinib-induced ILD have been issued.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "gefitinib",
      "effect": "ILD"
    },
    {
      "cause": "erlotinib",
      "effect": "ILD"
    },
    {
      "cause": "gefitinib",
      "effect": "interstitial lung disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "gefitinib"
      },
      "effect": {
        "span": "interstitial lung disease"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "erlotinib"
      },
      "effect": {
        "span": "ILD"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2212 ---

输入文本: Acute hemorrhagic gastritis associated with acetazolamide intoxication in a patient with chronic renal failure.

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
      "cause": "acetazolamide",
      "effect": "acetazolamide intoxication"
    },
    {
      "cause": "acetazolamide",
      "effect": "Acute hemorrhagic gastritis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "acetazolamide"
      },
      "effect": {
        "span": "Acute hemorrhagic gastritis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2216 ---

输入文本: To our knowledge, drug-induced fever has not been reported with the use of diltiazem hydrochloride, a commonly prescribed calcium channel blocker.

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
      "cause": "diltiazem hydrochloride",
      "effect": "fever"
    }
  ],
  "pred_triples": []
}
```

### --- id=2305 ---

输入文本: Patient A reported right leg weakness (foot drop) during week 4 of CAP-XRT (1600 mg/m2).

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
      "cause": "CAP-XRT",
      "effect": "foot drop"
    },
    {
      "cause": "CAP-XRT",
      "effect": "right leg weakness"
    }
  ],
  "pred_triples": []
}
```

### --- id=2326 ---

输入文本: We present the first case of WES in an infant born to a mother taking haloperidol during her pregnancy.

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
      "cause": "haloperidol",
      "effect": "WES"
    }
  ],
  "pred_triples": []
}
```

### --- id=2335 ---

输入文本: When co-trimoxazole was stopped the red cell aplasia resolved.

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
      "cause": "co-trimoxazole",
      "effect": "red cell aplasia"
    }
  ],
  "pred_triples": []
}
```

### --- id=2346 ---

输入文本: Severe steroid-induced glaucoma following intravitreal injection of triamcinolone acetonide.

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
      "cause": "steroid",
      "effect": "glaucoma"
    },
    {
      "cause": "triamcinolone acetonide",
      "effect": "glaucoma"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "triamcinolone acetonide"
      },
      "effect": {
        "span": "Severe steroid-induced glaucoma"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2378 ---

输入文本: Gold nephropathy.

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
      "cause": "Gold",
      "effect": "nephropathy"
    }
  ],
  "pred_triples": []
}
```

### --- id=2399 ---

输入文本: We describe a case of disseminated muscular cysticercosis followed by myositis (fever, diffuse myalgia, weakness of the lower limbs, and inflammatory reaction around dying cysticerci) induced by praziquantel therapy, an event not described previously.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 6,
    "fn": 5
  },
  "anchor_window_counts": {
    "tp": 5,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 6,
    "fn": 5
  },
  "gold_relations": [
    {
      "cause": "praziquantel",
      "effect": "diffuse myalgia"
    },
    {
      "cause": "praziquantel",
      "effect": "fever"
    },
    {
      "cause": "praziquantel",
      "effect": "inflammatory reaction around dying cysticerci"
    },
    {
      "cause": "praziquantel",
      "effect": "myositis"
    },
    {
      "cause": "praziquantel",
      "effect": "weakness of the lower limbs"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "praziquantel therapy"
      },
      "effect": {
        "span": "disseminated muscular cysticercosis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "praziquantel therapy"
      },
      "effect": {
        "span": "myositis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "praziquantel therapy"
      },
      "effect": {
        "span": "fever"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "praziquantel therapy"
      },
      "effect": {
        "span": "diffuse myalgia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "praziquantel therapy"
      },
      "effect": {
        "span": "weakness of the lower limbs"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "praziquantel therapy"
      },
      "effect": {
        "span": "inflammatory reaction around dying cysticerci"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2401 ---

输入文本: Hepatitis with bridging fibrosis and reversible hepatic insufficiency in a woman with rheumatoid arthritis taking methotrexate.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "methotrexate",
      "effect": "bridging fibrosis"
    },
    {
      "cause": "methotrexate",
      "effect": "Hepatitis"
    },
    {
      "cause": "methotrexate",
      "effect": "reversible hepatic insufficiency"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methotrexate"
      },
      "effect": {
        "span": "Hepatitis with bridging fibrosis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "methotrexate"
      },
      "effect": {
        "span": "reversible hepatic insufficiency"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2456 ---

输入文本: The increasing prevalence of methamphetamine abuse and the severity of the associated ulcers should alert ophthalmologists to the problem of methamphetamine-related keratitis.

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
      "cause": "methamphetamine",
      "effect": "keratitis"
    },
    {
      "cause": "methamphetamine",
      "effect": "ulcers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methamphetamine"
      },
      "effect": {
        "span": "keratitis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2465 ---

输入文本: Oral 25-hydroxyvitain D3 in treatment of osteomalacia associated with ileal resection and cholestyramine therapy.

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
      "cause": "25-hydroxyvitain D3",
      "effect": "ileal resection"
    }
  ],
  "pred_triples": []
}
```

### --- id=2502 ---

输入文本: On day 7 of linezolid treatment, the patient developed severe pruritus, macular rash, facial edema, eosinophilia, marked increase in serum creatinine level, and mild hepatitis.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 5,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 5,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 5,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "linezolid",
      "effect": "eosinophilia"
    },
    {
      "cause": "linezolid",
      "effect": "facial edema"
    },
    {
      "cause": "linezolid",
      "effect": "macular rash"
    },
    {
      "cause": "linezolid",
      "effect": "marked increase in serum creatinine level"
    },
    {
      "cause": "linezolid",
      "effect": "mild hepatitis"
    },
    {
      "cause": "linezolid",
      "effect": "severe pruritus"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "linezolid"
      },
      "effect": {
        "span": "severe pruritus"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "linezolid"
      },
      "effect": {
        "span": "macular rash"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "linezolid"
      },
      "effect": {
        "span": "facial edema"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "linezolid"
      },
      "effect": {
        "span": "eosinophilia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "linezolid"
      },
      "effect": {
        "span": "mild hepatitis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2628 ---

输入文本: ADR induced by drug treatment can be a side effect of treatment with antipsychotic drugs and other drugs; however, there have been no reports of lamivudine-induced ADR in the English literature.

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
      "cause": "lamivudine",
      "effect": "ADR"
    }
  ],
  "pred_triples": []
}
```

### --- id=2632 ---

输入文本: Avascular necrosis of the femoral head in patients with prostate cancer treated with cyproterone acetate and radiotherapy.

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
      "cause": "cyproterone acetate",
      "effect": "Avascular necrosis of the femoral head"
    }
  ],
  "pred_triples": []
}
```

### --- id=2798 ---

输入文本: We present a case of the syndrome of inappropriate antidiuretic hormone (SIADH) secondary to cisplatin therapy in a patient with advanced-stage large cell neuroendocrine carcinoma of the cervix.

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
      "cause": "cisplatin",
      "effect": "SIADH"
    },
    {
      "cause": "cisplatin",
      "effect": "syndrome of inappropriate antidiuretic hormone"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cisplatin therapy"
      },
      "effect": {
        "span": "syndrome of inappropriate antidiuretic hormone (SIADH)"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2800 ---

输入文本: During and after IFN therapy we should consider the possibility of occurrence of IDDM as well as other autoimmune diseases and observe the clinical course carefully.

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
      "cause": "IFN",
      "effect": "IDDM"
    }
  ],
  "pred_triples": []
}
```

### --- id=2814 ---

输入文本: Hepatotoxicity from green tea: a review of the literature and two unpublished cases.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "green tea"
      },
      "effect": {
        "span": "Hepatotoxicity"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2840 ---

输入文本: The aim of this study is to draw attention to the adverse effects of henna, applied over the whole body, observed in glucose-6-phosphate dehydrogenase (G6PD) enzyme deficient siblings.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "henna"
      },
      "effect": {
        "span": "adverse effects"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2947 ---

输入文本: Delayed pseudocyst of the pancreas can be a complication of intramuscular L-asparaginase.

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
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "L-asparaginase",
      "effect": "Delayed pseudocyst of the pancreas"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "intramuscular L-asparaginase"
      },
      "effect": {
        "span": "pseudocyst of the pancreas"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2948 ---

输入文本: The cause of these previously unreported side effects of niacin therapy is uncertain but may be related to prostaglandin-mediated vasodilatation, hyperalgesia of sensory nerve receptors, and potentiation of inflammation in the gingiva with referral of pain to the teeth.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "niacin",
      "effect": "hyperalgesia of sensory nerve receptors"
    },
    {
      "cause": "niacin",
      "effect": "pain to the teeth"
    },
    {
      "cause": "niacin",
      "effect": "potentiation of inflammation in the gingiva"
    },
    {
      "cause": "niacin",
      "effect": "prostaglandin-mediated vasodilatation"
    }
  ],
  "pred_triples": []
}
```

### --- id=2956 ---

输入文本: When measured, the serum lithium level had increased 4-fold during acyclovir therapy.

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
      "cause": "acyclovir",
      "effect": "serum lithium level had increased"
    },
    {
      "cause": "lithium",
      "effect": "serum lithium level had increased"
    }
  ],
  "pred_triples": []
}
```

### --- id=3125 ---

输入文本: Surprisingly, insulin therapy had to be suspended because of hypoglycemic fits and treatment with metformin was started.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "insulin therapy"
      },
      "effect": {
        "span": "hypoglycemic fits"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3145 ---

输入文本: One week after the termination of IFN therapy, TSH-receptor antibodies became positive and subsequently she showed Graves' hyperthyroidism.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "IFN therapy"
      },
      "effect": {
        "span": "TSH-receptor antibodies became positive"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "IFN therapy"
      },
      "effect": {
        "span": "Graves' hyperthyroidism"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3159 ---

输入文本: She had been on Copaxone 20 mg/day treatment for 2 years when she first exhibited gastrointestinal symptoms.

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
      "cause": "Copaxone",
      "effect": "gastrointestinal symptoms"
    }
  ],
  "pred_triples": []
}
```

### --- id=3176 ---

输入文本: The wide use of phenytoin during the recent tuberculosis epidemic makes it imperative to suspect this drug interaction in patients exhibiting clinical features that might be related to phenytoin toxicity.

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
      "cause": "phenytoin",
      "effect": "phenytoin toxicity"
    }
  ],
  "pred_triples": []
}
```

### --- id=3287 ---

输入文本: A severe lidocaine intoxication by cutaneous absorption is described.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "lidocaine"
      },
      "effect": {
        "span": "severe lidocaine intoxication"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3332 ---

输入文本: The authors report a longitudinal case study of a woman with a history of bipolar affective disorder in which L-dopa shortened the manic-depressive cycle length when administered in a double-blind trial.

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
      "cause": "L-dopa",
      "effect": "shortened the manic-depressive cycle"
    }
  ],
  "pred_triples": []
}
```

### --- id=3359 ---

输入文本: The side effects in all patients have included varying degrees of anorexia, fatigue, ipsilateral forehead dermatitis, blepharitis, and conjunctivitis.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "all patients"
      },
      "effect": {
        "span": "anorexia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "all patients"
      },
      "effect": {
        "span": "fatigue"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "all patients"
      },
      "effect": {
        "span": "ipsilateral forehead dermatitis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "all patients"
      },
      "effect": {
        "span": "blepharitis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "all patients"
      },
      "effect": {
        "span": "conjunctivitis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3407 ---

输入文本: It occasionally accompanies the heparin-associated thrombocytopenia and thrombosis syndrome.

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
      "cause": "heparin",
      "effect": "thrombocytopenia"
    },
    {
      "cause": "heparin",
      "effect": "thrombosis syndrome"
    }
  ],
  "pred_triples": []
}
```

### --- id=3487 ---

输入文本: The pulmonary emboli were thought to be associated with her oral contraceptive, which was discontinued at hospital admission.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "oral contraceptive"
      },
      "effect": {
        "span": "pulmonary emboli"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3497 ---

输入文本: Pulmonary gold toxicity.

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
      "cause": "gold",
      "effect": "Pulmonary gold toxicity"
    }
  ],
  "pred_triples": []
}
```

### --- id=3508 ---

输入文本: Based on these findings, the patient was diagnosed with DRESS/DIHS caused by zonisamide.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "zonisamide"
      },
      "effect": {
        "span": "DRESS/DIHS"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3570 ---

输入文本: A 61-year-old man with early diffuse cutaneous scleroderma with myositis and progressive interstitial pneumonia developed generalized erythema with high fever 3 weeks after taking sulfamethoxazole/trimethoprim.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "sulfamethoxazole",
      "effect": "generalized erythema"
    },
    {
      "cause": "trimethoprim",
      "effect": "generalized erythema"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "sulfamethoxazole"
      },
      "effect": {
        "span": "generalized erythema"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "trimethoprim"
      },
      "effect": {
        "span": "generalized erythema"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "sulfamethoxazole"
      },
      "effect": {
        "span": "high fever"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "trimethoprim"
      },
      "effect": {
        "span": "high fever"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3574 ---

输入文本: Cryptococcus neoformans fatal sepsis in a chronic lymphocytic leukemia patient treated with alemtuzumab: case report and review of the literature.

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
      "cause": "alemtuzumab",
      "effect": "Cryptococcus neoformans fatal sepsis"
    }
  ],
  "pred_triples": []
}
```

### --- id=3580 ---

输入文本: 1. Changes in the plasma cortisol level were reported in a male patient with panic disorder during the period of low-dose alprazolam treatment (mean 0.62 +/- 0.15 mg/day) compared with during the period of high-dose period (mean 1.08 +/- 0.28 mg/day).

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
      "cause": "alprazolam",
      "effect": "Changes in the plasma cortisol level"
    }
  ],
  "pred_triples": []
}
```

### --- id=3610 ---

输入文本: CONCLUSIONS: Although budesonide may be beneficial because of its anti-inflammatory effects, clinicians should be alert to its potential for causing contact dermatitis.

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
      "cause": "budesonide",
      "effect": "contact dermatitis"
    }
  ],
  "pred_triples": []
}
```

### --- id=3647 ---

输入文本: Two infants developed hyperkalemia shortly after cessation of prolonged ACTH therapy for infantile spasms.

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
      "cause": "ACTH",
      "effect": "hyperkalemia"
    }
  ],
  "pred_triples": []
}
```

### --- id=3652 ---

输入文本: CONCLUSIONS: This case report showed that the clinical appearance of Hashimoto's disease after IFN-alpha therapy for chronic C hepatitis in our patient was associated with a specific genetic predisposition (DR5) for this pathology.

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
      "cause": "IFN-alpha",
      "effect": "Hashimoto's disease"
    }
  ],
  "pred_triples": []
}
```

### --- id=3724 ---

输入文本: With the increasing use of Cyclosporine A in transplant patients, the incidence of herpes esophagitis may increase.

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
      "cause": "Cyclosporine A",
      "effect": "herpes esophagitis"
    }
  ],
  "pred_triples": []
}
```

### --- id=3847 ---

输入文本: Therefore, we diagnosed her eruption as contact dermatitis due to sodium bisulfite.

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
      "cause": "sodium bisulfite",
      "effect": "contact dermatitis"
    },
    {
      "cause": "sodium bisulfite",
      "effect": "eruption"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "sodium bisulfite"
      },
      "effect": {
        "span": "contact dermatitis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3872 ---

输入文本: Coagulation activation and fluid retention associated with the use of black cohosh: a case study.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "black cohosh"
      },
      "effect": {
        "span": "Coagulation activation"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "black cohosh"
      },
      "effect": {
        "span": "fluid retention"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3875 ---

输入文本: We report the case of an 87-year-old white woman with myasthenia gravis who presented with nausea, shortness of breath, azotemia, and hyperkalemia shortly after completing a course of intravenous immunoglobulin (IVIG).

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 8
  },
  "anchor_window_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 8
  },
  "gold_relations": [
    {
      "cause": "immunoglobulin",
      "effect": "azotemia"
    },
    {
      "cause": "IVIG",
      "effect": "azotemia"
    },
    {
      "cause": "immunoglobulin",
      "effect": "hyperkalemia"
    },
    {
      "cause": "IVIG",
      "effect": "hyperkalemia"
    },
    {
      "cause": "immunoglobulin",
      "effect": "nausea"
    },
    {
      "cause": "IVIG",
      "effect": "nausea"
    },
    {
      "cause": "immunoglobulin",
      "effect": "shortness of breath"
    },
    {
      "cause": "IVIG",
      "effect": "shortness of breath"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "intravenous immunoglobulin"
      },
      "effect": {
        "span": "nausea"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "intravenous immunoglobulin"
      },
      "effect": {
        "span": "shortness of breath"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "intravenous immunoglobulin"
      },
      "effect": {
        "span": "azotemia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "intravenous immunoglobulin"
      },
      "effect": {
        "span": "hyperkalemia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3938 ---

输入文本: Visual loss after a single small dose of vincristine has never been reported.

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
      "cause": "vincristine",
      "effect": "Visual loss"
    }
  ],
  "pred_triples": []
}
```

### --- id=3939 ---

输入文本: Vincristine overdose (7.5 mg/m2) was accidentally administered to 3 children with acute lymphoblastic leukemia.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Vincristine"
      },
      "effect": {
        "span": "overdose"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3945 ---

输入文本: We conclude that while thrombocytopenia and schistocytosis can be seen in quinine-associated TTP/HUS, the pathophysiology seems to be distinct from that seen in most cases of idiopathic TTP (i.e., severely decreased ADAMTS13 with an inhibitor).

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
      "cause": "quinine",
      "effect": "schistocytosis"
    },
    {
      "cause": "quinine",
      "effect": "thrombocytopenia"
    },
    {
      "cause": "quinine",
      "effect": "TTP/HUS"
    }
  ],
  "pred_triples": []
}
```

### --- id=3969 ---

输入文本: The rash seen in this patient, who was treated with cephalexin, may be similar to the rash seen with ampicillin treatment of patients with infectious mononucleosis.

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
      "cause": "cephalexin",
      "effect": "rash"
    },
    {
      "cause": "ampicillin",
      "effect": "rash"
    }
  ],
  "pred_triples": []
}
```

### --- id=4154 ---

输入文本: Transient, nonpigmenting fixed drug eruption caused by radiopaque contrast media.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "radiopaque contrast media"
      },
      "effect": {
        "span": "nonpigmenting fixed drug eruption"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4171 ---

输入文本: Controversy concerning the nephrotoxicity of lithium is discussed, and recommendations for the evaluation of renal failure during lithium therapy are provided.

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
      "cause": "lithium",
      "effect": "nephrotoxicity"
    },
    {
      "cause": "lithium",
      "effect": "renal failure"
    }
  ],
  "pred_triples": []
}
```

### --- id=4187 ---

输入文本: The pharmaceutical company producing Halfan has reported 8 cardiac arrests, leading to 6 deaths, when a higher dose than recommended was used, there was recent or concomitant treatment with mefloquine, there was pre-existing prolongation of the QT interval or the patient had a thiamine deficiency.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Halfan",
      "effect": "cardiac arrests"
    },
    {
      "cause": "mefloquine",
      "effect": "cardiac arrests"
    },
    {
      "cause": "Halfan",
      "effect": "deaths"
    },
    {
      "cause": "mefloquine",
      "effect": "deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Halfan"
      },
      "effect": {
        "span": "cardiac arrests"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Halfan"
      },
      "effect": {
        "span": "deaths"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4256 ---

输入文本: Prior to surgery, levodopa induced dyskinesia had improved (< or = 50%) under treatment with amantadine (400 mg/day, po) in all three patients.

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
      "cause": "levodopa",
      "effect": "dyskinesia"
    }
  ],
  "pred_triples": []
}
```

### --- id=4298 ---

输入文本: Ventricular tachycardia after ingestion of ayurveda herbal antidiarrheal medication containing aconitum.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "aconitum"
      },
      "effect": {
        "span": "Ventricular tachycardia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4333 ---

输入文本: A 57-year-old woman presented with a 3-week history of dysphagia for solids, 6 months after starting treatment with nifedipine.

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
      "cause": "nifedipine",
      "effect": "dysphagia for solids"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "nifedipine"
      },
      "effect": {
        "span": "dysphagia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4362 ---

输入文本: We suggest that nicotinic acid was the cause of his liver disease, that this case is of particular note because of the rather short period of therapy before the onset of liver injury and the severity of the hepatic failure, and that the probable increased use of nicotinic acid for serum cholesterol control makes it especially important for physicians and their patients to be alert to the signs of hepatotoxicity.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "nicotinic acid",
      "effect": "hepatotoxicity"
    },
    {
      "cause": "nicotinic acid",
      "effect": "liver disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "nicotinic acid"
      },
      "effect": {
        "span": "liver disease"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "nicotinic acid"
      },
      "effect": {
        "span": "liver injury"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "nicotinic acid"
      },
      "effect": {
        "span": "hepatic failure"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4364 ---

输入文本: A child in whom a phenobarbital hypersensitivity drug reaction developed which consisted of fever, a pruritic desquamating erythrodermic rash, alopecia, icterus, protein-losing enteropathy, myositis, and nephritis, is described.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 7,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 6,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 7,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "phenobarbital",
      "effect": "alopecia"
    },
    {
      "cause": "phenobarbital",
      "effect": "a pruritic desquamating erythrodermic rash"
    },
    {
      "cause": "phenobarbital",
      "effect": "fever"
    },
    {
      "cause": "phenobarbital",
      "effect": "hypersensitivity"
    },
    {
      "cause": "phenobarbital",
      "effect": "icterus"
    },
    {
      "cause": "phenobarbital",
      "effect": "myositis"
    },
    {
      "cause": "phenobarbital",
      "effect": "nephritis"
    },
    {
      "cause": "phenobarbital",
      "effect": "protein-losing enteropathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "fever"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "pruritic desquamating erythrodermic rash"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "alopecia"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "icterus"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "protein-losing enteropathy"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "myositis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "phenobarbital"
      },
      "effect": {
        "span": "nephritis"
      },
      "relation": "caused"
    }
  ]
}
```
