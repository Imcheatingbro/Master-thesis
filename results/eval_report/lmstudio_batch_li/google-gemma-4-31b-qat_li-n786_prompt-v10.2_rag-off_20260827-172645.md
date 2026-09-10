# Gemma 4 31B QAT Li full dataset eval report

## 配置
```json
{
  "label": "Gemma 4 31B QAT Li full dataset",
  "model": "google/gemma-4-31b-qat",
  "dataset": "li",
  "sample_count": 786,
  "prompt_name": "v10.2",
  "use_rag": false,
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
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ Gemma 4 31B QAT Li full dataset final report ================
样本总数: 786
  Gold 含因果: 191 | Pred 含因果: 176
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.966
  Precision: 0.966
  Recall   : 0.890
  F1       : 0.926
  (TP=170, TN=589, FP=6, FN=21)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 786
    Gold triples: 296 | Pred triples: 290
    Precision: 0.545
    Recall   : 0.534
    F1       : 0.539
    (TP=158, FP=132, FN=138)
  [anchor_window] (primary)
    样本数: 786
    Gold triples: 296 | Pred triples: 290
    Precision: 0.866
    Recall   : 0.848
    F1       : 0.857
    (TP=251, FP=39, FN=45)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 170
    Gold triples: 272 | Pred triples: 284
    Precision: 0.556
    Recall   : 0.581
    F1       : 0.568
    (TP=158, FP=126, FN=114)
  [anchor_window] (primary)
    样本数: 170
    Gold triples: 272 | Pred triples: 284
    Precision: 0.884
    Recall   : 0.923
    F1       : 0.903
    (TP=251, FP=33, FN=21)
================================================
```

## 生成失败统计
```json
{
  "total": 1,
  "by_type": {
    "no_json_object": 1
  },
  "samples": [
    {
      "id": 5,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    }
  ]
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

Sample details shown: all 57 wrong samples from 786 total samples.

### --- id=5 ---

输入文本: In economic terms, the ecological catastrophe caused by the Prestige oil spill is comparable with that caused by the Exxon Valdez.

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
      "cause": "the Prestige oil spill",
      "effect": "the ecological catastrophe"
    },
    {
      "cause": "the Exxon Valdez",
      "effect": "the ecological catastrophe"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
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
        "span": "the high heat-humidity"
      },
      "relation": "caused",
      "effect": {
        "span": "nausea"
      }
    },
    {
      "cause": {
        "span": "the high heat-humidity"
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
      "cause": "synaptic depression",
      "effect": "Inhibition"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "it turns on more slowly"
      },
      "relation": "caused",
      "effect": {
        "span": "acts as delayed negative feedback"
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
        "span": "enough discomfort"
      }
    },
    {
      "cause": {
        "span": "muscle spasm"
      },
      "relation": "caused",
      "effect": {
        "span": "enough discomfort"
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
      "relation": "caused",
      "effect": {
        "span": "Most deaths from the accident"
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
        "span": "you are losing hair"
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
        "span": "stress on the knee joints"
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
        "span": "a long-term increase of neck tension"
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
        "span": "factors that are ostensibly unrelated to race"
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
        "span": "it imperative that the highest supportable appraised vallue be offered first"
      }
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
        "span": "it"
      },
      "relation": "caused",
      "effect": {
        "span": "churches"
      }
    },
    {
      "cause": {
        "span": "it"
      },
      "relation": "caused",
      "effect": {
        "span": "religions"
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
        "span": "the stress on the kidneys"
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
        "span": "taking antibiotics a few times a year"
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
        "span": "a bacteria found in raw food, soil, or water"
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
