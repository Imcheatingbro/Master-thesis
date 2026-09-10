# ade first 1000 eval report

## 配置
```json
{
  "label": "ade first 1000",
  "model": "google/gemma-4-31b-qat",
  "dataset": "ade",
  "sample_count": 1000,
  "prompt_name": "v9.2",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 5,
  "temperature": 0.0,
  "max_tokens": 8192,
  "output_schema": "standard",
  "primary_metric": null,
  "progress_every": 500,
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
================ ade first 1000 final report ================
样本总数: 1000
  Gold 含因果: 145 | Pred 含因果: 159
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.936
  Precision: 0.755
  Recall   : 0.828
  F1       : 0.789
  (TP=120, TN=816, FP=39, FN=25)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 1000
    Gold triples: 205 | Pred triples: 219
    Precision: 0.475
    Recall   : 0.507
    F1       : 0.491
    (TP=104, FP=115, FN=101)
  [anchor_window] (primary)
    样本数: 1000
    Gold triples: 205 | Pred triples: 219
    Precision: 0.726
    Recall   : 0.776
    F1       : 0.750
    (TP=159, FP=60, FN=46)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 120
    Gold triples: 172 | Pred triples: 164
    Precision: 0.634
    Recall   : 0.605
    F1       : 0.619
    (TP=104, FP=60, FN=68)
  [anchor_window] (primary)
    样本数: 120
    Gold triples: 172 | Pred triples: 164
    Precision: 0.970
    Recall   : 0.924
    F1       : 0.946
    (TP=159, FP=5, FN=13)
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

Sample details shown: all 79 wrong samples from 1000 total samples.

### --- id=9 ---

输入文本: We present a fatal case of subacute methanol toxicity with associated diffuse brain involvement, including bilateral putaminal necrosis and cerebral edema with ventricular compression.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 3,
    "fp": 2,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 5,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 3,
    "fp": 2,
    "fn": 3
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
      "relation": "caused",
      "effect": {
        "span": "subacute methanol toxicity"
      }
    },
    {
      "cause": {
        "span": "methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "diffuse brain involvement"
      }
    },
    {
      "cause": {
        "span": "methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "bilateral putaminal necrosis"
      }
    },
    {
      "cause": {
        "span": "methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "cerebral edema with ventricular compression"
      }
    },
    {
      "cause": {
        "span": "methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "fatal case"
      }
    }
  ]
}
```

### --- id=17 ---

输入文本: Attempts were made to stop and then restart the theophylline therapy at progressively lower doses; however, with each attempt, the patient's reaction to the drug became more toxic, with serum theophylline levels ranging between 99.9 and 149.9 micromol/L (18 and 27 microg/mL).

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
      "cause": "theophylline",
      "effect": "reaction to the drug became more toxic"
    }
  ],
  "pred_triples": []
}
```

### --- id=18 ---

输入文本: Foreign body granuloma of activated charcoal.

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
        "span": "activated charcoal"
      },
      "relation": "caused",
      "effect": {
        "span": "Foreign body granuloma"
      }
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
      "relation": "caused",
      "effect": {
        "span": "renal disease"
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

### --- id=116 ---

输入文本: We report a 5-year-old boy with CF who had a stricture of the hepatic flexure region with associated narrowing due to submucosal fibrosis of the transverse colon, secondary to high-lipase pancreatin therapy.

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
      "relation": "caused",
      "effect": {
        "span": "submucosal fibrosis of the transverse colon"
      }
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
      "relation": "caused",
      "effect": {
        "span": "confusion"
      }
    },
    {
      "cause": {
        "span": "ifosfamide"
      },
      "relation": "caused",
      "effect": {
        "span": "lethargy"
      }
    },
    {
      "cause": {
        "span": "ifosfamide"
      },
      "relation": "caused",
      "effect": {
        "span": "speech deterioration"
      }
    }
  ]
}
```

### --- id=157 ---

输入文本: The case emphasises that immune reconstitution can be an extremely aggressive complication of HAART.

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
        "span": "HAART"
      },
      "relation": "caused",
      "effect": {
        "span": "immune reconstitution"
      }
    }
  ]
}
```

### --- id=163 ---

输入文本: The acronym 'EMPACT' is suggested (E: erythema; M: multiforme; associated with P: phenytoin; A: and; C: cranial, radiation; T: therapy) to best describe this disorder.

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
        "span": "phenytoin"
      },
      "relation": "caused",
      "effect": {
        "span": "erythema multiforme"
      }
    }
  ]
}
```

### --- id=170 ---

输入文本: The patient's platelet count dropped rapidly to a level of 1000/mm3 after receiving a single 600 mg dose of rifampin.

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
        "span": "rifampin"
      },
      "relation": "caused",
      "effect": {
        "span": "platelet count dropped rapidly"
      }
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
      "relation": "caused",
      "effect": {
        "span": "adverse reaction"
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

### --- id=235 ---

输入文本: The second patient experienced mild nitritoid symptoms following several GSTM injections prior experiencing a cerebrovascular accident within several hours of her next injection.

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
      "cause": "GSTM",
      "effect": "mild nitritoid symptoms"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "GSTM injections"
      },
      "relation": "caused",
      "effect": {
        "span": "mild nitritoid symptoms"
      }
    },
    {
      "cause": {
        "span": "GSTM injections"
      },
      "relation": "caused",
      "effect": {
        "span": "cerebrovascular accident"
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
      "relation": "caused",
      "effect": {
        "span": "increase in requirement for thyroxine"
      }
    }
  ]
}
```

### --- id=280 ---

输入文本: Seizures in patients receiving concomitant antimuscarinics and acetylcholinesterase inhibitor.

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
        "span": "antimuscarinics"
      },
      "relation": "caused",
      "effect": {
        "span": "Seizures"
      }
    },
    {
      "cause": {
        "span": "acetylcholinesterase inhibitor"
      },
      "relation": "caused",
      "effect": {
        "span": "Seizures"
      }
    }
  ]
}
```

### --- id=285 ---

输入文本: OBJECTIVE: To report a patient with a large gastrointestinal stromal tumor (GIST) who received multiple blood transfusions intraoperatively and developed a transfusion-related acute lung injury (TRALI).

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
        "span": "blood transfusions"
      },
      "relation": "caused",
      "effect": {
        "span": "transfusion-related acute lung injury (TRALI)"
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
        "span": "thrombotic microangiopathy (TMA)"
      }
    }
  ]
}
```

### --- id=287 ---

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

### --- id=352 ---

输入文本: Treatment of antithyroid drug-induced agranulocytosis by granulocyte colony-stimulating factor: a case of primum non nocere.

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
        "span": "antithyroid drug"
      },
      "relation": "caused",
      "effect": {
        "span": "agranulocytosis"
      }
    }
  ]
}
```

### --- id=355 ---

输入文本: Toxic optic neuropathy associated with ethambutol: implications for current therapy.

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
      "cause": "ethambutol",
      "effect": "Toxic optic neuropathy"
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
      "cause": "infliximab",
      "effect": "AVP"
    },
    {
      "cause": "infliximab",
      "effect": "Severe adenovirus pneumonia"
    }
  ],
  "pred_triples": []
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
        "span": "estrogen treatment"
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
  "pred_triples": []
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
        "span": "Transdermal scopolamine delivery system (TRANSDERM-V)"
      },
      "relation": "caused",
      "effect": {
        "span": "acute angle-closure glaucoma"
      }
    }
  ]
}
```

### --- id=469 ---

输入文本: We review the existing literature on this rare clinical entity, all-trans retinoic acid-induced myositis.

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
        "span": "all-trans retinoic acid"
      },
      "relation": "caused",
      "effect": {
        "span": "myositis"
      }
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
        "span": "phenobarbital"
      },
      "relation": "caused",
      "effect": {
        "span": "AHS"
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
        "span": "acute myelomonoblastic leukemia (M4)"
      }
    }
  ]
}
```

### --- id=513 ---

输入文本: Renal toxicities have been reported in less than one percent of the patients receiving ciprofloxacin therapy.

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
      "cause": "ciprofloxacin",
      "effect": "Renal toxicities"
    }
  ],
  "pred_triples": []
}
```

### --- id=521 ---

输入文本: Anaphylaxis to cisplatin is an infrequent life-threatening complication which may occur even in patients who have received prior treatment with cisplatin.

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
      "effect": "Anaphylaxis"
    }
  ],
  "pred_triples": []
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
        "span": "cocaine"
      },
      "relation": "caused",
      "effect": {
        "span": "drug-mediated hypertension"
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

### --- id=579 ---

输入文本: Patient 2 presented an acute left hemiballismus when consciousness was restored with naloxone.

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
        "span": "naloxone"
      },
      "relation": "caused",
      "effect": {
        "span": "acute left hemiballismus"
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
      "relation": "caused",
      "effect": {
        "span": "sub-acute leukoencephalopathy"
      }
    },
    {
      "cause": {
        "span": "methotrexate therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "right-sided paralysis"
      }
    },
    {
      "cause": {
        "span": "methotrexate therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "aphasia"
      }
    }
  ]
}
```

### --- id=601 ---

输入文本: The use of protease Inhibitors (PI) has been associated with many adverse effects including increased tendency to bleed, which is particularly problematic in individuals with congenital coagulation disorders.

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
        "span": "protease Inhibitors"
      },
      "relation": "caused",
      "effect": {
        "span": "increased tendency to bleed"
      }
    },
    {
      "cause": {
        "span": "PI"
      },
      "relation": "caused",
      "effect": {
        "span": "increased tendency to bleed"
      }
    }
  ]
}
```

### --- id=632 ---

输入文本: Sodium valproate and carbamazepine, antiepileptic drugs that are associated with a relatively low rate of adverse cutaneous reactions, should be added to the growing list of drugs that produce psoriasiform eruptions.

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
      "cause": "carbamazepine",
      "effect": "psoriasiform eruptions"
    },
    {
      "cause": "Sodium valproate",
      "effect": "psoriasiform eruptions"
    }
  ],
  "pred_triples": []
}
```

### --- id=639 ---

输入文本: We evaluated both healthy ferrets and animals in which we first induced tracheal inflammation with bacterial endotoxin (a lipopolysaccharide [LPS]).

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
        "span": "bacterial endotoxin"
      },
      "relation": "caused",
      "effect": {
        "span": "tracheal inflammation"
      }
    },
    {
      "cause": {
        "span": "lipopolysaccharide"
      },
      "relation": "caused",
      "effect": {
        "span": "tracheal inflammation"
      }
    },
    {
      "cause": {
        "span": "LPS"
      },
      "relation": "caused",
      "effect": {
        "span": "tracheal inflammation"
      }
    }
  ]
}
```

### --- id=655 ---

输入文本: Two children, 1 with idiopathic nephrotic syndrome and 1 with endo-extracapillary glomerulonephritis, presented an episode of seizures and transient blindness at different times after i.v. pulse methylprednisolone (IVPMP) treatment.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "methylprednisolone",
      "effect": "seizures"
    },
    {
      "cause": "methylprednisolone",
      "effect": "transient blindness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "i.v. pulse methylprednisolone"
      },
      "relation": "caused",
      "effect": {
        "span": "seizures"
      }
    },
    {
      "cause": {
        "span": "i.v. pulse methylprednisolone"
      },
      "relation": "caused",
      "effect": {
        "span": "transient blindness"
      }
    },
    {
      "cause": {
        "span": "IVPMP"
      },
      "relation": "caused",
      "effect": {
        "span": "seizures"
      }
    },
    {
      "cause": {
        "span": "IVPMP"
      },
      "relation": "caused",
      "effect": {
        "span": "transient blindness"
      }
    }
  ]
}
```

### --- id=675 ---

输入文本: To date, only three cases of seizures associated with amphotericin B have been reported in the literature, but healthcare providers should be aware of the potential for this rare adverse effect.

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
      "effect": "seizures"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "symptoms"
      }
    }
  ]
}
```

### --- id=700 ---

输入文本: Drug eruption was diagnosed in a 4-year-old German Shepherd Dog being treated with sulfonamides for vertebral osteomyelitis due to infection with Nocardia spp.

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
        "span": "sulfonamides"
      },
      "relation": "caused",
      "effect": {
        "span": "Drug eruption"
      }
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
      "relation": "caused",
      "effect": {
        "span": "rhabdomyolysis"
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

### --- id=789 ---

输入文本: Lithium is known to cause acute renal failure and tubulo-interstitial disease, but the recently described association with proteinuria or nephrotic syndrome is little recognized.

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
      "cause": "Lithium",
      "effect": "acute renal failure"
    },
    {
      "cause": "Lithium",
      "effect": "nephrotic syndrome"
    },
    {
      "cause": "Lithium",
      "effect": "proteinuria"
    },
    {
      "cause": "Lithium",
      "effect": "tubulo-interstitial disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Lithium"
      },
      "relation": "caused",
      "effect": {
        "span": "acute renal failure"
      }
    },
    {
      "cause": {
        "span": "Lithium"
      },
      "relation": "caused",
      "effect": {
        "span": "tubulo-interstitial disease"
      }
    }
  ]
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

### --- id=832 ---

输入文本: Incomplete posterior hyaloid detachment after intravitreal pegaptanib injection in diabetic macular edema.

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
      "cause": "pegaptanib",
      "effect": "Incomplete posterior hyaloid detachment"
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

### --- id=847 ---

输入文本: Persistent triamcinolone acetonide particles on the posterior lens capsule after intravitreal injection.

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
        "span": "triamcinolone acetonide"
      },
      "relation": "caused",
      "effect": {
        "span": "Persistent triamcinolone acetonide particles on the posterior lens capsule"
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

### --- id=857 ---

输入文本: Septic knee arthritis after intra-articular hyaluronate injection.

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
      "cause": "hyaluronate",
      "effect": "Septic knee arthritis"
    }
  ],
  "pred_triples": []
}
```

### --- id=859 ---

输入文本: We report the use of pamidronate for acute, severe hypercalcemia secondary to iatrogenic vitamin D poisoning.

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
      "cause": "vitamin D",
      "effect": "severe hypercalcemia"
    },
    {
      "cause": "vitamin D",
      "effect": "vitamin D poisoning"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "vitamin D"
      },
      "relation": "caused",
      "effect": {
        "span": "acute, severe hypercalcemia"
      }
    }
  ]
}
```

### --- id=883 ---

输入文本: Atrioventricular block complicating amiodarone-induced hypothyroidism in a patient with pre-excitation and rate-dependent bilateral bundle branch block.

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
      "cause": "amiodarone",
      "effect": "Atrioventricular block"
    },
    {
      "cause": "amiodarone",
      "effect": "hypothyroidism"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "amiodarone"
      },
      "relation": "caused",
      "effect": {
        "span": "hypothyroidism"
      }
    }
  ]
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

### --- id=912 ---

输入文本: Use of perospirone for obesity and diabetes mellitus in patients with schizophrenia: three case reports.

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
        "span": "perospirone"
      },
      "relation": "caused",
      "effect": {
        "span": "obesity"
      }
    },
    {
      "cause": {
        "span": "perospirone"
      },
      "relation": "caused",
      "effect": {
        "span": "diabetes mellitus"
      }
    }
  ]
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
        "span": "diethylstilbestrol (DES) therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "hepatocellular carcinoma"
      }
    }
  ]
}
```

### --- id=933 ---

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

### --- id=952 ---

输入文本: Pellagra should be suspected whenever tuberculous patients under treatment with isoniazid develop mental, neurological or gastrointestinal symptoms, even in the absence of typical pellagra dermatitis.

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
      "cause": "isoniazid",
      "effect": "mental, neurological or gastrointestinal symptoms"
    }
  ],
  "pred_triples": []
}
```

### --- id=953 ---

输入文本: Frequency of cough is variable and although this complication has been described as a class effect, patients with a persistent, severe ACE inhibitor-induced cough may benefit from a trial of fosinopril therapy.

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
        "span": "ACE inhibitor"
      },
      "relation": "caused",
      "effect": {
        "span": "persistent, severe ACE inhibitor-induced cough"
      }
    }
  ]
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

### --- id=964 ---

输入文本: Intravenous haloperidol is generally well tolerated, but multiform ventricular tachycardia has been reported.

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
      "effect": "multiform ventricular tachycardia"
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
