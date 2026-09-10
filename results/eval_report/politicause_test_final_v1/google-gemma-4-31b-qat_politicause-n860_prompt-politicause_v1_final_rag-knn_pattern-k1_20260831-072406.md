# Gemma 4 31B QAT politicause Fixed + RAG eval report

## 配置
```json
{
  "label": "Gemma 4 31B QAT politicause Fixed + RAG",
  "model": "google/gemma-4-31b-qat",
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
================ Gemma 4 31B QAT politicause Fixed + RAG final report ================
样本总数: 860
  Gold 含因果: 245 | Pred 含因果: 404
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.785
  Precision: 0.574
  Recall   : 0.947
  F1       : 0.715
  (TP=232, TN=443, FP=172, FN=13)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 860
    Gold triples: 245 | Pred triples: 404
    Precision: 0.240
    Recall   : 0.396
    F1       : 0.299
    (TP=97, FP=307, FN=148)
  [anchor_window] (primary)
    样本数: 860
    Gold triples: 245 | Pred triples: 404
    Precision: 0.485
    Recall   : 0.800
    F1       : 0.604
    (TP=196, FP=208, FN=49)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 232
    Gold triples: 232 | Pred triples: 232
    Precision: 0.418
    Recall   : 0.418
    F1       : 0.418
    (TP=97, FP=135, FN=135)
  [anchor_window] (primary)
    样本数: 232
    Gold triples: 232 | Pred triples: 232
    Precision: 0.845
    Recall   : 0.845
    F1       : 0.845
    (TP=196, FP=36, FN=36)
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

Sample details shown: first 200 of 221 wrong samples from 860 total samples.

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
        "span": "to thereby combat extreme poverty, which affects the most vulnerable in society"
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
      "cause": "get the jab",
      "effect": "this will help to prevent the serious consequences of catching COVID-19 in pregnancy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "go and get the jab"
      },
      "effect": {
        "span": "will help to prevent the serious consequences of catching COVID-19 in pregnancy"
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
        "span": "that will make it possible to reverse the abysmal and shameful inequality on the planet"
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
        "span": "without it"
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

### --- id=9737 ---

输入文本: His momentous visit put a spotlight on the climate crisis and the deepening threats to the ocean.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "His momentous visit"
      },
      "effect": {
        "span": "put a spotlight on the climate crisis and the deepening threats to the ocean"
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
        "span": "the South Caucasus to cease to be one of the areas of conflict and tension in the world"
      },
      "effect": {
        "span": "with a view to achieving a fair and peaceful future"
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
      "cause": "those",
      "effect": "more severe illness"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "characteristics that make them more transmissible, cause more severe illness or are more likely to evade immune responses developed from vaccination or prior infection"
      },
      "effect": {
        "span": "New variants are the most serious risk to global recovery from the pandemic"
      },
      "relation": "caused"
    }
  ]
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
        "span": "adverse effects that this glaring gap has had on Government’s ability to manage its macroeconomic affairs"
      },
      "relation": "caused"
    }
  ]
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
        "span": "bring together over 190 states to discuss issues relating to international travel"
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
        "span": "to safeguard the most important international strategic maritime lanes"
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
        "span": "It should provide us with a platform"
      },
      "effect": {
        "span": "to realistically address this serious issue"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=11051 ---

输入文本: We need to avoid creating rival economic blocs or a bifurcated global economy that forces countries to choose sides and undermines the international order.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "creating rival economic blocs or a bifurcated global economy"
      },
      "effect": {
        "span": "that forces countries to choose sides and undermines the international order"
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
        "span": "begin with small steps"
      },
      "effect": {
        "span": "to build trust"
      },
      "relation": "caused"
    }
  ]
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
        "span": "JCVI will continue to closely review all available data"
      },
      "effect": {
        "span": "to develop further advice in due course"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=1385 ---

输入文本: A further 3 cases have been identified in Scotland, bringing the total to 13.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "A further 3 cases have been identified in Scotland"
      },
      "effect": {
        "span": "bringing the total to 13"
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
        "span": "yearned for its reform"
      },
      "effect": {
        "span": "in order to make it more democratic and responsive to the needs of all nations, rich and poor, big and small, strong and weak"
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
        "span": "Andorra has promoted inclusive educational policies"
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

### --- id=12648 ---

输入文本: The unprecedented format of this 75th session of our General Assembly points to the gravity of the situation the world is experiencing, and the need to do everything possible to ensure that our Organization can continue to fulfil its missions in the service of humanity.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "do everything possible"
      },
      "effect": {
        "span": "to ensure that our Organization can continue to fulfil its missions in the service of humanity"
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
        "span": "upcoming NPT Review Conference will lead to a successful outcome"
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
        "span": "making sure they get the vaccine"
      },
      "effect": {
        "span": "to protect themselves and those around them"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15254 ---

输入文本: We support all efforts to make peacekeeping missions more effective, bringing real and tangible contributions to the host countries.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "make peacekeeping missions more effective"
      },
      "effect": {
        "span": "bringing real and tangible contributions to the host countries"
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
        "span": "as we look to spend more valuable time with our loved ones"
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

### --- id=4285 ---

输入文本: Looking to the future, G7 partners agreed that a joined-up approach was essential to mitigate against risks associated with the current pandemic and any future health threats, understanding how to safeguard international travel, and providing a high level of resilience for the sector in the longer term.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "a joined-up approach"
      },
      "effect": {
        "span": "to mitigate against risks associated with the current pandemic and any future health threats, understanding how to safeguard international travel, and providing a high level of resilience for the sector in the longer term"
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

### --- id=9003 ---

输入文本: This year’s landmark events including HM The Queen’s Platinum Jubilee, the Commonwealth Games and the ground-breaking ‘Unboxed’ events across the UK, set to be global tourism draws, also present exciting and timely opportunities to highlight experiences that visitors can only have here, and to promote our warm welcome and creativity to the world.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "This year’s landmark events including HM The Queen’s Platinum Jubilee, the Commonwealth Games and the ground-breaking ‘Unboxed’ events across the UK"
      },
      "effect": {
        "span": "present exciting and timely opportunities to highlight experiences that visitors can only have here, and to promote our warm welcome and creativity to the world"
      },
      "relation": "caused"
    }
  ]
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

### --- id=16031 ---

输入文本: The only way to overcome global challenges is to see and treat them as a whole — a complex, multifaceted threat, but doing so is far from easy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "to see and treat them as a whole — a complex, multifaceted threat"
      },
      "effect": {
        "span": "to overcome global challenges"
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

### --- id=12841 ---

输入文本: We are concerned about the threats to world peace and security from extremist groups in the Sahel, the Democratic Republic of the Congo, Mozambique and other parts of the world, which require the international community to constantly mobilize to strengthen our capacity to respond to such dangerous assaults on social and economic stability.

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
      "cause": "the threats to world peace and security from extremist groups in the Sahel, the Democratic Republic of the Congo, Mozambique and other parts of the world",
      "effect": "which require the international community to constantly mobilize to strengthen our capacity to respond to such dangerous assaults on social and economic stability"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "threats to world peace and security from extremist groups in the Sahel, the Democratic Republic of the Congo, Mozambique and other parts of the world"
      },
      "effect": {
        "span": "which require the international community to constantly mobilize to strengthen our capacity to respond to such dangerous assaults on social and economic stability"
      },
      "relation": "caused"
    }
  ]
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
        "span": "to ensure that the people have access to humanitarian assistance"
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
        "span": "we will collaborate with farmers to build systems in New Zealand"
      },
      "effect": {
        "span": "that every farmer will be able to use to measure, manage and reduce their own farm’s emissions"
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
        "span": "we must tackle together"
      },
      "effect": {
        "span": "if we are to energize multilateral efforts to eradicate poverty, promote quality education, address climate change and foster inclusion"
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
        "span": "an age-old atavistic claim"
      },
      "effect": {
        "span": "has hindered Belize’s development and made more difficult the relations of friendship and cooperation that both our peoples aspire to and deserve"
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
        "span": "so parents can, if they want, take up the offer to increase protection against potential future waves of COVID-19 as we learn to live with this virus"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10857 ---

输入文本: Technology has meant a qualitative leap for humankind.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Technology"
      },
      "effect": {
        "span": "a qualitative leap for humankind"
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
        "span": "in order to confront the urgency of the pandemic"
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
        "span": "the transformation of Botswana’s economy from one that largely relies on the extractive industry, which is vulnerable to globe shocks, to a knowledge-based economy"
      },
      "effect": {
        "span": "To realize this ambition"
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
        "span": "Switzerland works closely with universities and the private sector"
      },
      "effect": {
        "span": "to find innovative technological approaches for development and poverty-reduction projects"
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

### --- id=2720 ---

输入文本: The imminent water crisis is a threat, but it also presents an opportunity to rethink water innovation, governance and collaboration on all levels.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "The imminent water crisis"
      },
      "effect": {
        "span": "presents an opportunity to rethink water innovation, governance and collaboration on all levels"
      },
      "relation": "caused"
    }
  ]
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
        "span": "a key driver of our country’s sustainable economic development, prosperity, and stability"
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

### --- id=9697 ---

输入文本: In the same way, the world’s actions today are critical to our global prosperity tomorrow.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the world’s actions today"
      },
      "effect": {
        "span": "are critical to our global prosperity tomorrow"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=2989 ---

输入文本: Given the critical stage of the negotiations, Trinidad and Tobago remains hopeful for its early resumption, the successful completion of which would redound to the benefit of all humankind.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the successful completion of which"
      },
      "effect": {
        "span": "would redound to the benefit of all humankind"
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
        "span": "a key driver for a sustainable fight against poverty and climate change"
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
        "span": "that was preventing us from taking advantage of all the potential that we have to achieve greater levels of progress and development"
      },
      "relation": "caused"
    }
  ]
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

### --- id=4801 ---

输入文本: It celebrates those who have had their booster vaccine, and anyone who sees content with the booster filter can tap on a link to get more information about vaccines and where they can book their jab.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "can tap on a link"
      },
      "effect": {
        "span": "to get more information about vaccines and where they can book their jab"
      },
      "relation": "caused"
    }
  ]
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
      "cause": "imposing a blockade and unilateral coercive economic measures",
      "effect": "have resorted to economic terrorism"
    }
  ],
  "pred_triples": []
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

### --- id=1293 ---

输入文本: Dr Mary Ramsay, Head of Immunisation at UKHSA, said: These early estimates should be treated with caution but they indicate that a few months after the second jab, there is a greater risk of catching the Omicron variant compared to Delta strain.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "a few months after the second jab"
      },
      "effect": {
        "span": "there is a greater risk of catching the Omicron variant compared to Delta strain"
      },
      "relation": "caused"
    }
  ]
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
        "span": "coronavirus disease (COVID-19) pandemic"
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
      "cause": "climate change",
      "effect": "has tested the resilience of the food we grow as well as the patience of the growers."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "climate change"
      },
      "effect": {
        "span": "has tested the resilience of the food we grow as well as the patience of the growers"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8548 ---

输入文本: Anyone who needs to leave their home whilst they have symptoms of a respiratory infection such as COVID-19, or within 5 days following the day of their positive test, should take important precautions to minimise the chance of passing on their infection.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "should take important precautions"
      },
      "effect": {
        "span": "to minimise the chance of passing on their infection"
      },
      "relation": "caused"
    }
  ]
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
        "span": "were able to take advantage of the latest technological developments"
      },
      "effect": {
        "span": "to benefit everyone"
      },
      "relation": "caused"
    }
  ]
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

### --- id=2793 ---

输入文本: Agdam city was destroyed to such an extent that it was called as Hiroshima of Caucasus.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Agdam city was destroyed to such an extent"
      },
      "effect": {
        "span": "that it was called as Hiroshima of Caucasus"
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
        "span": "owing to its geographical location at the centre of the ancient world"
      },
      "effect": {
        "span": "Turkey is a rightful successor to the collective heritage of both Eastern and Western civilizations"
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
        "span": "by developing the vaccines and treatments"
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
        "span": "all the pressures on our finances in the United Kingdom"
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
        "span": "NVAP will continue to work with the WHO Eastern Mediterranean region"
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
        "span": "the climate crisis looms ever larger, heightened"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8258 ---

输入文本: Rohan said: Looking after our mental wellbeing is the most important thing we can do, and I want to encourage us all to think about the simple things we can do every day which are life-giving and positively impact our mental health.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the simple things we can do every day which are life-giving"
      },
      "effect": {
        "span": "positively impact our mental health"
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
        "span": "non-traditional security challenges as disease or climate change if they are not addressed in a timely and decisive manner"
      },
      "effect": {
        "span": "the shocking destruction"
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

### --- id=799 ---

输入文本: Anyone with symptoms or a positive tests should limit their contact with others as much as possible.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Anyone with symptoms or a positive tests"
      },
      "effect": {
        "span": "should limit their contact with others as much as possible"
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
        "span": "will be game-changers for Kiribati’s development curve"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9716 ---

输入文本: We are presently in a war against climate change, and it is a war that humankind can win if we first acknowledge the existential threat it poses and if the Security Council treats it as such, because it is in fact a security threat.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "if we first acknowledge the existential threat it poses and if the Security Council treats it as such"
      },
      "effect": {
        "span": "humankind can win"
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
        "span": "is protecting millions of people from COVID-19"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10054 ---

输入文本: I believe very strongly that we currently need a robust inter-Libyan reconciliation conference and a firm commitment from the African Union, alongside the United Nations, to achieve that.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "a robust inter-Libyan reconciliation conference and a firm commitment from the African Union, alongside the United Nations"
      },
      "effect": {
        "span": "to achieve that"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13629 ---

输入文本: And just as the Security Council should reflect the composition of the United Nations membership, I want to repeat Ireland’s deeply held view that political reform of the Council must lead to a greater sense of participation, responsibility and ownership among the membership, something that we believe would be a positive for the functioning of the United Nations more widely, as well as more just.

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
      "cause": "political reform of the Council",
      "effect": "lead to a greater sense"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "political reform of the Council must lead to"
      },
      "effect": {
        "span": "a greater sense of participation, responsibility and ownership among the membership"
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

### --- id=13046 ---

输入文本: Countries like Nepal need many resources if they are to fully realize the SDGs by 2030, and while mobilizing domestic financial resources is a priority for us, our national efforts, particularly those of LDCs and LLDCs, will have to be complemented by international support measures in the form of technical, financial, investment and other means of support.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Countries like Nepal need many resources"
      },
      "effect": {
        "span": "if they are to fully realize the SDGs by 2030"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4540 ---

输入文本: Six cases of Lambda have been identified across the country to date, all have been linked to overseas travel.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "overseas travel"
      },
      "effect": {
        "span": "Six cases of Lambda have been identified across the country to date"
      },
      "relation": "caused"
    }
  ]
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
        "span": "the new Independent Investigative Mechanism for Myanmar"
      },
      "effect": {
        "span": "to bring Myanmar before such tribunals as the International Criminal Court"
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
        "span": "Kazakhstan will not become a success story of socioeconomic development unless"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12437 ---

输入文本: Whether it is the fight against the pandemic, financing development to advance our quality of life or the need for collective action to maintain peace, we must act together to live together.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "we must act together"
      },
      "effect": {
        "span": "to live together"
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
        "span": "we have adopted the Aotearoa New Zealand Biodiversity Strategy 2020 — Te Mana o te Taiao"
      },
      "effect": {
        "span": "which will guide our actions domestically for the protection, restoration and sustainable use of biodiversity"
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
        "span": "because of the existential vulnerabilities that we suffer in the face of this growing threat"
      },
      "effect": {
        "span": "We speak out, and we speak loudly"
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
        "span": "New technologies are coming on line"
      },
      "effect": {
        "span": "creating a circular plastics economy"
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
        "span": "to building a stable and prosperous new Middle East"
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
        "span": "take the simple step"
      },
      "effect": {
        "span": "that will help secure greater freedom for us all"
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

### --- id=5482 ---

输入文本: The COVID-19 vaccination programme has been a historic national effort for both the NHS and the public, with tens of thousands of volunteers stepping up to support NHS staff and thousands of people queuing up to secure the protection for themselves and others.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "thousands of people queuing up"
      },
      "effect": {
        "span": "to secure the protection for themselves and others"
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
      "cause": "has taken specific steps",
      "effect": "to ensure international security, such as when it abandoned its nuclear arsenal, which at the time exceeded the nuclear capacities of the United Kingdom, France and China combined"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "abandoned its nuclear arsenal"
      },
      "effect": {
        "span": "to ensure international security"
      },
      "relation": "caused"
    }
  ]
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
        "span": "Security Council reform"
      },
      "effect": {
        "span": "so as to thereby transform the Council into a more inclusive and transparent body, capable of addressing threats to international peace and security"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=4302 ---

输入文本: Thanks to the phenomenal success of the vaccination programme, the data continues to show the link between cases, hospitalisations and deaths has weakened significantly.

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
      "cause": "the phenomenal success of the vaccination programme",
      "effect": "the data continues to show the link between cases, hospitalisations and deaths has weakened significantly"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Thanks to the phenomenal success of the vaccination programme"
      },
      "effect": {
        "span": "the link between cases, hospitalisations and deaths has weakened significantly"
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

### --- id=11312 ---

输入文本: This great Organization has helped foster peace and avert conflict for over half a century.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "This great Organization"
      },
      "effect": {
        "span": "has helped foster peace and avert conflict"
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
        "span": "to combat those challenges"
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
        "span": "A temporary ban on commercial and private planes travelling from the six countries will also come into force at midday on Friday until 4am Sunday"
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
      "cause": "can fluctuate",
      "effect": "should be interpreted with caution"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "new variants are identified"
      },
      "effect": {
        "span": "early findings can change quickly"
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

### --- id=10584 ---

输入文本: We continue to be confronted by the problems of blacklisting, which pale in significance when compared to climate change but which destroy our financial sector.

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
      "cause": "problems",
      "effect": "destroy our financial sector"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "blacklisting"
      },
      "effect": {
        "span": "which destroy our financial sector"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=15596 ---

输入文本: But this effort must be global, as neither the Principality’s commitments nor those of any other country alone will be able to prevent the temperature from rising beyond 1.5°C by the end of the century.

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
      "cause": "to prevent the temperature from rising beyond 1.5°C",
      "effect": "must be global"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "neither the Principality’s commitments nor those of any other country alone"
      },
      "effect": {
        "span": "will be able to prevent the temperature from rising beyond 1.5°C by the end of the century"
      },
      "relation": "caused"
    }
  ]
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
        "span": "will lead to the signing of peace agreements between our countries"
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
        "span": "our top priority must be to help all people to enjoy a safe and secure life in their home countries"
      },
      "effect": {
        "span": "We do this"
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
        "span": "develop programmes"
      },
      "effect": {
        "span": "aimed at increasing the opportunities for our young people to start their own businesses"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10052 ---

输入文本: It further requires a free electoral process that will include all Syrian citizens.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "a free electoral process"
      },
      "effect": {
        "span": "will include all Syrian citizens"
      },
      "relation": "caused"
    }
  ]
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
        "span": "by setting and improving global standards on human rights, rule of law, accountability, conflict prevention, peacekeeping and disarmament"
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
        "span": "to respect the rules and to live and act by them"
      },
      "effect": {
        "span": "because we can then predict how we behave and be prepared when the unexpected happens"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=13526 ---

输入文本: Our continent, Africa, has made considerable strides in the areas of governance, peace and security, which are prerequisites for sustainable development.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "considerable strides in the areas of governance, peace and security"
      },
      "effect": {
        "span": "which are prerequisites for sustainable development"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=7433 ---

输入文本: We have made every effort to mobilize our internal strength, maintain our self-reliance and adapt to the prevailing trends of our time to reach the level we are at in our potential, international standing and prestige today.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "made every effort to mobilize our internal strength, maintain our self-reliance and adapt to the prevailing trends of our time"
      },
      "effect": {
        "span": "to reach the level we are at in our potential, international standing and prestige today"
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
        "span": "The Judaization of Al-Quds, the policy of systematic colonization, the laws that contravene human rights, the recognition of the annexation of lands occupied by force, as in the case of the Golan Heights, the election promises to annex new lands, with all the leaks about the so-called deal of the century, changing the borders of some States and undermining their territorial unity, while eliminating the Palestinian cause and keeping the Palestinians where they are, as well as the damage that Lebanon is likely to suffer as a result because it hosts a large number of refugees"
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

### --- id=13817 ---

输入文本: While we recognize the difficulties and problems that stand in the way, we believe that with goodwill and firm resolve we can overcome them together.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "with goodwill and firm resolve"
      },
      "effect": {
        "span": "we can overcome them together"
      },
      "relation": "caused"
    }
  ]
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
        "span": "two antivirals"
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
        "span": "if not addressed"
      },
      "effect": {
        "span": "will make the achievement of the Sustainable Development Goals (SDGs) practically unattainable"
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

### --- id=16457 ---

输入文本: It is therefore critical that United Nations programmes target the family at that level, where the fragmentation of values creates a fault line in our societies.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the fragmentation of values"
      },
      "effect": {
        "span": "creates a fault line in our societies"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=8780 ---

输入文本: COVID-19 infections can be very severe in pregnancy, particularly if women get infected in the third trimester of pregnancy or if they have underlying medical problems.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "women get infected in the third trimester of pregnancy or if they have underlying medical problems"
      },
      "effect": {
        "span": "COVID-19 infections can be very severe in pregnancy"
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
        "span": "in preventing the collapse of the international order and preserving relations among States"
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
        "span": "boosters"
      },
      "effect": {
        "span": "give over 90% protection against symptomatic COVID-19 in adults over 50"
      },
      "relation": "caused"
    }
  ]
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

### --- id=397 ---

输入文本: And now we have the defensive shield of our vaccination programme, we must be ambitious about restoring services and not let anything stand in our way.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "we have the defensive shield of our vaccination programme"
      },
      "effect": {
        "span": "we must be ambitious about restoring services and not let anything stand in our way"
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
        "span": "education"
      },
      "effect": {
        "span": "has provided the fastest and most reliable route out of poverty"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=14321 ---

输入文本: The challenge of access to quality education for all, the second element of this session’s theme, is of particular concern to us because the development experience in the decades since our independence has strengthened our conviction that there is no wealth but human beings.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "because the development experience in the decades since our independence has strengthened our conviction that there is no wealth but human beings"
      },
      "effect": {
        "span": "is of particular concern to us"
      },
      "relation": "caused"
    }
  ]
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
        "span": "so that all countries of the world can enjoy a shared source of resiliency with the appropriate tools for dealing with myriad crises like COVID-19 and avoid undoing decades of collective work within our Organization and various regional communities"
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
        "span": "is turning our seas into a huge potential threat to humankind"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=12952 ---

输入文本: We are now engaged in direct diplomatic initiatives to strengthen the links as a matter of core strategic interests with our African brothers and sisters.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "We are now engaged in direct diplomatic initiatives"
      },
      "effect": {
        "span": "to strengthen the links as a matter of core strategic interests with our African brothers and sisters"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=10659 ---

输入文本: Built in 1863, over the decades this 89-foot lighthouse has helped to warn mariners of the dangerous reefs below.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "this 89-foot lighthouse"
      },
      "effect": {
        "span": "has helped to warn mariners of the dangerous reefs below"
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
        "span": "India is providing Digital Access to its millions of citizens"
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

### --- id=10827 ---

输入文本: I would like to end my address by appealing to the need to put an end to the economic, commercial and financial blockade that weighs on Cuba and by calling for positive developments to be resumed, which has given rise to great optimism in the international community.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "calling for positive developments to be resumed"
      },
      "effect": {
        "span": "which has given rise to great optimism in the international community"
      },
      "relation": "caused"
    }
  ]
}
```

### --- id=9889 ---

输入文本: Viet Nam believes that respect for international law is the most effective means of preventing conflicts and seeking sustainable solutions to disputes.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "respect for international law"
      },
      "effect": {
        "span": "preventing conflicts and seeking sustainable solutions to disputes"
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
