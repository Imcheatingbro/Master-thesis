# cnc first 20 eval report

## 配置
```json
{
  "label": "cnc first 20",
  "model": "qwen/qwen3-14b",
  "dataset": "cnc",
  "sample_count": 20,
  "prompt_name": "v4",
  "use_rag": true,
  "rag_mode": "knn_pattern",
  "rag_top_k": 2,
  "temperature": 0.0,
  "max_tokens": 2048,
  "progress_every": 50,
  "metadata_path": "D:\\Master thesis\\RAG Database\\bge-small-en-v1.5_examples.jsonl",
  "embeddings_path": "D:\\Master thesis\\RAG Database\\bge-small-en-v1.5_embeddings.npy"
}
```

## 统计指标
```text
================ cnc first 20 final report ================
样本总数: 20
  Gold 含因果: 10 | Pred 含因果: 6
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.700
  Precision: 0.833
  Recall   : 0.500
  F1       : 0.625
  (TP=5, TN=9, FP=1, FN=5)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 20
    Gold triples: 15 | Pred triples: 10
    Precision: 0.500
    Recall   : 0.333
    F1       : 0.400
    (TP=5, FP=5, FN=10)
  [anchor_window]
    样本数: 20
    Gold triples: 15 | Pred triples: 10
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=10, FN=15)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 5
    Gold triples: 8 | Pred triples: 7
    Precision: 0.714
    Recall   : 0.625
    F1       : 0.667
    (TP=5, FP=2, FN=3)
  [anchor_window]
    样本数: 5
    Gold triples: 8 | Pred triples: 7
    Precision: 0.000
    Recall   : 0.000
    F1       : 0.000
    (TP=0, FP=7, FN=8)
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

## 样本明细

### --- id=1 ---

输入文本: The State alleged they hacked Sabata Petros Chale , 39 , to death in Marikana West , on December 8 , 2016 , allegedly over the allocation of low cost ( RDP ) houses at Marikana West Extension 2 .

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
      "cause": "the allocation of low cost ( RDP ) houses at Marikana West Extension 2",
      "effect": "they hacked Sabata Petros Chale , 39 , to death in Marikana West , on December 8 , 2016"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the allocation of low cost ( RDP ) houses at Marikana West Extension 2"
      },
      "relation": "caused",
      "effect": {
        "span": "hacked Sabata Petros Chale , 39 , to death in Marikana West , on December 8 , 2016"
      }
    }
  ]
}
```

### --- id=2 ---

输入文本: Chale was allegedly chased by a group of about 30 people and was hacked to death with pangas , axes and spears .

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
        "span": "chased by a group of about 30 people"
      },
      "relation": "caused",
      "effect": {
        "span": "hacked to death with pangas , axes and spears"
      }
    },
    {
      "cause": {
        "span": "hacked to death with pangas , axes and spears"
      },
      "relation": "caused",
      "effect": {
        "span": "death"
      }
    },
    {
      "cause": {
        "span": "chased by a group of about 30 people"
      },
      "relation": "caused",
      "effect": {
        "span": "death"
      }
    }
  ]
}
```

### --- id=3 ---

输入文本: The farmworkers ' strike resumed on Tuesday when their demands were not met .

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
      "cause": "their demands were not met",
      "effect": "The farmworkers ' strike resumed on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "their demands were not met"
      },
      "relation": "caused",
      "effect": {
        "span": "The farmworkers ' strike resumed"
      }
    }
  ]
}
```

### --- id=4 ---

输入文本: Demonstrators have filed for a permit to hold a rally on Saturday in Yuen Long , the district on the outskirts of Hong Kong where dozens of masked men chased and beat commuters and protesters with wooden poles and metal rods , leaving at least 45 people in hospital .

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
      "cause": "to hold a rally on Saturday in Yuen Long",
      "effect": "Demonstrators have filed for a permit"
    },
    {
      "cause": "dozens of masked men chased and beat commuters and protesters with wooden poles and metal rods",
      "effect": "leaving at least 45 people in hospital"
    }
  ],
  "pred_triples": []
}
```

### --- id=5 ---

输入文本: Footage of the attack , which included a pregnant woman being hit , protesters being punched and kneed , and commuters screaming and crying while trying to shield themselves , emerged on Sunday night , fuelling further political unrest as demonstrators , opposition lawmakers and others demanded answers from authorities for failing to stop the violence .

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
      "cause": "Footage of the attack , which included a pregnant woman being hit , protesters being punched and kneed , and commuters screaming and crying while trying to shield themselves , emerged on Sunday night",
      "effect": "fuelling further political unrest"
    },
    {
      "cause": "failing to stop the violence",
      "effect": "demonstrators , opposition lawmakers and others demanded answers from authorities"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Footage of the attack , which included a pregnant woman being hit , protesters being punched and kneed , and commuters screaming and crying while trying to shield themselves"
      },
      "relation": "caused",
      "effect": {
        "span": "further political unrest"
      }
    }
  ]
}
```

### --- id=6 ---

输入文本: Max Chung , who delivered the application for a letter of no objection from the police , that is required to hold a rally , said : “ We want to show to the public and international community that Hong Kongers , we will never surrender in front of terrorism … To show our solidarity and say no to terrorism , we have to stand up. ” Chung said : “ Yuen Long was under terrorist attack and we have no choice but to take it back. ” The protests , principally over a controversial bill that would allow suspects to be extradited from Hong Kong to mainland China , have taken on new demands , including an investigation into police use of rubber bullets , teargas and physical violence against protesters .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": []
}
```

### --- id=7 ---

输入文本: Protesters are angry at the police ’ s slow response to the attack in Yuen Long and their pursuit of the case .

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
      "cause": "the police ’ s slow response to the attack in Yuen Long and their pursuit of the case",
      "effect": "Protesters are angry"
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
      "cause": "The violence in Yuen Long",
      "effect": "heightened tensions and fears of further attacks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "violence in Yuen Long"
      },
      "relation": "caused",
      "effect": {
        "span": "heightened tensions"
      }
    }
  ]
}
```

### --- id=9 ---

输入文本: On Tuesday evening , unverified footage showed men in white gathering in Tuen Mun , another city near Yuen Long in the New Territories .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": []
}
```

### --- id=10 ---

输入文本: Hong Kong ’ s leader , Carrie Lam , said the “ shocking violence ” in Yuen Long would be investigated , but devoted most of her comments to criticising protesters , who surrounded Beijing ’ s liaison office in Hong Kong and defaced the national emblem of the People ’ s Republic of China on Sunday .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": []
}
```

### --- id=11 ---

输入文本: On Tuesday , a group of aviation staff called for a protest at Hong Kong airport on Friday to condemn the government and police for “ ignoring the random attacks on citizens in Yuen Long ” .

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
      "cause": "to condemn the government and police",
      "effect": "a group of aviation staff called for a protest at Hong Kong airport on Friday"
    },
    {
      "cause": "“ ignoring the random attacks on citizens in Yuen Long ”",
      "effect": "to condemn the government and police"
    }
  ],
  "pred_triples": []
}
```

### --- id=12 ---

输入文本: In Yuen Long , Chung and other protesters are demanding the government conducts an independent investigation and officially characterises the violence as a “ cross-border terrorist attack ” .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": []
}
```

### --- id=13 ---

输入文本: Hailey Leung , a university student who has been attending the protests this summer , said : “ The fear of the gangs is definitely stronger than the fear of the use of violence of the police. ” Her parents have been supportive of the protests but , since the violence in Yuen Long , they have asked her not to attend .

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
      "cause": "the violence in Yuen Long",
      "effect": "they have asked her not to attend"
    }
  ],
  "pred_triples": []
}
```

### --- id=14 ---

输入文本: NHAI Case : Cops Fail to Produce Accused in Court

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": []
}
```

### --- id=15 ---

输入文本: 10th September 2015 03:49 AM KOCHI : Anoop George , the main accused in the case related to attack on the office of the National Highway Authority of India ( NHAI ) at Kalamassery , could not be produced before the Ernakulam District and Principal Sessions Court on Wednesday , after jail authorities in Coimbatore failed to arrange escort for him .

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
      "cause": "jail authorities in Coimbatore failed to arrange escort for him",
      "effect": "Anoop George , the main accused in the case related to attack on the office of the National Highway Authority of India ( NHAI ) at Kalamassery , could not be produced before the Ernakulam District and Principal Sessions Court on Wednesday"
    }
  ],
  "pred_triples": []
}
```

### --- id=16 ---

输入文本: Suddenly , a motley group of slogan-shouting students emerged from the dhaba .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": []
}
```

### --- id=17 ---

输入文本: They exhorted us to join the protest against the recommendations of the Mandal Commission , which had been implemented a day earlier .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": []
}
```

### --- id=18 ---

输入文本: Thus we too joined the sloganeering .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": []
}
```

### --- id=19 ---

输入文本: By the time the self-styled leaders had commandeered a few DTC buses , nearly 200 postgraduate and doctoral students had gathered at an intersection , which later became the epicentre of protests and was rechristened euphemistically as Kranti Chowk .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": []
}
```

### --- id=20 ---

输入文本: Some hotheads tried to gatecrash , provoking the policemen into action  they charged ferociously , dispersing the crowd within minutes .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 3,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 3,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "Some hotheads tried to gatecrash",
      "effect": "provoking the policemen into action"
    },
    {
      "cause": "provoking the policemen into action",
      "effect": "they charged ferociously"
    },
    {
      "cause": "they charged ferociously",
      "effect": "dispersing the crowd within minutes"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "hotheads tried to gatecrash"
      },
      "relation": "caused",
      "effect": {
        "span": "policemen into action"
      }
    },
    {
      "cause": {
        "span": "policemen into action"
      },
      "relation": "caused",
      "effect": {
        "span": "charged ferociously"
      }
    },
    {
      "cause": {
        "span": "charged ferociously"
      },
      "relation": "caused",
      "effect": {
        "span": "dispersing the crowd within minutes"
      }
    }
  ]
}
```
