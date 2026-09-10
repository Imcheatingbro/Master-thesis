# Gemma 4 26B A4B QAT CNC validation zero-shot eval report

## 配置
```json
{
  "label": "Gemma 4 26B A4B QAT CNC validation zero-shot",
  "model": "google/gemma-4-26b-a4b-qat",
  "dataset": "cnc_sft_validation",
  "sample_count": 500,
  "prompt_name": "v9.8_zero_shot",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 0,
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
  "llm_extra_body": null,
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
================ Gemma 4 26B A4B QAT CNC validation zero-shot final report ================
样本总数: 500
  Gold 含因果: 264 | Pred 含因果: 311
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.794
  Precision: 0.759
  Recall   : 0.894
  F1       : 0.821
  (TP=236, TN=161, FP=75, FN=28)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 500
    Gold triples: 366 | Pred triples: 364
    Precision: 0.401
    Recall   : 0.399
    F1       : 0.400
    (TP=146, FP=218, FN=220)
  [anchor_window] (primary)
    样本数: 500
    Gold triples: 366 | Pred triples: 364
    Precision: 0.393
    Recall   : 0.391
    F1       : 0.392
    (TP=143, FP=221, FN=223)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 236
    Gold triples: 330 | Pred triples: 278
    Precision: 0.525
    Recall   : 0.442
    F1       : 0.480
    (TP=146, FP=132, FN=184)
  [anchor_window] (primary)
    样本数: 236
    Gold triples: 330 | Pred triples: 278
    Precision: 0.514
    Recall   : 0.433
    F1       : 0.470
    (TP=143, FP=135, FN=187)
================================================
```

## 生成失败统计
```json
{
  "total": 9,
  "by_type": {
    "no_json_object": 9
  },
  "samples": [
    {
      "id": 617,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    },
    {
      "id": 3063,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    },
    {
      "id": 123,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    },
    {
      "id": 3045,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    },
    {
      "id": 923,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    },
    {
      "id": 1412,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    },
    {
      "id": 900,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    },
    {
      "id": 5,
      "error_type": "no_json_object",
      "error_message": "未找到 JSON 对象"
    },
    {
      "id": 1169,
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

Sample details shown: first 200 of 261 wrong samples from 500 total samples.

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
        "span": "Some schools which had to postpone their mid-term examinations"
      }
    }
  ]
}
```

### --- id=407 ---

输入文本: It ended only when the police removed all 850 workers from inside the plant on Saturday morning and detained them at two locations in Oragadam .

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
        "span": "the police removed all 850 workers from inside the plant on Saturday morning and detained them at two locations in Oragadam"
      },
      "relation": "caused",
      "effect": {
        "span": "It ended"
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
        "span": "a gun battle with the police"
      },
      "relation": "caused",
      "effect": {
        "span": "Two Maoist guerrillas were killed in a gun battle with the police in Orissa 's Malkangiri district"
      }
    }
  ]
}
```

### --- id=2873 ---

输入文本: Prosecutor Riekie Krause said on Monday that Sekhakhane had confessed to killing Chika and had led police to his gun .

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
        "span": "killing Chika"
      },
      "relation": "caused",
      "effect": {
        "span": "had led police to his gun"
      }
    },
    {
      "cause": {
        "span": "killing Chika"
      },
      "relation": "caused",
      "effect": {
        "span": "had confessed to killing Chika"
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
      "cause": "Police today arrested two top militants",
      "effect": "claimed to have solved the bomb blast at the high-security MLA hostel in Srinagar last year"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the bomb blast at the high-security MLA hostel in Srinagar last year"
      },
      "relation": "caused",
      "effect": {
        "span": "Police today arrested two top militants"
      }
    }
  ]
}
```

### --- id=297 ---

输入文本: “ Amid stone-throwing , some rounds were fired at the convoy going to Kupwara .

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
        "span": "stone-throwing"
      },
      "relation": "caused",
      "effect": {
        "span": "some rounds were fired at the convoy going to Kupwara"
      }
    }
  ]
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
        "span": "Chhattisgarh Chief Minister Raman Singh strongly condemned the attack , describing it as most unfortunate and cowardly act of Maoists"
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
        "span": "the increase in school and admission fee"
      },
      "relation": "caused",
      "effect": {
        "span": "Parents and guardians of students from Lord Mahavira Jain Public School , Ambala Cantonment , held a demonstration and dharna , on Thursday , to mark their protest against the increase in school and admission fee"
      }
    }
  ]
}
```

### --- id=1838 ---

输入文本: On Monday , the African National Congress condemned the shooting of Malunga , the Oshabeni branch chairman , and Chiliza , the branch secretary .

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
        "span": "the shooting of Malunga , the Oshabeni branch chairman , and Chiliza , the branch secretary"
      },
      "relation": "caused",
      "effect": {
        "span": "the African National Congress condemned the shooting of Malunga , the Oshabeni branch chairman , and Chiliza , the branch secretary"
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
        "span": "he had violated his bail conditions related to an earlier case when he was arrested during student protests in February last year"
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
        "span": "there was no evidence against the two"
      },
      "relation": "caused",
      "effect": {
        "span": "the trial court and the Bombay High Court acquitted the two"
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
    "tp": 2,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 1
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
        "span": "the medical crisis in Rajasthan"
      }
    },
    {
      "cause": {
        "span": "an indefinite strike by doctors"
      },
      "relation": "caused",
      "effect": {
        "span": "crippled health services and left over a dozen patients dead"
      }
    },
    {
      "cause": {
        "span": "an indefinite strike by doctors"
      },
      "relation": "caused",
      "effect": {
        "span": "the medical crisis in Rajasthan ... deepened on Friday with 5,000 doctors submitting their resignations"
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
      "cause": "opposed to development",
      "effect": "the shutdown"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the shutdown"
      },
      "relation": "caused",
      "effect": {
        "span": "Nitish Kumar termed the shutdown opposed to development"
      }
    }
  ]
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

### --- id=1754 ---

输入文本: Meanwhile , political activists continued their protest in several places in Tamil Nadu , particularly districts fed by the Mullaperiyar waters , to protest Kerala 's refusal to raise the storage level in the dam .

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
      "cause": "to protest Kerala 's refusal to raise the storage level in the dam",
      "effect": "political activists continued their protest in several places in Tamil Nadu , particularly districts fed by the Mullaperiyar waters"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Kerala 's refusal to raise the storage level in the dam"
      },
      "relation": "caused",
      "effect": {
        "span": "political activists continued their protest in several places in Tamil Nadu , particularly districts fed by the Mullaperiyar waters , to protest Kerala 's refusal to raise the storage level in the dam"
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
        "span": "When they failed to comply"
      },
      "relation": "caused",
      "effect": {
        "span": "a team of MC officials was dispatched to serve a final notice"
      }
    },
    {
      "cause": {
        "span": "a team of MC officials was dispatched to serve a final notice"
      },
      "relation": "caused",
      "effect": {
        "span": "which came under attack by the mob"
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
        "span": "the government decision to include the government Secretariat in the Kerala Administrative Service ( KAS )"
      },
      "relation": "caused",
      "effect": {
        "span": "A strike called by a section of employees against the government decision to include the government Secretariat in the Kerala Administrative Service ( KAS ) crippled the functioning of the State administrative headquarters on Thursday"
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
      "cause": "against the agitation in Singur",
      "effect": "This false propaganda is being carried out"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the agitation in Singur"
      },
      "relation": "caused",
      "effect": {
        "span": "This false propaganda is being carried out against"
      }
    }
  ]
}
```

### --- id=271 ---

输入文本: The protest march started at 7.30 p.m. but the police blocked it before it reached the venue .

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
        "span": "the police blocked it"
      },
      "relation": "caused",
      "effect": {
        "span": "the protest march started at 7.30 p.m. but the police blocked it before it reached the venue"
      }
    }
  ]
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
        "span": "The alleged attack on Nagari YSRC MLA RK Roja by some TDP men at Nagari on Friday mid-night , when she went there for offering the ‘ first Harathi ’ to the processional deity of Goddess Gangamma "
      },
      "relation": "caused",
      "effect": {
        "span": "tension in and round the town on Saturday with the actress-turned-politician and her supports staging widespread protests over the incident "
      }
    }
  ]
}
```

### --- id=286 ---

输入文本: Authorities yesterday said they would scrap the 10.4 billion yuan ( HK $ 12.7 billion ) project , the subject of demonstrations by tens of thousands of Shifang residents .

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
      "cause": "the subject of demonstrations by tens of thousands of Shifang residents",
      "effect": "they would scrap the 10.4 billion yuan ( HK $ 12.7 billion ) project"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demonstrations by tens of thousands of Shifang residents"
      },
      "relation": "caused",
      "effect": {
        "span": "the 10.4 billion yuan ( HK $ 12.7 billion ) project"
      }
    }
  ]
}
```

### --- id=2039 ---

输入文本: They protested against the Circle Inspector 's highhandedness .

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
      "cause": "against the Circle Inspector 's highhandedness",
      "effect": "They protested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Circle Inspector 's highhandedness"
      },
      "relation": "caused",
      "effect": {
        "span": "They protested against the Circle Inspector 's highhandedness"
      }
    }
  ]
}
```

### --- id=1174 ---

输入文本: A special three-judge bench of the Allahabad High Court 's Lucknow bench Thursday by a majority verdict ruled that the place where the Babri Masjid in Ayodhya stood , before it was razed by Hindu mobs in 1992 , was indeed the birthplace of Hindu god Ram .

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
        "span": "Hindu mobs in 1992"
      },
      "relation": "caused",
      "effect": {
        "span": "the Babri Masjid in Ayodhya stood , before it was razed by Hindu mobs in 1992"
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
      "cause": "two farmers accused of the murder of Matlhomola Jonas Mosweu were granted bail",
      "effect": "the violence that flared up in Coligny , in the North West"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
}
```

### --- id=1860 ---

输入文本: The DGP said steps have been taken to prevent the escalation of violence .

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
      "cause": "to prevent the escalation of violence",
      "effect": "steps have been taken"
    }
  ],
  "pred_triples": []
}
```

### --- id=1862 ---

输入文本: Assistant Sub Inspector Bhaskaran was attacked by a mob of about 25 hartal supporters .

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
        "span": "a mob of about 25 hartal supporters"
      },
      "relation": "caused",
      "effect": {
        "span": "Assistant Sub Inspector Bhaskaran was attacked"
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

### --- id=2318 ---

输入文本: Two photographers with The Indian Express  Prashant Nadkar and Ganesh Shirsekar  were also assaulted and threatened by the mob .

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
        "span": "the mob"
      },
      "relation": "caused",
      "effect": {
        "span": "Two photographers with The Indian Express  Prashant Nadkar and Ganesh Shirsekar  were also assaulted and threatened"
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
        "span": "the house"
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

### --- id=301 ---

输入文本: The action helped launch a 79-day street occupation that was described as the greatest challenge to China ’ s Communist rulers since the 1989 Tiananmen protests .

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
      "cause": "The action",
      "effect": "a 79-day street occupation that was described as the greatest challenge to China ’ s Communist rulers since the 1989 Tiananmen protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The action"
      },
      "relation": "caused",
      "effect": {
        "span": "launch a 79-day street occupation"
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

### --- id=2069 ---

输入文本: James Leibold , a Xinjiang expert from Australia ’ s La Trobe university , said that ever since deadly ethnic rioting in 2009 authorities had gradually been transforming the region into a police state in a bid to halt the killing .

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
        "span": "authorities had gradually been transforming the region into a police state in a bid to halt the killing"
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
        "span": "the issue of putting up religious flags"
      },
      "relation": "caused",
      "effect": {
        "span": "communal clashes that began on Saturday last over the issue of putting up religious flags"
      }
    }
  ]
}
```

### --- id=2382 ---

输入文本: “ It is apparent that all these attacks are undertaken with detailed planning and after surveillance of the movements of these activists .

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
        "span": "detailed planning and after surveillance of the movements of these activists"
      },
      "relation": "caused",
      "effect": {
        "span": "all these attacks are undertaken"
      }
    }
  ]
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
        "span": "a controversial bill that would allow suspects to be extradited from Hong Kong to mainland China"
      },
      "relation": "caused",
      "effect": {
        "span": "The protests , principally over a controversial bill that would allow suspects to be extradited from Hong Kong to mainland China , have taken on new demands, including an investigation into police use of rubber bullets, teargas and physical violence against protesters"
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
        "span": "to show black flags to the Prime Minister in his way back to the Ghughra helipad"
      },
      "relation": "caused",
      "effect": {
        "span": "a group of advocates who had gathered at Favvara circle"
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
        "span": "selective eviction of vendors in front of Sambalpur Town police station"
      },
      "relation": "caused",
      "effect": {
        "span": "Hundreds of roadside vendors under the banner of the Sambalpur Utha Dokani Sangha staged a demonstration in front of the office of the DIG ( NR ) on Wednesday in protest against selective eviction of vendors in front of Sambalpur Town police station and demanded their rehabilitation"
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
        "span": "the killing of Swami Laxamananda Saraswati"
      },
      "relation": "caused",
      "effect": {
        "span": "a large scale riot in the area in 2008"
      }
    },
    {
      "cause": {
        "span": "the members of the VHP assembled there to observe the death anniversary of Swami Laxamananda Saraswati"
      },
      "relation": "caused",
      "effect": {
        "span": "The communally sensitive Kandhamal district was today put under high security blanket"
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
        "span": "environmental and health concerns associated with pollution"
      },
      "relation": "caused",
      "effect": {
        "span": "mainlanders have gained awareness in recent years"
      }
    },
    {
      "cause": {
        "span": "polluting projects"
      },
      "relation": "caused",
      "effect": {
        "span": "The massive three-day protest this week was the latest in a series of grass-roots demonstrations"
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
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 1,
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
        "span": "religious extremism"
      },
      "relation": "caused",
      "effect": {
        "span": "trio plotted knife rampage"
      }
    },
    {
      "cause": {
        "span": "Kunming rail station attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Three given death penalty"
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

### --- id=2067 ---

输入文本: On January 23 , Amcu members at Lonmin , Amplats , and Implats downed tools , demanding a monthly basic salary of R12,500 .

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
      "cause": "demanding a monthly basic salary of R12,500",
      "effect": "On January 23 , Amcu members at Lonmin , Amplats , and Implats downed tools"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding a monthly basic salary of R12,500"
      },
      "relation": "caused",
      "effect": {
        "span": "Amcu members at Lonmin , Amplats , and Implats downed tools"
      }
    }
  ]
}
```

### --- id=3063 ---

输入文本: KERALA UDF whitewashing RSS violence : CPI(M) November 15 , 2007 00:00 IST Staff Reporter KANNUR : Communist Party of India ( Marxist ) State secretary Pinarayi Vijayan has accused the United Democratic Front ( UDF ) of whitewashing violence instigated by the Rashtriya Swayamsevak Sangh ( RSS ) in the State .

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
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
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
      "cause": "the decision of the State Government to resume work from early next month",
      "effect": "﻿The meeting discussed strategies to intensify the agitation against the Posco project and counter police action during construction of coastal road"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the decision of the State Government to resume work from early next month"
      },
      "relation": "caused",
      "effect": {
        "span": "strategies to intensify the agitation against the Posco project and counter police action during construction of coastal road"
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
        "span": "a blaze at a warehouse storing hazardous chemicals"
      },
      "relation": "caused",
      "effect": {
        "span": "Wednesday ’ s explosions"
      }
    },
    {
      "cause": {
        "span": "Wednesday ’ s explosions"
      },
      "relation": "caused",
      "effect": {
        "span": "a third day of protests in Tianjin over the government response to Wednesday ’ s explosions"
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
        "span": "the State Government ’ s ban on toddy tapping"
      },
      "relation": "caused",
      "effect": {
        "span": "some protestors drank toddy and certified that it was only a health drink with insignificant alcohol content and not an alcoholic beverage like the brew being sold in the IMFL outlets of the State Government"
      }
    },
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

### --- id=1301 ---

输入文本: Referring to a string of political and military heavyweights toppled by president Xi Jinping ’ s war on corruption , the newspaper added : “ If big cases such as those involving Zhou Yongkang , Xu Caihou , Guo Boxiong and Ling Jihua were thoroughly investigated in an open manner , why should there be cover-up over a safety accident ? ”

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
        "span": "president Xi Jinping ’ s war on corruption"
      },
      "relation": "caused",
      "effect": {
        "span": "a string of political and military heavyweights toppled"
      }
    }
  ]
}
```

### --- id=891 ---

输入文本: Singh said the militants had tried to breach the cordon Tuesday night , " but the troops fired at them , pushing them back into the jungle " .

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
        "span": "the militants had tried to breach the cordon Tuesday night"
      },
      "relation": "caused",
      "effect": {
        "span": "the troops fired at them , pushing them back into the jungle"
      }
    }
  ]
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
        "span": "a booing crowd had refused to let him speak at a rally in Bloemfontein on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "South African President Jacob Zuma was ushered away by minders on Wednesday as he was bombarded by questions about the fiasco on May Day"
      }
    },
    {
      "cause": {
        "span": "a booing crowd had refused to let him speak at a rally in Bloemfontein on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "he was bombarded by questions about the fiasco on May Day"
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

### --- id=68 ---

输入文本: Ishrat Jahan , a 19 - year-old college student was killed along with three others on June 15 , 2004 allegedly by a team of Crime Branch officials on the outskirts of Ahmedabad , after intelligence inputs that a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi to avenge the 2002 communal riots in the state .

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
      "cause": "intelligence inputs that a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi to avenge the 2002 communal riots in the state",
      "effect": "Ishrat Jahan , a 19 - year-old college student was killed along with three others on June 15 , 2004 allegedly by a team of Crime Branch officials on the outskirts of Ahmedabad"
    },
    {
      "cause": "to avenge the 2002 communal riots in the state",
      "effect": "a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the 2002 communal riots in the state"
      },
      "relation": "caused",
      "effect": {
        "span": "a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi"
      }
    },
    {
      "cause": {
        "span": "a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi"
      },
      "relation": "caused",
      "effect": {
        "span": "Ishrat Jahan , a 19 - year-old college student was killed along with three others on June 15 , 2004 allegedly by a team of Crime Branch officials on the outskirts of Ahmedabad"
      }
    }
  ]
}
```

### --- id=123 ---

输入文本: " He alleged that the police did act to prevent such incidents despite the party giving them inputs about the violence beforehand .

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
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
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
        "span": "the violence on Wednesday in which one senior company official was killed"
      },
      "relation": "caused",
      "effect": {
        "span": "its plant was remain closed for the second day"
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
        "span": "the organisation of the pro-Frelimo rallies in 1974 under the banner of the then South African Students Organisation ( SASO )"
      },
      "relation": "caused",
      "effect": {
        "span": "political activism"
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
    }
  ]
}
```

### --- id=3045 ---

输入文本: Muslims across the city of lakes , still haunted by memories of the 2002 Gujarat riots , say they will not vote for someone who was unable to stop a massacre of ‘ innocent people ’ in his state .

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
      "cause": "Muslims across the city of lakes , still haunted by memories of the 2002 Gujarat riots",
      "effect": "they will not vote for someone who was unable to stop a massacre of ‘ innocent people ’ in his state"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
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
        "span": "a planned attack instigated by the PMK"
      }
    },
    {
      "cause": {
        "span": "the PMK-led assault"
      },
      "relation": "caused",
      "effect": {
        "span": "members of a community in 30 villages , spread across political parties , joined the PMK-led assault"
      }
    }
  ]
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
        "span": "the negligence of the staff"
      },
      "relation": "caused",
      "effect": {
        "span": "a 25 -year-old man who died at the Government Chest Hospital in Erragadda"
      }
    },
    {
      "cause": {
        "span": "the negligence of the staff"
      },
      "relation": "caused",
      "effect": {
        "span": "The family of a 25 -year-old man who died at the Government Chest Hospital in Erragadda , allegedly due to the negligence of the staff , protested at the hospital on Tuesday"
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
        "span": "This"
      },
      "relation": "caused",
      "effect": {
        "span": "the owners , who first damaged the speakers of the protesters and then opened fire , injuring six persons"
      }
    },
    {
      "cause": {
        "span": "opened fire"
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
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
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
        "span": "claimed one life on Thursday"
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
        "span": "The members voiced concern over the absence of a breakthrough in earlier incidents of blasts in Punjab and emphasised that the culprits should be brought to book with an iron fist"
      }
    }
  ]
}
```

### --- id=805 ---

输入文本: Tens of thousands of pro-democracy protesters have marched across Hong Kong to mark the 20th anniversary of its return to Chinese control with a high-profile show of dissent .

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
      "cause": "to mark the 20th anniversary of its return to Chinese control with a high-profile show of dissent",
      "effect": "Tens of thousands of pro-democracy protesters have marched across Hong Kong"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to mark the 20th anniversary of its return to Chinese control"
      },
      "relation": "caused",
      "effect": {
        "span": "Tens of thousands of pro-democracy protesters have marched across Hong Kong with a high-profile show of dissent"
      }
    }
  ]
}
```

### --- id=1496 ---

输入文本: `` We would like to put it on record that this is the same substation where our staff members were chased away by the community earlier because of the protest action that happened today in Tshwane , '' Eskom said in a statement .

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
      "cause": "the protest action that happened today in Tshwane",
      "effect": "our staff members were chased away by the community earlier"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the protest action that happened today in Tshwane"
      },
      "relation": "caused",
      "effect": {
        "span": "our staff members were chased away by the community"
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
        "span": "the Ernakulam Central Police on Tuesday arrested the Ernakulam Law College student who allegedly ran naked through MG road"
      }
    }
  ]
}
```

### --- id=2154 ---

输入文本: Sagar denied that there was a fight between Tyagi and Prasad and added that the leprosy patients assaulted him when he went there to deliver the transfer orders .

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
      "cause": "he went there to deliver the transfer orders",
      "effect": "the leprosy patients assaulted him"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to deliver the transfer orders"
      },
      "relation": "caused",
      "effect": {
        "span": "the leprosy patients assaulted him"
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

### --- id=986 ---

输入文本: KOLLAM : Neglect of Kollam alleged August 06 , 2011 00:00 IST UDF government has declared war on people : Chandrappan The district unit of the Left Democratic Front ( LDF ) staged a dharna at the Press Club Maidan here on Friday to register its protest against the alleged neglect of the district in the revised Budget presented by Finance Minister K.M. Mani .

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
      "cause": "to register its protest against the alleged neglect of the district in the revised Budget presented by Finance Minister K.M. Mani",
      "effect": "The district unit of the Left Democratic Front ( LDF ) staged a dharna at the Press Club Maidan here on Friday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the alleged neglect of the district in the revised Budget presented by Finance Minister K.M. Mani"
      },
      "relation": "caused",
      "effect": {
        "span": "The district unit of the Left Democratic Front ( LDF ) staged a dharna at the Press Club Maidan here on Friday to register its protest against the alleged neglect of the district in the revised Budget presented by Finance Minister K.M. Mani"
      }
    }
  ]
}
```

### --- id=3057 ---

输入文本: The activists of Jaya Karnataka Sanghatane and Manava Hakkugala Horatagarara Parishat also staged separate protests at the Deputy Commissioner ’ s office demanding the State government hand over the probe to the Central Bureau of Investigation .

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
      "cause": "demanding the State government hand over the probe to the Central Bureau of Investigation",
      "effect": "The activists of Jaya Karnataka Sanghatane and Manava Hakkugala Horatagarara Parishat also staged separate protests at the Deputy Commissioner ’ s office"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to demand the State government hand over the probe to the Central Bureau of Investigation"
      },
      "relation": "caused",
      "effect": {
        "span": "staged separate protests at the Deputy Commissioner ’ s office"
      }
    }
  ]
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
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
  "pred_triples": [],
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
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

### --- id=1111 ---

输入文本: " We condemn the bomb blasts in Lord Buddha 's holy land .

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
        "span": "the bomb blasts in Lord Buddha 's holy land"
      },
      "relation": "caused",
      "effect": {
        "span": "We condemn the bomb blasts in Lord Buddha 's holy land"
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
        "span": "hundreds of police"
      },
      "relation": "caused",
      "effect": {
        "span": "thousands of residents of surrounding villages gathered to mourn but were stopped by hundreds of police"
      }
    }
  ]
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
        "span": "They were arrested and taken to the respective police stations "
      }
    }
  ]
}
```

### --- id=2798 ---

输入文本: The posters have warned them against joining the police and army and threatened to take up such cases in the praja court .

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
        "span": "against joining the police and army"
      },
      "relation": "caused",
      "effect": {
        "span": "The posters have warned them"
      }
    },
    {
      "cause": {
        "span": "against joining the police and army"
      },
      "relation": "caused",
      "effect": {
        "span": "threatened to take up such cases in the praja court"
      }
    }
  ]
}
```

### --- id=2156 ---

输入文本: Within seconds he had been thrown to the ground by the “ revolutionary masses ” , and thus he began a wretched phase in life , denounced and beaten at every turn .

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
      "cause": "Within seconds he had been thrown to the ground by the “ revolutionary masses ”",
      "effect": "he began a wretched phase in life , denounced and beaten at every turn"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he had been thrown to the ground by the “ revolutionary masses ”"
      },
      "relation": "caused",
      "effect": {
        "span": "he began a wretched phase in life , denounced and beaten at every turn"
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
        "span": "the killing"
      },
      "relation": "caused",
      "effect": {
        "span": "criticised the Odisha govenrment for not arresting all those involved in the killing"
      }
    }
  ]
}
```

### --- id=1617 ---

输入文本: April 4 , 2010 : Maoists detonate powerful landmine and blow up police bus in Koraput district , Orissa , killing around 10 Special Operations Group personnel and injuring 16 .

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
      "cause": "Maoists detonate powerful landmine and blow up police bus in Koraput district , Orissa",
      "effect": "killing around 10 Special Operations Group personnel and injuring 16"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Maoists detonate powerful landmine and blow up police bus in Koraput district, Orissa"
      },
      "relation": "caused",
      "effect": {
        "span": "killing around 10 Special Operations Group personnel and injuring 16"
      }
    }
  ]
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
        "span": "Louise Khurshid 's vehicle hit him"
      },
      "relation": "caused",
      "effect": {
        "span": "causing injuries"
      }
    },
    {
      "cause": {
        "span": "Congress district president Prakash Pradhan and his party workers assaulted him"
      },
      "relation": "caused",
      "effect": {
        "span": "lodged a complaint"
      }
    }
  ]
}
```

### --- id=1662 ---

输入文本: More than 50 people were reportedly taken to hospital for treatment after various protests throughout the day .

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
        "span": "various protests throughout the day"
      },
      "relation": "caused",
      "effect": {
        "span": "More than 50 people were reportedly taken to hospital for treatment"
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
      "cause": "his party was routed in the Lok Sabha polls",
      "effect": "Lalu Prasad lost his place in the Congress-led United Progressive Alliance central government last year"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "his party was routed in the Lok Sabha polls"
      },
      "relation": "caused",
      "effect": {
        "span": "Lalu Prasad lost his place in the Congress-led United Progressive Alliance central government last year"
      }
    },
    {
      "cause": {
        "span": "their ouster from power in 2005 in Bihar"
      },
      "relation": "caused",
      "effect": {
        "span": "Lalu-Rabri for the first time made a political mark by a near total shutdown"
      }
    }
  ]
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
        "span": "the negotiations were carried out by top officials of the airline and the UB Group"
      },
      "relation": "caused",
      "effect": {
        "span": "leading employees to demand his presence"
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
        "span": "the lack of women ’ s safety"
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

### --- id=254 ---

输入文本: This was the third panchayat office building blown up by the Maoists in the Kalimela area in the last 45 days .

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
        "span": "the Maoists"
      },
      "relation": "caused",
      "effect": {
        "span": "This was the third panchayat office building blown up by the Maoists in the Kalimela area in the last 45 days"
      }
    }
  ]
}
```

### --- id=2030 ---

输入文本: Abhishek Banerjee , nephew of the chief minister had said : " The Mamata Banerjee government , by killing him , has proved that in days to come , people will have the final word . " Communist Party of India-Maoist leader Koteswar Rao alias Kishenji was killed on November 24 , 2011 in a gun battle in West Midnapore district near the Bengal-Jharkhand border .

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
        "span": "by killing him"
      },
      "relation": "caused",
      "effect": {
        "span": "The Mamata Banerjee government , by killing him , has proved that in days to come , people will have the final word"
      }
    },
    {
      "cause": {
        "span": "a gun battle in West Midnapore district near the Bengal-Jharkhand border"
      },
      "relation": "caused",
      "effect": {
        "span": "Communist Party of India-Maoist leader Koteswar Rao alias Kishenji was killed on November 24 , 2011"
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
      "cause": "stone throwing had operated from the Palakkad depot on Friday , while five operated on Saturday",
      "effect": "These services were affected in the last two days"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "stone throwing"
      },
      "relation": "caused",
      "effect": {
        "span": "These services were affected in the last two days"
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
        "span": "Jimmy Mohlala , who was shot dead in January 2009"
      }
    }
  ]
}
```

### --- id=2065 ---

输入文本: The end to the platinum strike has brought a stop to the hardships that South Africa has suffered in the last few months , Lonmin CEO Ben Magara said on Tuesday .

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
      "cause": "The end to the platinum strike",
      "effect": "brought a stop to the hardships that South Africa has suffered in the last few months"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The end to the platinum strike"
      },
      "relation": "caused",
      "effect": {
        "span": "a stop to the hardships that South Africa has suffered in the last few months"
      }
    }
  ]
}
```

### --- id=2238 ---

输入文本: Municipal Commissioner Md. Abdul Azeem urged the employees to suspended their protest , and attend to their duties .

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
        "span": "to suspended their protest , and attend to their duties"
      },
      "relation": "caused",
      "effect": {
        "span": "Municipal Commissioner Md. Abdul Azeem urged the employees"
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
        "span": "the insensitive and indifferent attitude of the Government to the genuine demands of the pourakarmikas"
      },
      "relation": "caused",
      "effect": {
        "span": "hundreds of people , including many women , led by Sri Mahanta Shivacharyaru of the Sulpul Math , Sri Rajashekar Shivacharyaru , Guru Mahanta Shivacharyaru of the Hiremath at Pala , Shivanda Swamigalu of Sonna Dasoha Math , Gangadhar Swamigalu of Chowdapur Math , Kanchi Basava Shivacharyaru of Roza Math , battery of Congress leaders including DCC president Allamprabhu Patil , MLC , the former Mayor Chandrika Parameshwar , zilla panchayat member Ambaraya Ashtagi , the former president of the HKCCI Umakant Nigudgi , Karnataka Rakshana Vedike president Arunkumar Patil , Hyderabad Karnataka Janapara Sangarsh Samiti Laxman Dasti and others marched from the Super Market to the Deputy Commissioner 's office to register their protest against the insensitive and indifferent attitude of the Government to the genuine demands of the pourakarmikas"
      }
    }
  ]
}
```

### --- id=2937 ---

输入文本: South African truck drivers have embarked on a nationwide strike in protest at foreign drivers allegedly taking away their jobs .

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
      "cause": "in protest at foreign drivers allegedly taking away their jobs",
      "effect": "South African truck drivers have embarked on a nationwide strike"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "foreign drivers allegedly taking away their jobs"
      },
      "relation": "caused",
      "effect": {
        "span": "South African truck drivers have embarked on a nationwide strike in protest"
      }
    }
  ]
}
```

### --- id=970 ---

输入文本: This was Thackeray 's first and keenly watched public rally after his Aurangabad rally last Tuesday when his convoy was attacked allegedly by NCP workers .

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
        "span": "NCP workers"
      },
      "relation": "caused",
      "effect": {
        "span": "his convoy was attacked allegedly by NCP workers"
      }
    }
  ]
}
```

### --- id=2750 ---

输入文本: Kejriwals team attacked by Congress workers - Indian Express Express News Service , Express News Service : Lucknow , Thu Dec 13 2012 , 04:52 hrs A group of Congress workers allegedly attacked members of Arvind Kejriwal-led Aam Aadmi Party who were staging demonstration on the arrival of External Affairs Minister Salman Khurshid 's wife Louise Khurshid at an event in Mainpuri district on Wednesday .

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
        "span": "staging demonstration on the arrival of External Affairs Minister Salman Khurshid 's wife Louise Khurshid at an event in Mainpuri district on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "A group of Congress workers allegedly attacked members of Arvind Kejriwal-led Aam Aadmi Party"
      }
    }
  ]
}
```

### --- id=2848 ---

输入文本: Pakistan PM offers prayers at Ajmer dargah amid protests 09th March 2013 12:39 PM Pakistan Prime Minister Raja Parvez Ashraf today offered prayers at the historic dargah of Khwaja Moinuddin Chishti during his private visit here that was marked by protests .

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
      "cause": "protests",
      "relation": "caused",
      "effect": "his private visit here that was marked by protests"
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
        "span": "its revised Budget"
      },
      "relation": "caused",
      "effect": {
        "span": "the United Democratic Front ( UDF ) government seemed to have declared a war on the people"
      }
    }
  ]
}
```

### --- id=1554 ---

输入文本: Though he escaped the impact of the bombs , the gang chased and hacked him to death in full view of the public .

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
        "span": "the gang chased and hacked him to death in full view of the public"
      },
      "relation": "caused",
      "effect": {
        "span": "he escaped the impact of the bombs"
      }
    }
  ]
}
```

### --- id=1852 ---

输入文本: Medical services have been crippled as the junior doctors have resorted to cease-work agitation demanding removal of the college Dean as well as head of the Medicine Department along with arrest of the journalist , against whom they had lodged a complaint .

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
      "cause": "the junior doctors have resorted to cease-work agitation",
      "effect": "Medical services have been crippled"
    },
    {
      "cause": "demanding removal of the college Dean as well as head of the Medicine Department along with arrest of the journalist",
      "effect": "the junior doctors have resorted to cease-work agitation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the junior doctors have resorted to cease-work agitation demanding removal of the college Dean as well as head of the Medicine Department along with arrest of the journalist , against whom they had lodged a complaint"
      },
      "relation": "caused",
      "effect": {
        "span": "Medical services have been crippled"
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
      "cause": "the ambush in Manipur",
      "effect": "Naga insurgent outfit NSCN ( Khaplang ) , with which the Centre abrogated ceasefire in March , has claimed responsibility"
    },
    {
      "cause": "the ambush in Manipur",
      "effect": "18 army personnel were killed and 10 others injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the ambush in Manipur"
      },
      "relation": "caused",
      "effect": {
        "span": "18 army personnel were killed and 10 others injured"
      }
    }
  ]
}
```

### --- id=900 ---

输入文本: Dehradun : Mining will hit agriculturally-rich Tehri region , say villagers August 24 , 2014 00:00 IST More than 500 villagers on Saturday protested against the stone crushers who have been licensed to mine the agriculturally-rich region of Tehri district ’ s Maletha gram sabha .

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
      "cause": "who have been licensed to mine the agriculturally-rich region of Tehri district ’ s Maletha gram sabha",
      "effect": "More than 500 villagers on Saturday protested against the stone crushers"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
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
        "span": "two people were killed , allegedly by police"
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
    },
    {
      "cause": {
        "span": "some radio cab operators did not participate in the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "they made brisk business"
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
        "span": "the death of Shameel Ahmed"
      },
      "relation": "caused",
      "effect": {
        "span": "the deadly attack on police personnel in Ambur Town on Saturday night which left 38 police personnel , including women , and a couple of civilians injured"
      }
    },
    {
      "cause": {
        "span": "the deadly attack on police personnel in Ambur Town on Saturday night which left 38 police personnel , including women , and a couple of civilians injured"
      },
      "relation": "caused",
      "effect": {
        "span": "As many as 95 youth have been arrested"
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
        "span": "Congress and other BJP members rushed into the Well shouting slogans"
      }
    }
  ]
}
```

### --- id=117 ---

输入文本: Another Congress worker , Repon Sheikh , was killed at Bharatpur in the same district during a clash between rival party supporters , the police said .

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
      "cause": "a clash between rival party supporters",
      "effect": "Another Congress worker , Repon Sheikh , was killed at Bharatpur in the same district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a clash between rival party supporters"
      },
      "relation": "caused",
      "effect": {
        "span": "Repon Sheikh , was killed at Bharatpur in the same district during a clash between rival party supporters"
      }
    }
  ]
}
```

### --- id=939 ---

输入文本: BSP stir against fuel hike

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
      "cause": "against fuel hike",
      "effect": "BSP stir"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "fuel hike"
      },
      "relation": "caused",
      "effect": {
        "span": "BSP stir"
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
      "cause": "in support to farmers",
      "effect": "Telangana Rashtra Samithi ( TRS ) to participate in protests"
    }
  ],
  "pred_triples": []
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
        "span": "the security of students from the north-east"
      },
      "relation": "caused",
      "effect": {
        "span": "protests across New Delhi"
      }
    }
  ]
}
```

### --- id=164 ---

输入文本: Seven Maoists Killed in Gun Battle 18th February 2014 11:36 AM Seven Maoists were killed in a two-hour long gun battle with Maharashtra Police on the border the state shares with Chhattisgarh , a top official said Tuesday .

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
      "cause": "in a two-hour long gun battle with Maharashtra Police on the border the state shares with Chhattisgarh",
      "effect": "Seven Maoists were killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a two-hour long gun battle with Maharashtra Police on the border the state shares with Chhattisgarh"
      },
      "relation": "caused",
      "effect": {
        "span": "Seven Maoists were killed"
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
        "span": "sectarian clashes in which four persons were injured"
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
        "span": "total response in Bihar , upsetting Lalu-Rabri rival Nitish Kumar as well as the Bharatiya Janata Party ( BJP ) and the Congress , which is trying for a revival in the state"
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
        "span": "collecting high rates from students and patients"
      },
      "relation": "caused",
      "effect": {
        "span": "Parking contract has been given to some goons"
      }
    },
    {
      "cause": {
        "span": "Parking contract has been given to some goons who were collecting high rates from students and patients"
      },
      "relation": "caused",
      "effect": {
        "span": "warned of intensifying the agitation"
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
        "span": "the remarks they made during Anna Hazare ’ s one-day fast at Jantar Mantar on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "strongly condemned them for “ lowering the dignity of the House ”"
      }
    }
  ]
}
```

### --- id=2044 ---

输入文本: The party workers were also involved in a similar incident last Sunday when they manhandled a news channel cameraman while shooting the fighting of a few Congress workers outside the District Congress Committee office .

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
        "span": "shooting the fighting of a few Congress workers outside the District Congress Committee office"
      },
      "relation": "caused",
      "effect": {
        "span": "manhandled a news channel cameraman"
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
      "cause": "to protest against the proposed law allowing for the extradition of individuals for trial in mainland China , where the opaque court system is controlled by the Communist party",
      "relation": "caused",
      "effect": "Millions have taken to the streets"
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
        "span": "fighting for their cause"
      },
      "relation": "caused",
      "effect": {
        "span": "Prasadam was done to death by forces backed by the government"
      }
    },
    {
      "cause": {
        "span": "false cases"
      },
      "relation": "caused",
      "effect": {
        "span": "Several tribals were also put in jail by police"
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
      "cause": "they want answers",
      "effect": "About 200 members of the Treatment Action Campaign ( TAC ) protested outside the hospital and like the families"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they want answers"
      },
      "relation": "caused",
      "effect": {
        "span": "protested outside the hospital"
      }
    }
  ]
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

### --- id=2489 ---

输入文本: On Monday , the agitating lawyers wanted to meet the District Magistrate but in his absence met Additional District Magistrate Udhab Charan Majhi and Sub-Collector Madhusudan Das who asked them to call off the strike .

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
        "span": "the agitating lawyers wanted to meet the District Magistrate"
      },
      "relation": "caused",
      "effect": {
        "span": "met Additional District Magistrate Udhab Charan Majhi and Sub-Collector Madhusudan Das who asked them to call off the strike"
      }
    },
    {
      "cause": {
        "span": "who asked them to call off the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "the agitating lawyers wanted to meet the District Magistrate"
      }
    }
  ]
}
```

### --- id=533 ---

输入文本: Kishore Chandra Deo splits Cong , says Salwa Judum was a ' sinful strategy ' - Indian Express Press Trust Of India , Press Trust Of India : New Delhi , Thu May 30 2013 , 22:07 hrs Activists of Youth Indian National Trade Union Congress ( INTUC ) protest against recent Naxal attack on Congress leaders , in Raipur on Thursday .

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
      "cause": "against recent Naxal attack on Congress leaders",
      "effect": "Activists of Youth Indian National Trade Union Congress ( INTUC ) protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "recent Naxal attack on Congress leaders"
      },
      "relation": "caused",
      "effect": {
        "span": "Activists of Youth Indian National Trade Union Congress ( INTUC ) protest against recent Naxal attack on Congress leaders, in Raipur on Thursday"
      }
    }
  ]
}
```

### --- id=54 ---

输入文本: On media reports that the night vision device used by three terrorists in the Gurdaspur attack had US markings , Biswal said the US is in conversation with Indian authorities to try to ascertain and trace the origins of the equipment found .

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
      "cause": "to try to ascertain and trace the origins of the equipment found",
      "effect": "the US is in conversation with Indian authorities"
    }
  ],
  "pred_triples": []
}
```

### --- id=1996 ---

输入文本: Many Hong Kongers also cite the jailing of leaders and activists from the 2014 Occupy Central movement – a 79-day mass civil disobedience movement – as well as the disqualification of young localist lawmakers as signs of the erosion of civil freedoms .

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
      "cause": "the erosion of civil freedoms",
      "effect": "the jailing of leaders and activists from the 2014 Occupy Central movement – a 79-day mass civil disobedience movement – as well as the disqualification of young localist lawmakers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the jailing of leaders and activists from the 2014 Occupy Central movement – a 79-day mass civil disobedience movement – as well as the disqualification of young localist lawmakers"
      },
      "relation": "caused",
      "effect": {
        "span": "the erosion of civil freedoms "
      }
    }
  ]
}
```

### --- id=247 ---

输入文本: He was inaugurating the dharna held in front of the Secretariat , ahead of the general strike called for February 28 , demanding to reject the PFRDA Bill .

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
      "cause": "demanding to reject the PFRDA Bill",
      "effect": "He was inaugurating the dharna held in front of the Secretariat , ahead of the general strike called for February 28"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to reject the PFRDA Bill"
      },
      "relation": "caused",
      "effect": {
        "span": "He was inaugurating the dharna held in front of the Secretariat , ahead of the general strike called for February 28 , demanding to reject the PFRDA Bill"
      }
    }
  ]
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
        "span": "the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "employees who were given the sack"
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
        "span": "to Revoke ban"
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
      "cause": "IFP hotheads at the township entrance tried again to barricade the road",
      "effect": "were removed by the police"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "tried again to barricade the road"
      },
      "relation": "caused",
      "effect": {
        "span": "were removed by the police"
      }
    }
  ]
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
        "span": "as part of her election campaign in the city on Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "Mamata Banerjee organised a huge padayatra"
      }
    },
    {
      "cause": {
        "span": "as part of her election campaign in the city on Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "sending a message to the CPM leadership about the possible change in the state administration"
      }
    }
  ]
}
```

### --- id=2812 ---

输入文本: Yadav also alleged that Pradhan beat him when he was raising slogansin front of Khurshid 's vehicle .

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
        "span": "raising slogansin front of Khurshid 's vehicle"
      },
      "relation": "caused",
      "effect": {
        "span": "Pradhan beat him"
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
        "span": "the transfer of superintendent of police Umesh Chandra"
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
        "span": "further eroding the image of the police which touched an all-time low"
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

### --- id=778 ---

输入文本: Taking strong exception to the inordinate delay in release of the promised compensation for crop loss in the August 2005 floods , nearly 50 farmers , led by the Telugu Desam Party MPTC member Gurumurthy and local CPI - ( M ) leaders Krishna Babu and Kondala Babu , squatted before the MRO .

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
      "cause": "Taking strong exception to the inordinate delay in release of the promised compensation for crop loss in the August 2005 floods",
      "effect": "nearly 50 farmers , led by the Telugu Desam Party MPTC member Gurumurthy and local CPI - ( M ) leaders Krishna Babu and Kondala Babu , squatted before the MRO"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the inordinate delay in release of the promised compensation for crop loss in the August 2005 floods"
      },
      "relation": "caused",
      "effect": {
        "span": "nearly 50 farmers , led by the Telugu Desam Party MPTC member Gurumurthy and local CPI - ( M ) leaders Krishna Babu and Kondala Babu , squatted before the MRO"
      }
    }
  ]
}
```

### --- id=1265 ---

输入文本: The posters , allegedly put up by the CPI ( Maoist ) , have called on the people to join the Maoist group .

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
        "span": "The posters , allegedly put up by the CPI ( Maoist )"
      },
      "relation": "caused",
      "effect": {
        "span": "have called on the people to join the Maoist group"
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
        "span": "has forever tainted the image of Dharmapuri district as a former Naxal stronghold that , even a decade ago , had no place for caste or class differences"
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
        "span": "Nine security personnel , including CRPF troopers , ambushed by Maoists during a routine patrol in Saranda jungles in Jharkhand"
      }
    }
  ]
}
```

### --- id=435 ---

输入文本: Students and teachers of physical education relaunched their protest against the appointment of general teachers for physical education work in schools .

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
      "cause": "against the appointment of general teachers for physical education work in schools",
      "effect": "Students and teachers of physical education relaunched their protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the appointment of general teachers for physical education work in schools"
      },
      "relation": "caused",
      "effect": {
        "span": "Students and teachers of physical education relaunched their protest against the appointment of general teachers for physical education work in schools"
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
      "cause": "Tuesday 's rioting at Bhagwati Hospital, where a BJP leader, injured in a shootout, had succumbed to his injuries",
      "relation": "caused",
      "effect": "private hospitals from Jogeshwari to Dahisar decided to down shutters for a day"
    },
    {
      "cause": "Tuesday 's rioting at Bhagwati Hospital, where a BJP leader, injured in a shootout, had succumbed to his injuries",
      "relation": "caused",
      "effect": "doctors closed ranks to protest"
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
        "span": "a minor scuffle ensued"
      }
    }
  ]
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
        "span": "‘ elements in Pakistan ’ were responsible for last week ’ s terrorist outrage in Mumbai "
      },
      "relation": "caused",
      "effect": {
        "span": "Prime Minister Manmohan Singh is finding himself under tremendous pressure to respond decisively to initial evidence"
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
        "span": "the cases registered against the Christians in connection with church attacks"
      },
      "relation": "caused",
      "effect": {
        "span": "He urged the government to drop the cases"
      }
    }
  ]
}
```

### --- id=989 ---

输入文本: Inspector General of BSF Jammu Frontier Rajeev Krishna had said that its personnel opened fire in self-defence with " maximum restraint " to quell the violence by the mob which tried to storm their storehouse of arms and ammunition .

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
      "cause": "to quell the violence by the mob which tried to storm their storehouse of arms and ammunition",
      "effect": "its personnel opened fire in self-defence with \" maximum restraint \""
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the violence by the mob which tried to storm their storehouse of arms and ammunition"
      },
      "relation": "caused",
      "effect": {
        "span": "its personnel opened fire in self-defence with \" maximum restraint \" to quell the violence by the mob which tried to storm their storehouse of arms and ammunition"
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

### --- id=705 ---

输入文本: The performance comes at a time when instruction of the city ’ s history is becoming increasingly politicised , with recent government attempts to bury details that may be embarrassing for China .

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
        "span": "recent government attempts to bury details that may be embarrassing for China"
      },
      "relation": "caused",
      "effect": {
        "span": "instruction of the city ’ s history is becoming increasingly politicised"
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
      "cause": "a prominent human rights lawyer who helped organise the 1989 demonstration ; three days prior , he had participated in a private panel discussion commemorating the massacre",
      "effect": "In the early hours of 6 May , Beijing police detained Pu Zhiqiang"
    }
  ],
  "pred_triples": []
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
        "span": "The riots"
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
      "cause": "symbolically signifying betrayal",
      "relation": "caused",
      "effect": "the PMK held an unusual form of protest with members sporting a \" patta naamam \" ( holy ash spread across their foreheads )"
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
        "span": "the arrests of their activists"
      },
      "relation": "caused",
      "effect": {
        "span": "TRS students ' wing activists staged dharna in front of Karimnagar One Town police flaying the arrests of their activists and obstructing them from proceeding to Hyderabad"
      }
    }
  ]
}
```

### --- id=2760 ---

输入文本: Speaking to reporters here today , Inspector General of Police and the State Police official spokesperson AR Anuradha said that the police showed utmost restraint despite the provocation of anti-social elements involved in the incident .

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
        "span": "the provocation of anti-social elements involved in the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "the police showed utmost restraint"
      }
    }
  ]
}
```

### --- id=1273 ---

输入文本: Dewan told Newsline that the " protest will now continue at ward level and from next week onwards every ward will be sensitised against property tax and high charges of regularisation impsed by government " .

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
        "span": "high charges of regularisation impsed by government"
      },
      "relation": "caused",
      "effect": {
        "span": "protest will now continue at ward level and from next week onwards every ward will be sensitised against property tax and high charges of regularisation impsed by government"
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
        "span": "to ensure that it is scrapped altogether"
      },
      "relation": "caused",
      "effect": {
        "span": "opposition parties today said their fight will go on"
      }
    },
    {
      "cause": {
        "span": "Taking its protest against FDI to the streets"
      },
      "relation": "caused",
      "effect": {
        "span": "opposition parties today said their fight will go on"
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

### --- id=493 ---

输入文本: This attack comes two weeks after Nwabisa Ngcukana , 25 , was undressed assaulted by taxi drivers and hawkers because she was wearing a mini-skirt at the Noord Street taxi rank in Johannesburg .

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
      "cause": "she was wearing a mini-skirt at the Noord Street taxi rank in Johannesburg",
      "effect": "Nwabisa Ngcukana , 25 , was undressed assaulted by taxi drivers and hawkers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "she was wearing a mini-skirt"
      },
      "relation": "caused",
      "effect": {
        "span": "Nwabisa Ngcukana , 25 , was undressed assaulted by taxi drivers and hawkers"
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
        "span": "actions around the Copenhagen talks are being organised by Climate Satyagraha Camp"
      }
    }
  ]
}
```

### --- id=1790 ---

输入文本: Tshukudu was allegedly shot dead by Jaco du Plooy , 46 , on October 10 while he was diverting traffic on the R52 leading to Sannieshof to avoid protests further down the road .

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
      "cause": "to avoid protests further down the road",
      "effect": "he was diverting traffic on the R52 leading to Sannieshof"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he was diverting traffic on the R52 leading to Sannieshof to avoid protests further down the road"
      },
      "relation": "caused",
      "effect": {
        "span": "Tshukudu was allegedly shot dead by Jaco du Plooy , 46 , on October 10"
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

### --- id=246 ---

输入文本: Spokesman Keith Khoza said they had decided to March to Prime Media because the cartoon had raised various concerns .

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
      "cause": "the cartoon had raised various concerns",
      "effect": "they had decided to March to Prime Media"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the cartoon had raised various concerns"
      },
      "relation": "caused",
      "effect": {
        "span": "decided to March to Prime Media"
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

### --- id=337 ---

输入文本: ‘ ’ They did nothing when the staff were brutally attacked by anti-social elements and police officials , ’ ’ said Jose Jacob , general secretary of the KSRTEA .

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
        "span": "anti-social elements and police officials"
      },
      "relation": "caused",
      "effect": {
        "span": "the staff were brutally attacked"
      }
    }
  ]
}
```

### --- id=2114 ---

输入文本: KARNATAKA People want road developed January 18 , 2007 00:00 IST Correspondent KARWAR : People of Devbag , near here , staged a demonstration on Tuesday to protest against the move of the zilla panchayat to inaugurate a newly built bridge across the Mavinahole stream without developing the road connecting the bridge on either side .

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
      "cause": "to protest against the move of the zilla panchayat to inaugurate a newly built bridge across the Mavinahole stream without developing the road connecting the bridge on either side",
      "effect": "People of Devbag , near here , staged a demonstration on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the move of the zilla panchayat to inaugurate a newly built bridge across the Mavinahole stream without developing the road connecting the bridge on either side"
      },
      "relation": "caused",
      "effect": {
        "span": "People of Devbag , near here , staged a demonstration on Tuesday to protest against the move of the zilla panchayat to inaugurate a newly built bridge across the Mavinahole stream without developing the road connecting the bridge on either side"
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
        "span": "junior doctors ’ strike"
      },
      "relation": "caused",
      "effect": {
        "span": "has affected hundreds of patients"
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
      "cause": "against parallel trading in the New Territories and Tsim Sha Tsui",
      "effect": "there have been protests organised"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the abuse perpetrated by radical protest groups"
      },
      "relation": "caused",
      "effect": {
        "span": "Susan Chan denounces the abuse perpetrated by radical protest groups"
      }
    },
    {
      "cause": {
        "span": "parallel trading in the New Territories and Tsim Sha Tsui"
      },
      "relation": "caused",
      "effect": {
        "span": "protests organised against parallel trading in the New Territories and Tsim Sha Tsui"
      }
    }
  ]
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
        "span": "the attack at a Kunming rail station that killed 31 people and injured 141 in March"
      },
      "relation": "caused",
      "effect": {
        "span": "Three people were sentenced to death by a Yunnan court for their role in the attack at a Kunming rail station that killed 31 people and injured 141 in March"
      }
    }
  ]
}
```

### --- id=5 ---

输入文本: Footage of the attack , which included a pregnant woman being hit , protesters being punched and kneed , and commuters screaming and crying while trying to shield themselves , emerged on Sunday night , fuelling further political unrest as demonstrators , opposition lawmakers and others demanded answers from authorities for failing to stop the violence .

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
      "cause": "Footage of the attack , which included a pregnant woman being hit , protesters being punched and kneed , and commuters screaming and crying while trying to shield themselves , emerged on Sunday night",
      "effect": "fuelling further political unrest"
    },
    {
      "cause": "failing to stop the violence",
      "effect": "demonstrators , opposition lawmakers and others demanded answers from authorities"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "no_json_object",
  "generation_error_message": "未找到 JSON 对象"
}
```

### --- id=1407 ---

输入文本: At a meeting with the striking unions , Karunanidhi cited the increase in daily wages by Rs .40 , washing allowance by Rs .15 to Rs .25 and 8.33 percent bonus plus Rs .500 special payment while asking them to return to work .

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
        "span": "the increase in daily wages by Rs .40 , washing allowance by Rs .15 to Rs .25 and 8.33 percent bonus plus Rs .500 special payment"
      },
      "relation": "caused",
      "effect": {
        "span": "Karunanidhi cited the increase in daily wages by Rs .40 , washing allowance by Rs .15 to Rs .25 and 8.33 percent bonus plus Rs .500 special payment while asking them to return to work"
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
        "span": "the ' not in my backyard ' mentality"
      },
      "relation": "caused",
      "effect": {
        "span": "sparked similar protests in several mainland cities , including Dalian , Guangzhou and Shantou"
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
      "cause": "to support their demand of bringing in the proposed Gujarat Control of Organised Crime ( GUJCOC ) Act",
      "effect": "The four doctors had , as a part of the BJP protest , enacted a mock surgery of his skull near the Income Tax circle on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to support their demand of bringing in the proposed Gujarat Control of Organised Crime ( GUJCOC ) Act"
      },
      "relation": "caused",
      "effect": {
        "span": "enacted a mock surgery of his skull near the Income Tax circle on Tuesday"
      }
    },
    {
      "cause": {
        "span": "as a part of the BJP protest"
      },
      "relation": "caused",
      "effect": {
        "span": "enacted a mock surgery of his skull near the Income Tax circle on Tuesday"
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
      "cause": "Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday to address them",
      "effect": "A crowd of supporters erupted"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to address them"
      },
      "relation": "caused",
      "effect": {
        "span": "A crowd of supporters erupted as Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday"
      }
    }
  ]
}
```

### --- id=359 ---

输入文本: The students at the university of the North West had been protesting against a proposed increase in tuition fees and the merger of higher education institutions .

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
      "cause": "against a proposed increase in tuition fees and the merger of higher education institutions",
      "effect": "The students at the university of the North West had been protesting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a proposed increase in tuition fees and the merger of higher education institutions"
      },
      "relation": "caused",
      "effect": {
        "span": "The students at the university of the North West had been protesting against a proposed increase in tuition fees and the merger of higher education institutions"
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

### --- id=1773 ---

输入文本: Another minister and legislator from Gadwal , DK Aruna , whose father C Narsi Reddy ( the then Congress MLA ) was brutally killed by Maoists in Mahaboobnagar district , is also playing a key rule lobbying with the Congress high command for formation of Telangana State .

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
        "span": "Maoists in Mahaboobnagar district"
      },
      "relation": "caused",
      "effect": {
        "span": "C Narsi Reddy ( the then Congress MLA ) was brutally killed"
      }
    }
  ]
}
```

### --- id=2953 ---

输入文本: It had said that Shahzad , along with Junaid , had jumped off the balcony and fled after firing at the police team during the September 19 , 2008 encounter .

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
        "span": "firing at the police team during the September 19 , 2008 encounter"
      },
      "relation": "caused",
      "effect": {
        "span": "Shahzad , along with Junaid , had jumped off the balcony and fled"
      }
    }
  ]
}
```

### --- id=140 ---

输入文本: Protesters distributed protective gear such as face masks , in the event of clashes with police , who have used teargas on demonstrators .

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
        "span": "police, who have used teargas on demonstrators"
      },
      "relation": "caused",
      "effect": {
        "span": "Protesters distributed protective gear such as face masks , in the event of clashes with police"
      }
    }
  ]
}
```

### --- id=1720 ---

输入文本: The wife of the house owner , Taja , died in the shootout between the militants and the police .

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
      "cause": "in the shootout between the militants and the police",
      "effect": "The wife of the house owner , Taja , died"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the shootout between the militants and the police"
      },
      "relation": "caused",
      "effect": {
        "span": "Taja , died"
      }
    }
  ]
}
```

### --- id=2621 ---

输入文本: He claimed that YSR Congress activists " manhandled " TDP activists at A. Konduru and Khambhampadu villages in which about 10 workers were injured .

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
      "cause": "YSR Congress activists \" manhandled \" TDP activists at A. Konduru and Khambhampadu villages",
      "effect": "about 10 workers were injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "manhandled \" TDP activists at A. Konduru and Khambhampadu villages"
      },
      "relation": "caused",
      "effect": {
        "span": "about 10 workers were injured"
      }
    }
  ]
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
        "span": "some pupils returned to classes after having spent months out of school"
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
    "tp": 1,
    "fp": 0,
    "fn": 3
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
        "span": "Anger over last week ’ s Yuen Long attack"
      },
      "relation": "caused",
      "effect": {
        "span": "has added fuel to Hong Kong ’ s protest movement"
      }
    }
  ]
}
```

### --- id=874 ---

输入文本: About 28 organisations under the banner of Confederation of Sanathana Dharma Suhruth Vedi launched agitations about 20 months ago demanding that the study centres be opened .

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
      "cause": "demanding that the study centres be opened",
      "effect": "About 28 organisations under the banner of Confederation of Sanathana Dharma Suhruth Vedi launched agitations about 20 months ago"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding that the study centres be opened"
      },
      "relation": "caused",
      "effect": {
        "span": "launched agitations"
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
    },
    {
      "cause": {
        "span": "protestors pelted stones at police"
      },
      "relation": "caused",
      "effect": {
        "span": "Police injured"
      }
    }
  ]
}
```

### --- id=2663 ---

输入文本: ‘ Attack motivated ’ Speaking to The Hindu over telephone from her hospital bed , Ms. Rajakumari said it was a clear attempt on her life .

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
        "span": "it was a clear attempt on her life"
      },
      "relation": "caused",
      "effect": {
        "span": "Attack motivated"
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
        "span": "the department to conclude that I prompted the idea of an agitation among the inmates"
      }
    }
  ]
}
```
