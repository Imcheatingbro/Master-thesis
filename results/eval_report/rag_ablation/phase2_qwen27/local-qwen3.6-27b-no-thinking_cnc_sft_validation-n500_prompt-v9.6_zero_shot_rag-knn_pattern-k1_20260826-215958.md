# Qwen3.6 27B No Thinking CNC validation rag_only_k1 eval report

## 配置
```json
{
  "label": "Qwen3.6 27B No Thinking CNC validation rag_only_k1",
  "model": "local/qwen3.6-27b-no-thinking",
  "dataset": "cnc_sft_validation",
  "sample_count": 500,
  "prompt_name": "v9.6_zero_shot",
  "use_rag": true,
  "rag_mode": "knn_pattern",
  "rag_top_k": 1,
  "temperature": 0.0,
  "max_tokens": 2048,
  "output_schema": "standard",
  "primary_metric": "strict_token_f1",
  "progress_every": 500,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 8192,
  "reasoning_effort": null,
  "llm_extra_body": null,
  "api_key_source": "lmstudio-default",
  "report_detail_limit": 200,
  "report_detail_mode": "errors",
  "report_error_metric": "strict_token_f1",
  "metadata_path": "D:\\Master thesis\\RAG Database\\cnc_examples.jsonl",
  "embeddings_path": "D:\\Master thesis\\RAG Database\\cnc_embeddings.npy"
}
```

## 统计指标
```text
================ Qwen3.6 27B No Thinking CNC validation rag_only_k1 final report ================
样本总数: 500
  Gold 含因果: 264 | Pred 含因果: 258
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.836
  Precision: 0.853
  Recall   : 0.833
  F1       : 0.843
  (TP=220, TN=198, FP=38, FN=44)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 500
    Gold triples: 366 | Pred triples: 301
    Precision: 0.532
    Recall   : 0.437
    F1       : 0.480
    (TP=160, FP=141, FN=206)
  [anchor_window]
    样本数: 500
    Gold triples: 366 | Pred triples: 301
    Precision: 0.525
    Recall   : 0.432
    F1       : 0.474
    (TP=158, FP=143, FN=208)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 220
    Gold triples: 315 | Pred triples: 256
    Precision: 0.625
    Recall   : 0.508
    F1       : 0.560
    (TP=160, FP=96, FN=155)
  [anchor_window]
    样本数: 220
    Gold triples: 315 | Pred triples: 256
    Precision: 0.617
    Recall   : 0.502
    F1       : 0.553
    (TP=158, FP=98, FN=157)
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

Sample details shown: all 195 wrong samples from 500 total samples.

### --- id=2991 ---

输入文本: Today 's incident , comes barely days after the massacre of 23 Kashmiri Pandits by militants at Wandhama in the Ganderbal area of the Kashmir Valley , and has cast a shadow over the February 16 Lok Sabhapolls in the state .

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
      "cause": "the massacre of 23 Kashmiri Pandits by militants at Wandhama in the Ganderbal area of the Kashmir Valley",
      "effect": "Today 's incident"
    },
    {
      "cause": "Today 's incident",
      "effect": "has cast a shadow over the February 16 Lok Sabhapolls in the state"
    }
  ],
  "pred_triples": []
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
        "span": "the bandh"
      },
      "relation": "caused",
      "effect": {
        "span": "Some schools which had to postpone their mid-term examinations due to the bandh have the additional task of conducting the tests before resuming the classes"
      }
    }
  ]
}
```

### --- id=1269 ---

输入文本: Two Maoists killed in Orissa 22nd June 2009 09:49 AM BHUBANESWAR : Two Maoist guerrillas were killed in a gun battle with the police in Orissa 's Malkangiri district , authorities said Monday .

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
        "span": "a gun battle with the police in Orissa 's Malkangiri district"
      },
      "relation": "caused",
      "effect": {
        "span": "Two Maoist guerrillas were killed"
      }
    }
  ]
}
```

### --- id=2992 ---

输入文本: ANANTNAG : Police today arrested two top militants and claimed to have solved the bomb blast at the high-security MLA hostel in Srinagar last year .

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
      "cause": "Police today arrested two top militants",
      "effect": "claimed to have solved the bomb blast at the high-security MLA hostel in Srinagar last year"
    }
  ],
  "pred_triples": []
}
```

### --- id=2777 ---

输入文本: Chhattisgarh Chief Minister Raman Singh strongly condemned the attack , describing it as most unfortunate and cowardly act of Maoists .

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
        "span": "the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Chhattisgarh Chief Minister Raman Singh strongly condemned the attack"
      }
    }
  ]
}
```

### --- id=2342 ---

输入文本: Ambala : Parents and guardians of students from Lord Mahavira Jain Public School , Ambala Cantonment , held a demonstration and dharna , on Thursday , to mark their protest against the increase in school and admission fee .

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
      "cause": "against the increase in school and admission fee",
      "effect": "Parents and guardians of students from Lord Mahavira Jain Public School , Ambala Cantonment , held a demonstration and dharna , on Thursday , to mark their protest"
    },
    {
      "cause": "mark their protest against the increase in school and admission fee",
      "effect": "Parents and guardians of students from Lord Mahavira Jain Public School , Ambala Cantonment , held a demonstration and dharna , on Thursday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to mark their protest"
      },
      "relation": "caused",
      "effect": {
        "span": "Parents and guardians of students from Lord Mahavira Jain Public School , Ambala Cantonment , held a demonstration and dharna , on Thursday"
      }
    },
    {
      "cause": {
        "span": "against the increase in school and admission fee"
      },
      "relation": "caused",
      "effect": {
        "span": "protest"
      }
    }
  ]
}
```

### --- id=1403 ---

输入文本: Khanyile was last year denied bail as he had violated his bail conditions related to an earlier case when he was arrested during student protests in February last year .

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
      "cause": "he had violated his bail conditions related to an earlier case",
      "effect": "Khanyile was last year denied bail"
    },
    {
      "cause": "he was arrested",
      "effect": "his bail conditions related to an earlier case"
    },
    {
      "cause": "student protests in February last year",
      "effect": "he was arrested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he had violated his bail conditions related to an earlier case"
      },
      "relation": "caused",
      "effect": {
        "span": "Khanyile was last year denied bail"
      }
    }
  ]
}
```

### --- id=1542 ---

输入文本: Mumbai Crime Branch had accused Ansari and Sabbauddin of providing details of the targets attacked by the LeT during 60 hour gun battle and had to face embarrassment twice when the trial court and the Bombay High Court acquitted the two saying there was no evidence against the two .

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
      "cause": "the trial court and the Bombay High Court acquitted the two saying there was no evidence against the two",
      "effect": "Mumbai Crime Branch had accused Ansari and Sabbauddin of providing details of the targets attacked by the LeT during 60 hour gun battle and had to face embarrassment twice"
    },
    {
      "cause": "saying there was no evidence against the two",
      "effect": "the trial court and the Bombay High Court acquitted the two"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the trial court and the Bombay High Court acquitted the two saying there was no evidence against the two"
      },
      "relation": "caused",
      "effect": {
        "span": "Mumbai Crime Branch ... had to face embarrassment twice"
      }
    }
  ]
}
```

### --- id=1527 ---

输入文本: - Indian Express Press Trust Of India , Press Trust Of India : Jaipur , Sat Dec 24 2011 , 10:18 hrs The medical crisis in Rajasthan due to an indefinite strike by doctors , which has crippled health services and left over a dozen patients dead , deepened on Friday with 5,000 doctors submitting their resignations .

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
      "cause": "5,000 doctors submitting their resignations",
      "effect": "The medical crisis in Rajasthan due to an indefinite strike by doctors , which has crippled health services and left over a dozen patients dead , deepened on Friday"
    },
    {
      "cause": "an indefinite strike by doctors",
      "effect": "The medical crisis in Rajasthan"
    },
    {
      "cause": "an indefinite strike by doctors",
      "effect": "has crippled health services and left over a dozen patients dead"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an indefinite strike by doctors"
      },
      "relation": "caused",
      "effect": {
        "span": "The medical crisis in Rajasthan"
      }
    },
    {
      "cause": {
        "span": "an indefinite strike by doctors"
      },
      "relation": "caused",
      "effect": {
        "span": "crippled health services"
      }
    },
    {
      "cause": {
        "span": "an indefinite strike by doctors"
      },
      "relation": "caused",
      "effect": {
        "span": "left over a dozen patients dead"
      }
    }
  ]
}
```

### --- id=2593 ---

输入文本: However , Nitish Kumar termed the shutdown opposed to development .

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
      "cause": "opposed to development",
      "effect": "the shutdown"
    }
  ],
  "pred_triples": []
}
```

### --- id=621 ---

输入文本: While rivalry between student groups led to the violence in which firing from a country - made pistol allegedly took place and eight students were said to be injured , the exact provocation behind the incident is not clear .

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
      "cause": "rivalry between student groups",
      "effect": "the violence in which firing from a country - made pistol allegedly took place"
    },
    {
      "cause": "the violence in which firing from a country - made pistol allegedly took place",
      "effect": "eight students were said to be injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "rivalry between student groups"
      },
      "relation": "caused",
      "effect": {
        "span": "the violence in which firing from a country - made pistol allegedly took place and eight students were said to be injured"
      }
    }
  ]
}
```

### --- id=1314 ---

输入文本: Students declare that they cannot continue agitation as they have to concentrate on exams

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "they have to concentrate on exams",
      "effect": "they cannot continue agitation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they have to concentrate on exams"
      },
      "relation": "caused",
      "effect": {
        "span": "Students declare that they cannot continue agitation"
      }
    }
  ]
}
```

### --- id=1549 ---

输入文本: The High court concurred with the view taken by Sessions Judge that the map recovered from killed terrorist pocket should have some wrinkles on it and blood spots as the LeT terrorist was badly injured in the gun-fight .

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
      "cause": "the LeT terrorist was badly injured",
      "effect": "The High court concurred with the view taken by Sessions Judge that the map recovered from killed terrorist pocket should have some wrinkles on it and blood spots"
    },
    {
      "cause": "the gun-fight",
      "effect": "the LeT terrorist was badly injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the LeT terrorist was badly injured in the gun-fight"
      },
      "relation": "caused",
      "effect": {
        "span": "the map recovered from killed terrorist pocket should have some wrinkles on it and blood spots"
      }
    }
  ]
}
```

### --- id=393 ---

输入文本: When they failed to comply , a team of MC officials was dispatched to serve a final notice which came under attack by the mob .

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
      "cause": "to serve a final notice",
      "effect": "a team of MC officials was dispatched"
    },
    {
      "cause": "they failed to comply",
      "effect": "to serve a final notice"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they failed to comply"
      },
      "relation": "caused",
      "effect": {
        "span": "a team of MC officials was dispatched to serve a final notice"
      }
    }
  ]
}
```

### --- id=978 ---

输入文本: `` Workers have realised that they are not going to get anything for nothing , '' he said of the strikes that brought farming activity to a standstill in fruit-growing regions of the province in recent months .

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
      "cause": "Workers have realised that they are not going to get anything for nothing",
      "effect": "the strikes that brought farming activity to a standstill in fruit-growing regions of the province in recent months"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the strikes"
      },
      "relation": "caused",
      "effect": {
        "span": "brought farming activity to a standstill in fruit-growing regions of the province in recent months"
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
        "span": "CPI-Maoist cadres shot dead three persons"
      }
    }
  ]
}
```

### --- id=2459 ---

输入文本: A strike called by a section of employees against the government decision to include the government Secretariat in the Kerala Administrative Service ( KAS ) crippled the functioning of the State administrative headquarters on Thursday .

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
      "cause": "against the government decision to include the government Secretariat in the Kerala Administrative Service ( KAS )",
      "effect": "A strike called by a section of employees"
    },
    {
      "cause": "A strike called by a section of employees",
      "effect": "crippled the functioning of the State administrative headquarters on Thursday ."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the government decision to include the government Secretariat in the Kerala Administrative Service ( KAS )"
      },
      "relation": "caused",
      "effect": {
        "span": "A strike called by a section of employees"
      }
    },
    {
      "cause": {
        "span": "A strike called by a section of employees against the government decision to include the government Secretariat in the Kerala Administrative Service ( KAS )"
      },
      "relation": "caused",
      "effect": {
        "span": "crippled the functioning of the State administrative headquarters on Thursday"
      }
    }
  ]
}
```

### --- id=2430 ---

输入文本: This false propaganda is being carried out against the agitation in Singur .

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
      "cause": "against the agitation in Singur",
      "effect": "This false propaganda is being carried out"
    }
  ],
  "pred_triples": []
}
```

### --- id=2006 ---

输入文本: 14th September 2014 06:15 AM TIRUPATI : The alleged attack on Nagari YSRC MLA RK Roja by some TDP men at Nagari on Friday mid-night , when she went there for offering the ‘ first Harathi ’ to the processional deity of Goddess Gangamma , led to tension in and round the town on Saturday with the actress-turned-politician and her supports staging widespread protests over the incident .

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
      "cause": "The alleged attack on Nagari YSRC MLA RK Roja by some TDP men at Nagari on Friday mid-night , when she went there for offering the ‘ first Harathi ’ to the processional deity of Goddess Gangamma",
      "effect": "tension in and round the town on Saturday"
    },
    {
      "cause": "the actress-turned-politician and her supports staging widespread protests over the incident",
      "effect": "tension in and round the town on Saturday"
    },
    {
      "cause": "the incident",
      "effect": "the actress-turned-politician and her supports staging widespread protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The alleged attack on Nagari YSRC MLA RK Roja by some TDP men at Nagari on Friday mid-night , when she went there for offering the ‘ first Harathi ’ to the processional deity of Goddess Gangamma"
      },
      "relation": "caused",
      "effect": {
        "span": "led to tension in and round the town on Saturday with the actress-turned-politician and her supports staging widespread protests over the incident"
      }
    }
  ]
}
```

### --- id=617 ---

输入文本: Agri SA calls for calm in Coligny Molaole Montsho COLIGNY , May 8 ( ANA ) - Agricultural body Agri SA on Monday , slammed the violence that flared up in Coligny , in the North West , after two farmers accused of the murder of Matlhomola Jonas Mosweu were granted bail .

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
      "cause": "two farmers accused of the murder of Matlhomola Jonas Mosweu were granted bail",
      "effect": "the violence that flared up in Coligny , in the North West"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the violence that flared up in Coligny , in the North West"
      },
      "relation": "caused",
      "effect": {
        "span": "Agricultural body Agri SA on Monday , slammed the violence that flared up in Coligny , in the North West"
      }
    },
    {
      "cause": {
        "span": "two farmers accused of the murder of Matlhomola Jonas Mosweu were granted bail"
      },
      "relation": "caused",
      "effect": {
        "span": "the violence that flared up in Coligny , in the North West"
      }
    }
  ]
}
```

### --- id=2159 ---

输入文本: Concerned that this new policy would reduce their children ’ s chances of getting into university , they marched in the streets to protest .

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
      "cause": "to protest",
      "effect": "they marched in the streets"
    },
    {
      "cause": "Concerned that this new policy would reduce their children ’ s chances of getting into university",
      "effect": "to protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Concerned that this new policy would reduce their children ’ s chances of getting into university"
      },
      "relation": "caused",
      "effect": {
        "span": "they marched in the streets to protest"
      }
    }
  ]
}
```

### --- id=2784 ---

输入文本: " When the security forces surrounded the house , they came under heavy gunfire from inside .

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
        "span": "the security forces surrounded the house"
      },
      "relation": "caused",
      "effect": {
        "span": "they came under heavy gunfire from inside"
      }
    }
  ]
}
```

### --- id=2412 ---

输入文本: Though the police had assured people of full protection during the bandh , most business establishments remained closed .

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
      "cause": "the police had assured people of full protection during the bandh",
      "effect": "most business establishments remained closed"
    }
  ],
  "pred_triples": []
}
```

### --- id=1571 ---

输入文本: Broken glass , rocks , a broken traffic light and other debris were scattered on Albertina Sisulu Road during the protests .

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
      "cause": "the protests",
      "effect": "Broken glass , rocks , a broken traffic light and other debris were scattered on Albertina Sisulu Road"
    }
  ],
  "pred_triples": []
}
```

### --- id=1074 ---

输入文本: Sixteen people , including 4 policemen and 11 CRPF jawans , were killed in the attack .

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
        "span": "the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Sixteen people , including 4 policemen and 11 CRPF jawans , were killed"
      }
    }
  ]
}
```

### --- id=994 ---

输入文本: Angry over the denial of a ticket to Suryakant Nagamarapalli , his supporters attacked the district BJP office in Bidar and vandalised the furniture on Friday .

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
      "cause": "the denial of a ticket to Suryakant Nagamarapalli",
      "effect": "Angry"
    },
    {
      "cause": "Angry",
      "effect": "his supporters attacked the district BJP office in Bidar and vandalised the furniture on Friday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the denial of a ticket to Suryakant Nagamarapalli"
      },
      "relation": "caused",
      "effect": {
        "span": "his supporters attacked the district BJP office in Bidar and vandalised the furniture on Friday"
      }
    }
  ]
}
```

### --- id=2252 ---

输入文本: Keith Cheng , Sheung Shui Extravagant excess has fuelled anger Holden Chow , chairman of the Democratic Alliance for the Betterment and Progress of Hong Kong 's ( DAB ) youth wing , is shocked by the violence of recent protests ( ' Violent protests are sending wrong message to our younger generation ' , September 17 ) .

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
      "cause": "Extravagant excess",
      "effect": "has fuelled anger"
    },
    {
      "cause": "the violence of recent protests",
      "effect": "Holden Chow , chairman of the Democratic Alliance for the Betterment and Progress of Hong Kong 's ( DAB ) youth wing , is shocked"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Extravagant excess has fuelled anger"
      },
      "relation": "caused",
      "effect": {
        "span": "anger"
      }
    }
  ]
}
```

### --- id=2069 ---

输入文本: James Leibold , a Xinjiang expert from Australia ’ s La Trobe university , said that ever since deadly ethnic rioting in 2009 authorities had gradually been transforming the region into a police state in a bid to halt the killing .

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
      "cause": "in a bid to halt the killing",
      "effect": "authorities had gradually been transforming the region into a police state"
    },
    {
      "cause": "deadly ethnic rioting in 2009",
      "effect": "in a bid to halt the killing"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "deadly ethnic rioting in 2009"
      },
      "relation": "caused",
      "effect": {
        "span": "authorities had gradually been transforming the region into a police state"
      }
    },
    {
      "cause": {
        "span": "to halt the killing"
      },
      "relation": "caused",
      "effect": {
        "span": "authorities had gradually been transforming the region into a police state"
      }
    }
  ]
}
```

### --- id=731 ---

输入文本: The police said the two factions got engaged in the fight following a wordy duel over some poll issues .

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
      "cause": "a wordy duel",
      "effect": "the two factions got engaged in the fight"
    },
    {
      "cause": "some poll issues",
      "effect": "a wordy duel"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a wordy duel over some poll issues"
      },
      "relation": "caused",
      "effect": {
        "span": "the two factions got engaged in the fight"
      }
    }
  ]
}
```

### --- id=1918 ---

输入文本: Two persons had been killed and over 90 injured in communal clashes that began on Saturday last over the issue of putting up religious flags .

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
      "cause": "communal clashes that began on Saturday last",
      "effect": "Two persons had been killed and over 90 injured"
    },
    {
      "cause": "the issue of putting up religious flags",
      "effect": "communal clashes that began on Saturday last"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "communal clashes that began on Saturday last over the issue of putting up religious flags"
      },
      "relation": "caused",
      "effect": {
        "span": "Two persons had been killed and over 90 injured"
      }
    }
  ]
}
```

### --- id=251 ---

输入文本: The police said that around 50 armed ultras raided Kangurukunda village at Kalimela , about 40 km from here , early on Sunday and set off an explosion , destrying the panchayat office .

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
      "cause": "around 50 armed ultras raided Kangurukunda village at Kalimela , about 40 km from here , early on Sunday and set off an explosion",
      "effect": "destrying the panchayat office"
    }
  ],
  "pred_triples": []
}
```

### --- id=6 ---

输入文本: Max Chung , who delivered the application for a letter of no objection from the police , that is required to hold a rally , said : “ We want to show to the public and international community that Hong Kongers , we will never surrender in front of terrorism … To show our solidarity and say no to terrorism , we have to stand up. ” Chung said : “ Yuen Long was under terrorist attack and we have no choice but to take it back. ” The protests , principally over a controversial bill that would allow suspects to be extradited from Hong Kong to mainland China , have taken on new demands , including an investigation into police use of rubber bullets , teargas and physical violence against protesters .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "to show to the public and international community that Hong Kongers , we will never surrender in front of terrorism"
      },
      "relation": "caused",
      "effect": {
        "span": "Max Chung ... delivered the application for a letter of no objection from the police"
      }
    },
    {
      "cause": {
        "span": "To show our solidarity and say no to terrorism"
      },
      "relation": "caused",
      "effect": {
        "span": "we have to stand up"
      }
    },
    {
      "cause": {
        "span": "Yuen Long was under terrorist attack"
      },
      "relation": "caused",
      "effect": {
        "span": "we have no choice but to take it back"
      }
    },
    {
      "cause": {
        "span": "a controversial bill that would allow suspects to be extradited from Hong Kong to mainland China"
      },
      "relation": "caused",
      "effect": {
        "span": "The protests ... principally over a controversial bill"
      }
    }
  ]
}
```

### --- id=2883 ---

输入文本: Police used mild force to disperse a group of advocates who had gathered at Favvara circle to show black flags to the Prime Minister in his way back to the Ghughra helipad .

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
      "cause": "to disperse a group of advocates who had gathered at Favvara circle",
      "effect": "Police used mild force"
    },
    {
      "cause": "to show black flags to the Prime Minister in his way back to the Ghughra helipad",
      "effect": "who had gathered at Favvara circle"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to disperse a group of advocates who had gathered at Favvara circle to show black flags to the Prime Minister in his way back to the Ghughra helipad"
      },
      "relation": "caused",
      "effect": {
        "span": "Police used mild force"
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

### --- id=2271 ---

输入文本: 23rd August 2016 08:17 PM PHULBANI : The communally sensitive Kandhamal district was today put under high security blanket as the members of the VHP assembled there to observe the death anniversary of Swami Laxamananda Saraswati , whose killing had sparked a large scale riot in the area in 2008 .

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
      "cause": "the members of the VHP assembled there",
      "effect": "The communally sensitive Kandhamal district was today put under high security blanket"
    },
    {
      "cause": "to observe the death anniversary of Swami Laxamananda Saraswati",
      "effect": "the members of the VHP assembled there"
    },
    {
      "cause": "whose killing",
      "effect": "had sparked a large scale riot in the area in 2008"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the members of the VHP assembled there to observe the death anniversary of Swami Laxamananda Saraswati"
      },
      "relation": "caused",
      "effect": {
        "span": "The communally sensitive Kandhamal district was today put under high security blanket"
      }
    },
    {
      "cause": {
        "span": "whose killing had sparked a large scale riot in the area in 2008"
      },
      "relation": "caused",
      "effect": {
        "span": "a large scale riot in the area in 2008"
      }
    }
  ]
}
```

### --- id=287 ---

输入文本: ' Once the damage is done , it is long-lasting and not remediable . ' The massive three-day protest this week was the latest in a series of grass-roots demonstrations over polluting projects , as mainlanders have gained awareness in recent years of environmental and health concerns associated with pollution .

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
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "mainlanders have gained awareness in recent years of environmental and health concerns associated with pollution",
      "effect": "The massive three-day protest this week was the latest in a series of grass-roots demonstrations over polluting projects"
    },
    {
      "cause": "polluting projects",
      "effect": "a series of grass-roots demonstrations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over polluting projects"
      },
      "relation": "caused",
      "effect": {
        "span": "The massive three-day protest this week was the latest in a series of grass-roots demonstrations"
      }
    },
    {
      "cause": {
        "span": "mainlanders have gained awareness in recent years of environmental and health concerns associated with pollution"
      },
      "relation": "caused",
      "effect": {
        "span": "The massive three-day protest this week was the latest in a series of grass-roots demonstrations over polluting projects"
      }
    }
  ]
}
```

### --- id=70 ---

输入文本: Kunming railway station attack Three given death penalty over Kunming rail station attack Influenced by religious extremism , trio plotted knife rampage , court says , while a fourth defendant handed life sentence for taking part

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
      "cause": "Kunming rail station attack",
      "effect": "Three given death penalty"
    },
    {
      "cause": "Influenced by religious extremism",
      "effect": "trio plotted knife rampage"
    },
    {
      "cause": "taking part",
      "effect": "a fourth defendant handed life sentence"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Influenced by religious extremism"
      },
      "relation": "caused",
      "effect": {
        "span": "trio plotted knife rampage"
      }
    },
    {
      "cause": {
        "span": "taking part"
      },
      "relation": "caused",
      "effect": {
        "span": "a fourth defendant handed life sentence"
      }
    }
  ]
}
```

### --- id=2957 ---

输入文本: ﻿The meeting discussed strategies to intensify the agitation against the Posco project and counter police action during construction of coastal road following the decision of the State Government to resume work from early next month .

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
      "cause": "the decision of the State Government to resume work from early next month",
      "effect": "﻿The meeting discussed strategies to intensify the agitation against the Posco project and counter police action during construction of coastal road"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to intensify the agitation against the Posco project and counter police action during construction of coastal road"
      },
      "relation": "caused",
      "effect": {
        "span": "The meeting discussed strategies"
      }
    }
  ]
}
```

### --- id=1300 ---

输入文本: The newspaper ’ s insistence came after a third day of protests in Tianjin over the government response to Wednesday ’ s explosions , which followed a blaze at a warehouse storing hazardous chemicals .

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
      "cause": "the government response to Wednesday ’ s explosions",
      "effect": "protests in Tianjin"
    },
    {
      "cause": "a blaze at a warehouse storing hazardous chemicals",
      "effect": "Wednesday ’ s explosions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a third day of protests in Tianjin over the government response to Wednesday ’ s explosions"
      },
      "relation": "caused",
      "effect": {
        "span": "The newspaper ’ s insistence"
      }
    },
    {
      "cause": {
        "span": "a blaze at a warehouse storing hazardous chemicals"
      },
      "relation": "caused",
      "effect": {
        "span": "Wednesday ’ s explosions"
      }
    }
  ]
}
```

### --- id=2671 ---

输入文本: Raising slogans against the State Government ’ s ban on toddy tapping , which was later upheld by the Supreme Court , some protestors drank toddy and certified that it was only a health drink with insignificant alcohol content and not an alcoholic beverage like the brew being sold in the IMFL outlets of the State Government .

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
      "cause": "against the State Government ’ s ban on toddy tapping",
      "effect": "Raising slogans"
    },
    {
      "cause": "certified that it was only a health drink with insignificant alcohol content and not an alcoholic beverage like the brew being sold in the IMFL outlets of the State Government",
      "effect": "some protestors drank toddy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Raising slogans against the State Government ’ s ban on toddy tapping"
      },
      "relation": "caused",
      "effect": {
        "span": "some protestors drank toddy and certified that it was only a health drink with insignificant alcohol content and not an alcoholic beverage like the brew being sold in the IMFL outlets of the State Government"
      }
    }
  ]
}
```

### --- id=55 ---

输入文本: " We will continue to work very closely with the Indian government on those issues , " she said , adding that it is an ongoing process and the US is working with Indian authorities to address issues of concern emanating from the incident .

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
      "cause": "to address issues of concern emanating from the incident",
      "effect": "the US is working with Indian authorities"
    }
  ],
  "pred_triples": []
}
```

### --- id=2842 ---

输入文本: WEF Africa 2017 : Zuma ushered away amid questions over May Day fiasco Siobhan Cassidy DURBAN , May 3 ( ANA ) – South African President Jacob Zuma was ushered away by minders on Wednesday as he was bombarded by questions about the fiasco on May Day when a booing crowd had refused to let him speak at a rally in Bloemfontein on Monday .

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
      "cause": "he was bombarded by questions about the fiasco on May Day",
      "effect": "South African President Jacob Zuma was ushered away by minders on Wednesday"
    },
    {
      "cause": "a booing crowd had refused to let him speak at a rally in Bloemfontein on Monday",
      "effect": "he was bombarded by questions about the fiasco on May Day"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he was bombarded by questions about the fiasco on May Day when a booing crowd had refused to let him speak at a rally in Bloemfontein on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "South African President Jacob Zuma was ushered away by minders on Wednesday"
      }
    }
  ]
}
```

### --- id=525 ---

输入文本: The clashes erupted after a youth belonging to a minority Muslim sect was allegedly severely injured in a thrashing by a youth from the majority sect following an altercation .

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
      "cause": "a youth belonging to a minority Muslim sect was allegedly severely injured in a thrashing by a youth from the majority sect",
      "effect": "The clashes erupted"
    },
    {
      "cause": "an altercation",
      "effect": "a youth belonging to a minority Muslim sect was allegedly severely injured in a thrashing by a youth from the majority sect"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a youth belonging to a minority Muslim sect was allegedly severely injured in a thrashing by a youth from the majority sect following an altercation"
      },
      "relation": "caused",
      "effect": {
        "span": "The clashes erupted"
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

### --- id=1432 ---

输入文本: The agitating activists attacked the ruling party office to register their protest against the delay in categorisation of SCs .

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
      "cause": "to register their protest against the delay in categorisation of SCs",
      "effect": "The agitating activists attacked the ruling party office"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to register their protest"
      },
      "relation": "caused",
      "effect": {
        "span": "The agitating activists attacked the ruling party office"
      }
    },
    {
      "cause": {
        "span": "against the delay in categorisation of SCs"
      },
      "relation": "caused",
      "effect": {
        "span": "their protest"
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
    "tp": 0,
    "fp": 1,
    "fn": 2
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
        "span": "Probe into AIADMK Man 's Murder"
      },
      "relation": "caused",
      "effect": {
        "span": "Wife Stages Stir"
      }
    }
  ]
}
```

### --- id=2007 ---

输入文本: Tension in Nagari After TDP Men Attack Roja

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
      "cause": "TDP Men Attack Roja",
      "effect": "Tension in Nagari"
    }
  ],
  "pred_triples": []
}
```

### --- id=2075 ---

输入文本: This was to thwart economic well-being of the population .

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "to thwart economic well-being of the population",
      "effect": "This"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to thwart economic well-being of the population"
      },
      "relation": "caused",
      "effect": {
        "span": "This was"
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
        "span": "the violence on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "Maruti Suzuki India Friday said its plant was remain closed for the second day"
      }
    },
    {
      "cause": {
        "span": "the violence on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "one senior company official was killed"
      }
    }
  ]
}
```

### --- id=2719 ---

输入文本: Earlier , a group of protesters had smashed the windows of a Lexus near the train station after spotting rods similar to those used against passengers last Sunday , leaving fliers criticising the police on the bonnet .

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
      "cause": "spotting rods similar to those used against passengers last Sunday",
      "effect": "a group of protesters had smashed the windows of a Lexus near the train station"
    },
    {
      "cause": "a group of protesters had smashed the windows of a Lexus near the train station",
      "effect": "fliers criticising the police on the bonnet"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "spotting rods similar to those used against passengers last Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "a group of protesters had smashed the windows of a Lexus near the train station"
      }
    }
  ]
}
```

### --- id=919 ---

输入文本: He enrolled at UNISA after his expulsion from the University of the North ( Turfloop ) for political activism , which arose from the organisation of the pro-Frelimo rallies in 1974 under the banner of the then South African Students Organisation ( SASO ) .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "his expulsion from the University of the North ( Turfloop )"
      },
      "relation": "caused",
      "effect": {
        "span": "He enrolled at UNISA"
      }
    },
    {
      "cause": {
        "span": "political activism"
      },
      "relation": "caused",
      "effect": {
        "span": "his expulsion from the University of the North ( Turfloop )"
      }
    },
    {
      "cause": {
        "span": "the organisation of the pro-Frelimo rallies in 1974 under the banner of the then South African Students Organisation ( SASO )"
      },
      "relation": "caused",
      "effect": {
        "span": "political activism"
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
      "cause": "Muslims across the city of lakes , still haunted by memories of the 2002 Gujarat riots",
      "effect": "they will not vote for someone who was unable to stop a massacre of ‘ innocent people ’ in his state"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "unable to stop a massacre of ‘ innocent people ’ in his state"
      },
      "relation": "caused",
      "effect": {
        "span": "Muslims across the city of lakes ... say they will not vote for someone"
      }
    }
  ]
}
```

### --- id=2073 ---

输入文本: “ It was a planned attack instigated by the PMK , who are trying to gain political mileage , ” he charged and added that members of a community in 30 villages , spread across political parties , joined the PMK-led assault .

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "gain political mileage",
      "effect": "It was a planned attack instigated by the PMK"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "trying to gain political mileage"
      },
      "relation": "caused",
      "effect": {
        "span": "It was a planned attack instigated by the PMK"
      }
    }
  ]
}
```

### --- id=1575 ---

输入文本: Addressing a massive gathering of party workers and sympathisers from in and around the city at the ‘ maha dharna ' organised in the vicinity of the Collector 's office here on Monday , Mr. Naidu said the Rosaiah Government has failed on all fronts and neglected agriculture as reflected in the acute shortage of fertilizer faced by the farmers .

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
      "cause": "the Rosaiah Government has failed on all fronts and neglected agriculture",
      "effect": "the acute shortage of fertilizer faced by the farmers"
    }
  ],
  "pred_triples": []
}
```

### --- id=2571 ---

输入文本: HYDERABAD Patient ’ s kin protest at hospital March 15 , 2017 00:00 IST The family of a 25 - year-old man who died at the Government Chest Hospital in Erragadda , allegedly due to the negligence of the staff , protested at the hospital on Tuesday .

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
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "the negligence of the staff",
      "effect": "man who died at the Government Chest Hospital in Erragadda"
    },
    {
      "cause": "The family of a 25 - year-old man who died at the Government Chest Hospital in Erragadda , allegedly due to the negligence of the staff",
      "effect": "protested at the hospital on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "allegedly due to the negligence of the staff"
      },
      "relation": "caused",
      "effect": {
        "span": "a 25 - year-old man who died at the Government Chest Hospital in Erragadda"
      }
    },
    {
      "cause": {
        "span": "the family of a 25 - year-old man who died at the Government Chest Hospital in Erragadda , allegedly due to the negligence of the staff"
      },
      "relation": "caused",
      "effect": {
        "span": "protested at the hospital on Tuesday"
      }
    }
  ]
}
```

### --- id=2140 ---

输入文本: This reportedly angered the owners , who first damaged the speakers of the protesters and then opened fire , injuring six persons .

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
      "cause": "This",
      "effect": "reportedly angered the owners"
    },
    {
      "cause": "reportedly angered the owners",
      "effect": "who first damaged the speakers of the protesters and then opened fire"
    },
    {
      "cause": "who first damaged the speakers of the protesters and then opened fire",
      "effect": "injuring six persons"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the owners ... first damaged the speakers of the protesters and then opened fire"
      },
      "relation": "caused",
      "effect": {
        "span": "injuring six persons"
      }
    }
  ]
}
```

### --- id=923 ---

输入文本: Marchers carried placards reading : `` We demand decent salary with omnibus '' , and `` We demand stability at the metro police . ''

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "We demand decent salary with omnibus"
      },
      "relation": "caused",
      "effect": {
        "span": "Marchers carried placards reading : `` We demand decent salary with omnibus '' , and `` We demand stability at the metro police . ''"
      }
    },
    {
      "cause": {
        "span": "We demand stability at the metro police ."
      },
      "relation": "caused",
      "effect": {
        "span": "Marchers carried placards reading : `` We demand decent salary with omnibus '' , and `` We demand stability at the metro police . ''"
      }
    }
  ]
}
```

### --- id=2227 ---

输入文本: MUMBAI : The protest by NGO ‘ Swabhiman ’ led by Maharashtra Industry Minister Narayan Rane ’ s son Nitesh Rane against 15 percent water supply cut by the Shiv Sena-ruled Brihanmumbai Municipal Corporation ( BMC ) claimed one life on Thursday .

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
      "cause": "against 15 percent water supply cut by the Shiv Sena-ruled Brihanmumbai Municipal Corporation ( BMC )",
      "effect": "The protest by NGO ‘ Swabhiman ’ led by Maharashtra Industry Minister Narayan Rane ’ s son Nitesh Rane"
    },
    {
      "cause": "The protest by NGO ‘ Swabhiman ’ led by Maharashtra Industry Minister Narayan Rane ’ s son Nitesh Rane against 15 percent water supply cut by the Shiv Sena-ruled Brihanmumbai Municipal Corporation ( BMC )",
      "effect": "claimed one life on Thursday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The protest by NGO ‘ Swabhiman ’ led by Maharashtra Industry Minister Narayan Rane ’ s son Nitesh Rane against 15 percent water supply cut by the Shiv Sena-ruled Brihanmumbai Municipal Corporation ( BMC )"
      },
      "relation": "caused",
      "effect": {
        "span": "claimed one life"
      }
    }
  ]
}
```

### --- id=653 ---

输入文本: The members voiced concern over the absence of a breakthrough in earlier incidents of blasts in Punjab and emphasised that the culprits should be brought to book with an iron fist .

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
        "span": "the absence of a breakthrough in earlier incidents of blasts in Punjab"
      },
      "relation": "caused",
      "effect": {
        "span": "The members voiced concern"
      }
    }
  ]
}
```

### --- id=2954 ---

输入文本: Rajendran of the Thamizh Desiya Podhuvudamai Katchi , were arrested in Thanjavur , while 10 persons , including MDMK rural district secretary , Tiruchi , were held in Tiruchi in connection with the stone-throwing incident .

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
      "cause": "the stone-throwing incident",
      "effect": "Rajendran of the Thamizh Desiya Podhuvudamai Katchi , were arrested in Thanjavur , while 10 persons , including MDMK rural district secretary , Tiruchi , were held in Tiruchi"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the stone-throwing incident"
      },
      "relation": "caused",
      "effect": {
        "span": "Rajendran of the Thamizh Desiya Podhuvudamai Katchi , were arrested in Thanjavur"
      }
    },
    {
      "cause": {
        "span": "the stone-throwing incident"
      },
      "relation": "caused",
      "effect": {
        "span": "10 persons , including MDMK rural district secretary , Tiruchi , were held in Tiruchi"
      }
    }
  ]
}
```

### --- id=2120 ---

输入文本: Streaker surrenders 02nd January 2013 10:25 AM The Ernakulam Central Police on Tuesday arrested the Ernakulam Law College student who allegedly ran naked through MG road demanding the removal of Justice K G Balakrishanan from the Chairman post of the National Human Rights Commission on December 17 .

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
      "cause": "who allegedly ran naked through MG road",
      "effect": "The Ernakulam Central Police on Tuesday arrested the Ernakulam Law College student"
    },
    {
      "cause": "demanding the removal of Justice K G Balakrishanan from the Chairman post of the National Human Rights Commission on December 17",
      "effect": "the Ernakulam Law College student who allegedly ran naked through MG road"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding the removal of Justice K G Balakrishanan from the Chairman post of the National Human Rights Commission on December 17"
      },
      "relation": "caused",
      "effect": {
        "span": "The Ernakulam Central Police on Tuesday arrested the Ernakulam Law College student who allegedly ran naked through MG road"
      }
    }
  ]
}
```

### --- id=718 ---

输入文本: About 20 volunteers dressed in period British military uniforms have been gathering on the streets of the city over the past month to mark the 75th anniversary of Black Christmas , when in 1941 British forces in Hong Kong surrendered to the Japanese , the first ever for a Crown colony .

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
      "cause": "to mark the 75th anniversary of Black Christmas",
      "effect": "About 20 volunteers dressed in period British military uniforms have been gathering on the streets of the city over the past month"
    }
  ],
  "pred_triples": []
}
```

### --- id=1699 ---

输入文本: The number four shaft was closed on Tuesday night when violence erupted at a meeting attended by about 750 people , leading to the deaths .

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
      "cause": "violence erupted at a meeting attended by about 750 people",
      "effect": "The number four shaft was closed on Tuesday night"
    },
    {
      "cause": "violence erupted at a meeting attended by about 750 people",
      "effect": "leading to the deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "violence erupted at a meeting attended by about 750 people"
      },
      "relation": "caused",
      "effect": {
        "span": "The number four shaft was closed on Tuesday night"
      }
    },
    {
      "cause": {
        "span": "violence erupted at a meeting attended by about 750 people"
      },
      "relation": "caused",
      "effect": {
        "span": "the deaths"
      }
    }
  ]
}
```

### --- id=169 ---

输入文本: Speaking just after 1pm , Poni said he and the hundreds of residents who had demonstrated outside the court were now on their way by train to the High Court , where they would make another attempt to get an urgent interdict .

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
      "cause": "they would make another attempt",
      "effect": "he and the hundreds of residents who had demonstrated outside the court were now on their way by train to the High Court"
    },
    {
      "cause": "to get an urgent interdict",
      "effect": "they would make another attempt"
    }
  ],
  "pred_triples": []
}
```

### --- id=1412 ---

输入文本: 18th January 2012 03:14 AM BANGALORE : Traffic on major roads of Bangalore was paralysed for close to seven hours on Tuesday as advocates held a protest at the Mysore Bank Circle demanding suspension of a police constable for allegedly beating up a fellow advocate .

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
      "cause": "advocates held a protest at the Mysore Bank Circle",
      "effect": "Traffic on major roads of Bangalore was paralysed for close to seven hours on Tuesday"
    },
    {
      "cause": "demanding suspension of a police constable for allegedly beating up a fellow advocate",
      "effect": "advocates held a protest at the Mysore Bank Circle"
    },
    {
      "cause": "allegedly beating up a fellow advocate",
      "effect": "demanding suspension of a police constable"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "advocates held a protest at the Mysore Bank Circle"
      },
      "relation": "caused",
      "effect": {
        "span": "Traffic on major roads of Bangalore was paralysed for close to seven hours on Tuesday"
      }
    },
    {
      "cause": {
        "span": "demanding suspension of a police constable for allegedly beating up a fellow advocate"
      },
      "relation": "caused",
      "effect": {
        "span": "advocates held a protest at the Mysore Bank Circle"
      }
    }
  ]
}
```

### --- id=195 ---

输入文本: At the same time , the Jawaharlal Nehru University Staff Association ( JNUSA ) and Jawaharlal Nehru University Officers Association ( JNUOA ) also sought action against those who shouted anti-national slogans on the campus on February 9 .

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
        "span": "those who shouted anti-national slogans on the campus on February 9"
      },
      "relation": "caused",
      "effect": {
        "span": "the Jawaharlal Nehru University Staff Association ( JNUSA ) and Jawaharlal Nehru University Officers Association ( JNUOA ) also sought action against those who shouted anti-national slogans on the campus on February 9"
      }
    }
  ]
}
```

### --- id=2728 ---

输入文本: Those attending the rally on Saturday said they were not there to make political demands , but to speak out against violence .

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "to speak out against violence",
      "effect": "Those attending the rally on Saturday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to speak out against violence"
      },
      "relation": "caused",
      "effect": {
        "span": "Those attending the rally on Saturday said they were not there to make political demands , but to speak out against violence"
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
      "cause": "to mourn",
      "effect": "thousands of residents of surrounding villages gathered"
    },
    {
      "cause": "On New Year 's Day , seven days after Qian 's death",
      "effect": "to mourn"
    }
  ],
  "pred_triples": []
}
```

### --- id=2362 ---

输入文本: It was a surcharged atmosphere as some lawyers went on an attacking spree without any provocation , identifying visual media personnel .

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
      "cause": "some lawyers went on an attacking spree without any provocation , identifying visual media personnel",
      "effect": "It was a surcharged atmosphere"
    }
  ],
  "pred_triples": []
}
```

### --- id=1380 ---

输入文本: Party leaders and activists came onto the roads and stopped RTC buses around 6.30 a.m. They were arrested and taken to the respective police stations .

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
        "span": "Party leaders and activists came onto the roads and stopped RTC buses around 6.30 a.m."
      },
      "relation": "caused",
      "effect": {
        "span": "They were arrested and taken to the respective police stations"
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

### --- id=1802 ---

输入文本: Health Minister V S Sivakumar said the agitation was unnecessary as all the major demands have been agreed upon .

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
      "cause": "all the major demands have been agreed upon",
      "effect": "the agitation was unnecessary"
    }
  ],
  "pred_triples": []
}
```

### --- id=2761 ---

输入文本: One of the agitators , Vivek Yadav , who was later hospitalised , lodged a complaint alleging that Congress district president Prakash Pradhan and his party workers assaulted him while Louise Khurshid 's vehicle hit him causing injuries .

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
        "span": "Louise Khurshid 's vehicle hit him"
      },
      "relation": "caused",
      "effect": {
        "span": "causing injuries"
      }
    }
  ]
}
```

### --- id=2596 ---

输入文本: Political analyst Satyanarain Madan said Lalu-Rabri for the first time made a political mark by a near total shutdown after their ouster from power in 2005 in Bihar and after Lalu Prasad lost his place in the Congress-led United Progressive Alliance central government last year after his party was routed in the Lok Sabha polls .

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
      "cause": "his party was routed in the Lok Sabha polls",
      "effect": "Lalu Prasad lost his place in the Congress-led United Progressive Alliance central government last year"
    }
  ],
  "pred_triples": []
}
```

### --- id=3009 ---

输入文本: During the entire impasse , Mallya did not come in the forefront and the negotiations were carried out by top officials of the airline and the UB Group , leading employees to demand his presence .

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
      "cause": "During the entire impasse , Mallya did not come in the forefront and the negotiations were carried out by top officials of the airline and the UB Group",
      "effect": "employees to demand his presence"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Mallya did not come in the forefront"
      },
      "relation": "caused",
      "effect": {
        "span": "employees to demand his presence"
      }
    }
  ]
}
```

### --- id=1035 ---

输入文本: The meeting , chaired by Prime Minister Manmohan Singh , saw Ministers expressing concern over the gangrape , which has exposed the lack of women ’ s safety , and the public outrage that followed it .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "the gangrape"
      },
      "relation": "caused",
      "effect": {
        "span": "which has exposed the lack of women ’ s safety"
      }
    },
    {
      "cause": {
        "span": "the gangrape"
      },
      "relation": "caused",
      "effect": {
        "span": "the public outrage that followed it"
      }
    }
  ]
}
```

### --- id=639 ---

输入文本: These services were affected in the last two days following stone throwing had operated from the Palakkad depot on Friday , while five operated on Saturday .

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
      "cause": "stone throwing had operated from the Palakkad depot on Friday , while five operated on Saturday",
      "effect": "These services were affected in the last two days"
    }
  ],
  "pred_triples": []
}
```

### --- id=2910 ---

输入文本: In the other agitation , residents of ward 19 highlighted the drinking water issues , lethargic garbage removal and poor maintenance of street lights .

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
        "span": "the drinking water issues , lethargic garbage removal and poor maintenance of street lights"
      },
      "relation": "caused",
      "effect": {
        "span": "residents of ward 19 highlighted the drinking water issues , lethargic garbage removal and poor maintenance of street lights"
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
        "span": "to register their protest against the insensitive and indifferent attitude of the Government to the genuine demands of the pourakarmikas"
      },
      "relation": "caused",
      "effect": {
        "span": "hundreds of people , including many women , led by Sri Mahanta Shivacharyaru of the Sulpul Math , Sri Rajashekar Shivacharyaru , Guru Mahanta Shivacharyaru of the Hiremath at Pala , Shivanda Swamigalu of Sonna Dasoha Math , Gangadhar Swamigalu of Chowdapur Math , Kanchi Basava Shivacharyaru of Roza Math , battery of Congress leaders including DCC president Allamprabhu Patil , MLC , the former Mayor Chandrika Parameshwar , zilla panchayat member Ambaraya Ashtagi , the former president of the HKCCI Umakant Nigudgi , Karnataka Rakshana Vedike president Arunkumar Patil , Hyderabad Karnataka Janapara Sangarsh Samiti Laxman Dasti and others marched from the Super Market to the Deputy Commissioner 's office"
      }
    }
  ]
}
```

### --- id=988 ---

输入文本: Inaugurating the dharna , State secretary of the Communist Party of India C.K. Chandrappan said the United Democratic Front ( UDF ) government seemed to have declared a war on the people through its revised Budget .

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
        "span": "the United Democratic Front ( UDF ) government seemed to have declared a war on the people through its revised Budget"
      },
      "relation": "caused",
      "effect": {
        "span": "State secretary of the Communist Party of India C.K. Chandrappan said"
      }
    }
  ]
}
```

### --- id=955 ---

输入文本: NSCN(K) Claims Responsibility for Ambush on Army in Manipur 05th June 2015 03:41 PM GUWAHATI / KOHIMA : Naga insurgent outfit NSCN ( Khaplang ) , with which the Centre abrogated ceasefire in March , has claimed responsibility for the ambush in Manipur in which 18 army personnel were killed and 10 others injured .

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
      "cause": "the ambush in Manipur",
      "effect": "Naga insurgent outfit NSCN ( Khaplang ) , with which the Centre abrogated ceasefire in March , has claimed responsibility"
    },
    {
      "cause": "the ambush in Manipur",
      "effect": "18 army personnel were killed and 10 others injured"
    }
  ],
  "pred_triples": []
}
```

### --- id=1165 ---

输入文本: S. Sreenivas Reddy , convenor , Andhra Pradesh Recognised Private Schools Managements Association , has said that schools would be closed in anticipation of tense situation due to bandh .

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
      "cause": "tense situation",
      "effect": "schools would be closed"
    },
    {
      "cause": "bandh",
      "effect": "tense situation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "tense situation due to bandh"
      },
      "relation": "caused",
      "effect": {
        "span": "schools would be closed in anticipation of tense situation due to bandh"
      }
    }
  ]
}
```

### --- id=1711 ---

输入文本: On Monday , two people were killed , allegedly by police , during the protests .

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
      "cause": "allegedly by police , during the protests",
      "effect": "two people were killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the protests"
      },
      "relation": "caused",
      "effect": {
        "span": "two people were killed , allegedly by police , on Monday"
      }
    }
  ]
}
```

### --- id=1387 ---

输入文本: Passengers to the Shamshabad airport did not have much of a problem as some radio cab operators did not participate in the strike and they made brisk business .

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
      "cause": "some radio cab operators did not participate in the strike and they made brisk business",
      "effect": "Passengers to the Shamshabad airport did not have much of a problem"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "some radio cab operators did not participate in the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "Passengers to the Shamshabad airport did not have much of a problem"
      }
    }
  ]
}
```

### --- id=1687 ---

输入文本: 29th June 2015 06:08 AM VELLORE : As many as 95 youth have been arrested with the deadly attack on police personnel in Ambur Town on Saturday night which left 38 police personnel , including women , and a couple of civilians injured in connection with the death of Shameel Ahmed .

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
      "cause": "the deadly attack on police personnel in Ambur Town on Saturday night",
      "effect": "As many as 95 youth have been arrested"
    },
    {
      "cause": "the deadly attack on police personnel in Ambur Town on Saturday night",
      "effect": "which left 38 police personnel , including women , and a couple of civilians injured"
    },
    {
      "cause": "the death of Shameel Ahmed",
      "effect": "which left 38 police personnel , including women , and a couple of civilians injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the deadly attack on police personnel in Ambur Town on Saturday night which left 38 police personnel , including women , and a couple of civilians injured"
      },
      "relation": "caused",
      "effect": {
        "span": "As many as 95 youth have been arrested"
      }
    },
    {
      "cause": {
        "span": "the deadly attack on police personnel in Ambur Town on Saturday night"
      },
      "relation": "caused",
      "effect": {
        "span": "left 38 police personnel , including women , and a couple of civilians injured"
      }
    }
  ]
}
```

### --- id=1431 ---

输入文本: While Singhdeo sat on a dharna in the Well in protest , Congress and other BJP members rushed into the Well shouting slogans .

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
        "span": "in protest"
      },
      "relation": "caused",
      "effect": {
        "span": "Singhdeo sat on a dharna in the Well"
      }
    }
  ]
}
```

### --- id=2378 ---

输入文本: “ I am shocked to hear about the brutal killing of Shri V Ramesh our General Secretary of Tamil Nadu unit .

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
      "cause": "the brutal killing of Shri V Ramesh our General Secretary of Tamil Nadu unit",
      "effect": "I am shocked to hear"
    }
  ],
  "pred_triples": []
}
```

### --- id=1717 ---

输入文本: The incident has sparked protests across New Delhi over the security of students from the north-east .

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
      "cause": "The incident",
      "effect": "protests across New Delhi over the security of students from the north-east"
    },
    {
      "cause": "the security of students from the north-east",
      "effect": "protests across New Delhi"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The incident"
      },
      "relation": "caused",
      "effect": {
        "span": "protests across New Delhi over the security of students from the north-east"
      }
    }
  ]
}
```

### --- id=470 ---

输入文本: - Indian Express Agencies , Agencies : Srinagar , Thu Dec 23 2010 , 14:13 hrs Curfew continued to remain imposed without any relaxation in parts of Bandipora district of north Kashmir for the fourth consecutive day on Thursday following sectarian clashes in which four persons were injured .

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
      "cause": "sectarian clashes in which four persons were injured",
      "effect": "Curfew continued to remain imposed without any relaxation in parts of Bandipora district of north Kashmir for the fourth consecutive day on Thursday"
    },
    {
      "cause": "sectarian clashes",
      "effect": "four persons were injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "sectarian clashes"
      },
      "relation": "caused",
      "effect": {
        "span": "Curfew continued to remain imposed without any relaxation in parts of Bandipora district of north Kashmir for the fourth consecutive day on Thursday"
      }
    }
  ]
}
```

### --- id=1175 ---

输入文本: Mahant Jugal Kishore Shastri , a priest with the Ayodhya-based Saryu Kunj temple , said : " At this stage , if other religious leaders from different parts of the country also come forward and join hands to work out an amicable settlement of the Ayodhya issue , I personally feel that the Ansari 's move would definitely produce the desirable result . "

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
      "cause": "to work out an amicable settlement of the Ayodhya issue",
      "effect": "other religious leaders from different parts of the country also come forward and join hands"
    },
    {
      "cause": "other religious leaders from different parts of the country also come forward and join hands to work out an amicable settlement of the Ayodhya issue",
      "effect": "I personally feel that the Ansari 's move would definitely produce the desirable result"
    }
  ],
  "pred_triples": []
}
```

### --- id=2594 ---

输入文本: The dawn-to-dusk shutdown evoked total response in Bihar , upsetting Lalu-Rabri rival Nitish Kumar as well as the Bharatiya Janata Party ( BJP ) and the Congress , which is trying for a revival in the state .

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
      "cause": "The dawn-to-dusk shutdown",
      "effect": "total response in Bihar"
    },
    {
      "cause": "total response in Bihar",
      "effect": "upsetting Lalu-Rabri rival Nitish Kumar as well as the Bharatiya Janata Party ( BJP ) and the Congress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The dawn-to-dusk shutdown"
      },
      "relation": "caused",
      "effect": {
        "span": "upsetting Lalu-Rabri rival Nitish Kumar as well as the Bharatiya Janata Party ( BJP ) and the Congress , which is trying for a revival in the state ."
      }
    }
  ]
}
```

### --- id=1750 ---

输入文本: Parking contract has been given to some goons who were collecting high rates from students and patients , ” he claimed and warned of intensifying the agitation .

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
        "span": "Parking contract has been given to some goons who were collecting high rates from students and patients"
      },
      "relation": "caused",
      "effect": {
        "span": "he claimed and warned of intensifying the agitation"
      }
    }
  ]
}
```

### --- id=1411 ---

输入文本: Protesting lawyers paralyse Bangalore

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
      "cause": "Protesting lawyers",
      "effect": "paralyse Bangalore"
    }
  ],
  "pred_triples": []
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
        "span": "\" lowering the dignity of the House \" with the remarks they made during Anna Hazare ’ s one-day fast at Jantar Mantar on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "The Lok Sabha ... strongly condemned them"
      }
    }
  ]
}
```

### --- id=788 ---

输入文本: `` Prolonged strikes may lead to the company closing down , '' he said after a Congress of SA Trade Unions rally in Rustenburg .

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
      "cause": "Prolonged strikes",
      "effect": "the company closing down"
    }
  ],
  "pred_triples": []
}
```

### --- id=1321 ---

输入文本: " We conducted the march to request the global leaders to re-design the policies so that earth could become a peaceful place to live with harmony , " said Meeran Haider .

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
      "cause": "to request the global leaders",
      "effect": "We conducted the march"
    },
    {
      "cause": "to re-design the policies so that earth could become a peaceful place to live with harmony",
      "effect": "to request the global leaders"
    },
    {
      "cause": "re-design the policies",
      "effect": "earth could become a peaceful place to live with harmony"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to request the global leaders to re-design the policies so that earth could become a peaceful place to live with harmony"
      },
      "relation": "caused",
      "effect": {
        "span": "We conducted the march"
      }
    }
  ]
}
```

### --- id=2289 ---

输入文本: Millions have taken to the streets to protest against the proposed law allowing for the extradition of individuals for trial in mainland China , where the opaque court system is controlled by the Communist party .

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
      "cause": "against the proposed law allowing for the extradition of individuals for trial in mainland China , where the opaque court system is controlled by the Communist party",
      "effect": "Millions have taken to the streets to protest"
    },
    {
      "cause": "to protest against the proposed law allowing for the extradition of individuals for trial in mainland China , where the opaque court system is controlled by the Communist party",
      "effect": "Millions have taken to the streets"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest against the proposed law allowing for the extradition of individuals for trial in mainland China"
      },
      "relation": "caused",
      "effect": {
        "span": "Millions have taken to the streets"
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

### --- id=2607 ---

输入文本: Several tribals were also put in jail by police in false cases and Prasadam was fighting for their cause when he was done to death by forces backed by the government , CRPP general secretary Balla Ravindranath said in a press release .

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
      "cause": "false cases",
      "effect": "Several tribals were also put in jail by police"
    },
    {
      "cause": "Prasadam was fighting for their cause",
      "effect": "he was done to death by forces backed by the government"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Prasadam was fighting for their cause"
      },
      "relation": "caused",
      "effect": {
        "span": "he was done to death by forces backed by the government"
      }
    }
  ]
}
```

### --- id=2095 ---

输入文本: About 200 members of the Treatment Action Campaign ( TAC ) protested outside the hospital and like the families they want answers .

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
      "cause": "they want answers",
      "effect": "About 200 members of the Treatment Action Campaign ( TAC ) protested outside the hospital and like the families"
    }
  ],
  "pred_triples": []
}
```

### --- id=820 ---

输入文本: Both of these issues remain deeply unpopular among city residents and previous government attempts to enact security legislation and national education sparked mass protests .

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
      "cause": "Both of these issues remain deeply unpopular among city residents and previous government attempts to enact security legislation and national education",
      "effect": "mass protests ."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "previous government attempts to enact security legislation and national education"
      },
      "relation": "caused",
      "effect": {
        "span": "sparked mass protests"
      }
    }
  ]
}
```

### --- id=876 ---

输入文本: The TAC and a group of Khayelitsha residents , some of them HIV-positive , are seeking the reinstatement of the workers fired on June 11 after allegedly participating in the public service strike .

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
      "cause": "participating in the public service strike",
      "effect": "the workers fired on June 11"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the workers fired on June 11 after allegedly participating in the public service strike"
      },
      "relation": "caused",
      "effect": {
        "span": "The TAC and a group of Khayelitsha residents , some of them HIV-positive , are seeking the reinstatement"
      }
    }
  ]
}
```

### --- id=1996 ---

输入文本: Many Hong Kongers also cite the jailing of leaders and activists from the 2014 Occupy Central movement – a 79-day mass civil disobedience movement – as well as the disqualification of young localist lawmakers as signs of the erosion of civil freedoms .

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
      "cause": "the erosion of civil freedoms",
      "effect": "the jailing of leaders and activists from the 2014 Occupy Central movement – a 79-day mass civil disobedience movement – as well as the disqualification of young localist lawmakers"
    }
  ],
  "pred_triples": []
}
```

### --- id=2700 ---

输入文本: While the management agreed to take back all the employees who were given the sack after their participated in the strike , representatives of employees agreed to report for duty on Friday morning .

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
      "cause": "their participated in the strike",
      "effect": "the employees who were given the sack"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the management agreed to take back all the employees who were given the sack after their participated in the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "representatives of employees agreed to report for duty on Friday morning"
      }
    }
  ]
}
```

### --- id=2668 ---

输入文本: TAMIL NADU Toddy tappers held in districts January 22 , 2009 00:00 IST Revoke ban : Members of Tamil Nadu Nadar Peravai showing pots as a mark of protest in Virudhunagar on Wednesday .

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
      "cause": "a mark of protest in Virudhunagar on Wednesday",
      "effect": "Members of Tamil Nadu Nadar Peravai showing pots"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Revoke ban"
      },
      "relation": "caused",
      "effect": {
        "span": "Members of Tamil Nadu Nadar Peravai showing pots as a mark of protest in Virudhunagar on Wednesday"
      }
    }
  ]
}
```

### --- id=2002 ---

输入文本: IFP hotheads at the township entrance tried again to barricade the road and were removed by the police .

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
      "cause": "IFP hotheads at the township entrance tried again to barricade the road",
      "effect": "were removed by the police"
    }
  ],
  "pred_triples": []
}
```

### --- id=1173 ---

输入文本: Mamata shows off strength , takes out padayatra 01st April 2011 02:48 AM KOLKATA : Trinamool Congress supremo Mamata Banerjee organised a huge padayatra as part of her election campaign in the city on Thursday , sending a message to the CPM leadership about the possible change in the state administration .

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
      "cause": "her election campaign in the city on Thursday",
      "effect": "Trinamool Congress supremo Mamata Banerjee organised a huge padayatra"
    },
    {
      "cause": "sending a message to the CPM leadership about the possible change in the state administration",
      "effect": "her election campaign in the city on Thursday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "as part of her election campaign in the city"
      },
      "relation": "caused",
      "effect": {
        "span": "Trinamool Congress supremo Mamata Banerjee organised a huge padayatra"
      }
    },
    {
      "cause": {
        "span": "sending a message to the CPM leadership about the possible change in the state administration"
      },
      "relation": "caused",
      "effect": {
        "span": "Trinamool Congress supremo Mamata Banerjee organised a huge padayatra"
      }
    }
  ]
}
```

### --- id=1322 ---

输入文本: Posted : Tue Apr 21 1998 IST KARIMNAGAR , April 20 : Armed reserve and civil policemen revolted and unleashed a reign of terror in the town last night to protest against the transfer of superintendent of police Umesh Chandra , further eroding the image of the police which touched an all-time low due to several incidents recently .

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
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "to protest against the transfer of superintendent of police Umesh Chandra",
      "effect": "Armed reserve and civil policemen revolted and unleashed a reign of terror in the town last night"
    },
    {
      "cause": "Armed reserve and civil policemen revolted and unleashed a reign of terror in the town last night to protest against the transfer of superintendent of police Umesh Chandra",
      "effect": "further eroding the image of the police"
    },
    {
      "cause": "several incidents recently",
      "effect": "image of the police which touched an all-time low"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest against the transfer of superintendent of police Umesh Chandra"
      },
      "relation": "caused",
      "effect": {
        "span": "Armed reserve and civil policemen revolted and unleashed a reign of terror in the town last night"
      }
    },
    {
      "cause": {
        "span": "several incidents recently"
      },
      "relation": "caused",
      "effect": {
        "span": "the image of the police ... touched an all-time low"
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
        "span": "injuring four persons"
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

### --- id=1704 ---

输入文本: June 10 , 2009 : Nine security personnel , including CRPF troopers , ambushed by Maoists during a routine patrol in Saranda jungles in Jharkhand .

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
        "span": "Maoists"
      },
      "relation": "caused",
      "effect": {
        "span": "Nine security personnel , including CRPF troopers , ambushed ... during a routine patrol in Saranda jungles in Jharkhand"
      }
    }
  ]
}
```

### --- id=1164 ---

输入文本: Party leaders here have requested educational institutions and other private establishments in twin cities to cooperate with them and make bandh successful .

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
        "span": "to make bandh successful"
      },
      "relation": "caused",
      "effect": {
        "span": "Party leaders here have requested educational institutions and other private establishments in twin cities to cooperate with them"
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
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
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
        "span": "to protest Tuesday 's rioting at Bhagwati Hospital"
      },
      "relation": "caused",
      "effect": {
        "span": "An honorary orthopaedic surgeon with Bhagwati Hospital resigned today and private hospitals from Jogeshwari to Dahisar decided to down shutters for a day"
      }
    },
    {
      "cause": {
        "span": "Tuesday 's rioting at Bhagwati Hospital"
      },
      "relation": "caused",
      "effect": {
        "span": "doctors closed ranks"
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
      "cause": "to confront the protesters and a minor scuffle ensued",
      "effect": "The CPM workers too came out of the building"
    }
  ],
  "pred_triples": []
}
```

### --- id=1082 ---

输入文本: In the charged atmosphere generated by the dangerous currents of domestic politics and media-induced panic , Prime Minister Manmohan Singh is finding himself under tremendous pressure to respond decisively to initial evidence that ‘ elements in Pakistan ’ were responsible for last week ’ s terrorist outrage in Mumbai .

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
        "span": "the charged atmosphere generated by the dangerous currents of domestic politics and media-induced panic"
      },
      "relation": "caused",
      "effect": {
        "span": "Prime Minister Manmohan Singh is finding himself under tremendous pressure to respond decisively to initial evidence that ‘ elements in Pakistan ’ were responsible for last week ’ s terrorist outrage in Mumbai"
      }
    }
  ]
}
```

### --- id=967 ---

输入文本: He urged the government to drop the cases registered against the Christians in connection with church attacks .

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
        "span": "church attacks"
      },
      "relation": "caused",
      "effect": {
        "span": "cases registered against the Christians"
      }
    }
  ]
}
```

### --- id=2458 ---

输入文本: Today 's Paper One-day agitation against KAS cripples Secretariat

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
      "cause": "against KAS",
      "effect": "One-day agitation"
    },
    {
      "cause": "One-day agitation",
      "effect": "cripples Secretariat"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "One-day agitation against KAS"
      },
      "relation": "caused",
      "effect": {
        "span": "cripples Secretariat"
      }
    }
  ]
}
```

### --- id=2470 ---

输入文本: In the early hours of 6 May , Beijing police detained Pu Zhiqiang , a prominent human rights lawyer who helped organise the 1989 demonstration ; three days prior , he had participated in a private panel discussion commemorating the massacre .

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
      "cause": "a prominent human rights lawyer who helped organise the 1989 demonstration ; three days prior , he had participated in a private panel discussion commemorating the massacre",
      "effect": "In the early hours of 6 May , Beijing police detained Pu Zhiqiang"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he had participated in a private panel discussion commemorating the massacre"
      },
      "relation": "caused",
      "effect": {
        "span": "Beijing police detained Pu Zhiqiang , a prominent human rights lawyer who helped organise the 1989 demonstration"
      }
    }
  ]
}
```

### --- id=1293 ---

输入文本: The riots were a spillover of the Cultural Revolution that was launched on the mainland one year earlier .

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
        "span": "the Cultural Revolution that was launched on the mainland one year earlier"
      },
      "relation": "caused",
      "effect": {
        "span": "The riots were a spillover"
      }
    }
  ]
}
```

### --- id=90 ---

输入文本: Taxi strike impacts businesses in Soshanguve Brenda Masilela PRETORIA , November 8 ( ANA ) - Employees at the Soshanguve Plaza , south of Pretoria , arrived for work on Wednesday only to find businesses closed amid fears that the taxi strike might turn violent .

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
      "cause": "fears that the taxi strike might turn violent",
      "effect": "Employees at the Soshanguve Plaza , south of Pretoria , arrived for work on Wednesday only to find businesses closed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "fears that the taxi strike might turn violent"
      },
      "relation": "caused",
      "effect": {
        "span": "businesses closed"
      }
    }
  ]
}
```

### --- id=1538 ---

输入文本: Wednesday 's demonstration was the second one organised with the help of the Bharatiya Vidyarti Sena ( BVS ) .

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
      "cause": "with the help of the Bharatiya Vidyarti Sena ( BVS )",
      "effect": "Wednesday 's demonstration was the second one organised"
    }
  ],
  "pred_triples": []
}
```

### --- id=1915 ---

输入文本: Several persons , including two policemen , were injured in the clash that lasted nearly an hour .

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
        "span": "the clash that lasted nearly an hour"
      },
      "relation": "caused",
      "effect": {
        "span": "Several persons , including two policemen , were injured"
      }
    }
  ]
}
```

### --- id=1757 ---

输入文本: In Theni , the PMK held an unusual form of protest with members sporting a " patta naamam " ( holy ash spread across their foreheads ) , symbolically signifying betrayal .

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
        "span": "symbolically signifying betrayal"
      },
      "relation": "caused",
      "effect": {
        "span": "the PMK held an unusual form of protest with members sporting a \" patta naamam \" ( holy ash spread across their foreheads )"
      }
    }
  ]
}
```

### --- id=1604 ---

输入文本: The TRS students ' wing activists staged dharna in front of Karimnagar One Town police flaying the arrests of their activists and obstructing them from proceeding to Hyderabad .

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
      "cause": "the arrests of their activists and obstructing them from proceeding to Hyderabad",
      "effect": "The TRS students ' wing activists staged dharna in front of Karimnagar One Town police"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "flaying the arrests of their activists"
      },
      "relation": "caused",
      "effect": {
        "span": "The TRS students ' wing activists staged dharna in front of Karimnagar One Town police"
      }
    }
  ]
}
```

### --- id=2617 ---

输入文本: Sources said that a group of militants hiding in the area saw the team while they were going beyond Watsar towards Simpthan and laid an ambush on the Chattroo-Simpthan road by blocking it with stones .

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
      "cause": "blocking it with stones",
      "effect": "laid an ambush on the Chattroo-Simpthan road"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a group of militants hiding in the area saw the team while they were going beyond Watsar towards Simpthan"
      },
      "relation": "caused",
      "effect": {
        "span": "laid an ambush on the Chattroo-Simpthan road by blocking it with stones"
      }
    }
  ]
}
```

### --- id=1484 ---

输入文本: Fight against FDI to go on : Oppn - Indian Express Agencies , Agencies : New Delhi , Wed Dec 12 2012 , 19:55 hrs Taking its protest against FDI to the streets , opposition parties today said their fight will go on till they ensure that it is scrapped altogether .

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
      "cause": "their fight will go on till they ensure that it is scrapped altogether",
      "effect": "Taking its protest against FDI to the streets"
    },
    {
      "cause": "they ensure that it is scrapped altogether",
      "effect": "their fight will go on"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest against FDI"
      },
      "relation": "caused",
      "effect": {
        "span": "Taking its ... to the streets"
      }
    },
    {
      "cause": {
        "span": "till they ensure that it is scrapped altogether"
      },
      "relation": "caused",
      "effect": {
        "span": "their fight will go on"
      }
    }
  ]
}
```

### --- id=3050 ---

输入文本: Elaborating on the three issues , Singhvi said , “ The BJP gave sermons on Raj Dharma and turned a Nelson ’ s eye to the communal carnage , which became a big blot on the fair name of the country . ”

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
        "span": "The BJP gave sermons on Raj Dharma and turned a Nelson ’ s eye to the communal carnage"
      },
      "relation": "caused",
      "effect": {
        "span": "which became a big blot on the fair name of the country"
      }
    }
  ]
}
```

### --- id=1695 ---

输入文本: Around 50 women protested and tried to surround the Tahsildar office in Ambur Town demanding the release of the persons arrested , claiming the persons arrested were innocents .

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
      "cause": "demanding the release of the persons arrested",
      "effect": "Around 50 women protested and tried to surround the Tahsildar office in Ambur Town"
    },
    {
      "cause": "claiming the persons arrested were innocents",
      "effect": "demanding the release of the persons arrested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding the release of the persons arrested"
      },
      "relation": "caused",
      "effect": {
        "span": "Around 50 women protested and tried to surround the Tahsildar office in Ambur Town"
      }
    }
  ]
}
```

### --- id=1960 ---

输入文本: Protesting workers from petrol stations , car dealers and panel beaters warned their employers on Tuesday to prepare for a long battle in their campaign for better wages and allowances .

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
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "to prepare for a long battle in their campaign for better wages and allowances",
      "effect": "Protesting workers from petrol stations , car dealers and panel beaters warned their employers on Tuesday"
    },
    {
      "cause": "better wages and allowances",
      "effect": "their campaign"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in their campaign for better wages and allowances"
      },
      "relation": "caused",
      "effect": {
        "span": "Protesting workers from petrol stations , car dealers and panel beaters warned their employers on Tuesday to prepare for a long battle"
      }
    }
  ]
}
```

### --- id=1855 ---

输入文本: The petitioner Rohan Mohanty has submitted that junior doctors ’ strike has affected hundreds of patients and thus , they should be directed to join duty immediately .

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
      "cause": "junior doctors ’ strike",
      "effect": "has affected hundreds of patients"
    },
    {
      "cause": "has affected hundreds of patients",
      "effect": "they should be directed to join duty immediately"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "junior doctors ’ strike has affected hundreds of patients"
      },
      "relation": "caused",
      "effect": {
        "span": "they should be directed to join duty immediately"
      }
    }
  ]
}
```

### --- id=1436 ---

输入文本: During service delivery protests three people died .

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
        "span": "service delivery protests"
      },
      "relation": "caused",
      "effect": {
        "span": "three people died"
      }
    }
  ]
}
```

### --- id=2472 ---

输入文本: Hong Kong must not become a breeding ground for hate Susan Chan denounces the abuse perpetrated by radical protest groups PUBLISHED : Monday , 16 March , 2015 , 2:13pm In recent weeks , there have been protests organised against parallel trading in the New Territories and Tsim Sha Tsui .

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
      "cause": "against parallel trading in the New Territories and Tsim Sha Tsui",
      "effect": "there have been protests organised"
    }
  ],
  "pred_triples": []
}
```

### --- id=69 ---

输入文本: 13 Sep 2014 Three people were sentenced to death by a Yunnan court for their role in the attack at a Kunming rail station that killed 31 people and injured 141 in March .

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
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "their role in the attack at a Kunming rail station that killed 31 people and injured 141 in March .",
      "effect": "Three people were sentenced to death by a Yunnan court"
    },
    {
      "cause": "the attack at a Kunming rail station",
      "effect": "killed 31 people and injured 141 in March"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "their role in the attack at a Kunming rail station that killed 31 people and injured 141 in March"
      },
      "relation": "caused",
      "effect": {
        "span": "Three people were sentenced to death by a Yunnan court"
      }
    }
  ]
}
```

### --- id=290 ---

输入文本: Following the Xiamen incident , the ' not in my backyard ' mentality sparked similar protests in several mainland cities , including Dalian , Guangzhou and Shantou .

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
      "cause": "the Xiamen incident",
      "effect": "the ' not in my backyard ' mentality"
    },
    {
      "cause": "the ' not in my backyard ' mentality",
      "effect": "similar protests in several mainland cities , including Dalian , Guangzhou and Shantou"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Xiamen incident"
      },
      "relation": "caused",
      "effect": {
        "span": "the ' not in my backyard ' mentality sparked similar protests in several mainland cities , including Dalian , Guangzhou and Shantou"
      }
    }
  ]
}
```

### --- id=1886 ---

输入文本: The four doctors had , as a part of the BJP protest , enacted a mock surgery of his skull near the Income Tax circle on Tuesday to support their demand of bringing in the proposed Gujarat Control of Organised Crime ( GUJCOC ) Act .

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
      "cause": "to support their demand of bringing in the proposed Gujarat Control of Organised Crime ( GUJCOC ) Act",
      "effect": "The four doctors had , as a part of the BJP protest , enacted a mock surgery of his skull near the Income Tax circle on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "as a part of the BJP protest"
      },
      "relation": "caused",
      "effect": {
        "span": "The four doctors had enacted a mock surgery of his skull near the Income Tax circle on Tuesday"
      }
    },
    {
      "cause": {
        "span": "to support their demand of bringing in the proposed Gujarat Control of Organised Crime ( GUJCOC ) Act"
      },
      "relation": "caused",
      "effect": {
        "span": "The four doctors had enacted a mock surgery of his skull near the Income Tax circle on Tuesday"
      }
    }
  ]
}
```

### --- id=202 ---

输入文本: ( PICS AVAILABLE ON www.sapapics.co.za ) A crowd of supporters erupted as Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday to address them .

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
      "cause": "Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday to address them",
      "effect": "A crowd of supporters erupted"
    }
  ],
  "pred_triples": []
}
```

### --- id=734 ---

输入文本: Wits students held protests demanding the realisation of free , quality and decolonised education , in line with the call of the # FeesMustFall movement .

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
      "cause": "demanding the realisation of free , quality and decolonised education , in line with the call of the # FeesMustFall movement",
      "effect": "Wits students held protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding the realisation of free , quality and decolonised education"
      },
      "relation": "caused",
      "effect": {
        "span": "Wits students held protests"
      }
    }
  ]
}
```

### --- id=1472 ---

输入文本: The African nationals had sustained minor injuries in the attack that took place in South Delhi 's Mehrauli area on Friday .

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
        "span": "the attack that took place in South Delhi 's Mehrauli area on Friday"
      },
      "relation": "caused",
      "effect": {
        "span": "The African nationals had sustained minor injuries"
      }
    }
  ]
}
```

### --- id=1685 ---

输入文本: The Pathankot incident too exposed how far the malignant cancer of corruption has spread .

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
      "cause": "The Pathankot incident",
      "effect": "too exposed how far the malignant cancer of corruption has spread"
    }
  ],
  "pred_triples": []
}
```

### --- id=170 ---

输入文本: Police clueless about 15 abducted by Maoists 04th November 2011 09:45 PM PATNA : Four days after armed Maoists abducted 15 people , including 12 labourers , in Bihar 's Jamui district , police are still in dark about their whereabouts and have failed to rescue them , officials here said Friday .

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
        "span": "armed Maoists abducted 15 people , including 12 labourers , in Bihar 's Jamui district"
      },
      "relation": "caused",
      "effect": {
        "span": "police are still in dark about their whereabouts and have failed to rescue them"
      }
    }
  ]
}
```

### --- id=273 ---

输入文本: Then on Thursday , some pupils returned to classes after having spent months out of school as residents protested against the Municipal Demarcation Board 's decision to include their areas under a new municipality .

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
      "cause": "residents protested against the Municipal Demarcation Board 's decision to include their areas under a new municipality",
      "effect": "having spent months out of school"
    },
    {
      "cause": "against the Municipal Demarcation Board 's decision to include their areas under a new municipality",
      "effect": "residents protested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "residents protested against the Municipal Demarcation Board 's decision to include their areas under a new municipality"
      },
      "relation": "caused",
      "effect": {
        "span": "some pupils ... spent months out of school"
      }
    }
  ]
}
```

### --- id=2731 ---

输入文本: This is the way Hongkongers show their trust to each other – by showing up and standing up for each other. ” Anger over last week ’ s Yuen Long attack has added fuel to Hong Kong ’ s protest movement , with additional rallies planned for Sunday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "This is the way Hongkongers show their trust to each other",
      "effect": "showing up and standing up for each other"
    },
    {
      "cause": "last week ’ s Yuen Long attack",
      "effect": "Anger"
    },
    {
      "cause": "Anger over last week ’ s Yuen Long attack",
      "effect": "has added fuel to Hong Kong ’ s protest movement"
    },
    {
      "cause": "Anger over last week ’ s Yuen Long attack has added fuel to Hong Kong ’ s protest movement",
      "effect": "additional rallies planned for Sunday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Anger over last week ' s Yuen Long attack"
      },
      "relation": "caused",
      "effect": {
        "span": "added fuel to Hong Kong ' s protest movement"
      }
    }
  ]
}
```

### --- id=2275 ---

输入文本: So what has the three-day strike which put the common man through the wringer , finally achieved ?

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
        "span": "the three-day strike"
      },
      "relation": "caused",
      "effect": {
        "span": "put the common man through the wringer"
      }
    }
  ]
}
```

### --- id=1580 ---

输入文本: Police injured in stone pelting 29th January 2012 01:34 AM JCBs being pressed into service in the road widening drive at Kolar on Saturday | Express Photo KOLAR : Tension prevailed at Ammavarpet in the city after protestors pelted stones at police who accompanied officials in a road-widening drive on Saturday .

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
      "cause": "protestors pelted stones at police who accompanied officials in a road-widening drive on Saturday",
      "effect": "Tension prevailed at Ammavarpet in the city"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "protestors pelted stones at police"
      },
      "relation": "caused",
      "effect": {
        "span": "Tension prevailed at Ammavarpet in the city"
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
    }
  ]
}
```

### --- id=299 ---

输入文本: “ The youth was killed at a protest against the Army ’ s action halting the vehicles , ” alleged Mohammad Yasin Khan , head of a traders ’ body .

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
        "span": "at a protest against the Army ' s action halting the vehicles"
      },
      "relation": "caused",
      "effect": {
        "span": "The youth was killed"
      }
    }
  ]
}
```

### --- id=125 ---

输入文本: Beijing launched a campaign to ' educate ' Tibetan monks and nuns after unrest rocked Tibetan-populated areas in March 2008 .

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
      "cause": "to ' educate ' Tibetan monks and nuns",
      "effect": "Beijing launched a campaign"
    },
    {
      "cause": "unrest rocked Tibetan-populated areas in March 2008",
      "effect": "to ' educate ' Tibetan monks and nuns"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "unrest rocked Tibetan-populated areas in March 2008"
      },
      "relation": "caused",
      "effect": {
        "span": "Beijing launched a campaign to ' educate ' Tibetan monks and nuns"
      }
    }
  ]
}
```

### --- id=1169 ---

输入文本: 19th July 2016 05:10 PM MORIGAON : Normal life in Central Assam was today affected by a 12 - hour bandh called by several organisations to press their demands for setting up AIIMS at Raha and a judicial inquiry into the death of a person in clashes between police and protesters there three days back .

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
      "cause": "a 12 - hour bandh called by several organisations",
      "effect": "Normal life in Central Assam was today affected"
    },
    {
      "cause": "to press their demands for setting up AIIMS at Raha and a judicial inquiry into the death of a person in clashes between police and protesters there three days back",
      "effect": "a 12 - hour bandh called by several organisations"
    },
    {
      "cause": "clashes between police and protesters there three days back",
      "effect": "the death of a person"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to press their demands for setting up AIIMS at Raha and a judicial inquiry into the death of a person in clashes between police and protesters there three days back"
      },
      "relation": "caused",
      "effect": {
        "span": "a 12 - hour bandh called by several organisations"
      }
    },
    {
      "cause": {
        "span": "a 12 - hour bandh called by several organisations to press their demands for setting up AIIMS at Raha and a judicial inquiry into the death of a person in clashes between police and protesters there three days back"
      },
      "relation": "caused",
      "effect": {
        "span": "Normal life in Central Assam was today affected"
      }
    }
  ]
}
```

### --- id=1134 ---

输入文本: It was followed by a series of attempts to derail trains on the Erode-Coimbatore section , by placing boulders on the track .

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
      "cause": "placing boulders on the track",
      "effect": "a series of attempts to derail trains on the Erode-Coimbatore section"
    }
  ],
  "pred_triples": []
}
```

### --- id=934 ---

输入文本: KCR , who was arrested Sunday and sent to judicial custody for 14 days ahead of his ' fast unto death ' , launched the hunger strike in Khammam sub-jail .

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
      "cause": "KCR , who was arrested Sunday and sent to judicial custody for 14 days ahead of his ' fast unto death",
      "effect": "launched the hunger strike in Khammam sub-jail"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "his ' fast unto death '"
      },
      "relation": "caused",
      "effect": {
        "span": "KCR , who was arrested Sunday and sent to judicial custody for 14 days"
      }
    }
  ]
}
```

### --- id=2232 ---

输入文本: A woman was killed because of one of the explosions that ripped a hole in the northern wall of a mosque in Soweto 's Dhlamini area .

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
      "cause": "one of the explosions that ripped a hole in the northern wall of a mosque in Soweto 's Dhlamini area",
      "effect": "A woman was killed"
    },
    {
      "cause": "one of the explosions",
      "effect": "that ripped a hole in the northern wall of a mosque in Soweto 's Dhlamini area"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "one of the explosions that ripped a hole in the northern wall of a mosque in Soweto 's Dhlamini area"
      },
      "relation": "caused",
      "effect": {
        "span": "A woman was killed"
      }
    }
  ]
}
```

### --- id=2711 ---

输入文本: KARNATAKA Gulbarga city observes near-total bandh Joining hands : Members of several organisations taking out a rally in support of the former Minister S.K. Kanta , who is leading the pourakarmikas ' agitation , in Gulbarga on Friday .

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "in support of the former Minister S.K. Kanta",
      "effect": "Members of several organisations taking out a rally"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in support of the former Minister S.K. Kanta , who is leading the pourakarmikas ' agitation"
      },
      "relation": "caused",
      "effect": {
        "span": "Members of several organisations taking out a rally in Gulbarga on Friday"
      }
    }
  ]
}
```

### --- id=1109 ---

输入文本: At the Osmania University in Hyderabad , police stopped students trying to take out a rally in support of ' Sadak Bandh ' .

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
      "cause": "in support of ' Sadak Bandh '",
      "effect": "students trying to take out a rally"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "trying to take out a rally in support of ' Sadak Bandh '"
      },
      "relation": "caused",
      "effect": {
        "span": "police stopped students"
      }
    }
  ]
}
```

### --- id=2556 ---

输入文本: “ My film might provide them with an opportunity to look back at what happened during the protests so that they can tidy up their thoughts and emotions . ”

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
      "cause": "My film might provide them with an opportunity to look back at what happened during the protests",
      "effect": "they can tidy up their thoughts and emotions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "so that they can tidy up their thoughts and emotions"
      },
      "relation": "caused",
      "effect": {
        "span": "My film might provide them with an opportunity to look back at what happened during the protests"
      }
    }
  ]
}
```

### --- id=1065 ---

输入文本: The final leg of the march would be to deliver memorandums to the SA Chamber of Mines , the Johannesburg central police station , the office of the auditor general , and the Hawks .

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
      "cause": "would be to deliver memorandums to the SA Chamber of Mines , the Johannesburg central police station , the office of the auditor general , and the Hawks",
      "effect": "The final leg of the march"
    }
  ],
  "pred_triples": []
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
      "cause": "residents of Virupatchipuram , of ward 41 of Vellore Corporation , demanded an apology and transfer of a woman sub-inspector ( SI ) attached to the Bagayam police station",
      "effect": "High drama was witnessed on Arni Road on Wednesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "water stir"
      },
      "relation": "caused",
      "effect": {
        "span": "High drama was witnessed on Arni Road on Wednesday"
      }
    },
    {
      "cause": {
        "span": "protest against cop"
      },
      "relation": "caused",
      "effect": {
        "span": "residents of Virupatchipuram , of ward 41 of Vellore Corporation , demanded an apology and transfer of a woman sub-inspector ( SI ) attached to the Bagayam police station"
      }
    }
  ]
}
```

### --- id=2945 ---

输入文本: The court found Shahzad guilty of murder , attempt to murder , obstructing and assaulting public servants and grievously injuring the police officers to deter them from performing their duty .

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
      "cause": "to deter them from performing their duty",
      "effect": "The court found Shahzad guilty of murder , attempt to murder , obstructing and assaulting public servants and grievously injuring the police officers"
    },
    {
      "cause": "murder , attempt to murder , obstructing and assaulting public servants and grievously injuring the police officers to deter them from performing their duty",
      "effect": "The court found Shahzad guilty"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "murder , attempt to murder , obstructing and assaulting public servants and grievously injuring the police officers"
      },
      "relation": "caused",
      "effect": {
        "span": "The court found Shahzad guilty"
      }
    },
    {
      "cause": {
        "span": "to deter them from performing their duty"
      },
      "relation": "caused",
      "effect": {
        "span": "grievously injuring the police officers"
      }
    }
  ]
}
```

### --- id=2190 ---

输入文本: The incident took place at 8 am when Anurag Pandey , the newly elected LMC corporator from Mallahi Tola -1 , and his supporters had an argument with LMC sanitation workers Arun Kumar , Anil Kumar , Sachidanand , and their colleagues over the cleaning of streets in the locality .

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
      "cause": "Anurag Pandey , the newly elected LMC corporator from Mallahi Tola -1 , and his supporters had an argument with LMC sanitation workers Arun Kumar , Anil Kumar , Sachidanand , and their colleagues",
      "effect": "The incident took place at 8 am"
    },
    {
      "cause": "the cleaning of streets in the locality",
      "effect": "Anurag Pandey , the newly elected LMC corporator from Mallahi Tola -1 , and his supporters had an argument with LMC sanitation workers Arun Kumar , Anil Kumar , Sachidanand , and their colleagues"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over the cleaning of streets in the locality"
      },
      "relation": "caused",
      "effect": {
        "span": "Anurag Pandey , the newly elected LMC corporator from Mallahi Tola -1 , and his supporters had an argument with LMC sanitation workers Arun Kumar , Anil Kumar , Sachidanand , and their colleagues"
      }
    }
  ]
}
```

### --- id=1775 ---

输入文本: The memorandum called for the State to refuse bail for murderers , saying residents could be tempted to take the law into their own hands .

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
    "tp": 0,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "saying residents could be tempted to take the law into their own hands",
      "effect": "The memorandum called for the State to refuse bail for murderers"
    },
    {
      "cause": "called for the State to refuse bail for murderers",
      "effect": "The memorandum"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "residents could be tempted to take the law into their own hands"
      },
      "relation": "caused",
      "effect": {
        "span": "The memorandum called for the State to refuse bail for murderers"
      }
    }
  ]
}
```

### --- id=2351 ---

输入文本: PTI BANGALORE : All courts will be shut on Saturday after Friday 's violence the city 's civil court premises .

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
      "cause": "Friday 's violence the city 's civil court premises",
      "effect": "All courts will be shut on Saturday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Friday 's violence"
      },
      "relation": "caused",
      "effect": {
        "span": "All courts will be shut on Saturday"
      }
    }
  ]
}
```

### --- id=2797 ---

输入文本: Though rebels frequent the villages including Karada , Ranaba and Indragada , this is for the first time that posters exhorting the villagers to participate in the PLGA week have been found at several places in the block .

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
      "cause": "participate in the PLGA week",
      "effect": "posters exhorting the villagers"
    }
  ],
  "pred_triples": []
}
```

### --- id=49 ---

输入文本: VS condemns attack on NSS Karayogams 08th May 2011 05:00 AM THIRUVANANTHAPURAM : Chief Minister V S Achuthanandan has condemned the recent attacks on NSS Karayogams .

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
        "span": "the recent attacks on NSS Karayogams"
      },
      "relation": "caused",
      "effect": {
        "span": "Chief Minister V S Achuthanandan has condemned the recent attacks on NSS Karayogams"
      }
    }
  ]
}
```

### --- id=2408 ---

输入文本: 2 Shiv Sainiks held for threat to Navale Posted : Wed Jul 22 1998 IST July 21 : The Cuffe Parade police today arrested two persons and registered a case of rioting against 18 others in connection with the surprise attack on the bungalows of Shiv Sena minister Suresh Navale and former minister Gulabrao Gavande .

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "the surprise attack on the bungalows of Shiv Sena minister Suresh Navale and former minister Gulabrao Gavande",
      "effect": "The Cuffe Parade police today arrested two persons and registered a case of rioting against 18 others"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the surprise attack on the bungalows of Shiv Sena minister Suresh Navale and former minister Gulabrao Gavande"
      },
      "relation": "caused",
      "effect": {
        "span": "The Cuffe Parade police today arrested two persons and registered a case of rioting against 18 others in connection with the surprise attack on the bungalows of Shiv Sena minister Suresh Navale and former minister Gulabrao Gavande"
      }
    }
  ]
}
```

### --- id=1903 ---

输入文本: May 21 : CPI-Maoist cadres shot dead three persons and injured another at Kotam village in Gumla district of Jharkhand .

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
        "span": "CPI-Maoist cadres shot dead three persons and injured another at Kotam village in Gumla district of Jharkhand"
      },
      "relation": "caused",
      "effect": {
        "span": "three persons were killed and another was injured"
      }
    }
  ]
}
```

### --- id=1881 ---

输入文本: Without naming Railway Minister Mamata Banerjee , who recently organised a controversial rally in Lalgarh , Mr. Agarwal wanted to know whether the government would take action against “ influential ” people who were openly supporting the Maoists .

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
      "cause": "against “ influential ” people who were openly supporting the Maoists",
      "effect": "the government would take action"
    }
  ],
  "pred_triples": []
}
```

### --- id=600 ---

输入文本: MEDIA Caixin reporter freed on bail after forced demolition campaign Qingdao prosecutors order release of Chen Baocheng , lawyers involved in the case say .

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
      "cause": "forced demolition campaign Qingdao prosecutors order release of Chen Baocheng",
      "effect": "Caixin reporter freed on bail"
    }
  ],
  "pred_triples": []
}
```

### --- id=473 ---

输入文本: The police claimed they were killed while trying to blow up the local bus station .

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
      "cause": "trying to blow up the local bus station",
      "effect": "The police claimed they were killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "trying to blow up the local bus station"
      },
      "relation": "caused",
      "effect": {
        "span": "they were killed"
      }
    }
  ]
}
```

### --- id=1671 ---

输入文本: Speaking beside Lam , police chief Stephen Lo said : “ Protesters ’ violent acts have far exceeded the bottom line of peaceful expressions of demands. ” A joint statement from 41 pro-government lawmakers condemned what they described as “ extremely radical and violent acts ” , such as the occupying of roads and vandalism of the council building .

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
        "span": "Protesters ’ violent acts have far exceeded the bottom line of peaceful expressions of demands."
      },
      "relation": "caused",
      "effect": {
        "span": "A joint statement from 41 pro-government lawmakers condemned what they described as “ extremely radical and violent acts ” , such as the occupying of roads and vandalism of the council building ."
      }
    }
  ]
}
```

### --- id=1728 ---

输入文本: It is being alleged that racism could have been one of the triggers for the quarrel .

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
      "cause": "racism",
      "effect": "the quarrel"
    }
  ],
  "pred_triples": []
}
```

### --- id=1168 ---

输入文本: Normal life hit in Central Assam by bandh over AIIMS

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
      "cause": "bandh",
      "effect": "Normal life hit in Central Assam"
    },
    {
      "cause": "AIIMS",
      "effect": "bandh"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over AIIMS"
      },
      "relation": "caused",
      "effect": {
        "span": "Normal life hit in Central Assam by bandh"
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
      "cause": "his name was dragged into the 1984 anti-Sikh riots",
      "effect": "A move by Bollywood superstar Amitabh Bachchan to get a clean chit from the Sikh clergy"
    },
    {
      "cause": "to get a clean chit from the Sikh clergy",
      "effect": "A move by Bollywood superstar Amitabh Bachchan"
    }
  ],
  "pred_triples": []
}
```

### --- id=1526 ---

输入文本: 5,000 docs quit , crisis in Rajasthan

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
      "cause": "5,000 docs quit",
      "effect": "crisis in Rajasthan"
    }
  ],
  "pred_triples": []
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

### --- id=1552 ---

输入文本: 26th April 2014 09:26 AM Nearly three months after an AIADMK functionary was chased and hacked to death in full public view near the busy Chengalpattu government hospital , the victim ’ s wife and relatives staged a hunger strike demanding that the police arrest those who masterminded the murder .

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
      "cause": "demanding that the police arrest those who masterminded the murder",
      "effect": "the victim ’ s wife and relatives staged a hunger strike"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding that the police arrest those who masterminded the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "the victim ’ s wife and relatives staged a hunger strike"
      }
    },
    {
      "cause": {
        "span": "an AIADMK functionary was chased and hacked to death in full public view near the busy Chengalpattu government hospital"
      },
      "relation": "caused",
      "effect": {
        "span": "the victim ’ s wife and relatives staged a hunger strike demanding that the police arrest those who masterminded the murder"
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
      "cause": "to disperse a group of about 300 people protesting against poor service delivery in Landsdowne Road",
      "effect": "Police used rubber bullets"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "protesting against poor service delivery"
      },
      "relation": "caused",
      "effect": {
        "span": "Police used rubber bullets to disperse a group of about 300 people"
      }
    }
  ]
}
```

### --- id=2560 ---

输入文本: Confirming that Jagan had not taken food for the second consecutive day on Monday , Chanchalguda jail superintendent B Saidaiah said Jagan had refused food , in violation of prison rules .

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
      "cause": "Jagan had refused food",
      "effect": "in violation of prison rules"
    }
  ],
  "pred_triples": []
}
```

### --- id=2744 ---

输入文本: Over 250 people participated in the rally in support of the campaign .

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
        "span": "in support of the campaign"
      },
      "relation": "caused",
      "effect": {
        "span": "Over 250 people participated in the rally"
      }
    }
  ]
}
```

### --- id=979 ---

输入文本: Govt urged to take over Nellimarla jute mill 24th July 2009 03:08 AM HYDERABAD : Representatives of the Nellimarla Jute Mill Karmika Sangham , affiliated to IFTU , today urged Chief Minister YS Rajasekhara Reddy to intervene in resolving their problems and to put an end to the 10 - month-old strike involving about 5,000 jute mill workers at Nellimarla in Vizianagaram district .

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
        "span": "to intervene in resolving their problems and to put an end to the 10 - month-old strike involving about 5,000 jute mill workers at Nellimarla in Vizianagaram district"
      },
      "relation": "caused",
      "effect": {
        "span": "Representatives of the Nellimarla Jute Mill Karmika Sangham , affiliated to IFTU , today urged Chief Minister YS Rajasekhara Reddy"
      }
    }
  ]
}
```

### --- id=1037 ---

输入文本: Union Home Minister Sushilkumar Shinde , sources said , had a lot of explaining to do as to “ how ” such an incident took place in the heart of the city and “ why ” the Delhi Police came down so heavily on the youth who were legitimately protesting against the incident to demand immediate action against the culprits .

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
      "cause": "against the incident to demand immediate action against the culprits",
      "effect": "the youth who were legitimately protesting"
    }
  ],
  "pred_triples": []
}
```

### --- id=469 ---

输入文本: Curfew in Kashmir town for fourth day following clashes

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
      "cause": "clashes",
      "effect": "Curfew in Kashmir town for fourth day"
    }
  ],
  "pred_triples": []
}
```

### --- id=1058 ---

输入文本: The TDP members , holding placards , raised slogans against the ‘ negligent ' attitude of the government in taking steps to protect the interests of farmers .

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
      "cause": "against the ‘ negligent ' attitude of the government in taking steps to protect the interests of farmers",
      "effect": "The TDP members , holding placards , raised slogans"
    },
    {
      "cause": "to protect the interests of farmers",
      "effect": "taking steps"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the ‘ negligent ' attitude of the government in taking steps to protect the interests of farmers"
      },
      "relation": "caused",
      "effect": {
        "span": "The TDP members , holding placards , raised slogans against the ‘ negligent ' attitude of the government in taking steps to protect the interests of farmers"
      }
    }
  ]
}
```

### --- id=1762 ---

输入文本: 03rd June 2014 08:50 AM BHUBANESWAR : Outrage over large-scale discrepancy in Plus-Two results spilled on to the streets as hundreds of students and their parents laid siege to the Council of Higher Secondary Education ( CHSE ) head office here on Monday prompting the Higher Education department to order a re-verification within 48 hours .

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
      "cause": "hundreds of students and their parents laid siege to the Council of Higher Secondary Education ( CHSE ) head office here on Monday",
      "effect": "Outrage over large-scale discrepancy in Plus-Two results spilled on to the streets"
    },
    {
      "cause": "large-scale discrepancy in Plus-Two results",
      "effect": "Outrage"
    },
    {
      "cause": "hundreds of students and their parents laid siege to the Council of Higher Secondary Education ( CHSE ) head office here on Monday",
      "effect": "prompting the Higher Education department to order a re-verification within 48 hours"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "large-scale discrepancy in Plus-Two results"
      },
      "relation": "caused",
      "effect": {
        "span": "Outrage ... spilled on to the streets as hundreds of students and their parents laid siege to the Council of Higher Secondary Education ( CHSE ) head office here on Monday"
      }
    },
    {
      "cause": {
        "span": "hundreds of students and their parents laid siege to the Council of Higher Secondary Education ( CHSE ) head office here on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "the Higher Education department to order a re-verification within 48 hours"
      }
    }
  ]
}
```

### --- id=938 ---

输入文本: - Indian Express Express News Service , Express News Service : Chandigarh , Fri Jul 01 2011 , 03:05 hrs The Chandigarh unit of Bahujan Samaj Party held a protest at the rally ground in Sector 25 against the rising prices of cooking gas , petrol , diesel , etc. The protest is part of a nationwide campaign of the party on the issue .

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
      "cause": "against the rising prices of cooking gas , petrol , diesel , etc",
      "effect": "The Chandigarh unit of Bahujan Samaj Party held a protest at the rally ground in Sector 25"
    },
    {
      "cause": "is part of a nationwide campaign of the party on the issue",
      "effect": "The protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the rising prices of cooking gas , petrol , diesel , etc."
      },
      "relation": "caused",
      "effect": {
        "span": "The Chandigarh unit of Bahujan Samaj Party held a protest at the rally ground in Sector 25"
      }
    }
  ]
}
```

### --- id=716 ---

输入文本: Special team to probe 04th April 2009 12:12 AM THIRUVANANTHAPURAM : A special team led by City Control Room Assistant Commissioner Suresh Kumar will inquire into the destruction of the Chattambi Swami idol at Kannammoola .

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
        "span": "the destruction of the Chattambi Swami idol at Kannammoola"
      },
      "relation": "caused",
      "effect": {
        "span": "A special team led by City Control Room Assistant Commissioner Suresh Kumar will inquire into the destruction of the Chattambi Swami idol at Kannammoola"
      }
    }
  ]
}
```

### --- id=2266 ---

输入文本: Although these only represented a minority and disorganised voice - even among those present at last Sunday 's protest - this was still enough to set alarm bells ringing that discontent with the Government 's performance in recent years might spin out of control and pose a serious challenge to the authority of Mr Tung 's leadership .

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
      "cause": "these only represented a minority and disorganised voice - even among those present at last Sunday 's protest",
      "effect": "this was still enough to set alarm bells ringing"
    },
    {
      "cause": "discontent with the Government 's performance in recent years might spin out of control",
      "effect": "pose a serious challenge to the authority of Mr Tung 's leadership"
    }
  ],
  "pred_triples": []
}
```

### --- id=931 ---

输入文本: A group of TRS workers fled after setting the office on fire .

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
        "span": "setting the office on fire"
      },
      "relation": "caused",
      "effect": {
        "span": "A group of TRS workers fled"
      }
    }
  ]
}
```

### --- id=2066 ---

输入文本: It is not a time of celebration , there are no winners in this strike , '' Magara said .

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
      "cause": "there are no winners in this strike",
      "effect": "It is not a time of celebration"
    }
  ],
  "pred_triples": []
}
```

### --- id=2947 ---

输入文本: The police had reached Batla House on a tip off that some suspected militants involved in the blasts were holed up in the building .

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
        "span": "a tip off that some suspected militants involved in the blasts were holed up in the building"
      },
      "relation": "caused",
      "effect": {
        "span": "The police had reached Batla House"
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
        "span": "Muslim organisations called the hartal on Tuesday"
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

### --- id=2568 ---

输入文本: Han Dongfang , who was jailed as a leader of the Tiananmen protests and now runs the workers ’ advocacy group China Labour Bulletin from Hong Kong , believes Beijing can compromise when it sees it is necessary .

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
      "cause": "it sees it is necessary",
      "effect": "Beijing can compromise"
    }
  ],
  "pred_triples": []
}
```

### --- id=534 ---

输入文本: Tribal Affairs Minister V Kishore Chandra Deo today dubbed anti-Maoist militia Salwa Judum as a " sinful strategy " , bringing to the fore apparent differences in Congress over the approach to Maoists who last week wiped out party leadership in Chhattisgarh in a deadly attack .

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
      "cause": "Tribal Affairs Minister V Kishore Chandra Deo today dubbed anti-Maoist militia Salwa Judum as a \" sinful strategy \"",
      "effect": "bringing to the fore apparent differences in Congress over the approach to Maoists who last week wiped out party leadership in Chhattisgarh in a deadly attack"
    },
    {
      "cause": "a deadly attack",
      "effect": "Maoists who last week wiped out party leadership in Chhattisgarh"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Maoists who last week wiped out party leadership in Chhattisgarh in a deadly attack"
      },
      "relation": "caused",
      "effect": {
        "span": "bringing to the fore apparent differences in Congress over the approach to Maoists"
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
      "cause": "may be aimed at instilling fear in the minds of the people in general and of our party workers in particular",
      "effect": "These attacks and killings"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "These attacks and killings may be aimed at instilling fear in the minds of the people in general and of our party workers in particular"
      },
      "relation": "caused",
      "effect": {
        "span": "the statement read and demanded a Special Investigation Team to go into each of the incidents"
      }
    }
  ]
}
```

### --- id=2545 ---

输入文本: The violence that followed in Nandigram was due to them for which the BJP was criticising the CPI(M) , he added .

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
      "cause": "them for which the BJP was criticising the CPI(M)",
      "effect": "The violence that followed in Nandigram"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "them"
      },
      "relation": "caused",
      "effect": {
        "span": "The violence that followed in Nandigram"
      }
    },
    {
      "cause": {
        "span": "The violence that followed in Nandigram was due to them"
      },
      "relation": "caused",
      "effect": {
        "span": "the BJP was criticising the CPI(M)"
      }
    }
  ]
}
```

### --- id=2824 ---

输入文本: UFBU is meeting at Hyderabad on December 23 to discuss further course of action and the next phase of the agitation , Venkatachalam said .

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
        "span": "to discuss further course of action and the next phase of the agitation"
      },
      "relation": "caused",
      "effect": {
        "span": "UFBU is meeting at Hyderabad on December 23"
      }
    }
  ]
}
```
