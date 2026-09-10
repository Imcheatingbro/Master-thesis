# Qwen3.6 35B A3B ADE held-out test eval report

## 配置
```json
{
  "label": "Qwen3.6 35B A3B ADE held-out test",
  "model": "qwen/qwen3.6-35b-a3b",
  "dataset": "ade",
  "sample_count": 2942,
  "prompt_name": "v9.1",
  "use_rag": false,
  "rag_mode": "knn_pattern",
  "rag_top_k": 3,
  "temperature": 0.0,
  "max_tokens": 2048,
  "output_schema": "standard",
  "primary_metric": "anchor_window",
  "progress_every": 1000,
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
  "metadata_path": null,
  "embeddings_path": null
}
```

## 统计指标
```text
================ Qwen3.6 35B A3B ADE held-out test final report ================
样本总数: 2942
  Gold 含因果: 448 | Pred 含因果: 155
  Primary extraction metric: anchor_window
  strict_token_f1 阈值: 0.800
  anchor_window 阈值: 0.900

[Layer 1] Detection
  Accuracy : 0.881
  Precision: 0.819
  Recall   : 0.283
  F1       : 0.421
  (TP=127, TN=2466, FP=28, FN=321)

[Layer 2A] Extraction all_samples
  说明: 忽略 has_causal 字段，在全部样本上匹配 pred triples 与 gold relations。
  [strict_token_f1]
    样本数: 2942
    Gold triples: 663 | Pred triples: 215
    Precision: 0.581
    Recall   : 0.189
    F1       : 0.285
    (TP=125, FP=90, FN=538)
  [anchor_window] (primary)
    样本数: 2942
    Gold triples: 663 | Pred triples: 215
    Precision: 0.763
    Recall   : 0.247
    F1       : 0.374
    (TP=164, FP=51, FN=499)

[Layer 2B] Extraction detected_only
  说明: 只在 gold=True 且 pred=True 的样本上评估 span 质量，主要作为诊断视图。
  [strict_token_f1]
    样本数: 127
    Gold triples: 190 | Pred triples: 173
    Precision: 0.723
    Recall   : 0.658
    F1       : 0.689
    (TP=125, FP=48, FN=65)
  [anchor_window] (primary)
    样本数: 127
    Gold triples: 190 | Pred triples: 173
    Precision: 0.948
    Recall   : 0.863
    F1       : 0.904
    (TP=164, FP=9, FN=26)
================================================
```

## 生成失败统计
```json
{
  "total": 1742,
  "by_type": {
    "ConnectionResetError": 2,
    "URLError": 1740
  },
  "samples": [
    {
      "id": 1201,
      "error_type": "ConnectionResetError",
      "error_message": "[WinError 10054] 远程主机强迫关闭了一个现有的连接。"
    },
    {
      "id": 1202,
      "error_type": "ConnectionResetError",
      "error_message": "[WinError 10054] 远程主机强迫关闭了一个现有的连接。"
    },
    {
      "id": 1203,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1204,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1205,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1206,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1207,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1208,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1209,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1210,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1211,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1212,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1213,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1214,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1215,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1216,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1217,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1218,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1219,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1220,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1221,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1222,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1223,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1224,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1225,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1226,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1227,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1228,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1229,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1230,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1231,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1232,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1233,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1234,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1235,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1236,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1237,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1238,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1239,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1240,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1241,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1242,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1243,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1244,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1245,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1246,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1247,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1248,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1249,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1250,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1251,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1252,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1253,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1254,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1255,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1256,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1257,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1258,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1259,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1260,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1261,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1262,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1263,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1264,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1265,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1266,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1267,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1268,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1269,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1270,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1271,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1272,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1273,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1274,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1275,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1276,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1277,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1278,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1279,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1280,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1281,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1282,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1283,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1284,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1285,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1286,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1287,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1288,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1289,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1290,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1291,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1292,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1293,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1294,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1295,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1296,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1297,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1298,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1299,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1300,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1301,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1302,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1303,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1304,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1305,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1306,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1307,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1308,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1309,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1310,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1311,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1312,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1313,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1314,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1315,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1316,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1317,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1318,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1319,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1320,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1321,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1322,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1323,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1324,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1325,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1326,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1327,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1328,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1329,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1330,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1331,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1332,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1333,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1334,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1335,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1336,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1337,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1338,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1339,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1340,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1341,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1342,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1343,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1344,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1345,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1346,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1347,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1348,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1349,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1350,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1351,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1352,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1353,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1354,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1355,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1356,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1357,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1358,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1359,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1360,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1361,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1362,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1363,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1364,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1365,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1366,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1367,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1368,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1369,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1370,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1371,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1372,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1373,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1374,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1375,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1376,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1377,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1378,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1379,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1380,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1381,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1382,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1383,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1384,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1385,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1386,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1387,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1388,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1389,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1390,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1391,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1392,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1393,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1394,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1395,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1396,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1397,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1398,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1399,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1400,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1401,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1402,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1403,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1404,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1405,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1406,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1407,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1408,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1409,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1410,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1411,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1412,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1413,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1414,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1415,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1416,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1417,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1418,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1419,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1420,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1421,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1422,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1423,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1424,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1425,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1426,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1427,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1428,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1429,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1430,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1431,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1432,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1433,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1434,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1435,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1436,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1437,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1438,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1439,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1440,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1441,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1442,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1443,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1444,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1445,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1446,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1447,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1448,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1449,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1450,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1451,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1452,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1453,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1454,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1455,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1456,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1457,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1458,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1459,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1460,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1461,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1462,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1463,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1464,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1465,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1466,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1467,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1468,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1469,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1470,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1471,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1472,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1473,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1474,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1475,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1476,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1477,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1478,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1479,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1480,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1481,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1482,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1483,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1484,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1485,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1486,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1487,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1488,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1489,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1490,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1491,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1492,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1493,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1494,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1495,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1496,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1497,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1498,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1499,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1500,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1501,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1502,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1503,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1504,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1505,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1506,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1507,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1508,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1509,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1510,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1511,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1512,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1513,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1514,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1515,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1516,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1517,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1518,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1519,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1520,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1521,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1522,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1523,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1524,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1525,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1526,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1527,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1528,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1529,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1530,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1531,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1532,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1533,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1534,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1535,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1536,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1537,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1538,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1539,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1540,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1541,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1542,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1543,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1544,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1545,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1546,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1547,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1548,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1549,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1550,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1551,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1552,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1553,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1554,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1555,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1556,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1557,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1558,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1559,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1560,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1561,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1562,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1563,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1564,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1565,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1566,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1567,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1568,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1569,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1570,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1571,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1572,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1573,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1574,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1575,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1576,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1577,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1578,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1579,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1580,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1581,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1582,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1583,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1584,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1585,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1586,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1587,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1588,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1589,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1590,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1591,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1592,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1593,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1594,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1595,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1596,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1597,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1598,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1599,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1600,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1601,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1602,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1603,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1604,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1605,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1606,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1607,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1608,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1609,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1610,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1611,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1612,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1613,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1614,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1615,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1616,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1617,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1618,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1619,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1620,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1621,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1622,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1623,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1624,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1625,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1626,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1627,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1628,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1629,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1630,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1631,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1632,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1633,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1634,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1635,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1636,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1637,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1638,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1639,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1640,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1641,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1642,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1643,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1644,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1645,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1646,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1647,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1648,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1649,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1650,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1651,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1652,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1653,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1654,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1655,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1656,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1657,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1658,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1659,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1660,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1661,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1662,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1663,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1664,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1665,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1666,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1667,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1668,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1669,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1670,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1671,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1672,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1673,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1674,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1675,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1676,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1677,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1678,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1679,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1680,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1681,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1682,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1683,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1684,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1685,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1686,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1687,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1688,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1689,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1690,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1691,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1692,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1693,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1694,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1695,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1696,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1697,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1698,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1699,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1700,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1701,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1702,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1703,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1704,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1705,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1706,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1707,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1708,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1709,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1710,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1711,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1712,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1713,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1714,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1715,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1716,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1717,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1718,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1719,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1720,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1721,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1722,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1723,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1724,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1725,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1726,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1727,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1728,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1729,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1730,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1731,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1732,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1733,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1734,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1735,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1736,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1737,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1738,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1739,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1740,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1741,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1742,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1743,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1744,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1745,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1746,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1747,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1748,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1749,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1750,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1751,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1752,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1753,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1754,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1755,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1756,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1757,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1758,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1759,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1760,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1761,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1762,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1763,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1764,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1765,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1766,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1767,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1768,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1769,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1770,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1771,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1772,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1773,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1774,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1775,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1776,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1777,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1778,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1779,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1780,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1781,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1782,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1783,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1784,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1785,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1786,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1787,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1788,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1789,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1790,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1791,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1792,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1793,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1794,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1795,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1796,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1797,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1798,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1799,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1800,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1801,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1802,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1803,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1804,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1805,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1806,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1807,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1808,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1809,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1810,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1811,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1812,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1813,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1814,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1815,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1816,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1817,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1818,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1819,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1820,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1821,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1822,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1823,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1824,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1825,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1826,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1827,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1828,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1829,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1830,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1831,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1832,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1833,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1834,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1835,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1836,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1837,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1838,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1839,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1840,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1841,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1842,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1843,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1844,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1845,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1846,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1847,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1848,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1849,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1850,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1851,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1852,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1853,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1854,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1855,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1856,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1857,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1858,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1859,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1860,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1861,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1862,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1863,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1864,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1865,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1866,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1867,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1868,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1869,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1870,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1871,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1872,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1873,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1874,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1875,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1876,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1877,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1878,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1879,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1880,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1881,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1882,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1883,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1884,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1885,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1886,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1887,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1888,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1889,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1890,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1891,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1892,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1893,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1894,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1895,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1896,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1897,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1898,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1899,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1900,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1901,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1902,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1903,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1904,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1905,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1906,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1907,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1908,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1909,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1910,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1911,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1912,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1913,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1914,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1915,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1916,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1917,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1918,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1919,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1920,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1921,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1922,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1923,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1924,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1925,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1926,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1927,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1928,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1929,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1930,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1931,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1932,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1933,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1934,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1935,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1936,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1937,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1938,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1939,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1940,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1941,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1942,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1943,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1944,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1945,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1946,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1947,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1948,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1949,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1950,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1951,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1952,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1953,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1954,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1955,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1956,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1957,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1958,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1959,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1960,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1961,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1962,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1963,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1964,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1965,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1966,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1967,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1968,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1969,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1970,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1971,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1972,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1973,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1974,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1975,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1976,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1977,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1978,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1979,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1980,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1981,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1982,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1983,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1984,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1985,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1986,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1987,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1988,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1989,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1990,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1991,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1992,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1993,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1994,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1995,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1996,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1997,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1998,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 1999,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2000,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2001,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2010,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2013,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2015,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2020,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2022,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2024,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2025,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2028,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2030,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2033,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2036,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2040,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2041,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2044,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2045,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2047,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2050,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2053,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2056,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2057,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2060,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2061,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2067,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2069,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2076,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2079,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2082,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2083,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2087,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2088,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2095,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2096,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2105,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2106,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2112,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2118,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2121,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2122,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2125,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2132,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2143,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2145,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2149,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2150,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2153,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2156,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2167,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2178,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2181,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2184,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2185,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2187,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2199,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2210,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2212,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2213,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2216,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2226,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2227,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2229,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2245,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2248,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2253,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2261,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2262,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2265,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2267,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2271,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2273,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2276,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2287,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2294,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2295,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2300,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2305,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2307,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2319,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2326,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2330,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2334,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2335,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2336,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2339,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2341,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2346,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2352,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2377,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2378,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2382,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2394,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2395,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2399,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2401,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2403,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2410,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2412,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2413,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2416,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2420,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2423,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2427,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2430,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2434,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2436,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2444,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2447,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2448,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2449,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2450,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2451,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2452,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2456,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2460,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2461,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2465,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2466,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2471,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2475,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2478,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2480,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2482,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2486,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2487,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2488,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2493,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2496,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2502,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2504,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2505,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2506,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2515,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2517,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2519,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2520,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2523,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2527,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2528,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2537,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2538,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2540,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2542,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2547,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2549,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2553,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2555,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2558,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2559,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2569,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2570,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2572,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2592,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2596,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2597,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2601,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2602,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2603,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2604,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2613,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2621,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2628,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2629,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2631,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2632,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2633,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2634,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2636,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2638,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2641,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2643,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2644,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2648,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2652,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2656,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2657,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2658,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2666,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2669,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2673,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2674,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2684,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2695,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2706,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2709,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2710,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2714,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2724,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2725,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2728,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2732,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2734,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2737,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2745,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2746,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2755,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2760,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2763,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2768,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2777,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2783,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2788,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2789,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2798,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2800,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2802,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2809,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2814,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2816,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2827,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2830,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2831,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2840,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2843,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2844,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2853,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2857,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2858,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2859,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2860,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2863,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2864,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2868,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2869,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2879,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2882,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2883,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2884,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2890,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2893,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2899,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2907,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2912,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2913,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2914,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2920,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2923,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2940,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2942,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2945,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2946,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2947,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2948,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2950,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2952,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2956,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2963,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2967,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2970,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2972,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2973,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2976,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2978,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2980,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2986,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2987,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2989,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2990,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2991,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2993,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2997,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 2999,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3011,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3013,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3019,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3032,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3033,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3035,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3037,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3039,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3053,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3057,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3066,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3071,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3084,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3085,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3088,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3092,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3093,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3097,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3098,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3101,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3104,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3107,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3116,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3117,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3125,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3129,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3131,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3132,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3135,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3141,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3143,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3145,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3151,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3154,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3156,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3157,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3159,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3161,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3163,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3174,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3176,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3187,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3199,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3202,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3204,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3206,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3209,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3220,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3222,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3228,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3232,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3240,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3248,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3251,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3252,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3253,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3262,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3269,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3271,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3274,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3287,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3290,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3293,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3298,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3300,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3309,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3310,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3311,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3312,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3317,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3327,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3332,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3341,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3343,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3346,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3350,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3353,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3356,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3359,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3367,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3368,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3370,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3373,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3379,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3383,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3386,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3389,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3393,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3397,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3398,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3401,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3404,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3407,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3409,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3410,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3414,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3419,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3429,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3432,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3443,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3449,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3453,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3454,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3457,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3467,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3468,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3473,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3478,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3481,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3486,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3487,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3488,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3489,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3497,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3501,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3502,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3503,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3504,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3508,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3511,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3524,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3528,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3530,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3534,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3536,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3544,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3559,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3564,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3567,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3570,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3574,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3577,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3580,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3585,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3599,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3600,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3602,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3607,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3610,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3613,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3618,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3620,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3622,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3632,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3641,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3644,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3647,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3652,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3653,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3663,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3665,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3680,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3685,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3687,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3693,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3698,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3700,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3703,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3705,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3707,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3712,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3722,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3724,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3727,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3731,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3735,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3741,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3746,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3747,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3749,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3752,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3754,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3757,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3762,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3763,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3769,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3771,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3780,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3781,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3785,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3793,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3794,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3798,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3802,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3804,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3810,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3813,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3815,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3818,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3820,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3823,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3824,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3830,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3846,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3847,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3851,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3858,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3859,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3860,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3864,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3866,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3872,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3875,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3885,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3887,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3891,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3893,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3902,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3908,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3911,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3915,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3916,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3925,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3926,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3932,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3933,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3934,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3935,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3938,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3939,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3942,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3945,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3951,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3952,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3958,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3969,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3970,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3973,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3975,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3982,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3986,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3989,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 3992,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4000,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4007,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4008,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4011,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4013,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4015,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4023,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4024,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4025,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4031,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4046,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4053,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4054,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4062,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4068,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4073,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4075,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4079,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4082,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4091,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4093,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4100,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4102,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4104,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4107,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4108,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4112,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4116,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4135,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4136,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4137,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4139,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4141,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4144,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4148,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4149,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4152,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4154,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4171,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4172,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4173,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4178,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4187,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4191,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4198,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4203,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4205,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4212,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4227,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4231,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4244,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4256,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4268,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4270,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4273,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4276,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4287,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4289,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4293,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4298,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4299,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4301,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4302,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4303,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4306,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4307,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4311,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4313,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4316,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4323,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4324,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4325,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4328,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4333,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4335,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4340,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4354,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4356,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4359,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4361,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4362,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4363,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4364,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4365,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4369,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4372,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4374,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4389,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4390,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4392,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4394,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4398,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4400,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4401,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4404,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4408,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4409,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4410,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4418,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4420,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4427,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4428,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4432,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4440,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4441,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4444,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4453,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4459,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4460,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4464,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4465,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4473,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4477,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4481,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4482,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4487,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4490,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4496,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4502,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4503,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4507,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4512,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4515,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4520,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4522,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4524,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4526,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4527,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4528,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4535,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4536,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4537,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4538,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4540,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4545,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4548,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4551,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4562,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4564,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4565,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4575,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4578,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4581,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4585,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4589,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4596,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4598,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4599,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4601,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4602,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4604,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4607,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4614,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4616,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4623,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4629,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4630,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4642,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4645,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4646,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4648,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4659,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4665,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4666,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4667,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4668,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4671,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4675,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4681,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4684,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4685,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4692,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4693,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4695,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4696,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4701,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4712,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4713,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4725,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4734,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4735,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4736,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4739,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4741,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4742,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4743,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4747,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4748,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4750,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4760,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4768,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4776,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4778,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4780,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4783,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4797,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4798,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4799,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4801,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4804,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4808,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4811,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4814,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4816,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4818,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4821,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4823,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4827,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4845,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4854,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4855,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4859,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4860,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4865,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4867,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4868,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4869,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4870,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4871,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4878,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4884,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4885,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4886,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4891,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4894,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4905,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4912,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4913,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4921,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4922,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4932,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4938,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4939,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4941,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4947,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4949,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4954,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4958,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4963,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4969,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4973,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4974,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4977,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4979,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4980,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4987,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4988,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 4990,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5002,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5004,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5009,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5019,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5023,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5025,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5027,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5030,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5038,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5041,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5042,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5048,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5054,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5055,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5057,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5058,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5060,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5071,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5074,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5076,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5077,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5085,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5086,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5088,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5095,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5098,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5103,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5107,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5108,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5110,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5111,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5132,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5133,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5134,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5137,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5139,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5144,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5147,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5151,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5152,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5156,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5165,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5171,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5177,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5178,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5180,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5183,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5186,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5187,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5190,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5198,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5205,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5208,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5211,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5212,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5214,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5215,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5217,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5218,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5219,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5220,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5222,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5224,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5228,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5229,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5233,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5244,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5246,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5249,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5253,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5260,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5262,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5266,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5267,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5270,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5273,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5274,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5276,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5299,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5300,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5302,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5306,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5311,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5316,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5318,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5319,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5322,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5326,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5336,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5339,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5343,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5346,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5347,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5361,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5364,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5370,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5376,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5382,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5385,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5396,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5402,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5404,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5418,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5421,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5423,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5438,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5440,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5442,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5461,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5464,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5466,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5475,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5480,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5489,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5492,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5501,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5503,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5514,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5517,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5534,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5537,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5538,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5541,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5545,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5547,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5551,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5552,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5557,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5558,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5571,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5576,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5580,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5581,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5613,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5617,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5618,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5626,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5631,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5635,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5637,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5638,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5639,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5641,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5656,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5658,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5660,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5661,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5670,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5673,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5674,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5683,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5685,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5687,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5690,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5693,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5696,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5697,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5698,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5700,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5706,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5712,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5713,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5724,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5725,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5737,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5738,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5745,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5749,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5750,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5760,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5763,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5765,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5768,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5779,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5781,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5784,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5785,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5787,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5790,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5793,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5804,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5806,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5808,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5813,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5822,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5824,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5826,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5827,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5834,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5838,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5840,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5848,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5852,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5854,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5858,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5866,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5868,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5872,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5876,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    },
    {
      "id": 5879,
      "error_type": "URLError",
      "error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
    }
  ]
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

Sample details shown: first 200 of 1833 wrong samples from 2942 total samples.

### --- id=9 ---

输入文本: We present a fatal case of subacute methanol toxicity with associated diffuse brain involvement, including bilateral putaminal necrosis and cerebral edema with ventricular compression.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 4,
    "fp": 1,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 5,
    "fp": 0,
    "fn": 1
  },
  "token_f1_counts": {
    "tp": 4,
    "fp": 1,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "methanol",
      "effect": "bilateral putaminal necrosis"
    },
    {
      "cause": "methanol",
      "effect": "cerebral edema"
    },
    {
      "cause": "methanol",
      "effect": "diffuse brain involvement"
    },
    {
      "cause": "methanol",
      "effect": "fatal"
    },
    {
      "cause": "methanol",
      "effect": "methanol toxicity"
    },
    {
      "cause": "methanol",
      "effect": "ventricular compression"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "fatal"
      }
    },
    {
      "cause": {
        "span": "methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "subacute methanol toxicity"
      }
    },
    {
      "cause": {
        "span": "methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "diffuse brain involvement"
      }
    },
    {
      "cause": {
        "span": "methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "bilateral putaminal necrosis"
      }
    },
    {
      "cause": {
        "span": "methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "cerebral edema with ventricular compression"
      }
    }
  ]
}
```

### --- id=17 ---

输入文本: Attempts were made to stop and then restart the theophylline therapy at progressively lower doses; however, with each attempt, the patient's reaction to the drug became more toxic, with serum theophylline levels ranging between 99.9 and 149.9 micromol/L (18 and 27 microg/mL).

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
      "cause": "theophylline",
      "effect": "reaction to the drug became more toxic"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "theophylline"
      },
      "relation": "caused",
      "effect": {
        "span": "toxic"
      }
    }
  ]
}
```

### --- id=83 ---

输入文本: The cough continued for the duration of therapy with quinapril.

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
      "cause": "quinapril",
      "effect": "cough"
    }
  ],
  "pred_triples": []
}
```

### --- id=121 ---

输入文本: Just over 1 year following completion of his treatment, falling platelet and white cell counts were associated with the development of dysplastic features in his bone marrow and a rising blast cell count, culminating in the development of acute myeloid leukemia (AML).

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
        "span": "treatment"
      },
      "relation": "caused",
      "effect": {
        "span": "dysplastic features"
      }
    },
    {
      "cause": {
        "span": "treatment"
      },
      "relation": "caused",
      "effect": {
        "span": "acute myeloid leukemia"
      }
    }
  ]
}
```

### --- id=142 ---

输入文本: Osteonecrosis of the jaw is an uncommon consequence of biphosphonate therapy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "biphosphonate"
      },
      "relation": "caused",
      "effect": {
        "span": "Osteonecrosis of the jaw"
      }
    }
  ]
}
```

### --- id=154 ---

输入文本: The use of beclomethasone diproprionate inhaler complicated by the development of an eosinophilic pneumonia reaction.

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
      "cause": "beclomethasone diproprionate",
      "effect": "eosinophilic pneumonia reaction"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "beclomethasone diproprionate inhaler"
      },
      "relation": "caused",
      "effect": {
        "span": "eosinophilic pneumonia"
      }
    }
  ]
}
```

### --- id=169 ---

输入文本: Fatal spontaneous spinal epidural hematoma following thrombolysis for myocardial infarction.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "thrombolysis"
      },
      "relation": "caused",
      "effect": {
        "span": "spinal epidural hematoma"
      }
    }
  ]
}
```

### --- id=211 ---

输入文本: Administration of intravenous nitroglycerin in a patient with idiopathic pulmonary hypertension resulted in an increase in pulmonary artery pressure associated with a decrease in blood flow that is best explained by an increase in pulmonary vascular resistance.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "nitroglycerin",
      "effect": "decrease in blood flow"
    },
    {
      "cause": "nitroglycerin",
      "effect": "increase in pulmonary artery pressure"
    },
    {
      "cause": "nitroglycerin",
      "effect": "increase in pulmonary vascular resistance"
    }
  ],
  "pred_triples": []
}
```

### --- id=240 ---

输入文本: Three children presented with adrenal crises, manifested by vomiting and hypoglycaemia, after protracted courses of high-dose inhaled corticosteroids for asthma.

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
        "span": "high-dose inhaled corticosteroids"
      },
      "relation": "caused",
      "effect": {
        "span": "adrenal crises"
      }
    },
    {
      "cause": {
        "span": "high-dose inhaled corticosteroids"
      },
      "relation": "caused",
      "effect": {
        "span": "vomiting"
      }
    },
    {
      "cause": {
        "span": "high-dose inhaled corticosteroids"
      },
      "relation": "caused",
      "effect": {
        "span": "hypoglycaemia"
      }
    }
  ]
}
```

### --- id=244 ---

输入文本: We describe a 35-year-old woman who developed severe thrombotic complications due to heparinization and unrecognized HDAs.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "heparinization"
      },
      "relation": "caused",
      "effect": {
        "span": "severe thrombotic complications"
      }
    }
  ]
}
```

### --- id=273 ---

输入文本: Myoglobinuria and acute renal failure associated with intravenous vasopressin infusion.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "vasopressin",
      "effect": "acute renal failure"
    },
    {
      "cause": "vasopressin",
      "effect": "Myoglobinuria"
    }
  ],
  "pred_triples": []
}
```

### --- id=274 ---

输入文本: Although they had only a few nodules at diagnosis, the nodules increased in number and size 3 to 4 months after the start of methotrexate therapy in both patients.

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
      "cause": "methotrexate",
      "effect": "nodules"
    }
  ],
  "pred_triples": []
}
```

### --- id=277 ---

输入文本: These evolutional changes in both proteinuria and glomerular histology suggest a close linkage between the M-CSF treatment and macrophage-related glomerular injury.

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
      "cause": "M-CSF",
      "effect": "macrophage-related glomerular injury"
    }
  ],
  "pred_triples": []
}
```

### --- id=286 ---

输入文本: A retrospective review of TTP patients with quinine-associated thrombotic microangiopathy (TMA) for whom ADAMTS13 was measured before plasma exchange was performed.

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
      "cause": "quinine",
      "effect": "thrombotic microangiopathy"
    },
    {
      "cause": "quinine",
      "effect": "TMA"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "quinine"
      },
      "relation": "caused",
      "effect": {
        "span": "thrombotic microangiopathy"
      }
    }
  ]
}
```

### --- id=291 ---

输入文本: We report a cae of paranoid psychosis following use of a decongestant containing PPA and summarize the case report literature of psychiatric adverse effects to PPA in which doses were known and stated to be within recommended guidelines.

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
      "cause": "PPA",
      "effect": "paranoid psychosis"
    },
    {
      "cause": "PPA",
      "effect": "psychiatric adverse effects"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "PPA"
      },
      "relation": "caused",
      "effect": {
        "span": "paranoid psychosis"
      }
    }
  ]
}
```

### --- id=292 ---

输入文本: Pentavalent antimonial drugs used for the treatment of leishmaniasis have been associated with sudden deaths, probably due to the development of ventricular tachyarrhythmias.

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
        "span": "Pentavalent antimonial drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "sudden deaths"
      }
    },
    {
      "cause": {
        "span": "Pentavalent antimonial drugs"
      },
      "relation": "caused",
      "effect": {
        "span": "ventricular tachyarrhythmias"
      }
    }
  ]
}
```

### --- id=299 ---

输入文本: Thrombotic thrombocytopenic purpura induced by trimethoprim-sulfamethoxazole in a Jehovah's Witness.

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
      "cause": "sulfamethoxazole",
      "effect": "Thrombotic thrombocytopenic purpura"
    },
    {
      "cause": "trimethoprim",
      "effect": "Thrombotic thrombocytopenic purpura"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "trimethoprim-sulfamethoxazole"
      },
      "relation": "caused",
      "effect": {
        "span": "Thrombotic thrombocytopenic purpura"
      }
    }
  ]
}
```

### --- id=301 ---

输入文本: We report four cases of severe corneal ulceration in methamphetamine abusers.

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
      "cause": "methamphetamine",
      "effect": "severe corneal ulceration"
    }
  ],
  "pred_triples": []
}
```

### --- id=323 ---

输入文本: Thus, we confirm that desensitization may be a safe procedure in patients with cancer who experience methotrexate-induced anaphylaxis.

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
      "cause": "methotrexate",
      "effect": "anaphylaxis"
    }
  ],
  "pred_triples": []
}
```

### --- id=329 ---

输入文本: A clinically atypical, neuropathologically verified case of Creutzfeldt-Jakob disease is described in a 32-year-old New Zealand woman with idiopathic hypopituitarism who had been treated in late adolescence (1970 to 1973) with human growth hormone processed from pooled cadaveric pituitary glands.

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
      "cause": "human growth hormone",
      "effect": "Creutzfeldt-Jakob disease"
    }
  ],
  "pred_triples": []
}
```

### --- id=332 ---

输入文本: A case of pseudotumor cerebri following glucocorticoid therapy in which warfarin prevented recurrence.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "glucocorticoid therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "pseudotumor cerebri"
      }
    }
  ]
}
```

### --- id=346 ---

输入文本: Since ethambutol is actively excreted via the renal system, compromise of renal function such as due to renal tuberculosis may lead to serum concentration elevations of ethambutol sufficient to produce optic neuropathy.

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
      "cause": "ethambutol",
      "effect": "optic neuropathy"
    }
  ],
  "pred_triples": []
}
```

### --- id=365 ---

输入文本: Severe adenovirus pneumonia (AVP) following infliximab infusion for the treatment of Crohn's disease.

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
      "cause": "infliximab",
      "effect": "AVP"
    },
    {
      "cause": "infliximab",
      "effect": "Severe adenovirus pneumonia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "infliximab"
      },
      "relation": "caused",
      "effect": {
        "span": "Severe adenovirus pneumonia"
      }
    }
  ]
}
```

### --- id=390 ---

输入文本: The purpose of this work is to report the case of oral chemical burns caused by topical self-medication for tooth pain relief, and also to discuss the clinical presentation and the treatment performed.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "topical self-medication"
      },
      "relation": "caused",
      "effect": {
        "span": "oral chemical burns"
      }
    }
  ]
}
```

### --- id=396 ---

输入文本: Thus, an immunological mechanism might be involved in the mechanism of pirmenol-induced QT prolongation and T wave inversion on the electrocardiogram.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "pirmenol",
      "effect": "QT prolongation"
    },
    {
      "cause": "pirmenol",
      "effect": "T wave inversion"
    }
  ],
  "pred_triples": []
}
```

### --- id=399 ---

输入文本: Therefore, although garenoxacin reportedly causes fewer adverse reactions for cardiac rhythms than third-generation quinolone antibiotics, one must be cautious of the interference of other drugs during hypokalemia in order to prevent TdP.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "garenoxacin",
      "effect": "cardiac rhythms"
    },
    {
      "cause": "garenoxacin",
      "effect": "hypokalemia"
    }
  ],
  "pred_triples": []
}
```

### --- id=410 ---

输入文本: Graft versus host-like illness in a child with phenobarbital hypersensitivity.

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
      "cause": "phenobarbital",
      "effect": "Graft versus host-like illness"
    },
    {
      "cause": "phenobarbital",
      "effect": "hypersensitivity"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "phenobarbital"
      },
      "relation": "caused",
      "effect": {
        "span": "Graft versus host-like illness"
      }
    }
  ]
}
```

### --- id=419 ---

输入文本: CONCLUSIONS: Clinicians should be aware that Crohn's disease is a potential novel adverse drug effect of Copaxone.

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
      "cause": "Copaxone",
      "effect": "Crohn's disease"
    }
  ],
  "pred_triples": []
}
```

### --- id=420 ---

输入文本: Report of two cases of male breast cancer after prolonged estrogen treatment for prostatic carcinoma.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "estrogen"
      },
      "relation": "caused",
      "effect": {
        "span": "male breast cancer"
      }
    }
  ]
}
```

### --- id=436 ---

输入文本: Methanol toxicity can cause severe central nervous system insult in which a characteristic pattern of bilateral putaminal injury is noted on brain imaging studies.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "Methanol",
      "effect": "bilateral putaminal injury"
    },
    {
      "cause": "Methanol",
      "effect": "Methanol toxicity"
    },
    {
      "cause": "Methanol",
      "effect": "severe central nervous system insult"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "severe central nervous system insult"
      }
    },
    {
      "cause": {
        "span": "Methanol"
      },
      "relation": "caused",
      "effect": {
        "span": "bilateral putaminal injury"
      }
    }
  ]
}
```

### --- id=469 ---

输入文本: We review the existing literature on this rare clinical entity, all-trans retinoic acid-induced myositis.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "all-trans retinoic acid"
      },
      "relation": "caused",
      "effect": {
        "span": "myositis"
      }
    }
  ]
}
```

### --- id=490 ---

输入文本: These features have not previously been reported as side effects of glibenclamide therapy, but intrahepatic cholestasis may occur with chlorpropamide, a similar sulphonylurea agent.

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
      "cause": "chlorpropamide",
      "effect": "intrahepatic cholestasis"
    }
  ],
  "pred_triples": []
}
```

### --- id=493 ---

输入文本: Hepatocellular carcinoma in a young woman with prolonged exposure to oral contraceptives.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "oral contraceptives"
      },
      "relation": "caused",
      "effect": {
        "span": "Hepatocellular carcinoma"
      }
    }
  ]
}
```

### --- id=499 ---

输入文本: A 3-year-old boy developed alopecia areata (AA) universalis in the convalescent status of phenobarbital-induced AHS, compatible to the evidences of increased lymphocyte proliferation and increased dead cells percentages while his peripheral blood mononuclear cells were incubated with phenobarbital.

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
        "span": "phenobarbital"
      },
      "relation": "caused",
      "effect": {
        "span": "AHS"
      }
    },
    {
      "cause": {
        "span": "phenobarbital"
      },
      "relation": "caused",
      "effect": {
        "span": "alopecia areata (AA) universalis"
      }
    }
  ]
}
```

### --- id=501 ---

输入文本: A 40-year-old man who developed acute myelomonoblastic leukemia (M4) after 7 years of treatment for multiple myeloma with the alkylating agent melphalan and steroids is presented.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "melphalan"
      },
      "relation": "caused",
      "effect": {
        "span": "acute myelomonoblastic leukemia"
      }
    }
  ]
}
```

### --- id=513 ---

输入文本: Renal toxicities have been reported in less than one percent of the patients receiving ciprofloxacin therapy.

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
      "cause": "ciprofloxacin",
      "effect": "Renal toxicities"
    }
  ],
  "pred_triples": []
}
```

### --- id=522 ---

输入文本: We present 2 patients with demonstrated IgE-mediated allergy to cloxacillin and tolerance to amoxicillin and cefuroxime.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "cloxacillin"
      },
      "relation": "caused",
      "effect": {
        "span": "IgE-mediated allergy"
      }
    }
  ]
}
```

### --- id=534 ---

输入文本: We report a case of a 35-year old female who developed new onset type II diabetes mellitus with hyperosmolar hyperglycaemic coma and acute renal failure following treatment with a SGA for a first manic episode.

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
        "span": "SGA"
      },
      "relation": "caused",
      "effect": {
        "span": "type II diabetes mellitus"
      }
    },
    {
      "cause": {
        "span": "SGA"
      },
      "relation": "caused",
      "effect": {
        "span": "hyperosmolar hyperglycaemic coma"
      }
    },
    {
      "cause": {
        "span": "SGA"
      },
      "relation": "caused",
      "effect": {
        "span": "acute renal failure"
      }
    }
  ]
}
```

### --- id=547 ---

输入文本: The probable proarrhythmic action of amiodarone, although rare, is reviewed along with a discussion of the novel use of intravenous magnesium sulfate therapy.

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
      "cause": "amiodarone",
      "effect": "proarrhythmic"
    }
  ],
  "pred_triples": []
}
```

### --- id=548 ---

输入文本: We report an unusual case of a leiomyosarcoma of the urinary bladder after chemotherapy for retinoblastoma and the results of a review of the published reports of bladder sarcomas.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "chemotherapy"
      },
      "relation": "caused",
      "effect": {
        "span": "leiomyosarcoma of the urinary bladder"
      }
    }
  ]
}
```

### --- id=549 ---

输入文本: The case of a patient with apparent cocaine toxicity and drug-mediated hypertension and tachycardia is presented.

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
        "span": "cocaine"
      },
      "relation": "caused",
      "effect": {
        "span": "cocaine toxicity"
      }
    },
    {
      "cause": {
        "span": "cocaine"
      },
      "relation": "caused",
      "effect": {
        "span": "hypertension"
      }
    },
    {
      "cause": {
        "span": "cocaine"
      },
      "relation": "caused",
      "effect": {
        "span": "tachycardia"
      }
    }
  ]
}
```

### --- id=563 ---

输入文本: Ocular toxicity by latex of Calotropis procera (Sodom apple).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "latex of Calotropis procera"
      },
      "relation": "caused",
      "effect": {
        "span": "Ocular toxicity"
      }
    }
  ]
}
```

### --- id=590 ---

输入文本: Leukaemoid monocytosis in M4 AML following chemotherapy and G-CSF.

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
      "cause": "G-CSF",
      "effect": "Leukaemoid monocytosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=591 ---

输入文本: We describe longitudinal diffusion-weighted MRI findings of sub-acute leukoencephalopathy following methotrexate therapy in a 24-year-old man diagnosed with pre-B-cell acute lymphoblastic leukemia (ALL), presenting with right-sided paralysis and aphasia after second consolidation with intrathecal triple-drug therapy given intrathecally.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 2,
    "fn": 0
  },
  "gold_relations": [
    {
      "cause": "methotrexate",
      "effect": "sub-acute leukoencephalopathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "methotrexate"
      },
      "relation": "caused",
      "effect": {
        "span": "sub-acute leukoencephalopathy"
      }
    },
    {
      "cause": {
        "span": "intrathecal triple-drug therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "right-sided paralysis"
      }
    },
    {
      "cause": {
        "span": "intrathecal triple-drug therapy"
      },
      "relation": "caused",
      "effect": {
        "span": "aphasia"
      }
    }
  ]
}
```

### --- id=611 ---

输入文本: Ovarian endometrioid carcinoma and endometriosis developing in a postmenopausal breast cancer patient during tamoxifen therapy: a case report and review of the literature.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "tamoxifen",
      "effect": "endometriosis"
    },
    {
      "cause": "tamoxifen",
      "effect": "Ovarian endometrioid carcinoma"
    }
  ],
  "pred_triples": []
}
```

### --- id=652 ---

输入文本: Reversible leukopenia was documented in an 81-year-old woman treated with adjunctive ibopamine 100 mg t.i.d. for chronic congestive heart failure.

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
      "cause": "ibopamine",
      "effect": "Reversible leukopenia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "ibopamine"
      },
      "relation": "caused",
      "effect": {
        "span": "leukopenia"
      }
    }
  ]
}
```

### --- id=668 ---

输入文本: Reviewing data on these patients and recent literature indicate that fatal marrow aplasia seems to occur more frequently in sero-negative women who respond well to therapy with gold salts.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "gold salts"
      },
      "relation": "caused",
      "effect": {
        "span": "fatal marrow aplasia"
      }
    }
  ]
}
```

### --- id=682 ---

输入文本: The symptoms were attributed to hepatitis B vaccination.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "hepatitis B vaccination"
      },
      "relation": "caused",
      "effect": {
        "span": "symptoms"
      }
    }
  ]
}
```

### --- id=719 ---

输入文本: Possible serotonin syndrome associated with clomipramine after withdrawal of clozapine.

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
      "cause": "clomipramine",
      "effect": "serotonin syndrome"
    },
    {
      "cause": "clozapine",
      "effect": "serotonin syndrome"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "clomipramine"
      },
      "relation": "caused",
      "effect": {
        "span": "serotonin syndrome"
      }
    }
  ]
}
```

### --- id=761 ---

输入文本: A few recent individual case reports have suggested that a myasthenic syndrome may be associated with statin treatment, but this association is not well described.

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
      "cause": "statin",
      "effect": "myasthenic syndrome"
    }
  ],
  "pred_triples": []
}
```

### --- id=777 ---

输入文本: These findings support previous studies that showed that the use of aspirin during the antecedent illness may be a risk factor for the development of RS.

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
      "cause": "aspirin",
      "effect": "RS"
    }
  ],
  "pred_triples": []
}
```

### --- id=789 ---

输入文本: Lithium is known to cause acute renal failure and tubulo-interstitial disease, but the recently described association with proteinuria or nephrotic syndrome is little recognized.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "anchor_window_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "token_f1_counts": {
    "tp": 2,
    "fp": 0,
    "fn": 2
  },
  "gold_relations": [
    {
      "cause": "Lithium",
      "effect": "acute renal failure"
    },
    {
      "cause": "Lithium",
      "effect": "nephrotic syndrome"
    },
    {
      "cause": "Lithium",
      "effect": "proteinuria"
    },
    {
      "cause": "Lithium",
      "effect": "tubulo-interstitial disease"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "Lithium"
      },
      "relation": "caused",
      "effect": {
        "span": "acute renal failure"
      }
    },
    {
      "cause": {
        "span": "Lithium"
      },
      "relation": "caused",
      "effect": {
        "span": "tubulo-interstitial disease"
      }
    }
  ]
}
```

### --- id=794 ---

输入文本: Intravenous sodium bicarbonate appears to be indicated prophylactically in combating the associated metabolic acidosis due to absorbed formic acid.

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
      "cause": "formic acid",
      "effect": "metabolic acidosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=804 ---

输入文本: Panic anxiety after abrupt discontinuation of mianserin.

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
      "cause": "mianserin",
      "effect": "Panic anxiety"
    }
  ],
  "pred_triples": []
}
```

### --- id=816 ---

输入文本: We report a case of successful surgical management of arterial thrombosis after percutaneous thrombin injection of a femoral artery pseudoaneurysm in a 69-year-old woman.

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
      "cause": "thrombin",
      "effect": "arterial thrombosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=827 ---

输入文本: Sulfasalazine has been associated with bronchopulmonary complications of inflammatory bowel disease (IBD) in adults.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "Sulfasalazine",
      "effect": "bronchopulmonary complications of inflammatory bowel disease"
    },
    {
      "cause": "Sulfasalazine",
      "effect": "IBD"
    }
  ],
  "pred_triples": []
}
```

### --- id=841 ---

输入文本: After calling the salon and consulting Poisindex, the substance was found to be Mar-V-cide, containing 20% Hyamine 3500, 50% cationic detergents, 20% isopropyl alcohol, and 1% sodium nitrite, which caused the methemoglobinemia in this case.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 5,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "Mar-V-cide"
      },
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
    },
    {
      "cause": {
        "span": "Hyamine 3500"
      },
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
    },
    {
      "cause": {
        "span": "cationic detergents"
      },
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
    },
    {
      "cause": {
        "span": "isopropyl alcohol"
      },
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
    },
    {
      "cause": {
        "span": "sodium nitrite"
      },
      "relation": "caused",
      "effect": {
        "span": "methemoglobinemia"
      }
    }
  ]
}
```

### --- id=854 ---

输入文本: Vaccine-associated herpes zoster ophthalmicus [correction of opthalmicus] and encephalitis in an immunocompetent child.

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
        "span": "Vaccine"
      },
      "relation": "caused",
      "effect": {
        "span": "herpes zoster ophthalmicus"
      }
    },
    {
      "cause": {
        "span": "Vaccine"
      },
      "relation": "caused",
      "effect": {
        "span": "encephalitis"
      }
    }
  ]
}
```

### --- id=859 ---

输入文本: We report the use of pamidronate for acute, severe hypercalcemia secondary to iatrogenic vitamin D poisoning.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "vitamin D",
      "effect": "severe hypercalcemia"
    },
    {
      "cause": "vitamin D",
      "effect": "vitamin D poisoning"
    }
  ],
  "pred_triples": []
}
```

### --- id=880 ---

输入文本: Cerebrovascular complications of L-asparaginase therapy in children with leukemia: aphasia and other neuropsychological deficits.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "L-asparaginase",
      "effect": "aphasia"
    },
    {
      "cause": "L-asparaginase",
      "effect": "Cerebrovascular complications"
    },
    {
      "cause": "L-asparaginase",
      "effect": "neuropsychological deficits"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "L-asparaginase"
      },
      "relation": "caused",
      "effect": {
        "span": "aphasia"
      }
    },
    {
      "cause": {
        "span": "L-asparaginase"
      },
      "relation": "caused",
      "effect": {
        "span": "neuropsychological deficits"
      }
    }
  ]
}
```

### --- id=883 ---

输入文本: Atrioventricular block complicating amiodarone-induced hypothyroidism in a patient with pre-excitation and rate-dependent bilateral bundle branch block.

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
      "cause": "amiodarone",
      "effect": "Atrioventricular block"
    },
    {
      "cause": "amiodarone",
      "effect": "hypothyroidism"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "amiodarone"
      },
      "relation": "caused",
      "effect": {
        "span": "amiodarone-induced hypothyroidism"
      }
    }
  ]
}
```

### --- id=893 ---

输入文本: It is likely that the selective nephrotoxicity in these 3 patients with SIADH was induced by tetracycline.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "tetracycline"
      },
      "relation": "caused",
      "effect": {
        "span": "selective nephrotoxicity"
      }
    }
  ]
}
```

### --- id=903 ---

输入文本: Escape atrial complexes, which occurred following junctional premature complexes, failed to initiate tachycardia in the control state but tachycardia was always reinitiated by an identical escape sequence after procainamide.

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
      "cause": "procainamide",
      "effect": "tachycardia"
    }
  ],
  "pred_triples": []
}
```

### --- id=921 ---

输入文本: Use of the Naranjo probability scale determined the association between cephalosporin use and leukopenia to be probable.

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
      "cause": "cephalosporin",
      "effect": "leukopenia"
    }
  ],
  "pred_triples": []
}
```

### --- id=930 ---

输入文本: The present study describes a patient who had unusual weight fluctuation under corticosteroid and psychotropic treatment such as mianserin and aripiprazole.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "aripiprazole",
      "effect": "unusual weight fluctuation"
    },
    {
      "cause": "mianserin",
      "effect": "unusual weight fluctuation"
    }
  ],
  "pred_triples": []
}
```

### --- id=933 ---

输入文本: Postoperative hypocalcemic tetany caused by fleet phospho-soda preparation in a patient taking alendronate sodium: report of a case.

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
      "cause": "alendronate sodium",
      "effect": "hypocalcemic tetany"
    },
    {
      "cause": "fleet phospho-soda",
      "effect": "hypocalcemic tetany"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "fleet phospho-soda preparation"
      },
      "relation": "caused",
      "effect": {
        "span": "hypocalcemic tetany"
      }
    }
  ]
}
```

### --- id=943 ---

输入文本: This report describes the sudden appearance of mixed mania in three children with delusional depression soon after the commencement of tricyclic antidepressant therapy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "tricyclic antidepressant"
      },
      "relation": "caused",
      "effect": {
        "span": "mixed mania"
      }
    }
  ]
}
```

### --- id=949 ---

输入文本: Severe lidocaine intoxication by cutaneous absorption.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "lidocaine"
      },
      "relation": "caused",
      "effect": {
        "span": "Severe lidocaine intoxication"
      }
    }
  ]
}
```

### --- id=952 ---

输入文本: Pellagra should be suspected whenever tuberculous patients under treatment with isoniazid develop mental, neurological or gastrointestinal symptoms, even in the absence of typical pellagra dermatitis.

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
      "cause": "isoniazid",
      "effect": "mental, neurological or gastrointestinal symptoms"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "isoniazid"
      },
      "relation": "caused",
      "effect": {
        "span": "pellagra"
      }
    }
  ]
}
```

### --- id=955 ---

输入文本: Preliminary results suggest that the higher concentrations of dextrose induce increased histamine release from blood cells, and that this phenomenon is more marked in diabetic, and particularly diabetic-allergic, individuals.

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
      "cause": "dextrose",
      "effect": "increased histamine release"
    }
  ],
  "pred_triples": []
}
```

### --- id=956 ---

输入文本: We wish to call for cautious approach at time of cessation of prolonged ACTH therapy because of possible unexpected and only partially understood hazardous side effects such as hyperkalemia.

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
      "cause": "ACTH",
      "effect": "hyperkalemia"
    }
  ],
  "pred_triples": []
}
```

### --- id=957 ---

输入文本: Lithium neurotoxicity should be considered in Creutzfeldt-Jakob disease differential diagnosis, serial electroencephalograms being the most valuable.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "Lithium",
      "effect": "Creutzfeldt-Jakob disease"
    },
    {
      "cause": "Lithium",
      "effect": "Lithium neurotoxicity"
    }
  ],
  "pred_triples": []
}
```

### --- id=964 ---

输入文本: Intravenous haloperidol is generally well tolerated, but multiform ventricular tachycardia has been reported.

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
      "cause": "haloperidol",
      "effect": "multiform ventricular tachycardia"
    }
  ],
  "pred_triples": []
}
```

### --- id=971 ---

输入文本: The induction of hypoglycaemia with PAS in this patient suggests a potential role for PAS in the treatment of diabetes mellitus.

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
      "cause": "PAS",
      "effect": "hypoglycaemia"
    }
  ],
  "pred_triples": []
}
```

### --- id=1004 ---

输入文本: Posterior leukoencephalopathy following cisplatin, bleomycin and vinblastine therapy for germ cell tumor of the ovary.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 3,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "bleomycin",
      "effect": "Posterior leukoencephalopathy"
    },
    {
      "cause": "cisplatin",
      "effect": "Posterior leukoencephalopathy"
    },
    {
      "cause": "vinblastine",
      "effect": "Posterior leukoencephalopathy"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "cisplatin"
      },
      "relation": "caused",
      "effect": {
        "span": "leukoencephalopathy"
      }
    },
    {
      "cause": {
        "span": "bleomycin"
      },
      "relation": "caused",
      "effect": {
        "span": "leukoencephalopathy"
      }
    },
    {
      "cause": {
        "span": "vinblastine"
      },
      "relation": "caused",
      "effect": {
        "span": "leukoencephalopathy"
      }
    }
  ]
}
```

### --- id=1010 ---

输入文本: After discontinuation of danazol the diabetes completely resolved.

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
      "cause": "danazol",
      "effect": "diabetes"
    }
  ],
  "pred_triples": []
}
```

### --- id=1027 ---

输入文本: Case 3: A 29-year-old female alcoholic complained of general fatigue and a slight fever after 1.5 years of abstinence with cyanamide treatment.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "cyanamide",
      "effect": "fatigue"
    },
    {
      "cause": "cyanamide",
      "effect": "fever"
    }
  ],
  "pred_triples": []
}
```

### --- id=1030 ---

输入文本: This case had radiation fibrosis, so we suggest that radiation fibrosis may be another contributor of the occurrence of ILD in patients taking erlotinib.

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
      "cause": "erlotinib",
      "effect": "ILD"
    }
  ],
  "pred_triples": []
}
```

### --- id=1031 ---

输入文本: To develop information on the relative rarity or frequency of neurologic worsening with the initiation of penicillamine therapy, we conducted a retrospective survey of 25 additional patients with Wilson's disease who met the criteria of presenting with neurologic disease and having been treated with penicillamine.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "penicillamine",
      "effect": "neurologic disease"
    },
    {
      "cause": "penicillamine",
      "effect": "neurologic worsening"
    }
  ],
  "pred_triples": []
}
```

### --- id=1059 ---

输入文本: Correction of serum electrolyte imbalance prevents cardiac arrhythmia during amphotericin B administration.

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
      "cause": "amphotericin B",
      "effect": "cardiac arrhythmia"
    }
  ],
  "pred_triples": []
}
```

### --- id=1063 ---

输入文本: In the second case, five cardiac arrests due to ventricular tachycardia and fibrillation occurred during several hours after beginning a trial of bretylium maintenance therapy for complex ventricular ectopy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
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
      "cause": "bretylium",
      "effect": "cardiac arrests"
    },
    {
      "cause": "bretylium",
      "effect": "fibrillation"
    },
    {
      "cause": "bretylium",
      "effect": "ventricular tachycardia"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "bretylium"
      },
      "relation": "caused",
      "effect": {
        "span": "cardiac arrests"
      }
    }
  ]
}
```

### --- id=1083 ---

输入文本: Rifampin (RFP) increases hepatic microsomal enzyme activity, and there are case reports of RFP-induced hypothyroidism, all associated with Hashimoto's thyroiditis.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "anchor_window_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "token_f1_counts": {
    "tp": 1,
    "fp": 0,
    "fn": 3
  },
  "gold_relations": [
    {
      "cause": "RFP",
      "effect": "Hashimoto's thyroiditis"
    },
    {
      "cause": "Rifampin",
      "effect": "Hashimoto's thyroiditis"
    },
    {
      "cause": "RFP",
      "effect": "hypothyroidism"
    },
    {
      "cause": "Rifampin",
      "effect": "hypothyroidism"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "RFP"
      },
      "relation": "caused",
      "effect": {
        "span": "hypothyroidism"
      }
    }
  ]
}
```

### --- id=1102 ---

输入文本: Systemic lupus erythematosus (SLE) developed in as 23-year-old woman with psoriasis during treatment with psoralen-ultraviolet-A (PUVA).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "psoralen-ultraviolet-A"
      },
      "relation": "caused",
      "effect": {
        "span": "Systemic lupus erythematosus"
      }
    }
  ]
}
```

### --- id=1104 ---

输入文本: Although heparin-dependent antibodies (HDAs) typically manifest with thrombocytopenia as in heparin-induced thrombocytopenia (HIT), they may also manifest with preserved platelet counts.

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
      "cause": "heparin",
      "effect": "thrombocytopenia"
    }
  ],
  "pred_triples": []
}
```

### --- id=1108 ---

输入文本: Alprazolam withdrawal delirium unresponsive to diazepam: case report.

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
      "cause": "Alprazolam",
      "effect": "delirium"
    }
  ],
  "pred_triples": []
}
```

### --- id=1125 ---

输入文本: We describe two patients with profound hypothalamic-pituitary-adrenal axis suppression resulting from the unregulated use of super potent topical corticosteroids.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "super potent topical corticosteroids"
      },
      "relation": "caused",
      "effect": {
        "span": "profound hypothalamic-pituitary-adrenal axis suppression"
      }
    }
  ]
}
```

### --- id=1165 ---

输入文本: Visual system side effects caused by parasympathetic dysfunction after botulinum toxin type B injections.

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
      "cause": "botulinum toxin type B",
      "effect": "parasympathetic dysfunction"
    },
    {
      "cause": "botulinum toxin type B",
      "effect": "Visual system side effects"
    }
  ],
  "pred_triples": [
    {
      "cause": {
        "span": "botulinum toxin type B"
      },
      "relation": "caused",
      "effect": {
        "span": "Visual system side effects"
      }
    }
  ]
}
```

### --- id=1182 ---

输入文本: The incidence and clinical features of allergic contact and/or photocontact dermatitis due to psoralens were examined in 371 patients with psoriasis treated with topical PUVA.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": true,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 1,
    "fn": 0
  },
  "gold_relations": [],
  "pred_triples": [
    {
      "cause": {
        "span": "psoralens"
      },
      "relation": "caused",
      "effect": {
        "span": "allergic contact and/or photocontact dermatitis"
      }
    }
  ]
}
```

### --- id=1186 ---

输入文本: While for ribavirin antidepressant effects are not known, we suppose that antidepressants may prevent changes in serotonergic or noradrenergic neurotransmission caused by IFN-alpha.

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
      "cause": "IFN-alpha",
      "effect": "changes in serotonergic or noradrenergic neurotransmission"
    }
  ],
  "pred_triples": []
}
```

### --- id=1187 ---

输入文本: A potential role for renal and hepatic impairment in the observed protracted course of amiodarone-induced thyrotoxicosis is suggested.

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
      "cause": "amiodarone",
      "effect": "thyrotoxicosis"
    }
  ],
  "pred_triples": []
}
```

### --- id=1193 ---

输入文本: Myoglobinuria and acute renal failure were observed in two patients with vasopressin-treated gastrointestinal hemorrhage.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "vasopressin",
      "effect": "acute renal failure"
    },
    {
      "cause": "vasopressin",
      "effect": "Myoglobinuria"
    }
  ],
  "pred_triples": []
}
```

### --- id=1201 ---

输入文本: While approximately 70% of patients with schizophrenia and other psychotic disorders show a clear-cut reduction of symptoms in clinical trials, there is considerable variation in individual patient outcome, ranging from complete remission to absolute refractoriness.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "ConnectionResetError",
  "generation_error_message": "[WinError 10054] 远程主机强迫关闭了一个现有的连接。"
}
```

### --- id=1202 ---

输入文本: All three showed improved motor performance in response to the introduction of corticosteroids.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "ConnectionResetError",
  "generation_error_message": "[WinError 10054] 远程主机强迫关闭了一个现有的连接。"
}
```

### --- id=1203 ---

输入文本: A case may be made for the discontinuation of the usage of chloral hydrate.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1204 ---

输入文本: In those patients in whom a reduction in the blood flow to liver tumors was shown angiographically, there was a progressive improvement in hormone secretion and in tumor size in the ensuing year of treatment, suggesting that a major target of SMS is that vascular supply of the tumors.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1205 ---

输入文本: CLINICAL FEATURES: A 61 yr old man with severe mitral regurgitation and chronic obstructive lung disease underwent surgery for mitral valve repair.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1206 ---

输入文本: We diagnosed BP by histopathological and immunofluorescence studies.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1207 ---

输入文本: The patient did not fulfil criteria for Churg-Strauss syndrome.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1208 ---

输入文本: However, the similarities between patient reports and reports from healthcare professionals in most frequently reported ADRs and most frequently reported drugs are striking.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1209 ---

输入文本: Beneficial effects of telmisartan in an HIV+ diabetic insulin-dependent patient.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1210 ---

输入文本: Inflammatory mononuclear cells and granulocytes typically seen in patients with diffuse lamellar keratitis (DLK) were absent.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1211 ---

输入文本: Pure red cell aplasia due to parvovirus B19 infection after liver transplantation: a case report and review of the literature.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1212 ---

输入文本: The total number of nucleated cells infused was 0.8 x 108/kg, with CD34+ cells 1.8 x 106/kg and CFU-GM 1 x 104/kg.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1213 ---

输入文本: These effusions can be due to multiple causes with drugs being implicated as one of the etiological agents.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1214 ---

输入文本: A 78-year-old woman with many medical problems, including chronic obstructive pulmonary disease, was treated with parenteral levofloxacin for community-acquired pneumonia.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1215 ---

输入文本: Glucocorticoids may have many side effects, and therefore their use should always be carefully considered.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1216 ---

输入文本: INTERVENTION: The LASIK flap was lifted or amputated, samples were submitted for Ziehl-Neelsen acid-fast stain and Lowenstein-Jensen's agar cultures for diagnosis; topical treatment with fortified clarithromycin and amikacin was administered until clinical resolution.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1217 ---

输入文本: We report an unusual case of necrotizing scleritis with inflammation that occurred after strabismus surgery.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1218 ---

输入文本: This case illustrates that distortion-product otoacoustic emissions (DPOAEs) may be an appropriate cross-check measure to supplement and confirm pediatric behavioral data.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1219 ---

输入文本: Antimonial derivatives induced a rapid remission.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1220 ---

输入文本: We report a patient with inoperable pancreatic cancer who developed gastrointestinal bleeding secondary to radiation-recall related to gemcitabine and review literature.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "gemcitabine",
      "effect": "gastrointestinal bleeding"
    },
    {
      "cause": "gemcitabine",
      "effect": "radiation-recall"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1221 ---

输入文本: The patient in this report had long standing RA treated with MTX and had recently begun taking a cyclooxygenase-2 (COX-2) inhibitor.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1222 ---

输入文本: The potential anticonvulsant effect of these drugs was successfully reversed by the administration of intravenous flumazenil just prior to the treatments.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1223 ---

输入文本: L-asparaginase is a critical component in the treatment of acute lymphoblastic leukemia in children.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1224 ---

输入文本: Methotrexate inhibits the enzyme dihydrofolate reductase and prevents the formation of DNA and RNA.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1225 ---

输入文本: Kidney biopsy demonstrated membranous glomerulonephritis.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1226 ---

输入文本: RESULTS: The material from inside the lumen of the catheter was analyzed using x-ray spectroscopy and a scanning electron microscopy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1227 ---

输入文本: Generally, patients in treatment with isotretinoin avoid eventual pregnancy during assumption and, after its stopping, fertility and foetal development are normal once circulating isotretinoin levels return to normal.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1228 ---

输入文本: We describe a 50-year-old woman with rheumatoid arthritis in whom a severe postinjection vasomotor reaction was associated with a cerebral vascular accident.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1229 ---

输入文本: RESULTS: Both patients treated with bilateral subthalamotomy developed unilateral choreoballistic movements immediately after surgery, despite not taking levodopa (L-dopa).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1230 ---

输入文本: There were no complications of persistent bacteremia despite placement of the stent-graft device at the site of primary infection, reinfection, delayed rupture, paraplegia, distal emboli, or surgical conversion.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1231 ---

输入文本: Pseudomembranous colitis readily occurs in at least certain population groups receiving trimethoprim-sulfamethoxazole.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "sulfamethoxazole",
      "effect": "Pseudomembranous colitis"
    },
    {
      "cause": "trimethoprim",
      "effect": "Pseudomembranous colitis"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1232 ---

输入文本: These microorganisms are recognized as the cause of devastating soft tissue infections, such as cellulitis, myositis, and gas gangrene.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1233 ---

输入文本: BACKGROUND: Amiodarone is a benzofuran derivative used to treat cardiac arrhythmias.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1234 ---

输入文本: Within 10 minutes, the occluded artery was reopened by an intracoronary (i.c.) infusion of streptokinase, resulting in the disappearance of chest pain and normalization of ST segments.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1235 ---

输入文本: This 4-year-6-month-old girl had a history of moderate developmental delay and had received HOPA administration when first admitted at 2 years 6 months of age with hypoglycemia, hyperammonemia, lactic and pyruvic acidemia, and non-ketotic dicarboxylic aciduria.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1236 ---

输入文本: Detection of PVB19-DNA in serum with quantitative polymerase chain reaction (PCR) revealed a high level of viral load.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1237 ---

输入文本: Here we report the case of a 43-year-old Japanese woman with acute myelogenous leukemia who underwent 2 unrelated cord blood transplantations (UCBT), terminating in fatal disseminated tuberculosis (TB).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1238 ---

输入文本: The patient developed grade 3 capecitabine-induced headache.

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
      "cause": "capecitabine",
      "effect": "headache"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1239 ---

输入文本: The report is followed by a brief review of anticonvulsant hypersensitivity syndrome and DRESS.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1240 ---

输入文本: He did not respond to treatment with oral iron not a proton pump inhibitor and an upper endoscopy was performed.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1241 ---

输入文本: The child did not require dialysis therapy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1242 ---

输入文本: Generalized lichen nitidus with involvement of the palms following interferon alpha treatment.

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
      "cause": "interferon alpha",
      "effect": "Generalized lichen nitidus"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1243 ---

输入文本: The average time of presentation was 17 days after LASIK (range, 7-34).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1244 ---

输入文本: Such a rapid or complete response cannot be achieved by any conventional form of treatment.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1245 ---

输入文本: The lesions resolved completely approximately 30 min after removal of the hands from water.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1246 ---

输入文本: We report an additional case of isotretinoin teratogenicity in which the patient had agenesis of the cerebellar vermis, multiple leptomeningeal neuroglial heterotopias, hydrocephalus, and abnormalities of the corticospinal tracts.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
  "strict_token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 5
  },
  "anchor_window_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 5
  },
  "token_f1_counts": {
    "tp": 0,
    "fp": 0,
    "fn": 5
  },
  "gold_relations": [
    {
      "cause": "isotretinoin",
      "effect": "abnormalities of the corticospinal tracts"
    },
    {
      "cause": "isotretinoin",
      "effect": "agenesis of the cerebellar vermis"
    },
    {
      "cause": "isotretinoin",
      "effect": "hydrocephalus"
    },
    {
      "cause": "isotretinoin",
      "effect": "multiple leptomeningeal neuroglial heterotopias"
    },
    {
      "cause": "isotretinoin",
      "effect": "teratogenicity"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1247 ---

输入文本: Although dipyridamole perfusion imaging has a good safety record, serious side-effects may rarely occur.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1248 ---

输入文本: Subsequent radiologic examination revealed rachitic bone and joint changes.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1249 ---

输入文本: Actinomycosis of the female genital tract has greatly increased over the last two decades.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1250 ---

输入文本: Persistent hypoglycemia in a patient with diabetes taking etanercept for the treatment of psoriasis.

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
      "cause": "etanercept",
      "effect": "Persistent hypoglycemia"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1251 ---

输入文本: We suggest that the cause of this distressing syndrome, and ways to mitigate or circumvent it, must be discovered.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1252 ---

输入文本: Pulmonary hemorrhage is an uncommon feature in the HUS, and seems to appear especially in the HUS associated with MMC therapy.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "MMC",
      "effect": "HUS"
    },
    {
      "cause": "MMC",
      "effect": "Pulmonary hemorrhage"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1253 ---

输入文本: CASE SUMMARY: An elderly patient with chronic atrial fibrillation and prosthetic valve replacements had been taking warfarin 22.5 mg/wk.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1254 ---

输入文本: Our patient also did not completely respond to these medications, but was successfully treated with cyclosporine alone.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1255 ---

输入文本: A review of the literature of 68 case reports of acute leukemia following ovarian cancer is presented and 3 new cases are reported.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1256 ---

输入文本: Corticosteroids have an established place in the prevention and treatment of nausea and vomiting due to emetogenic cytotoxic agents.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1257 ---

输入文本: According to the Naranjo et al. adverse-reaction probability scale, enoxaparin was the probable cause of hepatotoxicity in this patient.

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
      "cause": "enoxaparin",
      "effect": "hepatotoxicity"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1258 ---

输入文本: The case of a young woman suffering from multiple autoimmune-dysreactive disorders (including thyreoiditis, myasthenia gravis, thymectomy, Crohn's disease, and erythema nodosum), while undergoing steroideal therapy, was complicated by a severe infectious disorder (severe upper urinary tract infection).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1259 ---

输入文本: Two days after the drug was discontinued, the duration of the QRS complex was normalized.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1260 ---

输入文本: Power spectrum analysis of heart rate variability is useful in this instance because it magnifies the trace and detects even minor disturbances.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1261 ---

输入文本: To our knowledge, this case report represents only the third description of laxative-induced TEN.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1262 ---

输入文本: This likely explains the noted response to a calcium channel blocker (CCB), namely diltiazem.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1263 ---

输入文本: We have observed an increasing number of autopsies on patients with chemotherapy-related complications.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1264 ---

输入文本: CONCLUSION: Our case shows a fatal side effect of erlotinib.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1265 ---

输入文本: However in some patients requiring emergency cardiac or vascular surgery, reexposure to heparin may be unavoidable.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1266 ---

输入文本: This paper reports an autopsy case of a 78-year-old male with multiple nodules in the liver developed after long-termed administration of phosphate diethylstilbestrol (PDES) for prostatic cancer.

```json
{
  "gold_has_causal": true,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
      "cause": "PDES",
      "effect": "multiple nodules in the liver"
    },
    {
      "cause": "phosphate diethylstilbestrol",
      "effect": "multiple nodules in the liver"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1267 ---

输入文本: A case of acute subdural haematoma originating spontaneously from an angiomatous meningioma in a patient receiving prophylactic aspirin therapy is presented.

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
      "cause": "aspirin",
      "effect": "acute subdural haematoma"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1268 ---

输入文本: CONCLUSION: We believe this to be the first reported case of rhGH-induced hypercalcemia in an HIV-infected patient.

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
      "cause": "rhGH",
      "effect": "hypercalcemia"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1269 ---

输入文本: Children seem to be unusually sensitive to the depressant effects of clonidine.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1270 ---

输入文本: Rectal biopsy analysis was consistent with pseudomembranous colitis.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1271 ---

输入文本: The other patient required a further course of treatment with lithium and the nephrotic syndrome returned.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1272 ---

输入文本: None of the patients treated with acyclovir had evidence of active varicella-zoster virus infection at post-mortem examination, but two had disseminated bacterial and fungal infections.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1273 ---

输入文本: Complete seizure control was achieved but the patient developed hallucinations, agitation and self-harming behaviour, as well as poor social contact.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1274 ---

输入文本: PATIENTS: Two women, ages 49 and 34 years, with endometrial hyperplasia without squamous metaplasia who were treated with progestin.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1275 ---

输入文本: The patient had a history of four resections since the age of 19 years.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1276 ---

输入文本: DISCUSSION: Opioid dependence is generally considered synonymous with heroin dependence or dependence on prescribed opioid analgesics.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1277 ---

输入文本: On this regime, together with supportive psychotherapy, she experienced a sense of emotional well-being, exhibited a good level of functioning and maintained a safe body weight.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1278 ---

输入文本: A partial empty sella was found on a computed tomography scan of the hypothalamic-pituitary region.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1279 ---

输入文本: Treatment of coccidioidomycosis with amphotericin B may be accomplished via an Ommaya reservoir.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1280 ---

输入文本: Her symptoms regressed after inhaler steroid treatment.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1281 ---

输入文本: Eosinophilic cystitis is a rare and poorly understood disorder.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1282 ---

输入文本: Therefore, thorough investigation with an ultrasound-guided aspiration followed by an early drainage of the collection is warranted and mandatory.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1283 ---

输入文本: HIV1 and HIV2 serology was negative.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1284 ---

输入文本: The development of internal tissue inflammation is reportedly correlated with a shorter interval from the time of completion of radiation therapy to the initiation of chemotherapy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1285 ---

输入文本: ABMT may later have triggered opportunistic infections in this patient.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1286 ---

输入文本: Magnetic resonance spectra provided a noninvasive means of monitoring CNS response.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1287 ---

输入文本: Paranoid psychosis may result from intoxication with, or withdrawal from amphetamines.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1288 ---

输入文本: Analysis and correlation of antenatal data and drug therapy with individual cases failed to show any specific abnormality that could reasonably be attributed to zidovudine therapy.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1289 ---

输入文本: The manual intravenous push has a greater possibility of inadvertent overdosage during some small time frame, as well as more local symptoms by some reports.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1290 ---

输入文本: Reactivation histoplasmosis after treatment with anti-tumor necrosis factor alpha in a patient from a nonendemic area.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1291 ---

输入文本: We report the case of a 19-year-old woman who developed PVOD accompanied by microangiopathic hemolytic anemia (MAHA) and hemolytic uremic syndrome (HUS) 1 year after a second BMT for relapsed acute lymphoblastic leukemia (ALL).

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1292 ---

输入文本: This case is reported here for documentation because of its rarity.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1293 ---

输入文本: 2). These findings were characteristic of granular parakeratosis.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1294 ---

输入文本: Interstitial pneumonitis associated with sirolimus: a dilemma for lung transplantation.

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
      "cause": "sirolimus",
      "effect": "Interstitial pneumonitis"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1295 ---

输入文本: Two weeks later, the patient went to a local emergency department after experiencing two brief syncopal episodes.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1296 ---

输入文本: Oral antiviral and topical steroids in tapered dosages were administered.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1297 ---

输入文本: The patient's visual acuity, eye movements and the pupillary defect did not improve in the affected eye even after mechanical decompression within 30 minutes and medical treatment, neither in the early period nor during the following two months.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1298 ---

输入文本: A case of SIADH associated with desipramine treatment in an elderly depressed woman is described.

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
      "cause": "desipramine",
      "effect": "SIADH"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1299 ---

输入文本: Methylphenidate-associated enuresis in attention deficit hyperactivity disorder.

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
      "cause": "Methylphenidate",
      "effect": "enuresis"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1300 ---

输入文本: BACKGROUND: Pelvic actinomycosis is a chronic suppurative inflammatory disease caused by the anaerobic Gram-positive bacilli Actinomyces israelii.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1301 ---

输入文本: Such abuse (possibly linked to the rewarding effect of dopamine) has been recently monitored in the context of Parkinson's disease (PD) (the "dopamine dysregulation syndrome").

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1302 ---

输入文本: A 25-year-old factory worker sustained inhalation injury and 2 per cent deep burns while fighting a fire in his factory (LSI factory) which was made of new synthetic building materials.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1303 ---

输入文本: Stopping the topical steroids with concurrent lowering of the IOP resulted in improvement in the uncorrected and best corrected visual acuities and was associated with resolution of the corneal findings.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1304 ---

输入文本: When phenytoin was discontinued, valproate levels increased, and he progressively improved.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1305 ---

输入文本: When the patient was subsequently treated by parenteral administration of Org 10172 as anticoagulant over a period of several weeks the number of platelets rapidly increased and the patient almost completely recovered.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1306 ---

输入文本: One patient suffered coronary artery vasospasm, attributed to the use of topical 1:1000 epinephrine during surgery.

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
      "cause": "epinephrine",
      "effect": "coronary artery vasospasm"
    }
  ],
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1307 ---

输入文本: Coagulase-negative staphylococci were detected in cerebrospinal fluid (CSF), and the infection persisted even with intrathecal administration of gentamycin, and intravenous administration of vancomycin and arbekacin.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1308 ---

输入文本: Investigations in two patients have revealed excessive renal loss of magnesium.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```

### --- id=1309 ---

输入文本: The purpose of this study was to evaluate the neuroprotective effect of MB in these patients and to review the literature.

```json
{
  "gold_has_causal": false,
  "pred_has_causal": false,
  "primary_metric": "anchor_window",
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
  "pred_triples": [],
  "generation_error_type": "URLError",
  "generation_error_message": "<urlopen error [WinError 10061] 由于目标计算机积极拒绝，无法连接。>"
}
```
