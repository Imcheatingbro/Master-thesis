"""SPEC_05 适配：通过 LM Studio 运行 GoLLIE-13B 联合因果检测与抽取。"""

from __future__ import annotations

import ast
import csv
import hashlib
import importlib.metadata
import json
import logging
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


logger = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = PROJECT_ROOT / "reference code from related work" / "GoLLIE-main" / "GoLLIE-main"
DEFAULT_BASE_URL = "http://127.0.0.1:1234/v1"
DEFAULT_MODEL_ID = "hitz-gollie-13b-assafetensors"
MODEL_DISPLAY_NAME = "GoLLIE-13B (Q8_0 GGUF)"
SOURCE_FILES = (
    "README.md",
    "notebooks/Create Custom Task.ipynb",
    "notebooks/Relation Extraction.ipynb",
    "configs/model_configs/eval/GoLLIE-13B_CodeLLaMA.yaml",
)

GUIDELINES = '''@dataclass
class CausalRelation(Relation):
    """A cause-effect relation asserted in the text. The cause brings about,
    contributes to, enables, prevents, or changes the effect. Annotate every
    distinct causal relation stated or clearly communicated by the text. Do not
    infer relations from outside knowledge. Return no instance when the text does
    not communicate a causal relation."""

    arg1: str
    """The exact continuous text span expressing the cause. Copy it verbatim and
    use the smallest complete span that identifies the causal argument."""

    arg2: str
    """The exact continuous text span expressing the effect. Copy it verbatim and
    use the smallest complete span that identifies the causal argument."""
'''

PROMPT_TEMPLATE = '''# The following lines describe the task definition
{guidelines}
# This is the text to analyze
text = {text}

# The annotation instances that take place in the text above are listed here
result = ['''


@dataclass(frozen=True)
class RunConfig:
    """保存 GoLLIE 的固定本地推理配置。"""

    model: str = DEFAULT_MODEL_ID
    base_url: str = DEFAULT_BASE_URL
    max_tokens: int = 1024
    temperature: float = 0.0
    seed: int = 4000
    timeout: float = 300.0
    retry_times: int = 3
    cache_prompt: bool = False
    quantization: str = "Q8_0 GGUF"

    def __post_init__(self) -> None:
        if self.max_tokens < 1:
            raise ValueError("max_tokens 必须大于 0")
        if self.temperature != 0.0:
            raise ValueError("GoLLIE baseline 固定使用 greedy decoding，temperature 必须为 0")
        if self.retry_times < 1:
            raise ValueError("retry_times 必须大于 0")


def build_prompt(sample: Mapping[str, Any]) -> str:
    """按作者 Relation Extraction 模板构造零样本代码式 prompt，且只读取原始 text。"""

    text = sample.get("text")
    if not isinstance(text, str) or not text.strip():
        raise ValueError("样本必须包含非空 text")
    return PROMPT_TEMPLATE.format(guidelines=GUIDELINES.rstrip(), text=repr(text))


def source_hashes(source_dir: Path | str = DEFAULT_SOURCE_DIR) -> dict[str, str]:
    """核对并记录本地作者源码中与本适配直接相关的文件。"""

    root = Path(source_dir)
    hashes: dict[str, str] = {}
    for relative in SOURCE_FILES:
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(f"缺少 GoLLIE 作者文件：{path}")
        hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def _response_fragment(response: str) -> str:
    fragment = response.strip()
    if "result =" in fragment:
        fragment = fragment.rsplit("result =", 1)[1].strip()
    if fragment.startswith("```python"):
        fragment = fragment[len("```python"):].lstrip()
    elif fragment.startswith("```"):
        fragment = fragment[3:].lstrip()
    # 作者 README 指定从 `result = [` 后开始续写；raw completion 因而通常不再包含左方括号。
    if not fragment.lstrip().startswith("["):
        fragment = "[" + fragment
    return fragment


def _first_balanced_list(text: str) -> str | None:
    start = text.find("[")
    if start < 0:
        return None
    depth = 0
    quote: str | None = None
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if quote is not None:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in ("'", '"'):
            quote = char
        elif char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return text[start:index + 1]
    return None


def _literal_string(node: ast.AST) -> str | None:
    try:
        value = ast.literal_eval(node)
    except (ValueError, SyntaxError):
        return None
    return value if isinstance(value, str) else None


def parse_gollie_output(response: str) -> tuple[list[dict[str, str]], list[str]]:
    """安全解析 GoLLIE 的 Python 列表，不执行模型生成的代码。"""

    literal = _first_balanced_list(_response_fragment(response))
    if literal is None:
        return [], ["missing_or_unclosed_list"]
    try:
        tree = ast.parse(literal, mode="eval")
    except SyntaxError as exc:
        return [], [f"invalid_python_list: {exc.msg}"]
    if not isinstance(tree.body, ast.List):
        return [], ["expected_list"]

    pairs: list[dict[str, str]] = []
    errors: list[str] = []
    for index, element in enumerate(tree.body.elts, start=1):
        if not isinstance(element, ast.Call) or not isinstance(element.func, ast.Name):
            errors.append(f"annotation_{index}: expected_class_call")
            continue
        if element.func.id != "CausalRelation":
            errors.append(f"annotation_{index}: unexpected_class_{element.func.id}")
            continue
        values: dict[str, str | None] = {}
        if element.args:
            if len(element.args) != 2 or element.keywords:
                errors.append(f"annotation_{index}: invalid_arguments")
                continue
            values = {"arg1": _literal_string(element.args[0]), "arg2": _literal_string(element.args[1])}
        else:
            if any(keyword.arg not in {"arg1", "arg2"} for keyword in element.keywords):
                errors.append(f"annotation_{index}: unexpected_field")
                continue
            if len({keyword.arg for keyword in element.keywords}) != len(element.keywords):
                errors.append(f"annotation_{index}: duplicate_field")
                continue
            values = {keyword.arg: _literal_string(keyword.value) for keyword in element.keywords if keyword.arg}
        cause, effect = values.get("arg1"), values.get("arg2")
        if not cause or not effect:
            errors.append(f"annotation_{index}: missing_or_non_string_span")
            continue
        pairs.append({"cause": cause, "effect": effect})
    return pairs, errors


def prediction_from_gollie_output(sample_id: Any, response: str) -> dict[str, Any]:
    """把 GoLLIE 联合抽取结果映射为项目 evaluator 的 prediction schema。"""

    pairs, errors = parse_gollie_output(response)
    triples = [
        {"cause": {"span": pair["cause"]}, "effect": {"span": pair["effect"]}}
        for pair in pairs
    ]
    return {
        "id": sample_id,
        "has_causal": bool(triples),
        "triples": triples,
        "source": "sainz2024_gollie13b_q8_0_lmstudio",
        "parse_errors": errors,
    }


class LMStudioGoLLIERunner:
    """使用 OpenAI-compatible raw completion 接口调用本地 GoLLIE。"""

    RETRYABLE_STATUS = {408, 409, 429, 500, 502, 503, 504}

    def __init__(self, config: RunConfig | None = None, source_dir: Path | str = DEFAULT_SOURCE_DIR) -> None:
        self.config = config or RunConfig()
        self.source_dir = Path(source_dir)
        self.source_sha256 = source_hashes(self.source_dir)
        self.runtime: dict[str, Any] = {
            "request_count": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        }
        self.identity = {
            "provider": "LM Studio",
            "endpoint": self.config.base_url.rstrip("/") + "/completions",
            "transport": "raw_completion_without_chat_template",
            "model": self.config.model,
            "upstream_model": "HiTZ/GoLLIE-13B",
            "gguf_repository": "mradermacher/HiTZ-GoLLIE-13B-AsSafeTensors-GGUF",
            "quantization": self.config.quantization,
            "thinking": "not_applicable_disabled",
        }

    def list_models(self) -> list[str]:
        """返回 LM Studio 当前公开的模型 ID。"""

        request = Request(self.config.base_url.rstrip("/") + "/models", headers={"Accept": "application/json"})
        try:
            with urlopen(request, timeout=min(self.config.timeout, 10.0)) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"无法连接 LM Studio：{exc}") from exc
        return [row["id"] for row in payload.get("data", []) if isinstance(row, dict) and isinstance(row.get("id"), str)]

    def model_metadata(self) -> dict[str, Any]:
        """读取 LM Studio 原生接口中的实际格式、量化和加载配置。"""

        server_root = self.config.base_url.rstrip("/")
        if server_root.endswith("/v1"):
            server_root = server_root[:-3]
        request = Request(server_root + "/api/v1/models", headers={"Accept": "application/json"})
        try:
            with urlopen(request, timeout=min(self.config.timeout, 10.0)) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"无法读取 LM Studio 模型元数据：{exc}") from exc
        for row in payload.get("models", []):
            if isinstance(row, dict) and row.get("key") == self.config.model:
                return row
        raise RuntimeError(f"LM Studio 模型元数据中找不到 {self.config.model}")

    def require_model(self) -> list[str]:
        """确认 LM Studio 服务可用且指定 GoLLIE 模型可见。"""

        models = self.list_models()
        if self.config.model not in models:
            raise RuntimeError(
                f"LM Studio 未公开模型 {self.config.model}；当前模型：{', '.join(models) or '无'}"
            )
        metadata = self.model_metadata()
        actual_quantization = (metadata.get("quantization") or {}).get("name")
        if actual_quantization != "Q8_0":
            raise RuntimeError(f"当前 GoLLIE 量化为 {actual_quantization}，预期 Q8_0")
        if not metadata.get("loaded_instances"):
            raise RuntimeError("GoLLIE 模型存在但尚未加载；请先在 LM Studio 中加载它")
        self.identity["lmstudio_model_metadata"] = {
            key: metadata.get(key)
            for key in ("publisher", "key", "display_name", "architecture", "quantization", "size_bytes", "params_string", "format")
        }
        self.identity["lmstudio_load_config"] = metadata["loaded_instances"][0].get("config", {})
        return models

    def generate(self, prompt: str) -> str:
        """按作者 greedy 设置生成一个 Python 列表 completion。"""

        payload = {
            "model": self.config.model,
            "prompt": prompt,
            "max_tokens": self.config.max_tokens,
            "temperature": self.config.temperature,
            "top_p": 1.0,
            "seed": self.config.seed,
            "stream": False,
            "echo": False,
            "cache_prompt": self.config.cache_prompt,
        }
        request = Request(
            self.config.base_url.rstrip("/") + "/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": "Bearer lm-studio"},
            method="POST",
        )
        result: dict[str, Any] | None = None
        for attempt in range(1, self.config.retry_times + 1):
            try:
                with urlopen(request, timeout=self.config.timeout) as response:
                    result = json.loads(response.read().decode("utf-8"))
                break
            except HTTPError as exc:
                if exc.code not in self.RETRYABLE_STATUS or attempt == self.config.retry_times:
                    detail = exc.read().decode("utf-8", errors="replace")[:500]
                    raise RuntimeError(f"LM Studio HTTP {exc.code}: {detail}") from exc
                time.sleep(min(2 ** (attempt - 1), 10.0))
            except (URLError, TimeoutError) as exc:
                if attempt == self.config.retry_times:
                    raise RuntimeError(f"LM Studio 请求失败：{exc}") from exc
                time.sleep(min(2 ** (attempt - 1), 10.0))
        if result is None:
            raise RuntimeError("LM Studio 未返回响应")
        try:
            content = result["choices"][0]["text"]
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(f"LM Studio completion 结构异常：{str(result)[:500]}") from exc
        if not isinstance(content, str) or not content.strip():
            raise RuntimeError("LM Studio 返回空 completion")
        usage = result.get("usage") or {}
        self.runtime["request_count"] += 1
        for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
            self.runtime[key] += int(usage.get(key) or 0)
        return content.strip()


def software_versions() -> dict[str, str | None]:
    """记录 baseline 运行环境中会影响数据、HTTP 与评估的依赖版本。"""

    versions: dict[str, str | None] = {"python": sys.version.split()[0]}
    for name in ("numpy", "pandas", "requests", "tqdm", "ipykernel"):
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    return versions


def _json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _load_saved_prefix(path: Path, expected_ids: Sequence[Any]) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            logger.warning("忽略原始输出末尾的不完整 JSON 行：%s", path)
            break
        if not isinstance(row, dict) or not isinstance(row.get("response"), str):
            raise ValueError(f"原始输出包含非法记录：{path}")
        rows.append(row)
    if [row.get("id") for row in rows] != list(expected_ids[:len(rows)]):
        raise ValueError("原始输出 ID 不是当前输入的连续前缀，拒绝错配续跑")
    return rows


def run_gollie_baseline(
    samples: Sequence[Mapping[str, Any]],
    runner: LMStudioGoLLIERunner,
    dataset: str,
    output_dir: Path | str,
    run_name: str,
    primary_metric: str | None = None,
    reuse_checkpoint: bool = True,
    progress_callback: Callable[[int, int], None] | None = None,
) -> dict[str, Any]:
    """运行单阶段 GoLLIE 联合抽取，保存审计文件并调用统一 evaluator。"""

    from src.evaluator import Evaluator

    if not samples:
        raise ValueError("评估样本不能为空")
    if not run_name or Path(run_name).name != run_name or run_name in {".", ".."}:
        raise ValueError("run_name 必须为文件名，不能包含路径")
    ids = [_json(sample.get("id")) for sample in samples]
    if len(set(ids)) != len(ids):
        raise ValueError("样本 id 不唯一，无法保证预测一对一映射")
    for sample in samples:
        build_prompt(sample)

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    paths = {key: output / f"{run_name}.{suffix}" for key, suffix in {
        "manifest": "manifest.json",
        "input_csv": "input.csv",
        "raw": "raw.jsonl",
        "predictions": "predictions.jsonl",
        "report_json": "report.json",
        "report_md": "report.md",
    }.items()}
    identity = {
        "adapter_version": 1,
        "dataset": dataset,
        "config": asdict(runner.config),
        "runner": runner.identity,
        "adapter_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_sha256": runner.source_sha256,
        "prompt_sha256": hashlib.sha256(GUIDELINES.encode("utf-8")).hexdigest(),
        "input_sha256": hashlib.sha256(
            _json([{"id": sample["id"], "text": sample["text"]} for sample in samples]).encode("utf-8")
        ).hexdigest(),
        "packages": software_versions(),
        "task_mode": "single_stage_joint_detection_and_extraction",
        "prompt_template": "author_relation_extraction_template",
        "author_prompt_structure_modified": False,
        "custom_task_guideline": "fixed_cross_dataset_causal_relation_schema",
    }
    fingerprint = hashlib.sha256(_json(identity).encode("utf-8")).hexdigest()
    old_manifest: dict[str, Any] = {}
    if paths["manifest"].is_file():
        old_manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
        if old_manifest.get("fingerprint") != fingerprint:
            raise ValueError("同名运行的输入、源码或配置已变化；请修改 run_name")
    elif any(path.exists() for key, path in paths.items() if key != "manifest"):
        raise ValueError("发现没有 manifest 的同名输出；请修改 run_name")
    manifest = {
        **identity,
        "fingerprint": fingerprint,
        "n_samples": len(samples),
        "runtime": old_manifest.get("runtime", {}),
    }
    _write_json(paths["manifest"], manifest)

    with paths["input_csv"].open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "sentence"])
        writer.writeheader()
        writer.writerows({"id": sample["id"], "sentence": sample["text"]} for sample in samples)

    saved = _load_saved_prefix(paths["raw"], [sample["id"] for sample in samples]) if reuse_checkpoint else []
    if progress_callback is not None:
        progress_callback(len(saved), len(samples))
    mode = "a" if saved else "w"
    try:
        with paths["raw"].open(mode, encoding="utf-8") as file:
            for sample in samples[len(saved):]:
                started = time.perf_counter()
                response = runner.generate(build_prompt(sample))
                row = {
                    "id": sample["id"],
                    "response": response,
                    "seconds": time.perf_counter() - started,
                }
                file.write(_json(row) + "\n")
                file.flush()
                saved.append(row)
                logger.info("GoLLIE %s：%s/%s", dataset, len(saved), len(samples))
                if progress_callback is not None:
                    progress_callback(len(saved), len(samples))
    finally:
        manifest["runtime"] = dict(runner.runtime)
        _write_json(paths["manifest"], manifest)

    predictions = [
        prediction_from_gollie_output(sample["id"], row["response"])
        for sample, row in zip(samples, saved)
    ]
    evaluator = Evaluator(dataset=dataset, primary_metric=primary_metric)
    for prediction, gold in zip(predictions, samples):
        evaluator.update(prediction=prediction, gold=dict(gold))
    report = evaluator.report()
    diagnostics = {
        "parse_error_samples": sum(bool(prediction["parse_errors"]) for prediction in predictions),
        "predicted_positive_samples": sum(prediction["has_causal"] for prediction in predictions),
        "predicted_pairs": sum(len(prediction["triples"]) for prediction in predictions),
        "nonverbatim_pairs": sum(
            triple["cause"]["span"].lower() not in sample["text"].lower()
            or triple["effect"]["span"].lower() not in sample["text"].lower()
            for sample, prediction in zip(samples, predictions)
            for triple in prediction["triples"]
        ),
    }
    report["baseline"] = {"manifest": str(paths["manifest"]), "diagnostics": diagnostics}
    formatted = evaluator.format_report(title=f"{MODEL_DISPLAY_NAME} / LM Studio: {dataset}")
    formatted += "\n\n适配诊断：\n" + json.dumps(diagnostics, ensure_ascii=False, indent=2)
    with paths["predictions"].open("w", encoding="utf-8") as file:
        for prediction in predictions:
            file.write(_json(prediction) + "\n")
    _write_json(paths["report_json"], report)
    paths["report_md"].write_text(formatted, encoding="utf-8")
    return {
        "dataset": dataset,
        "n_samples": len(samples),
        "predictions": predictions,
        "report": report,
        "formatted_report": formatted,
        "paths": paths,
    }
