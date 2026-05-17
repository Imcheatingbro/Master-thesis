"""数据清洗脚本的验收测试。"""

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from clean_data import parse_cnc_row, parse_li_item, run_cleaning


def test_parse_cnc_row_removes_sig_and_extracts_relation() -> None:
    row = {
        "text": "The farmworkers ' strike resumed on Tuesday when their demands were not met .",
        "causal_text_w_pairs": (
            "[\"<ARG1>The farmworkers ' strike resumed on Tuesday</ARG1> "
            "when <ARG0><SIG0>their</SIG0> demands were not met</ARG0> .\"]"
        ),
        "num_rs": "1",
    }

    sample, warnings = parse_cnc_row(row, 1)

    assert warnings["num_rs_mismatch"] == 0
    assert sample == {
        "id": 1,
        "text": "The farmworkers ' strike resumed on Tuesday when their demands were not met .",
        "has_causal": True,
        "relations": [
            {
                "cause": "their demands were not met",
                "effect": "The farmworkers ' strike resumed on Tuesday",
            }
        ],
    }


def test_parse_cnc_row_keeps_sample_when_relation_fails_substring() -> None:
    row = {
        "text": "Plain sentence .",
        "causal_text_w_pairs": "['<ARG1>missing effect</ARG1> because <ARG0>missing cause</ARG0> .']",
        "num_rs": "1",
    }

    sample, warnings = parse_cnc_row(row, 7)

    assert sample["has_causal"] is True
    assert sample["relations"] == []
    assert warnings["substring_check_failed_relations"] == 1
    assert warnings["substring_check_failed_samples"] == 1


def test_parse_li_item_extracts_multiple_relations_and_cleans_text() -> None:
    label = "Cause-Effect((e2,e1),(e3,e1))"
    sentence = (
        "Cutler ended up with <e1>a bleeding stomach ulcer</e1> caused by "
        "<e2>the stress</e2> and <e3>hard work</e3> supervising their tours."
    )

    sample, warnings = parse_li_item(label, sentence, 2)

    assert warnings["missing_entity_mapping"] == 0
    assert sample == {
        "id": 2,
        "text": "Cutler ended up with a bleeding stomach ulcer caused by the stress and hard work supervising their tours.",
        "has_causal": True,
        "relations": [
            {"cause": "the stress", "effect": "a bleeding stomach ulcer"},
            {"cause": "hard work", "effect": "a bleeding stomach ulcer"},
        ],
    }


def test_run_cleaning_writes_jsonl_and_stats_to_data_dir(tmp_path: Path) -> None:
    cnc_path = tmp_path / "Dataset_1_CNC_raw.csv"
    with cnc_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "corpus",
                "doc_id",
                "sent_id",
                "eg_id",
                "index",
                "text",
                "causal_text_w_pairs",
                "num_rs",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "corpus": "cnc",
                "doc_id": "d",
                "sent_id": "1",
                "eg_id": "0",
                "index": "i",
                "text": "Rain caused flooding .",
                "causal_text_w_pairs": "['<ARG0>Rain</ARG0> caused <ARG1>flooding</ARG1> .']",
                "num_rs": "1",
            }
        )
        writer.writerow(
            {
                "corpus": "cnc",
                "doc_id": "d",
                "sent_id": "2",
                "eg_id": "0",
                "index": "j",
                "text": "No relation here .",
                "causal_text_w_pairs": "[]",
                "num_rs": "0",
            }
        )

    (tmp_path / "Dataset_2_Li_raw.xml").write_text(
        """<?xml version="1.0" ?>
<test-corpus version="2018">
  <item id="1" label="Non-Causal">
    <sentence>A &lt;e1&gt;person&lt;/e1&gt; saw a &lt;e2&gt;car&lt;/e2&gt;.</sentence>
  </item>
  <item id="2" label="Cause-Effect((e2,e1),(e3,e1))">
    <sentence>&lt;e1&gt;Damage&lt;/e1&gt; came from &lt;e2&gt;wind&lt;/e2&gt; and &lt;e3&gt;rain&lt;/e3&gt;.</sentence>
  </item>
</test-corpus>
""",
        encoding="utf-8",
    )

    stats = run_cleaning(tmp_path)

    cnc_lines = (tmp_path / "Dataset_1_CNC_modified.jsonl").read_text(encoding="utf-8").splitlines()
    li_lines = (tmp_path / "Dataset_2_Li_modified.jsonl").read_text(encoding="utf-8").splitlines()
    stats_file = json.loads((tmp_path / "stats.json").read_text(encoding="utf-8"))

    assert [json.loads(line)["id"] for line in cnc_lines] == [1, 2]
    assert [json.loads(line)["id"] for line in li_lines] == [1, 2]
    assert stats == stats_file
    assert stats["cnc"]["relation_count_distribution"] == {"0": 1, "1": 1}
    assert stats["li"]["relation_count_distribution"] == {"0": 1, "2": 1}
