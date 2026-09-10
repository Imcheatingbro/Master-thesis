# Qwen3.6 35B A3B li Fixed + RAG eval report

## 配置
```json
{
  "label": "Qwen3.6 35B A3B li Fixed + RAG",
  "model": "qwen/qwen3.6-35b-a3b",
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
  "metadata_path": "D:\\Master thesis\\RAG Database\\bge-small-en-v1.5_examples.jsonl",
  "embeddings_path": "D:\\Master thesis\\RAG Database\\bge-small-en-v1.5_embeddings.npy"
}
```

## 统计指标
```text
================ Qwen3.6 35B A3B li Fixed + RAG final report ================
样本总数: 786
  Gold 含因果: 191 | Pred 含因果: 182
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.981
  Precision: 0.984
  Recall   : 0.937
  F1       : 0.960
  (TP=179, TN=592, FP=3, FN=12)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 786
    Gold triples: 296 | Pred triples: 268
    Precision: 0.627
    Recall   : 0.568
    F1       : 0.596
    (TP=168, FP=100, FN=128)
  [anchor_window] (primary)
    样本数: 786
    Gold triples: 296 | Pred triples: 268
    Precision: 0.836
    Recall   : 0.757
    F1       : 0.794
    (TP=224, FP=44, FN=72)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 179
    Gold triples: 282 | Pred triples: 265
    Precision: 0.634
    Recall   : 0.596
    F1       : 0.614
    (TP=168, FP=97, FN=114)
  [anchor_window] (primary)
    样本数: 179
    Gold triples: 282 | Pred triples: 265
    Precision: 0.845
    Recall   : 0.794
    F1       : 0.819
    (TP=224, FP=41, FN=58)
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

Sample details shown: all 62 wrong samples from 786 total samples.

### --- id=25 ---

输入文本: Priority must be given to efforts to combat insecurity and thus poverty, major cause of violence most often experienced by poorest.

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
      "cause": "poverty",
      "effect": "violence"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "insecurity"
      },
      "effect": {
        "span": "violence"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "poverty"
      },
      "effect": {
        "span": "violence"
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
        "span": "the debris"
      },
      "effect": {
        "span": "a crash"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=48 ---

输入文本: The vascular dilatation was caused by the sympathetic and the course of vaso-motor nerves.

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
      "cause": "the sympathetic",
      "effect": "The vascular dilatation"
    },
    {
      "cause": "the course",
      "effect": "The vascular dilatation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the sympathetic and the course of vaso-motor nerves"
      },
      "effect": {
        "span": "The vascular dilatation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=52 ---

输入文本: Colds and flu cause inflammation of the mucous membranes of the nose, throat and mouth.

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
      "cause": "Colds",
      "effect": "inflammation"
    },
    {
      "cause": "flu",
      "effect": "inflammation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Colds and flu"
      },
      "effect": {
        "span": "inflammation of the mucous membranes of the nose, throat and mouth"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=59 ---

输入文本: A cancer survivor writes about the relatively rare occurrence of calcification of the breast after radiation therapy.

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
      "cause": "radiation therapy",
      "effect": "calcification"
    }
  ],
  "pred_triples": []
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
        "span": "high heat-humidity"
      },
      "effect": {
        "span": "nausea"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "high heat-humidity"
      },
      "effect": {
        "span": "dizziness"
      },
      "relation": "caused"
    },
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
        "span": "ringworm of the scalp"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "a fungus"
      },
      "effect": {
        "span": "them"
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
        "span": "pollution"
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

### --- id=98 ---

输入文本: He created and advocated "flower power,"a strategy in which antiwar demonstrators promoted positive values like peace and love to dramatize their opposition to the destruction and death caused by the war in Vietnam.

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
      "cause": "the war",
      "effect": "the destruction"
    },
    {
      "cause": "the war",
      "effect": "death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the war in Vietnam"
      },
      "effect": {
        "span": "the destruction and death"
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
      "cause": "the earthquake",
      "effect": "the fire"
    }
  ],
  "pred_triples": []
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
        "span": "deaths"
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

### --- id=141 ---

输入文本: Pneumococcal meningitis is caused by pneumococcus bacteria, which also cause several diseases of the respiratory system, including pneumonia.

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
    }
  ]
}
```

### --- id=155 ---

输入文本: Zinc is essential for growth and cell division.

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
      "cause": "Zinc",
      "effect": "growth"
    },
    {
      "cause": "Zinc",
      "effect": "cell division"
    }
  ],
  "pred_triples": []
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

### --- id=190 ---

输入文本: The poet Essex Hemphill conquered sorrow after the loss of a friend by taking up the cause of that friend.

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
      "cause": "the loss",
      "effect": "sorrow"
    }
  ],
  "pred_triples": []
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

### --- id=229 ---

输入文本: The movie gives the inaccurate impression that the Apaches all surrendered.

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
      "cause": "The movie",
      "effect": "the inaccurate impression"
    }
  ],
  "pred_triples": []
}
```

### --- id=231 ---

输入文本: This is one of the more common causes of hair loss caused by stress and when you are losing hair because of this your hair stops growing and lies dormant.

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
      "cause": "stress",
      "effect": "hair loss"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "stress"
      },
      "effect": {
        "span": "hair loss"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "stress"
      },
      "effect": {
        "span": "losing hair"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "losing hair"
      },
      "effect": {
        "span": "hair stops growing and lies dormant"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=232 ---

输入文本: But the discomfort caused by the ointment and the duration of treatment often result in non-compliance.

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
      "cause": "the discomfort",
      "effect": "non-compliance"
    },
    {
      "cause": "the ointment",
      "effect": "the discomfort"
    },
    {
      "cause": "the duration",
      "effect": "non-compliance"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the ointment"
      },
      "effect": {
        "span": "the discomfort"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=240 ---

输入文本: When I start the engine the car makes a screaching sound.

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
      "cause": "the car",
      "effect": "a screaching sound"
    }
  ],
  "pred_triples": []
}
```

### --- id=244 ---

输入文本: The largest landslide triggered by the earthquake is located approximately 32 kilometers southeast of Muzafarrabad in a tributary valley of the Jhelum River.

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
      "cause": "the earthquake",
      "effect": "The largest landslide"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the earthquake"
      },
      "effect": {
        "span": "landslide"
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

### --- id=279 ---

输入文本: The news that the stock-index futures have been approved stimulated Wednesday's market.

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
        "span": "the stock-index futures have been approved"
      },
      "effect": {
        "span": "Wednesday's market"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=294 ---

输入文本: Aware of the suffering caused by exploitation, social injustice, stealing, and oppression, I am committed to cultivate loving kindness and learn ways to work for the well-being of people, animals, plants, and minerals.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "exploitation",
      "effect": "the suffering"
    },
    {
      "cause": "social injustice",
      "effect": "the suffering"
    },
    {
      "cause": "stealing",
      "effect": "the suffering"
    },
    {
      "cause": "oppression",
      "effect": "the suffering"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "exploitation"
      },
      "effect": {
        "span": "suffering"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "social injustice"
      },
      "effect": {
        "span": "suffering"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "stealing"
      },
      "effect": {
        "span": "suffering"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "oppression"
      },
      "effect": {
        "span": "suffering"
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
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
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
        "span": "complications"
      },
      "effect": {
        "span": "patient deaths"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "complications"
      },
      "effect": {
        "span": "a serious injury"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=353 ---

输入文本: The genreal anesthetic cause unconsciousness and insensibility to paid and are used for major surgical procedures.

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
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "The genreal anesthetic",
      "effect": "unconsciousness"
    },
    {
      "cause": "The genreal anesthetic",
      "effect": "insensibility"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "anesthetic"
      },
      "effect": {
        "span": "unconsciousness"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "anesthetic"
      },
      "effect": {
        "span": "insensibility"
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

### --- id=369 ---

输入文本: The drag caused by the Earth's atmosphere works against a rocket or a water molecule.

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
      "cause": "the Earth's atmosphere",
      "effect": "The drag"
    }
  ],
  "pred_triples": []
}
```

### --- id=370 ---

输入文本: Snails and slugs cause damage to seedlings, flowers, vegetables and shrubs.

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
      "cause": "Snails",
      "effect": "damage"
    },
    {
      "cause": "slugs",
      "effect": "damage"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Snails and slugs"
      },
      "effect": {
        "span": "damage"
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
      "cause": "These chemical studies",
      "effect": "proof"
    }
  ],
  "pred_triples": []
}
```

### --- id=435 ---

输入文本: I have found that I have extremely sensitive skin and most cleaners cause rash or a burning sensation if it has contact with my skin.

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
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "most cleaners",
      "effect": "rash"
    },
    {
      "cause": "most cleaners",
      "effect": "a burning sensation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cleaners"
      },
      "effect": {
        "span": "rash"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "cleaners"
      },
      "effect": {
        "span": "a burning sensation"
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

### --- id=489 ---

输入文本: The flooding, caused by a cyclone, came on the heels of a prolonged drought, which destroyed 60 percent of Fiji's sugar cane crop last year and cost more than 50 million Fijian dollars  in relief and rehabilitation.

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
      "cause": "a cyclone",
      "effect": "The flooding"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a cyclone"
      },
      "effect": {
        "span": "The flooding"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "a prolonged drought"
      },
      "effect": {
        "span": "60 percent of Fiji's sugar cane crop"
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

### --- id=532 ---

输入文本: Using the product around the house killed germs that were causing flu, colds or sore throat.

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
      "cause": "germs",
      "effect": "flu"
    },
    {
      "cause": "germs",
      "effect": "colds"
    },
    {
      "cause": "germs",
      "effect": "sore throat"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "germs"
      },
      "effect": {
        "span": "sore throat"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=538 ---

输入文本: The pipeline had to face the following main concerns from opposition: disturbance of animal migration patterns, environmental damage from spills, geological concerns and the Alaskan permafrost.

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
      "cause": "spills",
      "effect": "environmental damage"
    }
  ],
  "pred_triples": []
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
        "span": "clandestine wealth-transfer plaguing the productive sector"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=559 ---

输入文本: Dry air, dust and wind dry out the nose and throat and cause nosebleeds, coughing, wheezing, and other short-term respiratory problems

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 12
  },
  "anchor_window_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 8
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 12
  },
  "gold_relations": [
    {
      "cause": "Dry air",
      "effect": "nosebleeds"
    },
    {
      "cause": "Dry air",
      "effect": "coughing"
    },
    {
      "cause": "Dry air",
      "effect": "wheezing"
    },
    {
      "cause": "Dry air",
      "effect": "other short-term respiratory problems"
    },
    {
      "cause": "dust",
      "effect": "nosebleeds"
    },
    {
      "cause": "dust",
      "effect": "coughing"
    },
    {
      "cause": "dust",
      "effect": "wheezing"
    },
    {
      "cause": "dust",
      "effect": "other short-term respiratory problems"
    },
    {
      "cause": "wind",
      "effect": "nosebleeds"
    },
    {
      "cause": "wind",
      "effect": "coughing"
    },
    {
      "cause": "wind",
      "effect": "wheezing"
    },
    {
      "cause": "wind",
      "effect": "other short-term respiratory problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Dry air, dust and wind"
      },
      "effect": {
        "span": "nosebleeds"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Dry air, dust and wind"
      },
      "effect": {
        "span": "coughing"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Dry air, dust and wind"
      },
      "effect": {
        "span": "wheezing"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Dry air, dust and wind"
      },
      "effect": {
        "span": "other short-term respiratory problems"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=563 ---

输入文本: Collapsing commodity prices have pushed the farmer into poverty.

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
        "span": "Collapsing commodity prices"
      },
      "effect": {
        "span": "poverty"
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
      "cause": "The clock",
      "effect": "a loud chime"
    }
  ],
  "pred_triples": [
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

### --- id=576 ---

输入文本: Various hormonal, bacterial and inflammatory disturbances cause acne.

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
      "cause": "Various hormonal, bacterial and inflammatory disturbances",
      "effect": "acne"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "disturbances"
      },
      "effect": {
        "span": "acne"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=588 ---

输入文本: The presentation uses animation to show how germs and microbes cause sickness, and outlines simple preventive measures.

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
      "cause": "germs",
      "effect": "sickness"
    },
    {
      "cause": "microbes",
      "effect": "sickness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "germs and microbes"
      },
      "effect": {
        "span": "sickness"
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
      "cause": "The hull",
      "effect": "a scratch"
    }
  ],
  "pred_triples": [
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

### --- id=610 ---

输入文本: Getting help has reduced the time to reverse all the irritation that had been caused by the fungus.

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
      "cause": "the fungus",
      "effect": "all the irritation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the fungus"
      },
      "effect": {
        "span": "irritation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=633 ---

输入文本: The dust, noise, and sleep deprivation produced by the construction are intolerable.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 3,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 3,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "the construction",
      "effect": "The dust"
    },
    {
      "cause": "the construction",
      "effect": "noise"
    },
    {
      "cause": "the construction",
      "effect": "sleep deprivation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the construction"
      },
      "effect": {
        "span": "dust"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "the construction"
      },
      "effect": {
        "span": "noise"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "the construction"
      },
      "effect": {
        "span": "sleep deprivation"
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
        "span": "a pollutant"
      },
      "effect": {
        "span": "smog"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "a pollutant"
      },
      "effect": {
        "span": "acid rain"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=651 ---

输入文本: A method of mitigating the effect of a market spike caused by the triggering and the election of a conditional order includes monitoring conditional orders.

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
      "cause": "the triggering",
      "effect": "a market spike"
    },
    {
      "cause": "the election",
      "effect": "a market spike"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the triggering and the election of a conditional order"
      },
      "effect": {
        "span": "a market spike"
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

### --- id=667 ---

输入文本: Alcohol and drugs directly cause suicide by significantly diminishing the reasoning of the person at the time of the suicide.

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
      "cause": "Alcohol",
      "effect": "suicide"
    },
    {
      "cause": "drugs",
      "effect": "suicide"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Alcohol and drugs"
      },
      "effect": {
        "span": "suicide"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=673 ---

输入文本: A month of snowy sundays in January had an adverse impact on Prospect's finances.

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
        "span": "A month of snowy sundays in January"
      },
      "effect": {
        "span": "an adverse impact on Prospect's finances"
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

### --- id=678 ---

输入文本: The boom and shaking was caused by the asteroid that passed Earth yesterday.

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
      "cause": "the asteroid",
      "effect": "The boom"
    },
    {
      "cause": "the asteroid",
      "effect": "shaking"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the asteroid"
      },
      "effect": {
        "span": "The boom and shaking"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=682 ---

输入文本: The pollution from animal factories is also destroying parts of the world's oceans.

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
      "cause": "animal factories",
      "effect": "The pollution"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "animal factories"
      },
      "effect": {
        "span": "pollution"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=710 ---

输入文本: Bounding pulses are caused by the relatively low systemic arterial blood pressure due to the continuous runoff of blood from the aorta into the pulmonary artery.

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
      "cause": "the relatively low systemic arterial blood pressure",
      "effect": "Bounding pulses"
    },
    {
      "cause": "the continuous runoff",
      "effect": "the relatively low systemic arterial blood pressure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the relatively low systemic arterial blood pressure"
      },
      "effect": {
        "span": "Bounding pulses"
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
        "span": "Most illnesses, including colds and flu"
      },
      "effect": {
        "span": "a toxic overload"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "a toxic overload"
      },
      "effect": {
        "span": "the stress on the kidneys"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=724 ---

输入文本: The grief from sudden death is completely different from expected death, when families have time to prepare and say goodbye.

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
      "cause": "sudden death",
      "effect": "The grief"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "sudden death"
      },
      "effect": {
        "span": "grief"
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
        "span": "a bacteria"
      },
      "effect": {
        "span": "Salmonellosis"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=785 ---

输入文本: The earthquake caused the failures of the electric power system, the water supply system, the sewer system, the telephone and telegraph systems.

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
      "cause": "The earthquake",
      "effect": "the failures"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The earthquake"
      },
      "effect": {
        "span": "the failures of the electric power system"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "The earthquake"
      },
      "effect": {
        "span": "the water supply system"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "The earthquake"
      },
      "effect": {
        "span": "the sewer system"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "The earthquake"
      },
      "effect": {
        "span": "the telephone and telegraph systems"
      },
      "relation": "caused"
    }
  ]
}
```
