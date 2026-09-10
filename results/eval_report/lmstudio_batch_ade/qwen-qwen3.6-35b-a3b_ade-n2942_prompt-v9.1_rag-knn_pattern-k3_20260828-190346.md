# Qwen3.6 35B A3B ADE held-out test eval report

## 配置
```json
{
  "label": "Qwen3.6 35B A3B ADE held-out test",
  "model": "qwen/qwen3.6-35b-a3b",
  "dataset": "ade",
  "sample_count": 2942,
  "prompt_name": "v9.1",
  "use_rag": true,
  "rag_mode": "knn_pattern",
  "rag_top_k": 3,
  "temperature": 0.0,
  "max_tokens": 2048,
  "output_schema": "standard",
  "primary_metric": "anchor_window",
  "progress_every": 1000,
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
  "metadata_path": "D:\\Master thesis\\RAG Database\\bge-small-en-v1.5_examples.jsonl",
  "embeddings_path": "D:\\Master thesis\\RAG Database\\bge-small-en-v1.5_embeddings.npy"
}
```

## 统计指标
```text
================ Qwen3.6 35B A3B ADE held-out test final report ================
样本总数: 2942
  Gold 含因果: 448 | Pred 含因果: 482
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.938
  Precision: 0.776
  Recall   : 0.835
  F1       : 0.804
  (TP=374, TN=2386, FP=108, FN=74)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 2942
    Gold triples: 663 | Pred triples: 673
    Precision: 0.627
    Recall   : 0.637
    F1       : 0.632
    (TP=422, FP=251, FN=241)
  [anchor_window] (primary)
    样本数: 2942
    Gold triples: 663 | Pred triples: 673
    Precision: 0.752
    Recall   : 0.763
    F1       : 0.757
    (TP=506, FP=167, FN=157)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 374
    Gold triples: 559 | Pred triples: 526
    Precision: 0.802
    Recall   : 0.755
    F1       : 0.778
    (TP=422, FP=104, FN=137)
  [anchor_window] (primary)
    样本数: 374
    Gold triples: 559 | Pred triples: 526
    Precision: 0.962
    Recall   : 0.905
    F1       : 0.933
    (TP=506, FP=20, FN=53)
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

Sample details shown: first 200 of 232 wrong samples from 2942 total samples.

### --- id=44 ---

输入文本: Successful treatment of acute dapsone intoxication using charcoal hemoperfusion.

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
        "span": "dapsone"
      },
      "relation": "caused",
      "effect": {
        "span": "dapsone intoxication"
      }
    }
  ]
}
```

### --- id=65 ---

输入文本: Fever and neutrophilic alveolitis caused by a vanadium based catalyst.

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
        "span": "vanadium based catalyst"
      },
      "relation": "caused",
      "effect": {
        "span": "Fever"
      }
    },
    {
      "cause": {
        "span": "vanadium based catalyst"
      },
      "relation": "caused",
      "effect": {
        "span": "neutrophilic alveolitis"
      }
    }
  ]
}
```

### --- id=83 ---

输入文本: The cough continued for the duration of therapy with quinapril.

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
      "cause": "quinapril",
      "effect": "cough"
    }
  ],
  "pred_triples": []
}
```

### --- id=137 ---

输入文本: Additionally, clinically effective doses of conventional antipsychotics can actually aggravate negative symptoms through the development of extrapyramidal symptoms (EPS).

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
        "span": "conventional antipsychotics"
      },
      "relation": "caused",
      "effect": {
        "span": "extrapyramidal symptoms"
      }
    }
  ]
}
```

### --- id=142 ---

输入文本: Osteonecrosis of the jaw is an uncommon consequence of biphosphonate therapy.

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
        "span": "biphosphonate"
      },
      "relation": "caused",
      "effect": {
        "span": "Osteonecrosis of the jaw"
      }
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
      "relation": "caused",
      "effect": {
        "span": "eosinophilic pneumonia"
      }
    }
  ]
}
```

### --- id=160 ---

输入文本: Although, we cannot exclude the coincidence between the two diseases we discussed suspicious relationship between the interferon treatment and the tumour progression.

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
        "span": "interferon"
      },
      "relation": "caused",
      "effect": {
        "span": "tumour progression"
      }
    }
  ]
}
```

### --- id=169 ---

输入文本: Fatal spontaneous spinal epidural hematoma following thrombolysis for myocardial infarction.

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
        "span": "thrombolysis"
      },
      "relation": "caused",
      "effect": {
        "span": "spinal epidural hematoma"
      }
    }
  ]
}
```

### --- id=203 ---

输入文本: Delayed-onset multifocal keratitis is a rare complication of LASIK.

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
        "span": "LASIK"
      },
      "relation": "caused",
      "effect": {
        "span": "multifocal keratitis"
      }
    }
  ]
}
```

### --- id=211 ---

输入文本: Administration of intravenous nitroglycerin in a patient with idiopathic pulmonary hypertension resulted in an increase in pulmonary artery pressure associated with a decrease in blood flow that is best explained by an increase in pulmonary vascular resistance.

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
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
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
  "pred_triples": [
    {
      "cause": {
        "span": "intravenous nitroglycerin"
      },
      "relation": "caused",
      "effect": {
        "span": "increase in pulmonary artery pressure"
      }
    },
    {
      "cause": {
        "span": "intravenous nitroglycerin"
      },
      "relation": "caused",
      "effect": {
        "span": "decrease in blood flow"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "problems"
      }
    },
    {
      "cause": {
        "span": "HAART"
      },
      "relation": "caused",
      "effect": {
        "span": "immune-reconstitution syndrome"
      }
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
        "span": "high-dose inhaled corticosteroids"
      },
      "relation": "caused",
      "effect": {
        "span": "adrenal crises"
      }
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
      "relation": "caused",
      "effect": {
        "span": "severe thrombotic complications"
      }
    }
  ]
}
```

### --- id=246 ---

输入文本: An objective causality assessment suggested that the increased mania was probably related to the decrease in VPA concentration and that a possible interaction exists between lopinavir/ritonavir and VPA.

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
        "span": "lopinavir/ritonavir"
      },
      "relation": "caused",
      "effect": {
        "span": "increased mania"
      }
    },
    {
      "cause": {
        "span": "VPA"
      },
      "relation": "caused",
      "effect": {
        "span": "increased mania"
      }
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
      "relation": "caused",
      "effect": {
        "span": "malacoplakia"
      }
    }
  ]
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
      "cause": "M-CSF",
      "effect": "macrophage-related glomerular injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "M-CSF"
      },
      "relation": "caused",
      "effect": {
        "span": "glomerular injury"
      }
    }
  ]
}
```

### --- id=281 ---

输入文本: In this report, we will describe the first case of obsessive-compulsive behaviour following oral corticosteroid treatment in a 75-year old adult male patient with pulmonary disease, but without previous psychiatric symptoms or organic brain disorder.

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
        "span": "oral corticosteroid"
      },
      "relation": "caused",
      "effect": {
        "span": "obsessive-compulsive behaviour"
      }
    }
  ]
}
```

### --- id=286 ---

输入文本: A retrospective review of TTP patients with quinine-associated thrombotic microangiopathy (TMA) for whom ADAMTS13 was measured before plasma exchange was performed.

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
      "cause": "quinine",
      "effect": "thrombotic microangiopathy"
    },
    {
      "cause": "quinine",
      "effect": "TMA"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "quinine"
      },
      "relation": "caused",
      "effect": {
        "span": "thrombotic microangiopathy"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "paranoid psychosis"
      }
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
      "relation": "caused",
      "effect": {
        "span": "sudden deaths"
      }
    },
    {
      "cause": {
        "span": "Pentavalent antimonial drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "ventricular tachyarrhythmias"
      }
    }
  ]
}
```

### --- id=299 ---

输入文本: Thrombotic thrombocytopenic purpura induced by trimethoprim-sulfamethoxazole in a Jehovah's Witness.

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
      "cause": "sulfamethoxazole",
      "effect": "Thrombotic thrombocytopenic purpura"
    },
    {
      "cause": "trimethoprim",
      "effect": "Thrombotic thrombocytopenic purpura"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "trimethoprim-sulfamethoxazole"
      },
      "relation": "caused",
      "effect": {
        "span": "Thrombotic thrombocytopenic purpura"
      }
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

### --- id=326 ---

输入文本: Hypersexuality with antiparkinsonian therapy.

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
        "span": "antiparkinsonian therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "Hypersexuality"
      }
    }
  ]
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

### --- id=332 ---

输入文本: A case of pseudotumor cerebri following glucocorticoid therapy in which warfarin prevented recurrence.

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
        "span": "glucocorticoid therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "pseudotumor cerebri"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "Severe adenovirus pneumonia"
      }
    }
  ]
}
```

### --- id=390 ---

输入文本: The purpose of this work is to report the case of oral chemical burns caused by topical self-medication for tooth pain relief, and also to discuss the clinical presentation and the treatment performed.

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
        "span": "topical self-medication"
      },
      "relation": "caused",
      "effect": {
        "span": "oral chemical burns"
      }
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
      "relation": "caused",
      "effect": {
        "span": "multiple hepatic adenomas"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "Graft versus host-like illness"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "male breast cancer"
      }
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
      "relation": "caused",
      "effect": {
        "span": "severe central nervous system insult"
      }
    },
    {
      "cause": {
        "span": "Methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "bilateral putaminal injury"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Cough"
      }
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
      "relation": "caused",
      "effect": {
        "span": "acute angle-closure glaucoma"
      }
    }
  ]
}
```

### --- id=490 ---

输入文本: These features have not previously been reported as side effects of glibenclamide therapy, but intrahepatic cholestasis may occur with chlorpropamide, a similar sulphonylurea agent.

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
      "cause": "chlorpropamide",
      "effect": "intrahepatic cholestasis"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "Hepatocellular carcinoma"
      }
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
      "relation": "caused",
      "effect": {
        "span": "AHS"
      }
    },
    {
      "cause": {
        "span": "phenobarbital"
      },
      "relation": "caused",
      "effect": {
        "span": "alopecia areata (AA) universalis"
      }
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
      "relation": "caused",
      "effect": {
        "span": "acute myelomonoblastic leukemia"
      }
    }
  ]
}
```

### --- id=522 ---

输入文本: We present 2 patients with demonstrated IgE-mediated allergy to cloxacillin and tolerance to amoxicillin and cefuroxime.

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
        "span": "cloxacillin"
      },
      "relation": "caused",
      "effect": {
        "span": "IgE-mediated allergy"
      }
    }
  ]
}
```

### --- id=533 ---

输入文本: We describe children and adolescents with chronic hematologic and oncologic diseases who exhibited drug-seeking behavior or anticholinergic symptoms with the use of diphenhydramine.

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
      "cause": "diphenhydramine",
      "effect": "anticholinergic symptoms"
    },
    {
      "cause": "diphenhydramine",
      "effect": "drug-seeking behavior"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "diphenhydramine"
      },
      "relation": "caused",
      "effect": {
        "span": "anticholinergic symptoms"
      }
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
      "relation": "caused",
      "effect": {
        "span": "new onset type II diabetes mellitus"
      }
    },
    {
      "cause": {
        "span": "SGA"
      },
      "relation": "caused",
      "effect": {
        "span": "hyperosmolar hyperglycaemic coma"
      }
    },
    {
      "cause": {
        "span": "SGA"
      },
      "relation": "caused",
      "effect": {
        "span": "acute renal failure"
      }
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
      "relation": "caused",
      "effect": {
        "span": "cocaine toxicity"
      }
    },
    {
      "cause": {
        "span": "cocaine"
      },
      "relation": "caused",
      "effect": {
        "span": "hypertension"
      }
    },
    {
      "cause": {
        "span": "cocaine"
      },
      "relation": "caused",
      "effect": {
        "span": "tachycardia"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Ocular toxicity"
      }
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
      "cause": "methotrexate",
      "effect": "sub-acute leukoencephalopathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "sub-acute leukoencephalopathy"
      }
    },
    {
      "cause": {
        "span": "intrathecal triple-drug therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "right-sided paralysis"
      }
    },
    {
      "cause": {
        "span": "intrathecal triple-drug therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "aphasia"
      }
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
      "relation": "caused",
      "effect": {
        "span": "complications"
      }
    },
    {
      "cause": {
        "span": "Kayexalate"
      },
      "relation": "caused",
      "effect": {
        "span": "complications"
      }
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
      "relation": "caused",
      "effect": {
        "span": "leukopenia"
      }
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
      "relation": "caused",
      "effect": {
        "span": "fatal marrow aplasia"
      }
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
      "relation": "caused",
      "effect": {
        "span": "serotonin syndrome"
      }
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

### --- id=835 ---

输入文本: CASE HISTORY: A 58-year-old male Caucasian developed delayed onset diffuse lamellar keratitis, seemingly in the absence of an epithelial defect, 25 days following an enhancement LASIK procedure to his right eye.

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
        "span": "LASIK"
      },
      "relation": "caused",
      "effect": {
        "span": "diffuse lamellar keratitis"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
    },
    {
      "cause": {
        "span": "Hyamine 3500"
      },
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
    },
    {
      "cause": {
        "span": "cationic detergents"
      },
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
    },
    {
      "cause": {
        "span": "isopropyl alcohol"
      },
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
    },
    {
      "cause": {
        "span": "sodium nitrite"
      },
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
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
      "relation": "caused",
      "effect": {
        "span": "herpes zoster ophthalmicus"
      }
    },
    {
      "cause": {
        "span": "Vaccine"
      },
      "relation": "caused",
      "effect": {
        "span": "encephalitis"
      }
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
      "relation": "caused",
      "effect": {
        "span": "selective nephrotoxicity"
      }
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

### --- id=921 ---

输入文本: Use of the Naranjo probability scale determined the association between cephalosporin use and leukopenia to be probable.

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
      "cause": "cephalosporin",
      "effect": "leukopenia"
    }
  ],
  "pred_triples": []
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

### --- id=935 ---

输入文本: A 53-year-old female who developed myelodysplastic syndrome (MDS) after chemotherapy for adult T-cell leukaemia (ATL) is described.

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
        "span": "chemotherapy"
      },
      "relation": "caused",
      "effect": {
        "span": "myelodysplastic syndrome"
      }
    }
  ]
}
```

### --- id=938 ---

输入文本: Intravitreal bevacizumab was administered and optical coherence tomography revealed worsening of the cystoid macular edema 1 month after the injection.

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
        "span": "bevacizumab"
      },
      "relation": "caused",
      "effect": {
        "span": "worsening of the cystoid macular edema"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "mixed mania"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Severe lidocaine intoxication"
      }
    }
  ]
}
```

### --- id=952 ---

输入文本: Pellagra should be suspected whenever tuberculous patients under treatment with isoniazid develop mental, neurological or gastrointestinal symptoms, even in the absence of typical pellagra dermatitis.

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
      "cause": "isoniazid",
      "effect": "mental, neurological or gastrointestinal symptoms"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "isoniazid"
      },
      "relation": "caused",
      "effect": {
        "span": "Pellagra"
      }
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

### --- id=974 ---

输入文本: A case of normotensive scleroderma renal crisis after high-dose methylprednisolone treatment.

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
      "cause": "methylprednisolone",
      "effect": "normotensive scleroderma renal crisis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methylprednisolone"
      },
      "relation": "caused",
      "effect": {
        "span": "scleroderma renal crisis"
      }
    }
  ]
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
        "span": "bretylium"
      },
      "relation": "caused",
      "effect": {
        "span": "cardiac arrests"
      }
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
      "relation": "caused",
      "effect": {
        "span": "hypothyroidism"
      }
    }
  ]
}
```

### --- id=1087 ---

输入文本: Nocardiosis after corticosteroid therapy for malignant thymoma.

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
        "span": "corticosteroid"
      },
      "relation": "caused",
      "effect": {
        "span": "Nocardiosis"
      }
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
        "span": "psoralen-ultraviolet-A (PUVA)"
      },
      "relation": "caused",
      "effect": {
        "span": "Systemic lupus erythematosus (SLE)"
      }
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

### --- id=1125 ---

输入文本: We describe two patients with profound hypothalamic-pituitary-adrenal axis suppression resulting from the unregulated use of super potent topical corticosteroids.

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
        "span": "super potent topical corticosteroids"
      },
      "relation": "caused",
      "effect": {
        "span": "profound hypothalamic-pituitary-adrenal axis suppression"
      }
    }
  ]
}
```

### --- id=1165 ---

输入文本: Visual system side effects caused by parasympathetic dysfunction after botulinum toxin type B injections.

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
      "cause": "botulinum toxin type B",
      "effect": "parasympathetic dysfunction"
    },
    {
      "cause": "botulinum toxin type B",
      "effect": "Visual system side effects"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "allergic contact and/or photocontact dermatitis"
      }
    }
  ]
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

### --- id=1231 ---

输入文本: Pseudomembranous colitis readily occurs in at least certain population groups receiving trimethoprim-sulfamethoxazole.

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
      "cause": "sulfamethoxazole",
      "effect": "Pseudomembranous colitis"
    },
    {
      "cause": "trimethoprim",
      "effect": "Pseudomembranous colitis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "trimethoprim-sulfamethoxazole"
      },
      "relation": "caused",
      "effect": {
        "span": "Pseudomembranous colitis"
      }
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
      "relation": "caused",
      "effect": {
        "span": "agenesis of the cerebellar vermis"
      }
    },
    {
      "cause": {
        "span": "isotretinoin"
      },
      "relation": "caused",
      "effect": {
        "span": "multiple leptomeningeal neuroglial heterotopias"
      }
    },
    {
      "cause": {
        "span": "isotretinoin"
      },
      "relation": "caused",
      "effect": {
        "span": "hydrocephalus"
      }
    },
    {
      "cause": {
        "span": "isotretinoin"
      },
      "relation": "caused",
      "effect": {
        "span": "abnormalities of the corticospinal tracts"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Pulmonary hemorrhage"
      }
    }
  ]
}
```

### --- id=1264 ---

输入文本: CONCLUSION: Our case shows a fatal side effect of erlotinib.

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
        "span": "erlotinib"
      },
      "relation": "caused",
      "effect": {
        "span": "fatal side effect"
      }
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
      "relation": "caused",
      "effect": {
        "span": "multiple nodules in the liver"
      }
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

### --- id=1269 ---

输入文本: Children seem to be unusually sensitive to the depressant effects of clonidine.

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
        "span": "clonidine"
      },
      "relation": "caused",
      "effect": {
        "span": "depressant effects"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "nephrotic syndrome"
      }
    }
  ]
}
```

### --- id=1287 ---

输入文本: Paranoid psychosis may result from intoxication with, or withdrawal from amphetamines.

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
        "span": "amphetamines"
      },
      "relation": "caused",
      "effect": {
        "span": "Paranoid psychosis"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Reactivation histoplasmosis"
      }
    }
  ]
}
```

### --- id=1322 ---

输入文本: AIMS: To investigate a worker who experienced systemic and respiratory symptoms when exposed to a vanadium containing powder used as a catalyst in the production of maleic anhydride.

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
        "span": "vanadium containing powder"
      },
      "relation": "caused",
      "effect": {
        "span": "systemic and respiratory symptoms"
      }
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

### --- id=1350 ---

输入文本: This case and others indicate that caution should be exercised in administering IFN because low doses can be correlated with myasthenia gravis in patients without malignancies.

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
        "span": "IFN"
      },
      "relation": "caused",
      "effect": {
        "span": "myasthenia gravis"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "status epilepticus"
      }
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

### --- id=1397 ---

输入文本: The persistence of free steroid secretion with decreased formation of DS suggests that the o,p'-DDD may have altered sulfatase activity before causing tumor necrosis and total decrease in steroidogenesis.

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
        "span": "o,p'-DDD"
      },
      "relation": "caused",
      "effect": {
        "span": "tumor necrosis"
      }
    },
    {
      "cause": {
        "span": "o,p'-DDD"
      },
      "relation": "caused",
      "effect": {
        "span": "total decrease in steroidogenesis"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "QT-interval prolongation"
      }
    }
  ]
}
```

### --- id=1436 ---

输入文本: IMPLICATIONS:We discuss the successful management of gangrene of the upper and lower limbs after ergot-induced abortion by unlicensed medical charlatans in a developing country.

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
        "span": "ergot"
      },
      "relation": "caused",
      "effect": {
        "span": "gangrene"
      }
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
      "cause": "3,4-methylenedioxymet-amphetamine Ecstasy",
      "effect": "poisoning"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "3,4-methylenedioxymet-amphetamine Ecstasy"
      },
      "relation": "caused",
      "effect": {
        "span": "poisoning"
      }
    },
    {
      "cause": {
        "span": "3,4-methylenedioxymet-amphetamine Ecstasy"
      },
      "relation": "caused",
      "effect": {
        "span": "fatal outcome"
      }
    }
  ]
}
```

### --- id=1467 ---

输入文本: A patient with Hodgkin's disease developed acute radiation pneumonia four months after completion of mantle radiotherapy and during cyclical adjuvant chemotherapy.

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
        "span": "mantle radiotherapy"
      },
      "relation": "caused",
      "effect": {
        "span": "acute radiation pneumonia"
      }
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

### --- id=1489 ---

输入文本: His symptoms of brain stem compression were alleviated and the role of phenytoin in the production of his craniocervical abnormality is discussed.

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
      "effect": "craniocervical abnormality"
    }
  ],
  "pred_triples": []
}
```

### --- id=1496 ---

输入文本: Lipoatrophy although rare can still occur even with the use of technologically advanced insulin preparations.

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
        "span": "insulin"
      },
      "relation": "caused",
      "effect": {
        "span": "lipoatrophy"
      }
    }
  ]
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
      "cause": "methotrexate",
      "effect": "bilateral pulmonary infiltrates"
    },
    {
      "cause": "methotrexate",
      "effect": "diffuse interstitial pulmonary fibrosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "diffuse interstitial pulmonary fibrosis"
      }
    }
  ]
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
        "span": "hydroxychloroquine"
      },
      "relation": "caused",
      "effect": {
        "span": "loss of photoreceptor inner segment/outer segment (IS/OS) junction"
      }
    },
    {
      "cause": {
        "span": "hydroxychloroquine"
      },
      "relation": "caused",
      "effect": {
        "span": "downward \"sink-hole\" displacement of inner retinal structures"
      }
    }
  ]
}
```

### --- id=1534 ---

输入文本: Drug-induced pemphigoid.

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
        "span": "Drug"
      },
      "relation": "caused",
      "effect": {
        "span": "pemphigoid"
      }
    }
  ]
}
```

### --- id=1537 ---

输入文本: A case of high-grade endometrial stromal sarcoma, confined into an intrauterine polypoid growth, in a woman with a history of breast cancer who was treated with adjuvant tamoxifen.

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
      "cause": "tamoxifen",
      "effect": "high-grade endometrial stromal sarcoma"
    },
    {
      "cause": "tamoxifen",
      "effect": "intrauterine polypoid growth"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "tamoxifen"
      },
      "relation": "caused",
      "effect": {
        "span": "high-grade endometrial stromal sarcoma"
      }
    }
  ]
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
        "span": "TNF-alpha antagonists"
      },
      "relation": "caused",
      "effect": {
        "span": "chronic inflammatory demyelinating polyneuropathy"
      }
    },
    {
      "cause": {
        "span": "TNF-alpha antagonists"
      },
      "relation": "caused",
      "effect": {
        "span": "CIDP"
      }
    }
  ]
}
```

### --- id=1551 ---

输入文本: Alopecia is an adverse effect in those patients taking aromatic anti-convulsant drugs but is rarely reported after discontinuing such medications in the convalescent status of anti-convulsant hypersensitivity syndrome (AHS).

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
        "span": "aromatic anti-convulsant drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "Alopecia"
      }
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
      "relation": "caused",
      "effect": {
        "span": "proximal deep venous thrombosis"
      }
    },
    {
      "cause": {
        "span": "anabolic-androgenic steroids"
      },
      "relation": "caused",
      "effect": {
        "span": "pulmonary embolism"
      }
    }
  ]
}
```

### --- id=1569 ---

输入文本: The latex of Calotropis procera causes significant ocular morbidity which may be preventable by simple health education.

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
      "relation": "caused",
      "effect": {
        "span": "ocular morbidity"
      }
    }
  ]
}
```

### --- id=1592 ---

输入文本: With higher doses of radiation being given by using conformal techniques, more radiation-induced optic neuritis and neuropathy will be identified.

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
        "span": "radiation"
      },
      "relation": "caused",
      "effect": {
        "span": "optic neuritis"
      }
    },
    {
      "cause": {
        "span": "radiation"
      },
      "relation": "caused",
      "effect": {
        "span": "neuropathy"
      }
    }
  ]
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
        "span": "procainamide"
      },
      "relation": "caused",
      "effect": {
        "span": "clinical lupus syndrome"
      }
    },
    {
      "cause": {
        "span": "procainamide"
      },
      "relation": "caused",
      "effect": {
        "span": "diffuse proliferative glomerulonephritis"
      }
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
      "relation": "caused",
      "effect": {
        "span": "granulocytopenia"
      }
    },
    {
      "cause": {
        "span": "propylthiouracil"
      },
      "relation": "caused",
      "effect": {
        "span": "eosinophilia"
      }
    },
    {
      "cause": {
        "span": "propylthiouracil"
      },
      "relation": "caused",
      "effect": {
        "span": "skin reaction"
      }
    },
    {
      "cause": {
        "span": "propylthiouracil"
      },
      "relation": "caused",
      "effect": {
        "span": "hepatitis"
      }
    }
  ]
}
```

### --- id=1624 ---

输入文本: Toxic symptoms (sinus arrest) reappeared twice and were accompanied by increasing amounts of non-antibody-bound DGTX in the serum.

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
        "span": "DGTX"
      },
      "relation": "caused",
      "effect": {
        "span": "sinus arrest"
      }
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
      "relation": "caused",
      "effect": {
        "span": "HC pneumonitis"
      }
    },
    {
      "cause": {
        "span": "lamp oil"
      },
      "relation": "caused",
      "effect": {
        "span": "pneumatoceles"
      }
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
      "relation": "caused",
      "effect": {
        "span": "subacromial impingement syndrome"
      }
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
      "relation": "caused",
      "effect": {
        "span": "life-threatening toxicities"
      }
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

### --- id=1745 ---

输入文本: Prick tests and intradermal tests with a series of dilutions of carboplatin and cisplatin were performed on three patients who had exhibited medium and severe hypersensitivity reactions to carboplatin.

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
      "cause": "carboplatin",
      "effect": "severe hypersensitivity"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "carboplatin"
      },
      "relation": "caused",
      "effect": {
        "span": "hypersensitivity reactions"
      }
    }
  ]
}
```

### --- id=1748 ---

输入文本: The evidence from this series of cases and from six additional cases identified in the literature suggests that the risk of endometrial sarcomas may be increased by estrogen therapy or endogenous disorders that lead to unopposed estrogenic stimulation of the uterus.

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
        "span": "estrogen therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "endometrial sarcomas"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "palmar pruritus"
      }
    },
    {
      "cause": {
        "span": "cisplatin"
      },
      "relation": "caused",
      "effect": {
        "span": "urticaria"
      }
    },
    {
      "cause": {
        "span": "cisplatin"
      },
      "relation": "caused",
      "effect": {
        "span": "edema"
      }
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
        "span": "first product"
      },
      "relation": "caused",
      "effect": {
        "span": "Hyperglycemia"
      }
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
      "relation": "caused",
      "effect": {
        "span": "eosinophilic pneumonia"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "polymyositis"
      }
    },
    {
      "cause": {
        "span": "interferon"
      },
      "relation": "caused",
      "effect": {
        "span": "dilated cardiomyopathy"
      }
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
      "relation": "caused",
      "effect": {
        "span": "hepatotoxicity"
      }
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
      "relation": "caused",
      "effect": {
        "span": "diamorphine"
      }
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
      "relation": "caused",
      "effect": {
        "span": "syndrome"
      }
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

### --- id=1883 ---

输入文本: Aminoglycoside-induced renal tubular dysfunction could result in diffuse damage or manifest as a Fanconi-like syndrome, Bartter-like syndrome, or distal renal tubular acidosis.

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
        "span": "Aminoglycoside"
      },
      "relation": "caused",
      "effect": {
        "span": "renal tubular dysfunction"
      }
    },
    {
      "cause": {
        "span": "Aminoglycoside"
      },
      "relation": "caused",
      "effect": {
        "span": "diffuse damage"
      }
    },
    {
      "cause": {
        "span": "Aminoglycoside"
      },
      "relation": "caused",
      "effect": {
        "span": "Fanconi-like syndrome"
      }
    },
    {
      "cause": {
        "span": "Aminoglycoside"
      },
      "relation": "caused",
      "effect": {
        "span": "Bartter-like syndrome"
      }
    },
    {
      "cause": {
        "span": "Aminoglycoside"
      },
      "relation": "caused",
      "effect": {
        "span": "distal renal tubular acidosis"
      }
    }
  ]
}
```

### --- id=1892 ---

输入文本: Severe methotrexate toxicity occurred in two of these patients.

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
        "span": "methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "methotrexate toxicity"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "keratoacanthoma"
      }
    },
    {
      "cause": {
        "span": "polychemotherapy"
      },
      "relation": "caused",
      "effect": {
        "span": "accelerated transformation into squamous cell carcinoma"
      }
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
      "relation": "caused",
      "effect": {
        "span": "amiodarone-induced thyrotoxicosis"
      }
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

### --- id=1931 ---

输入文本: Psoriasis, razoxane and a cutaneous B-cell lymphoma.

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
        "span": "razoxane"
      },
      "relation": "caused",
      "effect": {
        "span": "Psoriasis"
      }
    },
    {
      "cause": {
        "span": "razoxane"
      },
      "relation": "caused",
      "effect": {
        "span": "cutaneous B-cell lymphoma"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "severe lipoatrophy"
      }
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
      "relation": "caused",
      "effect": {
        "span": "acute pneumonitis"
      }
    }
  ]
}
```

### --- id=1995 ---

输入文本: In one child, a second course of carbamazepine resulted in a return of the dystonia.

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
      "cause": "carbamazepine",
      "effect": "dystonia"
    }
  ],
  "pred_triples": []
}
```

### --- id=2069 ---

输入文本: We describe a case of a man treated with an EGFR-inhibitor (erlotinib) for a cell lung cancer who developed skin manifestations localized in an uncommon area and with an atypical evolution.

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
      "effect": "skin manifestations"
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
      "relation": "caused",
      "effect": {
        "span": "interstitial lung disease"
      }
    },
    {
      "cause": {
        "span": "erlotinib"
      },
      "relation": "caused",
      "effect": {
        "span": "ILD"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Acute hemorrhagic gastritis"
      }
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

### --- id=2300 ---

输入文本: One hour after she drank the second bowl of herbal decoction, she suddenly developed tonic contractions of all her limb muscles and carpopedal spasm lasting 5 min, difficulty in breathing, chest discomfort and perioral numbness.

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
        "span": "herbal decoction"
      },
      "relation": "caused",
      "effect": {
        "span": "tonic contractions of all her limb muscles"
      }
    },
    {
      "cause": {
        "span": "herbal decoction"
      },
      "relation": "caused",
      "effect": {
        "span": "carpopedal spasm"
      }
    },
    {
      "cause": {
        "span": "herbal decoction"
      },
      "relation": "caused",
      "effect": {
        "span": "difficulty in breathing"
      }
    },
    {
      "cause": {
        "span": "herbal decoction"
      },
      "relation": "caused",
      "effect": {
        "span": "chest discomfort"
      }
    },
    {
      "cause": {
        "span": "herbal decoction"
      },
      "relation": "caused",
      "effect": {
        "span": "perioral numbness"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "Severe steroid-induced glaucoma"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Hepatitis with bridging fibrosis"
      }
    },
    {
      "cause": {
        "span": "methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "reversible hepatic insufficiency"
      }
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
      "relation": "caused",
      "effect": {
        "span": "keratitis"
      }
    }
  ]
}
```

### --- id=2461 ---

输入文本: Ileus after administration of cold remedy in an elderly diabetic patient treated with acarbose.

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
        "span": "acarbose"
      },
      "relation": "caused",
      "effect": {
        "span": "Ileus"
      }
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

### --- id=2504 ---

输入文本: Four weeks later, a coronary arteriogram showed only minimal luminal irregularities at the original site of occlusion, where significant reduction in diameter could be induced by ergonovine maleate.

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
        "span": "ergonovine maleate"
      },
      "relation": "caused",
      "effect": {
        "span": "significant reduction in diameter"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Hepatotoxicity"
      }
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
      "relation": "caused",
      "effect": {
        "span": "adverse effects"
      }
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
      "relation": "caused",
      "effect": {
        "span": "pseudocyst of the pancreas"
      }
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
        "span": "insulin"
      },
      "relation": "caused",
      "effect": {
        "span": "hypoglycemic fits"
      }
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
        "span": "IFN"
      },
      "relation": "caused",
      "effect": {
        "span": "Graves' hyperthyroidism"
      }
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
      "relation": "caused",
      "effect": {
        "span": "severe lidocaine intoxication"
      }
    }
  ]
}
```

### --- id=3311 ---

输入文本: Deaths occurring during clinical studies of topical minoxidil.

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
        "span": "topical minoxidil"
      },
      "relation": "caused",
      "effect": {
        "span": "Deaths"
      }
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

### --- id=3414 ---

输入文本: At the onset of the ST elevation, all patients were receiving dopamine infusion, which in four of them was inadvertently increased shortly before the ECG changes, the ST elevation was not associated with chest pain, pericardial friction rub, or acute changes in the heart rate, or arterial blood pressure.

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
        "span": "dopamine infusion"
      },
      "relation": "caused",
      "effect": {
        "span": "ST elevation"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "pulmonary emboli"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "DRESS/DIHS"
      }
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
        "span": "sulfamethoxazole/trimethoprim"
      },
      "relation": "caused",
      "effect": {
        "span": "generalized erythema"
      }
    },
    {
      "cause": {
        "span": "sulfamethoxazole/trimethoprim"
      },
      "relation": "caused",
      "effect": {
        "span": "high fever"
      }
    }
  ]
}
```

### --- id=3574 ---

输入文本: Cryptococcus neoformans fatal sepsis in a chronic lymphocytic leukemia patient treated with alemtuzumab: case report and review of the literature.

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
      "cause": "alemtuzumab",
      "effect": "Cryptococcus neoformans fatal sepsis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "alemtuzumab"
      },
      "relation": "caused",
      "effect": {
        "span": "fatal sepsis"
      }
    }
  ]
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

### --- id=3749 ---

输入文本: Unexpectedly high toxicity of MACOP-B in young patients with low grade lymphoma.

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
        "span": "MACOP-B"
      },
      "relation": "caused",
      "effect": {
        "span": "toxicity"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "contact dermatitis"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Coagulation activation"
      }
    },
    {
      "cause": {
        "span": "black cohosh"
      },
      "relation": "caused",
      "effect": {
        "span": "fluid retention"
      }
    }
  ]
}
```

### --- id=3875 ---

输入文本: We report the case of an 87-year-old white woman with myasthenia gravis who presented with nausea, shortness of breath, azotemia, and hyperkalemia shortly after completing a course of intravenous immunoglobulin (IVIG).

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 8
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 8
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
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
  "pred_triples": []
}
```

### --- id=3933 ---

输入文本: A possible association between arterial dissection and ergotamine abuse is discussed.

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
        "span": "ergotamine"
      },
      "relation": "caused",
      "effect": {
        "span": "arterial dissection"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "Vincristine overdose"
      }
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

### --- id=3992 ---

输入文本: The association with etanercept therapy and granulomatous reactions is discussed along with the differential diagnosis.

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
        "span": "etanercept"
      },
      "relation": "caused",
      "effect": {
        "span": "granulomatous reactions"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "fixed drug eruption"
      }
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
