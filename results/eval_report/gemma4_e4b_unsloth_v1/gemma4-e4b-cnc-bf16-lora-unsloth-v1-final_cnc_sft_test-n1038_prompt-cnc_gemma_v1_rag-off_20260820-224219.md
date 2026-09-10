# gemma4-e4b-cnc-bf16-lora-unsloth-v1-final CNC SFT test eval report

## 配置
```json
{
  "label": "gemma4-e4b-cnc-bf16-lora-unsloth-v1-final CNC SFT test",
  "model": "gemma4-e4b-cnc-bf16-lora-unsloth-v1-final",
  "dataset": "cnc_sft_test",
  "sample_count": 1038,
  "prompt_name": "cnc_gemma_v1",
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
  "report_error_metric": "strict_token_f1",
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ gemma4-e4b-cnc-bf16-lora-unsloth-v1-final CNC SFT test final report ================
样本总数: 1038
  Gold 含因果: 548 | Pred 含因果: 488
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.840
  Precision: 0.891
  Recall   : 0.794
  F1       : 0.840
  (TP=435, TN=437, FP=53, FN=113)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 1038
    Gold triples: 763 | Pred triples: 613
    Precision: 0.622
    Recall   : 0.499
    F1       : 0.554
    (TP=381, FP=232, FN=382)
  [anchor_window]
    样本数: 1038
    Gold triples: 763 | Pred triples: 613
    Precision: 0.674
    Recall   : 0.541
    F1       : 0.600
    (TP=413, FP=200, FN=350)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 435
    Gold triples: 634 | Pred triples: 553
    Precision: 0.689
    Recall   : 0.601
    F1       : 0.642
    (TP=381, FP=172, FN=253)
  [anchor_window]
    样本数: 435
    Gold triples: 634 | Pred triples: 553
    Precision: 0.747
    Recall   : 0.651
    F1       : 0.696
    (TP=413, FP=140, FN=221)
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

Sample details shown: first 200 of 356 wrong samples from 1038 total samples.

### --- id=2070 ---

输入文本: 17th November 2012 11:20 AM Squarely blaming the Pattali Makkal Katchi ( PMK ) for orchestrating the violence against Dalits in three villages in Dharmapuri , VCK leader Thol Thirumavalavan on Friday demanded a CBI investigation into the matter and action against those openly instigating caste violence on public platforms .

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
        "span": "the violence"
      }
    },
    {
      "cause": {
        "span": "openly instigating caste violence on public platforms"
      },
      "relation": "caused",
      "effect": {
        "span": "action against those"
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
        "span": "expressing support for the police 's handling of a protest in Mong Kok at which rival groups clashed over a teacher 's verbal attack on officers"
      },
      "relation": "caused",
      "effect": {
        "span": "he caused uproar in some quarters"
      }
    }
  ]
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
        "span": "' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC ) to urge the central government to immediately carve out a Telangana state"
      },
      "relation": "caused",
      "effect": {
        "span": "﻿Police arrested leaders of various political parties who squatted on the highway"
      }
    },
    {
      "cause": {
        "span": "to urge the central government to immediately carve out a Telangana state"
      },
      "relation": "caused",
      "effect": {
        "span": "' Sadak Bandh ' called by Telangana Joint Action Committee ( JAC )"
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
        "span": "two persons , who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district with an intention of causing mass destruction to the train and passengers"
      },
      "relation": "caused",
      "effect": {
        "span": "were detained under the National Security Act in December"
      }
    },
    {
      "cause": {
        "span": "an intention of causing mass destruction to the train and passengers"
      },
      "relation": "caused",
      "effect": {
        "span": "two persons , who placed a cement slab on the railway track between Poovanur and Ulundurpet railway stations in Villupuram district"
      }
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
      "cause": "planning , financing and facilitating the Mumbai attack",
      "effect": "Pakistan has arrested seven suspected terrorists of the Lashkar-e-Taiba terror outfit , including its founding member Zakiur Rehman Lakhvi"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "who face charges of planning , financing and facilitating the Mumbai attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Pakistan has arrested seven suspected terrorists of the Lashkar-e-Taiba terror outfit , including its founding member Zakiur Rehman Lakhvi"
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
      "cause": "to condemn the “ extremely violent ” storming of the legislature",
      "effect": "Lam called a rare press conference early on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to condemn the “ extremely violent ” storming of the legislature"
      },
      "relation": "caused",
      "effect": {
        "span": "Lam called a rare press conference early on Tuesday"
      }
    },
    {
      "cause": {
        "span": "which she described as “ heartbreaking and shocking ”"
      },
      "relation": "caused",
      "effect": {
        "span": "to condemn the “ extremely violent ” storming of the legislature"
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
      "cause": "assaulted Akilan",
      "effect": "injuring him"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Five members of the old group entered the church during the Sunday mass yesterday and assaulted Akilan"
      },
      "relation": "caused",
      "effect": {
        "span": "injuring him"
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
        "span": "Four-time MP Yadav was arrested in 1999 and convicted"
      }
    },
    {
      "cause": {
        "span": "Four-time MP Yadav was arrested in 1999 and convicted"
      },
      "relation": "caused",
      "effect": {
        "span": "sentenced to life imprisonment Feb 14 , 2008"
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
      "relation": "caused",
      "effect": {
        "span": "opposition parties to raise fingers at \" TMC 's internal feud that led to the incident \""
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
        "span": "In retaliation"
      },
      "relation": "caused",
      "effect": {
        "span": "the police fired a few rounds in the air which finally capped the clashes"
      }
    },
    {
      "cause": {
        "span": "the police fired a few rounds in the air"
      },
      "relation": "caused",
      "effect": {
        "span": "which finally capped the clashes"
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
        "span": "the bloody crackdown"
      },
      "relation": "caused",
      "effect": {
        "span": "fear and economic inducements ensured they turned away from politics"
      }
    }
  ]
}
```

### --- id=395 ---

输入文本: 12 held after group clashes in Surat - Indian Express Express News Service , Express News Service : Surat , Tue Sep 04 2012 , 06:45 hrs The police have arrested 12 people in connection with the clashes that broke out between the members of Patel and Bharwad communities in Punagam area of the city on Sunday .

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
      "cause": "the clashes that broke out between the members of Patel and Bharwad communities in Punagam area of the city on Sunday",
      "effect": "The police have arrested 12 people"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "group clashes in Surat"
      },
      "relation": "caused",
      "effect": {
        "span": "12 held"
      }
    },
    {
      "cause": {
        "span": "the clashes that broke out between the members of Patel and Bharwad communities in Punagam area of the city on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "The police have arrested 12 people"
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
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

### --- id=2377 ---

输入文本: The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday to condemn what it called a “ concerted attack on Hindu leaders in the state . ” Ramesh , the state BJP unit ’ s general secretary and a charted accountant by profession , was murdered by assailants in Salem while he was on his way back home after visiting the party office on Friday evening .

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
        "span": "to condemn what it called a “ concerted attack on Hindu leaders in the state"
      },
      "relation": "caused",
      "effect": {
        "span": "The party leadership in Tamil Nadu , on the other hand , called for statewide bandh on Monday"
      }
    },
    {
      "cause": {
        "span": "visiting the party office on Friday evening"
      },
      "relation": "caused",
      "effect": {
        "span": "Ramesh , the state BJP unit ’ s general secretary and a charted accountant by profession , was on his way back home"
      }
    },
    {
      "cause": {
        "span": "assailants in Salem"
      },
      "relation": "caused",
      "effect": {
        "span": "Ramesh , the state BJP unit ’ s general secretary and a charted accountant by profession , was murdered"
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
        "span": "against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC )"
      },
      "relation": "caused",
      "effect": {
        "span": "youths protesting"
      }
    },
    {
      "cause": {
        "span": "youths protesting against the reservation policy of the Uttar Pradesh Public Service Commission ( UPPSC ) went on the rampage"
      },
      "relation": "caused",
      "effect": {
        "span": "the violence that took place on Monday"
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
        "span": "against renewed ' racism and Afro-phobia '"
      },
      "relation": "caused",
      "effect": {
        "span": "diplomats from 42 African nations boycotted the weeklong celebration of Africa Day , hosted by the Indian government as a sign of protest"
      }
    },
    {
      "cause": {
        "span": "a sign of protest against renewed ' racism and Afro-phobia '"
      },
      "relation": "caused",
      "effect": {
        "span": "diplomats from 42 African nations boycotted the weeklong celebration of Africa Day , hosted by the Indian government"
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
        "span": "the two-day bandh call given by the pro-United Andhra Pradesh groups"
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
        "span": "in support of party president Y.S. Jaganmohan Reddy ’ s indefinite ‘ deeksha ’ in Guntur seeking special category status for the State"
      },
      "relation": "caused",
      "effect": {
        "span": "YSR Congress leaders and cadres organised relay hunger strikes in various Assembly constituencies across the district on Thursday"
      }
    },
    {
      "cause": {
        "span": "seeking special category status for the State"
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
        "span": "Protests"
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
        "span": "violent protests in parts of the Western Cape"
      },
      "relation": "caused",
      "effect": {
        "span": "countrywide public hearings on a new minimum wage for the agriculture sector"
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
        "span": "Some of the youths decided"
      }
    }
  ]
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
        "span": "to mark the 22nd anniversary of the return of sovereignty from Britain to China"
      },
      "relation": "caused",
      "effect": {
        "span": "an official ceremony took place at the Hong Kong Convention and Exhibition Centre"
      }
    },
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
        "span": "the “ carnage"
      },
      "relation": "caused",
      "effect": {
        "span": "the people would give a fitting reply to the Communist Party of India (Marxist)-led government"
      }
    },
    {
      "cause": {
        "span": "the “ atrocities committed by CPI(M) cadres on the innocent people of Nandigram"
      },
      "relation": "caused",
      "effect": {
        "span": "Condemning"
      }
    },
    {
      "cause": {
        "span": "a year"
      },
      "relation": "caused",
      "effect": {
        "span": "“ those responsible had not been punished"
      }
    }
  ]
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
      "cause": "some of them raised slogans against Chief Minister YS Rajasekhara Reddy",
      "effect": "They were caned mercilessly and shooed out of the venue"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "some of them raised slogans against Chief Minister YS Rajasekhara Reddy who inaugurated the two-day job mela organised by the Greater Hyderabad Municipal Corporation ( GHMC )"
      },
      "relation": "caused",
      "effect": {
        "span": "They were caned mercilessly and shooed out of the venue"
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
      "relation": "caused",
      "effect": {
        "span": "About 1,000 foreign domestic helpers yesterday protested"
      }
    },
    {
      "cause": {
        "span": "saying it had threatened their livelihoods"
      },
      "relation": "caused",
      "effect": {
        "span": "About 1,000 foreign domestic helpers yesterday protested against the temporary suspension of the employers ' levy"
      }
    },
    {
      "cause": {
        "span": "permanent abolition of the tax"
      },
      "relation": "caused",
      "effect": {
        "span": "called"
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
      "cause": "Sectarian clashes broke out in Inderkoot village in Sumbal town on December 19",
      "effect": "one person was injured and a house was partially damaged in arson"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "arson"
      },
      "relation": "caused",
      "effect": {
        "span": "one person was injured and a house was partially damaged"
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
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
        "span": "to end the violence against north Indians and ensure the safety of everyone living in India 's financial capital"
      },
      "relation": "caused",
      "effect": {
        "span": "the Centre issued a stern advisory to the Maharashtra government , asking it to act quickly"
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
        "span": "the recent protests"
      }
    },
    {
      "cause": {
        "span": "against her administration and Beijing"
      },
      "relation": "caused",
      "effect": {
        "span": "the demonstrations have morphed into a wider movement"
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
        "span": "to discourage them from participating in separate Telangana agitations"
      },
      "relation": "caused",
      "effect": {
        "span": "the cases were filed against the students"
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
      "cause": "People invaded the land in Rus-ter-vaal in the previous weeks",
      "effect": "the Emfuleni Municipality had obtained a court order to evict them"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to evict them"
      },
      "relation": "caused",
      "effect": {
        "span": "the Emfuleni Municipality had obtained a court order"
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
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
        "span": "trying to disperse a group gathered on a hill near Lonmin 's platinum mine in Marikana on August 16"
      },
      "relation": "caused",
      "effect": {
        "span": "Police opened fire , killing 34 striking workers and wounding 78"
      }
    }
  ]
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
      "cause": "the potential effect of the strike was `` so serious ''",
      "effect": "there was a case to declare public transport an essential service that could not be disrupted by strike action"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "the potential effect"
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
        "span": "a flag of a separate Vidarbha state was recently hoisted in Nagpur on Maharashtra Day"
      },
      "relation": "caused",
      "effect": {
        "span": "Ruling alliance partner Shiv Sena today flayed Maharashtra Chief Minister Devendra Fadnavis for keeping mum"
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
        "span": "to release medical bulletins on the health of Jagan , who is fasting in the jail"
      },
      "relation": "caused",
      "effect": {
        "span": "YSRC leaders Shoba Nagireddy , Praveen Kumar Reddy , G Babu Rao met jails IG Sunil Kumar and represented to him"
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
        "span": "to foil the ‘ Million March '"
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
        "span": "whoever was responsible"
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
        "span": "Mining for trouble Sino Gold Mining , which only last week announced a joint venture to expand exploration near its White Mountain Mine in Jilin province , had to halt operations yesterday"
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
        "span": "which they said would cut their basic salary by up to 40 per cent"
      },
      "relation": "caused",
      "effect": {
        "span": "to protest against the proposal"
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
        "span": "'s turnout was smaller"
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
        "span": "to quell the mob"
      },
      "relation": "caused",
      "effect": {
        "span": "prompting them to use force"
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
        "span": "we push and we push"
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
        "span": "against the large-scale reclamation of Vellayani backwaters by the resorts and real-estate mafia"
      },
      "relation": "caused",
      "effect": {
        "span": "a Secretariat dharna was staged under the joint aegis of the Kalanilayam Paristhithi Vedi , environmentalists and cultural activists here on Monday"
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
        "span": "to join the statewide agitation"
      },
      "relation": "caused",
      "effect": {
        "span": "Traders pulled down their shutters"
      }
    },
    {
      "cause": {
        "span": "to oppose the State Government 's move to amend the APMC Act on Friday"
      },
      "relation": "caused",
      "effect": {
        "span": "to join the statewide agitation"
      }
    }
  ]
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
    "fp": 2,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
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
        "span": "to curb violence , protect infrastructure and prevent further damage to the economy"
      },
      "relation": "caused",
      "effect": {
        "span": "he would ask police commissioner General Khehla Sitole to activate the National Joint Operations and Intelligence Structure ( Natjoints )"
      }
    },
    {
      "cause": {
        "span": "looting , attacks on foreign nationals and the torching of trucks in an ongoing labour protest"
      },
      "relation": "caused",
      "effect": {
        "span": "curb violence , protect infrastructure and prevent further damage to the economy"
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
        "span": "to convene a 10 - day legislature session from June 2"
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
        "span": "poisoning threat to Tung"
      },
      "relation": "caused",
      "effect": {
        "span": "2 held"
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
        "span": "hearing about the protest on news channels"
      },
      "relation": "caused",
      "effect": {
        "span": "many residents too gathered here"
      }
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
        "span": "some of their colleagues got hurt during the stone-pelting and rataliated"
      },
      "relation": "caused",
      "effect": {
        "span": "the police showed maximum restraint but lost temper"
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
      "cause": "unrest",
      "effect": "VCK blames PMK"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "VCK blames PMK"
      },
      "relation": "caused",
      "effect": {
        "span": "unrest"
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
        "span": "their arrests on various routes proceeding to the capital"
      },
      "relation": "caused",
      "effect": {
        "span": "The district police foiled the attempts made by the TRS and pro-Telangana activists to proceed and participate in ‘ Million March ' in Hyderabad on Thursday"
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
        "span": "Distressed"
      }
    },
    {
      "cause": {
        "span": "Distressed"
      },
      "relation": "caused",
      "effect": {
        "span": "a Class XII Dalit dropout of the Government Higher Secondary School in Allinagaram , in Theni district , tied to immolate himself on Tuesday"
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
        "span": "they had met publicly on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "Shiv Sena workers had barged in violently to break up their peaceful protest"
      }
    },
    {
      "cause": {
        "span": "to break up their peaceful protest"
      },
      "relation": "caused",
      "effect": {
        "span": "Shiv Sena workers had barged in violently"
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
        "span": "This"
      },
      "relation": "caused",
      "effect": {
        "span": "injury to accused no : 37 in the case"
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
        "span": "protest the conspiracy to dislodge my government"
      },
      "relation": "caused",
      "effect": {
        "span": "People have been forced to come out on the streets"
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
        "span": "to take part in the last rites of N. Venkatesh"
      },
      "relation": "caused",
      "effect": {
        "span": "hundreds of employees from the city went to Vizianagaram"
      }
    },
    {
      "cause": {
        "span": "to protest against the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "N. Venkatesh , an assistant in the administration department of the corporation , who committed suicide on railway tracks"
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
        "span": "He accused the government of suppressing a peaceful and democratic protest"
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
    },
    {
      "cause": {
        "span": "charges that he too shouted the anti-Indian slogans at a meeting on Kashmir"
      },
      "relation": "caused",
      "effect": {
        "span": "the arrest of student union president Kanhaiya Kumar"
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
    },
    {
      "cause": {
        "span": "they alluded that he was anti-national , in addition to passing disparaging remarks about him"
      },
      "relation": "caused",
      "effect": {
        "span": "allegedly defaming Prime Minister Manmohan Singh in their protest act"
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
        "span": "to stage such a protest"
      },
      "relation": "caused",
      "effect": {
        "span": "the community members to inquire into the circumstances"
      }
    }
  ]
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
      "cause": "demanding the dismissal of the teacher who had set the question paper",
      "effect": "a group of students even storming into the university campus"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding the dismissal of the teacher who had set the question paper"
      },
      "relation": "caused",
      "effect": {
        "span": "violent protests across the city the next day , with a group of students even storming into the university campus"
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
        "span": "Anticipating the strike some of the banks , particularly SBI and its associates , had ensured that their ATMs ( automated teller machines ) had cash to meet the customer demand"
      },
      "relation": "caused",
      "effect": {
        "span": "to meet the customer demand"
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
        "span": "to help workers deal with financial difficulties"
      },
      "relation": "caused",
      "effect": {
        "span": "The company had further offered a once-off hardship allowance of R2000"
      }
    },
    {
      "cause": {
        "span": "the no-work , no-pay principle in place while they were striking"
      },
      "relation": "caused",
      "effect": {
        "span": "financial difficulties"
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

### --- id=513 ---

输入文本: A series of blasts took place Sunday before Modi was to address the BJP rally , leaving six dead and over 80 injured .

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
      "cause": "A series of blasts took place Sunday",
      "effect": "leaving six dead and over 80 injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "A series of blasts took place Sunday before Modi was to address the BJP rally"
      },
      "relation": "caused",
      "effect": {
        "span": "leaving six dead and over 80 injured"
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
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

### --- id=259 ---

输入文本: On Tuesday night tens of thousands of demonstrators packed the city ’ s downtown area for a third night as protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight .

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
        "span": "protest leaders warned they would step up their actions"
      },
      "relation": "caused",
      "effect": {
        "span": "On Tuesday night tens of thousands of demonstrators packed the city ’ s downtown area for a third night"
      }
    },
    {
      "cause": {
        "span": "Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight"
      },
      "relation": "caused",
      "effect": {
        "span": "protest leaders warned they would step up their actions"
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
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
        "span": "outstation students today making a slew of demands , including shifting the institute out of Kashmir and action against the policemen involved in lathicharge yesterday"
      },
      "relation": "caused",
      "effect": {
        "span": "Tension prevailed at NIT here"
      }
    },
    {
      "cause": {
        "span": "an HRD team rushed here from Delhi to resolve the crisis being witnessed since last six days"
      },
      "relation": "caused",
      "effect": {
        "span": "outstation students today making a slew of demands , including shifting the institute out of Kashmir and action against the policemen involved in lathicharge yesterday"
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
        "span": "a bandh on Thursday in the Visakha Agency for which the CPI ( Maoist ) gave the call"
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
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
        "span": "a suitably qualified person had been chosen"
      },
      "relation": "caused",
      "effect": {
        "span": "such a person would have foreseen that the demonstration would degenerate into violence and prepared for that eventuality"
      }
    },
    {
      "cause": {
        "span": "the demonstration would degenerate into violence"
      },
      "relation": "caused",
      "effect": {
        "span": "prepared for that eventuality"
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
        "span": "to prevent them from continuing the protest"
      },
      "relation": "caused",
      "effect": {
        "span": "senior officials on Thursday chalked out a strategy"
      }
    },
    {
      "cause": {
        "span": "deploying all the 1,200 KSRP personnel on various duties"
      },
      "relation": "caused",
      "effect": {
        "span": "to prevent them from continuing the protest"
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
        "span": "the Centre on Wednesday gave hint of enacting a tactical retreat from Naxal strongholds like Dantewada and Narayanpur in Chhattisgarh , camouflaging it as ‘ revisiting deployment ’ '"
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
        "span": "provided the much-needed shot in the arm to him to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP"
      }
    },
    {
      "cause": {
        "span": "to take on the state 's ruling Janata Dal-United ( JD-U ) and its ally , the BJP"
      },
      "relation": "caused",
      "effect": {
        "span": "provided the much-needed shot in the arm to him"
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
        "span": "2 K form human chain"
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
      "relation": "caused",
      "effect": {
        "span": "the residents staged a demonstration on Tuesday"
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
        "span": "the deaths of 192 people , mostly Han , in Xinjiang 's capital Urumqi , last week , and the injuries suffered by 1,680 people during clashes between the province 's Uygur Muslim minority and Han Chinese"
      },
      "relation": "caused",
      "effect": {
        "span": "Anger about the policy among Han Chinese , by far the largest group among China 's 56 ethnic communities , has been exacerbated"
      }
    },
    {
      "cause": {
        "span": "clashes between the province 's Uygur Muslim minority and Han Chinese"
      },
      "relation": "caused",
      "effect": {
        "span": "the injuries suffered by 1,680 people"
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
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
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
        "span": "protest against the murder"
      },
      "relation": "caused",
      "effect": {
        "span": "a large number of people who had blocked road near Mahabir bridge"
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "the ongoing plantation workers ’ stir affects 3.5 lakh of plantation workers across the state",
      "effect": "was a serious social issue"
    }
  ],
  "pred_triples": []
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
        "span": "left commuters stranded in Johannesburg"
      },
      "relation": "caused",
      "effect": {
        "span": "also disrupt matric pupils writing exams on Monday"
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
        "span": "Congress leaders on Thursday gave a clarion call to party workers and supporters to dethrone Naveen Patnaik Government in the 2014 general elections"
      }
    },
    {
      "cause": {
        "span": "to dethrone Naveen Patnaik Government in the 2014 general elections"
      },
      "relation": "caused",
      "effect": {
        "span": "Congress leaders on Thursday gave a clarion call to party workers and supporters"
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
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "four suspects appeared on charges of murdering a Victoria Hospital tutor last year"
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
        "span": "20 others , including two Additional SPs , were injured"
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
        "span": "rasta roko by students who were literally dragged away by police and SRP personnel and whisked away to Azad Maidan police station in police vans"
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
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "against water shortage in Mumbai India Thursday",
      "effect": "A boy holding an empty bucket participates along with others in a protest"
    }
  ],
  "pred_triples": []
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
        "span": "to investigate the circumstances of the police firing on agitating farmers on January 12"
      },
      "relation": "caused",
      "effect": {
        "span": "An Indian people 's tribunal to be presided over by former Bombay High Court judge B N Deshmukh will reach Multai in Betul district on April 8"
      }
    },
    {
      "cause": {
        "span": "the police firing on agitating farmers on January 12"
      },
      "relation": "caused",
      "effect": {
        "span": "the death of 19 persons"
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
        "span": "the education authorities conducted the meet on Friday afternoon"
      },
      "relation": "caused",
      "effect": {
        "span": "physical education students and teachers staged a protest by sitting on the tracks at the meet grounds"
      }
    }
  ]
}
```

### --- id=1947 ---

输入文本: Rebels have also planted landmines on the way to these places so as to target the security forces if they go to remove these effigies , " police sources said .

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
      "cause": "to target the security forces if they go to remove these effigies",
      "effect": "Rebels have also planted landmines on the way to these places"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they go to remove these effigies"
      },
      "relation": "caused",
      "effect": {
        "span": "Rebels have also planted landmines on the way to these places so as to target the security forces"
      }
    },
    {
      "cause": {
        "span": "to target the security forces"
      },
      "relation": "caused",
      "effect": {
        "span": "Rebels have also planted landmines on the way to these places"
      }
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
      "relation": "caused",
      "effect": {
        "span": "Vijaykumar , Assistant Director of the Agriculture Department , who rushed to the spot"
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
        "span": "against the alleged assault on Tasni Banu , a woman BPO employee of the Infopark in Kochi a few days ago"
      },
      "relation": "caused",
      "effect": {
        "span": "Dozens of people , including women , took out a ‘ Freedom Walk ' through the main thoroughfare of the city on Thursday midnight in protest"
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
        "span": "the Democratic Alliance showed support for the subsidy by marching to Cosatu 's headquarters in Johannesburg"
      },
      "relation": "caused",
      "effect": {
        "span": "Violence erupted on Tuesday"
      }
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
        "span": "protests from residents"
      },
      "relation": "caused",
      "effect": {
        "span": "The lift station in Keelkattalai was proposed to be built on Arulmurugan Main Road , but was dropped"
      }
    },
    {
      "cause": {
        "span": "it involved filling up of an abandoned well"
      },
      "relation": "caused",
      "effect": {
        "span": "protests from residents"
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
        "span": "to protest about the murders"
      },
      "relation": "caused",
      "effect": {
        "span": "Earlier , residents gathered outside the police station"
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

### --- id=3052 ---

输入文本: Month-long escalating protests to mark 4th anniversary of Mullivaikkal pogrom

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "to mark 4th anniversary of Mullivaikkal pogrom",
      "effect": "Month-long escalating protests"
    }
  ],
  "pred_triples": []
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
        "span": "following the Muzaffarnagar riots , the state government had received IB alerts on possible communal unrest"
      },
      "relation": "caused",
      "effect": {
        "span": "Party Vice-President Ram Kishore Singh threatened to “ put him ( Modi ) behind bars ”"
      }
    }
  ]
}
```

### --- id=850 ---

输入文本: The SAHRC investigated Tatane 's death , during a protest in Ficksburg in April 2011 , followed a complaint by the Council for the Advancement of the SA Constitution .

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
      "cause": "a complaint by the Council for the Advancement of the SA Constitution",
      "effect": "The SAHRC investigated Tatane 's death"
    },
    {
      "cause": "a protest in Ficksburg in April 2011",
      "effect": "Tatane 's death"
    }
  ],
  "pred_triples": []
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

### --- id=1684 ---

输入文本: Terrorist attack on the Pathankot airbase exposed another chink in our media armour .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "Terrorist attack on the Pathankot airbase",
      "effect": "exposed another chink in our media armour"
    }
  ],
  "pred_triples": []
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
        "span": "against atrocities on May 9"
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
        "span": "sparking off violence and vandalism , with several vehicles and buses burnt"
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
        "span": "against the Centre 's failure to contain prices of essential commodities and also against the land scams reported in the State"
      },
      "relation": "caused",
      "effect": {
        "span": "A large number of CPI activists took out a procession in protest"
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

### --- id=1989 ---

输入文本: — | Photo Credit : Photo : Vipin Chandran Staff Reporter KSRTC operates 64 additional services KOCHI : Private buses kept off the road on the first day of the indefinite strike called by trade unions demanding fair wages fixed by the State government .

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
      "cause": "the indefinite strike called by trade unions",
      "effect": "Private buses kept off the road on the first day"
    },
    {
      "cause": "demanding fair wages fixed by the State government",
      "effect": "the indefinite strike called by trade unions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding fair wages fixed by the State government"
      },
      "relation": "caused",
      "effect": {
        "span": "the indefinite strike called by trade unions"
      }
    }
  ]
}
```

### --- id=3051 ---

输入文本: 13th April 2013 08:05 AM The Students Struggle Committee for Tamil Eelam has announced that it would organise demonstrations and public meetings across the State from April 15 to May 19 , to mark the fourth anniversary of the Mullivaikkal massacre and the end of the civil war in Sri Lanka .

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
      "cause": "to mark the fourth anniversary of the Mullivaikkal massacre and the end of the civil war in Sri Lanka",
      "effect": "The Students Struggle Committee for Tamil Eelam has announced that it would organise demonstrations and public meetings across the State from April 15 to May 19"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to mark the fourth anniversary of the Mullivaikkal massacre and the end of the civil war in Sri Lanka"
      },
      "relation": "caused",
      "effect": {
        "span": "it would organise demonstrations and public meetings across the State from April 15 to May 19"
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

### --- id=315 ---

输入文本: Meanwhile , the four-day bandh call given by Maoists in Malkangiri and adjoining Koraput district demanding halt to police action and alleged atrocity against tribals had entered the third today affecting normal life in Maoist hinterlands including Padia , Kalimela and Motu areas .

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
      "cause": "demanding halt to police action and alleged atrocity against tribals",
      "effect": "the four-day bandh call given by Maoists in Malkangiri and adjoining Koraput district"
    },
    {
      "cause": "the four-day bandh call given by Maoists in Malkangiri and adjoining Koraput district demanding halt to police action and alleged atrocity against tribals had entered the third today",
      "effect": "affecting normal life in Maoist hinterlands including Padia , Kalimela and Motu areas"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding halt to police action and alleged atrocity against tribals"
      },
      "relation": "caused",
      "effect": {
        "span": "the four-day bandh call given by Maoists in Malkangiri and adjoining Koraput district"
      }
    },
    {
      "cause": {
        "span": "the four-day bandh call given by Maoists in Malkangiri and adjoining Koraput district"
      },
      "relation": "caused",
      "effect": {
        "span": "affecting normal life in Maoist hinterlands including Padia , Kalimela and Motu areas"
      }
    }
  ]
}
```

### --- id=847 ---

输入文本: Earlier , in a letter to the HRD ministry through NIT administration , the students had demanded hoisting of national flag , action against staff involved in anti-national activities and replacing Jammu and Kashmir Police by CRPF for security of the NIT campus , which has been gripped by tension following clashes in the wake of India 's loss to West Indies in the World T 20 Cup .

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
  "pred_triples": []
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
      "cause": "being beaten up at a market area in Lajpar Nagar here",
      "effect": "Nido Taniam , son of Arunachal Pradesh Congress legislator Nido Pavitra died on Thursday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Nido Taniam , son of Arunachal Pradesh Congress legislator Nido Pavitra died on Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "Sparks Protest"
      }
    },
    {
      "cause": {
        "span": "being beaten up at a market area in Lajpar Nagar here"
      },
      "relation": "caused",
      "effect": {
        "span": "Nido Taniam , son of Arunachal Pradesh Congress legislator Nido Pavitra died on Thursday"
      }
    }
  ]
}
```

### --- id=1607 ---

输入文本: Since two passenger trains were cancelled , engaging of private vehicles were restricted and each vehicle was thoroughly checked at all check-posts along the National Highway -7 many activists decided to give the march a miss .

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
      "cause": "two passenger trains were cancelled , engaging of private vehicles were restricted and each vehicle was thoroughly checked at all check-posts along the National Highway -7",
      "effect": "many activists decided to give the march a miss"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "two passenger trains were cancelled"
      },
      "relation": "caused",
      "effect": {
        "span": "engaging of private vehicles were restricted and each vehicle was thoroughly checked at all check-posts along the National Highway -7"
      }
    },
    {
      "cause": {
        "span": "engaging of private vehicles were restricted and each vehicle was thoroughly checked at all check-posts along the National Highway -7"
      },
      "relation": "caused",
      "effect": {
        "span": "many activists decided to give the march a miss"
      }
    }
  ]
}
```

### --- id=1457 ---

输入文本: Kopane handed over a memorandum to the municipality demanding answers as to why Matlakeng residents were struggling to access water daily .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "demanding answers as to why Matlakeng residents were struggling to access water daily",
      "effect": "Kopane handed over a memorandum to the municipality"
    }
  ],
  "pred_triples": []
}
```

### --- id=504 ---

输入文本: Two civilians also received gun shot wounds in the firing .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
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
      "effect": "Two civilians also received gun shot wounds"
    }
  ],
  "pred_triples": []
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

### --- id=902 ---

输入文本: The memorandum given to Chief Minister Harish Rawat , on Saturday , read : “ The stone crushers working in the area will [ be the cause of dust and health problems which will ] result in migration of the population … here most of the people are completely dependent on the earnings from the agricultural produce [ and the dust from the stone crushers would destroy agriculture ] . ”

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
      "cause": "The stone crushers working in the area",
      "effect": "dust and health problems"
    },
    {
      "cause": "dust and health problems",
      "effect": "migration of the population"
    },
    {
      "cause": "the dust from the stone crushers",
      "effect": "would destroy agriculture"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The stone crushers working in the area"
      },
      "relation": "caused",
      "effect": {
        "span": "dust and health problems which will ] result in migration of the population"
      }
    },
    {
      "cause": {
        "span": "dust and health problems which will ] result in migration of the population"
      },
      "relation": "caused",
      "effect": {
        "span": "migration of the population"
      }
    },
    {
      "cause": {
        "span": "the dust from the stone crushers"
      },
      "relation": "caused",
      "effect": {
        "span": "would destroy agriculture"
      }
    }
  ]
}
```

### --- id=1184 ---

输入文本: Visakhapatnam Harbour and Port Workers ’ Union honorary president V.V. Rama Rao hoisted the flag at the Three Horse Junction and called for unity among the trade unions to raise voice against privatisation policy .

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
      "cause": "to raise voice against privatisation policy",
      "effect": "Visakhapatnam Harbour and Port Workers ’ Union honorary president V.V. Rama Rao hoisted the flag at the Three Horse Junction and called for unity among the trade unions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to raise voice against privatisation policy"
      },
      "relation": "caused",
      "effect": {
        "span": "called for unity among the trade unions"
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
    "tp": 0,
    "fp": 2,
    "fn": 5
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 5
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
        "span": "the incident happened on Sunday night when the 21 - year-old Tanzanian student went through the ordeal in vigilante justice by an angry mob in a case of \" mistaken identity \" after a woman was mowed down by a car driven by a Sudanese here"
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
      "cause": "to extend support in giving a \" befitting farewell \" to the brave son of the soil , 23 - year-old Capt Pawan Kumar",
      "effect": "The Army today appealed to the people of Haryana"
    },
    {
      "cause": "fighting militants in Pulwama district of Jammu and Kashmir",
      "effect": "23 - year-old Capt Pawan Kumar , who died"
    }
  ],
  "pred_triples": []
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
        "span": "in protest against erratic supply of drinking water at Kelamagalam in Udhanapalli on Wednesday"
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
    },
    {
      "cause": {
        "span": "we will intensify our protest in the city in coming days"
      },
      "relation": "caused",
      "effect": {
        "span": "to stop the screening"
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
    },
    {
      "cause": {
        "span": "seeking public intervention against ‘ police-goonda ’ attack on employees"
      },
      "relation": "caused",
      "effect": {
        "span": "the Kerala State Road Transport Employees Association ( KSRTEA ) pasted stickers on KSRTC buses"
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

### --- id=80 ---

输入文本: At least five more people will be tried over the attack , Xinhua has reported .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
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
        "span": "At least five more people will be tried"
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
      "cause": "the killing of a Congolese man in the national capital",
      "effect": "a diplomatic row and instigated violence against Indians in Congo"
    },
    {
      "cause": "the killing of a Congolese man in the national capital",
      "effect": "four attacks on African nationals by the residents in Chattarpur"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the killing of a Congolese man in the national capital"
      },
      "relation": "caused",
      "effect": {
        "span": "that stirred a diplomatic row and instigated violence against Indians in Congo"
      }
    },
    {
      "cause": {
        "span": "that stirred a diplomatic row and instigated violence against Indians in Congo"
      },
      "relation": "caused",
      "effect": {
        "span": "four attacks on African nationals by the residents in Chattarpur were reported on Friday"
      }
    }
  ]
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
        "span": "On getting the news about Mr. Hazare breaking his fast"
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
        "span": "West Police Station PSI Agni allegedly assaulted a lorry driver and brandished his service revolver at the agitators during a protest by the lorry owners ’ association here"
      },
      "relation": "caused",
      "effect": {
        "span": "The ongoing agitation against the Centre ’ s decision to set up the state ’ s first IIT at Dharwad took an ugly turn on Thursday"
      }
    },
    {
      "cause": {
        "span": "a protest by the lorry owners ’ association here"
      },
      "relation": "caused",
      "effect": {
        "span": "West Police Station PSI Agni allegedly assaulted a lorry driver and brandished his service revolver at the agitators"
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
      "cause": "Accusing the CPM of instigating the violence",
      "effect": "she said the deaths were result of clashes between the Congress and the Marxists"
    },
    {
      "cause": "were result of clashes between the Congress and the Marxists",
      "effect": "the deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "clashes between the Congress and the Marxists"
      },
      "relation": "caused",
      "effect": {
        "span": "the deaths"
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

### --- id=1986 ---

输入文本: The rally culminated in a public meeting where senior Congress leaders held the BJD government responsible for the spate of farmer suicides in the State since September .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "senior Congress leaders held the BJD government responsible for the spate of farmer suicides in the State since September"
      },
      "relation": "caused",
      "effect": {
        "span": "The rally culminated in a public meeting"
      }
    }
  ]
}
```
