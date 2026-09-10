# politicause_validation first 300 eval report

## 配置
```json
{
  "label": "politicause_validation first 300",
  "model": "google/gemma-4-31b-qat",
  "dataset": "politicause_validation",
  "sample_count": 300,
  "prompt_name": "v8.10_zero_shot",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 1,
  "temperature": 0.0,
  "max_tokens": 8192,
  "output_schema": "standard",
  "primary_metric": "anchor_window",
  "progress_every": 100,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 8192,
  "reasoning_effort": "none",
  "llm_extra_body": {
    "cache_prompt": false
  },
  "api_key_source": "file:deepseek_api.txt",
  "report_detail_limit": 200,
  "report_detail_mode": "errors",
  "report_error_metric": "anchor_window",
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ politicause_validation first 300 final report ================
样本总数: 300
  Gold 含因果: 85 | Pred 含因果: 147
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.740
  Precision: 0.524
  Recall   : 0.906
  F1       : 0.664
  (TP=77, TN=145, FP=70, FN=8)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 300
    Gold triples: 85 | Pred triples: 147
    Precision: 0.238
    Recall   : 0.412
    F1       : 0.302
    (TP=35, FP=112, FN=50)
  [anchor_window] (primary)
    样本数: 300
    Gold triples: 85 | Pred triples: 147
    Precision: 0.299
    Recall   : 0.518
    F1       : 0.379
    (TP=44, FP=103, FN=41)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 77
    Gold triples: 77 | Pred triples: 77
    Precision: 0.455
    Recall   : 0.455
    F1       : 0.455
    (TP=35, FP=42, FN=42)
  [anchor_window] (primary)
    样本数: 77
    Gold triples: 77 | Pred triples: 77
    Precision: 0.571
    Recall   : 0.571
    F1       : 0.571
    (TP=44, FP=33, FN=33)
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

Sample details shown: all 111 wrong samples from 300 total samples.

### --- id=11504 ---

输入文本: It should serve as a clarion call to Member States to work collaboratively, in good faith, toward early reform of the Security Council to effectively respond to the urgent needs and challenges facing the diverse membership of the United Nations.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "work collaboratively, in good faith, toward early reform of the Security Council",
      "effect": "effectively respond to the urgent needs and challenges"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "early reform of the Security Council"
      },
      "relation": "caused",
      "effect": {
        "span": "effectively respond to the urgent needs and challenges facing the diverse membership of the United Nations"
      }
    }
  ]
}
```

### --- id=16035 ---

输入文本: We responded with the same resilience in confronting the tragic war of 2008, which led to the occupation of 20 per cent of our territory by Russia.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "the tragic war of 2008",
      "effect": "which led to the occupation of 20 per cent of our territory by Russia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the tragic war of 2008"
      },
      "relation": "caused",
      "effect": {
        "span": "the occupation of 20 per cent of our territory by Russia"
      }
    }
  ]
}
```

### --- id=16045 ---

输入文本: It should also be very clear that new conflicts should not cause us to forget older ones, for that would be a destructive message and peace is not divisible.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "new conflicts should not cause us to forget older ones"
      },
      "relation": "caused",
      "effect": {
        "span": "that would be a destructive message"
      }
    }
  ]
}
```

### --- id=15671 ---

输入文本: We will support all efforts to promote education, which is the best way to ensure a better future.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "support all efforts to promote education",
      "effect": "ensure a better future"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "promote education"
      },
      "relation": "caused",
      "effect": {
        "span": "ensure a better future"
      }
    }
  ]
}
```

### --- id=14305 ---

输入文本: The Compact aims to manage migration flows through enhanced international cooperation.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "through enhanced international cooperation",
      "effect": "aims to manage migration flows"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "enhanced international cooperation"
      },
      "relation": "caused",
      "effect": {
        "span": "manage migration flows"
      }
    }
  ]
}
```

### --- id=3643 ---

输入文本: The immense challenges demand that, as a global community, we combine our efforts in a sustained and coordinated manner to identify opportunities for effective remedial action.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "combine our efforts in a sustained and coordinated manner",
      "effect": "to identify opportunities for effective remedial action"
    }
  ],
  "pred_triples": []
}
```

### --- id=13153 ---

输入文本: The international community has played a key role in cooperating with the citizens and the Government of Paraguay, helping to preserve the democratic order and civic responsibility without disruptively interfering in internal affairs.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "has played a key role in cooperating with the citizens and the Government of Paraguay",
      "effect": "helping to preserve the democratic order and civic responsibility without disruptively interfering in internal affairs"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cooperating with the citizens and the Government of Paraguay"
      },
      "relation": "caused",
      "effect": {
        "span": "preserve the democratic order and civic responsibility"
      }
    }
  ]
}
```

### --- id=11859 ---

输入文本: Only through a responsible global alliance in which the most powerful respect international law and the Charter of the United Nations will it be possible to counter the impact of other pandemics, imposed by some Powers, which are a threat to peace, international security, independence and the sovereignty of States and self- determination of peoples.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "a responsible global alliance",
      "effect": "it be possible to counter the impact of other pandemics"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a responsible global alliance in which the most powerful respect international law and the Charter of the United Nations"
      },
      "relation": "caused",
      "effect": {
        "span": "counter the impact of other pandemics, imposed by some Powers, which are a threat to peace, international security, independence and the sovereignty of States and self- determination of peoples"
      }
    }
  ]
}
```

### --- id=10751 ---

输入文本: Without unity, the struggle will only drain our energy and will never be won.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Without unity"
      },
      "relation": "caused",
      "effect": {
        "span": "the struggle will only drain our energy and will never be won"
      }
    }
  ]
}
```

### --- id=4711 ---

输入文本: It was the jabs that have got us this far, and the jabs can keep us here too.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the jabs"
      },
      "relation": "caused",
      "effect": {
        "span": "got us this far"
      }
    }
  ]
}
```

### --- id=16904 ---

输入文本: Australia is not only acting in its own interest, but also helping its Pacific island family to reduce illegal fishing, which depletes the fish stocks of Pacific islanders, who rely on them for their jobs, revenue and food security.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "illegal fishing"
      },
      "relation": "caused",
      "effect": {
        "span": "depletes the fish stocks of Pacific islanders"
      }
    }
  ]
}
```

### --- id=1484 ---

输入文本: As a result of the pandemic, our Hub of Hope, the UK’s biggest and most comprehensive mental health signposting tool, witnessed an exceptional increase in demand from people looking for help and support across the UK.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "our Hub of Hope, the UK’s biggest and most comprehensive mental health signposting tool, witnessed an exceptional increase in demand from people looking for help and support across the UK"
      }
    }
  ]
}
```

### --- id=14306 ---

输入文本: Moreover, it reaffirms migrants’ human rights and dignity in order to ensure the protection of their fundamental rights.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "reaffirms migrants’ human rights and dignity",
      "effect": "ensure"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "it reaffirms migrants’ human rights and dignity"
      },
      "relation": "caused",
      "effect": {
        "span": "the protection of their fundamental rights"
      }
    }
  ]
}
```

### --- id=14028 ---

输入文本: That essential feature, which will remain a constant for a long time to come, has neutralized the effects of uninspired and even adventurous attempts to attract Moldova into alliances against others.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "That essential feature"
      },
      "relation": "caused",
      "effect": {
        "span": "neutralized the effects of uninspired and even adventurous attempts to attract Moldova into alliances against others"
      }
    }
  ]
}
```

### --- id=3173 ---

输入文本: We pioneered life-saving treatments, reducing our fatality rate 85 per cent since April.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "pioneered life-saving treatments",
      "effect": "reducing our fatality rate 85 per cent since April."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "We pioneered life-saving treatments"
      },
      "relation": "caused",
      "effect": {
        "span": "reducing our fatality rate 85 per cent since April"
      }
    }
  ]
}
```

### --- id=16580 ---

输入文本: This year our sister nation of Saudi Arabia hosted Gulf, Arab and Islamic summits, in a successful example of coordinating regional and international positions to address the critical security situation in the region.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Saudi Arabia hosted Gulf, Arab and Islamic summits"
      },
      "relation": "caused",
      "effect": {
        "span": "coordinating regional and international positions to address the critical security situation in the region"
      }
    }
  ]
}
```

### --- id=12762 ---

输入文本: As we have all along, we’ve invested early and at risk, before we know for sure if it will come good because from the start, we’ve taken a no regrets attitude to backing vaccines.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "we’ve taken a no regrets attitude to backing vaccines"
      },
      "relation": "caused",
      "effect": {
        "span": "we’ve invested early and at risk"
      }
    }
  ]
}
```

### --- id=5677 ---

输入文本: Trials have already shown that we can help suppress the disease in hospitals, schools and universities by testing large numbers of NHS workers, children, teachers and students.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "testing large numbers of NHS workers, children, teachers and students",
      "effect": "help suppress the disease in hospitals, schools and universities"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "testing large numbers of NHS workers, children, teachers and students"
      },
      "relation": "caused",
      "effect": {
        "span": "suppress the disease in hospitals, schools and universities"
      }
    }
  ]
}
```

### --- id=14909 ---

输入文本: Indeed, Guyana understands well the risks posed by climate change, as we see daily evidence of damage to the coastal zone, frequency of flooding in the hinterland areas and extreme meteorological events.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "climate change"
      },
      "relation": "caused",
      "effect": {
        "span": "damage to the coastal zone, frequency of flooding in the hinterland areas and extreme meteorological events"
      }
    }
  ]
}
```

### --- id=14081 ---

输入文本: In Iceland, our experience shows that both individuals’ rights and human rights are essential to positive economic and social development.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "both individuals’ rights and human rights"
      },
      "relation": "caused",
      "effect": {
        "span": "positive economic and social development"
      }
    }
  ]
}
```

### --- id=946 ---

输入文本: We need everyone to take action to stop the spread.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "take action",
      "effect": "stop the spread"
    }
  ],
  "pred_triples": []
}
```

### --- id=13805 ---

输入文本: In our opinion, they can be overcome if we harness political will and our efforts is properly organized.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "we harness political will and our efforts is properly organized"
      },
      "relation": "caused",
      "effect": {
        "span": "they can be overcome"
      }
    }
  ]
}
```

### --- id=3488 ---

输入文本: In fact, during the 2018-2020 period, we invested around 1.5 billion US dollars in the health sector to support the implementation of Universal Health Coverage.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "invested around 1.5 billion US dollars in the health sector",
      "effect": "support the implementation of Universal Health Coverage."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "we invested around 1.5 billion US dollars in the health sector"
      },
      "relation": "caused",
      "effect": {
        "span": "support the implementation of Universal Health Coverage"
      }
    }
  ]
}
```

### --- id=3616 ---

输入文本: Subsequently, additional measures were implemented to the approach to safeguarding the population.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "additional measures were implemented to the approach",
      "effect": "to safeguarding the population."
    }
  ],
  "pred_triples": []
}
```

### --- id=9698 ---

输入文本: As Micronesia is addressing the existential threat of climate change, we want to point out that it is impossible to tackle it without protecting the ocean, the world’s largest carbon sink.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "protecting the ocean, the world’s largest carbon sink"
      },
      "relation": "caused",
      "effect": {
        "span": "tackle it"
      }
    }
  ]
}
```

### --- id=14471 ---

输入文本: We must avoid any incident liable to trigger ever worse consequences.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "any incident"
      },
      "relation": "caused",
      "effect": {
        "span": "ever worse consequences"
      }
    }
  ]
}
```

### --- id=7041 ---

输入文本: In him, we saw a son who ensured the old and vulnerable people were protected from the infection.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "a son who ensured"
      },
      "relation": "caused",
      "effect": {
        "span": "the old and vulnerable people were protected from the infection"
      }
    }
  ]
}
```

### --- id=15621 ---

输入文本: For example, thanks to joint work with habitat countries and international organizations, we have succeeded in preventing the extinction of an animal as noble as the snow leopard.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "joint work with habitat countries and international organizations",
      "effect": "succeeded in preventing the extinction"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "joint work with habitat countries and international organizations"
      },
      "relation": "caused",
      "effect": {
        "span": "preventing the extinction of an animal as noble as the snow leopard"
      }
    }
  ]
}
```

### --- id=13856 ---

输入文本: Immense progress has been made towards macroeconomic and fiscal stabilization as well as high-impact projects that pave the way for private-sector-led growth.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "macroeconomic and fiscal stabilization as well as high-impact projects",
      "effect": "pave the way for private-sector-led growth"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "high-impact projects"
      },
      "relation": "caused",
      "effect": {
        "span": "pave the way for private-sector-led growth"
      }
    }
  ]
}
```

### --- id=5651 ---

输入文本: So, when the call comes, please do get a jab and, in the meantime, stay at home, protect the NHS and save lives.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "stay at home",
      "effect": "protect the NHS and save"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "stay at home, protect the NHS"
      },
      "relation": "caused",
      "effect": {
        "span": "save lives"
      }
    }
  ]
}
```

### --- id=6060 ---

输入文本: In order to meet the challenges of the modern age, the United Nations and the Security Council must show willingness to change and implement long-overdue reforms.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "show willingness to change and implement long-overdue reforms",
      "effect": "meet the challenges of the modern age"
    }
  ],
  "pred_triples": []
}
```

### --- id=17052 ---

输入文本: In his words: To save the Pacific is to save the whole planet. In fact, 7 of the 15 most climate-affected nations in the world sit within the Pacific region, including places like Tuvalu, with a population of just over 11,000 people, which barely contributes to global emissions but is paying the price for our collective inaction; atolls so low-lying that in weather events the water on either side of them can flow together and join at the narrowest points, engulfed by the sea; or Tokelau, a beautiful set of three atolls that can only be accessed by boat, where the children speak knowledgeably about climate change, knowing that unlike all the challenges their self-reliant forbears have ever faced, this one is completely and utterly in other people’s hands.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "our collective inaction"
      },
      "relation": "caused",
      "effect": {
        "span": "paying the price"
      }
    }
  ]
}
```

### --- id=11590 ---

输入文本: But I urge everyone to exercise the greatest caution because the choices we each make in the coming days will have a material effect on the road ahead.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "choices we each make in the coming days",
      "effect": "have a material effect on the road ahead"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the choices we each make in the coming days"
      },
      "relation": "caused",
      "effect": {
        "span": "a material effect on the road ahead"
      }
    }
  ]
}
```

### --- id=8813 ---

输入文本: However, staying at home and avoiding contact with others is still the most effective way to avoid passing on COVID-19 if you are infected.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "staying at home and avoiding contact with others"
      },
      "relation": "caused",
      "effect": {
        "span": "avoid passing on COVID-19"
      }
    }
  ]
}
```

### --- id=12660 ---

输入文本: These climatic conditions affect livelihoods by impeding food production.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "by impeding food production",
      "effect": "affect livelihoods"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "These climatic conditions"
      },
      "relation": "caused",
      "effect": {
        "span": "affect livelihoods by impeding food production"
      }
    }
  ]
}
```

### --- id=4641 ---

输入文本: The government has confirmed today that Richard Meddings will be the new Chair of NHS England, following a fair and open competition.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "a fair and open competition"
      },
      "relation": "caused",
      "effect": {
        "span": "Richard Meddings will be the new Chair of NHS England"
      }
    }
  ]
}
```

### --- id=12432 ---

输入文本: We must devise innovative and creative ways by which the world should act to avert the catastrophe that climate change so plainly portends.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "innovative and creative ways by which the world should act"
      },
      "relation": "caused",
      "effect": {
        "span": "avert the catastrophe that climate change so plainly portends"
      }
    }
  ]
}
```

### --- id=14229 ---

输入文本: By his spirit we entered the world so as to never give space to the Santander and oligarchic betrayal of the free peoples of the great homeland.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "By his spirit we entered the world"
      },
      "relation": "caused",
      "effect": {
        "span": "never give space to the Santander and oligarchic betrayal of the free peoples of the great homeland"
      }
    }
  ]
}
```

### --- id=8810 ---

输入文本: With the publication of the Living with COVID plan, the government has ended legal restrictions in England and is instead asking the public to practice specific safe and responsible behaviours as the primary means of stopping the spread of the virus.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "asking the public to practice specific safe and responsible behaviours"
      },
      "relation": "caused",
      "effect": {
        "span": "stopping the spread of the virus"
      }
    }
  ]
}
```

### --- id=17394 ---

输入文本: We are convinced that we can make the Organization’s functioning more efficient and flexible only through such essential reorganization efforts.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "only through such essential reorganization efforts",
      "effect": "we can make the Organization’s functioning more efficient and flexible"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "such essential reorganization efforts"
      },
      "relation": "caused",
      "effect": {
        "span": "make the Organization’s functioning more efficient and flexible"
      }
    }
  ]
}
```

### --- id=12540 ---

输入文本: There are also new and emerging threats: Cyber warfare and the risk of failing technological governance, bioterrorism, new geopolitical tensions due to an increasingly polycentric global system and climate change as the potential future super-crisis.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "l system and c",
      "effect": "eopolitical tensions due t"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an increasingly polycentric global system"
      },
      "relation": "caused",
      "effect": {
        "span": "new geopolitical tensions"
      }
    }
  ]
}
```

### --- id=1246 ---

输入文本: Omicron continues to grow faster than Delta, with an increased risk of transmission, particularly in contacts outside of the household.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Omicron continues to grow faster than Delta"
      },
      "relation": "caused",
      "effect": {
        "span": "an increased risk of transmission"
      }
    }
  ]
}
```

### --- id=2699 ---

输入文本: Samoa is confident that despite all the challenges, even existential threats for some of us; there is still hope if there is Unity amongst our UN family.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Unity amongst our UN family"
      },
      "relation": "caused",
      "effect": {
        "span": "there is still hope"
      }
    }
  ]
}
```

### --- id=12853 ---

输入文本: (spoke in Russian) That could lead to the collapse of the entire architecture of international relations.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "(spoke in Russian)"
      },
      "relation": "caused",
      "effect": {
        "span": "the collapse of the entire architecture of international relations"
      }
    }
  ]
}
```

### --- id=6493 ---

输入文本: The theme chosen for the current session reflects the unique and difficult context which all the countries in the world have been living through since 2019, on account of the coronavirus disease (COVID-19) pandemic.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "coronavirus disease (COVID-19) pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "the unique and difficult context which all the countries in the world have been living through since 2019"
      }
    }
  ]
}
```

### --- id=3198 ---

输入文本: Given the magnitude and impact of COVID-19 and other persistent disease burdens, we aim to invest in our health and other service delivery systems, and in a sustained and robust post COVID-19 recovery process.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the magnitude and impact of COVID-19 and other persistent disease burdens"
      },
      "relation": "caused",
      "effect": {
        "span": "we aim to invest in our health and other service delivery systems, and in a sustained and robust post COVID-19 recovery process"
      }
    }
  ]
}
```

### --- id=16302 ---

输入文本: We are providing better access to health care, plus free medicine for low-income earners, and entering into public-private partnerships to improve our hospitals.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "entering into public-private partnerships"
      },
      "relation": "caused",
      "effect": {
        "span": "improve our hospitals"
      }
    }
  ]
}
```

### --- id=7241 ---

输入文本: Pakistan and the United States trained Mujahideen groups to fight for the liberation of Afghanistan.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Pakistan and the United States trained Mujahideen groups"
      },
      "relation": "caused",
      "effect": {
        "span": "fight for the liberation of Afghanistan"
      }
    }
  ]
}
```

### --- id=16373 ---

输入文本: As the Security Council remains paralysed in critical situations, the threat of the use of nuclear weapons continues to haunt us.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the Security Council remains paralysed in critical situations"
      },
      "relation": "caused",
      "effect": {
        "span": "the threat of the use of nuclear weapons continues to haunt us"
      }
    }
  ]
}
```

### --- id=16355 ---

输入文本: We must take concerted measures over the next 10 years to foster stronger partnerships at the national, regional and, of course, global levels and ensure that no one is left behind as we guide our countries towards the 2030 milestone.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "take concerted measures over the next 10 years to foster stronger partnerships at the national, regional and, of course, global levels"
      },
      "relation": "caused",
      "effect": {
        "span": "ensure that no one is left behind as we guide our countries towards the 2030 milestone"
      }
    }
  ]
}
```

### --- id=3864 ---

输入文本: This will help break chains of transmission.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
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
        "span": "break chains of transmission"
      }
    }
  ]
}
```

### --- id=9918 ---

输入文本: Only when such commitment is guaranteed can we enter a new, brighter chapter in the history of humankind — a chapter of cooperation and dialogue; a chapter of sustainable peace and development.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "such commitment is guaranteed"
      },
      "relation": "caused",
      "effect": {
        "span": "we enter a new, brighter chapter in the history of humankind — a chapter of cooperation and dialogue; a chapter of sustainable peace and development"
      }
    }
  ]
}
```

### --- id=13656 ---

输入文本: Sustainable development is one of the most important pillars of Oman’s vision for the future and consecutive five-year development plans, which are an extension of the values and principles of sustainability as a means of achieving lasting equality, justice and peace in Omani society, as clearly reflected in our basic law.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "values and principles of sustainability"
      },
      "relation": "caused",
      "effect": {
        "span": "achieving lasting equality, justice and peace in Omani society"
      }
    }
  ]
}
```

### --- id=209 ---

输入文本: We are taking precautionary action to protect public health and the progress of our vaccine rollout at a critical moment as we enter winter, and we are monitoring the situation closely.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "taking precautionary action"
      },
      "relation": "caused",
      "effect": {
        "span": "protect public health and the progress of our vaccine rollout"
      }
    }
  ]
}
```

### --- id=13736 ---

输入文本: I call upon our international collaborators to work with the countries of the region to achieve a successful outcome for our wildlife.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "work",
      "effect": "achieve"
    }
  ],
  "pred_triples": []
}
```

### --- id=16750 ---

输入文本: We are open to partnerships, collaboration and ideas about how to continue improving the quality of education, because we believe that our success in a global digital economy in the fourth industrial revolution is predicated on our investment in the future of our children.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "our investment in the future of our children"
      },
      "relation": "caused",
      "effect": {
        "span": "our success in a global digital economy in the fourth industrial revolution"
      }
    }
  ]
}
```

### --- id=3576 ---

输入文本: Mr. President, The pandemic has highlighted pre-existing vulnerabilities and multiple structural weaknesses within our economies - large and small, rich and poor - and clearly demonstrated the systemic nature of risk worldwide.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "The pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "highlighted pre-existing vulnerabilities and multiple structural weaknesses within our economies - large and small, rich and poor - and clearly demonstrated the systemic nature of risk worldwide"
      }
    }
  ]
}
```

### --- id=10824 ---

输入文本: We believe that it is important to prioritize the peaceful resolution of conflicts, by creating the necessary conditions for development in post-conflict environments.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "creating the necessary conditions for development in post-conflict environments",
      "effect": "prioritize the peaceful resolution of conflicts"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "creating the necessary conditions for development in post-conflict environments"
      },
      "relation": "caused",
      "effect": {
        "span": "the peaceful resolution of conflicts"
      }
    }
  ]
}
```

### --- id=7126 ---

输入文本: I am certain that subsequent Governments will be able to do the same or better, which will benefit our generation, our children and their children.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "subsequent Governments will be able to do the same or better"
      },
      "relation": "caused",
      "effect": {
        "span": "will benefit our generation, our children and their children"
      }
    }
  ]
}
```

### --- id=9743 ---

输入文本: It would be a travesty, however, if our maritime zones and our right to them were challenged or reduced because of sea-level rise, to which we are among those who contribute the least.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "sea-level rise"
      },
      "relation": "caused",
      "effect": {
        "span": "our maritime zones and our right to them were challenged or reduced"
      }
    }
  ]
}
```

### --- id=4424 ---

输入文本: Anyone testing positive will need to isolate and take a confirmatory PCR test, at no additional cost to the traveller, which would be genomically sequenced to help identify new variants.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "testing positive"
      },
      "relation": "caused",
      "effect": {
        "span": "will need to isolate and take a confirmatory PCR test"
      }
    }
  ]
}
```

### --- id=13529 ---

输入文本: The success of that project can be guaranteed only by addressing the causes of conflict in the region.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "addressing the causes of conflict",
      "effect": "can be guaranteed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "addressing the causes of conflict in the region"
      },
      "relation": "caused",
      "effect": {
        "span": "The success of that project"
      }
    }
  ]
}
```

### --- id=10489 ---

输入文本: That is why we have taken the decision to implement a plan for a long-term low-emission strategy that will enable us to take the necessary steps to achieve more ambitious targets, such as carbon neutrality by the year 2050.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "taken the decision to implement a plan for a long-term low-emission strategy",
      "effect": "take the necessary steps to achieve more ambitious targets"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "implement a plan for a long-term low-emission strategy"
      },
      "relation": "caused",
      "effect": {
        "span": "take the necessary steps to achieve more ambitious targets, such as carbon neutrality by the year 2050"
      }
    }
  ]
}
```

### --- id=1811 ---

输入文本: When hail or frost strikes, Swiss winegrowers help one another, and they reach out to the insurance companies they have paid into.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "hail or frost strikes"
      },
      "relation": "caused",
      "effect": {
        "span": "Swiss winegrowers help one another, and they reach out to the insurance companies they have paid into"
      }
    }
  ]
}
```

### --- id=14394 ---

输入文本: As a matter of principle, Belarus believes that regional economic organizations must be actively involved as effectively as possible in efforts to implement the SDGs, in order to help coordinate the economic policies of regional blocs’ member States.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "regional economic organizations must be actively involved as effectively as possible in efforts to implement the SDGs"
      },
      "relation": "caused",
      "effect": {
        "span": "help coordinate the economic policies of regional blocs’ member States"
      }
    }
  ]
}
```

### --- id=7236 ---

输入文本: Together with the FAO, we have created the Food Coalition to combat malnutrition caused by the Covid-19 pandemic and we have hosted in Rome the Pre-Summit on Food Systems.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "he Covid-19 pandemic a",
      "effect": "alnutrition c"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Covid-19 pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "malnutrition"
      }
    }
  ]
}
```

### --- id=15900 ---

输入文本: For that reason, the President of Colombia and I, in my capacity as President of Peru, decided to convene a summit on 6 September with six countries of the region to address the challenges of the fires that have affected the Amazon.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the fires that have affected the Amazon"
      },
      "relation": "caused",
      "effect": {
        "span": "the President of Colombia and I, in my capacity as President of Peru, decided to convene a summit on 6 September with six countries of the region to address the challenges"
      }
    }
  ]
}
```

### --- id=13901 ---

输入文本: I therefore again call on our partners in the international community to support us in this process so that it is transparent and credible.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "our partners in the international community to support us in this process"
      },
      "relation": "caused",
      "effect": {
        "span": "it is transparent and credible"
      }
    }
  ]
}
```

### --- id=13361 ---

输入文本: At the same time, we have launched an ambitious public and private investment plan to increase national electricity production, which currently covers only 20 per cent of the demand, with the aim of covering 33 per cent by 2030 and 50 per cent by 2050.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "ambitious public and private investment plan to increase national electricity production"
      },
      "relation": "caused",
      "effect": {
        "span": "covering 33 per cent by 2030 and 50 per cent by 2050"
      }
    }
  ]
}
```

### --- id=3411 ---

输入文本: At the same time, we are struggling against the consequences of our own actions, which are causing the level of carbon in the atmosphere to become unsustainable.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "the consequences of our own actions",
      "effect": "which are causing the level of carbon in the atmosphere to become unsustainable"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "our own actions"
      },
      "relation": "caused",
      "effect": {
        "span": "the level of carbon in the atmosphere to become unsustainable"
      }
    }
  ]
}
```

### --- id=5025 ---

输入文本: The government invested early in Oxford University’s team, supporting their vaccine technology since 2016 and their COVID-19 jabs since March 2020 with more than £88 million to help research, develop and manufacture the vaccine.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "The government invested early in Oxford University’s team, supporting their vaccine technology since 2016 and their COVID-19 jabs since March 2020 with more than £88 million"
      },
      "relation": "caused",
      "effect": {
        "span": "help research, develop and manufacture the vaccine"
      }
    }
  ]
}
```

### --- id=14598 ---

输入文本: I therefore wish to invite my Azerbaijani counterpart, President Ilham Aliyev, to accept the formula that will create the conditions for a breakthrough in the peace process.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the formula"
      },
      "relation": "caused",
      "effect": {
        "span": "will create the conditions for a breakthrough in the peace process"
      }
    }
  ]
}
```

### --- id=12781 ---

输入文本: This session is being held at a time when the international community faces the adverse socioeconomic impact of the COVID-19 pandemic.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the COVID-19 pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "the adverse socioeconomic impact"
      }
    }
  ]
}
```

### --- id=12176 ---

输入文本: But there is another way of using these rapid tests, and that is to follow the example of Liverpool, where in the last two and a half weeks over 200,000 people have taken part in community testing, contributing to a very substantial fall in infections.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "ave taken part in community testing,",
      "effect": "ontributing to a very substantial fall in infections."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "over 200,000 people have taken part in community testing"
      },
      "relation": "caused",
      "effect": {
        "span": "a very substantial fall in infections"
      }
    }
  ]
}
```

### --- id=2971 ---

输入文本: COVID-19 has economically challenged us all and if the Sustainable Development Goals are to ever be realized, the world must recover better, for all, and together.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "Sustainable Development Goals are to ever be realized",
      "effect": "must recover better"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "COVID-19"
      },
      "relation": "caused",
      "effect": {
        "span": "economically challenged us all"
      }
    }
  ]
}
```

### --- id=13972 ---

输入文本: In 2017, 2018 and 2019, in order to properly ensure accountability, my country submitted voluntary reports that take stock of the significant progress we have made in each of the 17 Goals.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "submitted voluntary reports that take stock of the significant progress we have made in each of the 17 Goals",
      "effect": "in order to properly ensure accountability"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "my country submitted voluntary reports that take stock of the significant progress we have made in each of the 17 Goals"
      },
      "relation": "caused",
      "effect": {
        "span": "properly ensure accountability"
      }
    }
  ]
}
```

### --- id=13902 ---

输入文本: Faced with the immediate and lofty task of charting the future of the Union of the Comoros, I decided to work harder than ever to strengthen national unity and social cohesion, without which efforts for harmonious development would be in vain.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "work",
      "effect": "strengthen"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "strengthen national unity and social cohesion"
      },
      "relation": "caused",
      "effect": {
        "span": "harmonious development"
      }
    }
  ]
}
```

### --- id=12846 ---

输入文本: Guided by President El Ghazouani, the Government of the Islamic Republic of Mauritania has adopted many measures that made it possible to limit the spread of the pandemic and mitigate its effects on the population, especially the most vulnerable.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "adopted many measures",
      "effect": "made it possible to limit the spread of the pandemic and mitigate its effects on the population"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Government of the Islamic Republic of Mauritania has adopted many measures"
      },
      "relation": "caused",
      "effect": {
        "span": "limit the spread of the pandemic and mitigate its effects on the population, especially the most vulnerable"
      }
    }
  ]
}
```

### --- id=10557 ---

输入文本: Full and constructive engagement by nuclear-weapon States will be a necessary ingredient if we wish to move forward.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Full and constructive engagement by nuclear-weapon States"
      },
      "relation": "caused",
      "effect": {
        "span": "move forward"
      }
    }
  ]
}
```

### --- id=8652 ---

输入文本: One dose has been found to provide long-lasting protection against this disease for up to 6 months.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "One dose"
      },
      "relation": "caused",
      "effect": {
        "span": "long-lasting protection against this disease for up to 6 months"
      }
    }
  ]
}
```

### --- id=3375 ---

输入文本: 75 years after its creation, we can attest that the United Nations has been able to meet the expectations of its founding fathers in their efforts to save future generations from the scourge of a third world war, promote peace and develop friendly and cooperative relations among nations.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "has been able to meet the expectations of its founding fathers",
      "effect": "save future generations from the scourge of a third world war, promote peace and develop friendly and cooperative relations among nations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the United Nations"
      },
      "relation": "caused",
      "effect": {
        "span": "save future generations from the scourge of a third world war, promote peace and develop friendly and cooperative relations among nations"
      }
    }
  ]
}
```

### --- id=10938 ---

输入文本: In recent years, Prime Minister Netanyahu and I developed the Tracks for Regional Peace initiative, which will connect the Arab Gulf States by rail through Jordan to the Israeli ports in Haifa.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Tracks for Regional Peace initiative"
      },
      "relation": "caused",
      "effect": {
        "span": "will connect the Arab Gulf States by rail through Jordan to the Israeli ports in Haifa"
      }
    }
  ]
}
```

### --- id=5626 ---

输入文本: However, we must take action to suppress the disease.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "take action",
      "effect": "suppress the disease"
    }
  ],
  "pred_triples": []
}
```

### --- id=16718 ---

输入文本: The widespread expansion of international terrorism and extremism in their various manifestations, along with illegal drug and arms trafficking, human trafficking, cross-border crime and the threat of the emergence or escalation of conflicts, requires collective efforts for implementing preventive measures.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "The widespread expansion of international terrorism and extremism in their various manifestations, along with illegal drug and arms trafficking, human trafficking, cross-border crime and the threat of the emergence or escalation of conflicts"
      },
      "relation": "caused",
      "effect": {
        "span": "requires collective efforts for implementing preventive measures"
      }
    }
  ]
}
```

### --- id=5858 ---

输入文本: To ensure complete and lasting peace that begins firmly to take root on the Korean peninsula, Korea remains fully committed to doing its part.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "fully committed to doing its part",
      "effect": "ensure complete and lasting peace that begins firmly to take root"
    }
  ],
  "pred_triples": []
}
```

### --- id=4565 ---

输入文本: This is so that expert scientists can understand more about how to deploy these treatments in the NHS more widely later in the year – including who would benefit most from receiving antiviral treatments for COVID-19.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
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
        "span": "expert scientists can understand more about how to deploy these treatments in the NHS more widely later in the year – including who would benefit most from receiving antiviral treatments for COVID-19"
      }
    }
  ]
}
```

### --- id=15776 ---

输入文本: We need a stronger United Nations to respond more effectively to protracted conflicts and humanitarian crises in the Middle East, sub-Saharan Africa and other regions.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "a stronger United Nations"
      },
      "relation": "caused",
      "effect": {
        "span": "respond more effectively to protracted conflicts and humanitarian crises in the Middle East, sub-Saharan Africa and other regions"
      }
    }
  ]
}
```

### --- id=12969 ---

输入文本: It calls for the strengthening of active solidarity and the will to live together in the strict observance of world cultural diversity with a view to promoting and preserving the interests of everyone, especially the weak.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "strengthening of active solidarity and the will to live together in the strict observance of world cultural diversity"
      },
      "relation": "caused",
      "effect": {
        "span": "promoting and preserving the interests of everyone, especially the weak"
      }
    }
  ]
}
```

### --- id=11374 ---

输入文本: We must work to build a society more aware of the fact that our time on this the planet is fleeting but that the damage we cause can be irreversible.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the damage we cause"
      },
      "relation": "caused",
      "effect": {
        "span": "can be irreversible"
      }
    }
  ]
}
```

### --- id=8871 ---

输入文本: Although this age group is generally at very low risk of serious illness from the virus, a very small number of children who get infected do develop severe disease.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "get infected"
      },
      "relation": "caused",
      "effect": {
        "span": "develop severe disease"
      }
    }
  ]
}
```

### --- id=389 ---

输入文本: You’ve seen on the frontline how COVID-19 has brought with it less visible costs.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "COVID-19"
      },
      "relation": "caused",
      "effect": {
        "span": "less visible costs"
      }
    }
  ]
}
```

### --- id=3692 ---

输入文本:  The Joint Comprehensive Plan of Action with Iran hangs by a thread, which has led to a spiral of toughening positions.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "Joint Comprehensive Plan of Action with Iran hangs by a thread,",
      "effect": "which has led to a spiral of toughening positions."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The Joint Comprehensive Plan of Action with Iran hangs by a thread"
      },
      "relation": "caused",
      "effect": {
        "span": "a spiral of toughening positions"
      }
    }
  ]
}
```

### --- id=5236 ---

输入文本: As friends, families and loved ones gather for the festive season, the public is reminded that vaccines remain the best way to protect people against COVID-19.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "vaccines"
      },
      "relation": "caused",
      "effect": {
        "span": "protect people against COVID-19"
      }
    }
  ]
}
```

### --- id=11661 ---

输入文本: From 10th January, we will provide 100,000 critical workers in England with free lateral flow tests for every working day to help keep essential services running.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "provide 100,000 critical workers in England with free lateral flow tests",
      "effect": "help keep essential services running"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "provide 100,000 critical workers in England with free lateral flow tests for every working day"
      },
      "relation": "caused",
      "effect": {
        "span": "keep essential services running"
      }
    }
  ]
}
```

### --- id=13373 ---

输入文本: Achieving the Sustainable Development Goals would address most of the concerns and aspirations of the vast majority of the world’s inhabitants.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Achieving the Sustainable Development Goals"
      },
      "relation": "caused",
      "effect": {
        "span": "would address most of the concerns and aspirations of the vast majority of the world’s inhabitants"
      }
    }
  ]
}
```

### --- id=12133 ---

输入文本: We’re going to be throwing everything at it, in order to ensure that everyone eligible is offered that booster in just over two months.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "going to be throwing everything at it",
      "effect": "to ensure that everyone eligible is offered that booster in just over two months"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "throwing everything at it"
      },
      "relation": "caused",
      "effect": {
        "span": "everyone eligible is offered that booster in just over two months"
      }
    }
  ]
}
```

### --- id=14764 ---

输入文本: But to be able to benefit from these opportunities made possible by technology, we have to raise our infrastructure to a basic minimum level.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "raise our infrastructure to a basic minimum level"
      },
      "relation": "caused",
      "effect": {
        "span": "be able to benefit from these opportunities made possible by technology"
      }
    }
  ]
}
```

### --- id=5618 ---

输入文本: Again I want to thank the teachers, pupils and parents who have worked so hard to keep schools safe and keep them open.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "worked so hard",
      "effect": "keep schools safe and keep them open"
    }
  ],
  "pred_triples": []
}
```

### --- id=15544 ---

输入文本: Across the African continent, revenues have fallen by as much as $150 billion as economies are still reeling from the impact of the pandemic.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "reeling from the impact of the pandemic",
      "effect": "revenues have fallen by as much as $150 billion"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the impact of the pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "revenues have fallen by as much as $150 billion"
      }
    }
  ]
}
```

### --- id=3673 ---

输入文本: When wheat fields are burned down, oil fields are looted, and the energy sector is targeted, does that really protect civilians or does it deny them access to food, heating, gas, and electricity?

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "wheat fields are burned down, oil fields are looted, and the energy sector is targeted"
      },
      "relation": "caused",
      "effect": {
        "span": "deny them access to food, heating, gas, and electricity"
      }
    }
  ]
}
```

### --- id=13329 ---

输入文本: International energy supplies and maritime navigation in the Arabian Gulf, the Strait of Hormuz and the region as a whole face grave dangers due to the behaviour of the Iranian regime as it repeatedly targets commercial vessels in that region.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "due to the behaviour of the Iranian regime as it repeatedly targets commercial vessels in that region",
      "effect": "face grave dangers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the behaviour of the Iranian regime as it repeatedly targets commercial vessels in that region"
      },
      "relation": "caused",
      "effect": {
        "span": "International energy supplies and maritime navigation in the Arabian Gulf, the Strait of Hormuz and the region as a whole face grave dangers"
      }
    }
  ]
}
```

### --- id=8377 ---

输入文本: However, children under 2 can be at greater risk of severe illness, especially those born prematurely, with a heart condition or who have a chronic lung disease.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "born prematurely, with a heart condition or who have a chronic lung disease"
      },
      "relation": "caused",
      "effect": {
        "span": "children under 2 can be at greater risk of severe illness"
      }
    }
  ]
}
```

### --- id=15117 ---

输入文本: The Government of National Accord is also coordinating with the judiciary to create an environment conducive to its critical and important role, ensuring the principle of impunity and empowering law-enforcement agencies to do their job as required.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "coordinating with the judiciary to create an environment conducive to its critical and important role"
      },
      "relation": "caused",
      "effect": {
        "span": "ensuring the principle of impunity and empowering law-enforcement agencies to do their job as required"
      }
    }
  ]
}
```

### --- id=15575 ---

输入文本: Every year, Grenada reiterates the counterproductivity of the economic, commercial and financial embargo imposed by the United States of America against Cuba and the inhumane socioeconomic hardships it places on the people of the Republic of Cuba, a country that has provided a wealth of humanitarian assistance around the world, including during the onslaught of COVID-19, but is nevertheless hindered from participating in the global economy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "economic, commercial and financial embargo imposed by the United States of America against Cuba"
      },
      "relation": "caused",
      "effect": {
        "span": "inhumane socioeconomic hardships it places on the people of the Republic of Cuba"
      }
    }
  ]
}
```

### --- id=10582 ---

输入文本: Where is the constructive action by the countries responsible for carbon emissions that believe that it is okay to continue to build coal-power plants and not decommission them, and that do not understand that the world is providing us with prospects of new industries and new jobs while enabling us to save the world for our young people?

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "prospects of new industries and new jobs"
      },
      "relation": "caused",
      "effect": {
        "span": "enabling us to save the world for our young people"
      }
    }
  ]
}
```

### --- id=2819 ---

输入文本: However, it has awakened the discourse on how Uganda builds its systems to generate the required resilience to withstand such shocks.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "it"
      },
      "relation": "caused",
      "effect": {
        "span": "awakened the discourse on how Uganda builds its systems to generate the required resilience to withstand such shocks"
      }
    }
  ]
}
```

### --- id=699 ---

输入文本: If you have any symptoms of a respiratory infection, and a high temperature or feel unwell, try to stay at home or away from others – especially elderly or vulnerable people.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "symptoms of a respiratory infection, and a high temperature or feel unwell"
      },
      "relation": "caused",
      "effect": {
        "span": "stay at home or away from others – especially elderly or vulnerable people"
      }
    }
  ]
}
```

### --- id=16817 ---

输入文本: We therefore welcome the Addis Ababa Action Agenda of the Third International Conference on Financing for Development, which remains a key framework for mobilizing financial resources likely to lead to tangible progress in achieving the SDGs.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "mobilizing financial resources"
      },
      "relation": "caused",
      "effect": {
        "span": "tangible progress in achieving the SDGs"
      }
    }
  ]
}
```

### --- id=1299 ---

输入文本: Studies of households and contacts have found that there is a higher risk of transmission to contacts from an Omicron case, when compared to Delta.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "an Omicron case"
      },
      "relation": "caused",
      "effect": {
        "span": "a higher risk of transmission to contacts"
      }
    }
  ]
}
```

### --- id=811 ---

输入文本: Please help reduce transmission by wearing a face covering in crowded or enclosed spaces, washing hands regularly, keeping rooms well ventilated.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "wearing a face covering in crowded or enclosed spaces, washing hands regularly, keeping rooms well ventilated"
      },
      "relation": "caused",
      "effect": {
        "span": "reduce transmission"
      }
    }
  ]
}
```

### --- id=12827 ---

输入文本: The fight against COVID-19 and its new and frightening variants goes on, and our combined efforts, without distinction between rich and poor or based on other types of social categories, are the only way forward for us to fight this pandemic with outcomes that meet our peoples’ expectations of a full return to normal life.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "our combined efforts, without distinction between rich and poor or based on other types of social categories"
      },
      "relation": "caused",
      "effect": {
        "span": "outcomes that meet our peoples’ expectations of a full return to normal life"
      }
    }
  ]
}
```
