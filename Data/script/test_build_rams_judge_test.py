"""RAMS judge 数据集构造脚本的验收测试。"""

from build_rams_judge_test import (
    build_dataset,
    short_role,
    validate_dataset,
)


def sample_document() -> dict:
    """创建包含三个角色的最小 RAMS 样例。"""
    return {
        "doc_key": "test_doc",
        "sentences": [["Alice", "attacked", "Bob", "in", "Paris", "."]],
        "evt_triggers": [[1, 1, [["conflict.attack.n/a", 1.0]]]],
        "gold_evt_links": [
            [[1, 1], [0, 0], "evt001arg01attacker"],
            [[1, 1], [2, 2], "evt001arg02target"],
            [[1, 1], [4, 4], "evt001arg03place"],
        ],
    }


def test_short_role_matches_rams_scorer_rule() -> None:
    assert short_role("evt043arg01communicator") == "communicator"


def test_build_dataset_creates_balanced_unique_pairs() -> None:
    ontology = {
        "conflict.attack.n/a": ["attacker", "target", "instrument", "place"]
    }

    records, metadata = build_dataset([sample_document()], ontology, seed=7)
    checks = validate_dataset(records)

    assert len(records) == 6
    assert sum(record["label"] for record in records) == 3
    assert metadata["negative_type_counts"] == {
        "role_corruption": 2,
        "span_swap": 1,
    }
    assert checks["each_pair_has_one_positive_and_one_negative"] is True


def test_build_dataset_removes_duplicate_gold_links() -> None:
    document = sample_document()
    document["gold_evt_links"].append(document["gold_evt_links"][0])
    ontology = {
        "conflict.attack.n/a": ["attacker", "target", "instrument", "place"]
    }

    records, metadata = build_dataset([document], ontology, seed=7)

    assert len(records) == 6
    assert metadata["raw_gold_links"] == 4
    assert metadata["unique_gold_links"] == 3
    assert metadata["duplicate_gold_links_removed"] == 1


def test_build_dataset_omits_documents_without_gold_links() -> None:
    document = sample_document()
    document["gold_evt_links"] = []
    ontology = {
        "conflict.attack.n/a": ["attacker", "target", "instrument", "place"]
    }

    records, metadata = build_dataset([document], ontology, seed=7)

    assert records == []
    assert metadata["documents_without_gold_links"] == 1


def test_build_dataset_omits_link_without_semantic_negative() -> None:
    document = sample_document()
    document["gold_evt_links"] = [document["gold_evt_links"][0]]
    ontology = {"conflict.attack.n/a": ["attacker"]}

    records, metadata = build_dataset([document], ontology, seed=7)

    assert records == []
    assert metadata["gold_links_omitted_without_unique_semantic_negative"] == 1
