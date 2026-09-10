# politicause_validation first 300 eval report

## 配置
```json
{
  "label": "politicause_validation first 300",
  "model": "google/gemma-4-31b-qat",
  "dataset": "politicause_validation",
  "sample_count": 300,
  "prompt_name": "v8.9",
  "use_rag": true,
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
  Gold 含因果: 80 | Pred 含因果: 158
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.733
  Precision: 0.500
  Recall   : 0.988
  F1       : 0.664
  (TP=79, TN=141, FP=79, FN=1)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 300
    Gold triples: 105 | Pred triples: 193
    Precision: 0.197
    Recall   : 0.362
    F1       : 0.255
    (TP=38, FP=155, FN=67)
  [anchor_window] (primary)
    样本数: 300
    Gold triples: 105 | Pred triples: 193
    Precision: 0.269
    Recall   : 0.495
    F1       : 0.349
    (TP=52, FP=141, FN=53)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 79
    Gold triples: 104 | Pred triples: 100
    Precision: 0.380
    Recall   : 0.365
    F1       : 0.373
    (TP=38, FP=62, FN=66)
  [anchor_window] (primary)
    样本数: 79
    Gold triples: 104 | Pred triples: 100
    Precision: 0.520
    Recall   : 0.500
    F1       : 0.510
    (TP=52, FP=48, FN=52)
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

Sample details shown: all 122 wrong samples from 300 total samples.

### --- id=16270 ---

输入文本: Previous generations fought each other to uphold their own interests, but now the world must unite around our common interests to fight a more powerful enemy — a monster we created ourselves, a heating planet staggering under the excesses of all who have taken its resilience for granted.

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
        "span": "the excesses of all who have taken its resilience for granted"
      },
      "relation": "caused",
      "effect": {
        "span": "a heating planet staggering"
      }
    }
  ]
}
```

### --- id=13302 ---

输入文本: The launch in April of our Extended Monaco programme has put us on the road to a digital transition of unprecedented scale, while giving particular emphasis to the concepts of responsibility and sustainability.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "Extended Monaco programme",
      "effect": "put us on the road to a digital transition"
    },
    {
      "cause": "Extended Monaco programme",
      "effect": "giving particular emphasis to the concepts of responsibility and sustainability"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The launch in April of our Extended Monaco programme"
      },
      "relation": "caused",
      "effect": {
        "span": "has put us on the road to a digital transition of unprecedented scale"
      }
    }
  ]
}
```

### --- id=14752 ---

输入文本: According to that report, Africa is losing more than $50 billion annually through illicit financial outflows.

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
      "cause": "illicit financial outflows",
      "effect": "is losing"
    }
  ],
  "pred_triples": []
}
```

### --- id=3027 ---

输入文本: Increasingly frequent regional and local, but also international conflicts, with historical, political and economic causes and consequences, threaten to destabilize the international order and the world as we know it.

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
      "cause": "regional and local, but also international conflicts,",
      "effect": "threaten to destabilize the international order and the world as we know it"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Increasingly frequent regional and local, but also international conflicts"
      },
      "relation": "caused",
      "effect": {
        "span": "destabilize the international order and the world as we know it"
      }
    }
  ]
}
```

### --- id=15340 ---

输入文本: The resolution, in addition to the 29 other resolutions of its kind adopted since 1992, emphasizes the need to end the embargo, the already-disastrous socioeconomic and health consequences of which have been aggravated by the COVID-19 pandemic.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "the embargo"
      },
      "relation": "caused",
      "effect": {
        "span": "the already-disastrous socioeconomic and health consequences"
      }
    },
    {
      "cause": {
        "span": "the COVID-19 pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "aggravated"
      }
    }
  ]
}
```

### --- id=7302 ---

输入文本: Together with the Prime Minister of Spain, I have launched a network of leaders to support the Secretary-General in taking the Common Agenda forward.

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
        "span": "launched a network of leaders"
      },
      "relation": "caused",
      "effect": {
        "span": "support the Secretary-General in taking the Common Agenda forward"
      }
    }
  ]
}
```

### --- id=6082 ---

输入文本: We support the calls to strengthen the General Assembly and to reform the Security Council in order to make it more representative, more effective and more accountable to all Member States.

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
      "cause": "strengthen the General Assembly and to reform the Security Council",
      "effect": "make it more representative, more effective and more accountable"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "reform the Security Council"
      },
      "relation": "caused",
      "effect": {
        "span": "make it more representative, more effective and more accountable to all Member States"
      }
    }
  ]
}
```

### --- id=10752 ---

输入文本: They must therefore be well prepared in order to properly perform their task.

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
        "span": "be well prepared"
      },
      "relation": "caused",
      "effect": {
        "span": "properly perform their task"
      }
    }
  ]
}
```

### --- id=17608 ---

输入文本: Spain believes that the Common Framework can also benefit middle-income countries with liquidity problems caused by the COVID-19 pandemic — in addition to benefiting the most vulnerable low-income countries.

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
      "cause": "the COVID-19 pandemic",
      "effect": "-income countries with liquidity problems"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the COVID-19 pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "liquidity problems"
      }
    }
  ]
}
```

### --- id=16379 ---

输入文本: At the same time, we must strengthen our counter-terrorism efforts through collective measures in order to put an end to the terrorist scourge that is indiscriminately causing great damage to property and resulting in a massive loss of innocent lives.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "must strengthen our counter-terrorism efforts through collective measures",
      "effect": "in order to put an end to the terrorist scourge that is indiscriminately causing great damage to property and resulting in a massive loss of innocent lives"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "strengthen our counter-terrorism efforts through collective measures"
      },
      "relation": "caused",
      "effect": {
        "span": "put an end to the terrorist scourge"
      }
    },
    {
      "cause": {
        "span": "terrorist scourge"
      },
      "relation": "caused",
      "effect": {
        "span": "great damage to property"
      }
    },
    {
      "cause": {
        "span": "terrorist scourge"
      },
      "relation": "caused",
      "effect": {
        "span": "a massive loss of innocent lives"
      }
    }
  ]
}
```

### --- id=5903 ---

输入文本: We have also banned all travel from 22 countries where there is a risk of known variants including South Africa, Portugal and South American nations, and in order to reduce the risk posed by UK nationals and residents returning home from these countries,I can announce that we will require all such arrivals who cannot be refused entry to isolate in government-provided accommodation - such as hotels - for ten days without exception.

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
      "cause": "banned all travel from 22 countries where there is a risk of known variants including South Africa, Portugal and South American nations",
      "effect": "reduce the risk posed by UK nationals and residents returning home from these countries"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "require all such arrivals who cannot be refused entry to isolate in government-provided accommodation - such as hotels - for ten days without exception"
      },
      "relation": "caused",
      "effect": {
        "span": "reduce the risk posed by UK nationals and residents returning home from these countries"
      }
    }
  ]
}
```

### --- id=12412 ---

输入文本: Therefore, in the same way that we are leading a just recovery project to overcome the economic crisis, we must also commit ourselves to a just green transition, which we are convinced is the most effective way to reach new levels of progress and well-being.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "leading a just recovery project",
      "effect": "overcome the economic crisis"
    },
    {
      "cause": "we must also commit ourselves to a just green transition",
      "effect": "reach new levels of progress and well-being"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "leading a just recovery project"
      },
      "relation": "caused",
      "effect": {
        "span": "overcome the economic crisis"
      }
    },
    {
      "cause": {
        "span": "a just green transition"
      },
      "relation": "caused",
      "effect": {
        "span": "reach new levels of progress and well-being"
      }
    }
  ]
}
```

### --- id=7119 ---

输入文本: In Sierra Leone, we have expanded legal aid services to poor and underserved people and established special courts to fast-track cases in the areas of sexual offences, social security, corruption and small claims, among others.

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
        "span": "established special courts"
      },
      "relation": "caused",
      "effect": {
        "span": "fast-track cases in the areas of sexual offences, social security, corruption and small claims, among others"
      }
    }
  ]
}
```

### --- id=3143 ---

输入文本: Timing will depend on the readiness of our armed forces to march into battle.

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
        "span": "the readiness of our armed forces to march into battle"
      },
      "relation": "caused",
      "effect": {
        "span": "Timing"
      }
    }
  ]
}
```

### --- id=5217 ---

输入文本: The Adult Social Care – Omicron Support Fund is on top of the £388 million infection control and testing fund announced earlier in the year to prevent infections and provide testing in the care sector.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "the £388 million infection control and testing fund"
      },
      "relation": "caused",
      "effect": {
        "span": "prevent infections"
      }
    },
    {
      "cause": {
        "span": "the £388 million infection control and testing fund"
      },
      "relation": "caused",
      "effect": {
        "span": "provide testing in the care sector"
      }
    }
  ]
}
```

### --- id=13121 ---

输入文本: Against that backdrop, we welcome the operationalization of the repositioning of the United Nations development system so that it can respond effectively to addressing the development needs and priorities of Member States, with particular attention given to meeting the needs of countries in special situations, especially least developed countries (LDCs), landlocked least developed countries (LLDCs) and small island developing States, in order to help them deal with acute vulnerability and external shocks.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "welcome the operationalization of the repositioning of the United Nations development system",
      "effect": "it can respond effectively to addressing the development needs and priorities of Member States"
    },
    {
      "cause": "welcome the operationalization of the repositioning of the United Nations development system",
      "effect": "help them deal with acute vulnerability and external shocks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the operationalization of the repositioning of the United Nations development system"
      },
      "relation": "caused",
      "effect": {
        "span": "it can respond effectively to addressing the development needs and priorities of Member States"
      }
    },
    {
      "cause": {
        "span": "the operationalization of the repositioning of the United Nations development system"
      },
      "relation": "caused",
      "effect": {
        "span": "help them deal with acute vulnerability and external shocks"
      }
    }
  ]
}
```

### --- id=11159 ---

输入文本: In that regard, the nationally determined contributions are key to accelerated climate action.

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
        "span": "the nationally determined contributions"
      },
      "relation": "caused",
      "effect": {
        "span": "accelerated climate action"
      }
    }
  ]
}
```

### --- id=11576 ---

输入文本: And it is only because we know Omicron is less severe, that testing for Omicron on the colossal scale we have been doing is much less important, and much less valuable in preventing serious illness.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "know Omicron is less severe",
      "effect": "testing for Omicron on the colossal scale we have been doing is much less important"
    },
    {
      "cause": "know Omicron is less severe",
      "effect": "much less valuable in preventing serious illness."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "we know Omicron is less severe"
      },
      "relation": "caused",
      "effect": {
        "span": "testing for Omicron on the colossal scale we have been doing is much less important, and much less valuable in preventing serious illness"
      }
    }
  ]
}
```

### --- id=17211 ---

输入文本: These climate-change adaptation measures have led to more than 13,000 farmers being trained in sustainable land management, over 92 per cent of whom have adopted sustainable practices.

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
        "span": "These climate-change adaptation measures"
      },
      "relation": "caused",
      "effect": {
        "span": "more than 13,000 farmers being trained in sustainable land management"
      }
    }
  ]
}
```

### --- id=16426 ---

输入文本: The infrastructure components to improve neighbourhoods and lives will wrap up the last leg of what has been a transformative multi-year initiative.

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
        "span": "The infrastructure components"
      },
      "relation": "caused",
      "effect": {
        "span": "improve neighbourhoods and lives"
      }
    }
  ]
}
```

### --- id=10592 ---

输入文本: The fuelling of the greed of a few threatens to undermine what little gains we have made since independence, and we judge ourselves harshly because independence is a recent phenomenon for us.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "The fuelling of the greed of a few"
      },
      "relation": "caused",
      "effect": {
        "span": "threatens to undermine what little gains we have made since independence"
      }
    },
    {
      "cause": {
        "span": "independence is a recent phenomenon for us"
      },
      "relation": "caused",
      "effect": {
        "span": "we judge ourselves harshly"
      }
    }
  ]
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

### --- id=5206 ---

输入文本: We can all be incredibly proud of – and grateful for – a jab that has saved many millions of lives.

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
        "span": "a jab"
      },
      "relation": "caused",
      "effect": {
        "span": "saved many millions of lives"
      }
    }
  ]
}
```

### --- id=11195 ---

输入文本: Will we continue to wait for floods and droughts to devastate us and for thousands of people to be displaced without a future and even lose their lives?

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "floods and droughts"
      },
      "relation": "caused",
      "effect": {
        "span": "devastate us"
      }
    },
    {
      "cause": {
        "span": "floods and droughts"
      },
      "relation": "caused",
      "effect": {
        "span": "thousands of people to be displaced without a future and even lose their lives"
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
        "span": "pioneered life-saving treatments"
      },
      "relation": "caused",
      "effect": {
        "span": "reducing our fatality rate 85 per cent since April"
      }
    }
  ]
}
```

### --- id=9192 ---

输入文本: This has identified extra cases of infection that were previously removed as duplicates.

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
        "span": "identified extra cases of infection that were previously removed as duplicates"
      }
    }
  ]
}
```

### --- id=9523 ---

输入文本: For the sake of a peaceful future for all humankind, let us solve that problem as soon as possible on the basis of justice.

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
        "span": "solve that problem as soon as possible on the basis of justice"
      },
      "relation": "caused",
      "effect": {
        "span": "a peaceful future for all humankind"
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
        "span": "practice specific safe and responsible behaviours"
      },
      "relation": "caused",
      "effect": {
        "span": "stopping the spread of the virus"
      }
    }
  ]
}
```

### --- id=14174 ---

输入文本: I believe that we would all agree that no matter how many peacemaking or peacekeeping operations are deployed in conflict areas, at the end of the day peace and security cannot prevail in the absence of development and inclusive growth.

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
        "span": "absence of development and inclusive growth"
      },
      "relation": "caused",
      "effect": {
        "span": "peace and security cannot prevail"
      }
    }
  ]
}
```

### --- id=1685 ---

输入文本: The pandemic brought out the very essence of GNH, which seeks collective happiness and not just of oneself.

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
        "span": "brought out the very essence of GNH"
      }
    }
  ]
}
```

### --- id=16030 ---

输入文本: They provide the path towards a radical transformation in both the way we look at the world and our behaviour patterns.

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
        "span": "They"
      },
      "relation": "caused",
      "effect": {
        "span": "a radical transformation in both the way we look at the world and our behaviour patterns"
      }
    }
  ]
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
        "span": "save the Pacific"
      },
      "relation": "caused",
      "effect": {
        "span": "save the whole planet"
      }
    },
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

### --- id=11646 ---

输入文本: Prime Minister and NHS turbocharge booster programme against Omicron and launch an urgent national appeal calling for people to get jabbed Latest data shows booster is needed to protect ourselves and the NHS against the variant Prime Minister: A tidal wave of Omicron is coming.

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
      "cause": "ooster i",
      "effect": "rotect o"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "booster"
      },
      "relation": "caused",
      "effect": {
        "span": "protect ourselves and the NHS against the variant"
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

### --- id=5091 ---

输入文本: This included: opening over 3,000 vaccination sites, with 180 new sites having opened in December – including at football stadiums, shopping centres and at Christmas markets, with extended opening hours and some sites working around the clock sending over 30 million people invites from the NHS during 2021– including over 3.9 million letters, 26.7 million text messages and 14.7 million emails inviting people to book online sending a text to everyone in the country urging them to get boosted drafting in 750 armed forces personnel to support deployment, alongside a renewed drive that has meant the recruitment of tens of thousands of volunteers temporarily suspending the 15-minute observation period following Pfizer or Moderna booster jabs, where clinically safe and appropriate to do so, in order to get more jabs in arms Vaccines Minister Maggie Throup said: The UK COVID-19 vaccination programme is something we can all be proud of – having provided tens of millions of people with protection from this deadly virus over the past year.

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
        "span": "temporarily suspending the 15-minute observation period following Pfizer or Moderna booster jabs, where clinically safe and appropriate to do so"
      },
      "relation": "caused",
      "effect": {
        "span": "get more jabs in arms"
      }
    }
  ]
}
```

### --- id=10992 ---

输入文本: Developing countries often lack the capacity or capability to capitalize on the latest global trends in public-sector innovation, Government reform and technology in addressing development challenges.

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
        "span": "Developing countries often lack the capacity or capability to capitalize on the latest global trends in public-sector innovation, Government reform and technology"
      },
      "relation": "caused",
      "effect": {
        "span": "addressing development challenges"
      }
    }
  ]
}
```

### --- id=8833 ---

输入文本: Vaccines are one of the most important weapons we have against COVID-19 and they have prevented countless deaths and hospitalisations through this pandemic.

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
      "cause": "they",
      "effect": "have prevented countless deaths and hospitalisations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Vaccines"
      },
      "relation": "caused",
      "effect": {
        "span": "prevented countless deaths and hospitalisations"
      }
    }
  ]
}
```

### --- id=8254 ---

输入文本: I’ve found food preparation and cooking has helped me relax over the past year.

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
      "cause": "food preparation and cooking",
      "effect": "has helped me relax over the past year."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "food preparation and cooking"
      },
      "relation": "caused",
      "effect": {
        "span": "helped me relax"
      }
    }
  ]
}
```

### --- id=15608 ---

输入文本: Advanced economies have been able to use monetary and fiscal policies more robustly to contain the economic shock.

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
        "span": "use monetary and fiscal policies more robustly"
      },
      "relation": "caused",
      "effect": {
        "span": "contain the economic shock"
      }
    }
  ]
}
```

### --- id=12555 ---

输入文本: I hope that the UN and the international community provide support so that we can advance into an era of reconciliation and prosperity through the end-of-war declaration.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "provide support",
      "effect": "advance into an era of reconciliation and prosperity"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the UN and the international community provide support"
      },
      "relation": "caused",
      "effect": {
        "span": "we can advance into an era of reconciliation and prosperity"
      }
    },
    {
      "cause": {
        "span": "the end-of-war declaration"
      },
      "relation": "caused",
      "effect": {
        "span": "we can advance into an era of reconciliation and prosperity"
      }
    }
  ]
}
```

### --- id=15422 ---

输入文本: While we remained committed to all of its elements to this day and agreed to every call and initiative to achieve a political solution on the basis of international legitimacy, including the 2002 Arab Peace Initiative and the 2003 Quartet Roadmap, Israel has not honoured its obligations under the signed agreements and has evaded participating in peace initiatives and instead pursued its expansionist, colonial enterprise, destroying the prospect of a political settlement based on the two-State solution.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "not honoured its obligations under the signed agreements",
      "effect": "destroying the prospect of a political settlement based on the two-State solution"
    },
    {
      "cause": "evaded participating in peace initiatives",
      "effect": "destroying the prospect of a political settlement based on the two-State solution"
    },
    {
      "cause": "pursued its expansionist, colonial enterprise",
      "effect": "destroying the prospect of a political settlement based on the two-State solution"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Israel has not honoured its obligations under the signed agreements and has evaded participating in peace initiatives and instead pursued its expansionist, colonial enterprise"
      },
      "relation": "caused",
      "effect": {
        "span": "destroying the prospect of a political settlement based on the two-State solution"
      }
    }
  ]
}
```

### --- id=17549 ---

输入文本: Genuine security for either side — indeed, for the whole world — can only be achieved through the two-state solution, a solution that leads to the establishment of an independent, sovereign, and viable Palestinian state on the basis of the June 1967 lines, with East Jerusalem as its capital, living side-by-side with Israel in peace and security.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "the two-state solution",
      "effect": "the establishment of an independent, sovereign, and viable Palestinian state"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the two-state solution"
      },
      "relation": "caused",
      "effect": {
        "span": "Genuine security for either side — indeed, for the whole world"
      }
    },
    {
      "cause": {
        "span": "the two-state solution"
      },
      "relation": "caused",
      "effect": {
        "span": "the establishment of an independent, sovereign, and viable Palestinian state on the basis of the June 1967 lines, with East Jerusalem as its capital, living side-by-side with Israel in peace and security"
      }
    }
  ]
}
```

### --- id=12346 ---

输入文本: Education regression is now inevitable, considering the long period in which our children have been forced out of the formal classroom and the challenges that many developing countries face in delivering education virtually.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "the long period in which our children have been forced out of the formal classroom"
      },
      "relation": "caused",
      "effect": {
        "span": "Education regression"
      }
    },
    {
      "cause": {
        "span": "the challenges that many developing countries face in delivering education virtually"
      },
      "relation": "caused",
      "effect": {
        "span": "Education regression"
      }
    }
  ]
}
```

### --- id=2556 ---

输入文本: Those unhappy events prove that human rights are directly linked to sovereign rights and that without them, people cannot avoid the fate of stateless nations fraught with misery and disaster.

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
        "span": "without them"
      },
      "relation": "caused",
      "effect": {
        "span": "people cannot avoid the fate of stateless nations fraught with misery and disaster"
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

### --- id=11511 ---

输入文本: We hope for and expect the same behaviour and attitudes to save a planet that suffers abuses of all kinds, such as overexploitation and excess production and consumption.

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
        "span": "the same behaviour and attitudes"
      },
      "relation": "caused",
      "effect": {
        "span": "save a planet that suffers abuses of all kinds, such as overexploitation and excess production and consumption"
      }
    }
  ]
}
```

### --- id=1587 ---

输入文本: We have signed a pact with the youth to make a genuine change in the policies that will benefit them.

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
      "cause": "have signed a pact with the youth",
      "effect": "make a genuine change in the policies that will benefit them"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "signed a pact with the youth"
      },
      "relation": "caused",
      "effect": {
        "span": "make a genuine change in the policies that will benefit them"
      }
    }
  ]
}
```

### --- id=1212 ---

输入文本: When the reduced risk of hospitalisation was combined with vaccine effectiveness against symptomatic disease, the vaccine effectiveness against hospitalisation was estimated as 52% after one dose, 72% 2 to 24 weeks after dose 2, 52% 25 weeks after dose 2 and 88% 2 weeks after a booster dose.

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
        "span": "the reduced risk of hospitalisation was combined with vaccine effectiveness against symptomatic disease"
      },
      "relation": "caused",
      "effect": {
        "span": "the vaccine effectiveness against hospitalisation was estimated as 52% after one dose, 72% 2 to 24 weeks after dose 2, 52% 25 weeks after dose 2 and 88% 2 weeks after a booster dose"
      }
    }
  ]
}
```

### --- id=3986 ---

输入文本: From next week the slow and gradual unlocking begins, therefore more than ever it is vital you follow the guidelines.

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
        "span": "the slow and gradual unlocking begins"
      },
      "relation": "caused",
      "effect": {
        "span": "it is vital you follow the guidelines"
      }
    }
  ]
}
```

### --- id=15613 ---

输入文本: From that standpoint, we reiterate the call for the United Nations to lead the process of unifying efforts to prevent the misuse of the scientific progress in cybersecurity and regularize this vital aspect according to the rules of international law.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "unifying efforts"
      },
      "relation": "caused",
      "effect": {
        "span": "prevent the misuse of the scientific progress in cybersecurity"
      }
    },
    {
      "cause": {
        "span": "unifying efforts"
      },
      "relation": "caused",
      "effect": {
        "span": "regularize this vital aspect according to the rules of international law"
      }
    }
  ]
}
```

### --- id=5683 ---

输入文本: If we can catch more asymptomatic people before they unknowingly pass on the disease to the vulnerable, we can help to stop the virus’ vicious spread.

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
      "cause": "catch more asymptomatic people before they unknowingly pass on the disease",
      "effect": "help to stop the virus’ vicious spread"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "catch more asymptomatic people before they unknowingly pass on the disease to the vulnerable"
      },
      "relation": "caused",
      "effect": {
        "span": "stop the virus’ vicious spread"
      }
    }
  ]
}
```

### --- id=14057 ---

输入文本: Those days gave Afghans tremendous belief that peace is possible and proved that the Government has the ability to directly negotiate peace with our enemies.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "Those days"
      },
      "relation": "caused",
      "effect": {
        "span": "Afghans tremendous belief that peace is possible"
      }
    },
    {
      "cause": {
        "span": "Those days"
      },
      "relation": "caused",
      "effect": {
        "span": "proved that the Government has the ability to directly negotiate peace with our enemies"
      }
    }
  ]
}
```

### --- id=12208 ---

输入文本: The World Health Organization’s COVAX programme and bilateral solidarity actions around the world give hope that, together, we will be able to overcome this disease.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "COVAX programme",
      "effect": "give hope that, together, we will be able to overcome this disease"
    },
    {
      "cause": "bilateral solidarity actions around the world",
      "effect": "give hope that, together, we will be able to overcome this disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The World Health Organization’s COVAX programme and bilateral solidarity actions around the world"
      },
      "relation": "caused",
      "effect": {
        "span": "we will be able to overcome this disease"
      }
    }
  ]
}
```

### --- id=2758 ---

输入文本: The threat of nuclear weapons, possessed under the guise of nuclear deterrence, creates an ethos of fear based on mutual annihilation, and poisons relationships between peoples, obstructs dialogue, and undermines hope.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 3,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "threat of nuclear weapons",
      "effect": "creates an ethos of fear based on mutual annihilation"
    },
    {
      "cause": "threat of nuclear weapons",
      "effect": "poisons relationships between peoples, obstructs dialogue, and undermines hope"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The threat of nuclear weapons, possessed under the guise of nuclear deterrence"
      },
      "relation": "caused",
      "effect": {
        "span": "creates an ethos of fear based on mutual annihilation"
      }
    },
    {
      "cause": {
        "span": "The threat of nuclear weapons, possessed under the guise of nuclear deterrence"
      },
      "relation": "caused",
      "effect": {
        "span": "poisons relationships between peoples"
      }
    },
    {
      "cause": {
        "span": "The threat of nuclear weapons, possessed under the guise of nuclear deterrence"
      },
      "relation": "caused",
      "effect": {
        "span": "obstructs dialogue"
      }
    },
    {
      "cause": {
        "span": "The threat of nuclear weapons, possessed under the guise of nuclear deterrence"
      },
      "relation": "caused",
      "effect": {
        "span": "undermines hope"
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

### --- id=17624 ---

输入文本: The pandemic, the climate crisis, unemployment and limited levels of investment are putting extreme stress on the social and political stability of developing countries, as well as the stability of the entire planet, owing to global interconnectedness.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "the climate crisis",
      "effect": "are putting extreme stress"
    },
    {
      "cause": "unemployment",
      "effect": "are putting extreme stress"
    },
    {
      "cause": "limited levels of investment",
      "effect": "are putting extreme stress"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The pandemic, the climate crisis, unemployment and limited levels of investment"
      },
      "relation": "caused",
      "effect": {
        "span": "putting extreme stress on the social and political stability of developing countries, as well as the stability of the entire planet"
      }
    }
  ]
}
```

### --- id=13660 ---

输入文本: In conclusion, my country renews its call to all countries of the world to adhere to the principles of the Charter of the United Nations and international law in order to resolve their differences through peaceful and diplomatic means.

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
      "cause": "peaceful and diplomatic means",
      "effect": "resolve their differences"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "adhere to the principles of the Charter of the United Nations and international law"
      },
      "relation": "caused",
      "effect": {
        "span": "resolve their differences through peaceful and diplomatic means"
      }
    }
  ]
}
```

### --- id=12002 ---

输入文本: We believe that through implementing hydropower plant construction projects in Kyrgyzstan we can meet the Central Asian countries’ hydropower needs and thereby create the conditions necessary for the sustainable development of our entire region.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "through implementing hydropower plant construction projects",
      "effect": "can meet the Central Asian countries’ hydropower needs"
    },
    {
      "cause": "through implementing hydropower plant construction projects",
      "effect": "create the conditions necessary"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "implementing hydropower plant construction projects in Kyrgyzstan"
      },
      "relation": "caused",
      "effect": {
        "span": "meet the Central Asian countries’ hydropower needs"
      }
    },
    {
      "cause": {
        "span": "implementing hydropower plant construction projects in Kyrgyzstan"
      },
      "relation": "caused",
      "effect": {
        "span": "create the conditions necessary for the sustainable development of our entire region"
      }
    }
  ]
}
```

### --- id=17531 ---

输入文本: We raise it again today, not because we are bound by practice to do so, but because we resolutely believe that there shall be no peace and no justice until the Palestinian people are free from occupation and are able to exercise the rights for which this United Nations stands.

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
        "span": "the Palestinian people are free from occupation and are able to exercise the rights for which this United Nations stands"
      },
      "relation": "caused",
      "effect": {
        "span": "there shall be no peace and no justice"
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

### --- id=6588 ---

输入文本: Independent and sovereign states are being driven under multiple pressures to force them to subordinate to the will of Washington and to an order based on its capricious rules.

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
        "span": "multiple pressures"
      },
      "relation": "caused",
      "effect": {
        "span": "force them to subordinate to the will of Washington and to an order based on its capricious rules"
      }
    }
  ]
}
```

### --- id=500 ---

输入文本: We know that in older age groups, protection from the first 2 vaccines is beginning to wear off, leaving millions that need extra protection as we head into winter.

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
        "span": "protection from the first 2 vaccines is beginning to wear off"
      },
      "relation": "caused",
      "effect": {
        "span": "leaving millions that need extra protection"
      }
    }
  ]
}
```

### --- id=14432 ---

输入文本: Climate change is having a structural impact on food security, migration and even stability in many countries.

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
        "span": "Climate change"
      },
      "relation": "caused",
      "effect": {
        "span": "a structural impact on food security, migration and even stability in many countries"
      }
    }
  ]
}
```

### --- id=10950 ---

输入文本: In its 39 years of existence, Vanuatu has been a small open island economy and, in recent years, we have experienced sustained economic growth, underpinned by good macroeconomic stability and a responsible and effective Government.

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
        "span": "good macroeconomic stability and a responsible and effective Government"
      },
      "relation": "caused",
      "effect": {
        "span": "sustained economic growth"
      }
    }
  ]
}
```

### --- id=16774 ---

输入文本: The adverse effects of climate change pose significant obstacles to poverty reduction and threaten hard-won progress towards the achievement of the Sustainable Development Goals.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "The adverse effects of climate change"
      },
      "relation": "caused",
      "effect": {
        "span": "pose significant obstacles to poverty reduction"
      }
    },
    {
      "cause": {
        "span": "The adverse effects of climate change"
      },
      "relation": "caused",
      "effect": {
        "span": "threaten hard-won progress towards the achievement of the Sustainable Development Goals"
      }
    }
  ]
}
```

### --- id=3524 ---

输入文本: International financial institutions should re-examine their eligibility criteria to tailor SIDS’ access to concessional financing to take into account our extreme vulnerability to economic, climate and now public health shocks that put us at particular risk and disadvantage.

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
        "span": "re-examine their eligibility criteria"
      },
      "relation": "caused",
      "effect": {
        "span": "tailor SIDS’ access to concessional financing to take into account our extreme vulnerability to economic, climate and now public health shocks"
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

### --- id=12286 ---

输入文本: The closure of schools and institutions of higher learning due to the pandemic, has had an unparalleled devastating impact to millions of learners.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "the pandemic",
      "effect": "closure of schools and institutions of higher learning"
    },
    {
      "cause": "the pandemic",
      "effect": "unparalleled devastating impact"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "The closure of schools and institutions of higher learning"
      }
    },
    {
      "cause": {
        "span": "The closure of schools and institutions of higher learning"
      },
      "relation": "caused",
      "effect": {
        "span": "an unparalleled devastating impact to millions of learners"
      }
    }
  ]
}
```

### --- id=5088 ---

输入文本: This week, the NHS ensured over 1.5 million appointments were still available between 27 December and tomorrow (Monday 3 January), allowing anyone eligible who had not yet had the booster the opportunity to book their appointment.

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
        "span": "the NHS ensured over 1.5 million appointments were still available between 27 December and tomorrow (Monday 3 January)"
      },
      "relation": "caused",
      "effect": {
        "span": "allowing anyone eligible who had not yet had the booster the opportunity to book their appointment"
      }
    }
  ]
}
```

### --- id=7509 ---

输入文本: Let all the difficulties we have overcome lay the firm foundation for a new understanding among peoples.

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
        "span": "all the difficulties we have overcome"
      },
      "relation": "caused",
      "effect": {
        "span": "lay the firm foundation for a new understanding among peoples"
      }
    }
  ]
}
```

### --- id=13845 ---

输入文本: It is self-evident that opaque, non-inclusive and undemocratic entities are presuming to impose an illegitimate rule-making authority on island States in the hope that their financial sector will collapse under the weight of onerous regulation, rapidly changing requirements and the threat of unilateral blacklists.

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
        "span": "onerous regulation, rapidly changing requirements and the threat of unilateral blacklists"
      },
      "relation": "caused",
      "effect": {
        "span": "their financial sector will collapse"
      }
    }
  ]
}
```

### --- id=17529 ---

输入文本: As for COVID-19, we cannot afford to wait for an even deadlier variant to emerge and claim more lives.

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
        "span": "an even deadlier variant to emerge"
      },
      "relation": "caused",
      "effect": {
        "span": "claim more lives"
      }
    }
  ]
}
```

### --- id=15301 ---

输入文本: Therefore, it is the duty of every country to take stock of their achievements, verify progress, monitor remaining challenges and, of course, immediately take the necessary actions to ensure success for each one of the Goals.

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
        "span": "immediately take the necessary actions"
      },
      "relation": "caused",
      "effect": {
        "span": "ensure success for each one of the Goals"
      }
    }
  ]
}
```

### --- id=14348 ---

输入文本: That is why we support immediate concerted action to preserve the Treaty’s achievements in our shared home, the European continent.

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
        "span": "immediate concerted action"
      },
      "relation": "caused",
      "effect": {
        "span": "preserve the Treaty’s achievements in our shared home, the European continent"
      }
    }
  ]
}
```

### --- id=14810 ---

输入文本: Rwanda stands ready to do its part, including by guaranteeing the rights and opportunities of women and girls.

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
        "span": "guaranteeing the rights and opportunities of women and girls"
      },
      "relation": "caused",
      "effect": {
        "span": "do its part"
      }
    }
  ]
}
```

### --- id=16383 ---

输入文本: It should be the United Nations that takes bold steps in addressing the question of Palestine and protecting the viability of a two-State solution, with Palestine and Israel coexisting side by side in peace and within internationally recognized secure borders.

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
        "span": "the United Nations that takes bold steps in addressing the question of Palestine and protecting the viability of a two-State solution"
      },
      "relation": "caused",
      "effect": {
        "span": "Palestine and Israel coexisting side by side in peace and within internationally recognized secure borders"
      }
    }
  ]
}
```

### --- id=432 ---

输入文本: Bringing the right people and organisations to improve the health and wellbeing of their areas through integrated care systems, and giving them the funds and support they need to do just that.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "Bringing the right people and organisations"
      },
      "relation": "caused",
      "effect": {
        "span": "improve the health and wellbeing of their areas"
      }
    },
    {
      "cause": {
        "span": "integrated care systems"
      },
      "relation": "caused",
      "effect": {
        "span": "improve the health and wellbeing of their areas"
      }
    },
    {
      "cause": {
        "span": "giving them the funds and support they need"
      },
      "relation": "caused",
      "effect": {
        "span": "do just that"
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
        "span": "coordinating regional and international positions"
      },
      "relation": "caused",
      "effect": {
        "span": "address the critical security situation in the region"
      }
    }
  ]
}
```

### --- id=13560 ---

输入文本: Their peoples have become refugees or been displaced and their schools have been closed, sacrificing generations of young people who no longer have the opportunity to learn.

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
        "span": "their schools have been closed"
      },
      "relation": "caused",
      "effect": {
        "span": "sacrificing generations of young people who no longer have the opportunity to learn"
      }
    }
  ]
}
```

### --- id=8205 ---

输入文本: A survey by the World Health Organization (WHO) showed that the pandemic disrupted mental health services in 93% of countries worldwide.

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
        "span": "disrupted mental health services in 93% of countries worldwide"
      }
    }
  ]
}
```

### --- id=17038 ---

输入文本: As a testament to its keenness to further the wellbeing of the sisterly peoples of the Nile basin, Egypt has expressed its understanding regarding Ethiopia’s first steps towards construction of the Renaissance Dam, despite the fact that Ethiopia did not conduct the necessary studies on the effects of that huge project to ensure that no harm befalls the water interests of downstream countries, including Egypt.

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
        "span": "conduct the necessary studies on the effects of that huge project"
      },
      "relation": "caused",
      "effect": {
        "span": "no harm befalls the water interests of downstream countries, including Egypt"
      }
    }
  ]
}
```

### --- id=12608 ---

输入文本: I call on all partners across the continent to take bolder measures aimed at relieving the burden on our economies, which have been hard hit by the effects of Covid-19.

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
      "cause": "the effects of Covid-19",
      "effect": "have been hard hit"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Covid-19"
      },
      "relation": "caused",
      "effect": {
        "span": "our economies, which have been hard hit"
      }
    }
  ]
}
```

### --- id=7007 ---

输入文本: We will proudly be at the forefront in this area, owing to our love for nature and respect for the environment.

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
        "span": "our love for nature and respect for the environment"
      },
      "relation": "caused",
      "effect": {
        "span": "We will proudly be at the forefront in this area"
      }
    }
  ]
}
```

### --- id=10112 ---

输入文本: We must give it legal status and build effective action to eradicate it.

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
      "cause": "must give it legal status and build effective action",
      "effect": "eradicate it"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "build effective action"
      },
      "relation": "caused",
      "effect": {
        "span": "eradicate it"
      }
    }
  ]
}
```

### --- id=14966 ---

输入文本: I take this opportunity to reaffirm Guyana’s commitment to the disarmament agenda of the United Nations as central to the Organization’s efforts to achieve a stable, secure and peaceful world order.

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
        "span": "the disarmament agenda of the United Nations"
      },
      "relation": "caused",
      "effect": {
        "span": "achieve a stable, secure and peaceful world order"
      }
    }
  ]
}
```

### --- id=4567 ---

输入文本: Anyone over the age of 50 or between 18 to 49 with an underlying health condition can sign up to the study as soon as they receive a positive PCR or lateral flow test result.

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
        "span": "receive a positive PCR or lateral flow test result"
      },
      "relation": "caused",
      "effect": {
        "span": "can sign up to the study"
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

### --- id=8072 ---

输入文本: By using the UK’s world class scientific abilities, the UKHSA will play a major role in protecting people from COVID-19 and future emerging health threats at home and abroad.

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
        "span": "using the UK’s world class scientific abilities"
      },
      "relation": "caused",
      "effect": {
        "span": "the UKHSA will play a major role in protecting people from COVID-19 and future emerging health threats at home and abroad"
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
        "span": "coordinating with the judiciary to create an environment conducive to its critical and important role"
      },
      "relation": "caused",
      "effect": {
        "span": "ensuring the principle of impunity"
      }
    },
    {
      "cause": {
        "span": "coordinating with the judiciary to create an environment conducive to its critical and important role"
      },
      "relation": "caused",
      "effect": {
        "span": "empowering law-enforcement agencies to do their job as required"
      }
    }
  ]
}
```

### --- id=10698 ---

输入文本: Dividing lines are damaging to the world economy as well as world politics.

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
        "span": "Dividing lines"
      },
      "relation": "caused",
      "effect": {
        "span": "damaging to the world economy as well as world politics"
      }
    }
  ]
}
```

### --- id=3604 ---

输入文本: Our prospects for achieving sustainable development hinge heavily on the safety and security of our people.

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
        "span": "the safety and security of our people"
      },
      "relation": "caused",
      "effect": {
        "span": "achieving sustainable development"
      }
    }
  ]
}
```

### --- id=1306 ---

输入文本: They are our best defence and we have turbocharged our rollout programme inviting 7 million more people over the age of 40 to get their booster jab so even more people get protection from this disease.

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
      "cause": "turbocharged our rollout programme inviting",
      "effect": "even more people get protection from this disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "inviting 7 million more people over the age of 40 to get their booster jab"
      },
      "relation": "caused",
      "effect": {
        "span": "even more people get protection from this disease"
      }
    }
  ]
}
```

### --- id=12214 ---

输入文本: This openness gave us the ability to purchase vaccines from around the world, giving our citizens the unique freedom to choose which vaccine they prefer.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "openness",
      "effect": "ability to purchase vaccines"
    },
    {
      "cause": "openness",
      "effect": "unique freedom to choose"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "This openness"
      },
      "relation": "caused",
      "effect": {
        "span": "gave us the ability to purchase vaccines from around the world"
      }
    },
    {
      "cause": {
        "span": "purchase vaccines from around the world"
      },
      "relation": "caused",
      "effect": {
        "span": "giving our citizens the unique freedom to choose which vaccine they prefer"
      }
    }
  ]
}
```

### --- id=3484 ---

输入文本: In addition, programmes have been developed to train young people and help them to enter the labour market, thereby contributing to the development of the national economy.

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
      "cause": "programmes have been developed",
      "effect": "train young people and help them to enter the labour market"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "programmes have been developed to train young people and help them to enter the labour market"
      },
      "relation": "caused",
      "effect": {
        "span": "contributing to the development of the national economy"
      }
    }
  ]
}
```

### --- id=119 ---

输入文本: Temporary and precautionary measures to prevent the spread of the new COVID-19 Omicron variant in the UK will come into force on Tuesday, the government has confirmed.

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
        "span": "Temporary and precautionary measures"
      },
      "relation": "caused",
      "effect": {
        "span": "prevent the spread of the new COVID-19 Omicron variant in the UK"
      }
    }
  ]
}
```

### --- id=13085 ---

输入文本: Greater multilateral cooperation is likewise needed to create the conditions and take the steps necessary for the elimination of nuclear weapons.

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
      "cause": "create the conditions and take the steps",
      "effect": "elimination of nuclear weapons"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Greater multilateral cooperation"
      },
      "relation": "caused",
      "effect": {
        "span": "create the conditions and take the steps necessary for the elimination of nuclear weapons"
      }
    }
  ]
}
```

### --- id=5668 ---

输入文本: The vaccination programme and test, trace and isolate system continue to be the most effective way of reducing transmission, along with practicing good hygiene, keeping spaces well ventilated, and wearing a face covering in enclosed or crowded spaces.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 4
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 4
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 4,
    "fn": 4
  },
  "gold_relations": [
    {
      "cause": "vaccination programme and test, trace and isolate system",
      "effect": "most effective way of reducing transmission"
    },
    {
      "cause": "good hygiene",
      "effect": "most effective way of reducing transmission"
    },
    {
      "cause": "keeping spaces well ventilated",
      "effect": "most effective way of reducing transmission"
    },
    {
      "cause": "wearing a face covering in enclosed or crowded spaces",
      "effect": "most effective way of reducing transmission"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The vaccination programme and test, trace and isolate system"
      },
      "relation": "caused",
      "effect": {
        "span": "reducing transmission"
      }
    },
    {
      "cause": {
        "span": "practicing good hygiene"
      },
      "relation": "caused",
      "effect": {
        "span": "reducing transmission"
      }
    },
    {
      "cause": {
        "span": "keeping spaces well ventilated"
      },
      "relation": "caused",
      "effect": {
        "span": "reducing transmission"
      }
    },
    {
      "cause": {
        "span": "wearing a face covering in enclosed or crowded spaces"
      },
      "relation": "caused",
      "effect": {
        "span": "reducing transmission"
      }
    }
  ]
}
```

### --- id=5066 ---

输入文本: We are so fortunate to have great teachers and parents who have already done so much to have children back in the classroom, and former teachers happy to volunteer extra support to keep children there.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "great teachers and parents who have already done so much"
      },
      "relation": "caused",
      "effect": {
        "span": "have children back in the classroom"
      }
    },
    {
      "cause": {
        "span": "former teachers happy to volunteer extra support"
      },
      "relation": "caused",
      "effect": {
        "span": "keep children there"
      }
    }
  ]
}
```

### --- id=9408 ---

输入文本: That could jeopardize all the progress made by the Dominican Government.

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
        "span": "That"
      },
      "relation": "caused",
      "effect": {
        "span": "jeopardize all the progress made by the Dominican Government"
      }
    }
  ]
}
```

### --- id=16473 ---

输入文本: With a fragile population of 110,000, almost half of whom are young people, I am convinced that such an investment will yield a population dividend that will raise our nation.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
        "span": "such an investment"
      },
      "relation": "caused",
      "effect": {
        "span": "will yield a population dividend"
      }
    },
    {
      "cause": {
        "span": "a population dividend"
      },
      "relation": "caused",
      "effect": {
        "span": "will raise our nation"
      }
    }
  ]
}
```

### --- id=4341 ---

输入文本: Selected patients in low risk groups who are fully vaccinated, asymptomatic, with a negative lateral flow test on the day of their procedure will no longer need to have a negative PCR and isolate for 3 days.

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
        "span": "Selected patients in low risk groups who are fully vaccinated, asymptomatic, with a negative lateral flow test on the day of their procedure"
      },
      "relation": "caused",
      "effect": {
        "span": "will no longer need to have a negative PCR and isolate for 3 days"
      }
    }
  ]
}
```

### --- id=14258 ---

输入文本: Recent developments in the global political landscape have created obstacles to the development of multilateralism, thereby putting it at risk.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "have created obstacles",
      "effect": "putting it at risk"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Recent developments in the global political landscape"
      },
      "relation": "caused",
      "effect": {
        "span": "created obstacles to the development of multilateralism"
      }
    },
    {
      "cause": {
        "span": "Recent developments in the global political landscape"
      },
      "relation": "caused",
      "effect": {
        "span": "putting it at risk"
      }
    }
  ]
}
```

### --- id=13734 ---

输入文本: Those summits, among other things, recognized the need for partnerships with communities and the private sector as key in securing wildlife and enhancing economic benefits from wildlife.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "partnerships",
      "effect": "securing"
    },
    {
      "cause": "partnerships",
      "effect": "enhancing"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "partnerships with communities and the private sector"
      },
      "relation": "caused",
      "effect": {
        "span": "securing wildlife and enhancing economic benefits from wildlife"
      }
    }
  ]
}
```

### --- id=4705 ---

输入文本: Even before the Omicron wave we had a COVID backlog of elective care, and now, unfortunately, that COVID backlog will be larger still.

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
        "span": "the Omicron wave"
      },
      "relation": "caused",
      "effect": {
        "span": "that COVID backlog will be larger still"
      }
    }
  ]
}
```

### --- id=13995 ---

输入文本: Secondly, with regard to the fight against climate change, if we are to succeed, we must be aware that the harmful effects of climate change directly affect the increase in poverty and global economic and social inequality.

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
      "cause": "harmful effects of climate change",
      "effect": "affect the increase"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the harmful effects of climate change"
      },
      "relation": "caused",
      "effect": {
        "span": "the increase in poverty and global economic and social inequality"
      }
    }
  ]
}
```

### --- id=13766 ---

输入文本: With regard to international solidarity, for 2021-2025, Luxembourg will allocate €200 million for financial and technical assistance to combat climate change in developing countries, with priority given to the least developed countries and small island developing States.

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
        "span": "Luxembourg will allocate €200 million for financial and technical assistance"
      },
      "relation": "caused",
      "effect": {
        "span": "combat climate change in developing countries"
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

### --- id=11381 ---

输入文本: As a result of these initiatives, in times of turbulence for the regional and perhaps the global economy, our growth has surpassed the average growth of the countries of the region, which has merited the major recognition of the world’s investors.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "our growth has surpassed the average growth of the countries of the region",
      "effect": "merited the major recognition of the world’s investors"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "these initiatives"
      },
      "relation": "caused",
      "effect": {
        "span": "our growth has surpassed the average growth of the countries of the region"
      }
    },
    {
      "cause": {
        "span": "our growth has surpassed the average growth of the countries of the region"
      },
      "relation": "caused",
      "effect": {
        "span": "merited the major recognition of the world’s investors"
      }
    }
  ]
}
```

### --- id=2670 ---

输入文本: We achieved our goal of defeating those who wrought horrendous terror on that city 20 years ago.

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
        "span": "those who wrought horrendous terror on that city 20 years ago"
      },
      "relation": "caused",
      "effect": {
        "span": "horrendous terror on that city 20 years ago"
      }
    }
  ]
}
```

### --- id=17034 ---

输入文本: I stress the importance in that regard of implementing Security Council resolution 2354 (2017), on the implementation of the comprehensive international framework to counter terrorist narratives, which was adopted on the basis of an Egyptian initiative to uphold the values of tolerance and the renewal of religious discourse.

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
        "span": "Egyptian initiative"
      },
      "relation": "caused",
      "effect": {
        "span": "comprehensive international framework to counter terrorist narratives"
      }
    }
  ]
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
        "span": "protecting the ocean"
      },
      "relation": "caused",
      "effect": {
        "span": "tackle it"
      }
    }
  ]
}
```

### --- id=13132 ---

输入文本: In order to finance those national development plans and strategies, we have mobilized the resources required from every source available, undertaking initiatives to promote domestic investment, attract high-quality foreign direct investment, carry out tax reform, diversify the economy and promote public-private partnerships in order to finance our national development agenda.

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
      "cause": "have mobilized the resources required from every source available, undertaking initiatives to promote domestic investment, attract high-quality foreign direct investment, carry out tax reform, diversify the economy and promote public-private partnerships",
      "effect": "in order to finance our national development agenda"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "mobilized the resources required from every source available, undertaking initiatives to promote domestic investment, attract high-quality foreign direct investment, carry out tax reform, diversify the economy and promote public-private partnerships"
      },
      "relation": "caused",
      "effect": {
        "span": "finance our national development agenda"
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

### --- id=12745 ---

输入文本: To improve our resilience, we need a One Health approach.

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
      "cause": "need a One Health approach",
      "effect": "improve our resilience"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a One Health approach"
      },
      "relation": "caused",
      "effect": {
        "span": "improve our resilience"
      }
    }
  ]
}
```

### --- id=527 ---

输入文本: With 1 in 3 people with COVID-19 showing no symptoms, it is easy to pass it onto others without knowing.

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
        "span": "1 in 3 people with COVID-19 showing no symptoms"
      },
      "relation": "caused",
      "effect": {
        "span": "it is easy to pass it onto others without knowing"
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
        "span": "support us in this process"
      },
      "relation": "caused",
      "effect": {
        "span": "it is transparent and credible"
      }
    }
  ]
}
```

### --- id=15437 ---

输入文本: The CNRD has already taken measures to ease the sociopolitical and economic situation, including the release of people arrested during opposition demonstrations and the reopening of air, land and sea borders to ensure the free movement of people and goods and promote good-neighbourly relations.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 5
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 5
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 5
  },
  "gold_relations": [
    {
      "cause": "taken measures",
      "effect": "ease the sociopolitical and economic situation"
    },
    {
      "cause": "taken measures",
      "effect": "release of people arrested during opposition demonstrations"
    },
    {
      "cause": "taken measures",
      "effect": "reopening of air, land and sea borders"
    },
    {
      "cause": "taken measures",
      "effect": "ensure the free movement of people and goods"
    },
    {
      "cause": "taken measures",
      "effect": "promote good-neighbourly relations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the reopening of air, land and sea borders"
      },
      "relation": "caused",
      "effect": {
        "span": "ensure the free movement of people and goods"
      }
    },
    {
      "cause": {
        "span": "the reopening of air, land and sea borders"
      },
      "relation": "caused",
      "effect": {
        "span": "promote good-neighbourly relations"
      }
    }
  ]
}
```

### --- id=6676 ---

输入文本: Time and experience have shown us that common problems are best tackled through unity, and we already have the tools and knowledge to overcome such a test and succeed.

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
      "cause": "have",
      "effect": "overcome such a test and succeed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "unity"
      },
      "relation": "caused",
      "effect": {
        "span": "common problems are best tackled"
      }
    }
  ]
}
```

### --- id=14259 ---

输入文本: However, the increasingly evident interrelationships among various global challenges have highlighted the need, today more than ever, for Member States to work together in order to overcome these difficulties.

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
        "span": "Member States to work together"
      },
      "relation": "caused",
      "effect": {
        "span": "overcome these difficulties"
      }
    }
  ]
}
```

### --- id=16044 ---

输入文本: Every forum and dialogue, formal or informal, should be used to engage Russia in discussions on the strict implementation of the ceasefire agreement and on allowing the European Union Monitoring Mechanism, as was agreed, to monitor all Georgian territory, because de-escalation along the line of occupation is our top priority, which would then pave the way towards an effective settlement.

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
        "span": "de-escalation along the line of occupation"
      },
      "relation": "caused",
      "effect": {
        "span": "pave the way towards an effective settlement"
      }
    }
  ]
}
```

### --- id=13231 ---

输入文本: However, plastic pollution carries toxic pollutants into our own food chain.

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
        "span": "plastic pollution"
      },
      "relation": "caused",
      "effect": {
        "span": "carries toxic pollutants into our own food chain"
      }
    }
  ]
}
```

### --- id=12283 ---

输入文本: I believe that our Government’s achievements in dealing with the global health and climate change crises will contribute to the efforts of the international community to recover from COVID-19 and build sustainable socioeconomic resilience.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "achievements in dealing with the global health and climate change crises",
      "effect": "contribute to the efforts of the international community to recover from COVID-19"
    },
    {
      "cause": "achievements in dealing with the global health and climate change crises",
      "effect": "build sustainable socioeconomic resilience"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "our Government’s achievements in dealing with the global health and climate change crises"
      },
      "relation": "caused",
      "effect": {
        "span": "the efforts of the international community to recover from COVID-19 and build sustainable socioeconomic resilience"
      }
    }
  ]
}
```
