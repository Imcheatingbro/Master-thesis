# Qwen3.6 35B A3B politicause Fixed + RAG eval report

## 配置
```json
{
  "label": "Qwen3.6 35B A3B politicause Fixed + RAG",
  "model": "qwen/qwen3.6-35b-a3b",
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
================ Qwen3.6 35B A3B politicause Fixed + RAG final report ================
样本总数: 860
  Gold 含因果: 245 | Pred 含因果: 344
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.797
  Precision: 0.602
  Recall   : 0.845
  F1       : 0.703
  (TP=207, TN=478, FP=137, FN=38)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 860
    Gold triples: 245 | Pred triples: 344
    Precision: 0.256
    Recall   : 0.359
    F1       : 0.299
    (TP=88, FP=256, FN=157)
  [anchor_window] (primary)
    样本数: 860
    Gold triples: 245 | Pred triples: 344
    Precision: 0.430
    Recall   : 0.604
    F1       : 0.503
    (TP=148, FP=196, FN=97)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 207
    Gold triples: 207 | Pred triples: 207
    Precision: 0.425
    Recall   : 0.425
    F1       : 0.425
    (TP=88, FP=119, FN=119)
  [anchor_window] (primary)
    样本数: 207
    Gold triples: 207 | Pred triples: 207
    Precision: 0.715
    Recall   : 0.715
    F1       : 0.715
    (TP=148, FP=59, FN=59)
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

Sample details shown: first 200 of 234 wrong samples from 860 total samples.

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
        "span": "the world can incentivise them to go this direction"
      },
      "effect": {
        "span": "this twenty-year presence of the coalition forces in Afghanistan would not be wasted after all"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10561 ---

输入文本: Post-conflict reconstruction can be successful only when all segments of society are included.

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
        "span": "all segments of society are included"
      },
      "effect": {
        "span": "Post-conflict reconstruction can be successful"
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

### --- id=13166 ---

输入文本: In that regard, in cooperation with the Green Climate Fund and the Food and Agriculture Organization of the United Nations, Paraguay has recently concluded negotiations to establish a special reforestation fund and to thereby combat extreme poverty, which affects the most vulnerable in society.

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
      "cause": "has recently concluded negotiations to establish a special reforestation fund",
      "effect": "thereby combat extreme poverty, which affects the most vulnerable in society"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "establish a special reforestation fund"
      },
      "effect": {
        "span": "to thereby combat extreme poverty"
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
      "cause": "get the jab",
      "effect": "this will help to prevent the serious consequences of catching COVID-19 in pregnancy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "get the jab"
      },
      "effect": {
        "span": "prevent the serious consequences of catching COVID-19 in pregnancy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=11100 ---

输入文本: All of those efforts constitute a process that will help solidify the foundation for peace on the Korean peninsula, as well as contribute to peace and stability in North-East Asia.

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
        "span": "All of those efforts constitute a process"
      },
      "effect": {
        "span": "that will help solidify the foundation for peace on the Korean peninsula, as well as contribute to peace and stability in North-East Asia"
      },
      "relation": "caused"
    }
  ]
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
        "span": "incremental effects of climate change"
      },
      "effect": {
        "span": "threaten the livelihoods, security, and well-being of our people"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13987 ---

输入文本: We are not utopian, but we believe that it is possible and necessary to take steps towards a gradual but effective action that will make it possible to reverse the abysmal and shameful inequality on the planet.

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
        "span": "take steps towards a gradual but effective action"
      },
      "effect": {
        "span": "make it possible to reverse the abysmal and shameful inequality on the planet"
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
        "span": "the two leaders to talk candidly with each other and try to work out the issues at hand"
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
        "span": "over 37 million people have been boosted"
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

### --- id=14041 ---

输入文本: This very rare situation, involving a special moment of agreement, at both the domestic and the international level, fuels our hopes for real progress on the path towards developing such needed internal reforms as justice reform and the fight against corruption, as well as the way the Transnistrian problem is to be solved.

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
        "span": "This very rare situation, involving a special moment of agreement, at both the domestic and the international level"
      },
      "effect": {
        "span": "fuels our hopes for real progress on the path towards developing such needed internal reforms as justice reform and the fight against corruption, as well as the way the Transnistrian problem is to be solved"
      },
      "relation": "caused"
    }
  ]
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

### --- id=6590 ---

输入文本: It also destroyed millions of dollars’ worth of crops and wreaked significant havoc on our reefs and corals, consequently undermining Palau’s food security.

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
      "cause": "also destroyed millions of dollars’ worth of crops and wreaked significant havoc on our reefs and corals",
      "effect": "consequently undermining Palau’s food security"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "destroyed millions of dollars’ worth of crops and wreaked significant havoc on our reefs and corals"
      },
      "effect": {
        "span": "undermining Palau’s food security"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9633 ---

输入文本: It is also very important for the South Caucasus to cease to be one of the areas of conflict and tension in the world, with a view to achieving a fair and peaceful future.

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
        "span": "cease to be one of the areas of conflict and tension in the world"
      },
      "effect": {
        "span": "achieving a fair and peaceful future"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5875 ---

输入文本: Today, almost two years into the pandemic, a global effort has resulted in the development and distribution of safe and effective vaccines.

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
      "cause": "a global effort",
      "effect": "resulted in the development and distribution of safe and effective vaccines"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a global effort"
      },
      "effect": {
        "span": "the development and distribution of safe and effective vaccines"
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
        "span": "this glaring gap"
      },
      "effect": {
        "span": "adverse effects ... on Government’s ability to manage its macroeconomic affairs"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1283 ---

输入文本: Due to the early nature of the findings, all estimates are subject to significant uncertainty and are subject to change.

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
      "cause": "early nature of the findings",
      "effect": "all estimates are subject to significant uncertainty and are subject to change"
    }
  ],
  "pred_triples": []
}
```

### --- id=8695 ---

输入文本: Dr Jenny Harries, Chief Executive of the UK Health Security Agency (UKHSA), said: This data confirms that cases have declined substantially following the peak of the Omicron wave.

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
        "span": "the peak of the Omicron wave"
      },
      "effect": {
        "span": "cases have declined substantially"
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
      "cause": "the new variants",
      "effect": "have made this fight a whole lot tougher."
    }
  ],
  "pred_triples": []
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
        "span": "helping to achieve a common approach for aviation recovery"
      },
      "effect": {
        "span": "as we continue to collaborate with our international partners in response to the pandemic"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5275 ---

输入文本: This means delivering mobile vaccinations where people are sleeping on the streets, supporting outreach work in shelters to educate people about the dangers of the virus, and giving money to councils to provide safe and secure accommodation while their level of vaccination is increased.

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
        "span": "delivering mobile vaccinations where people are sleeping on the streets, supporting outreach work in shelters to educate people about the dangers of the virus, and giving money to councils to provide safe and secure accommodation"
      },
      "effect": {
        "span": "while their level of vaccination is increased"
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
        "span": "instability, power struggles, crises, waste and extravagance"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10822 ---

输入文本: It should provide us with a platform to realistically address this serious issue, which is one of the factors that hinders the development of the vast potential of the African continent.

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
        "span": "this serious issue"
      },
      "effect": {
        "span": "hinders the development of the vast potential of the African continent"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=17375 ---

输入文本: Let us begin with small steps to build trust, and then we can move towards resolving other regional and global issues together.

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
        "span": "begin with small steps to build trust"
      },
      "effect": {
        "span": "we can move towards resolving other regional and global issues together"
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

### --- id=16744 ---

输入文本: We have expanded opportunities in education for girls by creating safe spaces in schools, while campaigning vigorously against early marriage and sexual and gender-based violence.

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
      "cause": "creating safe spaces in schools",
      "effect": "have expanded opportunities"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "creating safe spaces in schools"
      },
      "effect": {
        "span": "expanded opportunities in education for girls"
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

### --- id=15651 ---

输入文本: However, I would like to draw the Assembly’s attention to the fact that the successful implementation of investment projects and new transport corridors will not bring the maximum possible benefits if barriers to the crossing of State borders continue.

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
      "cause": "barriers to the crossing of State borders continue",
      "effect": "successful implementation of investment projects and new transport corridors will not bring the maximum possible benefits"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "barriers to the crossing of State borders continue"
      },
      "effect": {
        "span": "will not bring the maximum possible benefits"
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
      "cause": "have increasingly yearned for its reform",
      "effect": "make it more democratic and responsive to the needs"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "reform"
      },
      "effect": {
        "span": "make it more democratic and responsive to the needs of all nations, rich and poor, big and small, strong and weak"
      },
      "relation": "caused"
    }
  ]
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
        "span": "promoted inclusive educational policies"
      },
      "effect": {
        "span": "providing our young people with the tools they need to develop their potential in a multicultural and global world"
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
      "cause": "customers look to go abroad with ease and without the added expense of testing",
      "effect": "strong and sustained booking patterns"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the announcement"
      },
      "effect": {
        "span": "we’ve seen strong and sustained booking patterns"
      },
      "relation": "caused"
    }
  ]
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
        "span": "a negative impact on the entire Sahel region"
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
        "span": "This situation compromises the ethical values of democracy"
      },
      "effect": {
        "span": "affects the competitiveness of the State and the economy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9923 ---

输入文本: The great qualities and skills that we all recognize in him are undoubtedly a guarantee of the success of the work of this session, whose central theme Galvanizing multilateral efforts for poverty eradication, quality education, climate action and inclusion pragmatically deals with the key challenges facing the world today.

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
        "span": "The great qualities and skills that we all recognize in him"
      },
      "effect": {
        "span": "are undoubtedly a guarantee of the success of the work of this session"
      },
      "relation": "caused"
    }
  ]
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
        "span": "Tocilizumab and Sarilumab"
      },
      "effect": {
        "span": "reduce the risk of death for critically ill patients"
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
      "cause": "local restrictions",
      "effect": "helped slow the spread of the virus"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "local restrictions have helped slow the spread of the virus"
      },
      "effect": {
        "span": "The natural rate of R is around 3"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12227 ---

输入文本: We hope that the upcoming NPT Review Conference will lead to a successful outcome that will facilitate global denuclearization.

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
      "cause": "the upcoming NPT Review Conference",
      "effect": "successful outcome"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the upcoming NPT Review Conference will lead to a successful outcome"
      },
      "effect": {
        "span": "that will facilitate global denuclearization"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4319 ---

输入文本: It’s been so instrumental in getting us back to normal, and as we get going with this year’s season, we need to make sure all our fans are as safe as they can possibly be – and that includes making sure they get the vaccine to protect themselves and those around them.

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
        "span": "getting the vaccine"
      },
      "effect": {
        "span": "to protect themselves and those around them"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=462 ---

输入文本: To all those eligible – getting the booster could be the most important thing you do this Christmas as we look to spend more valuable time with our loved ones.

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
        "span": "getting the booster"
      },
      "effect": {
        "span": "we look to spend more valuable time with our loved ones"
      },
      "relation": "caused"
    }
  ]
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
        "span": "fail to prepare young people"
      },
      "effect": {
        "span": "prepare a generation to fail"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14219 ---

输入文本: Precisely with a view to achieving, guaranteeing and preserving peace and order in our republic, President Nicolas Maduro invited all segments of society to participate in a sovereign dialogue.

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
      "cause": "invited all segments of society to participate in a sovereign dialogue",
      "effect": "achieving, guaranteeing and preserving"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Precisely with a view to achieving, guaranteeing and preserving peace and order in our republic"
      },
      "effect": {
        "span": "President Nicolas Maduro invited all segments of society to participate in a sovereign dialogue"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9490 ---

输入文本: The use of the Nile waters also offers a unique opportunity for transboundary cooperation among the sisterly countries of the region.

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
        "span": "The use of the Nile waters"
      },
      "effect": {
        "span": "offers a unique opportunity for transboundary cooperation among the sisterly countries of the region"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16317 ---

输入文本: As a result, the Government has been able to increase its development budget allocation to 40 per cent, as compared to 25 per cent in 2015.

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
        "span": "As a result"
      },
      "effect": {
        "span": "the Government has been able to increase its development budget allocation to 40 per cent"
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
        "span": "working closely with international counterparts"
      },
      "effect": {
        "span": "ensure a longer-term solution can be reached for these individuals"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5717 ---

输入文本: There is currently no mechanism for accessing concessional finance that would allow us to solve the liquidity crisis.

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
      "cause": "mechanism for accessing concessional finance",
      "effect": "solve the liquidity crisis"
    }
  ],
  "pred_triples": []
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
        "span": "the Delta variant continues to circulate at high levels across all age ranges"
      },
      "effect": {
        "span": "is still causing substantial infection and hospitalisation in older people"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12841 ---

输入文本: We are concerned about the threats to world peace and security from extremist groups in the Sahel, the Democratic Republic of the Congo, Mozambique and other parts of the world, which require the international community to constantly mobilize to strengthen our capacity to respond to such dangerous assaults on social and economic stability.

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
      "cause": "the threats to world peace and security from extremist groups in the Sahel, the Democratic Republic of the Congo, Mozambique and other parts of the world",
      "effect": "which require the international community to constantly mobilize to strengthen our capacity to respond to such dangerous assaults on social and economic stability"
    }
  ],
  "pred_triples": []
}
```

### --- id=16694 ---

输入文本: In the context of implementing the Sustainable Development Goals, the Kyrgyz Republic continues to address socioeconomic issues, including reducing unemployment, raising the standard of living of the population by implementing national programmes in the areas of education and health care, youth policies and infrastructure projects, as well as by attracting investment and creating the most favourable conditions to that end.

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
        "span": "implementing national programmes in the areas of education and health care, youth policies and infrastructure projects, as well as by attracting investment and creating the most favourable conditions to that end"
      },
      "effect": {
        "span": "raising the standard of living of the population"
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
        "span": "ensure that the people have access to humanitarian assistance"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3229 ---

输入文本: In this regard, the United Nations Economic Commission for Latin America and the Caribbean (ECLAC), has cautioned that a debt crisis is looming for the economies of the Latin American and Caribbean subregion, which will compound their high debt to GDP and debt service ratios.

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
      "cause": "is looming for the economies of the Latin American and Caribbean subregion",
      "effect": "compound their high debt to GDP and debt service ratios"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a debt crisis is looming"
      },
      "effect": {
        "span": "will compound their high debt to GDP and debt service ratios"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15136 ---

输入文本: They were prevented from bringing their spouses and children, had 75 per cent of their wages confiscated by the Cuban regime and were denied basic freedoms, such as that of coming and going.

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
        "span": "unilateral action by the Cuban regime"
      },
      "effect": {
        "span": "left Brazil"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4276 ---

输入文本: G7 members also agreed to focus on facilitating a sustainable global recovery committing to prioritising the sustainable decarbonisation of transport and protecting the rights of transport workers in their vital work to facilitate international travel.

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
        "span": "committing to prioritising the sustainable decarbonisation of transport and protecting the rights of transport workers"
      },
      "effect": {
        "span": "to facilitate international travel"
      },
      "relation": "caused"
    }
  ]
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
        "span": "collaborate with farmers to build systems in New Zealand"
      },
      "effect": {
        "span": "every farmer will be able to use to measure, manage and reduce their own farm’s emissions"
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
        "span": "blind support of certain countries"
      },
      "effect": {
        "span": "consequences of Israel’s actions"
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

### --- id=16447 ---

输入文本: That will finally bring an end to an age-old atavistic claim that has hindered Belize’s development and made more difficult the relations of friendship and cooperation that both our peoples aspire to and deserve.

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
        "span": "an age-old atavistic claim that has hindered Belize’s development"
      },
      "effect": {
        "span": "made more difficult the relations of friendship and cooperation that both our peoples aspire to and deserve"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13224 ---

输入文本: However, climate change and pollution threaten our natural resources, our delicate ecosystems and our Adriatic Sea.

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
        "span": "climate change and pollution"
      },
      "effect": {
        "span": "threaten our natural resources, our delicate ecosystems and our Adriatic Sea"
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
        "span": "this has led to increased hospital admissions and, sadly, more deaths"
      },
      "effect": {
        "span": "increased hospital admissions and, sadly, more deaths"
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
      "cause": "need to seriously address the issue of developing countries’ debt",
      "effect": "overcome the shocks of the COVID-19 pandemic"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "In order to overcome the shocks of the COVID-19 pandemic"
      },
      "effect": {
        "span": "we need to seriously address the issue of developing countries’ debt"
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
        "span": "take up the offer"
      },
      "effect": {
        "span": "increase protection against potential future waves of COVID-19"
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
        "span": "In order to confront the urgency of the pandemic"
      },
      "effect": {
        "span": "Governments across the globe reallocated funds to meet desperate needs"
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

### --- id=3348 ---

输入文本: We in Botswana remain committed to accelerate our efforts towards the attainment of SDGs during this remaining ‘Decade of Action.’ To realize this ambition, my Government is resolute in the transformation of Botswana’s economy from one that largely relies on the extractive industry, which is vulnerable to globe shocks, to a knowledge-based economy.

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
        "span": "transformation of Botswana’s economy from one that largely relies on the extractive industry, which is vulnerable to globe shocks, to a knowledge-based economy"
      },
      "effect": {
        "span": "realize this ambition"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=17614 ---

输入文本: At the international level, heavy-handed policies of containment and encirclement to forestall healthy strategic competition and mutual progress based on symmetric, equitable, and rules-based international system has, and is stoking, a climate of confrontation and instability with all the risks that this may entail in the period ahead.

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
      "cause": "forestall",
      "effect": "stoking"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "heavy-handed policies of containment and encirclement to forestall healthy strategic competition and mutual progress based on symmetric, equitable, and rules-based international system"
      },
      "effect": {
        "span": "a climate of confrontation and instability with all the risks that this may entail in the period ahead"
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
        "span": "without the support of this community, without the true support of the States Members of the United Nations"
      },
      "effect": {
        "span": "those who left their homes with the desire to return will not easily find their way back"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=6336 ---

输入文本: Switzerland works closely with universities and the private sector to find innovative technological approaches for development and poverty-reduction projects.

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
        "span": "works closely with universities and the private sector"
      },
      "effect": {
        "span": "to find innovative technological approaches for development and poverty-reduction projects"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=17420 ---

输入文本: Mr. President, Zimbabwe launched Vision 2030, aimed at improving the lives of our people, sustainably managing the environment and ensuring that no one is left behind.

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
        "span": "launched Vision 2030"
      },
      "effect": {
        "span": "aimed at improving the lives of our people, sustainably managing the environment and ensuring that no one is left behind"
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
        "span": "enabling them to benefit from the Algerian experience in the area of national reconciliation"
      },
      "effect": {
        "span": "benefit from the Algerian experience in the area of national reconciliation"
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
        "span": "weakening the link between infection and serious illness"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12931 ---

输入文本: In Grenada, we are currently pushing forward with our National Sustainable Development Plan 2035, which will resolutely set us on an unprecedented long-term development path.

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
      "cause": "pushing forward with our National Sustainable Development Plan 2035",
      "effect": "will resolutely set us on an unprecedented long-term development path"
    }
  ],
  "pred_triples": []
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

### --- id=9749 ---

输入文本: The conservation and sustainable use of our ocean is a key driver of our country’s sustainable economic development, prosperity, and stability.

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
        "span": "The conservation and sustainable use of our ocean"
      },
      "effect": {
        "span": "our country’s sustainable economic development, prosperity, and stability"
      },
      "relation": "caused"
    }
  ]
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

### --- id=11920 ---

输入文本: The Kingdom of Morocco is hopeful that a just, comprehensive and sustainable peace will be reached in the Middle East, leading to the establishment of an independent State of Palestine, on its national territory within the borders of June 1967 and with East Jerusalem as its capital, living side by side with Israel in peace and security.

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
      "cause": "comprehensive and sustainable peace",
      "effect": "establishment"
    }
  ],
  "pred_triples": []
}
```

### --- id=3081 ---

输入文本: Such as in Ukraine, where the negotiations between Russia, Ukraine, France and Germany have helped to bring about the longest ceasefire since the beginning of the conflict.

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
      "cause": "the negotiations between Russia, Ukraine, France and Germany",
      "effect": "helped to bring about the longest ceasefire since the beginning of the conflict"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the negotiations between Russia, Ukraine, France and Germany"
      },
      "effect": {
        "span": "to bring about the longest ceasefire since the beginning of the conflict"
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
      "cause": "the COVID-19 pandemic emergency",
      "effect": "has compromised our capacity to respond to the harmful impact of climate change"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the COVID-19 pandemic emergency"
      },
      "effect": {
        "span": "compromised our capacity to respond to the harmful impact of climate change"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16612 ---

输入文本: Our children’s access to quality education is a key driver for a sustainable fight against poverty and climate change.

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
        "span": "Our children’s access to quality education"
      },
      "effect": {
        "span": "a sustainable fight against poverty and climate change"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=11216 ---

输入文本: We provide access to a health benefits package that prioritizes primary health-care interventions, reduces the cost of medicine and increases the number of people with insurance coverage.

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
        "span": "provide access to a health benefits package that prioritizes primary health-care interventions"
      },
      "effect": {
        "span": "reduces the cost of medicine and increases the number of people with insurance coverage"
      },
      "relation": "caused"
    }
  ]
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
        "span": "corruption had become a cancer"
      },
      "effect": {
        "span": "preventing us from taking advantage of all the potential that we have to achieve greater levels of progress and development"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4342 ---

输入文本: Patients who are contacts of a confirmed case of SARS-CoV-2 will still need to go through the current PCR pathway.

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
      "cause": "are contacts of a confirmed case of SARS-CoV-2",
      "effect": "need to go through the current PCR pathway"
    }
  ],
  "pred_triples": []
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

### --- id=16824 ---

输入文本: At the subregional level, the adoption of the principle of a common ECOWAS currency is also to be welcomed as an important factor in accelerating integration.

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
        "span": "the adoption of the principle of a common ECOWAS currency"
      },
      "effect": {
        "span": "accelerating integration"
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
        "span": "reducing the risk of hospitalisation or death for at-risk non-hospitalised adults with mild to moderate COVID-19 by 50%"
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
        "span": "imposing a blockade and unilateral coercive economic measures"
      },
      "effect": {
        "span": "economic terrorism"
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
        "span": "assistance extended to other member states who are facing difficulties"
      },
      "effect": {
        "span": "enables us to control the outbreak of the COVID-19 at a certain level"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=17413 ---

输入文本: This must be seen for what it is — pre-planned ethnic cleansing to drive ethnic Georgians out.

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
      "cause": "pre-planned ethnic cleansing",
      "effect": "drive ethnic Georgians out"
    }
  ],
  "pred_triples": []
}
```

### --- id=13794 ---

输入文本: As experience has shown, preventive diplomacy under the auspices of the United Nations can produce real results.

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
        "span": "preventive diplomacy under the auspices of the United Nations"
      },
      "effect": {
        "span": "can produce real results"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5915 ---

输入文本: To continue to receive the best possible protection against COVID, all adults are encouraged to get two vaccine doses.

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
      "cause": "encouraged to get two vaccine doses",
      "effect": "continue to receive the best possible protection against COVID"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "get two vaccine doses"
      },
      "effect": {
        "span": "to continue to receive the best possible protection against COVID"
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

### --- id=3496 ---

输入文本: In that regard, I commend the initiative of the Secretary-General who, from the very beginning of the pandemic, launched a global response by the United Nations system to address the pandemic and guide our States to safeguard themselves against the adverse consequences of the pandemic.

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
        "span": "launched a global response by the United Nations system"
      },
      "effect": {
        "span": "to address the pandemic and guide our States to safeguard themselves against the adverse consequences of the pandemic"
      },
      "relation": "caused"
    }
  ]
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
        "span": "continues to claim thousands of lives daily"
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

### --- id=10872 ---

输入文本: Our efforts in the past were often been rewarded when we were able to take advantage of the latest technological developments to benefit everyone.

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
        "span": "take advantage of the latest technological developments"
      },
      "effect": {
        "span": "to benefit everyone"
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
        "span": "come forward for their booster dose, or if unvaccinated, for their first 2 doses"
      },
      "effect": {
        "span": "to increase their protection against serious illness"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13322 ---

输入文本: That will allow for a peaceful resolution of the crisis, based on the Gulf Cooperation Council Initiative and its Implementation Mechanism, the outcomes of National Dialogue Conference and Security Council resolution 2216 (2015).

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
        "span": "That will allow for a peaceful resolution of the crisis"
      },
      "effect": {
        "span": "based on the Gulf Cooperation Council Initiative and its Implementation Mechanism, the outcomes of National Dialogue Conference and Security Council resolution 2216 (2015)"
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
        "span": "could gradually replace those restrictions"
      },
      "relation": "caused"
    }
  ]
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
        "span": "pressures on our finances in the United Kingdom caused by COVID-19"
      },
      "effect": {
        "span": "we have kept that promise to the letter"
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
        "span": "share their vaccination status on dating apps"
      },
      "effect": {
        "span": "receive 30% more matches than those who don’t"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=50 ---

输入文本: So we’ll require anyone who enters the UK to take a PCR test by the end of their second day after they arrive and to self-isolate until they’ve received a negative result.

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
        "span": "require anyone who enters the UK to take a PCR test by the end of their second day after they arrive"
      },
      "effect": {
        "span": "to self-isolate until they’ve received a negative result"
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
        "span": "continue to work with the WHO Eastern Mediterranean region"
      },
      "effect": {
        "span": "improve regional genomic sequencing hubs in Oman, Abu Dhabi and Morocco"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=7830 ---

输入文本: It’s thanks to the success of our vaccination programme that we can make this switch – giving the industry and consumers a much-needed boost.

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
      "cause": "the success of our vaccination programme",
      "effect": "we can make this switch – giving the industry and consumers a much-needed boost"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the success of our vaccination programme"
      },
      "effect": {
        "span": "we can make this switch"
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
      "cause": "looms ever larger",
      "effect": "needs the United Nations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "our collective inability to address it"
      },
      "effect": {
        "span": "the climate crisis looms ever larger"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9337 ---

输入文本: As of today, the lifting of Plan B means: mandatory COVID-19 certification will end, but venues may choose to use the NHS COVID Pass voluntarily face coverings will not be required by law in indoor venues local directors of public health are still able to recommend face coverings in communal areas only in education settings within their area, but only where the department and public health experts judge the measures to be proportionate – this is a temporary measure infection prevention control guidance continues to require face coverings to be worn in health and care settings, including primary care and pharmacies it is suggested that people wear face coverings in crowded and enclosed spaces where they might come into contact with people they do not normally meet it is still a legal requirement for those with COVID-19 to self-isolate for 10 days with the option to end self-isolation after 5 full days following 2 negative rapid lateral flow tests As of Wednesday 19 January, the government no longer asked people to work from home.

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
        "span": "the lifting of Plan B"
      },
      "effect": {
        "span": "mandatory COVID-19 certification will end"
      },
      "relation": "caused"
    }
  ]
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
        "span": "if they are not addressed in a timely and decisive manner"
      },
      "effect": {
        "span": "results from such non-traditional security challenges as disease or climate change"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2042 ---

输入文本: The African peoples and their leaders are sufficiently aware that the development of their continent is solely their responsibility and depends on incorporating their respective countries into a free trade area.

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
        "span": "incorporating their respective countries into a free trade area"
      },
      "effect": {
        "span": "the development of their continent"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13653 ---

输入文本: We believe that failure to establish a Palestinian State will mean continued violence and terrorism.

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
      "cause": "failure to establish",
      "effect": "will mean continued"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "failure to establish a Palestinian State"
      },
      "effect": {
        "span": "continued violence and terrorism"
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
      "cause": "concrete outcome of the Doha conference",
      "effect": "sustainably graduate from the LDC category"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the enabling of more countries"
      },
      "effect": {
        "span": "to sustainably graduate from the LDC category"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16468 ---

输入文本: Those critical investments will be game-changers for Kiribati’s development curve.

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
        "span": "Those critical investments"
      },
      "effect": {
        "span": "game-changers for Kiribati’s development curve"
      },
      "relation": "caused"
    }
  ]
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
        "span": "protecting millions of people from COVID-19"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5927 ---

输入文本: The problem is that schools may nonetheless act as vectors for transmission, causing the virus to spread between households.

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
      "cause": "schools may nonetheless act as vectors for transmission",
      "effect": "causing the virus to spread between households"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "schools may nonetheless act as vectors for transmission"
      },
      "effect": {
        "span": "the virus to spread between households"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13657 ---

输入文本: In that regard, my country was an active partner in all the international and regional forums, deliberations and dialogues that resulted in the 2030 Agenda for Sustainable Development.

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
      "cause": "all the international and regional forums, deliberations and dialogues",
      "effect": "that resulted in the 2030 Agenda for Sustainable Development"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "all the international and regional forums, deliberations and dialogues"
      },
      "effect": {
        "span": "the 2030 Agenda for Sustainable Development"
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
        "span": "the government is looking to replace the hotel quarantine policy with other contingency measures including home isolation"
      },
      "effect": {
        "span": "a sufficiently robust digital solution to ensure compliance with home isolation can be found"
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
        "span": "relieves the financial burden of PPE procurement done on an individual basis"
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
        "span": "bold leadership, innovative ideas and schemes"
      },
      "effect": {
        "span": "make possible what seems to be a chimera"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1763 ---

输入文本: For New Zealand’s part, we have adopted the Aotearoa New Zealand Biodiversity Strategy 2020 — Te Mana o te Taiao — which will guide our actions domestically for the protection, restoration and sustainable use of biodiversity.

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
        "span": "adopted the Aotearoa New Zealand Biodiversity Strategy 2020 — Te Mana o te Taiao"
      },
      "effect": {
        "span": "will guide our actions domestically for the protection, restoration and sustainable use of biodiversity"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16909 ---

输入文本: In 2015, Australia set up the International Partnership for Blue Carbon with the aim of protecting and conserving mangroves, tidal marshes and seagrasses for climate change mitigation and adaptation.

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
        "span": "set up the International Partnership for Blue Carbon"
      },
      "effect": {
        "span": "protecting and conserving mangroves, tidal marshes and seagrasses for climate change mitigation and adaptation"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=328 ---

输入文本: NHS COVID Pass can now be used to demonstrate proof of a booster or third dose for outbound international travel Booster vaccination records to be visible through both NHS App and on NHS.UK Over 13 million booster vaccines and third doses delivered across the UK so far Travellers who have had a booster or a third dose will be able to demonstrate their vaccine status through the NHS COVID Pass from Friday 19 November.

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
        "span": "NHS COVID Pass can now be used to demonstrate proof of a booster or third dose for outbound international travel"
      },
      "effect": {
        "span": "Travellers who have had a booster or a third dose will be able to demonstrate their vaccine status through the NHS COVID Pass from Friday 19 November"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4215 ---

输入文本: The current measures are in place to help protect all of us, and anyone can suffer serious illness from this virus.

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
        "span": "The current measures are in place"
      },
      "effect": {
        "span": "to help protect all of us"
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

### --- id=13641 ---

输入文本: We also highly appreciate the regional mediation efforts that have led the Sudanese parties to this great national achievement.

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
      "cause": "the regional mediation efforts",
      "effect": "led the Sudanese parties to this great national achievement"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "regional mediation efforts that have led"
      },
      "effect": {
        "span": "the Sudanese parties to this great national achievement"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16896 ---

输入文本: New technologies are coming on line, with the potential to recycle used plastics into valuable new plastics, creating a circular plastics economy.

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
        "span": "recycle used plastics into valuable new plastics"
      },
      "effect": {
        "span": "creating a circular plastics economy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=7067 ---

输入文本: The aim of the package was to support the economic sectors affected by the pandemic, the private sector and citizens, as well as to support wages and protect jobs.

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
        "span": "The aim of the package was to support the economic sectors affected by the pandemic, the private sector and citizens"
      },
      "effect": {
        "span": "as well as to support wages and protect jobs"
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
        "span": "develop severe disease"
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
        "span": "acting together"
      },
      "effect": {
        "span": "make a difference"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4836 ---

输入文本: If we’re to maintain this collective protection we’ve built up, we need everyone to choose responsibly and take the simple step that will help secure greater freedom for us all.

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
        "span": "everyone to choose responsibly and take the simple step"
      },
      "effect": {
        "span": "help secure greater freedom for us all"
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
        "span": "advocate Security Council reform"
      },
      "effect": {
        "span": "thereby transform the Council into a more inclusive and transparent body, capable of addressing threats to international peace and security"
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
        "span": "protect yourself and your loved ones from COVID-19"
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

### --- id=11169 ---

输入文本: We need to pool our resources, streamline our efforts and apply multi-stakeholder approaches to combat those challenges.

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
        "span": "pool our resources, streamline our efforts and apply multi-stakeholder approaches"
      },
      "effect": {
        "span": "combat those challenges"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15388 ---

输入文本: I call on the Member States of the General Assembly to work together in a spirit of true cooperation, generosity, goodwill and mutual respect to foster a better and more sustainable future for all humankind.

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
      "cause": "work together in a spirit of true cooperation, generosity, goodwill and mutual respect",
      "effect": "foster a better and more sustainable future"
    }
  ],
  "pred_triples": []
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
        "span": "A temporary ban on commercial and private planes travelling from the six countries will also come into force at midday on Friday until 4am Sunday"
      },
      "effect": {
        "span": "to reduce the risk of importing this new variant under investigation while hotel quarantine is stood up"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2848 ---

输入文本: At the same time, we must recognize that it is urgent that we overcome the challenges surrounding the production, distribution, deployment and acceptance of vaccines if we are to prevent the spread of dangerous new virus strains.

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
      "cause": "overcome the challenges",
      "effect": "prevent the spread of dangerous new virus strains."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "overcome the challenges surrounding the production, distribution, deployment and acceptance of vaccines"
      },
      "effect": {
        "span": "prevent the spread of dangerous new virus strains"
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

### --- id=13007 ---

输入文本: However, long after the guns have been silenced, the survivors have to live with the collateral damage of the war-wounded, the shattered families, the displaced populations, the resettlement of refugees and all the other negative consequences of a national socioeconomic fabric that has been torn apart.

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
        "span": "a national socioeconomic fabric that has been torn apart"
      },
      "effect": {
        "span": "the collateral damage of the war-wounded, the shattered families, the displaced populations, the resettlement of refugees and all the other negative consequences"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13353 ---

输入文本: But while we can make significant progress in reducing inequalities or promoting education at the national level, it is utterly impossible to address the issue of climate change from a purely unilateral perspective, because the environmental policy of a single country, however ambitious it may be, is totally ineffective without action at on a global scale.

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
      "cause": "environmental policy of a single country, however ambitious it may be, is totally ineffective",
      "effect": "utterly impossible to address the issue of climate change from a purely unilateral perspective"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the environmental policy of a single country, however ambitious it may be"
      },
      "effect": {
        "span": "is totally ineffective without action at on a global scale"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5730 ---

输入文本: In Yemen, relentless fighting has worsened the humanitarian catastrophe.

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
      "cause": "relentless fighting",
      "effect": "worsened the humanitarian catastrophe"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "relentless fighting"
      },
      "effect": {
        "span": "the humanitarian catastrophe"
      },
      "relation": "caused"
    }
  ]
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
      "cause": "broader and sustainable incomes",
      "effect": "contribute to the increased levels"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "This"
      },
      "effect": {
        "span": "broader and sustainable incomes for the majority of people living in rural areas who now contribute to the increased levels of household and national food and nutrition security"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10584 ---

输入文本: We continue to be confronted by the problems of blacklisting, which pale in significance when compared to climate change but which destroy our financial sector.

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
      "cause": "problems",
      "effect": "destroy our financial sector"
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

### --- id=10942 ---

输入文本: I hope that such cooperation will lead to the signing of peace agreements between our countries, as we signed them with Egypt and Jordan.

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
        "span": "such cooperation"
      },
      "effect": {
        "span": "the signing of peace agreements between our countries"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14129 ---

输入文本: We do this because our top priority must be to help all people to enjoy a safe and secure life in their home countries.

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
        "span": "We do this"
      },
      "effect": {
        "span": "our top priority must be to help all people to enjoy a safe and secure life in their home countries"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10388 ---

输入文本: We also have to develop programmes aimed at increasing the opportunities for our young people to start their own businesses.

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
        "span": "develop programmes aimed at increasing the opportunities for our young people"
      },
      "effect": {
        "span": "to start their own businesses"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13896 ---

输入文本: We must follow up on these recommendations in order to give meaning to the shared commitments to our young people.

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
      "cause": "must follow up",
      "effect": "give meaning"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "follow up on these recommendations"
      },
      "effect": {
        "span": "in order to give meaning to the shared commitments to our young people"
      },
      "relation": "caused"
    }
  ]
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

### --- id=9191 ---

输入文本: As part of the changes made, UKHSA has used more accurate algorithms to check existing surveillance data.

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
        "span": "UKHSA has used more accurate algorithms"
      },
      "effect": {
        "span": "to check existing surveillance data"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2923 ---

输入文本: And in what can only be considered a collective punishment against a million civilians that have rejected the Turkish occupation in Hasakah and a dozen other towns, the Turkish regime has deliberately and repeatedly cut the city’s water supply, endangering the lives of civilians, especially in the COVID-19 pandemic.

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
      "cause": "has deliberately and repeatedly cut the city’s water supply",
      "effect": "endangering the lives of civilians, especially in the COVID-19 pandemic"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Turkish regime has deliberately and repeatedly cut the city’s water supply"
      },
      "effect": {
        "span": "endangering the lives of civilians"
      },
      "relation": "caused"
    }
  ]
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

### --- id=11074 ---

输入文本: In accordance with the resolution, the joint military exercises between the Republic of Korea and the United States that had been planned for the spring of 2018 were suspended, thereby creating an environment that enabled the North Korean Olympic delegation to come to Pyeong Chang.

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
      "cause": "were suspended",
      "effect": "thereby creating an environment that enabled the North Korean Olympic delegation to come to Pyeong Chang"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the joint military exercises between the Republic of Korea and the United States that had been planned for the spring of 2018 were suspended"
      },
      "effect": {
        "span": "creating an environment that enabled the North Korean Olympic delegation to come to Pyeong Chang"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=5218 ---

输入文本: As cases of Omicron rise rapidly around the country, the additional £60 million will help protect both those who receive care, the family and friends who support them, as well as the adult social care workforce.

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
      "cause": "the additional £60 million",
      "effect": "will help protect both those who receive care, the family and friends who support them, as well as the adult social care workforce"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the additional £60 million"
      },
      "effect": {
        "span": "help protect both those who receive care, the family and friends who support them, as well as the adult social care workforce"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=3535 ---

输入文本: It has made our planet safer by setting and improving global standards on human rights, rule of law, accountability, conflict prevention, peacekeeping and disarmament.

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
      "cause": "setting and improving global standards on human rights, rule of law, accountability, conflict prevention, peacekeeping and disarmament",
      "effect": "has made our planet safer"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "setting and improving global standards on human rights, rule of law, accountability, conflict prevention, peacekeeping and disarmament"
      },
      "effect": {
        "span": "made our planet safer"
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

### --- id=9976 ---

输入文本: The world we live in today needs a consensual approach, now more than ever before, in order to confront such major challenges as climate change, terrorism, the peaceful settlement of conflicts, peacekeeping around the world, the reform of the Security Council, threats to multilateralism and the issue of migration.

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
        "span": "needs a consensual approach"
      },
      "effect": {
        "span": "in order to confront such major challenges as climate change, terrorism, the peaceful settlement of conflicts, peacekeeping around the world, the reform of the Security Council, threats to multilateralism and the issue of migration"
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
        "span": "the damage that Lebanon is likely to suffer as a result because it hosts a large number of refugees"
      },
      "effect": {
        "span": "undermine any chance for peace in the Middle East"
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
        "span": "relocated some of them to Bhasan Char"
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
        "span": "two antivirals"
      },
      "effect": {
        "span": "speed up recovery time and stop infections progressing"
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
        "span": "the achievement of the Sustainable Development Goals (SDGs) practically unattainable"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16023 ---

输入文本: In the absence of trust, the potential for conflict grows and once conflicts have erupted, their resolution always requires rebuilding trust.

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
        "span": "In the absence of trust"
      },
      "effect": {
        "span": "the potential for conflict grows"
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
        "span": "help them weather the economic storm"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=454 ---

输入文本: New findings on Monday reinforced how vital the boosters are in maintaining protection ahead of winter, with the first UK real-world study from the UK Health Security Agency showing that boosters give over 90% protection against symptomatic COVID-19 in adults over 50.

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
        "span": "boosters give over 90% protection against symptomatic COVID-19 in adults over 50"
      },
      "effect": {
        "span": "maintaining protection ahead of winter"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=355 ---

输入文本: It was created after our shared experience of the strife and suffering of the Second World War with a noble mission to transform the nation’s health.

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
        "span": "our shared experience of the strife and suffering of the Second World War"
      },
      "effect": {
        "span": "to transform the nation’s health"
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

### --- id=13705 ---

输入文本: To this end, the Government has introduced feed-in tariffs for wind, solar and hydropower energy and is working to refine the relevant legislation in support of renewable energy.

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
        "span": "the Government has introduced feed-in tariffs for wind, solar and hydropower energy"
      },
      "effect": {
        "span": "in support of renewable energy"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14758 ---

输入文本: Throughout the ages, education has been the most equitable source of opportunities and has provided the fastest and most reliable route out of poverty.

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
        "span": "education has been the most equitable source of opportunities"
      },
      "effect": {
        "span": "has provided the fastest and most reliable route out of poverty"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13754 ---

输入文本: To protect human life, the international community should continue to seriously address that vice.

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
      "cause": "address",
      "effect": "protect"
    }
  ],
  "pred_triples": []
}
```

### --- id=16361 ---

输入文本: It is time for all countries — developed or developing, rich or poor — to join hands and take bold climate action to save Mother Earth.

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
        "span": "join hands and take bold climate action"
      },
      "effect": {
        "span": "to save Mother Earth"
      },
      "relation": "caused"
    }
  ]
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
        "span": "all countries of the world can enjoy a shared source of resiliency with the appropriate tools for dealing with myriad crises like COVID-19 and avoid undoing decades of collective work within our Organization and various regional communities"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=16264 ---

输入文本: They warn that global warming is turning our seas into a huge potential threat to humankind, reporting that global average sea levels could rise by up to 1.1 metres by 2100, in the worst-case warming scenario.

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
        "span": "global warming"
      },
      "effect": {
        "span": "global average sea levels could rise by up to 1.1 metres by 2100"
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
        "span": "providing Digital Access to its millions of citizens"
      },
      "effect": {
        "span": "ensuring empowerment and transparency"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4313 ---

输入文本: In the film, the players discuss how the pandemic has directly affected their lives.

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
      "effect": {
        "span": "directly affected their lives"
      },
      "relation": "caused"
    }
  ]
}
```
