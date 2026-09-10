# politicause_validation first 300 eval report

## 配置
```json
{
  "label": "politicause_validation first 300",
  "model": "google/gemma-4-31b-qat",
  "dataset": "politicause_validation",
  "sample_count": 300,
  "prompt_name": "v8.6",
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
  Gold 含因果: 85 | Pred 含因果: 129
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.807
  Precision: 0.605
  Recall   : 0.918
  F1       : 0.729
  (TP=78, TN=164, FP=51, FN=7)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 300
    Gold triples: 85 | Pred triples: 129
    Precision: 0.248
    Recall   : 0.376
    F1       : 0.299
    (TP=32, FP=97, FN=53)
  [anchor_window] (primary)
    样本数: 300
    Gold triples: 85 | Pred triples: 129
    Precision: 0.395
    Recall   : 0.600
    F1       : 0.477
    (TP=51, FP=78, FN=34)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 78
    Gold triples: 78 | Pred triples: 78
    Precision: 0.410
    Recall   : 0.410
    F1       : 0.410
    (TP=32, FP=46, FN=46)
  [anchor_window] (primary)
    样本数: 78
    Gold triples: 78 | Pred triples: 78
    Precision: 0.654
    Recall   : 0.654
    F1       : 0.654
    (TP=51, FP=27, FN=27)
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

Sample details shown: all 85 wrong samples from 300 total samples.

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

### --- id=15348 ---

输入文本: At the same time, to help us recover from the economic devastation caused by this pandemic, the starting point is three words: Cancel the Debts.

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
      "cause": "this pandemic",
      "effect": "the economic devastation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Cancel the Debts"
      },
      "relation": "caused",
      "effect": {
        "span": "help us recover from the economic devastation caused by this pandemic"
      }
    }
  ]
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
        "span": "the category 5 Hurricane Maria"
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
        "span": "efforts for harmonious development would be in vain"
      }
    }
  ]
}
```

### --- id=1486 ---

输入文本: A challenge which has been made easier as a result of this grant.

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
      "cause": "this grant",
      "effect": "has been made easier"
    }
  ],
  "pred_triples": []
}
```

### --- id=7592 ---

输入文本: Last week, clinical guidance was updated to enable COVID-19 boosters to be given slightly earlier to those at highest risk, where this makes operational sense to do so.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "clinical guidance was updated"
      },
      "relation": "caused",
      "effect": {
        "span": "enable COVID-19 boosters to be given slightly earlier to those at highest risk"
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
        "span": "the Tracks for Regional Peace initiative"
      },
      "relation": "caused",
      "effect": {
        "span": "will connect the Arab Gulf States by rail through Jordan to the Israeli ports in Haifa"
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
        "span": "so that it is transparent and credible"
      }
    }
  ]
}
```

### --- id=6964 ---

输入文本: It is necessary to struggle so that solidarity, cooperation and mutual respect prevail if we are to provide an effective response to the needs and aspirations of all peoples and preserve what is most valuable: human life and dignity.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "struggle"
      },
      "relation": "caused",
      "effect": {
        "span": "solidarity, cooperation and mutual respect prevail"
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
        "span": "the mobile and instantaneous nature of communications"
      },
      "relation": "caused",
      "effect": {
        "span": "brought us closer to the misfortunes of all in a much more direct way"
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

### --- id=13195 ---

输入文本: That leads us to our current dedicated efforts, which we are undertaking together with other ASEAN members, to push for partnership and turn conflicts into cooperation so that development and progress can be sustainable.

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
      "cause": "current dedicated efforts, which we are undertaking together with other ASEAN members",
      "effect": "development and progress can be sustainable"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "push for partnership and turn conflicts into cooperation"
      },
      "relation": "caused",
      "effect": {
        "span": "development and progress can be sustainable"
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
        "span": "our tourism sector, which was badly affected"
      }
    }
  ]
}
```

### --- id=6032 ---

输入文本: I think that it is a very wise choice, as today we hear more news that makes despair and lose hope nowadays.

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
      "cause": "hear more news",
      "effect": "makes despair and lose hope nowadays"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "news"
      },
      "relation": "caused",
      "effect": {
        "span": "makes despair and lose hope nowadays"
      }
    }
  ]
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
        "span": "gave Afghans tremendous belief that peace is possible"
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

### --- id=9960 ---

输入文本: We firmly condemn the unjustified political and diplomatic aggression against Burundi and its people by foreign Governments, some of which were known to have attempted regime change in 2015 through unconstitutional means.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "unconstitutional means"
      },
      "relation": "caused",
      "effect": {
        "span": "attempted regime change in 2015"
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

### --- id=7291 ---

输入文本: For Nauru, and our small population of 12,000, with limited health infrastructure, our best defence against the virus is our closed borders and a capture and contain policy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "our closed borders and a capture and contain policy"
      },
      "relation": "caused",
      "effect": {
        "span": "our best defence against the virus"
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
        "span": "new conflicts"
      },
      "relation": "caused",
      "effect": {
        "span": "forget older ones"
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
        "span": "ensure that everyone eligible is offered that booster in just over two months"
      }
    }
  ]
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

### --- id=10899 ---

输入文本: Those actions constitute a serious threat to regional peace and security and a direct attack on the Venezuelan people, in an attempt to break them in the cruellest of ways.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Those actions"
      },
      "relation": "caused",
      "effect": {
        "span": "break them in the cruellest of ways"
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
        "span": "enable us to take the necessary steps to achieve more ambitious targets, such as carbon neutrality by the year 2050"
      }
    }
  ]
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

### --- id=13276 ---

输入文本: We must reflect those messages in our policies if we are to respond bravely and with determination.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "reflect those messages in our policies"
      },
      "relation": "caused",
      "effect": {
        "span": "respond bravely and with determination"
      }
    }
  ]
}
```

### --- id=14050 ---

输入文本: I am very confident that such an effort, with the support of the Russian Federation and the West, could radically change the profile of my country, about which I spoke with such great concern at the beginning of my address.

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
      "cause": "effort, with the support of the Russian Federation",
      "effect": "could radically change"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "such an effort, with the support of the Russian Federation and the West"
      },
      "relation": "caused",
      "effect": {
        "span": "radically change the profile of my country"
      }
    }
  ]
}
```

### --- id=6094 ---

输入文本: We must therefore maintain our regional and international solidarity in a relentless effort to combat it and ensure our regional security.

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
      "cause": "maintain our regional and international solidarity in",
      "effect": "to combat it and ensure our regional security."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "maintain our regional and international solidarity"
      },
      "relation": "caused",
      "effect": {
        "span": "combat it and ensure our regional security"
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
        "span": "lead to tangible progress in achieving the SDGs"
      }
    }
  ]
}
```

### --- id=3687 ---

输入文本: Yet, they try in vain to deprive Iran of its minimum defense requirements, and disregard international law and global consensus in order to extend arms restrictions against Iran in contravention of the letter of UNSCR 2231.

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
      "cause": "try in vain to deprive Iran of its minimum defense requirements, and disregard international law and global consensus",
      "effect": "in order to extend arms restrictions against Iran in contravention of the letter of UNSCR 2231"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "disregard international law and global consensus"
      },
      "relation": "caused",
      "effect": {
        "span": "extend arms restrictions against Iran in contravention of the letter of UNSCR 2231"
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

### --- id=12744 ---

输入文本: After all, we are living in an era in which humankind can irreversibly destroy the living conditions on our planet.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "humankind"
      },
      "relation": "caused",
      "effect": {
        "span": "irreversibly destroy the living conditions on our planet"
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

### --- id=15266 ---

输入文本: Those visits will strengthen friendship and deepen relations with Japan, China, Saudi Arabia, the United Arab Emirates and Qatar.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Those visits"
      },
      "relation": "caused",
      "effect": {
        "span": "strengthen friendship and deepen relations with Japan, China, Saudi Arabia, the United Arab Emirates and Qatar"
      }
    }
  ]
}
```

### --- id=16619 ---

输入文本: In the fight against a blind and often invisible enemy developing unexpected resilience, the huge sacrifices made have not enabled us to overcome that evil.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the huge sacrifices made"
      },
      "relation": "caused",
      "effect": {
        "span": "not enabled us to overcome that evil"
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

### --- id=3014 ---

输入文本: In order to respond to climate change with success, promoting inclusiveness in international cooperation is indispensable.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "promoting inclusiveness in international cooperation"
      },
      "relation": "caused",
      "effect": {
        "span": "respond to climate change with success"
      }
    }
  ]
}
```

### --- id=3569 ---

输入文本: Mr. President, Myself as co-convener of the High Level Event on Financing for Development in the Era of COVID-19 and Beyond, along with Secretary-General Guterres and Prime Minister Trudeau, remain committed to facilitate the process of developing concrete global solutions and actions to enable countries to respond and recover better from what the Secretary-General refers to as the world’s first development emergency.

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
      "cause": "the process of developing concrete global solutions and actions",
      "effect": "enable countries to respond and recover better from what the Secretary-General refers to as the world’s first development emergency."
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "developing concrete global solutions and actions"
      },
      "relation": "caused",
      "effect": {
        "span": "enable countries to respond and recover better from what the Secretary-General refers to as the world’s first development emergency"
      }
    }
  ]
}
```

### --- id=3421 ---

输入文本: By devising a long-term low greenhouse gas emission development strategy, we will work with the international community in realizing a low-carbon society by 2050.

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
      "cause": "devising a long-term low greenhouse gas emission development strategy",
      "effect": "will work with the international community in realizing a low-carbon society by 2050"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "devising a long-term low greenhouse gas emission development strategy"
      },
      "relation": "caused",
      "effect": {
        "span": "realizing a low-carbon society by 2050"
      }
    }
  ]
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
        "span": "911"
      },
      "relation": "caused",
      "effect": {
        "span": "Islamophobia has grown at an alarming pace"
      }
    }
  ]
}
```

### --- id=4674 ---

输入文本: Because I’ve always been extremely conscious of the impact that blanket restrictions can have, for instance on jobs, on education and mental health.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "blanket restrictions"
      },
      "relation": "caused",
      "effect": {
        "span": "impact that blanket restrictions can have, for instance on jobs, on education and mental health"
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
      "cause": "the sooner you are vaccinated",
      "effect": "the sooner you and your family and friends will be protected"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "you are vaccinated"
      },
      "relation": "caused",
      "effect": {
        "span": "you and your family and friends will be protected"
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

### --- id=5483 ---

输入文本: In a new short film, Sarah Hunter, Harriet Millar-Mills and Amber Reed are encouraging people to continue to do what they love by getting the protection provided by the booster.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "getting the protection provided by the booster"
      },
      "relation": "caused",
      "effect": {
        "span": "continue to do what they love"
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

### --- id=3134 ---

输入文本: This placed us in a position to implement an initial social and economic stimulus programme, in addition to our early response to control the spread of the coronavirus and to treat those infected.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
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
        "span": "placed us in a position to implement an initial social and economic stimulus programme"
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

### --- id=16991 ---

输入文本: The most secure foundation on which those changes can occur is political stability, good governance and trust rooted in the rule of law and the integrity of our institutions.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "political stability, good governance and trust rooted in the rule of law and the integrity of our institutions"
      },
      "relation": "caused",
      "effect": {
        "span": "those changes can occur"
      }
    }
  ]
}
```

### --- id=12379 ---

输入文本: We look forward to the implementation of the outcomes of the UN Food Systems Summit to complement and scale up our existing food security systems and programs to adapt better to climate change and support progress on the SDGs.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "the implementation of the outcomes of the UN Food Systems Summit"
      },
      "relation": "caused",
      "effect": {
        "span": "complement and scale up our existing food security systems and programs to adapt better to climate change and support progress on the SDGs"
      }
    }
  ]
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
        "span": "added to the social and fiscal strains weighing on them and on us"
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
        "span": "address most of the concerns and aspirations of the vast majority of the world’s inhabitants"
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
        "span": "benefit our generation, our children and their children"
      }
    }
  ]
}
```

### --- id=13521 ---

输入文本: By building resilient and inclusive societies, we can withstand terrorist ideologies and those who espouse them.

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
      "cause": "building resilient and inclusive societies",
      "effect": "can withstand terrorist ideologies and those who espouse them"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "building resilient and inclusive societies"
      },
      "relation": "caused",
      "effect": {
        "span": "withstand terrorist ideologies and those who espouse them"
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
        "span": "the strengthening of active solidarity and the will to live together in the strict observance of world cultural diversity"
      },
      "relation": "caused",
      "effect": {
        "span": "promoting and preserving the interests of everyone, especially the weak"
      }
    }
  ]
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
      "cause": "we invested in genomic sequencing capability right at the start of this pandemic",
      "effect": "giving the UK one of the biggest genomic sequencing capabilities in the world"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "genomic sequencing"
      },
      "relation": "caused",
      "effect": {
        "span": "how you identify new variants"
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
      "cause": "by offering our people, and our young people in particular, opportunities to forge a future",
      "effect": "contribute to tackling such scourges as illegal immigration, drugs, organized crime, youth radicalization, terrorism, obscurantism, unemployment, marginalization"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "offering our people, and our young people in particular, opportunities to forge a future"
      },
      "relation": "caused",
      "effect": {
        "span": "contribute to tackling such scourges as illegal immigration, drugs, organized crime, youth radicalization, terrorism, obscurantism, unemployment, marginalization on the basis of social inequality and, particularly, gender inequality"
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
        "span": "strengthen our counter-terrorism efforts through collective measures"
      },
      "relation": "caused",
      "effect": {
        "span": "put an end to the terrorist scourge"
      }
    }
  ]
}
```

### --- id=14809 ---

输入文本: There is no doubt that the challenge of global inequality can be addressed only by working together.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "working together"
      },
      "relation": "caused",
      "effect": {
        "span": "the challenge of global inequality can be addressed"
      }
    }
  ]
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
      "cause": "continue to work with the hospitality sector",
      "effect": "to ensure it is ready to meet any increased demand"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "work with the hospitality sector"
      },
      "relation": "caused",
      "effect": {
        "span": "ensure it is ready to meet any increased demand"
      }
    }
  ]
}
```
