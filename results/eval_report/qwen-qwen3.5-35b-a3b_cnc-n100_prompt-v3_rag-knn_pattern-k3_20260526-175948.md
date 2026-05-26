# cnc first 100 eval report

## 配置
```json
{
  "label": "cnc first 100",
  "model": "qwen/qwen3.5-35b-a3b",
  "dataset": "cnc",
  "sample_count": 100,
  "prompt_name": "v3",
  "use_rag": true,
  "rag_mode": "knn_pattern",
  "rag_top_k": 3,
  "temperature": 0.0,
  "max_tokens": 2048,
  "progress_every": 50,
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ cnc first 100 final report ================
样本总数: 100
  Gold 含因果: 51 | Pred 含因果: 31
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.720
  Precision: 0.871
  Recall   : 0.529
  F1       : 0.659
  (TP=27, TN=45, FP=4, FN=24)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 100
    Gold triples: 74 | Pred triples: 35
    Precision: 0.486
    Recall   : 0.230
    F1       : 0.312
    (TP=17, FP=18, FN=57)
  [anchor_window]
    样本数: 100
    Gold triples: 74 | Pred triples: 35
    Precision: 0.400
    Recall   : 0.189
    F1       : 0.257
    (TP=14, FP=21, FN=60)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 27
    Gold triples: 45 | Pred triples: 31
    Precision: 0.548
    Recall   : 0.378
    F1       : 0.447
    (TP=17, FP=14, FN=28)
  [anchor_window]
    样本数: 27
    Gold triples: 45 | Pred triples: 31
    Precision: 0.452
    Recall   : 0.311
    F1       : 0.368
    (TP=14, FP=17, FN=31)
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
    "tp": 1,
    "fp": 0,
    "fn": 0
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
        "span": "over the allocation of low cost ( RDP ) houses at Marikana West Extension 2"
      },
      "relation": "caused",
      "effect": {
        "span": "they hacked Sabata Petros Chale , 39 , to death in Marikana West , on December 8 , 2016"
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

### --- id=3 ---

输入文本: The farmworkers ' strike resumed on Tuesday when their demands were not met .

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
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
        "span": "The farmworkers ' strike resumed on Tuesday"
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
      "cause": "to hold a rally on Saturday in Yuen Long",
      "effect": "Demonstrators have filed for a permit"
    },
    {
      "cause": "dozens of masked men chased and beat commuters and protesters with wooden poles and metal rods",
      "effect": "leaving at least 45 people in hospital"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "dozens of masked men chased and beat commuters and protesters with wooden poles and metal rods"
      },
      "relation": "caused",
      "effect": {
        "span": "leaving at least 45 people in hospital"
      }
    }
  ]
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
        "span": "Yuen Long was under terrorist attack"
      },
      "relation": "caused",
      "effect": {
        "span": "we have no choice but to take it back"
      }
    }
  ]
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
      "cause": "The violence in Yuen Long",
      "effect": "heightened tensions and fears of further attacks"
    }
  ],
  "pred_triples": []
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
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "the violence in Yuen Long",
      "effect": "they have asked her not to attend"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the violence in Yuen Long"
      },
      "relation": "caused",
      "effect": {
        "span": "they have asked her not to attend"
      }
    }
  ]
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
      "cause": "jail authorities in Coimbatore failed to arrange escort for him",
      "effect": "Anoop George , the main accused in the case related to attack on the office of the National Highway Authority of India ( NHAI ) at Kalamassery , could not be produced before the Ernakulam District and Principal Sessions Court on Wednesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "jail authorities in Coimbatore failed to arrange escort for him"
      },
      "relation": "caused",
      "effect": {
        "span": "Anoop George ... could not be produced before the Ernakulam District and Principal Sessions Court on Wednesday"
      }
    }
  ]
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
        "span": "Some hotheads tried to gatecrash"
      },
      "relation": "caused",
      "effect": {
        "span": "provoking the policemen into action"
      }
    },
    {
      "cause": {
        "span": "they charged ferociously"
      },
      "relation": "caused",
      "effect": {
        "span": "dispersing the crowd within minutes"
      }
    }
  ]
}
```

### --- id=21 ---

输入文本: That night , Doordarshan telecast news of protests .

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

### --- id=22 ---

输入文本: Jammu : Delhi court blast accused killed in Kishtwar August 07 , 2012 00:00 IST A 2011 Delhi High Court blast accused , Amir Ali Kamal , was among two Hizb—ul—Mujahideen ( HM ) militants killed on Monday in a shootout with security forces in the mountainous Kishtwar district of Jammu and Kashmir , police said .

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
      "cause": "a shootout with security forces in the mountainous Kishtwar district of Jammu and Kashmir",
      "effect": "A 2011 Delhi High Court blast accused , Amir Ali Kamal , was among two Hizb—ul—Mujahideen ( HM ) militants killed on Monday"
    }
  ],
  "pred_triples": []
}
```

### --- id=23 ---

输入文本: As we closed in on the hideout of the militants , a fire fight began that continued for over an hour , ” he said .

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

### --- id=24 ---

输入文本: According to reports , two militants have been shot dead in the encounter .

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

### --- id=25 ---

输入文本: “ One of them is Amir Ali Kamal , code name Akram , who was prime accused in the Delhi High Court blast , ” the officer said .

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

### --- id=26 ---

输入文本: It was in January this year a group of persons attacked the NHAI office at Kalamassery and distributed notices supporting armed revolt against the government .

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

### --- id=27 ---

输入文本: Akram was on the radar of the National Investigation Agency ( NIA ) as he is believed to have arranged explosives and planter for the blast .

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
      "cause": "he is believed to have arranged explosives and planter for the blast",
      "effect": "Akram was on the radar of the National Investigation Agency ( NIA )"
    },
    {
      "cause": "the blast",
      "effect": "arranged explosives and planter"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "arranged explosives and planter"
      },
      "relation": "caused",
      "effect": {
        "span": "blast"
      }
    }
  ]
}
```

### --- id=28 ---

输入文本: He is an accused in the Delhi High Court blast of Sep 7 , 2011 in which at least 10 people were killed and over 70 injured .

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
      "cause": "the Delhi High Court blast of Sep 7 , 2011",
      "effect": "at least 10 people were killed and over 70 injured"
    }
  ],
  "pred_triples": []
}
```

### --- id=29 ---

输入文本: The NIA wanted to catch Akram alive as he could provide clues in resolving the blast case .

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
      "cause": "he could provide clues in resolving the blast case",
      "effect": "The NIA wanted to catch Akram alive"
    }
  ],
  "pred_triples": []
}
```

### --- id=30 ---

输入文本: The Kishtwar area has been in focus ever since the Delhi High Court blast as the first of the e—mails claiming responsibility for the blast emanated from here .

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
        "span": "the first of the e-mails claiming responsibility for the blast emanated from here"
      },
      "relation": "caused",
      "effect": {
        "span": "The Kishtwar area has been in focus"
      }
    }
  ]
}
```

### --- id=31 ---

输入文本: Two more youths were arrested later for allegedly being involved in the blast .

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
      "cause": "allegedly being involved in the blast",
      "effect": "Two more youths were arrested later"
    }
  ],
  "pred_triples": []
}
```

### --- id=32 ---

输入文本: Modi visited the homes of all the six victims of the serial blasts which rocked Patna ’ s Gandhi Maidan and other parts of the city during his visit to address the Hunkar Rally on October 27 .

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

### --- id=33 ---

输入文本: ﻿NaMo , who had avoided visiting the victims of the 2002 riots in his own state for a long time , lost no time in burning up aviation fuel by dashing to Patna twice in one week to express condolences and score points over his rambunctious rivals .

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
      "cause": "dashing to Patna twice in one week to express condolences and score points over his rambunctious rivals",
      "effect": "﻿NaMo , who had avoided visiting the victims of the 2002 riots in his own state for a long time , lost no time in burning up aviation fuel"
    },
    {
      "cause": "to express condolences and score points over his rambunctious rivals",
      "effect": "dashing to Patna twice in one week"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to express condolences and score points over his rambunctious rivals"
      },
      "relation": "caused",
      "effect": {
        "span": "burning up aviation fuel by dashing to Patna twice in one week"
      }
    }
  ]
}
```

### --- id=34 ---

输入文本: Now , he is charged with exploiting the grief of the terror victims of 26/10 .

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

### --- id=35 ---

输入文本: By visiting the families of the Patna blast victims , NaMo is drilling home the point that NiKu is least bothered about the personal tragedies of his people .

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
        "span": "NiKu is least bothered about the personal tragedies of his people"
      },
      "relation": "caused",
      "effect": {
        "span": "NaMo is drilling home the point"
      }
    }
  ]
}
```

### --- id=36 ---

输入文本: In August that year , militantly aggressive Kurmis mowed down 14 Dalits in the sleepy hamlet of Belchchi in Nalanda district .

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

### --- id=37 ---

输入文本: Both Anoop and Ramanan are also accused in the case related to attack on the Nitta Gelatin office at Panampilly Nagar last year .

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

### --- id=38 ---

输入文本: Indira landed in Nalanda and waded into the floodwaters on an elephant to visit each Dalit family , which had lost members in the caste pogrom .

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
      "cause": "to visit each Dalit family , which had lost members in the caste pogrom",
      "effect": "Indira landed in Nalanda and waded into the floodwaters on an elephant"
    }
  ],
  "pred_triples": []
}
```

### --- id=39 ---

输入文本: The grief list also includes the nights spent by Rahul in Dalit colonies and the visits of Manmohan Singh and Sonia Gandhi to Chhattisgarh after top Congress leaders were massacred by Naxalites .

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

### --- id=40 ---

输入文本: Modiites are now reminding the Congress about the trips which Sonia and the Prime Minister made to Muzzafarnagar after 43 were killed in the worst-ever communal clashes in decades .

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

### --- id=41 ---

输入文本: Bandhopadhay also said two Trinamool Congress workers were killed at Sashan in North 24 Parganas district recently .

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

### --- id=42 ---

输入文本: A car with Union ministers Mukul Roy and Sultan Ahmed was attacked allegedly by CPM cadres on Wednesday , he alleged .

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

### --- id=43 ---

输入文本: December 05 , 2017 00:00 IST Say officials at the panchayat level are colluding with locals Residents of Varavani panchayat staged a protest at the collectorate here on Monday , against illegal tapping of drinking water supplied through pipelines under the Cauvery combined water supply scheme and irregular supply of water to their villages .

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
      "cause": "against illegal tapping of drinking water supplied through pipelines under the Cauvery combined water supply scheme and irregular supply of water to their villages",
      "effect": "Residents of Varavani panchayat staged a protest at the collectorate here on Monday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "illegal tapping of drinking water supplied through pipelines under the Cauvery combined water supply scheme and irregular supply of water to their villages"
      },
      "relation": "caused",
      "effect": {
        "span": "Residents of Varavani panchayat staged a protest at the collectorate here on Monday"
      }
    }
  ]
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

### --- id=45 ---

输入文本: Led by A Sagayamadha , an office-bearer of the All India Farm Workers Association , the villagers , including a large number of women from the panchayat comprising six villages , staged the protest urging the district administration to immediately disconnect the illegal water connections and ensure uninterrupted water supply to them .

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
      "cause": "Led by A Sagayamadha , an office-bearer of the All India Farm Workers Association",
      "effect": "the villagers , including a large number of women from the panchayat comprising six villages , staged the protest urging the district administration to immediately disconnect the illegal water connections and ensure uninterrupted water supply to them"
    },
    {
      "cause": "urging the district administration to immediately disconnect the illegal water connections and ensure uninterrupted water supply to them",
      "effect": "the villagers , including a large number of women from the panchayat comprising six villages , staged the protest"
    }
  ],
  "pred_triples": []
}
```

### --- id=46 ---

输入文本: US Committed to Seeking Justice on Behalf of All 26/11 Victims 05th August 2015 12:04 PM NEW YORK : The US is committed to pursuing justice on behalf of the victims of the 2008 Mumbai attack no matter how " arduous " the task is , a top Indian-origin American diplomat has said .

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

### --- id=47 ---

输入文本: " We have certainly reiterated our support and our commitment to India 's efforts to seek justice on behalf of the victims " of the 26/11 attack , Assistant Secretary of State for South and Central Asian Affairs Nisha Desai Biswal told PTI when asked about the delay in bringing to justice the perpetrators of the 2008 terror attacks .

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

### --- id=48 ---

输入文本: Biswal , who had travelled to the city from Washington to speak at the Indian Consulate General 's Media-India Lecture Series yesterday , said not only were there a large number of Indian victims in the attack but there were Americans also who lost their lives .

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
      "cause": "to speak at the Indian Consulate General 's Media-India Lecture Series yesterday",
      "effect": "Biswal , who had travelled to the city from Washington"
    }
  ],
  "pred_triples": []
}
```

### --- id=49 ---

输入文本: VS condemns attack on NSS Karayogams 08th May 2011 05:00 AM THIRUVANANTHAPURAM : Chief Minister V S Achuthanandan has condemned the recent attacks on NSS Karayogams .

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

### --- id=50 ---

输入文本: Given that nearly seven years have passed since the horrendous terror attacks that claimed over 160 lives and injured many others , Biswal said bringing justice for the victims in terror attacks may appear to be an arduous andlong-drawn process .

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

### --- id=51 ---

输入文本: Biswal underlined that the US on its part had offered rewards for information leading to the arrest and prosecution of individuals associated with the Mumbai attack .

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

### --- id=52 ---

输入文本: Referring to the terror attack in Punjab 's Gurdaspur district on July 27 , Biswal said the US has strongly condemned and expressed its concern over the attack .

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

### --- id=53 ---

输入文本: She said the US has expressed its cooperation ith Indian authorities on on any specific aspects of the incident .

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

### --- id=54 ---

输入文本: On media reports that the night vision device used by three terrorists in the Gurdaspur attack had US markings , Biswal said the US is in conversation with Indian authorities to try to ascertain and trace the origins of the equipment found .

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
      "cause": "to try to ascertain and trace the origins of the equipment found",
      "effect": "the US is in conversation with Indian authorities"
    }
  ],
  "pred_triples": []
}
```

### --- id=55 ---

输入文本: " We will continue to work very closely with the Indian government on those issues , " she said , adding that it is an ongoing process and the US is working with Indian authorities to address issues of concern emanating from the incident .

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
      "cause": "to address issues of concern emanating from the incident",
      "effect": "the US is working with Indian authorities"
    }
  ],
  "pred_triples": []
}
```

### --- id=56 ---

输入文本: The step came after RLD workers , led by district party president Ajit Rathi , former UP minister Dharamvir Balyan and MLC Chaudhry Mushtaq , staged a dharna outside the DM 's office here yesterday and submitted a memorandum to him .

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

### --- id=57 ---

输入文本: CHENNAI : Chennai sees its first ever hunger fast against HCL April 08 , 2013 00:00 IST For the first time in Chennai , graduates denied jobs by a multi-national corporation who had recruited them from their college campuses , staged a hunger strike on Sunday .

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
        "span": "graduates denied jobs by a multi-national corporation who had recruited them from their college campuses"
      },
      "relation": "caused",
      "effect": {
        "span": "staged a hunger strike on Sunday"
      }
    }
  ]
}
```

### --- id=58 ---

输入文本: As many as 59 recruits who had graduated from different colleges of the State came together for the fourth time to demand answers from HCL Technologies , the company that had recruited them in 2011 .

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
      "cause": "to demand answers from HCL Technologies , the company that had recruited them in 2011",
      "effect": "As many as 59 recruits who had graduated from different colleges of the State came together for the fourth time"
    }
  ],
  "pred_triples": []
}
```

### --- id=59 ---

输入文本: The recruits , at Valluvar Kottam shouted slogans including , “ HCL lend us your ears , give us back our two years , ” while undertaking the day-long fast .

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

### --- id=60 ---

输入文本: When asked about the series of attacks on Karayogams , he said that such attacks could not be entertained .

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

### --- id=61 ---

输入文本: Three Arrested in Bimbola Clash 18th June 2014 09:39 AM DHENKANAL : Three persons were arrested on Tuesday for their alleged involvement in killing of a naib sarpanch in a clash between members of two communities at Bimbola village under Dhenkanal Sadar police limits on Monday .

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
      "cause": "their alleged involvement in killing of a naib sarpanch in a clash between members of two communities at Bimbola village under Dhenkanal Sadar police limits on Monday",
      "effect": "Three persons were arrested on Tuesday"
    },
    {
      "cause": "a clash between members of two communities at Bimbola village under Dhenkanal Sadar police limits on Monday",
      "effect": "killing of a naib sarpanch"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Three persons were arrested"
      },
      "relation": "caused",
      "effect": {
        "span": "for their alleged involvement in killing of a naib sarpanch in a clash between members of two communities at Bimbola village under Dhenkanal Sadar police limits on Monday"
      }
    }
  ]
}
```

### --- id=62 ---

输入文本: The naib sarpanch was killed and 17 others were seriously injured in the clash over use of a village field .

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
      "cause": "the clash",
      "effect": "The naib sarpanch was killed and 17 others were seriously injured"
    },
    {
      "cause": "use of a village field",
      "effect": "the clash"
    }
  ],
  "pred_triples": []
}
```

### --- id=63 ---

输入文本: Bimbola village turned into a battle field as rival groups wielding guns took the centre stage .

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
      "cause": "rival groups wielding guns took the centre stage",
      "effect": "Bimbola village turned into a battle field"
    }
  ],
  "pred_triples": []
}
```

### --- id=64 ---

输入文本: The clash took place over use of the field .

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
      "cause": "use of the field",
      "effect": "The clash took place"
    }
  ],
  "pred_triples": []
}
```

### --- id=65 ---

输入文本: Police said he was detained by group of 30 to 40 persons from the general caste on Monday morning but he managed to escape .

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

### --- id=66 ---

输入文本: However , when he was returning home in the night , Pradhan was intercepted again by them and killed .

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

### --- id=67 ---

输入文本: Soon a clash ensued between supporters of Pradhan and the rival group in which 17 persons were injured .

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

### --- id=68 ---

输入文本: Ishrat Jahan , a 19 - year-old college student was killed along with three others on June 15 , 2004 allegedly by a team of Crime Branch officials on the outskirts of Ahmedabad , after intelligence inputs that a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi to avenge the 2002 communal riots in the state .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "intelligence inputs that a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi to avenge the 2002 communal riots in the state",
      "effect": "Ishrat Jahan , a 19 - year-old college student was killed along with three others on June 15 , 2004 allegedly by a team of Crime Branch officials on the outskirts of Ahmedabad"
    },
    {
      "cause": "to avenge the 2002 communal riots in the state",
      "effect": "a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "intelligence inputs that a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi"
      },
      "relation": "caused",
      "effect": {
        "span": "Ishrat Jahan , a 19 - year-old college student was killed along with three others on June 15 , 2004 allegedly by a team of Crime Branch officials"
      }
    },
    {
      "cause": {
        "span": "the 2002 communal riots in the state"
      },
      "relation": "caused",
      "effect": {
        "span": "a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi to avenge"
      }
    }
  ]
}
```

### --- id=69 ---

输入文本: 13 Sep 2014 Three people were sentenced to death by a Yunnan court for their role in the attack at a Kunming rail station that killed 31 people and injured 141 in March .

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
      "cause": "their role in the attack at a Kunming rail station that killed 31 people and injured 141 in March .",
      "effect": "Three people were sentenced to death by a Yunnan court"
    },
    {
      "cause": "the attack at a Kunming rail station",
      "effect": "killed 31 people and injured 141 in March"
    }
  ],
  "pred_triples": []
}
```

### --- id=70 ---

输入文本: Kunming railway station attack Three given death penalty over Kunming rail station attack Influenced by religious extremism , trio plotted knife rampage , court says , while a fourth defendant handed life sentence for taking part

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
      "cause": "Kunming rail station attack",
      "effect": "Three given death penalty"
    },
    {
      "cause": "Influenced by religious extremism",
      "effect": "trio plotted knife rampage"
    },
    {
      "cause": "taking part",
      "effect": "a fourth defendant handed life sentence"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Influenced by religious extremism"
      },
      "relation": "caused",
      "effect": {
        "span": "trio plotted knife rampage"
      }
    }
  ]
}
```

### --- id=71 ---

输入文本: PUBLISHED : Friday , 12 September , 2014 , 12:28pm Xi Jinping urges China ’ s central Asian neighbours to help step up extremism fight

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

### --- id=72 ---

输入文本: Patigul Tohti , who was wounded and captured at the scene , was jailed for life after being convicted of taking part in the attack .

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
      "cause": "being convicted of taking part in the attack",
      "effect": "Patigul Tohti , who was wounded and captured at the scene , was jailed for life"
    }
  ],
  "pred_triples": []
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
        "span": "NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections , as it did not want Achuthanandan to come back to power for another term"
      },
      "relation": "caused",
      "effect": {
        "span": "The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram"
      }
    }
  ]
}
```

### --- id=74 ---

输入文本: Tohtunyaz helped them to acquire more than 10 knives used in the attack .

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

### --- id=75 ---

输入文本: Two days before the attack , local police arrested Tohtunyaz , Ehet and Muhammad as they tried to illegally cross into Vietnam via Honghe county , the court said .

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
      "cause": "they tried to illegally cross into Vietnam via Honghe county",
      "effect": "local police arrested Tohtunyaz , Ehet and Muhammad"
    }
  ],
  "pred_triples": []
}
```

### --- id=76 ---

输入文本: They did not confess to the planned attack after their capture , and so should bear full responsibility for the loss of life , the court said .

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
      "cause": "They did not confess to the planned attack after their capture",
      "effect": "should bear full responsibility for the loss of life"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "did not confess to the planned attack after their capture"
      },
      "relation": "caused",
      "effect": {
        "span": "should bear full responsibility for the loss of life"
      }
    }
  ]
}
```

### --- id=77 ---

输入文本: Despite losing contact with the three men , five other members of the group went ahead with the attack .

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

### --- id=78 ---

输入文本: Initial reports by a variety of media , some quoting witnesses , said eight people brandished knives in the Saturday , March 1 attack .

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

### --- id=79 ---

输入文本: Police announced on the Monday after the attack that three suspects had been taken into custody , which now appears to be a reference to the trio detained on February 27 .

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

### --- id=80 ---

输入文本: At least five more people will be tried over the attack , Xinhua has reported .

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

### --- id=81 ---

输入文本: The government has blamed separatist forces from Xinjiang for the attack .

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
      "cause": "the attack",
      "effect": "The government has blamed separatist forces from Xinjiang"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "separatist forces from Xinjiang"
      },
      "relation": "caused",
      "effect": {
        "span": "the attack"
      }
    }
  ]
}
```

### --- id=82 ---

输入文本: Mainland authorities have launched a massive crackdown against terrorism in wake of a string of violent attacks in the restive Xinjiang region and other cities on the mainland .

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
      "cause": "a string of violent attacks in the restive Xinjiang region and other cities on the mainland",
      "effect": "Mainland authorities have launched a massive crackdown against terrorism"
    },
    {
      "cause": "against terrorism",
      "effect": "Mainland authorities have launched a massive crackdown"
    }
  ],
  "pred_triples": []
}
```

### --- id=83 ---

输入文本: The pair ’ s oaths are invalid and they will not be able to retake them , China ’ s rubberstamp legislature said , one day after thousands marched through the streets of Hong Kong to protest against Beijing ’ s interference .

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
      "cause": "to protest against Beijing ’ s interference",
      "effect": "thousands marched through the streets of Hong Kong"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "thousands marched through the streets of Hong Kong to protest against Beijing's interference"
      },
      "relation": "caused",
      "effect": {
        "span": "The pair's oaths are invalid and they will not be able to retake them"
      }
    }
  ]
}
```

### --- id=84 ---

输入文本: During a chaotic swearing-in ceremony last month , Yau and Leung thumbed their noses at Beijing by refusing to declare their allegiance to China and carrying blue flags reading : “ Hong Kong is not China. ”

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
      "cause": "Yau and Leung thumbed their noses at Beijing",
      "effect": "refusing to declare their allegiance to China and carrying blue flags reading : “ Hong Kong is not China"
    }
  ],
  "pred_triples": []
}
```

### --- id=85 ---

输入文本: The attack on Karayogams had sparked sharp reactions from the CPM leaders .

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "The attack on Karayogams",
      "effect": "sharp reactions from the CPM leaders"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The attack on Karayogams"
      },
      "relation": "caused",
      "effect": {
        "span": "sharp reactions from the CPM leaders"
      }
    }
  ]
}
```

### --- id=86 ---

输入文本: But many in Hong Kong complain those freedoms have been eroded in recent years , leading to nearly three months of street protests in 2014 – known as the umbrella revolution – and to the election in September this year of six politicians pushing for greater autonomy for the city .

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
      "cause": "many in Hong Kong complain those freedoms have been eroded in recent years",
      "effect": "nearly three months of street protests in 2014 – known as the umbrella revolution – and to the election in September this year of six politicians pushing for greater autonomy for the city"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "many in Hong Kong complain those freedoms have been eroded in recent years"
      },
      "relation": "caused",
      "effect": {
        "span": "nearly three months of street protests in 2014 – known as the umbrella revolution"
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
        "span": "marched on Sunday to protest against China 's intervention"
      },
      "relation": "caused",
      "effect": {
        "span": "clashes with police outside Beijing 's main presence in the city and four arrests"
      }
    }
  ]
}
```

### --- id=88 ---

输入文本: Some schools which had to postpone their mid-term examinations due to the bandh have the additional task of conducting the tests before resuming the classes .

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
      "cause": "the bandh",
      "effect": "Some schools which had to postpone their mid-term examinations"
    },
    {
      "cause": "Some schools which had to postpone their mid-term examinations",
      "effect": "have the additional task of conducting the tests before resuming the classes"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the bandh"
      },
      "relation": "caused",
      "effect": {
        "span": "postpone their mid-term examinations"
      }
    }
  ]
}
```

### --- id=89 ---

输入文本: Yes , he 's the fellow who assured his government bosses the July 1 , 2003 , protest march would draw mere thousands , not the half a million that actually turned up .

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

### --- id=90 ---

输入文本: Taxi strike impacts businesses in Soshanguve Brenda Masilela PRETORIA , November 8 ( ANA ) - Employees at the Soshanguve Plaza , south of Pretoria , arrived for work on Wednesday only to find businesses closed amid fears that the taxi strike might turn violent .

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
      "cause": "fears that the taxi strike might turn violent",
      "effect": "Employees at the Soshanguve Plaza , south of Pretoria , arrived for work on Wednesday only to find businesses closed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the taxi strike"
      },
      "relation": "caused",
      "effect": {
        "span": "businesses closed"
      }
    }
  ]
}
```

### --- id=91 ---

输入文本: 27th February 2009 02:04 AM COLOMBO : India on Thursday told Pakistan that it recognised what Islamabad had done so far to investigate the involvement of Pakistanis in the Mumbai attacks and curb crossborder terrorism , but a lot more remained to be done to ensure that such attacks did not recur .

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
      "cause": "to investigate the involvement of Pakistanis in the Mumbai attacks and curb crossborder terrorism",
      "effect": "what Islamabad had done so far"
    }
  ],
  "pred_triples": []
}
```

### --- id=92 ---

输入文本: A lot more to be done , India tells Pakistan

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

### --- id=93 ---

输入文本: Foreign Secretary Shivshankar Menon , who discussed bilateral issues with his Pakistani counterpart Salman Bashir on the sidelines of the SAARC Foreign Secretaries meeting here , said that Islamabad would have to bring the perpetrators of the Mumbai attack to justice and give credible evidence of dismantling the terrorist infrastructure on the soil of Pakistan .

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

### --- id=94 ---

输入文本: About 125 bus operators across Gauteng stopped reporting for duty two weeks ago following a dispute in mileage payment .

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
      "cause": "a dispute in mileage payment",
      "effect": "About 125 bus operators across Gauteng stopped reporting for duty two weeks ago"
    },
    {
      "cause": "duty",
      "effect": "reporting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a dispute in mileage payment"
      },
      "relation": "caused",
      "effect": {
        "span": "About 125 bus operators across Gauteng stopped reporting for duty two weeks ago"
      }
    }
  ]
}
```

### --- id=95 ---

输入文本: Over 60,000 pupils were left stranded by the strike .

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
      "cause": "the strike",
      "effect": "Over 60,000 pupils were left stranded"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "pupils were left stranded"
      }
    }
  ]
}
```

### --- id=96 ---

输入文本: Flash strike by guards delays suburban trains - Indian Express Express News Service , Express News Service : Fri Nov 30 2012 , 03:16 hrs Most guards on local trains abstained from work Thursday protesting " irritable " behaviour of the area officer at Churchgate , forcing station masters and traffic inspectors to take up their role .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "Flash strike by guards",
      "effect": "delays suburban trains"
    },
    {
      "cause": "protesting \" irritable \" behaviour of the area officer at Churchgate",
      "effect": "Most guards on local trains abstained from work Thursday"
    },
    {
      "cause": "Most guards on local trains abstained from work Thursday protesting \" irritable \" behaviour of the area officer at Churchgate",
      "effect": "forcing station masters and traffic inspectors to take up their role"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Flash strike by guards"
      },
      "relation": "caused",
      "effect": {
        "span": "delays suburban trains"
      }
    },
    {
      "cause": {
        "span": "protesting \" irritable \" behaviour of the area officer at Churchgate"
      },
      "relation": "caused",
      "effect": {
        "span": "Most guards on local trains abstained from work Thursday"
      }
    },
    {
      "cause": {
        "span": "abstained from work Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "forcing station masters and traffic inspectors to take up their role"
      }
    }
  ]
}
```

### --- id=97 ---

输入文本: `` I am going to argue your evidence that strikers at Marikana in August 2012 attacked the police should be kicked out .

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

### --- id=98 ---

输入文本: Four days ago , guard Rakesh Jha had gone on a hunger strike at Churchgate Station after he was denied leave despite applying two months back .

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
      "cause": "he was denied leave despite applying two months back",
      "effect": "guard Rakesh Jha had gone on a hunger strike at Churchgate Station"
    },
    {
      "cause": "applying two months back",
      "effect": "he was denied leave"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he was denied leave despite applying two months back"
      },
      "relation": "caused",
      "effect": {
        "span": "guard Rakesh Jha had gone on a hunger strike"
      }
    }
  ]
}
```

### --- id=99 ---

输入文本: A guard said , " When Jha did not get leave till four hours before departure of his train , he hanged a poster around his neck announcing an indefinite hunger strike .

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
      "cause": "announcing an indefinite hunger strike",
      "effect": "he hanged a poster around his neck"
    },
    {
      "cause": "Jha did not get leave till four hours before departure of his train",
      "effect": "announcing an indefinite hunger strike"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Jha did not get leave till four hours before departure of his train"
      },
      "relation": "caused",
      "effect": {
        "span": "he hanged a poster around his neck announcing an indefinite hunger strike"
      }
    }
  ]
}
```

### --- id=100 ---

输入文本: All the 417 guards in the suburban section refused to work extra hours in protest .

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
      "cause": "in protest",
      "effect": "All the 417 guards in the suburban section refused to work extra hours"
    }
  ],
  "pred_triples": []
}
```
