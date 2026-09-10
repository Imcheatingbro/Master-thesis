# Gemma 4 26B A4B QAT politicause Fixed + RAG eval report

## 配置
```json
{
  "label": "Gemma 4 26B A4B QAT politicause Fixed + RAG",
  "model": "google/gemma-4-26b-a4b-qat",
  "dataset": "politicause",
  "sample_count": 860,
  "prompt_name": "politicause_v1_final",
  "use_rag": true,
  "rag_mode": "knn_pattern",
  "rag_top_k": 1,
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
  "metadata_path": "D:\\Master thesis\\RAG Database\\politicause_examples.jsonl",
  "embeddings_path": "D:\\Master thesis\\RAG Database\\politicause_embeddings.npy"
}
```

## 统计指标
```text
================ Gemma 4 26B A4B QAT politicause Fixed + RAG final report ================
样本总数: 860
  Gold 含因果: 245 | Pred 含因果: 290
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.834
  Precision: 0.676
  Recall   : 0.800
  F1       : 0.733
  (TP=196, TN=521, FP=94, FN=49)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 860
    Gold triples: 245 | Pred triples: 290
    Precision: 0.293
    Recall   : 0.347
    F1       : 0.318
    (TP=85, FP=205, FN=160)
  [anchor_window] (primary)
    样本数: 860
    Gold triples: 245 | Pred triples: 290
    Precision: 0.579
    Recall   : 0.686
    F1       : 0.628
    (TP=168, FP=122, FN=77)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 196
    Gold triples: 196 | Pred triples: 196
    Precision: 0.434
    Recall   : 0.434
    F1       : 0.434
    (TP=85, FP=111, FN=111)
  [anchor_window] (primary)
    样本数: 196
    Gold triples: 196 | Pred triples: 196
    Precision: 0.857
    Recall   : 0.857
    F1       : 0.857
    (TP=168, FP=28, FN=28)
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

Sample details shown: all 171 wrong samples from 860 total samples.

### --- id=12317 ---

输入文本: Let us work together to give them a future to blossom in peace.

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
        "span": "work together"
      },
      "effect": {
        "span": "to give them a future to blossom in peace"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1697 ---

输入文本: If the world can incentivise them to go this direction, then this twenty-year presence of the coalition forces in Afghanistan would not be wasted after all.

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
        "span": "If the world can incentivise them to go this direction"
      },
      "effect": {
        "span": "this twenty-year presence of the coalition forces in Afghanistan would not be wasted after all"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16758 ---

输入文本: We also believe that we cannot achieve universal health coverage without delivering mental health care for all.

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
        "span": "delivering mental health care for all"
      },
      "effect": {
        "span": "achieve universal health coverage"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2233 ---

输入文本: Recently, Uganda experienced impacts of intensive and prolonged droughts and rainfall, severely impacting lives and livelihoods.

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
      "cause": "impacts of intensive and prolonged droughts and rainfall",
      "effect": "impacting lives and livelihoods"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "intensive and prolonged droughts and rainfall"
      },
      "effect": {
        "span": "severely impacting lives and livelihoods"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=238 ---

输入文本: Every pregnant woman who has not yet been vaccinated should feel confident to go and get the jab, and that this will help to prevent the serious consequences of catching COVID-19 in pregnancy.

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
      "cause": "get the jab",
      "effect": "this will help to prevent the serious consequences of catching COVID-19 in pregnancy"
    }
  ],
  "pred_triples": []
}
```

### --- id=2778 ---

输入文本: As a Small Island Developing State, Solomon Islands continues to battle with the incremental effects of climate change and its negative impacts that threaten the livelihoods, security, and well-being of our people.

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
        "span": "incremental effects of climate change and its negative impacts"
      },
      "effect": {
        "span": "threaten the livelihoods, security, and well-being of our people"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14872 ---

输入文本: First, with regard to North Korea, Japan supports the approach President Trump has taken, which has allowed the two leaders to talk candidly with each other and try to work out the issues at hand, while looking ahead to a bright future.

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
      "cause": "supports the approach",
      "effect": "talk candidly"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the approach President Trump has taken"
      },
      "effect": {
        "span": "which has allowed the two leaders to talk candidly with each other and try to work out the issues at hand"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9339 ---

输入文本: Health and Social Care Secretary, Sajid Javid, said: The tireless efforts of NHS and care staff, and the army of volunteers, as well as the phenomenal response of the British public means over 37 million people have been boosted.

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
        "span": "The tireless efforts of NHS and care staff, and the army of volunteers, as well as the phenomenal response of the British public"
      },
      "effect": {
        "span": "means over 37 million people have been boosted"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15713 ---

输入文本: Securing climate financing is the main priority for Tonga, as without it no action on our nationally determined contributions is possible.

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
        "span": "Securing climate financing"
      },
      "effect": {
        "span": "no action on our nationally determined contributions is possible"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15447 ---

输入文本: We have to ensure that adequate and sustainable financing is available to support the responses from the Resident Coordinators to the needs of the most vulnerable.

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
      "cause": "ensure that adequate and sustainable financing is available",
      "effect": "support the responses from the Resident Coordinators to the needs of the most vulnerable"
    }
  ],
  "pred_triples": []
}
```

### --- id=12568 ---

输入文本: We are taking the lead in delivering development to our people and working with our valuable international partners to ensure we rebuild a democratic, inclusive and economically prosperous Somalia.

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
        "span": "working with our valuable international partners"
      },
      "effect": {
        "span": "to ensure we rebuild a democratic, inclusive and economically prosperous Somalia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=7600 ---

输入文本: Voiced by Dr Helen Lawal, the film demonstrates how, in a home setting, someone infected with the virus talking and interacting with another person produces a build-up of COVID-19 particles in the air.

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
      "cause": "in a home setting, someone infected with the virus talking and interacting with another person",
      "effect": "produces a build-up of COVID-19 particles in the air"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "someone infected with the virus talking and interacting with another person"
      },
      "effect": {
        "span": "produces a build-up of COVID-19 particles in the air"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=394 ---

输入文本: You all went into health and care because you want to help people.

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
      "cause": "you want to help people",
      "effect": "went into health and care"
    }
  ],
  "pred_triples": []
}
```

### --- id=8066 ---

输入文本: New variants are the most serious risk to global recovery from the pandemic, particularly those which have characteristics that make them more transmissible, cause more severe illness or are more likely to evade immune responses developed from vaccination or prior infection.

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
      "cause": "those",
      "effect": "more severe illness"
    }
  ],
  "pred_triples": []
}
```

### --- id=12933 ---

输入文本: We are now working assiduously to correct that, given the adverse effects that this glaring gap has had on Government’s ability to manage its macroeconomic affairs.

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
      "cause": "given the adverse effects that this glaring gap has had on Government’s ability to manage its macroeconomic affairs",
      "effect": "working assiduously to correct that"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "this glaring gap has had"
      },
      "effect": {
        "span": "adverse effects that this glaring gap has had on Government’s ability to manage its macroeconomic affairs"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12739 ---

输入文本: There’s no question that the new variants have made this fight a whole lot tougher.

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
      "cause": "the new variants",
      "effect": "have made this fight a whole lot tougher."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the new variants"
      },
      "effect": {
        "span": "have made this fight a whole lot tougher"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4284 ---

输入文本: The conference will bring together over 190 states to discuss issues relating to international travel, helping to achieve a common approach for aviation recovery as we continue to collaborate with our international partners in response to the pandemic.

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
        "span": "The conference will bring together over 190 states to discuss issues relating to international travel"
      },
      "effect": {
        "span": "helping to achieve a common approach for aviation recovery"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4329 ---

输入文本: Vaccinated people are far less likely to get COVID-19 with symptoms and are less likely to get serious COVID-19, to be admitted to hospital, or to die from it.

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
        "span": "Vaccinated people"
      },
      "effect": {
        "span": "are far less likely to get COVID-19 with symptoms and are less likely to get serious COVID-19, to be admitted to hospital, or to die from it"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4792 ---

输入文本: Health and Social Care Secretary Sajid Javid said: We can learn to live with COVID-19 if everybody gets their vaccines and booster jabs.

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
        "span": "everybody gets their vaccines and booster jabs"
      },
      "effect": {
        "span": "We can learn to live with COVID-19"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9509 ---

输入文本: At the same time, injustice generates instability, power struggles, crises, waste and extravagance.

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
        "span": "injustice"
      },
      "effect": {
        "span": "generates instability, power struggles, crises, waste and extravagance"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13334 ---

输入文本: Consistent with its sense of responsibility to establish stability in the region and the entire world, and in line with its historic role and commitment to joint action with its brothers, allies and international partners to address international and regional challenges, as well as combating terrorism and piracy in the Arabian Gulf, the Kingdom of Bahrain joined the International Maritime Security Construct at this critical and important period to safeguard the most important international strategic maritime lanes, which are vital for commerce and energy.

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
      "cause": "joined the International Maritime Security Construct at this critical and important period",
      "effect": "safeguard the most important international strategic maritime lanes, which are vital for commerce and energy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Kingdom of Bahrain joined the International Maritime Security Construct"
      },
      "effect": {
        "span": "to safeguard the most important international strategic maritime lanes, which are vital for commerce and energy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16636 ---

输入文本: In this regard, Chad welcomes the momentum for dialogue and reconciliation that has begun in the Central African Republic, the Sudan and South Sudan, and urges all relevant stakeholders to redouble their efforts to achieve lasting peace in these brotherly countries.

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
      "cause": "redouble their efforts",
      "effect": "achieve"
    }
  ],
  "pred_triples": []
}
```

### --- id=480 ---

输入文本: JCVI will continue to closely review all available data to develop further advice in due course.

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
        "span": "will continue to closely review all available data"
      },
      "effect": {
        "span": "to develop further advice in due course"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=7106 ---

输入文本: Therefore, despite the weakness of the economy and the persistence of other impacts, in particular with respect to security and climate, the Government took bold measures to maintain a positive growth rate of 3 per cent in 2020.

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
        "span": "the Government took bold measures"
      },
      "effect": {
        "span": "to maintain a positive growth rate of 3 per cent in 2020"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=11723 ---

输入文本: The States Members of the Organization have increasingly yearned for its reform in order to make it more democratic and responsive to the needs of all nations, rich and poor, big and small, strong and weak.

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
      "cause": "have increasingly yearned for its reform",
      "effect": "make it more democratic and responsive to the needs"
    }
  ],
  "pred_triples": []
}
```

### --- id=13351 ---

输入文本: In recent years, Andorra has promoted inclusive educational policies aimed at providing our young people with the tools they need to develop their potential in a multicultural and global world.

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
        "span": "has promoted inclusive educational policies"
      },
      "effect": {
        "span": "aimed at providing our young people with the tools they need to develop their potential in a multicultural and global world"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9012 ---

输入文本: There remains a huge pent-up demand for international travel and we’ve seen strong and sustained booking patterns since the announcement as customers look to go abroad with ease and without the added expense of testing.

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
      "cause": "customers look to go abroad with ease and without the added expense of testing",
      "effect": "strong and sustained booking patterns"
    }
  ],
  "pred_triples": []
}
```

### --- id=13482 ---

输入文本: We continue to be deeply concerned about the situation in Libya, which is still having a negative impact on the entire Sahel region.

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
        "span": "the situation in Libya"
      },
      "effect": {
        "span": "which is still having a negative impact on the entire Sahel region"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16386 ---

输入文本: As I conclude my statement, I want to underscore that it is not our rhetoric delivered from this rostrum that will change the global socioeconomic, political and security trajectory but rather our willingness to put our words into action that will usher the world out of ongoing misery.

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
        "span": "our willingness to put our words into action"
      },
      "effect": {
        "span": "will usher the world out of ongoing misery"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8300 ---

输入文本: The best way to protect yourself and others against COVID-19 is to get the vaccine – please make sure to get it if you are eligible.

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
        "span": "get the vaccine"
      },
      "effect": {
        "span": "protect yourself and others against COVID-19"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=6231 ---

输入文本: This situation compromises the ethical values of democracy and affects the competitiveness of the State and the economy.

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
        "span": "This situation"
      },
      "effect": {
        "span": "compromises the ethical values of democracy and affects the competitiveness of the State and the economy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13286 ---

输入文本: Starting in 2020, for example, Monaco will be increasing its international funding aimed at preserving and regenerating biodiversity, while mitigating and promoting adaptation to climate change and improving the resilience of vulnerable populations.

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
      "cause": "increasing its international funding",
      "effect": "preserving and regenerating biodiversity"
    }
  ],
  "pred_triples": []
}
```

### --- id=5950 ---

输入文本: In particular, Tocilizumab, sorry I’ll say it again, Tocilizumab and Sarilumab, they’ll shortly be on everybody’s lips which have been found to reduce the risk of death for critically ill patients by almost a quarter and they’ve cut time spent in intensive care by as much as ten days and these lifesaving drugs will be available through the NHS with immediate effect, potentially saving thousands of lives.

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
        "span": "these lifesaving drugs will be available through the NHS with immediate effect"
      },
      "effect": {
        "span": "potentially saving thousands of lives"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5892 ---

输入文本: The natural rate of R is around 3, meaning local restrictions have helped slow the spread of the virus, whilst NHS Test and Trace is testing more than any other country in Europe.

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
      "cause": "local restrictions",
      "effect": "helped slow the spread of the virus"
    }
  ],
  "pred_triples": []
}
```

### --- id=17440 ---

输入文本: We hope that in the not too distant future that authority will regulate the energy space to facilitate more investment into, and development of, the different energy options, especially the clean energy sources that we advocate.

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
      "cause": "regulate the energy space",
      "effect": "facilitate more investment into, and development of, the different energy options"
    }
  ],
  "pred_triples": []
}
```

### --- id=16722 ---

输入文本: In that regard, we support the peaceful resolution of the ongoing conflicts and crises around the world by promoting dialogue between all political and military forces under the auspices of the United Nations.

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
      "cause": "promoting dialogue",
      "effect": "support the peaceful resolution"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "by promoting dialogue between all political and military forces under the auspices of the United Nations"
      },
      "effect": {
        "span": "the peaceful resolution of the ongoing conflicts and crises around the world"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16557 ---

输入文本: Among the plans for reform, we support with special conviction the Secretary-General’s commitment to the empowerment of women and girls and the achievement of gender equality as instruments for strengthening the effectiveness of the Organization.

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
        "span": "the Secretary-General’s commitment to the empowerment of women and girls and the achievement of gender equality"
      },
      "effect": {
        "span": "as instruments for strengthening the effectiveness of the Organization"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=17148 ---

输入文本: To fail to prepare young people is to prepare a generation to fail.

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
        "span": "To fail to prepare young people"
      },
      "effect": {
        "span": "to prepare a generation to fail"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3628 ---

输入文本: The Bolivian people, however, courageously and determinedly stopped the organized and systematic attempt to overthrow democracy and reinstall the dictatorship in Bolivia.

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
        "span": "The Bolivian people, however, courageously and determinedly stopped the organized and systematic attempt to overthrow democracy and reinstall the dictatorship in Bolivia"
      },
      "effect": {
        "span": "the organized and systematic attempt to overthrow democracy and reinstall the dictatorship in Bolivia"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13423 ---

输入文本: Following extensive geothermal exploration, it was confirmed in 2012 that the reservoir in the Roseau Valley, the subject of exploration, had a potential of 120 megawatts, which would not only satisfy domestic needs but could potentially produce electricity for export to the neighbouring French islands of Martinique and Guadeloupe, thereby reducing their carbon footprint as well.

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
      "cause": "produce electricity for export to the neighbouring French islands of Martinique and Guadeloupe",
      "effect": "reducing their carbon footprint"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the reservoir in the Roseau Valley, the subject of exploration, had a potential of 120 megawatts"
      },
      "effect": {
        "span": "which would not only satisfy domestic needs but could potentially produce electricity for export to the neighbouring French islands of Martinique and Guadeloupe, thereby reducing their carbon footprint as well"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8106 ---

输入文本: The government is working closely with international counterparts to ensure a longer-term solution can be reached for these individuals, and is in active conversations with other countries through groups such as the G7, the EU Commission and the World Health Organization (WHO).

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
        "span": "The government is working closely with international counterparts"
      },
      "effect": {
        "span": "to ensure a longer-term solution can be reached for these individuals"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13621 ---

输入文本: As for migration, how we respond to the needs of those forced to leave their homes due to conflict and instability is a moral test of our times and our common humanity.

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
      "cause": "conflict and instability",
      "effect": "forced to leave"
    }
  ],
  "pred_triples": []
}
```

### --- id=2414 ---

输入文本: We must commit to achieving climate neutrality through reform and investments in the areas of energy efficiency, renewable energy, sustainable mobility and circular business models.

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
      "cause": "reform and investments in the areas of energy efficiency, renewable energy, sustainable mobility and circular business models",
      "effect": "achieving climate neutrality"
    }
  ],
  "pred_triples": []
}
```

### --- id=967 ---

输入文本: Professor Steven Riley, Director General of Data, Analytics and Surveillance at UKHSA, said: As we observe the Omicron variant emerging, the Delta variant continues to circulate at high levels across all age ranges, and is still causing substantial infection and hospitalisation in older people.

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
        "span": "the Delta variant"
      },
      "effect": {
        "span": "substantial infection and hospitalisation in older people"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1718 ---

输入文本: As I mentioned earlier, due to unbalanced growth and development, the world is facing a growing existential threat of natural catastrophes connected with climate change on an unprecedented scale.

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
      "cause": "unbalanced growth and development",
      "effect": "facing a growing existential threat of natural catastrophes connected with climate change on an unprecedented scale"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "unbalanced growth and development"
      },
      "effect": {
        "span": "the world is facing a growing existential threat of natural catastrophes"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9288 ---

输入文本: Anyone over the age of 50 or between 18 to 49 with certain underlying health conditions can sign up to the study as soon as they receive a positive PCR or lateral flow test result.

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
      "effect": {
        "span": "can sign up to the study"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2547 ---

输入文本: The humanitarian needs in the country are immense, and it is critical that we act together to ensure that the people have access to humanitarian assistance.

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
      "cause": "we act",
      "effect": "ensure that the people have access to humanitarian assistance"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "act together"
      },
      "effect": {
        "span": "to ensure that the people have access to humanitarian assistance"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=17565 ---

输入文本: We have long said that climate change poses a very serious existential threat to our national security and well-being.

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
      "cause": "climate change",
      "effect": "poses a very serious existential threat"
    }
  ],
  "pred_triples": []
}
```

### --- id=17057 ---

输入文本: Over the next five years, we will collaborate with farmers to build systems in New Zealand that every farmer will be able to use to measure, manage and reduce their own farm’s emissions.

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
        "span": "we will collaborate with farmers"
      },
      "effect": {
        "span": "to build systems in New Zealand that every farmer will be able to use to measure, manage and reduce their own farm’s emissions"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13393 ---

输入文本: They are the real challenges that we must tackle together if we are to energize multilateral efforts to eradicate poverty, promote quality education, address climate change and foster inclusion.

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
        "span": "tackle together"
      },
      "effect": {
        "span": "to energize multilateral efforts to eradicate poverty, promote quality education, address climate change and foster inclusion"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10790 ---

输入文本: Such Israeli violations would not continue to escalate were it not for the blind support of certain countries that are fully responsible for the consequences of Israel’s actions.

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
        "span": "the blind support of certain countries"
      },
      "effect": {
        "span": "Such Israeli violations would not continue to escalate"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=6936 ---

输入文本: Thirdly, development priorities and needs must be mainstreamed into all humanitarian aid activities to spur early recovery by focusing on socioeconomic activities and implementing the Sustainable Development Goals.

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
        "span": "development priorities and needs must be mainstreamed into all humanitarian aid activities"
      },
      "effect": {
        "span": "to spur early recovery by focusing on socioeconomic activities and implementing the Sustainable Development Goals"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=11094 ---

输入文本: Its borders define the tragedy spawned by 70 years of military confrontation, but, paradoxically, it has become a pristine ecological treasure trove.

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
        "span": "70 years of military confrontation"
      },
      "effect": {
        "span": "the tragedy spawned by 70 years of military confrontation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12097 ---

输入文本: Now is the time to turn hope into meaningful action, for the benefit of all our peoples.

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
      "cause": "meaningful action",
      "effect": "benefit"
    }
  ],
  "pred_triples": []
}
```

### --- id=10730 ---

输入文本: We urge the international community to mobilize the necessary financial resources to support those efforts.

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
        "span": "urge the international community to mobilize the necessary financial resources"
      },
      "effect": {
        "span": "to support those efforts"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=11327 ---

输入文本: We are also in the process of establishing a plastic-recycling plant that will enable our country to become plastic-neutral.

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
      "cause": "establishing a plastic-recycling plant",
      "effect": "will enable our country to become plastic-neutral"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "establishing a plastic-recycling plant"
      },
      "effect": {
        "span": "enable our country to become plastic-neutral"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=11636 ---

输入文本: It is true that the number of new cases is growing fastest amongst those aged 20-29, but the evidence shows that the virus is spreading to other more vulnerable age groups, as we have seen in France and Spain where this has led to increased hospital admissions and, sadly, more deaths.

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
        "span": "the virus is spreading to other more vulnerable age groups"
      },
      "effect": {
        "span": "this has led to increased hospital admissions and, sadly, more deaths"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5846 ---

输入文本: In order to overcome the shocks of the COVID-19 pandemic, we need to seriously address the issue of developing countries’ debt.

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
      "cause": "need to seriously address the issue of developing countries’ debt",
      "effect": "overcome the shocks of the COVID-19 pandemic"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "seriously address the issue of developing countries’ debt"
      },
      "effect": {
        "span": "in order to overcome the shocks of the COVID-19 pandemic"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8889 ---

输入文本: The NHS will prepare to extend this non-urgent offer to all children during April so parents can, if they want, take up the offer to increase protection against potential future waves of COVID-19 as we learn to live with this virus.

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
        "span": "The NHS will prepare to extend this non-urgent offer to all children during April"
      },
      "effect": {
        "span": "so parents can, if they want, take up the offer to increase protection against potential future waves of COVID-19"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2609 ---

输入文本: In order to confront the urgency of the pandemic, Governments across the globe reallocated funds to meet desperate needs.

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
      "cause": "reallocated funds to meet desperate needs",
      "effect": "confront the urgency of the pandemic"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Governments across the globe reallocated funds"
      },
      "effect": {
        "span": "to meet desperate needs"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4871 ---

输入文本: Mr Deputy Speaker, we’ve now entered the third year of this country’s fight against COVID-19 and thanks to an incredible national endeavour, we’re now better protected than ever before.

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
        "span": "thanks to an incredible national endeavour"
      },
      "effect": {
        "span": "we’re now better protected than ever before"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15705 ---

输入文本: For all of these reasons, here, on this world stage, I courageously express to the international community that Colombia will continue to be committed to the defence of democracy in Venezuela, but, my fellow representatives, without the support of this community, without the true support of the States Members of the United Nations, those who left their homes with the desire to return will not easily find their way back.

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
        "span": "without the true support of the States Members of the United Nations"
      },
      "effect": {
        "span": "those who left their homes with the desire to return will not easily find their way back"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12776 ---

输入文本: Algeria is prepared to continue its efforts and support our Libyan brothers, while enabling them to benefit from the Algerian experience in the area of national reconciliation.

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
        "span": "continue its efforts and support our Libyan brothers"
      },
      "effect": {
        "span": "enabling them to benefit from the Algerian experience in the area of national reconciliation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8391 ---

输入文本: The pandemic is not over but vaccination is weakening the link between infection and serious illness.

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
        "span": "vaccination"
      },
      "effect": {
        "span": "is weakening the link between infection and serious illness"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15948 ---

输入文本: Likewise, the United Nations must engage with the people of West Papua to find lasting solutions to their struggle.

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
      "cause": "must engage",
      "effect": "find"
    }
  ],
  "pred_triples": []
}
```

### --- id=5747 ---

输入文本: France hopes that the Security Council, Libya’s neighbours and those which have influence over the country can collaborate to achieve our shared objective of completing the ongoing transition.

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
      "cause": "collaborate",
      "effect": "achieve our shared objective of completing the ongoing transition"
    }
  ],
  "pred_triples": []
}
```

### --- id=7723 ---

输入文本: Vaccinated people are far less likely to get COVID-19 with symptoms and even more unlikely to get serious COVID-19, to be admitted to hospital, or to die from the virus.

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
        "span": "Vaccinated people"
      },
      "effect": {
        "span": "are far less likely to get COVID-19 with symptoms and even more unlikely to get serious COVID-19, to be admitted to hospital, or to die from the virus"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13083 ---

输入文本: No effort must be spared to ensure their full reintegration into society.

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
        "span": "No effort must be spared"
      },
      "effect": {
        "span": "to ensure their full reintegration into society"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5942 ---

输入文本: Because it would be an absolute tragedy if in our eagerness, we were to boost the nutjobs – the anti vaxxers, dangerous obsessives who campaign against the whole concept of vaccination and who would risk further millions of lives.

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
        "span": "if in our eagerness, we were to boost the nutjobs – the anti vaxxers, dangerous obsessives who campaign against the whole concept of vaccination and who would risk further millions of lives"
      },
      "effect": {
        "span": "it would be an absolute tragedy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12680 ---

输入文本: The Government of Tanzania spends between 2 and 3 per cent of our gross domestic product on mitigation and on building community resilience, and that is a lot in a country that is still grappling with poverty, along with the COVID-19 pandemic emergency, which itself has compromised our capacity to respond to the harmful impact of climate change.

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
      "cause": "the COVID-19 pandemic emergency",
      "effect": "has compromised our capacity to respond to the harmful impact of climate change"
    }
  ],
  "pred_triples": []
}
```

### --- id=17381 ---

输入文本: It is no secret that the pandemic has placed enormous strain on developing economies.

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
      "cause": "the pandemic",
      "effect": "placed enormous strain on developing economies"
    }
  ],
  "pred_triples": []
}
```

### --- id=15872 ---

输入文本: I also emphasized how corruption had become a cancer that was preventing us from taking advantage of all the potential that we have to achieve greater levels of progress and development, in the face of which my Government could not stand by idly.

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
        "span": "corruption"
      },
      "effect": {
        "span": "was preventing us from taking advantage of all the potential that we have to achieve greater levels of progress and development"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5581 ---

输入文本: I hope that by working together, we can get that great city on top of the virus.

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
      "cause": "by working together",
      "effect": "get that great city on top of the virus"
    }
  ],
  "pred_triples": []
}
```

### --- id=4906 ---

输入文本: If they have not received a PCR test kit they can arrange to have a PCR test.

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
        "span": "If they have not received a PCR test kit"
      },
      "effect": {
        "span": "they can arrange to have a PCR test"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=7644 ---

输入文本: In clinical trials, Lagevrio was found to be effective in reducing the risk of hospitalisation or death for at-risk non-hospitalised adults with mild to moderate COVID-19 by 50%.

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
      "cause": "Lagevrio was found to be effective",
      "effect": "reducing the risk of hospitalisation or death for at-risk non-hospitalised adults with mild to moderate COVID-19"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Lagevrio"
      },
      "effect": {
        "span": "be effective in reducing the risk of hospitalisation or death for at-risk non-hospitalised adults with mild to moderate COVID-19 by 50%"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10785 ---

输入文本: Having failed to achieve their goals through armed terrorism, those countries have resorted to economic terrorism, which is an equally brutal form of terrorism, by imposing a blockade and unilateral coercive economic measures.

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
      "cause": "imposing a blockade and unilateral coercive economic measures",
      "effect": "have resorted to economic terrorism"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Having failed to achieve their goals through armed terrorism"
      },
      "effect": {
        "span": "those countries have resorted to economic terrorism"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3513 ---

输入文本: In this regard, I would like to take this opportunity to express our heartfelt congratulation to the efforts made by international organizations, in particular the World Health Organization and all countries for the assistance extended to other member states who are facing difficulties, which enables us to control the outbreak of the COVID-19 at a certain level, including the initiative to establish a project to promote and ensure global access to vaccine without discrimination.

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
      "cause": "the efforts made by international organizations, in particular the World Health Organization and all countries for the assistance extended to other member states who are facing difficulties",
      "effect": "which enables us to control the outbreak of the COVID-19 at a certain level"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the assistance extended to other member states who are facing difficulties"
      },
      "effect": {
        "span": "which enables us to control the outbreak of the COVID-19 at a certain level"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12070 ---

输入文本: Morocco believes that it is crucial that elections be organized in Libya as a decisive step on the path to achieving peace in that country.

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
      "cause": "elections be organized in Libya",
      "effect": "achieving peace"
    }
  ],
  "pred_triples": []
}
```

### --- id=11751 ---

输入文本: We need to know so we can prevent this death and this calamity being visited upon the world again.

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
      "cause": "need to know",
      "effect": "prevent"
    }
  ],
  "pred_triples": []
}
```

### --- id=12188 ---

输入文本: For the second year in a row, the world finds itself engulfed by the dark cloud of the coronavirus disease (COVID-19) pandemic, which continues to claim thousands of lives daily.

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
        "span": "the coronavirus disease (COVID-19) pandemic"
      },
      "effect": {
        "span": "which continues to claim thousands of lives daily"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15460 ---

输入文本: In all the discussions about food security, one immediate challenge besides the pandemic is the climate change that has tested the resilience of the food we grow as well as the patience of the growers.

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
      "cause": "climate change",
      "effect": "has tested the resilience of the food we grow as well as the patience of the growers."
    }
  ],
  "pred_triples": []
}
```

### --- id=5143 ---

输入文本: The dose interval between the second dose and booster dose was also reduced from 6 months to 3 months on the advice of the independent Joint Committee on Vaccination and Immunisation (JCVI) – with booking made available one month in advance.

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
        "span": "on the advice of the independent Joint Committee on Vaccination and Immunisation (JCVI)"
      },
      "effect": {
        "span": "The dose interval between the second dose and booster dose was also reduced from 6 months to 3 months"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4948 ---

输入文本: With Omicron continuing to spread widely, I encourage everyone to come forward for their booster dose, or if unvaccinated, for their first 2 doses, to increase their protection against serious illness.

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
        "span": "I encourage everyone to come forward for their booster dose, or if unvaccinated, for their first 2 doses"
      },
      "effect": {
        "span": "to increase their protection against serious illness"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13192 ---

输入文本: In fact, if the philosophy is adequately and wisely implemented, SDG 1, on poverty eradication, will no longer need to be part of the equation.

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
        "span": "if the philosophy is adequately and wisely implemented"
      },
      "effect": {
        "span": "SDG 1, on poverty eradication, will no longer need to be part of the equation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9657 ---

输入文本: Turkey is a rightful successor to the collective heritage of both Eastern and Western civilizations, owing to its geographical location at the centre of the ancient world.

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
        "span": "its geographical location at the centre of the ancient world"
      },
      "effect": {
        "span": "Turkey is a rightful successor to the collective heritage of both Eastern and Western civilizations"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5874 ---

输入文本: They once again underscore the central role of the United Nations and of international organizations in uniting those with differing positions in order to address these dangers, and it is time to address them together.

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
      "cause": "uniting those with differing positions",
      "effect": "in order to address these dangers"
    }
  ],
  "pred_triples": []
}
```

### --- id=11581 ---

输入文本: So from the outset, we were clear that we must chart a course back towards normality as rapidly as possible, by developing the vaccines and treatments that could gradually replace those restrictions.

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
      "cause": "developing the vaccines and treatments that could gradually replace those restrictions",
      "effect": "chart a course back towards normality as rapidly as possible"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "developing the vaccines and treatments"
      },
      "effect": {
        "span": "that could gradually replace those restrictions"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8729 ---

输入文本: If you decided to take part but changed your mind when completing the form, you could exit the website at any stage.

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
        "span": "decided to take part but changed your mind when completing the form"
      },
      "effect": {
        "span": "you could exit the website at any stage"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16836 ---

输入文本: Because of its proximity to neighbouring countries hard hit by the scourge of terrorism, Togo is well aware of the magnitude of the threat and remains on high alert in the face of this asymmetrical threat.

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
      "cause": "its proximity",
      "effect": "is well aware"
    }
  ],
  "pred_triples": []
}
```

### --- id=2893 ---

输入文本: I want the Assembly to know that in spite of all the pressures on our finances in the United Kingdom caused by COVID-19, we have kept that promise to the letter.

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
      "effect": {
        "span": "pressures on our finances in the United Kingdom"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=822 ---

输入文本: While rates of severe disease and death due to COVID-19 remain low, hospital admissions have risen and we will therefore continue to monitor this data closely.

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
      "cause": "hospital admissions have risen",
      "effect": "continue to monitor this data closely"
    }
  ],
  "pred_triples": []
}
```

### --- id=9022 ---

输入文本: New data released today, Thursday 10 February, from Hinge shows users who share their vaccination status on dating apps receive 30% more matches than those who don’t.

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
        "span": "users who share their vaccination status on dating apps"
      },
      "effect": {
        "span": "receive 30% more matches than those who don’t"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1069 ---

输入文本: Over the coming year, NVAP will continue to work with the WHO Eastern Mediterranean region to improve regional genomic sequencing hubs in Oman, Abu Dhabi and Morocco.

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
        "span": "will continue to work with the WHO Eastern Mediterranean region"
      },
      "effect": {
        "span": "to improve regional genomic sequencing hubs in Oman, Abu Dhabi and Morocco"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=11288 ---

输入文本: Meanwhile, the climate crisis looms ever larger, heightened by our collective inability to address it — which is why the world needs the United Nations now more than ever.

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
      "cause": "looms ever larger",
      "effect": "needs the United Nations"
    }
  ],
  "pred_triples": []
}
```

### --- id=7361 ---

输入文本: The pandemic has sounded a warning bell of the shocking destruction that results from such non-traditional security challenges as disease or climate change if they are not addressed in a timely and decisive manner.

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
        "span": "such non-traditional security challenges as disease or climate change if they are not addressed in a timely and decisive manner"
      },
      "effect": {
        "span": "the shocking destruction"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12225 ---

输入文本: As one of the Co-Chairs of the Preparatory Committee for the Fifth United Nations Conference on the Least Developed Countries, we expect that a concrete outcome of the Doha conference will be the enabling of more countries to sustainably graduate from the LDC category.

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
      "cause": "concrete outcome of the Doha conference",
      "effect": "sustainably graduate from the LDC category"
    }
  ],
  "pred_triples": []
}
```

### --- id=4894 ---

输入文本: Health and Social Care Secretary Sajid Javid said: Our world-leading testing system is protecting millions of people from COVID-19.

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
        "span": "Our world-leading testing system"
      },
      "effect": {
        "span": "is protecting millions of people from COVID-19"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14853 ---

输入文本: However, they were not only there as onlookers; at the event educational materials on avoiding teenage pregnancy were distributed so that the girls could read them.

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
        "span": "educational materials on avoiding teenage pregnancy were distributed"
      },
      "effect": {
        "span": "so that the girls could read them"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8468 ---

输入文本: The storage temperature for the Valneva vaccine - of 2°C to 8°C - is similar to that of a domestic fridge, making it appropriate for use in countries where storage at very low temperatures is not possible.

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
        "span": "The storage temperature for the Valneva vaccine - of 2°C to 8°C - is similar to that of a domestic fridge"
      },
      "effect": {
        "span": "making it appropriate for use in countries where storage at very low temperatures is not possible"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13703 ---

输入文本: Given the fact that over 80 per cent of rural people’s livelihoods depend on nature, climate change is already having a devastating impact on our people, our lives and our economy.

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
      "cause": "climate change",
      "effect": "having a devastating impact"
    }
  ],
  "pred_triples": []
}
```

### --- id=9018 ---

输入文本: While the red list will continue to remain on standby as our first line of defence against future variants of concern arriving from abroad, the government is looking to replace the hotel quarantine policy with other contingency measures including home isolation – provided a sufficiently robust digital solution to ensure compliance with home isolation can be found.

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
        "span": "a sufficiently robust digital solution to ensure compliance with home isolation can be found"
      },
      "effect": {
        "span": "the government is looking to replace the hotel quarantine policy with other contingency measures including home isolation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12057 ---

输入文本: Australia called for an independent review, and sees understanding the cause of this pandemic, not as a political issue, but as being essential, simply, to prevent the next one.

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
      "cause": "understanding the cause of this pandemic",
      "effect": "prevent the next one"
    }
  ],
  "pred_triples": []
}
```

### --- id=16794 ---

输入文本: We therefore also reject the establishment of the new Independent Investigative Mechanism for Myanmar, which was set up to bring Myanmar before such tribunals as the International Criminal Court, to which we strongly object.

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
        "span": "the establishment of the new Independent Investigative Mechanism for Myanmar"
      },
      "effect": {
        "span": "which was set up to bring Myanmar before such tribunals as the International Criminal Court"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4881 ---

输入文本: Free, centrally procured PPE relieves the financial burden of PPE procurement done on an individual basis, and also enables access to quality PPE of a reliable standard.

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
        "span": "Free, centrally procured PPE"
      },
      "effect": {
        "span": "relieves the financial burden of PPE procurement done on an individual basis, and also enables access to quality PPE of a reliable standard"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15617 ---

输入文本: Ghana has been advocating for ensuring that innovative financing also addresses structural challenges, beyond responding to immediate fiscal needs, by providing mechanisms to facilitate investments in health infrastructure, technology, the environment and people that will foster resilience and equitable recovery.

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
      "cause": "providing mechanisms to facilitate investments in health infrastructure, technology, the environment and people that will foster resilience and equitable recovery",
      "effect": "ensuring that innovative financing also addresses structural challenges"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "providing mechanisms to facilitate investments in health infrastructure, technology, the environment and people"
      },
      "effect": {
        "span": "that will foster resilience and equitable recovery"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15984 ---

输入文本: Kazakhstan will not become a success story of socioeconomic development unless profound political transformation is accomplished.

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
        "span": "profound political transformation is accomplished"
      },
      "effect": {
        "span": "Kazakhstan will not become a success story of socioeconomic development"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15683 ---

输入文本: We will emerge from the triple pandemic that I mentioned at the beginning only through bold leadership, innovative ideas and schemes that make possible what seems to be a chimera.

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
      "cause": "bold leadership, innovative ideas and schemes",
      "effect": "emerge from the triple pandemic"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "only through bold leadership, innovative ideas and schemes"
      },
      "effect": {
        "span": "make possible what seems to be a chimera"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10999 ---

输入文本: We speak out, and we speak loudly, because of the existential vulnerabilities that we suffer in the face of this growing threat.

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
        "span": "the existential vulnerabilities that we suffer in the face of this growing threat"
      },
      "effect": {
        "span": "We speak out, and we speak loudly"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13654 ---

输入文本: Cooperation between the international community and the relevant actors in creating the necessary conditions to end the more than 70 years of conflict is crucial to building a stable and prosperous new Middle East.

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
        "span": "Cooperation between the international community and the relevant actors in creating the necessary conditions to end the more than 70 years of conflict"
      },
      "effect": {
        "span": "is crucial to building a stable and prosperous new Middle East"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8638 ---

输入文本: Pregnant women who develop severe disease have increased rates of admission to intensive care, the need for invasive ventilation and pre-term delivery.

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
        "span": "Pregnant women who develop severe disease"
      },
      "effect": {
        "span": "have increased rates of admission to intensive care, the need for invasive ventilation and pre-term delivery"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=6794 ---

输入文本: We are moving forward with resolve, but we must make a difference by acting together.

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
        "span": "by acting together"
      },
      "effect": {
        "span": "must make a difference"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3636 ---

输入文本: The country continues to enjoy political stability, social order and continued economic growth, which has significantly contributed to the poverty reduction and improving living standard of all multi-ethnic people.

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
      "cause": "continues to enjoy political stability, social order and continued economic growth",
      "effect": "which has significantly contributed to the poverty reduction and improving living standard of all multi-ethnic people"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "political stability, social order and continued economic growth"
      },
      "effect": {
        "span": "which has significantly contributed to the poverty reduction and improving living standard of all multi-ethnic people"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=52 ---

输入文本: Second, we’ve announced measures to slow the spread of the virus here in the UK.

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
        "span": "we’ve announced measures"
      },
      "effect": {
        "span": "to slow the spread of the virus here in the UK"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13137 ---

输入文本: Ukraine has always demonstrated to the world its readiness to ensure peace in a civilized manner and has taken specific steps to ensure international security, such as when it abandoned its nuclear arsenal, which at the time exceeded the nuclear capacities of the United Kingdom, France and China combined.

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
      "cause": "has taken specific steps",
      "effect": "to ensure international security, such as when it abandoned its nuclear arsenal, which at the time exceeded the nuclear capacities of the United Kingdom, France and China combined"
    }
  ],
  "pred_triples": []
}
```

### --- id=13173 ---

输入文本: Paraguay joins States that advocate Security Council reform so as to thereby transform the Council into a more inclusive and transparent body, capable of addressing threats to international peace and security.

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
      "cause": "joins States that advocate Security Council reform",
      "effect": "transform the Council into a more inclusive and transparent body"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "States that advocate Security Council reform"
      },
      "effect": {
        "span": "so as to thereby transform the Council into a more inclusive and transparent body, capable of addressing threats to international peace and security"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9025 ---

输入文本: Vaccines Minister, Maggie Throup, said: Getting your booster vaccine is the best way to protect yourself and your loved ones from COVID-19.

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
        "span": "Getting your booster vaccine"
      },
      "effect": {
        "span": "to protect yourself and your loved ones from COVID-19"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14467 ---

输入文本: The multiplication of tensions and crises, if not defused swiftly enough, can spiral out of control, seriously threatening peace and security.

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
        "span": "The multiplication of tensions and crises, if not defused swiftly enough"
      },
      "effect": {
        "span": "can spiral out of control, seriously threatening peace and security"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=205 ---

输入文本: A temporary ban on commercial and private planes travelling from the six countries will also come into force at midday on Friday until 4am Sunday to reduce the risk of importing this new variant under investigation while hotel quarantine is stood up.

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
        "span": "A temporary ban on commercial and private planes travelling from the six countries"
      },
      "effect": {
        "span": "to reduce the risk of importing this new variant under investigation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1132 ---

输入文本: These early findings should be interpreted with caution as transmission data and dynamics can fluctuate, meaning that early findings can change quickly when new variants are identified.

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
      "cause": "can fluctuate",
      "effect": "should be interpreted with caution"
    }
  ],
  "pred_triples": []
}
```

### --- id=12191 ---

输入文本: The implementation of chapter V, on transitional justice, accountability, reconciliation and healing, is moving forward at a relatively slow pace, not for lack of political will but rather for objective reasons that we are addressing with our regional and international partners.

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
      "cause": "objective reasons",
      "effect": "moving forward at a relatively slow pace"
    }
  ],
  "pred_triples": []
}
```

### --- id=3485 ---

输入文本: In addition, the situation in the Middle East also continues to cause concern in us, in light of the constant hostility between Israel and Palestine, as well as the situation in Syria and Yemen.

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
      "cause": "the situation in the Middle East",
      "effect": "cause concern"
    }
  ],
  "pred_triples": []
}
```

### --- id=5271 ---

输入文本: Dr Nikki Kanani, deputy lead for the NHS Covid vaccination programme, said: It is so encouraging to see that alongside the incredible booster uptake we’ve seen in the last couple of weeks, and throughout Christmas, every day people are continuing to come forward for their first and second doses – allowing them to also get their booster as soon as possible.

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
        "span": "every day people are continuing to come forward for their first and second doses"
      },
      "effect": {
        "span": "allowing them to also get their booster as soon as possible"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=17497 ---

输入文本: This has led to broader and sustainable incomes for the majority of people living in rural areas who now contribute to the increased levels of household and national food and nutrition security.

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
      "cause": "broader and sustainable incomes",
      "effect": "contribute to the increased levels"
    }
  ],
  "pred_triples": []
}
```

### --- id=15596 ---

输入文本: But this effort must be global, as neither the Principality’s commitments nor those of any other country alone will be able to prevent the temperature from rising beyond 1.5°C by the end of the century.

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
      "cause": "to prevent the temperature from rising beyond 1.5°C",
      "effect": "must be global"
    }
  ],
  "pred_triples": []
}
```

### --- id=17297 ---

输入文本: For the forthcoming COP26 in Glasgow to respond adequately to the crisis we face, we need to see greater ambition and progress on mitigation, adaptation and the means of implementation.

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
      "cause": "see greater ambition and progress on mitigation, adaptation and the means of implementation",
      "effect": "respond adequately to the crisis we face"
    }
  ],
  "pred_triples": []
}
```

### --- id=10507 ---

输入文本: Because I am convinced that in order to grow and develop, to have the life that we Argentines deserve, we must be better integrated into the world and deploy all of our labour and talent to that end.

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
      "cause": "better integrated into the world and deploy all of our labour and talent to that end",
      "effect": "grow and develop"
    }
  ],
  "pred_triples": []
}
```

### --- id=12405 ---

输入文本: I wish you every success as you chart a new course for a re-vitalized United Nations capable of energizing and supporting the efforts of all nations and people, particularly those lagging behind due to the many challenges that are far beyond their economic power and means.

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
      "cause": "many challenges",
      "effect": "lagging behind"
    }
  ],
  "pred_triples": []
}
```

### --- id=10051 ---

输入文本: We will continue to work towards a sustainable and inclusive political solution in Syria, which entails the work of the constitutional committee and securing Syrian territory so as to enable the voluntary and safe return of all refugees.

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
      "cause": "the work of the constitutional committee and securing Syrian territory",
      "effect": "enable the voluntary and safe return of all refugees"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "securing Syrian territory"
      },
      "effect": {
        "span": "so as to enable the voluntary and safe return of all refugees"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16246 ---

输入文本: And the best way to build trust is to respect the rules and to live and act by them, because we can then predict how we behave and be prepared when the unexpected happens.

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
        "span": "respect the rules and to live and act by them"
      },
      "effect": {
        "span": "we can then predict how we behave and be prepared when the unexpected happens"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16678 ---

输入文本: The Judaization of Al-Quds, the policy of systematic colonization, the laws that contravene human rights, the recognition of the annexation of lands occupied by force, as in the case of the Golan Heights, the election promises to annex new lands, with all the leaks about the so-called deal of the century, changing the borders of some States and undermining their territorial unity, while eliminating the Palestinian cause and keeping the Palestinians where they are, as well as the damage that Lebanon is likely to suffer as a result because it hosts a large number of refugees — all of these undermine any chance for peace in the Middle East and unquestionably point to a dark, unknown future.

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
        "span": "The Judaization of Al-Quds, the policy of systematic colonization, the laws that contravene human rights, the recognition of the annexation of lands occupied by force, as in the case of the Golan Heights, the election promises to annex new lands, with all the leaks about the so-called deal of the century, changing the borders of some States and undermining their territorial unity, while eliminating the Palestinian cause and keeping the Palestinians where they are, as well as the damage that Lebanon is likely to suffer as a result because it hosts a large number of refugees"
      },
      "effect": {
        "span": "all of these undermine any chance for peace in the Middle East and unquestionably point to a dark, unknown future"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12371 ---

输入文本: For our part, to facilitate the temporary stay of the forcibly displaced Myanmar national Rohingyas in Bangladesh, we have relocated some of them to Bhasan Char.

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
      "cause": "facilitate the temporary stay of the forcibly displaced Myanmar national Rohingyas in Bangladesh",
      "effect": "relocated some of them to Bhasan Char"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "we have relocated some of them to Bhasan Char"
      },
      "effect": {
        "span": "to facilitate the temporary stay of the forcibly displaced Myanmar national Rohingyas in Bangladesh"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12257 ---

输入文本: Today we are talking about billions of people who cannot access vaccines to combat the coronavirus disease (COVID-19) pandemic, which will certainty leave an indelible mark on our century.

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
      "cause": "coronavirus disease (COVID-19) pandemic",
      "effect": "leave an indelible mark on our century"
    }
  ],
  "pred_triples": []
}
```

### --- id=11420 ---

输入文本: We are calling for a new strategic orientation and partnership that would accelerate our pandemic recovery.

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
      "cause": "new strategic orientation and partnership",
      "effect": "accelerate our pandemic recovery"
    }
  ],
  "pred_triples": []
}
```

### --- id=17417 ---

输入文本: As we enter the second year of the UN decade of action, it is imperative that we, as a community of nations, take deliberate, collaborative and decisive actions to guarantee a future that leaves no one behind.

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
      "cause": "take deliberate, collaborative and decisive actions",
      "effect": "guarantee a future that leaves no one behind"
    }
  ],
  "pred_triples": []
}
```

### --- id=11616 ---

输入文本: Because measures at the border can only ever minimise and delay the arrival of a new variant, rather than stop it altogether.

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
      "cause": "measures at the border",
      "effect": "minimise and delay the arrival of a new variant"
    }
  ],
  "pred_triples": []
}
```

### --- id=7845 ---

输入文本: Close contacts who are symptomatic will also be advised to take a test in line with normal practice.

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
        "span": "Close contacts who are symptomatic"
      },
      "effect": {
        "span": "will also be advised to take a test"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16 ---

输入文本: We’ve already secured hundreds of thousands of doses of two antivirals, that have the potential to speed up recovery time and stop infections progressing.

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
        "span": "hundreds of thousands of doses of two antivirals"
      },
      "effect": {
        "span": "that have the potential to speed up recovery time and stop infections progressing"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13938 ---

输入文本: Secondly, I must mention an obstacle that is still unresolved and that if not addressed will make the achievement of the Sustainable Development Goals (SDGs) practically unattainable — our classification as a middle-income country.

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
        "span": "our classification as a middle-income country"
      },
      "effect": {
        "span": "will make the achievement of the Sustainable Development Goals (SDGs) practically unattainable"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16576 ---

输入文本: The first is promoting the implementation of international law and the Charter of the United Nations as core pillars in preventing the collapse of the international order and preserving relations among States.

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
        "span": "promoting the implementation of international law and the Charter of the United Nations as core pillars"
      },
      "effect": {
        "span": "preventing the collapse of the international order and preserving relations among States"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5459 ---

输入文本: The teams will be distributing leaflets on the Get Boosted Now campaign, as well as information on testing and advice to limit the spread of COVID-19 in the run up to Christmas.

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
        "span": "distributing leaflets on the Get Boosted Now campaign, as well as information on testing and advice"
      },
      "effect": {
        "span": "to limit the spread of COVID-19 in the run up to Christmas"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12906 ---

输入文本: While we can’t make up for all the trade they will lose over Christmas, I hope this new £1000 grant – on top of the furlough, VAT and business rates relief and existing grants, goes some way to help them weather the economic storm.

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
        "span": "this new £1000 grant – on top of the furlough, VAT and business rates relief and existing grants"
      },
      "effect": {
        "span": "goes some way to help them weather the economic storm"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16475 ---

输入文本: It is our aspiration to drive inclusive education by improving access to education and by ensuring quality education for all.

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
      "cause": "improving",
      "effect": "drive inclusive education"
    }
  ],
  "pred_triples": []
}
```

### --- id=11903 ---

输入文本: All that was caused by an invisible virus that continues to evolve and mutate, threatening to claim more lives all over the world.

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
      "cause": "invisible virus",
      "effect": "threatening to claim more lives all"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an invisible virus that continues to evolve and mutate"
      },
      "effect": {
        "span": "All that"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3068 ---

输入文本: Once human activities came to a halt, blue skies re-emerged in parts of the world.

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
        "span": "human activities came to a halt"
      },
      "effect": {
        "span": "blue skies re-emerged in parts of the world"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=17255 ---

输入文本: We believe that by working together, we can better respond to global crises such as the COVID-19 pandemic and climate change and their consequences.

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
      "cause": "working together",
      "effect": "can better respond to global crises"
    }
  ],
  "pred_triples": []
}
```

### --- id=13062 ---

输入文本: We hope that the initiatives will lead to lasting peace and stability on the Korean peninsula.

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
      "cause": "the initiatives",
      "effect": "lasting peace and stability"
    }
  ],
  "pred_triples": []
}
```

### --- id=3084 ---

输入文本: That brings us back to the obvious need to rethink the scope and reach of the multilateralism that we are promoting so that all countries of the world can enjoy a shared source of resiliency with the appropriate tools for dealing with myriad crises like COVID-19 and avoid undoing decades of collective work within our Organization and various regional communities.

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
        "span": "rethink the scope and reach of the multilateralism that we are promoting"
      },
      "effect": {
        "span": "so that all countries of the world can enjoy a shared source of resiliency with the appropriate tools for dealing with myriad crises like COVID-19 and avoid undoing decades of collective work within our Organization and various regional communities"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3145 ---

输入文本: Today, India is providing Digital Access to its millions of citizens, and in the process ensuring empowerment and transparency.

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
        "span": "is providing Digital Access to its millions of citizens"
      },
      "effect": {
        "span": "ensuring empowerment and transparency"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8946 ---

输入文本: Agile and decisive decision making This was an entirely new approach to government procurement – we were inviting industry to come to us: opening up fresh sources of supply that we could rapidly vet as being technically, legally and commercially compliant in order to secure product in the rapidly-moving global market for PPE.

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
        "span": "opening up fresh sources of supply that we could rapidly vet as being technically, legally and commercially compliant"
      },
      "effect": {
        "span": "in order to secure product in the rapidly-moving global market for PPE"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14720 ---

输入文本: This year we ratified the Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment, bringing to six the number of core human rights conventions to which we are a State party.

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
        "span": "we ratified the Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment"
      },
      "effect": {
        "span": "bringing to six the number of core human rights conventions to which we are a State party"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=6232 ---

输入文本: The time has come to reconsider our activities so that we can achieve sustainable development in harmony with the planet, with a view to leaving a habitable world for future generations.

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
        "span": "reconsider our activities"
      },
      "effect": {
        "span": "so that we can achieve sustainable development in harmony with the planet, with a view to leaving a habitable world for future generations"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5059 ---

输入文本: It is through the hard work of all of you that we have ensured, and will continue to ensure pupils and students get the learning that they deserve.

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
      "cause": "the hard work of all of you",
      "effect": "ensured, and will continue to ensure pupils and students get the learning that they deserve"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the hard work of all of you"
      },
      "effect": {
        "span": "ensure pupils and students get the learning that they deserve"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5603 ---

输入文本: This will mean that those countries most affected by climate change are better able to participate fully in discussions about creating a greener future for the planet.

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
      "cause": "most affected by climate change",
      "effect": "able to participate fully in discussions about creating a greener future for the planet"
    }
  ],
  "pred_triples": []
}
```

### --- id=6890 ---

输入文本: International peace and security is thus at risk each time a crisis breaks out or reaches a new level.

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
        "span": "a crisis breaks out or reaches a new level"
      },
      "effect": {
        "span": "International peace and security is thus at risk"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8070 ---

输入文本: Through the New Variant Assessment Platform (NVAP), the UK is making its world-leading capability available to other countries to support the global response to the pandemic.

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
      "cause": "the New Variant Assessment Platform (NVAP),",
      "effect": "is making its world-leading capability available to other countries to support the global response to the pandemic"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "making its world-leading capability available to other countries through the New Variant Assessment Platform (NVAP)"
      },
      "effect": {
        "span": "to support the global response to the pandemic"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3093 ---

输入文本: The United Nations and its institutions should closely monitor the situation in Belarus and insistently call on its authorities to refrain from the use of force, to ensure adherence to the principles of international law and human rights and to finally start a peaceful transition of power.

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
        "span": "closely monitor the situation in Belarus and insistently call on its authorities to refrain from the use of force"
      },
      "effect": {
        "span": "to ensure adherence to the principles of international law and human rights and to finally start a peaceful transition of power"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=6631 ---

输入文本: In this respect, I am pleased to welcome the return to the fold of several of our compatriots in exile and members of some armed groups, who responded favourably to the Government’s policy of extending a helping hand.

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
        "span": "the Government’s policy of extending a helping hand"
      },
      "effect": {
        "span": "who responded favourably to the Government’s policy of extending a helping hand"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10469 ---

输入文本: Instead, it is more efficient to use wood for making products, which is not only carbon-neutral but carbon-positive, as such products store carbon for their entire lifetime.

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
        "span": "as such products store carbon for their entire lifetime"
      },
      "effect": {
        "span": "it is more efficient to use wood for making products, which is not only carbon-neutral but carbon-positive"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=11603 ---

输入文本: I simply believe – as a former COVID patient – that we all have a right to know, so that we can collectively do our best to prevent a recurrence.

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
      "cause": "have a right to know",
      "effect": "can collectively do our best to prevent a recurrence"
    }
  ],
  "pred_triples": []
}
```

### --- id=86 ---

输入文本: COVID-19 is not going away, and so we’ll have to keep seeing new variants emerge.

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
      "cause": "is not going away",
      "effect": "so we’ll have to keep seeing new variants emerge"
    }
  ],
  "pred_triples": []
}
```

### --- id=17110 ---

输入文本: We cannot make lasting democratic achievements without sustained economic growth.

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
        "span": "sustained economic growth"
      },
      "effect": {
        "span": "make lasting democratic achievements"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14266 ---

输入文本: San Marino believes that sustainability is a major issue that must be addressed at the global level in order to ensure the future of the planet and that of young and future generations.

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
      "cause": "issue that must be addressed",
      "effect": "ensure"
    }
  ],
  "pred_triples": []
}
```

### --- id=16275 ---

输入文本: Unless we stop burning coal, we have no hope of achieving net zero emissions in 31 years’ time.

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
        "span": "stop burning coal"
      },
      "effect": {
        "span": "achieving net zero emissions in 31 years’ time"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=6937 ---

输入文本: Armenia is ready for a constructive dialogue, which should lead to the establishment of sustainable and lasting peace in the region.

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
      "cause": "constructive dialogue",
      "effect": "lead to the establishment"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "constructive dialogue"
      },
      "effect": {
        "span": "the establishment of sustainable and lasting peace in the region"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13381 ---

输入文本: We must firmly reject populist rhetoric, which manipulates minds, fosters hatred and, ultimately, trivializes racism, xenophobia and violent extremism.

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
        "span": "populist rhetoric"
      },
      "effect": {
        "span": "which manipulates minds, fosters hatred and, ultimately, trivializes racism, xenophobia and violent extremism"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8795 ---

输入文本: The new system builds on user feedback to improve the experience of those using the site.

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
        "span": "The new system builds on user feedback"
      },
      "effect": {
        "span": "to improve the experience of those using the site"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14346 ---

输入文本: In August, the Intermediate-Range Nuclear Forces Treaty, one of the pillars of the modern disarmament architecture and a symbol of the end of the Cold War, ceased to function, creating a real danger that the types of missiles it covered, with a flying time of a few minutes, could be deployed in various regions of the world, including Europe.

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
        "span": "the Intermediate-Range Nuclear Forces Treaty, one of the pillars of the modern disarmament architecture and a symbol of the end of the Cold War, ceased to function"
      },
      "effect": {
        "span": "creating a real danger that the types of missiles it covered, with a flying time of a few minutes, could be deployed in various regions of the world, including Europe"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13854 ---

输入文本: Zimbabwe is confident that under his able stewardship, the General Assembly will accelerate towards achieving our Organization’s objectives.

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
        "span": "under his able stewardship"
      },
      "effect": {
        "span": "the General Assembly will accelerate towards achieving our Organization’s objectives"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5109 ---

输入文本: She also led the successful responses to the detection of MERS in the UK and the first UK cases of monkeypox, ensuring dangerous infectious diseases were swiftly contained.

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
      "cause": "also led the successful responses to the detection of MERS in the UK and the first UK cases of monkeypox",
      "effect": "ensuring dangerous infectious diseases were swiftly contained"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "led the successful responses to the detection of MERS in the UK and the first UK cases of monkeypox"
      },
      "effect": {
        "span": "ensuring dangerous infectious diseases were swiftly contained"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16053 ---

输入文本: Some countries fear a future decline because they are losing their vitality, their brains and their younger generations to the outside world.

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
        "span": "they are losing their vitality, their brains and their younger generations to the outside world"
      },
      "effect": {
        "span": "a future decline"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9827 ---

输入文本: Australia stepped forward to support that step by donating a patrol boat in 1996.

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
        "span": "Australia stepped forward to support that step by donating a patrol boat in 1996"
      },
      "effect": {
        "span": "support that step"
      },
      "relation": "caused"
    }
  ]
}
```
