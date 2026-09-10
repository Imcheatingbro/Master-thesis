# cnc first 300 eval report

## 配置
```json
{
  "label": "cnc first 300",
  "model": "google/gemma-4-31b-qat",
  "dataset": "cnc",
  "sample_count": 300,
  "prompt_name": "v9.8",
  "use_rag": false,
  "rag_mode": "knn",
  "rag_top_k": 5,
  "temperature": 0.0,
  "max_tokens": 16384,
  "progress_every": 500,
  "max_workers": 1,
  "llm_provider": "lmstudio",
  "llm_base_url": "http://127.0.0.1:1234/v1",
  "context_length": 16384,
  "reasoning_effort": "none",
  "llm_extra_body": {},
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
================ cnc first 300 final report ================
样本总数: 300
  Gold 含因果: 154 | Pred 含因果: 180
  Primary extraction metric: strict_token_f1
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.820
  Precision: 0.778
  Recall   : 0.909
  F1       : 0.838
  (TP=140, TN=106, FP=40, FN=14)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1] (primary)
    样本数: 300
    Gold triples: 210 | Pred triples: 220
    Precision: 0.568
    Recall   : 0.595
    F1       : 0.581
    (TP=125, FP=95, FN=85)
  [anchor_window]
    样本数: 300
    Gold triples: 210 | Pred triples: 220
    Precision: 0.618
    Recall   : 0.648
    F1       : 0.633
    (TP=136, FP=84, FN=74)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1] (primary)
    样本数: 140
    Gold triples: 194 | Pred triples: 175
    Precision: 0.714
    Recall   : 0.644
    F1       : 0.678
    (TP=125, FP=50, FN=69)
  [anchor_window]
    样本数: 140
    Gold triples: 194 | Pred triples: 175
    Precision: 0.777
    Recall   : 0.701
    F1       : 0.737
    (TP=136, FP=39, FN=58)
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
  "total": 3,
  "by_type": {
    "duplicate_effect_closing_brace": 3
  },
  "samples": [
    {
      "id": 40,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 139,
      "repair_type": "duplicate_effect_closing_brace"
    },
    {
      "id": 225,
      "repair_type": "duplicate_effect_closing_brace"
    }
  ]
}
```

## 样本明细

Sample details shown: all 112 wrong samples from 300 total samples.

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
        "span": "leaving at least 45 people in hospital ."
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
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 1,
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
        "span": "to demand answers from authorities for failing to stop the violence ."
      },
      "relation": "caused",
      "effect": {
        "span": "demonstrators , opposition lawmakers and others demanded answers from authorities"
      }
    },
    {
      "cause": {
        "span": "for failing to stop the violence ."
      },
      "relation": "caused",
      "effect": {
        "span": "demonstrators , opposition lawmakers and others demanded answers from authorities"
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
        "span": "To show our solidarity and say no to terrorism"
      },
      "relation": "caused",
      "effect": {
        "span": "we have to stand up."
      }
    },
    {
      "cause": {
        "span": "Yuen Long was under terrorist attack"
      },
      "relation": "caused",
      "effect": {
        "span": "we have no choice but to take it back."
      }
    },
    {
      "cause": {
        "span": "over a controversial bill that would allow suspects to be extradited from Hong Kong to mainland China"
      },
      "relation": "caused",
      "effect": {
        "span": "The protests"
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
        "span": "to condemn the government and police for “ ignoring the random attacks on citizens in Yuen Long ” ."
      },
      "relation": "caused",
      "effect": {
        "span": "a group of aviation staff called for a protest at Hong Kong airport on Friday"
      }
    }
  ]
}
```

### --- id=12 ---

输入文本: In Yuen Long , Chung and other protesters are demanding the government conducts an independent investigation and officially characterises the violence as a “ cross-border terrorist attack ” .

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
        "span": "demanding the government conducts an independent investigation and officially characterises the violence as a “ cross-border terrorist attack ” ."
      },
      "relation": "caused",
      "effect": {
        "span": "In Yuen Long , Chung and other protesters are"
      }
    }
  ]
}
```

### --- id=17 ---

输入文本: They exhorted us to join the protest against the recommendations of the Mandal Commission , which had been implemented a day earlier .

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
        "span": "against the recommendations of the Mandal Commission"
      },
      "relation": "caused",
      "effect": {
        "span": "to join the protest"
      }
    }
  ]
}
```

### --- id=23 ---

输入文本: As we closed in on the hideout of the militants , a fire fight began that continued for over an hour , ” he said .

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
        "span": "As we closed in on the hideout of the militants"
      },
      "relation": "caused",
      "effect": {
        "span": "a fire fight began that continued for over an hour"
      }
    }
  ]
}
```

### --- id=24 ---

输入文本: According to reports , two militants have been shot dead in the encounter .

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
        "span": "in the encounter ."
      },
      "relation": "caused",
      "effect": {
        "span": "two militants have been shot dead"
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
        "span": "as he is believed to have arranged explosives and planter for the blast ."
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
        "span": "as the first of the e—mails claiming responsibility for the blast emanated from here ."
      },
      "relation": "caused",
      "effect": {
        "span": "The Kishtwar area has been in focus ever since the Delhi High Court blast"
      }
    }
  ]
}
```

### --- id=32 ---

输入文本: Modi visited the homes of all the six victims of the serial blasts which rocked Patna ’ s Gandhi Maidan and other parts of the city during his visit to address the Hunkar Rally on October 27 .

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
        "span": "the serial blasts which rocked Patna ’ s Gandhi Maidan and other parts of the city"
      },
      "relation": "caused",
      "effect": {
        "span": "Modi visited the homes of all the six victims of the serial blasts"
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
        "span": "to express condolences and score points over his rambunctious rivals ."
      },
      "relation": "caused",
      "effect": {
        "span": "NaMo , who had avoided visiting the victims of the 2002 riots in his own state for a long time , lost no time in burning up aviation fuel by dashing to Patna twice in one week"
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
        "span": "with exploiting the grief of the terror victims of 26/10 ."
      },
      "relation": "caused",
      "effect": {
        "span": "Now , he is charged"
      }
    }
  ]
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
        "span": "By visiting the families of the Patna blast victims"
      },
      "relation": "caused",
      "effect": {
        "span": "NaMo is drilling home the point that NiKu is least bothered about the personal tragedies of his people ."
      }
    }
  ]
}
```

### --- id=37 ---

输入文本: Both Anoop and Ramanan are also accused in the case related to attack on the Nitta Gelatin office at Panampilly Nagar last year .

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
        "span": "in the case related to attack on the Nitta Gelatin office at Panampilly Nagar last year ."
      },
      "relation": "caused",
      "effect": {
        "span": "Both Anoop and Ramanan are also accused"
      }
    }
  ]
}
```

### --- id=39 ---

输入文本: The grief list also includes the nights spent by Rahul in Dalit colonies and the visits of Manmohan Singh and Sonia Gandhi to Chhattisgarh after top Congress leaders were massacred by Naxalites .

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
        "span": "after top Congress leaders were massacred by Naxalites ."
      },
      "relation": "caused",
      "effect": {
        "span": "the visits of Manmohan Singh and Sonia Gandhi to Chhattisgarh"
      }
    }
  ]
}
```

### --- id=40 ---

输入文本: Modiites are now reminding the Congress about the trips which Sonia and the Prime Minister made to Muzzafarnagar after 43 were killed in the worst-ever communal clashes in decades .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "the worst-ever communal clashes in decades"
      },
      "relation": "caused",
      "effect": {
        "span": "43 were killed"
      }
    },
    {
      "cause": {
        "span": "after 43 were killed in the worst-ever communal clashes in decades ."
      },
      "relation": "caused",
      "effect": {
        "span": "the trips which Sonia and the Prime Minister made to Muzzafarnagar"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
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
        "span": "urging the district administration to immediately disconnect the illegal water connections and ensure uninterrupted water supply to them ."
      },
      "relation": "caused",
      "effect": {
        "span": "the villagers , including a large number of women from the panchayat comprising six villages , staged the protest"
      }
    }
  ]
}
```

### --- id=49 ---

输入文本: VS condemns attack on NSS Karayogams 08th May 2011 05:00 AM THIRUVANANTHAPURAM : Chief Minister V S Achuthanandan has condemned the recent attacks on NSS Karayogams .

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
        "span": "the recent attacks on NSS Karayogams ."
      },
      "relation": "caused",
      "effect": {
        "span": "Chief Minister V S Achuthanandan has condemned"
      }
    }
  ]
}
```

### --- id=50 ---

输入文本: Given that nearly seven years have passed since the horrendous terror attacks that claimed over 160 lives and injured many others , Biswal said bringing justice for the victims in terror attacks may appear to be an arduous andlong-drawn process .

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
        "span": "the horrendous terror attacks"
      },
      "relation": "caused",
      "effect": {
        "span": "that claimed over 160 lives and injured many others"
      }
    }
  ]
}
```

### --- id=51 ---

输入文本: Biswal underlined that the US on its part had offered rewards for information leading to the arrest and prosecution of individuals associated with the Mumbai attack .

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
        "span": "for information leading to the arrest and prosecution of individuals associated with the Mumbai attack ."
      },
      "relation": "caused",
      "effect": {
        "span": "the US on its part had offered rewards"
      }
    }
  ]
}
```

### --- id=52 ---

输入文本: Referring to the terror attack in Punjab 's Gurdaspur district on July 27 , Biswal said the US has strongly condemned and expressed its concern over the attack .

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
        "span": "over the attack ."
      },
      "relation": "caused",
      "effect": {
        "span": "the US has strongly condemned and expressed its concern"
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
      "cause": "to try to ascertain and trace the origins of the equipment found",
      "effect": "the US is in conversation with Indian authorities"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "On media reports that the night vision device used by three terrorists in the Gurdaspur attack had US markings"
      },
      "relation": "caused",
      "effect": {
        "span": "Biswal said the US is in conversation with Indian authorities to try to ascertain and trace the origins of the equipment found ."
      }
    },
    {
      "cause": {
        "span": "to try to ascertain and trace the origins of the equipment found ."
      },
      "relation": "caused",
      "effect": {
        "span": "the US is in conversation with Indian authorities"
      }
    }
  ]
}
```

### --- id=56 ---

输入文本: The step came after RLD workers , led by district party president Ajit Rathi , former UP minister Dharamvir Balyan and MLC Chaudhry Mushtaq , staged a dharna outside the DM 's office here yesterday and submitted a memorandum to him .

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
        "span": "after RLD workers , led by district party president Ajit Rathi , former UP minister Dharamvir Balyan and MLC Chaudhry Mushtaq , staged a dharna outside the DM 's office here yesterday and submitted a memorandum to him ."
      },
      "relation": "caused",
      "effect": {
        "span": "The step came"
      }
    }
  ]
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
        "span": "denied jobs by a multi-national corporation who had recruited them from their college campuses"
      },
      "relation": "caused",
      "effect": {
        "span": "graduates denied jobs by a multi-national corporation who had recruited them from their college campuses , staged a hunger strike on Sunday ."
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
        "span": "for their alleged involvement in killing of a naib sarpanch in a clash between members of two communities at Bimbola village under Dhenkanal Sadar police limits on Monday ."
      },
      "relation": "caused",
      "effect": {
        "span": "Three persons were arrested on Tuesday"
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
        "span": "after NSS secretary Sukumaran Nair had said that the NSS did not support the LDF in the recent Assembly elections"
      },
      "relation": "caused",
      "effect": {
        "span": "The NSS Karayogams were attacked in Thrissur and Thiruvananthapuram"
      }
    },
    {
      "cause": {
        "span": "as it did not want Achuthanandan to come back to power for another term ."
      },
      "relation": "caused",
      "effect": {
        "span": "the NSS did not support the LDF in the recent Assembly elections"
      }
    }
  ]
}
```

### --- id=80 ---

输入文本: At least five more people will be tried over the attack , Xinhua has reported .

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
        "span": "over the attack"
      },
      "relation": "caused",
      "effect": {
        "span": "At least five more people will be tried"
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
        "span": "in wake of a string of violent attacks in the restive Xinjiang region and other cities on the mainland ."
      },
      "relation": "caused",
      "effect": {
        "span": "Mainland authorities have launched a massive crackdown against terrorism"
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
        "span": "by refusing to declare their allegiance to China and carrying blue flags reading : “ Hong Kong is not China. ”"
      },
      "relation": "caused",
      "effect": {
        "span": "Yau and Leung thumbed their noses at Beijing"
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
        "span": "leading to nearly three months of street protests in 2014 – known as the umbrella revolution – and to the election in September this year of six politicians pushing for greater autonomy for the city ."
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
        "span": "due to the bandh"
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
        "span": "amid fears that the taxi strike might turn violent ."
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
        "span": "following a dispute in mileage payment ."
      },
      "relation": "caused",
      "effect": {
        "span": "About 125 bus operators across Gauteng stopped reporting for duty two weeks ago"
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
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
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
        "span": "protesting \" irritable \" behaviour of the area officer at Churchgate"
      },
      "relation": "caused",
      "effect": {
        "span": "Most guards on local trains abstained from work Thursday"
      }
    },
    {
      "cause": {
        "span": "Most guards on local trains abstained from work Thursday"
      },
      "relation": "caused",
      "effect": {
        "span": "forcing station masters and traffic inspectors to take up their role ."
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
        "span": "after he was denied leave despite applying two months back ."
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
        "span": "When Jha did not get leave till four hours before departure of his train"
      },
      "relation": "caused",
      "effect": {
        "span": "he hanged a poster around his neck announcing an indefinite hunger strike ."
      }
    }
  ]
}
```

### --- id=103 ---

输入文本: She did not directly name Bhatta-Parsaul , the twin villages that have emerged as the epicentre of the agitation against land acquisition by the Uttar Pradesh government for an expressway project , but specifically mentioned the atrocities on farmers .

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
        "span": "against land acquisition by the Uttar Pradesh government for an expressway project"
      },
      "relation": "caused",
      "effect": {
        "span": "the agitation"
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
      "cause": "demanding Thampu 's resignation for shielding the accused",
      "effect": "Scores of students , teachers and women rights organisations had yesterday staged a protest outside college"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "demanding Thampu 's resignation for shielding the accused ."
      },
      "relation": "caused",
      "effect": {
        "span": "Scores of students , teachers and women rights organisations had yesterday staged a protest outside college"
      }
    },
    {
      "cause": {
        "span": "for shielding the accused ."
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
    "tp": 2,
    "fp": 0,
    "fn": 1
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 1,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 1
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
        "span": "demanding the arrest of a territorial army jawan"
      },
      "relation": "caused",
      "effect": {
        "span": "Locals took to the streets in frontier district of Kupwara today"
      }
    },
    {
      "cause": {
        "span": "who allegedly tried to molest a young woman"
      },
      "relation": "caused",
      "effect": {
        "span": "she committed suicide ."
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
        "span": "led to the death of three Congress workers on Sunday ."
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
      "cause": "There were reports of skirmishes and clashes , including stone pelting , in the area",
      "effect": "two policemen were injured"
    }
  ],
  "pred_triples": []
}
```

### --- id=120 ---

输入文本: `` I observed the attack on the police , I have no doubt about it , '' Modiba said during cross-examination .

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
      "cause": "I observed the attack on the police",
      "effect": "I have no doubt about it"
    }
  ],
  "pred_triples": []
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
        "span": "Accusing the CPM of instigating the violence"
      },
      "relation": "caused",
      "effect": {
        "span": "she said the deaths were result of clashes between the Congress and the Marxists ."
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
        "span": "after unrest rocked Tibetan-populated areas in March 2008 ."
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
        "span": "that left commuters stranded in Johannesburg"
      }
    }
  ]
}
```

### --- id=127 ---

输入文本: `` We have been told of a possible one-day strike that has already affected Soweto .

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
        "span": "a possible one-day strike"
      },
      "relation": "caused",
      "effect": {
        "span": "that has already affected Soweto ."
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
      "cause": "the strike",
      "effect": "also disrupt the Reya Vaya bus service"
    }
  ],
  "pred_triples": []
}
```

### --- id=132 ---

输入文本: `` We do not know about the strike , if we called for a strike we could have informed commuters , '' said president Philip Taaibosch .

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
      "cause": "we called for a strike",
      "effect": "we could have informed commuters"
    }
  ],
  "pred_triples": []
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
        "span": "protesting the ' forcible installation ' of a Kannadiga mayor in Marathi-dominated Belgaum city ."
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
      "cause": "demanding that Belgaum , along with Marathi speaking areas in that state , be merged with Maharashtra",
      "effect": "The protesters shouted slogans against the Karnataka CM"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "against the Karnataka CM"
      },
      "relation": "caused",
      "effect": {
        "span": "The protesters shouted slogans"
      }
    },
    {
      "cause": {
        "span": "demanding that Belgaum , along with Marathi speaking areas in that state , be merged with Maharashtra ."
      },
      "relation": "caused",
      "effect": {
        "span": "The protesters shouted slogans against the Karnataka CM"
      }
    }
  ]
}
```

### --- id=139 ---

输入文本: One group held a black banner with the words : “ The police have overstepped ” , while others chanted for the release of protesters who have been arrested over the last two months of demonstrations .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "for the release of protesters who have been arrested over the last two months of demonstrations ."
      },
      "relation": "caused",
      "effect": {
        "span": "others chanted"
      }
    },
    {
      "cause": {
        "span": "over the last two months of demonstrations ."
      },
      "relation": "caused",
      "effect": {
        "span": "protesters who have been arrested"
      }
    }
  ],
  "parse_repair_type": "duplicate_effect_closing_brace"
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
        "span": "over a proposal to allow extradition to China"
      },
      "relation": "caused",
      "effect": {
        "span": "The protests , which began"
      }
    }
  ]
}
```

### --- id=146 ---

输入文本: In recent days , Beijing has ramped up its condemnation of the protests , which it describes as “ riots ” , and has accused the US and other western powers of instigating the unrest to hurt China .

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
        "span": "to hurt China ."
      },
      "relation": "caused",
      "effect": {
        "span": "instigating the unrest"
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
      "cause": "requested",
      "effect": "the military was “ determined to protect [ the ] national sovereignty ” of Hong Kong and would help put down the “ intolerable ” unrest"
    }
  ],
  "pred_triples": []
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
        "span": "Hong Kong police on Thursday also charged 44 people linked to the protests with “ rioting ”"
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
      "cause": "peaceful marches",
      "effect": "that disrupt the road for an afternoon or so"
    },
    {
      "cause": "peaceful marches that disrupt the road for an afternoon or so don ’ t work",
      "effect": "maybe it spills over to blockading more roads , maybe for long"
    }
  ],
  "pred_triples": []
}
```

### --- id=151 ---

输入文本: The statement condemned authorities for turning “ a deaf ear to peaceful protests from a wide section society ” and threatened more actions .

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
        "span": "for turning “ a deaf ear to peaceful protests from a wide section society ”"
      },
      "relation": "caused",
      "effect": {
        "span": "The statement condemned authorities"
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
        "span": "to demand payment of their delayed wages from Northstar Textiles ."
      },
      "relation": "caused",
      "effect": {
        "span": "party functionaries who staged dharna in front of Kadapa Collectorate on Thursday"
      }
    }
  ]
}
```

### --- id=153 ---

输入文本: The commission , chaired by retired Judge Ian Farlam , is investigating the deaths of 44 people during the wage-related strike at Lonmin 's platinum mining operations at Marikana in August 2012 .

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
        "span": "during the wage-related strike at Lonmin 's platinum mining operations at Marikana in August 2012 ."
      },
      "relation": "caused",
      "effect": {
        "span": "the deaths of 44 people"
      }
    }
  ]
}
```

### --- id=154 ---

输入文本: ANDHRA PRADESH Work in banks , insurance firms hit August 21 , 2008 00:00 IST Back to old days : A horse-drawn cart comes in handy for passengers as autos went off the road during the general strike in Kurnool on Wednesday .

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
        "span": "during the general strike in Kurnool on Wednesday ."
      },
      "relation": "caused",
      "effect": {
        "span": "autos went off the road"
      }
    }
  ]
}
```

### --- id=158 ---

输入文本: Besides the bank and the insurance company employees , medical and sales representatives , members of the UTF , anganwadi , municipal and construction workers , hamalis , including the RTC porters , participated in the rally taken out under the banner of the leftist unions protesting against the ‘ anti-employee ’ and ‘ anti-national ’ policies of the Congress-led UPA government .

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
        "span": "protesting against the ‘ anti-employee ’ and ‘ anti-national ’ policies of the Congress-led UPA government ."
      },
      "relation": "caused",
      "effect": {
        "span": "Besides the bank and the insurance company employees , medical and sales representatives , members of the UTF , anganwadi , municipal and construction workers , hamalis , including the RTC porters , participated in the rally taken out under the banner of the leftist unions"
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
        "span": "for doing nothing except chanting ‘ Indira , Rajiv and Sonia ’ mantra , grossly sideling the National Common Minimum Programme ."
      },
      "relation": "caused",
      "effect": {
        "span": "Leaders of the CPI-M , CPI , TDP and the frontal units , addressing the rally , lashed out at the Central and State governments"
      }
    }
  ]
}
```

### --- id=161 ---

输入文本: Secretary of the Insurance Corporation Employees ’ Union , Nellore Division , K. Gopalakrishnaiah and other leaders , who held a demonstration in front of the United India Insurance Company here , criticised the UPA that had categorically said it would strengthen the LIC and GICs but was doing just the opposite by hiking the cap on the Foreign Direct Investment in the insurance sector .

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
        "span": "by hiking the cap on the Foreign Direct Investment in the insurance sector ."
      },
      "relation": "caused",
      "effect": {
        "span": "was doing just the opposite"
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
      "cause": "a clash with police who were trying to disarm and disperse them",
      "effect": "On August 16 , 2012 , 34 people , mostly mineworkers , were shot dead"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "in a clash with police who were trying to disarm and disperse them"
      },
      "relation": "caused",
      "effect": {
        "span": "34 people , mostly mineworkers , were shot dead"
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
        "span": "to get an urgent interdict ."
      },
      "relation": "caused",
      "effect": {
        "span": "they would make another attempt"
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
      "cause": "to trace and recover the abducted people",
      "effect": "Search is on"
    }
  ],
  "pred_triples": []
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
        "span": "it was the turn of Telangana Rashtra Samithi ( TRS ) to participate in protests"
      }
    },
    {
      "cause": {
        "span": "in support to farmers"
      },
      "relation": "caused",
      "effect": {
        "span": "on Monday it was the Telugu Desam"
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
      "cause": "assurances by the authorities",
      "effect": "the stock of urea is not reaching farmers"
    }
  ],
  "pred_triples": []
}
```

### --- id=195 ---

输入文本: At the same time , the Jawaharlal Nehru University Staff Association ( JNUSA ) and Jawaharlal Nehru University Officers Association ( JNUOA ) also sought action against those who shouted anti-national slogans on the campus on February 9 .

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
        "span": "against those who shouted anti-national slogans on the campus on February 9 ."
      },
      "relation": "caused",
      "effect": {
        "span": "the Jawaharlal Nehru University Staff Association ( JNUSA ) and Jawaharlal Nehru University Officers Association ( JNUOA ) also sought action"
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
        "span": "the arrest of student union president Kanhaiya Kumar on charges that he too shouted the anti-Indian slogans at a meeting on Kashmir ."
      },
      "relation": "caused",
      "effect": {
        "span": "The escalating protests in the JNU"
      }
    },
    {
      "cause": {
        "span": "that he too shouted the anti-Indian slogans at a meeting on Kashmir ."
      },
      "relation": "caused",
      "effect": {
        "span": "the arrest of student union president Kanhaiya Kumar"
      }
    }
  ]
}
```

### --- id=199 ---

输入文本: " We appeal the JNU administration and central government to take strict action against whomsoever is responsible for the ( slogan-shouting ) incident . " " The guilty should be immediately arrested and severely punished , " JNUSA general secretary Ajay Kumar told the media .

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
        "span": "to take strict action against whomsoever is responsible for the ( slogan-shouting ) incident ."
      },
      "relation": "caused",
      "effect": {
        "span": "We appeal the JNU administration and central government"
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
      "cause": "Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday to address them",
      "effect": "A crowd of supporters erupted"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "as Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday to address them ."
      },
      "relation": "caused",
      "effect": {
        "span": "A crowd of supporters erupted"
      }
    },
    {
      "cause": {
        "span": "to address them ."
      },
      "relation": "caused",
      "effect": {
        "span": "Jacob Zuma walked on to a stage outside the Pietermaritzburg High Court on Thursday"
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
        "span": "A day after alleged suicide by one of their colleagues"
      },
      "relation": "caused",
      "effect": {
        "span": "the employees , including officers , went on a mass casual leave on Tuesday"
      }
    },
    {
      "cause": {
        "span": "to press for their demand to withdraw decision on privatisation of Dredging Corporation of India ( DCI ) ."
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
      "cause": "threaten to intensify stir",
      "effect": "DCI employees go on mass casual leave"
    }
  ],
  "pred_triples": []
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
        "span": "to take part in the last rites of N. Venkatesh , 28 , an assistant in the administration department of the corporation , who committed suicide on railway tracks to protest against the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "hundreds of employees from the city went to Vizianagaram"
      }
    },
    {
      "cause": {
        "span": "to protest against the Centre ’ s decision on strategic stake sale of DCI"
      },
      "relation": "caused",
      "effect": {
        "span": "who committed suicide on railway tracks"
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
        "span": "which claimed 14 lives in the village in East Midnapore district ."
      }
    }
  ]
}
```

### --- id=211 ---

输入文本: Addressing a congregation at Gokulnagar , Nandigram , Trinamool Congress chief Mamata Banerjee said the people would give a fitting reply to the Communist Party of India (Marxist)-led government for the “ carnage . ” “ Violence continues ” Condemning the “ atrocities committed by CPI(M) cadres on the innocent people of Nandigram , ” Ms. Banerjee said even after a year “ those responsible had not been punished .

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "strict_token_f1",
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
        "span": "for the “ carnage . ”"
      },
      "relation": "caused",
      "effect": {
        "span": "the people would give a fitting reply to the Communist Party of India (Marxist)-led government"
      }
    },
    {
      "cause": {
        "span": "Condemning the “ atrocities committed by CPI(M) cadres on the innocent people of Nandigram , ”"
      },
      "relation": "caused",
      "effect": {
        "span": "Ms. Banerjee said even after a year “ those responsible had not been punished ."
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
      "cause": "over the past three weeks , more than 60 trucks had come under attack",
      "effect": "there were `` a lot of injuries '' of drivers"
    }
  ],
  "pred_triples": []
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
      "cause": "protesting the fare hike and demanded an immediate rollback in the fares",
      "effect": "The party activists held demonstrations in various parts of the state"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "protesting the fare hike"
      },
      "relation": "caused",
      "effect": {
        "span": "The party activists held demonstrations in various parts of the state"
      }
    },
    {
      "cause": {
        "span": "protesting the fare hike"
      },
      "relation": "caused",
      "effect": {
        "span": "demanded an immediate rollback in the fares ."
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
      "cause": "to solve the wage dispute and to end the strike",
      "effect": "Talks are underway"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "to solve the wage dispute"
      },
      "relation": "caused",
      "effect": {
        "span": "Talks are underway"
      }
    },
    {
      "cause": {
        "span": "to end the strike"
      },
      "relation": "caused",
      "effect": {
        "span": "Talks are underway"
      }
    }
  ]
}
```

### --- id=234 ---

输入文本: The Muslim Youth Movement of South Africa on Tuesday pledged solidarity with the striking workers .

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
        "span": "with the striking workers ."
      },
      "relation": "caused",
      "effect": {
        "span": "The Muslim Youth Movement of South Africa on Tuesday pledged solidarity"
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
    "fp": 2,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 2,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 2,
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
        "span": "to put the striking workers and all the poor people battling against capitalist greed in their prayers"
      },
      "relation": "caused",
      "effect": {
        "span": "We call upon the Muslim community"
      }
    },
    {
      "cause": {
        "span": "to use this glorious month of Ramadan to re-commit themselves to the struggle for socio-economic justice , equity and freedom for all"
      },
      "relation": "caused",
      "effect": {
        "span": "We call upon the Muslim community"
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
        "span": "for attempted arson ."
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
      "cause": "A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials",
      "effect": "were arrested in Central yesterday"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials"
      },
      "relation": "caused",
      "effect": {
        "span": "A couple suspected of sending a letter addressed to Chief Executive Tung Chee-hwa threatening to poison his food and drink and that of his two top officials were arrested in Central yesterday ."
      }
    }
  ]
}
```

### --- id=244 ---

输入文本: Signed ' Hong Kong bin Laden ' , it also said the author was not happy with the work of Mr Tung 's two top officials , Chief Secretary Donald Tsang Yam-kuen and Financial Secretary Antony Leung Kam-chung , whom it also threatened to poison , a police source said last night .

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
        "span": "the author was not happy with the work of Mr Tung's two top officials , Chief Secretary Donald Tsang Yam-kuen and Financial Secretary Antony Leung Kam-chung"
      },
      "relation": "caused",
      "effect": {
        "span": "whom it also threatened to poison"
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
      "cause": "around 50 armed ultras raided Kangurukunda village at Kalimela , about 40 km from here , early on Sunday and set off an explosion",
      "effect": "destrying the panchayat office"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "set off an explosion"
      },
      "relation": "caused",
      "effect": {
        "span": "destrying the panchayat office ."
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
        "span": "against JR Power Plant ."
      },
      "relation": "caused",
      "effect": {
        "span": "They made their intention loud and clear raising slogans"
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
        "span": "as protest leaders warned they would step up their actions if Hong Kong ’ s chief executive , Leung Chun-ying , did not meet them by midnight ."
      },
      "relation": "caused",
      "effect": {
        "span": "tens of thousands of demonstrators packed the city ’ s downtown area for a third night"
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
        "span": "following the blockade by people of Kishorenagar area ."
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
      "cause": "the Chief Minister had himself announced , during an election rally , allocation of funds for the proposed Sureswari irrigation project here",
      "effect": "The protestors accused the Government of reneging on its commitment"
    },
    {
      "cause": "the proposed Sureswari irrigation project here",
      "effect": "allocation of funds"
    }
  ],
  "pred_triples": []
}
```

### --- id=267 ---

输入文本: September 14 , 2012 00:00 IST Her absence from Vijayamma ’ s protest meet gives credence to rumours Rumour mills are abuzz in Warangal hinting that YSR Congress party leader and former Minister Konda Surekha may join the Congress soon .

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
      "cause": "Her absence from Vijayamma ’ s protest meet",
      "effect": "rumours"
    }
  ],
  "pred_triples": []
}
```

### --- id=269 ---

输入文本: Hindu outfits blocked by police 04th November 2009 04:48 AM THIRUVANANTHAPURAM : Protests against foreign missionary Bernard Blessing ’ s presence in the city spilled into the streets on Tuesday evening with Hindu organisations taking out a march to his prayer meeting , and engaging in a minor scuffle with the police .

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
        "span": "against foreign missionary Bernard Blessing ’ s presence in the city"
      },
      "relation": "caused",
      "effect": {
        "span": "Protests against foreign missionary Bernard Blessing ’ s presence in the city spilled into the streets on Tuesday evening with Hindu organisations taking out a march to his prayer meeting , and engaging in a minor scuffle with the police ."
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
        "span": "after having spent months out of school"
      },
      "relation": "caused",
      "effect": {
        "span": "some pupils returned to classes"
      }
    },
    {
      "cause": {
        "span": "against the Municipal Demarcation Board 's decision to include their areas under a new municipality ."
      },
      "relation": "caused",
      "effect": {
        "span": "residents protested"
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
        "span": "Accusing the United Progressive Alliance ( UPA ) government of adopting a confrontationist attitude towards the states"
      },
      "relation": "caused",
      "effect": {
        "span": "he said it has been demolishing the constitutional institutions whereas the need of the hour is a cooperative attitude ."
      }
    }
  ]
}
```

### --- id=275 ---

输入文本: Addressing a massive public rally at Vandalur , around 40 km from here , Modi said : " The central government should be strong , only then the neighbouring countries will be friendly with us . "

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
        "span": "The central government should be strong"
      },
      "relation": "caused",
      "effect": {
        "span": "the neighbouring countries will be friendly with us ."
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
        "span": "hundreds of Bengal traders launched an agitation on Monday and threatened to intensify it"
      }
    }
  ]
}
```

### --- id=280 ---

输入文本: “ Though after the CM-level talks , we released all the detained trucks to West Bengal , they took back all the potato-laden trucks to their State , ” Agrawal said .

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
        "span": "after the CM-level talks"
      },
      "relation": "caused",
      "effect": {
        "span": "we released all the detained trucks to West Bengal"
      }
    }
  ]
}
```

### --- id=281 ---

输入文本: Labour Minister Mildred Oliphant intervened on Monday in an extended strike by petrol attendants and workers in the automotive industry .

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
        "span": "in an extended strike by petrol attendants and workers in the automotive industry ."
      },
      "relation": "caused",
      "effect": {
        "span": "Labour Minister Mildred Oliphant intervened on Monday"
      }
    }
  ]
}
```

### --- id=284 ---

输入文本: Protests show rising green concerns PUBLISHED : Wednesday , 04 July , 2012 , 12:00am Mass protests this week over the planned construction of a molybdenum-copper alloy plant in Shifang , Sichuan province show that environmental concerns are becoming a leading cause of social unrest .

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
        "span": "over the planned construction of a molybdenum-copper alloy plant in Shifang , Sichuan province"
      },
      "relation": "caused",
      "effect": {
        "span": "Mass protests this week"
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
        "span": "to protest against plans to built a paraxylene chemical plant in the city ."
      },
      "relation": "caused",
      "effect": {
        "span": "over 20,000 people rallied in Xiamen , a coastal city in Fujian province ,"
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
        "span": "because they lack adequate channels to express their concerns about environmental risks posed by massive industrial projects ."
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
        "span": "to make their voices heard"
      },
      "relation": "caused",
      "effect": {
        "span": "the Shifang protests came as a last resort for local residents"
      }
    },
    {
      "cause": {
        "span": "as ' all other channels for public participation were ineffective '"
      },
      "relation": "caused",
      "effect": {
        "span": "the Shifang protests came as a last resort for local residents"
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
        "span": "leaving a civilian dead and over 100 injured ."
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
        "span": "to probe into the violence and the deaths of 44 people in wage-related protests ."
      },
      "relation": "caused",
      "effect": {
        "span": "The three-member Farlam Commission , chaired by retired judge Ian Farlam , was established by President Jacob Zuma"
      }
    }
  ]
}
```

### --- id=297 ---

输入文本: “ Amid stone-throwing , some rounds were fired at the convoy going to Kupwara .

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
        "span": "Amid stone-throwing"
      },
      "relation": "caused",
      "effect": {
        "span": "some rounds were fired at the convoy going to Kupwara ."
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
        "span": "when the latter stopped the movement of fruit trucks in Rafiabad and Sopore , asking the drivers to ply only during the shutdown period ."
      },
      "relation": "caused",
      "effect": {
        "span": "clashes between the residents and the Army started in the morning"
      }
    }
  ]
}
```

### --- id=299 ---

输入文本: “ The youth was killed at a protest against the Army ’ s action halting the vehicles , ” alleged Mohammad Yasin Khan , head of a traders ’ body .

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
        "span": "against the Army ’ s action halting the vehicles"
      },
      "relation": "caused",
      "effect": {
        "span": "The youth was killed at a protest"
      }
    }
  ]
}
```
