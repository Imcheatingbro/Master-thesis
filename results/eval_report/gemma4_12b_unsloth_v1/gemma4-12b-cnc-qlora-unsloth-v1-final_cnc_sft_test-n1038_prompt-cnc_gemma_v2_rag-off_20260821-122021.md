# gemma4-12b-cnc-qlora-unsloth-v1-final CNC SFT test eval report

> **实验口径说明：** 本报告是一次直接生成的 raw 结果，但该 test 输出随后被用于诊断和决定后续修改，因此不再属于未触碰的最终 held-out 评估；保留作探索性 raw baseline，不用于修改后的模型选择或调参。

## 配置
```json
{
  "label": "gemma4-12b-cnc-qlora-unsloth-v1-final CNC SFT test",
  "model": "gemma4-12b-cnc-qlora-unsloth-v1-final",
  "dataset": "cnc_sft_test",
  "sample_count": 1038,
  "prompt_name": "cnc_gemma_v2",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 0,
  "temperature": 0.0,
  "max_tokens": 512,
  "progress_every": 100,
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
================ gemma4-12b-cnc-qlora-unsloth-v1-final CNC SFT test final report ================
样本总数: 1038
  Gold 含因果: 548 | Pred 含因果: 39
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.504
  Precision: 0.923
  Recall   : 0.066
  F1       : 0.123
  (TP=36, TN=487, FP=3, FN=512)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 1038
    Gold triples: 763 | Pred triples: 39
    Precision: 0.872
    Recall   : 0.045
    F1       : 0.085
    (TP=34, FP=5, FN=729)
  [anchor_window]
    样本数: 1038
    Gold triples: 763 | Pred triples: 39
    Precision: 0.846
    Recall   : 0.043
    F1       : 0.082
    (TP=33, FP=6, FN=730)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 36
    Gold triples: 45 | Pred triples: 36
    Precision: 0.944
    Recall   : 0.756
    F1       : 0.840
    (TP=34, FP=2, FN=11)
  [anchor_window]
    样本数: 36
    Gold triples: 45 | Pred triples: 36
    Precision: 0.917
    Recall   : 0.733
    F1       : 0.815
    (TP=33, FP=3, FN=12)
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

Sample details shown: first 200 of 525 wrong samples from 1038 total samples.

### --- id=2124 ---

输入文本: On Tuesday we went to picket at the Western Cape Provincial Legislature after we had gone over a month without teachers .

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
      "cause": "we had gone over a month without teachers",
      "effect": "On Tuesday we went to picket at the Western Cape Provincial Legislature"
    }
  ],
  "pred_triples": []
}
```

### --- id=542 ---

输入文本: We totally support the ongoing strike since VAT imposed by the government is unjust but the business has to run if we are to recover losses , ” said a shop owner near Charminar .

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
      "cause": "VAT imposed by the government is unjust",
      "effect": "We totally support the ongoing strike"
    },
    {
      "cause": "if we are to recover losses",
      "effect": "the business has to run"
    }
  ],
  "pred_triples": []
}
```

### --- id=1368 ---

输入文本: According to one villager , officials have frozen that money to prevent villagers funding a journey to Beijing to continue their petitioning .

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
      "cause": "to prevent villagers funding a journey to Beijing to continue their petitioning",
      "effect": "officials have frozen that money"
    },
    {
      "cause": "to continue their petitioning",
      "effect": "villagers funding a journey to Beijing"
    }
  ],
  "pred_triples": []
}
```

### --- id=2070 ---

输入文本: 17th November 2012 11:20 AM Squarely blaming the Pattali Makkal Katchi ( PMK ) for orchestrating the violence against Dalits in three villages in Dharmapuri , VCK leader Thol Thirumavalavan on Friday demanded a CBI investigation into the matter and action against those openly instigating caste violence on public platforms .

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
      "cause": "orchestrating the violence against Dalits in three villages in Dharmapuri",
      "effect": "Squarely blaming the Pattali Makkal Katchi ( PMK )"
    },
    {
      "cause": "Squarely blaming the Pattali Makkal Katchi ( PMK ) for orchestrating the violence against Dalits in three villages in Dharmapuri",
      "effect": "VCK leader Thol Thirumavalavan on Friday demanded a CBI investigation into the matter and action against those openly instigating caste violence on public platforms"
    }
  ],
  "pred_triples": []
}
```

### --- id=688 ---

输入文本: Leung Chun-ying 's second meet-the-public session , in Kwun Tong , was a much quieter affair than his first one last week , when he caused uproar in some quarters by expressing support for the police 's handling of a protest in Mong Kok at which rival groups clashed over a teacher 's verbal attack on officers .

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
  "pred_triples": []
}
```

### --- id=1338 ---

输入文本: Meanwhile , protesting against the attack , RTC staff observed a bandh ; no RTC bus in the district plied today as they parked them on the main thoroughfare , putting the public to great inconvenience .

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
  "pred_triples": []
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
      "cause": "she explained her views",
      "effect": "Law ’ s parents , who initially opposed her protesting , backed her"
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
  "pred_triples": []
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
      "cause": "buses go off road",
      "effect": "Passengers stranded"
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

### --- id=2085 ---

输入文本: That apparent calm was shattered in late December , when security forces shot four militants who allegedly attempted to blow up a Communist party building in southern Xinjiang .

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
      "cause": "security forces shot four militants who allegedly attempted to blow up a Communist party building in southern Xinjiang",
      "effect": "That apparent calm was shattered in late December"
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
      "cause": "the National Security Act in December",
      "effect": "two persons , who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district with an intention of causing mass destruction to the train and passengers , were detained"
    },
    {
      "cause": "an intention of causing mass destruction to the train and passengers",
      "effect": "two persons , who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district"
    }
  ],
  "pred_triples": []
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

### --- id=2153 ---

输入文本: According to Singh , his suspension and the hunger strike were the result of an argument between Prasad and S.C. Tyagi , a deputy director at the Department of Social Welfare .

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
      "cause": "an argument between Prasad and S.C. Tyagi , a deputy director at the Department of Social Welfare",
      "effect": "his suspension and the hunger strike"
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
      "cause": "NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections",
      "effect": "The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram"
    },
    {
      "cause": "it did not want Achuthanandan to come back to power for another term",
      "effect": "NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections"
    }
  ],
  "pred_triples": []
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

### --- id=2035 ---

输入文本: Anantapur : Accused ‘ paraded ' half-naked by CI September 17 , 2010 00:00 IST Eight members of handloom weavers ' community including local councillor Pola Venkatanarayana were paraded half-naked by Circle Inspector Venugopala Reddy for allegedly beating up and threatening one B. Ramana , member of the local weavers enforcement committee .

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
      "cause": "allegedly beating up and threatening one B. Ramana , member of the local weavers enforcement committee",
      "effect": "Eight members of handloom weavers ' community including local councillor Pola Venkatanarayana were paraded half-naked by Circle Inspector Venugopala Reddy"
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
      "cause": "who managed to escape in dense forests after carrying out the attack",
      "effect": "The Army and police have now launched extensive combing operations in the area to flush out the terrorists"
    },
    {
      "cause": "to flush out the terrorists who managed to escape in dense forests after carrying out the attack",
      "effect": "The Army and police have now launched extensive combing operations in the area"
    }
  ],
  "pred_triples": []
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
      "cause": "pelting them with stones when they approached with a proposal to accept their demands",
      "effect": "brick kiln owners have charged the protesters"
    }
  ],
  "pred_triples": []
}
```

### --- id=1057 ---

输入文本: TDP MLAs led by the party president N. Chandrababu Naidu staged a protest at Gun Park in front of the Assembly against the government 's inability in stopping construction of projects by the neighbouring States .

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
      "cause": "against the government 's inability in stopping construction of projects by the neighbouring States",
      "effect": "TDP MLAs led by the party president N. Chandrababu Naidu staged a protest at Gun Park in front of the Assembly"
    }
  ],
  "pred_triples": []
}
```

### --- id=1313 ---

输入文本: Four-time MP Yadav was arrested in 1999 and convicted for the murder and sentenced to life imprisonment Feb 14 , 2008 .

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
      "cause": "the murder",
      "effect": "Four-time MP Yadav was arrested in 1999 and convicted"
    },
    {
      "cause": "the murder",
      "effect": "and sentenced to life imprisonment Feb 14 , 2008"
    }
  ],
  "pred_triples": []
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

### --- id=2900 ---

输入文本: However , the absence of senior Trinamool Congress leaders during the agitation prompted opposition parties to raise fingers at " TMC 's internal feud that led to the incident " .

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
      "cause": "the absence of senior Trinamool Congress leaders during the agitation",
      "effect": "opposition parties to raise fingers at \" TMC 's internal feud that led to the incident \""
    },
    {
      "cause": "TMC 's internal feud",
      "effect": "the incident"
    }
  ],
  "pred_triples": []
}
```

### --- id=713 ---

输入文本: - Indian Express Agencies , Agencies : Bangalore , Fri Jul 27 2012 , 15:59 hrs Karnataka Assembly today witnessed a brief dharna by the entire opposition members protesting the government move to pass the Finance Bill without tabling the annual and performance reports of various departments .

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
      "cause": "protesting the government move to pass the Finance Bill without tabling the annual and performance reports of various departments",
      "effect": "Karnataka Assembly today witnessed a brief dharna by the entire opposition members"
    }
  ],
  "pred_triples": []
}
```

### --- id=1971 ---

输入文本: In retaliation , the police fired a few rounds in the air which finally capped the clashes .

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
      "cause": "retaliation",
      "effect": "the police fired a few rounds in the air"
    },
    {
      "cause": "the police fired a few rounds in the air",
      "effect": "which finally capped the clashes"
    }
  ],
  "pred_triples": []
}
```

### --- id=1302 ---

输入文本: Protests were held over the weekend as displaced families and relatives of missing firefighters demanded compensation and answers about the whereabouts of their loved ones .

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
      "cause": "displaced families and relatives of missing firefighters demanded compensation and answers about the whereabouts of their loved ones",
      "effect": "Protests were held over the weekend"
    }
  ],
  "pred_triples": []
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
      "cause": "fear and economic inducements",
      "effect": "they turned away from politics"
    }
  ],
  "pred_triples": []
}
```

### --- id=395 ---

输入文本: 12 held after group clashes in Surat - Indian Express Express News Service , Express News Service : Surat , Tue Sep 04 2012 , 06:45 hrs The police have arrested 12 people in connection with the clashes that broke out between the members of Patel and Bharwad communities in Punagam area of the city on Sunday .

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
      "cause": "the clashes that broke out between the members of Patel and Bharwad communities in Punagam area of the city on Sunday",
      "effect": "The police have arrested 12 people"
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
      "cause": "the Joint Action Committee ( JAC ) of VMC Employees bent upon continuing ‘ Work to Rule ’",
      "effect": "The stalemate over payment of salaries to municipal workers continued on Saturday"
    }
  ],
  "pred_triples": []
}
```

### --- id=2101 ---

输入文本: LeT , Hamas use violence for political objectives

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
      "cause": "political objectives",
      "effect": "LeT , Hamas use violence"
    }
  ],
  "pred_triples": []
}
```

### --- id=2167 ---

输入文本: " These cases were registered against them only to restrain them from taking part in the agitation .

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
      "cause": "only to restrain them from taking part in the agitation",
      "effect": "These cases were registered against them"
    }
  ],
  "pred_triples": []
}
```

### --- id=2377 ---

输入文本: The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday to condemn what it called a “ concerted attack on Hindu leaders in the state . ” Ramesh , the state BJP unit ’ s general secretary and a charted accountant by profession , was murdered by assailants in Salem while he was on his way back home after visiting the party office on Friday evening .

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
      "cause": "to condemn what it called a “ concerted attack on Hindu leaders in the state",
      "effect": "The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday"
    },
    {
      "cause": "visiting the party office on Friday evening",
      "effect": "he was on his way back home"
    }
  ],
  "pred_triples": []
}
```

### --- id=241 ---

输入文本: Fri 27 Fire Walking A 59 - year-old “ barefoot doctor ” is sentenced to four months in jail for attempted arson .

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
      "cause": "attempted arson",
      "effect": "Fri 27 Fire Walking A 59 - year-old “ barefoot doctor ” is sentenced to four months in jail"
    }
  ],
  "pred_triples": []
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
      "cause": "the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire to control a mob that was pelting stones on the evening of December 20",
      "effect": "three were wounded"
    },
    {
      "cause": "to control a mob that was pelting stones on the evening of December 20",
      "effect": "the security personnel guarding the house of political activist Abdul Rehman Kawoosa in Sumbal allegedly opened fire"
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
      "cause": "diplomats from 42 African nations boycotted the weeklong celebration of Africa Day , hosted by the Indian government as a sign of protest against renewed ' racism and Afro-phobia '",
      "effect": "It is shameful that the government takes this issue so lightly"
    },
    {
      "cause": "protest against renewed ' racism and Afro-phobia '",
      "effect": "diplomats from 42 African nations boycotted the weeklong celebration of Africa Day , hosted by the Indian government"
    }
  ],
  "pred_triples": []
}
```

### --- id=945 ---

输入文本: But with the agitation in full swing and disturbances on the campus , they were further postponed .

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
      "cause": "But with the agitation in full swing and disturbances on the campus",
      "effect": "they were further postponed"
    }
  ],
  "pred_triples": []
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
      "cause": "they clashed with campus security on Wednesday",
      "effect": "Several students at the Mafikeng Campus of the North West University were injured"
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
      "cause": "against the Cabinet 's nod for draft bill for bifurcation of the state",
      "effect": "The two-day bandh call given by the pro-United Andhra Pradesh groups"
    },
    {
      "cause": "The two-day bandh call given by the pro-United Andhra Pradesh groups against the Cabinet 's nod for draft bill for bifurcation of the state",
      "effect": "a mixed response in the coastal Andhra and Rayalaseema regions on the second day today"
    }
  ],
  "pred_triples": []
}
```

### --- id=31 ---

输入文本: Two more youths were arrested later for allegedly being involved in the blast .

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
      "cause": "allegedly being involved in the blast",
      "effect": "Two more youths were arrested later"
    }
  ],
  "pred_triples": []
}
```

### --- id=2870 ---

输入文本: ( With additional reporting from K. Raju in Dindigul ) Relatives of Shankar and locals staged a road blockade for almost four hours , demanding compensation and a government job for Kausalya .

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
      "cause": "demanding compensation and a government job for Kausalya",
      "effect": "Relatives of Shankar and locals staged a road blockade for almost four hours"
    }
  ],
  "pred_triples": []
}
```

### --- id=2529 ---

输入文本: The Tanzanian woman was reportedly dragged out of the car in which she was seated along with her three friends when she reached the accident spot with the miscreants mistaking them to have caused the fatal accident though a Sudanese was involved in it , police said .

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
      "cause": "she reached the accident spot with the miscreants mistaking them to have caused the fatal accident",
      "effect": "The Tanzanian woman was reportedly dragged out of the car in which she was seated along with her three friends"
    },
    {
      "cause": "a Sudanese was involved in it",
      "effect": "the miscreants mistaking them to have caused the fatal accident"
    }
  ],
  "pred_triples": []
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

### --- id=2256 ---

输入文本: ' Lately , much of the publicity has focused too much on anti-separatism and less on unity . ' Beijing has been under pressure over its crackdown on Tibetan protesters involved in rioting last year .

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
      "cause": "its crackdown on Tibetan protesters involved in rioting last year",
      "effect": "Beijing has been under pressure"
    }
  ],
  "pred_triples": []
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

### --- id=2328 ---

输入文本: Police use tear gas to control communal clash at Mirzapur - Indian Express Express News Service , Express News Service : Ahmedabad , Tue Sep 15 2009 , 01:09 hrs The city police had to resort to tear gas shelling after a communal violence broke out near St Xavier 's High School in the Mirzapur area of Ahmedabad late on Sunday .

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
      "cause": "to control communal clash at Mirzapur",
      "effect": "Police use tear gas"
    },
    {
      "cause": "a communal violence broke out near St Xavier 's High School in the Mirzapur area of Ahmedabad late on Sunday",
      "effect": "The city police had to resort to tear gas shelling"
    }
  ],
  "pred_triples": []
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
      "cause": "to protest the political implications that we didnt do our jobs",
      "effect": "The boycott of meals"
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
      "cause": "a march over salary grades on Wednesday",
      "effect": "Hundreds of members of the Police and Prisons Civil Rights Union gathered at the King Dinuzulu Gardens in Durban on Wednesday"
    },
    {
      "cause": "salary grades",
      "effect": "a march"
    }
  ],
  "pred_triples": []
}
```

### --- id=977 ---

输入文本: The labour minister 's announcement followed countrywide public hearings on a new minimum wage for the agriculture sector , which were prompted by violent protests in parts of the Western Cape .

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
      "cause": "countrywide public hearings on a new minimum wage for the agriculture sector",
      "effect": "The labour minister 's announcement"
    },
    {
      "cause": "violent protests in parts of the Western Cape",
      "effect": "countrywide public hearings on a new minimum wage for the agriculture sector"
    }
  ],
  "pred_triples": []
}
```

### --- id=1893 ---

输入文本: The Left , the BJP and a few other parties have been disrupting Parliament proceedings for the past two days over the alleged involvement of the Maoists in organising Trinamool Congress rally at Lalgarh in West Bengal .

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
      "cause": "the alleged involvement of the Maoists in organising Trinamool Congress rally at Lalgarh in West Bengal",
      "effect": "The Left , the BJP and a few other parties have been disrupting Parliament proceedings for the past two days"
    }
  ],
  "pred_triples": []
}
```

### --- id=2739 ---

输入文本: Khan 's boycott will be largely symbolic because he is seen as a ceremonial head .

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
      "cause": "he is seen as a ceremonial head",
      "effect": "Khan 's boycott will be largely symbolic"
    }
  ],
  "pred_triples": []
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

### --- id=2350 ---

输入文本: Bangalore courts to remain shut today 03rd March 2012 08:32 AM Police personnels control the situation after a clash between the lawyers and media in the Civil court premises in Bangalore on Friday .

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
      "cause": "a clash between the lawyers and media in the Civil court premises in Bangalore on Friday",
      "effect": "Police personnels control the situation"
    }
  ],
  "pred_triples": []
}
```

### --- id=2986 ---

输入文本: Three Armymen , including a Subedar and two jawans , were injured when the villagers threw stones , sources said .

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
      "cause": "the villagers threw stones",
      "effect": "Three Armymen , including a Subedar and two jawans , were injured"
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

### --- id=867 ---

输入文本: There was also largescale displacement in Kandhamal district during and after the 2008 riots following the killing of Swami Lakshmanananda Saraswati .

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
      "cause": "the killing of Swami Lakshmanananda Saraswati",
      "effect": "There was also largescale displacement in Kandhamal district during and after the 2008 riots"
    }
  ],
  "pred_triples": []
}
```

### --- id=973 ---

输入文本: DUT was closed last week after about 300 students clashed with police and campus security personnel in running battles on the institution 's Steve Biko campus in Durban .

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
      "cause": "about 300 students clashed with police and campus security personnel in running battles on the institution 's Steve Biko campus in Durban",
      "effect": "DUT was closed last week"
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
  "pred_triples": []
}
```

### --- id=1003 ---

输入文本: According to the SABC , when Mbeki took the podium at the Harry Gwala Stadium , a section of the crowd started howling and leaving the stadium .

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
      "cause": "Mbeki took the podium at the Harry Gwala Stadium",
      "effect": "a section of the crowd started howling and leaving the stadium"
    }
  ],
  "pred_triples": []
}
```

### --- id=935 ---

输入文本: They were caned mercilessly and shooed out of the venue when some of them raised slogans against Chief Minister YS Rajasekhara Reddy who inaugurated the two-day job mela organised by the Greater Hyderabad Municipal Corporation ( GHMC ) .

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
      "cause": "some of them raised slogans against Chief Minister YS Rajasekhara Reddy",
      "effect": "They were caned mercilessly and shooed out of the venue"
    }
  ],
  "pred_triples": []
}
```

### --- id=2097 ---

输入文本: Maids protest over suspension of levy PUBLISHED : Monday , 28 July , 2008 , 12:00am About 1,000 foreign domestic helpers yesterday protested against the temporary suspension of the employers ' levy , saying it had threatened their livelihoods , and called for permanent abolition of the tax .

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
  "pred_triples": []
}
```

### --- id=2879 ---

输入文本: " It is due to such people ( those who unfurled the Vidarbha flag ) that the country 's integrity is damaged .

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
      "cause": "such people ( those who unfurled the Vidarbha flag )",
      "effect": "that the country 's integrity is damaged"
    }
  ],
  "pred_triples": []
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
      "cause": "against the Union and state governments",
      "effect": "Farmers on Saturday blocked the busy National Highway 7 on the outskirts of the city for nearly five hours and shouted slogans"
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
      "cause": "asking it to act quickly",
      "effect": "the Centre issued a stern advisory to the Maharashtra government"
    },
    {
      "cause": "to end the violence against north Indians and ensure the safety of everyone living in India 's financial capital",
      "effect": "asking it to act quickly"
    }
  ],
  "pred_triples": []
}
```

### --- id=1673 ---

输入文本: While the recent protests were initially sparked by Lam ’ s attempts to pass the proposed extradition legislation , the demonstrations have morphed into a wider movement against her administration and Beijing .

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
      "cause": "Lam ’ s attempts to pass the proposed extradition legislation",
      "effect": "the recent protests"
    },
    {
      "cause": "against her administration and Beijing",
      "effect": "a wider movement"
    }
  ],
  "pred_triples": []
}
```

### --- id=1275 ---

输入文本: 31st December 2014 06:04 AM MADURAI : Tension continued in Keelakuilkudi near here for the third day on Tuesday when Arunthathiyar community men refused to perform funeral rituals for a Caste Hindu family to protest denial of worship rights in the village temple .

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
      "cause": "Arunthathiyar community men refused to perform funeral rituals for a Caste Hindu family",
      "effect": "Tension continued in Keelakuilkudi near here for the third day on Tuesday"
    },
    {
      "cause": "to protest denial of worship rights in the village temple",
      "effect": "Arunthathiyar community men refused to perform funeral rituals for a Caste Hindu family"
    }
  ],
  "pred_triples": []
}
```

### --- id=2166 ---

输入文本: Alleging that the cases were filed against the students only to discourage them from participating in separate Telangana agitations , Chandrasekhar Rao demanded that the cases be lifted immediately .

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
      "cause": "discourage them from participating in separate Telangana agitations",
      "effect": "the cases were filed against the students"
    },
    {
      "cause": "the cases were filed against the students only to discourage them from participating in separate Telangana agitations",
      "effect": "Chandrasekhar Rao demanded that the cases be lifted immediately"
    }
  ],
  "pred_triples": []
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

### --- id=2969 ---

输入文本: Meanwhile , security forces and Naxalites had an encounter near village Belgaon  12 km from Bairamgarh in Bijapurkilling a Maoist rebel on the spot .

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
      "cause": "security forces and Naxalites had an encounter near village Belgaon  12 km from Bairamgarh in Bijapur",
      "effect": "killing a Maoist rebel on the spot"
    }
  ],
  "pred_triples": []
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
      "cause": "trying to disperse a group gathered on a hill near Lonmin 's platinum mine in Marikana on August 16",
      "effect": "Police opened fire"
    },
    {
      "cause": "Police opened fire",
      "effect": "killing 34 striking workers and wounding 78"
    }
  ],
  "pred_triples": []
}
```

### --- id=2147 ---

输入文本: In all , 58 persons were arrested for indulging in violence .

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
      "cause": "indulging in violence",
      "effect": "58 persons were arrested"
    }
  ],
  "pred_triples": []
}
```

### --- id=2882 ---

输入文本: By unfurling a separate flag , the supporters of a separate Vidarbha have insulted the tricolour and the Constitution , " it said .

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
      "cause": "unfurling a separate flag",
      "effect": "the supporters of a separate Vidarbha have insulted the tricolour and the Constitution"
    }
  ],
  "pred_triples": []
}
```

### --- id=691 ---

输入文本: In the streets too the general sense of animosity prevailed as the CPM and BJP workers scuffled outside the AKG Centre and 600 people were detained .

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
      "cause": "the CPM and BJP workers scuffled outside the AKG Centre and 600 people were detained",
      "effect": "In the streets too the general sense of animosity prevailed"
    }
  ],
  "pred_triples": []
}
```

### --- id=2347 ---

输入文本: Volunteers from the alliance have been camping at Queen 's Pier since April 26 in an attempt to save it from being demolished in a harbour reclamation plan .

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
      "cause": "to save it from being demolished in a harbour reclamation plan",
      "effect": "Volunteers from the alliance have been camping at Queen 's Pier since April 26"
    }
  ],
  "pred_triples": []
}
```

### --- id=44 ---

输入文本: Ramanathapuram Residents protest against illegal water connections

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
      "cause": "against illegal water connections",
      "effect": "Ramanathapuram Residents protest"
    }
  ],
  "pred_triples": []
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

### --- id=776 ---

输入文本: They had been on a wildcat strike since September 12 , demanding to be paid a minimum of R16,000 a month .

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
      "cause": "demanding to be paid a minimum of R16,000 a month",
      "effect": "They had been on a wildcat strike since September 12"
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
      "cause": "Keeping Mum While Vidarbha Flag Was Hoisted",
      "effect": "Sena Flays CM"
    },
    {
      "cause": "keeping mum when a flag of a separate Vidarbha state was recently hoisted in Nagpur on Maharashtra Day",
      "effect": "Ruling alliance partner Shiv Sena today flayed Maharashtra Chief Minister Devendra Fadnavis"
    }
  ],
  "pred_triples": []
}
```

### --- id=2004 ---

输入文本: Twelve students arrested for public violence while protesting against financial aid cuts at the University of the Witwatersrand appeared in the Johannesburg Regional Court on Tuesday .

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
      "cause": "public violence while protesting against financial aid cuts at the University of the Witwatersrand",
      "effect": "Twelve students arrested"
    },
    {
      "cause": "against financial aid cuts",
      "effect": "protesting"
    }
  ],
  "pred_triples": []
}
```

### --- id=976 ---

输入文本: There was a shutdown in various towns in Jammu regions against the incident .

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
      "cause": "against the incident",
      "effect": "There was a shutdown in various towns in Jammu regions"
    }
  ],
  "pred_triples": []
}
```

### --- id=386 ---

输入文本: A group of protesters pelted the police with stones , after the police dispersed them from blocking the road linking Brits and Letlhabile .

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
      "cause": "the police dispersed them from blocking the road linking Brits and Letlhabile",
      "effect": "A group of protesters pelted the police with stones"
    }
  ],
  "pred_triples": []
}
```

### --- id=1778 ---

输入文本: Addressing a rally here to protest against the offensive , he said , " Tamils should be given equal rights and powers in the affairs of Sri Lanka .

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
      "cause": "to protest against the offensive",
      "effect": "a rally here"
    }
  ],
  "pred_triples": []
}
```

### --- id=484 ---

输入文本: The clash left at least three students injured .

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
      "cause": "The clash",
      "effect": "left at least three students injured"
    }
  ],
  "pred_triples": []
}
```

### --- id=1595 ---

输入文本: ADILABAD : TRS condemns arrests March 11 , 2011 00:00 IST Telangana Rastra Samiti ( TRS ) on Thursday condemned arrests of Telangana protagonists from Adilabad district to foil the ‘ Million March ' .

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
      "cause": "to foil the ‘ Million March '",
      "effect": "Telangana Rastra Samiti ( TRS ) on Thursday condemned arrests of Telangana protagonists from Adilabad district"
    }
  ],
  "pred_triples": []
}
```

### --- id=1642 ---

输入文本: Mr. Bommai later told presspersons that whoever was responsible for forcing the protestors to stage such a protest would be dealt with sternly .

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
      "cause": "whoever was responsible for forcing the protestors to stage such a protest",
      "effect": "would be dealt with sternly"
    }
  ],
  "pred_triples": []
}
```

### --- id=1723 ---

输入文本: Mining for trouble Sino Gold Mining , which only last week announced a joint venture to expand exploration near its White Mountain Mine in Jilin province , had to halt operations yesterday as protesting farmers blocked the main access road .

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
      "cause": "protesting farmers blocked the main access road",
      "effect": "Sino Gold Mining , which only last week announced a joint venture to expand exploration near its White Mountain Mine in Jilin province , had to halt operations yesterday"
    },
    {
      "cause": "to expand exploration near its White Mountain Mine in Jilin province",
      "effect": "Sino Gold Mining , which only last week announced a joint venture"
    }
  ],
  "pred_triples": []
}
```

### --- id=2840 ---

输入文本: Thirty-seven of the operators signed a petition and held a press conference last Sunday to protest against the proposal , which they said would cut their basic salary by up to 40 per cent .

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
      "cause": "to protest",
      "effect": "Thirty-seven of the operators signed a petition and held a press conference last Sunday"
    },
    {
      "cause": "against the proposal , which they said would cut their basic salary by up to 40 per cent",
      "effect": "to protest"
    }
  ],
  "pred_triples": []
}
```

### --- id=296 ---

输入文本: The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma to probe into the violence and the deaths of 44 people in wage-related protests .

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
      "cause": "to probe into the violence and the deaths of 44 people in wage-related protests",
      "effect": "The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma"
    },
    {
      "cause": "wage-related protests",
      "effect": "the violence and the deaths of 44 people"
    }
  ],
  "pred_triples": []
}
```

### --- id=499 ---

输入文本: On August 16 , 2012 , police shot dead 34 people , almost all striking mineworkers , while trying to disperse and disarm them .

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
      "cause": "trying to disperse and disarm them",
      "effect": "police shot dead 34 people , almost all striking mineworkers"
    }
  ],
  "pred_triples": []
}
```

### --- id=1036 ---

输入文本: The fresh clash came a day after over 22 people , including five media men and 11 security personnel with an officer among them , were injured last night when students agitating over creation of a separate Telangana hurled stones at them on the Osmania University campus prompting them to use force to quell the mob .

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
  "pred_triples": []
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

### --- id=2060 ---

输入文本: 27th March 2012 05:03 AM THIRUVANANTHAPURAM : Protesting against the large-scale reclamation of Vellayani backwaters by the resorts and real-estate mafia , a Secretariat dharna was staged under the joint aegis of the Kalanilayam Paristhithi Vedi , environmentalists and cultural activists here on Monday .

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
      "cause": "against the large-scale reclamation of Vellayani backwaters by the resorts and real-estate mafia",
      "effect": "Protesting"
    },
    {
      "cause": "Protesting against the large-scale reclamation of Vellayani backwaters by the resorts and real-estate mafia",
      "effect": "a Secretariat dharna was staged under the joint aegis of the Kalanilayam Paristhithi Vedi , environmentalists and cultural activists here on Monday"
    }
  ],
  "pred_triples": []
}
```

### --- id=2849 ---

输入文本: Traders pulled down their shutters to join the statewide agitation to oppose the State Government 's move to amend the APMC Act on Friday .

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
  "pred_triples": []
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

### --- id=324 ---

输入文本: Hartal supporters pelted stones at a KSRTC bus at Karamana injuring driver Babu .

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
      "cause": "Hartal supporters pelted stones at a KSRTC bus at Karamana",
      "effect": "injuring driver Babu"
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
      "cause": "Congress workers on Monday attacked TDP senior leader and MLC Nannapaneni Rajakumari with sticks and stones",
      "effect": "leaving her badly mauled at Karamchedu"
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

### --- id=817 ---

输入文本: “ I think it is very selfish , ” explained the teenager , who was at his first rally and said he had come because he wanted to experience first-hand Hong Kong ’ s vibrant democracy movement .

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
      "cause": "he wanted to experience first-hand Hong Kong ’ s vibrant democracy movement",
      "effect": "he had come"
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
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
  "pred_triples": []
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
      "cause": "the state Cabinet urged him to accord permission to convene a 10 - day legislature session from June 2",
      "effect": "BJP legislators staged a dharna demanding Bhardwaj ’ s recall for his “ undemocratic conduct ”"
    },
    {
      "cause": "demanding Bhardwaj ’ s recall for his “ undemocratic conduct ”",
      "effect": "BJP legislators staged a dharna"
    }
  ],
  "pred_triples": []
}
```

### --- id=243 ---

输入文本: 2 held over poisoning threat to Tung PUBLISHED : Wednesday , 03 October , 2001 , 12:00am Donald Tsang Donald Tsang A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials were arrested in Central yesterday .

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
      "cause": "A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials",
      "effect": "were arrested in Central yesterday"
    }
  ],
  "pred_triples": []
}
```

### --- id=2601 ---

输入文本: Apart from students and teachers of Jawaharlal Nehru University , many residents too gathered here after hearing about the protest on news channels .

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
      "cause": "hearing about the protest on news channels",
      "effect": "Apart from students and teachers of Jawaharlal Nehru University , many residents too gathered here"
    }
  ],
  "pred_triples": []
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

### --- id=43 ---

输入文本: December 05 , 2017 00:00 IST Say officials at the panchayat level are colluding with locals Residents of Varavani panchayat staged a protest at the collectorate here on Monday , against illegal tapping of drinking water supplied through pipelines under the Cauvery combined water supply scheme and irregular supply of water to their villages .

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
      "cause": "against illegal tapping of drinking water supplied through pipelines under the Cauvery combined water supply scheme and irregular supply of water to their villages",
      "effect": "Residents of Varavani panchayat staged a protest at the collectorate here on Monday"
    }
  ],
  "pred_triples": []
}
```

### --- id=1248 ---

输入文本: Candlelight vigil held 27th December 2012 11:19 AM As many as 150 students and members of Akhila Bharatha Janavaadi Mahila Sangatane staged a protest on Wednesday to condemn the recent gang-rape on a 23 - year-old student in Delhi .

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
      "cause": "to condemn the recent gang-rape on a 23 - year-old student in Delhi",
      "effect": "As many as 150 students and members of Akhila Bharatha Janavaadi Mahila Sangatane staged a protest on Wednesday"
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
  "pred_triples": []
}
```

### --- id=8 ---

输入文本: The violence in Yuen Long has heightened tensions and fears of further attacks .

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
      "cause": "The violence in Yuen Long",
      "effect": "heightened tensions and fears of further attacks"
    }
  ],
  "pred_triples": []
}
```

### --- id=2636 ---

输入文本: Eight killed after 22 - hour Kashmir gunbattle

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
      "cause": "22 - hour Kashmir gunbattle",
      "effect": "Eight killed"
    }
  ],
  "pred_triples": []
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
      "cause": "to protest",
      "effect": "over 20,000 people rallied in Xiamen , a coastal city in Fujian province"
    },
    {
      "cause": "against plans to built a paraxylene chemical plant in the city",
      "effect": "to protest"
    }
  ],
  "pred_triples": []
}
```

### --- id=1602 ---

输入文本: Attempts Karimnagar Staff Reporter adds : The district police foiled the attempts made by the TRS and pro-Telangana activists to proceed and participate in ‘ Million March ' in Hyderabad on Thursday with their arrests on various routes proceeding to the capital .

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
      "cause": "their arrests on various routes proceeding to the capital",
      "effect": "The district police foiled the attempts made by the TRS and pro-Telangana activists to proceed and participate in ‘ Million March ' in Hyderabad on Thursday"
    },
    {
      "cause": "to proceed and participate in ‘ Million March ' in Hyderabad on Thursday",
      "effect": "the attempts made by the TRS and pro-Telangana activists"
    }
  ],
  "pred_triples": []
}
```

### --- id=2119 ---

输入文本: In a related development at Salem in Tamil Nadu , a 26 year-old man attempted self-immolation protesting against Rajapaksa ' visit .

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
      "cause": "protesting against Rajapaksa ' visit",
      "effect": "a 26 year-old man attempted self-immolation"
    }
  ],
  "pred_triples": []
}
```

### --- id=2104 ---

输入文本: Six protesters were injured in the firing .

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
      "cause": "the firing",
      "effect": "Six protesters were injured"
    }
  ],
  "pred_triples": []
}
```

### --- id=2494 ---

输入文本: About a hundred Maoists blew up part of a power sub-station in Naxal-dominated Jamui district , affecting power supply in the area .

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
      "cause": "About a hundred Maoists blew up part of a power sub-station in Naxal-dominated Jamui district",
      "effect": "affecting power supply in the area"
    }
  ],
  "pred_triples": []
}
```

### --- id=709 ---

输入文本: KRISHNAGIRI / DHARMAPURI : Water supply disrupted , villagers block road

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
      "cause": "Water supply disrupted",
      "effect": "villagers block road"
    }
  ],
  "pred_triples": []
}
```

### --- id=1715 ---

输入文本: NGO volunteers and prostitutes , holding red umbrellas symbolising protection , shouted : ' Legalisation of sex workers , innocence of sex workers ! ' The authorities quickly stepped in and banned the petition .

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
      "cause": "NGO volunteers and prostitutes , holding red umbrellas symbolising protection , shouted : ' Legalisation of sex workers , innocence of sex workers !",
      "effect": "The authorities quickly stepped in and banned the petition"
    }
  ],
  "pred_triples": []
}
```

### --- id=217 ---

输入文本: Local drivers have allegedly been attacking the vehicles and threatening foreign drivers , who they accuse of taking jobs meant for locals .

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
      "cause": "who they accuse of taking jobs meant for locals",
      "effect": "Local drivers have allegedly been attacking the vehicles and threatening foreign drivers"
    }
  ],
  "pred_triples": []
}
```

### --- id=1042 ---

输入文本: 19th June 2014 07:22 AM MADURAI : Distressed after allegedly being denied a scholarship by his school , a Class XII Dalit dropout of the Government Higher Secondary School in Allinagaram , in Theni district , tied to immolate himself on Tuesday .

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
      "cause": "allegedly being denied a scholarship by his school",
      "effect": "Distressed"
    },
    {
      "cause": "Distressed after allegedly being denied a scholarship by his school",
      "effect": "a Class XII Dalit dropout of the Government Higher Secondary School in Allinagaram , in Theni district , tied to immolate himself on Tuesday"
    }
  ],
  "pred_triples": []
}
```

### --- id=2168 ---

输入文本: He was addressing a dharna organised by the Joint Action Committee ( JAC ) of various Telangana outfits demanding scrapping of cases against the students .

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
      "cause": "demanding scrapping of cases against the students",
      "effect": "a dharna organised by the Joint Action Committee ( JAC ) of various Telangana outfits"
    }
  ],
  "pred_triples": []
}
```

### --- id=2181 ---

输入文本: For when they had met publicly on Sunday , Shiv Sena workers had barged in violently to break up their peaceful protest .

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
      "cause": "to break up their peaceful protest",
      "effect": "Shiv Sena workers had barged in violently"
    }
  ],
  "pred_triples": []
}
```

### --- id=1207 ---

输入文本: Three people have died and scores have been injured in violence related to the illegal strike .

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
      "cause": "the illegal strike",
      "effect": "Three people have died and scores have been injured in violence"
    },
    {
      "cause": "violence related to the illegal strike",
      "effect": "Three people have died and scores have been injured"
    }
  ],
  "pred_triples": []
}
```

### --- id=598 ---

输入文本: Alongside the protests , there were also celebrations in different parts of the city to hail the decision .

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
      "cause": "to hail the decision",
      "effect": "Alongside the protests , there were also celebrations in different parts of the city"
    }
  ],
  "pred_triples": []
}
```

### --- id=1290 ---

输入文本: The 1966 riots , which were prompted by a 50 per cent increase in cross-harbour ferry fares , took place against the backdrop of a bad economy and widening gap between the government and the people .

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
      "cause": "a 50 per cent increase in cross-harbour ferry fares",
      "effect": "The 1966 riots"
    }
  ],
  "pred_triples": []
}
```

### --- id=596 ---

输入文本: People have been forced to come out on the streets to protest the conspiracy to dislodge my government , " said Modi while demanding that she should be recalled .

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
      "cause": "to protest the conspiracy",
      "effect": "People have been forced to come out on the streets"
    },
    {
      "cause": "to dislodge my government",
      "effect": "to protest the conspiracy"
    }
  ],
  "pred_triples": []
}
```

### --- id=607 ---

输入文本: Reliance attacks : Congress expels NSUI leader 16th January 2010 09:33 PM HYDERABAD : The ruling Congress party in Andhra Pradesh Saturday expelled a leader of National Students Union of India ( NSUI ) from the party for his alleged involvement in the recent attacks on Reliance outlets in the state .

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
      "cause": "his alleged involvement in the recent attacks on Reliance outlets in the state",
      "effect": "The ruling Congress party in Andhra Pradesh Saturday expelled a leader of National Students Union of India ( NSUI ) from the party"
    }
  ],
  "pred_triples": []
}
```

### --- id=208 ---

输入文本: As hundreds of employees from the city went to Vizianagaram to take part in the last rites of N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI , an all-union meeting convened by the CITU resolved to organise demonstrations in front of all industrial establishments located in the city on Wednesday .

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
      "cause": "to take part in the last rites of N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI",
      "effect": "hundreds of employees from the city went to Vizianagaram"
    },
    {
      "cause": "to protest against the Centre ’ s decision on strategic stake sale of DCI",
      "effect": "N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks"
    }
  ],
  "pred_triples": []
}
```

### --- id=288 ---

输入文本: Last summer , tens of thousands of people in the northeastern city of Dalian , Liaoning , marched to demand the relocation of a chemical plant .

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
      "cause": "to demand the relocation of a chemical plant",
      "effect": "Last summer , tens of thousands of people in the northeastern city of Dalian , Liaoning , marched"
    }
  ],
  "pred_triples": []
}
```

### --- id=428 ---

输入文本: The legislator and his family members went on an indefinite fast here alleging that the Congress government was trying to implicate him in a false case .

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
      "cause": "alleging that the Congress government was trying to implicate him in a false case",
      "effect": "The legislator and his family members went on an indefinite fast here"
    }
  ],
  "pred_triples": []
}
```

### --- id=2484 ---

输入文本: The protestors removed a portion of the railway track between Diphu and Doldoli stations today , halting train movement , they said .

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
      "cause": "The protestors removed a portion of the railway track between Diphu and Doldoli stations today",
      "effect": "halting train movement"
    }
  ],
  "pred_triples": []
}
```

### --- id=1105 ---

输入文本: He accused the government of suppressing a peaceful and democratic protest to demand Telangana state .

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
      "cause": "suppressing a peaceful and democratic protest to demand Telangana state",
      "effect": "He accused the government"
    },
    {
      "cause": "to demand Telangana state",
      "effect": "a peaceful and democratic protest"
    }
  ],
  "pred_triples": []
}
```

### --- id=196 ---

输入文本: The escalating protests in the JNU follow the arrest of student union president Kanhaiya Kumar on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir .

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
      "cause": "the arrest of student union president Kanhaiya Kumar",
      "effect": "The escalating protests in the JNU"
    },
    {
      "cause": "on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir",
      "effect": "the arrest of student union president Kanhaiya Kumar"
    }
  ],
  "pred_triples": []
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

### --- id=2645 ---

输入文本: Mathura clashes : Superintendent of Police among two policemen killed 03rd June 2016 08:59 AM A fire break out after clashes between the police and the encroachers who were being evicted from Jawaharbagh in Mathura on Thursday .

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
      "cause": "clashes between the police and the encroachers who were being evicted from Jawaharbagh in Mathura on Thursday",
      "effect": "A fire break out"
    }
  ],
  "pred_triples": []
}
```

### --- id=2113 ---

输入文本: Main accused Dawood Ibrahim Kaskar and Tiger Memon have still not been brought to trial as they fled India hours after the blasts .

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
      "cause": "they fled India hours after the blasts",
      "effect": "Main accused Dawood Ibrahim Kaskar and Tiger Memon have still not been brought to trial"
    }
  ],
  "pred_triples": []
}
```

### --- id=2916 ---

输入文本: A group of conservationists has been camping at the pier for nearly two months , in protest at its proposed demolition .

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
      "cause": "in protest at its proposed demolition",
      "effect": "A group of conservationists has been camping at the pier for nearly two months"
    }
  ],
  "pred_triples": []
}
```

### --- id=1950 ---

输入文本: The altercation took a turn for the worse as bystanders from both the communities joined in with whatever they could lay their hands on .

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
      "cause": "bystanders from both the communities joined in with whatever they could lay their hands on",
      "effect": "The altercation took a turn for the worse"
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

### --- id=2011 ---

输入文本: Then , Roja , along with other YSRC leaders and activists , immediately staged a dharna at the temple itself until the early hours of Saturday seeking action against those involved in the incident .

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
      "cause": "seeking action against those involved in the incident",
      "effect": "Roja , along with other YSRC leaders and activists , immediately staged a dharna at the temple itself until the early hours of Saturday"
    }
  ],
  "pred_triples": []
}
```

### --- id=1640 ---

输入文本: Mr. Bommai visited Savanur on Wednesday along with officials and other elected representatives and asked the Deputy Commissioner to inquire into the circumstances that forced the community members to stage such a protest .

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
      "cause": "asked the Deputy Commissioner to inquire into the circumstances that forced the community members to stage such a protest .",
      "effect": "Mr. Bommai visited Savanur on Wednesday along with officials and other elected representatives"
    }
  ],
  "pred_triples": []
}
```

### --- id=215 ---

输入文本: We wo n't tolerate attacks on our drivers , say KZN trucking companies ANA Reporter DURBAN , June 3 ( ANA ) – Trucking companies said on Monday they would not tolerate attacks on their drivers , following the torching of 17 trucks in KwaZulu-Natal at the weekend .

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
      "cause": "the torching of 17 trucks in KwaZulu-Natal at the weekend",
      "effect": "Trucking companies said on Monday they would not tolerate attacks on their drivers"
    }
  ],
  "pred_triples": []
}
```

### --- id=2531 ---

输入文本: India had suspended the talks after Pakistani gunmen attacked Mumbai last year , saying it would not be resumed till Islamabad showed concrete action on meeting India ’ s concerns over cross-border terrorism .

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
  "pred_triples": []
}
```

### --- id=3013 ---

输入文本: Led by former Minister Mandava Venkateswar Rao , MLA ( Nizamabad Urban ) MLAs Annapoornamma and Hanmanth Shinde and MLCs V.G. Goud and A. Narsa Reddy held protest demonstration in front of the office of Superintending Engineer demanding rectification of the situation within two days .

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
      "cause": "demanding rectification of the situation within two days",
      "effect": "MLA ( Nizamabad Urban ) MLAs Annapoornamma and Hanmanth Shinde and MLCs V.G. Goud and A. Narsa Reddy held protest demonstration in front of the office of Superintending Engineer"
    }
  ],
  "pred_triples": []
}
```

### --- id=2705 ---

输入文本: This led to violent protests across the city the next day , with a group of students even storming into the university campus and demanding the dismissal of the teacher who had set the question paper .

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
      "cause": "demanding the dismissal of the teacher who had set the question paper",
      "effect": "a group of students even storming into the university campus"
    }
  ],
  "pred_triples": []
}
```

### --- id=783 ---

输入文本: The company had further offered a once-off hardship allowance of R2000 to help workers deal with financial difficulties arising from the no-work , no-pay principle in place while they were striking .

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
      "cause": "to help workers deal with financial difficulties arising from the no-work , no-pay principle in place while they were striking",
      "effect": "The company had further offered a once-off hardship allowance of R2000"
    },
    {
      "cause": "the no-work , no-pay principle in place",
      "effect": "financial difficulties"
    }
  ],
  "pred_triples": []
}
```

### --- id=1512 ---

输入文本: " I had to walk half the distance after some people forcibly stopped the auto I was travelling in , " said a commuter .

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
      "cause": "some people forcibly stopped the auto I was travelling in",
      "effect": "I had to walk half the distance"
    }
  ],
  "pred_triples": []
}
```

### --- id=2372 ---

输入文本: It is learnt that the abducted TDP leaders along with several others working for the ruling party in the mandals of GK Veedhi and Chintapalle , have agreed to resign from the party and intensify agitations against bauxite mining , as demanded by the Maoists .

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
      "cause": "demanded by the Maoists",
      "effect": "the abducted TDP leaders along with several others working for the ruling party in the mandals of GK Veedhi and Chintapalle , have agreed to resign from the party and intensify agitations against bauxite mining"
    }
  ],
  "pred_triples": []
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

### --- id=2537 ---

输入文本: More than 1,200 permanent and 600 casual workers are protesting for their jobs and salaries .

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
      "cause": "their jobs and salaries",
      "effect": "More than 1,200 permanent and 600 casual workers are protesting"
    }
  ],
  "pred_triples": []
}
```

### --- id=513 ---

输入文本: A series of blasts took place Sunday before Modi was to address the BJP rally , leaving six dead and over 80 injured .

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
      "cause": "A series of blasts took place Sunday",
      "effect": "leaving six dead and over 80 injured"
    }
  ],
  "pred_triples": []
}
```

### --- id=2653 ---

输入文本: The encroachers , who have been on a protest for two years , demand " cancellation of the elections " of the President and Prime Minister of India .

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
      "cause": "demand \" cancellation of the elections \" of the President and Prime Minister of India",
      "effect": "The encroachers , who have been on a protest for two years"
    }
  ],
  "pred_triples": []
}
```

### --- id=2538 ---

输入文本: TAMIL NADU Post blasts , the web of security tightens May 29 , 2014 00:00 IST Railway stations , places of worship , cinema halls , malls – the enhanced protective measures are everywhere The May Day twin blasts on platform nine of Chennai Central sent a strong message to various enforcement agencies in the city .

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
      "cause": "The May Day twin blasts on platform nine of Chennai Central sent a strong message to various enforcement agencies in the city",
      "effect": "Railway stations , places of worship , cinema halls , malls – the enhanced protective measures are everywhere"
    }
  ],
  "pred_triples": []
}
```

### --- id=29 ---

输入文本: The NIA wanted to catch Akram alive as he could provide clues in resolving the blast case .

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
      "cause": "he could provide clues in resolving the blast case",
      "effect": "The NIA wanted to catch Akram alive"
    }
  ],
  "pred_triples": []
}
```

### --- id=360 ---

输入文本: Director Tlhalefang Kuetsile earlier said eight students were arrested and four injured when police fired rubber bullets during a protest on the campus .

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
      "cause": "police fired rubber bullets during a protest on the campus",
      "effect": "eight students were arrested and four injured"
    }
  ],
  "pred_triples": []
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

### --- id=1453 ---

输入文本: Angered community members mobilised and marched to a suspected gang member 's house in Bardien Street where Tavern Moss was stabbed and beaten to death , police said at the time .

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
      "cause": "Tavern Moss was stabbed and beaten to death",
      "effect": "Angered community members mobilised and marched to a suspected gang member 's house in Bardien Street"
    }
  ],
  "pred_triples": []
}
```

### --- id=2212 ---

输入文本: COIMBATORE : Fire triggers flash stir by conservancy workers

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
      "cause": "Fire",
      "effect": "flash stir by conservancy workers"
    }
  ],
  "pred_triples": []
}
```

### --- id=2413 ---

输入文本: The protestors were apparently protesting about water shortages in Ntsweletsoku village in Lehurutshe in the North West .

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
      "cause": "water shortages in Ntsweletsoku village in Lehurutshe in the North West",
      "effect": "The protestors were apparently protesting"
    }
  ],
  "pred_triples": []
}
```

### --- id=835 ---

输入文本: Srinagar in Jammu | PTI SRINAGAR : Tension prevailed at NIT here with outstation students today making a slew of demands , including shifting the institute out of Kashmir and action against the policemen involved in lathicharge yesterday , as an HRD team rushed here from Delhi to resolve the crisis being witnessed since last six days .

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
      "cause": "outstation students today making a slew of demands",
      "effect": "Tension prevailed at NIT here"
    },
    {
      "cause": "to resolve the crisis being witnessed since last six days",
      "effect": "an HRD team rushed here from Delhi"
    }
  ],
  "pred_triples": []
}
```

### --- id=2023 ---

输入文本: Arrest of ISI Spies Have Created Panic Among People

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
      "cause": "Arrest of ISI Spies",
      "effect": "Have Created Panic Among People"
    }
  ],
  "pred_triples": []
}
```

### --- id=2907 ---

输入文本: VISAKHAPATNAM : Maoists observe bandh in Visakha Agency area October 07 , 2011 00:00 IST Vijayadasami festival coincided with a bandh on Thursday in the Visakha Agency for which the CPI ( Maoist ) gave the call demanding that the police produce in a court of law the party 's Andhra-Orissa border special zone committee member and a central committee member Damodar alias Azad , who was reportedly taken into custody a few days ago .

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
      "cause": "demanding that the police produce in a court of law the party 's Andhra-Orissa border special zone committee member and a central committee member Damodar alias Azad , who was reportedly taken into custody a few days ago",
      "effect": "a bandh on Thursday in the Visakha Agency for which the CPI ( Maoist ) gave the call"
    },
    {
      "cause": "the CPI ( Maoist ) gave the call",
      "effect": "a bandh on Thursday in the Visakha Agency"
    }
  ],
  "pred_triples": []
}
```

### --- id=2061 ---

输入文本: Dharna staged against reclamation of lake

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
      "cause": "against reclamation of lake",
      "effect": "Dharna staged"
    }
  ],
  "pred_triples": []
}
```

### --- id=584 ---

输入文本: 20th July 2015 03:05 AM GUWAHATI : In the aftermath of the murder of two Hindi-speaking persons last week by the Paresh Baruah faction of the banned United Liberation Front of Assam ( Ulfa ) , which also threatened to target the community in the coming days , people took out a march here on Sunday to demonstrate their anger against the outfit .

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
      "cause": "the murder of two Hindi-speaking persons last week by the Paresh Baruah faction of the banned United Liberation Front of Assam ( Ulfa )",
      "effect": "people took out a march here on Sunday to demonstrate their anger against the outfit"
    },
    {
      "cause": "to demonstrate their anger against the outfit",
      "effect": "people took out a march here on Sunday"
    }
  ],
  "pred_triples": []
}
```

### --- id=1579 ---

输入文本: DAVANGERE : CPI protests against price rise in Davangere

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
      "cause": "against price rise in Davangere",
      "effect": "CPI protests"
    }
  ],
  "pred_triples": []
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
      "cause": "The ongoing strike of PG medical students of the Government General Hospital ( GGH )",
      "effect": "hit medical services badly"
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
      "cause": "urging the party leader ’ s intervention",
      "effect": "they handed over a memorandum to her assistants"
    }
  ],
  "pred_triples": []
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
      "cause": "the Naxalites ’ falling support base",
      "effect": "the abductions"
    },
    {
      "cause": "The official claim that the abductions are the outcome of the Naxalites ’ falling support base",
      "effect": "divert attention from the core issue"
    }
  ],
  "pred_triples": []
}
```

### --- id=1194 ---

输入文本: A day after the snap protest by the Karnataka State Reserve Police ( KSRP ) personnel extending support to their chief P. Ravindranath , who has now been transferred , senior officials on Thursday chalked out a strategy to prevent them from continuing the protest by deploying all the 1,200 KSRP personnel on various duties .

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
      "cause": "to prevent them from continuing the protest",
      "effect": "senior officials on Thursday chalked out a strategy"
    },
    {
      "cause": "to prevent them from continuing the protest",
      "effect": "deploying all the 1,200 KSRP personnel on various duties"
    }
  ],
  "pred_triples": []
}
```

### --- id=2930 ---

输入文本: 01st July 2010 03:56 AM NEW DELHI : Unnerved by another instance of sudden ambush and massacre of Central Reserve Police Force personnel by Maoists , the Centre on Wednesday gave hint of enacting a tactical retreat from Naxal strongholds like Dantewada and Narayanpur in Chhattisgarh , camouflaging it as ‘ revisiting deployment ’ .

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
      "cause": "another instance of sudden ambush and massacre of Central Reserve Police Force personnel by Maoists",
      "effect": "Unnerved"
    },
    {
      "cause": "Unnerved by another instance of sudden ambush and massacre of Central Reserve Police Force personnel by Maoists",
      "effect": "the Centre on Wednesday gave hint of enacting a tactical retreat from Naxal strongholds like Dantewada and Narayanpur in Chhattisgarh"
    }
  ],
  "pred_triples": []
}
```

### --- id=2595 ---

输入文本: But the shutdown success has provided the much-needed shot in the arm to him to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP .

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
      "cause": "the shutdown success",
      "effect": "the much-needed shot in the arm to him to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP"
    }
  ],
  "pred_triples": []
}
```

### --- id=1590 ---

输入文本: 2 K form human chain to protest blocked road 24th July 2016 06:30 AM BENGALURU : IN an unprecedented show of strength , around 2,000 residents of Somasandrapalya , Haraluru , HSR Layout , Kudlu , Mangamanapalya , Hosapalya and surrounding areas gathered near Ravindra Bharathi Global School in HSR Layout on Saturday and formed a human chain near a wall constructed by Sobha Daffodil apartment .

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
  "pred_triples": []
}
```

### --- id=326 ---

输入文本: Hartal supporters surrounded a police station at Attakkulangara demanding that four men arrested by police for pelting stones at KSRTC buses be freed .

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
      "cause": "demanding that four men arrested by police for pelting stones at KSRTC buses be freed",
      "effect": "Hartal supporters surrounded a police station at Attakkulangara"
    },
    {
      "cause": "pelting stones at KSRTC buses",
      "effect": "four men arrested by police"
    }
  ],
  "pred_triples": []
}
```

### --- id=2122 ---

输入文本: - Indian Express Express News Service , Express News Service : Chandigarh , Tue Aug 20 2013 , 03:19 hrs CHANDIGARH : Panjab University Student Union ( PUSU ) , a student 's organisations of the Panjab University ( PU ) , staged a protest outside the vice-chancellor office on Monday demanding re-appear examination at the earliest to fulfill 50 per cent credit requirement for students in University Institute of Engineering and Technology ( UIET ) .

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
      "cause": "demanding re-appear examination at the earliest",
      "effect": "Panjab University Student Union ( PUSU ) , a student 's organisations of the Panjab University ( PU ) , staged a protest outside the vice-chancellor office on Monday"
    },
    {
      "cause": "to fulfill 50 per cent credit requirement for students in University Institute of Engineering and Technology ( UIET )",
      "effect": "demanding re-appear examination at the earliest"
    }
  ],
  "pred_triples": []
}
```

### --- id=1900 ---

输入文本: June 30 : A DSP and four constables were killed in a landmine blast triggered by suspected CPI-Maoist cadres at Pundigiri village in Bundu , 50 - kilometres from Ranchi .

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
      "cause": "a landmine blast",
      "effect": "A DSP and four constables were killed"
    },
    {
      "cause": "suspected CPI-Maoist cadres at Pundigiri village in Bundu , 50 - kilometres from Ranchi",
      "effect": "a landmine blast"
    }
  ],
  "pred_triples": []
}
```

### --- id=2406 ---

输入文本: Mulaudzi could not confirm reports that the miners were demonstrating after Xstrata fired them .

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
      "cause": "Xstrata fired them",
      "effect": "the miners were demonstrating"
    }
  ],
  "pred_triples": []
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

### --- id=2415 ---

输入文本: Protestors had made the road completely impassable by adding more stones .

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
      "cause": "adding more stones",
      "effect": "Protestors had made the road completely impassable"
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
