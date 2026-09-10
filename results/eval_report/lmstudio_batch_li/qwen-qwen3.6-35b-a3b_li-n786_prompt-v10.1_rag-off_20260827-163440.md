# Qwen3.6 35B A3B Li full dataset eval report

## 配置
```json
{
  "label": "Qwen3.6 35B A3B Li full dataset",
  "model": "qwen/qwen3.6-35b-a3b",
  "dataset": "li",
  "sample_count": 786,
  "prompt_name": "v10.1",
  "use_rag": false,
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
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ Qwen3.6 35B A3B Li full dataset final report ================
样本总数: 786
  Gold 含因果: 191 | Pred 含因果: 162
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.958
  Precision: 0.988
  Recall   : 0.838
  F1       : 0.907
  (TP=160, TN=593, FP=2, FN=31)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 786
    Gold triples: 296 | Pred triples: 257
    Precision: 0.584
    Recall   : 0.507
    F1       : 0.542
    (TP=150, FP=107, FN=146)
  [anchor_window] (primary)
    样本数: 786
    Gold triples: 296 | Pred triples: 257
    Precision: 0.833
    Recall   : 0.723
    F1       : 0.774
    (TP=214, FP=43, FN=82)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 160
    Gold triples: 263 | Pred triples: 255
    Precision: 0.588
    Recall   : 0.570
    F1       : 0.579
    (TP=150, FP=105, FN=113)
  [anchor_window] (primary)
    样本数: 160
    Gold triples: 263 | Pred triples: 255
    Precision: 0.839
    Recall   : 0.814
    F1       : 0.826
    (TP=214, FP=41, FN=49)
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

Sample details shown: all 78 wrong samples from 786 total samples.

### --- id=5 ---

输入文本: In economic terms, the ecological catastrophe caused by the Prestige oil spill is comparable with that caused by the Exxon Valdez.

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
      "cause": "the Prestige oil spill",
      "effect": "the ecological catastrophe"
    },
    {
      "cause": "the Exxon Valdez",
      "effect": "the ecological catastrophe"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Prestige oil spill"
      },
      "relation": "caused",
      "effect": {
        "span": "the ecological catastrophe"
      }
    },
    {
      "cause": {
        "span": "the Exxon Valdez"
      },
      "relation": "caused",
      "effect": {
        "span": "that"
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
      "relation": "caused",
      "effect": {
        "span": "The vascular dilatation"
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
      "cause": "the silversmiths",
      "effect": "a riot"
    }
  ],
  "pred_triples": [
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
      "relation": "caused",
      "effect": {
        "span": "inflammation of the mucous membranes of the nose, throat and mouth"
      }
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
      "relation": "caused",
      "effect": {
        "span": "nausea"
      }
    },
    {
      "cause": {
        "span": "high heat-humidity"
      },
      "relation": "caused",
      "effect": {
        "span": "dizziness"
      }
    },
    {
      "cause": {
        "span": "exhaustion"
      },
      "relation": "caused",
      "effect": {
        "span": "nausea"
      }
    },
    {
      "cause": {
        "span": "exhaustion"
      },
      "relation": "caused",
      "effect": {
        "span": "dizziness"
      }
    },
    {
      "cause": {
        "span": "dehydration"
      },
      "relation": "caused",
      "effect": {
        "span": "nausea"
      }
    },
    {
      "cause": {
        "span": "dehydration"
      },
      "relation": "caused",
      "effect": {
        "span": "dizziness"
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
        "span": "the cases of ringworm of the scalp"
      }
    },
    {
      "cause": {
        "span": "Trichophyton tonsurans"
      },
      "relation": "caused",
      "effect": {
        "span": "them"
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
      "relation": "caused",
      "effect": {
        "span": "pollution"
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

### --- id=72 ---

输入文本: If a participant complaint is the source of an investigative lead, interim contact with the participant should be made by the investigator.

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
      "cause": "a participant complaint",
      "effect": "an investigative lead"
    }
  ],
  "pred_triples": []
}
```

### --- id=74 ---

输入文本: The transmitter generates the electromagnetic wave, some of which will be incident on the receiver.

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
      "effect": "the electromagnetic wave"
    }
  ],
  "pred_triples": []
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
        "span": "The drone strike"
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
      "cause": "the injury",
      "effect": "enough discomfort"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the injury and muscle spasm"
      },
      "relation": "caused",
      "effect": {
        "span": "discomfort"
      }
    }
  ]
}
```

### --- id=106 ---

输入文本: Four of the entrapments resulted in suffocation: a 7-month-old in Gouverneur, N.Y.; a 7-month-old in New Iberia, La.; a 6-month-old in Summersville, W.Va.; and a 9-month-old in Bronx, N.Y.

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
      "cause": "the entrapments",
      "effect": "suffocation"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "deaths"
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
      "cause": "this staring effect",
      "effect": "Eye discomfort"
    }
  ],
  "pred_triples": [
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

### --- id=175 ---

输入文本: The presentation generated debate and there was general discussion on how journalists can better equip themselves to handle the challenges.

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
      "cause": "The presentation",
      "effect": "debate"
    }
  ],
  "pred_triples": []
}
```

### --- id=182 ---

输入文本: Germs are microscopic organisms that cause sickness or disease.

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
      "cause": "Germs",
      "effect": "sickness"
    },
    {
      "cause": "Germs",
      "effect": "disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Germs"
      },
      "relation": "caused",
      "effect": {
        "span": "sickness or disease"
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
    "fp": 3,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 3,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 3,
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
        "span": "stress"
      },
      "relation": "caused",
      "effect": {
        "span": "losing hair"
      }
    },
    {
      "cause": {
        "span": "losing hair"
      },
      "relation": "caused",
      "effect": {
        "span": "hair stops growing"
      }
    },
    {
      "cause": {
        "span": "losing hair"
      },
      "relation": "caused",
      "effect": {
        "span": "lies dormant"
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
        "span": "the discomfort"
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

### --- id=243 ---

输入文本: Seniors get much joy from animals.

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
      "cause": "animals",
      "effect": "much joy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "animals"
      },
      "relation": "caused",
      "effect": {
        "span": "joy"
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
        "span": "abnormal build-up of fluid"
      },
      "relation": "caused",
      "effect": {
        "span": "swelling"
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
      "cause": "The malfunctions",
      "effect": "delays"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The malfunctions"
      },
      "relation": "caused",
      "effect": {
        "span": "delays"
      }
    },
    {
      "cause": {
        "span": "The malfunctions"
      },
      "relation": "caused",
      "effect": {
        "span": "access"
      }
    }
  ]
}
```

### --- id=325 ---

输入文本: The disruption caused by the latest Christmas terrorist has added too much to the weary trip home.

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
      "cause": "the latest Christmas terrorist",
      "effect": "The disruption"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "patient deaths"
      }
    },
    {
      "cause": {
        "span": "complications"
      },
      "relation": "caused",
      "effect": {
        "span": "a serious injury"
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

### --- id=367 ---

输入文本: As the molten metal cools, it hardens and assumes the shape created by the mold's cavity.

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
      "cause": "the mold's cavity",
      "effect": "the shape"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "damage"
      }
    }
  ]
}
```

### --- id=399 ---

输入文本: The problem comes from the widgets resembling HTC's own Sense UI widgets.

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
      "cause": "the widgets",
      "effect": "The problem"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "rash"
      }
    },
    {
      "cause": {
        "span": "cleaners"
      },
      "relation": "caused",
      "effect": {
        "span": "a burning sensation"
      }
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
      "relation": "caused",
      "effect": {
        "span": "neck tension"
      }
    },
    {
      "cause": {
        "span": "such an event"
      },
      "relation": "caused",
      "effect": {
        "span": "long-term increase of neck tension"
      }
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
        "span": "60 percent of Fiji's sugar cane crop"
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

### --- id=524 ---

输入文本: Sip the tea slowly to reduce stomach pain from indigestion, bloating and feeling of fullness.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "indigestion",
      "effect": "stomach pain"
    },
    {
      "cause": "bloating",
      "effect": "stomach pain"
    },
    {
      "cause": "feeling",
      "effect": "stomach pain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "indigestion"
      },
      "relation": "caused",
      "effect": {
        "span": "stomach pain"
      }
    },
    {
      "cause": {
        "span": "indigestion"
      },
      "relation": "caused",
      "effect": {
        "span": "bloating"
      }
    },
    {
      "cause": {
        "span": "indigestion"
      },
      "relation": "caused",
      "effect": {
        "span": "feeling of fullness"
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

### --- id=536 ---

输入文本: Discussion ensued from the Florida contingent on the fact that very stringent landowner protection laws in Florida make it imperative that the highest supportable appraised vallue be offered first.

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
      "cause": "the Florida contingent",
      "effect": "Discussion"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "nosebleeds"
      }
    },
    {
      "cause": {
        "span": "Dry air, dust and wind"
      },
      "relation": "caused",
      "effect": {
        "span": "coughing"
      }
    },
    {
      "cause": {
        "span": "Dry air, dust and wind"
      },
      "relation": "caused",
      "effect": {
        "span": "wheezing"
      }
    },
    {
      "cause": {
        "span": "Dry air, dust and wind"
      },
      "relation": "caused",
      "effect": {
        "span": "other short-term respiratory problems"
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
        "span": "poverty"
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
      "cause": "The clock",
      "effect": "a loud chime"
    }
  ],
  "pred_triples": []
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
      "cause": "Various hormonal, bacterial and inflammatory disturbances",
      "effect": "acne"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "hormonal, bacterial and inflammatory disturbances"
      },
      "relation": "caused",
      "effect": {
        "span": "acne"
      }
    }
  ]
}
```

### --- id=581 ---

输入文本: After the war, as the Midway was preparing for retirement, she was called upon one last time to the Philippines to help with an evacuation after the eruption of Mt. Pinatubo.

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
      "cause": "the eruption",
      "effect": "an evacuation"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "sickness"
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
    "tp": 4,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 3,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 4,
    "fp": 0,
    "fn": 0
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
      "relation": "caused",
      "effect": {
        "span": "smog"
      }
    },
    {
      "cause": {
        "span": "a pollutant"
      },
      "relation": "caused",
      "effect": {
        "span": "acid rain"
      }
    },
    {
      "cause": {
        "span": "a pollutant"
      },
      "relation": "caused",
      "effect": {
        "span": "asthma attacks"
      }
    },
    {
      "cause": {
        "span": "a pollutant"
      },
      "relation": "caused",
      "effect": {
        "span": "breathing problems"
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
      "relation": "caused",
      "effect": {
        "span": "suicide"
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
      "cause": "the quake",
      "effect": "a fire"
    }
  ],
  "pred_triples": []
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
      "relation": "caused",
      "effect": {
        "span": "The damages"
      }
    },
    {
      "cause": {
        "span": "tremors"
      },
      "relation": "caused",
      "effect": {
        "span": "The damages"
      }
    },
    {
      "cause": {
        "span": "subsidence"
      },
      "relation": "caused",
      "effect": {
        "span": "The damages"
      }
    },
    {
      "cause": {
        "span": "superficial or underground water"
      },
      "relation": "caused",
      "effect": {
        "span": "The damages"
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
        "span": "the asteroid"
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
      "cause": "animal factories",
      "effect": "The pollution"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "pollution"
      },
      "relation": "caused",
      "effect": {
        "span": "destroying parts of the world's oceans"
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
        "span": "the stress on the kidneys"
      }
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
      "relation": "caused",
      "effect": {
        "span": "grief"
      }
    }
  ]
}
```

### --- id=763 ---

输入文本: Thus, evaluating capital punishment as a form of retribution is reduced by Sellin to merely estimating the proportion of capital murders that result in execution.

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
      "cause": "capital murders",
      "effect": "execution"
    }
  ],
  "pred_triples": []
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
        "span": "taking antibiotics"
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
