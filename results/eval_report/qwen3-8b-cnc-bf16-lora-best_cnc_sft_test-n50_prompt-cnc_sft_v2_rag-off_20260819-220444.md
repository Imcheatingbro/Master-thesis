# qwen3-8b-cnc-bf16-lora-best CNC SFT held-out test eval report

## 配置
```json
{
  "label": "qwen3-8b-cnc-bf16-lora-best CNC SFT held-out test",
  "model": "qwen3-8b-cnc-bf16-lora-best",
  "dataset": "cnc_sft_test",
  "sample_count": 50,
  "prompt_name": "cnc_sft_v2",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 0,
  "temperature": 0.0,
  "max_tokens": 512,
  "progress_every": 10,
  "max_workers": 1,
  "llm_provider": "openai_compatible",
  "llm_base_url": "http://127.0.0.1:8000/v1",
  "context_length": null,
  "reasoning_effort": null,
  "llm_extra_body": null,
  "api_key_source": "local LLaMA-Factory API",
  "report_detail_limit": 200,
  "report_detail_mode": "errors",
  "report_error_metric": "strict_token_f1",
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ qwen3-8b-cnc-bf16-lora-best CNC SFT held-out test final report ================
样本总数: 50
  Gold 含因果: 27 | Pred 含因果: 23
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.840
  Precision: 0.913
  Recall   : 0.778
  F1       : 0.840
  (TP=21, TN=21, FP=2, FN=6)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 50
    Gold triples: 41 | Pred triples: 34
    Precision: 0.618
    Recall   : 0.512
    F1       : 0.560
    (TP=21, FP=13, FN=20)
  [anchor_window]
    样本数: 50
    Gold triples: 41 | Pred triples: 34
    Precision: 0.294
    Recall   : 0.244
    F1       : 0.267
    (TP=10, FP=24, FN=31)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 21
    Gold triples: 33 | Pred triples: 32
    Precision: 0.656
    Recall   : 0.636
    F1       : 0.646
    (TP=21, FP=11, FN=12)
  [anchor_window]
    样本数: 21
    Gold triples: 33 | Pred triples: 32
    Precision: 0.312
    Recall   : 0.303
    F1       : 0.308
    (TP=10, FP=22, FN=23)
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

Sample details shown: all 19 wrong samples from 50 total samples.

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
        "span": "to prevent villagers funding a journey to Beijing to continue their petitioning"
      },
      "relation": "caused",
      "effect": {
        "span": "officials have frozen that money"
      }
    }
  ]
}
```

### --- id=2070 ---

输入文本: 17th November 2012 11:20 AM Squarely blaming the Pattali Makkal Katchi ( PMK ) for orchestrating the violence against Dalits in three villages in Dharmapuri , VCK leader Thol Thirumavalavan on Friday demanded a CBI investigation into the matter and action against those openly instigating caste violence on public platforms .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 4,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 4,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 4,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "orchestrating the violence against Dalits in three villages in Dharmapuri",
      "effect": "Squarely blaming the Pattali Makkal Katchi ( PMK )"
    },
    {
      "cause": "Squarely blaming the Pattali Makkal Katchi ( PMK ) for orchestrating the violence against Dalits in three villages in Dharmapuri",
      "effect": "VCK leader Thol Thirumavalavan on Friday demanded a CBI investigation into the matter and action against those openly instigating caste violence on public platforms"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "orchestrating the violence against Dalits in three villages in Dharmapuri"
      },
      "relation": "caused",
      "effect": {
        "span": "Squarely blaming the Pattali Makkal Katchi ( PMK )"
      }
    },
    {
      "cause": {
        "span": "against Dalits in three villages in Dharmapuri"
      },
      "relation": "caused",
      "effect": {
        "span": "orchestrating the violence"
      }
    },
    {
      "cause": {
        "span": "the violence against Dalits in three villages in Dharmapuri"
      },
      "relation": "caused",
      "effect": {
        "span": "Squarely blaming the Pattali Makkal Katchi ( PMK )"
      }
    },
    {
      "cause": {
        "span": "the violence"
      },
      "relation": "caused",
      "effect": {
        "span": "against Dalits in three villages in Dharmapuri"
      }
    },
    {
      "cause": {
        "span": "a CBI investigation into the matter and action against those openly instigating caste violence on public platforms"
      },
      "relation": "caused",
      "effect": {
        "span": "VCK leader Thol Thirumavalavan on Friday demanded"
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
    "tp": 0,
    "fp": 2,
    "fn": 3
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
        "span": "he caused uproar in some quarters by expressing support for the police's handling of a protest in Mong Kok at which rival groups clashed over a teacher's verbal attack on officers"
      },
      "relation": "caused",
      "effect": {
        "span": "Leung Chun-ying's second meet-the-public session, in Kwun Tong, was a much quieter affair than his first one last week"
      }
    },
    {
      "cause": {
        "span": "rival groups clashed over a teacher's verbal attack on officers"
      },
      "relation": "caused",
      "effect": {
        "span": "a protest in Mong Kok"
      }
    }
  ]
}
```

### --- id=1338 ---

输入文本: Meanwhile , protesting against the attack , RTC staff observed a bandh ; no RTC bus in the district plied today as they parked them on the main thoroughfare , putting the public to great inconvenience .

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
      "cause": "protesting against the attack",
      "effect": "RTC staff observed a bandh"
    },
    {
      "cause": "they parked them on the main thoroughfare",
      "effect": "no RTC bus in the district plied today"
    },
    {
      "cause": "they parked them on the main thoroughfare",
      "effect": "putting the public to great inconvenience"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "protesting against the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "RTC staff observed a bandh"
      }
    },
    {
      "cause": {
        "span": "they parked them on the main thoroughfare"
      },
      "relation": "caused",
      "effect": {
        "span": "no RTC bus in the district plied today"
      }
    },
    {
      "cause": {
        "span": "no RTC bus in the district plied today"
      },
      "relation": "caused",
      "effect": {
        "span": "putting the public to great inconvenience"
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
        "span": "I was clicking pictures"
      },
      "relation": "caused",
      "effect": {
        "span": "Some protesters attacked me"
      }
    }
  ]
}
```

### --- id=2418 ---

输入文本: New Delhi : Centre to hold talks to end Manipur crisis

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
      "cause": "to end Manipur crisis",
      "effect": "Centre to hold talks"
    }
  ],
  "pred_triples": []
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
        "span": "' Sadak Bandh'called by Telangana Joint Action Committee ( JAC )"
      },
      "relation": "caused",
      "effect": {
        "span": "Police arrested leaders of various political parties who squatted on the highway"
      }
    },
    {
      "cause": {
        "span": "to urge the central government to immediately carve out a Telangana state"
      },
      "relation": "caused",
      "effect": {
        "span": "' Sadak Bandh'called by Telangana Joint Action Committee ( JAC )"
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
      "cause": "who also sustained injuries",
      "effect": "Akilan was admitted to hospital here along with member of rivaal group Stalin Dinakaraj"
    },
    {
      "cause": "the melee",
      "effect": "who also sustained injuries"
    }
  ],
  "pred_triples": []
}
```

### --- id=2605 ---

输入文本: Political Prisoners ' Rights Day today 13th September 2013 08:33 AM The Committee for the Release of Political Prisoners ( CRPP ) is observing September 13 as Political Prisoners Rights Day , commemorating the sacrifice of Shaheed Jitin Das and organising a memorial programme for Maoist idealogue Ganti Prasadam , in Hyderabad on the occasion .

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
      "cause": "The Committee for the Release of Political Prisoners ( CRPP ) is observing September 13 as Political Prisoners Rights Day",
      "effect": "commemorating the sacrifice of Shaheed Jitin Das and organising a memorial programme for Maoist idealogue Ganti Prasadam , in Hyderabad on the occasion"
    }
  ],
  "pred_triples": []
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
        "span": "an intention of causing mass destruction to the train and passengers"
      },
      "relation": "caused",
      "effect": {
        "span": "two persons, who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district"
      }
    },
    {
      "cause": {
        "span": "two persons, who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district with an intention of causing mass destruction to the train and passengers"
      },
      "relation": "caused",
      "effect": {
        "span": "were detained under the National Security Act in December"
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

### --- id=2338 ---

输入文本: Pakistan has arrested seven suspected terrorists of the Lashkar-e-Taiba terror outfit , including its founding member Zakiur Rehman Lakhvi , who face charges of planning , financing and facilitating the Mumbai attack .

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
      "cause": "planning , financing and facilitating the Mumbai attack",
      "effect": "Pakistan has arrested seven suspected terrorists of the Lashkar-e-Taiba terror outfit , including its founding member Zakiur Rehman Lakhvi"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "who face charges of planning, financing and facilitating the Mumbai attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Pakistan has arrested seven suspected terrorists of the Lashkar-e-Taiba terror outfit, including its founding member Zakiur Rehman Lakhvi"
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
      "cause": "expressing concern at the growing violence against Muslims by vigilante groups and has urged the Minister to work towards creating a sense of security amongst the minorities",
      "effect": "National Commission for Minorities ( NCM ) chairperson Naseem Ahmad has written to Union Home Minister Rajnath Singh"
    },
    {
      "cause": "the growing violence against Muslims by vigilante groups",
      "effect": "expressing concern"
    }
  ],
  "pred_triples": []
}
```

### --- id=1669 ---

输入文本: Lam called a rare press conference early on Tuesday to condemn the “ extremely violent ” storming of the legislature , which she described as “ heartbreaking and shocking ” .

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
      "cause": "to condemn the “ extremely violent ” storming of the legislature",
      "effect": "Lam called a rare press conference early on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to condemn the “ extremely violent ” storming of the legislature, which she described as “ heartbreaking and shocking ”"
      },
      "relation": "caused",
      "effect": {
        "span": "Lam called a rare press conference early on Tuesday"
      }
    }
  ]
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
        "span": "NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections"
      },
      "relation": "caused",
      "effect": {
        "span": "The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram"
      }
    },
    {
      "cause": {
        "span": "it did not want Achuthanandan to come back to power for another term"
      },
      "relation": "caused",
      "effect": {
        "span": "the NSS did not support the LDF in the recent Assembly elections"
      }
    }
  ]
}
```

### --- id=1931 ---

输入文本: Five members of the old group entered the church during the Sunday mass yesterday and assaulted Akilan injuring him .

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
      "cause": "assaulted Akilan",
      "effect": "injuring him"
    }
  ],
  "pred_triples": []
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
      "cause": "pelting them with stones when they approached with a proposal to accept their demands",
      "effect": "brick kiln owners have charged the protesters"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they approached with a proposal to accept their demands"
      },
      "relation": "caused",
      "effect": {
        "span": "the brick kiln owners have charged the protesters with pelting them with stones"
      }
    }
  ]
}
```

### --- id=2753 ---

输入文本: The march , which began with only a few hundred people at around 10am in Phahameng , had attracted more than 5,000 once it had reached the city centre at lunch time .

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
        "span": "it had reached the city centre at lunch time"
      },
      "relation": "caused",
      "effect": {
        "span": "The march, which began with only a few hundred people at around 10am in Phahameng, had attracted more than 5,000"
      }
    }
  ]
}
```
