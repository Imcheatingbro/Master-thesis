# cnc_positive_rag_eval first 500 eval report

## 配置
```json
{
  "label": "cnc_positive_rag_eval first 500",
  "model": "google/gemma-4-31b-qat",
  "dataset": "cnc_positive_rag_eval",
  "sample_count": 500,
  "prompt_name": "v17",
  "use_rag": true,
  "rag_mode": "knn",
  "rag_top_k": 5,
  "temperature": 0.0,
  "max_tokens": 16384,
  "progress_every": 500,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 16384,
  "reasoning_effort": null,
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
================ cnc_positive_rag_eval first 500 final report ================
样本总数: 500
  Gold 含因果: 500 | Pred 含因果: 500
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 1.000
  Precision: 1.000
  Recall   : 1.000
  F1       : 1.000
  (TP=500, TN=0, FP=0, FN=0)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 500
    Gold triples: 651 | Pred triples: 642
    Precision: 0.628
    Recall   : 0.619
    F1       : 0.623
    (TP=403, FP=239, FN=248)
  [anchor_window]
    样本数: 500
    Gold triples: 651 | Pred triples: 642
    Precision: 0.751
    Recall   : 0.740
    F1       : 0.746
    (TP=482, FP=160, FN=169)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 500
    Gold triples: 651 | Pred triples: 642
    Precision: 0.628
    Recall   : 0.619
    F1       : 0.623
    (TP=403, FP=239, FN=248)
  [anchor_window]
    样本数: 500
    Gold triples: 651 | Pred triples: 642
    Precision: 0.751
    Recall   : 0.740
    F1       : 0.746
    (TP=482, FP=160, FN=169)
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
  "total": 8,
  "by_type": {
    "duplicate_effect_closing_brace": 8
  },
  "samples": [
    {
      "id": 2271,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 2455,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 3045,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 2624,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 790,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 2116,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 1474,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 2587,
      "repair_type": "duplicate_effect_closing_brace"
    }
  ]
}
```

## 样本明细

Sample details shown: all 176 wrong samples from 500 total samples.

### --- id=1427 ---

输入文本: 12th March 2009 03:09 AM HYDERABAD : Expressing sympathy to the family members of Special Police Officer ( SPO ) K Subrahmanyam Raju who died in the attack on Gandhi Bhavan by MRPS activists recently , Pradesh Congress Committee president D Srinivas today announced an ex gratia of Rs 10 lakh to the bereaved family .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "the attack on Gandhi Bhavan by MRPS activists recently",
      "effect": "Special Police Officer ( SPO ) K Subrahmanyam Raju who died"
    },
    {
      "cause": "Expressing sympathy to the family members of Special Police Officer ( SPO ) K Subrahmanyam Raju who died in the attack on Gandhi Bhavan by MRPS activists recently",
      "effect": "Pradesh Congress Committee president D Srinivas today announced an ex gratia of Rs 10 lakh to the bereaved family"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the attack on Gandhi Bhavan by MRPS activists recently"
      },
      "relation": "caused",
      "effect": {
        "span": "Special Police Officer ( SPO ) K Subrahmanyam Raju who died"
      }
    },
    {
      "cause": {
        "span": "Special Police Officer ( SPO ) K Subrahmanyam Raju who died in the attack on Gandhi Bhavan by MRPS activists recently"
      },
      "relation": "caused",
      "effect": {
        "span": "Pradesh Congress Committee president D Srinivas today announced an ex gratia of Rs 10 lakh to the bereaved family"
      }
    }
  ]
}
```

### --- id=823 ---

输入文本: Thousands of heavily armed troops have paraded through cities in China ’ s troubled far west with officials there vowing a “ thunderous ” anti-terror crackdown after an apparent upsurge in deadly ethnic violence .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "an apparent upsurge in deadly ethnic violence",
      "effect": "Thousands of heavily armed troops have paraded through cities in China ’ s troubled far west with officials there vowing a “ thunderous ” anti-terror crackdown"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an apparent upsurge in deadly ethnic violence"
      },
      "relation": "caused",
      "effect": {
        "span": "officials there vowing a “ thunderous ” anti-terror crackdown"
      }
    },
    {
      "cause": {
        "span": "an apparent upsurge in deadly ethnic violence"
      },
      "relation": "caused",
      "effect": {
        "span": "Thousands of heavily armed troops have paraded through cities in China ’ s troubled far west"
      }
    }
  ]
}
```

### --- id=2465 ---

输入文本: Association leader Benny said that their members who availed themselves of casual leave on Wednesday as a mark of protest , would continue to boycott duties and organise a 24 - hour satyagraha before the Secretariat on February 20 .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "a mark of protest",
      "effect": "their members who availed themselves of casual leave on Wednesday"
    },
    {
      "cause": "would continue to boycott duties and organise a 24 - hour satyagraha before the Secretariat on February 20",
      "effect": "a mark of protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "as a mark of protest"
      },
      "relation": "caused",
      "effect": {
        "span": "their members who availed themselves of casual leave on Wednesday"
      }
    }
  ]
}
```

### --- id=347 ---

输入文本: But the caste violence that wrecked the lives of over a thousand Dalits earlier this month has forever tainted the image of Dharmapuri district as a former Naxal stronghold that , even a decade ago , had no place for caste or class differences .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the caste violence",
      "effect": "wrecked the lives of over a thousand Dalits earlier this month"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the caste violence that wrecked the lives of over a thousand Dalits earlier this month"
      },
      "relation": "caused",
      "effect": {
        "span": "has forever tainted the image of Dharmapuri district as a former Naxal stronghold that , even a decade ago , had no place for caste or class differences ."
      }
    }
  ]
}
```

### --- id=7 ---

输入文本: Protesters are angry at the police ’ s slow response to the attack in Yuen Long and their pursuit of the case .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "the police ’ s slow response to the attack in Yuen Long and their pursuit of the case",
      "effect": "Protesters are angry"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the police ’ s slow response to the attack in Yuen Long"
      },
      "relation": "caused",
      "effect": {
        "span": "Protesters are angry"
      }
    },
    {
      "cause": {
        "span": "their pursuit of the case"
      },
      "relation": "caused",
      "effect": {
        "span": "Protesters are angry"
      }
    }
  ]
}
```

### --- id=471 ---

输入文本: Police statistics say 16 extremists died in 18 exchanges of fire in just the six weeks from 14 December 2004 .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "18 exchanges of fire in just the six weeks from 14 December 2004",
      "effect": "16 extremists died"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "18 exchanges of fire"
      },
      "relation": "caused",
      "effect": {
        "span": "Police statistics say 16 extremists died"
      }
    }
  ]
}
```

### --- id=1290 ---

输入文本: The 1966 riots , which were prompted by a 50 per cent increase in cross-harbour ferry fares , took place against the backdrop of a bad economy and widening gap between the government and the people .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "a 50 per cent increase in cross-harbour ferry fares",
      "effect": "The 1966 riots"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a 50 per cent increase in cross-harbour ferry fares"
      },
      "relation": "caused",
      "effect": {
        "span": "The 1966 riots"
      }
    },
    {
      "cause": {
        "span": "against the backdrop of a bad economy and widening gap between the government and the people"
      },
      "relation": "caused",
      "effect": {
        "span": "The 1966 riots , which were prompted by a 50 per cent increase in cross-harbour ferry fares , took place"
      }
    }
  ]
}
```

### --- id=2447 ---

输入文本: Party Vice-President Ram Kishore Singh threatened to “ put him ( Modi ) behind bars ” , because following the Muzaffarnagar riots , the state government had received IB alerts on possible communal unrest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the state government had received IB alerts on possible communal unrest",
      "effect": "Party Vice-President Ram Kishore Singh threatened to “ put him ( Modi ) behind bars"
    },
    {
      "cause": "the Muzaffarnagar riots",
      "effect": "the state government had received IB alerts on possible communal unrest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "following the Muzaffarnagar riots , the state government had received IB alerts on possible communal unrest"
      },
      "relation": "caused",
      "effect": {
        "span": "Party Vice-President Ram Kishore Singh threatened to “ put him ( Modi ) behind bars ”"
      }
    }
  ]
}
```

### --- id=308 ---

输入文本: Some police personnel intervened and urged them to give up their protest - but to no avail .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Some police personnel intervened",
      "effect": "urged them to give up their protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to give up their protest"
      },
      "relation": "caused",
      "effect": {
        "span": "Some police personnel intervened and urged them"
      }
    }
  ]
}
```

### --- id=1442 ---

输入文本: While the Congress members walked out in protest , the BJP members continued the dharna in the Well till the House was adjourned for the day after the presentation of the Budget .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "in protest",
      "effect": "the Congress members walked out"
    },
    {
      "cause": "the House was adjourned for the day after the presentation of the Budget",
      "effect": "the BJP members continued the dharna in the Well"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest"
      },
      "relation": "caused",
      "effect": {
        "span": "the Congress members walked out"
      }
    },
    {
      "cause": {
        "span": "after the presentation of the Budget"
      },
      "relation": "caused",
      "effect": {
        "span": "the House was adjourned for the day"
      }
    }
  ]
}
```

### --- id=1059 ---

输入文本: MYSURU : Tension prevails as Falcon Tyres employees block KRS Road March 03 , 2016 00:00 IST Tension prevailed on the KRS Road for sometime on Wednesday after scores of Falcon Tyres employees staged a demonstration against the factory management demanding immediate settlement of their pending wages .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Falcon Tyres employees block KRS Road",
      "effect": "Tension prevails"
    },
    {
      "cause": "scores of Falcon Tyres employees staged a demonstration against the factory management",
      "effect": "Tension prevailed on the KRS Road for sometime on Wednesday"
    },
    {
      "cause": "demanding immediate settlement of their pending wages",
      "effect": "scores of Falcon Tyres employees staged a demonstration against the factory management"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "scores of Falcon Tyres employees staged a demonstration against the factory management demanding immediate settlement of their pending wages"
      },
      "relation": "caused",
      "effect": {
        "span": "Tension prevailed on the KRS Road for sometime on Wednesday"
      }
    },
    {
      "cause": {
        "span": "demanding immediate settlement of their pending wages"
      },
      "relation": "caused",
      "effect": {
        "span": "scores of Falcon Tyres employees staged a demonstration against the factory management"
      }
    }
  ]
}
```

### --- id=1163 ---

输入文本: The party was protesting the arrest of its president N. Chandrababu Naidu and other leaders by Maharashtra police when they tried to visit Babli project .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the arrest of its president N. Chandrababu Naidu and other leaders by Maharashtra police",
      "effect": "The party was protesting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the arrest of its president N. Chandrababu Naidu and other leaders by Maharashtra police"
      },
      "relation": "caused",
      "effect": {
        "span": "The party was protesting"
      }
    },
    {
      "cause": {
        "span": "when they tried to visit Babli project"
      },
      "relation": "caused",
      "effect": {
        "span": "The party was protesting the arrest of its president N. Chandrababu Naidu and other leaders by Maharashtra police"
      }
    }
  ]
}
```

### --- id=2450 ---

输入文本: They alleged that the police tried to intimidate religious leaders and pressured them to withdraw the bandh call and had issued notices to them saying that if there was any untoward incident during the bandh they would be held responsible for it .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "there was any untoward incident during the bandh",
      "effect": "they would be held responsible for it"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to withdraw the bandh call"
      },
      "relation": "caused",
      "effect": {
        "span": "They alleged that the police tried to intimidate religious leaders and pressured them"
      }
    },
    {
      "cause": {
        "span": "if there was any untoward incident during the bandh"
      },
      "relation": "caused",
      "effect": {
        "span": "they would be held responsible for it"
      }
    }
  ]
}
```

### --- id=1369 ---

输入文本: On New Year 's Day , seven days after Qian 's death , thousands of residents of surrounding villages gathered to mourn but were stopped by hundreds of police .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to mourn",
      "effect": "thousands of residents of surrounding villages gathered"
    },
    {
      "cause": "On New Year 's Day , seven days after Qian 's death",
      "effect": "to mourn"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to mourn"
      },
      "relation": "caused",
      "effect": {
        "span": "thousands of residents of surrounding villages gathered"
      }
    },
    {
      "cause": {
        "span": "after Qian 's death"
      },
      "relation": "caused",
      "effect": {
        "span": "thousands of residents of surrounding villages gathered to mourn but were stopped by hundreds of police ."
      }
    }
  ]
}
```

### --- id=2790 ---

输入文本: `` In recent weeks , residents invaded land in the area and to curb the mushrooming of structures on the land , the municipality obtained a court order to remove the land invaders .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to curb the mushrooming of structures on the land",
      "effect": "the municipality obtained a court order to remove the land invaders"
    },
    {
      "cause": "to remove the land invaders",
      "effect": "the municipality obtained a court order"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "residents invaded land in the area"
      },
      "relation": "caused",
      "effect": {
        "span": "the municipality obtained a court order to remove the land invaders"
      }
    },
    {
      "cause": {
        "span": "to curb the mushrooming of structures on the land"
      },
      "relation": "caused",
      "effect": {
        "span": "the municipality obtained a court order to remove the land invaders"
      }
    }
  ]
}
```

### --- id=612 ---

输入文本: Maruti 's Manesar plant closed for 2nd day - Indian Express Agencies , Agencies : Manesar , Fri Jul 20 2012 , 11:11 hrs Maruti Suzuki India Friday said its plant was remain closed for the second day after the violence on Wednesday in which one senior company official was killed .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the violence on Wednesday in which one senior company official was killed",
      "effect": "its plant was remain closed for the second day"
    },
    {
      "cause": "the violence on Wednesday",
      "effect": "one senior company official was killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after the violence on Wednesday in which one senior company official was killed"
      },
      "relation": "caused",
      "effect": {
        "span": "Maruti Suzuki India Friday said its plant was remain closed for the second day"
      }
    }
  ]
}
```

### --- id=2127 ---

输入文本: When we got up to go home the police acted violently towards us even though our protest was peaceful .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to go home",
      "effect": "we got up"
    },
    {
      "cause": "we got up",
      "effect": "the police acted violently towards us"
    },
    {
      "cause": "our protest was peaceful",
      "effect": "the police acted violently towards us"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "When we got up to go home"
      },
      "relation": "caused",
      "effect": {
        "span": "the police acted violently towards us"
      }
    }
  ]
}
```

### --- id=150 ---

输入文本: “ If peaceful marches that disrupt the road for an afternoon or so don ’ t work , maybe it spills over to blockading more roads , maybe for long .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "peaceful marches",
      "effect": "that disrupt the road for an afternoon or so"
    },
    {
      "cause": "peaceful marches that disrupt the road for an afternoon or so don ’ t work",
      "effect": "maybe it spills over to blockading more roads , maybe for long"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "peaceful marches that disrupt the road for an afternoon or so don ’ t work"
      },
      "relation": "caused",
      "effect": {
        "span": "maybe it spills over to blockading more roads , maybe for long ."
      }
    }
  ]
}
```

### --- id=2563 ---

输入文本: Will the unprecedented protests embolden them to fight for their beliefs in future , or convince them that resistance to Beijing ’ s will is futile ?

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the unprecedented protests",
      "effect": "embolden them to fight for their beliefs in future , or convince them that resistance to Beijing ’ s will is futile"
    },
    {
      "cause": "their beliefs in future",
      "effect": "embolden them to fight"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the unprecedented protests"
      },
      "relation": "caused",
      "effect": {
        "span": "embolden them to fight for their beliefs in future"
      }
    },
    {
      "cause": {
        "span": "the unprecedented protests"
      },
      "relation": "caused",
      "effect": {
        "span": "convince them that resistance to Beijing ’ s will is futile"
      }
    },
    {
      "cause": {
        "span": "to fight for their beliefs in future"
      },
      "relation": "caused",
      "effect": {
        "span": "embolden them"
      }
    },
    {
      "cause": {
        "span": "that resistance to Beijing ’ s will is futile"
      },
      "relation": "caused",
      "effect": {
        "span": "convince them"
      }
    }
  ]
}
```

### --- id=2557 ---

输入文本: Fasting Jagan denied mulakats 27th August 2013 11:23 AM The indefinite fast of YSR Congress chief YS Jaganmohan Reddy in protest against state division continued on the second day on Monday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against state division",
      "effect": "The indefinite fast of YSR Congress chief YS Jaganmohan Reddy in protest"
    },
    {
      "cause": "protest against state division",
      "effect": "The indefinite fast of YSR Congress chief YS Jaganmohan Reddy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against state division"
      },
      "relation": "caused",
      "effect": {
        "span": "The indefinite fast of YSR Congress chief YS Jaganmohan Reddy"
      }
    }
  ]
}
```

### --- id=2763 ---

输入文本: She claimed that the police showed maximum restraint but lost temper when some of their colleagues got hurt during the stone-pelting and rataliated .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "and rataliated",
      "effect": "She claimed that the police showed maximum restraint but lost temper when some of their colleagues got hurt during the stone-pelting"
    },
    {
      "cause": "some of their colleagues got hurt",
      "effect": "lost temper"
    },
    {
      "cause": "the stone-pelting",
      "effect": "some of their colleagues got hurt"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when some of their colleagues got hurt during the stone-pelting"
      },
      "relation": "caused",
      "effect": {
        "span": "the police showed maximum restraint but lost temper"
      }
    },
    {
      "cause": {
        "span": "when some of their colleagues got hurt during the stone-pelting"
      },
      "relation": "caused",
      "effect": {
        "span": "rataliated"
      }
    }
  ]
}
```

### --- id=27 ---

输入文本: Akram was on the radar of the National Investigation Agency ( NIA ) as he is believed to have arranged explosives and planter for the blast .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "he is believed to have arranged explosives and planter for the blast",
      "effect": "Akram was on the radar of the National Investigation Agency ( NIA )"
    },
    {
      "cause": "the blast",
      "effect": "arranged explosives and planter"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he is believed to have arranged explosives and planter for the blast"
      },
      "relation": "caused",
      "effect": {
        "span": "Akram was on the radar of the National Investigation Agency ( NIA )"
      }
    }
  ]
}
```

### --- id=1826 ---

输入文本: Simon Blore , director , Leadarchitects Limited Angered by anti-Occupy Central march I have followed with dismay the all-too apparent manipulation of gullible people being fed propaganda by pro-Beijing loyalists about the Occupy Central initiative for a freer election process .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "anti-Occupy Central march",
      "effect": "Angered"
    },
    {
      "cause": "Angered by anti-Occupy Central march",
      "effect": "I have followed with dismay the all-too apparent manipulation of gullible people being fed propaganda by pro-Beijing loyalists about the Occupy Central initiative for a freer election process"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "anti-Occupy Central march"
      },
      "relation": "caused",
      "effect": {
        "span": "Simon Blore , director , Leadarchitects Limited Angered"
      }
    }
  ]
}
```

### --- id=1253 ---

输入文本: Militants fired a rocket at the headquarters of 84th battalion of BSF in Sopore in North Kashmir late last night which missed its target and caused no loss of life or damage to property , police said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Militants fired a rocket at the headquarters of 84th battalion of BSF in Sopore in North Kashmir late last night which missed its target",
      "effect": "no loss of life or damage to property"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Militants fired a rocket at the headquarters of 84th battalion of BSF in Sopore in North Kashmir late last night"
      },
      "relation": "caused",
      "effect": {
        "span": "which missed its target and caused no loss of life or damage to property"
      }
    }
  ]
}
```

### --- id=2567 ---

输入文本: Millions on the mainland took part in the pro-reform protests of 1989 which began in Tiananmen Square , but after the bloody crackdown , fear and economic inducements ensured they turned away from politics .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "fear and economic inducements",
      "effect": "they turned away from politics"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after the bloody crackdown"
      },
      "relation": "caused",
      "effect": {
        "span": "fear and economic inducements ensured they turned away from politics ."
      }
    }
  ]
}
```

### --- id=2878 ---

输入文本: Sena Flays CM for Keeping Mum While Vidarbha Flag Was Hoisted 03rd May 2016 04:32 PM MUMBAI : Ruling alliance partner Shiv Sena today flayed Maharashtra Chief Minister Devendra Fadnavis for keeping mum when a flag of a separate Vidarbha state was recently hoisted in Nagpur on Maharashtra Day .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Keeping Mum While Vidarbha Flag Was Hoisted",
      "effect": "Sena Flays CM"
    },
    {
      "cause": "keeping mum when a flag of a separate Vidarbha state was recently hoisted in Nagpur on Maharashtra Day",
      "effect": "Ruling alliance partner Shiv Sena today flayed Maharashtra Chief Minister Devendra Fadnavis"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "keeping mum when a flag of a separate Vidarbha state was recently hoisted in Nagpur on Maharashtra Day"
      },
      "relation": "caused",
      "effect": {
        "span": "Ruling alliance partner Shiv Sena today flayed Maharashtra Chief Minister Devendra Fadnavis"
      }
    }
  ]
}
```

### --- id=2999 ---

输入文本: Wild , irresponsible and most unfounded allegations , by certain sections of the Sikh community , about my involvement in the inciting of violence against them during the most unfortunate Sikh riots of 1984 , soon after the death of Shrimati Indira Gandhi , the then prime minister of India , has caused me acute agony .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Wild , irresponsible and most unfounded allegations , by certain sections of the Sikh community , about my involvement in the inciting of violence against them during the most unfortunate Sikh riots of 1984 , soon after the death of Shrimati Indira Gandhi , the then prime minister of India",
      "effect": "has caused me acute agony"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Wild , irresponsible and most unfounded allegations , by certain sections of the Sikh community , about my involvement in the inciting of violence against them during the most unfortunate Sikh riots of 1984 , soon after the death of Shrimati Indira Gandhi , the then prime minister of India"
      },
      "relation": "caused",
      "effect": {
        "span": "has caused me acute agony ."
      }
    },
    {
      "cause": {
        "span": "the death of Shrimati Indira Gandhi , the then prime minister of India"
      },
      "relation": "caused",
      "effect": {
        "span": "the most unfortunate Sikh riots of 1984"
      }
    }
  ]
}
```

### --- id=2751 ---

输入文本: Striking workers will not return to work unless health workers who were fired for taking part in salary protest actions are reinstated , the National Education , Health and Allied Workers Union ( Nehawu ) said in Bloemfontein on Wednesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "health workers who were fired for taking part in salary protest actions are reinstated",
      "effect": "Striking workers will not return to work"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "taking part in salary protest actions"
      },
      "relation": "caused",
      "effect": {
        "span": "health workers who were fired"
      }
    },
    {
      "cause": {
        "span": "unless health workers who were fired for taking part in salary protest actions are reinstated"
      },
      "relation": "caused",
      "effect": {
        "span": "Striking workers will not return to work"
      }
    }
  ]
}
```

### --- id=2611 ---

输入文本: " Based on specific inputs , security forces cordoned off a house and that resulted in an encounter with the militant first opening fire on the security team , " Kokrajhar police chief P.K. Dutta said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "security forces cordoned off a house",
      "effect": "an encounter with the militant first opening fire on the security team"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Based on specific inputs"
      },
      "relation": "caused",
      "effect": {
        "span": "security forces cordoned off a house"
      }
    },
    {
      "cause": {
        "span": "security forces cordoned off a house"
      },
      "relation": "caused",
      "effect": {
        "span": "that resulted in an encounter with the militant first opening fire on the security team"
      }
    }
  ]
}
```

### --- id=1988 ---

输入文本: KERALA Private bus strike total in city August 14 , 2008 00:00 IST DIFFICULT RIDE : Commuters had a hard time on the first day of the private bus strike in the city on Wednesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the private bus strike in the city on Wednesday",
      "effect": "Commuters had a hard time on the first day"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the first day of the private bus strike in the city on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "Commuters had a hard time"
      }
    }
  ]
}
```

### --- id=1367 ---

输入文本: ' He refused a two million ( HK $ 2.34 million ) yuan bribe and pretty girls offered by authorities who wanted him to stop petitioning , ' said another villager .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "who wanted him to stop petitioning",
      "effect": "a two million ( HK $ 2.34 million ) yuan bribe and pretty girls offered by authorities"
    },
    {
      "cause": "authorities who wanted him to stop petitioning",
      "effect": "a two million ( HK $ 2.34 million ) yuan bribe and pretty girls offered"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "who wanted him to stop petitioning"
      },
      "relation": "caused",
      "effect": {
        "span": "authorities who wanted him to stop petitioning"
      }
    },
    {
      "cause": {
        "span": "to stop petitioning"
      },
      "relation": "caused",
      "effect": {
        "span": "authorities who wanted him to stop petitioning"
      }
    }
  ]
}
```

### --- id=2455 ---

输入文本: In reply to the argument of the defence counsel that the UDF used the murder of Chandrasekharan for political gain by blaming CPM for the killing , Rema told the court that this was not right .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "political gain by blaming CPM for the killing",
      "effect": "the UDF used the murder of Chandrasekharan"
    },
    {
      "cause": "the UDF used the murder of Chandrasekharan for political gain",
      "effect": "blaming CPM for the killing"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the argument of the defence counsel that the UDF used the murder of Chandrasekharan for political gain by blaming CPM for the killing"
      },
      "relation": "caused",
      "effect": {
        "span": "Rema told the court that this was not right ."
      }
    },
    {
      "cause": {
        "span": "blaming CPM for the killing"
      },
      "relation": "caused",
      "effect": {
        "span": "the UDF used the murder of Chandrasekharan for political gain"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=2377 ---

输入文本: The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday to condemn what it called a “ concerted attack on Hindu leaders in the state . ” Ramesh , the state BJP unit ’ s general secretary and a charted accountant by profession , was murdered by assailants in Salem while he was on his way back home after visiting the party office on Friday evening .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to condemn what it called a “ concerted attack on Hindu leaders in the state",
      "effect": "The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday"
    },
    {
      "cause": "visiting the party office on Friday evening",
      "effect": "he was on his way back home"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to condemn what it called a “ concerted attack on Hindu leaders in the state . ”"
      },
      "relation": "caused",
      "effect": {
        "span": "The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday"
      }
    },
    {
      "cause": {
        "span": "assailants in Salem"
      },
      "relation": "caused",
      "effect": {
        "span": "Ramesh , the state BJP unit ’ s general secretary and a charted accountant by profession , was murdered"
      }
    }
  ]
}
```

### --- id=676 ---

输入文本: The enthusiastic plans of the freedom fighters , satyagrahis , revolutionaries and soldiers for grand celebrations began to ebb right after the Mumbai attacks , with Subhash Chandra Bose and Bhagat Singh leading the agitation to boycott the celebrations .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Subhash Chandra Bose and Bhagat Singh leading the agitation to boycott the celebrations",
      "effect": "The enthusiastic plans of the freedom fighters , satyagrahis , revolutionaries and soldiers for grand celebrations began to ebb right after the Mumbai attacks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Mumbai attacks"
      },
      "relation": "caused",
      "effect": {
        "span": "The enthusiastic plans of the freedom fighters , satyagrahis , revolutionaries and soldiers for grand celebrations began to ebb"
      }
    },
    {
      "cause": {
        "span": "to boycott the celebrations"
      },
      "relation": "caused",
      "effect": {
        "span": "Subhash Chandra Bose and Bhagat Singh leading the agitation"
      }
    }
  ]
}
```

### --- id=2712 ---

输入文本: The protesters – many of whom were wearing black T-shirts and hard hats and were armed with shields made from boards of wood and surfboards , as well as hiking sticks and rods – retaliated by throwing umbrellas and water bottles .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "throwing umbrellas and water bottles",
      "effect": "The protesters – many of whom were wearing black T-shirts and hard hats and were armed with shields made from boards of wood and surfboards , as well as hiking sticks and rods – retaliated"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The protesters – many of whom were wearing black T-shirts and hard hats and were armed with shields made from boards of wood and surfboards , as well as hiking sticks and rods – retaliated"
      },
      "relation": "caused",
      "effect": {
        "span": "by throwing umbrellas and water bottles ."
      }
    }
  ]
}
```

### --- id=2718 ---

输入文本: Hong Kong ’ s hospital authority said 17 people had been hospitalised following the clashes , including two who were in serious condition .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the clashes",
      "effect": "17 people had been hospitalised"
    },
    {
      "cause": "the clashes",
      "effect": "including two who were in serious condition"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "following the clashes"
      },
      "relation": "caused",
      "effect": {
        "span": "Hong Kong ’ s hospital authority said 17 people had been hospitalised"
      }
    }
  ]
}
```

### --- id=1817 ---

输入文本: Five people died on the spot in the second blast and over 50 were injured , several critically .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "the second blast",
      "effect": "Five people died on the spot"
    },
    {
      "cause": "the second blast",
      "effect": "and over 50 were injured , several critically"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in the second blast"
      },
      "relation": "caused",
      "effect": {
        "span": "Five people died on the spot"
      }
    },
    {
      "cause": {
        "span": "in the second blast"
      },
      "relation": "caused",
      "effect": {
        "span": "over 50 were injured , several critically ."
      }
    }
  ]
}
```

### --- id=302 ---

输入文本: More violence in TN district Posted : Wed Jun 25 1997 IST RAJAPALAYAM , June 23 : In continuing violence in TN 's Kamarajar district , one person was stabbed and buses being attacked .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "In continuing violence in TN 's Kamarajar district",
      "effect": "one person was stabbed and buses being attacked"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "continuing violence in TN 's Kamarajar district"
      },
      "relation": "caused",
      "effect": {
        "span": "one person was stabbed and buses being attacked ."
      }
    }
  ]
}
```

### --- id=1062 ---

输入文本: Later in the day , the entire opposition - TDP , CPI , CPI(M) and PDF staged a walk out when government turned down their demand to adopt a resolution urging Centre to withdraw recent hike in fuel prices and the decision on deregulation of petrol .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "government turned down their demand to adopt a resolution urging Centre to withdraw recent hike in fuel prices and the decision on deregulation of petrol",
      "effect": "the entire opposition - TDP , CPI , CPI(M) and PDF staged a walk out"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when government turned down their demand to adopt a resolution urging Centre to withdraw recent hike in fuel prices and the decision on deregulation of petrol"
      },
      "relation": "caused",
      "effect": {
        "span": "the entire opposition - TDP , CPI , CPI(M) and PDF staged a walk out"
      }
    },
    {
      "cause": {
        "span": "to adopt a resolution urging Centre to withdraw recent hike in fuel prices and the decision on deregulation of petrol"
      },
      "relation": "caused",
      "effect": {
        "span": "their demand"
      }
    }
  ]
}
```

### --- id=2384 ---

输入文本: These attacks and killings may be aimed at instilling fear in the minds of the people in general and of our party workers in particular , ” the statement read and demanded a Special Investigation Team to go into each of the incidents .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "may be aimed at instilling fear in the minds of the people in general and of our party workers in particular",
      "effect": "These attacks and killings"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to instilling fear in the minds of the people in general and of our party workers in particular"
      },
      "relation": "caused",
      "effect": {
        "span": "These attacks and killings may be aimed"
      }
    },
    {
      "cause": {
        "span": "to go into each of the incidents"
      },
      "relation": "caused",
      "effect": {
        "span": "the statement read and demanded a Special Investigation Team"
      }
    }
  ]
}
```

### --- id=1281 ---

输入文本: Truckers put govt on notice 08th January 2009 03:57 AM CHENNAI : With the national-level truckers ’ strike called by the All-India Motor Transport Congress ( AIMTC ) demanding immediate reduction of diesel prices entering the third day on Wednesday , representatives of the striking truckers have issued an ultimatum to the government to act before Thursday midnight to resolve the issue or face severe consequences .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding immediate reduction of diesel prices",
      "effect": "the national-level truckers ’ strike called by the All-India Motor Transport Congress ( AIMTC )"
    },
    {
      "cause": "the national-level truckers ’ strike called by the All-India Motor Transport Congress ( AIMTC ) demanding immediate reduction of diesel prices entering the third day on Wednesday",
      "effect": "representatives of the striking truckers have issued an ultimatum to the government to act before Thursday midnight to resolve the issue or face severe consequences"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding immediate reduction of diesel prices"
      },
      "relation": "caused",
      "effect": {
        "span": "the national-level truckers ’ strike called by the All-India Motor Transport Congress ( AIMTC )"
      }
    },
    {
      "cause": {
        "span": "to resolve the issue"
      },
      "relation": "caused",
      "effect": {
        "span": "representatives of the striking truckers have issued an ultimatum to the government to act before Thursday midnight"
      }
    }
  ]
}
```

### --- id=2341 ---

输入文本: KARIMNAGAR : TDP rasta roko against fuel price hike June 28 , 2010 00:00 IST The TDP district unit leaders staged a rasta roko in front of the RTC bus station complex here on Sunday in protest against the fuel price hike .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against the fuel price hike",
      "effect": "The TDP district unit leaders staged a rasta roko in front of the RTC bus station complex here on Sunday in protest"
    },
    {
      "cause": "in protest against the fuel price hike",
      "effect": "The TDP district unit leaders staged a rasta roko in front of the RTC bus station complex here on Sunday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the fuel price hike"
      },
      "relation": "caused",
      "effect": {
        "span": "The TDP district unit leaders staged a rasta roko in front of the RTC bus station complex here on Sunday"
      }
    }
  ]
}
```

### --- id=1551 ---

输入文本: Upset with Probe into AIADMK Man 's Murder , Wife Stages Stir

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Probe into AIADMK Man 's Murder",
      "effect": "Upset"
    },
    {
      "cause": "Upset with Probe into AIADMK Man 's Murder",
      "effect": "Wife Stages Stir"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Upset with Probe into AIADMK Man 's Murder"
      },
      "relation": "caused",
      "effect": {
        "span": "Wife Stages Stir"
      }
    }
  ]
}
```

### --- id=1967 ---

输入文本: There was also allegation that some of the Congress workers , who came to interrupt the fest , were in an inebriated state .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "were in an inebriated state",
      "effect": "some of the Congress workers , who came to interrupt the fest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "who came to interrupt the fest"
      },
      "relation": "caused",
      "effect": {
        "span": "There was also allegation that some of the Congress workers , who came to interrupt the fest , were in an inebriated state ."
      }
    }
  ]
}
```

### --- id=3045 ---

输入文本: Muslims across the city of lakes , still haunted by memories of the 2002 Gujarat riots , say they will not vote for someone who was unable to stop a massacre of ‘ innocent people ’ in his state .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Muslims across the city of lakes , still haunted by memories of the 2002 Gujarat riots",
      "effect": "they will not vote for someone who was unable to stop a massacre of ‘ innocent people ’ in his state"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "memories of the 2002 Gujarat riots"
      },
      "relation": "caused",
      "effect": {
        "span": "Muslims across the city of lakes , still haunted by memories of the 2002 Gujarat riots , say they will not vote for someone who was unable to stop a massacre of ‘ innocent people ’ in his state ."
      }
    },
    {
      "cause": {
        "span": "who was unable to stop a massacre of ‘ innocent people ’ in his state"
      },
      "relation": "caused",
      "effect": {
        "span": "they will not vote for someone"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=1460 ---

输入文本: The Bhim Army and other Dalit groups were refused permission to organise a rally against atrocities on May 9 sparking off violence and vandalism , with several vehicles and buses burnt .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against atrocities on May 9",
      "effect": "organise a rally"
    },
    {
      "cause": "The Bhim Army and other Dalit groups were refused permission to organise a rally against atrocities on May 9",
      "effect": "violence and vandalism , with several vehicles and buses burnt"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The Bhim Army and other Dalit groups were refused permission to organise a rally against atrocities on May 9"
      },
      "relation": "caused",
      "effect": {
        "span": "sparking off violence and vandalism , with several vehicles and buses burnt ."
      }
    },
    {
      "cause": {
        "span": "against atrocities"
      },
      "relation": "caused",
      "effect": {
        "span": "to organise a rally"
      }
    }
  ]
}
```

### --- id=2626 ---

输入文本: Twin Bomb Blasts Injures Four in Guwahati 's Fancy Bazar Area : Police 05th December 2015 04:37 PM A screen grab of the fancy Bazaar area from Google Maps GUWAHATI : Two low intensity blasts rocked the busy commercial Fancy Bazaar area in Guwahati Saturday afternoon , injuring four persons .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Twin Bomb Blasts",
      "effect": "Injures Four in Guwahati 's Fancy Bazar Area"
    },
    {
      "cause": "Two low intensity blasts rocked the busy commercial Fancy Bazaar area in Guwahati Saturday afternoon",
      "effect": "injuring four persons"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Two low intensity blasts rocked the busy commercial Fancy Bazaar area in Guwahati Saturday afternoon"
      },
      "relation": "caused",
      "effect": {
        "span": "injuring four persons ."
      }
    }
  ]
}
```

### --- id=1570 ---

输入文本: The protests started on Tuesday , with residents demanding better service delivery and housing .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "residents demanding better service delivery and housing",
      "effect": "The protests started on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding better service delivery and housing"
      },
      "relation": "caused",
      "effect": {
        "span": "The protests started on Tuesday"
      }
    }
  ]
}
```

### --- id=181 ---

输入文本: While earlier it was the turn of Telangana Rashtra Samithi ( TRS ) to participate in protests in support to farmers , on Monday it was the Telugu Desam .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "in support to farmers",
      "effect": "Telangana Rashtra Samithi ( TRS ) to participate in protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in support to farmers"
      },
      "relation": "caused",
      "effect": {
        "span": "earlier it was the turn of Telangana Rashtra Samithi ( TRS ) to participate in protests"
      }
    },
    {
      "cause": {
        "span": "in support to farmers"
      },
      "relation": "caused",
      "effect": {
        "span": "on Monday it was the Telugu Desam"
      }
    }
  ]
}
```

### --- id=2726 ---

输入文本: The protests , which began over a controversial extradition bill , have evolved to take in other demands , including a police inquiry into the violence in Yuen Long last week .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to take in other demands",
      "effect": "The protests , which began over a controversial extradition bill , have evolved"
    },
    {
      "cause": "a controversial extradition bill",
      "effect": "The protests , which began"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over a controversial extradition bill"
      },
      "relation": "caused",
      "effect": {
        "span": "The protests"
      }
    }
  ]
}
```

### --- id=962 ---

输入文本: Christians flay Commission ’ s report 21st February 2011 04:25 AM MANGALORE : Thousands of Christians took out a silent march from Ambedkar ( Jyothi ) Circle to Nehru Maidan on Sunday by wrapping their mouth with black cloth and holding black flags to oppose Justice Somasekhara Commission ’ s report on church attacks .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to oppose Justice Somasekhara Commission ’ s report on church attacks",
      "effect": "Thousands of Christians took out a silent march from Ambedkar ( Jyothi ) Circle to Nehru Maidan on Sunday by wrapping their mouth with black cloth and holding black flags"
    },
    {
      "cause": "Thousands of Christians took out a silent march from Ambedkar ( Jyothi ) Circle to Nehru Maidan on Sunday",
      "effect": "wrapping their mouth with black cloth and holding black flags"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to oppose Justice Somasekhara Commission ’ s report on church attacks"
      },
      "relation": "caused",
      "effect": {
        "span": "Thousands of Christians took out a silent march from Ambedkar ( Jyothi ) Circle to Nehru Maidan on Sunday by wrapping their mouth with black cloth and holding black flags"
      }
    }
  ]
}
```

### --- id=1080 ---

输入文本: OPINION India ’ s Pakistan problem is Pakistan ’ s problem too December 03 , 2008 00:00 IST Siddharth Varadarajan If politics and emotion do not dictate India ’ s response , the terrorist strikes in Mumbai could be a catalyst for ending the Pakistani military ’ s fatal patronage of jihadi groups .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "politics and emotion do not dictate India ’ s response",
      "effect": "the terrorist strikes in Mumbai could be a catalyst for ending the Pakistani military ’ s fatal patronage of jihadi groups"
    },
    {
      "cause": "the terrorist strikes in Mumbai",
      "effect": "ending the Pakistani military ’ s fatal patronage of jihadi groups"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the terrorist strikes in Mumbai"
      },
      "relation": "caused",
      "effect": {
        "span": "could be a catalyst for ending the Pakistani military ’ s fatal patronage of jihadi groups"
      }
    }
  ]
}
```

### --- id=2624 ---

输入文本: " Rebels opened fire on the IAF chopper when it tried to land in a conflict zone in Sukma district to rescue a few troopers who had received gunshots in an encounter .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "it tried to land in a conflict zone in Sukma district",
      "effect": "Rebels opened fire on the IAF chopper"
    },
    {
      "cause": "to rescue a few troopers who had received gunshots in an encounter",
      "effect": "it tried to land in a conflict zone in Sukma district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when it tried to land in a conflict zone in Sukma district to rescue a few troopers who had received gunshots in an encounter"
      },
      "relation": "caused",
      "effect": {
        "span": "Rebels opened fire on the IAF chopper"
      }
    },
    {
      "cause": {
        "span": "to rescue a few troopers who had received gunshots in an encounter"
      },
      "relation": "caused",
      "effect": {
        "span": "it tried to land in a conflict zone in Sukma district"
      }
    },
    {
      "cause": {
        "span": "in an encounter"
      },
      "relation": "caused",
      "effect": {
        "span": "who had received gunshots"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=1560 ---

输入文本: Police officers arrived on the spot and promised action and convinced Jaya to stop the protest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Police officers arrived on the spot and promised action",
      "effect": "convinced Jaya to stop the protest"
    },
    {
      "cause": "to stop the protest",
      "effect": "convinced Jaya"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to stop the protest"
      },
      "relation": "caused",
      "effect": {
        "span": "convinced Jaya"
      }
    }
  ]
}
```

### --- id=148 ---

输入文本: Hong Kong police on Thursday also charged 44 people linked to the protests with “ rioting ” , a crime that carries a maximum penalty of 10 years in prison .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "“ rioting ”",
      "effect": "Hong Kong police on Thursday also charged 44 people linked to the protests"
    },
    {
      "cause": "linked to the protests with “ rioting ”",
      "effect": "Hong Kong police on Thursday also charged 44 people"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "linked to the protests"
      },
      "relation": "caused",
      "effect": {
        "span": "Hong Kong police on Thursday also charged 44 people linked to the protests with “ rioting ”"
      }
    },
    {
      "cause": {
        "span": "“ rioting ”"
      },
      "relation": "caused",
      "effect": {
        "span": "a crime that carries a maximum penalty of 10 years in prison ."
      }
    }
  ]
}
```

### --- id=2302 ---

输入文本: On Wednesday , a crowd , made up of mainly young people from various civil community organisations and students from universities and schools across the city , gathered outside the CTICC , chanting struggle songs and holding posters on which was written `` enough is enough '' and `` stop killing women and children '' .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "chanting struggle songs and holding posters on which was written `` enough is enough '' and `` stop killing women and children ''",
      "effect": "On Wednesday , a crowd , made up of mainly young people from various civil community organisations and students from universities and schools across the city , gathered outside the CTICC"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "enough is enough"
      },
      "relation": "caused",
      "effect": {
        "span": "a crowd , made up of mainly young people from various civil community organisations and students from universities and schools across the city , gathered outside the CTICC , chanting struggle songs and holding posters"
      }
    },
    {
      "cause": {
        "span": "stop killing women and children"
      },
      "relation": "caused",
      "effect": {
        "span": "a crowd , made up of mainly young people from various civil community organisations and students from universities and schools across the city , gathered outside the CTICC , chanting struggle songs and holding posters"
      }
    }
  ]
}
```

### --- id=1072 ---

输入文本: In India , actions around the Copenhagen talks are being organised by Climate Satyagraha Camp , a civil society coalition to give Indians a voice to the Climate Summit in Copenhagen .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to give Indians a voice to the Climate Summit in Copenhagen",
      "effect": "In India , actions around the Copenhagen talks are being organised by Climate Satyagraha Camp , a civil society coalition"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to give Indians a voice to the Climate Summit in Copenhagen"
      },
      "relation": "caused",
      "effect": {
        "span": "Climate Satyagraha Camp , a civil society coalition"
      }
    }
  ]
}
```

### --- id=2569 ---

输入文本: Earlier in the day , the hotel premises saw party workers waving Trinamool flags and shouting slogans demanding justice from the management .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding justice from the management",
      "effect": "the hotel premises saw party workers waving Trinamool flags and shouting slogans"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding justice from the management"
      },
      "relation": "caused",
      "effect": {
        "span": "party workers waving Trinamool flags and shouting slogans"
      }
    }
  ]
}
```

### --- id=296 ---

输入文本: The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma to probe into the violence and the deaths of 44 people in wage-related protests .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to probe into the violence and the deaths of 44 people in wage-related protests",
      "effect": "The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma"
    },
    {
      "cause": "wage-related protests",
      "effect": "the violence and the deaths of 44 people"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to probe into the violence and the deaths of 44 people in wage-related protests"
      },
      "relation": "caused",
      "effect": {
        "span": "The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma"
      }
    }
  ]
}
```

### --- id=2925 ---

输入文本: Sub-Inspector Murlidhar Bastia of Raghunathpur area was killed in Maoist attack while working in Keonjhar district .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Maoist attack while working in Keonjhar district",
      "effect": "Sub-Inspector Murlidhar Bastia of Raghunathpur area was killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in Maoist attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Sub-Inspector Murlidhar Bastia of Raghunathpur area was killed"
      }
    }
  ]
}
```

### --- id=1238 ---

输入文本: Till the filing of this report , all protesters were squatting outside Vikas Bhawan and said would call off their stir only after getting formal orders regarding regularisation of all retrenched staffers .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the filing of this report",
      "effect": "all protesters were squatting outside Vikas Bhawan"
    },
    {
      "cause": "getting formal orders regarding regularisation of all retrenched staffers",
      "effect": "would call off their stir"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after getting formal orders regarding regularisation of all retrenched staffers"
      },
      "relation": "caused",
      "effect": {
        "span": "all protesters were squatting outside Vikas Bhawan and said would call off their stir"
      }
    }
  ]
}
```

### --- id=1555 ---

输入文本: Subsequently , the police arrested six persons in connection with the murder and eight others turned themselves in .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "in connection with the murder and eight others turned themselves in",
      "effect": "the police arrested six persons"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "the police arrested six persons in connection with the murder"
      }
    },
    {
      "cause": {
        "span": "the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "eight others turned themselves in"
      }
    }
  ]
}
```

### --- id=3038 ---

输入文本: April 13 , 2013 00:00 IST Police step up security Several hundred shops in Podanur , Sundarapuram , Kuniamuthur , Kovaipudur , Milekal , Machampalayam , Idayarpalayam , Kulathupalayam and Sungapuram areas remained closed on Friday in protest against the damage caused to an idol at a temple on Monday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "in protest against the damage caused to an idol at a temple on Monday",
      "effect": "Several hundred shops in Podanur , Sundarapuram , Kuniamuthur , Kovaipudur , Milekal , Machampalayam , Idayarpalayam , Kulathupalayam and Sungapuram areas remained closed on Friday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the damage caused to an idol at a temple on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "Several hundred shops in Podanur , Sundarapuram , Kuniamuthur , Kovaipudur , Milekal , Machampalayam , Idayarpalayam , Kulathupalayam and Sungapuram areas remained closed on Friday"
      }
    },
    {
      "cause": {
        "span": "the damage caused to an idol at a temple on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "damage caused to an idol at a temple on Monday"
      }
    }
  ]
}
```

### --- id=2051 ---

输入文本: Meanwhile , the Salem Range DIG , Sanjay Kumar , said that a special team has been formed to nab the assailants who murdered Ramesh .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to nab the assailants who murdered Ramesh",
      "effect": "a special team has been formed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to nab the assailants who murdered Ramesh"
      },
      "relation": "caused",
      "effect": {
        "span": "the Salem Range DIG , Sanjay Kumar , said that a special team has been formed"
      }
    },
    {
      "cause": {
        "span": "who murdered Ramesh"
      },
      "relation": "caused",
      "effect": {
        "span": "to nab the assailants"
      }
    }
  ]
}
```

### --- id=1461 ---

输入文本: The police charged Mr. Chandrashekhar with instigating violence on May 9 under various IPC sections .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "instigating violence on May 9 under various IPC sections",
      "effect": "The police charged Mr. Chandrashekhar"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "instigating violence on May 9"
      },
      "relation": "caused",
      "effect": {
        "span": "The police charged Mr. Chandrashekhar with instigating violence on May 9 under various IPC sections ."
      }
    }
  ]
}
```

### --- id=2281 ---

输入文本: While an official ceremony took place at the Hong Kong Convention and Exhibition Centre to mark the 22nd anniversary of the return of sovereignty from Britain to China , tensions spiked once more in the financial hub after hundreds of mainly young , masked protesters mostly in black wearing hard hats and goggles seized three key thoroughfares , some deploying metal and plastic barriers to block the way .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to mark the 22nd anniversary of the return of sovereignty from Britain to China",
      "effect": "an official ceremony took place at the Hong Kong Convention and Exhibition Centre"
    },
    {
      "cause": "hundreds of mainly young , masked protesters mostly in black wearing hard hats and goggles seized three key thoroughfares",
      "effect": "tensions spiked once more in the financial hub"
    },
    {
      "cause": "to block the way",
      "effect": "some deploying metal and plastic barriers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "hundreds of mainly young , masked protesters mostly in black wearing hard hats and goggles seized three key thoroughfares , some deploying metal and plastic barriers to block the way"
      },
      "relation": "caused",
      "effect": {
        "span": "tensions spiked once more in the financial hub"
      }
    }
  ]
}
```

### --- id=1138 ---

输入文本: Senior teachers , concerned about the future of students , agreed that the university administration had made a smart move to conduct classes even as the exams were boycotted to ensure that the mandatory instruction days were met with .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to ensure that the mandatory instruction days were met with",
      "effect": "the university administration had made a smart move to conduct classes even as the exams were boycotted"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "concerned about the future of students"
      },
      "relation": "caused",
      "effect": {
        "span": "Senior teachers , concerned about the future of students , agreed that the university administration had made a smart move to conduct classes even as the exams were boycotted to ensure that the mandatory instruction days were met with ."
      }
    },
    {
      "cause": {
        "span": "to ensure that the mandatory instruction days were met with"
      },
      "relation": "caused",
      "effect": {
        "span": "the university administration had made a smart move to conduct classes even as the exams were boycotted"
      }
    }
  ]
}
```

### --- id=1172 ---

输入文本: On July 16 , one person identified as Mintu Deori was killed during a protest while 20 others , including two Additional SPs , were injured in clashes between police and protesters demanding shifting of proposed AIIMS in Assam from Changsari to Raha .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "a protest",
      "effect": "one person identified as Mintu Deori was killed"
    },
    {
      "cause": "clashes between police and protesters",
      "effect": "20 others , including two Additional SPs , were injured"
    },
    {
      "cause": "demanding shifting of proposed AIIMS in Assam from Changsari to Raha",
      "effect": "clashes between police and protesters"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "clashes between police and protesters demanding shifting of proposed AIIMS in Assam from Changsari to Raha"
      },
      "relation": "caused",
      "effect": {
        "span": "one person identified as Mintu Deori was killed during a protest"
      }
    },
    {
      "cause": {
        "span": "clashes between police and protesters demanding shifting of proposed AIIMS in Assam from Changsari to Raha"
      },
      "relation": "caused",
      "effect": {
        "span": "20 others , including two Additional SPs , were injured"
      }
    },
    {
      "cause": {
        "span": "demanding shifting of proposed AIIMS in Assam from Changsari to Raha"
      },
      "relation": "caused",
      "effect": {
        "span": "clashes between police and protesters demanding shifting of proposed AIIMS in Assam from Changsari to Raha"
      }
    }
  ]
}
```

### --- id=905 ---

输入文本: The incident triggered outrage across the country and was condemned as despicable and shameful stirring memories of a similar attack last December in New Delhi that sparked nationwide protests .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "The incident",
      "effect": "triggered outrage across the country and was condemned as despicable and shameful stirring memories of a similar attack last December in New Delhi that sparked nationwide protests"
    },
    {
      "cause": "a similar attack last December in New Delhi",
      "effect": "nationwide protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The incident"
      },
      "relation": "caused",
      "effect": {
        "span": "triggered outrage across the country"
      }
    },
    {
      "cause": {
        "span": "The incident"
      },
      "relation": "caused",
      "effect": {
        "span": "was condemned as despicable and shameful stirring memories of a similar attack last December in New Delhi"
      }
    },
    {
      "cause": {
        "span": "a similar attack last December in New Delhi"
      },
      "relation": "caused",
      "effect": {
        "span": "that sparked nationwide protests ."
      }
    }
  ]
}
```

### --- id=1928 ---

输入文本: The municipality witnessed protests by residents in Boitumelong in the beginning of April , when a number of houses , including a councillor 's , were burnt down .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "The municipality witnessed protests by residents in Boitumelong in the beginning of April",
      "effect": "a number of houses , including a councillor 's , were burnt down"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "protests by residents in Boitumelong in the beginning of April"
      },
      "relation": "caused",
      "effect": {
        "span": "a number of houses , including a councillor 's , were burnt down ."
      }
    }
  ]
}
```

### --- id=809 ---

输入文本: “ We are here to fight for democracy and universal suffrage. ”

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "for democracy and universal suffrage",
      "effect": "We are here to fight"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to fight for democracy and universal suffrage"
      },
      "relation": "caused",
      "effect": {
        "span": "We are here"
      }
    }
  ]
}
```

### --- id=1943 ---

输入文本: Speakers at the rally , orgainsed by the Peoples Union for Civil Liberties ( PUCL ) , CPI , CPM , and Chhattisgarh Mukti Morcha ( CMM ) , accused the Raman Singh government of having implicated Sen in a false case .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "having implicated Sen in a false case",
      "effect": "Speakers at the rally , orgainsed by the Peoples Union for Civil Liberties ( PUCL ) , CPI , CPM , and Chhattisgarh Mukti Morcha ( CMM ) , accused the Raman Singh government of"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "having implicated Sen in a false case"
      },
      "relation": "caused",
      "effect": {
        "span": "Speakers at the rally , orgainsed by the Peoples Union for Civil Liberties ( PUCL ) , CPI , CPM , and Chhattisgarh Mukti Morcha ( CMM ) , accused the Raman Singh government"
      }
    }
  ]
}
```

### --- id=2540 ---

输入文本: Soon after the heat and dust of the twin blasts settled , city policemen worked overtime to step up security arrangements all over the city and schools were among the most important establishments under the scanner .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "step up security arrangements all over the city",
      "effect": "city policemen worked overtime"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the heat and dust of the twin blasts settled"
      },
      "relation": "caused",
      "effect": {
        "span": "city policemen worked overtime to step up security arrangements all over the city"
      }
    },
    {
      "cause": {
        "span": "to step up security arrangements all over the city"
      },
      "relation": "caused",
      "effect": {
        "span": "city policemen worked overtime"
      }
    }
  ]
}
```

### --- id=790 ---

输入文本: The youth 's murder took political overtones this morning with the Leader of Opposition ( LoP ) Prem Kumar meeting the family members of the victim to express sorrow and later addressed a large number of people who had blocked road near Mahabir bridge to protest against the murder .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "the Leader of Opposition ( LoP ) Prem Kumar meeting the family members of the victim to express sorrow and later addressed a large number of people who had blocked road near Mahabir bridge to protest against the murder",
      "effect": "The youth 's murder took political overtones this morning"
    },
    {
      "cause": "to express sorrow",
      "effect": "the Leader of Opposition ( LoP ) Prem Kumar meeting the family members of the victim"
    },
    {
      "cause": "against the murder",
      "effect": "a large number of people who had blocked road near Mahabir bridge to protest"
    },
    {
      "cause": "to protest",
      "effect": "a large number of people who had blocked road near Mahabir bridge"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The youth 's murder"
      },
      "relation": "caused",
      "effect": {
        "span": "took political overtones this morning with the Leader of Opposition ( LoP ) Prem Kumar meeting the family members of the victim to express sorrow and later addressed a large number of people who had blocked road near Mahabir bridge to protest against the murder ."
      }
    },
    {
      "cause": {
        "span": "to express sorrow"
      },
      "relation": "caused",
      "effect": {
        "span": "the Leader of Opposition ( LoP ) Prem Kumar meeting the family members of the victim"
      }
    },
    {
      "cause": {
        "span": "to protest against the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "a large number of people who had blocked road near Mahabir bridge"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=3010 ---

输入文本: March 03 , 2013 00:00 IST Holds demonstration in front of SE office in Nizamabad The TDP Legislators on Saturday , seriously warned the electricity authorities against the frequent cuts in power supply to the farm sector resulting in damage to the crop which is in its last stage for harvest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the frequent cuts in power supply to the farm sector",
      "effect": "damage to the crop which is in its last stage for harvest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the frequent cuts in power supply to the farm sector"
      },
      "relation": "caused",
      "effect": {
        "span": "resulting in damage to the crop which is in its last stage for harvest ."
      }
    },
    {
      "cause": {
        "span": "the frequent cuts in power supply to the farm sector resulting in damage to the crop which is in its last stage for harvest ."
      },
      "relation": "caused",
      "effect": {
        "span": "The TDP Legislators on Saturday , seriously warned the electricity authorities"
      }
    }
  ]
}
```

### --- id=1446 ---

输入文本: KERALA Bishops express concern December 27 , 2007 00:00 IST Kochi : The Kerala Catholic Bishops ’ Council ( KCBC ) has expressed concern over the attack on Christian churches , orphanages and the Bishop ’ s House at Kandhamal in Orissa .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the attack on Christian churches , orphanages and the Bishop ’ s House at Kandhamal in Orissa .",
      "effect": "The Kerala Catholic Bishops ’ Council ( KCBC ) has expressed concern"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the attack on Christian churches , orphanages and the Bishop ’ s House at Kandhamal in Orissa"
      },
      "relation": "caused",
      "effect": {
        "span": "The Kerala Catholic Bishops ’ Council ( KCBC ) has expressed concern"
      }
    }
  ]
}
```

### --- id=708 ---

输入文本: September 04 , 2014 00:00 IST Officials promise to supply water in tankers Women took to streets carrying pots in protest against erratic supply of drinking water at Kelamagalam in Udhanapalli on Wednesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against erratic supply of drinking water at Kelamagalam in Udhanapalli on Wednesday",
      "effect": "Women took to streets carrying pots in protest"
    },
    {
      "cause": "in protest against erratic supply of drinking water at Kelamagalam in Udhanapalli on Wednesday",
      "effect": "Women took to streets carrying pots"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against erratic supply of drinking water at Kelamagalam in Udhanapalli on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "Women took to streets carrying pots"
      }
    }
  ]
}
```

### --- id=91 ---

输入文本: 27th February 2009 02:04 AM COLOMBO : India on Thursday told Pakistan that it recognised what Islamabad had done so far to investigate the involvement of Pakistanis in the Mumbai attacks and curb crossborder terrorism , but a lot more remained to be done to ensure that such attacks did not recur .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to investigate the involvement of Pakistanis in the Mumbai attacks and curb crossborder terrorism",
      "effect": "what Islamabad had done so far"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to ensure that such attacks did not recur"
      },
      "relation": "caused",
      "effect": {
        "span": "a lot more remained to be done"
      }
    }
  ]
}
```

### --- id=2997 ---

输入文本: Big B in big trouble for anti-Sikh remarks 17th December 2011 02:43 PM AMRITSAR : A move by Bollywood superstar Amitabh Bachchan to get a clean chit from the Sikh clergy after his name was dragged into the 1984 anti-Sikh riots is facing opposition from sections of the community .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "his name was dragged into the 1984 anti-Sikh riots",
      "effect": "A move by Bollywood superstar Amitabh Bachchan to get a clean chit from the Sikh clergy"
    },
    {
      "cause": "to get a clean chit from the Sikh clergy",
      "effect": "A move by Bollywood superstar Amitabh Bachchan"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "his name was dragged into the 1984 anti-Sikh riots"
      },
      "relation": "caused",
      "effect": {
        "span": "A move by Bollywood superstar Amitabh Bachchan to get a clean chit from the Sikh clergy"
      }
    }
  ]
}
```

### --- id=1934 ---

输入文本: DA MP Yusuf Cassim said in a statement on Tuesday that universities affected by violent student protests had recorded damages worth more than R150 million .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "universities affected by violent student protests",
      "effect": "had recorded damages worth more than R150 million"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "violent student protests"
      },
      "relation": "caused",
      "effect": {
        "span": "universities affected by violent student protests had recorded damages worth more than R150 million"
      }
    }
  ]
}
```

### --- id=2284 ---

输入文本: In the memorial meeting presided over by the VHP district unit president Kamadab Pradhan and attended by many others including Saraswati 's successor Swami Sachidananda Maharaj criticised the Odisha govenrment for not arresting all those involved in the killing .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "not arresting all those involved in the killing",
      "effect": "In the memorial meeting presided over by the VHP district unit president Kamadab Pradhan and attended by many others including Saraswati 's successor Swami Sachidananda Maharaj criticised the Odisha govenrment"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "not arresting all those involved in the killing"
      },
      "relation": "caused",
      "effect": {
        "span": "Swami Sachidananda Maharaj criticised the Odisha govenrment"
      }
    }
  ]
}
```

### --- id=145 ---

输入文本: ﻿The protests , which began over a proposal to allow extradition to China , pose the most serious challenge to China ’ s authority over the city since 1997 , when it was returned from British to Chinese control .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "a proposal to allow extradition to China",
      "effect": "﻿The protests"
    },
    {
      "cause": "it was returned from British to Chinese control",
      "effect": "pose the most serious challenge to China ’ s authority over the city since 1997"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a proposal to allow extradition to China"
      },
      "relation": "caused",
      "effect": {
        "span": "The protests , which began over a proposal to allow extradition to China"
      }
    }
  ]
}
```

### --- id=1493 ---

输入文本: This was after the Student Representative Council and management clashed over how to deal with rising student debt .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "how to deal with rising student debt",
      "effect": "the Student Representative Council and management clashed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "how to deal with rising student debt"
      },
      "relation": "caused",
      "effect": {
        "span": "the Student Representative Council and management clashed over how to deal with rising student debt"
      }
    },
    {
      "cause": {
        "span": "after the Student Representative Council and management clashed over how to deal with rising student debt"
      },
      "relation": "caused",
      "effect": {
        "span": "This was"
      }
    }
  ]
}
```

### --- id=1492 ---

输入文本: Durban University of Technology ( DUT ) students went on strike early this month which led to the institution being closed for over a week .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Durban University of Technology ( DUT ) students went on strike early this month",
      "effect": "which led to the institution being closed for over a week"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Durban University of Technology ( DUT ) students went on strike early this month"
      },
      "relation": "caused",
      "effect": {
        "span": "the institution being closed for over a week ."
      }
    }
  ]
}
```

### --- id=321 ---

输入文本: Sporadic violence during hartal 20th May 2009 10:23 AM THIRUVANANTHAPURAM : Sporadic violence marked the hartal on Tuesday called by Muslim organisations in protest against the police action in Cheriyathura-Beemappally areas on Sunday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "protest",
      "effect": "Sporadic violence marked the hartal on Tuesday called by Muslim organisations"
    },
    {
      "cause": "against the police action in Cheriyathura-Beemappally areas on Sunday",
      "effect": "protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the police action in Cheriyathura-Beemappally areas on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "Sporadic violence marked the hartal on Tuesday called by Muslim organisations"
      }
    }
  ]
}
```

### --- id=1564 ---

输入文本: The Patels have been seeking quota under the OBC category through a pitched 10 - month-old agitation across the state , and this proved to be a key factor for the exit of Anandiben Patel as the Chief Minister .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "The Patels have been seeking quota under the OBC category through a pitched 10 - month-old agitation across the state",
      "effect": "the exit of Anandiben Patel as the Chief Minister"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a pitched 10 - month-old agitation across the state"
      },
      "relation": "caused",
      "effect": {
        "span": "The Patels have been seeking quota under the OBC category"
      }
    },
    {
      "cause": {
        "span": "a pitched 10 - month-old agitation across the state"
      },
      "relation": "caused",
      "effect": {
        "span": "this proved to be a key factor for the exit of Anandiben Patel as the Chief Minister ."
      }
    }
  ]
}
```

### --- id=1760 ---

输入文本: Some protesters wore T-shirts bearing the image of Mbombela municipal speaker Jimmy Mohlala , who was shot dead in January 2009 after blowing the whistle on companies and individuals he claimed were involved in tender corruption .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "blowing the whistle on companies and individuals he claimed were involved in tender corruption",
      "effect": "Mbombela municipal speaker Jimmy Mohlala , who was shot dead in January 2009"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "blowing the whistle on companies and individuals he claimed were involved in tender corruption"
      },
      "relation": "caused",
      "effect": {
        "span": "who was shot dead in January 2009"
      }
    }
  ]
}
```

### --- id=693 ---

输入文本: The CPM workers too came out of the building to confront the protesters and a minor scuffle ensued .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to confront the protesters and a minor scuffle ensued",
      "effect": "The CPM workers too came out of the building"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to confront the protesters"
      },
      "relation": "caused",
      "effect": {
        "span": "The CPM workers too came out of the building"
      }
    },
    {
      "cause": {
        "span": "The CPM workers too came out of the building to confront the protesters"
      },
      "relation": "caused",
      "effect": {
        "span": "a minor scuffle ensued ."
      }
    }
  ]
}
```

### --- id=2773 ---

输入文本: As the Muslims and tribals clashed , eight people were injured in police firing .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "police firing",
      "effect": "eight people were injured"
    },
    {
      "cause": "the Muslims and tribals clashed",
      "effect": "police firing"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "As the Muslims and tribals clashed"
      },
      "relation": "caused",
      "effect": {
        "span": "eight people were injured in police firing ."
      }
    }
  ]
}
```

### --- id=1780 ---

输入文本: Activists of Bajrang Dal , who had gathered outside Vikram University in Ujjain to catch those found celebrating Valentine 's Day , stopped the two young people and beat up the man .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to catch those found celebrating Valentine 's Day",
      "effect": "Activists of Bajrang Dal , who had gathered outside Vikram University in Ujjain"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to catch those found celebrating Valentine 's Day"
      },
      "relation": "caused",
      "effect": {
        "span": "Activists of Bajrang Dal , who had gathered outside Vikram University in Ujjain"
      }
    },
    {
      "cause": {
        "span": "who had gathered outside Vikram University in Ujjain to catch those found celebrating Valentine 's Day"
      },
      "relation": "caused",
      "effect": {
        "span": "stopped the two young people and beat up the man ."
      }
    }
  ]
}
```

### --- id=418 ---

输入文本: Posted : Fri Aug 28 1998 IST MUMBAI , Aug 27 : An honorary orthopaedic surgeon with Bhagwati Hospital resigned today and private hospitals from Jogeshwari to Dahisar decided to down shutters for a day , as doctors closed ranks to protest Tuesday 's rioting at Bhagwati Hospital , where a BJP leader , injured in a shootout , had succumbed to his injuries .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "doctors closed ranks to protest Tuesday 's rioting at Bhagwati Hospital",
      "effect": "An honorary orthopaedic surgeon with Bhagwati Hospital resigned today and private hospitals from Jogeshwari to Dahisar decided to down shutters for a day"
    },
    {
      "cause": "to protest Tuesday 's rioting at Bhagwati Hospital",
      "effect": "doctors closed ranks"
    },
    {
      "cause": "a BJP leader , injured in a shootout",
      "effect": "had succumbed to his injuries"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest Tuesday 's rioting at Bhagwati Hospital , where a BJP leader , injured in a shootout , had succumbed to his injuries ."
      },
      "relation": "caused",
      "effect": {
        "span": "An honorary orthopaedic surgeon with Bhagwati Hospital resigned today and private hospitals from Jogeshwari to Dahisar decided to down shutters for a day"
      }
    },
    {
      "cause": {
        "span": "Tuesday 's rioting at Bhagwati Hospital , where a BJP leader , injured in a shootout , had succumbed to his injuries ."
      },
      "relation": "caused",
      "effect": {
        "span": "doctors closed ranks to protest Tuesday 's rioting at Bhagwati Hospital"
      }
    },
    {
      "cause": {
        "span": "a shootout"
      },
      "relation": "caused",
      "effect": {
        "span": "a BJP leader , injured in a shootout , had succumbed to his injuries ."
      }
    }
  ]
}
```

### --- id=1739 ---

输入文本: Placard at a protest outside the Zimbabwe consulate in Johannesburg against the `` deafening silence '' of South Africa over the situation in Zimbabwe .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against the `` deafening silence '' of South Africa over the situation in Zimbabwe",
      "effect": "Placard at a protest outside the Zimbabwe consulate in Johannesburg"
    },
    {
      "cause": "the situation in Zimbabwe",
      "effect": "the `` deafening silence '' of South Africa"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the `` deafening silence '' of South Africa over the situation in Zimbabwe"
      },
      "relation": "caused",
      "effect": {
        "span": "Placard at a protest outside the Zimbabwe consulate in Johannesburg"
      }
    }
  ]
}
```

### --- id=48 ---

输入文本: Biswal , who had travelled to the city from Washington to speak at the Indian Consulate General 's Media-India Lecture Series yesterday , said not only were there a large number of Indian victims in the attack but there were Americans also who lost their lives .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to speak at the Indian Consulate General 's Media-India Lecture Series yesterday",
      "effect": "Biswal , who had travelled to the city from Washington"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to speak at the Indian Consulate General 's Media-India Lecture Series yesterday"
      },
      "relation": "caused",
      "effect": {
        "span": "Biswal , who had travelled to the city from Washington"
      }
    },
    {
      "cause": {
        "span": "the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "there were a large number of Indian victims in the attack"
      }
    },
    {
      "cause": {
        "span": "the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "there were Americans also who lost their lives"
      }
    }
  ]
}
```

### --- id=2116 ---

输入文本: Meanwhile , police sources said the brick kiln owners have charged the protesters with pelting them with stones when they approached with a proposal to accept their demands .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "pelting them with stones when they approached with a proposal to accept their demands",
      "effect": "brick kiln owners have charged the protesters"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "pelting them with stones"
      },
      "relation": "caused",
      "effect": {
        "span": "police sources said the brick kiln owners have charged the protesters"
      }
    },
    {
      "cause": {
        "span": "when they approached with a proposal to accept their demands"
      },
      "relation": "caused",
      "effect": {
        "span": "pelting them with stones"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=1573 ---

输入文本: September 28 , 2010 00:00 IST TDP chief addresses ‘ maha dharna ' in the vicinity of Anantapur Collector 's office Telugu Desam president Nara Chandrababu Naidu has called upon the cadre and people to be prepared to march to the State capital and if necessary , to the Assembly , to pressurise the government to solve the farmers problems .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to march to the State capital and if necessary , to the Assembly",
      "effect": "Telugu Desam president Nara Chandrababu Naidu has called upon the cadre and people to be prepared"
    },
    {
      "cause": "to pressurise the government to solve the farmers problems",
      "effect": "to march to the State capital and if necessary , to the Assembly"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to pressurise the government to solve the farmers problems"
      },
      "relation": "caused",
      "effect": {
        "span": "Telugu Desam president Nara Chandrababu Naidu has called upon the cadre and people to be prepared to march to the State capital and if necessary , to the Assembly"
      }
    }
  ]
}
```

### --- id=795 ---

输入文本: The move was seen as highly controversial and sparked about 13,000 to take to the streets in a protest that ended in clashes with police .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "The move was seen as highly controversial",
      "effect": "about 13,000 to take to the streets in a protest"
    },
    {
      "cause": "about 13,000 to take to the streets in a protest",
      "effect": "that ended in clashes with police"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The move was seen as highly controversial"
      },
      "relation": "caused",
      "effect": {
        "span": "sparked about 13,000 to take to the streets in a protest that ended in clashes with police ."
      }
    },
    {
      "cause": {
        "span": "a protest that ended in clashes with police"
      },
      "relation": "caused",
      "effect": {
        "span": "ended in clashes with police ."
      }
    }
  ]
}
```

### --- id=524 ---

输入文本: " The relay fast is a way of supporting Anna from Pune .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "a way of supporting Anna from Pune",
      "effect": "The relay fast"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "supporting Anna from Pune"
      },
      "relation": "caused",
      "effect": {
        "span": "The relay fast is a way"
      }
    }
  ]
}
```

### --- id=2305 ---

输入文本: As a nationwide commuter rail strike entered its second day on Tuesday , delaying thousands of commuters , Metrorail increased its alternative service in Cape Town to 360 bus journeys .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "a nationwide commuter rail strike entered its second day on Tuesday",
      "effect": "delaying thousands of commuters"
    },
    {
      "cause": "a nationwide commuter rail strike entered its second day on Tuesday , delaying thousands of commuters",
      "effect": "Metrorail increased its alternative service in Cape Town to 360 bus journeys"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "As a nationwide commuter rail strike entered its second day on Tuesday"
      },
      "relation": "caused",
      "effect": {
        "span": "delaying thousands of commuters"
      }
    },
    {
      "cause": {
        "span": "As a nationwide commuter rail strike entered its second day on Tuesday"
      },
      "relation": "caused",
      "effect": {
        "span": "Metrorail increased its alternative service in Cape Town to 360 bus journeys ."
      }
    }
  ]
}
```

### --- id=1995 ---

输入文本: But the authorities ’ harsh policing of the protests , coupled with a refusal by Hong Kong ’ s leader to completely withdraw the bill , mean protesters have returned to the streets time and again .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the authorities ’ harsh policing of the protests , coupled with a refusal by Hong Kong ’ s leader to completely withdraw the bill",
      "effect": "mean protesters have returned to the streets time and again"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the authorities ’ harsh policing of the protests , coupled with a refusal by Hong Kong ’ s leader to completely withdraw the bill"
      },
      "relation": "caused",
      "effect": {
        "span": "protesters have returned to the streets time and again"
      }
    }
  ]
}
```

### --- id=711 ---

输入文本: At Balagangamanahalli panchayat in Dharmapuri , residents of Eechampatti village laid siege to the Nallampalli BDO ’ s office in protest against non supply of water .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "in protest against non supply of water",
      "effect": "At Balagangamanahalli panchayat in Dharmapuri , residents of Eechampatti village laid siege to the Nallampalli BDO ’ s office"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against non supply of water"
      },
      "relation": "caused",
      "effect": {
        "span": "residents of Eechampatti village laid siege to the Nallampalli BDO ’ s office"
      }
    }
  ]
}
```

### --- id=382 ---

输入文本: “ Suddenly the situation flared up and the vehicle was vandalised .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Suddenly the situation flared up",
      "effect": "the vehicle was vandalised"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the situation flared up"
      },
      "relation": "caused",
      "effect": {
        "span": "the vehicle was vandalised ."
      }
    }
  ]
}
```

### --- id=2706 ---

输入文本: A peaceful march in the town of Yuen Long to condemn an attack by suspected gang members on commuters turned violent as Hong Kong riot police fired teargas and rubber bullets on the crowd and used batons to beat protesters .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "Hong Kong riot police fired teargas and rubber bullets on the crowd and used batons to beat protesters",
      "effect": "A peaceful march in the town of Yuen Long to condemn an attack by suspected gang members on commuters turned violent"
    },
    {
      "cause": "condemn an attack by suspected gang members on commuters",
      "effect": "A peaceful march in the town of Yuen Long"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an attack by suspected gang members on commuters"
      },
      "relation": "caused",
      "effect": {
        "span": "A peaceful march in the town of Yuen Long to condemn an attack by suspected gang members on commuters"
      }
    },
    {
      "cause": {
        "span": "Hong Kong riot police fired teargas and rubber bullets on the crowd and used batons to beat protesters"
      },
      "relation": "caused",
      "effect": {
        "span": "A peaceful march in the town of Yuen Long to condemn an attack by suspected gang members on commuters turned violent"
      }
    }
  ]
}
```

### --- id=1437 ---

输入文本: Two protestors were shot dead , allegedly by police , on Monday during a service delivery protest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "a service delivery protest",
      "effect": "Two protestors were shot dead , allegedly by police , on Monday"
    },
    {
      "cause": "allegedly by police , on Monday during a service delivery protest",
      "effect": "Two protestors were shot dead"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "during a service delivery protest"
      },
      "relation": "caused",
      "effect": {
        "span": "Two protestors were shot dead , allegedly by police , on Monday"
      }
    }
  ]
}
```

### --- id=1714 ---

输入文本: It was against this background that the centre started its public campaign to collect signatures in Wuhan on July 29 .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to collect signatures in Wuhan on July 29",
      "effect": "the centre started its public campaign"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against this background"
      },
      "relation": "caused",
      "effect": {
        "span": "the centre started its public campaign to collect signatures in Wuhan on July 29"
      }
    },
    {
      "cause": {
        "span": "to collect signatures in Wuhan on July 29"
      },
      "relation": "caused",
      "effect": {
        "span": "the centre started its public campaign"
      }
    }
  ]
}
```

### --- id=2915 ---

输入文本: The umbrella movement protests did not achieve “ what the demonstrators wanted and of course they didn ’ t have a well thought out strategy ” .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "they didn ’ t have a well thought out strategy",
      "effect": "The umbrella movement protests did not achieve “ what the demonstrators wanted"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they ’ t have a well thought out strategy"
      },
      "relation": "caused",
      "effect": {
        "span": "The umbrella movement protests did not achieve “ what the demonstrators wanted"
      }
    }
  ]
}
```

### --- id=2451 ---

输入文本: Only CPM had enmity towards TP , says Rema 27th February 2013 08:44 AM K K Rema , wife of slain leader T P Chandrasekharan , stuck to her statement before the Special Additional District and Sessions Court ( Marad cases ) here that the CPM had enmity towards her husband and denied the suggestions made by the defence counsel .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "K K Rema , wife of slain leader T P Chandrasekharan , stuck to her statement before the Special Additional District and Sessions Court ( Marad cases ) here that the CPM had enmity towards her husband",
      "effect": "denied the suggestions made by the defence counsel"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the CPM had enmity towards her husband"
      },
      "relation": "caused",
      "effect": {
        "span": "K K Rema , wife of slain leader T P Chandrasekharan , stuck to her statement before the Special Additional District and Sessions Court ( Marad cases ) here"
      }
    }
  ]
}
```

### --- id=1869 ---

输入文本: - Indian Express Express News Service , Express News Service : Surat , Tue Jan 20 2009 , 01:11 hrs Thousands of workers had queued up outside SDA office to collect forms to waive school fees

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to collect forms",
      "effect": "Thousands of workers had queued up outside SDA office"
    },
    {
      "cause": "to waive school fees",
      "effect": "collect forms"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to collect forms to waive school fees"
      },
      "relation": "caused",
      "effect": {
        "span": "Thousands of workers had queued up outside SDA office"
      }
    }
  ]
}
```

### --- id=298 ---

输入文本: But the locals said clashes between the residents and the Army started in the morning when the latter stopped the movement of fruit trucks in Rafiabad and Sopore , asking the drivers to ply only during the shutdown period .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the latter stopped the movement of fruit trucks in Rafiabad and Sopore",
      "effect": "clashes between the residents and the Army started in the morning"
    },
    {
      "cause": "asking the drivers to ply only during the shutdown period",
      "effect": "the latter stopped the movement of fruit trucks in Rafiabad and Sopore"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when the latter stopped the movement of fruit trucks in Rafiabad and Sopore , asking the drivers to ply only during the shutdown period"
      },
      "relation": "caused",
      "effect": {
        "span": "the locals said clashes between the residents and the Army started in the morning"
      }
    }
  ]
}
```

### --- id=261 ---

输入文本: The slogan , “ We want Sureswari irrigation project not JR Power Plant ” rented the air even as vehicular traffic came to a standstill from 6 am till noon following the blockade by people of Kishorenagar area .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the blockade by people of Kishorenagar area",
      "effect": "The slogan , “ We want Sureswari irrigation project not JR Power Plant ” rented the air even as vehicular traffic came to a standstill from 6 am till noon"
    },
    {
      "cause": "vehicular traffic came to a standstill from 6 am till noon",
      "effect": "The slogan , “ We want Sureswari irrigation project not JR Power Plant ” rented the air"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "following the blockade by people of Kishorenagar area"
      },
      "relation": "caused",
      "effect": {
        "span": "vehicular traffic came to a standstill from 6 am till noon"
      }
    }
  ]
}
```

### --- id=2201 ---

输入文本: High drama as water stir turns protest against cop 25th April 2013 11:10 AM High drama was witnessed on Arni Road on Wednesday , when residents of Virupatchipuram , of ward 41 of Vellore Corporation , demanded an apology and transfer of a woman sub-inspector ( SI ) attached to the Bagayam police station .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "residents of Virupatchipuram , of ward 41 of Vellore Corporation , demanded an apology and transfer of a woman sub-inspector ( SI ) attached to the Bagayam police station",
      "effect": "High drama was witnessed on Arni Road on Wednesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanded an apology and transfer of a woman sub-inspector ( SI ) attached to the Bagayam police station"
      },
      "relation": "caused",
      "effect": {
        "span": "High drama was witnessed on Arni Road on Wednesday"
      }
    }
  ]
}
```

### --- id=2046 ---

输入文本: Recent years have seen radicals with links to Xinjiang use vehicles to carry out a series of terror attacks in China including a May 2014 market bombing in the capital Urumqi and an attack in Beijing ’ s Tiananmen Square in October 2013 .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to carry out a series of terror attacks in China including a May 2014 market bombing in the capital Urumqi and an attack in Beijing ’ s Tiananmen Square in October 2013",
      "effect": "radicals with links to Xinjiang use vehicles"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "radicals with links to Xinjiang use vehicles"
      },
      "relation": "caused",
      "effect": {
        "span": "to carry out a series of terror attacks in China including a May 2014 market bombing in the capital Urumqi and an attack in Beijing ’ s Tiananmen Square in October 2013 ."
      }
    }
  ]
}
```

### --- id=2182 ---

输入文本: Since the Senas recent attack on railway recruitment candidates at Kalyan station , groups of 100 -200 migrants have been meeting at various locations , to voice their disbelief , disquiet and make plans .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the Senas recent attack on railway recruitment candidates at Kalyan station",
      "effect": "groups of 100 -200 migrants have been meeting at various locations , to voice their disbelief , disquiet and make plans"
    },
    {
      "cause": "voice their disbelief , disquiet and make plans",
      "effect": "groups of 100 -200 migrants have been meeting at various locations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Since the Senas recent attack on railway recruitment candidates at Kalyan station"
      },
      "relation": "caused",
      "effect": {
        "span": "groups of 100 -200 migrants have been meeting at various locations"
      }
    },
    {
      "cause": {
        "span": "to voice their disbelief , disquiet and make plans"
      },
      "relation": "caused",
      "effect": {
        "span": "groups of 100 -200 migrants have been meeting at various locations"
      }
    }
  ]
}
```

### --- id=2280 ---

输入文本: The semi-autonomous city has been shaken by historic demonstrations in the past month , when protesters have demanded the withdrawal of a bill that would allow extraditions to the Chinese mainland .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "historic demonstrations in the past month",
      "effect": "The semi-autonomous city has been shaken"
    },
    {
      "cause": "protesters have demanded the withdrawal of a bill that would allow extraditions to the Chinese mainland",
      "effect": "historic demonstrations in the past month"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "historic demonstrations in the past month"
      },
      "relation": "caused",
      "effect": {
        "span": "The semi-autonomous city has been shaken"
      }
    },
    {
      "cause": {
        "span": "to demand the withdrawal of a bill that would allow extraditions to the Chinese mainland"
      },
      "relation": "caused",
      "effect": {
        "span": "protesters have demanded the withdrawal of a bill that would allow extraditions to the Chinese mainland"
      }
    }
  ]
}
```

### --- id=2565 ---

输入文本: Yet older people have been drawn into the protests too : not just democracy veterans , but citizens inspired by the younger generation .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "citizens inspired by the younger generation",
      "effect": "older people have been drawn into the protests too"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "inspired by the younger generation"
      },
      "relation": "caused",
      "effect": {
        "span": "citizens"
      }
    }
  ]
}
```

### --- id=879 ---

输入文本: Andhra Bifurcation : Mixed Response for Seemandhra Bandh 07th December 2013 03:28 PM The two-day bandh call given by the pro-United Andhra Pradesh groups against the Cabinet 's nod for draft bill for bifurcation of the state has evoked a mixed response in the coastal Andhra and Rayalaseema regions on the second day today .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against the Cabinet 's nod for draft bill for bifurcation of the state",
      "effect": "The two-day bandh call given by the pro-United Andhra Pradesh groups"
    },
    {
      "cause": "The two-day bandh call given by the pro-United Andhra Pradesh groups against the Cabinet 's nod for draft bill for bifurcation of the state",
      "effect": "a mixed response in the coastal Andhra and Rayalaseema regions on the second day today"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the Cabinet 's nod for draft bill for bifurcation of the state"
      },
      "relation": "caused",
      "effect": {
        "span": "The two-day bandh call given by the pro-United Andhra Pradesh groups"
      }
    }
  ]
}
```

### --- id=1462 ---

输入文本: 31st May 2016 10:32 AM NEW DELHI : Jawaharlal Nehru University Students Union ( JNUSU ) president Kanhaiya Kumar urged the nation to come out in large numbers and join the African students for the ‘ March for Justice ’ at the Jantar Mantar in the national capital on Tuesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the ‘ March for Justice ’ at the Jantar Mantar in the national capital on Tuesday",
      "effect": "Jawaharlal Nehru University Students Union ( JNUSU ) president Kanhaiya Kumar urged the nation to come out in large numbers and join the African students"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to come out in large numbers and join the African students for the ‘ March for Justice ’ at the Jantar Mantar in the national capital on Tuesday"
      },
      "relation": "caused",
      "effect": {
        "span": "Jawaharlal Nehru University Students Union ( JNUSU ) president Kanhaiya Kumar urged the nation"
      }
    }
  ]
}
```

### --- id=2481 ---

输入文本: - Indian Express PTI , PTI : Guwahati , Sat Aug 03 2013 , 14:53 hrs Violence continued to rock Karbi Anglong district where various government offices were torched and train tracks removed by activists of different organisations today demanding a separate state on the lines of Telangana .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "various government offices were torched and train tracks removed by activists of different organisations today",
      "effect": "Violence continued to rock Karbi Anglong district"
    },
    {
      "cause": "demanding a separate state on the lines of Telangana",
      "effect": "various government offices were torched and train tracks removed by activists of different organisations today"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding a separate state on the lines of Telangana"
      },
      "relation": "caused",
      "effect": {
        "span": "Violence continued to rock Karbi Anglong district where various government offices were torched and train tracks removed by activists of different organisations today"
      }
    }
  ]
}
```

### --- id=232 ---

输入文本: `` Talks are underway to solve the wage dispute and to end the strike , '' she said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to solve the wage dispute and to end the strike",
      "effect": "Talks are underway"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to solve the wage dispute"
      },
      "relation": "caused",
      "effect": {
        "span": "Talks are underway"
      }
    },
    {
      "cause": {
        "span": "to end the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "Talks are underway"
      }
    }
  ]
}
```

### --- id=1292 ---

输入文本: The 1967 riots , which were triggered by a labour dispute in San Po Kong , claimed 51 lives and briefly brought the city to a standstill .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "which were triggered by a labour dispute in San Po Kong",
      "effect": "The 1967 riots"
    },
    {
      "cause": "The 1967 riots",
      "effect": "claimed 51 lives and briefly brought the city to a standstill"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a labour dispute in San Po Kong"
      },
      "relation": "caused",
      "effect": {
        "span": "The 1967 riots , which were triggered by a labour dispute in San Po Kong"
      }
    },
    {
      "cause": {
        "span": "The 1967 riots , which were triggered by a labour dispute in San Po Kong"
      },
      "relation": "caused",
      "effect": {
        "span": "claimed 51 lives and briefly brought the city to a standstill ."
      }
    }
  ]
}
```

### --- id=2525 ---

输入文本: `` We suspect that he pulled the trigger that killed Chika '' .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "he pulled the trigger",
      "effect": "that killed Chika"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he pulled the trigger"
      },
      "relation": "caused",
      "effect": {
        "span": "We suspect that he pulled the trigger that killed Chika"
      }
    },
    {
      "cause": {
        "span": "the trigger"
      },
      "relation": "caused",
      "effect": {
        "span": "that killed Chika"
      }
    }
  ]
}
```

### --- id=521 ---

输入文本: Their names have been registered so that they can be called to participate in the relay fast , " said K D Pawar of Bhrashtachar Virodhi Janandolan , coordinating the agitation in the city .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "so that they can be called to participate in the relay fast",
      "effect": "Their names have been registered"
    },
    {
      "cause": "to participate in the relay fast",
      "effect": "they can be called"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "so that they can be called to participate in the relay fast"
      },
      "relation": "caused",
      "effect": {
        "span": "Their names have been registered"
      }
    }
  ]
}
```

### --- id=786 ---

输入文本: May 19 , 2012 00:00 IST Members of the Dakshina Kannada and Udupi district units of the Communist Party of India ( CPI ) staged a protest in front of the Deputy Commissioner 's office here on Friday condemning the BJP Government for arresting Vittala Malekudiya , a postgraduate student of Mass Communication and Journalism of Mangalore University , for alleged links with Maoists .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "condemning the BJP Government",
      "effect": "Members of the Dakshina Kannada and Udupi district units of the Communist Party of India ( CPI ) staged a protest in front of the Deputy Commissioner 's office here on Friday"
    },
    {
      "cause": "arresting Vittala Malekudiya , a postgraduate student of Mass Communication and Journalism of Mangalore University , for alleged links with Maoists .",
      "effect": "condemning the BJP Government"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "arresting Vittala Malekudiya , a postgraduate student of Mass Communication and Journalism of Mangalore University , for alleged links with Maoists"
      },
      "relation": "caused",
      "effect": {
        "span": "Members of the Dakshina Kannada and Udupi district units of the Communist Party of India ( CPI ) staged a protest in front of the Deputy Commissioner 's office here on Friday condemning the BJP Government"
      }
    },
    {
      "cause": {
        "span": "alleged links with Maoists"
      },
      "relation": "caused",
      "effect": {
        "span": "arresting Vittala Malekudiya , a postgraduate student of Mass Communication and Journalism of Mangalore University"
      }
    }
  ]
}
```

### --- id=210 ---

输入文本: NATIONAL Rallies mark Nandigram anniversary March 15 , 2008 00:00 IST KOLKATA : Processions and rallies were taken out at Nandigram and here on Friday , first anniversary of the police firing and subsequent violence , which claimed 14 lives in the village in East Midnapore district .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "first anniversary of the police firing and subsequent violence",
      "effect": "Processions and rallies were taken out at Nandigram and here on Friday"
    },
    {
      "cause": "the police firing and subsequent violence",
      "effect": "which claimed 14 lives in the village in East Midnapore district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the police firing and subsequent violence"
      },
      "relation": "caused",
      "effect": {
        "span": "which claimed 14 lives in the village in East Midnapore district ."
      }
    }
  ]
}
```

### --- id=1700 ---

输入文本: Police said that they had clashed over the election of a new branch committee and the two were beaten to death with sticks and knobkerries .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "they had clashed over the election of a new branch committee",
      "effect": "the two were beaten to death with sticks and knobkerries"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over the election of a new branch committee"
      },
      "relation": "caused",
      "effect": {
        "span": "Police said that they had clashed"
      }
    },
    {
      "cause": {
        "span": "Police said that they had clashed over the election of a new branch committee"
      },
      "relation": "caused",
      "effect": {
        "span": "the two were beaten to death with sticks and knobkerries ."
      }
    }
  ]
}
```

### --- id=796 ---

输入文本: In a separate and extremely rare protest , more than 2,000 members of the legal profession marched against Beijing ’ s meddling in the local legal system .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against Beijing ’ s meddling in the local legal system",
      "effect": "In a separate and extremely rare protest , more than 2,000 members of the legal profession marched"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against Beijing ’ s meddling in the local legal system"
      },
      "relation": "caused",
      "effect": {
        "span": "more than 2,000 members of the legal profession marched"
      }
    }
  ]
}
```

### --- id=2475 ---

输入文本: Although the people who have organised these events try to blame the government for what has happened , a clear and strong message about such radical and irrational activities must be sent across society , not for the sake of our tourism or economy , but in defence of Hong Kong 's core values .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the people who have organised these events try to blame the government for what has happened",
      "effect": "a clear and strong message about such radical and irrational activities must be sent across society , not for the sake of our tourism or economy , but in defence of Hong Kong 's core values"
    },
    {
      "cause": "in defence of Hong Kong 's core values",
      "effect": "a clear and strong message about such radical and irrational activities must be sent across society"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "what has happened"
      },
      "relation": "caused",
      "effect": {
        "span": "the people who have organised these events try to blame the government"
      }
    },
    {
      "cause": {
        "span": "in defence of Hong Kong 's core values"
      },
      "relation": "caused",
      "effect": {
        "span": "a clear and strong message about such radical and irrational activities must be sent across society"
      }
    }
  ]
}
```

### --- id=2152 ---

输入文本: " This has led the department to conclude that I prompted the idea of an agitation among the inmates after the two officials were transferred , ' ' he said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "This",
      "effect": "the department to conclude that I prompted the idea of an agitation among the inmates after the two officials were transferred"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the two officials were transferred"
      },
      "relation": "caused",
      "effect": {
        "span": "I prompted the idea of an agitation among the inmates"
      }
    },
    {
      "cause": {
        "span": "I prompted the idea of an agitation among the inmates after the two officials were transferred"
      },
      "relation": "caused",
      "effect": {
        "span": "This has led the department to conclude"
      }
    }
  ]
}
```

### --- id=2425 ---

输入文本: Braving scorching sun , hundreds of people , including many women , led by Sri Mahanta Shivacharyaru of the Sulpul Math , Sri Rajashekar Shivacharyaru , Guru Mahanta Shivacharyaru of the Hiremath at Pala , Shivanda Swamigalu of Sonna Dasoha Math , Gangadhar Swamigalu of Chowdapur Math , Kanchi Basava Shivacharyaru of Roza Math , battery of Congress leaders including DCC president Allamprabhu Patil , MLC , the former Mayor Chandrika Parameshwar , zilla panchayat member Ambaraya Ashtagi , the former president of the HKCCI Umakant Nigudgi , Karnataka Rakshana Vedike president Arunkumar Patil , Hyderabad Karnataka Janapara Sangarsh Samiti Laxman Dasti and others marched from the Super Market to the Deputy Commissioner 's office to register their protest against the insensitive and indifferent attitude of the Government to the genuine demands of the pourakarmikas .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to register their protest against the insensitive and indifferent attitude of the Government to the genuine demands of the pourakarmikas",
      "effect": "hundreds of people , including many women , led by Sri Mahanta Shivacharyaru of the Sulpul Math , Sri Rajashekar Shivacharyaru , Guru Mahanta Shivacharyaru of the Hiremath at Pala , Shivanda Swamigalu of Sonna Dasoha Math , Gangadhar Swamigalu of Chowdapur Math , Kanchi Basava Shivacharyaru of Roza Math , battery of Congress leaders including DCC president Allamprabhu Patil , MLC , the former Mayor Chandrika Parameshwar , zilla panchayat member Ambaraya Ashtagi , the former president of the HKCCI Umakant Nigudgi , Karnataka Rakshana Vedike president Arunkumar Patil , Hyderabad Karnataka Janapara Sangarsh Samiti Laxman Dasti and others marched from the Super Market to the Deputy Commissioner 's office"
    },
    {
      "cause": "against the insensitive and indifferent attitude of the Government to the genuine demands of the pourakarmikas",
      "effect": "their protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to register their protest against the insensitive and indifferent attitude of the Government to the genuine demands of the pourakarmikas ."
      },
      "relation": "caused",
      "effect": {
        "span": "hundreds of people , including many women , led by Sri Mahanta Shivacharyaru of the Sulpul Math , Sri Rajashekar Shivacharyaru , Guru Mahanta Shivacharyaru of the Hiremath at Pala , Shivanda Swamigalu of Sonna Dasoha Math , Gangadhar Swamigalu of Chowdapur Math , Kanchi Basava Shivacharyaru of Roza Math , battery of Congress leaders including DCC president Allamprabhu Patil , MLC , the former Mayor Chandrika Parameshwar , zilla panchayat member Ambaraya Ashtagi , the former president of the HKCCI Umakant Nigudgi , Karnataka Rakshana Vedike president Arunkumar Patil , Hyderabad Karnataka Janapara Sangarsh Samiti Laxman Dasti and others marched from the Super Market to the Deputy Commissioner 's office"
      }
    }
  ]
}
```

### --- id=2391 ---

输入文本: KALPETTA : AIYF activists stall bank work November 24 , 2011 00:00 IST Activists under the Mananthavady taluk committee of the All India Youth Federation ( AIYF ) , the youth organisation of the Communist Party of India ( CPI ) , stalled work of the Mananthavady branch of Punjab National Bank on Wednesday in protest against the bank 's alleged move to appoint agencies to recover overdue loan amounts from farmers in the district .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "in protest against the bank 's alleged move to appoint agencies to recover overdue loan amounts from farmers in the district",
      "effect": "Activists under the Mananthavady taluk committee of the All India Youth Federation ( AIYF ) , the youth organisation of the Communist Party of India ( CPI ) , stalled work of the Mananthavady branch of Punjab National Bank on Wednesday"
    },
    {
      "cause": "to recover overdue loan amounts from farmers in the district",
      "effect": "the bank 's alleged move to appoint agencies"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the bank 's alleged move to appoint agencies to recover overdue loan amounts from farmers in the district"
      },
      "relation": "caused",
      "effect": {
        "span": "Activists under the Mananthavady taluk committee of the All India Youth Federation ( AIYF ) , the youth organisation of the Communist Party of India ( CPI ) , stalled work of the Mananthavady branch of Punjab National Bank on Wednesday"
      }
    }
  ]
}
```

### --- id=1096 ---

输入文本: JAC convenor M. Kodandaram , Telangana Rashtra Samithi ( TRS ) legislators K. Tarakarama Rao , E. Rajender and Harishwar Reddy were among dozens of leaders arrested by the police for staging protests on the highway despite police not giving permission for the same .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "staging protests on the highway despite police not giving permission for the same",
      "effect": "JAC convenor M. Kodandaram , Telangana Rashtra Samithi ( TRS ) legislators K. Tarakarama Rao , E. Rajender and Harishwar Reddy were among dozens of leaders arrested by the police"
    },
    {
      "cause": "police not giving permission for the same",
      "effect": "staging protests on the highway"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "for staging protests on the highway despite police not giving permission for the same"
      },
      "relation": "caused",
      "effect": {
        "span": "JAC convenor M. Kodandaram , Telangana Rashtra Samithi ( TRS ) legislators K. Tarakarama Rao , E. Rajender and Harishwar Reddy were among dozens of leaders arrested by the police"
      }
    }
  ]
}
```

### --- id=2185 ---

输入文本: September 24 , 2011 00:00 IST General strike to derail train services in Telangana All train services in the Telangana region are expected to stop from Saturday morning , signifying a virtual halt to every form of mass transport in the region as the Telangana Joint Action Committee ( T-JAC ) racheted up its agitation demanding a separate State .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to derail train services in Telangana",
      "effect": "General strike"
    },
    {
      "cause": "the Telangana Joint Action Committee ( T-JAC ) racheted up its agitation demanding a separate State",
      "effect": "All train services in the Telangana region are expected to stop from Saturday morning"
    },
    {
      "cause": "All train services in the Telangana region are expected to stop from Saturday morning",
      "effect": "signifying a virtual halt to every form of mass transport in the region"
    },
    {
      "cause": "demanding a separate State",
      "effect": "the Telangana Joint Action Committee ( T-JAC ) racheted up its agitation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding a separate State"
      },
      "relation": "caused",
      "effect": {
        "span": "the Telangana Joint Action Committee ( T-JAC ) racheted up its agitation"
      }
    },
    {
      "cause": {
        "span": "the Telangana Joint Action Committee ( T-JAC ) racheted up its agitation demanding a separate State"
      },
      "relation": "caused",
      "effect": {
        "span": "All train services in the Telangana region are expected to stop from Saturday morning"
      }
    }
  ]
}
```

### --- id=1985 ---

输入文本: KERALA Picketing held April 21 , 2010 00:00 IST KALPETTA : Congress activists picketed State government offices at six centres in the district on Tuesday as a part of a State-wide agitation by the Kerala Pradesh Congress Committee against the rise in prices of essential commodities .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "as a part of a State-wide agitation by the Kerala Pradesh Congress Committee",
      "effect": "Congress activists picketed State government offices at six centres in the district on Tuesday"
    },
    {
      "cause": "against the rise in prices of essential commodities",
      "effect": "a State-wide agitation by the Kerala Pradesh Congress Committee"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the rise in prices of essential commodities"
      },
      "relation": "caused",
      "effect": {
        "span": "Congress activists picketed State government offices at six centres in the district on Tuesday as a part of a State-wide agitation by the Kerala Pradesh Congress Committee"
      }
    }
  ]
}
```

### --- id=2573 ---

输入文本: Bank work hit by staff strike - Indian Express Express News Service , Express News Service : Faridkot / Moga , Thu Dec 17 2009 , 00:02 hrs Bank work remained paralysed in the region after the employees went on strike following a call given by the All India Bank Employees ' Union and the All India Bank Officers ' Association .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "staff strike",
      "effect": "Bank work hit"
    },
    {
      "cause": "the employees went on strike",
      "effect": "Bank work remained paralysed in the region"
    },
    {
      "cause": "a call given by the All India Bank Employees ' Union and the All India Bank Officers ' Association",
      "effect": "the employees went on strike"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the employees went on strike following a call given by the All India Bank Employees ' Union and the All India Bank Officers ' Association"
      },
      "relation": "caused",
      "effect": {
        "span": "Bank work remained paralysed in the region"
      }
    },
    {
      "cause": {
        "span": "a call given by the All India Bank Employees ' Union and the All India Bank Officers ' Association"
      },
      "relation": "caused",
      "effect": {
        "span": "the employees went on strike"
      }
    }
  ]
}
```

### --- id=1891 ---

输入文本: July 26 : A day later , it was Ahmedabad 's turn as 29 people were killed and over 100 hurt as 16 bombs went off in a space of 90 minutes .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "29 people were killed and over 100 hurt",
      "effect": "it was Ahmedabad 's turn"
    },
    {
      "cause": "16 bombs went off in a space of 90 minutes",
      "effect": "29 people were killed and over 100 hurt"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "16 bombs went off in a space of 90 minutes"
      },
      "relation": "caused",
      "effect": {
        "span": "29 people were killed and over 100 hurt"
      }
    }
  ]
}
```

### --- id=2161 ---

输入文本: ﻿In recent years , for instance , many retired military veterans have gathered together across the country in protests against the stingy benefits and pensions they receive from the state .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against the stingy benefits and pensions they receive from the state",
      "effect": "many retired military veterans have gathered together across the country in protests"
    },
    {
      "cause": "in protests against the stingy benefits and pensions they receive from the state",
      "effect": "many retired military veterans have gathered together across the country"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the stingy benefits and pensions they receive from the state"
      },
      "relation": "caused",
      "effect": {
        "span": "many retired military veterans have gathered together across the country in protests"
      }
    }
  ]
}
```

### --- id=598 ---

输入文本: Alongside the protests , there were also celebrations in different parts of the city to hail the decision .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to hail the decision",
      "effect": "Alongside the protests , there were also celebrations in different parts of the city"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to hail the decision"
      },
      "relation": "caused",
      "effect": {
        "span": "there were also celebrations in different parts of the city"
      }
    }
  ]
}
```

### --- id=2169 ---

输入文本: September 22 , 2016 00:00 IST Ahmad writes to Rajnath on violence by vigilante groups National Commission for Minorities ( NCM ) chairperson Naseem Ahmad has written to Union Home Minister Rajnath Singh , expressing concern at the growing violence against Muslims by vigilante groups and has urged the Minister to work towards creating a sense of security amongst the minorities .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "expressing concern at the growing violence against Muslims by vigilante groups and has urged the Minister to work towards creating a sense of security amongst the minorities",
      "effect": "National Commission for Minorities ( NCM ) chairperson Naseem Ahmad has written to Union Home Minister Rajnath Singh"
    },
    {
      "cause": "the growing violence against Muslims by vigilante groups",
      "effect": "expressing concern"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the growing violence against Muslims by vigilante groups"
      },
      "relation": "caused",
      "effect": {
        "span": "National Commission for Minorities ( NCM ) chairperson Naseem Ahmad has written to Union Home Minister Rajnath Singh , expressing concern"
      }
    },
    {
      "cause": {
        "span": "to work towards creating a sense of security amongst the minorities"
      },
      "relation": "caused",
      "effect": {
        "span": "has urged the Minister"
      }
    }
  ]
}
```

### --- id=2394 ---

输入文本: Police used rubber bullets to disperse a group of about 300 people protesting against poor service delivery in Landsdowne Road , Superintendent Riaan Pool said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to disperse a group of about 300 people protesting against poor service delivery in Landsdowne Road",
      "effect": "Police used rubber bullets"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to disperse a group of about 300 people protesting against poor service delivery in Landsdowne Road"
      },
      "relation": "caused",
      "effect": {
        "span": "Police used rubber bullets"
      }
    },
    {
      "cause": {
        "span": "against poor service delivery in Landsdowne Road"
      },
      "relation": "caused",
      "effect": {
        "span": "a group of about 300 people protesting"
      }
    }
  ]
}
```

### --- id=196 ---

输入文本: The escalating protests in the JNU follow the arrest of student union president Kanhaiya Kumar on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the arrest of student union president Kanhaiya Kumar",
      "effect": "The escalating protests in the JNU"
    },
    {
      "cause": "on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir",
      "effect": "the arrest of student union president Kanhaiya Kumar"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the arrest of student union president Kanhaiya Kumar on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir"
      },
      "relation": "caused",
      "effect": {
        "span": "The escalating protests in the JNU"
      }
    },
    {
      "cause": {
        "span": "that he too shouted the anti-Indian slogans at a meeting on Kashmir"
      },
      "relation": "caused",
      "effect": {
        "span": "the arrest of student union president Kanhaiya Kumar"
      }
    }
  ]
}
```

### --- id=2520 ---

输入文本: The police have denied allegations that they were targeting leaders of the student protests in order to thwart the ' # FeesMustFall ' campaign after the arrest of former Witwatersrand University Student Representative Council president Mcebo Dlamini .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to thwart the ' # FeesMustFall ' campaign",
      "effect": "they were targeting leaders of the student protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in order to thwart the ' # FeesMustFall ' campaign"
      },
      "relation": "caused",
      "effect": {
        "span": "they were targeting leaders of the student protests"
      }
    },
    {
      "cause": {
        "span": "after the arrest of former Witwatersrand University Student Representative Council president Mcebo Dlamini ."
      },
      "relation": "caused",
      "effect": {
        "span": "they were targeting leaders of the student protests in order to thwart the ' # FeesMustFall ' campaign"
      }
    }
  ]
}
```

### --- id=1474 ---

输入文本: After coming to power , the SP government , headed by Chief Minister Akhilesh Yadav , has now demonstrated that it meant business by issuing a notification seeking withdrawal of cases against those accused in the March 2006 Varanasi serial blasts , which had claimed 25 lives .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the SP government , headed by Chief Minister Akhilesh Yadav , has now demonstrated that it meant business",
      "effect": "issuing a notification seeking withdrawal of cases against those accused in the March 2006 Varanasi serial blasts"
    },
    {
      "cause": "seeking withdrawal of cases against those accused in the March 2006 Varanasi serial blasts",
      "effect": "issuing a notification"
    },
    {
      "cause": "the March 2006 Varanasi serial blasts",
      "effect": "which had claimed 25 lives"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "coming to power"
      },
      "relation": "caused",
      "effect": {
        "span": "the SP government , headed by Chief Minister Akhilesh Yadav , has now demonstrated that it meant business by issuing a notification seeking withdrawal of cases against those accused in the March 2006 Varanasi serial blasts"
      }
    },
    {
      "cause": {
        "span": "the March 2006 Varanasi serial blasts"
      },
      "relation": "caused",
      "effect": {
        "span": "which had claimed 25 lives ."
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=3014 ---

输入文本: When quizzed about the alleged police intimidation most of those who submitted claimed off-record that they had been individually helped by the police during riots and that yesterday , some officers did call them up and ask them to depose in their favour .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "quizzed about the alleged police intimidation",
      "effect": "most of those who submitted claimed off-record that they had been individually helped by the police during riots and that yesterday , some officers did call them up and ask them to depose in their favour"
    },
    {
      "cause": "and ask them to depose in their favour",
      "effect": "some officers did call them up"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "When quizzed about the alleged police intimidation"
      },
      "relation": "caused",
      "effect": {
        "span": "most of those who submitted claimed off-record that they had been individually helped by the police during riots and that yesterday , some officers did call them up and ask them to depose in their favour ."
      }
    }
  ]
}
```

### --- id=850 ---

输入文本: The SAHRC investigated Tatane 's death , during a protest in Ficksburg in April 2011 , followed a complaint by the Council for the Advancement of the SA Constitution .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "a complaint by the Council for the Advancement of the SA Constitution",
      "effect": "The SAHRC investigated Tatane 's death"
    },
    {
      "cause": "a protest in Ficksburg in April 2011",
      "effect": "Tatane 's death"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a complaint by the Council for the Advancement of the SA Constitution"
      },
      "relation": "caused",
      "effect": {
        "span": "The SAHRC investigated Tatane 's death , during a protest in Ficksburg in April 2011"
      }
    }
  ]
}
```

### --- id=2721 ---

输入文本: The police also issued a statement on Saturday reminding protesters that they were participating in an “ unauthorised assembly ” and could be punished with up to five years in prison .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "reminding protesters that they were participating in an “ unauthorised assembly ” and could be punished with up to five years in prison",
      "effect": "The police also issued a statement on Saturday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they were participating in an “ unauthorised assembly ”"
      },
      "relation": "caused",
      "effect": {
        "span": "could be punished with up to five years in prison"
      }
    }
  ]
}
```

### --- id=2346 ---

输入文本: The four inmates who held her hostage were arrested .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "The four inmates who held her hostage",
      "effect": "arrested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "who held her hostage"
      },
      "relation": "caused",
      "effect": {
        "span": "The four inmates who held her hostage were arrested ."
      }
    }
  ]
}
```

### --- id=1532 ---

输入文本: Around 30,000 truck drivers countrywide began striking for better pay on Tuesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "better pay on Tuesday",
      "effect": "Around 30,000 truck drivers countrywide began striking"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "for better pay"
      },
      "relation": "caused",
      "effect": {
        "span": "Around 30,000 truck drivers countrywide began striking"
      }
    }
  ]
}
```

### --- id=88 ---

输入文本: Some schools which had to postpone their mid-term examinations due to the bandh have the additional task of conducting the tests before resuming the classes .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the bandh",
      "effect": "Some schools which had to postpone their mid-term examinations"
    },
    {
      "cause": "Some schools which had to postpone their mid-term examinations",
      "effect": "have the additional task of conducting the tests before resuming the classes"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "due to the bandh"
      },
      "relation": "caused",
      "effect": {
        "span": "Some schools which had to postpone their mid-term examinations"
      }
    },
    {
      "cause": {
        "span": "postpone their mid-term examinations due to the bandh"
      },
      "relation": "caused",
      "effect": {
        "span": "Some schools which had to postpone their mid-term examinations due to the bandh have the additional task of conducting the tests before resuming the classes ."
      }
    }
  ]
}
```

### --- id=951 ---

输入文本: 28th March 2012 01:49 AM NEW DELHI : The Lok Sabha on Tuesday lashed out against Team Anna members for the intemperate language they used against Members of Parliament , and strongly condemned them for “ lowering the dignity of the House ” with the remarks they made during Anna Hazare ’ s one-day fast at Jantar Mantar on Sunday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the intemperate language they used against Members of Parliament",
      "effect": "The Lok Sabha on Tuesday lashed out against Team Anna members"
    },
    {
      "cause": "“ lowering the dignity of the House ”",
      "effect": "strongly condemned them"
    },
    {
      "cause": "the remarks they made during Anna Hazare ’ s one-day fast at Jantar Mantar on Sunday",
      "effect": "“ lowering the dignity of the House ”"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the intemperate language they used against Members of Parliament"
      },
      "relation": "caused",
      "effect": {
        "span": "The Lok Sabha on Tuesday lashed out against Team Anna members"
      }
    },
    {
      "cause": {
        "span": "“ lowering the dignity of the House ” with the remarks they made during Anna Hazare ’ s one-day fast at Jantar Mantar on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "strongly condemned them"
      }
    }
  ]
}
```

### --- id=1827 ---

输入文本: Others , opposing the movement , were bussed in on Sunday , August 17 , for a free lunch to participate in a march which occupied Central , thereby undermining their own argument .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "to participate in a march which occupied Central",
      "effect": "Others , opposing the movement , were bussed in on Sunday , August 17 , for a free lunch"
    },
    {
      "cause": "a free lunch to participate in a march which occupied Central",
      "effect": "Others , opposing the movement , were bussed in on Sunday , August 17"
    },
    {
      "cause": "Others , opposing the movement , were bussed in on Sunday , August 17 , for a free lunch to participate in a march which occupied Central",
      "effect": "undermining their own argument"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "opposing the movement"
      },
      "relation": "caused",
      "effect": {
        "span": "Others , opposing the movement , were bussed in on Sunday, August 17 , for a free lunch to participate in a march which occupied Central"
      }
    },
    {
      "cause": {
        "span": "to participate in a march which occupied Central"
      },
      "relation": "caused",
      "effect": {
        "span": "Others , opposing the movement , were bussed in on Sunday, August 17 , for a free lunch"
      }
    },
    {
      "cause": {
        "span": "a march which occupied Central"
      },
      "relation": "caused",
      "effect": {
        "span": "thereby undermining their own argument ."
      }
    }
  ]
}
```

### --- id=1783 ---

输入文本: Haryana had been on the boil for nearly a fortnight last month as protesters agitating for reservation to the Jat community in government jobs went on rampage and blocked road and rail routes at several places .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "protesters agitating for reservation to the Jat community in government jobs went on rampage and blocked road and rail routes at several places",
      "effect": "Haryana had been on the boil for nearly a fortnight last month"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "protesters agitating for reservation to the Jat community in government jobs went on rampage and blocked road and rail routes at several places"
      },
      "relation": "caused",
      "effect": {
        "span": "Haryana had been on the boil for nearly a fortnight last month"
      }
    },
    {
      "cause": {
        "span": "for reservation to the Jat community in government jobs"
      },
      "relation": "caused",
      "effect": {
        "span": "protesters agitating for reservation to the Jat community in government jobs went on rampage and blocked road and rail routes at several places"
      }
    }
  ]
}
```

### --- id=1745 ---

输入文本: 02nd September 2010 04:30 AM HYDERABAD : Medical services were affected at Gandhi General Hospital ( GGH ) here on Wednesday following a flash strike by postgraduate , undergraduate and intern doctors demanding immediate suspension of the hospital superintendent and the resident medical officer-I ( RMO ) for their alleged irregularities in the name of hospital development .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "flash strike by postgraduate , undergraduate and intern doctors",
      "effect": "Medical services were affected at Gandhi General Hospital ( GGH ) here on Wednesday"
    },
    {
      "cause": "demanding immediate suspension of the hospital superintendent and the resident medical officer-I ( RMO )",
      "effect": "flash strike by postgraduate , undergraduate and intern doctors"
    },
    {
      "cause": "their alleged irregularities",
      "effect": "demanding immediate suspension of the hospital superintendent and the resident medical officer-I ( RMO )"
    },
    {
      "cause": "hospital development",
      "effect": "their alleged irregularities"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a flash strike by postgraduate , undergraduate and intern doctors demanding immediate suspension of the hospital superintendent and the resident medical officer-I ( RMO ) for their alleged irregularities in the name of hospital development"
      },
      "relation": "caused",
      "effect": {
        "span": "Medical services were affected at Gandhi General Hospital ( GGH ) here on Wednesday"
      }
    },
    {
      "cause": {
        "span": "their alleged irregularities in the name of hospital development"
      },
      "relation": "caused",
      "effect": {
        "span": "demanding immediate suspension of the hospital superintendent and the resident medical officer-I ( RMO )"
      }
    }
  ]
}
```

### --- id=2438 ---

输入文本: The protesters raised slogans against the State Government and the police for arresting nearly 70 Dalits after an incident in which stones were thrown at the police personnel at Tarfail slum .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "against the State Government and the police for arresting nearly 70 Dalits after an incident in which stones were thrown at the police personnel at Tarfail slum",
      "effect": "The protesters raised slogans"
    },
    {
      "cause": "an incident in which stones were thrown at the police personnel at Tarfail slum",
      "effect": "the police for arresting nearly 70 Dalits"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "arresting nearly 70 Dalits after an incident in which stones were thrown at the police personnel at Tarfail slum"
      },
      "relation": "caused",
      "effect": {
        "span": "The protesters raised slogans against the State Government and the police"
      }
    },
    {
      "cause": {
        "span": "an incident in which stones were thrown at the police personnel at Tarfail slum"
      },
      "relation": "caused",
      "effect": {
        "span": "arresting nearly 70 Dalits"
      }
    }
  ]
}
```

### --- id=3035 ---

输入文本: Evicted vendors stage demo 10th May 2013 11:36 AM Hundreds of roadside vendors under the banner of the Sambalpur Utha Dokani Sangha staged a demonstration in front of the office of the DIG ( NR ) on Wednesday in protest against selective eviction of vendors in front of Sambalpur Town police station and demanded their rehabilitation .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "in protest against selective eviction of vendors in front of Sambalpur Town police station",
      "effect": "Hundreds of roadside vendors under the banner of the Sambalpur Utha Dokani Sangha staged a demonstration in front of the office of the DIG ( NR ) on Wednesday"
    },
    {
      "cause": "against selective eviction of vendors in front of Sambalpur Town police station",
      "effect": "demanded their rehabilitation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against selective eviction of vendors in front of Sambalpur Town police station"
      },
      "relation": "caused",
      "effect": {
        "span": "Hundreds of roadside vendors under the banner of the Sambalpur Utha Dokani Sangha staged a demonstration in front of the office of the DIG ( NR ) on Wednesday"
      }
    },
    {
      "cause": {
        "span": "demanded their rehabilitation"
      },
      "relation": "caused",
      "effect": {
        "span": "Hundreds of roadside vendors under the banner of the Sambalpur Utha Dokani Sangha staged a demonstration in front of the office of the DIG ( NR ) on Wednesday"
      }
    }
  ]
}
```

### --- id=1441 ---

输入文本: During the previous voter registration weekend last month , some IEC staff had to be withdrawn from communities on police recommendation due to safety concerns sparked by protests .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "safety concerns sparked by protests",
      "effect": "some IEC staff had to be withdrawn from communities on police recommendation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "safety concerns sparked by protests"
      },
      "relation": "caused",
      "effect": {
        "span": "some IEC staff had to be withdrawn from communities on police recommendation"
      }
    },
    {
      "cause": {
        "span": "protests"
      },
      "relation": "caused",
      "effect": {
        "span": "safety concerns sparked by protests"
      }
    }
  ]
}
```

### --- id=1913 ---

输入文本: January 26 : CPI-Maoist cadres shot dead three persons , accusing them of being police spies , at Borlagunda village in Andhra Pradesh 's Karimnagar district .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "accusing them of being police spies , at Borlagunda village in Andhra Pradesh 's Karimnagar district",
      "effect": "CPI-Maoist cadres shot dead three persons"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "accusing them of being police spies"
      },
      "relation": "caused",
      "effect": {
        "span": "CPI-Maoist cadres shot dead three persons , accusing them of being police spies , at Borlagunda village in Andhra Pradesh 's Karimnagar district ."
      }
    }
  ]
}
```

### --- id=843 ---

输入文本: Seeking to allay apprehensions of the students who feared that the agitation will have a bearing on their academic performance as exams are due , the Union Minister said the HRD team will stay at NIT Srinagar till exams , which begin on April 11 , are not over .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "who feared that the agitation will have a bearing on their academic performance",
      "effect": "apprehensions of the students"
    },
    {
      "cause": "exams are due",
      "effect": "who feared that the agitation will have a bearing on their academic performance"
    },
    {
      "cause": "Seeking to allay apprehensions of the students who feared that the agitation will have a bearing on their academic performance as exams are due",
      "effect": "the Union Minister said the HRD team will stay at NIT Srinagar till exams , which begin on April 11 , are not over"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Seeking to allay apprehensions of the students who feared that the agitation will have a bearing on their academic performance as exams are due"
      },
      "relation": "caused",
      "effect": {
        "span": "the Union Minister said the HRD team will stay at NIT Srinagar till exams , which begin on April 11 , are not over ."
      }
    },
    {
      "cause": {
        "span": "as exams are due"
      },
      "relation": "caused",
      "effect": {
        "span": "the students who feared that the agitation will have a bearing on their academic performance"
      }
    }
  ]
}
```

### --- id=2267 ---

输入文本: These aspirations were behind the series of demonstrations and rallies held last Sunday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "These aspirations",
      "effect": "were behind the series of demonstrations and rallies held last Sunday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "These aspirations"
      },
      "relation": "caused",
      "effect": {
        "span": "the series of demonstrations and rallies held last Sunday"
      }
    }
  ]
}
```

### --- id=2473 ---

输入文本: The scenes are getting more and more ugly and disturbing , with shops being forced to close and people who are not parallel traders being molested and bullied .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "shops being forced to close and people who are not parallel traders being molested and bullied",
      "effect": "The scenes are getting more and more ugly and disturbing"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The scenes are getting more and more ugly and disturbing"
      },
      "relation": "caused",
      "effect": {
        "span": "with shops being forced to close"
      }
    },
    {
      "cause": {
        "span": "The scenes are getting more and more ugly and disturbing"
      },
      "relation": "caused",
      "effect": {
        "span": "people who are not parallel traders being molested and bullied ."
      }
    }
  ]
}
```

### --- id=1942 ---

输入文本: Rights groups for review of sedition law - Indian Express Express News Service , Express News Service : Jaipur , Sat Jan 01 2011 , 09:27 hrs Civil rights organisations and Left parties on Friday staged a protest rally , demanding review of sedition law , repeal of the controversial Chhattisgarh Special Public Security Act , and unconditional release of Binayak Sen , who was sentenced to life by a trial court on the charges of sedition for ' helping the Maoists ' .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding review of sedition law , repeal of the controversial Chhattisgarh Special Public Security Act , and unconditional release of Binayak Sen",
      "effect": "Civil rights organisations and Left parties on Friday staged a protest rally"
    },
    {
      "cause": "on the charges of sedition for ' helping the Maoists '",
      "effect": "Binayak Sen , who was sentenced to life by a trial court"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding review of sedition law , repeal of the controversial Chhattisgarh Special Public Security Act , and unconditional release of Binayak Sen"
      },
      "relation": "caused",
      "effect": {
        "span": "Civil rights organisations and Left parties on Friday staged a protest rally"
      }
    },
    {
      "cause": {
        "span": "for ' helping the Maoists '"
      },
      "relation": "caused",
      "effect": {
        "span": "who was sentenced to life by a trial court on the charges of sedition"
      }
    }
  ]
}
```

### --- id=2022 ---

输入文本: Senior Congress leader Narsingh Mishra said the massive turnout at the rally showed that the people want a change .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the people want a change",
      "effect": "the massive turnout at the rally"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the massive turnout at the rally"
      },
      "relation": "caused",
      "effect": {
        "span": "showed that the people want a change"
      }
    }
  ]
}
```

### --- id=465 ---

输入文本: While private bus operators are running only a limited number of services , many school managements have closed the institutions to mark their protest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to mark their protest",
      "effect": "many school managements have closed the institutions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to mark their protest"
      },
      "relation": "caused",
      "effect": {
        "span": "many school managements have closed the institutions"
      }
    },
    {
      "cause": {
        "span": "While private bus operators are running only a limited number of services"
      },
      "relation": "caused",
      "effect": {
        "span": "many school managements have closed the institutions to mark their protest ."
      }
    }
  ]
}
```

### --- id=421 ---

输入文本: The Indian Medical Association has , while condemning the incident , decided that a more trenchant protest needs to be made against the increasing attacks on the medical community .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against the increasing attacks on the medical community",
      "effect": "a more trenchant protest needs to be made"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "The Indian Medical Association has , while condemning the incident , decided that a more trenchant protest needs to be made against the increasing attacks on the medical community ."
      }
    },
    {
      "cause": {
        "span": "against the increasing attacks on the medical community"
      },
      "relation": "caused",
      "effect": {
        "span": "a more trenchant protest needs to be made"
      }
    }
  ]
}
```

### --- id=637 ---

输入文本: Thackeray , however , said if the exam was not deferred care would be taken to ensure it is not affected by the strike .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the exam was not deferred",
      "effect": "care would be taken to ensure it is not affected by the strike"
    },
    {
      "cause": "to ensure it is not affected by the strike",
      "effect": "care would be taken"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "if the exam was not deferred"
      },
      "relation": "caused",
      "effect": {
        "span": "care would be taken to ensure it is not affected by the strike"
      }
    },
    {
      "cause": {
        "span": "the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "it is not affected by the strike"
      }
    }
  ]
}
```

### --- id=205 ---

输入文本: December 06 , 2017 00:00 IST Urge Central government to drop privatisation move A day after alleged suicide by one of their colleagues , the employees , including officers , went on a mass casual leave on Tuesday to press for their demand to withdraw decision on privatisation of Dredging Corporation of India ( DCI ) .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to press for their demand to withdraw decision on privatisation of Dredging Corporation of India ( DCI )",
      "effect": "the employees , including officers , went on a mass casual leave on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "alleged suicide by one of their colleagues"
      },
      "relation": "caused",
      "effect": {
        "span": "the employees , including officers , went on a mass casual leave on Tuesday"
      }
    },
    {
      "cause": {
        "span": "to press for their demand to withdraw decision on privatisation of Dredging Corporation of India ( DCI )"
      },
      "relation": "caused",
      "effect": {
        "span": "the employees , including officers , went on a mass casual leave on Tuesday"
      }
    }
  ]
}
```

### --- id=2587 ---

输入文本: Lalu , Rabri upbeat after success of shutdown 29th January 2010 01:40 PM An RJD activist wears a garland and crown made of vegetables and shouts slogans along with others during a protest against inflation in Patna .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against inflation in Patna",
      "effect": "An RJD activist wears a garland and crown made of vegetables and shouts slogans along with others during a protest"
    },
    {
      "cause": "during a protest against inflation in Patna",
      "effect": "An RJD activist wears a garland and crown made of vegetables and shouts slogans along with others"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "success of shutdown"
      },
      "relation": "caused",
      "effect": {
        "span": "Rabri upbeat"
      }
    },
    {
      "cause": {
        "span": "against inflation in Patna"
      },
      "relation": "caused",
      "effect": {
        "span": "An RJD activist wears a garland and crown made of vegetables and shouts slogans along with others during a protest"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=588 ---

输入文本: The murders evoked widespread protest with people speaking out openly against Baruah and demanding stringent action against the perpetrators of the crime .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "The murders",
      "effect": "widespread protest with people speaking out openly against Baruah and demanding stringent action against the perpetrators of the crime"
    },
    {
      "cause": "against Baruah and demanding stringent action against the perpetrators of the crime",
      "effect": "widespread protest with people speaking out openly"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The murders"
      },
      "relation": "caused",
      "effect": {
        "span": "evoked widespread protest with people speaking out openly against Baruah and demanding stringent action against the perpetrators of the crime ."
      }
    },
    {
      "cause": {
        "span": "against Baruah"
      },
      "relation": "caused",
      "effect": {
        "span": "people speaking out openly"
      }
    },
    {
      "cause": {
        "span": "demanding stringent action against the perpetrators of the crime"
      },
      "relation": "caused",
      "effect": {
        "span": "people speaking out openly"
      }
    }
  ]
}
```

### --- id=3066 ---

输入文本: He said that Leader of the Opposition Oommen Chandy was worried about the arrest of Akhil Bharatiya Vidyarthi Parishad workers in connection with the killing immediately after the incident .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the killing",
      "effect": "the arrest of Akhil Bharatiya Vidyarthi Parishad workers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the arrest of Akhil Bharatiya Vidyarthi Parishad workers in connection with the killing immediately after the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "He said that Leader of the Opposition Oommen Chandy was worried"
      }
    }
  ]
}
```

### --- id=596 ---

输入文本: People have been forced to come out on the streets to protest the conspiracy to dislodge my government , " said Modi while demanding that she should be recalled .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to protest the conspiracy",
      "effect": "People have been forced to come out on the streets"
    },
    {
      "cause": "to dislodge my government",
      "effect": "to protest the conspiracy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the conspiracy to dislodge my government"
      },
      "relation": "caused",
      "effect": {
        "span": "People have been forced to come out on the streets to protest"
      }
    },
    {
      "cause": {
        "span": "to protest the conspiracy to dislodge my government"
      },
      "relation": "caused",
      "effect": {
        "span": "People have been forced to come out on the streets"
      }
    }
  ]
}
```

### --- id=945 ---

输入文本: But with the agitation in full swing and disturbances on the campus , they were further postponed .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "But with the agitation in full swing and disturbances on the campus",
      "effect": "they were further postponed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "with the agitation in full swing and disturbances on the campus"
      },
      "relation": "caused",
      "effect": {
        "span": "they were further postponed ."
      }
    }
  ]
}
```

### --- id=2295 ---

输入文本: At least 44 persons were killed , about 4,800 houses burnt or damaged leaving about 20,000 people homeless during the riot that broke out immediately after Saraswati 's killing on the night of Janmastami ( August 23 , 2008 ) .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "the riot that broke out immediately after Saraswati 's killing on the night of Janmastami ( August 23 , 2008 )",
      "effect": "At least 44 persons were killed , about 4,800 houses burnt or damaged leaving about 20,000 people homeless"
    },
    {
      "cause": "about 4,800 houses burnt or damaged",
      "effect": "about 20,000 people homeless during the riot that broke out immediately after Saraswati 's killing on the night of Janmastami ( August 23 , 2008 )"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the riot that broke out immediately after Saraswati 's killing on the night of Janmastami ( August 23 , 2008 )"
      },
      "relation": "caused",
      "effect": {
        "span": "At least 44 persons were killed"
      }
    },
    {
      "cause": {
        "span": "the riot that broke out immediately after Saraswati 's killing on the night of Janmastami ( August 23 , 2008 )"
      },
      "relation": "caused",
      "effect": {
        "span": "about 4,800 houses burnt or damaged"
      }
    },
    {
      "cause": {
        "span": "about 4,800 houses burnt or damaged"
      },
      "relation": "caused",
      "effect": {
        "span": "leaving about 20,000 people homeless"
      }
    },
    {
      "cause": {
        "span": "Saraswati 's killing on the night of Janmastami ( August 23 , 2008 )"
      },
      "relation": "caused",
      "effect": {
        "span": "the riot that broke out immediately after Saraswati 's killing on the night of Janmastami ( August 23 , 2008 )"
      }
    }
  ]
}
```

### --- id=2675 ---

输入文本: At Virudhunagar , the peravai ’ s district president , K.G.N. Kanagarathinam , who led the protest , flayed the successive State governments which promised to allow toddy tapping before elections and reversed their decision after coming to power .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "which promised to allow toddy tapping before elections and reversed their decision after coming to power",
      "effect": "the peravai ’ s district president , K.G.N. Kanagarathinam , who led the protest , flayed the successive State governments"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "which promised to allow toddy tapping before elections and reversed their decision after coming to power"
      },
      "relation": "caused",
      "effect": {
        "span": "the peravai ’ s district president , K.G.N. Kanagarathinam , who led the protest , flayed the successive State governments"
      }
    },
    {
      "cause": {
        "span": "coming to power"
      },
      "relation": "caused",
      "effect": {
        "span": "reversed their decision"
      }
    }
  ]
}
```

### --- id=2616 ---

输入文本: Army officials said that the five-member team , which included Lt Col Ajay Kumar Verma , GREF engineer S K Singh , a protection force of two Army jawans from the JAKRIF regiment and their driver , was on its way to inspect construction work on the Chattroo-Simthan road when it came under heavy fire .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the five-member team , which included Lt Col Ajay Kumar Verma , GREF engineer S K Singh , a protection force of two Army jawans from the JAKRIF regiment and their driver , was on its way to inspect construction work on the Chattroo-Simthan road",
      "effect": "it came under heavy fire"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "it came under heavy fire"
      },
      "relation": "caused",
      "effect": {
        "span": "Army officials said that the five-member team , which included Lt Col Ajay Kumar Verma , GREF engineer S K Singh , a protection force of two Army jawans from the JAKRIF regiment and their driver , was on its way to inspect construction work on the Chattroo-Simthan road"
      }
    }
  ]
}
```

### --- id=2226 ---

输入文本: Violence over cut in water supply 04th December 2009 02:16 AM A boy holding an empty bucket participates along with others in a protest against water shortage in Mumbai India Thursday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "against water shortage in Mumbai India Thursday",
      "effect": "A boy holding an empty bucket participates along with others in a protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cut in water supply"
      },
      "relation": "caused",
      "effect": {
        "span": "Violence"
      }
    },
    {
      "cause": {
        "span": "against water shortage in Mumbai India Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "A boy holding an empty bucket participates along with others in a protest"
      }
    }
  ]
}
```

### --- id=2619 ---

输入文本: The Army and police have now launched extensive combing operations in the area to flush out the terrorists who managed to escape in dense forests after carrying out the attack .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "who managed to escape in dense forests after carrying out the attack",
      "effect": "The Army and police have now launched extensive combing operations in the area to flush out the terrorists"
    },
    {
      "cause": "to flush out the terrorists who managed to escape in dense forests after carrying out the attack",
      "effect": "The Army and police have now launched extensive combing operations in the area"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to flush out the terrorists who managed to escape in dense forests after carrying out the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "The Army and police have now launched extensive combing operations in the area"
      }
    },
    {
      "cause": {
        "span": "after carrying out the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "the terrorists who managed to escape in dense forests"
      }
    }
  ]
}
```

### --- id=797 ---

输入文本: Additional forces were deployed in sensitive areas a day after four persons were killed and 44 others , including security personnel , injured in stone-pelting and resultant firing when a mob attacked a BSF camp in Ramban district over alleged high-handedness by a BSF team .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 2,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "a day after four persons were killed and 44 others , including security personnel , injured in stone-pelting and resultant firing when a mob attacked a BSF camp in Ramban district over alleged high-handedness by a BSF team",
      "effect": "Additional forces were deployed in sensitive areas"
    },
    {
      "cause": "stone-pelting and resultant firing",
      "effect": "four persons were killed and 44 others , including security personnel , injured"
    },
    {
      "cause": "a mob attacked a BSF camp in Ramban district",
      "effect": "stone-pelting and resultant firing"
    },
    {
      "cause": "alleged high-handedness by a BSF team",
      "effect": "a mob attacked a BSF camp in Ramban district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "four persons were killed and 44 others , including security personnel , injured in stone-pelting and resultant firing when a mob attacked a BSF camp in Ramban district over alleged high-handedness by a BSF team"
      },
      "relation": "caused",
      "effect": {
        "span": "Additional forces were deployed in sensitive areas a day after"
      }
    },
    {
      "cause": {
        "span": "a mob attacked a BSF camp in Ramban district over alleged high-handedness by a BSF team"
      },
      "relation": "caused",
      "effect": {
        "span": "four persons were killed and 44 others , including security personnel , injured in stone-pelting and resultant firing"
      }
    },
    {
      "cause": {
        "span": "over alleged high-handedness by a BSF team"
      },
      "relation": "caused",
      "effect": {
        "span": "a mob attacked a BSF camp in Ramban district"
      }
    },
    {
      "cause": {
        "span": "stone-pelting"
      },
      "relation": "caused",
      "effect": {
        "span": "resultant firing"
      }
    }
  ]
}
```

### --- id=390 ---

输入文本: MC officials beat hasty retreat as mob attacks team - Indian Express Express News Service , Express News Service : Kharar , Wed Mar 18 2009 , 03:33 hrs Officials of the Kharar Municipal Council , on an anti-encroachment drive at Santemajra village , had to duck for cover following a fierce attack by residents on Tuesday evening .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "mob attacks team",
      "effect": "MC officials beat hasty retreat"
    },
    {
      "cause": "a fierce attack by residents on Tuesday evening",
      "effect": "Officials of the Kharar Municipal Council , on an anti-encroachment drive at Santemajra village , had to duck for cover"
    },
    {
      "cause": "cover",
      "effect": "Officials of the Kharar Municipal Council , on an anti-encroachment drive at Santemajra village , had to duck"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "following a fierce attack by residents on Tuesday evening"
      },
      "relation": "caused",
      "effect": {
        "span": "Officials of the Kharar Municipal Council , on an anti-encroachment drive at Santemajra village , had to duck for cover"
      }
    }
  ]
}
```
