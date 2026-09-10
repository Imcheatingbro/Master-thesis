# politicause_validation first 300 eval report

## 配置
```json
{
  "label": "politicause_validation first 300",
  "model": "google/gemma-4-31b-qat",
  "dataset": "politicause_validation",
  "sample_count": 300,
  "prompt_name": "v8.12_zero_shot",
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
  Gold 含因果: 85 | Pred 含因果: 47
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.760
  Precision: 0.638
  Recall   : 0.353
  F1       : 0.455
  (TP=30, TN=198, FP=17, FN=55)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 300
    Gold triples: 85 | Pred triples: 47
    Precision: 0.298
    Recall   : 0.165
    F1       : 0.212
    (TP=14, FP=33, FN=71)
  [anchor_window] (primary)
    样本数: 300
    Gold triples: 85 | Pred triples: 47
    Precision: 0.447
    Recall   : 0.247
    F1       : 0.318
    (TP=21, FP=26, FN=64)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 30
    Gold triples: 30 | Pred triples: 30
    Precision: 0.467
    Recall   : 0.467
    F1       : 0.467
    (TP=14, FP=16, FN=16)
  [anchor_window] (primary)
    样本数: 30
    Gold triples: 30 | Pred triples: 30
    Precision: 0.700
    Recall   : 0.700
    F1       : 0.700
    (TP=21, FP=9, FN=9)
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

Sample details shown: all 81 wrong samples from 300 total samples.

### --- id=12959 ---

输入文本: I have no doubt that his extensive experience and leadership will enable him to successfully conduct our deliberations.

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
      "cause": "his extensive experience and leadership",
      "effect": "enable him to successfully conduct our deliberations"
    }
  ],
  "pred_triples": []
}
```

### --- id=15348 ---

输入文本: At the same time, to help us recover from the economic devastation caused by this pandemic, the starting point is three words: Cancel the Debts.

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
      "cause": "this pandemic",
      "effect": "the economic devastation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "this pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "economic devastation"
      }
    }
  ]
}
```

### --- id=5582 ---

输入文本: Today, we are also reminded about the vital importance of fighting this virus to protect our economy.

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
      "cause": "fighting this virus",
      "effect": "protect our economy"
    }
  ],
  "pred_triples": []
}
```

### --- id=13401 ---

输入文本: We are profoundly thankful for all the attention and support from the Organization and its Member States and specialized agencies in the aftermath of the massive devastation inflicted on us by the category 5 Hurricane Maria in September 2017.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "category 5 Hurricane Maria in September 2017"
      },
      "relation": "caused",
      "effect": {
        "span": "massive devastation inflicted on us"
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
      "cause": "submitted voluntary reports that take stock of the significant progress we have made in each of the 17 Goals",
      "effect": "in order to properly ensure accountability"
    }
  ],
  "pred_triples": []
}
```

### --- id=15577 ---

输入文本: It also inflicted collective punishment on people, deliberately and repeatedly cutting off the water supply of more than 1 million Syrians in Al-Hasakah and its surrounding residential areas.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "deliberately and repeatedly cutting off the water supply of more than 1 million Syrians in Al-Hasakah and its surrounding residential areas"
      },
      "relation": "caused",
      "effect": {
        "span": "inflicted collective punishment on people"
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
      "effect": "strengthen"
    }
  ],
  "pred_triples": []
}
```

### --- id=2595 ---

输入文本: Only a global response facilitating access for all to vaccines can put an end to this global scourge.

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
      "cause": "facilitating access for all to vaccines",
      "effect": "put an end to this global scourge"
    }
  ],
  "pred_triples": []
}
```

### --- id=13779 ---

输入文本: Today, the mobile and instantaneous nature of communications have brought us closer to the misfortunes of all in a much more direct way.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the mobile and instantaneous nature of communications have brought us closer"
      },
      "relation": "caused",
      "effect": {
        "span": "to the misfortunes of all in a much more direct way"
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
      "cause": "have signed a pact with the youth",
      "effect": "make a genuine change in the policies that will benefit them"
    }
  ],
  "pred_triples": []
}
```

### --- id=13195 ---

输入文本: That leads us to our current dedicated efforts, which we are undertaking together with other ASEAN members, to push for partnership and turn conflicts into cooperation so that development and progress can be sustainable.

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
      "cause": "current dedicated efforts, which we are undertaking together with other ASEAN members",
      "effect": "development and progress can be sustainable"
    }
  ],
  "pred_triples": []
}
```

### --- id=12742 ---

输入文本: We are now embarking on reviving our tourism sector, which was badly affected because of the travel restrictions imposed in many countries in order to curb the spread of COVID-19.

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
      "cause": "travel restrictions imposed in many countries in order to curb the spread of COVID-19",
      "effect": "was badly affected"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the travel restrictions imposed in many countries"
      },
      "relation": "caused",
      "effect": {
        "span": "tourism sector, which was badly affected"
      }
    }
  ]
}
```

### --- id=6025 ---

输入文本: On this note, the Lao PDR continues its economic infrastructure development in order to efficiently facilitate the regional and subregional integration through various cooperation frameworks.

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
      "cause": "economic infrastructure development",
      "effect": "efficiently facilitate the regional and subregional integration through various cooperation frameworks"
    }
  ],
  "pred_triples": []
}
```

### --- id=11986 ---

输入文本: We reiterate the call on all parties to commit to updated and more ambitious NDCs in order to meet the Paris Agreement promise.

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
      "cause": "commit to updated and more ambitious NDCs",
      "effect": "meet the Paris Agreement promise"
    }
  ],
  "pred_triples": []
}
```

### --- id=13587 ---

输入文本: To reject the norms of collective, mutually respectful action taken together in favour of aggressive individual action, or to retreat to an old, false rhetoric of war, promises misery in the form of a continuity of instability, imbalance, social inequality and exploitation in every aspect of a potential shared life.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "To reject the norms of collective, mutually respectful action taken together in favour of aggressive individual action, or to retreat to an old, false rhetoric of war"
      },
      "relation": "caused",
      "effect": {
        "span": "promises misery in the form of a continuity of instability, imbalance, social inequality and exploitation in every aspect of a potential shared life"
      }
    }
  ]
}
```

### --- id=11364 ---

输入文本: Precisely because it was Germany that 80 years ago unleashed fire and destruction in Europe and the world, we must assume a special responsibility today for an order that secures peace.

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
      "cause": "80 years ago unleashed fire and destruction in Europe and the world",
      "effect": "we must assume a special responsibility today for an order that secures peace"
    }
  ],
  "pred_triples": []
}
```

### --- id=12299 ---

输入文本: We urge the United Nations to increase its collaboration and partnerships with those bodies and Governments in order to usher in a more peaceful subregion.

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
      "cause": "increase its collaboration and partnerships",
      "effect": "usher in a more peaceful subregion"
    }
  ],
  "pred_triples": []
}
```

### --- id=7769 ---

输入文本: This is now easier than ever before as vaccinations are now available both through school or a walk-in centre.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "vaccinations are now available both through school or a walk-in centre"
      },
      "relation": "caused",
      "effect": {
        "span": "This is now easier than ever before"
      }
    }
  ]
}
```

### --- id=13844 ---

输入文本: The constant bullying by ruffians — and the original meaning of the word ruffians is bully boys — particularly the ruffians who are the bureaucrats of the European Union, has revealed that the unambiguous objective of the European Union is not well-regulated Caribbean financial centres but a decimated and discredited sector, while it panders to the thriving centres that exist within its own borders or in other more powerful locales.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "The constant bullying by ruffians — and the original meaning of the word ruffians is bully boys — particularly the ruffians who are the bureaucrats of the European Union"
      },
      "relation": "caused",
      "effect": {
        "span": "has revealed that the unambiguous objective of the European Union is not well-regulated Caribbean financial centres but a decimated and discredited sector"
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
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
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
        "span": "gave Afghans tremendous belief that peace is possible and proved that the Government has the ability to directly negotiate peace with our enemies"
      }
    }
  ]
}
```

### --- id=15742 ---

输入文本: The United in Science report details the degree of acidification and deoxygenation affecting our oceans and killing marine life.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "acidification and deoxygenation affecting our oceans"
      },
      "relation": "caused",
      "effect": {
        "span": "killing marine life"
      }
    }
  ]
}
```

### --- id=11504 ---

输入文本: It should serve as a clarion call to Member States to work collaboratively, in good faith, toward early reform of the Security Council to effectively respond to the urgent needs and challenges facing the diverse membership of the United Nations.

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
      "cause": "work collaboratively, in good faith, toward early reform of the Security Council",
      "effect": "effectively respond to the urgent needs and challenges"
    }
  ],
  "pred_triples": []
}
```

### --- id=14009 ---

输入文本: In Uruguay, we are absolutely convinced that the key to facing those challenges lies in the universalization of education.

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
      "cause": "universalization of education",
      "effect": "facing"
    }
  ],
  "pred_triples": []
}
```

### --- id=13856 ---

输入文本: Immense progress has been made towards macroeconomic and fiscal stabilization as well as high-impact projects that pave the way for private-sector-led growth.

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
      "cause": "macroeconomic and fiscal stabilization as well as high-impact projects",
      "effect": "pave the way for private-sector-led growth"
    }
  ],
  "pred_triples": []
}
```

### --- id=15895 ---

输入文本: In that context, Peru reaffirms its commitment to a rules-based multilateral trading system, as reflected in the World Trade Organization, and encourages everyone to work towards strengthening and improving that organization in order to guarantee the stability, predictability and transparency of the multilateral trading system, for the benefit of all.

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
      "cause": "strengthening and improving",
      "effect": "guarantee"
    }
  ],
  "pred_triples": []
}
```

### --- id=1214 ---

输入文本: The latest data confirmed that among those who had received 2 doses of AstraZeneca, there was no effect against Omicron from 20 weeks after the second dose.

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
      "cause": "received 2 doses of AstraZeneca",
      "effect": "no effect against Omicron from 20 weeks after the second dose"
    }
  ],
  "pred_triples": []
}
```

### --- id=11799 ---

输入文本: Even more so, the path to membership serves to secure the higher standards all peoples aspire to.

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
      "cause": "membership",
      "effect": "secure"
    }
  ],
  "pred_triples": []
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

### --- id=5651 ---

输入文本: So, when the call comes, please do get a jab and, in the meantime, stay at home, protect the NHS and save lives.

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
      "cause": "stay at home",
      "effect": "protect the NHS and save"
    }
  ],
  "pred_triples": []
}
```

### --- id=10886 ---

输入文本: I urge the international community to mobilize resources in order to provide assistance.

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
      "cause": "mobilize resources",
      "effect": "provide assistance"
    }
  ],
  "pred_triples": []
}
```

### --- id=11213 ---

输入文本: In Kenya we have invested heavily in education and health in an effort to achieve social inclusion, develop knowledge and competencies and secure the future by not leaving anyone behind.

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
      "cause": "invested heavily in education and health",
      "effect": "achieve social inclusion, develop knowledge and competencies and secure the future"
    }
  ],
  "pred_triples": []
}
```

### --- id=5683 ---

输入文本: If we can catch more asymptomatic people before they unknowingly pass on the disease to the vulnerable, we can help to stop the virus’ vicious spread.

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
      "cause": "catch more asymptomatic people before they unknowingly pass on the disease",
      "effect": "help to stop the virus’ vicious spread"
    }
  ],
  "pred_triples": []
}
```

### --- id=6591 ---

输入文本: In order to prevent high-handedness and arbitrariness in the Security Council, we should increase its representation of developing countries, which make up a majority of the United Nations.

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
      "cause": "increase its representation of developing",
      "effect": "prevent"
    }
  ],
  "pred_triples": []
}
```

### --- id=12133 ---

输入文本: We’re going to be throwing everything at it, in order to ensure that everyone eligible is offered that booster in just over two months.

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
      "cause": "going to be throwing everything at it",
      "effect": "to ensure that everyone eligible is offered that booster in just over two months"
    }
  ],
  "pred_triples": []
}
```

### --- id=16743 ---

输入文本: As a nation, we see human capital as a critical enabler for achieving the SDGs.

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
      "cause": "human capital",
      "effect": "achieving"
    }
  ],
  "pred_triples": []
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

### --- id=10489 ---

输入文本: That is why we have taken the decision to implement a plan for a long-term low-emission strategy that will enable us to take the necessary steps to achieve more ambitious targets, such as carbon neutrality by the year 2050.

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
      "cause": "taken the decision to implement a plan for a long-term low-emission strategy",
      "effect": "take the necessary steps to achieve more ambitious targets"
    }
  ],
  "pred_triples": []
}
```

### --- id=14787 ---

输入文本: The transformational potential of universal health coverage is now at the top of the global health agenda, thanks to the outstanding leadership of the World Health Organization and many other stakeholders.

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
      "cause": "thanks to the outstanding leadership of the World Health Organization and many other stakeholders",
      "effect": "is now at the top of the global health agenda"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the outstanding leadership of the World Health Organization and many other stakeholders"
      },
      "relation": "caused",
      "effect": {
        "span": "The transformational potential of universal health coverage is now at the top of the global health agenda"
      }
    }
  ]
}
```

### --- id=13269 ---

输入文本: Speaking of international solidarity and inclusion, I would once again like to call from this rostrum for the total lifting of the decades-long embargo imposed on the Government and people of Cuba, in order to remove the obstacles to their achievement of the Sustainable Development Goals, which is a legitimate aspiration for all the peoples of the world.

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
      "cause": "lifting of the decades-long embargo imposed on the Government and people of Cuba",
      "effect": "remove the obstacles to their achievement of the Sustainable Development Goals"
    }
  ],
  "pred_triples": []
}
```

### --- id=11717 ---

输入文本: The European Union and its Member States must strengthen the dialogue on migration issues with the countries of origin and transit of migrants, in order to achieve joint responsibility in the management of flows.

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
      "cause": "strengthen the dialogue on migration issues with the countries of origin and transit",
      "effect": "achieve joint responsibility in the management of flows"
    }
  ],
  "pred_triples": []
}
```

### --- id=12408 ---

输入文本: Namibia, however, aims to deploy innovative approaches to ensure sustainable economic development in this volatile period of pandemic and climate change.

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
      "cause": "deploy innovative approaches",
      "effect": "ensure sustainable economic development"
    }
  ],
  "pred_triples": []
}
```

### --- id=7709 ---

输入文本: Hundreds of thousands of people continue to book in for their vital boosters with a further 1.7 million invites due to land this week and the NHS has now opened up hundreds of walk-in sites across the country so people can get their top-up protection without delay.

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
      "cause": "has now opened up hundreds of walk-in sites across the country",
      "effect": "people can get their top-up protection without delay"
    }
  ],
  "pred_triples": []
}
```

### --- id=14050 ---

输入文本: I am very confident that such an effort, with the support of the Russian Federation and the West, could radically change the profile of my country, about which I spoke with such great concern at the beginning of my address.

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
      "cause": "effort, with the support of the Russian Federation",
      "effect": "could radically change"
    }
  ],
  "pred_triples": []
}
```

### --- id=6094 ---

输入文本: We must therefore maintain our regional and international solidarity in a relentless effort to combat it and ensure our regional security.

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
      "cause": "maintain our regional and international solidarity in",
      "effect": "to combat it and ensure our regional security."
    }
  ],
  "pred_triples": []
}
```

### --- id=17630 ---

输入文本: I would like to thank the Secretariat and the host country’s services for the enormous effort they have invested to ensure that the general debate is not only a demonstration of hope and belief that the world will deal with the pandemic but also a secure and safe event for all participants.

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
      "cause": "enormous effort",
      "effect": "ensure"
    }
  ],
  "pred_triples": []
}
```

### --- id=16535 ---

输入文本: As we all know, migration is the result of deep-rooted causes that require immediate action, together with medium- to long-term perspectives.

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
      "cause": "deep-rooted causes",
      "effect": "migration"
    }
  ],
  "pred_triples": []
}
```

### --- id=16652 ---

输入文本: We are currently working on an ambitious low-carbon development strategy that will enable Latvia to reach climate neutrality by 2050.

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
      "cause": "an ambitious low-carbon development strategy",
      "effect": "reach climate neutrality"
    }
  ],
  "pred_triples": []
}
```

### --- id=3687 ---

输入文本: Yet, they try in vain to deprive Iran of its minimum defense requirements, and disregard international law and global consensus in order to extend arms restrictions against Iran in contravention of the letter of UNSCR 2231.

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
      "cause": "try in vain to deprive Iran of its minimum defense requirements, and disregard international law and global consensus",
      "effect": "in order to extend arms restrictions against Iran in contravention of the letter of UNSCR 2231"
    }
  ],
  "pred_triples": []
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
        "span": "provide long-lasting protection against this disease for up to 6 months"
      }
    }
  ]
}
```

### --- id=4182 ---

输入文本: Over time we can expect that to lead to fewer hospitalisations and deaths.

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
      "cause": "that",
      "effect": "lead to fewer hospitalisations and deaths"
    }
  ],
  "pred_triples": []
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
        "span": "Climate change is having a structural impact"
      },
      "relation": "caused",
      "effect": {
        "span": "food security, migration and even stability in many countries"
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

### --- id=15671 ---

输入文本: We will support all efforts to promote education, which is the best way to ensure a better future.

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
      "cause": "support all efforts to promote education",
      "effect": "ensure a better future"
    }
  ],
  "pred_triples": []
}
```

### --- id=16593 ---

输入文本: We must not forget the suffering of millions all over the world that results from war and natural disasters, whose severe impact requires intensified humanitarian efforts.

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
      "cause": "war and natural disasters",
      "effect": "the suffering"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "war and natural disasters"
      },
      "relation": "caused",
      "effect": {
        "span": "suffering of millions all over the world"
      }
    }
  ]
}
```

### --- id=11945 ---

输入文本: If Small States are to build back greener, bluer, and better, we will need an equal voice about and vote on decisions that determine our future.

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
      "cause": "equal voice about and vote on decisions that determine",
      "effect": "build back greener, bluer, and better"
    }
  ],
  "pred_triples": []
}
```

### --- id=3569 ---

输入文本: Mr. President, Myself as co-convener of the High Level Event on Financing for Development in the Era of COVID-19 and Beyond, along with Secretary-General Guterres and Prime Minister Trudeau, remain committed to facilitate the process of developing concrete global solutions and actions to enable countries to respond and recover better from what the Secretary-General refers to as the world’s first development emergency.

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
      "cause": "the process of developing concrete global solutions and actions",
      "effect": "enable countries to respond and recover better from what the Secretary-General refers to as the world’s first development emergency."
    }
  ],
  "pred_triples": []
}
```

### --- id=13529 ---

输入文本: The success of that project can be guaranteed only by addressing the causes of conflict in the region.

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
      "cause": "addressing the causes of conflict",
      "effect": "can be guaranteed"
    }
  ],
  "pred_triples": []
}
```

### --- id=3421 ---

输入文本: By devising a long-term low greenhouse gas emission development strategy, we will work with the international community in realizing a low-carbon society by 2050.

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
      "cause": "devising a long-term low greenhouse gas emission development strategy",
      "effect": "will work with the international community in realizing a low-carbon society by 2050"
    }
  ],
  "pred_triples": []
}
```

### --- id=10270 ---

输入文本: Since 911, Islamophobia has grown at an alarming pace.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Since 911"
      },
      "relation": "caused",
      "effect": {
        "span": "Islamophobia has grown at an alarming pace"
      }
    }
  ]
}
```

### --- id=8506 ---

输入文本: If you have not yet come forward for your primary or booster vaccine I would urge you to do so straight away – the NHS vaccine programme is there to help you and the sooner you are vaccinated the sooner you and your family and friends will be protected.

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
      "cause": "the sooner you are vaccinated",
      "effect": "the sooner you and your family and friends will be protected"
    }
  ],
  "pred_triples": []
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

### --- id=13034 ---

输入文本: The ensuing insecurity and disorder hurt least-developed countries (LDCs), landlocked developing countries (LLDCs) and small island developing States the most.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "The ensuing insecurity and disorder"
      },
      "relation": "caused",
      "effect": {
        "span": "hurt least-developed countries (LDCs), landlocked developing countries (LLDCs) and small island developing States the most"
      }
    }
  ]
}
```

### --- id=11401 ---

输入文本: In concrete terms, it will create high value-added chains through the promotion of local industry in agro-industrial sectors such as cotton, soy, sesame, coffee, cocoa and poultry.

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
      "cause": "the promotion of local industry in agro-industrial sectors such as cotton, soy, sesame, coffee, cocoa and poultry",
      "effect": "create high value-added chains"
    }
  ],
  "pred_triples": []
}
```

### --- id=3437 ---

输入文本: Egypt stresses the importance of expanding the Council in both its permanent and non-permanent categories, which will enhance its credibility and achieve a fair representation of Africa to correct the historical injustice inflicted on it, and address its legitimate demands enshrined in the Ezulwini Consensus and Sirte Declaration.

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
      "cause": "expanding the Council in both its permanent and non-permanent categories",
      "effect": "enhance its credibility and achieve a fair representation"
    }
  ],
  "pred_triples": []
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
        "span": "food preparation and cooking has helped"
      },
      "relation": "caused",
      "effect": {
        "span": "me relax"
      }
    }
  ]
}
```

### --- id=15391 ---

输入文本: Having participated virtually in the Pre-Summit held in April, I trust that the United Nations Food Systems Summit later this month will result in actionable outcomes to promote healthier, more sustainable and equitable food systems globally.

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
      "cause": "United Nations Food Systems Summit",
      "effect": "actionable outcomes to promote healthier, more sustainable and equitable food systems globally"
    }
  ],
  "pred_triples": []
}
```

### --- id=17042 ---

输入文本: While we recognize Ethiopia’s right to development, for Egypt the water of the Nile is a matter of life and existence, which places a great responsibility on the international community to play a constructive role in urging all parties to demonstrate flexibility in order to achieve a mutually satisfactory agreement.

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
      "cause": "demonstrate flexibility",
      "effect": "achieve"
    }
  ],
  "pred_triples": []
}
```

### --- id=16675 ---

输入文本: In a related context, I want to warn against the danger of reducing the services provided to Palestinian refugees by the United Nations Relief and Works Agency for Palestine Refugees in the Near East (UNRWA), which have added to the social and fiscal strains weighing on them and on us and threaten to turn Palestinian school students into young people seeking revenge.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "reducing the services provided to Palestinian refugees by the United Nations Relief and Works Agency for Palestine Refugees in the Near East (UNRWA)"
      },
      "relation": "caused",
      "effect": {
        "span": "have added to the social and fiscal strains weighing on them and on us"
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
        "span": "brought with it less visible costs"
      }
    }
  ]
}
```

### --- id=2706 ---

输入文本: In order to fulfil those promises, Lithuania will make use of the experience gained by its membership within various United Nations bodies.

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
      "cause": "make use",
      "effect": "fulfil"
    }
  ],
  "pred_triples": []
}
```

### --- id=5803 ---

输入文本: Trinidad and Tobago remains dedicated to ensuring our children and youth, including those in vulnerable situations, have the necessary opportunities, tools and a safe environment in order to reach their highest potential.

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
      "cause": "have the necessary opportunities, tools and a safe environment",
      "effect": "reach their highest potential"
    }
  ],
  "pred_triples": []
}
```

### --- id=11719 ---

输入文本: I am confident that with your leadership you will help us overcome the vast challenges we are facing.

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
      "cause": "your leadership",
      "effect": "help us overcome the vast challenges we are facing"
    }
  ],
  "pred_triples": []
}
```

### --- id=13521 ---

输入文本: By building resilient and inclusive societies, we can withstand terrorist ideologies and those who espouse them.

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
      "cause": "building resilient and inclusive societies",
      "effect": "can withstand terrorist ideologies and those who espouse them"
    }
  ],
  "pred_triples": []
}
```

### --- id=12717 ---

输入文本: Knowing this, we invested in genomic sequencing capability right at the start of this pandemic genomic sequencing is how you identify new variants giving the UK one of the biggest genomic sequencing capabilities in the world.

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
      "cause": "we invested in genomic sequencing capability right at the start of this pandemic",
      "effect": "giving the UK one of the biggest genomic sequencing capabilities in the world"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "invested in genomic sequencing capability right at the start of this pandemic"
      },
      "relation": "caused",
      "effect": {
        "span": "giving the UK one of the biggest genomic sequencing capabilities in the world"
      }
    }
  ]
}
```

### --- id=11130 ---

输入文本: In that context, UNESCO should play a more prominent role in improving our education systems, because only by offering our people, and our young people in particular, opportunities to forge a future can we contribute to tackling such scourges as illegal immigration, drugs, organized crime, youth radicalization, terrorism, obscurantism, unemployment, marginalization on the basis of social inequality and, particularly, gender inequality.

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
      "cause": "by offering our people, and our young people in particular, opportunities to forge a future",
      "effect": "contribute to tackling such scourges as illegal immigration, drugs, organized crime, youth radicalization, terrorism, obscurantism, unemployment, marginalization"
    }
  ],
  "pred_triples": []
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
      "cause": "must strengthen our counter-terrorism efforts through collective measures",
      "effect": "in order to put an end to the terrorist scourge that is indiscriminately causing great damage to property and resulting in a massive loss of innocent lives"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the terrorist scourge"
      },
      "relation": "caused",
      "effect": {
        "span": "is indiscriminately causing great damage to property and resulting in a massive loss of innocent lives"
      }
    }
  ]
}
```

### --- id=3027 ---

输入文本: Increasingly frequent regional and local, but also international conflicts, with historical, political and economic causes and consequences, threaten to destabilize the international order and the world as we know it.

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
      "cause": "regional and local, but also international conflicts,",
      "effect": "threaten to destabilize the international order and the world as we know it"
    }
  ],
  "pred_triples": []
}
```

### --- id=13126 ---

输入文本: In ASEAN, we continue to promote regionalism and multilateralism that emphasize the importance of inclusivity and mutual benefits and respect, forming a solid foundation for all of the essential cooperation frameworks within ASEAN.

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
      "cause": "continue to promote regionalism and multilateralism that emphasize the importance of inclusivity and mutual benefits and respect",
      "effect": "forming a solid foundation for all of the essential cooperation frameworks within ASEAN"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "promote regionalism and multilateralism that emphasize the importance of inclusivity and mutual benefits and respect"
      },
      "relation": "caused",
      "effect": {
        "span": "forming a solid foundation for all of the essential cooperation frameworks within ASEAN"
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

### --- id=218 ---

输入文本: We continue to work with the hospitality sector to ensure it is ready to meet any increased demand – with hundreds of rooms on standby which can be made available to book as needed.

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
      "cause": "continue to work with the hospitality sector",
      "effect": "to ensure it is ready to meet any increased demand"
    }
  ],
  "pred_triples": []
}
```
