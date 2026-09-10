# gemma4-12b-overfit20-base CNC SFT overfit20_train eval report

## 配置
```json
{
  "label": "gemma4-12b-overfit20-base CNC SFT overfit20_train",
  "model": "gemma4-12b-overfit20-base",
  "dataset": "cnc_gemma12_overfit20_train",
  "sample_count": 20,
  "prompt_name": "cnc_gemma_v2",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 0,
  "temperature": 0.0,
  "max_tokens": 512,
  "primary_metric": "anchor_window",
  "progress_every": 10,
  "max_workers": 1,
  "llm_provider": "openai_compatible",
  "llm_base_url": "http://127.0.0.1:8001/v1",
  "context_length": null,
  "reasoning_effort": null,
  "llm_extra_body": null,
  "api_key_source": "local direct Unsloth API",
  "report_detail_limit": 200,
  "report_detail_mode": "errors",
  "report_error_metric": "anchor_window",
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ gemma4-12b-overfit20-base CNC SFT overfit20_train final report ================
样本总数: 20
  Gold 含因果: 10 | Pred 含因果: 13
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.650
  Precision: 0.615
  Recall   : 0.800
  F1       : 0.696
  (TP=8, TN=5, FP=5, FN=2)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 20
    Gold triples: 14 | Pred triples: 18
    Precision: 0.056
    Recall   : 0.071
    F1       : 0.062
    (TP=1, FP=17, FN=13)
  [anchor_window] (primary)
    样本数: 20
    Gold triples: 14 | Pred triples: 18
    Precision: 0.056
    Recall   : 0.071
    F1       : 0.062
    (TP=1, FP=17, FN=13)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 8
    Gold triples: 11 | Pred triples: 13
    Precision: 0.077
    Recall   : 0.091
    F1       : 0.083
    (TP=1, FP=12, FN=10)
  [anchor_window] (primary)
    样本数: 8
    Gold triples: 11 | Pred triples: 13
    Precision: 0.077
    Recall   : 0.091
    F1       : 0.083
    (TP=1, FP=12, FN=10)
================================================
```

## 生成失败统计
```json
{
  "total": 4,
  "by_type": {
    "no_json_object": 1,
    "invalid_json_syntax": 3
  },
  "samples": [
    {
      "id": 2854,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    },
    {
      "id": 849,
      "error_type": "invalid_json_syntax",
      "error_message": "Expecting ',' delimiter: line 1 column 137 (char 136)"
    },
    {
      "id": 1601,
      "error_type": "invalid_json_syntax",
      "error_message": "Expecting ',' delimiter: line 1 column 168 (char 167)"
    },
    {
      "id": 535,
      "error_type": "invalid_json_syntax",
      "error_message": "Expecting ',' delimiter: line 1 column 334 (char 333)"
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

Sample details shown: all 16 wrong samples from 20 total samples.

### --- id=2854 ---

输入文本: Even the merchants and brokers operating outside the APMC yards in various towns and cities closed the shutters of their shops in response to the bandh .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the bandh",
      "effect": "the merchants and brokers operating outside the APMC yards in various towns and cities closed the shutters of their shops"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
}
```

### --- id=503 ---

输入文本: While two persons received bullet injuries , another man was injured in stone pelting .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "two persons received bullet injuries"
      },
      "relation": "caused",
      "effect": {
        "span": "another man was injured in stone pelting"
      }
    }
  ]
}
```

### --- id=1707 ---

输入文本: According to police , one person was arrested for public violence on Saturday after about 70 protesting residents stoned a car and attempted to blockade roads in Goedgevonden .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "about 70 protesting residents stoned a car and attempted to blockade roads in Goedgevonden",
      "effect": "one person was arrested for public violence on Saturday"
    },
    {
      "cause": "public violence",
      "effect": "one person was arrested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "one person was arrested"
      },
      "relation": "caused",
      "effect": {
        "span": "for public violence"
      }
    },
    {
      "cause": {
        "span": "protesting"
      },
      "relation": "caused",
      "effect": {
        "span": "stoned a car"
      }
    },
    {
      "cause": {
        "span": "attempted to blockade roads"
      },
      "relation": "caused",
      "effect": {
        "span": "in Goedgevonden"
      }
    }
  ]
}
```

### --- id=849 ---

输入文本: They waved placards with slogans such as `` Justice must be done '' and `` Stop killing our mothers '' .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "invalid_json_syntax",
  "generation_error_message": "Expecting ',' delimiter: line 1 column 137 (char 136)"
}
```

### --- id=1355 ---

输入文本: They refused to disperse and threw stones at the police who then opened fire , killing and injuring some of the learners .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "They refused to disperse and threw stones at the police",
      "effect": "who then opened fire"
    },
    {
      "cause": "who then opened fire",
      "effect": "killing and injuring some of the learners"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "refused to disperse"
      },
      "relation": "caused",
      "effect": {
        "span": "threw stones at the police"
      }
    },
    {
      "cause": {
        "span": "threw stones at the police"
      },
      "relation": "caused",
      "effect": {
        "span": "opened fire"
      }
    },
    {
      "cause": {
        "span": "opened fire"
      },
      "relation": "caused",
      "effect": {
        "span": "killing and injuring some of the learners"
      }
    }
  ]
}
```

### --- id=620 ---

输入文本: A group of farmers pointed protesting residents with guns when they were walking home from court , and other group of farmers attacked journalist after a farm house was looted and torched .

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
      "cause": "a farm house was looted and torched",
      "effect": "other group of farmers attacked journalist"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "protesting residents with guns"
      },
      "relation": "caused",
      "effect": {
        "span": "journalist attacked"
      }
    },
    {
      "cause": {
        "span": "farm house was looted and torched"
      },
      "relation": "caused",
      "effect": {
        "span": "journalist attacked"
      }
    }
  ]
}
```

### --- id=1601 ---

输入文本: In all , about 150 activists proceeding towards Hyderabad were detained by police on Thursday morning .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [],
  "generation_error_type": "invalid_json_syntax",
  "generation_error_message": "Expecting ',' delimiter: line 1 column 168 (char 167)"
}
```

### --- id=1209 ---

输入文本: While Mamata Banerjee participated in her padayatra , her arch political rival and West Bengal Chief Minister Buddhadeb Bhattacharjee confined himself with an interactive session with the students on a college campus in Garia , Southern part of the city to get their support .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "While Mamata Banerjee participated in her padayatra"
      },
      "relation": "caused",
      "effect": {
        "span": "her arch political rival and West Bengal Chief Minister Buddhadeb Bhattacharjee confined himself with an interactive session with the students on a college campus in Garia , Southern part of the city to get their support."
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
        "span": "Two protestors were shot dead"
      },
      "relation": "caused",
      "effect": {
        "span": "allegedly by police"
      }
    }
  ]
}
```

### --- id=535 ---

输入文本: Deo warned that the nation would witness " worse consequences " if the Naxalite issue is treated as a mere law and order problem , just days after his colleague Union Rural Development Minister Jairam Ramesh termed them as " terrorists " after the May 25 bloodbath .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
      "cause": "the Naxalite issue is treated as a mere law and order problem",
      "effect": "the nation would witness \" worse consequences \""
    },
    {
      "cause": "the May 25 bloodbath",
      "effect": "his colleague Union Rural Development Minister Jairam Ramesh termed them as \" terrorists \""
    }
  ],
  "pred_triples": [],
  "generation_error_type": "invalid_json_syntax",
  "generation_error_message": "Expecting ',' delimiter: line 1 column 334 (char 333)"
}
```

### --- id=2868 ---

输入文本: In the evening , activists attached to the Untouchability Movement staged a similar agitation in Udumalpet .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "activists attached to the Untouchability Movement"
      },
      "relation": "caused",
      "effect": {
        "span": "staged a similar agitation in Udumalpet"
      }
    }
  ]
}
```

### --- id=1349 ---

输入文本: Besides , Jaya , a woman from the Vanniyar community , said the day after the incident , police had said they had so far booked around 150 Vanniyars and remanded about 85 .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "police had said they had so far booked around 150 Vanniyars and remanded about 85."
      }
    }
  ]
}
```

### --- id=2872 ---

输入文本: Opposing the Pakistan premier 's visit that was marked by tight security , local lawyers , some BJP activists and representatives of markets associations staged protests and shouted anti-Pakistan slogans .

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
      "cause": "Opposing the Pakistan premier 's visit that was marked by tight security",
      "effect": "local lawyers , some BJP activists and representatives of markets associations staged protests and shouted anti-Pakistan slogans"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Opposing the Pakistan premier's visit"
      },
      "relation": "caused",
      "effect": {
        "span": "tight security, local lawyers, some BJP activists and representatives of markets associations staged protests and shouted anti-Pakistan slogans."
      }
    }
  ]
}
```

### --- id=1276 ---

输入文本: Following this , the Caste Hindu youths ( Kallar ) allegedly attacked an Arunthathiyar community member P Pandi Kumar , a sweeper , while he was on his way to Nagamalai Pudukottai .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "allegedly attacked"
      },
      "effect": {
        "span": "a Arunthathiyar community member P Pandi Kumar, a sweeper"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2864 ---

输入文本: Chinnasamy , father-in-law of V. Shankar ( 22 ) , the Dalit youth who was hacked to death in broad daylight in a suspected honour killing in Udumalpet on Sunday , surrendered before the Judicial Magistrate Court in Nilakottai , Dindigul district on Monday .

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
      "cause": "a suspected honour killing in Udumalpet on Sunday",
      "effect": "V. Shankar ( 22 ) , the Dalit youth who was hacked to death in broad daylight"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Dalit youth who was hacked"
      },
      "effect": {
        "span": "to death"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2178 ---

输入文本: The organisers then signed a petition demanding strict legal action against the accused which would be sent to the Delhi CM , PM , and Home Minister .

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
      "cause": "demanding strict legal action against the accused",
      "effect": "The organisers then signed a petition"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "petition demanding strict legal action"
      },
      "relation": "caused",
      "effect": {
        "span": "the Delhi CM , PM , and Home Minister"
      }
    }
  ]
}
```
