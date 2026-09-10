# Gemma 4 26B A4B QAT Li full dataset family RAG reload50 rerun eval report

## 配置
```json
{
  "label": "Gemma 4 26B A4B QAT Li full dataset family RAG reload50 rerun",
  "model": "google/gemma-4-26b-a4b-qat",
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
  "metadata_path": "D:\\Master thesis\\RAG Database\\cnc_examples.jsonl",
  "embeddings_path": "D:\\Master thesis\\RAG Database\\cnc_embeddings.npy"
}
```

## 统计指标
```text
================ Gemma 4 26B A4B QAT Li full dataset family RAG reload50 rerun final report ================
样本总数: 786
  Gold 含因果: 191 | Pred 含因果: 210
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.945
  Precision: 0.852
  Recall   : 0.937
  F1       : 0.893
  (TP=179, TN=564, FP=31, FN=12)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 786
    Gold triples: 296 | Pred triples: 326
    Precision: 0.405
    Recall   : 0.446
    F1       : 0.424
    (TP=132, FP=194, FN=164)
  [anchor_window] (primary)
    样本数: 786
    Gold triples: 296 | Pred triples: 326
    Precision: 0.718
    Recall   : 0.791
    F1       : 0.752
    (TP=234, FP=92, FN=62)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 179
    Gold triples: 282 | Pred triples: 295
    Precision: 0.447
    Recall   : 0.468
    F1       : 0.458
    (TP=132, FP=163, FN=150)
  [anchor_window] (primary)
    样本数: 179
    Gold triples: 282 | Pred triples: 295
    Precision: 0.793
    Recall   : 0.830
    F1       : 0.811
    (TP=234, FP=61, FN=48)
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

Sample details shown: all 98 wrong samples from 786 total samples.

### --- id=9 ---

输入文本: The bottle carrier converts your bottle into a canteen.

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
        "span": "The bottle carrier"
      },
      "relation": "caused",
      "effect": {
        "span": "your bottle into a canteen"
      }
    }
  ]
}
```

### --- id=22 ---

输入文本: Every child and young person seen at Starship with intoxication from alcohol or illicit drug use had a social work assessment before leaving the hospital.

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
      "cause": "alcohol or illicit drug use",
      "effect": "intoxication"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "alcohol"
      },
      "relation": "caused",
      "effect": {
        "span": "intoxication"
      }
    },
    {
      "cause": {
        "span": "illicit drug use"
      },
      "relation": "caused",
      "effect": {
        "span": "intoxication"
      }
    }
  ]
}
```

### --- id=29 ---

输入文本: The warmth was radiating from the fireplace to all corners of the room.

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
      "cause": "the fireplace",
      "effect": "The warmth"
    }
  ],
  "pred_triples": []
}
```

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
      "relation": "caused",
      "effect": {
        "span": "A blood clot"
      }
    }
  ]
}
```

### --- id=47 ---

输入文本: Glaucoma is one of the leading causes for blindness and currently about 90 million patients worldwide are affected by the disease.

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
      "cause": "Glaucoma",
      "effect": "blindness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Glaucoma"
      },
      "relation": "caused",
      "effect": {
        "span": "blindness"
      }
    },
    {
      "cause": {
        "span": "the disease"
      },
      "relation": "caused",
      "effect": {
        "span": "about 90 million patients worldwide are affected"
      }
    }
  ]
}
```

### --- id=49 ---

输入文本: Before he leaves Ephesus, however, a riot breaks out, instigated by the silversmiths who manufacture idols of the goddess Artemis; they are afraid that Paul's evangelistic success will ruin their business.

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
      "cause": "the silversmiths",
      "effect": "a riot"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the silversmiths who manufacture idols of the goddess Artemis"
      },
      "relation": "caused",
      "effect": {
        "span": "a riot"
      }
    },
    {
      "cause": {
        "span": "Paul's evangelistic success"
      },
      "relation": "caused",
      "effect": {
        "span": "ruin their business"
      }
    }
  ]
}
```

### --- id=61 ---

输入文本: Just like in Oyo State, Obasanjo sired a clique of renegades, who believe that the State treasury is their birthright.

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
        "span": "Obasanjo"
      },
      "relation": "caused",
      "effect": {
        "span": "a clique of renegades"
      }
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
      "relation": "caused",
      "effect": {
        "span": "ringworm of the scalp"
      }
    },
    {
      "cause": {
        "span": "a fungus that infects the hairs"
      },
      "relation": "caused",
      "effect": {
        "span": "them to break"
      }
    }
  ]
}
```

### --- id=67 ---

输入文本: He likewise directed Edric to fling out his nets, who was rewarded with a miraculous draught of salmons.

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
        "span": "He likewise directed Edric to fling out his nets"
      },
      "relation": "caused",
      "effect": {
        "span": "a miraculous draught of salmons"
      }
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
      "relation": "caused",
      "effect": {
        "span": "the pollution"
      }
    },
    {
      "cause": {
        "span": "soot"
      },
      "relation": "caused",
      "effect": {
        "span": "the light-colored tree trunks became darker"
      }
    }
  ]
}
```

### --- id=76 ---

输入文本: Inhibition through synaptic depression is unlike the previous forms of inhibition in that it turns on more slowly and thus acts as delayed negative feedback.

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
      "cause": "synaptic depression",
      "effect": "Inhibition"
    }
  ],
  "pred_triples": []
}
```

### --- id=77 ---

输入文本: The drone strike that resulted in the death of Pakistan's most wanted terrorist is believed to be a result of deliberately planted false intelligence, sources in South Waziristan have confirmed.

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
      "cause": "The drone strike",
      "effect": "the death"
    },
    {
      "cause": "deliberately planted false intelligence",
      "effect": "The drone strike"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "deliberately planted false intelligence"
      },
      "relation": "caused",
      "effect": {
        "span": "the drone strike"
      }
    },
    {
      "cause": {
        "span": "deliberately planted false intelligence"
      },
      "relation": "caused",
      "effect": {
        "span": "the death of Pakistan's most wanted terrorist"
      }
    }
  ]
}
```

### --- id=83 ---

输入文本: Cold sores or fever blisters are caused by the herpes simplex virus and are usually relatively easy to identify.

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
      "cause": "the herpes simplex virus",
      "effect": "Cold sores"
    },
    {
      "cause": "the herpes simplex virus",
      "effect": "fever blisters"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the herpes simplex virus"
      },
      "relation": "caused",
      "effect": {
        "span": "Cold sores or fever blisters"
      }
    }
  ]
}
```

### --- id=84 ---

输入文本: Our company converts waste plastics into crude oil.

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
        "span": "waste plastics"
      },
      "relation": "caused",
      "effect": {
        "span": "crude oil"
      }
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
      "relation": "caused",
      "effect": {
        "span": "discomfort"
      }
    },
    {
      "cause": {
        "span": "muscle spasm"
      },
      "relation": "caused",
      "effect": {
        "span": "discomfort"
      }
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
      "relation": "caused",
      "effect": {
        "span": "the destruction and death"
      }
    }
  ]
}
```

### --- id=100 ---

输入文本: This paralyzed him so much that when trying to lay back on the bed, he fell on his back and hit his head on the bed post.

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
        "span": "This"
      },
      "relation": "caused",
      "effect": {
        "span": "he fell on his back and hit his head on the bed post"
      }
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
      "relation": "caused",
      "effect": {
        "span": "the three musicians improvised an album's worth of material"
      }
    }
  ]
}
```

### --- id=110 ---

输入文本: I too, get a headache from wine, and was always told that it was the sulfites.

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
      "cause": "wine",
      "effect": "a headache"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "wine"
      },
      "relation": "caused",
      "effect": {
        "span": "a headache"
      }
    },
    {
      "cause": {
        "span": "the sulfites"
      },
      "relation": "caused",
      "effect": {
        "span": "a headache"
      }
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
      "cause": "the earthquake",
      "effect": "the fire"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the earthquake"
      },
      "relation": "caused",
      "effect": {
        "span": "the fire"
      }
    },
    {
      "cause": {
        "span": "the fire"
      },
      "relation": "caused",
      "effect": {
        "span": "burned out 7456 houses in over 530 localities"
      }
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
      "relation": "caused",
      "effect": {
        "span": "the on average lower share of female aldermen than female local councillors"
      }
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
      "relation": "caused",
      "effect": {
        "span": "suffocation"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Pneumococcal meningitis"
      }
    },
    {
      "cause": {
        "span": "pneumococcus bacteria"
      },
      "relation": "caused",
      "effect": {
        "span": "several diseases of the respiratory system"
      }
    },
    {
      "cause": {
        "span": "pneumococcus bacteria"
      },
      "relation": "caused",
      "effect": {
        "span": "pneumonia"
      }
    }
  ]
}
```

### --- id=151 ---

输入文本: Eye discomfort from this staring effect is exacerbated by low humidity.

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
      "cause": "this staring effect",
      "effect": "Eye discomfort"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "this staring effect"
      },
      "relation": "caused",
      "effect": {
        "span": "Eye discomfort"
      }
    },
    {
      "cause": {
        "span": "low humidity"
      },
      "relation": "caused",
      "effect": {
        "span": "Eye discomfort"
      }
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

### --- id=156 ---

输入文本: The average soldier joins your army for the pay, and if you cannot pay him he will walk away and go back to get a job as a farmer or laborer.

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
        "span": "you cannot pay him"
      },
      "relation": "caused",
      "effect": {
        "span": "he will walk away and go back to get a job as a farmer or laborer"
      }
    }
  ]
}
```

### --- id=169 ---

输入文本: Menopause and PMS cause stress and anxiety even without imbalanced hormones.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 4
  },
  "gold_relations": [
    {
      "cause": "Menopause",
      "effect": "stress"
    },
    {
      "cause": "Menopause",
      "effect": "anxiety"
    },
    {
      "cause": "PMS",
      "effect": "stress"
    },
    {
      "cause": "PMS",
      "effect": "anxiety"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Menopause"
      },
      "relation": "caused",
      "effect": {
        "span": "stress and anxiety"
      }
    },
    {
      "cause": {
        "span": "PMS"
      },
      "relation": "caused",
      "effect": {
        "span": "stress and anxiety"
      }
    }
  ]
}
```

### --- id=188 ---

输入文本: When the force was generated via the joystick, the reproduced force matched the original force much more accurately.

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
      "cause": "the joystick",
      "effect": "the force"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the force was generated via the joystick"
      },
      "relation": "caused",
      "effect": {
        "span": "the reproduced force matched the original force much more accurately"
      }
    }
  ]
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
    "tp": 0,
    "fp": 6,
    "fn": 6
  },
  "anchor_window_counts": {
    "tp": 3,
    "fp": 3,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 6,
    "fn": 6
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
        "span": "the location design"
      },
      "relation": "caused",
      "effect": {
        "span": "setbacks and technical problems"
      }
    },
    {
      "cause": {
        "span": "flooding"
      },
      "relation": "caused",
      "effect": {
        "span": "setbacks and technical problems"
      }
    },
    {
      "cause": {
        "span": "moisture"
      },
      "relation": "caused",
      "effect": {
        "span": "setbacks and technical problems"
      }
    },
    {
      "cause": {
        "span": "the location design"
      },
      "relation": "caused",
      "effect": {
        "span": "bumped up the investment cost beyond the initial budgetary estimates"
      }
    },
    {
      "cause": {
        "span": "flooding"
      },
      "relation": "caused",
      "effect": {
        "span": "bumped up the investment cost beyond the initial budgetary estimates"
      }
    },
    {
      "cause": {
        "span": "moisture"
      },
      "relation": "caused",
      "effect": {
        "span": "bumped up the investment cost beyond the initial budgetary estimates"
      }
    }
  ]
}
```

### --- id=193 ---

输入文本: An oil spill caused by a collision between a ship and a barge closed the ship channel servicing the nation's second largest port.

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
      "cause": "a collision",
      "effect": "An oil spill"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a collision between a ship and a barge"
      },
      "relation": "caused",
      "effect": {
        "span": "An oil spill"
      }
    },
    {
      "cause": {
        "span": "An oil spill"
      },
      "relation": "caused",
      "effect": {
        "span": "closed the ship channel servicing the nation's second largest port"
      }
    }
  ]
}
```

### --- id=212 ---

输入文本: My wife mistakenly poured water into the valve cover of her 1999 Sebring when it began overheating.

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
        "span": "it began overheating"
      },
      "relation": "caused",
      "effect": {
        "span": "My wife mistakenly poured water into the valve cover of her 1999 Sebring"
      }
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

### --- id=231 ---

输入文本: This is one of the more common causes of hair loss caused by stress and when you are losing hair because of this your hair stops growing and lies dormant.

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
      "cause": "stress",
      "effect": "hair loss"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "stress"
      },
      "relation": "caused",
      "effect": {
        "span": "hair loss"
      }
    },
    {
      "cause": {
        "span": "this"
      },
      "relation": "caused",
      "effect": {
        "span": "your hair stops growing and lies dormant"
      }
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
        "span": "the discomfort caused by the ointment"
      },
      "relation": "caused",
      "effect": {
        "span": "non-compliance"
      }
    },
    {
      "cause": {
        "span": "the duration of treatment"
      },
      "relation": "caused",
      "effect": {
        "span": "non-compliance"
      }
    }
  ]
}
```

### --- id=239 ---

输入文本: Dartmouth nearly narrowed the gap to one goal when a slapshot popped out of the glove of Princeton goalie Zane Kalemba '10.

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
        "span": "a slapshot popped out of the glove of Princeton goalie Zane Kalemba '10"
      },
      "relation": "caused",
      "effect": {
        "span": "Dartmouth nearly narrowed the gap to one goal"
      }
    }
  ]
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
        "span": "I start the engine"
      },
      "relation": "caused",
      "effect": {
        "span": "the car makes a screaching sound"
      }
    }
  ]
}
```

### --- id=241 ---

输入文本: This year's Nobel Laureates in Physiology or Medicine made the remarkable and unexpected discovery that inflammation in the stomach  as well as ulceration of the stomach or duodenum  is the result of an infection of the stomach caused by the bacterium Helicobacter pylori.

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
    "tp": 0,
    "fp": 2,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "an infection",
      "effect": "inflammation"
    },
    {
      "cause": "an infection",
      "effect": "ulceration"
    },
    {
      "cause": "the bacterium Helicobacter pylori",
      "effect": "an infection"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the bacterium Helicobacter pylori"
      },
      "relation": "caused",
      "effect": {
        "span": "inflammation in the stomach"
      }
    },
    {
      "cause": {
        "span": "the bacterium Helicobacter pylori"
      },
      "relation": "caused",
      "effect": {
        "span": "ulceration of the stomach or duodenum"
      }
    }
  ]
}
```

### --- id=245 ---

输入文本: The transmitter emits a constant radio signal to crea.

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
      "cause": "The transmitter",
      "effect": "a constant radio signal"
    }
  ],
  "pred_triples": []
}
```

### --- id=251 ---

输入文本: These are all symptoms of the muscle paralysis caused by the bacterial toxin.

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
      "cause": "the bacterial toxin",
      "effect": "the muscle paralysis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the bacterial toxin"
      },
      "relation": "caused",
      "effect": {
        "span": "muscle paralysis"
      }
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
      "relation": "caused",
      "effect": {
        "span": "pain"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Wednesday's market"
      }
    }
  ]
}
```

### --- id=290 ---

输入文本: Lymphedema is an abnormal build-up of fluid that causes swelling, most often in the arms or legs.

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
      "cause": "Lymphedema",
      "effect": "swelling"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an abnormal build-up of fluid"
      },
      "relation": "caused",
      "effect": {
        "span": "swelling"
      }
    }
  ]
}
```

### --- id=297 ---

输入文本: On 8 February 1992, Ulysses reached Jupiter for the gravity-assist manoeuvre that placed the spacecraft in a polar orbit.

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
        "span": "the gravity-assist manoeuvre"
      },
      "relation": "caused",
      "effect": {
        "span": "placed the spacecraft in a polar orbit"
      }
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
      "cause": "The malfunctions",
      "effect": "delays"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The malfunctions on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "delays for patrons waiting to check out or renew books at the branches"
      }
    },
    {
      "cause": {
        "span": "The malfunctions on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "impeded access to personal accounts that allow users to renew or hold books online"
      }
    }
  ]
}
```

### --- id=310 ---

输入文本: General information about the infection caused by the bacteria called Salmonella, when food is eaten raw or undercooked.

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
      "cause": "the bacteria",
      "effect": "the infection"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the bacteria called Salmonella"
      },
      "relation": "caused",
      "effect": {
        "span": "the infection"
      }
    },
    {
      "cause": {
        "span": "food is eaten raw or undercooked"
      },
      "relation": "caused",
      "effect": {
        "span": "the infection"
      }
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
      "relation": "caused",
      "effect": {
        "span": "patient deaths"
      }
    },
    {
      "cause": {
        "span": "16 percent"
      },
      "relation": "caused",
      "effect": {
        "span": "a serious injury"
      }
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
        "span": "The genreal anesthetic"
      },
      "relation": "caused",
      "effect": {
        "span": "unconsciousness and insensibility to paid"
      }
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
      "relation": "caused",
      "effect": {
        "span": "water pollution"
      }
    }
  ]
}
```

### --- id=356 ---

输入文本: We poured the molten aluminium into ingots, which was very dangerous.

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
        "span": "We poured the molten aluminium into ingots"
      },
      "relation": "caused",
      "effect": {
        "span": "which was very dangerous"
      }
    }
  ]
}
```

### --- id=359 ---

输入文本: The subject was taken into custody for trespassing.

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
        "span": "trespassing"
      },
      "relation": "caused",
      "effect": {
        "span": "The subject was taken into custody"
      }
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
      "relation": "caused",
      "effect": {
        "span": "increases stress on the knee joints up to 38%"
      }
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

### --- id=407 ---

输入文本: In that case, the doctor stops the bleeding with hormones.

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
        "span": "hormones"
      },
      "relation": "caused",
      "effect": {
        "span": "the bleeding"
      }
    }
  ]
}
```

### --- id=422 ---

输入文本: My problem is that the advertisement gives the impression that women in rural Bangladesh have 6 children.

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
      "cause": "the advertisement",
      "effect": "the impression"
    }
  ],
  "pred_triples": []
}
```

### --- id=428 ---

输入文本: The radiation from the atomic bomb explosion is a typical acute radiation.

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
      "cause": "the atomic bomb explosion",
      "effect": "The radiation"
    }
  ],
  "pred_triples": []
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
      "cause": "a cyclone",
      "effect": "The flooding"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a cyclone"
      },
      "relation": "caused",
      "effect": {
        "span": "The flooding"
      }
    },
    {
      "cause": {
        "span": "a prolonged drought"
      },
      "relation": "caused",
      "effect": {
        "span": "destroyed 60 percent of Fiji's sugar cane crop last year"
      }
    },
    {
      "cause": {
        "span": "a prolonged drought"
      },
      "relation": "caused",
      "effect": {
        "span": "cost more than 50 million Fijian dollars in relief and rehabilitation"
      }
    }
  ]
}
```

### --- id=497 ---

输入文本: Obama's economic policies are turning into a global disaster.

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
      "cause": "Obama's economic policies",
      "effect": "a global disaster"
    }
  ],
  "pred_triples": []
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
        "span": "factors that are ostensibly unrelated to race but nonetheless contribute to racial inequality"
      },
      "relation": "caused",
      "effect": {
        "span": "racial inequality"
      }
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
      "relation": "caused",
      "effect": {
        "span": "an infection of the airways"
      }
    }
  ]
}
```

### --- id=531 ---

输入文本: Sensitive pets experience rashes and discomfort from ticks and fleas.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 4
  },
  "gold_relations": [
    {
      "cause": "ticks",
      "effect": "rashes"
    },
    {
      "cause": "ticks",
      "effect": "discomfort"
    },
    {
      "cause": "fleas",
      "effect": "rashes"
    },
    {
      "cause": "fleas",
      "effect": "discomfort"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "ticks"
      },
      "relation": "caused",
      "effect": {
        "span": "rashes and discomfort"
      }
    },
    {
      "cause": {
        "span": "fleas"
      },
      "relation": "caused",
      "effect": {
        "span": "rashes and discomfort"
      }
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
    "tp": 3,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 3,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 3,
    "fp": 1,
    "fn": 0
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
        "span": "the product around the house"
      },
      "relation": "caused",
      "effect": {
        "span": "germs"
      }
    },
    {
      "cause": {
        "span": "germs"
      },
      "relation": "caused",
      "effect": {
        "span": "flu"
      }
    },
    {
      "cause": {
        "span": "germs"
      },
      "relation": "caused",
      "effect": {
        "span": "colds"
      }
    },
    {
      "cause": {
        "span": "germs"
      },
      "relation": "caused",
      "effect": {
        "span": "sore throat"
      }
    }
  ]
}
```

### --- id=536 ---

输入文本: Discussion ensued from the Florida contingent on the fact that very stringent landowner protection laws in Florida make it imperative that the highest supportable appraised vallue be offered first.

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
      "cause": "the Florida contingent",
      "effect": "Discussion"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "very stringent landowner protection laws in Florida"
      },
      "relation": "caused",
      "effect": {
        "span": "it be imperative that the highest supportable appraised vallue be offered first"
      }
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
      "relation": "caused",
      "effect": {
        "span": "the falling interest-rate structure"
      }
    },
    {
      "cause": {
        "span": "the falling interest-rate structure"
      },
      "relation": "caused",
      "effect": {
        "span": "the clandestine wealth-transfer plaguing the productive sector"
      }
    },
    {
      "cause": {
        "span": "the clandestine wealth-transfer plaguing the productive sector"
      },
      "relation": "caused",
      "effect": {
        "span": "Swissair was a victim"
      }
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
    "fp": 6,
    "fn": 12
  },
  "anchor_window_counts": {
    "tp": 3,
    "fp": 3,
    "fn": 9
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 6,
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
        "span": "Dry air"
      },
      "relation": "caused",
      "effect": {
        "span": "dry out the nose and throat"
      }
    },
    {
      "cause": {
        "span": "Dry air"
      },
      "relation": "caused",
      "effect": {
        "span": "nosebleeds, coughing, wheezing, and other short-term respiratory problems"
      }
    },
    {
      "cause": {
        "span": "dust"
      },
      "relation": "caused",
      "effect": {
        "span": "dry out the nose and throat"
      }
    },
    {
      "cause": {
        "span": "dust"
      },
      "relation": "caused",
      "effect": {
        "span": "nosebleeds, coughing, wheezing, and other short-term respiratory problems"
      }
    },
    {
      "cause": {
        "span": "wind"
      },
      "relation": "caused",
      "effect": {
        "span": "dry out the nose and throat"
      }
    },
    {
      "cause": {
        "span": "wind"
      },
      "relation": "caused",
      "effect": {
        "span": "nosebleeds, coughing, wheezing, and other short-term respiratory problems"
      }
    }
  ]
}
```

### --- id=561 ---

输入文本: When the first model sank in August 1991, the crash caused a seismic event registering 3.0 on the Richter scale, and left nothing but a pile of debris at 220m of depth.

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
      "cause": "the crash",
      "effect": "a seismic event"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the crash"
      },
      "relation": "caused",
      "effect": {
        "span": "a seismic event registering 3.0 on the Richter scale"
      }
    },
    {
      "cause": {
        "span": "the crash"
      },
      "relation": "caused",
      "effect": {
        "span": "a pile of debris at 220m of depth"
      }
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
      "relation": "caused",
      "effect": {
        "span": "the farmer into poverty"
      }
    }
  ]
}
```

### --- id=564 ---

输入文本: Progress comes from constructive competition, and churches and religions can benefit greatly from it.

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
      "cause": "constructive competition",
      "effect": "Progress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "constructive competition"
      },
      "relation": "caused",
      "effect": {
        "span": "Progress"
      }
    },
    {
      "cause": {
        "span": "constructive competition"
      },
      "relation": "caused",
      "effect": {
        "span": "churches and religions can benefit greatly"
      }
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
      "relation": "caused",
      "effect": {
        "span": "me jump"
      }
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
      "relation": "caused",
      "effect": {
        "span": "decreasing the ROI for these programs"
      }
    }
  ]
}
```

### --- id=577 ---

输入文本: In any case, fish oil did harm patients.

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
        "span": "fish oil"
      },
      "relation": "caused",
      "effect": {
        "span": "harm"
      }
    }
  ]
}
```

### --- id=587 ---

输入文本: The alleged abuse resulted in bruises and swelling of the brain.

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
      "cause": "The alleged abuse",
      "effect": "bruises"
    },
    {
      "cause": "The alleged abuse",
      "effect": "swelling"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The alleged abuse"
      },
      "relation": "caused",
      "effect": {
        "span": "bruises and swelling of the brain"
      }
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

### --- id=608 ---

输入文本: The accolade was decided upon after an intense discussion between about 200 members.

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
      "cause": "an intense discussion",
      "effect": "The accolade"
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
      "relation": "caused",
      "effect": {
        "span": "a scratch on the eye"
      }
    },
    {
      "cause": {
        "span": "a scratch on the eye"
      },
      "relation": "caused",
      "effect": {
        "span": "it's not healing all the way"
      }
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
    "tp": 0,
    "fp": 4,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 4
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
        "span": "nitrogen oxides"
      },
      "relation": "caused",
      "effect": {
        "span": "smog"
      }
    },
    {
      "cause": {
        "span": "nitrogen oxides"
      },
      "relation": "caused",
      "effect": {
        "span": "acid rain"
      }
    },
    {
      "cause": {
        "span": "nitrogen oxides"
      },
      "relation": "caused",
      "effect": {
        "span": "asthma attacks"
      }
    },
    {
      "cause": {
        "span": "nitrogen oxides"
      },
      "relation": "caused",
      "effect": {
        "span": "other breathing problems"
      }
    }
  ]
}
```

### --- id=641 ---

输入文本: In an experiment, proteins successfully transported copper into the tissue.

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
        "span": "proteins"
      },
      "relation": "caused",
      "effect": {
        "span": "copper into the tissue"
      }
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
      "relation": "caused",
      "effect": {
        "span": "a market spike"
      }
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
      "relation": "caused",
      "effect": {
        "span": "the devastation"
      }
    }
  ]
}
```

### --- id=670 ---

输入文本: And with a flourish of her wand she unleashed a plague of biting insects, the sand fly.

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
        "span": "a flourish of her wand"
      },
      "relation": "caused",
      "effect": {
        "span": "a plague of biting insects, the sand fly"
      }
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
      "relation": "caused",
      "effect": {
        "span": "an adverse impact on Prospect's finances"
      }
    }
  ]
}
```

### --- id=674 ---

输入文本: Three people had been killed in a fire after the quake and hundreds of people were injured.

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
      "cause": "the quake",
      "effect": "a fire"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the quake"
      },
      "relation": "caused",
      "effect": {
        "span": "Three people had been killed in a fire"
      }
    },
    {
      "cause": {
        "span": "the quake"
      },
      "relation": "caused",
      "effect": {
        "span": "hundreds of people were injured"
      }
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
        "span": "the asteroid that passed Earth yesterday"
      },
      "relation": "caused",
      "effect": {
        "span": "The boom and shaking"
      }
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
      "cause": "animal factories",
      "effect": "The pollution"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "animal factories"
      },
      "relation": "caused",
      "effect": {
        "span": "The pollution"
      }
    },
    {
      "cause": {
        "span": "The pollution"
      },
      "relation": "caused",
      "effect": {
        "span": "destroying parts of the world's oceans"
      }
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
      "relation": "caused",
      "effect": {
        "span": "to copy the chosen translation to the clipboard"
      }
    }
  ]
}
```

### --- id=686 ---

输入文本: Manufacturers passed on the costs to the consumers.

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
        "span": "the costs"
      },
      "relation": "caused",
      "effect": {
        "span": "the consumers"
      }
    }
  ]
}
```

### --- id=695 ---

输入文本: Little did these naive people realize at the time that they were embracing a foul brood of ungrateful vipers, which would soon prove to be their undoing.

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
        "span": "a foul brood of ungrateful vipers"
      },
      "relation": "caused",
      "effect": {
        "span": "their undoing"
      }
    }
  ]
}
```

### --- id=698 ---

输入文本: The fibre pellets were blown into cavities using special equipment.

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
        "span": "special equipment"
      },
      "relation": "caused",
      "effect": {
        "span": "The fibre pellets were blown into cavities"
      }
    }
  ]
}
```

### --- id=715 ---

输入文本: The disruption of electricity and telecommunication lines have thrown the city into darkness.

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
        "span": "The disruption of electricity and telecommunication lines"
      },
      "relation": "caused",
      "effect": {
        "span": "the city into darkness"
      }
    }
  ]
}
```

### --- id=718 ---

输入文本: Bed sores  are caused by pressure, which cuts off blood flow to parts of the body.

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
      "cause": "pressure",
      "effect": "Bed sores"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "pressure"
      },
      "relation": "caused",
      "effect": {
        "span": "Bed sores"
      }
    },
    {
      "cause": {
        "span": "pressure"
      },
      "relation": "caused",
      "effect": {
        "span": "cuts off blood flow to parts of the body"
      }
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
      "relation": "caused",
      "effect": {
        "span": "a toxic overload"
      }
    },
    {
      "cause": {
        "span": "a toxic overload"
      },
      "relation": "caused",
      "effect": {
        "span": "increases the stress on the kidneys"
      }
    }
  ]
}
```

### --- id=722 ---

输入文本: I've just sold a gold ring, which was my last asset and now we have nothing left for a better life.

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
        "span": "I've just sold a gold ring"
      },
      "relation": "caused",
      "effect": {
        "span": "we have nothing left for a better life"
      }
    }
  ]
}
```

### --- id=730 ---

输入文本: The accident caused a traffic snarl on the ever busy bridge leading to diversions to other routes.

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
      "cause": "The accident",
      "effect": "a traffic snarl"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The accident"
      },
      "relation": "caused",
      "effect": {
        "span": "a traffic snarl on the ever busy bridge"
      }
    },
    {
      "cause": {
        "span": "a traffic snarl on the ever busy bridge"
      },
      "relation": "caused",
      "effect": {
        "span": "diversions to other routes"
      }
    }
  ]
}
```

### --- id=742 ---

输入文本: His deeds have thrown thousands of people into eternal financial damnation.

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
        "span": "His deeds"
      },
      "relation": "caused",
      "effect": {
        "span": "eternal financial damnation"
      }
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
      "relation": "caused",
      "effect": {
        "span": "terrible headaches"
      }
    },
    {
      "cause": {
        "span": "sinus infections"
      },
      "relation": "caused",
      "effect": {
        "span": "taking antibiotics a few times a year"
      }
    },
    {
      "cause": {
        "span": "terrible headaches"
      },
      "relation": "caused",
      "effect": {
        "span": "taking antibiotics a few times a year"
      }
    }
  ]
}
```

### --- id=777 ---

输入文本: Later on that same day, an electrical short at the Farragut North station caused a fire on the tracks which shut down service three times over the course of the day.

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
      "cause": "an electrical short",
      "effect": "a fire"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an electrical short at the Farragut North station"
      },
      "relation": "caused",
      "effect": {
        "span": "a fire on the tracks"
      }
    },
    {
      "cause": {
        "span": "a fire on the tracks"
      },
      "relation": "caused",
      "effect": {
        "span": "shut down service three times over the course of the day"
      }
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
    "fp": 4,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
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
      "relation": "caused",
      "effect": {
        "span": "Salmonellosis"
      }
    },
    {
      "cause": {
        "span": "raw food"
      },
      "relation": "caused",
      "effect": {
        "span": "Salmonellosis"
      }
    },
    {
      "cause": {
        "span": "soil"
      },
      "relation": "caused",
      "effect": {
        "span": "Salmonellosis"
      }
    },
    {
      "cause": {
        "span": "water"
      },
      "relation": "caused",
      "effect": {
        "span": "Salmonellosis"
      }
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
      "relation": "caused",
      "effect": {
        "span": "the failures of the electric power system"
      }
    },
    {
      "cause": {
        "span": "The earthquake"
      },
      "relation": "caused",
      "effect": {
        "span": "the water supply system"
      }
    },
    {
      "cause": {
        "span": "The earthquake"
      },
      "relation": "caused",
      "effect": {
        "span": "the sewer system"
      }
    },
    {
      "cause": {
        "span": "The earthquake"
      },
      "relation": "caused",
      "effect": {
        "span": "the telephone and telegraph systems"
      }
    }
  ]
}
```
