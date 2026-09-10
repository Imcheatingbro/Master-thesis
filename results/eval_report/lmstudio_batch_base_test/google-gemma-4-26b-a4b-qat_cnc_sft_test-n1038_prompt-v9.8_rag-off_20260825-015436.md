# Gemma 4 26B A4B QAT CNC fixed test eval report

## 配置
```json
{
  "label": "Gemma 4 26B A4B QAT CNC fixed test",
  "model": "google/gemma-4-26b-a4b-qat",
  "dataset": "cnc_sft_test",
  "sample_count": 1038,
  "prompt_name": "v9.8",
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
================ Gemma 4 26B A4B QAT CNC fixed test final report ================
样本总数: 1038
  Gold 含因果: 548 | Pred 含因果: 658
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.782
  Precision: 0.745
  Recall   : 0.894
  F1       : 0.813
  (TP=490, TN=322, FP=168, FN=58)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 1038
    Gold triples: 763 | Pred triples: 745
    Precision: 0.501
    Recall   : 0.489
    F1       : 0.495
    (TP=373, FP=372, FN=390)
  [anchor_window] (primary)
    样本数: 1038
    Gold triples: 763 | Pred triples: 745
    Precision: 0.574
    Recall   : 0.561
    F1       : 0.568
    (TP=428, FP=317, FN=335)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 490
    Gold triples: 698 | Pred triples: 561
    Precision: 0.665
    Recall   : 0.534
    F1       : 0.593
    (TP=373, FP=188, FN=325)
  [anchor_window] (primary)
    样本数: 490
    Gold triples: 698 | Pred triples: 561
    Precision: 0.763
    Recall   : 0.613
    F1       : 0.680
    (TP=428, FP=133, FN=270)
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

Sample details shown: first 200 of 459 wrong samples from 1038 total samples.

### --- id=2291 ---

输入文本: Protesters have also surrounded the police headquarters twice in past weeks in noisy and emotionally charged protests in which young people spray-painted obscenities on its front wall and barricaded its entrances .

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
        "span": "in noisy and emotionally charged protests"
      },
      "relation": "caused",
      "effect": {
        "span": "Protesters have also surrounded the police headquarters twice in past weeks in noisy and emotionally charged protests in which young people spray-painted obscenities on its front wall and barricaded its entrances"
      }
    },
    {
      "cause": {
        "span": "in noisy and emotionally charged protests in which young people spray-painted obscenities on its front wall and barricaded its entrances"
      },
      "relation": "caused",
      "effect": {
        "span": "young people spray-painted obscenities on its front wall and barricaded its entrances"
      }
    }
  ]
}
```

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
      "relation": "caused",
      "effect": {
        "span": "police fired teargas and rubber bullets on demonstrators"
      }
    }
  ]
}
```

### --- id=450 ---

输入文本: Protestors in Clashes With Police on Jammu-Pathankot NH During Eviction Drive 22nd February 2016 05:22 PM JAMMU : Clashes erupted on the Jammu-Pathankot national highway between police and protesters in Samba district of Jammu region on Monday , police said .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "During Eviction Drive"
      },
      "relation": "caused",
      "effect": {
        "span": "Clashes erupted on the Jammu-Pathankot national highway between police and protesters in Samba district of Jammu region on Monday"
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
        "span": "Delay ' in compensation"
      },
      "relation": "caused",
      "effect": {
        "span": "ryots lay siege to MRO office March 14 , 2006 00:00 IST"
      }
    },
    {
      "cause": {
        "span": "Delay ' in compensation"
      },
      "relation": "caused",
      "effect": {
        "span": "Betel nut farmers from Garikaparru and Thotlavalluru villages under Thotlavalluru mandal laid siege to the Mandal Revenue Office on Monday ."
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
      "relation": "caused",
      "effect": {
        "span": "We totally support the ongoing strike"
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

### --- id=2070 ---

输入文本: 17th November 2012 11:20 AM Squarely blaming the Pattali Makkal Katchi ( PMK ) for orchestrating the violence against Dalits in three villages in Dharmapuri , VCK leader Thol Thirumavalavan on Friday demanded a CBI investigation into the matter and action against those openly instigating caste violence on public platforms .

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
        "span": "for orchestrating the violence against Dalits in three villages in Dharmapuri"
      },
      "relation": "caused",
      "effect": {
        "span": "VCK leader Thol Thirumavalavan on Friday demanded a CBI investigation into the matter and action against those openly instigating caste violence on public platforms ."
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
        "span": "to urge the central government to immediately carve out a Telangana state ."
      },
      "relation": "caused",
      "effect": {
        "span": "the ' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC )"
      }
    },
    {
      "cause": {
        "span": "the ' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC )"
      },
      "relation": "caused",
      "effect": {
        "span": "leaders of various political parties who squatted on the highway"
      }
    },
    {
      "cause": {
        "span": "leaders of various political parties who squatted on the highway"
      },
      "relation": "caused",
      "effect": {
        "span": "Police arrested leaders of various political parties"
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
        "span": "the Maoist ambush in Koraput district yesterday"
      },
      "relation": "caused",
      "effect": {
        "span": "SOG jawan Partharanjan Behera , who was killed in the Maoist ambush in Koraput district yesterday , were consigned to flames today at his village in Sarilo under Kujang police limits ."
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
        "span": "who allegedly attempted to blow up a Communist party building in southern Xinjiang"
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
        "span": "two persons , who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district ... were detained under the National Security Act in December"
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
        "span": "in a drive-by shooting"
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
        "span": "the growing violence against Muslims by vigilante groups"
      },
      "relation": "caused",
      "effect": {
        "span": "has urged the Minister to work towards creating a sense of security amongst the minorities ."
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
        "span": "as it did not want Achuthanandan to come back to power for another term"
      },
      "relation": "caused",
      "effect": {
        "span": "the NSS did not support the LDF in the recent Assembly elections"
      }
    },
    {
      "cause": {
        "span": "NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections , as it did not want Achuthanandan to come back to power for another term"
      },
      "relation": "caused",
      "effect": {
        "span": "The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram"
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

### --- id=229 ---

输入文本: Violence first broke out in the hill district on September 26 when three auto-rickshaw drivers , all belonging to the Dimasa tribe , were killed .

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
      "cause": "three auto-rickshaw drivers , all belonging to the Dimasa tribe , were killed",
      "effect": "Violence first broke out in the hill district on September 26"
    }
  ],
  "pred_triples": []
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
        "span": "when they approached with a proposal to accept their demands"
      },
      "relation": "caused",
      "effect": {
        "span": "the brick kiln owners have charged the protesters with pelting them with stones"
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
        "span": "during the violence"
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
        "span": "for the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "Four-time MP Yadav was arrested in 1999 and convicted for the murder and sentenced to life imprisonment Feb 14 , 2008 ."
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
        "span": "the Trinamool Congress leader participated the 7 - km padayatra from Rajabazar , a minority dominated area to Ballygung Phari covering five Assembly constituencies ."
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
        "span": "Following a demonstration at the district collectorate on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "the students handed over a memorandum addressed to the Governor to Additional District Magistrate Akhilesh Ojha, who assured them of a fair inquiry ."
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
        "span": "fear and economic inducements ensured they turned away from politics"
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
        "span": "The stalemate over payment of salaries to municipal workers"
      },
      "relation": "caused",
      "effect": {
        "span": "the Joint Action Committee ( JAC ) of VMC Employees bent upon continuing ‘ Work to Rule ’ ."
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
        "span": "The anti-Posco activists"
      },
      "relation": "caused",
      "effect": {
        "span": "torched our houses , damaged our betel vines and paddy crops and threw us out ."
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
        "span": "the agitation against land acquisition by the Uttar Pradesh government for an expressway project"
      },
      "relation": "caused",
      "effect": {
        "span": "the twin villages that have emerged as the epicentre of the agitation"
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
        "span": "the violence that took place on Monday when youths protesting against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC ) went on the rampage"
      },
      "relation": "caused",
      "effect": {
        "span": "The Allahabad police Tuesday registered a total of four FIRs , all at Civil Lines police station"
      }
    },
    {
      "cause": {
        "span": "protesting against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC )"
      },
      "relation": "caused",
      "effect": {
        "span": "youths ... went on the rampage"
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
        "span": "for attempted arson"
      },
      "relation": "caused",
      "effect": {
        "span": "A 59-year-old “ barefoot doctor ” is sentenced to four months in jail"
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
        "span": "to control a mob that was pelting stones on the evening of December 20"
      },
      "relation": "caused",
      "effect": {
        "span": "the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire"
      }
    },
    {
      "cause": {
        "span": "the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire"
      },
      "relation": "caused",
      "effect": {
        "span": "Of the four persons injured in the clashes , three were wounded"
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
        "span": "as a sign of protest against renewed ' racism and Afro-phobia '"
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
        "span": "mistaking them to have caused the fatal accident"
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
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
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
        "span": "against lack of amenities"
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
        "span": "after a communal violence broke out near St Xavier 's High School in the Mirzapur area of Ahmedabad late on Sunday ."
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

### --- id=2770 ---

输入文本: The boycott of meals is to protest the political implications that we didnt do our jobs ,   one of the agitating officers said .

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
      "cause": "to protest the political implications that we didnt do our jobs",
      "effect": "The boycott of meals"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the political implications that we didnt do our jobs"
      },
      "relation": "caused",
      "effect": {
        "span": "The boycott of meals"
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
        "span": "over salary grades on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "Hundreds of members of the Police and Prisons Civil Rights Union gathered at the King Dinuzulu Gardens in Durban on Wednesday ahead of a march"
      }
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
        "span": "the police forced a bandh"
      },
      "relation": "caused",
      "effect": {
        "span": "reports came in that the police forced a bandh in Huzurabad town , 40 km from here ."
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
      "cause": "Some of the youths decided they were not satisfied with this",
      "effect": "on Wednesday morning barricaded the doors of their cells"
    }
  ],
  "pred_triples": []
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
        "span": "ended on Tuesday with eight dead and nine wounded"
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

### --- id=211 ---

输入文本: Addressing a congregation at Gokulnagar , Nandigram , Trinamool Congress chief Mamata Banerjee said the people would give a fitting reply to the Communist Party of India (Marxist)-led government for the “ carnage . ” “ Violence continues ” Condemning the “ atrocities committed by CPI(M) cadres on the innocent people of Nandigram , ” Ms. Banerjee said even after a year “ those responsible had not been punished .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the “ atrocities committed by CPI(M) cadres on the innocent people of Nandigram , ”"
      },
      "relation": "caused",
      "effect": {
        "span": "Ms. Banerjee said even after a year “those responsible had not been punished ."
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
        "span": "condemned the attack on the woman MLA"
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
        "span": "About 1,000 foreign domestic helpers yesterday protested against the temporary suspension of the employers ' levy , saying it had threatened their livelihoods , and called for permanent abolition of the tax ."
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
        "span": "for nearly five hours and shouted slogans against the Union and state governments"
      },
      "relation": "caused",
      "effect": {
        "span": "Farmers on Saturday blocked the busy National Highway 7 on the outskirts of the city"
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
        "span": "two army personnel from elite Para unit who lost their lives today"
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
        "span": "Several hours after a migrant labourer from U P was allegedly beaten to death by a group of Marathi-speaking men on a suburban train headed for Mumbai"
      },
      "relation": "caused",
      "effect": {
        "span": "the Centre issued a stern advisory to the Maharashtra government , asking it to act quickly to end the violence against north Indians and ensure the safety of everyone living in India 's financial capital ."
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
      "relation": "caused",
      "effect": {
        "span": "the recent protests were initially sparked"
      }
    },
    {
      "cause": {
        "span": "the recent protests"
      },
      "relation": "caused",
      "effect": {
        "span": "the demonstrations have morphed into a wider movement against her administration and Beijing ."
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

### --- id=520 ---

输入文本: Afew social organisations chipped in by holding agitations , though not with ' India Against Corruption ' ( IAC ) in front of the PMC headquarters , but in their own areas on Thursday .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "by holding agitations , though not with ' India Against Corruption ' ( IAC ) in front of the PMC headquarters , but in their own areas on Thursday ."
      },
      "relation": "caused",
      "effect": {
        "span": "Afew social organisations chipped in"
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
        "span": "that the cases were filed against the students only to discourage them from participating in separate Telangana agitations"
      },
      "relation": "caused",
      "effect": {
        "span": "Chandrasekhar Rao demanded that the cases be lifted immediately"
      }
    }
  ]
}
```

### --- id=2789 ---

输入文本: People invaded the land in Rus-ter-vaal in the previous weeks and the Emfuleni Municipality had obtained a court order to evict them .

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
      "cause": "People invaded the land in Rus-ter-vaal in the previous weeks",
      "effect": "the Emfuleni Municipality had obtained a court order to evict them"
    }
  ],
  "pred_triples": []
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

### --- id=1666 ---

输入文本: Local TV footage showed police officers armed with non-lethal weaponry in other parts of the government complex as the protesters broke in .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "as the protesters broke in"
      },
      "relation": "caused",
      "effect": {
        "span": "police officers armed with non-lethal weaponry in other parts of the government complex"
      }
    }
  ]
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
        "span": "an encounter near village Belgaon  12 km from Bairamgarh in Bijapur"
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
        "span": "Some chanted ' Give me back my right of abode ' outside the Court of Final Appeal ."
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
        "span": "while trying to disperse a group gathered on a hill near Lonmin 's platinum mine in Marikana on August 16"
      },
      "relation": "caused",
      "effect": {
        "span": "Police opened fire , killing 34 striking workers and wounding 78"
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
        "span": "The miscreants , who were earlier with the CPM and have recently joined the TMC ,"
      },
      "relation": "caused",
      "effect": {
        "span": "are responsible for the violence"
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
      "relation": "caused",
      "effect": {
        "span": "Twelve students arrested"
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
        "span": "to release medical bulletins on the health of Jagan , who is fasting in the jail ."
      },
      "relation": "caused",
      "effect": {
        "span": "YSRC leaders Shoba Nagireddy , Praveen Kumar Reddy , G Babu Rao met jails IG Sunil Kumar and represented to him"
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
        "span": "protesting farmers blocked the main access road"
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
        "span": "in a landmine blast in Malkangiri district"
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
        "span": "to protest against the proposal , which they said would cut their basic salary by up to 40 per cent ."
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
        "span": "a protest in Bekkersdal where the police had to restore public order"
      },
      "relation": "caused",
      "effect": {
        "span": "The image used in the advert was taken from a protest in Bekkersdal"
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
        "span": "reports the authorities had tried to prevent the demonstration"
      },
      "relation": "caused",
      "effect": {
        "span": "One protester said yesterday 's turnout was smaller"
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
        "span": "I was threatened that I will also meet the fate of my daughter"
      },
      "relation": "caused",
      "effect": {
        "span": "Police did not provide any protection to us ."
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
        "span": "students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus"
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
        "span": "until the state listens to us"
      },
      "relation": "caused",
      "effect": {
        "span": "we must make sure we push , we push and we push"
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
        "span": "plus minus 60 people made a noise when the president was about to speak"
      },
      "relation": "caused",
      "effect": {
        "span": "decided to walk out"
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
        "span": "to join the statewide agitation to oppose the State Government 's move to amend the APMC Act on Friday ."
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
        "span": "being involved in the murder of ANC North West official Obuti Chika"
      },
      "relation": "caused",
      "effect": {
        "span": "Two men who confessed to being involved in the murder of ANC North West official Obuti Chika were tortured by police"
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
    "tp": 1,
    "fp": 1,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 4
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
        "span": "events such as looting , attacks on foreign nationals and the torching of trucks in an ongoing labour protest"
      },
      "relation": "caused",
      "effect": {
        "span": "violence , protect infrastructure and prevent further damage to the economy"
      }
    },
    {
      "cause": {
        "span": "events such as looting , attacks on foreign nationals and the torching of trucks in an ongoing labour protest"
      },
      "relation": "caused",
      "effect": {
        "span": "further damage to the economy"
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
        "span": "the high crime rate in the country , in Alice in particular ."
      },
      "relation": "caused",
      "effect": {
        "span": "The memorandum , from the residents of Ward 10 in the Nkonkobe municipality registered resentment and disapproval"
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
        "span": "violence that erupted during a rally by Muslims in Mumbai ’ s Azad Maidan"
      },
      "relation": "caused",
      "effect": {
        "span": "This outrageous and provocative statement"
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
        "span": "to withdraw the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "the police appealed to the agitators"
      }
    }
  ]
}
```

### --- id=2601 ---

输入文本: Apart from students and teachers of Jawaharlal Nehru University , many residents too gathered here after hearing about the protest on news channels .

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
      "cause": "hearing about the protest on news channels",
      "effect": "Apart from students and teachers of Jawaharlal Nehru University , many residents too gathered here"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "after hearing about the protest on news channels"
      },
      "relation": "caused",
      "effect": {
        "span": "many residents too gathered here"
      }
    }
  ]
}
```

### --- id=889 ---

输入文本: The Congress leader was kidnapped and beheaded by Lashkar terrorists on the night of May 16 .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "by Lashkar terrorists on the night of May 16"
      },
      "relation": "caused",
      "effect": {
        "span": "The Congress leader was kidnapped and beheaded"
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
        "span": "when some of their colleagues got hurt during the stone-pelting"
      },
      "relation": "caused",
      "effect": {
        "span": "lost temper and rataliated"
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
        "span": "over 20,000 people rallied in Xiamen , a coastal city in Fujian province ,"
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
        "span": "the attempts made by the TRS and pro-Telangana activists to proceed and participate in ‘ Million March ' in Hyderabad on Thursday with their arrests on various routes proceeding to the capital ."
      },
      "relation": "caused",
      "effect": {
        "span": "The district police foiled the attempts"
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
        "span": "within minutes a farm house was on fire , two more house were set alight and road blocked ."
      }
    }
  ]
}
```

### --- id=2494 ---

输入文本: About a hundred Maoists blew up part of a power sub-station in Naxal-dominated Jamui district , affecting power supply in the area .

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
      "cause": "About a hundred Maoists blew up part of a power sub-station in Naxal-dominated Jamui district",
      "effect": "affecting power supply in the area"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Maoists blew up part of a power sub-station in Naxal-dominated Jamui district"
      },
      "relation": "caused",
      "effect": {
        "span": "affecting power supply in the area"
      }
    }
  ]
}
```

### --- id=1715 ---

输入文本: NGO volunteers and prostitutes , holding red umbrellas symbolising protection , shouted : ' Legalisation of sex workers , innocence of sex workers ! ' The authorities quickly stepped in and banned the petition .

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
      "cause": "NGO volunteers and prostitutes , holding red umbrellas symbolising protection , shouted : ' Legalisation of sex workers , innocence of sex workers !",
      "effect": "The authorities quickly stepped in and banned the petition"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "' Legalisation of sex workers , innocence of sex workers ! '"
      },
      "relation": "caused",
      "effect": {
        "span": "The authorities quickly stepped in and banned the petition ."
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
        "span": "the SI had used unparliamentary language when they were staging a road roko"
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
        "span": "the illegal strike"
      },
      "relation": "caused",
      "effect": {
        "span": "Three people have died and scores have been injured in violence"
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
        "span": "to protest the conspiracy to dislodge my government"
      },
      "relation": "caused",
      "effect": {
        "span": "People have been forced to come out on the streets"
      }
    },
    {
      "cause": {
        "span": "the conspiracy to dislodge my government"
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
        "span": "the strike on November 15"
      },
      "relation": "caused",
      "effect": {
        "span": "all these shops had downed shutters on first day of the strike on November 15"
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
        "span": "whose regular promotions were denied and the former two were transferred to Nashik on the same post"
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
        "span": "in separate gunfights"
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
        "span": "to protest against the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "an all-union meeting convened by the CITU resolved to organise demonstrations in front of all industrial establishments located in the city on Wednesday ."
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
        "span": "as the political and media pressure mounts"
      },
      "relation": "caused",
      "effect": {
        "span": "it becomes harder for us to exercise those options"
      }
    },
    {
      "cause": {
        "span": "The executioners of the terrorist attack on Pakistan"
      },
      "relation": "caused",
      "effect": {
        "span": "would like nothing better than for India to get trapped into an aggressive , and preferably , military response"
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
        "span": "to demand the relocation of a chemical plant ."
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
        "span": "The students said the police had taken away national flag from them"
      }
    },
    {
      "cause": {
        "span": "the police had taken away national flag from them"
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
        "span": "to demand Telangana state"
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
        "span": "the arrest of student union president Kanhaiya Kumar on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir"
      },
      "relation": "caused",
      "effect": {
        "span": "The escalating protests in the JNU"
      }
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
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "supporting Mr Zong and were demanding reassurances about the future of the venture and their jobs"
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
        "span": "the circumstances that forced the community members to stage such a protest"
      },
      "relation": "caused",
      "effect": {
        "span": "Mr. Bommai visited Savanur on Wednesday along with officials and other elected representatives and asked the Deputy Commissioner to inquire into the circumstances"
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
        "span": "had spilled over to Coverdale in Christiana where a community hall was torched"
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
        "span": "Pakistani gunmen attacked Mumbai last year"
      },
      "relation": "caused",
      "effect": {
        "span": "India had suspended the talks"
      }
    },
    {
      "cause": {
        "span": "Islamabad showed concrete action on meeting India ’ s concerns over cross-border terrorism"
      },
      "relation": "caused",
      "effect": {
        "span": "it would not be resumed"
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
        "span": "led to violent protests across the city the next day , with a group of students even storming into the university campus and demanding the dismissal of the teacher who had set the question paper ."
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
        "span": "the no-work , no-pay principle in place while they were striking"
      },
      "relation": "caused",
      "effect": {
        "span": "financial difficulties"
      }
    },
    {
      "cause": {
        "span": "financial difficulties arising from the no-work , no-pay principle in place while they were striking"
      },
      "relation": "caused",
      "effect": {
        "span": "The company had further offered a once-off hardship allowance of R2000 to help workers deal with"
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
      "cause": "TDP members were probing irregularities in wage payment under NRLEGP",
      "effect": "they were mobbed"
    }
  ],
  "pred_triples": []
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
        "span": "who have been on a protest for two years"
      },
      "relation": "caused",
      "effect": {
        "span": "The encroachers demand \" cancellation of the elections \" of the President and Prime Minister of India ."
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
        "span": "sent a strong message to various enforcement agencies in the city"
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
        "span": "On Tuesday night tens of thousands of demonstrators packed the city ’ s downtown area for a third night"
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
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
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
      "relation": "caused",
      "effect": {
        "span": "he said the protestors against the church attack were assaulted by police , youth were hunted and criminal cases were booked on them ."
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
      "cause": "Tavern Moss was stabbed and beaten to death",
      "effect": "Angered community members mobilised and marched to a suspected gang member 's house in Bardien Street"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Angered community members"
      },
      "relation": "caused",
      "effect": {
        "span": "mobilised and marched to a suspected gang member 's house in Bardien Street"
      }
    },
    {
      "cause": {
        "span": "mobilised and marched to a suspected gang member 's house in Bardien Street"
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
        "span": "Tension prevailed at NIT here"
      }
    },
    {
      "cause": {
        "span": "to resolve the crisis being witnessed since last six days"
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
        "span": "demanding that the police produce in a court of law the party 's Andhra-Orissa border special zone committee member and a central committee member Damodar alias Azad, who was reportedly taken into custody a few days ago"
      },
      "relation": "caused",
      "effect": {
        "span": "the CPI ( Maoist ) gave the call"
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
        "span": "Tohtunyaz helped them to acquire more than 10 knives"
      },
      "relation": "caused",
      "effect": {
        "span": "used in the attack ."
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
        "span": "CPI protests"
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
        "span": "The four inmates were arrested"
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
        "span": "when police tried to stop Arya Pratinidhi Sabha activists from marching towards the Ashram"
      },
      "relation": "caused",
      "effect": {
        "span": "The row over possession of Satlok Ashram , headed by Rampal , took a violent turn on Sunday"
      }
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
        "span": "demanding that four men arrested by police for pelting stones at KSRTC buses be freed"
      },
      "relation": "caused",
      "effect": {
        "span": "Hartal supporters surrounded a police station at Attakkulangara"
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
        "span": "a mob gathered near a mosque threw two crude bombs at the police"
      },
      "relation": "caused",
      "effect": {
        "span": "Trouble was also reported from Mirzapur in the city"
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
        "span": "against plan to amend APMC Act"
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
      "relation": "caused",
      "effect": {
        "span": "A DSP and four constables were killed in a landmine blast"
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
        "span": "regarding the threat call to Nehru"
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
        "span": "in connection with the serial blasts of July 26, 2008 there"
      },
      "relation": "caused",
      "effect": {
        "span": "both lodged in Sabarmati jail in Ahmedabad"
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
        "span": "how the power of the internet helped foster the massive march in 2003"
      },
      "relation": "caused",
      "effect": {
        "span": "the massive march in 2003"
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
      "cause": "demanded that the government must review Section 124 A of the Indian Penal Code ( IPC ) which deals with sedition , the law under which Sen has been sentenced",
      "effect": "Others who addressed the dharna"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "that the government must review Section 124 A of the Indian Penal Code ( IPC ) which deals with sedition"
      },
      "relation": "caused",
      "effect": {
        "span": "Others who addressed the dharna demanded"
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
        "span": "the injuries suffered by 1,680 people during clashes between the province 's Uygur Muslim minority and Han Chinese"
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
        "span": "to protest against the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "a large number of people who had blocked road near Mahabir bridge"
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
        "span": "the drastic downsizing of Nokia ’s Sriperumbudur plant"
      },
      "relation": "caused",
      "effect": {
        "span": "BYD Electronics India Private Ltd announced a VRS offer for its 1,500 employees"
      }
    }
  ]
}
```

### --- id=2509 ---

输入文本: The Left leaders pointed out that the ongoing plantation workers ’ stir affects 3.5 lakh of plantation workers across the state and hence was a serious social issue .

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
      "cause": "the ongoing plantation workers ’ stir affects 3.5 lakh of plantation workers across the state",
      "effect": "was a serious social issue"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the ongoing plantation workers ’ stir"
      },
      "relation": "caused",
      "effect": {
        "span": "affects 3.5 lakh of plantation workers across the state and hence was a serious social issue ."
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
        "span": "The journalist was manhandled"
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

### --- id=948 ---

输入文本: A civilian was also abducted along with the troopers either on suspicion of being a policeman or for interfering in the abduction , he added .

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
      "cause": "either on suspicion of being a policeman or for interfering in the abduction",
      "effect": "A civilian was also abducted along with the troopers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "on suspicion of being a policeman or for interfering in the abduction"
      },
      "relation": "caused",
      "effect": {
        "span": "A civilian was also abducted along with the troopers"
      }
    }
  ]
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
        "span": "while undertaking the day-long fast"
      },
      "relation": "caused",
      "effect": {
        "span": "The recruits , at Valluvar Kottam shouted slogans including , “ HCL lend us your ears , give us back our two years , ”"
      }
    }
  ]
}
```

### --- id=1200 ---

输入文本: Jail Superintendent Veerabhadra Swamy told presspersons that the trouble broke out after a few inmates , who were praying outside a place of worship in the jail , took serious exception to the disturbance being caused by some inmates belonging to a different faith .

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
      "cause": "a few inmates , who were praying outside a place of worship in the jail , took serious exception to the disturbance being caused by some inmates belonging to a different faith",
      "effect": "the trouble broke out"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the disturbance being caused by some inmates belonging to a different faith"
      },
      "relation": "caused",
      "effect": {
        "span": "a few inmates , who were praying outside a place of worship in the jail , took serious exception"
      }
    },
    {
      "cause": {
        "span": "a few inmates , who were praying outside a place of worship in the jail , took serious exception to the disturbance being caused by some inmates belonging to a different faith"
      },
      "relation": "caused",
      "effect": {
        "span": "the trouble broke out"
      }
    }
  ]
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
        "span": "in a gunfight with security forces in Assam Saturday"
      },
      "relation": "caused",
      "effect": {
        "span": "A top separatist bomber and close associate of Paresh Baruah , commander-in-chief of the outlawed United Liberation Front of Asom ( ULFA ) , was killed"
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
        "span": "left commuters stranded in Johannesburg"
      }
    },
    {
      "cause": {
        "span": "The taxi strike"
      },
      "relation": "caused",
      "effect": {
        "span": "was expected to also disrupt matric pupils writing exams on Monday"
      }
    }
  ]
}
```

### --- id=702 ---

输入文本: It was on July 4 that seven persons of the Popular Front of India intercepted the car of colege lecturer Joseph , who was then working at Newman College and chopped off his palm .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "intercepted the car of colege lecturer Joseph , who was then working at Newman College and chopped off his palm"
      },
      "relation": "caused",
      "effect": {
        "span": "seven persons of the Popular Front of India"
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
    "tp": 1,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 3
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
        "span": "the massive turnout at the ‘ Parivartan ’ rally"
      },
      "relation": "caused",
      "effect": {
        "span": "Congress leaders on Thursday gave a clarion call to party workers and supporters to dethrone Naveen Patnaik Government in the 2014 general elections ."
      }
    }
  ]
}
```

### --- id=1740 ---

输入文本: About 1,000 angry protesters gathered outside the Alice Magistrates Court on Thursday where four suspects appeared on charges of murdering a Victoria Hospital tutor last year .

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
        "span": "on charges of murdering a Victoria Hospital tutor last year"
      },
      "relation": "caused",
      "effect": {
        "span": "four suspects appeared"
      }
    },
    {
      "cause": {
        "span": "on charges of murdering a Victoria Hospital tutor last year"
      },
      "relation": "caused",
      "effect": {
        "span": "About 1,000 angry protesters gathered outside the Alice Magistrates Court on Thursday"
      }
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
      "relation": "caused",
      "effect": {
        "span": "we also have plans to organise talks with the public and also with those who hold protests against plywood factories"
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
        "span": "demanding shifting of proposed AIIMS in Assam from Changsari to Raha"
      },
      "relation": "caused",
      "effect": {
        "span": "clashes between police and protesters"
      }
    },
    {
      "cause": {
        "span": "clashes between police and protesters"
      },
      "relation": "caused",
      "effect": {
        "span": "one person identified as Mintu Deori was killed during a protest while 20 others , including two Additional SPs , were injured"
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
        "span": "following rasta roko by students"
      },
      "relation": "caused",
      "effect": {
        "span": "Traffic was held up for an hour"
      }
    }
  ]
}
```

### --- id=1736 ---

输入文本: As many as 217 members of 52 families were forcibly thrown out of their village in June , 2007 by a group of people led by Posco Pratirodha Sangram Samiti ( PPSS ) president Abhaya Sahu .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "by a group of people led by Posco Pratirodha Sangram Samiti ( PPSS ) president Abhaya Sahu"
      },
      "relation": "caused",
      "effect": {
        "span": "As many as 217 members of 52 families were forcibly thrown out of their village in June , 2007"
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
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "following Wednesday 's mass gathering against the abuse and violence directed at women and children outside the meeting venue of the World Economic Forum in Cape Town"
      },
      "relation": "caused",
      "effect": {
        "span": "South Africa President Cyril Ramaphosa on Thursday addressed thousands of protesters outside Parliament"
      }
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
