# Qwen3.6 27B No Thinking CNC test fixed_rag_k3 samples 501-1038 eval report

## 配置
```json
{
  "label": "Qwen3.6 27B No Thinking CNC test fixed_rag_k3 samples 501-1038",
  "model": "local/qwen3.6-27b-no-thinking",
  "dataset": "cnc_sft_test",
  "sample_count": 538,
  "prompt_name": "v9.6",
  "use_rag": true,
  "rag_mode": "knn_pattern",
  "rag_top_k": 3,
  "temperature": 0.0,
  "max_tokens": 2048,
  "output_schema": "standard",
  "primary_metric": "strict_token_f1",
  "progress_every": 100,
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
  "report_error_metric": "strict_token_f1",
  "metadata_path": "D:\\Master thesis\\RAG Database\\cnc_examples.jsonl",
  "embeddings_path": "D:\\Master thesis\\RAG Database\\cnc_embeddings.npy"
}
```

## 统计指标
```text
================ Qwen3.6 27B No Thinking CNC test fixed_rag_k3 samples 501-1038 final report ================
样本总数: 538
  Gold 含因果: 282 | Pred 含因果: 280
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.814
  Precision: 0.825
  Recall   : 0.819
  F1       : 0.822
  (TP=231, TN=207, FP=49, FN=51)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 538
    Gold triples: 394 | Pred triples: 332
    Precision: 0.611
    Recall   : 0.515
    F1       : 0.559
    (TP=203, FP=129, FN=191)
  [anchor_window]
    样本数: 538
    Gold triples: 394 | Pred triples: 332
    Precision: 0.645
    Recall   : 0.543
    F1       : 0.590
    (TP=214, FP=118, FN=180)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 231
    Gold triples: 334 | Pred triples: 281
    Precision: 0.722
    Recall   : 0.608
    F1       : 0.660
    (TP=203, FP=78, FN=131)
  [anchor_window]
    样本数: 231
    Gold triples: 334 | Pred triples: 281
    Precision: 0.762
    Recall   : 0.641
    F1       : 0.696
    (TP=214, FP=67, FN=120)
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

Sample details shown: first 200 of 204 wrong samples from 538 total samples.

### --- id=1076 ---

输入文本: Meanwhile , dalit organisations supported by leaders cutting across partylines geared up to enforce a bandh on Monday demanding the arrest of ‘ real culprits ' behind the vandalism .

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
      "cause": "demanding the arrest of ‘ real culprits ' behind the vandalism",
      "effect": "dalit organisations supported by leaders cutting across partylines geared up to enforce a bandh on Monday"
    },
    {
      "cause": "to enforce a bandh on Monday demanding the arrest of ‘ real culprits ' behind the vandalism",
      "effect": "dalit organisations supported by leaders cutting across partylines geared up"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding the arrest of ‘ real culprits ' behind the vandalism"
      },
      "relation": "caused",
      "effect": {
        "span": "dalit organisations supported by leaders cutting across partylines geared up to enforce a bandh on Monday"
      }
    }
  ]
}
```

### --- id=377 ---

输入文本: They began to march at around 2 pm , attracting onlookers and passers-by as they moved towards a popular shopping and entertainment area under close police watch .

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
      "cause": "they moved towards a popular shopping and entertainment area under close police watch",
      "effect": "attracting onlookers and passers-by"
    }
  ],
  "pred_triples": []
}
```

### --- id=847 ---

输入文本: Earlier , in a letter to the HRD ministry through NIT administration , the students had demanded hoisting of national flag , action against staff involved in anti-national activities and replacing Jammu and Kashmir Police by CRPF for security of the NIT campus , which has been gripped by tension following clashes in the wake of India 's loss to West Indies in the World T 20 Cup .

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
      "cause": "security of the NIT campus",
      "effect": "replacing Jammu and Kashmir Police by CRPF"
    },
    {
      "cause": "clashes",
      "effect": "the NIT campus , which has been gripped by tension"
    },
    {
      "cause": "India 's loss to West Indies in the World T 20 Cup",
      "effect": "clashes"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "clashes"
      },
      "relation": "caused",
      "effect": {
        "span": "the NIT campus , which has been gripped by tension"
      }
    },
    {
      "cause": {
        "span": "India 's loss to West Indies in the World T 20 Cup"
      },
      "relation": "caused",
      "effect": {
        "span": "clashes"
      }
    },
    {
      "cause": {
        "span": "the NIT campus , which has been gripped by tension following clashes in the wake of India 's loss to West Indies in the World T 20 Cup"
      },
      "relation": "caused",
      "effect": {
        "span": "the students had demanded hoisting of national flag , action against staff involved in anti-national activities and replacing Jammu and Kashmir Police by CRPF for security of the NIT campus"
      }
    }
  ]
}
```

### --- id=1706 ---

输入文本: NE Youth 's Death Sparks Protest 01st February 2014 09:23 AM Nido Taniam , son of Arunachal Pradesh Congress legislator Nido Pavitra died on Thursday allegedly after being beaten up at a market area in Lajpar Nagar here .

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
      "cause": "being beaten up at a market area in Lajpar Nagar here",
      "effect": "Nido Taniam , son of Arunachal Pradesh Congress legislator Nido Pavitra died on Thursday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Nido Taniam , son of Arunachal Pradesh Congress legislator Nido Pavitra died on Thursday allegedly after being beaten up at a market area in Lajpar Nagar here ."
      },
      "relation": "caused",
      "effect": {
        "span": "NE Youth 's Death Sparks Protest"
      }
    }
  ]
}
```

### --- id=2433 ---

输入文本: ﻿The popular social network has been blocked since ethnic riots in China ’ s far west in 2009 and Instagram was banned during pro-democracy protests in Hong Kong in 2014 .

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
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "ethnic riots in China ’ s far west in 2009",
      "effect": "﻿The popular social network has been blocked"
    },
    {
      "cause": "pro-democracy protests in Hong Kong in 2014",
      "effect": "Instagram was banned"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "ethnic riots in China ’ s far west in 2009"
      },
      "relation": "caused",
      "effect": {
        "span": "The popular social network has been blocked since ethnic riots in China ’ s far west in 2009"
      }
    },
    {
      "cause": {
        "span": "pro-democracy protests in Hong Kong in 2014"
      },
      "relation": "caused",
      "effect": {
        "span": "Instagram was banned during pro-democracy protests in Hong Kong in 2014"
      }
    }
  ]
}
```

### --- id=1751 ---

输入文本: `` We simply do not have space for such a detrimental amount of pollution that is to come out from that coal-fired power station , '' the organisation 's project co-ordinator Tristen Taylor said at a protest against the mining company in Johannesburg .

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
        "span": "against the mining company"
      },
      "relation": "caused",
      "effect": {
        "span": "the organisation 's project co-ordinator Tristen Taylor said at a protest"
      }
    }
  ]
}
```

### --- id=834 ---

输入文本: 07th April 2016 12:37 AM Students of Jammu University shout slogans during a protest rally against the police action on non-Kashmiri students in NIT

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
      "cause": "a protest rally",
      "effect": "Students of Jammu University shout slogans"
    },
    {
      "cause": "against the police action on non-Kashmiri students in NIT",
      "effect": "a protest rally"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the police action on non-Kashmiri students in NIT"
      },
      "relation": "caused",
      "effect": {
        "span": "Students of Jammu University shout slogans during a protest rally"
      }
    }
  ]
}
```

### --- id=717 ---

输入文本: City Police Commissioner Ravada Chandrasekhar has also directed Shangumugham Assistant Commissioner Suresh Kumar to probe into the role of the police in the incident , including the allegation that LDF candidate P. Ramachandran Nair was pushed by the Pettah Circle Inspector .

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
        "span": "to probe into the role of the police in the incident , including the allegation that LDF candidate P. Ramachandran Nair was pushed by the Pettah Circle Inspector"
      },
      "relation": "caused",
      "effect": {
        "span": "City Police Commissioner Ravada Chandrasekhar has also directed Shangumugham Assistant Commissioner Suresh Kumar"
      }
    }
  ]
}
```

### --- id=2528 ---

输入文本: Nine persons have been arrested so far since the incident happened on Sunday night when the 21 - year-old Tanzanian student went through the ordeal in vigilante justice by an angry mob in a case of " mistaken identity " after a woman was mowed down by a car driven by a Sudanese here .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 4
  },
  "gold_relations": [
    {
      "cause": "the incident happened on Sunday night",
      "effect": "Nine persons have been arrested so far"
    },
    {
      "cause": "the 21 - year-old Tanzanian student went through the ordeal",
      "effect": "the incident happened on Sunday night"
    },
    {
      "cause": "vigilante justice by an angry mob",
      "effect": "the 21 - year-old Tanzanian student went through the ordeal"
    },
    {
      "cause": "a case of \" mistaken identity \"",
      "effect": "vigilante justice by an angry mob"
    },
    {
      "cause": "a woman was mowed down by a car driven by a Sudanese here",
      "effect": "a case of \" mistaken identity \""
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the incident happened on Sunday night"
      },
      "relation": "caused",
      "effect": {
        "span": "Nine persons have been arrested so far"
      }
    },
    {
      "cause": {
        "span": "a woman was mowed down by a car driven by a Sudanese here"
      },
      "relation": "caused",
      "effect": {
        "span": "the 21 - year-old Tanzanian student went through the ordeal in vigilante justice by an angry mob in a case of \" mistaken identity \""
      }
    }
  ]
}
```

### --- id=1124 ---

输入文本: 21st February 2016 10:28 PM JAMMU : The Army today appealed to the people of Haryana , which has been hit by Jat quota stir , to extend support in giving a " befitting farewell " to the brave son of the soil , 23 - year-old Capt Pawan Kumar , who died while fighting militants in Pulwama district of Jammu and Kashmir .

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
      "cause": "to extend support in giving a \" befitting farewell \" to the brave son of the soil , 23 - year-old Capt Pawan Kumar",
      "effect": "The Army today appealed to the people of Haryana"
    },
    {
      "cause": "fighting militants in Pulwama district of Jammu and Kashmir",
      "effect": "23 - year-old Capt Pawan Kumar , who died"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Capt Pawan Kumar , who died while fighting militants in Pulwama district of Jammu and Kashmir"
      },
      "relation": "caused",
      "effect": {
        "span": "The Army today appealed to the people of Haryana ... to extend support in giving a \" befitting farewell \" to the brave son of the soil , 23 - year-old Capt Pawan Kumar"
      }
    },
    {
      "cause": {
        "span": "fighting militants in Pulwama district of Jammu and Kashmir"
      },
      "relation": "caused",
      "effect": {
        "span": "Capt Pawan Kumar , who died"
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
        "span": "in protest against erratic supply of drinking water at Kelamagalam in Udhanapalli"
      },
      "relation": "caused",
      "effect": {
        "span": "Women took to streets carrying pots on Wednesday"
      }
    }
  ]
}
```

### --- id=2832 ---

输入文本: I am warning other theatres to stop the screening , otherwise , we will intensify our protest in the city in coming days , ” said city Bajrang Dal chief Jwalit Mehta , who led the attack .

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
      "cause": "other theatres to stop the screening",
      "effect": "we will intensify our protest in the city in coming days"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "otherwise"
      },
      "relation": "caused",
      "effect": {
        "span": "we will intensify our protest in the city in coming days"
      }
    }
  ]
}
```

### --- id=335 ---

输入文本: The controversy sparked off after the Kerala State Road Transport Employees Association ( KSRTEA ) pasted stickers on KSRTC buses seeking public intervention against ‘ police-goonda ’ attack on employees .

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
      "cause": "the Kerala State Road Transport Employees Association ( KSRTEA ) pasted stickers on KSRTC buses",
      "effect": "The controversy"
    },
    {
      "cause": "seeking public intervention",
      "effect": "the Kerala State Road Transport Employees Association ( KSRTEA ) pasted stickers on KSRTC buses"
    },
    {
      "cause": "against ‘ police-goonda ’ attack on employees",
      "effect": "public intervention"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Kerala State Road Transport Employees Association ( KSRTEA ) pasted stickers on KSRTC buses seeking public intervention against ‘ police-goonda ’ attack on employees"
      },
      "relation": "caused",
      "effect": {
        "span": "The controversy sparked off"
      }
    }
  ]
}
```

### --- id=2935 ---

输入文本: Whitfield said the part fortnight has seen highways blocked , 20 trucks burnt and a driver die of injuries sustained when his truck was petrol bombed near Touws River in the Western Cape .

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
      "cause": "his truck was petrol bombed near Touws River in the Western Cape",
      "effect": "the part fortnight has seen highways blocked , 20 trucks burnt and a driver die of injuries sustained"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "his truck was petrol bombed near Touws River in the Western Cape"
      },
      "relation": "caused",
      "effect": {
        "span": "a driver die of injuries sustained"
      }
    }
  ]
}
```

### --- id=810 ---

输入文本: HUBLI : Support for Anna Hazare December 29 , 2011 00:00 IST Day two of the dharna organised by India Against Corruption , Hubli , in support of anti-corruption activist Anna Hazare attracted people from various sections of society .

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
        "span": "in support of anti-corruption activist Anna Hazare"
      },
      "relation": "caused",
      "effect": {
        "span": "Day two of the dharna organised by India Against Corruption , Hubli , attracted people from various sections of society ."
      }
    }
  ]
}
```

### --- id=2826 ---

输入文本: TAMIL NADU Demonstration staged September 17 , 2012 00:00 IST Members of Popular Front of India staged a demonstration in Tirupur on Saturday against anti-Islam film .

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
        "span": "against anti-Islam film"
      },
      "relation": "caused",
      "effect": {
        "span": "Members of Popular Front of India staged a demonstration in Tirupur on Saturday"
      }
    }
  ]
}
```

### --- id=1166 ---

输入文本: During the recent country-wide bandh called by all the Opposition parties in protest against the fuel price hikes , most firms asked their staff to work from home .

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
      "cause": "in protest against the fuel price hikes",
      "effect": "the recent country-wide bandh called by all the Opposition parties"
    },
    {
      "cause": "the recent country-wide bandh called by all the Opposition parties",
      "effect": "most firms asked their staff to work from home"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the fuel price hikes"
      },
      "relation": "caused",
      "effect": {
        "span": "the recent country-wide bandh called by all the Opposition parties"
      }
    },
    {
      "cause": {
        "span": "the recent country-wide bandh called by all the Opposition parties in protest against the fuel price hikes"
      },
      "relation": "caused",
      "effect": {
        "span": "most firms asked their staff to work from home"
      }
    }
  ]
}
```

### --- id=1470 ---

输入文本: A week after the killing of a Congolese man in the national capital that stirred a diplomatic row and instigated violence against Indians in Congo , four attacks on African nationals by the residents in Chattarpur were reported on Friday .

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
      "cause": "the killing of a Congolese man in the national capital",
      "effect": "a diplomatic row and instigated violence against Indians in Congo"
    },
    {
      "cause": "the killing of a Congolese man in the national capital",
      "effect": "four attacks on African nationals by the residents in Chattarpur"
    }
  ],
  "pred_triples": []
}
```

### --- id=833 ---

输入文本: On getting the news about Mr. Hazare breaking his fast , they too ended their dharna .

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
        "span": "getting the news about Mr. Hazare breaking his fast"
      },
      "relation": "caused",
      "effect": {
        "span": "they too ended their dharna"
      }
    }
  ]
}
```

### --- id=225 ---

输入文本: 02nd October 2015 03:39 AM RAICHUR : The ongoing agitation against the Centre ’ s decision to set up the state ’ s first IIT at Dharwad took an ugly turn on Thursday after West Police Station PSI Agni allegedly assaulted a lorry driver and brandished his service revolver at the agitators during a protest by the lorry owners ’ association here .

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
      "cause": "West Police Station PSI Agni allegedly assaulted a lorry driver and brandished his service revolver at the agitators during a protest by the lorry owners ’ association here",
      "effect": "The ongoing agitation against the Centre ’ s decision to set up the state ’ s first IIT at Dharwad took an ugly turn on Thursday"
    },
    {
      "cause": "against the Centre ’ s decision to set up the state ’ s first IIT at Dharwad",
      "effect": "The ongoing agitation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the Centre 's decision to set up the state 's first IIT at Dharwad"
      },
      "relation": "caused",
      "effect": {
        "span": "The ongoing agitation ... took an ugly turn on Thursday after West Police Station PSI Agni allegedly assaulted a lorry driver and brandished his service revolver at the agitators during a protest by the lorry owners ' association here"
      }
    },
    {
      "cause": {
        "span": "West Police Station PSI Agni allegedly assaulted a lorry driver and brandished his service revolver at the agitators during a protest by the lorry owners ' association here"
      },
      "relation": "caused",
      "effect": {
        "span": "The ongoing agitation against the Centre 's decision to set up the state 's first IIT at Dharwad took an ugly turn on Thursday"
      }
    }
  ]
}
```

### --- id=1100 ---

输入文本: Students and lawyers also joined the protests , focusing on Mahabubnagar district to stop vehicles entering Telangana coming from Kurnool district , which is a part of the Rayalaseema region .

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
      "cause": "to stop vehicles entering Telangana coming from Kurnool district , which is a part of the Rayalaseema region",
      "effect": "Students and lawyers also joined the protests , focusing on Mahabubnagar district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to stop vehicles entering Telangana coming from Kurnool district"
      },
      "relation": "caused",
      "effect": {
        "span": "Students and lawyers also joined the protests , focusing on Mahabubnagar district"
      }
    }
  ]
}
```

### --- id=672 ---

输入文本: Photo : A. Muralitharan Staff Reporter Being built as part of underground drainage network scheme TAMBARAM : Residents of Keelkattalai on Tuesday protested the construction of a lift station ( a powerful pumping station ) at a burial ground at Arulmurugan Nagar .

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
        "span": "protested the construction of a lift station ( a powerful pumping station ) at a burial ground at Arulmurugan Nagar"
      },
      "relation": "caused",
      "effect": {
        "span": "Residents of Keelkattalai on Tuesday protested"
      }
    }
  ]
}
```

### --- id=2105 ---

输入文本: The call was given by the Joint Front of Trade Unions of the GIC and the LIC.The front has given a call to hold daily protest demonstrations until Parliament session gets over .

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
        "span": "until Parliament session gets over"
      },
      "relation": "caused",
      "effect": {
        "span": "The front has given a call to hold daily protest demonstrations"
      }
    }
  ]
}
```

### --- id=2330 ---

输入文本: In the same breath , he made light of the Seemandhra protests , observing that when a state is bifurcated , it is natural for some to resign and protest .

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
      "cause": "a state is bifurcated",
      "effect": "some to resign and protest"
    }
  ],
  "pred_triples": []
}
```

### --- id=121 ---

输入文本: Accusing the CPM of instigating the violence , she said the deaths were result of clashes between the Congress and the Marxists .

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
      "cause": "Accusing the CPM of instigating the violence",
      "effect": "she said the deaths were result of clashes between the Congress and the Marxists"
    },
    {
      "cause": "were result of clashes between the Congress and the Marxists",
      "effect": "the deaths"
    }
  ],
  "pred_triples": []
}
```

### --- id=2103 ---

输入文本: Protest heldAs a part of the on-going nation-wide agitation , the employees of the insurance companies held a demonstration in front of the regional office of the National Insurance Company Limited in Sector 35 here .

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
        "span": "As a part of the on-going nation-wide agitation"
      },
      "relation": "caused",
      "effect": {
        "span": "the employees of the insurance companies held a demonstration in front of the regional office of the National Insurance Company Limited in Sector 35 here"
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
      "cause": "18 exchanges of fire in just the six weeks from 14 December 2004",
      "effect": "16 extremists died"
    }
  ],
  "pred_triples": []
}
```

### --- id=2045 ---

输入文本: But the attacks by Congress workers in Malappuram district have tarnished him and the yatra .

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
        "span": "the attacks by Congress workers in Malappuram district"
      },
      "relation": "caused",
      "effect": {
        "span": "have tarnished him and the yatra"
      }
    }
  ]
}
```

### --- id=2896 ---

输入文本: Trinamool activist dies in police custody in Hooghly , cadres go on rampage

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
      "cause": "Trinamool activist dies in police custody in Hooghly",
      "effect": "cadres go on rampage"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Trinamool activist dies in 'police custody' in Hooghly"
      },
      "relation": "caused",
      "effect": {
        "span": "cadres go on rampage"
      }
    }
  ]
}
```

### --- id=623 ---

输入文本: The move angered residents who had been protesting in front of the court against the two being granted bail .

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
      "cause": "The move",
      "effect": "angered residents who had been protesting in front of the court against the two being granted bail"
    },
    {
      "cause": "against the two being granted bail",
      "effect": "residents who had been protesting in front of the court"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the two being granted bail"
      },
      "relation": "caused",
      "effect": {
        "span": "residents who had been protesting in front of the court against the two being granted bail"
      }
    },
    {
      "cause": {
        "span": "The move"
      },
      "relation": "caused",
      "effect": {
        "span": "angered residents who had been protesting in front of the court against the two being granted bail"
      }
    }
  ]
}
```

### --- id=2677 ---

输入文本: PTI Guwahati Police Commissioner Mukesh Aggarwal said that the anti-talk faction of ULFA may be behind the attack .

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
      "cause": "the anti-talk faction of ULFA",
      "effect": "the attack"
    }
  ],
  "pred_triples": []
}
```

### --- id=2667 ---

输入文本: TDP district president Karanam Balaramakrishna Murthi , who went to the village along with the team , blamed the police for remaining mute spectators to the one-hour ‘ sordid drama .

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
      "cause": "remaining mute spectators to the one-hour ‘ sordid drama",
      "effect": "TDP district president Karanam Balaramakrishna Murthi , who went to the village along with the team , blamed the police"
    }
  ],
  "pred_triples": []
}
```

### --- id=2024 ---

输入文本: : DMK President 14th September 2014 01:12 PM CHENNAI : DMK chief M Karunanidhi today said the arrest of ISI spies and their activities in Tamil Nadu has created panic among people and asked why no arrests have been made in connection with the May 1 twin bomb blasts in a train at the Central Railway Station in which a woman was killed .

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
      "cause": "the arrest of ISI spies and their activities in Tamil Nadu",
      "effect": "has created panic among people"
    },
    {
      "cause": "the May 1 twin bomb blasts in a train at the Central Railway Station",
      "effect": "a woman was killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the arrest of ISI spies and their activities in Tamil Nadu"
      },
      "relation": "caused",
      "effect": {
        "span": "panic among people"
      }
    }
  ]
}
```

### --- id=2456 ---

输入文本: CPM leaders hatched a conspiracy and killed him brutally using hired killers .

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
        "span": "hatched a conspiracy"
      },
      "relation": "caused",
      "effect": {
        "span": "CPM leaders ... killed him brutally using hired killers"
      }
    }
  ]
}
```

### --- id=824 ---

输入文本: The parades come after two separate eruptions of bloodletting claimed more than a dozen lives in Xinjiang , a sprawling border region which has been blighted by repeated outbreaks of ethnic violence and terrorist attacks .

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
        "span": "two separate eruptions of bloodletting claimed more than a dozen lives in Xinjiang"
      },
      "relation": "caused",
      "effect": {
        "span": "The parades come"
      }
    }
  ]
}
```

### --- id=87 ---

输入文本: About 13,000 marched on Sunday to protest against China ’ s intervention , ending in clashes with police outside Beijing ’ s main presence in the city and four arrests .

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
      "cause": "to protest against China ’ s intervention",
      "effect": "About 13,000 marched on Sunday"
    },
    {
      "cause": "About 13,000 marched on Sunday",
      "effect": "clashes with police outside Beijing ’ s main presence in the city and four arrests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest against China ’ s intervention"
      },
      "relation": "caused",
      "effect": {
        "span": "About 13,000 marched on Sunday"
      }
    },
    {
      "cause": {
        "span": "About 13,000 marched on Sunday to protest against China ’ s intervention"
      },
      "relation": "caused",
      "effect": {
        "span": "ending in clashes with police outside Beijing ’ s main presence in the city and four arrests"
      }
    }
  ]
}
```

### --- id=1718 ---

输入文本: Four jawans were also injured in the encounter but they were all out of danger , police said .

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
        "span": "the encounter"
      },
      "relation": "caused",
      "effect": {
        "span": "Four jawans were also injured"
      }
    }
  ]
}
```

### --- id=2258 ---

输入文本: A Day of Protests Inside and Outside Assembly 17th February 2016 05:40 AM THIRUVANANTHAPURAM : Be it in the Assembly or outside , protests will be heard only if they rise to a high .

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
      "cause": "they rise to a high",
      "effect": "protests will be heard"
    }
  ],
  "pred_triples": []
}
```

### --- id=2823 ---

输入文本: “ We are sorry that the public would have been inconvenienced by this strike but it was unavoidable due to the non-serious approach of the IBA and government to avert the strike by improving their offer on wage increase and discussing our concerns on the banking sector reforms , ” he said .

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
      "cause": "the public would have been inconvenienced by this strike",
      "effect": "We are sorry"
    },
    {
      "cause": "this strike",
      "effect": "the public would have been inconvenienced"
    },
    {
      "cause": "the non-serious approach of the IBA and government to avert the strike by improving their offer on wage increase and discussing our concerns on the banking sector reforms",
      "effect": "it was unavoidable"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the non-serious approach of the IBA and government to avert the strike by improving their offer on wage increase and discussing our concerns on the banking sector reforms"
      },
      "relation": "caused",
      "effect": {
        "span": "it was unavoidable"
      }
    }
  ]
}
```

### --- id=1445 ---

输入文本: After firing , Chandrababu , Left gun for YSR - Indian Express Express News Service , Express News Service : HYDERABAD / KHAMMAM , JULY 29 , Sun Jul 29 2007 , 23:47 hrs The embers left by Saturday 's police firing which killed six Left activists agitating for land are unlikely to die soon .

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
      "cause": "Saturday 's police firing",
      "effect": "killed six Left activists agitating for land"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Saturday 's police firing"
      },
      "relation": "caused",
      "effect": {
        "span": "six Left activists agitating for land are unlikely to die soon"
      }
    }
  ]
}
```

### --- id=2589 ---

输入文本: Chief Minister Nitish Kumar , on the other hand , said Thursday 's shutdown was opposed to development .

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
      "effect": "Thursday 's shutdown"
    }
  ],
  "pred_triples": []
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
        "span": "condemning the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "The Indian Medical Association has decided that a more trenchant protest needs to be made against the increasing attacks on the medical community"
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

### --- id=1284 ---

输入文本: The attack was in retaliation to a similar attack on a Congress leader by TDP activists one year ago .

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
        "span": "a similar attack on a Congress leader by TDP activists one year ago"
      },
      "relation": "caused",
      "effect": {
        "span": "The attack was in retaliation"
      }
    }
  ]
}
```

### --- id=2762 ---

输入文本: Some anti-social elements which were already in the area took advantage of the incident to pelt stones at the police , ’ ’ Anuradha said .

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
        "span": "Some anti-social elements which were already in the area took advantage of the incident to pelt stones at the police"
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
        "span": "the clashes"
      },
      "relation": "caused",
      "effect": {
        "span": "17 people had been hospitalised"
      }
    }
  ]
}
```

### --- id=1994 ---

输入文本: The protests were initially focused on a bill that that would make it easier to extradite people to China from the semi-autonomous city .

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
      "cause": "were initially focused on a bill that that would make it easier to extradite people to China from the semi-autonomous city",
      "effect": "The protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a bill that that would make it easier to extradite people to China from the semi-autonomous city"
      },
      "relation": "caused",
      "effect": {
        "span": "The protests were initially focused on a bill that that would make it easier to extradite people to China from the semi-autonomous city"
      }
    }
  ]
}
```

### --- id=1399 ---

输入文本: EFF protests at Constitutional Court as Fees Must Fall activist fights for bail ANA Reporter JOHANNESBURG , March 1 ( ANA ) - Demonstrators clad in Economic Freedom Fighters ( EFF ) regalia gathered at the Constitutional Court on Wednesday as an application by student activist Bonginkosi Khanyile was being heard .

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
      "cause": "an application by student activist Bonginkosi Khanyile was being heard",
      "effect": "Demonstrators clad in Economic Freedom Fighters ( EFF ) regalia gathered at the Constitutional Court on Wednesday"
    }
  ],
  "pred_triples": []
}
```

### --- id=2539 ---

输入文本: City police have now constituted teams to carry out regular inspection at malls following the blasts .

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
      "cause": "to carry out regular inspection at malls",
      "effect": "City police have now constituted teams"
    },
    {
      "cause": "the blasts",
      "effect": "to carry out regular inspection at malls"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the blasts"
      },
      "relation": "caused",
      "effect": {
        "span": "City police have now constituted teams to carry out regular inspection at malls"
      }
    }
  ]
}
```

### --- id=911 ---

输入文本: Mr. Patil and others insisted that Deputy Commissioner Pankaj Kumar Pandey arrive at the scene of protest to receive the memorandum from them .

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
      "cause": "to receive the memorandum from them",
      "effect": "Deputy Commissioner Pankaj Kumar Pandey arrive at the scene of protest"
    }
  ],
  "pred_triples": []
}
```

### --- id=640 ---

输入文本: ANDHRA PRADESH Protests mar land distribution

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
      "cause": "Protests",
      "effect": "mar land distribution"
    }
  ],
  "pred_triples": []
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

### --- id=1043 ---

输入文本: Denied Aid , Dalit Boy tries to End Life

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
      "cause": "Denied Aid",
      "effect": "Dalit Boy tries to End Life"
    }
  ],
  "pred_triples": []
}
```

### --- id=2523 ---

输入文本: Describing the incident as " a dastardly and anti-democratic act " , Singh said , " Government will take firm action against the perpetrators of violence of any kind . "

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
      "cause": "against the perpetrators of violence of any kind",
      "effect": "Government will take firm action"
    }
  ],
  "pred_triples": []
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
        "span": "a similar attack last December in New Delhi"
      },
      "relation": "caused",
      "effect": {
        "span": "sparked nationwide protests"
      }
    }
  ]
}
```

### --- id=678 ---

输入文本: Great revolutionaries of the Hindustan Republican Association including Jogesh Chatterjee , Chandrashekhar Azad , Yogendra Shukla , Ashfaqullah Khan , Bhagat Singh , and Batukeshwar Dutt protested against decreased sense of patriotism amongst the youth and the depraved polity increasingly leading to reduced sense of citizenry .

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
      "cause": "against decreased sense of patriotism amongst the youth and the depraved polity increasingly leading to reduced sense of citizenry",
      "effect": "Great revolutionaries of the Hindustan Republican Association including Jogesh Chatterjee , Chandrashekhar Azad , Yogendra Shukla , Ashfaqullah Khan , Bhagat Singh , and Batukeshwar Dutt protested"
    },
    {
      "cause": "decreased sense of patriotism amongst the youth and the depraved polity",
      "effect": "reduced sense of citizenry"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against decreased sense of patriotism amongst the youth and the depraved polity increasingly leading to reduced sense of citizenry"
      },
      "relation": "caused",
      "effect": {
        "span": "Great revolutionaries of the Hindustan Republican Association including Jogesh Chatterjee , Chandrashekhar Azad , Yogendra Shukla , Ashfaqullah Khan , Bhagat Singh , and Batukeshwar Dutt protested"
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
      "cause": "against inflation in Patna",
      "effect": "An RJD activist wears a garland and crown made of vegetables and shouts slogans along with others during a protest"
    },
    {
      "cause": "during a protest against inflation in Patna",
      "effect": "An RJD activist wears a garland and crown made of vegetables and shouts slogans along with others"
    }
  ],
  "pred_triples": []
}
```

### --- id=2276 ---

输入文本: The strike was called off after the CM personally intervened to hold an hour-long meeting with Mayor Nandu Satam , BEST Chairman Arvind Nerkar , Rao and other union leaders earlier in the day .

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
      "cause": "the CM personally intervened to hold an hour-long meeting with Mayor Nandu Satam , BEST Chairman Arvind Nerkar , Rao and other union leaders earlier in the day",
      "effect": "The strike was called off"
    },
    {
      "cause": "to hold an hour-long meeting with Mayor Nandu Satam , BEST Chairman Arvind Nerkar , Rao and other union leaders earlier in the day",
      "effect": "the CM personally intervened"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the CM personally intervened to hold an hour-long meeting with Mayor Nandu Satam , BEST Chairman Arvind Nerkar , Rao and other union leaders earlier in the day"
      },
      "relation": "caused",
      "effect": {
        "span": "The strike was called off"
      }
    }
  ]
}
```

### --- id=1125 ---

输入文本: Army Appeals to Haryana People on Captain Pawan Kumar 's Last Rites

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
      "cause": "Captain Pawan Kumar 's Last Rites",
      "effect": "Army Appeals to Haryana People"
    }
  ],
  "pred_triples": []
}
```

### --- id=291 ---

输入文本: Analysts say the mainland public has taken to such protests because they lack adequate channels to express their concerns about environmental risks posed by massive industrial projects .

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
      "cause": "they lack adequate channels to express their concerns about environmental risks posed by massive industrial projects",
      "effect": "the mainland public has taken to such protests"
    },
    {
      "cause": "massive industrial projects",
      "effect": "environmental risks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they lack adequate channels to express their concerns about environmental risks posed by massive industrial projects"
      },
      "relation": "caused",
      "effect": {
        "span": "the mainland public has taken to such protests"
      }
    }
  ]
}
```

### --- id=574 ---

输入文本: Babbar was equally scathing in his attack against Samajwadi Party chief Mulayam Singh Yadav , when he deplored the state administration 's high-handedness in dealing with agitating farmers .

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
        "span": "the state administration 's high-handedness in dealing with agitating farmers"
      },
      "relation": "caused",
      "effect": {
        "span": "Babbar was equally scathing in his attack against Samajwadi Party chief Mulayam Singh Yadav , when he deplored"
      }
    }
  ]
}
```

### --- id=1957 ---

输入文本: 59 persons died in the Sabarmati express attack in Godhra on February 27 , 2002 while around 1,000 persons were killed in the resultant riots .

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
      "cause": "the Sabarmati express attack in Godhra on February 27 , 2002",
      "effect": "59 persons died"
    },
    {
      "cause": "the resultant riots",
      "effect": "around 1,000 persons were killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Sabarmati express attack in Godhra on February 27 , 2002"
      },
      "relation": "caused",
      "effect": {
        "span": "59 persons died"
      }
    },
    {
      "cause": {
        "span": "the Sabarmati express attack in Godhra on February 27 , 2002"
      },
      "relation": "caused",
      "effect": {
        "span": "around 1,000 persons were killed in the resultant riots"
      }
    }
  ]
}
```

### --- id=515 ---

输入文本: ( SUBS/NEDS : IF USED , CREDIT MUST BE RETAINED ) Two Daily Sun reporters were held captive , allegedly by Economic Freedom Fighters members during a protest in Nellmapius , Pretoria , Beeld reported on Thursday .

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
        "span": "during a protest in Nellmapius , Pretoria"
      },
      "relation": "caused",
      "effect": {
        "span": "Two Daily Sun reporters were held captive , allegedly by Economic Freedom Fighters members"
      }
    }
  ]
}
```

### --- id=864 ---

输入文本: Muslim women sit on dharna , demand passage of Womens Reservation Bill

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
      "cause": "demand passage of Womens Reservation Bill",
      "effect": "Muslim women sit on dharna"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demand passage of Women's Reservation Bill"
      },
      "relation": "caused",
      "effect": {
        "span": "Muslim women sit on dharna"
      }
    }
  ]
}
```

### --- id=789 ---

输入文本: |PTI GAYA : A 20 - year-old youth was shot dead allegedly by JD(U) MLC Manorama Devi 's son Rocky for overtaking his vehicle near police line in Bihar 's Gaya district , triggering protests in the area .

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
      "cause": "overtaking his vehicle near police line in Bihar 's Gaya district",
      "effect": "A 20 - year-old youth was shot dead allegedly by JD(U) MLC Manorama Devi 's son Rocky"
    },
    {
      "cause": "A 20 - year-old youth was shot dead allegedly by JD(U) MLC Manorama Devi 's son Rocky",
      "effect": "triggering protests in the area"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "overtaking his vehicle near police line in Bihar 's Gaya district"
      },
      "relation": "caused",
      "effect": {
        "span": "A 20 - year-old youth was shot dead allegedly by JD(U) MLC Manorama Devi 's son Rocky"
      }
    },
    {
      "cause": {
        "span": "A 20 - year-old youth was shot dead allegedly by JD(U) MLC Manorama Devi 's son Rocky for overtaking his vehicle near police line in Bihar 's Gaya district"
      },
      "relation": "caused",
      "effect": {
        "span": "triggering protests in the area"
      }
    }
  ]
}
```

### --- id=1533 ---

输入文本: The religious seers and right-wing activists were earlier arrested at the Khairatabad Crossroads when they were marching towards the Raj Bhavan to meet the governor to submit a representation for the release of the swami who was arrested by the Special Investigating Team ( SIT ) on Monday for delivering an alleged hate speech at Indira Park in the city on January 8 .

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
      "cause": "they were marching towards the Raj Bhavan to meet the governor to submit a representation for the release of the swami",
      "effect": "The religious seers and right-wing activists were earlier arrested at the Khairatabad Crossroads"
    },
    {
      "cause": "to meet the governor",
      "effect": "they were marching towards the Raj Bhavan"
    },
    {
      "cause": "to submit a representation for the release of the swami",
      "effect": "to meet the governor"
    },
    {
      "cause": "delivering an alleged hate speech at Indira Park in the city on January 8",
      "effect": "was arrested by the Special Investigating Team ( SIT ) on Monday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they were marching towards the Raj Bhavan to meet the governor to submit a representation for the release of the swami"
      },
      "relation": "caused",
      "effect": {
        "span": "The religious seers and right-wing activists were earlier arrested at the Khairatabad Crossroads"
      }
    },
    {
      "cause": {
        "span": "delivering an alleged hate speech at Indira Park in the city on January 8"
      },
      "relation": "caused",
      "effect": {
        "span": "the swami who was arrested by the Special Investigating Team ( SIT ) on Monday"
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
        "span": "At least 44 persons were killed , about 4,800 houses burnt or damaged leaving about 20,000 people homeless"
      }
    }
  ]
}
```

### --- id=2236 ---

输入文本: VIJAYAWADA : Impasse over payment of salaries to civic workers continues

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
      "cause": "payment of salaries to civic workers",
      "effect": "Impasse"
    }
  ],
  "pred_triples": []
}
```

### --- id=2090 ---

输入文本: `` The group split themselves in two to execute attack at around 8pm , '' Brigadier Thulane Ngubane said .

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
      "cause": "to execute attack at around 8pm",
      "effect": "The group split themselves in two"
    }
  ],
  "pred_triples": []
}
```

### --- id=2929 ---

输入文本: Maoists force Centre to revisit CRPF deployment

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
        "span": "Maoists force"
      },
      "relation": "caused",
      "effect": {
        "span": "Centre to revisit CRPF deployment"
      }
    }
  ]
}
```

### --- id=132 ---

输入文本: `` We do not know about the strike , if we called for a strike we could have informed commuters , '' said president Philip Taaibosch .

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
      "cause": "we called for a strike",
      "effect": "we could have informed commuters"
    }
  ],
  "pred_triples": []
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
        "span": "Maoist attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Sub-Inspector Murlidhar Bastia of Raghunathpur area was killed"
      }
    }
  ]
}
```

### --- id=463 ---

输入文本: 22nd June 2012 11:06 AM With transport officials continuing the crackdown against private buses , transport operators and managements of educational institutions are trying to bring pressure on the state government by shutting the services .

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
      "cause": "transport officials continuing the crackdown against private buses",
      "effect": "transport operators and managements of educational institutions are trying to bring pressure on the state government"
    },
    {
      "cause": "transport operators and managements of educational institutions are trying to bring pressure on the state government",
      "effect": "shutting the services"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "transport officials continuing the crackdown against private buses"
      },
      "relation": "caused",
      "effect": {
        "span": "transport operators and managements of educational institutions are trying to bring pressure on the state government by shutting the services"
      }
    },
    {
      "cause": {
        "span": "to bring pressure on the state government"
      },
      "relation": "caused",
      "effect": {
        "span": "transport operators and managements of educational institutions are trying ... by shutting the services"
      }
    }
  ]
}
```

### --- id=82 ---

输入文本: Mainland authorities have launched a massive crackdown against terrorism in wake of a string of violent attacks in the restive Xinjiang region and other cities on the mainland .

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
      "cause": "a string of violent attacks in the restive Xinjiang region and other cities on the mainland",
      "effect": "Mainland authorities have launched a massive crackdown against terrorism"
    },
    {
      "cause": "against terrorism",
      "effect": "Mainland authorities have launched a massive crackdown"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a string of violent attacks in the restive Xinjiang region and other cities on the mainland"
      },
      "relation": "caused",
      "effect": {
        "span": "Mainland authorities have launched a massive crackdown against terrorism"
      }
    }
  ]
}
```

### --- id=2043 ---

输入文本: Service delivery protests turned violent over the weekend with sections of the N14 being blockaded .

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
        "span": "Service delivery protests"
      },
      "relation": "caused",
      "effect": {
        "span": "sections of the N14 being blockaded"
      }
    }
  ]
}
```

### --- id=837 ---

输入文本: The developments at the prestigious engineering institute also triggered politicking even as the state government assured that safety will be ensured for the students hailing from other states at the campus where CRPF has been deployed to instill a sense of security .

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
        "span": "The developments at the prestigious engineering institute"
      },
      "relation": "caused",
      "effect": {
        "span": "triggered politicking"
      }
    },
    {
      "cause": {
        "span": "to instill a sense of security"
      },
      "relation": "caused",
      "effect": {
        "span": "CRPF has been deployed"
      }
    }
  ]
}
```

### --- id=629 ---

输入文本: NIZAMABAD : Students take out rally seeking fee reimbursement dues October 22 , 2016 00:00 IST In response to the State-wide call , the students under the banner of Progressive Democratic Students Union took out rallies here and in Kamareddy district headquarters on Friday demanding the release of fee reimbursement and scholarships .

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
      "cause": "seeking fee reimbursement dues",
      "effect": "Students take out rally"
    },
    {
      "cause": "In response to the State-wide call",
      "effect": "the students under the banner of Progressive Democratic Students Union took out rallies here and in Kamareddy district headquarters on Friday demanding the release of fee reimbursement and scholarships"
    },
    {
      "cause": "demanding the release of fee reimbursement and scholarships",
      "effect": "the students under the banner of Progressive Democratic Students Union took out rallies here and in Kamareddy district headquarters on Friday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "In response to the State-wide call"
      },
      "relation": "caused",
      "effect": {
        "span": "the students under the banner of Progressive Democratic Students Union took out rallies here and in Kamareddy district headquarters on Friday"
      }
    },
    {
      "cause": {
        "span": "demanding the release of fee reimbursement and scholarships"
      },
      "relation": "caused",
      "effect": {
        "span": "the students under the banner of Progressive Democratic Students Union took out rallies here and in Kamareddy district headquarters on Friday"
      }
    }
  ]
}
```

### --- id=2687 ---

输入文本: Pinarayi ’ s march Mr. Chandy said the march led by Communist Party of India ( Marxist ) State secretary Pinarayi Vijayan was leaving a trail of clashes and violence , though the march ’ s motto was ‘ prosperous Kerala .

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
        "span": "the march led by Communist Party of India ( Marxist ) State secretary Pinarayi Vijayan"
      },
      "relation": "caused",
      "effect": {
        "span": "leaving a trail of clashes and violence"
      }
    }
  ]
}
```

### --- id=2885 ---

输入文本: Hoisting of the specially prepared multi-colour flag was seen as a mark of protest against the merger of the then Vidarbha , the Central Provinces and Berar into Maharashtra on May 1 , 1960 .

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
        "span": "as a mark of protest against the merger of the then Vidarbha , the Central Provinces and Berar into Maharashtra on May 1 , 1960"
      },
      "relation": "caused",
      "effect": {
        "span": "Hoisting of the specially prepared multi-colour flag was seen"
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
        "span": "Activists of Bajrang Dal , who had gathered outside Vikram University in Ujjain , stopped the two young people and beat up the man"
      }
    }
  ]
}
```

### --- id=2603 ---

输入文本: The bus stop walls were soon covered with posters , many of them exhorting people to " continue the struggle against patriarchy so that every woman can live a life free of violence " .

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
      "cause": "against patriarchy",
      "effect": "continue the struggle"
    },
    {
      "cause": "so that every woman can live a life free of violence",
      "effect": "against patriarchy"
    }
  ],
  "pred_triples": []
}
```

### --- id=1719 ---

输入文本: The encounter broke out at Amlar-Tral , 50 kms from here , this morning when the militants hiding in a house in the village opened fire on a joint search party of police and CRPF , they said .

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
      "cause": "the militants hiding in a house in the village opened fire on a joint search party of police and CRPF",
      "effect": "The encounter broke out at Amlar-Tral , 50 kms from here , this morning"
    },
    {
      "cause": "a joint search party of police and CRPF",
      "effect": "the militants hiding in a house in the village opened fire"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the militants hiding in a house in the village opened fire on a joint search party of police and CRPF"
      },
      "relation": "caused",
      "effect": {
        "span": "The encounter broke out at Amlar-Tral , 50 kms from here , this morning"
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
        "span": "me acute agony"
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

### --- id=3060 ---

输入文本: Ahmed , who was arrested in the Raju Pal murder case and was out on bail , allegedly threatened witnesses for deposing against him .

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
      "cause": "deposing against him",
      "effect": "Ahmed , who was arrested in the Raju Pal murder case and was out on bail , allegedly threatened witnesses"
    }
  ],
  "pred_triples": []
}
```

### --- id=609 ---

输入文本: ” AMU Registrar Prof. V. K. Abdul Jaleel 's notice says the university was being closed sine die “ on the basis of report received from the district administration and in the view of the unfortunate incident that occurred ” on Friday evening .

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
      "cause": "“ on the basis of report received from the district administration and in the view of the unfortunate incident that occurred ” on Friday evening",
      "effect": "the university was being closed sine die"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "report received from the district administration"
      },
      "relation": "caused",
      "effect": {
        "span": "the university was being closed sine die"
      }
    },
    {
      "cause": {
        "span": "the unfortunate incident that occurred on Friday evening"
      },
      "relation": "caused",
      "effect": {
        "span": "the university was being closed sine die"
      }
    }
  ]
}
```

### --- id=2971 ---

输入文本: IDUKKI / KOCHI : Kerala CPI(M) leader faces murder charge May 29 , 2012 00:00 IST The Communist Party of India ( Marxist ) in Kerala has suffered a major setback with the State police registering a case of murder against the party 's Idukki district secretary M.M. Mony for his sensational disclosure the other day that the CPI(M) eliminated its enemies during the 1980 s according to a list prepared for the purpose .

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
      "cause": "the State police registering a case of murder against the party 's Idukki district secretary M.M. Mony",
      "effect": "The Communist Party of India ( Marxist ) in Kerala has suffered a major setback"
    },
    {
      "cause": "his sensational disclosure the other day that the CPI(M) eliminated its enemies during the 1980 s according to a list prepared for the purpose",
      "effect": "the State police registering a case of murder against the party 's Idukki district secretary M.M. Mony"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "his sensational disclosure the other day that the CPI(M) eliminated its enemies during the 1980 s according to a list prepared for the purpose"
      },
      "relation": "caused",
      "effect": {
        "span": "the State police registering a case of murder against the party 's Idukki district secretary M.M. Mony"
      }
    }
  ]
}
```

### --- id=1697 ---

输入文本: Goldfields Limited would only reopen its number four shaft at the Beatrix mine in the Free State once it was assured of worker safety after two people were killed during a National Union of Mineworkers ( NUM ) meeting at the mine , Goldfields spokesman Willie Jacobsz said on Wednesday .

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
      "cause": "it was assured of worker safety",
      "effect": "Goldfields Limited would only reopen its number four shaft at the Beatrix mine in the Free State"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "two people were killed during a National Union of Mineworkers ( NUM ) meeting at the mine"
      },
      "relation": "caused",
      "effect": {
        "span": "Goldfields Limited would only reopen its number four shaft at the Beatrix mine in the Free State once it was assured of worker safety"
      }
    }
  ]
}
```

### --- id=2583 ---

输入文本: The R300 and N2 highways in Cape Town were reopened on Saturday afternoon following a brief protest , the Western Cape Traffic department said .

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
      "cause": "a brief protest",
      "effect": "The R300 and N2 highways in Cape Town were reopened on Saturday afternoon"
    }
  ],
  "pred_triples": []
}
```

### --- id=485 ---

输入文本: This membership drive issue spilled over to the streets as another group took on its rivals near Keshari Talkies .

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
      "cause": "another group took on its rivals near Keshari Talkies",
      "effect": "This membership drive issue spilled over to the streets"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "This membership drive issue"
      },
      "relation": "caused",
      "effect": {
        "span": "another group took on its rivals near Keshari Talkies"
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
      "cause": "which promised to allow toddy tapping before elections and reversed their decision after coming to power",
      "effect": "the peravai ’ s district president , K.G.N. Kanagarathinam , who led the protest , flayed the successive State governments"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the successive State governments which promised to allow toddy tapping before elections and reversed their decision after coming to power"
      },
      "relation": "caused",
      "effect": {
        "span": "K.G.N. Kanagarathinam , who led the protest , flayed"
      }
    }
  ]
}
```

### --- id=883 ---

输入文本: TDP legislator Devineni Umamaheswara Rao , former MP Gadde Ramamohan and city unit president B Venkanna alongwith other protesters staged demonstration at the bus station , stalling district bus services for about two hours .

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
        "span": "TDP legislator Devineni Umamaheswara Rao , former MP Gadde Ramamohan and city unit president B Venkanna alongwith other protesters staged demonstration at the bus station"
      },
      "relation": "caused",
      "effect": {
        "span": "stalling district bus services for about two hours"
      }
    }
  ]
}
```

### --- id=616 ---

输入文本: Taking a serious view of the violence , Haryana Chief Secretary P K Chaudhery had said a special investigating team has been formed under Assistant Commissioner of Police , Gurgaon , Ravinder Tomar , to investigate the matter .

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
      "cause": "to investigate the matter",
      "effect": "a special investigating team has been formed under Assistant Commissioner of Police , Gurgaon , Ravinder Tomar"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the violence"
      },
      "relation": "caused",
      "effect": {
        "span": "Haryana Chief Secretary P K Chaudhery had said a special investigating team has been formed under Assistant Commissioner of Police , Gurgaon , Ravinder Tomar , to investigate the matter"
      }
    },
    {
      "cause": {
        "span": "to investigate the matter"
      },
      "relation": "caused",
      "effect": {
        "span": "a special investigating team has been formed under Assistant Commissioner of Police , Gurgaon , Ravinder Tomar"
      }
    }
  ]
}
```

### --- id=1177 ---

输入文本: Violence broke out when DYFI members protested against a Youth Congress meeting being held at the junction .

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
      "cause": "DYFI members protested",
      "effect": "Violence broke out"
    },
    {
      "cause": "against a Youth Congress meeting being held at the junction",
      "effect": "DYFI members protested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "DYFI members protested against a Youth Congress meeting being held at the junction"
      },
      "relation": "caused",
      "effect": {
        "span": "Violence broke out"
      }
    }
  ]
}
```

### --- id=1979 ---

输入文本: The platinum miner has reportedly offered workers eight to nine percent increases , and warned that should the strike continue , it may be forced to cut jobs .

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
      "cause": "should the strike continue",
      "effect": "it may be forced to cut jobs"
    }
  ],
  "pred_triples": []
}
```

### --- id=2686 ---

输入文本: Speeches of Congress leaders who addressed a large gathering of party men made it abundantly clear that all major issues prominent in the political discourse of the State would be highlighted by the march visiting all constituencies in the State .

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
      "cause": "the march visiting all constituencies in the State",
      "effect": "all major issues prominent in the political discourse of the State would be highlighted"
    }
  ],
  "pred_triples": []
}
```

### --- id=1967 ---

输入文本: There was also allegation that some of the Congress workers , who came to interrupt the fest , were in an inebriated state .

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
      "cause": "were in an inebriated state",
      "effect": "some of the Congress workers , who came to interrupt the fest"
    }
  ],
  "pred_triples": []
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
    "tp": 2,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 3,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 2
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
        "span": "a flash strike by postgraduate , undergraduate and intern doctors"
      },
      "relation": "caused",
      "effect": {
        "span": "Medical services were affected at Gandhi General Hospital ( GGH ) here on Wednesday"
      }
    },
    {
      "cause": {
        "span": "demanding immediate suspension of the hospital superintendent and the resident medical officer-I ( RMO )"
      },
      "relation": "caused",
      "effect": {
        "span": "a flash strike by postgraduate , undergraduate and intern doctors"
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

### --- id=2013 ---

输入文本: Meanwhile , on Saturday morning , after learning about the incident , YSRC MLAs from the district rushed to Nagari and staged a protest outside the police station demanding the suspension of the Puttur DSP Krishna Kishore as he was acting as per the diktats of TDP leaders .

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
    "tp": 3,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "learning about the incident",
      "effect": "YSRC MLAs from the district rushed to Nagari and staged a protest outside the police station"
    },
    {
      "cause": "demanding the suspension of the Puttur DSP Krishna Kishore",
      "effect": "staged a protest outside the police station"
    },
    {
      "cause": "he was acting as per the diktats of TDP leaders",
      "effect": "demanding the suspension of the Puttur DSP Krishna Kishore"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "learning about the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "YSRC MLAs from the district rushed to Nagari and staged a protest outside the police station demanding the suspension of the Puttur DSP Krishna Kishore as he was acting as per the diktats of TDP leaders"
      }
    },
    {
      "cause": {
        "span": "demanding the suspension of the Puttur DSP Krishna Kishore as he was acting as per the diktats of TDP leaders"
      },
      "relation": "caused",
      "effect": {
        "span": "YSRC MLAs from the district rushed to Nagari and staged a protest outside the police station"
      }
    },
    {
      "cause": {
        "span": "he was acting as per the diktats of TDP leaders"
      },
      "relation": "caused",
      "effect": {
        "span": "demanding the suspension of the Puttur DSP Krishna Kishore"
      }
    }
  ]
}
```

### --- id=351 ---

输入文本: They allege that the attack , apparently triggered by an inter-caste marriage , was politically engineered .

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
        "span": "an inter-caste marriage"
      },
      "relation": "caused",
      "effect": {
        "span": "the attack"
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

### --- id=1430 ---

输入文本: In all , three persons who included two MRPS workers died in the incident due to burns .

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
      "cause": "burns",
      "effect": "three persons who included two MRPS workers died"
    },
    {
      "cause": "the incident",
      "effect": "three persons who included two MRPS workers died"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "burns"
      },
      "relation": "caused",
      "effect": {
        "span": "three persons who included two MRPS workers died in the incident"
      }
    }
  ]
}
```

### --- id=1888 ---

输入文本: DOMESTIC VIOLENCE - Indian Express Sun Aug 03 2008 , 12:04 hrs It has been a disturbing six months for India 's internal security : first the Naxal attacks in Orissa and the bomb blasts in Bangalore and Ahmedabad .

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
      "cause": "first the Naxal attacks in Orissa and the bomb blasts in Bangalore and Ahmedabad",
      "effect": "It has been a disturbing six months for India 's internal security"
    }
  ],
  "pred_triples": []
}
```

### --- id=870 ---

输入文本: The IEC in the Eastern Cape has overcome road blocks , intimidation and missing ballot papers for its 4165 voting stations to be running smoothly , it said on Wednesday .

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
      "cause": "its 4165 voting stations to be running smoothly",
      "effect": "The IEC in the Eastern Cape has overcome road blocks , intimidation and missing ballot papers"
    }
  ],
  "pred_triples": []
}
```

### --- id=308 ---

输入文本: Some police personnel intervened and urged them to give up their protest - but to no avail .

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
      "cause": "Some police personnel intervened",
      "effect": "urged them to give up their protest"
    }
  ],
  "pred_triples": []
}
```

### --- id=1805 ---

输入文本: The leader 's henchmen offered him a " settlement " but when he approached the state Lok Ayukta with a complaint of corruption , they attacked him and his wife .

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
        "span": "he approached the state Lok Ayukta with a complaint of corruption"
      },
      "relation": "caused",
      "effect": {
        "span": "they attacked him and his wife"
      }
    }
  ]
}
```

### --- id=1726 ---

输入文本: Even as the strike has entered its seventh day on Sunday , the medicos warned of intensifying their stir if the government continues to give them a cold shoulder .

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
      "cause": "the strike has entered its seventh day on Sunday",
      "effect": "the medicos warned of intensifying their stir if the government continues to give them a cold shoulder"
    },
    {
      "cause": "the government continues to give them a cold shoulder",
      "effect": "the medicos warned of intensifying their stir"
    }
  ],
  "pred_triples": []
}
```

### --- id=641 ---

输入文本: NALGONDA : The divisional level meeting convened to distribute pattas to beneficiaries under the fifth phase of the land distribution programme in Bhongir on Thursday was marred by protests , as Minister for Information Technology Komatireddy Venkat Reddy distributed pattas .

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
    "tp": 0,
    "fp": 1,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "protests",
      "effect": "The divisional level meeting convened to distribute pattas to beneficiaries under the fifth phase of the land distribution programme in Bhongir on Thursday was marred"
    },
    {
      "cause": "to distribute pattas to beneficiaries",
      "effect": "The divisional level meeting convened"
    },
    {
      "cause": "the fifth phase of the land distribution programme",
      "effect": "to distribute pattas to beneficiaries"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Minister for Information Technology Komatireddy Venkat Reddy distributed pattas"
      },
      "relation": "caused",
      "effect": {
        "span": "The divisional level meeting convened to distribute pattas to beneficiaries under the fifth phase of the land distribution programme in Bhongir on Thursday was marred by protests"
      }
    }
  ]
}
```

### --- id=2807 ---

输入文本: TAMIL NADU Strike hits work in many offices October 31 , 2007 00:00 IST MADURAI : Normal work was affected in many Central and State Government offices in Madurai as employees belonging to various unions struck work as part of the nationwide strike demanding interim relief .

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
      "cause": "employees belonging to various unions struck work",
      "effect": "Normal work was affected in many Central and State Government offices in Madurai"
    },
    {
      "cause": "demanding interim relief",
      "effect": "employees belonging to various unions struck work as part of the nationwide strike"
    },
    {
      "cause": "as part of the nationwide strike",
      "effect": "employees belonging to various unions struck work"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "employees belonging to various unions struck work"
      },
      "relation": "caused",
      "effect": {
        "span": "Normal work was affected in many Central and State Government offices in Madurai"
      }
    },
    {
      "cause": {
        "span": "demanding interim relief"
      },
      "relation": "caused",
      "effect": {
        "span": "employees belonging to various unions struck work"
      }
    }
  ]
}
```

### --- id=2696 ---

输入文本: " We had gone to study the life of people in remote and Naxal-affected tribal areas as part of our mission and did not expect to be kidnapped by the Naxals , though we fully knew about their presence , " they said .

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
      "cause": "our mission",
      "effect": "We had gone to study the life of people in remote and Naxal-affected tribal areas"
    }
  ],
  "pred_triples": []
}
```

### --- id=591 ---

输入文本: Modi , who has been accused of allowing communal polarisation of the state following the Sabarmati Express train burning incident at Godhra in and the riots that followed , has led the BJP to two massive victories in the 2002 and 2007 Assembly elections .

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
      "cause": "the Sabarmati Express train burning incident at Godhra in and the riots that followed",
      "effect": "Modi , who has been accused of allowing communal polarisation of the state"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Sabarmati Express train burning incident at Godhra"
      },
      "relation": "caused",
      "effect": {
        "span": "the riots that followed"
      }
    }
  ]
}
```

### --- id=1182 ---

输入文本: VISAKHAPATNAM Rallies , meetings mark May Day fete May 02 , 2017 00:00 IST Anti-labour policies of Centre , State government criticised Rallies and meetings marked May Day celebrations by various trade unions with focus on taking up a united fight against NDA Government ’ s alleged attempts to dilute labour welfare policies .

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
        "span": "against NDA Government 's alleged attempts to dilute labour welfare policies"
      },
      "relation": "caused",
      "effect": {
        "span": "Rallies and meetings marked May Day celebrations by various trade unions with focus on taking up a united fight"
      }
    }
  ]
}
```

### --- id=2336 ---

输入文本: This , according to Islamabad , will help in prosecuting the suspected masterminds of the 2008 terror strike in which 166 people were killed when 10 Pakistani terrorists sneaked into Mumbai and unleashed murder and mayhem with bombs and guns at multiple targets .

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
      "cause": "10 Pakistani terrorists sneaked into Mumbai and unleashed murder and mayhem with bombs and guns at multiple targets",
      "effect": "166 people were killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the 2008 terror strike"
      },
      "relation": "caused",
      "effect": {
        "span": "166 people were killed"
      }
    }
  ]
}
```

### --- id=505 ---

输入文本: Police and security forces immediately cordoned off the area to nab the militants responsible for the firing which triggered panic in the over-crowded area .

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
      "cause": "to nab the militants responsible for the firing",
      "effect": "Police and security forces immediately cordoned off the area"
    },
    {
      "cause": "Police and security forces immediately cordoned off the area",
      "effect": "which triggered panic in the over-crowded area"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to nab the militants responsible for the firing"
      },
      "relation": "caused",
      "effect": {
        "span": "Police and security forces immediately cordoned off the area"
      }
    },
    {
      "cause": {
        "span": "the firing"
      },
      "relation": "caused",
      "effect": {
        "span": "triggered panic in the over-crowded area"
      }
    }
  ]
}
```

### --- id=2932 ---

输入文本: Their proposed visit to Darasuram and Gangaikondacholapuram were cancelled following the incident Gnanaloka Thero has been staying in New Delhi for the last one-and-half years pursuing the diploma course .

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
      "cause": "the incident",
      "effect": "Their proposed visit to Darasuram and Gangaikondacholapuram were cancelled"
    },
    {
      "cause": "pursuing the diploma course",
      "effect": "Gnanaloka Thero has been staying in New Delhi for the last one-and-half years"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "Their proposed visit to Darasuram and Gangaikondacholapuram were cancelled"
      }
    }
  ]
}
```

### --- id=357 ---

输入文本: The university was closed following the disturbances , Vice-Chancellor Ngoato Takalo said on Monday .

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
        "span": "the disturbances"
      },
      "relation": "caused",
      "effect": {
        "span": "The university was closed"
      }
    }
  ]
}
```

### --- id=838 ---

输入文本: A day after lathicharge by local police on the agitating non-local students at the campus , the Union HRD Ministry rushed a three-member team -- Sanjeev Sharma , Director ( Technical Education ) in the ministry , Deputy Director Finance Fazal Mehmood and Chairman of Board of Governors of NIT M JZarabi -- here this morning .

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
        "span": "lathicharge by local police on the agitating non-local students at the campus"
      },
      "relation": "caused",
      "effect": {
        "span": "the Union HRD Ministry rushed a three-member team -- Sanjeev Sharma , Director ( Technical Education ) in the ministry , Deputy Director Finance Fazal Mehmood and Chairman of Board of Governors of NIT M JZarabi -- here this morning"
      }
    }
  ]
}
```

### --- id=206 ---

输入文本: VISAKHAPATNAM DCI employees go on mass casual leave , threaten to intensify stir

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
      "cause": "threaten to intensify stir",
      "effect": "DCI employees go on mass casual leave"
    }
  ],
  "pred_triples": []
}
```

### --- id=2057 ---

输入文本: Vehicles have also been used to commit attacks on civilians in Nice and Berlin .

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
      "cause": "to commit attacks on civilians in Nice and Berlin",
      "effect": "Vehicles have also been used"
    }
  ],
  "pred_triples": []
}
```

### --- id=412 ---

输入文本: He also sought punishments to MNS legislators who attacked Samajwadi Party ’ s MLA Abu Asim Azmi for taking oath in Hindi and not in Marathi in the Maharashtra Assembly .

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
      "cause": "taking oath in Hindi and not in Marathi in the Maharashtra Assembly",
      "effect": "MNS legislators who attacked Samajwadi Party ’ s MLA Abu Asim Azmi"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "MNS legislators who attacked Samajwadi Party ’ s MLA Abu Asim Azmi for taking oath in Hindi and not in Marathi in the Maharashtra Assembly"
      },
      "relation": "caused",
      "effect": {
        "span": "He also sought punishments to MNS legislators"
      }
    },
    {
      "cause": {
        "span": "taking oath in Hindi and not in Marathi in the Maharashtra Assembly"
      },
      "relation": "caused",
      "effect": {
        "span": "MNS legislators who attacked Samajwadi Party ’ s MLA Abu Asim Azmi"
      }
    }
  ]
}
```

### --- id=1867 ---

输入文本: Among these was the petition filed on behalf of Kersi Adajania who was convicted for helping to melt the AK -56 rifle which Mr. Dutt had stored in his house .

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
      "cause": "helping to melt the AK -56 rifle",
      "effect": "Kersi Adajania who was convicted"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "helping to melt the AK -56 rifle which Mr. Dutt had stored in his house"
      },
      "relation": "caused",
      "effect": {
        "span": "Kersi Adajania who was convicted"
      }
    }
  ]
}
```

### --- id=1066 ---

输入文本: Activists hold Earth ’ s funeral march 13th December 2009 04:26 AM BANGALORE : The Global Day of Action initiative gained support in Bangalore during a march conducted by Greenpeace in response to the uncertainity of the the UN Climate Change Conference in Copenhagen .

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
        "span": "the uncertainity of the the UN Climate Change Conference in Copenhagen"
      },
      "relation": "caused",
      "effect": {
        "span": "a march conducted by Greenpeace"
      }
    }
  ]
}
```

### --- id=2160 ---

输入文本: Something similar happened a few years ago in Shanghai , when retirees took to the streets , worried that if welfare funds were allocated to poor areas , their own retirement benefits would be slashed .

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
      "cause": "worried that if welfare funds were allocated to poor areas , their own retirement benefits would be slashed",
      "effect": "retirees took to the streets"
    },
    {
      "cause": "welfare funds were allocated to poor areas",
      "effect": "their own retirement benefits would be slashed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "worried that if welfare funds were allocated to poor areas , their own retirement benefits would be slashed"
      },
      "relation": "caused",
      "effect": {
        "span": "retirees took to the streets"
      }
    }
  ]
}
```

### --- id=2727 ---

输入文本: Residents , activists and opposition lawmakers have accused the government and police of colluding with the triads in an attempt to suppress protests , a charge vehemently denied by Hong Kong ’ s chief executive , Carrie Lam .

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
      "cause": "in an attempt to suppress protests",
      "effect": "the government and police of colluding with the triads"
    }
  ],
  "pred_triples": []
}
```

### --- id=1183 ---

输入文本: CITU took out a rally from Saraswati Park to LIC junction with placards and banners ridiculing anti-labour policies pursued by the Central and State Governments .

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
        "span": "ridiculing anti-labour policies pursued by the Central and State Governments"
      },
      "relation": "caused",
      "effect": {
        "span": "CITU took out a rally from Saraswati Park to LIC junction with placards and banners"
      }
    }
  ]
}
```

### --- id=1713 ---

输入文本: The petition came at a sensitive time , with the mainland in the midst of a massive crackdown on vice .

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
      "cause": "the mainland in the midst of a massive crackdown on vice",
      "effect": "The petition came at a sensitive time"
    }
  ],
  "pred_triples": []
}
```

### --- id=2519 ---

输入文本: Their ages range from 19 to 30 years , they were arrested in connection with incidents of public violence on campus , which included the continuous stoning of SA Police Service members , '' said police spokeswoman Brigadier Sally de Beer .

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
      "cause": "incidents of public violence on campus , which included the continuous stoning of SA Police Service members",
      "effect": "they were arrested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "incidents of public violence on campus"
      },
      "relation": "caused",
      "effect": {
        "span": "they were arrested in connection with incidents of public violence on campus"
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
      "cause": "how to deal with rising student debt",
      "effect": "the Student Representative Council and management clashed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Student Representative Council and management clashed over how to deal with rising student debt"
      },
      "relation": "caused",
      "effect": {
        "span": "This"
      }
    }
  ]
}
```

### --- id=1511 ---

输入文本: The bandh took a nasty turn in the afternoon when enforcers dragged passengers out of autos whose drivers had not joined the strike .

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
      "cause": "enforcers dragged passengers out of autos",
      "effect": "The bandh took a nasty turn in the afternoon"
    },
    {
      "cause": "drivers had not joined the strike",
      "effect": "enforcers dragged passengers out of autos"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "enforcers dragged passengers out of autos whose drivers had not joined the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "The bandh took a nasty turn in the afternoon"
      }
    }
  ]
}
```

### --- id=2374 ---

输入文本: 21st July 2013 09:56 AM The murder of Tamil Nadu BJP General Secretary V Ramesh invoked strong response from the national leadership on Saturday with the party top brass , including Leader of Opposition Sushma Swaraj and Gujarat Chief Minister Narendra Modi demanding that the state government initiate a thorough probe into the incident and take action against culprits .

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
      "cause": "The murder of Tamil Nadu BJP General Secretary V Ramesh",
      "effect": "strong response from the national leadership on Saturday"
    },
    {
      "cause": "The murder of Tamil Nadu BJP General Secretary V Ramesh invoked strong response from the national leadership on Saturday",
      "effect": "the party top brass , including Leader of Opposition Sushma Swaraj and Gujarat Chief Minister Narendra Modi demanding that the state government initiate a thorough probe into the incident and take action against culprits"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The murder of Tamil Nadu BJP General Secretary V Ramesh"
      },
      "relation": "caused",
      "effect": {
        "span": "invoked strong response from the national leadership on Saturday with the party top brass , including Leader of Opposition Sushma Swaraj and Gujarat Chief Minister Narendra Modi demanding that the state government initiate a thorough probe into the incident and take action against culprits"
      }
    },
    {
      "cause": {
        "span": "demanding that the state government initiate a thorough probe into the incident and take action against culprits"
      },
      "relation": "caused",
      "effect": {
        "span": "the party top brass , including Leader of Opposition Sushma Swaraj and Gujarat Chief Minister Narendra Modi"
      }
    }
  ]
}
```

### --- id=2233 ---

输入文本: Other explosions cut railway lines between the sprawling township and Johannesburg .

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
      "cause": "Other explosions",
      "effect": "cut railway lines between the sprawling township and Johannesburg"
    }
  ],
  "pred_triples": []
}
```

### --- id=478 ---

输入文本: 24th March 2016 05:23 AM THOOTHUKUDI : In recent days , particularly after the attack on Nadar Outfit leader , Subash Pannayar , police ‘ activism ’ in the form of torture has allegedly increased and the place that has been allegedly chosen for such torture is the shooting range on Vallanadu Hills .

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
      "cause": "the attack on Nadar Outfit leader , Subash Pannayar",
      "effect": "police ‘ activism ’ in the form of torture has allegedly increased"
    }
  ],
  "pred_triples": []
}
```

### --- id=679 ---

输入文本: The entire protest against the celebrations began with Mangal Pandey , joined by Rani Lakshmi Bai , Maulavi Ahmedullah Shah , Rao Sahib , Tantia Tope , Azimullah Khan , Kunwar Singh , Rajput chief of Jagadishpur , Firuz Saha , Pran Sukh Yadav and Rao Tula Ram of Rewari , who refused food and water against the leaders and people of India for letting down every single person who fought for freedom .

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
      "cause": "against the celebrations",
      "effect": "The entire protest"
    },
    {
      "cause": "for",
      "effect": "refused food and water against the leaders and people of India"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the celebrations"
      },
      "relation": "caused",
      "effect": {
        "span": "The entire protest began with Mangal Pandey , joined by Rani Lakshmi Bai , Maulavi Ahmedullah Shah , Rao Sahib , Tantia Tope , Azimullah Khan , Kunwar Singh , Rajput chief of Jagadishpur , Firuz Saha , Pran Sukh Yadav and Rao Tula Ram of Rewari"
      }
    },
    {
      "cause": {
        "span": "against the leaders and people of India for letting down every single person who fought for freedom"
      },
      "relation": "caused",
      "effect": {
        "span": "Mangal Pandey , joined by Rani Lakshmi Bai , Maulavi Ahmedullah Shah , Rao Sahib , Tantia Tope , Azimullah Khan , Kunwar Singh , Rajput chief of Jagadishpur , Firuz Saha , Pran Sukh Yadav and Rao Tula Ram of Rewari ... refused food and water"
      }
    }
  ]
}
```

### --- id=1497 ---

输入文本: Tshwane residents in townships including Atteridgeville , Soshanguve , Hammanskraal and Mamelodi , on Tuesday morning went on a frenzied rampage , torching vehicles , closing down streets and looting shops in protest against the imposition of an African National Congress ( ANC ) Mayoral Candidate .

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
      "cause": "against the imposition of an African National Congress ( ANC ) Mayoral Candidate",
      "effect": "Tshwane residents in townships including Atteridgeville , Soshanguve , Hammanskraal and Mamelodi , on Tuesday morning went on a frenzied rampage , torching vehicles , closing down streets and looting shops in protest"
    },
    {
      "cause": "in protest against the imposition of an African National Congress ( ANC ) Mayoral Candidate",
      "effect": "Tshwane residents in townships including Atteridgeville , Soshanguve , Hammanskraal and Mamelodi , on Tuesday morning went on a frenzied rampage , torching vehicles , closing down streets and looting shops"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the imposition of an African National Congress ( ANC ) Mayoral Candidate"
      },
      "relation": "caused",
      "effect": {
        "span": "Tshwane residents in townships including Atteridgeville , Soshanguve , Hammanskraal and Mamelodi , on Tuesday morning went on a frenzied rampage , torching vehicles , closing down streets and looting shops"
      }
    }
  ]
}
```

### --- id=2303 ---

输入文本: The protesters , during the gathering on Wednesday said they were not willing to listen to any government official and demanded that Ramaphosa come out to address them on how he is planning to stop the scourge of abuse directed at women and children in the country .

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
      "cause": "to address them on how he is planning to stop the scourge of abuse directed at women and children in the country",
      "effect": "demanded that Ramaphosa come out"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they were not willing to listen to any government official"
      },
      "relation": "caused",
      "effect": {
        "span": "demanded that Ramaphosa come out to address them on how he is planning to stop the scourge of abuse directed at women and children in the country"
      }
    }
  ]
}
```

### --- id=1992 ---

输入文本: Talks fail The indefinite strike will continue as the meeting convened by District Collector M. Beena to end the private bus strike failed to reach a consensus .

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
      "cause": "the meeting convened by District Collector M. Beena to end the private bus strike failed to reach a consensus",
      "effect": "The indefinite strike will continue"
    },
    {
      "cause": "to end the private bus strike",
      "effect": "the meeting convened by District Collector M. Beena"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the meeting convened by District Collector M. Beena to end the private bus strike failed to reach a consensus"
      },
      "relation": "caused",
      "effect": {
        "span": "The indefinite strike will continue"
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
        "span": "police firing"
      },
      "relation": "caused",
      "effect": {
        "span": "eight people were injured"
      }
    }
  ]
}
```

### --- id=1936 ---

输入文本: Cassim said that the DA had since laid a complaint at the South African Human Rights Commission ( SAHRC ) against one identified leader in the EFF structure , Omphile Seleke , who allegedly incited chaos and violence at the University of Pretoria ( Tuks ) campus in particular .

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
      "cause": "who allegedly incited chaos and violence at the University of Pretoria ( Tuks ) campus in particular",
      "effect": "the DA had since laid a complaint at the South African Human Rights Commission ( SAHRC ) against one identified leader in the EFF structure , Omphile Seleke"
    }
  ],
  "pred_triples": []
}
```

### --- id=158 ---

输入文本: Besides the bank and the insurance company employees , medical and sales representatives , members of the UTF , anganwadi , municipal and construction workers , hamalis , including the RTC porters , participated in the rally taken out under the banner of the leftist unions protesting against the ‘ anti-employee ’ and ‘ anti-national ’ policies of the Congress-led UPA government .

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
        "span": "protesting against the ‘ anti-employee ’ and ‘ anti-national ’ policies of the Congress-led UPA government"
      },
      "relation": "caused",
      "effect": {
        "span": "Besides the bank and the insurance company employees , medical and sales representatives , members of the UTF , anganwadi , municipal and construction workers , hamalis , including the RTC porters , participated in the rally taken out under the banner of the leftist unions"
      }
    }
  ]
}
```

### --- id=601 ---

输入文本: PUBLISHED : Wednesday , 25 June , 2014 , 8:11pm Seven detained after arson attack kills Shandong villager in latest China land dispute violence

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
      "cause": "arson attack kills Shandong villager in latest China land dispute violence",
      "effect": "Seven detained"
    },
    {
      "cause": "arson attack",
      "effect": "kills Shandong villager"
    }
  ],
  "pred_triples": []
}
```

### --- id=1535 ---

输入文本: RFEA chief executive Nico Badenhorst said the strike was costing the country R100 million a day .

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
      "cause": "the strike",
      "effect": "costing the country R100 million a day"
    }
  ],
  "pred_triples": []
}
```

### --- id=2514 ---

输入文本: He said there was an " ulterior motive " in Karunanidhi ’ s comments , made during an election speech in Puducherry on Thursday , that riots ensued following the demolition of the mosque .

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
      "cause": "the demolition of the mosque",
      "effect": "riots ensued"
    }
  ],
  "pred_triples": []
}
```

### --- id=161 ---

输入文本: Secretary of the Insurance Corporation Employees ’ Union , Nellore Division , K. Gopalakrishnaiah and other leaders , who held a demonstration in front of the United India Insurance Company here , criticised the UPA that had categorically said it would strengthen the LIC and GICs but was doing just the opposite by hiking the cap on the Foreign Direct Investment in the insurance sector .

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
        "span": "the UPA that had categorically said it would strengthen the LIC and GICs but was doing just the opposite by hiking the cap on the Foreign Direct Investment in the insurance sector"
      },
      "relation": "caused",
      "effect": {
        "span": "Secretary of the Insurance Corporation Employees ’ Union , Nellore Division , K. Gopalakrishnaiah and other leaders , who held a demonstration in front of the United India Insurance Company here , criticised"
      }
    }
  ]
}
```

### --- id=2859 ---

输入文本: The brief trip of 62 - year-old Ashraf to the 13th century shrine hit a sour note following a boycott by the Dargahs spiritual head in protest against the recent brutal killing and beheading of Indian soldiers by the Pakistani Army .

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
      "cause": "a boycott by the Dargahs spiritual head",
      "effect": "The brief trip of 62 - year-old Ashraf to the 13th century shrine hit a sour note"
    },
    {
      "cause": "in protest",
      "effect": "a boycott by the Dargahs spiritual head"
    },
    {
      "cause": "against the recent brutal killing and beheading of Indian soldiers by the Pakistani Army",
      "effect": "in protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the recent brutal killing and beheading of Indian soldiers by the Pakistani Army"
      },
      "relation": "caused",
      "effect": {
        "span": "a boycott by the Dargahs spiritual head"
      }
    },
    {
      "cause": {
        "span": "a boycott by the Dargahs spiritual head in protest against the recent brutal killing and beheading of Indian soldiers by the Pakistani Army"
      },
      "relation": "caused",
      "effect": {
        "span": "The brief trip of 62 - year-old Ashraf to the 13th century shrine hit a sour note"
      }
    }
  ]
}
```

### --- id=953 ---

输入文本: Lok Sabha members , cutting across party lines , meanwhile , expressed outrage at the language used by members of Team Anna during Anna ’ s one-day sit-in fast at Jantar Mantar .

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
        "span": "the language used by members of Team Anna during Anna ’ s one-day sit-in fast at Jantar Mantar"
      },
      "relation": "caused",
      "effect": {
        "span": "Lok Sabha members , cutting across party lines , meanwhile , expressed outrage"
      }
    }
  ]
}
```

### --- id=2480 ---

输入文本: The earlier reports of rivalry among nursing homes resulting in the explosion , have now been ruled out .

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
      "cause": "rivalry among nursing homes",
      "effect": "resulting in the explosion"
    }
  ],
  "pred_triples": []
}
```

### --- id=2941 ---

输入文本: Batla House shootout : Shahzad Ahmed convicted for cop 's murder 25th July 2013 03:24 PM Lone suspected Indian Mujahideen operative Shahzad Ahmad was on Thursday convicted in the 2008 Batla House encounter case by a Delhi court for murdering a police inspector and assaulting other officers .

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
      "cause": "cop 's murder",
      "effect": "Shahzad Ahmed convicted"
    },
    {
      "cause": "murdering a police inspector and assaulting other officers",
      "effect": "Lone suspected Indian Mujahideen operative Shahzad Ahmad was on Thursday convicted in the 2008 Batla House encounter case by a Delhi court"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "murdering a police inspector and assaulting other officers"
      },
      "relation": "caused",
      "effect": {
        "span": "Lone suspected Indian Mujahideen operative Shahzad Ahmad was on Thursday convicted in the 2008 Batla House encounter case by a Delhi court"
      }
    }
  ]
}
```

### --- id=1190 ---

输入文本: As part of the strike , the medicos who are not getting their stipend for the past four months , have also boycotted emergency services .

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
      "cause": "As part of the strike , the medicos who are not getting their stipend for the past four months",
      "effect": "have also boycotted emergency services"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "the medicos who are not getting their stipend for the past four months , have also boycotted emergency services"
      }
    }
  ]
}
```

### --- id=2835 ---

输入文本: The workers forced the manager of Deepak Cinema , a down grade cinema hall , at Parel here to stall the film ’ s screening .

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
        "span": "The workers forced the manager of Deepak Cinema , a down grade cinema hall , at Parel here"
      },
      "relation": "caused",
      "effect": {
        "span": "to stall the film ’ s screening"
      }
    }
  ]
}
```

### --- id=741 ---

输入文本: CHENNAI : Give free hand to police : Karunanidhi September 27 , 2016 00:00 IST DMK leader M. Karunanidhi on Monday alleged that violence broke out in Coimbatore and Tirupur districts following the murder of Hindu Munnani spokesperson C. Sasikumar because the police was not given a free hand to deal with the situation .

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
      "cause": "the police was not given a free hand to deal with the situation",
      "effect": "violence broke out in Coimbatore and Tirupur districts following the murder of Hindu Munnani spokesperson C. Sasikumar"
    },
    {
      "cause": "the murder of Hindu Munnani spokesperson C. Sasikumar",
      "effect": "violence broke out in Coimbatore and Tirupur districts"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the murder of Hindu Munnani spokesperson C. Sasikumar"
      },
      "relation": "caused",
      "effect": {
        "span": "violence broke out in Coimbatore and Tirupur districts"
      }
    },
    {
      "cause": {
        "span": "the police was not given a free hand to deal with the situation"
      },
      "relation": "caused",
      "effect": {
        "span": "violence broke out in Coimbatore and Tirupur districts"
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

### --- id=570 ---

输入文本: B. Rajeswari Sunday died of burn injuries at a corporate hospital , where she was undergoing treatment after she set herself ablaze four days ago .

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
      "cause": "burn injuries",
      "effect": "B. Rajeswari Sunday died"
    },
    {
      "cause": "she set herself ablaze four days ago",
      "effect": "burn injuries"
    },
    {
      "cause": "she set herself ablaze four days ago",
      "effect": "she was undergoing treatment"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "she set herself ablaze four days ago"
      },
      "relation": "caused",
      "effect": {
        "span": "B. Rajeswari Sunday died of burn injuries at a corporate hospital , where she was undergoing treatment"
      }
    }
  ]
}
```

### --- id=2956 ---

输入文本: This hints at possible differences in the organisation that backed the villagers protesting the proposed project about six years ago .

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
        "span": "the proposed project"
      },
      "relation": "caused",
      "effect": {
        "span": "the villagers protesting"
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
        "span": "the Sena's recent attack on railway recruitment candidates at Kalyan station"
      },
      "relation": "caused",
      "effect": {
        "span": "groups of 100 -200 migrants have been meeting at various locations , to voice their disbelief , disquiet and make plans"
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

### --- id=984 ---

输入文本: He is facing charges of violating a court order , public violence , assault , theft , and damage to property during the 2016 protest against `` colonised '' tertiary education .

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
      "cause": "the 2016 protest",
      "effect": "He is facing charges of violating a court order , public violence , assault , theft , and damage to property"
    },
    {
      "cause": "violating a court order , public violence , assault , theft , and damage to property",
      "effect": "He is facing charges"
    },
    {
      "cause": "against `` colonised '' tertiary education",
      "effect": "the 2016 protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "violating a court order , public violence , assault , theft , and damage to property during the 2016 protest against `` colonised '' tertiary education"
      },
      "relation": "caused",
      "effect": {
        "span": "He is facing charges"
      }
    }
  ]
}
```

### --- id=152 ---

输入文本: An integrated steel plant , agriculture and mineral-based industries should be set up in Kadapa district for ensuring its comprehensive development and generate employment , CPI(M) district secretary B. Narayana demanded while addressing party functionaries who staged dharna in front of Kadapa Collectorate on Thursday .

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
      "cause": "ensuring its comprehensive development",
      "effect": "An integrated steel plant , agriculture and mineral-based industries should be set up in Kadapa district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "for ensuring its comprehensive development and generate employment"
      },
      "relation": "caused",
      "effect": {
        "span": "An integrated steel plant , agriculture and mineral-based industries should be set up in Kadapa district"
      }
    }
  ]
}
```

### --- id=2660 ---

输入文本: The wordy duel soon turned violent with Congress workers pushing and pulling Ms. Rajakumari .

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
        "span": "the wordy duel"
      },
      "relation": "caused",
      "effect": {
        "span": "soon turned violent with Congress workers pushing and pulling Ms. Rajakumari"
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
      "cause": "in connection with the murder and eight others turned themselves in",
      "effect": "the police arrested six persons"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in connection with the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "the police arrested six persons"
      }
    }
  ]
}
```

### --- id=319 ---

输入文本: Table grape harvesters started protesting about their working conditions in De Doorns last month .

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
        "span": "about their working conditions"
      },
      "relation": "caused",
      "effect": {
        "span": "Table grape harvesters started protesting in De Doorns last month"
      }
    }
  ]
}
```

### --- id=2866 ---

输入文本: Shankar died in the attack while Kausalya escaped with severe injuries .

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
        "span": "the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Shankar died"
      }
    },
    {
      "cause": {
        "span": "the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Kausalya escaped with severe injuries"
      }
    }
  ]
}
```

### --- id=3014 ---

输入文本: When quizzed about the alleged police intimidation most of those who submitted claimed off-record that they had been individually helped by the police during riots and that yesterday , some officers did call them up and ask them to depose in their favour .

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
      "cause": "quizzed about the alleged police intimidation",
      "effect": "most of those who submitted claimed off-record that they had been individually helped by the police during riots and that yesterday , some officers did call them up and ask them to depose in their favour"
    },
    {
      "cause": "and ask them to depose in their favour",
      "effect": "some officers did call them up"
    }
  ],
  "pred_triples": []
}
```

### --- id=1391 ---

输入文本: Leaders of both the organisations including the President of the KPKCS Bhimshetty Yempalli and Secretaryof the KPRS Gouramma Patil staged a dharna outside the Vikas Soudha , housing all the government offices in Gulbarga city on Friday demanding the regularisation of the unauthorised cultivation which would help tens of thousands of landless agricultural labourers as a one-time measure .

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
      "cause": "demanding the regularisation of the unauthorised cultivation",
      "effect": "Leaders of both the organisations including the President of the KPKCS Bhimshetty Yempalli and Secretaryof the KPRS Gouramma Patil staged a dharna outside the Vikas Soudha , housing all the government offices in Gulbarga city on Friday"
    },
    {
      "cause": "the regularisation of the unauthorised cultivation",
      "effect": "which would help tens of thousands of landless agricultural labourers as a one-time measure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding the regularisation of the unauthorised cultivation which would help tens of thousands of landless agricultural labourers as a one-time measure"
      },
      "relation": "caused",
      "effect": {
        "span": "Leaders of both the organisations including the President of the KPKCS Bhimshetty Yempalli and Secretaryof the KPRS Gouramma Patil staged a dharna outside the Vikas Soudha , housing all the government offices in Gulbarga city on Friday"
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
      "cause": "having implicated Sen in a false case",
      "effect": "Speakers at the rally , orgainsed by the Peoples Union for Civil Liberties ( PUCL ) , CPI , CPM , and Chhattisgarh Mukti Morcha ( CMM ) , accused the Raman Singh government of"
    }
  ],
  "pred_triples": []
}
```

### --- id=576 ---

输入文本: ( Photo : Reuters ) MUMBAI ( Reuters ): State-run banks remained shut on Friday as a nationwide strike by their employees demanding higher wages and pensions entered the second day , hurting volumes in the currency and bond markets .

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
    "tp": 2,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "a nationwide strike by their employees",
      "effect": "State-run banks remained shut on Friday"
    },
    {
      "cause": "demanding higher wages and pensions",
      "effect": "a nationwide strike by their employees"
    },
    {
      "cause": "State-run banks remained shut on Friday",
      "effect": "hurting volumes in the currency and bond markets"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding higher wages and pensions"
      },
      "relation": "caused",
      "effect": {
        "span": "a nationwide strike by their employees"
      }
    },
    {
      "cause": {
        "span": "a nationwide strike by their employees demanding higher wages and pensions entered the second day"
      },
      "relation": "caused",
      "effect": {
        "span": "State-run banks remained shut on Friday"
      }
    },
    {
      "cause": {
        "span": "a nationwide strike by their employees demanding higher wages and pensions entered the second day"
      },
      "relation": "caused",
      "effect": {
        "span": "hurting volumes in the currency and bond markets"
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
        "span": "the Union Minister said the HRD team will stay at NIT Srinagar till exams , which begin on April 11 , are not over"
      }
    },
    {
      "cause": {
        "span": "exams are due"
      },
      "relation": "caused",
      "effect": {
        "span": "the agitation will have a bearing on their academic performance"
      }
    }
  ]
}
```

### --- id=917 ---

输入文本: `` This was part of their lobbying campaign to be appointed into permanent part-time positions , '' SAPO said at the time .

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
        "span": "to be appointed into permanent part-time positions"
      },
      "relation": "caused",
      "effect": {
        "span": "This was part of their lobbying campaign"
      }
    }
  ]
}
```

### --- id=120 ---

输入文本: `` I observed the attack on the police , I have no doubt about it , '' Modiba said during cross-examination .

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
      "cause": "I observed the attack on the police",
      "effect": "I have no doubt about it"
    }
  ],
  "pred_triples": []
}
```

### --- id=828 ---

输入文本: “ Chen has gone in the opposite direction with these military parades which are quite remarkable really … We saw similar-type events after the 2009 riots but here we are talking about in response to what was really a small knife attack in Hotan .

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
        "span": "what was really a small knife attack in Hotan"
      },
      "relation": "caused",
      "effect": {
        "span": "these military parades which are quite remarkable really"
      }
    }
  ]
}
```

### --- id=682 ---

输入文本: 19th July 2013 12:22 PM Protests rocked several areas of Jammu division today to protest the firing incident in Ramban where curfew remained in force even as authorities stopped a fresh batch of Amarnath pilgrims from leaving for the shrine .

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
      "cause": "to protest the firing incident in Ramban",
      "effect": "Protests rocked several areas of Jammu division today"
    },
    {
      "cause": "authorities stopped a fresh batch of Amarnath pilgrims from leaving for the shrine",
      "effect": "curfew remained in force"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest the firing incident in Ramban"
      },
      "relation": "caused",
      "effect": {
        "span": "Protests rocked several areas of Jammu division today"
      }
    }
  ]
}
```

### --- id=583 ---

输入文本: Stiff Protest Against Ulfa for Targeting Hindi-speakers

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
      "cause": "Targeting Hindi-speakers",
      "effect": "Stiff Protest Against Ulfa"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Ulfa for Targeting Hindi-speakers"
      },
      "relation": "caused",
      "effect": {
        "span": "Stiff Protest Against Ulfa"
      }
    }
  ]
}
```

### --- id=2704 ---

输入文本: Within hours of the Chinese government making it clear that the people of Hong Kong will not have a free choice when they vote to elect the territory ’ s next chief executive , Hong Kong police had made their first arrests of demonstrators protesting against that decision .

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
      "cause": "the Chinese government making it clear that the people of Hong Kong will not have a free choice when they vote to elect the territory ’ s next chief executive",
      "effect": "Hong Kong police had made their first arrests of demonstrators protesting against that decision"
    },
    {
      "cause": "the people of Hong Kong will not have a free choice when they vote to elect the territory ’ s next chief executive",
      "effect": "demonstrators protesting against that decision"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Chinese government making it clear that the people of Hong Kong will not have a free choice when they vote to elect the territory ’ s next chief executive"
      },
      "relation": "caused",
      "effect": {
        "span": "Hong Kong police had made their first arrests of demonstrators protesting against that decision"
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
        "span": "The protests , which began"
      }
    }
  ]
}
```

### --- id=2558 ---

输入文本: Jagan had taken up the hunger strike on Sunday morning in support of ‘ Samaikyandra ’ agitation in Coastal Andhra and Rayalaseema regions , which is going on for the last 27 days .

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
      "cause": "in support of ‘ Samaikyandra ’ agitation in Coastal Andhra and Rayalaseema regions , which is going on for the last 27 days",
      "effect": "Jagan had taken up the hunger strike on Sunday morning"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in support of ‘ Samaikyandra ’ agitation in Coastal Andhra and Rayalaseema regions"
      },
      "relation": "caused",
      "effect": {
        "span": "Jagan had taken up the hunger strike on Sunday morning"
      }
    }
  ]
}
```

### --- id=2173 ---

输入文本: New Year celebrations fail to affect protests 01st January 2013 09:11 AM Even as the city geared up for new year celebrations , there remained a big section of people who refused to lose focus and take the pressure off the government demanding stricter rules for sexual offenders .

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
      "cause": "the city geared up for new year celebrations",
      "effect": "there remained a big section of people who refused to lose focus and take the pressure off the government demanding stricter rules for sexual offenders"
    },
    {
      "cause": "demanding stricter rules for sexual offenders",
      "effect": "there remained a big section of people who refused to lose focus and take the pressure off the government"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding stricter rules for sexual offenders"
      },
      "relation": "caused",
      "effect": {
        "span": "there remained a big section of people who refused to lose focus and take the pressure off the government"
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
      "cause": "they didn ’ t have a well thought out strategy",
      "effect": "The umbrella movement protests did not achieve “ what the demonstrators wanted"
    }
  ],
  "pred_triples": []
}
```

### --- id=2787 ---

输入文本: ANA Reporter JOHANNESBURG , 10 April ( ANA ) - Emfuleni Local Municipality in Gauteng has said that it regrets the loss of life following incidents of violence in Rus-ter-vaal earlier on Wednesday morning in which two people died in alleged clashes between security agency the Red Ants and land invaders in the area .

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
      "cause": "incidents of violence in Rus-ter-vaal earlier on Wednesday morning",
      "effect": "the loss of life"
    },
    {
      "cause": "alleged clashes between security agency the Red Ants and land invaders in the area",
      "effect": "two people died"
    }
  ],
  "pred_triples": []
}
```

### --- id=921 ---

输入文本: Protest against proposed Jaitapur nuke power plant

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
      "cause": "against proposed Jaitapur nuke power plant",
      "effect": "Protest"
    }
  ],
  "pred_triples": []
}
```

### --- id=550 ---

输入文本: Four Fisheries Control and Parks officers were taken hostage after 15 armed poachers ambushed them at Hout Bay , SABC radio news reported on Wednesday .

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
        "span": "15 armed poachers ambushed them at Hout Bay"
      },
      "relation": "caused",
      "effect": {
        "span": "Four Fisheries Control and Parks officers were taken hostage"
      }
    }
  ]
}
```

### --- id=567 ---

输入文本: Earlier , Sikhs began gathering at the Takht premises as early as 9 am and heads of various organisations met the Takht jathedars , demanding " severe action " against the Dera chief .

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
      "cause": "against the Dera chief",
      "effect": "Earlier , Sikhs began gathering at the Takht premises as early as 9 am and heads of various organisations met the Takht jathedars , demanding \" severe action \""
    },
    {
      "cause": "demanding \" severe action \" against the Dera chief",
      "effect": "Earlier , Sikhs began gathering at the Takht premises as early as 9 am and heads of various organisations met the Takht jathedars"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding \" severe action \" against the Dera chief"
      },
      "relation": "caused",
      "effect": {
        "span": "Sikhs began gathering at the Takht premises as early as 9 am and heads of various organisations met the Takht jathedars"
      }
    }
  ]
}
```

### --- id=827 ---

输入文本: China says Islamic extremists and separatists are behind such attacks although human rights activists suspect much of the violence is driven by resentment at Communist party rule among the region ’ s predominantly Muslim ethnic Uighur population .

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
      "cause": "human rights activists suspect much of the violence is driven by resentment at Communist party rule among the region ’ s predominantly Muslim ethnic Uighur population",
      "effect": "China says Islamic extremists and separatists are behind such attacks"
    },
    {
      "cause": "resentment at Communist party rule among the region ’ s predominantly Muslim ethnic Uighur population",
      "effect": "much of the violence"
    }
  ],
  "pred_triples": []
}
```

### --- id=1049 ---

输入文本: There would have been no West Bengal as the entire state would have become part of East Pakistan ( present-day Bangladesh ) . ” Addressing the gathering , the state BJP leaders asked the party workers “ not to get provoked by the TMC goons but to strengthen the organisation as the party ’ s goal was to capture power in the state in the 2016 Assembly elections ” .

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
        "span": "the party 's goal was to capture power in the state in the 2016 Assembly elections"
      },
      "relation": "caused",
      "effect": {
        "span": "the state BJP leaders asked the party workers “ not to get provoked by the TMC goons but to strengthen the organisation"
      }
    }
  ]
}
```

### --- id=474 ---

输入文本: Protests erupted and Home Minister Jani Reddy declared there would be no more   encounters   .

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
        "span": "Protests erupted"
      },
      "relation": "caused",
      "effect": {
        "span": "Home Minister Jani Reddy declared there would be no more ' encounters '"
      }
    }
  ]
}
```

### --- id=57 ---

输入文本: CHENNAI : Chennai sees its first ever hunger fast against HCL April 08 , 2013 00:00 IST For the first time in Chennai , graduates denied jobs by a multi-national corporation who had recruited them from their college campuses , staged a hunger strike on Sunday .

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
        "span": "graduates denied jobs by a multi-national corporation who had recruited them from their college campuses"
      },
      "relation": "caused",
      "effect": {
        "span": "staged a hunger strike on Sunday"
      }
    }
  ]
}
```

### --- id=2796 ---

输入文本: The PLGA week coincides with the 48 - hour bandh call by the Maoists protesting the killing of Kishenji .

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
        "span": "protesting the killing of Kishenji"
      },
      "relation": "caused",
      "effect": {
        "span": "the 48 - hour bandh call by the Maoists"
      }
    }
  ]
}
```

### --- id=904 ---

输入文本: Dr Joshi said , “ The protest was to make the government realise the hazards of allowing stone crushers to function in an agriculturally rich area .

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
      "cause": "to make the government realise the hazards of allowing stone crushers to function in an agriculturally rich area",
      "effect": "The protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to make the government realise the hazards of allowing stone crushers to function in an agriculturally rich area"
      },
      "relation": "caused",
      "effect": {
        "span": "The protest was"
      }
    }
  ]
}
```

### --- id=1614 ---

输入文本: SC curbs on NIA questioning Sadhvi Pragya 09th July 2012 09:26 PM The Supreme Court Monday restrained the National Investigation Agency from interrogating Sadhvi Pragya Singh Thakur in connection with the 2007 murder of Rashtriya Swayamsewak Sangh activist Sunil Joshi in Madhya Pradesh .

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
        "span": "in connection with the 2007 murder of Rashtriya Swayamsewak Sangh activist Sunil Joshi in Madhya Pradesh"
      },
      "relation": "caused",
      "effect": {
        "span": "The Supreme Court Monday restrained the National Investigation Agency from interrogating Sadhvi Pragya Singh Thakur"
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
      "cause": "The municipality witnessed protests by residents in Boitumelong in the beginning of April",
      "effect": "a number of houses , including a councillor 's , were burnt down"
    }
  ],
  "pred_triples": []
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
        "span": "the withdrawal of a bill that would allow extraditions to the Chinese mainland"
      },
      "relation": "caused",
      "effect": {
        "span": "protesters have demanded"
      }
    }
  ]
}
```

### --- id=2638 ---

输入文本: The two Lashkar-e-Toiba militants drove up to the Central Reserve Police Force ( CRPF ) camp on Monday evening and forced their way in by lobbing a grenade at the gate .

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
      "cause": "lobbing a grenade at the gate",
      "effect": "forced their way in"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "lobbing a grenade at the gate"
      },
      "relation": "caused",
      "effect": {
        "span": "The two Lashkar-e-Toiba militants drove up to the Central Reserve Police Force ( CRPF ) camp on Monday evening and forced their way in"
      }
    }
  ]
}
```

### --- id=1193 ---

输入文本: May 31 , 2014 00:00 IST KSRP deployed to stop protest

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
      "cause": "to stop protest",
      "effect": "KSRP deployed"
    }
  ],
  "pred_triples": []
}
```

### --- id=2781 ---

输入文本: In another attack in 2009 , ultra ’ s quick action group killed Cahnnu Karma , his close relative .

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
        "span": "ultra 's quick action group killed Cahnnu Karma , his close relative"
      },
      "relation": "caused",
      "effect": {
        "span": "In another attack in 2009"
      }
    }
  ]
}
```

### --- id=1825 ---

输入文本: After triggering the blasts in a public place , the ULFA is in a denial mode , fearing public outcry against it , ” he said .

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
      "cause": "triggering the blasts in a public place",
      "effect": "the ULFA is in a denial mode , fearing public outcry against it"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "triggering the blasts in a public place"
      },
      "relation": "caused",
      "effect": {
        "span": "the ULFA is in a denial mode"
      }
    },
    {
      "cause": {
        "span": "fearing public outcry against it"
      },
      "relation": "caused",
      "effect": {
        "span": "the ULFA is in a denial mode"
      }
    }
  ]
}
```

### --- id=530 ---

输入文本: It is neccessary to take up the agitation at a local level and hence , we will hold rally at Hadapsar instead of coming all the way to Shivajinagar , " he said adding a few groups are outside Collector office supporting Hazare 's stir .

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
      "cause": "It is neccessary to take up the agitation at a local level",
      "effect": "we will hold rally at Hadapsar instead of coming all the way to Shivajinagar"
    },
    {
      "cause": "supporting Hazare 's stir",
      "effect": "a few groups are outside Collector office"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "It is neccessary to take up the agitation at a local level"
      },
      "relation": "caused",
      "effect": {
        "span": "we will hold rally at Hadapsar instead of coming all the way to Shivajinagar"
      }
    }
  ]
}
```

### --- id=1889 ---

输入文本: civilians and security forces killed in Naxals attacks in 2008 .

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
        "span": "Naxals attacks in 2008"
      },
      "relation": "caused",
      "effect": {
        "span": "civilians and security forces killed"
      }
    }
  ]
}
```

### --- id=1170 ---

输入文本: Shops and business establishments , educational institutions , banks and private offices remained closed in Morigaon district and parts of Nagaon and Kamrup ( East ) districts in response to the bandh from 5 AM called by the All Tiwa Students Union ( ATSU ) and three other organisations in support of their demands .

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
      "cause": "the bandh from 5 AM called by the All Tiwa Students Union ( ATSU ) and three other organisations",
      "effect": "Shops and business establishments , educational institutions , banks and private offices remained closed in Morigaon district and parts of Nagaon and Kamrup ( East ) districts"
    },
    {
      "cause": "their demands",
      "effect": "the bandh from 5 AM called by the All Tiwa Students Union ( ATSU ) and three other organisations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in response to the bandh from 5 AM called by the All Tiwa Students Union ( ATSU ) and three other organisations in support of their demands"
      },
      "relation": "caused",
      "effect": {
        "span": "Shops and business establishments , educational institutions , banks and private offices remained closed in Morigaon district and parts of Nagaon and Kamrup ( East ) districts"
      }
    }
  ]
}
```

### --- id=2426 ---

输入文本: March 15 , 2016 00:00 IST Union Public Service Commission ( UPSC ) aspirants staged a protest near Parliament House on Monday demanding compensation in the form of additional attempts , which they say they lost due to a discriminatory Civil Services Aptitude Test ( CSAT ) paper during the preliminary examination .

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
      "cause": "demanding compensation in the form of additional attempts",
      "effect": "Union Public Service Commission ( UPSC ) aspirants staged a protest near Parliament House on Monday"
    },
    {
      "cause": "a discriminatory Civil Services Aptitude Test ( CSAT ) paper during the preliminary examination",
      "effect": "they lost"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding compensation in the form of additional attempts"
      },
      "relation": "caused",
      "effect": {
        "span": "Union Public Service Commission ( UPSC ) aspirants staged a protest near Parliament House on Monday"
      }
    },
    {
      "cause": {
        "span": "a discriminatory Civil Services Aptitude Test ( CSAT ) paper during the preliminary examination"
      },
      "relation": "caused",
      "effect": {
        "span": "they lost additional attempts"
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
        "span": "staging protests on the highway despite police not giving permission for the same"
      },
      "relation": "caused",
      "effect": {
        "span": "JAC convenor M. Kodandaram , Telangana Rashtra Samithi ( TRS ) legislators K. Tarakarama Rao , E. Rajender and Harishwar Reddy were among dozens of leaders arrested by the police"
      }
    }
  ]
}
```

### --- id=1879 ---

输入文本: Partial in Singareni The Telangana NGOs State associate president , M. Sudhakar , who took part in the protest at the Collectorate , said the fears being expressed by employees and workers owed mainly to the moves of the government .

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
      "cause": "the moves of the government",
      "effect": "the fears being expressed by employees and workers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the moves of the government"
      },
      "relation": "caused",
      "effect": {
        "span": "the fears being expressed by employees and workers owed mainly to the moves of the government"
      }
    }
  ]
}
```

### --- id=2518 ---

输入文本: Some locals gheraoed the policemen , when they were in the village for investigation , demanding immediate arrest of the culprits .

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
      "cause": "demanding immediate arrest of the culprits",
      "effect": "Some locals gheraoed the policemen , when they were in the village for investigation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding immediate arrest of the culprits"
      },
      "relation": "caused",
      "effect": {
        "span": "Some locals gheraoed the policemen"
      }
    }
  ]
}
```

### --- id=2427 ---

输入文本: NEW DELHI : UPSC aspirants stage protest , detained

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
      "cause": "UPSC aspirants stage protest",
      "effect": "detained"
    }
  ],
  "pred_triples": []
}
```
