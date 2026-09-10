# cnc_positive first 200 eval report

## 配置
```json
{
  "label": "cnc_positive first 200",
  "model": "lmstudio-community/Qwen3.6-27B-GGUF-no-thinking",
  "dataset": "cnc_positive",
  "sample_count": 200,
  "prompt_name": "v11",
  "use_rag": false,
  "rag_mode": "knn_pattern",
  "rag_top_k": 2,
  "temperature": 0.0,
  "max_tokens": 8192,
  "progress_every": 500,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 8196,
  "reasoning_effort": null,
  "llm_extra_body": {},
  "api_key_source": "file:deepseek_api.txt",
  "report_detail_limit": 200,
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ cnc_positive first 200 final report ================
样本总数: 200
  Gold 含因果: 200 | Pred 含因果: 200
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 1.000
  Precision: 1.000
  Recall   : 1.000
  F1       : 1.000
  (TP=200, TN=0, FP=0, FN=0)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 200
    Gold triples: 269 | Pred triples: 241
    Precision: 0.581
    Recall   : 0.520
    F1       : 0.549
    (TP=140, FP=101, FN=129)
  [anchor_window]
    样本数: 200
    Gold triples: 269 | Pred triples: 241
    Precision: 0.544
    Recall   : 0.487
    F1       : 0.514
    (TP=131, FP=110, FN=138)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 200
    Gold triples: 269 | Pred triples: 241
    Precision: 0.581
    Recall   : 0.520
    F1       : 0.549
    (TP=140, FP=101, FN=129)
  [anchor_window]
    样本数: 200
    Gold triples: 269 | Pred triples: 241
    Precision: 0.544
    Recall   : 0.487
    F1       : 0.514
    (TP=131, FP=110, FN=138)
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
        "span": "the allocation of low cost ( RDP ) houses at Marikana West Extension 2"
      },
      "relation": "caused",
      "effect": {
        "span": "they hacked Sabata Petros Chale , 39 , to death in Marikana West , on December 8 , 2016"
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
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
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
        "span": "Footage of the attack , which included a pregnant woman being hit , protesters being punched and kneed , and commuters screaming and crying while trying to shield themselves , emerged on Sunday night"
      },
      "relation": "caused",
      "effect": {
        "span": "fuelling further political unrest"
      }
    },
    {
      "cause": {
        "span": "failing to stop the violence"
      },
      "relation": "caused",
      "effect": {
        "span": "demonstrators , opposition lawmakers and others demanded answers from authorities"
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
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "the police ’ s slow response to the attack in Yuen Long and their pursuit of the case",
      "effect": "Protesters are angry"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the police ’ s slow response to the attack in Yuen Long and their pursuit of the case"
      },
      "relation": "caused",
      "effect": {
        "span": "Protesters are angry at the police"
      }
    }
  ]
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
      "cause": "The violence in Yuen Long",
      "effect": "heightened tensions and fears of further attacks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The violence in Yuen Long"
      },
      "relation": "caused",
      "effect": {
        "span": "heightened tensions and fears of further attacks"
      }
    }
  ]
}
```

### --- id=11 ---

输入文本: On Tuesday , a group of aviation staff called for a protest at Hong Kong airport on Friday to condemn the government and police for “ ignoring the random attacks on citizens in Yuen Long ” .

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
      "cause": "to condemn the government and police",
      "effect": "a group of aviation staff called for a protest at Hong Kong airport on Friday"
    },
    {
      "cause": "“ ignoring the random attacks on citizens in Yuen Long ”",
      "effect": "to condemn the government and police"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to condemn the government and police for “ ignoring the random attacks on citizens in Yuen Long ”"
      },
      "relation": "caused",
      "effect": {
        "span": "a group of aviation staff called for a protest at Hong Kong airport on Friday"
      }
    }
  ]
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

### --- id=15 ---

输入文本: 10th September 2015 03:49 AM KOCHI : Anoop George , the main accused in the case related to attack on the office of the National Highway Authority of India ( NHAI ) at Kalamassery , could not be produced before the Ernakulam District and Principal Sessions Court on Wednesday , after jail authorities in Coimbatore failed to arrange escort for him .

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
        "span": "Anoop George , the main accused in the case related to attack on the office of the National Highway Authority of India ( NHAI ) at Kalamassery , could not be produced before the Ernakulam District and Principal Sessions Court on Wednesday"
      }
    }
  ]
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

### --- id=22 ---

输入文本: Jammu : Delhi court blast accused killed in Kishtwar August 07 , 2012 00:00 IST A 2011 Delhi High Court blast accused , Amir Ali Kamal , was among two Hizb—ul—Mujahideen ( HM ) militants killed on Monday in a shootout with security forces in the mountainous Kishtwar district of Jammu and Kashmir , police said .

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
      "cause": "a shootout with security forces in the mountainous Kishtwar district of Jammu and Kashmir",
      "effect": "A 2011 Delhi High Court blast accused , Amir Ali Kamal , was among two Hizb—ul—Mujahideen ( HM ) militants killed on Monday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a shootout with security forces"
      },
      "relation": "caused",
      "effect": {
        "span": "two Hizb—ul—Mujahideen ( HM ) militants killed on Monday in the mountainous Kishtwar district of Jammu and Kashmir"
      }
    }
  ]
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
        "span": "he is believed to have arranged explosives and planter for the blast"
      },
      "relation": "caused",
      "effect": {
        "span": "Akram was on the radar of the National Investigation Agency ( NIA )"
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
      "cause": "the Delhi High Court blast of Sep 7 , 2011",
      "effect": "at least 10 people were killed and over 70 injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Delhi High Court blast of Sep 7 , 2011"
      },
      "relation": "caused",
      "effect": {
        "span": "at least 10 people were killed and over 70 injured"
      }
    }
  ]
}
```

### --- id=29 ---

输入文本: The NIA wanted to catch Akram alive as he could provide clues in resolving the blast case .

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
      "cause": "he could provide clues in resolving the blast case",
      "effect": "The NIA wanted to catch Akram alive"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he could provide clues in resolving the blast case"
      },
      "relation": "caused",
      "effect": {
        "span": "The NIA wanted to catch Akram alive"
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
      "cause": "allegedly being involved in the blast",
      "effect": "Two more youths were arrested later"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "allegedly being involved in the blast"
      },
      "relation": "caused",
      "effect": {
        "span": "Two more youths were arrested later"
      }
    }
  ]
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
        "span": "NaMo , who had avoided visiting the victims of the 2002 riots in his own state for a long time , lost no time in burning up aviation fuel by dashing to Patna twice in one week"
      }
    }
  ]
}
```

### --- id=38 ---

输入文本: Indira landed in Nalanda and waded into the floodwaters on an elephant to visit each Dalit family , which had lost members in the caste pogrom .

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
      "cause": "to visit each Dalit family , which had lost members in the caste pogrom",
      "effect": "Indira landed in Nalanda and waded into the floodwaters on an elephant"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the caste pogrom"
      },
      "relation": "caused",
      "effect": {
        "span": "which had lost members"
      }
    }
  ]
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
      "cause": "against illegal water connections",
      "effect": "Ramanathapuram Residents protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "illegal water connections"
      },
      "relation": "caused",
      "effect": {
        "span": "Ramanathapuram Residents protest against illegal water connections"
      }
    }
  ]
}
```

### --- id=45 ---

输入文本: Led by A Sagayamadha , an office-bearer of the All India Farm Workers Association , the villagers , including a large number of women from the panchayat comprising six villages , staged the protest urging the district administration to immediately disconnect the illegal water connections and ensure uninterrupted water supply to them .

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
      "cause": "Led by A Sagayamadha , an office-bearer of the All India Farm Workers Association",
      "effect": "the villagers , including a large number of women from the panchayat comprising six villages , staged the protest urging the district administration to immediately disconnect the illegal water connections and ensure uninterrupted water supply to them"
    },
    {
      "cause": "urging the district administration to immediately disconnect the illegal water connections and ensure uninterrupted water supply to them",
      "effect": "the villagers , including a large number of women from the panchayat comprising six villages , staged the protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "urging the district administration to immediately disconnect the illegal water connections and ensure uninterrupted water supply to them"
      },
      "relation": "caused",
      "effect": {
        "span": "the villagers , including a large number of women from the panchayat comprising six villages , staged the protest"
      }
    }
  ]
}
```

### --- id=48 ---

输入文本: Biswal , who had travelled to the city from Washington to speak at the Indian Consulate General 's Media-India Lecture Series yesterday , said not only were there a large number of Indian victims in the attack but there were Americans also who lost their lives .

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
      "cause": "to speak at the Indian Consulate General 's Media-India Lecture Series yesterday",
      "effect": "Biswal , who had travelled to the city from Washington"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "there were Americans also who lost their lives"
      }
    }
  ]
}
```

### --- id=54 ---

输入文本: On media reports that the night vision device used by three terrorists in the Gurdaspur attack had US markings , Biswal said the US is in conversation with Indian authorities to try to ascertain and trace the origins of the equipment found .

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
      "cause": "to try to ascertain and trace the origins of the equipment found",
      "effect": "the US is in conversation with Indian authorities"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "media reports that the night vision device used by three terrorists in the Gurdaspur attack had US markings"
      },
      "relation": "caused",
      "effect": {
        "span": "Biswal said the US is in conversation with Indian authorities to try to ascertain and trace the origins of the equipment found"
      }
    }
  ]
}
```

### --- id=55 ---

输入文本: " We will continue to work very closely with the Indian government on those issues , " she said , adding that it is an ongoing process and the US is working with Indian authorities to address issues of concern emanating from the incident .

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
      "cause": "to address issues of concern emanating from the incident",
      "effect": "the US is working with Indian authorities"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "issues of concern emanating from the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "the US is working with Indian authorities to address issues of concern emanating from the incident"
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
      "cause": "to demand answers from HCL Technologies , the company that had recruited them in 2011",
      "effect": "As many as 59 recruits who had graduated from different colleges of the State came together for the fourth time"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to demand answers from HCL Technologies"
      },
      "relation": "caused",
      "effect": {
        "span": "As many as 59 recruits who had graduated from different colleges of the State came together for the fourth time"
      }
    }
  ]
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
        "span": "their alleged involvement in killing of a naib sarpanch"
      },
      "relation": "caused",
      "effect": {
        "span": "Three persons were arrested on Tuesday"
      }
    },
    {
      "cause": {
        "span": "a clash between members of two communities at Bimbola village under Dhenkanal Sadar police limits on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "killing of a naib sarpanch"
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
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
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
  "pred_triples": [
    {
      "cause": {
        "span": "the clash"
      },
      "relation": "caused",
      "effect": {
        "span": "The naib sarpanch was killed and 17 others were seriously injured"
      }
    },
    {
      "cause": {
        "span": "use of a village field"
      },
      "relation": "caused",
      "effect": {
        "span": "the clash"
      }
    }
  ]
}
```

### --- id=63 ---

输入文本: Bimbola village turned into a battle field as rival groups wielding guns took the centre stage .

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
      "cause": "rival groups wielding guns took the centre stage",
      "effect": "Bimbola village turned into a battle field"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "rival groups wielding guns took the centre stage"
      },
      "relation": "caused",
      "effect": {
        "span": "Bimbola village turned into a battle field"
      }
    }
  ]
}
```

### --- id=64 ---

输入文本: The clash took place over use of the field .

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
      "cause": "use of the field",
      "effect": "The clash took place"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "use of the field"
      },
      "relation": "caused",
      "effect": {
        "span": "The clash took place"
      }
    }
  ]
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
    "tp": 1,
    "fp": 1,
    "fn": 1
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
        "span": "intelligence inputs that a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi to avenge the 2002 communal riots in the state"
      },
      "relation": "caused",
      "effect": {
        "span": "Ishrat Jahan , a 19 - year-old college student was killed along with three others on June 15 , 2004 allegedly by a team of Crime Branch officials on the outskirts of Ahmedabad"
      }
    },
    {
      "cause": {
        "span": "the 2002 communal riots in the state"
      },
      "relation": "caused",
      "effect": {
        "span": "a group of Lashkar terrorists have plotted to kill Gujarat Chief Minister Narendra Modi"
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
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
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
  "pred_triples": [
    {
      "cause": {
        "span": "their role in the attack at a Kunming rail station that killed 31 people and injured 141 in March"
      },
      "relation": "caused",
      "effect": {
        "span": "Three people were sentenced to death by a Yunnan court"
      }
    },
    {
      "cause": {
        "span": "the attack at a Kunming rail station"
      },
      "relation": "caused",
      "effect": {
        "span": "killed 31 people and injured 141 in March"
      }
    }
  ]
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
    },
    {
      "cause": {
        "span": "taking part"
      },
      "relation": "caused",
      "effect": {
        "span": "a fourth defendant handed life sentence"
      }
    }
  ]
}
```

### --- id=72 ---

输入文本: Patigul Tohti , who was wounded and captured at the scene , was jailed for life after being convicted of taking part in the attack .

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
      "cause": "being convicted of taking part in the attack",
      "effect": "Patigul Tohti , who was wounded and captured at the scene , was jailed for life"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "being convicted of taking part in the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Patigul Tohti , who was wounded and captured at the scene , was jailed for life"
      }
    }
  ]
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
    },
    {
      "cause": {
        "span": "it did not want Achuthanandan to come back to power for another term"
      },
      "relation": "caused",
      "effect": {
        "span": "the NSS did not support the LDF in the recent Assembly elections"
      }
    }
  ]
}
```

### --- id=75 ---

输入文本: Two days before the attack , local police arrested Tohtunyaz , Ehet and Muhammad as they tried to illegally cross into Vietnam via Honghe county , the court said .

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
      "cause": "they tried to illegally cross into Vietnam via Honghe county",
      "effect": "local police arrested Tohtunyaz , Ehet and Muhammad"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they tried to illegally cross into Vietnam via Honghe county"
      },
      "relation": "caused",
      "effect": {
        "span": "local police arrested Tohtunyaz , Ehet and Muhammad"
      }
    }
  ]
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
      "cause": "They did not confess to the planned attack after their capture",
      "effect": "should bear full responsibility for the loss of life"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "They did not confess to the planned attack after their capture"
      },
      "relation": "caused",
      "effect": {
        "span": "should bear full responsibility for the loss of life"
      }
    }
  ]
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
      "cause": "the attack",
      "effect": "The government has blamed separatist forces from Xinjiang"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "The government has blamed separatist forces from Xinjiang"
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
      "cause": "a string of violent attacks in the restive Xinjiang region and other cities on the mainland",
      "effect": "Mainland authorities have launched a massive crackdown against terrorism"
    },
    {
      "cause": "against terrorism",
      "effect": "Mainland authorities have launched a massive crackdown"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a string of violent attacks in the restive Xinjiang region and other cities on the mainland"
      },
      "relation": "caused",
      "effect": {
        "span": "Mainland authorities have launched a massive crackdown against terrorism"
      }
    }
  ]
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
        "span": "thousands marched through the streets of Hong Kong to protest against Beijing 's interference"
      },
      "relation": "caused",
      "effect": {
        "span": "The pair ' s oaths are invalid and they will not be able to retake them , China 's rubberstamp legislature said"
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
      "cause": "Yau and Leung thumbed their noses at Beijing",
      "effect": "refusing to declare their allegiance to China and carrying blue flags reading : “ Hong Kong is not China"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "refusing to declare their allegiance to China and carrying blue flags reading : “ Hong Kong is not China. ”"
      },
      "relation": "caused",
      "effect": {
        "span": "Yau and Leung thumbed their noses at Beijing"
      }
    }
  ]
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
        "span": "had sparked sharp reactions from the CPM leaders"
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
      "cause": "many in Hong Kong complain those freedoms have been eroded in recent years",
      "effect": "nearly three months of street protests in 2014 – known as the umbrella revolution – and to the election in September this year of six politicians pushing for greater autonomy for the city"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "those freedoms have been eroded in recent years"
      },
      "relation": "caused",
      "effect": {
        "span": "nearly three months of street protests in 2014 – known as the umbrella revolution – and to the election in September this year of six politicians pushing for greater autonomy for the city"
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
    "tp": 0,
    "fp": 2,
    "fn": 2
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
        "span": "to protest against China 's intervention"
      },
      "relation": "caused",
      "effect": {
        "span": "About 13,000 marched on Sunday"
      }
    },
    {
      "cause": {
        "span": "About 13,000 marched on Sunday to protest against China 's intervention"
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
        "span": "Some schools which had to postpone their mid-term examinations"
      }
    }
  ]
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
      "cause": "fears that the taxi strike might turn violent",
      "effect": "Employees at the Soshanguve Plaza , south of Pretoria , arrived for work on Wednesday only to find businesses closed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "fears that the taxi strike might turn violent"
      },
      "relation": "caused",
      "effect": {
        "span": "businesses closed"
      }
    },
    {
      "cause": {
        "span": "the taxi strike"
      },
      "relation": "caused",
      "effect": {
        "span": "impacts businesses in Soshanguve"
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
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to investigate the involvement of Pakistanis in the Mumbai attacks and curb crossborder terrorism",
      "effect": "what Islamabad had done so far"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to investigate the involvement of Pakistanis in the Mumbai attacks and curb crossborder terrorism"
      },
      "relation": "caused",
      "effect": {
        "span": "India on Thursday told Pakistan that it recognised what Islamabad had done so far"
      }
    },
    {
      "cause": {
        "span": "to ensure that such attacks did not recur"
      },
      "relation": "caused",
      "effect": {
        "span": "a lot more remained to be done"
      }
    }
  ]
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
        "span": "Over 60,000 pupils were left stranded"
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
    "tp": 1,
    "fp": 2,
    "fn": 2
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
        "span": "Most guards on local trains abstained from work Thursday protesting \" irritable \" behaviour of the area officer at Churchgate"
      },
      "relation": "caused",
      "effect": {
        "span": "Flash strike by guards delays suburban trains"
      }
    },
    {
      "cause": {
        "span": "\" irritable \" behaviour of the area officer at Churchgate"
      },
      "relation": "caused",
      "effect": {
        "span": "Most guards on local trains abstained from work Thursday"
      }
    },
    {
      "cause": {
        "span": "Most guards on local trains abstained from work Thursday protesting \" irritable \" behaviour of the area officer at Churchgate"
      },
      "relation": "caused",
      "effect": {
        "span": "forcing station masters and traffic inspectors to take up their role"
      }
    }
  ]
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
        "span": "guard Rakesh Jha had gone on a hunger strike at Churchgate Station"
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
      "cause": "in protest",
      "effect": "All the 417 guards in the suburban section refused to work extra hours"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest"
      },
      "relation": "caused",
      "effect": {
        "span": "All the 417 guards in the suburban section refused to work extra hours"
      }
    }
  ]
}
```

### --- id=104 ---

输入文本: Her son and Congress general secretary Rahul Gandhi has taken up the issue in a big way , staging a daylong sit-in at the village after four people , including two police personnel , were killed in clashes .

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
      "cause": "four people , including two police personnel , were killed in clashes",
      "effect": "Her son and Congress general secretary Rahul Gandhi has taken up the issue in a big way , staging a daylong sit-in at the village"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "four people , including two police personnel , were killed in clashes"
      },
      "relation": "caused",
      "effect": {
        "span": "Her son and Congress general secretary Rahul Gandhi has taken up the issue in a big way , staging a daylong sit-in at the village"
      }
    }
  ]
}
```

### --- id=105 ---

输入文本: Scores of students , teachers and women rights organisations had yesterday staged a protest outside college demanding Thampu 's resignation for shielding the accused .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "demanding Thampu 's resignation for shielding the accused",
      "effect": "Scores of students , teachers and women rights organisations had yesterday staged a protest outside college"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding Thampu 's resignation"
      },
      "relation": "caused",
      "effect": {
        "span": "Scores of students , teachers and women rights organisations had yesterday staged a protest outside college"
      }
    },
    {
      "cause": {
        "span": "shielding the accused"
      },
      "relation": "caused",
      "effect": {
        "span": "demanding Thampu 's resignation"
      }
    }
  ]
}
```

### --- id=106 ---

输入文本: Protests in Kupwara molestation of girl over - Indian Express Agencies , Agencies : Srinagar , Thu Jul 09 2009 , 12:30 hrs Locals took to the streets in frontier district of Kupwara today demanding the arrest of a territorial army jawan , who allegedly tried to molest a young woman following which she committed suicide .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "demanding the arrest of a territorial army jawan",
      "effect": "Locals took to the streets in frontier district of Kupwara today"
    },
    {
      "cause": "who allegedly tried to molest a young woman following which she committed suicide",
      "effect": "demanding the arrest of a territorial army jawan"
    },
    {
      "cause": "a territorial army jawan , who allegedly tried to molest a young woman",
      "effect": "she committed suicide"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "molestation of girl"
      },
      "relation": "caused",
      "effect": {
        "span": "Protests in Kupwara"
      }
    },
    {
      "cause": {
        "span": "demanding the arrest of a territorial army jawan , who allegedly tried to molest a young woman following which she committed suicide ."
      },
      "relation": "caused",
      "effect": {
        "span": "Locals took to the streets in frontier district of Kupwara today"
      }
    },
    {
      "cause": {
        "span": "a territorial army jawan , who allegedly tried to molest a young woman"
      },
      "relation": "caused",
      "effect": {
        "span": "she committed suicide ."
      }
    }
  ]
}
```

### --- id=107 ---

输入文本: After family members narrated the incident to their neighbours , people came on the road and held demonstrations .

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
      "cause": "family members narrated the incident to their neighbours",
      "effect": "people came on the road and held demonstrations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "family members narrated the incident to their neighbours"
      },
      "relation": "caused",
      "effect": {
        "span": "people came on the road and held demonstrations"
      }
    }
  ]
}
```

### --- id=108 ---

输入文本: Mpofu said Lt-Col Kaizer Modiba was fabricating his evidence about the violence during the mineworkers ' strike at Marikana , near Rustenburg in the North West , because he had not been in a position to witness an attack .

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
      "cause": "he had not been in a position to witness an attack",
      "effect": "Lt-Col Kaizer Modiba was fabricating his evidence about the violence during the mineworkers ' strike at Marikana , near Rustenburg in the North West"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he had not been in a position to witness an attack"
      },
      "relation": "caused",
      "effect": {
        "span": "Mpofu said Lt-Col Kaizer Modiba was fabricating his evidence about the violence during the mineworkers ' strike at Marikana , near Rustenburg in the North West"
      }
    }
  ]
}
```

### --- id=109 ---

输入文本: Tiruvannamalai : Cab drivers , owners take out rally May 22 , 2012 00:00 IST Tourist cab drivers and owners took out a rally here on Monday demanding to scrap lifetime tax system introduced by Tamil Nadu government .

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
      "cause": "demanding to scrap lifetime tax system introduced by Tamil Nadu government",
      "effect": "Tourist cab drivers and owners took out a rally here on Monday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding to scrap lifetime tax system introduced by Tamil Nadu government"
      },
      "relation": "caused",
      "effect": {
        "span": "Tourist cab drivers and owners took out a rally here on Monday"
      }
    }
  ]
}
```

### --- id=113 ---

输入文本: 3 Cong workers killed on phase-IV eve - Indian Express Kolkata , Mon Jul 22 2013 , 01:36 hrs On the eve of the fourth phase of panchayat elections , widespread incidents of violence led to the death of three Congress workers on Sunday .

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
      "cause": "On the eve of the fourth phase of panchayat elections , widespread incidents of violence",
      "effect": "the death of three Congress workers on Sunday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "widespread incidents of violence"
      },
      "relation": "caused",
      "effect": {
        "span": "the death of three Congress workers on Sunday"
      }
    }
  ]
}
```

### --- id=114 ---

输入文本: Police said two Congress workers  Nurmohhamad Sheikh and Ahad Ali  were killed after being hit by crude bombs late Saturday night at Kapasdanga in Murshidabad district .

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
      "cause": "being hit by crude bombs late Saturday night at Kapasdanga in Murshidabad district",
      "effect": "two Congress workers  Nurmohhamad Sheikh and Ahad Ali  were killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "being hit by crude bombs"
      },
      "relation": "caused",
      "effect": {
        "span": "two Congress workers  Nurmohhamad Sheikh and Ahad Ali  were killed"
      }
    }
  ]
}
```

### --- id=116 ---

输入文本: There were reports of skirmishes and clashes , including stone pelting , in the area in which two policemen were injured .

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
      "cause": "There were reports of skirmishes and clashes , including stone pelting , in the area",
      "effect": "two policemen were injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "skirmishes and clashes , including stone pelting"
      },
      "relation": "caused",
      "effect": {
        "span": "two policemen were injured"
      }
    }
  ]
}
```

### --- id=117 ---

输入文本: Another Congress worker , Repon Sheikh , was killed at Bharatpur in the same district during a clash between rival party supporters , the police said .

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
      "cause": "a clash between rival party supporters",
      "effect": "Another Congress worker , Repon Sheikh , was killed at Bharatpur in the same district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a clash between rival party supporters"
      },
      "relation": "caused",
      "effect": {
        "span": "Another Congress worker , Repon Sheikh , was killed at Bharatpur in the same district"
      }
    }
  ]
}
```

### --- id=120 ---

输入文本: `` I observed the attack on the police , I have no doubt about it , '' Modiba said during cross-examination .

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
      "cause": "I observed the attack on the police",
      "effect": "I have no doubt about it"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "I observed the attack on the police"
      },
      "relation": "caused",
      "effect": {
        "span": "I have no doubt about it"
      }
    }
  ]
}
```

### --- id=121 ---

输入文本: Accusing the CPM of instigating the violence , she said the deaths were result of clashes between the Congress and the Marxists .

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
    "tp": 0,
    "fp": 2,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "Accusing the CPM of instigating the violence",
      "effect": "she said the deaths were result of clashes between the Congress and the Marxists"
    },
    {
      "cause": "were result of clashes between the Congress and the Marxists",
      "effect": "the deaths"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the CPM of instigating the violence"
      },
      "relation": "caused",
      "effect": {
        "span": "she said the deaths were result of clashes between the Congress and the Marxists"
      }
    },
    {
      "cause": {
        "span": "clashes between the Congress and the Marxists"
      },
      "relation": "caused",
      "effect": {
        "span": "the deaths"
      }
    }
  ]
}
```

### --- id=125 ---

输入文本: Beijing launched a campaign to ' educate ' Tibetan monks and nuns after unrest rocked Tibetan-populated areas in March 2008 .

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
      "cause": "to ' educate ' Tibetan monks and nuns",
      "effect": "Beijing launched a campaign"
    },
    {
      "cause": "unrest rocked Tibetan-populated areas in March 2008",
      "effect": "to ' educate ' Tibetan monks and nuns"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "unrest rocked Tibetan-populated areas in March 2008"
      },
      "relation": "caused",
      "effect": {
        "span": "Beijing launched a campaign to ' educate ' Tibetan monks and nuns"
      }
    }
  ]
}
```

### --- id=126 ---

输入文本: The taxi strike that left commuters stranded in Johannesburg was expected to also disrupt matric pupils writing exams on Monday , the Gauteng education department said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "The taxi strike",
      "effect": "that left commuters stranded in Johannesburg was expected to also disrupt matric pupils writing exams on Monday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The taxi strike"
      },
      "relation": "caused",
      "effect": {
        "span": "left commuters stranded in Johannesburg"
      }
    },
    {
      "cause": {
        "span": "The taxi strike"
      },
      "relation": "caused",
      "effect": {
        "span": "was expected to also disrupt matric pupils writing exams on Monday"
      }
    }
  ]
}
```

### --- id=128 ---

输入文本: Earlier , the Johannesburg metro police said the strike was expected to also disrupt the Reya Vaya bus service .

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
      "cause": "the strike",
      "effect": "also disrupt the Reya Vaya bus service"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "disrupt the Reya Vaya bus service"
      }
    }
  ]
}
```

### --- id=132 ---

输入文本: `` We do not know about the strike , if we called for a strike we could have informed commuters , '' said president Philip Taaibosch .

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
      "cause": "we called for a strike",
      "effect": "we could have informed commuters"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "We do not know about the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "we could have informed commuters"
      }
    }
  ]
}
```

### --- id=133 ---

输入文本: Sena legislators protest against Yedyurappa 01st April 2010 10:08 PM MUMBAI : Shiv Sena workers , including some legislators , today staged demonstrations against Karnataka Chief Minister B S Yeddyurappa here , protesting the ' forcible installation ' of a Kannadiga mayor in Marathi-dominated Belgaum city .

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
      "cause": "protesting the ' forcible installation ' of a Kannadiga mayor in Marathi-dominated Belgaum city",
      "effect": "Shiv Sena workers , including some legislators , today staged demonstrations against Karnataka Chief Minister B S Yeddyurappa here"
    },
    {
      "cause": "against Karnataka Chief Minister B S Yeddyurappa",
      "effect": "Shiv Sena workers , including some legislators , today staged demonstrations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the ' forcible installation ' of a Kannadiga mayor in Marathi-dominated Belgaum city"
      },
      "relation": "caused",
      "effect": {
        "span": "Shiv Sena workers , including some legislators , today staged demonstrations against Karnataka Chief Minister B S Yeddyurappa here"
      }
    }
  ]
}
```

### --- id=135 ---

输入文本: The protesters shouted slogans against the Karnataka CM , demanding that Belgaum , along with Marathi speaking areas in that state , be merged with Maharashtra .

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
      "cause": "demanding that Belgaum , along with Marathi speaking areas in that state , be merged with Maharashtra",
      "effect": "The protesters shouted slogans against the Karnataka CM"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding that Belgaum , along with Marathi speaking areas in that state , be merged with Maharashtra"
      },
      "relation": "caused",
      "effect": {
        "span": "The protesters shouted slogans against the Karnataka CM"
      }
    }
  ]
}
```

### --- id=136 ---

输入文本: Yesterday , over 50 Karnataka Rakshana Vedike ( KRV ) activists were taken into custody when they allegedly tried to attack some members of Maharashtra Ekikaran Samithi ( MES ) and corporators of Belgaum City Corporation .

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
      "cause": "they allegedly tried to attack some members of Maharashtra Ekikaran Samithi ( MES ) and corporators of Belgaum City Corporation",
      "effect": "over 50 Karnataka Rakshana Vedike ( KRV ) activists were taken into custody"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they allegedly tried to attack some members of Maharashtra Ekikaran Samithi ( MES ) and corporators of Belgaum City Corporation"
      },
      "relation": "caused",
      "effect": {
        "span": "over 50 Karnataka Rakshana Vedike ( KRV ) activists were taken into custody"
      }
    }
  ]
}
```

### --- id=143 ---

输入文本: ﻿As the city enters its ninth consecutive week of protests , the movement shows few signs of abating , as public anger at the government spreads to more parts of Hong Kong society .

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
      "cause": "public anger at the government spreads to more parts of Hong Kong society",
      "effect": "the movement shows few signs of abating"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "public anger at the government spreads to more parts of Hong Kong society"
      },
      "relation": "caused",
      "effect": {
        "span": "the movement shows few signs of abating"
      }
    }
  ]
}
```

### --- id=145 ---

输入文本: ﻿The protests , which began over a proposal to allow extradition to China , pose the most serious challenge to China ’ s authority over the city since 1997 , when it was returned from British to Chinese control .

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
      "cause": "a proposal to allow extradition to China",
      "effect": "﻿The protests"
    },
    {
      "cause": "it was returned from British to Chinese control",
      "effect": "pose the most serious challenge to China ’ s authority over the city since 1997"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a proposal to allow extradition to China"
      },
      "relation": "caused",
      "effect": {
        "span": "The protests , which began over a proposal to allow extradition to China"
      }
    }
  ]
}
```

### --- id=147 ---

输入文本: On Thursday , Chen Daoxiang , the head of the Chinese army garrison in Hong Kong , said the military was “ determined to protect [ the ] national sovereignty ” of Hong Kong and would help put down the “ intolerable ” unrest if requested .

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
      "cause": "requested",
      "effect": "the military was “ determined to protect [ the ] national sovereignty ” of Hong Kong and would help put down the “ intolerable ” unrest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "if requested"
      },
      "relation": "caused",
      "effect": {
        "span": "the military ... would help put down the “ intolerable ” unrest"
      }
    }
  ]
}
```

### --- id=148 ---

输入文本: Hong Kong police on Thursday also charged 44 people linked to the protests with “ rioting ” , a crime that carries a maximum penalty of 10 years in prison .

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
      "cause": "“ rioting ”",
      "effect": "Hong Kong police on Thursday also charged 44 people linked to the protests"
    },
    {
      "cause": "linked to the protests with “ rioting ”",
      "effect": "Hong Kong police on Thursday also charged 44 people"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "linked to the protests"
      },
      "relation": "caused",
      "effect": {
        "span": "Hong Kong police on Thursday also charged 44 people with “ rioting ”"
      }
    }
  ]
}
```

### --- id=149 ---

输入文本: On online forums there were claims that police decided to allow the previously banned protest in Mongkok in order to surround demonstrators and arrest them en masse .

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
      "cause": "to surround demonstrators and arrest them en masse",
      "effect": "police decided to allow the previously banned protest in Mongkok"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in order to surround demonstrators and arrest them en masse"
      },
      "relation": "caused",
      "effect": {
        "span": "police decided to allow the previously banned protest in Mongkok"
      }
    }
  ]
}
```

### --- id=150 ---

输入文本: “ If peaceful marches that disrupt the road for an afternoon or so don ’ t work , maybe it spills over to blockading more roads , maybe for long .

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
      "cause": "peaceful marches",
      "effect": "that disrupt the road for an afternoon or so"
    },
    {
      "cause": "peaceful marches that disrupt the road for an afternoon or so don ’ t work",
      "effect": "maybe it spills over to blockading more roads , maybe for long"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "peaceful marches that disrupt the road for an afternoon or so don ’ t work"
      },
      "relation": "caused",
      "effect": {
        "span": "it spills over to blockading more roads , maybe for long"
      }
    }
  ]
}
```

### --- id=152 ---

输入文本: An integrated steel plant , agriculture and mineral-based industries should be set up in Kadapa district for ensuring its comprehensive development and generate employment , CPI(M) district secretary B. Narayana demanded while addressing party functionaries who staged dharna in front of Kadapa Collectorate on Thursday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "ensuring its comprehensive development",
      "effect": "An integrated steel plant , agriculture and mineral-based industries should be set up in Kadapa district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "for ensuring its comprehensive development and generate employment"
      },
      "relation": "caused",
      "effect": {
        "span": "An integrated steel plant , agriculture and mineral-based industries should be set up in Kadapa district"
      }
    },
    {
      "cause": {
        "span": "party functionaries who staged dharna in front of Kadapa Collectorate on Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "CPI(M) district secretary B. Narayana demanded while addressing party functionaries"
      }
    }
  ]
}
```

### --- id=155 ---

输入文本: CMP TIRUPATI : The all-India general strike called by trade unions on Wednesday badly hit the working of the PSU banks , LIC and the General Insurance Companies in Chittoor district .

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
      "cause": "The all-India general strike called by trade unions on Wednesday",
      "effect": "badly hit the working of the PSU banks , LIC and the General Insurance Companies in Chittoor district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The all-India general strike called by trade unions on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "badly hit the working of the PSU banks , LIC and the General Insurance Companies in Chittoor district"
      }
    }
  ]
}
```

### --- id=159 ---

输入文本: UPA criticised Demonstrations were held in front of the bank branches and the insurance company premises denouncing the failure of the UPA government in holding the price line .

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
      "cause": "denouncing the failure of the UPA government in holding the price line",
      "effect": "Demonstrations were held in front of the bank branches and the insurance company premises"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the failure of the UPA government in holding the price line"
      },
      "relation": "caused",
      "effect": {
        "span": "Demonstrations were held in front of the bank branches and the insurance company premises denouncing the failure of the UPA government in holding the price line"
      }
    }
  ]
}
```

### --- id=160 ---

输入文本: Leaders of the CPI-M , CPI , TDP and the frontal units , addressing the rally , lashed out at the Central and State governments for doing nothing except chanting ‘ Indira , Rajiv and Sonia ’ mantra , grossly sideling the National Common Minimum Programme .

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
      "cause": "doing nothing except chanting ‘ Indira , Rajiv and Sonia ’ mantra",
      "effect": "Leaders of the CPI-M , CPI , TDP and the frontal units , addressing the rally , lashed out at the Central and State governments"
    },
    {
      "cause": "doing nothing except chanting ‘ Indira , Rajiv and Sonia ’ mantra",
      "effect": "grossly sideling the National Common Minimum Programme"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "doing nothing except chanting ‘ Indira , Rajiv and Sonia ’ mantra , grossly sideling the National Common Minimum Programme"
      },
      "relation": "caused",
      "effect": {
        "span": "Leaders of the CPI-M , CPI , TDP and the frontal units , addressing the rally , lashed out at the Central and State governments"
      }
    }
  ]
}
```

### --- id=162 ---

输入文本: Kurnool : Work in all offices and financial institutions came to a stand still on account of the strike .

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
      "cause": "the strike",
      "effect": "Work in all offices and financial institutions came to a stand still"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "Work in all offices and financial institutions came to a stand still"
      }
    }
  ]
}
```

### --- id=164 ---

输入文本: Seven Maoists Killed in Gun Battle 18th February 2014 11:36 AM Seven Maoists were killed in a two-hour long gun battle with Maharashtra Police on the border the state shares with Chhattisgarh , a top official said Tuesday .

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
      "cause": "in a two-hour long gun battle with Maharashtra Police on the border the state shares with Chhattisgarh",
      "effect": "Seven Maoists were killed"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a two-hour long gun battle with Maharashtra Police on the border the state shares with Chhattisgarh"
      },
      "relation": "caused",
      "effect": {
        "span": "Seven Maoists were killed"
      }
    }
  ]
}
```

### --- id=166 ---

输入文本: On August 16 , 2012 , 34 people , mostly mineworkers , were shot dead in a clash with police who were trying to disarm and disperse them .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "a clash with police who were trying to disarm and disperse them",
      "effect": "On August 16 , 2012 , 34 people , mostly mineworkers , were shot dead"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a clash with police"
      },
      "relation": "caused",
      "effect": {
        "span": "34 people , mostly mineworkers , were shot dead"
      }
    },
    {
      "cause": {
        "span": "trying to disarm and disperse them"
      },
      "relation": "caused",
      "effect": {
        "span": "a clash with police"
      }
    }
  ]
}
```

### --- id=168 ---

输入文本: Several hundred people who have occupied homes at Delft on the Cape Flats are on their way to the Cape High Court in a bid to block their impending eviction , a spokesman said .

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
      "cause": "in a bid to block their impending eviction",
      "effect": "Several hundred people who have occupied homes at Delft on the Cape Flats are on their way to the Cape High Court"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in a bid to block their impending eviction"
      },
      "relation": "caused",
      "effect": {
        "span": "Several hundred people who have occupied homes at Delft on the Cape Flats are on their way to the Cape High Court"
      }
    }
  ]
}
```

### --- id=169 ---

输入文本: Speaking just after 1pm , Poni said he and the hundreds of residents who had demonstrated outside the court were now on their way by train to the High Court , where they would make another attempt to get an urgent interdict .

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
      "cause": "they would make another attempt",
      "effect": "he and the hundreds of residents who had demonstrated outside the court were now on their way by train to the High Court"
    },
    {
      "cause": "to get an urgent interdict",
      "effect": "they would make another attempt"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to get an urgent interdict"
      },
      "relation": "caused",
      "effect": {
        "span": "Poni said he and the hundreds of residents who had demonstrated outside the court were now on their way by train to the High Court , where they would make another attempt"
      }
    }
  ]
}
```

### --- id=172 ---

输入文本: Additional Director General of Police ( HQs ) Ravinder Kumar said that the state police along with central paramilitary forces have been working to rescue the abducted people .

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
      "cause": "to rescue the abducted people",
      "effect": "the state police along with central paramilitary forces have been working"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the abducted people"
      },
      "relation": "caused",
      "effect": {
        "span": "the state police along with central paramilitary forces have been working to rescue the abducted people"
      }
    }
  ]
}
```

### --- id=173 ---

输入文本: Search is on to trace and recover the abducted people , " he said .

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
      "cause": "to trace and recover the abducted people",
      "effect": "Search is on"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the abducted people"
      },
      "relation": "caused",
      "effect": {
        "span": "Search is on to trace and recover the abducted people"
      }
    }
  ]
}
```

### --- id=175 ---

输入文本: Police suspect that the Maoists abducted the workers after the company refused to pay " protection money " demanded by the rebels .

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
      "cause": "the company refused to pay \" protection money \" demanded by the rebels",
      "effect": "the Maoists abducted the workers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the company refused to pay \" protection money \" demanded by the rebels"
      },
      "relation": "caused",
      "effect": {
        "span": "the Maoists abducted the workers"
      }
    }
  ]
}
```

### --- id=179 ---

输入文本: SANGAREDDY : Shortage of urea : farmers protest in Sangareddy

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
      "cause": "Shortage of urea",
      "effect": "farmers protest in Sangareddy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Shortage of urea"
      },
      "relation": "caused",
      "effect": {
        "span": "farmers protest in Sangareddy"
      }
    }
  ]
}
```

### --- id=180 ---

输入文本: August 17 , 2010 00:00 IST With the shortage of urea staring farmers on their face , scores of farmers held ‘ rasta roko ' and ‘ dharna ' across the district .

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
      "cause": "the shortage of urea staring farmers on their face",
      "effect": "scores of farmers held ‘ rasta roko ' and ‘ dharna ' across the district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the shortage of urea staring farmers on their face"
      },
      "relation": "caused",
      "effect": {
        "span": "scores of farmers held ‘ rasta roko ' and ‘ dharna ' across the district"
      }
    }
  ]
}
```

### --- id=181 ---

输入文本: While earlier it was the turn of Telangana Rashtra Samithi ( TRS ) to participate in protests in support to farmers , on Monday it was the Telugu Desam .

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
      "cause": "in support to farmers",
      "effect": "Telangana Rashtra Samithi ( TRS ) to participate in protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in support to farmers"
      },
      "relation": "caused",
      "effect": {
        "span": "it was the Telugu Desam"
      }
    }
  ]
}
```

### --- id=187 ---

输入文本: Despite assurances by the authorities , the stock of urea is not reaching farmers

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
      "cause": "assurances by the authorities",
      "effect": "the stock of urea is not reaching farmers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "assurances by the authorities"
      },
      "relation": "caused",
      "effect": {
        "span": "the stock of urea is not reaching farmers"
      }
    }
  ]
}
```

### --- id=189 ---

输入文本: The stir intensified when women activists on Tuesday voiced their support for those women set to march towards Shani Shingnapur temple in Maharashtra to break the centuries old tradition of not allowing the feminine gender to enter the sanctum sanctorum .

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
      "cause": "women activists on Tuesday voiced their support for those women set to march towards Shani Shingnapur temple in Maharashtra to break the centuries old tradition of not allowing the feminine gender to enter the sanctum sanctorum",
      "effect": "The stir intensified"
    },
    {
      "cause": "to break the centuries old tradition of not allowing the feminine gender to enter the sanctum sanctorum",
      "effect": "those women set to march towards Shani Shingnapur temple in Maharashtra"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "women activists on Tuesday voiced their support for those women set to march towards Shani Shingnapur temple in Maharashtra to break the centuries old tradition of not allowing the feminine gender to enter the sanctum sanctorum"
      },
      "relation": "caused",
      "effect": {
        "span": "The stir intensified"
      }
    }
  ]
}
```

### --- id=191 ---

输入文本: Following the Shani temple stir , Muslim women too on Thursday staged a protest demanding entry into a restricted area of the Haji Ali dargah .

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
      "cause": "the Shani temple stir",
      "effect": "Muslim women too on Thursday staged a protest demanding entry into a restricted area of the Haji Ali dargah"
    },
    {
      "cause": "demanding entry into a restricted area of the Haji Ali dargah",
      "effect": "Muslim women too on Thursday staged a protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Following the Shani temple stir"
      },
      "relation": "caused",
      "effect": {
        "span": "Muslim women too on Thursday staged a protest demanding entry into a restricted area of the Haji Ali dargah"
      }
    }
  ]
}
```

### --- id=192 ---

输入文本: Two labourers killed , workers stir at BALCO Raipur , june 3 Tension gripped BALCOs Korba plant and work was disrupted after two labourers were killed inside the plant .

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
      "cause": "two labourers were killed inside the plant",
      "effect": "Tension gripped BALCOs Korba plant and work was disrupted"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "two labourers were killed inside the plant"
      },
      "relation": "caused",
      "effect": {
        "span": "Tension gripped BALCOs Korba plant and work was disrupted"
      }
    }
  ]
}
```

### --- id=193 ---

输入文本: Following the incident , the labourers went on a dharna and stopped work .

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
      "cause": "the incident",
      "effect": "the labourers went on a dharna and stopped work"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "the labourers went on a dharna and stopped work"
      }
    }
  ]
}
```

### --- id=196 ---

输入文本: The escalating protests in the JNU follow the arrest of student union president Kanhaiya Kumar on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir .

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
      "cause": "the arrest of student union president Kanhaiya Kumar",
      "effect": "The escalating protests in the JNU"
    },
    {
      "cause": "on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir",
      "effect": "the arrest of student union president Kanhaiya Kumar"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the arrest of student union president Kanhaiya Kumar on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir"
      },
      "relation": "caused",
      "effect": {
        "span": "The escalating protests in the JNU"
      }
    }
  ]
}
```

### --- id=197 ---

输入文本: His arrest has sparked widespread protests by students , teachers as well as opposition parties .

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
      "cause": "His arrest",
      "effect": "widespread protests by students , teachers as well as opposition parties"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "His arrest"
      },
      "relation": "caused",
      "effect": {
        "span": "sparked widespread protests by students , teachers as well as opposition parties"
      }
    }
  ]
}
```

### --- id=202 ---

输入文本: ( PICS AVAILABLE ON www.sapapics.co.za ) A crowd of supporters erupted as Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday to address them .

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
      "cause": "Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday to address them",
      "effect": "A crowd of supporters erupted"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "A crowd of supporters erupted"
      }
    }
  ]
}
```

### --- id=205 ---

输入文本: December 06 , 2017 00:00 IST Urge Central government to drop privatisation move A day after alleged suicide by one of their colleagues , the employees , including officers , went on a mass casual leave on Tuesday to press for their demand to withdraw decision on privatisation of Dredging Corporation of India ( DCI ) .

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
      "cause": "to press for their demand to withdraw decision on privatisation of Dredging Corporation of India ( DCI )",
      "effect": "the employees , including officers , went on a mass casual leave on Tuesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "alleged suicide by one of their colleagues"
      },
      "relation": "caused",
      "effect": {
        "span": "the employees , including officers , went on a mass casual leave on Tuesday"
      }
    },
    {
      "cause": {
        "span": "to press for their demand to withdraw decision on privatisation of Dredging Corporation of India ( DCI )"
      },
      "relation": "caused",
      "effect": {
        "span": "the employees , including officers , went on a mass casual leave on Tuesday"
      }
    }
  ]
}
```

### --- id=206 ---

输入文本: VISAKHAPATNAM DCI employees go on mass casual leave , threaten to intensify stir

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
      "cause": "threaten to intensify stir",
      "effect": "DCI employees go on mass casual leave"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "threaten to intensify stir"
      },
      "relation": "caused",
      "effect": {
        "span": "VISAKHAPATNAM DCI employees go on mass casual leave"
      }
    }
  ]
}
```

### --- id=207 ---

输入文本: The employees also served an ultimatum to the government that unless they shelved the decision on privatisation , they would go ahead with their indefinite strike plan and intensify their ongoing agitation .

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
      "cause": "they shelved the decision on privatisation",
      "effect": "they would go ahead with their indefinite strike plan and intensify their ongoing agitation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "unless they shelved the decision on privatisation"
      },
      "relation": "caused",
      "effect": {
        "span": "they would go ahead with their indefinite strike plan and intensify their ongoing agitation"
      }
    }
  ]
}
```

### --- id=208 ---

输入文本: As hundreds of employees from the city went to Vizianagaram to take part in the last rites of N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI , an all-union meeting convened by the CITU resolved to organise demonstrations in front of all industrial establishments located in the city on Wednesday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to take part in the last rites of N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI",
      "effect": "hundreds of employees from the city went to Vizianagaram"
    },
    {
      "cause": "to protest against the Centre ’ s decision on strategic stake sale of DCI",
      "effect": "N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "N. Venkatesh , 28 , an assistant in the administration department of the corporation ... committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI"
      }
    },
    {
      "cause": {
        "span": "the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "an all-union meeting convened by the CITU resolved to organise demonstrations in front of all industrial establishments located in the city on Wednesday"
      }
    }
  ]
}
```

### --- id=210 ---

输入文本: NATIONAL Rallies mark Nandigram anniversary March 15 , 2008 00:00 IST KOLKATA : Processions and rallies were taken out at Nandigram and here on Friday , first anniversary of the police firing and subsequent violence , which claimed 14 lives in the village in East Midnapore district .

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
      "cause": "first anniversary of the police firing and subsequent violence",
      "effect": "Processions and rallies were taken out at Nandigram and here on Friday"
    },
    {
      "cause": "the police firing and subsequent violence",
      "effect": "which claimed 14 lives in the village in East Midnapore district"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the police firing and subsequent violence"
      },
      "relation": "caused",
      "effect": {
        "span": "claimed 14 lives in the village in East Midnapore district"
      }
    }
  ]
}
```

### --- id=213 ---

输入文本: Cubbon Park Walkers Oppose Government Move 08th January 2014 07:49 AM Members of the Cubbon Park Walkers ’ Association on Tuesday held a candlelight protest against the state government ’ s plan to set up a Cubbon Park Development Authority .

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
      "cause": "against the state government ’ s plan to set up a Cubbon Park Development Authority",
      "effect": "Members of the Cubbon Park Walkers ’ Association on Tuesday held a candlelight protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the state government ’ s plan to set up a Cubbon Park Development Authority"
      },
      "relation": "caused",
      "effect": {
        "span": "Members of the Cubbon Park Walkers ’ Association on Tuesday held a candlelight protest against the state government ’ s plan to set up a Cubbon Park Development Authority"
      }
    }
  ]
}
```

### --- id=215 ---

输入文本: We wo n't tolerate attacks on our drivers , say KZN trucking companies ANA Reporter DURBAN , June 3 ( ANA ) – Trucking companies said on Monday they would not tolerate attacks on their drivers , following the torching of 17 trucks in KwaZulu-Natal at the weekend .

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
      "cause": "the torching of 17 trucks in KwaZulu-Natal at the weekend",
      "effect": "Trucking companies said on Monday they would not tolerate attacks on their drivers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the torching of 17 trucks in KwaZulu-Natal at the weekend"
      },
      "relation": "caused",
      "effect": {
        "span": "Trucking companies said on Monday they would not tolerate attacks on their drivers"
      }
    }
  ]
}
```

### --- id=216 ---

输入文本: Hassan said that over the past three weeks , more than 60 trucks had come under attack and there were `` a lot of injuries '' of drivers .

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
      "cause": "over the past three weeks , more than 60 trucks had come under attack",
      "effect": "there were `` a lot of injuries '' of drivers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "more than 60 trucks had come under attack"
      },
      "relation": "caused",
      "effect": {
        "span": "there were `` a lot of injuries '' of drivers"
      }
    }
  ]
}
```

### --- id=217 ---

输入文本: Local drivers have allegedly been attacking the vehicles and threatening foreign drivers , who they accuse of taking jobs meant for locals .

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
      "cause": "who they accuse of taking jobs meant for locals",
      "effect": "Local drivers have allegedly been attacking the vehicles and threatening foreign drivers"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "taking jobs meant for locals"
      },
      "relation": "caused",
      "effect": {
        "span": "Local drivers have allegedly been attacking the vehicles and threatening foreign drivers"
      }
    }
  ]
}
```

### --- id=218 ---

输入文本: Zikalala said that following stakeholder meetings on Sunday and Monday morning , all parties decided that the police would establish a rapid response team to attend to the attacks .

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
      "cause": "stakeholder meetings on Sunday and Monday morning",
      "effect": "all parties decided that the police would establish a rapid response team to attend to the attacks"
    },
    {
      "cause": "to attend to the attacks",
      "effect": "the police would establish a rapid response team"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "following stakeholder meetings on Sunday and Monday morning"
      },
      "relation": "caused",
      "effect": {
        "span": "all parties decided that the police would establish a rapid response team to attend to the attacks"
      }
    }
  ]
}
```

### --- id=219 ---

输入文本: KERALA Demanding quota Show of strength : A protest rally by the Vaikunta Swamy Dharma Pracharana Sabha ( VSDP ) in front of the Secretariat on Wednesday raising various demands , including 10 per cent reservation .

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
      "cause": "raising various demands , including 10 per cent reservation",
      "effect": "A protest rally by the Vaikunta Swamy Dharma Pracharana Sabha ( VSDP ) in front of the Secretariat on Wednesday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Demanding quota Show of strength"
      },
      "relation": "caused",
      "effect": {
        "span": "A protest rally by the Vaikunta Swamy Dharma Pracharana Sabha ( VSDP ) in front of the Secretariat on Wednesday raising various demands , including 10 per cent reservation"
      }
    },
    {
      "cause": {
        "span": "raising various demands , including 10 per cent reservation"
      },
      "relation": "caused",
      "effect": {
        "span": "A protest rally by the Vaikunta Swamy Dharma Pracharana Sabha ( VSDP ) in front of the Secretariat on Wednesday"
      }
    }
  ]
}
```

### --- id=220 ---

输入文本: Congress Workers Stage ' Rail Roko ' in Maharashtra Against Train Fare Hike 25th June 2014 12:36 PM MUMBAI : Congress workers today staged a ' rail roko ' in various parts of Maharashtra , excluding Mumbai , to protest the train fare hike .

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
      "cause": "to protest the train fare hike",
      "effect": "Congress workers today staged a ' rail roko ' in various parts of Maharashtra , excluding Mumbai"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest the train fare hike"
      },
      "relation": "caused",
      "effect": {
        "span": "Congress workers today staged a ' rail roko ' in various parts of Maharashtra , excluding Mumbai"
      }
    }
  ]
}
```

### --- id=221 ---

输入文本: " We decided to exclude Mumbai , where the ' rail roko ' demonstrations were slated from 11 AM to 12 noon , to avoid inconvenience to suburban commuters , " MPCC spokesperson Sachin Sawant told PTI .

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
      "cause": "to avoid inconvenience to suburban commuters",
      "effect": "We decided to exclude Mumbai , where the ' rail roko ' demonstrations were slated from 11 AM to 12 noon"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to avoid inconvenience to suburban commuters"
      },
      "relation": "caused",
      "effect": {
        "span": "We decided to exclude Mumbai , where the ' rail roko ' demonstrations were slated from 11 AM to 12 noon"
      }
    }
  ]
}
```

### --- id=225 ---

输入文本: 02nd October 2015 03:39 AM RAICHUR : The ongoing agitation against the Centre ’ s decision to set up the state ’ s first IIT at Dharwad took an ugly turn on Thursday after West Police Station PSI Agni allegedly assaulted a lorry driver and brandished his service revolver at the agitators during a protest by the lorry owners ’ association here .

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
      "cause": "West Police Station PSI Agni allegedly assaulted a lorry driver and brandished his service revolver at the agitators during a protest by the lorry owners ’ association here",
      "effect": "The ongoing agitation against the Centre ’ s decision to set up the state ’ s first IIT at Dharwad took an ugly turn on Thursday"
    },
    {
      "cause": "against the Centre ’ s decision to set up the state ’ s first IIT at Dharwad",
      "effect": "The ongoing agitation"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Centre ’ s decision to set up the state ’ s first IIT at Dharwad"
      },
      "relation": "caused",
      "effect": {
        "span": "The ongoing agitation against the Centre ’ s decision to set up the state ’ s first IIT at Dharwad took an ugly turn on Thursday"
      }
    },
    {
      "cause": {
        "span": "West Police Station PSI Agni allegedly assaulted a lorry driver and brandished his service revolver at the agitators during a protest by the lorry owners ’ association here"
      },
      "relation": "caused",
      "effect": {
        "span": "The ongoing agitation against the Centre ’ s decision to set up the state ’ s first IIT at Dharwad took an ugly turn on Thursday"
      }
    }
  ]
}
```

### --- id=226 ---

输入文本: Congress is protesting the recent hike in railway passenger fares and freight rates announced by the Centre .

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
      "cause": "the recent hike in railway passenger fares and freight rates announced by the Centre",
      "effect": "Congress is protesting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the recent hike in railway passenger fares and freight rates announced by the Centre"
      },
      "relation": "caused",
      "effect": {
        "span": "Congress is protesting"
      }
    }
  ]
}
```

### --- id=227 ---

输入文本: The party activists held demonstrations in various parts of the state protesting the fare hike and demanded an immediate rollback in the fares .

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
      "cause": "protesting the fare hike and demanded an immediate rollback in the fares",
      "effect": "The party activists held demonstrations in various parts of the state"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the fare hike"
      },
      "relation": "caused",
      "effect": {
        "span": "The party activists held demonstrations in various parts of the state protesting the fare hike and demanded an immediate rollback in the fares"
      }
    }
  ]
}
```

### --- id=229 ---

输入文本: Violence first broke out in the hill district on September 26 when three auto-rickshaw drivers , all belonging to the Dimasa tribe , were killed .

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
      "cause": "three auto-rickshaw drivers , all belonging to the Dimasa tribe , were killed",
      "effect": "Violence first broke out in the hill district on September 26"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "three auto-rickshaw drivers , all belonging to the Dimasa tribe , were killed"
      },
      "relation": "caused",
      "effect": {
        "span": "Violence first broke out in the hill district on September 26"
      }
    }
  ]
}
```

### --- id=230 ---

输入文本: TIRUCHI : Residents raise black flag atop their houses May 06 , 2016 00:00 IST Residents of Quaide Milleth Nagar near Ariyamangalam on Thursday hoisted black flags atop their houses demanding basic amenities and threatened to boycott the Assembly election if their demands were not conceded .

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
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "demanding basic amenities",
      "effect": "Residents of Quaide Milleth Nagar near Ariyamangalam on Thursday hoisted black flags atop their houses"
    },
    {
      "cause": "their demands were not conceded",
      "effect": "threatened to boycott the Assembly election"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding basic amenities"
      },
      "relation": "caused",
      "effect": {
        "span": "Residents of Quaide Milleth Nagar near Ariyamangalam on Thursday hoisted black flags atop their houses"
      }
    },
    {
      "cause": {
        "span": "their demands were not conceded"
      },
      "relation": "caused",
      "effect": {
        "span": "threatened to boycott the Assembly election"
      }
    }
  ]
}
```

### --- id=232 ---

输入文本: `` Talks are underway to solve the wage dispute and to end the strike , '' she said .

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
      "cause": "to solve the wage dispute and to end the strike",
      "effect": "Talks are underway"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the wage dispute"
      },
      "relation": "caused",
      "effect": {
        "span": "Talks are underway to solve the wage dispute and to end the strike"
      }
    }
  ]
}
```

### --- id=235 ---

输入文本: `` We call upon the Muslim community to put the striking workers and all the poor people battling against capitalist greed in their prayers and to use this glorious month of Ramadan to re-commit themselves to the struggle for socio-economic justice , equity and freedom for all , '' the organisation said .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to put the striking workers and all the poor people battling against capitalist greed in their prayers and to use this glorious month of Ramadan to re-commit themselves to the struggle for socio-economic justice , equity and freedom for all",
      "effect": "We call upon the Muslim community"
    },
    {
      "cause": "against capitalist greed",
      "effect": "the striking workers and all the poor people battling"
    },
    {
      "cause": "to re-commit themselves to the struggle for socio-economic justice , equity and freedom",
      "effect": "use this glorious month of Ramadan"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to use this glorious month of Ramadan to re-commit themselves to the struggle for socio-economic justice , equity and freedom for all"
      },
      "relation": "caused",
      "effect": {
        "span": "We call upon the Muslim community to put the striking workers and all the poor people battling against capitalist greed in their prayers"
      }
    }
  ]
}
```

### --- id=237 ---

输入文本: The lorry owners ’ association was staging a protest by blocking the road near Ambedkar Circle .

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
      "cause": "blocking the road near Ambedkar Circle",
      "effect": "The lorry owners ’ association was staging a protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "staging a protest"
      },
      "relation": "caused",
      "effect": {
        "span": "blocking the road near Ambedkar Circle"
      }
    }
  ]
}
```

### --- id=240 ---

输入文本: Lee said her hunger strike would continue until the government instituted a stronger official response to Occupy Central and recent “ radical ” protests at Legco .

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "the government instituted a stronger official response to Occupy Central and recent “ radical ” protests at Legco",
      "effect": "her hunger strike would continue"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the government instituted a stronger official response to Occupy Central and recent “ radical ” protests at Legco"
      },
      "relation": "caused",
      "effect": {
        "span": "Lee said her hunger strike would continue until the government instituted a stronger official response to Occupy Central and recent “ radical ” protests at Legco"
      }
    }
  ]
}
```

### --- id=241 ---

输入文本: Fri 27 Fire Walking A 59 - year-old “ barefoot doctor ” is sentenced to four months in jail for attempted arson .

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
      "cause": "attempted arson",
      "effect": "Fri 27 Fire Walking A 59 - year-old “ barefoot doctor ” is sentenced to four months in jail"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "attempted arson"
      },
      "relation": "caused",
      "effect": {
        "span": "A 59 - year-old “ barefoot doctor ” is sentenced to four months in jail"
      }
    }
  ]
}
```

### --- id=243 ---

输入文本: 2 held over poisoning threat to Tung PUBLISHED : Wednesday , 03 October , 2001 , 12:00am Donald Tsang Donald Tsang A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials were arrested in Central yesterday .

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
      "cause": "A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials",
      "effect": "were arrested in Central yesterday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials"
      },
      "relation": "caused",
      "effect": {
        "span": "A couple ... were arrested in Central yesterday"
      }
    }
  ]
}
```

### --- id=246 ---

输入文本: Spokesman Keith Khoza said they had decided to March to Prime Media because the cartoon had raised various concerns .

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
      "cause": "the cartoon had raised various concerns",
      "effect": "they had decided to March to Prime Media"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the cartoon had raised various concerns"
      },
      "relation": "caused",
      "effect": {
        "span": "they had decided to March to Prime Media"
      }
    }
  ]
}
```

### --- id=247 ---

输入文本: He was inaugurating the dharna held in front of the Secretariat , ahead of the general strike called for February 28 , demanding to reject the PFRDA Bill .

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
      "cause": "demanding to reject the PFRDA Bill",
      "effect": "He was inaugurating the dharna held in front of the Secretariat , ahead of the general strike called for February 28"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding to reject the PFRDA Bill"
      },
      "relation": "caused",
      "effect": {
        "span": "He was inaugurating the dharna held in front of the Secretariat , ahead of the general strike called for February 28"
      }
    }
  ]
}
```

### --- id=250 ---

输入文本: Maoists blow up panchayat office , godown - Indian Express Agencies , Agencies : Malkangiri ( Orissa ) , Sun May 30 2010 , 13:37 hrs Maoists blew up a panchayat office building and a godown in 's Malkangiri district early on Sunday in an apparent bid to prevent security personnel from camping there .

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
      "cause": "to prevent security personnel from camping there",
      "effect": "Maoists blew up a panchayat office building and a godown in 's Malkangiri district early on Sunday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in an apparent bid to prevent security personnel from camping there"
      },
      "relation": "caused",
      "effect": {
        "span": "Maoists blew up a panchayat office building and a godown in 's Malkangiri district early on Sunday"
      }
    }
  ]
}
```

### --- id=251 ---

输入文本: The police said that around 50 armed ultras raided Kangurukunda village at Kalimela , about 40 km from here , early on Sunday and set off an explosion , destrying the panchayat office .

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
      "cause": "around 50 armed ultras raided Kangurukunda village at Kalimela , about 40 km from here , early on Sunday and set off an explosion",
      "effect": "destrying the panchayat office"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "around 50 armed ultras raided Kangurukunda village at Kalimela , about 40 km from here , early on Sunday and set off an explosion"
      },
      "relation": "caused",
      "effect": {
        "span": "destrying the panchayat office"
      }
    }
  ]
}
```

### --- id=253 ---

输入文本: The two structures were targeted by the ultras because they believed they could serve as temporary camps for sheltering security personnel deployed in the area .

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
      "cause": "they believed they could serve as temporary camps for sheltering security personnel deployed in the area",
      "effect": "The two structures were targeted by the ultras"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they believed they could serve as temporary camps for sheltering security personnel deployed in the area"
      },
      "relation": "caused",
      "effect": {
        "span": "The two structures were targeted by the ultras"
      }
    }
  ]
}
```

### --- id=256 ---

输入文本: Kasimedu Fishermen Keep Up Strike 18th January 2016 04:09 AM CHENNAI : Monday would mark the fifth day of strike by Kasimedu fishermen , who are protesting against the use of high-powered engines by Andhra fishermen .

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
      "cause": "against the use of high-powered engines by Andhra fishermen",
      "effect": "Kasimedu fishermen , who are protesting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "protesting against the use of high-powered engines by Andhra fishermen"
      },
      "relation": "caused",
      "effect": {
        "span": "Kasimedu Fishermen Keep Up Strike"
      }
    }
  ]
}
```

### --- id=257 ---

输入文本: As many as 6,000 fishing boats , including mechanised boats and fibre boats from the region had stopped venturing into the sea from January 13 due to which the inflow of fish into the city ’ s market decreased .

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
      "cause": "As many as 6,000 fishing boats , including mechanised boats and fibre boats from the region had stopped venturing into the sea from January 13",
      "effect": "the inflow of fish into the city ’ s market decreased"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "As many as 6,000 fishing boats , including mechanised boats and fibre boats from the region had stopped venturing into the sea from January 13"
      },
      "relation": "caused",
      "effect": {
        "span": "the inflow of fish into the city ’ s market decreased"
      }
    }
  ]
}
```

### --- id=258 ---

输入文本: Blockade against power plant 13th September 2011 08:19 AM ANGUL : They made their intention loud and clear raising slogans against JR Power Plant .

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
      "cause": "They made their intention loud and clear",
      "effect": "raising slogans against JR Power Plant"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "raising slogans against JR Power Plant"
      },
      "relation": "caused",
      "effect": {
        "span": "They made their intention loud and clear"
      }
    }
  ]
}
```

### --- id=259 ---

输入文本: On Tuesday night tens of thousands of demonstrators packed the city ’ s downtown area for a third night as protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight .

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
      "cause": "protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight",
      "effect": "On Tuesday night tens of thousands of demonstrators packed the city ’ s downtown area for a third night"
    },
    {
      "cause": "Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight",
      "effect": "they would step up their actions"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight"
      },
      "relation": "caused",
      "effect": {
        "span": "tens of thousands of demonstrators packed the city ’ s downtown area for a third night"
      }
    }
  ]
}
```

### --- id=260 ---

输入文本: Hundreds of locals on Monday blocked NH 55 for six hours demanding scraping of the MoU .

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
      "cause": "demanding scraping of the MoU",
      "effect": "Hundreds of locals on Monday blocked NH 55 for six hours"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding scraping of the MoU"
      },
      "relation": "caused",
      "effect": {
        "span": "Hundreds of locals on Monday blocked NH 55 for six hours"
      }
    }
  ]
}
```

### --- id=261 ---

输入文本: The slogan , “ We want Sureswari irrigation project not JR Power Plant ” rented the air even as vehicular traffic came to a standstill from 6 am till noon following the blockade by people of Kishorenagar area .

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
      "cause": "the blockade by people of Kishorenagar area",
      "effect": "The slogan , “ We want Sureswari irrigation project not JR Power Plant ” rented the air even as vehicular traffic came to a standstill from 6 am till noon"
    },
    {
      "cause": "vehicular traffic came to a standstill from 6 am till noon",
      "effect": "The slogan , “ We want Sureswari irrigation project not JR Power Plant ” rented the air"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the blockade by people of Kishorenagar area"
      },
      "relation": "caused",
      "effect": {
        "span": "vehicular traffic came to a standstill from 6 am till noon"
      }
    }
  ]
}
```

### --- id=263 ---

输入文本: The protestors accused the Government of reneging on its commitment when the Chief Minister had himself announced , during an election rally , allocation of funds for the proposed Sureswari irrigation project here .

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
      "cause": "the Chief Minister had himself announced , during an election rally , allocation of funds for the proposed Sureswari irrigation project here",
      "effect": "The protestors accused the Government of reneging on its commitment"
    },
    {
      "cause": "the proposed Sureswari irrigation project here",
      "effect": "allocation of funds"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Government of reneging on its commitment when the Chief Minister had himself announced , during an election rally , allocation of funds for the proposed Sureswari irrigation project here"
      },
      "relation": "caused",
      "effect": {
        "span": "The protestors accused"
      }
    }
  ]
}
```

### --- id=267 ---

输入文本: September 14 , 2012 00:00 IST Her absence from Vijayamma ’ s protest meet gives credence to rumours Rumour mills are abuzz in Warangal hinting that YSR Congress party leader and former Minister Konda Surekha may join the Congress soon .

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
    "tp": 1,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 1
  },
  "gold_relations": [
    {
      "cause": "Her absence from Vijayamma ’ s protest meet",
      "effect": "rumours"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Her absence from Vijayamma ’ s protest meet"
      },
      "relation": "caused",
      "effect": {
        "span": "gives credence to rumours"
      }
    }
  ]
}
```

### --- id=273 ---

输入文本: Then on Thursday , some pupils returned to classes after having spent months out of school as residents protested against the Municipal Demarcation Board 's decision to include their areas under a new municipality .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "residents protested against the Municipal Demarcation Board 's decision to include their areas under a new municipality",
      "effect": "having spent months out of school"
    },
    {
      "cause": "against the Municipal Demarcation Board 's decision to include their areas under a new municipality",
      "effect": "residents protested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "residents protested against the Municipal Demarcation Board 's decision to include their areas under a new municipality"
      },
      "relation": "caused",
      "effect": {
        "span": "some pupils ... spent months out of school"
      }
    },
    {
      "cause": {
        "span": "the Municipal Demarcation Board 's decision to include their areas under a new municipality"
      },
      "relation": "caused",
      "effect": {
        "span": "residents protested against the Municipal Demarcation Board 's decision to include their areas under a new municipality"
      }
    }
  ]
}
```

### --- id=274 ---

输入文本: Accusing the United Progressive Alliance ( UPA ) government of adopting a confrontationist attitude towards the states , he said it has been demolishing the constitutional institutions whereas the need of the hour is a cooperative attitude .

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
      "cause": "he said it has been demolishing the constitutional institutions whereas the need of the hour is a cooperative attitude",
      "effect": "Accusing the United Progressive Alliance ( UPA ) government of adopting a confrontationist attitude towards the states"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the United Progressive Alliance ( UPA ) government ... adopting a confrontationist attitude towards the states"
      },
      "relation": "caused",
      "effect": {
        "span": "he said it has been demolishing the constitutional institutions whereas the need of the hour is a cooperative attitude"
      }
    }
  ]
}
```

### --- id=276 ---

输入文本: Trump faced a backlash in March when he referred to the 1989 Tiananmen Square protests as a “ riot ” .

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
      "cause": "he referred to the 1989 Tiananmen Square protests as a “ riot ”",
      "effect": "Trump faced a backlash in March"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he referred to the 1989 Tiananmen Square protests as a “ riot ”"
      },
      "relation": "caused",
      "effect": {
        "span": "Trump faced a backlash in March"
      }
    }
  ]
}
```

### --- id=277 ---

输入文本: If it does , when you ’ re confronting an enemy that beheads people and wants to put nuclear bombs in our subways , then waterboarding is well within the rules. ”

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
      "cause": "you ’ re confronting an enemy that beheads people and wants to put nuclear bombs in our subways",
      "effect": "waterboarding is well within the rules"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "confronting an enemy that beheads people and wants to put nuclear bombs in our subways"
      },
      "relation": "caused",
      "effect": {
        "span": "waterboarding is well within the rules"
      }
    }
  ]
}
```

### --- id=278 ---

输入文本: Protesting the unethical ban , hundreds of Bengal traders launched an agitation on Monday and threatened to intensify it , if the matter is not resolved soon .

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
      "cause": "Protesting the unethical ban",
      "effect": "hundreds of Bengal traders launched an agitation on Monday and threatened to intensify it , if the matter is not resolved soon"
    },
    {
      "cause": "the matter is not resolved soon",
      "effect": "threatened to intensify it"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Protesting the unethical ban"
      },
      "relation": "caused",
      "effect": {
        "span": "hundreds of Bengal traders launched an agitation on Monday and threatened to intensify it , if the matter is not resolved soon ."
      }
    }
  ]
}
```

### --- id=279 ---

输入文本: The neighbouring State apparently relented after 500 trucks carrying vegetables , eggs , fishes and other perishable items from Andhra Pradesh were detained by BJD activists at various places in Balasore .

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
      "cause": "500 trucks carrying vegetables , eggs , fishes and other perishable items from Andhra Pradesh were detained by BJD activists at various places in Balasore",
      "effect": "The neighbouring State apparently relented"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "500 trucks carrying vegetables , eggs , fishes and other perishable items from Andhra Pradesh were detained by BJD activists at various places in Balasore"
      },
      "relation": "caused",
      "effect": {
        "span": "The neighbouring State apparently relented"
      }
    }
  ]
}
```

### --- id=282 ---

输入文本: The strike began on September 9 , with Numsa demanding a double-digit percentage increase .

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
      "cause": "with Numsa demanding a double-digit percentage increase",
      "effect": "The strike began on September 9"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding a double-digit percentage increase"
      },
      "relation": "caused",
      "effect": {
        "span": "The strike began on September 9"
      }
    }
  ]
}
```

### --- id=285 ---

输入文本: Police opened fire , killing 34 striking workers and wounding 78 while trying to disperse a group gathered on a hill near Lonmin 's platinum mine in Marikana on August 16 .

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
      "cause": "trying to disperse a group gathered on a hill near Lonmin 's platinum mine in Marikana on August 16",
      "effect": "Police opened fire"
    },
    {
      "cause": "Police opened fire",
      "effect": "killing 34 striking workers and wounding 78"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Police opened fire"
      },
      "relation": "caused",
      "effect": {
        "span": "killing 34 striking workers and wounding 78"
      }
    }
  ]
}
```

### --- id=286 ---

输入文本: Authorities yesterday said they would scrap the 10.4 billion yuan ( HK $ 12.7 billion ) project , the subject of demonstrations by tens of thousands of Shifang residents .

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
      "cause": "the subject of demonstrations by tens of thousands of Shifang residents",
      "effect": "they would scrap the 10.4 billion yuan ( HK $ 12.7 billion ) project"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demonstrations by tens of thousands of Shifang residents"
      },
      "relation": "caused",
      "effect": {
        "span": "Authorities yesterday said they would scrap the 10.4 billion yuan ( HK $ 12.7 billion ) project"
      }
    }
  ]
}
```

### --- id=287 ---

输入文本: ' Once the damage is done , it is long-lasting and not remediable . ' The massive three-day protest this week was the latest in a series of grass-roots demonstrations over polluting projects , as mainlanders have gained awareness in recent years of environmental and health concerns associated with pollution .

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
      "cause": "mainlanders have gained awareness in recent years of environmental and health concerns associated with pollution",
      "effect": "The massive three-day protest this week was the latest in a series of grass-roots demonstrations over polluting projects"
    },
    {
      "cause": "polluting projects",
      "effect": "a series of grass-roots demonstrations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "polluting projects"
      },
      "relation": "caused",
      "effect": {
        "span": "The massive three-day protest this week was the latest in a series of grass-roots demonstrations"
      }
    },
    {
      "cause": {
        "span": "mainlanders have gained awareness in recent years of environmental and health concerns associated with pollution"
      },
      "relation": "caused",
      "effect": {
        "span": "The massive three-day protest this week was the latest in a series of grass-roots demonstrations"
      }
    }
  ]
}
```

### --- id=288 ---

输入文本: Last summer , tens of thousands of people in the northeastern city of Dalian , Liaoning , marched to demand the relocation of a chemical plant .

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
      "cause": "to demand the relocation of a chemical plant",
      "effect": "Last summer , tens of thousands of people in the northeastern city of Dalian , Liaoning , marched"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to demand the relocation of a chemical plant"
      },
      "relation": "caused",
      "effect": {
        "span": "tens of thousands of people in the northeastern city of Dalian , Liaoning , marched"
      }
    }
  ]
}
```

### --- id=289 ---

输入文本: And in June 2007 , over 20,000 people rallied in Xiamen , a coastal city in Fujian province , to protest against plans to built a paraxylene chemical plant in the city .

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
      "cause": "to protest",
      "effect": "over 20,000 people rallied in Xiamen , a coastal city in Fujian province"
    },
    {
      "cause": "against plans to built a paraxylene chemical plant in the city",
      "effect": "to protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "plans to built a paraxylene chemical plant in the city"
      },
      "relation": "caused",
      "effect": {
        "span": "over 20,000 people rallied in Xiamen , a coastal city in Fujian province , to protest against plans to built a paraxylene chemical plant in the city"
      }
    }
  ]
}
```

### --- id=290 ---

输入文本: Following the Xiamen incident , the ' not in my backyard ' mentality sparked similar protests in several mainland cities , including Dalian , Guangzhou and Shantou .

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
      "cause": "the Xiamen incident",
      "effect": "the ' not in my backyard ' mentality"
    },
    {
      "cause": "the ' not in my backyard ' mentality",
      "effect": "similar protests in several mainland cities , including Dalian , Guangzhou and Shantou"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Xiamen incident"
      },
      "relation": "caused",
      "effect": {
        "span": "the ' not in my backyard ' mentality sparked similar protests in several mainland cities , including Dalian , Guangzhou and Shantou"
      }
    },
    {
      "cause": {
        "span": "the ' not in my backyard ' mentality"
      },
      "relation": "caused",
      "effect": {
        "span": "sparked similar protests in several mainland cities , including Dalian , Guangzhou and Shantou"
      }
    }
  ]
}
```

### --- id=291 ---

输入文本: Analysts say the mainland public has taken to such protests because they lack adequate channels to express their concerns about environmental risks posed by massive industrial projects .

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
      "cause": "they lack adequate channels to express their concerns about environmental risks posed by massive industrial projects",
      "effect": "the mainland public has taken to such protests"
    },
    {
      "cause": "massive industrial projects",
      "effect": "environmental risks"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they lack adequate channels to express their concerns about environmental risks posed by massive industrial projects"
      },
      "relation": "caused",
      "effect": {
        "span": "the mainland public has taken to such protests"
      }
    }
  ]
}
```

### --- id=292 ---

输入文本: Ma Jun , director of the Institute of Public and Environmental Affairs in Beijing , said the Shifang protests came as a last resort for local residents to make their voices heard , as ' all other channels for public participation were ineffective ' .

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
      "cause": "' all other channels for public participation were ineffective '",
      "effect": "the Shifang protests came as a last resort for local residents to make their voices heard"
    },
    {
      "cause": "to make their voices heard",
      "effect": "the Shifang protests came as a last resort for local residents"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "all other channels for public participation were ineffective"
      },
      "relation": "caused",
      "effect": {
        "span": "the Shifang protests came as a last resort for local residents to make their voices heard"
      }
    }
  ]
}
```

### --- id=293 ---

输入文本: SRINAGAR : One killed , 100 injured in Valley September 01 , 2016 00:00 IST As curfew was lifted from all 10 districts , violence singed the Kashmir Valley on Wednesday , leaving a civilian dead and over 100 injured .

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
      "cause": "curfew was lifted from all 10 districts",
      "effect": "violence singed the Kashmir Valley on Wednesday , leaving a civilian dead and over 100 injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "violence singed the Kashmir Valley on Wednesday"
      },
      "relation": "caused",
      "effect": {
        "span": "leaving a civilian dead and over 100 injured"
      }
    }
  ]
}
```

### --- id=296 ---

输入文本: The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma to probe into the violence and the deaths of 44 people in wage-related protests .

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
      "cause": "to probe into the violence and the deaths of 44 people in wage-related protests",
      "effect": "The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma"
    },
    {
      "cause": "wage-related protests",
      "effect": "the violence and the deaths of 44 people"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the violence and the deaths of 44 people in wage-related protests"
      },
      "relation": "caused",
      "effect": {
        "span": "The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma to probe into"
      }
    }
  ]
}
```

### --- id=298 ---

输入文本: But the locals said clashes between the residents and the Army started in the morning when the latter stopped the movement of fruit trucks in Rafiabad and Sopore , asking the drivers to ply only during the shutdown period .

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
      "cause": "the latter stopped the movement of fruit trucks in Rafiabad and Sopore",
      "effect": "clashes between the residents and the Army started in the morning"
    },
    {
      "cause": "asking the drivers to ply only during the shutdown period",
      "effect": "the latter stopped the movement of fruit trucks in Rafiabad and Sopore"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the latter stopped the movement of fruit trucks in Rafiabad and Sopore , asking the drivers to ply only during the shutdown period"
      },
      "relation": "caused",
      "effect": {
        "span": "clashes between the residents and the Army started in the morning"
      }
    }
  ]
}
```

### --- id=301 ---

输入文本: The action helped launch a 79-day street occupation that was described as the greatest challenge to China ’ s Communist rulers since the 1989 Tiananmen protests .

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
      "cause": "The action",
      "effect": "a 79-day street occupation that was described as the greatest challenge to China ’ s Communist rulers since the 1989 Tiananmen protests"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The action"
      },
      "relation": "caused",
      "effect": {
        "span": "helped launch a 79-day street occupation that was described as the greatest challenge to China ’ s Communist rulers since the 1989 Tiananmen protests ."
      }
    }
  ]
}
```

### --- id=302 ---

输入文本: More violence in TN district Posted : Wed Jun 25 1997 IST RAJAPALAYAM , June 23 : In continuing violence in TN 's Kamarajar district , one person was stabbed and buses being attacked .

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
      "cause": "In continuing violence in TN 's Kamarajar district",
      "effect": "one person was stabbed and buses being attacked"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "continuing violence in TN 's Kamarajar district"
      },
      "relation": "caused",
      "effect": {
        "span": "one person was stabbed and buses being attacked"
      }
    }
  ]
}
```

### --- id=307 ---

输入文本: Lt-Col Andre Traut said the teenager laid the complaint at the Robertson police station following a farmworkers ' protest in the area .

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
      "cause": "a farmworkers ' protest in the area",
      "effect": "the teenager laid the complaint at the Robertson police station"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a farmworkers ' protest in the area"
      },
      "relation": "caused",
      "effect": {
        "span": "the teenager laid the complaint at the Robertson police station"
      }
    }
  ]
}
```

### --- id=308 ---

输入文本: Some police personnel intervened and urged them to give up their protest - but to no avail .

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
      "cause": "Some police personnel intervened",
      "effect": "urged them to give up their protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "urged them to give up their protest"
      },
      "relation": "caused",
      "effect": {
        "span": "to no avail"
      }
    }
  ]
}
```

### --- id=309 ---

输入文本: They poured out their woes to the reporters and photographers who reached the Police Stadium on hearing about the incident .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "hearing about the incident",
      "effect": "They poured out their woes to the reporters and photographers who reached the Police Stadium"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "hearing about the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "the reporters and photographers ... reached the Police Stadium"
      }
    },
    {
      "cause": {
        "span": "They poured out their woes to the reporters and photographers who reached the Police Stadium on hearing about the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "the reporters and photographers ... reached the Police Stadium"
      }
    }
  ]
}
```

### --- id=310 ---

输入文本: Maoist Kill Local Leader in Odisha 30th December 2013 01:37 PM Suspecting him to be a police informer , Maoists have killed a local leader in Kosa

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
      "cause": "Suspecting him to be a police informer",
      "effect": "Maoists have killed a local leader"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Suspecting him to be a police informer"
      },
      "relation": "caused",
      "effect": {
        "span": "Maoists have killed a local leader in Kosa"
      }
    }
  ]
}
```

### --- id=311 ---

输入文本: Madhi ( 38 ) of Sangel village under Kalimela police station , secretary of local Panipanchyat , was kidnapped by the ultras on Friday when they triggered a blast with explosives and destroyed the bridge over river Poteru apparently to stop movement of security personnel between Kalimela and Padia .

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
    "tp": 0,
    "fp": 2,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "apparently to stop movement of security personnel between Kalimela and Padia",
      "effect": "they triggered a blast with explosives and destroyed the bridge over river Poteru"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "they triggered a blast with explosives"
      },
      "relation": "caused",
      "effect": {
        "span": "destroyed the bridge over river Poteru"
      }
    },
    {
      "cause": {
        "span": "to stop movement of security personnel between Kalimela and Padia"
      },
      "relation": "caused",
      "effect": {
        "span": "they triggered a blast with explosives and destroyed the bridge over river Poteru"
      }
    }
  ]
}
```

### --- id=312 ---

输入文本: Madhi was produced before the ' Kangaroo Court ' and killed by the ultra for acting as a police informer , villagers alleged .

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
      "cause": "acting as a police informer",
      "effect": "Madhi was produced before the ' Kangaroo Court ' and killed by the ultra"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "acting as a police informer"
      },
      "relation": "caused",
      "effect": {
        "span": "Madhi was produced before the ' Kangaroo Court ' and killed by the ultra"
      }
    }
  ]
}
```

### --- id=315 ---

输入文本: Meanwhile , the four-day bandh call given by Maoists in Malkangiri and adjoining Koraput district demanding halt to police action and alleged atrocity against tribals had entered the third today affecting normal life in Maoist hinterlands including Padia , Kalimela and Motu areas .

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
      "cause": "demanding halt to police action and alleged atrocity against tribals",
      "effect": "the four-day bandh call given by Maoists in Malkangiri and adjoining Koraput district"
    },
    {
      "cause": "the four-day bandh call given by Maoists in Malkangiri and adjoining Koraput district demanding halt to police action and alleged atrocity against tribals had entered the third today",
      "effect": "affecting normal life in Maoist hinterlands including Padia , Kalimela and Motu areas"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the four-day bandh call given by Maoists in Malkangiri and adjoining Koraput district demanding halt to police action and alleged atrocity against tribals"
      },
      "relation": "caused",
      "effect": {
        "span": "affecting normal life in Maoist hinterlands including Padia , Kalimela and Motu areas"
      }
    }
  ]
}
```

### --- id=317 ---

输入文本: Hassan : Residents protest delay in improving road September 25 , 2013 00:00 IST Residents of Belur on Monday protested the delay in repairing the main road in the town by planting banana saplings in the middle of the road .

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
      "cause": "the delay in repairing the main road in the town",
      "effect": "Residents of Belur on Monday protested"
    },
    {
      "cause": "Residents of Belur on Monday protested the delay in repairing the main road in the town",
      "effect": "planting banana saplings in the middle of the road"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the delay in repairing the main road in the town"
      },
      "relation": "caused",
      "effect": {
        "span": "Residents of Belur on Monday protested ... by planting banana saplings in the middle of the road"
      }
    }
  ]
}
```

### --- id=318 ---

输入文本: The protesters planted the saplings in potholes to draw the attention of the officials to the poor condition of the road .

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
      "cause": "to draw the attention of the officials to the poor condition of the road",
      "effect": "The protesters planted the saplings in potholes"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to draw the attention of the officials to the poor condition of the road"
      },
      "relation": "caused",
      "effect": {
        "span": "The protesters planted the saplings in potholes"
      }
    }
  ]
}
```

### --- id=320 ---

输入文本: Earlier , the protesters , led by workers of Jaya Karnataka Vedike , took out a procession and stopped the movement of vehicles for half an hour .

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
      "cause": "Earlier , the protesters , led by workers of Jaya Karnataka Vedike , took out a procession",
      "effect": "stopped the movement of vehicles for half an hour"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the protesters , led by workers of Jaya Karnataka Vedike , took out a procession"
      },
      "relation": "caused",
      "effect": {
        "span": "stopped the movement of vehicles for half an hour"
      }
    }
  ]
}
```

### --- id=321 ---

输入文本: Sporadic violence during hartal 20th May 2009 10:23 AM THIRUVANANTHAPURAM : Sporadic violence marked the hartal on Tuesday called by Muslim organisations in protest against the police action in Cheriyathura-Beemappally areas on Sunday .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "protest",
      "effect": "Sporadic violence marked the hartal on Tuesday called by Muslim organisations"
    },
    {
      "cause": "against the police action in Cheriyathura-Beemappally areas on Sunday",
      "effect": "protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in protest against the police action in Cheriyathura-Beemappally areas on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "the hartal on Tuesday called by Muslim organisations"
      }
    },
    {
      "cause": {
        "span": "the hartal on Tuesday called by Muslim organisations in protest against the police action in Cheriyathura-Beemappally areas on Sunday"
      },
      "relation": "caused",
      "effect": {
        "span": "Sporadic violence marked the hartal on Tuesday"
      }
    }
  ]
}
```

### --- id=323 ---

输入文本: Two bus drivers were hurt in the attacks .

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
      "cause": "the attacks",
      "effect": "Two bus drivers were hurt"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the attacks"
      },
      "relation": "caused",
      "effect": {
        "span": "Two bus drivers were hurt"
      }
    }
  ]
}
```

### --- id=324 ---

输入文本: Hartal supporters pelted stones at a KSRTC bus at Karamana injuring driver Babu .

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
      "cause": "Hartal supporters pelted stones at a KSRTC bus at Karamana",
      "effect": "injuring driver Babu"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Hartal supporters pelted stones at a KSRTC bus at Karamana"
      },
      "relation": "caused",
      "effect": {
        "span": "injuring driver Babu"
      }
    }
  ]
}
```

### --- id=326 ---

输入文本: Hartal supporters surrounded a police station at Attakkulangara demanding that four men arrested by police for pelting stones at KSRTC buses be freed .

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
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "demanding that four men arrested by police for pelting stones at KSRTC buses be freed",
      "effect": "Hartal supporters surrounded a police station at Attakkulangara"
    },
    {
      "cause": "pelting stones at KSRTC buses",
      "effect": "four men arrested by police"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding that four men arrested by police for pelting stones at KSRTC buses be freed"
      },
      "relation": "caused",
      "effect": {
        "span": "Hartal supporters surrounded a police station at Attakkulangara"
      }
    },
    {
      "cause": {
        "span": "pelting stones at KSRTC buses"
      },
      "relation": "caused",
      "effect": {
        "span": "four men arrested by police"
      }
    }
  ]
}
```

### --- id=329 ---

输入文本: However , local people and the shopkeepers joined forces and pelted stones at the hartal supporters forcing them to flee .

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
      "cause": "local people and the shopkeepers joined forces and pelted stones at the hartal supporters",
      "effect": "forcing them to flee"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "local people and the shopkeepers joined forces and pelted stones at the hartal supporters"
      },
      "relation": "caused",
      "effect": {
        "span": "forcing them to flee"
      }
    }
  ]
}
```

### --- id=330 ---

输入文本: The protests spread to 15 other towns and resulted in two deaths and the destruction of property .

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
      "cause": "The protests spread to 15 other towns",
      "effect": "two deaths and the destruction of property"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The protests"
      },
      "relation": "caused",
      "effect": {
        "span": "resulted in two deaths and the destruction of property"
      }
    }
  ]
}
```

### --- id=331 ---

输入文本: He was seen as proactive when he disposed of the mercy petitions of 26/11 attack convict Ajmal Kasab and Parliament attack convict Afzal Guru that had triggered a controversy but his aides explain that as President he had no choice but to go by the Cabinet advice .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "he disposed of the mercy petitions of 26/11 attack convict Ajmal Kasab and Parliament attack convict Afzal Guru",
      "effect": "He was seen as proactive"
    },
    {
      "cause": "the mercy petitions of 26/11 attack convict Ajmal Kasab and Parliament attack convict Afzal Guru",
      "effect": "a controversy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the mercy petitions of 26/11 attack convict Ajmal Kasab and Parliament attack convict Afzal Guru"
      },
      "relation": "caused",
      "effect": {
        "span": "triggered a controversy"
      }
    },
    {
      "cause": {
        "span": "the Cabinet advice"
      },
      "relation": "caused",
      "effect": {
        "span": "he had no choice but to go by the Cabinet advice"
      }
    }
  ]
}
```

### --- id=332 ---

输入文本: During the turbulent period last year-end in the capital , the demonstrations against the rape and murder of a 23 - year-old paramedical student reached the gates of Rashtrapati Bhavan seeking his intervention .

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
      "cause": "seeking his intervention",
      "effect": "the demonstrations against the rape and murder of a 23 - year-old paramedical student reached the gates of Rashtrapati Bhavan"
    },
    {
      "cause": "against the rape and murder of a 23 - year-old paramedical student",
      "effect": "the demonstrations"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the rape and murder of a 23 - year-old paramedical student"
      },
      "relation": "caused",
      "effect": {
        "span": "the demonstrations against the rape and murder of a 23 - year-old paramedical student reached the gates of Rashtrapati Bhavan seeking his intervention"
      }
    }
  ]
}
```

### --- id=335 ---

输入文本: The controversy sparked off after the Kerala State Road Transport Employees Association ( KSRTEA ) pasted stickers on KSRTC buses seeking public intervention against ‘ police-goonda ’ attack on employees .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "the Kerala State Road Transport Employees Association ( KSRTEA ) pasted stickers on KSRTC buses",
      "effect": "The controversy"
    },
    {
      "cause": "seeking public intervention",
      "effect": "the Kerala State Road Transport Employees Association ( KSRTEA ) pasted stickers on KSRTC buses"
    },
    {
      "cause": "against ‘ police-goonda ’ attack on employees",
      "effect": "public intervention"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the Kerala State Road Transport Employees Association ( KSRTEA ) pasted stickers on KSRTC buses seeking public intervention against ‘ police-goonda ’ attack on employees"
      },
      "relation": "caused",
      "effect": {
        "span": "The controversy sparked off"
      }
    }
  ]
}
```

### --- id=338 ---

输入文本: KERALA Brewing protest Members of the Kerala Mahila Sangham , the State unit of the National Federation of Indian Women , protest against the hike in cooking gas price , in Thrissur on Thursday .

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
      "cause": "against the hike in cooking gas price , in Thrissur on Thursday",
      "effect": "Members of the Kerala Mahila Sangham , the State unit of the National Federation of Indian Women , protest"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the hike in cooking gas price"
      },
      "relation": "caused",
      "effect": {
        "span": "Members of the Kerala Mahila Sangham , the State unit of the National Federation of Indian Women , protest against the hike in cooking gas price , in Thrissur on Thursday ."
      }
    }
  ]
}
```

### --- id=339 ---

输入文本: Distributing medals and trophies to winners of the five-day event in which 702 personnel from 22 State police teams and eight Central police organisations participated , the chief minister recalled the 26/11 incidents in Mumbai to stress her point .

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
      "cause": "to stress her point",
      "effect": "the chief minister recalled the 26/11 incidents in Mumbai"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to stress her point"
      },
      "relation": "caused",
      "effect": {
        "span": "the chief minister recalled the 26/11 incidents in Mumbai"
      }
    }
  ]
}
```

### --- id=341 ---

输入文本: The blockade was lifted following an assurance from ADM Debraj Senapati and the additional SP J. Mahapatra to apprise the State Government of their demand .

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
      "cause": "an assurance from ADM Debraj Senapati and the additional SP J. Mahapatra",
      "effect": "The blockade was lifted"
    },
    {
      "cause": "to apprise the State Government of their demand",
      "effect": "The blockade was lifted"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "an assurance from ADM Debraj Senapati and the additional SP J. Mahapatra to apprise the State Government of their demand"
      },
      "relation": "caused",
      "effect": {
        "span": "The blockade was lifted"
      }
    }
  ]
}
```

### --- id=344 ---

输入文本: Congress leaders led by Gandhiji , including Rajaji , Jawaharlal Nehru , Sardar Vallabhbhai Patel , Abul Kalam and Jayant Kriplani sat on a hunger strike , demanding the government reassess its priorities , commitment to original principles , ability to link national sovereignty and independence to the truest freedoms of every Indian , including freedom from poverty , hunger , exploitation and slavery .

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
      "cause": "demanding the government reassess its priorities , commitment to original principles , ability to link national sovereignty and independence to the truest freedoms of every Indian , including freedom from poverty , hunger , exploitation and slavery",
      "effect": "Congress leaders led by Gandhiji , including Rajaji , Jawaharlal Nehru , Sardar Vallabhbhai Patel , Abul Kalam and Jayant Kriplani sat on a hunger strike"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding the government reassess its priorities , commitment to original principles , ability to link national sovereignty and independence to the truest freedoms of every Indian , including freedom from poverty , hunger , exploitation and slavery"
      },
      "relation": "caused",
      "effect": {
        "span": "Congress leaders led by Gandhiji , including Rajaji , Jawaharlal Nehru , Sardar Vallabhbhai Patel , Abul Kalam and Jayant Kriplani sat on a hunger strike"
      }
    }
  ]
}
```

### --- id=345 ---

输入文本: We protest against you , for turning so viciously against our own people … and express our unhappiness with our people for having let narrow-mindedness blind you and for giving up the welfare of the nation to such leaders .

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
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "turning so viciously against our own people",
      "effect": "We protest against you"
    },
    {
      "cause": "having let narrow-mindedness blind you and for giving up the welfare of the nation to such leaders",
      "effect": "express our unhappiness with our people"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "turning so viciously against our own people"
      },
      "relation": "caused",
      "effect": {
        "span": "We protest against you"
      }
    },
    {
      "cause": {
        "span": "having let narrow-mindedness blind you and for giving up the welfare of the nation to such leaders"
      },
      "relation": "caused",
      "effect": {
        "span": "express our unhappiness with our people"
      }
    }
  ]
}
```

### --- id=347 ---

输入文本: But the caste violence that wrecked the lives of over a thousand Dalits earlier this month has forever tainted the image of Dharmapuri district as a former Naxal stronghold that , even a decade ago , had no place for caste or class differences .

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
      "cause": "the caste violence",
      "effect": "wrecked the lives of over a thousand Dalits earlier this month"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the caste violence"
      },
      "relation": "caused",
      "effect": {
        "span": "wrecked the lives of over a thousand Dalits earlier this month"
      }
    },
    {
      "cause": {
        "span": "the caste violence that wrecked the lives of over a thousand Dalits earlier this month"
      },
      "relation": "caused",
      "effect": {
        "span": "has forever tainted the image of Dharmapuri district as a former Naxal stronghold that , even a decade ago , had no place for caste or class differences ."
      }
    }
  ]
}
```

### --- id=352 ---

输入文本: The discovery of his body later that day is said to have provoked a 1,500 - strong mob to rampage through Natham and two smaller Dalit settlements , Kondampatti and Anna Nagar , where it set ablaze over 200 houses , damaged at least 50 others , and allegedly looted valuables and cash worth lakhs of rupees .

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
      "cause": "The discovery of his body later that day",
      "effect": "a 1,500 - strong mob to rampage through Natham and two smaller Dalit settlements , Kondampatti and Anna Nagar"
    },
    {
      "cause": "a 1,500 - strong mob to rampage through Natham and two smaller Dalit settlements , Kondampatti and Anna Nagar",
      "effect": "it set ablaze over 200 houses , damaged at least 50 others , and allegedly looted valuables and cash worth lakhs of rupees"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "The discovery of his body later that day"
      },
      "relation": "caused",
      "effect": {
        "span": "a 1,500 - strong mob to rampage through Natham and two smaller Dalit settlements , Kondampatti and Anna Nagar"
      }
    },
    {
      "cause": {
        "span": "the rampage"
      },
      "relation": "caused",
      "effect": {
        "span": "it set ablaze over 200 houses , damaged at least 50 others , and allegedly looted valuables and cash worth lakhs of rupees"
      }
    }
  ]
}
```

### --- id=353 ---

输入文本: In 2009 , riots broke out in the capital , Urumqui , and in their wake , mass arrests were made and many Uyghurs were imprisoned or “ disappeared ” .

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
      "cause": "riots broke out in the capital",
      "effect": "mass arrests were made and many Uyghurs were imprisoned or “ disappeared ”"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "riots broke out in the capital , Urumqui"
      },
      "relation": "caused",
      "effect": {
        "span": "mass arrests were made and many Uyghurs were imprisoned or “ disappeared ”"
      }
    }
  ]
}
```

### --- id=354 ---

输入文本: A high level team of the party led by State vice-president of the BJP , Nalini Mohanty is to visit Jogiapalli on Friday to enquire about the incident and meet the injured party workers .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "to enquire about the incident and meet the injured party workers .",
      "effect": "A high level team of the party led by State vice-president of the BJP , Nalini Mohanty is to visit Jogiapalli on Friday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to enquire about the incident"
      },
      "relation": "caused",
      "effect": {
        "span": "A high level team of the party led by State vice-president of the BJP , Nalini Mohanty is to visit Jogiapalli on Friday"
      }
    },
    {
      "cause": {
        "span": "to meet the injured party workers"
      },
      "relation": "caused",
      "effect": {
        "span": "A high level team of the party led by State vice-president of the BJP , Nalini Mohanty is to visit Jogiapalli on Friday"
      }
    }
  ]
}
```

### --- id=355 ---

输入文本: Four students were injured when police fired rubber bullets during a protest on the campus of the University of the North West in Mafikeng on Monday .

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
      "cause": "police fired rubber bullets during a protest on the campus of the University of the North West in Mafikeng on Monday",
      "effect": "Four students were injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "police fired rubber bullets during a protest on the campus of the University of the North West in Mafikeng on Monday"
      },
      "relation": "caused",
      "effect": {
        "span": "Four students were injured"
      }
    }
  ]
}
```

### --- id=356 ---

输入文本: Eight students were arrested by police who fired teargas and rubber bullets after students barricaded the main entrance .

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
      "cause": "students barricaded the main entrance",
      "effect": "Eight students were arrested by police who fired teargas and rubber bullets"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "students barricaded the main entrance"
      },
      "relation": "caused",
      "effect": {
        "span": "Eight students were arrested by police who fired teargas and rubber bullets"
      }
    }
  ]
}
```

### --- id=358 ---

输入文本: Since last week students have been protesting against a proposed increase in tuition fees and the merger of higher education institutions .

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
      "cause": "against a proposed increase in tuition fees and the merger of higher education institutions",
      "effect": "Since last week students have been protesting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a proposed increase in tuition fees and the merger of higher education institutions"
      },
      "relation": "caused",
      "effect": {
        "span": "students have been protesting"
      }
    }
  ]
}
```

### --- id=359 ---

输入文本: The students at the university of the North West had been protesting against a proposed increase in tuition fees and the merger of higher education institutions .

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
      "cause": "against a proposed increase in tuition fees and the merger of higher education institutions",
      "effect": "The students at the university of the North West had been protesting"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a proposed increase in tuition fees and the merger of higher education institutions"
      },
      "relation": "caused",
      "effect": {
        "span": "The students at the university of the North West had been protesting"
      }
    }
  ]
}
```

### --- id=360 ---

输入文本: Director Tlhalefang Kuetsile earlier said eight students were arrested and four injured when police fired rubber bullets during a protest on the campus .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "police fired rubber bullets during a protest on the campus",
      "effect": "eight students were arrested and four injured"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "police fired rubber bullets"
      },
      "relation": "caused",
      "effect": {
        "span": "eight students were arrested and four injured"
      }
    },
    {
      "cause": {
        "span": "a protest on the campus"
      },
      "relation": "caused",
      "effect": {
        "span": "police fired rubber bullets"
      }
    }
  ]
}
```

### --- id=361 ---

输入文本: Police apparently fired teargas and rubber bullets after students barricaded the main entrance .

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
      "cause": "students barricaded the main entrance",
      "effect": "Police apparently fired teargas and rubber bullets"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "students barricaded the main entrance"
      },
      "relation": "caused",
      "effect": {
        "span": "Police apparently fired teargas and rubber bullets"
      }
    }
  ]
}
```

### --- id=365 ---

输入文本: ROHTAK : Protesters block traffic , Hooda orders probe into violence ROHTAK : , May 14 , 2013 00:00 IST Arya Samaj leader Acharya Baldev addressing followers in Rohtak on Monday during a protest to demand release of leaders arrested in connection with Sunday ’ s clash .

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
      "cause": "to demand release of leaders arrested in connection with Sunday ’ s clash",
      "effect": "a protest"
    },
    {
      "cause": "Sunday ’ s clash",
      "effect": "leaders arrested"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demand release of leaders arrested in connection with Sunday 's clash"
      },
      "relation": "caused",
      "effect": {
        "span": "Arya Samaj leader Acharya Baldev addressing followers in Rohtak on Monday during a protest"
      }
    }
  ]
}
```

### --- id=369 ---

输入文本: They said the strikes would continue in the coming days to express solidarity with their leader .

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
      "cause": "to express solidarity with their leader",
      "effect": "the strikes would continue in the coming days"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to express solidarity with their leader"
      },
      "relation": "caused",
      "effect": {
        "span": "the strikes would continue in the coming days"
      }
    }
  ]
}
```

### --- id=370 ---

输入文本: Hundreds join second protest in Kunming over oil refinery Protesters in Kunming defy warnings by police , but disperse after question and answer session

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
      "cause": "oil refinery Protesters in Kunming",
      "effect": "Hundreds join second protest in Kunming"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "oil refinery"
      },
      "relation": "caused",
      "effect": {
        "span": "Hundreds join second protest in Kunming"
      }
    },
    {
      "cause": {
        "span": "question and answer session"
      },
      "relation": "caused",
      "effect": {
        "span": "Protesters in Kunming ... disperse"
      }
    }
  ]
}
```

### --- id=371 ---

输入文本: 29 Aug 2013 Hundreds defied police orders and took to the streets of Yunnan 's provincial capital Kunming yesterday to protest against an oil refinery project .

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
      "cause": "to protest against an oil refinery project",
      "effect": "Hundreds defied police orders and took to the streets of Yunnan 's provincial capital Kunming yesterday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to protest against an oil refinery project"
      },
      "relation": "caused",
      "effect": {
        "span": "Hundreds defied police orders and took to the streets of Yunnan 's provincial capital Kunming yesterday"
      }
    }
  ]
}
```

### --- id=372 ---

输入文本: PUBLISHED : Friday , 17 May , 2013 , 12:00am Kunming mayor stays true to his promise and opens microblog account

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
      "cause": "Kunming mayor stays true to his promise",
      "effect": "and opens microblog account"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "stays true to his promise"
      },
      "relation": "caused",
      "effect": {
        "span": "Kunming mayor ... opens microblog account"
      }
    }
  ]
}
```

### --- id=374 ---

输入文本: At least one demonstrator was briefly detained when he unfolded a banner , witnesses said .

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
      "cause": "he unfolded a banner",
      "effect": "At least one demonstrator was briefly detained"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "he unfolded a banner"
      },
      "relation": "caused",
      "effect": {
        "span": "At least one demonstrator was briefly detained"
      }
    }
  ]
}
```

### --- id=377 ---

输入文本: They began to march at around 2 pm , attracting onlookers and passers-by as they moved towards a popular shopping and entertainment area under close police watch .

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
      "cause": "they moved towards a popular shopping and entertainment area under close police watch",
      "effect": "attracting onlookers and passers-by"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "They began to march at around 2 pm"
      },
      "relation": "caused",
      "effect": {
        "span": "attracting onlookers and passers-by"
      }
    }
  ]
}
```

### --- id=381 ---

输入文本: Locals said the attack was triggered when a “ vehicle of the security forces ” could not pass because of the rally and the jawans got into an “ altercation ” with some people in the gathering .

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "a “ vehicle of the security forces ” could not pass because of the rally and the jawans got into an “ altercation ” with some people in the gathering",
      "effect": "the attack was triggered"
    },
    {
      "cause": "the rally and the jawans got into an “ altercation ” with some people in the gathering",
      "effect": "a “ vehicle of the security forces ” could not pass"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "a “ vehicle of the security forces ” could not pass because of the rally"
      },
      "relation": "caused",
      "effect": {
        "span": "the attack was triggered"
      }
    },
    {
      "cause": {
        "span": "the rally"
      },
      "relation": "caused",
      "effect": {
        "span": "a “ vehicle of the security forces ” could not pass"
      }
    },
    {
      "cause": {
        "span": "the attack was triggered when a “ vehicle of the security forces ” could not pass because of the rally"
      },
      "relation": "caused",
      "effect": {
        "span": "the jawans got into an “ altercation ” with some people in the gathering"
      }
    }
  ]
}
```

### --- id=382 ---

输入文本: “ Suddenly the situation flared up and the vehicle was vandalised .

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
      "cause": "Suddenly the situation flared up",
      "effect": "the vehicle was vandalised"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the situation flared up"
      },
      "relation": "caused",
      "effect": {
        "span": "the vehicle was vandalised"
      }
    }
  ]
}
```

### --- id=383 ---

输入文本: After the jawans left , the Kaliachak police station was attacked , ” said a resident .

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
      "cause": "the jawans left",
      "effect": "the Kaliachak police station was attacked"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "the jawans left"
      },
      "relation": "caused",
      "effect": {
        "span": "the Kaliachak police station was attacked"
      }
    }
  ]
}
```
