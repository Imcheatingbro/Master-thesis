"""SPEC_05 适配：复用 Anuyah 等人的 PCD 代码，完成检测、抽取与项目统一评估。"""

from __future__ import annotations

import csv
import gc
import hashlib
import importlib.metadata
import importlib.util
import json
import logging
import re
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from types import ModuleType
from typing import Any, Mapping, Sequence


logger = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = (
    PROJECT_ROOT / "reference code from related work" / "CausalDiscovery-main" / "CausalDiscovery-main"
)
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"
SOURCE_FILES = (
    "experiments/experiment1/main.py",
    "experiments/experiment1/prompts.py",
    "experiments/experiment2/exp2.py",
    "experiments/experiment2/prompts.py",
)


@dataclass(frozen=True)
class RunConfig:
    """固定论文报告的提示策略；较小 batch 用于单卡运行，其余生成设置沿用作者代码。"""

    model_name_or_path: str = MODEL_ID
    batch_size: int = 4
    seed: int = 4000
    detection_prompt: str = "few_ICL_system"
    extraction_prompt: str = "chain_of_thought"
    detection_max_new_tokens: int = 512
    extraction_max_new_tokens: int = 256
    extraction_top_k: int = 40
    extraction_temperature: float = 0.7

    def __post_init__(self) -> None:
        if self.batch_size < 1:
            raise ValueError("batch_size 必须大于 0")


def _import_file(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"无法加载作者文件：{path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_author_templates(source_dir: Path | str = DEFAULT_SOURCE_DIR) -> dict[str, Any]:
    """直接读取两个原始 prompts.py，避免两个同名模块在 notebook 中互相覆盖。"""

    root = Path(source_dir)
    for relative in SOURCE_FILES:
        if not (root / relative).is_file():
            raise FileNotFoundError(f"缺少作者源码：{root / relative}")
    detection = _import_file(root / SOURCE_FILES[1], "_pcd_detection_prompts")
    extraction = _import_file(root / SOURCE_FILES[3], "_pcd_extraction_prompts")
    return {
        "detection": detection.prompts,
        "extraction": extraction.PROMPTS2,
        "source_sha256": {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in SOURCE_FILES},
    }


def _load_author_script(root: Path, stage: str) -> ModuleType:
    # 作者两份脚本均使用绝对导入 from prompts；导入期间绑定对应模块，随后恢复原状态。
    index = 0 if stage == "detection" else 2
    prompts_module = _import_file(root / SOURCE_FILES[index + 1], f"_pcd_{stage}_prompts")
    previous = sys.modules.get("prompts")
    sys.modules["prompts"] = prompts_module
    try:
        return _import_file(root / SOURCE_FILES[index], f"_pcd_{stage}_script")
    finally:
        if previous is None:
            sys.modules.pop("prompts", None)
        else:
            sys.modules["prompts"] = previous


def build_prompts(
    samples: Sequence[Mapping[str, Any]], stage: str, templates: Mapping[str, Any], config: RunConfig,
) -> list[str]:
    """保持原始 prompt 拼接方式；输入只读取 text，不读取标签、关系或样本类型。"""

    if stage == "detection":
        template = templates[stage][config.detection_prompt]
        return [template["system"] + "\n\n" + template["user"].format(sentence=s["text"]) for s in samples]
    if stage == "extraction":
        template = templates[stage][config.extraction_prompt]
        return [template.format(input_sentence=s["text"]) for s in samples]
    raise ValueError(f"未知阶段：{stage}")


def parse_author_json(response: str) -> tuple[dict[str, Any], str]:
    """沿用作者首个左括号到最后右括号的 JSON 解析规则，同时显式记录失败。"""

    start, end = response.find("{"), response.rfind("}")
    if start < 0 or end < start:
        return {}, "missing_json_object"
    try:
        parsed = json.loads(response[start:end + 1])
    except json.JSONDecodeError as exc:
        return {}, f"invalid_json: {exc.msg}"
    if not isinstance(parsed, dict):
        return {}, "expected_json_object"
    return parsed, ""


def parse_detection(response: str) -> tuple[str | None, str]:
    """只接受作者定义的 causal/noncausal，不用抽取结果反推检测标签。"""

    parsed, error = parse_author_json(response)
    if error:
        return None, error
    label = parsed.get("answer")
    if label not in ("causal", "noncausal"):
        return None, "invalid_detection_label"
    return label, ""


def prediction_from_author_outputs(
    sample_id: Any, detection_response: str, extraction_response: str | None,
) -> dict[str, Any]:
    """将作者平铺的多对字段映射到 evaluator；保留方向、重复预测和非原文 span。"""

    label, detection_error = parse_detection(detection_response)
    triples: list[dict[str, Any]] = []
    extraction_errors: list[str] = []
    if label == "causal":
        if extraction_response is None:
            raise ValueError(f"预测正例 {sample_id} 缺少抽取输出")
        parsed, error = parse_author_json(extraction_response)
        if error:
            extraction_errors.append(error)
        suffixes: set[str] = set()
        for key in parsed:
            match = re.fullmatch(r"(?:cause|effect)(_(?:[2-9]|[1-9][0-9]+))?", key)
            if match:
                suffixes.add(match.group(1) or "")
        if not error and not suffixes:
            extraction_errors.append("missing_cause_effect_fields")
        for suffix in sorted(suffixes, key=lambda value: int(value[1:]) if value else 1):
            cause, effect = parsed.get(f"cause{suffix}"), parsed.get(f"effect{suffix}")
            if not isinstance(cause, str) or not isinstance(effect, str) or not cause.strip() or not effect.strip():
                extraction_errors.append(f"incomplete_pair{suffix}")
                continue
            triples.append({"cause": {"span": cause}, "effect": {"span": effect}})
    return {
        "id": sample_id,
        "has_causal": label == "causal",
        "triples": triples,
        "source": "anuyah2025_pcd_mistral",
        "detection_label": label,
        "detection_error": detection_error,
        "extraction_errors": extraction_errors,
    }


class _ContinuationTokenizer:
    """仅修正作者输出分离：按输入 token 数去掉前缀，不依赖解码字符串逐字相同。"""

    def __init__(self, tokenizer: Any) -> None:
        self.tokenizer = tokenizer
        self.input_width = 0

    def __getattr__(self, name: str) -> Any:
        return getattr(self.tokenizer, name)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        inputs = self.tokenizer(*args, **kwargs)
        self.input_width = inputs["input_ids"].shape[1]
        return inputs

    def batch_decode(self, output_ids: Any, **kwargs: Any) -> list[str]:
        """原脚本仍执行所有生成步骤；只将续写部分交给其 JSON 解析逻辑。"""

        return self.tokenizer.batch_decode(output_ids[:, self.input_width:], **kwargs)


class AuthorRunner:
    """复用本地作者脚本；检测 FP4 默认设置与抽取 NF4 分别加载，避免占用两份显存。"""

    def __init__(self, source_dir: Path | str = DEFAULT_SOURCE_DIR, config: RunConfig | None = None) -> None:
        self.source_dir = Path(source_dir)
        self.config = config or RunConfig()
        self.templates = load_author_templates(self.source_dir)
        self.stage: str | None = None
        self.model: Any = None
        self.tokenizer: Any = None
        self.pipe: Any = None
        self.script: Any = None
        self.runtime: dict[str, Any] = {}

    def prepare(self, stage: str) -> None:
        """按作者配置加载某个阶段；首次调用由 Transformers 下载官方权重。"""

        if stage not in ("detection", "extraction"):
            raise ValueError(f"未知阶段：{stage}")
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TextGenerationPipeline

        if not torch.cuda.is_available():
            raise RuntimeError("当前 kernel 的 PyTorch 无法使用 CUDA；请先执行 notebook 的环境安装步骤并重启 kernel。")
        if self.stage != stage:
            self.close()
            self.script = _load_author_script(self.source_dir, stage)
        # 每个阶段在加载模型之前初始化随机状态，与作者独立实验的顺序一致。
        from transformers import set_seed

        set_seed(self.config.seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        if self.stage != stage:
            name = self.config.model_name_or_path
            self.tokenizer = AutoTokenizer.from_pretrained(name, padding_side="left")
            self.tokenizer.pad_token = self.tokenizer.eos_token
            if stage == "detection":
                self.model = AutoModelForCausalLM.from_pretrained(
                    name, quantization_config=BitsAndBytesConfig(load_in_4bit=True), device_map="auto",
                )
                self.pipe = TextGenerationPipeline(model=self.model, tokenizer=self.tokenizer)
            else:
                self.model = self.script.quantize_4bit(name)
            self.model.eval()
            self.stage = stage
        quantization = self.model.config.quantization_config
        self.runtime[stage] = {
            "model_commit": getattr(self.model.config, "_commit_hash", None),
            "quantization_config": quantization.to_dict() if hasattr(quantization, "to_dict") else quantization,
            "generation_config": self.model.generation_config.to_dict(),
            "gpu": torch.cuda.get_device_name(0),
        }
        if self.pipe is not None and hasattr(self.pipe, "generation_config"):
            self.runtime[stage]["pipeline_generation_config"] = self.pipe.generation_config.to_dict()

    def generate(self, prompts: list[str]) -> list[str]:
        """检测沿用作者 pipeline 调用，抽取直接调用其 run_llm_batch。"""

        if self.stage == "detection":
            outputs = self.pipe(
                prompts, max_new_tokens=self.config.detection_max_new_tokens,
                batch_size=self.config.batch_size, truncation=True,
                return_full_text=False, pad_token_id=self.tokenizer.eos_token_id,
            )
            return [row[0]["generated_text"].strip() for row in outputs]
        if self.stage == "extraction":
            outputs, _ = self.script.run_llm_batch(
                self.model, _ContinuationTokenizer(self.tokenizer), prompts,
                batch_size=self.config.batch_size, top_k=self.config.extraction_top_k,
                temperature=self.config.extraction_temperature,
                max_new_tokens=self.config.extraction_max_new_tokens,
            )
            return outputs
        raise RuntimeError("请先 prepare 一个阶段")

    def close(self) -> None:
        """释放当前阶段的模型；不会卸载其他应用持有的模型。"""

        self.pipe = self.model = self.tokenizer = self.script = None
        self.stage = None
        gc.collect()
        if "torch" in sys.modules:
            torch = sys.modules["torch"]
            if torch.cuda.is_available():
                torch.cuda.empty_cache()


def _json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def software_versions() -> dict[str, str | None]:
    """记录影响模型加载和解码的依赖版本；缺失依赖留空，便于在 CPU 环境先检查数据。"""

    versions: dict[str, str | None] = {"python": sys.version.split()[0]}
    for name in ("torch", "transformers", "accelerate", "bitsandbytes", "tokenizers", "numpy", "pandas"):
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    return versions


def _run_stage(
    samples: Sequence[Mapping[str, Any]], stage: str, runner: Any, path: Path, reuse: bool,
) -> list[dict[str, Any]]:
    expected_ids = [s["id"] for s in samples]
    if reuse and path.is_file():
        try:
            saved = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        except json.JSONDecodeError:
            saved = []
            logger.warning("%s 检查点不完整，将从该阶段开头重新运行", stage)
        if (all(isinstance(r, dict) and isinstance(r.get("response"), str) for r in saved)
                and [r.get("id") for r in saved] == expected_ids):
            logger.info("复用已完整保存的 %s 阶段：%s 条", stage, len(saved))
            return saved
    rows: list[dict[str, Any]] = []
    if samples:
        runner.prepare(stage)
    with path.open("w", encoding="utf-8") as file:
        for start in range(0, len(samples), runner.config.batch_size):
            batch = samples[start:start + runner.config.batch_size]
            prompts = build_prompts(batch, stage, runner.templates, runner.config)
            started = time.perf_counter()
            responses = runner.generate(prompts)
            elapsed = time.perf_counter() - started
            if len(responses) != len(batch) or not all(isinstance(s, str) for s in responses):
                raise RuntimeError("生成输出与输入 batch 不对应，停止保存，避免错配样本")
            for sample, response in zip(batch, responses):
                row = {"id": sample["id"], "response": response, "seconds_per_sample": elapsed / len(batch)}
                file.write(_json(row) + "\n")
                rows.append(row)
            file.flush()
            logger.info("%s：%s/%s", stage, len(rows), len(samples))
    return rows


def run_causal_discovery_baseline(
    samples: Sequence[Mapping[str, Any]], runner: Any, dataset: str,
    output_dir: Path | str, run_name: str, primary_metric: str | None = None,
    reuse_completed_stages: bool = True,
) -> dict[str, Any]:
    """导出作者 CSV、预测正例门控抽取、保存原始输出，并在完整样本集合上运行 evaluator。"""

    from src.evaluator import Evaluator

    if not samples:
        raise ValueError("评估样本不能为空")
    if not run_name or Path(run_name).name != run_name or run_name in (".", ".."):
        raise ValueError("run_name 必须为文件名，不能包含路径")
    ids = [_json(s["id"]) for s in samples]
    if len(set(ids)) != len(ids):
        raise ValueError("样本 id 不唯一，无法保证输出一对一映射")
    if any(not isinstance(s.get("text"), str) or not s["text"].strip() for s in samples):
        raise ValueError("每条样本必须包含非空 text")
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    paths = {key: output / f"{run_name}.{suffix}" for key, suffix in {
        "manifest": "manifest.json", "input_csv": "input.csv",
        "extraction_input_csv": "extraction_input.csv", "detection_raw": "detection.raw.jsonl",
        "extraction_raw": "extraction.raw.jsonl", "predictions": "predictions.jsonl",
        "report_json": "report.json", "report_md": "report.md",
    }.items()}
    identity = {
        "adapter_version": 1, "dataset": dataset, "config": asdict(runner.config),
        "adapter_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_sha256": runner.templates["source_sha256"],
        "input_sha256": hashlib.sha256(_json([{"id": s["id"], "text": s["text"]} for s in samples]).encode()).hexdigest(),
        "packages": software_versions(),
        "extraction_scope": "predicted_causal_only", "prompt_modified": False,
        "output_decode": "continuation_tokens_only",
    }
    fingerprint = hashlib.sha256(_json(identity).encode()).hexdigest()
    old: dict[str, Any] = {}
    if paths["manifest"].is_file():
        old = json.loads(paths["manifest"].read_text(encoding="utf-8"))
        if old.get("fingerprint") != fingerprint:
            raise ValueError("同名运行的输入、源码或配置已变化；请修改 run_name，避免混用旧预测")
    elif any(path.exists() for key, path in paths.items() if key != "manifest"):
        raise ValueError("发现没有 manifest 的同名输出，请使用新的 run_name")
    manifest = {**identity, "fingerprint": fingerprint, "n_samples": len(samples), "runtime": old.get("runtime", {})}
    _write_json(paths["manifest"], manifest)

    def export_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
        # CSV 中不写 gold 标签或关系；这些字段只在最后的 evaluator 中使用。
        with path.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "sentence"])
            writer.writeheader()
            writer.writerows({"id": s["id"], "sentence": s["text"]} for s in rows)

    export_csv(paths["input_csv"], samples)
    runner.runtime.clear()
    try:
        detection = _run_stage(samples, "detection", runner, paths["detection_raw"], reuse_completed_stages)
        positives = [s for s, r in zip(samples, detection) if parse_detection(r["response"])[0] == "causal"]
        export_csv(paths["extraction_input_csv"], positives)
        extraction = _run_stage(positives, "extraction", runner, paths["extraction_raw"], reuse_completed_stages)
    finally:
        manifest["runtime"].update(runner.runtime)
        _write_json(paths["manifest"], manifest)
        runner.close()
    extracted = {_json(r["id"]): r["response"] for r in extraction}
    predictions = [prediction_from_author_outputs(s["id"], r["response"], extracted.get(_json(s["id"])))
                   for s, r in zip(samples, detection)]
    evaluator = Evaluator(dataset=dataset, primary_metric=primary_metric)
    for prediction, gold in zip(predictions, samples):
        evaluator.update(prediction=prediction, gold=dict(gold))
    report = evaluator.report()
    diagnostics = {
        "invalid_detection_outputs": sum(bool(p["detection_error"]) for p in predictions),
        "invalid_extraction_outputs": sum(bool(p["extraction_errors"]) for p in predictions),
        "n_extraction_inputs": len(positives),
        "nonverbatim_pairs": sum(
            t["cause"]["span"] not in s["text"] or t["effect"]["span"] not in s["text"]
            for s, p in zip(samples, predictions) for t in p["triples"]
        ),
    }
    report["baseline"] = {"manifest": str(paths["manifest"]), "diagnostics": diagnostics}
    formatted = evaluator.format_report(title=f"Anuyah et al. (2025) / Mistral-7B: {dataset}")
    formatted += "\n\n适配诊断：\n" + json.dumps(diagnostics, ensure_ascii=False, indent=2)
    with paths["predictions"].open("w", encoding="utf-8") as file:
        for row in predictions:
            file.write(_json(row) + "\n")
    _write_json(paths["report_json"], report)
    paths["report_md"].write_text(formatted, encoding="utf-8")
    return {"dataset": dataset, "n_samples": len(samples), "predictions": predictions,
            "report": report, "formatted_report": formatted, "paths": paths}
