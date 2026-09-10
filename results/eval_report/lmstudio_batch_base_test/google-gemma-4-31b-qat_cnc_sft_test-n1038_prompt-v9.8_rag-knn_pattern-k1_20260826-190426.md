# Gemma 4 31B QAT CNC fixed test eval report

## 配置
```json
{
  "label": "Gemma 4 31B QAT CNC fixed test",
  "model": "google/gemma-4-31b-qat",
  "dataset": "cnc_sft_test",
  "sample_count": 1038,
  "prompt_name": "v9.8",
  "use_rag": true,
  "rag_mode": "knn_pattern",
  "rag_top_k": 1,
  "temperature": 0.0,
  "max_tokens": 2048,
  "output_schema": "standard",
  "primary_metric": "anchor_window",
  "progress_every": 100,
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
  "metadata_path": "D:\\Master thesis\\RAG Database\\cnc_examples.jsonl",
  "embeddings_path": "D:\\Master thesis\\RAG Database\\cnc_embeddings.npy"
}
```

## 统计指标
```text
================ Gemma 4 31B QAT CNC fixed test final report ================
样本总数: 1038
  Gold 含因果: 548 | Pred 含因果: 649
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.820
  Precision: 0.778
  Recall   : 0.922
  F1       : 0.844
  (TP=505, TN=346, FP=144, FN=43)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 1038
    Gold triples: 763 | Pred triples: 811
    Precision: 0.545
    Recall   : 0.579
    F1       : 0.562
    (TP=442, FP=369, FN=321)
  [anchor_window] (primary)
    样本数: 1038
    Gold triples: 763 | Pred triples: 811
    Precision: 0.625
    Recall   : 0.664
    F1       : 0.644
    (TP=507, FP=304, FN=256)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 505
    Gold triples: 719 | Pred triples: 653
    Precision: 0.677
    Recall   : 0.615
    F1       : 0.644
    (TP=442, FP=211, FN=277)
  [anchor_window] (primary)
    样本数: 505
    Gold triples: 719 | Pred triples: 653
    Precision: 0.776
    Recall   : 0.705
    F1       : 0.739
    (TP=507, FP=146, FN=212)
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
  "total": 17,
  "by_type": {
    "duplicate_effect_closing_brace": 17
  },
  "samples": [
    {
      "id": 1095,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 2085,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 2169,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 977,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 964,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 1138,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 2019,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 997,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 2528,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 1124,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 623,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 1533,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 463,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 3060,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 2013,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 679,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 1992,
      "repair_type": "duplicate_effect_closing_brace"
    }
  ]
}
```

## 样本明细

Sample details shown: first 200 of 387 wrong samples from 1038 total samples.

### --- id=2733 ---

输入文本: Authorities also rejected a request to hold one on Sunday in Sheung Wan , near where police fired teargas and rubber bullets on demonstrators who had defaced China ’ s representative office in Hong Kong last week .

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
        "span": "demonstrators who had defaced China ’ s representative office in Hong Kong last week"
      },
      "relation": "caused",
      "effect": {
        "span": "police fired teargas and rubber bullets on demonstrators"
      }
    }
  ]
}
```

### --- id=1368 ---

输入文本: According to one villager , officials have frozen that money to prevent villagers funding a journey to Beijing to continue their petitioning .

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
      "cause": "to prevent villagers funding a journey to Beijing to continue their petitioning",
      "effect": "officials have frozen that money"
    },
    {
      "cause": "to continue their petitioning",
      "effect": "villagers funding a journey to Beijing"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to prevent villagers funding a journey to Beijing to continue their petitioning ."
      },
      "relation": "caused",
      "effect": {
        "span": "officials have frozen that money"
      }
    }
  ]
}
```

### --- id=688 ---

输入文本: Leung Chun-ying 's second meet-the-public session , in Kwun Tong , was a much quieter affair than his first one last week , when he caused uproar in some quarters by expressing support for the police 's handling of a protest in Mong Kok at which rival groups clashed over a teacher 's verbal attack on officers .

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
      "cause": "expressing support for the police 's handling of a protest in Mong Kok at which rival groups clashed over a teacher 's verbal attack on officers",
      "effect": "he caused uproar in some quarters"
    },
    {
      "cause": "rival groups clashed over a teacher 's verbal attack on officers",
      "effect": "a protest in Mong Kok"
    },
    {
      "cause": "a teacher 's verbal attack on officers",
      "effect": "rival groups clashed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "by expressing support for the police 's handling of a protest in Mong Kok"
      },
      "relation": "caused",
      "effect": {
        "span": "he caused uproar in some quarters"
      }
    },
    {
      "cause": {
        "span": "over a teacher 's verbal attack on officers ."
      },
      "relation": "caused",
      "effect": {
        "span": "rival groups clashed"
      }
    }
  ]
}
```

### --- id=2316 ---

输入文本: " Some protesters attacked me when I was clicking pictures , but their colleagues dissuaded them .

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
        "span": "when I was clicking pictures"
      },
      "relation": "caused",
      "effect": {
        "span": "Some protesters attacked me"
      }
    }
  ]
}
```

### --- id=1095 ---

输入文本: ﻿Police arrested leaders of various political parties who squatted on the highway in response to ' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC ) to urge the central government to immediately carve out a Telangana state .

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
      "cause": "who squatted on the highway",
      "effect": "﻿Police arrested leaders of various political parties"
    },
    {
      "cause": "' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC )",
      "effect": "leaders of various political parties who squatted on the highway"
    },
    {
      "cause": "to urge the central government to immediately carve out a Telangana state",
      "effect": "' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC )"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in response to ' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC )"
      },
      "relation": "caused",
      "effect": {
        "span": "leaders of various political parties who squatted on the highway"
      }
    },
    {
      "cause": {
        "span": "to urge the central government to immediately carve out a Telangana state ."
      },
      "relation": "caused",
      "effect": {
        "span": "' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC )"
      }
    },
    {
      "cause": {
        "span": "who squatted on the highway in response to ' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC ) to urge the central government to immediately carve out a Telangana state ."
      },
      "relation": "caused",
      "effect": {
        "span": "Police arrested leaders of various political parties"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=2923 ---

输入文本: Slain SOG jawan cremated 06th April 2010 03:49 AM PARADIP : The mortal remains of SOG jawan Partharanjan Behera , who was killed in the Maoist ambush in Koraput district yesterday , were consigned to flames today at his village in Sarilo under Kujang police limits .

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
        "span": "the Maoist ambush in Koraput district yesterday"
      },
      "relation": "caused",
      "effect": {
        "span": "SOG jawan Partharanjan Behera , who was killed"
      }
    }
  ]
}
```

### --- id=1932 ---

输入文本: Akilan was admitted to hospital here along with member of rivaal group Stalin Dinakaraj , who also sustained injuries in the melee .

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
      "cause": "who also sustained injuries",
      "effect": "Akilan was admitted to hospital here along with member of rivaal group Stalin Dinakaraj"
    },
    {
      "cause": "the melee",
      "effect": "who also sustained injuries"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in the melee ."
      },
      "relation": "caused",
      "effect": {
        "span": "Stalin Dinakaraj , who also sustained injuries"
      }
    }
  ]
}
```

### --- id=2605 ---

输入文本: Political Prisoners ' Rights Day today 13th September 2013 08:33 AM The Committee for the Release of Political Prisoners ( CRPP ) is observing September 13 as Political Prisoners Rights Day , commemorating the sacrifice of Shaheed Jitin Das and organising a memorial programme for Maoist idealogue Ganti Prasadam , in Hyderabad on the occasion .

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
      "cause": "The Committee for the Release of Political Prisoners ( CRPP ) is observing September 13 as Political Prisoners Rights Day",
      "effect": "commemorating the sacrifice of Shaheed Jitin Das and organising a memorial programme for Maoist idealogue Ganti Prasadam , in Hyderabad on the occasion"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "commemorating the sacrifice of Shaheed Jitin Das and organising a memorial programme for Maoist idealogue Ganti Prasadam , in Hyderabad on the occasion"
      },
      "relation": "caused",
      "effect": {
        "span": "The Committee for the Release of Political Prisoners ( CRPP ) is observing September 13 as Political Prisoners Rights Day"
      }
    }
  ]
}
```

### --- id=1958 ---

输入文本: Ex - Congress MP Ehasan Jafri was among those killed in the Gulberg Society riots .

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
        "span": "in the Gulberg Society riots ."
      },
      "relation": "caused",
      "effect": {
        "span": "Ex - Congress MP Ehasan Jafri was among those killed"
      }
    }
  ]
}
```

### --- id=2085 ---

输入文本: That apparent calm was shattered in late December , when security forces shot four militants who allegedly attempted to blow up a Communist party building in southern Xinjiang .

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
      "cause": "security forces shot four militants who allegedly attempted to blow up a Communist party building in southern Xinjiang",
      "effect": "That apparent calm was shattered in late December"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when security forces shot four militants who allegedly attempted to blow up a Communist party building in southern Xinjiang ."
      },
      "relation": "caused",
      "effect": {
        "span": "That apparent calm was shattered in late December"
      }
    },
    {
      "cause": {
        "span": "who allegedly attempted to blow up a Communist party building in southern Xinjiang ."
      },
      "relation": "caused",
      "effect": {
        "span": "security forces shot four militants"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=1136 ---

输入文本: Thereafter , two persons , who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district with an intention of causing mass destruction to the train and passengers , were detained under the National Security Act in December .

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
      "cause": "the National Security Act in December",
      "effect": "two persons , who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district with an intention of causing mass destruction to the train and passengers , were detained"
    },
    {
      "cause": "an intention of causing mass destruction to the train and passengers",
      "effect": "two persons , who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "with an intention of causing mass destruction to the train and passengers"
      },
      "relation": "caused",
      "effect": {
        "span": "two persons , who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district with an intention of causing mass destruction to the train and passengers , were detained under the National Security Act in December ."
      }
    }
  ]
}
```

### --- id=1796 ---

输入文本: Govt Readies to Wield the Stick as Striking Doctors Decide to Harden Their Stand

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
      "cause": "Striking Doctors Decide to Harden Their Stand",
      "effect": "Govt Readies to Wield the Stick"
    }
  ],
  "pred_triples": []
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
        "span": "expressing concern at the growing violence against Muslims by vigilante groups"
      },
      "relation": "caused",
      "effect": {
        "span": "National Commission for Minorities ( NCM ) chairperson Naseem Ahmad has written to Union Home Minister Rajnath Singh"
      }
    },
    {
      "cause": {
        "span": "to work towards creating a sense of security amongst the minorities ."
      },
      "relation": "caused",
      "effect": {
        "span": "has urged the Minister"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=73 ---

输入文本: The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram after NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections , as it did not want Achuthanandan to come back to power for another term .

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
      "cause": "NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections",
      "effect": "The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram"
    },
    {
      "cause": "it did not want Achuthanandan to come back to power for another term",
      "effect": "NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections"
      },
      "relation": "caused",
      "effect": {
        "span": "The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram"
      }
    },
    {
      "cause": {
        "span": "as it did not want Achuthanandan to come back to power for another term"
      },
      "relation": "caused",
      "effect": {
        "span": "the NSS did not support the LDF in the recent Assembly elections"
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
        "span": "to flush out the terrorists who managed to escape in dense forests after carrying out the attack ."
      },
      "relation": "caused",
      "effect": {
        "span": "The Army and police have now launched extensive combing operations in the area"
      }
    },
    {
      "cause": {
        "span": "after carrying out the attack ."
      },
      "relation": "caused",
      "effect": {
        "span": "the terrorists who managed to escape in dense forests"
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
        "span": "with pelting them with stones"
      },
      "relation": "caused",
      "effect": {
        "span": "the brick kiln owners have charged the protesters"
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
  ]
}
```

### --- id=614 ---

输入文本: Awanish Kumar Dev , HR GM , was burnt beyond recognition while 100 others were injured during the violence .

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
        "span": "during the violence ."
      },
      "relation": "caused",
      "effect": {
        "span": "Awanish Kumar Dev , HR GM , was burnt beyond recognition while 100 others were injured"
      }
    }
  ]
}
```

### --- id=1313 ---

输入文本: Four-time MP Yadav was arrested in 1999 and convicted for the murder and sentenced to life imprisonment Feb 14 , 2008 .

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
      "cause": "the murder",
      "effect": "Four-time MP Yadav was arrested in 1999 and convicted"
    },
    {
      "cause": "the murder",
      "effect": "and sentenced to life imprisonment Feb 14 , 2008"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "for the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "Four-time MP Yadav was arrested in 1999 and convicted"
      }
    },
    {
      "cause": {
        "span": "for the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "sentenced to life imprisonment Feb 14 , 2008 ."
      }
    }
  ]
}
```

### --- id=1007 ---

输入文本: He said he told Ndebele that since this was a repeat of what happened when the prime minister of India was in the country , party officials should have followed those who were leaving the stadium and observed them .

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
        "span": "since this was a repeat of what happened when the prime minister of India was in the country"
      },
      "relation": "caused",
      "effect": {
        "span": "party officials should have followed those who were leaving the stadium and observed them"
      }
    }
  ]
}
```

### --- id=1343 ---

输入文本: “ There was no formal notice of strike and this has created a lot of hassle for the public .

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
        "span": "There was no formal notice of strike"
      },
      "relation": "caused",
      "effect": {
        "span": "this has created a lot of hassle for the public ."
      }
    }
  ]
}
```

### --- id=1270 ---

输入文本: " Be good citizens and contribute to the development and pay property tax because it is the most affordable tax imposed ever and we all should pay it , " Ashu told Newsline when asked why he was absent from the protest staged by the Congress at the MC headquarters on Monday .

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
        "span": "because it is the most affordable tax imposed ever and we all should pay it"
      },
      "relation": "caused",
      "effect": {
        "span": "Be good citizens and contribute to the development and pay property tax"
      }
    }
  ]
}
```

### --- id=2373 ---

输入文本: Following a demonstration at the district collectorate on Wednesday , the students handed over a memorandum addressed to the Governor to Additional District Magistrate Akhilesh Ojha , who assured them of a fair inquiry .

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
        "span": "Following a demonstration at the district collectorate on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "the students handed over a memorandum addressed to the Governor to Additional District Magistrate Akhilesh Ojha"
      }
    }
  ]
}
```

### --- id=1589 ---

输入文本: The Global Times , a state-run newspaper known for its hawkish stance , said in an editorial that the event to commemorate the June 4 crackdown had " clearly crossed the red line of the law " as it was related to " the most sensitive political issue " in China .

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
      "cause": "it was related to \" the most sensitive political issue \" in China",
      "effect": "The Global Times , a state-run newspaper known for its hawkish stance , said in an editorial that the event to commemorate the June 4 crackdown had \" clearly crossed the red line of the law \""
    },
    {
      "cause": "to commemorate the June 4 crackdown",
      "effect": "the event"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "as it was related to \" the most sensitive political issue \" in China ."
      },
      "relation": "caused",
      "effect": {
        "span": "the event to commemorate the June 4 crackdown had \" clearly crossed the red line of the law \""
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

### --- id=2063 ---

输入文本: Noted sculptor Kanayi Kunhiraman said the Vilappilsala agitation was a successful example of local people ’ s fight against forces imposing injustice on them .

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
      "cause": "against forces imposing injustice on them",
      "effect": "local people ’ s fight"
    }
  ],
  "pred_triples": []
}
```

### --- id=2237 ---

输入文本: December 16 , 2012 00:00 IST VMC employees are determined to continue ‘ Work to Rule ’ The stalemate over payment of salaries to municipal workers continued on Saturday , with the Joint Action Committee ( JAC ) of VMC Employees bent upon continuing ‘ Work to Rule ’ .

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
      "cause": "the Joint Action Committee ( JAC ) of VMC Employees bent upon continuing ‘ Work to Rule ’",
      "effect": "The stalemate over payment of salaries to municipal workers continued on Saturday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over payment of salaries to municipal workers"
      },
      "relation": "caused",
      "effect": {
        "span": "The stalemate"
      }
    }
  ]
}
```

### --- id=2167 ---

输入文本: " These cases were registered against them only to restrain them from taking part in the agitation .

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
      "cause": "only to restrain them from taking part in the agitation",
      "effect": "These cases were registered against them"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to restrain them from taking part in the agitation ."
      },
      "relation": "caused",
      "effect": {
        "span": "These cases were registered against them only"
      }
    }
  ]
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
    }
  ]
}
```

### --- id=103 ---

输入文本: She did not directly name Bhatta-Parsaul , the twin villages that have emerged as the epicentre of the agitation against land acquisition by the Uttar Pradesh government for an expressway project , but specifically mentioned the atrocities on farmers .

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
        "span": "against land acquisition by the Uttar Pradesh government for an expressway project"
      },
      "relation": "caused",
      "effect": {
        "span": "the agitation"
      }
    }
  ]
}
```

### --- id=1008 ---

输入文本: UPPSC quota protest : 4 FIRs name 2,500 for rioting , mischief - Indian Express Express News Service , Express News Service : Allahabad , Wed Jul 17 2013 , 04:07 hrs The Allahabad police Tuesday registered a total of four FIRs , all at Civil Lines police station , in connection with the violence that took place on Monday when youths protesting against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC ) went on the rampage .

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
        "span": "protesting against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC )"
      },
      "relation": "caused",
      "effect": {
        "span": "youths protesting against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC ) went on the rampage"
      }
    },
    {
      "cause": {
        "span": "the violence that took place on Monday when youths protesting against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC ) went on the rampage"
      },
      "relation": "caused",
      "effect": {
        "span": "The Allahabad police Tuesday registered a total of four FIRs , all at Civil Lines police station , in connection with the violence"
      }
    }
  ]
}
```

### --- id=241 ---

输入文本: Fri 27 Fire Walking A 59 - year-old “ barefoot doctor ” is sentenced to four months in jail for attempted arson .

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
      "cause": "attempted arson",
      "effect": "Fri 27 Fire Walking A 59 - year-old “ barefoot doctor ” is sentenced to four months in jail"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "for attempted arson ."
      },
      "relation": "caused",
      "effect": {
        "span": "A 59 - year-old “ barefoot doctor ” is sentenced to four months in jail"
      }
    }
  ]
}
```

### --- id=3017 ---

输入文本: Maretha , where till recently riot victims were not allowed to return home , victims of Best Bakery carnage , residents of Noor Park , and some other hotbeds of violence went unrepresented .

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
      "cause": "Maretha , where till recently riot victims were not allowed to return home",
      "effect": "victims of Best Bakery carnage , residents of Noor Park , and some other hotbeds of violence went unrepresented"
    }
  ],
  "pred_triples": []
}
```

### --- id=492 ---

输入文本: Of the four persons injured in the clashes , three were wounded when the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire to control a mob that was pelting stones on the evening of December 20 .

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
      "cause": "the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire to control a mob that was pelting stones on the evening of December 20",
      "effect": "three were wounded"
    },
    {
      "cause": "to control a mob that was pelting stones on the evening of December 20",
      "effect": "the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire"
      },
      "relation": "caused",
      "effect": {
        "span": "three were wounded"
      }
    },
    {
      "cause": {
        "span": "to control a mob that was pelting stones on the evening of December 20 ."
      },
      "relation": "caused",
      "effect": {
        "span": "the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire"
      }
    }
  ]
}
```

### --- id=1467 ---

输入文本: It is shameful that the government takes this issue so lightly when diplomats from 42 African nations boycotted the weeklong celebration of Africa Day , hosted by the Indian government as a sign of protest against renewed ' racism and Afro-phobia ' , ” he added .

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
      "cause": "diplomats from 42 African nations boycotted the weeklong celebration of Africa Day , hosted by the Indian government as a sign of protest against renewed ' racism and Afro-phobia '",
      "effect": "It is shameful that the government takes this issue so lightly"
    },
    {
      "cause": "protest against renewed ' racism and Afro-phobia '",
      "effect": "diplomats from 42 African nations boycotted the weeklong celebration of Africa Day , hosted by the Indian government"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "as a sign of protest against renewed ' racism and Afro-phobia ' "
      },
      "relation": "caused",
      "effect": {
        "span": "diplomats from 42 African nations boycotted the weeklong celebration of Africa Day , hosted by the Indian government"
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

### --- id=2529 ---

输入文本: The Tanzanian woman was reportedly dragged out of the car in which she was seated along with her three friends when she reached the accident spot with the miscreants mistaking them to have caused the fatal accident though a Sudanese was involved in it , police said .

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
      "cause": "she reached the accident spot with the miscreants mistaking them to have caused the fatal accident",
      "effect": "The Tanzanian woman was reportedly dragged out of the car in which she was seated along with her three friends"
    },
    {
      "cause": "a Sudanese was involved in it",
      "effect": "the miscreants mistaking them to have caused the fatal accident"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "with the miscreants mistaking them to have caused the fatal accident though a Sudanese was involved in it"
      },
      "relation": "caused",
      "effect": {
        "span": "The Tanzanian woman was reportedly dragged out of the car in which she was seated along with her three friends"
      }
    }
  ]
}
```

### --- id=116 ---

输入文本: There were reports of skirmishes and clashes , including stone pelting , in the area in which two policemen were injured .

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
      "cause": "There were reports of skirmishes and clashes , including stone pelting , in the area",
      "effect": "two policemen were injured"
    }
  ],
  "pred_triples": []
}
```

### --- id=362 ---

输入文本: VIJAYAWADA YSRC leaders hold relay fasts in support of Jagan October 09 , 2015 00:00 IST YSR Congress leaders and cadres organised relay hunger strikes in various Assembly constituencies across the district on Thursday in support of party president Y.S. Jaganmohan Reddy ’ s indefinite ‘ deeksha ’ in Guntur seeking special category status for the State .

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
        "span": "in support of party president Y.S. Jaganmohan Reddy ’ s indefinite ‘ deeksha ’ in Guntur seeking special category status for the State ."
      },
      "relation": "caused",
      "effect": {
        "span": "YSR Congress leaders and cadres organised relay hunger strikes in various Assembly constituencies across the district on Thursday"
      }
    },
    {
      "cause": {
        "span": "seeking special category status for the State ."
      },
      "relation": "caused",
      "effect": {
        "span": "party president Y.S. Jaganmohan Reddy ’ s indefinite ‘ deeksha ’ in Guntur"
      }
    }
  ]
}
```

### --- id=3074 ---

输入文本: Tirupur : Protests against lack of amenities November 27 , 2014 00:00 IST Two separate agitations were witnessed on the Corporation office premises on Tuesday with residents and political activists laying siege to the offices of the Mayor and the Commissioner .

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
      "cause": "residents and political activists laying siege to the offices of the Mayor and the Commissioner",
      "effect": "Two separate agitations were witnessed on the Corporation office premises on Tuesday"
    }
  ],
  "pred_triples": []
}
```

### --- id=1424 ---

输入文本: `` Under ANC president Jacob Zuma 's leadership , South Africa has become a banana state , '' he told DA supporters at a rally for jobs at the Ellis Park indoor arena in Johannesburg .

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
      "cause": "ANC president Jacob Zuma 's leadership",
      "effect": "South Africa has become a banana state"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "for jobs"
      },
      "relation": "caused",
      "effect": {
        "span": "a rally"
      }
    }
  ]
}
```

### --- id=1923 ---

输入文本: It finally ended up in clashes between two communities .

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
        "span": "It"
      },
      "relation": "caused",
      "effect": {
        "span": "clashes between two communities"
      }
    }
  ]
}
```

### --- id=1465 ---

输入文本: Hundreds of members of the Police and Prisons Civil Rights Union gathered at the King Dinuzulu Gardens in Durban on Wednesday ahead of a march over salary grades on Wednesday .

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
      "cause": "a march over salary grades on Wednesday",
      "effect": "Hundreds of members of the Police and Prisons Civil Rights Union gathered at the King Dinuzulu Gardens in Durban on Wednesday"
    },
    {
      "cause": "salary grades",
      "effect": "a march"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over salary grades"
      },
      "relation": "caused",
      "effect": {
        "span": "a march"
      }
    }
  ]
}
```

### --- id=977 ---

输入文本: The labour minister 's announcement followed countrywide public hearings on a new minimum wage for the agriculture sector , which were prompted by violent protests in parts of the Western Cape .

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
      "cause": "countrywide public hearings on a new minimum wage for the agriculture sector",
      "effect": "The labour minister 's announcement"
    },
    {
      "cause": "violent protests in parts of the Western Cape",
      "effect": "countrywide public hearings on a new minimum wage for the agriculture sector"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "countrywide public hearings on a new minimum wage for the agriculture sector"
      },
      "relation": "caused",
      "effect": {
        "span": "The labour minister 's announcement followed countrywide public hearings on a new minimum wage for the agriculture sector"
      }
    },
    {
      "cause": {
        "span": "by violent protests in parts of the Western Cape"
      },
      "relation": "caused",
      "effect": {
        "span": "which were prompted by violent protests in parts of the Western Cape"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=2786 ---

输入文本: A house was destroyed in the gun battle and security forces are removing the debris .

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
        "span": "in the gun battle"
      },
      "relation": "caused",
      "effect": {
        "span": "A house was destroyed"
      }
    }
  ]
}
```

### --- id=2210 ---

输入文本: But Nithin would continue his hunger strike by not eating anything , he added .

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
      "cause": "not eating anything",
      "effect": "Nithin would continue his hunger strike"
    }
  ],
  "pred_triples": []
}
```

### --- id=2635 ---

输入文本: Posted : Wed Dec 06 2000 IST SRINAGAR , DEC 5 : Paramilitary troops and a two-person militant suicide squad fought a 22 - hour gunbattle at a Kashmir security camp which ended on Tuesday with eight dead and nine wounded , police said .

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
      "cause": "Paramilitary troops and a two-person militant suicide squad fought a 22 - hour gunbattle at a Kashmir security camp which ended on Tuesday",
      "effect": "eight dead and nine wounded"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a 22 - hour gunbattle at a Kashmir security camp"
      },
      "relation": "caused",
      "effect": {
        "span": "eight dead and nine wounded"
      }
    }
  ]
}
```

### --- id=867 ---

输入文本: There was also largescale displacement in Kandhamal district during and after the 2008 riots following the killing of Swami Lakshmanananda Saraswati .

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
      "cause": "the killing of Swami Lakshmanananda Saraswati",
      "effect": "There was also largescale displacement in Kandhamal district during and after the 2008 riots"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "during and after the 2008 riots following the killing of Swami Lakshmanananda Saraswati ."
      },
      "relation": "caused",
      "effect": {
        "span": "There was also largescale displacement in Kandhamal district"
      }
    },
    {
      "cause": {
        "span": "following the killing of Swami Lakshmanananda Saraswati ."
      },
      "relation": "caused",
      "effect": {
        "span": "the 2008 riots"
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
        "span": "after hundreds of mainly young , masked protesters mostly in black wearing hard hats and goggles seized three key thoroughfares , some deploying metal and plastic barriers to block the way ."
      },
      "relation": "caused",
      "effect": {
        "span": "tensions spiked once more in the financial hub"
      }
    }
  ]
}
```

### --- id=211 ---

输入文本: Addressing a congregation at Gokulnagar , Nandigram , Trinamool Congress chief Mamata Banerjee said the people would give a fitting reply to the Communist Party of India (Marxist)-led government for the “ carnage . ” “ Violence continues ” Condemning the “ atrocities committed by CPI(M) cadres on the innocent people of Nandigram , ” Ms. Banerjee said even after a year “ those responsible had not been punished .

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
        "span": "for the “ carnage . ”"
      },
      "relation": "caused",
      "effect": {
        "span": "the people would give a fitting reply to the Communist Party of India (Marxist)-led government"
      }
    },
    {
      "cause": {
        "span": "Condemning the “ atrocities committed by CPI(M) cadres on the innocent people of Nandigram , ”"
      },
      "relation": "caused",
      "effect": {
        "span": "Ms. Banerjee said even after a year “ those responsible had not been punished ."
      }
    }
  ]
}
```

### --- id=2014 ---

输入文本: The MLAs , along with a large number of party supporters , raised slogans against the government and condemned the attack on the woman MLA .

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
        "span": "against the government"
      },
      "relation": "caused",
      "effect": {
        "span": "The MLAs , along with a large number of party supporters , raised slogans"
      }
    },
    {
      "cause": {
        "span": "condemning the attack on the woman MLA ."
      },
      "relation": "caused",
      "effect": {
        "span": "The MLAs , along with a large number of party supporters , raised slogans against the government and condemned the attack on the woman MLA ."
      }
    }
  ]
}
```

### --- id=2097 ---

输入文本: Maids protest over suspension of levy PUBLISHED : Monday , 28 July , 2008 , 12:00am About 1,000 foreign domestic helpers yesterday protested against the temporary suspension of the employers ' levy , saying it had threatened their livelihoods , and called for permanent abolition of the tax .

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
      "cause": "suspension of levy",
      "effect": "Maids protest"
    },
    {
      "cause": "against the temporary suspension of the employers ' levy",
      "effect": "About 1,000 foreign domestic helpers yesterday protested"
    },
    {
      "cause": "saying it had threatened their livelihoods",
      "effect": "against the temporary suspension of the employers ' levy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over suspension of levy"
      },
      "relation": "caused",
      "effect": {
        "span": "Maids protest"
      }
    },
    {
      "cause": {
        "span": "against the temporary suspension of the employers ' levy"
      },
      "relation": "caused",
      "effect": {
        "span": "About 1,000 foreign domestic helpers yesterday protested"
      }
    },
    {
      "cause": {
        "span": "it had threatened their livelihoods"
      },
      "relation": "caused",
      "effect": {
        "span": "saying it had threatened their livelihoods"
      }
    }
  ]
}
```

### --- id=2879 ---

输入文本: " It is due to such people ( those who unfurled the Vidarbha flag ) that the country 's integrity is damaged .

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
      "cause": "such people ( those who unfurled the Vidarbha flag )",
      "effect": "that the country 's integrity is damaged"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "due to such people ( those who unfurled the Vidarbha flag )"
      },
      "relation": "caused",
      "effect": {
        "span": "the country 's integrity is damaged"
      }
    }
  ]
}
```

### --- id=514 ---

输入文本: Sectarian clashes broke out in Inderkoot village in Sumbal town on December 19 in which one person was injured and a house was partially damaged in arson .

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
      "cause": "Sectarian clashes broke out in Inderkoot village in Sumbal town on December 19",
      "effect": "one person was injured and a house was partially damaged in arson"
    }
  ],
  "pred_triples": []
}
```

### --- id=1126 ---

输入文本: Kumar , an officer of the elite Para unit who hailed from Jind , was among two army personnel from elite Para unit who lost their lives today in the fierce encounter with militants holed up inside a government building in Pampore town .

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
        "span": "in the fierce encounter with militants holed up inside a government building in Pampore town ."
      },
      "relation": "caused",
      "effect": {
        "span": "Kumar , an officer of the elite Para unit who hailed from Jind , was among two army personnel from elite Para unit who lost their lives today"
      }
    }
  ]
}
```

### --- id=645 ---

输入文本: New Delhi , October 29 , Thu Oct 30 2008 , 01:17 hrs Several hours after a migrant labourer from U P was allegedly beaten to death by a group of Marathi-speaking men on a suburban train headed for Mumbai , the Centre issued a stern advisory to the Maharashtra government , asking it to act quickly to end the violence against north Indians and ensure the safety of everyone living in India 's financial capital .

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
      "cause": "asking it to act quickly",
      "effect": "the Centre issued a stern advisory to the Maharashtra government"
    },
    {
      "cause": "to end the violence against north Indians and ensure the safety of everyone living in India 's financial capital",
      "effect": "asking it to act quickly"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after a migrant labourer from U P was allegedly beaten to death by a group of Marathi-speaking men on a suburban train headed for Mumbai"
      },
      "relation": "caused",
      "effect": {
        "span": "the Centre issued a stern advisory to the Maharashtra government"
      }
    },
    {
      "cause": {
        "span": "to end the violence against north Indians and ensure the safety of everyone living in India 's financial capital ."
      },
      "relation": "caused",
      "effect": {
        "span": "asking it to act quickly"
      }
    }
  ]
}
```

### --- id=1275 ---

输入文本: 31st December 2014 06:04 AM MADURAI : Tension continued in Keelakuilkudi near here for the third day on Tuesday when Arunthathiyar community men refused to perform funeral rituals for a Caste Hindu family to protest denial of worship rights in the village temple .

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
      "cause": "Arunthathiyar community men refused to perform funeral rituals for a Caste Hindu family",
      "effect": "Tension continued in Keelakuilkudi near here for the third day on Tuesday"
    },
    {
      "cause": "to protest denial of worship rights in the village temple",
      "effect": "Arunthathiyar community men refused to perform funeral rituals for a Caste Hindu family"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest denial of worship rights in the village temple ."
      },
      "relation": "caused",
      "effect": {
        "span": "Arunthathiyar community men refused to perform funeral rituals for a Caste Hindu family"
      }
    }
  ]
}
```

### --- id=1816 ---

输入文本: As a huge crowd of market-goers gathered to help the injured and to witness the blast after-effects , another powerful blast occurred soon a few feet away from the first blast site .

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
      "cause": "to help the injured and to witness the blast after-effects",
      "effect": "a huge crowd of market-goers gathered"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "As a huge crowd of market-goers gathered to help the injured and to witness the blast after-effects"
      },
      "relation": "caused",
      "effect": {
        "span": "another powerful blast occurred soon a few feet away from the first blast site ."
      }
    },
    {
      "cause": {
        "span": "to help the injured and to witness the blast after-effects"
      },
      "relation": "caused",
      "effect": {
        "span": "a huge crowd of market-goers gathered"
      }
    }
  ]
}
```

### --- id=2672 ---

输入文本: Similarly , some palmyrah farmers tapped toddy at Pattankaadu even as the police arrested 517 protestors , including 66 women , in the neighbouring town of Vasudevanallur .

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
      "cause": "the police arrested 517 protestors , including 66 women , in the neighbouring town of Vasudevanallur",
      "effect": "some palmyrah farmers tapped toddy at Pattankaadu"
    }
  ],
  "pred_triples": []
}
```

### --- id=2933 ---

输入文本: Condemning Tuesday ’ s incident , Chidambaram refered to the Dantewada massacre of 75 CRPF men and said the companies of CRPF in Chintalnar and Chintagufa were deployed by the state government .

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
        "span": "Condemning Tuesday ’ s incident"
      },
      "relation": "caused",
      "effect": {
        "span": "Chidambaram refered to the Dantewada massacre of 75 CRPF men and said the companies of CRPF in Chintalnar and Chintagufa were deployed by the state government ."
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
        "span": "for keeping mum when a flag of a separate Vidarbha state was recently hoisted in Nagpur on Maharashtra Day ."
      },
      "relation": "caused",
      "effect": {
        "span": "Ruling alliance partner Shiv Sena today flayed Maharashtra Chief Minister Devendra Fadnavis"
      }
    }
  ]
}
```

### --- id=2004 ---

输入文本: Twelve students arrested for public violence while protesting against financial aid cuts at the University of the Witwatersrand appeared in the Johannesburg Regional Court on Tuesday .

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
      "cause": "public violence while protesting against financial aid cuts at the University of the Witwatersrand",
      "effect": "Twelve students arrested"
    },
    {
      "cause": "against financial aid cuts",
      "effect": "protesting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "for public violence"
      },
      "relation": "caused",
      "effect": {
        "span": "Twelve students arrested"
      }
    },
    {
      "cause": {
        "span": "protesting against financial aid cuts at the University of the Witwatersrand"
      },
      "relation": "caused",
      "effect": {
        "span": "public violence"
      }
    }
  ]
}
```

### --- id=1877 ---

输入文本: Led by the Joint Action Committee of Employees Teachers and Workers , a huge rally was organised from pavilion grounds to the Collectorate .

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
        "span": "Led by the Joint Action Committee of Employees Teachers and Workers"
      },
      "relation": "caused",
      "effect": {
        "span": "a huge rally was organised from pavilion grounds to the Collectorate ."
      }
    }
  ]
}
```

### --- id=1339 ---

输入文本: Hundreds of them raised slogans against the SP .

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
        "span": "against the SP ."
      },
      "relation": "caused",
      "effect": {
        "span": "Hundreds of them raised slogans"
      }
    }
  ]
}
```

### --- id=1239 ---

输入文本: Protest Federation of various autorickshaw employees union on Thursday staged a protest in front of regional transport office raising several demands .

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
        "span": "raising several demands ."
      },
      "relation": "caused",
      "effect": {
        "span": "Protest Federation of various autorickshaw employees union on Thursday staged a protest in front of regional transport office"
      }
    }
  ]
}
```

### --- id=1595 ---

输入文本: ADILABAD : TRS condemns arrests March 11 , 2011 00:00 IST Telangana Rastra Samiti ( TRS ) on Thursday condemned arrests of Telangana protagonists from Adilabad district to foil the ‘ Million March ' .

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
      "cause": "to foil the ‘ Million March '",
      "effect": "Telangana Rastra Samiti ( TRS ) on Thursday condemned arrests of Telangana protagonists from Adilabad district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to foil the ‘ Million March ' ."
      },
      "relation": "caused",
      "effect": {
        "span": "arrests of Telangana protagonists from Adilabad district"
      }
    }
  ]
}
```

### --- id=1642 ---

输入文本: Mr. Bommai later told presspersons that whoever was responsible for forcing the protestors to stage such a protest would be dealt with sternly .

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
      "cause": "whoever was responsible for forcing the protestors to stage such a protest",
      "effect": "would be dealt with sternly"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "forcing the protestors to stage such a protest"
      },
      "relation": "caused",
      "effect": {
        "span": "whoever was responsible for forcing the protestors to stage such a protest would be dealt with sternly"
      }
    }
  ]
}
```

### --- id=1723 ---

输入文本: Mining for trouble Sino Gold Mining , which only last week announced a joint venture to expand exploration near its White Mountain Mine in Jilin province , had to halt operations yesterday as protesting farmers blocked the main access road .

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
      "cause": "protesting farmers blocked the main access road",
      "effect": "Sino Gold Mining , which only last week announced a joint venture to expand exploration near its White Mountain Mine in Jilin province , had to halt operations yesterday"
    },
    {
      "cause": "to expand exploration near its White Mountain Mine in Jilin province",
      "effect": "Sino Gold Mining , which only last week announced a joint venture"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "as protesting farmers blocked the main access road"
      },
      "relation": "caused",
      "effect": {
        "span": "Sino Gold Mining , which only last week announced a joint venture to expand exploration near its White Mountain Mine in Jilin province , had to halt operations yesterday"
      }
    }
  ]
}
```

### --- id=1897 ---

输入文本: July 16 : CPI-Maoist cadres killed 17 personnel of the Special Operations Group of the Orissa Police in a landmine blast in Malkangiri district .

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
        "span": "a landmine blast in Malkangiri district"
      },
      "relation": "caused",
      "effect": {
        "span": "CPI-Maoist cadres killed 17 personnel of the Special Operations Group of the Orissa Police"
      }
    }
  ]
}
```

### --- id=2840 ---

输入文本: Thirty-seven of the operators signed a petition and held a press conference last Sunday to protest against the proposal , which they said would cut their basic salary by up to 40 per cent .

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
      "cause": "to protest",
      "effect": "Thirty-seven of the operators signed a petition and held a press conference last Sunday"
    },
    {
      "cause": "against the proposal , which they said would cut their basic salary by up to 40 per cent",
      "effect": "to protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest against the proposal"
      },
      "relation": "caused",
      "effect": {
        "span": "Thirty-seven of the operators signed a petition and held a press conference last Sunday"
      }
    },
    {
      "cause": {
        "span": "against the proposal"
      },
      "relation": "caused",
      "effect": {
        "span": "to protest"
      }
    }
  ]
}
```

### --- id=2779 ---

输入文本: After the blast , Maoists opened indiscriminate firing .

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
        "span": "After the blast"
      },
      "relation": "caused",
      "effect": {
        "span": "Maoists opened indiscriminate firing ."
      }
    }
  ]
}
```

### --- id=376 ---

输入文本: One protester said yesterday 's turnout was smaller , following reports the authorities had tried to prevent the demonstration .

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
        "span": "following reports the authorities had tried to prevent the demonstration"
      },
      "relation": "caused",
      "effect": {
        "span": "yesterday 's turnout was smaller"
      }
    }
  ]
}
```

### --- id=1036 ---

输入文本: The fresh clash came a day after over 22 people , including five media men and 11 security personnel with an officer among them , were injured last night when students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus prompting them to use force to quell the mob .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 3,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 3,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 3,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus prompting them to use force to quell the mob",
      "effect": "over 22 people , including five media men and 11 security personnel with an officer among them , were injured last night"
    },
    {
      "cause": "students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus",
      "effect": "them to use force"
    },
    {
      "cause": "to quell the mob",
      "effect": "them to use force"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over 22 people , including five media men and 11 security personnel with an officer among them , were injured last night when students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus prompting them to use force to quell the mob ."
      },
      "relation": "caused",
      "effect": {
        "span": "The fresh clash came a day after"
      }
    },
    {
      "cause": {
        "span": "students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus"
      },
      "relation": "caused",
      "effect": {
        "span": "over 22 people , including five media men and 11 security personnel with an officer among them , were injured last night"
      }
    },
    {
      "cause": {
        "span": "over creation of a separate Telangana"
      },
      "relation": "caused",
      "effect": {
        "span": "students agitating"
      }
    },
    {
      "cause": {
        "span": "students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus"
      },
      "relation": "caused",
      "effect": {
        "span": "prompting them to use force to quell the mob ."
      }
    }
  ]
}
```

### --- id=759 ---

输入文本: About 20 police personnel , including Nedumangad DySP Sukeshan , Palode circle inspector Anil Kumar , sub-inspector Anil Kumar and Pangode sub-inspector Praveen , and about the same number of local people belonging to various political parties were injured in the clashes .

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
      "cause": "the clashes",
      "effect": "About 20 police personnel , including Nedumangad DySP Sukeshan , Palode circle inspector Anil Kumar , sub-inspector Anil Kumar and Pangode sub-inspector Praveen , and about the same number of local people belonging to various political parties were injured"
    }
  ],
  "pred_triples": []
}
```

### --- id=2755 ---

输入文本: We need to make sure , we must make sure we push , we push and we push until the state listens to us , '' Makwaiba told a cheering crowd .

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
        "span": "the state listens to us"
      },
      "relation": "caused",
      "effect": {
        "span": "we push , we push and we push"
      }
    }
  ]
}
```

### --- id=2060 ---

输入文本: 27th March 2012 05:03 AM THIRUVANANTHAPURAM : Protesting against the large-scale reclamation of Vellayani backwaters by the resorts and real-estate mafia , a Secretariat dharna was staged under the joint aegis of the Kalanilayam Paristhithi Vedi , environmentalists and cultural activists here on Monday .

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
      "cause": "against the large-scale reclamation of Vellayani backwaters by the resorts and real-estate mafia",
      "effect": "Protesting"
    },
    {
      "cause": "Protesting against the large-scale reclamation of Vellayani backwaters by the resorts and real-estate mafia",
      "effect": "a Secretariat dharna was staged under the joint aegis of the Kalanilayam Paristhithi Vedi , environmentalists and cultural activists here on Monday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Protesting against the large-scale reclamation of Vellayani backwaters by the resorts and real-estate mafia"
      },
      "relation": "caused",
      "effect": {
        "span": "a Secretariat dharna was staged under the joint aegis of the Kalanilayam Paristhithi Vedi , environmentalists and cultural activists here on Monday ."
      }
    }
  ]
}
```

### --- id=2555 ---

输入文本: “ Hong Kong has changed a lot [ since the protests ] .

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
        "span": "since the protests"
      },
      "relation": "caused",
      "effect": {
        "span": "Hong Kong has changed a lot"
      }
    }
  ]
}
```

### --- id=1006 ---

输入文本: `` They said to me that the reburial was very dignified , proceeded very well , until plus minus 60 people made a noise when the president was about to speak , and decided to walk out , '' Motlanthe said .

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
        "span": "when the president was about to speak"
      },
      "relation": "caused",
      "effect": {
        "span": "plus minus 60 people made a noise"
      }
    }
  ]
}
```

### --- id=2849 ---

输入文本: Traders pulled down their shutters to join the statewide agitation to oppose the State Government 's move to amend the APMC Act on Friday .

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
      "cause": "to join the statewide agitation",
      "effect": "Traders pulled down their shutters"
    },
    {
      "cause": "to oppose the State Government 's move",
      "effect": "to join the statewide agitation"
    },
    {
      "cause": "to amend the APMC Act on Friday",
      "effect": "the State Government 's move"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to join the statewide agitation to oppose the State Government 's move to amend the APMC Act on Friday ."
      },
      "relation": "caused",
      "effect": {
        "span": "Traders pulled down their shutters"
      }
    },
    {
      "cause": {
        "span": "to oppose the State Government 's move to amend the APMC Act on Friday ."
      },
      "relation": "caused",
      "effect": {
        "span": "to join the statewide agitation"
      }
    }
  ]
}
```

### --- id=1885 ---

输入文本: Picking PMs brain : 4 BJP docs under fire for mocking at PM

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
      "cause": "mocking at PM",
      "effect": "4 BJP docs under fire"
    }
  ],
  "pred_triples": []
}
```

### --- id=2934 ---

输入文本: DA MP Andrew Whitfield said he would ask police commissioner General Khehla Sitole to activate the National Joint Operations and Intelligence Structure ( Natjoints ) to intervene to curb violence , protect infrastructure and prevent further damage to the economy arising out of events such as looting , attacks on foreign nationals and the torching of trucks in an ongoing labour protest .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "to activate the National Joint Operations and Intelligence Structure ( Natjoints )",
      "effect": "he would ask police commissioner General Khehla Sitole"
    },
    {
      "cause": "to intervene",
      "effect": "to activate the National Joint Operations and Intelligence Structure ( Natjoints )"
    },
    {
      "cause": "to curb violence , protect infrastructure and prevent further damage to the economy",
      "effect": "to intervene"
    },
    {
      "cause": "arising out of events such as looting , attacks on foreign nationals and the torching of trucks in an ongoing labour protest",
      "effect": "damage to the economy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to curb violence , protect infrastructure and prevent further damage to the economy arising out of events such as looting , attacks on foreign nationals and the torching of trucks in an ongoing labour protest ."
      },
      "relation": "caused",
      "effect": {
        "span": "he would ask police commissioner General Khehla Sitole to activate the National Joint Operations and Intelligence Structure ( Natjoints ) to intervene"
      }
    },
    {
      "cause": {
        "span": "events such as looting , attacks on foreign nationals and the torching of trucks in an ongoing labour protest ."
      },
      "relation": "caused",
      "effect": {
        "span": "further damage to the economy"
      }
    }
  ]
}
```

### --- id=1870 ---

输入文本: Soon after the meeting , BJP legislators staged a dharna demanding Bhardwaj ’ s recall for his “ undemocratic conduct ” , even as the state Cabinet urged him to accord permission to convene a 10 - day legislature session from June 2 .

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
      "cause": "the state Cabinet urged him to accord permission to convene a 10 - day legislature session from June 2",
      "effect": "BJP legislators staged a dharna demanding Bhardwaj ’ s recall for his “ undemocratic conduct ”"
    },
    {
      "cause": "demanding Bhardwaj ’ s recall for his “ undemocratic conduct ”",
      "effect": "BJP legislators staged a dharna"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding Bhardwaj ’ s recall for his “ undemocratic conduct ”"
      },
      "relation": "caused",
      "effect": {
        "span": "BJP legislators staged a dharna"
      }
    },
    {
      "cause": {
        "span": "for his “ undemocratic conduct ”"
      },
      "relation": "caused",
      "effect": {
        "span": "demanding Bhardwaj ’ s recall"
      }
    },
    {
      "cause": {
        "span": "to convene a 10 - day legislature session from June 2 ."
      },
      "relation": "caused",
      "effect": {
        "span": "the state Cabinet urged him to accord permission"
      }
    }
  ]
}
```

### --- id=243 ---

输入文本: 2 held over poisoning threat to Tung PUBLISHED : Wednesday , 03 October , 2001 , 12:00am Donald Tsang Donald Tsang A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials were arrested in Central yesterday .

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
      "cause": "A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials",
      "effect": "were arrested in Central yesterday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials"
      },
      "relation": "caused",
      "effect": {
        "span": "A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials were arrested in Central yesterday ."
      }
    }
  ]
}
```

### --- id=2747 ---

输入文本: This outrageous and provocative statement comes in the wake of violence that erupted during a rally by Muslims in Mumbai ’ s Azad Maidan .

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
        "span": "violence that erupted during a rally by Muslims in Mumbai ’ s Azad Maidan ."
      },
      "relation": "caused",
      "effect": {
        "span": "This outrageous and provocative statement comes"
      }
    }
  ]
}
```

### --- id=881 ---

输入文本: Most government and private establishments remained open in Vijayawada city , one of the nerve centres of the agitation against the bifurcation .

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
        "span": "against the bifurcation"
      },
      "relation": "caused",
      "effect": {
        "span": "the agitation"
      }
    }
  ]
}
```

### --- id=1127 ---

输入文本: Following this , the police appealed to the agitators to withdraw the strike .

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
        "span": "to withdraw the strike ."
      },
      "relation": "caused",
      "effect": {
        "span": "the police appealed to the agitators"
      }
    }
  ]
}
```

### --- id=949 ---

输入文本: The abducted jawans were unarmed and also not in police uniform as they were returning from leave to district headquarters Narayanpur town .

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
        "span": "as they were returning from leave to district headquarters Narayanpur town ."
      },
      "relation": "caused",
      "effect": {
        "span": "The abducted jawans were unarmed and also not in police uniform"
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

### --- id=2071 ---

输入文本: VCK blames PMK for unrest

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
      "cause": "unrest",
      "effect": "VCK blames PMK"
    }
  ],
  "pred_triples": []
}
```

### --- id=289 ---

输入文本: And in June 2007 , over 20,000 people rallied in Xiamen , a coastal city in Fujian province , to protest against plans to built a paraxylene chemical plant in the city .

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
      "effect": "over 20,000 people rallied in Xiamen , a coastal city in Fujian province"
    },
    {
      "cause": "against plans to built a paraxylene chemical plant in the city",
      "effect": "to protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest against plans to built a paraxylene chemical plant in the city ."
      },
      "relation": "caused",
      "effect": {
        "span": "over 20,000 people rallied in Xiamen , a coastal city in Fujian province"
      }
    }
  ]
}
```

### --- id=1602 ---

输入文本: Attempts Karimnagar Staff Reporter adds : The district police foiled the attempts made by the TRS and pro-Telangana activists to proceed and participate in ‘ Million March ' in Hyderabad on Thursday with their arrests on various routes proceeding to the capital .

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
      "cause": "their arrests on various routes proceeding to the capital",
      "effect": "The district police foiled the attempts made by the TRS and pro-Telangana activists to proceed and participate in ‘ Million March ' in Hyderabad on Thursday"
    },
    {
      "cause": "to proceed and participate in ‘ Million March ' in Hyderabad on Thursday",
      "effect": "the attempts made by the TRS and pro-Telangana activists"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to proceed and participate in ‘ Million March ' in Hyderabad on Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "the attempts made by the TRS and pro-Telangana activists"
      }
    },
    {
      "cause": {
        "span": "the attempts made by the TRS and pro-Telangana activists to proceed and participate in ‘ Million March ' in Hyderabad on Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "their arrests on various routes proceeding to the capital ."
      }
    }
  ]
}
```

### --- id=1927 ---

输入文本: Demonstrators flayed the advocates for the violent incidents that took place at the Madras High Court premises in Chennai on February 19 this year .

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
        "span": "for the violent incidents that took place at the Madras High Court premises in Chennai on February 19 this year ."
      },
      "relation": "caused",
      "effect": {
        "span": "Demonstrators flayed the advocates"
      }
    }
  ]
}
```

### --- id=624 ---

输入文本: They took to the street and within minutes a farm house was on fire , two more house were set alight and road blocked .

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
        "span": "They took to the street"
      },
      "relation": "caused",
      "effect": {
        "span": "within minutes a farm house was on fire , two more house were set alight and road blocked ."
      }
    }
  ]
}
```

### --- id=1042 ---

输入文本: 19th June 2014 07:22 AM MADURAI : Distressed after allegedly being denied a scholarship by his school , a Class XII Dalit dropout of the Government Higher Secondary School in Allinagaram , in Theni district , tied to immolate himself on Tuesday .

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
      "cause": "allegedly being denied a scholarship by his school",
      "effect": "Distressed"
    },
    {
      "cause": "Distressed after allegedly being denied a scholarship by his school",
      "effect": "a Class XII Dalit dropout of the Government Higher Secondary School in Allinagaram , in Theni district , tied to immolate himself on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after allegedly being denied a scholarship by his school"
      },
      "relation": "caused",
      "effect": {
        "span": "a Class XII Dalit dropout of the Government Higher Secondary School in Allinagaram , in Theni district , tied to immolate himself on Tuesday ."
      }
    }
  ]
}
```

### --- id=1565 ---

输入文本: Reacting to the news , Hardik Patel , the face of Patel quota stir , called it " failure " of the government .

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
        "span": "Reacting to the news"
      },
      "relation": "caused",
      "effect": {
        "span": "Hardik Patel , the face of Patel quota stir , called it \" failure \" of the government ."
      }
    }
  ]
}
```

### --- id=2181 ---

输入文本: For when they had met publicly on Sunday , Shiv Sena workers had barged in violently to break up their peaceful protest .

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
      "cause": "to break up their peaceful protest",
      "effect": "Shiv Sena workers had barged in violently"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when they had met publicly on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "Shiv Sena workers had barged in violently to break up their peaceful protest ."
      }
    },
    {
      "cause": {
        "span": "to break up their peaceful protest ."
      },
      "relation": "caused",
      "effect": {
        "span": "Shiv Sena workers had barged in violently"
      }
    }
  ]
}
```

### --- id=2202 ---

输入文本: The residents said the SI had used unparliamentary language when they were staging a road roko , over supply of drinking water .

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
        "span": "over supply of drinking water ."
      },
      "relation": "caused",
      "effect": {
        "span": "they were staging a road roko"
      }
    }
  ]
}
```

### --- id=1207 ---

输入文本: Three people have died and scores have been injured in violence related to the illegal strike .

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
      "cause": "the illegal strike",
      "effect": "Three people have died and scores have been injured in violence"
    },
    {
      "cause": "violence related to the illegal strike",
      "effect": "Three people have died and scores have been injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "violence related to the illegal strike ."
      },
      "relation": "caused",
      "effect": {
        "span": "Three people have died and scores have been injured"
      }
    }
  ]
}
```

### --- id=704 ---

输入文本: This caused injury to accused no : 37 in the case .

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
        "span": "This"
      },
      "relation": "caused",
      "effect": {
        "span": "injury to accused no : 37 in the case ."
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
        "span": "to hail the decision ."
      },
      "relation": "caused",
      "effect": {
        "span": "there were also celebrations in different parts of the city"
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

### --- id=543 ---

输入文本: Interestingly , all these shops had downed shutters on first day of the strike on November 15 .

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
        "span": "on first day of the strike on November 15"
      },
      "relation": "caused",
      "effect": {
        "span": "all these shops had downed shutters"
      }
    }
  ]
}
```

### --- id=661 ---

输入文本: Coinciding with the unrest in the board is the indefinite hunger strike launched by three employees Mahesh Ahire , Shriram Gavai and Balkrishna Gadekar whose regular promotions were denied and the former two were transferred to Nashik on the same post .

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
        "span": "whose regular promotions were denied and the former two were transferred to Nashik on the same post ."
      },
      "relation": "caused",
      "effect": {
        "span": "the indefinite hunger strike launched by three employees Mahesh Ahire , Shriram Gavai and Balkrishna Gadekar"
      }
    }
  ]
}
```

### --- id=2612 ---

输入文本: Security forces in Kokrajhar district have so far killed 19 militants since April 29 in separate gunfights .

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
        "span": "separate gunfights"
      },
      "relation": "caused",
      "effect": {
        "span": "Security forces in Kokrajhar district have so far killed 19 militants since April 29"
      }
    }
  ]
}
```

### --- id=208 ---

输入文本: As hundreds of employees from the city went to Vizianagaram to take part in the last rites of N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI , an all-union meeting convened by the CITU resolved to organise demonstrations in front of all industrial establishments located in the city on Wednesday .

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
      "cause": "to take part in the last rites of N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI",
      "effect": "hundreds of employees from the city went to Vizianagaram"
    },
    {
      "cause": "to protest against the Centre ’ s decision on strategic stake sale of DCI",
      "effect": "N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest against the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "who committed suicide on railway tracks"
      }
    },
    {
      "cause": {
        "span": "the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "to protest against the Centre ’ s decision on strategic stake sale of DCI"
      }
    },
    {
      "cause": {
        "span": "As hundreds of employees from the city went to Vizianagaram to take part in the last rites of N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "an all-union meeting convened by the CITU resolved to organise demonstrations in front of all industrial establishments located in the city on Wednesday ."
      }
    }
  ]
}
```

### --- id=153 ---

输入文本: The commission , chaired by retired Judge Ian Farlam , is investigating the deaths of 44 people during the wage-related strike at Lonmin 's platinum mining operations at Marikana in August 2012 .

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
        "span": "the wage-related strike at Lonmin 's platinum mining operations at Marikana in August 2012"
      },
      "relation": "caused",
      "effect": {
        "span": "the deaths of 44 people"
      }
    }
  ]
}
```

### --- id=2817 ---

输入文本: Rs 2,200 cr Transactions Hit as Staff Strike Shuts Banks Across the State

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
        "span": "Staff Strike Shuts Banks Across the State"
      },
      "relation": "caused",
      "effect": {
        "span": "Rs 2,200 cr Transactions Hit"
      }
    }
  ]
}
```

### --- id=1087 ---

输入文本: “ But as the political and media pressure mounts , it becomes harder for us to exercise those options . ” The executioners of the terrorist attack on Pakistan , of course , would like nothing better than for India to get trapped into an aggressive , and preferably , military response .

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
        "span": "as the political and media pressure mounts"
      },
      "relation": "caused",
      "effect": {
        "span": "it becomes harder for us to exercise those options ."
      }
    }
  ]
}
```

### --- id=839 ---

输入文本: The students said the police had taken away national flag from them during a clash on Friday last and demanded that it be returned to them .

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
        "span": "during a clash on Friday last"
      },
      "relation": "caused",
      "effect": {
        "span": "the police had taken away national flag from them"
      }
    },
    {
      "cause": {
        "span": "that it be returned to them ."
      },
      "relation": "caused",
      "effect": {
        "span": "demanded"
      }
    }
  ]
}
```

### --- id=638 ---

输入文本: I would like to request people to reconsider the strike , so that common people do not suffer , " he said .

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
        "span": "so that common people do not suffer"
      },
      "relation": "caused",
      "effect": {
        "span": "I would like to request people to reconsider the strike"
      }
    }
  ]
}
```

### --- id=1105 ---

输入文本: He accused the government of suppressing a peaceful and democratic protest to demand Telangana state .

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
      "cause": "suppressing a peaceful and democratic protest to demand Telangana state",
      "effect": "He accused the government"
    },
    {
      "cause": "to demand Telangana state",
      "effect": "a peaceful and democratic protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to demand Telangana state ."
      },
      "relation": "caused",
      "effect": {
        "span": "a peaceful and democratic protest"
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
        "span": "the arrest of student union president Kanhaiya Kumar on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir ."
      },
      "relation": "caused",
      "effect": {
        "span": "The escalating protests in the JNU"
      }
    },
    {
      "cause": {
        "span": "that he too shouted the anti-Indian slogans at a meeting on Kashmir ."
      },
      "relation": "caused",
      "effect": {
        "span": "charges"
      }
    }
  ]
}
```

### --- id=1091 ---

输入文本: And the deliberate targeting of U.S. and British citizens and Jews in the Mumbai attacks should be a further reminder to Washington of the danger of allowing groups like LeT any breathing space .

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
        "span": "the deliberate targeting of U.S. and British citizens and Jews in the Mumbai attacks"
      },
      "relation": "caused",
      "effect": {
        "span": "should be a further reminder to Washington of the danger of allowing groups like LeT any breathing space ."
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
      "cause": "Suddenly the situation flared up",
      "effect": "the vehicle was vandalised"
    }
  ],
  "pred_triples": []
}
```

### --- id=1884 ---

输入文本: - Indian Express Parimal Dabhi , Parimal Dabhi : Ahmedabad , September 18 , Fri Sep 19 2008 , 01:25 hrs One Charul Vakta , a businessman by profession , has filed a police complaint against four members of the City Doctors ' Cell of the Ahmedabad unit of the BJP for allegedly defaming Prime Minister Manmohan Singh in their protest act , wherein they alluded that he was anti-national , in addition to passing disparaging remarks about him .

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
      "cause": "allegedly defaming Prime Minister Manmohan Singh in their protest act",
      "effect": "Charul Vakta , a businessman by profession , has filed a police complaint against four members of the City Doctors ' Cell of the Ahmedabad unit of the BJP"
    },
    {
      "cause": "they alluded that he was anti-national , in addition to passing disparaging remarks about him",
      "effect": "allegedly defaming Prime Minister Manmohan Singh in their protest act"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "for allegedly defaming Prime Minister Manmohan Singh in their protest act , wherein they alluded that he was anti-national , in addition to passing disparaging remarks about him ."
      },
      "relation": "caused",
      "effect": {
        "span": "One Charul Vakta , a businessman by profession , has filed a police complaint against four members of the City Doctors ' Cell of the Ahmedabad unit of the BJP"
      }
    }
  ]
}
```

### --- id=432 ---

输入文本: Employees at three factories had signed a petition supporting Mr Zong and were demanding reassurances about the future of the venture and their jobs , Xinhua said .

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
        "span": "supporting Mr Zong"
      },
      "relation": "caused",
      "effect": {
        "span": "Employees at three factories had signed a petition"
      }
    },
    {
      "cause": {
        "span": "demanding reassurances about the future of the venture and their jobs"
      },
      "relation": "caused",
      "effect": {
        "span": "Employees at three factories ... were demanding reassurances about the future of the venture and their jobs"
      }
    }
  ]
}
```

### --- id=1640 ---

输入文本: Mr. Bommai visited Savanur on Wednesday along with officials and other elected representatives and asked the Deputy Commissioner to inquire into the circumstances that forced the community members to stage such a protest .

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
      "cause": "asked the Deputy Commissioner to inquire into the circumstances that forced the community members to stage such a protest .",
      "effect": "Mr. Bommai visited Savanur on Wednesday along with officials and other elected representatives"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the circumstances that forced the community members to stage such a protest"
      },
      "relation": "caused",
      "effect": {
        "span": "to stage such a protest"
      }
    }
  ]
}
```

### --- id=1681 ---

输入文本: By Tuesday , the protest had spilled over to Coverdale in Christiana where a community hall was torched .

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
        "span": "the protest had spilled over to Coverdale in Christiana"
      },
      "relation": "caused",
      "effect": {
        "span": "a community hall was torched ."
      }
    }
  ]
}
```

### --- id=2531 ---

输入文本: India had suspended the talks after Pakistani gunmen attacked Mumbai last year , saying it would not be resumed till Islamabad showed concrete action on meeting India ’ s concerns over cross-border terrorism .

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
      "cause": "Pakistani gunmen attacked Mumbai last year",
      "effect": "India had suspended the talks"
    },
    {
      "cause": "Islamabad showed concrete action on meeting India ’ s concerns over cross-border terrorism",
      "effect": "it would not be resumed"
    },
    {
      "cause": "cross-border terrorism",
      "effect": "India ’ s concerns"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after Pakistani gunmen attacked Mumbai last year"
      },
      "relation": "caused",
      "effect": {
        "span": "India had suspended the talks"
      }
    },
    {
      "cause": {
        "span": "over cross-border terrorism"
      },
      "relation": "caused",
      "effect": {
        "span": "India ’ s concerns"
      }
    }
  ]
}
```

### --- id=1010 ---

输入文本: They have been identified on the basis of the photographs and video footage of the incident .

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
        "span": "on the basis of the photographs and video footage of the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "They have been identified"
      }
    }
  ]
}
```

### --- id=2705 ---

输入文本: This led to violent protests across the city the next day , with a group of students even storming into the university campus and demanding the dismissal of the teacher who had set the question paper .

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
      "cause": "demanding the dismissal of the teacher who had set the question paper",
      "effect": "a group of students even storming into the university campus"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "This"
      },
      "relation": "caused",
      "effect": {
        "span": "led to violent protests across the city the next day"
      }
    },
    {
      "cause": {
        "span": "demanding the dismissal of the teacher who had set the question paper ."
      },
      "relation": "caused",
      "effect": {
        "span": "a group of students even storming into the university campus"
      }
    }
  ]
}
```

### --- id=1213 ---

输入文本: Anticipating the strike some of the banks , particularly SBI and its associates , had ensured that their ATMs ( automated teller machines ) had cash to meet the customer demand , he added .

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
        "span": "Anticipating the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "some of the banks , particularly SBI and its associates , had ensured that their ATMs ( automated teller machines ) had cash to meet the customer demand"
      }
    }
  ]
}
```

### --- id=1050 ---

输入文本: And two BJP central teams , which visited Birbhum and South 24 Parganas districts to investigate the violent attacks on party cadre , had submitted its report to Union Home Minister Rajnath Singh .

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
        "span": "to investigate the violent attacks on party cadre"
      },
      "relation": "caused",
      "effect": {
        "span": "two BJP central teams , which visited Birbhum and South 24 Parganas districts"
      }
    }
  ]
}
```

### --- id=1227 ---

输入文本: ( SUBS : Pics will be available later on www.sapapics.co.za ) South African rape laws still blame the survivor of rape , People Opposing Woman Abuse ( Powa ) said on Friday at a protest outside the Johannesburg High Court .

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
        "span": "South African rape laws still blame the survivor of rape"
      },
      "relation": "caused",
      "effect": {
        "span": "People Opposing Woman Abuse ( Powa ) said on Friday at a protest outside the Johannesburg High Court ."
      }
    }
  ]
}
```

### --- id=2538 ---

输入文本: TAMIL NADU Post blasts , the web of security tightens May 29 , 2014 00:00 IST Railway stations , places of worship , cinema halls , malls – the enhanced protective measures are everywhere The May Day twin blasts on platform nine of Chennai Central sent a strong message to various enforcement agencies in the city .

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
      "cause": "The May Day twin blasts on platform nine of Chennai Central sent a strong message to various enforcement agencies in the city",
      "effect": "Railway stations , places of worship , cinema halls , malls – the enhanced protective measures are everywhere"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The May Day twin blasts on platform nine of Chennai Central"
      },
      "relation": "caused",
      "effect": {
        "span": "sent a strong message to various enforcement agencies in the city ."
      }
    }
  ]
}
```

### --- id=1121 ---

输入文本: Prof. Ratnam , who was one of the faculty members who got arrested during the unrest in UoH on March 22 , rejected Justice Roopanwal Commission report that declared Rohith Vemula non-Dalit .

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
        "span": "during the unrest in UoH on March 22"
      },
      "relation": "caused",
      "effect": {
        "span": "Prof. Ratnam , who was one of the faculty members who got arrested"
      }
    }
  ]
}
```

### --- id=2785 ---

输入文本: " The gun fire was returned and a firefight ensued , " the officer said .

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
        "span": "The gun fire was returned"
      },
      "relation": "caused",
      "effect": {
        "span": "a firefight ensued"
      }
    }
  ]
}
```

### --- id=259 ---

输入文本: On Tuesday night tens of thousands of demonstrators packed the city ’ s downtown area for a third night as protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight .

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
      "cause": "protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight",
      "effect": "On Tuesday night tens of thousands of demonstrators packed the city ’ s downtown area for a third night"
    },
    {
      "cause": "Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight",
      "effect": "they would step up their actions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "as protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight ."
      },
      "relation": "caused",
      "effect": {
        "span": "tens of thousands of demonstrators packed the city ’ s downtown area for a third night"
      }
    }
  ]
}
```

### --- id=964 ---

输入文本: Urging the Commission to reveal names of people involved in the attacks , he said the protestors against the church attack were assaulted by police , youth were hunted and criminal cases were booked on them .

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
        "span": "Urging the Commission to reveal names of people involved in the attacks"
      },
      "relation": "caused",
      "effect": {
        "span": "he said the protestors against the church attack were assaulted by police , youth were hunted and criminal cases were booked on them ."
      }
    },
    {
      "cause": {
        "span": "against the church attack"
      },
      "relation": "caused",
      "effect": {
        "span": "the protestors"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=1453 ---

输入文本: Angered community members mobilised and marched to a suspected gang member 's house in Bardien Street where Tavern Moss was stabbed and beaten to death , police said at the time .

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
      "cause": "Tavern Moss was stabbed and beaten to death",
      "effect": "Angered community members mobilised and marched to a suspected gang member 's house in Bardien Street"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Angered community members mobilised and marched to a suspected gang member 's house in Bardien Street"
      },
      "relation": "caused",
      "effect": {
        "span": "Tavern Moss was stabbed and beaten to death"
      }
    }
  ]
}
```

### --- id=835 ---

输入文本: Srinagar in Jammu | PTI SRINAGAR : Tension prevailed at NIT here with outstation students today making a slew of demands , including shifting the institute out of Kashmir and action against the policemen involved in lathicharge yesterday , as an HRD team rushed here from Delhi to resolve the crisis being witnessed since last six days .

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
      "cause": "outstation students today making a slew of demands",
      "effect": "Tension prevailed at NIT here"
    },
    {
      "cause": "to resolve the crisis being witnessed since last six days",
      "effect": "an HRD team rushed here from Delhi"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to resolve the crisis being witnessed since last six days ."
      },
      "relation": "caused",
      "effect": {
        "span": "an HRD team rushed here from Delhi"
      }
    }
  ]
}
```

### --- id=2907 ---

输入文本: VISAKHAPATNAM : Maoists observe bandh in Visakha Agency area October 07 , 2011 00:00 IST Vijayadasami festival coincided with a bandh on Thursday in the Visakha Agency for which the CPI ( Maoist ) gave the call demanding that the police produce in a court of law the party 's Andhra-Orissa border special zone committee member and a central committee member Damodar alias Azad , who was reportedly taken into custody a few days ago .

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
      "cause": "demanding that the police produce in a court of law the party 's Andhra-Orissa border special zone committee member and a central committee member Damodar alias Azad , who was reportedly taken into custody a few days ago",
      "effect": "a bandh on Thursday in the Visakha Agency for which the CPI ( Maoist ) gave the call"
    },
    {
      "cause": "the CPI ( Maoist ) gave the call",
      "effect": "a bandh on Thursday in the Visakha Agency"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding that the police produce in a court of law the party 's Andhra-Orissa border special zone committee member and a central committee member Damodar alias Azad , who was reportedly taken into custody a few days ago ."
      },
      "relation": "caused",
      "effect": {
        "span": "the CPI ( Maoist ) gave the call"
      }
    }
  ]
}
```

### --- id=584 ---

输入文本: 20th July 2015 03:05 AM GUWAHATI : In the aftermath of the murder of two Hindi-speaking persons last week by the Paresh Baruah faction of the banned United Liberation Front of Assam ( Ulfa ) , which also threatened to target the community in the coming days , people took out a march here on Sunday to demonstrate their anger against the outfit .

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
      "cause": "the murder of two Hindi-speaking persons last week by the Paresh Baruah faction of the banned United Liberation Front of Assam ( Ulfa )",
      "effect": "people took out a march here on Sunday to demonstrate their anger against the outfit"
    },
    {
      "cause": "to demonstrate their anger against the outfit",
      "effect": "people took out a march here on Sunday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "In the aftermath of the murder of two Hindi-speaking persons last week by the Paresh Baruah faction of the banned United Liberation Front of Assam ( Ulfa ) , which also threatened to target the community in the coming days"
      },
      "relation": "caused",
      "effect": {
        "span": "people took out a march here on Sunday"
      }
    },
    {
      "cause": {
        "span": "to demonstrate their anger against the outfit ."
      },
      "relation": "caused",
      "effect": {
        "span": "people took out a march here on Sunday"
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

### --- id=853 ---

输入文本: `` If a suitably qualified person had been chosen , such a person would have foreseen that the demonstration would degenerate into violence and prepared for that eventuality , '' said SAHRC said .

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
      "cause": "a suitably qualified person had been chosen",
      "effect": "such a person would have foreseen that the demonstration would degenerate into violence and prepared for that eventuality"
    },
    {
      "cause": "the demonstration",
      "effect": "violence"
    },
    {
      "cause": "such a person would have foreseen that the demonstration would degenerate into violence",
      "effect": "prepared for that eventuality"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "If a suitably qualified person had been chosen"
      },
      "relation": "caused",
      "effect": {
        "span": "such a person would have foreseen that the demonstration would degenerate into violence and prepared for that eventuality"
      }
    }
  ]
}
```

### --- id=1834 ---

输入文本: The official claim that the abductions are the outcome of the Naxalites ’ falling support base , only helps to divert attention from the core issue .

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
      "cause": "the Naxalites ’ falling support base",
      "effect": "the abductions"
    },
    {
      "cause": "The official claim that the abductions are the outcome of the Naxalites ’ falling support base",
      "effect": "divert attention from the core issue"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Naxalites ’ falling support base"
      },
      "relation": "caused",
      "effect": {
        "span": "the abductions"
      }
    }
  ]
}
```

### --- id=1194 ---

输入文本: A day after the snap protest by the Karnataka State Reserve Police ( KSRP ) personnel extending support to their chief P. Ravindranath , who has now been transferred , senior officials on Thursday chalked out a strategy to prevent them from continuing the protest by deploying all the 1,200 KSRP personnel on various duties .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 3,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 3,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 3,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "to prevent them from continuing the protest",
      "effect": "senior officials on Thursday chalked out a strategy"
    },
    {
      "cause": "to prevent them from continuing the protest",
      "effect": "deploying all the 1,200 KSRP personnel on various duties"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "extending support to their chief P. Ravindranath , who has now been transferred ,"
      },
      "relation": "caused",
      "effect": {
        "span": "the snap protest by the Karnataka State Reserve Police ( KSRP ) personnel"
      }
    },
    {
      "cause": {
        "span": "the snap protest by the Karnataka State Reserve Police ( KSRP ) personnel extending support to their chief P. Ravindranath , who has now been transferred ,"
      },
      "relation": "caused",
      "effect": {
        "span": "senior officials on Thursday chalked out a strategy to prevent them from continuing the protest by deploying all the 1,200 KSRP personnel on various duties ."
      }
    },
    {
      "cause": {
        "span": "to prevent them from continuing the protest"
      },
      "relation": "caused",
      "effect": {
        "span": "senior officials on Thursday chalked out a strategy"
      }
    },
    {
      "cause": {
        "span": "by deploying all the 1,200 KSRP personnel on various duties ."
      },
      "relation": "caused",
      "effect": {
        "span": "prevent them from continuing the protest"
      }
    }
  ]
}
```

### --- id=2930 ---

输入文本: 01st July 2010 03:56 AM NEW DELHI : Unnerved by another instance of sudden ambush and massacre of Central Reserve Police Force personnel by Maoists , the Centre on Wednesday gave hint of enacting a tactical retreat from Naxal strongholds like Dantewada and Narayanpur in Chhattisgarh , camouflaging it as ‘ revisiting deployment ’ .

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
      "cause": "another instance of sudden ambush and massacre of Central Reserve Police Force personnel by Maoists",
      "effect": "Unnerved"
    },
    {
      "cause": "Unnerved by another instance of sudden ambush and massacre of Central Reserve Police Force personnel by Maoists",
      "effect": "the Centre on Wednesday gave hint of enacting a tactical retreat from Naxal strongholds like Dantewada and Narayanpur in Chhattisgarh"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Unnerved by another instance of sudden ambush and massacre of Central Reserve Police Force personnel by Maoists"
      },
      "relation": "caused",
      "effect": {
        "span": "the Centre on Wednesday gave hint of enacting a tactical retreat from Naxal strongholds like Dantewada and Narayanpur in Chhattisgarh , camouflaging it as ‘ revisiting deployment ’ ."
      }
    }
  ]
}
```

### --- id=2595 ---

输入文本: But the shutdown success has provided the much-needed shot in the arm to him to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP .

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
      "cause": "the shutdown success",
      "effect": "the much-needed shot in the arm to him to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the shutdown success"
      },
      "relation": "caused",
      "effect": {
        "span": "has provided the much-needed shot in the arm to him to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP ."
      }
    },
    {
      "cause": {
        "span": "to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP ."
      },
      "relation": "caused",
      "effect": {
        "span": "the much-needed shot in the arm to him"
      }
    }
  ]
}
```

### --- id=1590 ---

输入文本: 2 K form human chain to protest blocked road 24th July 2016 06:30 AM BENGALURU : IN an unprecedented show of strength , around 2,000 residents of Somasandrapalya , Haraluru , HSR Layout , Kudlu , Mangamanapalya , Hosapalya and surrounding areas gathered near Ravindra Bharathi Global School in HSR Layout on Saturday and formed a human chain near a wall constructed by Sobha Daffodil apartment .

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
      "cause": "to protest blocked road",
      "effect": "2 K form human chain"
    },
    {
      "cause": "around 2,000 residents of Somasandrapalya , Haraluru , HSR Layout , Kudlu , Mangamanapalya , Hosapalya and surrounding areas gathered near Ravindra Bharathi Global School in HSR Layout on Saturday and formed a human chain near a wall constructed by Sobha Daffodil apartment",
      "effect": "an unprecedented show of strength"
    },
    {
      "cause": "formed a human chain near a wall constructed by Sobha Daffodil apartment",
      "effect": "around 2,000 residents of Somasandrapalya , Haraluru , HSR Layout , Kudlu , Mangamanapalya , Hosapalya and surrounding areas gathered near Ravindra Bharathi Global School in HSR Layout on Saturday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest blocked road"
      },
      "relation": "caused",
      "effect": {
        "span": "around 2,000 residents of Somasandrapalya , Haraluru , HSR Layout , Kudlu , Mangamanapalya , Hosapalya and surrounding areas gathered near Ravindra Bharathi Global School in HSR Layout on Saturday and formed a human chain near a wall constructed by Sobha Daffodil apartment ."
      }
    }
  ]
}
```

### --- id=457 ---

输入文本: The row over possession of Satlok Ashram , headed by Rampal , took a violent turn on Sunday when police tried to stop Arya Pratinidhi Sabha activists from marching towards the Ashram .

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
        "span": "when police tried to stop Arya Pratinidhi Sabha activists from marching towards the Ashram ."
      },
      "relation": "caused",
      "effect": {
        "span": "The row over possession of Satlok Ashram , headed by Rampal , took a violent turn on Sunday"
      }
    }
  ]
}
```

### --- id=439 ---

输入文本: Students under the banner of the Students Federation of India ( SFI ) , Kerala Students Union ( KSU ) , and Muslim Students Federation ( MSF ) expressed solidarity with the protesting students and teachers .

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
        "span": "with the protesting students and teachers ."
      },
      "relation": "caused",
      "effect": {
        "span": "Students under the banner of the Students Federation of India ( SFI ) , Kerala Students Union ( KSU ) , and Muslim Students Federation ( MSF ) expressed solidarity"
      }
    }
  ]
}
```

### --- id=2943 ---

输入文本: “ We arrived in Thanjavur by train on Saturday morning and were taken on a field visit to Big Temple when the assault took place at around 9.30 a.m. Soon after , we were all put in two vehicles immediately and sent to Tiruchi , ” he said .

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
        "span": "when the assault took place at around 9.30 a.m."
      },
      "relation": "caused",
      "effect": {
        "span": "we were all put in two vehicles immediately and sent to Tiruchi"
      }
    }
  ]
}
```

### --- id=2846 ---

输入文本: KARNATAKA Traders against plan to amend APMC Act January 06 , 2007 00:00 IST REST : A farmer takes a nap on a cotton bale at the APMC yard , in Hubli on Friday as the APMC traders across the State observe bandh .

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
        "span": "against plan to amend APMC Act"
      },
      "relation": "caused",
      "effect": {
        "span": "KARNATAKA Traders"
      }
    },
    {
      "cause": {
        "span": "as the APMC traders across the State observe bandh ."
      },
      "relation": "caused",
      "effect": {
        "span": "A farmer takes a nap on a cotton bale at the APMC yard , in Hubli on Friday"
      }
    }
  ]
}
```

### --- id=2122 ---

输入文本: - Indian Express Express News Service , Express News Service : Chandigarh , Tue Aug 20 2013 , 03:19 hrs CHANDIGARH : Panjab University Student Union ( PUSU ) , a student 's organisations of the Panjab University ( PU ) , staged a protest outside the vice-chancellor office on Monday demanding re-appear examination at the earliest to fulfill 50 per cent credit requirement for students in University Institute of Engineering and Technology ( UIET ) .

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
      "cause": "demanding re-appear examination at the earliest",
      "effect": "Panjab University Student Union ( PUSU ) , a student 's organisations of the Panjab University ( PU ) , staged a protest outside the vice-chancellor office on Monday"
    },
    {
      "cause": "to fulfill 50 per cent credit requirement for students in University Institute of Engineering and Technology ( UIET )",
      "effect": "demanding re-appear examination at the earliest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding re-appear examination at the earliest to fulfill 50 per cent credit requirement for students in University Institute of Engineering and Technology ( UIET ) ."
      },
      "relation": "caused",
      "effect": {
        "span": "Panjab University Student Union ( PUSU ) , a student 's organisations of the Panjab University ( PU ) , staged a protest outside the vice-chancellor office on Monday"
      }
    }
  ]
}
```

### --- id=1900 ---

输入文本: June 30 : A DSP and four constables were killed in a landmine blast triggered by suspected CPI-Maoist cadres at Pundigiri village in Bundu , 50 - kilometres from Ranchi .

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
      "cause": "a landmine blast",
      "effect": "A DSP and four constables were killed"
    },
    {
      "cause": "suspected CPI-Maoist cadres at Pundigiri village in Bundu , 50 - kilometres from Ranchi",
      "effect": "a landmine blast"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "triggered by suspected CPI-Maoist cadres"
      },
      "relation": "caused",
      "effect": {
        "span": "a landmine blast"
      }
    },
    {
      "cause": {
        "span": "in a landmine blast triggered by suspected CPI-Maoist cadres at Pundigiri village in Bundu , 50 - kilometres from Ranchi ."
      },
      "relation": "caused",
      "effect": {
        "span": "A DSP and four constables were killed"
      }
    }
  ]
}
```

### --- id=736 ---

输入文本: The police questioned Sanmugavel regarding the threat call to Nehru .

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
        "span": "regarding the threat call to Nehru ."
      },
      "relation": "caused",
      "effect": {
        "span": "The police questioned Sanmugavel"
      }
    }
  ]
}
```

### --- id=2951 ---

输入文本: During the trial , Shahzad had called as defence witnesses Saif and Zeeshan , both lodged in Sabarmati jail in Ahmedabad in connection with the serial blasts of July 26 , 2008 there , claiming that he was not at the spot .

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
        "span": "claiming that he was not at the spot ."
      },
      "relation": "caused",
      "effect": {
        "span": "Shahzad had called as defence witnesses Saif and Zeeshan , both lodged in Sabarmati jail in Ahmedabad in connection with the serial blasts of July 26 , 2008 there"
      }
    }
  ]
}
```

### --- id=333 ---

输入文本: Although everyone is keenly aware of how the power of the internet helped foster the massive march in 2003 , for now there are hotter topics in local cyberspace .

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
        "span": "the power of the internet"
      },
      "relation": "caused",
      "effect": {
        "span": "helped foster the massive march in 2003"
      }
    }
  ]
}
```

### --- id=1821 ---

输入文本: A senior police officer , who declined to be quoted on the ground that investigations were still on , told The Hindu that whether the ULFA denied it or not , the police suspected the twin blasts to be the handiwork of the militant outfit .

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
      "cause": "investigations were still",
      "effect": "A senior police officer , who declined to be quoted"
    },
    {
      "cause": "the twin blasts",
      "effect": "the militant outfit"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "investigations were still on"
      },
      "relation": "caused",
      "effect": {
        "span": "who declined to be quoted on the ground that investigations were still on"
      }
    }
  ]
}
```

### --- id=2088 ---

输入文本: `` Our disappointment is that the violence occurred after attempts earlier in the day by my office to receive a memorandum from the community . ''

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
      "cause": "attempts earlier in the day by my office to receive a memorandum from the community",
      "effect": "the violence occurred"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after attempts earlier in the day by my office to receive a memorandum from the community"
      },
      "relation": "caused",
      "effect": {
        "span": "the violence occurred"
      }
    },
    {
      "cause": {
        "span": "to receive a memorandum from the community"
      },
      "relation": "caused",
      "effect": {
        "span": "attempts earlier in the day by my office"
      }
    }
  ]
}
```

### --- id=1143 ---

输入文本: Anger about the policy among Han Chinese , by far the largest group among China 's 56 ethnic communities , has been exacerbated by the deaths of 192 people , mostly Han , in Xinjiang 's capital Urumqi , last week , and the injuries suffered by 1,680 people during clashes between the province 's Uygur Muslim minority and Han Chinese .

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
      "cause": "the deaths of 192 people , mostly Han , in Xinjiang 's capital Urumqi , last week , and the injuries suffered by 1,680 people during clashes between the province 's Uygur Muslim minority and Han Chinese",
      "effect": "Anger about the policy among Han Chinese , by far the largest group among China 's 56 ethnic communities , has been exacerbated"
    },
    {
      "cause": "the policy",
      "effect": "Anger"
    },
    {
      "cause": "clashes between the province 's Uygur Muslim minority and Han Chinese",
      "effect": "the deaths of 192 people , mostly Han , in Xinjiang 's capital Urumqi , last week , and the injuries suffered by 1,680 people"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the deaths of 192 people , mostly Han , in Xinjiang 's capital Urumqi , last week"
      },
      "relation": "caused",
      "effect": {
        "span": "Anger about the policy among Han Chinese , by far the largest group among China 's 56 ethnic communities , has been exacerbated"
      }
    },
    {
      "cause": {
        "span": "the injuries suffered by 1,680 people during clashes between the province 's Uygur Muslim minority and Han Chinese ."
      },
      "relation": "caused",
      "effect": {
        "span": "Anger about the policy among Han Chinese , by far the largest group among China 's 56 ethnic communities , has been exacerbated"
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
    "fp": 1,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
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
        "span": "to express sorrow"
      },
      "relation": "caused",
      "effect": {
        "span": "the Leader of Opposition ( LoP ) Prem Kumar meeting the family members of the victim"
      }
    },
    {
      "cause": {
        "span": "to protest against the murder ."
      },
      "relation": "caused",
      "effect": {
        "span": "people who had blocked road near Mahabir bridge"
      }
    }
  ]
}
```

### --- id=3021 ---

输入文本: Soon , the huge posse of advocates started raising defamatory slogans against a few judges .

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
        "span": "against a few judges ."
      },
      "relation": "caused",
      "effect": {
        "span": "the huge posse of advocates started raising defamatory slogans"
      }
    }
  ]
}
```

### --- id=404 ---

输入文本: Nokia Supplier 's Turn to Offer VRS ; 850 Staffers Strike Work 22nd June 2014 07:37 AM CHENNAI : The ripple effect of the drastic downsizing of Nokia ’ s Sriperumbudur plant was felt in another ancillary company , as BYD Electronics India Private Ltd announced a VRS offer for its 1,500 employees .

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
        "span": "the drastic downsizing of Nokia ’ s Sriperumbudur plant"
      },
      "relation": "caused",
      "effect": {
        "span": "The ripple effect of the drastic downsizing of Nokia ’ s Sriperumbudur plant was felt in another ancillary company , as BYD Electronics India Private Ltd announced a VRS offer for its 1,500 employees ."
      }
    }
  ]
}
```

### --- id=3029 ---

输入文本: The journalist who had put out a report to that effect was manhandled .

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
        "span": "who had put out a report to that effect"
      },
      "relation": "caused",
      "effect": {
        "span": "The journalist who had put out a report to that effect was manhandled ."
      }
    }
  ]
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
        "span": "to pressurise the government to solve the farmers problems ."
      },
      "relation": "caused",
      "effect": {
        "span": "Telugu Desam president Nara Chandrababu Naidu has called upon the cadre and people to be prepared to march to the State capital and if necessary , to the Assembly"
      }
    }
  ]
}
```

### --- id=948 ---

输入文本: A civilian was also abducted along with the troopers either on suspicion of being a policeman or for interfering in the abduction , he added .

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
      "cause": "either on suspicion of being a policeman or for interfering in the abduction",
      "effect": "A civilian was also abducted along with the troopers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "on suspicion of being a policeman"
      },
      "relation": "caused",
      "effect": {
        "span": "A civilian was also abducted along with the troopers"
      }
    },
    {
      "cause": {
        "span": "for interfering in the abduction"
      },
      "relation": "caused",
      "effect": {
        "span": "A civilian was also abducted along with the troopers"
      }
    }
  ]
}
```

### --- id=2944 ---

输入文本: “ He is also found guilty of assaulting police officers and obstructing them from doing their duty , ” he said .

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
      "cause": "assaulting police officers and obstructing them from doing their duty",
      "effect": "He is also found guilty"
    }
  ],
  "pred_triples": []
}
```

### --- id=2610 ---

输入文本: Top ULFA bomber killed in Assam 05th September 2009 10:34 PM GUWAHATI : A top separatist bomber and close associate of Paresh Baruah , commander-in-chief of the outlawed United Liberation Front of Asom ( ULFA ) , was killed in a gunfight with security forces in Assam Saturday , officials said .

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
        "span": "a gunfight with security forces in Assam Saturday"
      },
      "relation": "caused",
      "effect": {
        "span": "A top separatist bomber and close associate of Paresh Baruah , commander-in-chief of the outlawed United Liberation Front of Asom ( ULFA ) , was killed"
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
        "span": "Senior teachers agreed that the university administration had made a smart move to conduct classes even as the exams were boycotted"
      }
    },
    {
      "cause": {
        "span": "to ensure that the mandatory instruction days were met with ."
      },
      "relation": "caused",
      "effect": {
        "span": "the university administration had made a smart move to conduct classes even as the exams were boycotted"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
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
        "span": "when government turned down their demand to adopt a resolution urging Centre to withdraw recent hike in fuel prices and the decision on deregulation of petrol ."
      },
      "relation": "caused",
      "effect": {
        "span": "the entire opposition - TDP , CPI , CPI(M) and PDF staged a walk out"
      }
    },
    {
      "cause": {
        "span": "to adopt a resolution urging Centre to withdraw recent hike in fuel prices and the decision on deregulation of petrol ."
      },
      "relation": "caused",
      "effect": {
        "span": "their demand"
      }
    }
  ]
}
```

### --- id=126 ---

输入文本: The taxi strike that left commuters stranded in Johannesburg was expected to also disrupt matric pupils writing exams on Monday , the Gauteng education department said .

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
      "cause": "The taxi strike",
      "effect": "that left commuters stranded in Johannesburg was expected to also disrupt matric pupils writing exams on Monday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The taxi strike"
      },
      "relation": "caused",
      "effect": {
        "span": "that left commuters stranded in Johannesburg"
      }
    }
  ]
}
```

### --- id=2019 ---

输入文本: Dethrone Naveen government : Congress 07th September 2012 12:07 PM Buoyed by the massive turnout at the ‘ Parivartan ’ rally , Congress leaders on Thursday gave a clarion call to party workers and supporters to dethrone Naveen Patnaik Government in the 2014 general elections .

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
      "cause": "the massive turnout at the ‘ Parivartan ’ rally",
      "effect": "Buoyed"
    },
    {
      "cause": "Buoyed by the massive turnout at the ‘ Parivartan ’ rally",
      "effect": "Congress leaders on Thursday gave a clarion call to party workers and supporters to dethrone Naveen Patnaik Government in the 2014 general elections"
    },
    {
      "cause": "to dethrone Naveen Patnaik Government in the 2014 general elections",
      "effect": "Congress leaders on Thursday gave a clarion call to party workers and supporters"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Buoyed by the massive turnout at the ‘ Parivartan ’ rally"
      },
      "relation": "caused",
      "effect": {
        "span": "Congress leaders on Thursday gave a clarion call to party workers and supporters to dethrone Naveen Patnaik Government in the 2014 general elections ."
      }
    },
    {
      "cause": {
        "span": "to dethrone Naveen Patnaik Government in the 2014 general elections ."
      },
      "relation": "caused",
      "effect": {
        "span": "Congress leaders on Thursday gave a clarion call to party workers and supporters"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
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
        "span": "clashes between police and protesters demanding shifting of proposed AIIMS in Assam from Changsari to Raha ."
      },
      "relation": "caused",
      "effect": {
        "span": "one person identified as Mintu Deori was killed during a protest"
      }
    },
    {
      "cause": {
        "span": "clashes between police and protesters demanding shifting of proposed AIIMS in Assam from Changsari to Raha ."
      },
      "relation": "caused",
      "effect": {
        "span": "20 others , including two Additional SPs , were injured"
      }
    },
    {
      "cause": {
        "span": "demanding shifting of proposed AIIMS in Assam from Changsari to Raha ."
      },
      "relation": "caused",
      "effect": {
        "span": "clashes between police and protesters"
      }
    }
  ]
}
```

### --- id=1455 ---

输入文本: Traffic was held up for an hour following rasta roko by students who were literally dragged away by police and SRP personnel and whisked away to Azad Maidan police station in police vans .

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
      "cause": "rasta roko by students",
      "effect": "Traffic was held up for an hour"
    },
    {
      "cause": "Traffic was held up for an hour following rasta roko by students",
      "effect": "who were literally dragged away by police and SRP personnel and whisked away to Azad Maidan police station in police vans"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "following rasta roko by students who were literally dragged away by police and SRP personnel and whisked away to Azad Maidan police station in police vans ."
      },
      "relation": "caused",
      "effect": {
        "span": "Traffic was held up for an hour"
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
        "span": "against water shortage in Mumbai India Thursday ."
      },
      "relation": "caused",
      "effect": {
        "span": "A boy holding an empty bucket participates along with others in a protest"
      }
    }
  ]
}
```

### --- id=2298 ---

输入文本: Ramaphosa promises instant response to violence against women and children in SA Songezo Ndlendle CAPE TOWN , September 5 ( ANA ) - South Africa President Cyril Ramaphosa on Thursday addressed thousands of protesters outside Parliament following Wednesday 's mass gathering against the abuse and violence directed at women and children outside the meeting venue of the World Economic Forum in Cape Town .

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
        "span": "following Wednesday 's mass gathering against the abuse and violence directed at women and children outside the meeting venue of the World Economic Forum in Cape Town ."
      },
      "relation": "caused",
      "effect": {
        "span": "South Africa President Cyril Ramaphosa on Thursday addressed thousands of protesters outside Parliament"
      }
    },
    {
      "cause": {
        "span": "against the abuse and violence directed at women and children outside the meeting venue of the World Economic Forum in Cape Town ."
      },
      "relation": "caused",
      "effect": {
        "span": "Wednesday 's mass gathering"
      }
    }
  ]
}
```

### --- id=2396 ---

输入文本: Posted : Thu Apr 02 1998 IST BHOPAL , April 1 : An Indian people 's tribunal to be presided over by former Bombay High Court judge B N Deshmukh will reach Multai in Betul district on April 8 to investigate the circumstances of the police firing on agitating farmers on January 12 which had resulted in the death of 19 persons .

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
      "cause": "to investigate the circumstances of the police firing on agitating farmers on January 12 which had resulted in the death of 19 persons",
      "effect": "An Indian people 's tribunal to be presided over by former Bombay High Court judge B N Deshmukh will reach Multai in Betul district on April 8"
    },
    {
      "cause": "the police firing on agitating farmers on January 12",
      "effect": "the death of 19 persons"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the police firing on agitating farmers on January 12"
      },
      "relation": "caused",
      "effect": {
        "span": "which had resulted in the death of 19 persons ."
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

### --- id=603 ---

输入文本: 26 Mar 2014 A prominent journalist who has been held in detention for 10 months after protesting against the demolition of homes in Shandong province has been freed on bail .

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
      "cause": "protesting against the demolition of homes in Shandong province",
      "effect": "A prominent journalist who has been held in detention for 10 months"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after protesting against the demolition of homes in Shandong province"
      },
      "relation": "caused",
      "effect": {
        "span": "A prominent journalist who has been held in detention for 10 months"
      }
    },
    {
      "cause": {
        "span": "against the demolition of homes in Shandong province"
      },
      "relation": "caused",
      "effect": {
        "span": "protesting against the demolition of homes in Shandong province"
      }
    }
  ]
}
```

### --- id=437 ---

输入文本: When the education authorities conducted the meet on Friday afternoon , physical education students and teachers staged a protest by sitting on the tracks at the meet grounds .

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
      "cause": "physical education students and teachers staged a protest",
      "effect": "sitting on the tracks at the meet grounds"
    }
  ],
  "pred_triples": []
}
```

### --- id=683 ---

输入文本: Vijaykumar , Assistant Director of the Agriculture Department , who rushed to the spot on being informed that farmers were staging a dharna in front of the department , assured the protesters that he would meet their demands in 15 days .

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
        "span": "that farmers were staging a dharna in front of the department"
      },
      "relation": "caused",
      "effect": {
        "span": "Vijaykumar , Assistant Director of the Agriculture Department , who rushed to the spot on being informed"
      }
    }
  ]
}
```

### --- id=801 ---

输入文本: Thiruvananthapuram : Protest against assault on woman in Kochi June 25 , 2011 00:00 IST Dozens of people , including women , took out a ‘ Freedom Walk ' through the main thoroughfare of the city on Thursday midnight in protest against the alleged assault on Tasni Banu , a woman BPO employee of the Infopark in Kochi a few days ago .

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
      "cause": "against assault on woman in Kochi",
      "effect": "Protest"
    },
    {
      "cause": "in protest against the alleged assault on Tasni Banu , a woman BPO employee of the Infopark in Kochi a few days ago",
      "effect": "Dozens of people , including women , took out a ‘ Freedom Walk ' through the main thoroughfare of the city on Thursday midnight"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the alleged assault on Tasni Banu , a woman BPO employee of the Infopark in Kochi a few days ago ."
      },
      "relation": "caused",
      "effect": {
        "span": "Dozens of people , including women , took out a ‘ Freedom Walk ' through the main thoroughfare of the city on Thursday midnight"
      }
    }
  ]
}
```

### --- id=1392 ---

输入文本: Violence erupted on Tuesday when the Democratic Alliance showed support for the subsidy by marching to Cosatu 's headquarters in Johannesburg .

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
      "cause": "marching to Cosatu 's headquarters in Johannesburg",
      "effect": "Violence erupted on Tuesday"
    },
    {
      "cause": "the subsidy",
      "effect": "the Democratic Alliance showed support"
    },
    {
      "cause": "the Democratic Alliance showed support",
      "effect": "marching to Cosatu 's headquarters in Johannesburg"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when the Democratic Alliance showed support for the subsidy by marching to Cosatu 's headquarters in Johannesburg ."
      },
      "relation": "caused",
      "effect": {
        "span": "Violence erupted on Tuesday"
      }
    },
    {
      "cause": {
        "span": "for the subsidy"
      },
      "relation": "caused",
      "effect": {
        "span": "the Democratic Alliance showed support"
      }
    }
  ]
}
```

### --- id=1158 ---

输入文本: Earlier , residents gathered outside the police station to protest about the murders .

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
      "effect": "residents gathered outside the police station"
    },
    {
      "cause": "the murders",
      "effect": "to protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest about the murders ."
      },
      "relation": "caused",
      "effect": {
        "span": "residents gathered outside the police station"
      }
    }
  ]
}
```

### --- id=414 ---

输入文本: " People shouted out things , which were so provoking we were very worried [ the man ] would jump in many instances , " Cheung said .

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
        "span": "People shouted out things , which were so provoking"
      },
      "relation": "caused",
      "effect": {
        "span": "we were very worried [ the man ] would jump in many instances"
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
      "cause": "to carry out a series of terror attacks in China including a May 2014 market bombing in the capital Urumqi and an attack in Beijing ’ s Tiananmen Square in October 2013",
      "effect": "radicals with links to Xinjiang use vehicles"
    }
  ],
  "pred_triples": []
}
```

### --- id=2902 ---

输入文本: Residents chanted songs drowning out the mayor , who had to be removed from the stadium under police escort .

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
        "span": "Residents chanted songs drowning out the mayor"
      },
      "relation": "caused",
      "effect": {
        "span": "who had to be removed from the stadium under police escort ."
      }
    }
  ]
}
```

### --- id=2018 ---

输入文本: Another restaurant owner , Clara Li , said owners wanted to take their protest further , but had not yet settled on a plan to do so if their demands were not met after yesterday 's protest .

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
      "cause": "their demands were not met after yesterday 's protest",
      "effect": "owners wanted to take their protest further"
    }
  ],
  "pred_triples": []
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
        "span": "followed a complaint by the Council for the Advancement of the SA Constitution ."
      },
      "relation": "caused",
      "effect": {
        "span": "The SAHRC investigated Tatane 's death , during a protest in Ficksburg in April 2011"
      }
    }
  ]
}
```

### --- id=2609 ---

输入文本: Jitin Das , among them , resorted to fast unto death and died on the 63rd day of his fast ( September 13 ) , he said .

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
      "cause": "Jitin Das , among them , resorted to fast unto death",
      "effect": "died on the 63rd day of his fast ( September 13 )"
    }
  ],
  "pred_triples": []
}
```

### --- id=2262 ---

输入文本: When the Opposition members boycotted the House proceedings of the day at the end of their virulent protests and demands for the resignation of ‘ corrupt ’ Chief Minister Oommen Chandy and Excise Minister K Babu , an anxious crowd of Assembly staff and watch and ward personnel were looking at the crown of a big coconut tree , where a middle-aged person was staging a protest under the scorching sun and swaying palm fronds .

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
        "span": "at the end of their virulent protests and demands for the resignation of ‘ corrupt ’ Chief Minister Oommen Chandy and Excise Minister K Babu"
      },
      "relation": "caused",
      "effect": {
        "span": "the Opposition members boycotted the House proceedings of the day"
      }
    }
  ]
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
        "span": "against atrocities"
      },
      "relation": "caused",
      "effect": {
        "span": "The Bhim Army and other Dalit groups were refused permission to organise a rally"
      }
    },
    {
      "cause": {
        "span": "The Bhim Army and other Dalit groups were refused permission to organise a rally against atrocities on May 9"
      },
      "relation": "caused",
      "effect": {
        "span": "sparking off violence and vandalism , with several vehicles and buses burnt ."
      }
    }
  ]
}
```

### --- id=1578 ---

输入文本: December 01 , 2010 00:00 IST A large number of CPI activists took out a procession in protest against the Centre 's failure to contain prices of essential commodities and also against the land scams reported in the State .

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
      "cause": "in protest against the Centre 's failure to contain prices of essential commodities and also against the land scams reported in the State",
      "effect": "A large number of CPI activists took out a procession"
    },
    {
      "cause": "against the Centre 's failure to contain prices of essential commodities and also against the land scams reported in the State",
      "effect": "large number of CPI activists took out a procession in protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the Centre 's failure to contain prices of essential commodities and also against the land scams reported in the State ."
      },
      "relation": "caused",
      "effect": {
        "span": "A large number of CPI activists took out a procession"
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
      "cause": "chanting struggle songs and holding posters on which was written `` enough is enough '' and `` stop killing women and children ''",
      "effect": "On Wednesday , a crowd , made up of mainly young people from various civil community organisations and students from universities and schools across the city , gathered outside the CTICC"
    }
  ],
  "pred_triples": []
}
```

### --- id=30 ---

输入文本: The Kishtwar area has been in focus ever since the Delhi High Court blast as the first of the e—mails claiming responsibility for the blast emanated from here .

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
        "span": "as the first of the e—mails claiming responsibility for the blast emanated from here ."
      },
      "relation": "caused",
      "effect": {
        "span": "The Kishtwar area has been in focus ever since the Delhi High Court blast"
      }
    }
  ]
}
```

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
        "span": "demanding the arrest of ‘ real culprits ' behind the vandalism ."
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
        "span": "in the wake of India 's loss to West Indies in the World T 20 Cup"
      },
      "relation": "caused",
      "effect": {
        "span": "clashes"
      }
    },
    {
      "cause": {
        "span": "following clashes in the wake of India 's loss to West Indies in the World T 20 Cup"
      },
      "relation": "caused",
      "effect": {
        "span": "the NIT campus , which has been gripped by tension"
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
        "span": "since ethnic riots in China ’ s far west in 2009"
      },
      "relation": "caused",
      "effect": {
        "span": "The popular social network has been blocked"
      }
    },
    {
      "cause": {
        "span": "during pro-democracy protests in Hong Kong in 2014"
      },
      "relation": "caused",
      "effect": {
        "span": "Instagram was banned"
      }
    }
  ]
}
```

### --- id=2279 ---

输入文本: Anti-government protesters in Hong Kong took over key roads early on Monday amid rising tensions ahead of what expected to be a huge pro-democracy rally on the anniversary of the city ’ s handover to China .

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
        "span": "amid rising tensions ahead of what expected to be a huge pro-democracy rally on the anniversary of the city ’ s handover to China ."
      },
      "relation": "caused",
      "effect": {
        "span": "Anti-government protesters in Hong Kong took over key roads early on Monday"
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
        "span": "against the mining company in Johannesburg"
      },
      "relation": "caused",
      "effect": {
        "span": "a protest"
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

### --- id=2528 ---

输入文本: Nine persons have been arrested so far since the incident happened on Sunday night when the 21 - year-old Tanzanian student went through the ordeal in vigilante justice by an angry mob in a case of " mistaken identity " after a woman was mowed down by a car driven by a Sudanese here .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
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
        "span": "since the incident happened on Sunday night"
      },
      "relation": "caused",
      "effect": {
        "span": "Nine persons have been arrested so far"
      }
    },
    {
      "cause": {
        "span": "in a case of \" mistaken identity \""
      },
      "relation": "caused",
      "effect": {
        "span": "the 21 - year-old Tanzanian student went through the ordeal in vigilante justice by an angry mob"
      }
    },
    {
      "cause": {
        "span": "after a woman was mowed down by a car driven by a Sudanese here ."
      },
      "relation": "caused",
      "effect": {
        "span": "the 21 - year-old Tanzanian student went through the ordeal in vigilante justice by an angry mob"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
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
        "span": "when it tried to land in a conflict zone in Sukma district to rescue a few troopers who had received gunshots in an encounter ."
      },
      "relation": "caused",
      "effect": {
        "span": "Rebels opened fire on the IAF chopper"
      }
    },
    {
      "cause": {
        "span": "to rescue a few troopers who had received gunshots in an encounter ."
      },
      "relation": "caused",
      "effect": {
        "span": "it tried to land in a conflict zone in Sukma district"
      }
    },
    {
      "cause": {
        "span": "in an encounter ."
      },
      "relation": "caused",
      "effect": {
        "span": "a few troopers who had received gunshots"
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
        "span": "Jat quota stir"
      },
      "relation": "caused",
      "effect": {
        "span": "Haryana , which has been hit by Jat quota stir"
      }
    },
    {
      "cause": {
        "span": "fighting militants in Pulwama district of Jammu and Kashmir"
      },
      "relation": "caused",
      "effect": {
        "span": "23 - year-old Capt Pawan Kumar , who died"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
}
```

### --- id=2639 ---

输入文本: Today 's Paper Fiery protest YSR Congress activists take out a candlelight rally on Necklace Road on Monday to protest the delay in bail to Y.S. Jaganmohan Reddy .

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
      "cause": "to protest the delay in bail to Y.S. Jaganmohan Reddy",
      "effect": "Today 's Paper Fiery protest YSR Congress activists take out a candlelight rally on Necklace Road on Monday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest the delay in bail to Y.S. Jaganmohan Reddy ."
      },
      "relation": "caused",
      "effect": {
        "span": "YSR Congress activists take out a candlelight rally on Necklace Road on Monday"
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
        "span": "Women took to streets carrying pots"
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
        "span": "to stop the screening"
      },
      "relation": "caused",
      "effect": {
        "span": "I am warning other theatres"
      }
    }
  ]
}
```
