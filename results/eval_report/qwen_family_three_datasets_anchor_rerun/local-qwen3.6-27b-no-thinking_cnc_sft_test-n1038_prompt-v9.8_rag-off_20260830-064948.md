# Qwen3.6 27B No Thinking cnc_sft_test Fixed eval report

## 配置
```json
{
  "label": "Qwen3.6 27B No Thinking cnc_sft_test Fixed",
  "model": "local/qwen3.6-27b-no-thinking",
  "dataset": "cnc_sft_test",
  "sample_count": 1038,
  "prompt_name": "v9.8",
  "use_rag": false,
  "rag_mode": "off",
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
================ Qwen3.6 27B No Thinking cnc_sft_test Fixed final report ================
样本总数: 1038
  Gold 含因果: 548 | Pred 含因果: 594
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.800
  Precision: 0.786
  Recall   : 0.852
  F1       : 0.818
  (TP=467, TN=363, FP=127, FN=81)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 1038
    Gold triples: 763 | Pred triples: 625
    Precision: 0.538
    Recall   : 0.440
    F1       : 0.484
    (TP=336, FP=289, FN=427)
  [anchor_window] (primary)
    样本数: 1038
    Gold triples: 763 | Pred triples: 625
    Precision: 0.650
    Recall   : 0.532
    F1       : 0.585
    (TP=406, FP=219, FN=357)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 467
    Gold triples: 668 | Pred triples: 495
    Precision: 0.679
    Recall   : 0.503
    F1       : 0.578
    (TP=336, FP=159, FN=332)
  [anchor_window] (primary)
    样本数: 467
    Gold triples: 668 | Pred triples: 495
    Precision: 0.820
    Recall   : 0.608
    F1       : 0.698
    (TP=406, FP=89, FN=262)
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
  "total": 4,
  "by_type": {
    "missing_triple_closing_brace": 4
  },
  "samples": [
    {
      "id": 581,
      "repair_type": "missing_triple_closing_brace"
    },
    {
      "id": 2817,
      "repair_type": "missing_triple_closing_brace"
    },
    {
      "id": 1706,
      "repair_type": "missing_triple_closing_brace"
    },
    {
      "id": 1286,
      "repair_type": "missing_triple_closing_brace"
    }
  ]
}
```

## 样本明细

Sample details shown: first 200 of 418 wrong samples from 1038 total samples.

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
        "span": "who had defaced China ’ s representative office in Hong Kong last week"
      },
      "effect": {
        "span": "police fired teargas and rubber bullets on demonstrators"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=542 ---

输入文本: We totally support the ongoing strike since VAT imposed by the government is unjust but the business has to run if we are to recover losses , ” said a shop owner near Charminar .

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
      "cause": "VAT imposed by the government is unjust",
      "effect": "We totally support the ongoing strike"
    },
    {
      "cause": "if we are to recover losses",
      "effect": "the business has to run"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "since VAT imposed by the government is unjust"
      },
      "effect": {
        "span": "We totally support the ongoing strike"
      },
      "relation": "caused"
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
      "effect": {
        "span": "officials have frozen that money"
      },
      "relation": "caused"
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
        "span": "Squarely blaming the Pattali Makkal Katchi ( PMK ) for orchestrating the violence against Dalits in three villages in Dharmapuri"
      },
      "effect": {
        "span": "VCK leader Thol Thirumavalavan on Friday demanded a CBI investigation into the matter and action against those openly instigating caste violence on public platforms ."
      },
      "relation": "caused"
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
        "span": "by expressing support for the police 's handling of a protest in Mong Kok at which rival groups clashed over a teacher 's verbal attack on officers ."
      },
      "effect": {
        "span": "he caused uproar in some quarters"
      },
      "relation": "caused"
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
      "effect": {
        "span": "RTC staff observed a bandh ; no RTC bus in the district plied today as they parked them on the main thoroughfare , putting the public to great inconvenience ."
      },
      "relation": "caused"
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
        "span": "Some protesters attacked me when I was clicking pictures"
      },
      "effect": {
        "span": "their colleagues dissuaded them ."
      },
      "relation": "caused"
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
        "span": "to urge the central government to immediately carve out a Telangana state ."
      },
      "effect": {
        "span": "Police arrested leaders of various political parties who squatted on the highway in response to ' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC )"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Akilan was admitted to hospital here along with member of rivaal group Stalin Dinakaraj , who also sustained injuries"
      },
      "relation": "caused"
    }
  ]
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

### --- id=581 ---

输入文本: After returning home from office on Oct 15 , the Devarkadra agriculture extension officer had poured kerosene over herself and lit the match .

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
        "span": "After returning home from office on Oct 15"
      },
      "effect": {
        "span": "the Devarkadra agriculture extension officer had poured kerosene over herself and lit the match ."
      },
      "relation": "caused"
    }
  ],
  "parse_repair_type": "missing_triple_closing_brace"
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
      "cause": "security forces shot four militants who allegedly attempted to blow up a Communist party building in southern Xinjiang",
      "effect": "That apparent calm was shattered in late December"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when security forces shot four militants who allegedly attempted to blow up a Communist party building in southern Xinjiang ."
      },
      "effect": {
        "span": "That apparent calm was shattered"
      },
      "relation": "caused"
    }
  ]
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
        "span": "who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district with an intention of causing mass destruction to the train and passengers"
      },
      "effect": {
        "span": "two persons ... were detained under the National Security Act in December ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1651 ---

输入文本: `` Free Napoleon and six others now , '' read one placard and another read : `` Stop police brutality '' .

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
        "span": "\" Free Napoleon and six others now , \" read one placard"
      },
      "effect": {
        "span": "another read : `` Stop police brutality '' ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2338 ---

输入文本: Pakistan has arrested seven suspected terrorists of the Lashkar-e-Taiba terror outfit , including its founding member Zakiur Rehman Lakhvi , who face charges of planning , financing and facilitating the Mumbai attack .

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
      "cause": "planning , financing and facilitating the Mumbai attack",
      "effect": "Pakistan has arrested seven suspected terrorists of the Lashkar-e-Taiba terror outfit , including its founding member Zakiur Rehman Lakhvi"
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
      "effect": {
        "span": "National Commission for Minorities ( NCM ) chairperson Naseem Ahmad has written to Union Home Minister Rajnath Singh"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "has urged the Minister to work towards creating a sense of security amongst the minorities ."
      },
      "effect": {
        "span": "National Commission for Minorities ( NCM ) chairperson Naseem Ahmad has written to Union Home Minister Rajnath Singh"
      },
      "relation": "caused"
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
        "span": "after NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections , as it did not want Achuthanandan to come back to power for another term ."
      },
      "effect": {
        "span": "The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram"
      },
      "relation": "caused"
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
        "span": "to flush out the terrorists who managed to escape in dense forests after carrying out the attack ."
      },
      "effect": {
        "span": "The Army and police have now launched extensive combing operations in the area"
      },
      "relation": "caused"
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
        "span": "with pelting them with stones"
      },
      "effect": {
        "span": "the brick kiln owners have charged the protesters"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Four-time MP Yadav was arrested in 1999 and convicted"
      },
      "relation": "caused"
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
      "effect": {
        "span": "party officials should have followed those who were leaving the stadium and observed them ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2900 ---

输入文本: However , the absence of senior Trinamool Congress leaders during the agitation prompted opposition parties to raise fingers at " TMC 's internal feud that led to the incident " .

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
      "cause": "the absence of senior Trinamool Congress leaders during the agitation",
      "effect": "opposition parties to raise fingers at \" TMC 's internal feud that led to the incident \""
    },
    {
      "cause": "TMC 's internal feud",
      "effect": "the incident"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the absence of senior Trinamool Congress leaders during the agitation"
      },
      "effect": {
        "span": "opposition parties to raise fingers at \" TMC 's internal feud that led to the incident \""
      },
      "relation": "caused"
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
      "effect": {
        "span": "this has created a lot of hassle for the public ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1971 ---

输入文本: In retaliation , the police fired a few rounds in the air which finally capped the clashes .

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
      "cause": "retaliation",
      "effect": "the police fired a few rounds in the air"
    },
    {
      "cause": "the police fired a few rounds in the air",
      "effect": "which finally capped the clashes"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the police fired a few rounds in the air"
      },
      "effect": {
        "span": "finally capped the clashes ."
      },
      "relation": "caused"
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
        "span": "because it is the most affordable tax imposed ever and we all should pay it , "
      },
      "effect": {
        "span": "\" Be good citizens and contribute to the development and pay property tax"
      },
      "relation": "caused"
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
      "effect": {
        "span": "the students handed over a memorandum addressed to the Governor to Additional District Magistrate Akhilesh Ojha , who assured them of a fair inquiry ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1589 ---

输入文本: The Global Times , a state-run newspaper known for its hawkish stance , said in an editorial that the event to commemorate the June 4 crackdown had " clearly crossed the red line of the law " as it was related to " the most sensitive political issue " in China .

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
      "cause": "it was related to \" the most sensitive political issue \" in China",
      "effect": "The Global Times , a state-run newspaper known for its hawkish stance , said in an editorial that the event to commemorate the June 4 crackdown had \" clearly crossed the red line of the law \""
    },
    {
      "cause": "to commemorate the June 4 crackdown",
      "effect": "the event"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "fear and economic inducements ensured they turned away from politics ."
      },
      "relation": "caused"
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
        "span": "The stalemate over payment of salaries to municipal workers"
      },
      "effect": {
        "span": "the Joint Action Committee ( JAC ) of VMC Employees bent upon continuing ‘ Work to Rule ’ ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "These cases were registered against them"
      },
      "relation": "caused"
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
      "effect": {
        "span": "The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday"
      },
      "relation": "caused"
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
      "effect": {
        "span": "the agitation"
      },
      "relation": "caused"
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
        "span": "in connection with the violence that took place on Monday when youths protesting against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC ) went on the rampage ."
      },
      "effect": {
        "span": "The Allahabad police Tuesday registered a total of four FIRs , all at Civil Lines police station"
      },
      "relation": "caused"
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
      "effect": {
        "span": "A 59 - year-old “ barefoot doctor ” is sentenced to four months in jail"
      },
      "relation": "caused"
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
        "span": "when the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire to control a mob that was pelting stones on the evening of December 20 ."
      },
      "effect": {
        "span": "three were wounded"
      },
      "relation": "caused"
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
        "span": "as a sign of protest against renewed ' racism and Afro-phobia '"
      },
      "effect": {
        "span": "diplomats from 42 African nations boycotted the weeklong celebration of Africa Day , hosted by the Indian government"
      },
      "relation": "caused"
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
      "effect": {
        "span": "they were further postponed ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2349 ---

输入文本: She has worked as an assistant for legislators , been involved in a youth action group , competed in a District Council election in 2003 , helped with the organisation of the July 1 march in 2004 and 2005 , and has taken part in the fight to preserve the Star Ferry pier .

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
      "cause": "to preserve the Star Ferry pier",
      "effect": "has taken part in the fight"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "The two-day bandh call given by the pro-United Andhra Pradesh groups"
      },
      "relation": "caused"
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
        "span": "the miscreants mistaking them to have caused the fatal accident"
      },
      "effect": {
        "span": "The Tanzanian woman was reportedly dragged out of the car in which she was seated along with her three friends"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=116 ---

输入文本: There were reports of skirmishes and clashes , including stone pelting , in the area in which two policemen were injured .

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
      "cause": "There were reports of skirmishes and clashes , including stone pelting , in the area",
      "effect": "two policemen were injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in the area"
      },
      "effect": {
        "span": "two policemen were injured ."
      },
      "relation": "caused"
    }
  ]
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
        "span": "in support of party president Y.S. Jaganmohan Reddy ’ s indefinite ‘ deeksha ’ in Guntur seeking special category status for the State ."
      },
      "effect": {
        "span": "YSR Congress leaders and cadres organised relay hunger strikes in various Assembly constituencies across the district on Thursday"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3074 ---

输入文本: Tirupur : Protests against lack of amenities November 27 , 2014 00:00 IST Two separate agitations were witnessed on the Corporation office premises on Tuesday with residents and political activists laying siege to the offices of the Mayor and the Commissioner .

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
      "cause": "residents and political activists laying siege to the offices of the Mayor and the Commissioner",
      "effect": "Two separate agitations were witnessed on the Corporation office premises on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against lack of amenities"
      },
      "effect": {
        "span": "Two separate agitations were witnessed on the Corporation office premises on Tuesday with residents and political activists laying siege to the offices of the Mayor and the Commissioner ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2328 ---

输入文本: Police use tear gas to control communal clash at Mirzapur - Indian Express Express News Service , Express News Service : Ahmedabad , Tue Sep 15 2009 , 01:09 hrs The city police had to resort to tear gas shelling after a communal violence broke out near St Xavier 's High School in the Mirzapur area of Ahmedabad late on Sunday .

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
      "cause": "to control communal clash at Mirzapur",
      "effect": "Police use tear gas"
    },
    {
      "cause": "a communal violence broke out near St Xavier 's High School in the Mirzapur area of Ahmedabad late on Sunday",
      "effect": "The city police had to resort to tear gas shelling"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after a communal violence broke out near St Xavier 's High School in the Mirzapur area of Ahmedabad late on Sunday ."
      },
      "effect": {
        "span": "The city police had to resort to tear gas shelling"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1905 ---

输入文本: April 26 : Three policemen and two CPI-Maoist cadres were killed in an encounter in Dumka , Jharkhand .

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
      "cause": "an encounter in Dumka , Jharkhand .",
      "effect": "Three policemen and two CPI-Maoist cadres were killed"
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
      "cause": "ANC president Jacob Zuma 's leadership",
      "effect": "South Africa has become a banana state"
    }
  ],
  "pred_triples": []
}
```

### --- id=3067 ---

输入文本: The CPI(M) leader said that while CPI(M) workers were the victims of RSS attacks at Thalassery and Malampuzha , the UDF was organising a Shanthi Yatra ( a foot march for peace by the Congress ) to target the CPI(M) as perpetrators of violence .

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
      "cause": "to target the CPI(M) as perpetrators of violence",
      "effect": "the UDF was organising a Shanthi Yatra ( a foot march for peace by the Congress )"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "Hundreds of members of the Police and Prisons Civil Rights Union gathered at the King Dinuzulu Gardens in Durban on Wednesday ahead of a march"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1325 ---

输入文本: Even as the Chief Minister was in the district headquarters , reports came in that the police forced a bandh in Huzurabad town , 40 km from here .

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
        "span": "Even as the Chief Minister was in the district headquarters"
      },
      "effect": {
        "span": "the police forced a bandh in Huzurabad town , 40 km from here ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1423 ---

输入文本: Some of the youths decided they were not satisfied with this , and on Wednesday morning barricaded the doors of their cells , he said .

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
      "cause": "Some of the youths decided they were not satisfied with this",
      "effect": "on Wednesday morning barricaded the doors of their cells"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they were not satisfied with this"
      },
      "effect": {
        "span": "Some of the youths decided ... and on Wednesday morning barricaded the doors of their cells , he said ."
      },
      "relation": "caused"
    }
  ]
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
      "effect": {
        "span": "A house was destroyed"
      },
      "relation": "caused"
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
      "cause": "Paramilitary troops and a two-person militant suicide squad fought a 22 - hour gunbattle at a Kashmir security camp which ended on Tuesday",
      "effect": "eight dead and nine wounded"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "tensions spiked once more in the financial hub"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Addressing a congregation at Gokulnagar , Nandigram , Trinamool Congress chief Mamata Banerjee said the people would give a fitting reply to the Communist Party of India (Marxist)-led government"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "Condemning the “ atrocities committed by CPI(M) cadres on the innocent people of Nandigram , ”"
      },
      "effect": {
        "span": "Ms. Banerjee said even after a year “ those responsible had not been punished ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=694 ---

输入文本: Farmers stage dharna in Harihar No grants released so far : officials

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
        "span": "No grants released so far"
      },
      "effect": {
        "span": "Farmers stage dharna in Harihar"
      },
      "relation": "caused"
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
      "effect": {
        "span": "The MLAs , along with a large number of party supporters , raised slogans"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "condemned the attack on the woman MLA ."
      },
      "effect": {
        "span": "The MLAs , along with a large number of party supporters ,"
      },
      "relation": "caused"
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
        "span": "against the temporary suspension of the employers ' levy"
      },
      "effect": {
        "span": "About 1,000 foreign domestic helpers yesterday protested"
      },
      "relation": "caused"
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
        "span": "such people ( those who unfurled the Vidarbha flag )"
      },
      "effect": {
        "span": "the country 's integrity is damaged ."
      },
      "relation": "caused"
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

### --- id=645 ---

输入文本: New Delhi , October 29 , Thu Oct 30 2008 , 01:17 hrs Several hours after a migrant labourer from U P was allegedly beaten to death by a group of Marathi-speaking men on a suburban train headed for Mumbai , the Centre issued a stern advisory to the Maharashtra government , asking it to act quickly to end the violence against north Indians and ensure the safety of everyone living in India 's financial capital .

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
        "span": "Several hours after a migrant labourer from U P was allegedly beaten to death by a group of Marathi-speaking men on a suburban train headed for Mumbai"
      },
      "effect": {
        "span": "the Centre issued a stern advisory to the Maharashtra government , asking it to act quickly to end the violence against north Indians and ensure the safety of everyone living in India 's financial capital ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1673 ---

输入文本: While the recent protests were initially sparked by Lam ’ s attempts to pass the proposed extradition legislation , the demonstrations have morphed into a wider movement against her administration and Beijing .

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
      "cause": "Lam ’ s attempts to pass the proposed extradition legislation",
      "effect": "the recent protests"
    },
    {
      "cause": "against her administration and Beijing",
      "effect": "a wider movement"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Lam ’ s attempts to pass the proposed extradition legislation"
      },
      "effect": {
        "span": "the recent protests were initially sparked"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Arunthathiyar community men refused to perform funeral rituals for a Caste Hindu family"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2166 ---

输入文本: Alleging that the cases were filed against the students only to discourage them from participating in separate Telangana agitations , Chandrasekhar Rao demanded that the cases be lifted immediately .

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
      "cause": "discourage them from participating in separate Telangana agitations",
      "effect": "the cases were filed against the students"
    },
    {
      "cause": "the cases were filed against the students only to discourage them from participating in separate Telangana agitations",
      "effect": "Chandrasekhar Rao demanded that the cases be lifted immediately"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Alleging that the cases were filed against the students only to discourage them from participating in separate Telangana agitations"
      },
      "effect": {
        "span": "Chandrasekhar Rao demanded that the cases be lifted immediately ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1816 ---

输入文本: As a huge crowd of market-goers gathered to help the injured and to witness the blast after-effects , another powerful blast occurred soon a few feet away from the first blast site .

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
      "cause": "to help the injured and to witness the blast after-effects",
      "effect": "a huge crowd of market-goers gathered"
    }
  ],
  "pred_triples": []
}
```

### --- id=2969 ---

输入文本: Meanwhile , security forces and Naxalites had an encounter near village Belgaon  12 km from Bairamgarh in Bijapurkilling a Maoist rebel on the spot .

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
      "cause": "security forces and Naxalites had an encounter near village Belgaon  12 km from Bairamgarh in Bijapur",
      "effect": "killing a Maoist rebel on the spot"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "security forces and Naxalites had an encounter near village Belgaon  12 km from Bairamgarh in Bijapur"
      },
      "effect": {
        "span": "killing a Maoist rebel on the spot ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2889 ---

输入文本: Some chanted ' Give me back my right of abode ' outside the Court of Final Appeal .

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
        "span": "' Give me back my right of abode '"
      },
      "effect": {
        "span": "Some chanted"
      },
      "relation": "caused"
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

### --- id=285 ---

输入文本: Police opened fire , killing 34 striking workers and wounding 78 while trying to disperse a group gathered on a hill near Lonmin 's platinum mine in Marikana on August 16 .

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
      "cause": "trying to disperse a group gathered on a hill near Lonmin 's platinum mine in Marikana on August 16",
      "effect": "Police opened fire"
    },
    {
      "cause": "Police opened fire",
      "effect": "killing 34 striking workers and wounding 78"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Police opened fire , killing 34 striking workers and wounding 78 while trying to disperse a group gathered on a hill near Lonmin 's platinum mine in Marikana on August 16 ."
      },
      "effect": {
        "span": "killing 34 striking workers and wounding 78"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=691 ---

输入文本: In the streets too the general sense of animosity prevailed as the CPM and BJP workers scuffled outside the AKG Centre and 600 people were detained .

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
      "cause": "the CPM and BJP workers scuffled outside the AKG Centre and 600 people were detained",
      "effect": "In the streets too the general sense of animosity prevailed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "as the CPM and BJP workers scuffled outside the AKG Centre"
      },
      "effect": {
        "span": "600 people were detained ."
      },
      "relation": "caused"
    }
  ]
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
      "effect": {
        "span": "Chidambaram refered to the Dantewada massacre of 75 CRPF men and said the companies of CRPF in Chintalnar and Chintagufa were deployed by the state government ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2311 ---

输入文本: The Cape Town Regional Chamber of Commerce and Industry said the potential effect of the strike was `` so serious '' that there was a case to declare public transport an essential service that could not be disrupted by strike action .

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
      "cause": "the potential effect of the strike was `` so serious ''",
      "effect": "there was a case to declare public transport an essential service that could not be disrupted by strike action"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "Ruling alliance partner Shiv Sena today flayed Maharashtra Chief Minister Devendra Fadnavis"
      },
      "relation": "caused"
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
        "span": "for public violence while protesting against financial aid cuts at the University of the Witwatersrand"
      },
      "effect": {
        "span": "Twelve students arrested"
      },
      "relation": "caused"
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
      "effect": {
        "span": "a huge rally was organised from pavilion grounds to the Collectorate ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2561 ---

输入文本: Later , YSRC leaders Shoba Nagireddy , Praveen Kumar Reddy , G Babu Rao met jails IG Sunil Kumar and represented to him to release medical bulletins on the health of Jagan , who is fasting in the jail .

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
        "span": "to release medical bulletins on the health of Jagan , who is fasting in the jail ."
      },
      "effect": {
        "span": "YSRC leaders Shoba Nagireddy , Praveen Kumar Reddy , G Babu Rao met jails IG Sunil Kumar and represented to him"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Hundreds of them raised slogans"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Protest Federation of various autorickshaw employees union on Thursday staged a protest in front of regional transport office"
      },
      "relation": "caused"
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
        "span": "as protesting farmers blocked the main access road ."
      },
      "effect": {
        "span": "Sino Gold Mining , which only last week announced a joint venture to expand exploration near its White Mountain Mine in Jilin province , had to halt operations yesterday"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Thirty-seven of the operators signed a petition and held a press conference last Sunday"
      },
      "relation": "caused"
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
        "span": "to probe into the violence and the deaths of 44 people in wage-related protests ."
      },
      "effect": {
        "span": "The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Maoists opened indiscriminate firing ."
      },
      "relation": "caused"
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
        "span": "following reports the authorities had tried to prevent the demonstration ."
      },
      "effect": {
        "span": "One protester said yesterday 's turnout was smaller"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1806 ---

输入文本: I was threatened that I will also meet the fate of my daughter but Police did not provide any protection to us .

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
        "span": "I was threatened that I will also meet the fate of my daughter"
      },
      "effect": {
        "span": "Police did not provide any protection to us ."
      },
      "relation": "caused"
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
        "span": "when students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus"
      },
      "effect": {
        "span": "over 22 people , including five media men and 11 security personnel with an officer among them , were injured last night"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "when students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus"
      },
      "effect": {
        "span": "prompting them to use force to quell the mob ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "a Secretariat dharna was staged under the joint aegis of the Kalanilayam Paristhithi Vedi , environmentalists and cultural activists here on Monday ."
      },
      "relation": "caused"
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
        "span": "to join the statewide agitation to oppose the State Government 's move to amend the APMC Act"
      },
      "effect": {
        "span": "Traders pulled down their shutters"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3062 ---

输入文本: A bodyguard of Javed was killed in that attack .

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
      "cause": "that attack",
      "effect": "A bodyguard of Javed was killed"
    }
  ],
  "pred_triples": []
}
```

### --- id=2552 ---

输入文本: At one point , recorded in the documentary , the filmmaker himself was embroiled in the violence , when he was hit in the face by a police officer .

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
      "cause": "he was hit in the face by a police officer",
      "effect": "the filmmaker himself was embroiled in the violence"
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
    "tp": 0,
    "fp": 1,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 4
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
      "effect": {
        "span": "DA MP Andrew Whitfield said he would ask police commissioner General Khehla Sitole to activate the National Joint Operations and Intelligence Structure ( Natjoints ) to intervene"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1764 ---

输入文本: The memorandum , from the residents of Ward 10 in the Nkonkobe municipality registered resentment and disapproval of the high crime rate in the country , in Alice in particular .

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
        "span": "resentment and disapproval of the high crime rate in the country , in Alice in particular ."
      },
      "effect": {
        "span": "The memorandum , from the residents of Ward 10 in the Nkonkobe municipality registered"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2417 ---

输入文本: January 31 , 2017 00:00 IST Tripartite dialogue mooted with United Naga Council and State government over the ongoing highway blockade

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
      "cause": "the ongoing highway blockade",
      "effect": "Tripartite dialogue mooted with United Naga Council and State government"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "BJP legislators staged a dharna"
      },
      "relation": "caused"
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
        "span": "over poisoning threat to Tung"
      },
      "effect": {
        "span": "2 held"
      },
      "relation": "caused"
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
        "span": "in the wake of violence that erupted during a rally by Muslims in Mumbai ’ s Azad Maidan ."
      },
      "effect": {
        "span": "This outrageous and provocative statement"
      },
      "relation": "caused"
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
      "effect": {
        "span": "The abducted jawans were unarmed and also not in police uniform"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1450 ---

输入文本: The incident took place around noon in Gaya district 's Uchla village near Sherghati , about 100 km from here , when Maoists blew up a patrolling vehicle of the Roshanganj police station .

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
      "cause": "Maoists blew up a patrolling vehicle of the Roshanganj police station",
      "effect": "The incident took place around noon in Gaya district 's Uchla village near Sherghati , about 100 km from here"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "the police ... lost temper and rataliated ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "over 20,000 people rallied in Xiamen , a coastal city in Fujian province"
      },
      "relation": "caused"
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
        "span": "with their arrests on various routes proceeding to the capital ."
      },
      "effect": {
        "span": "The district police foiled the attempts made by the TRS and pro-Telangana activists to proceed and participate in ‘ Million March ' in Hyderabad on Thursday"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Demonstrators flayed the advocates"
      },
      "relation": "caused"
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
      "effect": {
        "span": "within minutes a farm house was on fire , two more house were set alight and road blocked ."
      },
      "relation": "caused"
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
        "span": "Distressed after allegedly being denied a scholarship by his school"
      },
      "effect": {
        "span": "a Class XII Dalit dropout of the Government Higher Secondary School in Allinagaram , in Theni district , tied to immolate himself on Tuesday ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "Hardik Patel , the face of Patel quota stir , called it \" failure \" of the government ."
      },
      "relation": "caused"
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
      "cause": "to break up their peaceful protest",
      "effect": "Shiv Sena workers had barged in violently"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "For when they had met publicly on Sunday"
      },
      "effect": {
        "span": "Shiv Sena workers had barged in violently to break up their peaceful protest ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "they were staging a road roko"
      },
      "relation": "caused"
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
        "span": "in violence related to the illegal strike ."
      },
      "effect": {
        "span": "Three people have died and scores have been injured"
      },
      "relation": "caused"
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
      "effect": {
        "span": "injury to accused no : 37 in the case ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "there were also celebrations in different parts of the city"
      },
      "relation": "caused"
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
      "effect": {
        "span": "People have been forced to come out on the streets"
      },
      "relation": "caused"
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
        "span": "on first day of the strike on November 15 ."
      },
      "effect": {
        "span": "all these shops had downed shutters"
      },
      "relation": "caused"
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
        "span": "whose regular promotions were denied"
      },
      "effect": {
        "span": "the indefinite hunger strike launched by three employees Mahesh Ahire , Shriram Gavai and Balkrishna Gadekar"
      },
      "relation": "caused"
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
        "span": "in separate gunfights ."
      },
      "effect": {
        "span": "Security forces in Kokrajhar district have so far killed 19 militants since April 29"
      },
      "relation": "caused"
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
      "effect": {
        "span": "N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "As hundreds of employees from the city went to Vizianagaram to take part in the last rites of N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI"
      },
      "effect": {
        "span": "an all-union meeting convened by the CITU resolved to organise demonstrations in front of all industrial establishments located in the city on Wednesday ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "Rs 2,200 cr Transactions Hit"
      },
      "relation": "caused"
    }
  ],
  "parse_repair_type": "missing_triple_closing_brace"
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
      "effect": {
        "span": "it becomes harder for us to exercise those options ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=288 ---

输入文本: Last summer , tens of thousands of people in the northeastern city of Dalian , Liaoning , marched to demand the relocation of a chemical plant .

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
      "cause": "to demand the relocation of a chemical plant",
      "effect": "Last summer , tens of thousands of people in the northeastern city of Dalian , Liaoning , marched"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to demand the relocation of a chemical plant ."
      },
      "effect": {
        "span": "tens of thousands of people in the northeastern city of Dalian , Liaoning , marched"
      },
      "relation": "caused"
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
        "span": "the police had taken away national flag from them during a clash on Friday last"
      },
      "effect": {
        "span": "The students ... demanded that it be returned to them ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "I would like to request people to reconsider the strike"
      },
      "relation": "caused"
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
      "effect": {
        "span": "a peaceful and democratic protest"
      },
      "relation": "caused"
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
      "effect": {
        "span": "The escalating protests in the JNU"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=339 ---

输入文本: Distributing medals and trophies to winners of the five-day event in which 702 personnel from 22 State police teams and eight Central police organisations participated , the chief minister recalled the 26/11 incidents in Mumbai to stress her point .

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
      "cause": "to stress her point",
      "effect": "the chief minister recalled the 26/11 incidents in Mumbai"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "the vehicle was vandalised ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1884 ---

输入文本: - Indian Express Parimal Dabhi , Parimal Dabhi : Ahmedabad , September 18 , Fri Sep 19 2008 , 01:25 hrs One Charul Vakta , a businessman by profession , has filed a police complaint against four members of the City Doctors ' Cell of the Ahmedabad unit of the BJP for allegedly defaming Prime Minister Manmohan Singh in their protest act , wherein they alluded that he was anti-national , in addition to passing disparaging remarks about him .

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
      "cause": "allegedly defaming Prime Minister Manmohan Singh in their protest act",
      "effect": "Charul Vakta , a businessman by profession , has filed a police complaint against four members of the City Doctors ' Cell of the Ahmedabad unit of the BJP"
    },
    {
      "cause": "they alluded that he was anti-national , in addition to passing disparaging remarks about him",
      "effect": "allegedly defaming Prime Minister Manmohan Singh in their protest act"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "Employees at three factories had signed a petition"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "were demanding reassurances about the future of the venture and their jobs"
      },
      "effect": {
        "span": "Employees at three factories had signed a petition"
      },
      "relation": "caused"
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
        "span": "the circumstances"
      },
      "effect": {
        "span": "forced the community members to stage such a protest ."
      },
      "relation": "caused"
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
        "span": "the protest"
      },
      "effect": {
        "span": "a community hall was torched"
      },
      "relation": "caused"
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
      "effect": {
        "span": "India had suspended the talks"
      },
      "relation": "caused"
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
      "cause": "demanding the dismissal of the teacher who had set the question paper",
      "effect": "a group of students even storming into the university campus"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "This"
      },
      "effect": {
        "span": "violent protests across the city the next day , with a group of students even storming into the university campus and demanding the dismissal of the teacher who had set the question paper ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "some of the banks , particularly SBI and its associates , had ensured that their ATMs ( automated teller machines ) had cash to meet the customer demand"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=783 ---

输入文本: The company had further offered a once-off hardship allowance of R2000 to help workers deal with financial difficulties arising from the no-work , no-pay principle in place while they were striking .

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
      "cause": "to help workers deal with financial difficulties arising from the no-work , no-pay principle in place while they were striking",
      "effect": "The company had further offered a once-off hardship allowance of R2000"
    },
    {
      "cause": "the no-work , no-pay principle in place",
      "effect": "financial difficulties"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to help workers deal with financial difficulties arising from the no-work , no-pay principle in place while they were striking ."
      },
      "effect": {
        "span": "The company had further offered a once-off hardship allowance of R2000"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2658 ---

输入文本: TDP members were probing irregularities in wage payment under NRLEGP when they were mobbed

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
      "cause": "TDP members were probing irregularities in wage payment under NRLEGP",
      "effect": "they were mobbed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "probing irregularities in wage payment under NRLEGP"
      },
      "effect": {
        "span": "TDP members were mobbed"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=836 ---

输入文本: Tension on ; Outstation Students Seek Shifting Out of NIT

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
        "span": "Outstation Students Seek Shifting Out of NIT"
      },
      "effect": {
        "span": "Tension on ;"
      },
      "relation": "caused"
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
        "span": "at a protest outside the Johannesburg High Court ."
      },
      "effect": {
        "span": "South African rape laws still blame the survivor of rape , People Opposing Woman Abuse ( Powa ) said on Friday"
      },
      "relation": "caused"
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
      "effect": {
        "span": "the web of security tightens"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=360 ---

输入文本: Director Tlhalefang Kuetsile earlier said eight students were arrested and four injured when police fired rubber bullets during a protest on the campus .

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
      "cause": "police fired rubber bullets during a protest on the campus",
      "effect": "eight students were arrested and four injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when police fired rubber bullets"
      },
      "effect": {
        "span": "eight students were arrested and four injured"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=259 ---

输入文本: On Tuesday night tens of thousands of demonstrators packed the city ’ s downtown area for a third night as protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight .

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
      "cause": "protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight",
      "effect": "On Tuesday night tens of thousands of demonstrators packed the city ’ s downtown area for a third night"
    },
    {
      "cause": "Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight",
      "effect": "they would step up their actions"
    }
  ],
  "pred_triples": []
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
        "span": "Urging the Commission to reveal names of people involved in the attacks"
      },
      "effect": {
        "span": "he said the protestors against the church attack were assaulted by police , youth were hunted and criminal cases were booked on them ."
      },
      "relation": "caused"
    }
  ]
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
        "span": "Angered"
      },
      "effect": {
        "span": "community members mobilised and marched to a suspected gang member 's house in Bardien Street where Tavern Moss was stabbed and beaten to death , police said at the time ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "the CPI ( Maoist ) gave the call"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "for which the CPI ( Maoist ) gave the call demanding that the police produce in a court of law the party 's Andhra-Orissa border special zone committee member and a central committee member Damodar alias Azad , who was reportedly taken into custody a few days ago ."
      },
      "effect": {
        "span": "a bandh on Thursday in the Visakha Agency"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=74 ---

输入文本: Tohtunyaz helped them to acquire more than 10 knives used in the attack .

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
        "span": "used in the attack ."
      },
      "effect": {
        "span": "Tohtunyaz helped them to acquire more than 10 knives"
      },
      "relation": "caused"
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
      "effect": {
        "span": "people took out a march here on Sunday to demonstrate their anger against the outfit ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2346 ---

输入文本: The four inmates who held her hostage were arrested .

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
      "cause": "The four inmates who held her hostage",
      "effect": "arrested"
    }
  ],
  "pred_triples": []
}
```

### --- id=1188 ---

输入文本: Medicos ' Stir Hits GGH Services 04th January 2012 02:56 AM GUNTUR : The ongoing strike of PG medical students of the Government General Hospital ( GGH ) has hit medical services badly .

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
      "cause": "The ongoing strike of PG medical students of the Government General Hospital ( GGH )",
      "effect": "hit medical services badly"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The ongoing strike of PG medical students of the Government General Hospital ( GGH )"
      },
      "effect": {
        "span": "medical services badly ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=853 ---

输入文本: `` If a suitably qualified person had been chosen , such a person would have foreseen that the demonstration would degenerate into violence and prepared for that eventuality , '' said SAHRC said .

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
  "pred_triples": []
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
      "effect": {
        "span": "the abductions"
      },
      "relation": "caused"
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
        "span": "A day after the snap protest by the Karnataka State Reserve Police ( KSRP ) personnel extending support to their chief P. Ravindranath , who has now been transferred"
      },
      "effect": {
        "span": "senior officials on Thursday chalked out a strategy to prevent them from continuing the protest by deploying all the 1,200 KSRP personnel on various duties ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "the Centre on Wednesday gave hint of enacting a tactical retreat from Naxal strongholds like Dantewada and Narayanpur in Chhattisgarh , camouflaging it as ‘ revisiting deployment ’ ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "around 2,000 residents of Somasandrapalya , Haraluru , HSR Layout , Kudlu , Mangamanapalya , Hosapalya and surrounding areas gathered near Ravindra Bharathi Global School in HSR Layout on Saturday and formed a human chain near a wall constructed by Sobha Daffodil apartment ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "The row over possession of Satlok Ashram , headed by Rampal , took a violent turn on Sunday"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=326 ---

输入文本: Hartal supporters surrounded a police station at Attakkulangara demanding that four men arrested by police for pelting stones at KSRTC buses be freed .

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
      "cause": "demanding that four men arrested by police for pelting stones at KSRTC buses be freed",
      "effect": "Hartal supporters surrounded a police station at Attakkulangara"
    },
    {
      "cause": "pelting stones at KSRTC buses",
      "effect": "four men arrested by police"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding that four men arrested by police for pelting stones at KSRTC buses be freed ."
      },
      "effect": {
        "span": "Hartal supporters surrounded a police station at Attakkulangara"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=402 ---

输入文本: Trouble was also reported from Mirzapur in the city , when a mob gathered near a mosque threw two crude bombs at the police .

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
        "span": "when a mob gathered near a mosque threw two crude bombs at the police ."
      },
      "effect": {
        "span": "Trouble was also reported from Mirzapur in the city"
      },
      "relation": "caused"
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
        "span": "as the APMC traders across the State observe bandh ."
      },
      "effect": {
        "span": "A farmer takes a nap on a cotton bale at the APMC yard , in Hubli on Friday"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=26 ---

输入文本: It was in January this year a group of persons attacked the NHAI office at Kalamassery and distributed notices supporting armed revolt against the government .

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
        "span": "supporting armed revolt against the government ."
      },
      "effect": {
        "span": "a group of persons attacked the NHAI office at Kalamassery and distributed notices"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Panjab University Student Union ( PUSU ) , a student 's organisations of the Panjab University ( PU ) , staged a protest outside the vice-chancellor office on Monday"
      },
      "relation": "caused"
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
      "effect": {
        "span": "a landmine blast"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2822 ---

输入文本: Hence , the strike was forced on us , ” he added .

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
        "span": "Hence"
      },
      "effect": {
        "span": "the strike was forced on us , ” he added ."
      },
      "relation": "caused"
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
        "span": "the power of the internet helped foster the massive march in 2003"
      },
      "effect": {
        "span": "everyone is keenly aware"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1944 ---

输入文本: Others who addressed the dharna demanded that the government must review Section 124 A of the Indian Penal Code ( IPC ) which deals with sedition , the law under which Sen has been sentenced .

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
      "cause": "demanded that the government must review Section 124 A of the Indian Penal Code ( IPC ) which deals with sedition , the law under which Sen has been sentenced",
      "effect": "Others who addressed the dharna"
    }
  ],
  "pred_triples": []
}
```

### --- id=674 ---

输入文本: Consequently , the residents staged a demonstration on Tuesday .

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
        "span": "Consequently"
      },
      "effect": {
        "span": "the residents staged a demonstration on Tuesday ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1821 ---

输入文本: A senior police officer , who declined to be quoted on the ground that investigations were still on , told The Hindu that whether the ULFA denied it or not , the police suspected the twin blasts to be the handiwork of the militant outfit .

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
      "cause": "investigations were still",
      "effect": "A senior police officer , who declined to be quoted"
    },
    {
      "cause": "the twin blasts",
      "effect": "the militant outfit"
    }
  ],
  "pred_triples": []
}
```

### --- id=2088 ---

输入文本: `` Our disappointment is that the violence occurred after attempts earlier in the day by my office to receive a memorandum from the community . ''

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
      "cause": "attempts earlier in the day by my office to receive a memorandum from the community",
      "effect": "the violence occurred"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "Anger about the policy among Han Chinese , by far the largest group among China 's 56 ethnic communities , has been exacerbated"
      },
      "relation": "caused"
    },
    {
      "cause": {
        "span": "the injuries suffered by 1,680 people during clashes between the province 's Uygur Muslim minority and Han Chinese ."
      },
      "effect": {
        "span": "Anger about the policy among Han Chinese , by far the largest group among China 's 56 ethnic communities , has been exacerbated"
      },
      "relation": "caused"
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
    "tp": 0,
    "fp": 1,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 4
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
        "span": "to protest against the murder ."
      },
      "effect": {
        "span": "a large number of people who had blocked road near Mahabir bridge"
      },
      "relation": "caused"
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
        "span": "against a few judges"
      },
      "effect": {
        "span": "the huge posse of advocates started raising defamatory slogans"
      },
      "relation": "caused"
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
        "span": "The ripple effect of the drastic downsizing of Nokia ’ s Sriperumbudur plant"
      },
      "effect": {
        "span": "BYD Electronics India Private Ltd announced a VRS offer for its 1,500 employees ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "The journalist ... was manhandled ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "Telugu Desam president Nara Chandrababu Naidu has called upon the cadre and people to be prepared to march to the State capital and if necessary , to the Assembly"
      },
      "relation": "caused"
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

### --- id=59 ---

输入文本: The recruits , at Valluvar Kottam shouted slogans including , “ HCL lend us your ears , give us back our two years , ” while undertaking the day-long fast .

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
        "span": "to demand answers"
      },
      "effect": {
        "span": "The recruits , at Valluvar Kottam shouted slogans including , “ HCL lend us your ears , give us back our two years , ” while undertaking the day-long fast ."
      },
      "relation": "caused"
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
      "effect": {
        "span": "that left commuters stranded in Johannesburg"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Congress leaders on Thursday gave a clarion call to party workers and supporters to dethrone Naveen Patnaik Government in the 2014 general elections ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=997 ---

输入文本: Hence , we also have plans to organise talks with the public and also with those who hold protests against plywood factories so that the actual issues can be sorted out , ” he added .

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
      "cause": "so that the actual issues can be sorted out",
      "effect": "we also have plans to organise talks with the public and also with those who hold protests against plywood factories"
    },
    {
      "cause": "against plywood factories",
      "effect": "protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "so that the actual issues can be sorted out"
      },
      "effect": {
        "span": "we also have plans to organise talks with the public and also with those who hold protests against plywood factories"
      },
      "relation": "caused"
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
        "span": "during a protest while 20 others , including two Additional SPs , were injured in clashes between police and protesters demanding shifting of proposed AIIMS in Assam from Changsari to Raha ."
      },
      "effect": {
        "span": "one person identified as Mintu Deori was killed"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Traffic was held up for an hour"
      },
      "relation": "caused"
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
      "cause": "against water shortage in Mumbai India Thursday",
      "effect": "A boy holding an empty bucket participates along with others in a protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against water shortage"
      },
      "effect": {
        "span": "A boy holding an empty bucket participates along with others in a protest"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2170 ---

输入文本: NEW DELHI : Minorities panel voices concern over attack on Muslims

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
      "cause": "attack on Muslims",
      "effect": "Minorities panel voices concern"
    }
  ],
  "pred_triples": []
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
      "effect": {
        "span": "which had resulted in the death of 19 persons ."
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=189 ---

输入文本: The stir intensified when women activists on Tuesday voiced their support for those women set to march towards Shani Shingnapur temple in Maharashtra to break the centuries old tradition of not allowing the feminine gender to enter the sanctum sanctorum .

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
      "cause": "women activists on Tuesday voiced their support for those women set to march towards Shani Shingnapur temple in Maharashtra to break the centuries old tradition of not allowing the feminine gender to enter the sanctum sanctorum",
      "effect": "The stir intensified"
    },
    {
      "cause": "to break the centuries old tradition of not allowing the feminine gender to enter the sanctum sanctorum",
      "effect": "those women set to march towards Shani Shingnapur temple in Maharashtra"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "when women activists on Tuesday voiced their support for those women set to march towards Shani Shingnapur temple in Maharashtra to break the centuries old tradition of not allowing the feminine gender to enter the sanctum sanctorum ."
      },
      "effect": {
        "span": "The stir intensified"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Thousands of workers had queued up outside SDA office"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1738 ---

输入文本: Constable Sefako Xaba after hundreds of pupils threw stones at police transporting five men accused of murdering 14-year-old Thato Radebe to the Johannesburg prison .

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
        "span": "after hundreds of pupils threw stones at police transporting five men accused of murdering 14-year-old Thato Radebe to the Johannesburg prison ."
      },
      "effect": {
        "span": "Constable Sefako Xaba"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=437 ---

输入文本: When the education authorities conducted the meet on Friday afternoon , physical education students and teachers staged a protest by sitting on the tracks at the meet grounds .

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
      "cause": "physical education students and teachers staged a protest",
      "effect": "sitting on the tracks at the meet grounds"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "When the education authorities conducted the meet on Friday afternoon"
      },
      "effect": {
        "span": "physical education students and teachers staged a protest by sitting on the tracks at the meet grounds ."
      },
      "relation": "caused"
    }
  ]
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
        "span": "on being informed that farmers were staging a dharna in front of the department"
      },
      "effect": {
        "span": "Vijaykumar , Assistant Director of the Agriculture Department , who rushed to the spot"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Dozens of people , including women , took out a ‘ Freedom Walk ' through the main thoroughfare of the city on Thursday midnight"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Violence erupted on Tuesday"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=673 ---

输入文本: The lift station in Keelkattalai was proposed to be built on Arulmurugan Main Road , but was dropped following protests from residents as it involved filling up of an abandoned well .

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
      "cause": "protests from residents",
      "effect": "dropped"
    },
    {
      "cause": "it involved filling up of an abandoned well",
      "effect": "protests from residents"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "following protests from residents"
      },
      "effect": {
        "span": "The lift station in Keelkattalai was proposed to be built on Arulmurugan Main Road , but was dropped"
      },
      "relation": "caused"
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
      "effect": {
        "span": "Earlier , residents gathered outside the police station"
      },
      "relation": "caused"
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
      "effect": {
        "span": "we were very worried [ the man ] would jump in many instances"
      },
      "relation": "caused"
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

### --- id=1901 ---

输入文本: June 29 : 35 security force personnel belonging to the Greyhounds from Andhra Pradesh were killed in a Naxal attack on a 68 - member Andhra Pradesh-Orissa police party in the Chitrakonda reservoir of Malkangiri district , close to the Andhra Pradesh border .

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
      "cause": "a Naxal attack on a 68 - member Andhra Pradesh-Orissa police party in the Chitrakonda reservoir of Malkangiri district , close to the Andhra Pradesh border",
      "effect": "35 security force personnel belonging to the Greyhounds from Andhra Pradesh were killed"
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
      "effect": {
        "span": "who had to be removed from the stadium under police escort ."
      },
      "relation": "caused"
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
        "span": "because following the Muzaffarnagar riots , the state government had received IB alerts on possible communal unrest ."
      },
      "effect": {
        "span": "Party Vice-President Ram Kishore Singh threatened to “ put him ( Modi ) behind bars ”"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1203 ---

输入文本: Striking mine workers at Impala Platinum ( Implats ) mine near Rustenburg braved the hot morning sun on Tuesday to wait for ANC Youth League president Julius Malema .

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
      "cause": "to wait for ANC Youth League president Julius Malema",
      "effect": "Striking mine workers at Impala Platinum ( Implats ) mine near Rustenburg braved the hot morning sun on Tuesday"
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
      "effect": {
        "span": "The SAHRC investigated Tatane 's death , during a protest in Ficksburg in April 2011 ,"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2609 ---

输入文本: Jitin Das , among them , resorted to fast unto death and died on the 63rd day of his fast ( September 13 ) , he said .

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
      "cause": "Jitin Das , among them , resorted to fast unto death",
      "effect": "died on the 63rd day of his fast ( September 13 )"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "resorted to fast unto death"
      },
      "effect": {
        "span": "died on the 63rd day of his fast ( September 13 )"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1624 ---

输入文本: July 12 , 2009 : Three separate attacks in Rajnandgaon district of Chhattisgarh claim the lives of 30 security personnel .

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
      "cause": "Three separate attacks in Rajnandgaon district of Chhattisgarh",
      "effect": "claim the lives of 30 security personnel"
    }
  ],
  "pred_triples": []
}
```
