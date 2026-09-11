"""验证 PCD baseline 的作者模板、负例门控、输出配对及统一评估接口。"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from types import ModuleType, SimpleNamespace
from typing import Any

import pytest

from src.causal_discovery_baseline import (
    DEFAULT_SOURCE_DIR,
    AuthorRunner,
    RunConfig,
    _ContinuationTokenizer,
    _load_author_script,
    build_prompts,
    load_author_templates,
    parse_detection,
    prediction_from_author_outputs,
    run_causal_discovery_baseline,
)


@pytest.fixture
def templates() -> dict[str, Any]:
    if not DEFAULT_SOURCE_DIR.is_dir():
        pytest.skip("未下载作者仓库，仅跳过依赖该本地仓库的测试")
    return load_author_templates()


def test_original_prompts_receive_only_text_and_keep_examples(templates: dict[str, Any]) -> None:
    config = RunConfig()
    sample = {"id": "hidden-id", "text": 'A {literal} causes B.\nSecond line.',
              "has_causal": True, "relations": [{"cause": "SECRET_GOLD"}]}
    detection = build_prompts([sample], "detection", templates, config)[0]
    original = templates["detection"]["few_ICL_system"]
    assert detection == original["system"] + "\n\n" + original["user"].format(sentence=sample["text"])
    assert "Example 3:" in detection
    assert "SECRET_GOLD" not in detection and "hidden-id" not in detection
    extraction = build_prompts([sample], "extraction", templates, config)[0]
    assert extraction == templates["extraction"]["chain_of_thought"].format(input_sentence=sample["text"])
    assert "Think (silently)" in extraction
    changed_gold = dict(sample, has_causal=False, relations=[])
    assert build_prompts([changed_gold], "detection", templates, config) == [detection]
    assert build_prompts([changed_gold], "extraction", templates, config) == [extraction]


@pytest.mark.parametrize("raw", ['{"answer": true}', '{"answer":"Causal"}', 'causal', '{"answer":'])
def test_detection_invalid_outputs_are_not_guessed(raw: str) -> None:
    label, error = parse_detection(raw)
    assert label is None and error


def test_multipair_mapping_preserves_direction_duplicates_and_nonverbatim_text() -> None:
    parsed = {"cause_10": "paraphrased cause", "effect_10": "third effect",
              "effect_2": "B", "cause_2": "A", "cause": "A", "effect": "B",
              "cause_3": "orphan cause", "causal_markers": ["causes"]}
    prediction = prediction_from_author_outputs(17, '{"answer":"causal"}', json.dumps(parsed))
    assert prediction["id"] == 17 and prediction["has_causal"] is True
    assert prediction["triples"] == [
        {"cause": {"span": "A"}, "effect": {"span": "B"}},
        {"cause": {"span": "A"}, "effect": {"span": "B"}},
        {"cause": {"span": "paraphrased cause"}, "effect": {"span": "third effect"}},
    ]
    assert prediction["extraction_errors"] == ["incomplete_pair_3"]


@pytest.mark.parametrize("response", ['{"cause":', '{}'])
def test_empty_or_malformed_extraction_does_not_change_positive_detection(response: str) -> None:
    prediction = prediction_from_author_outputs("a", '{"answer":"causal"}', response)
    assert prediction["has_causal"] is True
    assert prediction["triples"] == []
    assert prediction["extraction_errors"]
    negative = prediction_from_author_outputs("a", '{"answer":"noncausal"}', None)
    assert negative["has_causal"] is False and negative["triples"] == []
    with pytest.raises(ValueError, match="缺少抽取输出"):
        prediction_from_author_outputs("a", '{"answer":"causal"}', None)


class FakeRunner:
    """以可控响应验证完整接线，测试不下载模型或调用外部 API。"""

    def __init__(self, templates: dict[str, Any]) -> None:
        self.templates = templates
        self.config = RunConfig(batch_size=2)
        self.runtime: dict[str, Any] = {}
        self.prepared: list[str] = []
        self.prompts: dict[str, list[str]] = {"detection": [], "extraction": []}
        self.stage = ""
        self.responses = {
            "detection": ['{"answer":"causal"}', '{"answer":"noncausal"}',
                          '{"answer":"causal"}', 'broken response'],
            "extraction": ['{"cause":"Rain","effect":"flooding"}',
                           '{"cause":"wind","effect":"damage"}'],
        }

    def prepare(self, stage: str) -> None:
        self.stage = stage
        self.prepared.append(stage)

    def generate(self, prompts: list[str]) -> list[str]:
        start = len(self.prompts[self.stage])
        self.prompts[self.stage].extend(prompts)
        return self.responses[self.stage][start:start + len(prompts)]

    def close(self) -> None:
        self.stage = ""


def _samples() -> list[dict[str, Any]]:
    return [
        {"id": 1, "text": "Rain causes flooding.", "has_causal": True,
         "relations": [{"cause": "Rain", "effect": "flooding"}]},
        {"id": 2, "text": "Heat causes fire.", "has_causal": True,
         "relations": [{"cause": "Heat", "effect": "fire"}]},
        {"id": 3, "text": "The report mentions wind and damage.", "has_causal": False, "relations": []},
        {"id": 4, "text": "Birds are singing.", "has_causal": False, "relations": []},
    ]


def test_end_to_end_counts_misses_false_positives_and_preserves_all_samples(
    tmp_path: Path, templates: dict[str, Any],
) -> None:
    runner = FakeRunner(templates)
    result = run_causal_discovery_baseline(_samples(), runner, "cnc_sft_test", tmp_path, "example")
    assert runner.prepared == ["detection", "extraction"]
    assert len(runner.prompts["extraction"]) == 2
    assert "Heat causes fire." not in "\n".join(runner.prompts["extraction"])
    assert "The report mentions wind and damage." in runner.prompts["extraction"][1]
    report = result["report"]
    assert report["n_samples"] == 4
    assert {k: report["detection"][k] for k in ("tp", "tn", "fp", "fn")} == dict(tp=1, tn=1, fp=1, fn=1)
    counts = report["extraction"]["strict_token_f1"]["all_samples"]
    assert {k: counts[k] for k in ("tp", "fp", "fn")} == dict(tp=1, fp=1, fn=1)
    assert report["extraction"]["strict_token_f1"]["detected_only"]["f1"] == 1.0
    assert report["baseline"]["diagnostics"]["invalid_detection_outputs"] == 1
    with result["paths"]["input_csv"].open(encoding="utf-8", newline="") as file:
        inputs = list(csv.DictReader(file))
    assert list(inputs[0]) == ["id", "sentence"]
    assert inputs[0]["sentence"] == _samples()[0]["text"]
    assert all(path.is_file() for path in result["paths"].values())
    fresh_runner = FakeRunner(templates)
    second = run_causal_discovery_baseline(_samples(), fresh_runner, "cnc_sft_test", tmp_path, "example")
    assert fresh_runner.prepared == []
    assert second["predictions"] == result["predictions"]
    changed = _samples()
    changed[0]["text"] += " Changed."
    with pytest.raises(ValueError, match="同名运行"):
        run_causal_discovery_baseline(changed, FakeRunner(templates), "cnc_sft_test", tmp_path, "example")


def test_all_negative_predictions_skip_extraction_model(tmp_path: Path, templates: dict[str, Any]) -> None:
    runner = FakeRunner(templates)
    runner.responses["detection"] = ['{"answer":"noncausal"}'] * 4
    result = run_causal_discovery_baseline(_samples(), runner, "li", tmp_path, "negative")
    assert runner.prepared == ["detection"]
    assert result["report"]["extraction"]["primary_metric"] == "anchor_window"
    assert result["report"]["n_samples"] == 4
    assert result["paths"]["extraction_raw"].read_text() == ""


def test_incomplete_stage_is_restarted_without_reusing_partial_generations(
    tmp_path: Path, templates: dict[str, Any],
) -> None:
    runner = FakeRunner(templates)
    result = run_causal_discovery_baseline(_samples(), runner, "ade", tmp_path, "partial")
    path = result["paths"]["extraction_raw"]
    path.write_text('{"id":1,', encoding="utf-8")
    runner = FakeRunner(templates)
    rerun = run_causal_discovery_baseline(_samples(), runner, "ade", tmp_path, "partial")
    assert runner.prepared == ["extraction"]
    assert rerun["predictions"] == result["predictions"]


def test_original_generation_function_decodes_only_new_tokens(templates: dict[str, Any]) -> None:
    import torch

    sentinel = object()
    old = sys.modules.get("prompts", sentinel)
    script = _load_author_script(DEFAULT_SOURCE_DIR, "extraction")
    assert sys.modules.get("prompts", sentinel) is old

    class Tokenizer:
        pad_token_id = 0

        def __call__(self, prompts: Any, **kwargs: Any) -> dict[str, Any]:
            assert kwargs["max_length"] == 1024
            return {"input_ids": torch.tensor([[10, 11, 12]]), "attention_mask": torch.ones((1, 3))}

        def batch_decode(self, tokens: Any, **kwargs: Any) -> list[str]:
            assert tokens.tolist() == [[20, 21]]
            return ['{"cause":"Rain","effect":"flooding"}']

    class Model:
        device = "cpu"

        def generate(self, **kwargs: Any) -> Any:
            assert kwargs["do_sample"] is True
            assert kwargs["temperature"] == 0.7 and kwargs["top_k"] == 40
            assert kwargs["max_new_tokens"] == 256
            return torch.tensor([[10, 11, 12, 20, 21]])

    outputs, _ = script.run_llm_batch(Model(), _ContinuationTokenizer(Tokenizer()), ["un-normalized prompt"])
    assert json.loads(outputs[0])["cause"] == "Rain"


def test_duplicate_ids_are_rejected(tmp_path: Path, templates: dict[str, Any]) -> None:
    samples = _samples()
    samples[1]["id"] = samples[0]["id"]
    with pytest.raises(ValueError, match="id 不唯一"):
        run_causal_discovery_baseline(samples, FakeRunner(templates), "ade", tmp_path, "duplicate")


def test_author_stages_keep_distinct_quantization_and_serializable_runtime(
    monkeypatch: pytest.MonkeyPatch, templates: dict[str, Any],
) -> None:
    import torch

    loads: list[dict[str, Any]] = []
    order: list[str] = []
    monkeypatch.setattr(torch.cuda, "is_available", lambda: True)
    monkeypatch.setattr(torch.cuda, "empty_cache", lambda: None)
    monkeypatch.setattr(torch.cuda, "get_device_name", lambda index: "test GPU")

    class Quantization:
        def __init__(self, **kwargs: Any) -> None:
            self.values = kwargs

        def to_dict(self) -> dict[str, Any]:
            return {k: str(v) if isinstance(v, torch.dtype) else v for k, v in self.values.items()}

    def load_model(name: str, **kwargs: Any) -> Any:
        assert order[-1] == "seed:4000"
        order.append("load")
        loads.append(kwargs)
        return SimpleNamespace(config=SimpleNamespace(quantization_config=kwargs["quantization_config"],
                                                       _commit_hash="test-commit"),
                               generation_config=SimpleNamespace(to_dict=lambda: {"do_sample": False}),
                               eval=lambda: None)

    # Transformers 的惰性导出可能绕过属性补丁，因此在导入边界替换整个测试模块。
    backend = ModuleType("transformers")
    backend.BitsAndBytesConfig = Quantization
    backend.AutoModelForCausalLM = SimpleNamespace(from_pretrained=load_model)
    backend.AutoTokenizer = SimpleNamespace(from_pretrained=lambda *args, **kwargs: SimpleNamespace(
        eos_token="</s>", eos_token_id=2))
    backend.TextGenerationPipeline = lambda **kwargs: SimpleNamespace(
        generation_config=SimpleNamespace(to_dict=lambda: {"do_sample": True}))
    backend.set_seed = lambda seed: order.append(f"seed:{seed}")
    monkeypatch.setitem(sys.modules, "transformers", backend)
    runner = AuthorRunner()
    runner.prepare("detection")
    runner.prepare("extraction")
    assert loads[0]["quantization_config"].to_dict() == {"load_in_4bit": True}
    assert loads[1]["quantization_config"].to_dict() == {
        "load_in_4bit": True, "bnb_4bit_use_double_quant": True,
        "bnb_4bit_quant_type": "nf4", "bnb_4bit_compute_dtype": "torch.float16",
    }
    assert loads[1]["torch_dtype"] == torch.float16
    assert runner.runtime["detection"]["pipeline_generation_config"] == {"do_sample": True}
    assert json.loads(json.dumps(runner.runtime))["extraction"]["model_commit"] == "test-commit"
    runner.close()
