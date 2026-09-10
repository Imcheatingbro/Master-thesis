# ade first 1000 eval report

## 配置
```json
{
  "label": "ade first 1000",
  "model": "google/gemma-4-31b-qat",
  "dataset": "ade",
  "sample_count": 1000,
  "prompt_name": "v9.1",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 5,
  "temperature": 0.0,
  "max_tokens": 16384,
  "progress_every": 500,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 16384,
  "reasoning_effort": "none",
  "llm_extra_body": {},
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
  Gold 含因果: 145 | Pred 含因果: 213
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.924
  Precision: 0.662
  Recall   : 0.972
  F1       : 0.788
  (TP=141, TN=783, FP=72, FN=4)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 1000
    Gold triples: 205 | Pred triples: 287
    Precision: 0.460
    Recall   : 0.644
    F1       : 0.537
    (TP=132, FP=155, FN=73)
  [anchor_window] (primary)
    样本数: 1000
    Gold triples: 205 | Pred triples: 287
    Precision: 0.627
    Recall   : 0.878
    F1       : 0.732
    (TP=180, FP=107, FN=25)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 141
    Gold triples: 199 | Pred triples: 195
    Precision: 0.677
    Recall   : 0.663
    F1       : 0.670
    (TP=132, FP=63, FN=67)
  [anchor_window] (primary)
    样本数: 141
    Gold triples: 199 | Pred triples: 195
    Precision: 0.923
    Recall   : 0.905
    F1       : 0.914
    (TP=180, FP=15, FN=19)
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

Sample details shown: all 98 wrong samples from 1000 total samples.

### --- id=9 ---

输入文本: We present a fatal case of subacute methanol toxicity with associated diffuse brain involvement, including bilateral putaminal necrosis and cerebral edema with ventricular compression.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 3,
    "fp": 1,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 3,
    "fp": 1,
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
        "span": "fatal"
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
    }
  ]
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

### --- id=28 ---

输入文本: CONCLUSIONS: These findings suggest that, in patients who are susceptible, the periocular or systemic absorption of inhaled corticosteroids may be sufficient to produce CSC in humans, supporting previous hypotheses regarding the pathogenesis of the disorder.

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
        "span": "inhaled corticosteroids"
      },
      "relation": "caused",
      "effect": {
        "span": "CSC"
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
        "span": "procainamide"
      },
      "relation": "caused",
      "effect": {
        "span": "renal disease"
      }
    }
  ]
}
```

### --- id=51 ---

输入文本: Vitamin D toxicity complicating the treatment of senile, postmenopausal, and glucocorticoid-induced osteoporosis.

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
        "span": "Vitamin D"
      },
      "relation": "caused",
      "effect": {
        "span": "Vitamin D toxicity"
      }
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
      "relation": "caused",
      "effect": {
        "span": "symptomatic cardiomyopathy"
      }
    },
    {
      "cause": {
        "span": "all-trans retinoic acid (ATRA)"
      },
      "relation": "caused",
      "effect": {
        "span": "symptomatic cardiomyopathy"
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

### --- id=75 ---

输入文本: Upon withdrawal of ibopamine but continuation of all other drugs, the patient recovered from the blood dyscrasia within 5 days and showed resolution of symptoms.

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
        "span": "ibopamine"
      },
      "relation": "caused",
      "effect": {
        "span": "blood dyscrasia"
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
        "span": "stricture of the hepatic flexure region"
      }
    },
    {
      "cause": {
        "span": "high-lipase pancreatin therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "narrowing due to submucosal fibrosis of the transverse colon"
      }
    }
  ]
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
        "span": "extrapyramidal symptoms (EPS)"
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
        "span": "Fatal spontaneous spinal epidural hematoma"
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

### --- id=183 ---

输入文本: Correction after vitamin K administration suggested an organophosphate-related effect on vitamin K-dependent factor VII activity.

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
        "span": "organophosphate"
      },
      "relation": "caused",
      "effect": {
        "span": "effect on vitamin K-dependent factor VII activity"
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

### --- id=208 ---

输入文本: We describe an 11-year-old girl who presented with widespread erythematous and pustular lesions being treated with topical corticosteroid.

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
        "span": "topical corticosteroid"
      },
      "relation": "caused",
      "effect": {
        "span": "widespread erythematous and pustular lesions"
      }
    }
  ]
}
```

### --- id=222 ---

输入文本: Case report: persistent cytomegalovirus (CMV) infection after haploidentical hematopoietic stem cell transplantation using in vivo alemtuzumab: emergence of resistant CMV due to mutations in the UL97 and UL54 genes.

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
        "span": "alemtuzumab"
      },
      "relation": "caused",
      "effect": {
        "span": "persistent cytomegalovirus (CMV) infection"
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
      "cause": "GSTM",
      "effect": "mild nitritoid symptoms"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "GSTM"
      },
      "relation": "caused",
      "effect": {
        "span": "mild nitritoid symptoms"
      }
    },
    {
      "cause": {
        "span": "GSTM"
      },
      "relation": "caused",
      "effect": {
        "span": "cerebrovascular accident"
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
      "relation": "caused",
      "effect": {
        "span": "adrenal crises"
      }
    },
    {
      "cause": {
        "span": "high-dose inhaled corticosteroids"
      },
      "relation": "caused",
      "effect": {
        "span": "vomiting"
      }
    },
    {
      "cause": {
        "span": "high-dose inhaled corticosteroids"
      },
      "relation": "caused",
      "effect": {
        "span": "hypoglycaemia"
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

### --- id=278 ---

输入文本: One of the patients had had earlier exposure to typical antipsychotic drugs, but no other predisposing factors for TD were noted.

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
        "span": "typical antipsychotic drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "TD"
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
        "span": "thrombotic microangiopathy"
      }
    }
  ]
}
```

### --- id=289 ---

输入文本: Bilateral inguinal scrofuloderma during steroid therapy in a patient with bullous pemphigoid.

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
        "span": "steroid"
      },
      "relation": "caused",
      "effect": {
        "span": "Bilateral inguinal scrofuloderma"
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

### --- id=295 ---

输入文本: Reversal of pathologic cardiac parameters after transition from clozapine to olanzapine treatment: a case report.

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
        "span": "clozapine"
      },
      "relation": "caused",
      "effect": {
        "span": "pathologic cardiac parameters"
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
        "span": "glucocorticoid"
      },
      "relation": "caused",
      "effect": {
        "span": "pseudotumor cerebri"
      }
    }
  ]
}
```

### --- id=349 ---

输入文本: Reversal of CNS-prophylaxis-related leukoencephalopathy after CSF shunting: case histories of identical twins.

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
        "span": "CNS-prophylaxis"
      },
      "relation": "caused",
      "effect": {
        "span": "leukoencephalopathy"
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

### --- id=356 ---

输入文本: Reviewing the literature, another eight cases of acute leukemia after cytotoxic treatment for nonmalignant disease in childhood have been reported.

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
        "span": "cytotoxic treatment"
      },
      "relation": "caused",
      "effect": {
        "span": "acute leukemia"
      }
    }
  ]
}
```

### --- id=357 ---

输入文本: Two hours after a documented overdosage of more than 100 tablets oxcarbazepine, the serum level of the parent compound was 10-fold higher than the therapeutic dosage (31.6 mg l(-1)).

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
        "span": "oxcarbazepine"
      },
      "relation": "caused",
      "effect": {
        "span": "overdosage"
      }
    }
  ]
}
```

### --- id=360 ---

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

### --- id=567 ---

输入文本: A 26-year-old HIV-seropositive Caucasian man with cryptococcal meningitis developed permanent bilateral blindness shortly after starting highly active antiretroviral treatment.

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
        "span": "highly active antiretroviral treatment"
      },
      "relation": "caused",
      "effect": {
        "span": "permanent bilateral blindness"
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
        "span": "methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "right-sided paralysis"
      }
    },
    {
      "cause": {
        "span": "methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "aphasia"
      }
    }
  ]
}
```

### --- id=596 ---

输入文本: Chronic inflammatory demyelinating polyneuropathy associated with tumor necrosis factor-alpha antagonists.

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
        "span": "tumor necrosis factor-alpha antagonists"
      },
      "relation": "caused",
      "effect": {
        "span": "Chronic inflammatory demyelinating polyneuropathy"
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

### --- id=612 ---

输入文本: There are several factors which might promote a peripheral ischemic response to vasopressin in the bleeding cirrhotic patient, including altered resting hemodynamics, increased resting sympathetic tone, impaired vasodilation as a compensatory response to vasopressin, and reduced hepatic drug clearance.

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
        "span": "vasopressin"
      },
      "relation": "caused",
      "effect": {
        "span": "peripheral ischemic response"
      }
    }
  ]
}
```

### --- id=635 ---

输入文本: Herpes simplex epithelial keratitis developed in four renal transplant recipients while they were receiving high-dose systemic corticosteroid and immunosuppressive therapy.

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
        "span": "high-dose systemic corticosteroid"
      },
      "relation": "caused",
      "effect": {
        "span": "Herpes simplex epithelial keratitis"
      }
    }
  ]
}
```

### --- id=638 ---

输入文本: Treatment of a patient with severe digitoxin intoxication by Fab fragments of anti-digitalis antibodies.

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
        "span": "digitoxin"
      },
      "relation": "caused",
      "effect": {
        "span": "severe digitoxin intoxication"
      }
    }
  ]
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
        "span": "lipopolysaccharide [LPS]"
      },
      "relation": "caused",
      "effect": {
        "span": "tracheal inflammation"
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

### --- id=697 ---

输入文本: In both instances, reversion of intraventricular conduction to normal occurred within 72 hours, coinciding with clearance of carbamazepine from the blood stream.

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
        "span": "carbamazepine"
      },
      "relation": "caused",
      "effect": {
        "span": "intraventricular conduction"
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

### --- id=732 ---

输入文本: Progressive interstitial fibrosis with roentgenographic honeycombing developed in the case of a psoriatic patient who had been on a regimen of methotrexate for 18 years.

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
      "cause": "methotrexate",
      "effect": "Progressive interstitial fibrosis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "Progressive interstitial fibrosis"
      }
    },
    {
      "cause": {
        "span": "methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "roentgenographic honeycombing"
      }
    }
  ]
}
```

### --- id=737 ---

输入文本: Despite their effectiveness, anti-TNF drugs have some drawbacks such as severe adverse effects including infections and possibly lymphoproliferative disorders.

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
        "span": "anti-TNF drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "infections"
      }
    },
    {
      "cause": {
        "span": "anti-TNF drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "lymphoproliferative disorders"
      }
    }
  ]
}
```

### --- id=788 ---

输入文本: Methanol poisoning continues to be a public health problem in Tunisia in spite of the different legislative measures.

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
        "span": "Methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "Methanol poisoning"
      }
    }
  ]
}
```

### --- id=827 ---

输入文本: Sulfasalazine has been associated with bronchopulmonary complications of inflammatory bowel disease (IBD) in adults.

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
      "cause": "Sulfasalazine",
      "effect": "bronchopulmonary complications of inflammatory bowel disease"
    },
    {
      "cause": "Sulfasalazine",
      "effect": "IBD"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Sulfasalazine"
      },
      "relation": "caused",
      "effect": {
        "span": "bronchopulmonary complications"
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
      "relation": "caused",
      "effect": {
        "span": "rhabdomyolysis"
      }
    },
    {
      "cause": {
        "span": "macrolide antibiotic"
      },
      "relation": "caused",
      "effect": {
        "span": "rhabdomyolysis"
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

### --- id=855 ---

输入文本: Steroid rosacea in children.

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
        "span": "Steroid"
      },
      "relation": "caused",
      "effect": {
        "span": "rosacea"
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
        "span": "diethylstilbestrol (DES)"
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

### --- id=942 ---

输入文本: Cerebrospinal fluid examination prior to the last dosage of cytosine arabinoside revealed a mononuclear pleocytosis and increased protein.

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
        "span": "cytosine arabinoside"
      },
      "relation": "caused",
      "effect": {
        "span": "mononuclear pleocytosis"
      }
    },
    {
      "cause": {
        "span": "cytosine arabinoside"
      },
      "relation": "caused",
      "effect": {
        "span": "increased protein"
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
        "span": "tricyclic antidepressant"
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
    "fp": 5,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 5,
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
    },
    {
      "cause": {
        "span": "isoniazid"
      },
      "relation": "caused",
      "effect": {
        "span": "mental"
      }
    },
    {
      "cause": {
        "span": "isoniazid"
      },
      "relation": "caused",
      "effect": {
        "span": "neurological"
      }
    },
    {
      "cause": {
        "span": "isoniazid"
      },
      "relation": "caused",
      "effect": {
        "span": "gastrointestinal symptoms"
      }
    },
    {
      "cause": {
        "span": "isoniazid"
      },
      "relation": "caused",
      "effect": {
        "span": "pellagra dermatitis"
      }
    }
  ]
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
        "span": "cough"
      }
    }
  ]
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
