# Qwen3.6 27B No Thinking CNC fixed test eval report

## 配置
```json
{
  "label": "Qwen3.6 27B No Thinking CNC fixed test",
  "model": "local/qwen3.6-27b-no-thinking",
  "dataset": "cnc_sft_test",
  "sample_count": 1038,
  "prompt_name": "v9.6",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 5,
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
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ Qwen3.6 27B No Thinking CNC fixed test final report ================
样本总数: 1038
  Gold 含因果: 548 | Pred 含因果: 677
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.774
  Precision: 0.731
  Recall   : 0.903
  F1       : 0.808
  (TP=495, TN=308, FP=182, FN=53)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 1038
    Gold triples: 763 | Pred triples: 759
    Precision: 0.493
    Recall   : 0.490
    F1       : 0.491
    (TP=374, FP=385, FN=389)
  [anchor_window] (primary)
    样本数: 1038
    Gold triples: 763 | Pred triples: 759
    Precision: 0.481
    Recall   : 0.478
    F1       : 0.480
    (TP=365, FP=394, FN=398)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 495
    Gold triples: 703 | Pred triples: 567
    Precision: 0.660
    Recall   : 0.532
    F1       : 0.589
    (TP=374, FP=193, FN=329)
  [anchor_window] (primary)
    样本数: 495
    Gold triples: 703 | Pred triples: 567
    Precision: 0.644
    Recall   : 0.519
    F1       : 0.575
    (TP=365, FP=202, FN=338)
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

Sample details shown: first 200 of 502 wrong samples from 1038 total samples.

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
        "span": "demonstrators who had defaced China 's representative office in Hong Kong"
      },
      "relation": "caused",
      "effect": {
        "span": "police fired teargas and rubber bullets on demonstrators"
      }
    }
  ]
}
```

### --- id=2124 ---

输入文本: On Tuesday we went to picket at the Western Cape Provincial Legislature after we had gone over a month without teachers .

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
      "cause": "we had gone over a month without teachers",
      "effect": "On Tuesday we went to picket at the Western Cape Provincial Legislature"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "we had gone over a month without teachers"
      },
      "relation": "caused",
      "effect": {
        "span": "we went to picket at the Western Cape Provincial Legislature"
      }
    }
  ]
}
```

### --- id=777 ---

输入文本: ANDHRA PRADESH ` Delay ' in compensation : ryots lay siege to MRO office March 14 , 2006 00:00 IST Staff Reporter Telugu Desam , CPI(M) leaders lead the protest VIJAYAWADA : Betel nut farmers from Garikaparru and Thotlavalluru villages under Thotlavalluru mandal laid siege to the Mandal Revenue Office on Monday .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "` Delay ' in compensation"
      },
      "relation": "caused",
      "effect": {
        "span": "ryots lay siege to MRO office"
      }
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
        "span": "VAT imposed by the government is unjust"
      },
      "relation": "caused",
      "effect": {
        "span": "We totally support the ongoing strike"
      }
    },
    {
      "cause": {
        "span": "we are to recover losses"
      },
      "relation": "caused",
      "effect": {
        "span": "the business has to run"
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
        "span": "the Pattali Makkal Katchi ( PMK ) for orchestrating the violence against Dalits in three villages in Dharmapuri"
      },
      "relation": "caused",
      "effect": {
        "span": "VCK leader Thol Thirumavalavan on Friday demanded a CBI investigation into the matter and action against those openly instigating caste violence on public platforms"
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
        "span": "expressing support for the police 's handling of a protest in Mong Kok"
      },
      "relation": "caused",
      "effect": {
        "span": "he caused uproar in some quarters"
      }
    },
    {
      "cause": {
        "span": "a teacher 's verbal attack on officers"
      },
      "relation": "caused",
      "effect": {
        "span": "rival groups clashed"
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
        "span": "Some protesters attacked me when I was clicking pictures"
      },
      "relation": "caused",
      "effect": {
        "span": "their colleagues dissuaded them"
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

### --- id=2566 ---

输入文本: Law ’ s parents , who initially opposed her protesting , backed her after she explained her views .

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
      "cause": "she explained her views",
      "effect": "Law ’ s parents , who initially opposed her protesting , backed her"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "she explained her views"
      },
      "relation": "caused",
      "effect": {
        "span": "Law 's parents backed her"
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
        "span": "squatted on the highway"
      },
      "relation": "caused",
      "effect": {
        "span": "Police arrested leaders of various political parties"
      }
    },
    {
      "cause": {
        "span": "to urge the central government to immediately carve out a Telangana state"
      },
      "relation": "caused",
      "effect": {
        "span": "leaders of various political parties ... squatted on the highway"
      }
    }
  ]
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
        "span": "was killed in the Maoist ambush in Koraput district yesterday"
      },
      "relation": "caused",
      "effect": {
        "span": "The mortal remains of SOG jawan Partharanjan Behera were consigned to flames today at his village in Sarilo under Kujang police limits"
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
        "span": "sustained injuries in the melee"
      },
      "relation": "caused",
      "effect": {
        "span": "Akilan was admitted to hospital here along with member of rivaal group Stalin Dinakaraj"
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
        "span": "commemorating the sacrifice of Shaheed Jitin Das and organising a memorial programme for Maoist idealogue Ganti Prasadam"
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
        "span": "the Gulberg Society riots"
      },
      "relation": "caused",
      "effect": {
        "span": "Ex - Congress MP Ehasan Jafri was among those killed"
      }
    }
  ]
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
        "span": "returning home from office on Oct 15"
      },
      "relation": "caused",
      "effect": {
        "span": "the Devarkadra agriculture extension officer had poured kerosene over herself and lit the match"
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
        "span": "allegedly attempted to blow up a Communist party building in southern Xinjiang"
      },
      "relation": "caused",
      "effect": {
        "span": "security forces shot four militants"
      }
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
        "span": "placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district with an intention of causing mass destruction to the train and passengers"
      },
      "relation": "caused",
      "effect": {
        "span": "two persons ... were detained under the National Security Act in December"
      }
    }
  ]
}
```

### --- id=2153 ---

输入文本: According to Singh , his suspension and the hunger strike were the result of an argument between Prasad and S.C. Tyagi , a deputy director at the Department of Social Welfare .

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
      "cause": "an argument between Prasad and S.C. Tyagi , a deputy director at the Department of Social Welfare",
      "effect": "his suspension and the hunger strike"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an argument between Prasad and S.C. Tyagi"
      },
      "relation": "caused",
      "effect": {
        "span": "his suspension and the hunger strike were the result"
      }
    }
  ]
}
```

### --- id=1842 ---

输入文本: In July , ANC councillor Wandile Mkhize was shot dead in a drive-by shooting near his home in Manaba , Margate .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "a drive-by shooting near his home in Manaba , Margate"
      },
      "relation": "caused",
      "effect": {
        "span": "ANC councillor Wandile Mkhize was shot dead"
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
        "span": "urged the Minister to work towards creating a sense of security amongst the minorities"
      },
      "relation": "caused",
      "effect": {
        "span": "National Commission for Minorities ( NCM ) chairperson Naseem Ahmad has written to Union Home Minister Rajnath Singh"
      }
    }
  ]
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
      "cause": "to condemn the “ extremely violent ” storming of the legislature",
      "effect": "Lam called a rare press conference early on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the “ extremely violent ” storming of the legislature"
      },
      "relation": "caused",
      "effect": {
        "span": "Lam called a rare press conference early on Tuesday to condemn"
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
        "span": "NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections , as it did not want Achuthanandan to come back to power for another term"
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

### --- id=2619 ---

输入文本: The Army and police have now launched extensive combing operations in the area to flush out the terrorists who managed to escape in dense forests after carrying out the attack .

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
        "span": "to flush out the terrorists"
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
        "span": "pelting them with stones"
      },
      "relation": "caused",
      "effect": {
        "span": "the brick kiln owners have charged the protesters"
      }
    }
  ]
}
```

### --- id=1057 ---

输入文本: TDP MLAs led by the party president N. Chandrababu Naidu staged a protest at Gun Park in front of the Assembly against the government 's inability in stopping construction of projects by the neighbouring States .

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
      "cause": "against the government 's inability in stopping construction of projects by the neighbouring States",
      "effect": "TDP MLAs led by the party president N. Chandrababu Naidu staged a protest at Gun Park in front of the Assembly"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the government 's inability in stopping construction of projects by the neighbouring States"
      },
      "relation": "caused",
      "effect": {
        "span": "TDP MLAs led by the party president N. Chandrababu Naidu staged a protest at Gun Park in front of the Assembly"
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
        "span": "the violence"
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
        "span": "the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "Four-time MP Yadav was arrested in 1999 and convicted for the murder and sentenced to life imprisonment Feb 14 , 2008 ."
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
        "span": "this was a repeat of what happened when the prime minister of India was in the country"
      },
      "relation": "caused",
      "effect": {
        "span": "party officials should have followed those who were leaving the stadium and observed them"
      }
    }
  ]
}
```

### --- id=1185 ---

输入文本: In a bid to reach out to voters , the Trinamool Congress leader participated the 7 - km padayatra from Rajabazar , a minority dominated area to Ballygung Phari covering five Assembly constituencies .

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
      "cause": "In a bid to reach out to voters",
      "effect": "the Trinamool Congress leader participated the 7 - km padayatra from Rajabazar , a minority dominated area to Ballygung Phari covering five Assembly constituencies"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to reach out to voters"
      },
      "relation": "caused",
      "effect": {
        "span": "the Trinamool Congress leader participated the 7 - km padayatra from Rajabazar , a minority dominated area to Ballygung Phari covering five Assembly constituencies"
      }
    }
  ]
}
```

### --- id=713 ---

输入文本: - Indian Express Agencies , Agencies : Bangalore , Fri Jul 27 2012 , 15:59 hrs Karnataka Assembly today witnessed a brief dharna by the entire opposition members protesting the government move to pass the Finance Bill without tabling the annual and performance reports of various departments .

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
      "cause": "protesting the government move to pass the Finance Bill without tabling the annual and performance reports of various departments",
      "effect": "Karnataka Assembly today witnessed a brief dharna by the entire opposition members"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the government move to pass the Finance Bill without tabling the annual and performance reports of various departments"
      },
      "relation": "caused",
      "effect": {
        "span": "Karnataka Assembly today witnessed a brief dharna by the entire opposition members protesting"
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
        "span": "this has created a lot of hassle for the public"
      }
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
      "relation": "caused",
      "effect": {
        "span": "capped the clashes"
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
        "span": "it is the most affordable tax imposed ever and we all should pay it"
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
        "span": "a demonstration at the district collectorate on Wednesday"
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
        "span": "the stalemate over payment of salaries to municipal workers"
      },
      "relation": "caused",
      "effect": {
        "span": "the Joint Action Committee ( JAC ) of VMC Employees bent upon continuing ‘ Work to Rule ’"
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
        "span": "to restrain them from taking part in the agitation"
      },
      "relation": "caused",
      "effect": {
        "span": "These cases were registered against them"
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

### --- id=2905 ---

输入文本: A local business was also set alight but police again managed to extinguish the fire before it did serious damage .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "police again managed to extinguish the fire"
      },
      "relation": "caused",
      "effect": {
        "span": "it did serious damage"
      }
    }
  ]
}
```

### --- id=1737 ---

输入文本: The anti-Posco activists torched our houses , damaged our betel vines and paddy crops and threw us out .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "The anti-Posco activists torched our houses , damaged our betel vines and paddy crops"
      },
      "relation": "caused",
      "effect": {
        "span": "threw us out"
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
        "span": "the agitation against land acquisition by the Uttar Pradesh government for an expressway project"
      },
      "relation": "caused",
      "effect": {
        "span": "She did not directly name Bhatta-Parsaul , the twin villages that have emerged as the epicentre of the agitation against land acquisition by the Uttar Pradesh government for an expressway project , but specifically mentioned the atrocities on farmers"
      }
    },
    {
      "cause": {
        "span": "land acquisition by the Uttar Pradesh government for an expressway project"
      },
      "relation": "caused",
      "effect": {
        "span": "the agitation against land acquisition by the Uttar Pradesh government for an expressway project"
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
        "span": "youths ... went on the rampage"
      }
    },
    {
      "cause": {
        "span": "the violence that took place on Monday when youths protesting against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC ) went on the rampage"
      },
      "relation": "caused",
      "effect": {
        "span": "The Allahabad police Tuesday registered a total of four FIRs , all at Civil Lines police station"
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
        "span": "attempted arson"
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
        "span": "renewed ' racism and Afro-phobia '"
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
        "span": "the agitation in full swing and disturbances on the campus"
      },
      "relation": "caused",
      "effect": {
        "span": "they were further postponed"
      }
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

### --- id=2963 ---

输入文本: NWU students injured in clash with security Molaole Montsho RUSTENBURG , February 24 ( ANA ) - Several students at the Mafikeng Campus of the North West University were injured when they clashed with campus security on Wednesday , the University said .

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
      "cause": "they clashed with campus security on Wednesday",
      "effect": "Several students at the Mafikeng Campus of the North West University were injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they clashed with campus security"
      },
      "relation": "caused",
      "effect": {
        "span": "Several students at the Mafikeng Campus of the North West University were injured"
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
        "span": "the Cabinet 's nod for draft bill for bifurcation of the state"
      },
      "relation": "caused",
      "effect": {
        "span": "The two-day bandh call given by the pro-United Andhra Pradesh groups against the Cabinet 's nod for draft bill for bifurcation of the state has evoked a mixed response in the coastal Andhra and Rayalaseema regions on the second day today"
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
        "span": "skirmishes and clashes , including stone pelting"
      },
      "relation": "caused",
      "effect": {
        "span": "two policemen were injured"
      }
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
        "span": "in support of party president Y.S. Jaganmohan Reddy ’ s indefinite ‘ deeksha ’ in Guntur seeking special category status for the State"
      },
      "relation": "caused",
      "effect": {
        "span": "YSR Congress leaders and cadres organised relay hunger strikes in various Assembly constituencies across the district on Thursday"
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
        "span": "lack of amenities"
      },
      "relation": "caused",
      "effect": {
        "span": "Two separate agitations were witnessed on the Corporation office premises on Tuesday with residents and political activists laying siege to the offices of the Mayor and the Commissioner ."
      }
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
        "span": "a communal violence broke out near St Xavier 's High School in the Mirzapur area of Ahmedabad late on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "The city police had to resort to tear gas shelling"
      }
    }
  ]
}
```

### --- id=1905 ---

输入文本: April 26 : Three policemen and two CPI-Maoist cadres were killed in an encounter in Dumka , Jharkhand .

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
      "cause": "an encounter in Dumka , Jharkhand .",
      "effect": "Three policemen and two CPI-Maoist cadres were killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an encounter in Dumka , Jharkhand"
      },
      "relation": "caused",
      "effect": {
        "span": "Three policemen and two CPI-Maoist cadres were killed"
      }
    }
  ]
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
      "relation": "caused",
      "effect": {
        "span": "Hundreds of members of the Police and Prisons Civil Rights Union gathered at the King Dinuzulu Gardens in Durban on Wednesday ahead of a march"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Some of the youths ... barricaded the doors of their cells"
      }
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
        "span": "the gun battle"
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
      "cause": "Paramilitary troops and a two-person militant suicide squad fought a 22 - hour gunbattle at a Kashmir security camp which ended on Tuesday",
      "effect": "eight dead and nine wounded"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Paramilitary troops and a two-person militant suicide squad fought a 22 - hour gunbattle at a Kashmir security camp"
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
      "cause": "the killing of Swami Lakshmanananda Saraswati",
      "effect": "There was also largescale displacement in Kandhamal district during and after the 2008 riots"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the killing of Swami Lakshmanananda Saraswati"
      },
      "relation": "caused",
      "effect": {
        "span": "largescale displacement in Kandhamal district during and after the 2008 riots"
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
        "span": "hundreds of mainly young , masked protesters mostly in black wearing hard hats and goggles seized three key thoroughfares"
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
        "span": "the “ carnage . ”"
      },
      "relation": "caused",
      "effect": {
        "span": "the people would give a fitting reply to the Communist Party of India (Marxist)-led government"
      }
    },
    {
      "cause": {
        "span": "the “ atrocities committed by CPI(M) cadres on the innocent people of Nandigram , ”"
      },
      "relation": "caused",
      "effect": {
        "span": "Ms. Banerjee said even after a year “ those responsible had not been punished ."
      }
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
      "relation": "caused",
      "effect": {
        "span": "Farmers stage dharna in Harihar"
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
        "span": "the attack on the woman MLA"
      },
      "relation": "caused",
      "effect": {
        "span": "The MLAs , along with a large number of party supporters , condemned"
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
        "span": "the temporary suspension of the employers ' levy"
      },
      "relation": "caused",
      "effect": {
        "span": "About 1,000 foreign domestic helpers yesterday protested against the temporary suspension of the employers ' levy"
      }
    },
    {
      "cause": {
        "span": "it had threatened their livelihoods"
      },
      "relation": "caused",
      "effect": {
        "span": "About 1,000 foreign domestic helpers yesterday protested against the temporary suspension of the employers ' levy"
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
        "span": "such people ( those who unfurled the Vidarbha flag )"
      },
      "relation": "caused",
      "effect": {
        "span": "the country 's integrity is damaged"
      }
    }
  ]
}
```

### --- id=1225 ---

输入文本: “ Members of Hindu organisations are blaming the violence at Ambur on us and allege the presence of MLA A Aslam Basha at the incident site .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the violence at Ambur"
      },
      "relation": "caused",
      "effect": {
        "span": "Members of Hindu organisations are blaming ... us"
      }
    }
  ]
}
```

### --- id=1038 ---

输入文本: Farmers Block NH 7 , Say Government Blind to Their Plight 21st June 2015 06:00 AM CHIKBALLAPUR : Farmers on Saturday blocked the busy National Highway 7 on the outskirts of the city for nearly five hours and shouted slogans against the Union and state governments .

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
      "cause": "against the Union and state governments",
      "effect": "Farmers on Saturday blocked the busy National Highway 7 on the outskirts of the city for nearly five hours and shouted slogans"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Government Blind to Their Plight"
      },
      "relation": "caused",
      "effect": {
        "span": "Farmers on Saturday blocked the busy National Highway 7 on the outskirts of the city for nearly five hours and shouted slogans against the Union and state governments"
      }
    }
  ]
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
        "span": "the fierce encounter with militants holed up inside a government building in Pampore town"
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
        "span": "a migrant labourer from U P was allegedly beaten to death by a group of Marathi-speaking men on a suburban train headed for Mumbai"
      },
      "relation": "caused",
      "effect": {
        "span": "the Centre issued a stern advisory to the Maharashtra government , asking it to act quickly to end the violence against north Indians and ensure the safety of everyone living in India 's financial capital"
      }
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
        "span": "Lam ' s attempts to pass the proposed extradition legislation"
      },
      "relation": "caused",
      "effect": {
        "span": "the recent protests were initially sparked"
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
        "span": "to protest denial of worship rights in the village temple"
      },
      "relation": "caused",
      "effect": {
        "span": "Arunthathiyar community men refused to perform funeral rituals for a Caste Hindu family"
      }
    }
  ]
}
```

### --- id=115 ---

输入文本: TMC workers have been accused of leading the attacks .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "leading the attacks"
      },
      "relation": "caused",
      "effect": {
        "span": "TMC workers have been accused"
      }
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
        "span": "the cases were filed against the students only to discourage them from participating in separate Telangana agitations"
      },
      "relation": "caused",
      "effect": {
        "span": "Chandrasekhar Rao demanded that the cases be lifted immediately"
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
      "cause": "security forces and Naxalites had an encounter near village Belgaon  12 km from Bairamgarh in Bijapur",
      "effect": "killing a Maoist rebel on the spot"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "security forces and Naxalites had an encounter near village Belgaon"
      },
      "relation": "caused",
      "effect": {
        "span": "killing a Maoist rebel on the spot"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Some chanted"
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

### --- id=285 ---

输入文本: Police opened fire , killing 34 striking workers and wounding 78 while trying to disperse a group gathered on a hill near Lonmin 's platinum mine in Marikana on August 16 .

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
        "span": "Police opened fire"
      },
      "relation": "caused",
      "effect": {
        "span": "killing 34 striking workers and wounding 78"
      }
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
        "span": "the CPM and BJP workers scuffled outside the AKG Centre"
      },
      "relation": "caused",
      "effect": {
        "span": "600 people were detained"
      }
    }
  ]
}
```

### --- id=124 ---

输入文本: " The miscreants , who were earlier with the CPM and have recently joined the TMC , are responsible for the violence , " Chowdhury said .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "The miscreants , who were earlier with the CPM and have recently joined the TMC"
      },
      "relation": "caused",
      "effect": {
        "span": "the violence"
      }
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
        "span": "Tuesday ’ s incident"
      },
      "relation": "caused",
      "effect": {
        "span": "Chidambaram refered to the Dantewada massacre of 75 CRPF men and said the companies of CRPF in Chintalnar and Chintagufa were deployed by the state government"
      }
    }
  ]
}
```

### --- id=44 ---

输入文本: Ramanathapuram Residents protest against illegal water connections

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
      "cause": "against illegal water connections",
      "effect": "Ramanathapuram Residents protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "illegal water connections"
      },
      "relation": "caused",
      "effect": {
        "span": "Ramanathapuram Residents protest against illegal water connections"
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

### --- id=1839 ---

输入文本: `` We are very concerned with the killing of our comrades .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the killing of our comrades"
      },
      "relation": "caused",
      "effect": {
        "span": "We are very concerned"
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
        "span": "public violence while protesting against financial aid cuts at the University of the Witwatersrand"
      },
      "relation": "caused",
      "effect": {
        "span": "Twelve students arrested"
      }
    }
  ]
}
```

### --- id=976 ---

输入文本: There was a shutdown in various towns in Jammu regions against the incident .

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
      "cause": "against the incident",
      "effect": "There was a shutdown in various towns in Jammu regions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "There was a shutdown in various towns in Jammu regions"
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
        "span": "a huge rally was organised from pavilion grounds to the Collectorate"
      }
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
        "span": "to release medical bulletins on the health of Jagan"
      },
      "relation": "caused",
      "effect": {
        "span": "YSRC leaders Shoba Nagireddy , Praveen Kumar Reddy , G Babu Rao met jails IG Sunil Kumar and represented to him"
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
        "span": "against the SP"
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
        "span": "raising several demands"
      },
      "relation": "caused",
      "effect": {
        "span": "Protest Federation of various autorickshaw employees union on Thursday staged a protest in front of regional transport office"
      }
    }
  ]
}
```

### --- id=484 ---

输入文本: The clash left at least three students injured .

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
      "cause": "The clash",
      "effect": "left at least three students injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The clash"
      },
      "relation": "caused",
      "effect": {
        "span": "at least three students injured"
      }
    }
  ]
}
```

### --- id=1809 ---

输入文本: Maoist banners found 10th April 2011 05:14 AM KORAPUT : MAOIST banners were found near the District Primary Education Project ( DPEP ) office today in which the ultras threatened to kill Shikhya Sahayak candidates , outsiders to the district , who have been selected to join the service here .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the ultras threatened to kill Shikhya Sahayak candidates , outsiders to the district , who have been selected to join the service here"
      },
      "relation": "caused",
      "effect": {
        "span": "MAOIST banners were found near the District Primary Education Project ( DPEP ) office today"
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
        "span": "arrests of Telangana protagonists from Adilabad district"
      },
      "relation": "caused",
      "effect": {
        "span": "TRS ... condemned arrests"
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
        "span": "whoever was responsible ... would be dealt with sternly"
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
        "span": "protesting farmers blocked the main access road"
      },
      "relation": "caused",
      "effect": {
        "span": "Sino Gold Mining ... had to halt operations yesterday"
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
        "span": "CPI-Maoist cadres killed 17 personnel of the Special Operations Group of the Orissa Police in a landmine blast in Malkangiri district"
      },
      "relation": "caused",
      "effect": {
        "span": "July 16"
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
      "relation": "caused",
      "effect": {
        "span": "Thirty-seven of the operators signed a petition and held a press conference last Sunday"
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

### --- id=1506 ---

输入文本: The image used in the advert was taken from a protest in Bekkersdal where the police had to restore public order , he said .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "a protest in Bekkersdal"
      },
      "relation": "caused",
      "effect": {
        "span": "the police had to restore public order"
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
        "span": "the blast"
      },
      "relation": "caused",
      "effect": {
        "span": "Maoists opened indiscriminate firing"
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
        "span": "reports the authorities had tried to prevent the demonstration"
      },
      "relation": "caused",
      "effect": {
        "span": "yesterday 's turnout was smaller"
      }
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
        "span": "Police did not provide any protection to us"
      },
      "relation": "caused",
      "effect": {
        "span": "I was threatened that I will also meet the fate of my daughter"
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
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
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
        "span": "students agitating over creation of a separate Telangana hurled stones at them"
      },
      "relation": "caused",
      "effect": {
        "span": "over 22 people , including five media men and 11 security personnel with an officer among them , were injured last night"
      }
    },
    {
      "cause": {
        "span": "students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus"
      },
      "relation": "caused",
      "effect": {
        "span": "prompting them to use force to quell the mob"
      }
    },
    {
      "cause": {
        "span": "creation of a separate Telangana"
      },
      "relation": "caused",
      "effect": {
        "span": "students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus"
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
        "span": "a Secretariat dharna was staged under the joint aegis of the Kalanilayam Paristhithi Vedi , environmentalists and cultural activists here on Monday"
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
        "span": "the protests"
      },
      "relation": "caused",
      "effect": {
        "span": "Hong Kong has changed a lot"
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
      "relation": "caused",
      "effect": {
        "span": "Traders pulled down their shutters"
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

### --- id=2659 ---

输入文本: ONGOLE : Congress workers on Monday attacked TDP senior leader and MLC Nannapaneni Rajakumari with sticks and stones leaving her badly mauled at Karamchedu , native village of Union Minister of State Daggubati Purandeswari ’ s husband and Parchur MLA Venkateswara Rao .

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
      "cause": "Congress workers on Monday attacked TDP senior leader and MLC Nannapaneni Rajakumari with sticks and stones",
      "effect": "leaving her badly mauled at Karamchedu"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Congress workers on Monday attacked TDP senior leader and MLC Nannapaneni Rajakumari with sticks and stones"
      },
      "relation": "caused",
      "effect": {
        "span": "leaving her badly mauled"
      }
    }
  ]
}
```

### --- id=2871 ---

输入文本: Two men who confessed to being involved in the murder of ANC North West official Obuti Chika were tortured by police , the Klerksdorp Magistrate 's Court heard on Tuesday .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "confessed to being involved in the murder of ANC North West official Obuti Chika"
      },
      "relation": "caused",
      "effect": {
        "span": "Two men ... were tortured by police"
      }
    }
  ]
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
        "span": "to curb violence , protect infrastructure and prevent further damage to the economy arising out of events such as looting , attacks on foreign nationals and the torching of trucks in an ongoing labour protest"
      },
      "relation": "caused",
      "effect": {
        "span": "DA MP Andrew Whitfield said he would ask police commissioner General Khehla Sitole to activate the National Joint Operations and Intelligence Structure ( Natjoints ) to intervene"
      }
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
        "span": "the high crime rate in the country , in Alice in particular"
      },
      "relation": "caused",
      "effect": {
        "span": "The memorandum , from the residents of Ward 10 in the Nkonkobe municipality registered resentment and disapproval"
      }
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
      "relation": "caused",
      "effect": {
        "span": "BJP legislators staged a dharna"
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
      "cause": "A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials",
      "effect": "were arrested in Central yesterday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials"
      },
      "relation": "caused",
      "effect": {
        "span": "A couple ... were arrested in Central yesterday"
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
        "span": "violence that erupted during a rally by Muslims in Mumbai 's Azad Maidan"
      },
      "relation": "caused",
      "effect": {
        "span": "This outrageous and provocative statement comes"
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
        "span": "this"
      },
      "relation": "caused",
      "effect": {
        "span": "the police appealed to the agitators to withdraw the strike"
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
        "span": "they were returning from leave to district headquarters Narayanpur town"
      },
      "relation": "caused",
      "effect": {
        "span": "The abducted jawans were unarmed and also not in police uniform"
      }
    }
  ]
}
```

### --- id=43 ---

输入文本: December 05 , 2017 00:00 IST Say officials at the panchayat level are colluding with locals Residents of Varavani panchayat staged a protest at the collectorate here on Monday , against illegal tapping of drinking water supplied through pipelines under the Cauvery combined water supply scheme and irregular supply of water to their villages .

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
      "cause": "against illegal tapping of drinking water supplied through pipelines under the Cauvery combined water supply scheme and irregular supply of water to their villages",
      "effect": "Residents of Varavani panchayat staged a protest at the collectorate here on Monday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "illegal tapping of drinking water supplied through pipelines under the Cauvery combined water supply scheme and irregular supply of water to their villages"
      },
      "relation": "caused",
      "effect": {
        "span": "Residents of Varavani panchayat staged a protest at the collectorate here on Monday"
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
        "span": "some of their colleagues got hurt during the stone-pelting"
      },
      "relation": "caused",
      "effect": {
        "span": "the police ... lost temper and rataliated"
      }
    }
  ]
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
        "span": "to protest against plans to built a paraxylene chemical plant in the city"
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
        "span": "the attempts made by the TRS and pro-Telangana activists to proceed and participate in ‘ Million March ' in Hyderabad on Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "The district police foiled ... with their arrests on various routes proceeding to the capital"
      }
    }
  ]
}
```

### --- id=3026 ---

输入文本: The BJP leader also termed that beating of those persons , who throws ink or slaps Kejriwal by his supporters looks like filmy and part of this conspiracy .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "beating of those persons , who throws ink or slaps Kejriwal by his supporters looks like filmy and part of this conspiracy"
      },
      "relation": "caused",
      "effect": {
        "span": "The BJP leader also termed that beating of those persons , who throws ink or slaps Kejriwal by his supporters looks like filmy and part of this conspiracy"
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
        "span": "the violent incidents that took place at the Madras High Court premises in Chennai on February 19 this year"
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
        "span": "a farm house was on fire , two more house were set alight and road blocked"
      }
    }
  ]
}
```

### --- id=536 ---

输入文本: Members of the minority sect went on a rampage and allegedly set fire to the kitchen of the house belonging to a member of the majority sect .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Members of the minority sect went on a rampage"
      },
      "relation": "caused",
      "effect": {
        "span": "allegedly set fire to the kitchen of the house belonging to a member of the majority sect"
      }
    }
  ]
}
```

### --- id=217 ---

输入文本: Local drivers have allegedly been attacking the vehicles and threatening foreign drivers , who they accuse of taking jobs meant for locals .

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
      "cause": "who they accuse of taking jobs meant for locals",
      "effect": "Local drivers have allegedly been attacking the vehicles and threatening foreign drivers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they accuse of taking jobs meant for locals"
      },
      "relation": "caused",
      "effect": {
        "span": "Local drivers have allegedly been attacking the vehicles and threatening foreign drivers"
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
        "span": "allegedly being denied a scholarship by his school"
      },
      "relation": "caused",
      "effect": {
        "span": "a Class XII Dalit dropout of the Government Higher Secondary School in Allinagaram , in Theni district , tied to immolate himself on Tuesday"
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
        "span": "the news"
      },
      "relation": "caused",
      "effect": {
        "span": "Hardik Patel , the face of Patel quota stir , called it \" failure \" of the government"
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
        "span": "they had met publicly on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "Shiv Sena workers had barged in violently to break up their peaceful protest"
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
        "span": "over supply of drinking water"
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
        "span": "violence related to the illegal strike"
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
        "span": "the case"
      },
      "relation": "caused",
      "effect": {
        "span": "injury to accused no : 37"
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
        "span": "the strike"
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
        "span": "their regular promotions were denied"
      },
      "relation": "caused",
      "effect": {
        "span": "the indefinite hunger strike launched by three employees Mahesh Ahire , Shriram Gavai and Balkrishna Gadekar"
      }
    }
  ]
}
```

### --- id=66 ---

输入文本: However , when he was returning home in the night , Pradhan was intercepted again by them and killed .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "he was returning home in the night"
      },
      "relation": "caused",
      "effect": {
        "span": "Pradhan was intercepted again by them and killed"
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
        "span": "N. Venkatesh , 28 , an assistant in the administration department of the corporation ... committed suicide on railway tracks"
      }
    },
    {
      "cause": {
        "span": "the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "an all-union meeting convened by the CITU resolved to organise demonstrations in front of all industrial establishments located in the city on Wednesday"
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
        "span": "the political and media pressure mounts"
      },
      "relation": "caused",
      "effect": {
        "span": "it becomes harder for us to exercise those options"
      }
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
        "span": "to demand the relocation of a chemical plant"
      },
      "relation": "caused",
      "effect": {
        "span": "tens of thousands of people in the northeastern city of Dalian , Liaoning , marched"
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
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
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
      "relation": "caused",
      "effect": {
        "span": "The students ... demanded that it be returned to them"
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
        "span": "common people do not suffer"
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
        "span": "suppressing a peaceful and democratic protest"
      },
      "relation": "caused",
      "effect": {
        "span": "He accused the government"
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
        "span": "the arrest of student union president Kanhaiya Kumar"
      },
      "relation": "caused",
      "effect": {
        "span": "The escalating protests in the JNU"
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
        "span": "should be a further reminder to Washington of the danger of allowing groups like LeT any breathing space"
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
        "span": "the vehicle was vandalised"
      }
    }
  ]
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
        "span": "allegedly defaming Prime Minister Manmohan Singh in their protest act , wherein they alluded that he was anti-national , in addition to passing disparaging remarks about him"
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
        "span": "Employees at three factories had signed a petition"
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
        "span": "the circumstances"
      },
      "relation": "caused",
      "effect": {
        "span": "forced the community members to stage such a protest"
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
        "span": "the protest"
      },
      "relation": "caused",
      "effect": {
        "span": "a community hall was torched"
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
        "span": "Pakistani gunmen attacked Mumbai last year"
      },
      "relation": "caused",
      "effect": {
        "span": "India had suspended the talks"
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
      "relation": "caused",
      "effect": {
        "span": "violent protests across the city the next day , with a group of students even storming into the university campus and demanding the dismissal of the teacher who had set the question paper ."
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

### --- id=783 ---

输入文本: The company had further offered a once-off hardship allowance of R2000 to help workers deal with financial difficulties arising from the no-work , no-pay principle in place while they were striking .

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
        "span": "financial difficulties arising from the no-work , no-pay principle in place while they were striking"
      },
      "relation": "caused",
      "effect": {
        "span": "The company had further offered a once-off hardship allowance of R2000 to help workers deal with financial difficulties arising from the no-work , no-pay principle in place while they were striking"
      }
    },
    {
      "cause": {
        "span": "the no-work , no-pay principle in place while they were striking"
      },
      "relation": "caused",
      "effect": {
        "span": "financial difficulties arising from the no-work , no-pay principle in place while they were striking"
      }
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
      "relation": "caused",
      "effect": {
        "span": "TDP members were mobbed"
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
        "span": "two BJP central teams , which visited Birbhum and South 24 Parganas districts , had submitted its report to Union Home Minister Rajnath Singh"
      }
    }
  ]
}
```

### --- id=2653 ---

输入文本: The encroachers , who have been on a protest for two years , demand " cancellation of the elections " of the President and Prime Minister of India .

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
      "cause": "demand \" cancellation of the elections \" of the President and Prime Minister of India",
      "effect": "The encroachers , who have been on a protest for two years"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "on a protest"
      },
      "relation": "caused",
      "effect": {
        "span": "The encroachers ... demand \" cancellation of the elections \" of the President and Prime Minister of India ."
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
        "span": "People Opposing Woman Abuse ( Powa ) said on Friday at a protest outside the Johannesburg High Court"
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
        "span": "the web of security tightens"
      }
    },
    {
      "cause": {
        "span": "The May Day twin blasts on platform nine of Chennai Central"
      },
      "relation": "caused",
      "effect": {
        "span": "sent a strong message to various enforcement agencies in the city"
      }
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
        "span": "police fired rubber bullets"
      },
      "relation": "caused",
      "effect": {
        "span": "eight students were arrested and four injured"
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
        "span": "the protestors against the church attack were assaulted by police , youth were hunted and criminal cases were booked on them"
      },
      "relation": "caused",
      "effect": {
        "span": "Urging the Commission to reveal names of people involved in the attacks"
      }
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
      "relation": "caused",
      "effect": {
        "span": "community members mobilised and marched to a suspected gang member 's house in Bardien Street where Tavern Moss was stabbed and beaten to death"
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
        "span": "making a slew of demands , including shifting the institute out of Kashmir and action against the policemen involved in lathicharge yesterday"
      },
      "relation": "caused",
      "effect": {
        "span": "Tension prevailed at NIT here with outstation students today"
      }
    },
    {
      "cause": {
        "span": "the crisis being witnessed since last six days"
      },
      "relation": "caused",
      "effect": {
        "span": "an HRD team rushed here from Delhi to resolve the crisis being witnessed since last six days"
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
        "span": "demanding that the police produce in a court of law the party 's Andhra-Orissa border special zone committee member and a central committee member Damodar alias Azad , who was reportedly taken into custody a few days ago"
      },
      "relation": "caused",
      "effect": {
        "span": "the CPI ( Maoist ) gave the call"
      }
    },
    {
      "cause": {
        "span": "the CPI ( Maoist ) gave the call demanding that the police produce in a court of law the party 's Andhra-Orissa border special zone committee member and a central committee member Damodar alias Azad , who was reportedly taken into custody a few days ago"
      },
      "relation": "caused",
      "effect": {
        "span": "Maoists observe bandh in Visakha Agency area"
      }
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
        "span": "used in the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Tohtunyaz helped them to acquire more than 10 knives"
      }
    }
  ]
}
```

### --- id=2061 ---

输入文本: Dharna staged against reclamation of lake

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
      "cause": "against reclamation of lake",
      "effect": "Dharna staged"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "reclamation of lake"
      },
      "relation": "caused",
      "effect": {
        "span": "Dharna staged against reclamation of lake"
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
        "span": "the murder of two Hindi-speaking persons last week by the Paresh Baruah faction of the banned United Liberation Front of Assam ( Ulfa ) , which also threatened to target the community in the coming days"
      },
      "relation": "caused",
      "effect": {
        "span": "people took out a march here on Sunday to demonstrate their anger against the outfit"
      }
    }
  ]
}
```

### --- id=1579 ---

输入文本: DAVANGERE : CPI protests against price rise in Davangere

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
      "cause": "against price rise in Davangere",
      "effect": "CPI protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "price rise in Davangere"
      },
      "relation": "caused",
      "effect": {
        "span": "CPI protests against price rise in Davangere"
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

### --- id=1197 ---

输入文本: Later , they handed over a memorandum to her assistants urging the party leader ’ s intervention .

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
      "cause": "urging the party leader ’ s intervention",
      "effect": "they handed over a memorandum to her assistants"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "urging the party leader 's intervention"
      },
      "relation": "caused",
      "effect": {
        "span": "they handed over a memorandum to her assistants"
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
        "span": "the Naxalites ' falling support base"
      },
      "relation": "caused",
      "effect": {
        "span": "the abductions are the outcome"
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
        "span": "the snap protest by the Karnataka State Reserve Police ( KSRP ) personnel extending support to their chief P. Ravindranath , who has now been transferred"
      },
      "relation": "caused",
      "effect": {
        "span": "senior officials on Thursday chalked out a strategy to prevent them from continuing the protest by deploying all the 1,200 KSRP personnel on various duties"
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
        "span": "another instance of sudden ambush and massacre of Central Reserve Police Force personnel by Maoists"
      },
      "relation": "caused",
      "effect": {
        "span": "the Centre on Wednesday gave hint of enacting a tactical retreat from Naxal strongholds like Dantewada and Narayanpur in Chhattisgarh , camouflaging it as ‘ revisiting deployment ’"
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
      "cause": "the shutdown success",
      "effect": "the much-needed shot in the arm to him to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the shutdown success has provided the much-needed shot in the arm to him"
      },
      "relation": "caused",
      "effect": {
        "span": "him to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP"
      }
    }
  ]
}
```

### --- id=983 ---

输入文本: Police quickly took away protesters displaying banners .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "displaying banners"
      },
      "relation": "caused",
      "effect": {
        "span": "Police quickly took away protesters"
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
        "span": "around 2,000 residents of Somasandrapalya , Haraluru , HSR Layout , Kudlu , Mangamanapalya , Hosapalya and surrounding areas gathered near Ravindra Bharathi Global School in HSR Layout on Saturday and formed a human chain near a wall constructed by Sobha Daffodil apartment"
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
        "span": "police tried to stop Arya Pratinidhi Sabha activists from marching towards the Ashram"
      },
      "relation": "caused",
      "effect": {
        "span": "The row over possession of Satlok Ashram , headed by Rampal , took a violent turn on Sunday"
      }
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
        "span": "a mob gathered near a mosque"
      },
      "relation": "caused",
      "effect": {
        "span": "threw two crude bombs at the police"
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
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Traders against plan to amend APMC Act"
      },
      "relation": "caused",
      "effect": {
        "span": "the APMC traders across the State observe bandh"
      }
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
        "span": "supporting armed revolt against the government"
      },
      "relation": "caused",
      "effect": {
        "span": "a group of persons attacked the NHAI office at Kalamassery and distributed notices"
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
        "span": "demanding re-appear examination at the earliest to fulfill 50 per cent credit requirement for students in University Institute of Engineering and Technology ( UIET )"
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
        "span": "a landmine blast triggered by suspected CPI-Maoist cadres at Pundigiri village in Bundu , 50 - kilometres from Ranchi"
      },
      "relation": "caused",
      "effect": {
        "span": "A DSP and four constables were killed"
      }
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
        "span": "the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "was forced on us"
      }
    }
  ]
}
```

### --- id=2042 ---

输入文本: The party 's provincial task team co-ordinator Saki Mafikeng said the meeting took place at the Tshing stadium , following service delivery protests in the Ventersdorp area over the weekend .

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
      "cause": "service delivery protests in the Ventersdorp area over the weekend",
      "effect": "the meeting took place at the Tshing stadium"
    }
  ],
  "pred_triples": []
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
        "span": "the threat call to Nehru"
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
        "span": "claiming that he was not at the spot"
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
        "span": "the power of the internet helped foster the massive march in 2003"
      },
      "relation": "caused",
      "effect": {
        "span": "everyone is keenly aware"
      }
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
