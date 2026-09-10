# Gemma 4 31B QAT Li original generic RAG k1 rerun eval report

## 配置
```json
{
  "label": "Gemma 4 31B QAT Li original generic RAG k1 rerun",
  "model": "google/gemma-4-31b-qat",
  "dataset": "li",
  "sample_count": 786,
  "prompt_name": "v10.2",
  "use_rag": true,
  "rag_mode": "knn_pattern",
  "rag_top_k": 1,
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
================ Gemma 4 31B QAT Li original generic RAG k1 rerun final report ================
样本总数: 786
  Gold 含因果: 191 | Pred 含因果: 197
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.985
  Precision: 0.954
  Recall   : 0.984
  F1       : 0.969
  (TP=188, TN=586, FP=9, FN=3)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 786
    Gold triples: 296 | Pred triples: 304
    Precision: 0.632
    Recall   : 0.649
    F1       : 0.640
    (TP=192, FP=112, FN=104)
  [anchor_window] (primary)
    样本数: 786
    Gold triples: 296 | Pred triples: 304
    Precision: 0.852
    Recall   : 0.875
    F1       : 0.863
    (TP=259, FP=45, FN=37)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 188
    Gold triples: 292 | Pred triples: 295
    Precision: 0.651
    Recall   : 0.658
    F1       : 0.654
    (TP=192, FP=103, FN=100)
  [anchor_window] (primary)
    样本数: 188
    Gold triples: 292 | Pred triples: 295
    Precision: 0.878
    Recall   : 0.887
    F1       : 0.882
    (TP=259, FP=36, FN=33)
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

Sample details shown: all 47 wrong samples from 786 total samples.

### --- id=33 ---

输入文本: A blood clot is a normal reaction of the body that occurs if a blood vessel is injured.

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
        "span": "a blood vessel is injured"
      },
      "effect": {
        "span": "A blood clot"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=40 ---

输入文本: Cervical cancer is caused by infection with the human papillomavirus  and is one of the most common cancers in women in developing countries.

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
      "cause": "infection",
      "effect": "Cervical cancer"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the human papillomavirus"
      },
      "effect": {
        "span": "Cervical cancer"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=43 ---

输入文本: The debris caused a crash on the Schuylkill, and it has been closed for hours because of the mishap.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "The debris",
      "effect": "a crash"
    },
    {
      "cause": "the mishap",
      "effect": "closed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "debris"
      },
      "effect": {
        "span": "a crash"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "the mishap"
      },
      "effect": {
        "span": "it has been closed for hours"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=64 ---

输入文本: The elderly found it hard to cope with the high heat-humidity, which often causes nausea and dizziness from exhaustion and dehydration.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 4,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 4,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 4,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "exhaustion",
      "effect": "nausea"
    },
    {
      "cause": "exhaustion",
      "effect": "dizziness"
    },
    {
      "cause": "dehydration",
      "effect": "nausea"
    },
    {
      "cause": "dehydration",
      "effect": "dizziness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "exhaustion"
      },
      "effect": {
        "span": "nausea"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "exhaustion"
      },
      "effect": {
        "span": "dizziness"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dehydration"
      },
      "effect": {
        "span": "nausea"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "dehydration"
      },
      "effect": {
        "span": "dizziness"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "the high heat-humidity"
      },
      "effect": {
        "span": "nausea"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "the high heat-humidity"
      },
      "effect": {
        "span": "dizziness"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=66 ---

输入文本: Over 90% of the cases of ringworm of the scalp are caused by Trichophyton tonsurans, a fungus that infects the hairs and causes them to break.

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
      "cause": "Trichophyton tonsurans",
      "effect": "ringworm"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Trichophyton tonsurans"
      },
      "effect": {
        "span": "ringworm of the scalp"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "a fungus"
      },
      "effect": {
        "span": "them to break"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=70 ---

输入文本: With the pollution caused by the buring of coal, the light-colored tree trunks became darker due to soot.

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
      "cause": "the buring",
      "effect": "the pollution"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the buring of coal"
      },
      "effect": {
        "span": "the pollution"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "soot"
      },
      "effect": {
        "span": "the light-colored tree trunks became darker"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=72 ---

输入文本: If a participant complaint is the source of an investigative lead, interim contact with the participant should be made by the investigator.

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
      "cause": "a participant complaint",
      "effect": "an investigative lead"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "complaint"
      },
      "effect": {
        "span": "lead"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=74 ---

输入文本: The transmitter generates the electromagnetic wave, some of which will be incident on the receiver.

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
      "cause": "The transmitter",
      "effect": "the electromagnetic wave"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "transmitter"
      },
      "effect": {
        "span": "the electromagnetic wave"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=88 ---

输入文本: An alert victim with a broken neck or severely torn ligament has enough discomfort from the injury and muscle spasm to force him to hold his neck still.

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
      "cause": "the injury",
      "effect": "enough discomfort"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the injury"
      },
      "effect": {
        "span": "discomfort"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "muscle spasm"
      },
      "effect": {
        "span": "discomfort"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=105 ---

输入文本: No material was prepared for the sessions, so the three musicians improvised an album's worth of material.

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
        "span": "No material was prepared for the sessions"
      },
      "effect": {
        "span": "the three musicians improvised an album's worth of material"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=114 ---

输入文本: Overall, the fire after the earthquake burned out 7456 houses in over 530 localities.

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
      "cause": "the earthquake",
      "effect": "the fire"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "earthquake"
      },
      "effect": {
        "span": "the fire"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=124 ---

输入文本: Most deaths from the accident were caused by radiation poisoning.

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
      "cause": "the accident",
      "effect": "Most deaths"
    },
    {
      "cause": "radiation poisoning",
      "effect": "Most deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "radiation poisoning"
      },
      "effect": {
        "span": "Most deaths from the accident"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=126 ---

输入文本: And one third of the bench of aldermen is exclusively composed of men, which explains the on average lower share of female aldermen than female local councillors.

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
        "span": "one third of the bench of aldermen is exclusively composed of men"
      },
      "effect": {
        "span": "the on average lower share of female aldermen than female local councillors"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=131 ---

输入文本: The drugs he sold had caused the overdose death of Matthew Lessard, 19, of Lowell.

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
      "cause": "The drugs",
      "effect": "the overdose death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "drugs"
      },
      "effect": {
        "span": "overdose death"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=133 ---

输入文本: Three years ago the coalition organized a strategic cooperative of several farmers associations to export mangos under the Taiwan Mango brand.

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
        "span": "the coalition"
      },
      "effect": {
        "span": "a strategic cooperative of several farmers associations"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=138 ---

输入文本: Each year, many infants and toddlers die due to suffocation from breathing small objects into their breathing passages and lungs.

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
      "cause": "suffocation",
      "effect": "die"
    },
    {
      "cause": "breathing small objects",
      "effect": "suffocation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "breathing small objects into their breathing passages and lungs"
      },
      "effect": {
        "span": "suffocation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=139 ---

输入文本: Gross revenues from the selling of crude oil in 2003 reached US$11.508 billion or some 112.85 percent of the amount targeted in the 2003 state budget.

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
      "cause": "the selling",
      "effect": "Gross revenues"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "selling"
      },
      "effect": {
        "span": "Gross revenues"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=141 ---

输入文本: Pneumococcal meningitis is caused by pneumococcus bacteria, which also cause several diseases of the respiratory system, including pneumonia.

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
    "tp": 2,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "pneumococcus bacteria",
      "effect": "Pneumococcal meningitis"
    },
    {
      "cause": "pneumococcus bacteria",
      "effect": "several diseases"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "pneumococcus bacteria"
      },
      "effect": {
        "span": "Pneumococcal meningitis"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "pneumococcus bacteria"
      },
      "effect": {
        "span": "several diseases of the respiratory system"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "pneumococcus bacteria"
      },
      "effect": {
        "span": "pneumonia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=188 ---

输入文本: When the force was generated via the joystick, the reproduced force matched the original force much more accurately.

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
      "cause": "the joystick",
      "effect": "the force"
    }
  ],
  "pred_triples": []
}
```

### --- id=189 ---

输入文本: There were setbacks and technical problems that ensued from the location design, flooding, and moisture that plagued the winery and bumped up the investment cost beyond the initial budgetary estimates.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 6,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 4,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 6,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "the location design",
      "effect": "setbacks"
    },
    {
      "cause": "the location design",
      "effect": "technical problems"
    },
    {
      "cause": "flooding",
      "effect": "setbacks"
    },
    {
      "cause": "flooding",
      "effect": "technical problems"
    },
    {
      "cause": "moisture",
      "effect": "setbacks"
    },
    {
      "cause": "moisture",
      "effect": "technical problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "location design"
      },
      "effect": {
        "span": "setbacks"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "location design"
      },
      "effect": {
        "span": "technical problems"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "flooding"
      },
      "effect": {
        "span": "setbacks"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "flooding"
      },
      "effect": {
        "span": "technical problems"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "moisture"
      },
      "effect": {
        "span": "setbacks"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "moisture"
      },
      "effect": {
        "span": "technical problems"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=225 ---

输入文本: The cow makes a sound called lowing, also known as mooing.

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
      "cause": "The cow",
      "effect": "a sound"
    }
  ],
  "pred_triples": []
}
```

### --- id=240 ---

输入文本: When I start the engine the car makes a screaching sound.

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
      "cause": "the car",
      "effect": "a screaching sound"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "car"
      },
      "effect": {
        "span": "sound"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=245 ---

输入文本: The transmitter emits a constant radio signal to crea.

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
      "cause": "The transmitter",
      "effect": "a constant radio signal"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "transmitter"
      },
      "effect": {
        "span": "constant radio signal"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=260 ---

输入文本: He encourages students to read beyond the mandatory texts in order to prepare for his exam.

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
        "span": "read beyond the mandatory texts"
      },
      "effect": {
        "span": "prepare for his exam"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=267 ---

输入文本: Patients with adenomyosis experience pain from this disease in the early 30's.

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
      "cause": "this disease",
      "effect": "adenomyosis experience pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "this disease"
      },
      "effect": {
        "span": "pain"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=303 ---

输入文本: The malfunctions on Monday caused delays for patrons waiting to check out or renew books at the branches, and impeded access to personal accounts that allow users to renew or hold books online.

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
      "cause": "The malfunctions",
      "effect": "delays"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "malfunctions"
      },
      "effect": {
        "span": "delays"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=344 ---

输入文本: Eighty-four percent of the complications resulted in patient deaths, while 16 percent resulted in a serious injury.

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
      "cause": "the complications",
      "effect": "patient deaths"
    },
    {
      "cause": "the complications",
      "effect": "a serious injury"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Eighty-four percent of the complications"
      },
      "effect": {
        "span": "patient deaths"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "16 percent"
      },
      "effect": {
        "span": "a serious injury"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=354 ---

输入文本: Even nuclear energy is among the causes of water pollution.

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
      "cause": "Even nuclear energy",
      "effect": "water pollution"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "nuclear energy"
      },
      "effect": {
        "span": "water pollution"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=377 ---

输入文本: Compared to running barefoot, running in conventional running shoes increases stress on the knee joints up to 38%.

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
        "span": "running in conventional running shoes"
      },
      "effect": {
        "span": "stress on the knee joints"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=405 ---

输入文本: These chemical studies were directed toward proof of structure of the indole components of the seeds.

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
      "cause": "These chemical studies",
      "effect": "proof"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "studies"
      },
      "effect": {
        "span": "proof"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=439 ---

输入文本: In a person who already has some neck tension from stress, such an event can lead to a long-term increase of neck tension.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "stress",
      "effect": "some neck tension"
    },
    {
      "cause": "such an event",
      "effect": "a long-term increase"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "stress"
      },
      "effect": {
        "span": "neck tension"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "such an event"
      },
      "effect": {
        "span": "a long-term increase of neck tension"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=509 ---

输入文本: In the second section, the authors explore factors that are ostensibly unrelated to race but nonetheless contribute to racial inequality.

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
        "span": "factors that are ostensibly unrelated to race"
      },
      "effect": {
        "span": "racial inequality"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=527 ---

输入文本: Whooping cough is another name for the pertussis, an infection of the airways caused by the bacteria bordetella pertussis.

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
      "cause": "the bacteria bordetella pertussis",
      "effect": "the pertussis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the bacteria bordetella pertussis"
      },
      "effect": {
        "span": "an infection of the airways"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=555 ---

输入文本: Swissair was a victim of the clandestine wealth-transfer plaguing the productive sector as a result of the falling interest-rate structure caused by bond speculation.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "the falling interest-rate structure",
      "effect": "a victim"
    },
    {
      "cause": "bond speculation",
      "effect": "the falling interest-rate structure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "bond speculation"
      },
      "effect": {
        "span": "the falling interest-rate structure"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "the falling interest-rate structure"
      },
      "effect": {
        "span": "the clandestine wealth-transfer plaguing the productive sector"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=568 ---

输入文本: The clock struck twelve with a loud chime that made me jump.

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
      "cause": "The clock",
      "effect": "a loud chime"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "clock"
      },
      "effect": {
        "span": "chime"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "a loud chime"
      },
      "effect": {
        "span": "me jump"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=574 ---

输入文本: The email marketing is landing into the spam folders decreasing the ROI for these programs.

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
        "span": "The email marketing is landing into the spam folders"
      },
      "effect": {
        "span": "decreasing the ROI for these programs"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=581 ---

输入文本: After the war, as the Midway was preparing for retirement, she was called upon one last time to the Philippines to help with an evacuation after the eruption of Mt. Pinatubo.

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
      "cause": "the eruption",
      "effect": "an evacuation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "eruption of Mt. Pinatubo"
      },
      "effect": {
        "span": "an evacuation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=604 ---

输入文本: A stereo buss outputs the stereo buss signal; a record buss outputs the record buss signal.

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
      "cause": "A stereo buss",
      "effect": "the stereo buss signal"
    },
    {
      "cause": "a record buss",
      "effect": "the record buss signal"
    }
  ],
  "pred_triples": []
}
```

### --- id=609 ---

输入文本: The hull caused a scratch on the eye and that is why it's not healing all the way.

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
      "cause": "The hull",
      "effect": "a scratch"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The hull"
      },
      "effect": {
        "span": "a scratch on the eye"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "a scratch on the eye"
      },
      "effect": {
        "span": "it's not healing all the way"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=630 ---

输入文本: The violence resulted in the death of police "capo" Filippo Raciti, which caused widespread soul-searching and a week-long suspension of Italian football.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "The violence",
      "effect": "the death"
    },
    {
      "cause": "the death",
      "effect": "widespread soul-searching"
    },
    {
      "cause": "the death",
      "effect": "a week-long suspension"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "violence"
      },
      "effect": {
        "span": "the death of police \"capo\" Filippo Raciti"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "the death of police \"capo\" Filippo Raciti"
      },
      "effect": {
        "span": "widespread soul-searching"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "the death of police \"capo\" Filippo Raciti"
      },
      "effect": {
        "span": "a week-long suspension of Italian football"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=635 ---

输入文本: More than 4500 tons of nitrogen oxides annually -- a pollutant that causes smog, acid rain, and contributes to asthma attacks and other breathing problems.

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
    "tp": 0,
    "fp": 2,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "a pollutant",
      "effect": "smog"
    },
    {
      "cause": "a pollutant",
      "effect": "acid rain"
    },
    {
      "cause": "a pollutant",
      "effect": "asthma attacks"
    },
    {
      "cause": "a pollutant",
      "effect": "other breathing problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "pollutant"
      },
      "effect": {
        "span": "smog"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "pollutant"
      },
      "effect": {
        "span": "acid rain"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=662 ---

输入文本: Thus previous scientific estimates had overstated the devastation caused by the asteroid, since topographic and ecologic factors contributing to the result had not been taken into account.

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
      "cause": "the asteroid",
      "effect": "the devastation"
    },
    {
      "cause": "topographic and ecologic factors",
      "effect": "the result"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the asteroid"
      },
      "effect": {
        "span": "the devastation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=677 ---

输入文本: The damages caused by mudslides, tremors, subsidence, superficial or underground water were verified, as well as swelling clay soils.

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
      "cause": "mudslides",
      "effect": "The damages"
    },
    {
      "cause": "tremors",
      "effect": "The damages"
    },
    {
      "cause": "subsidence",
      "effect": "The damages"
    },
    {
      "cause": "superficial or underground water",
      "effect": "The damages"
    },
    {
      "cause": "swelling clay soils",
      "effect": "The damages"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "mudslides"
      },
      "effect": {
        "span": "The damages"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "tremors"
      },
      "effect": {
        "span": "The damages"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "subsidence"
      },
      "effect": {
        "span": "The damages"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "superficial or underground water"
      },
      "effect": {
        "span": "The damages"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=684 ---

输入文本: He clicked the left key of the mouse in order to copy the chosen translation to the clipboard.

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
        "span": "He clicked the left key of the mouse"
      },
      "effect": {
        "span": "copy the chosen translation to the clipboard"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=721 ---

输入文本: Most illnesses, including colds and flu, cause a toxic overload that also increases the stress on the kidneys.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "colds",
      "effect": "a toxic overload"
    },
    {
      "cause": "flu",
      "effect": "a toxic overload"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Most illnesses"
      },
      "effect": {
        "span": "a toxic overload"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "colds"
      },
      "effect": {
        "span": "a toxic overload"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "flu"
      },
      "effect": {
        "span": "a toxic overload"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=771 ---

输入文本: I used to get terrible headaches from sinus infections that resulted in taking antibiotics a few times a year.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "terrible headaches",
      "effect": "taking antibiotics"
    },
    {
      "cause": "sinus infections",
      "effect": "terrible headaches"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "sinus infections"
      },
      "effect": {
        "span": "terrible headaches"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "sinus infections"
      },
      "effect": {
        "span": "taking antibiotics a few times a year"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=781 ---

输入文本: Information about Salmonellosis, an illness caused by a bacteria found in raw food, soil, or water.

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
      "cause": "a bacteria",
      "effect": "an illness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a bacteria found in raw food, soil, or water"
      },
      "effect": {
        "span": "Salmonellosis"
      },
      "relation": "caused"
    }
  ]
}
```
