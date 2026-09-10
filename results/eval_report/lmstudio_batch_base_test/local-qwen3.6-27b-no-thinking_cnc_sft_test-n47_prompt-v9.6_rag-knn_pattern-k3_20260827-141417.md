# Qwen3.6 27B No Thinking cache_prompt off diagnostic 590-636 eval report

## 配置
```json
{
  "label": "Qwen3.6 27B No Thinking cache_prompt off diagnostic 590-636",
  "model": "local/qwen3.6-27b-no-thinking",
  "dataset": "cnc_sft_test",
  "sample_count": 47,
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
================ Qwen3.6 27B No Thinking cache_prompt off diagnostic 590-636 final report ================
样本总数: 47
  Gold 含因果: 25 | Pred 含因果: 26
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.809
  Precision: 0.808
  Recall   : 0.840
  F1       : 0.824
  (TP=21, TN=17, FP=5, FN=4)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 47
    Gold triples: 32 | Pred triples: 31
    Precision: 0.710
    Recall   : 0.688
    F1       : 0.698
    (TP=22, FP=9, FN=10)
  [anchor_window]
    样本数: 47
    Gold triples: 32 | Pred triples: 31
    Precision: 0.677
    Recall   : 0.656
    F1       : 0.667
    (TP=21, FP=10, FN=11)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 21
    Gold triples: 28 | Pred triples: 26
    Precision: 0.846
    Recall   : 0.786
    F1       : 0.815
    (TP=22, FP=4, FN=6)
  [anchor_window]
    样本数: 21
    Gold triples: 28 | Pred triples: 26
    Precision: 0.808
    Recall   : 0.750
    F1       : 0.778
    (TP=21, FP=5, FN=7)
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

Sample details shown: all 14 wrong samples from 47 total samples.

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
