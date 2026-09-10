# qwen3-8b-base CNC SFT held-out test eval report

## 配置
```json
{
  "label": "qwen3-8b-base CNC SFT held-out test",
  "model": "qwen3-8b-base",
  "dataset": "cnc_sft_test",
  "sample_count": 50,
  "prompt_name": "cnc_sft_v1",
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
================ qwen3-8b-base CNC SFT held-out test final report ================
样本总数: 50
  Gold 含因果: 27 | Pred 含因果: 33
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.720
  Precision: 0.697
  Recall   : 0.852
  F1       : 0.767
  (TP=23, TN=13, FP=10, FN=4)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 50
    Gold triples: 41 | Pred triples: 35
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=35, FN=41)
  [anchor_window]
    样本数: 50
    Gold triples: 41 | Pred triples: 35
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=35, FN=41)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 23
    Gold triples: 36 | Pred triples: 23
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=23, FN=36)
  [anchor_window]
    样本数: 23
    Gold triples: 36 | Pred triples: 23
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=23, FN=36)
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

Sample details shown: all 37 wrong samples from 50 total samples.

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
      "cause.span": "Protesters have also surrounded the police headquarters twice in past weeks",
      "relation": "caused",
      "effect.span": "noisy and emotionally charged protests"
    },
    {
      "cause.span": "young people spray-painted obscenities on its front wall and barricaded its entrances",
      "relation": "caused",
      "effect.span": "noisy and emotionally charged protests"
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
      "cause": "we had gone over a month without teachers",
      "effect": "On Tuesday we went to picket at the Western Cape Provincial Legislature"
    }
  ],
  "pred_triples": [
    {
      "cause.span": "we had gone over a month without teachers",
      "relation": "caused",
      "effect.span": "we went to picket at the Western Cape Provincial Legislature"
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
      "cause.span": "Delay",
      "relation": "caused",
      "effect.span": "ryots lay siege to MRO office"
    },
    {
      "cause.span": "Delay",
      "relation": "caused",
      "effect.span": "Betel nut farmers from Garikaparru and Thotlavalluru villages under Thotlavalluru mandal laid siege to the Mandal Revenue Office on Monday"
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
      "cause.span": "VAT imposed by the government is unjust",
      "relation": "caused",
      "effect.span": "the business has to run if we are to recover losses"
    }
  ]
}
```

### --- id=1420 ---

输入文本: The protest went on for more than two hours and shops on the highway were shut during that time .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause.span": "The protest went on for more than two hours",
      "relation": "caused",
      "effect.span": "shops on the highway were shut during that time"
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
      "cause.span": "officials have frozen that money",
      "relation": "caused",
      "effect.span": "villagers funding a journey to Beijing to continue their petitioning"
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
      "cause.span": "orchestrating the violence against Dalits in three villages in Dharmapuri",
      "relation": "caused",
      "effect.span": "violence against Dalits in three villages in Dharmapuri"
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
      "cause.span": "he expressed support for the police 's handling of a protest in Mong Kok at which rival groups clashed over a teacher 's verbal attack on officers",
      "relation": "caused",
      "effect.span": "he caused uproar in some quarters"
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
      "cause.span": "parked them on the main thoroughfare",
      "relation": "caused",
      "effect.span": "putting the public to great inconvenience"
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
      "cause.span": "Some protesters attacked me when I was clicking pictures",
      "relation": "caused",
      "effect.span": "their colleagues dissuaded them"
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
      "cause.span": "she explained her views",
      "relation": "caused",
      "effect.span": "backed her"
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
      "cause.span": "called by Telangana Joint Action Committee ( JAC )",
      "effect.span": "Police arrested leaders of various political parties who squatted on the highway"
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
      "cause.span": "was killed in the Maoist ambush in Koraput district yesterday",
      "relation": "caused",
      "effect.span": "were consigned to flames today at his village in Sarilo under Kujang police limits"
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

### --- id=464 ---

输入文本: Passengers stranded as buses go off road

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
      "cause": "buses go off road",
      "effect": "Passengers stranded"
    }
  ],
  "pred_triples": [
    {
      "cause.span": "Passengers stranded",
      "effect.span": "buses go off road"
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
      "cause.span": "the Devarkadra agriculture extension officer had poured kerosene over herself and lit the match",
      "relation": "caused",
      "effect.span": "the Devarkadra agriculture extension officer had poured kerosene over herself and lit the match"
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
      "cause.span": "security forces shot four militants who allegedly attempted to blow up a Communist party building in southern Xinjiang",
      "relation": "caused",
      "effect.span": "That apparent calm was shattered in late December"
    }
  ]
}
```

### --- id=1129 ---

输入文本: 2010 : ‘ Track record ’ in trouble for Railways 21st June 2011 02:31 AM CHENNAI : A failed attempt to sabotage express trains by placing fishplates on the track in Virudhunagar district on Monday morning is probably the first major case to be reported this year .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause.span": "A failed attempt to sabotage express trains by placing fishplates on the track in Virudhunagar district on Monday morning",
      "relation": "caused",
      "effect.span": "is probably the first major case to be reported this year"
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
      "cause.span": "placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district",
      "relation": "caused",
      "effect.span": "mass destruction to the train and passengers"
    }
  ]
}
```

### --- id=1796 ---

输入文本: Govt Readies to Wield the Stick as Striking Doctors Decide to Harden Their Stand

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
      "cause": "Striking Doctors Decide to Harden Their Stand",
      "effect": "Govt Readies to Wield the Stick"
    }
  ],
  "pred_triples": [
    {
      "cause.span": "Striking Doctors",
      "relation": "caused",
      "effect.span": "Harden Their Stand"
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
      "cause.span": "an argument between Prasad and S.C. Tyagi , a deputy director at the Department of Social Welfare",
      "relation": "caused",
      "effect.span": "his suspension and the hunger strike"
    }
  ]
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
      "cause.span": "planning , financing and facilitating the Mumbai attack",
      "relation": "caused",
      "effect.span": "arrested"
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
      "cause.span": "In July , ANC councillor Wandile Mkhize was shot dead in a drive-by shooting near his home in Manaba , Margate .",
      "relation": "caused",
      "effect.span": "was shot dead"
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
      "cause.span": "violence by vigilante groups",
      "relation": "caused",
      "effect.span": "growing violence against Muslims"
    }
  ]
}
```

### --- id=1669 ---

输入文本: Lam called a rare press conference early on Tuesday to condemn the “ extremely violent ” storming of the legislature , which she described as “ heartbreaking and shocking ” .

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
      "cause": "to condemn the “ extremely violent ” storming of the legislature",
      "effect": "Lam called a rare press conference early on Tuesday"
    }
  ],
  "pred_triples": []
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
      "cause.span": "NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections",
      "relation": "caused",
      "effect.span": "The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram"
    }
  ]
}
```

### --- id=1872 ---

输入文本: Fearing they would not get the forms , the mob turned violent and pelted stones at SDA property and vehicles parked outside .

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
      "cause": "Fearing they would not get the forms",
      "effect": "the mob turned violent and pelted stones at SDA property and vehicles parked outside"
    }
  ],
  "pred_triples": [
    {
      "cause.span": "Fearing they would not get the forms",
      "relation": "caused",
      "effect.span": "the mob turned violent and pelted stones at SDA property and vehicles parked outside"
    }
  ]
}
```

### --- id=1931 ---

输入文本: Five members of the old group entered the church during the Sunday mass yesterday and assaulted Akilan injuring him .

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
      "cause": "assaulted Akilan",
      "effect": "injuring him"
    }
  ],
  "pred_triples": [
    {
      "cause.span": "assaulted Akilan",
      "relation": "caused",
      "effect.span": "injuring him"
    }
  ]
}
```

### --- id=2035 ---

输入文本: Anantapur : Accused ‘ paraded ' half-naked by CI September 17 , 2010 00:00 IST Eight members of handloom weavers ' community including local councillor Pola Venkatanarayana were paraded half-naked by Circle Inspector Venugopala Reddy for allegedly beating up and threatening one B. Ramana , member of the local weavers enforcement committee .

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
      "cause": "allegedly beating up and threatening one B. Ramana , member of the local weavers enforcement committee",
      "effect": "Eight members of handloom weavers ' community including local councillor Pola Venkatanarayana were paraded half-naked by Circle Inspector Venugopala Reddy"
    }
  ],
  "pred_triples": [
    {
      "cause.span": "Eight members of handloom weavers ' community including local councillor Pola Venkatanarayana",
      "relation": "caused",
      "effect.span": "were paraded half-naked by Circle Inspector Venugopala Reddy"
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
      "cause.span": "carrying out the attack",
      "relation": "caused",
      "effect.span": "escape in dense forests"
    }
  ]
}
```

### --- id=229 ---

输入文本: Violence first broke out in the hill district on September 26 when three auto-rickshaw drivers , all belonging to the Dimasa tribe , were killed .

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
      "cause": "three auto-rickshaw drivers , all belonging to the Dimasa tribe , were killed",
      "effect": "Violence first broke out in the hill district on September 26"
    }
  ],
  "pred_triples": [
    {
      "cause.span": "Violence first broke out in the hill district on September 26 when three auto-rickshaw drivers , all belonging to the Dimasa tribe , were killed",
      "relation": "caused",
      "effect.span": "three auto-rickshaw drivers , all belonging to the Dimasa tribe , were killed"
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
      "cause.span": "have charged the protesters with pelting them with stones",
      "relation": "caused",
      "effect.span": "they approached with a proposal to accept their demands"
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
      "cause.span": "had attracted more than 5,000",
      "relation": "caused",
      "effect.span": "reached the city centre at lunch time"
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
      "cause": "against the government 's inability in stopping construction of projects by the neighbouring States",
      "effect": "TDP MLAs led by the party president N. Chandrababu Naidu staged a protest at Gun Park in front of the Assembly"
    }
  ],
  "pred_triples": [
    {
      "cause.span": "government 's inability in stopping construction of projects by the neighbouring States",
      "relation": "caused",
      "effect.span": "staged a protest at Gun Park in front of the Assembly"
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
      "cause.span": "during the violence",
      "relation": "caused",
      "effect.span": "was burnt beyond recognition while 100 others were injured"
    }
  ]
}
```
