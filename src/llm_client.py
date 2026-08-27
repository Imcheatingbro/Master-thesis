"""SPEC_02：封装 LM Studio 兼容 OpenAI Chat Completion API 的客户端。"""

from __future__ import annotations

import json
import logging
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

import yaml
from openai import OpenAI


LOGGER = logging.getLogger(__name__)
DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "llm.yaml"
DEFAULT_LMSTUDIO_EXTRA_BODY: dict[str, Any] = {"cache_prompt": False}


class LLMEmptyContentError(RuntimeError):
    """LM Studio 没有返回可解析正文时抛出的错误。"""


class LLMClient:
    """读取本地配置并调用 LM Studio Chat Completion API。"""

    def __init__(
        self,
        config_path: Path | str = DEFAULT_CONFIG_PATH,
        openai_client: Any | None = None,
        urlopen_func: Callable[..., Any] | None = None,
        **overrides: Any,
    ) -> None:
        config = self._load_config(Path(config_path))
        config.update({key: value for key, value in overrides.items() if value is not None})

        self.provider = str(config.get("provider", "lmstudio")).lower()
        self.base_url = str(config["base_url"])
        self.model = str(config["model"])
        self.api_key = str(config["api_key"])
        self.temperature = float(config["temperature"])
        self.max_tokens = int(config["max_tokens"])
        self.context_length = int(config.get("context_length", 8192))
        self.reasoning = config.get("reasoning")
        self.reasoning_effort = config.get("reasoning_effort")
        configured_extra_body = _load_extra_body(config.get("extra_body"))
        self.extra_body = (
            {**DEFAULT_LMSTUDIO_EXTRA_BODY, **configured_extra_body}
            if self.provider == "lmstudio"
            else configured_extra_body
        )
        self.timeout = float(config["timeout"])
        self.retry_times = int(config["retry_times"])
        self._client = openai_client or OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
            timeout=self.timeout,
        )
        self._urlopen = urlopen_func or urlopen

    @staticmethod
    def _load_config(config_path: Path) -> dict[str, Any]:
        with config_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}
        llm_config = data.get("llm")
        if not isinstance(llm_config, dict):
            raise ValueError(f"配置文件缺少 llm 字段：{config_path}")
        return dict(llm_config)

    def ping(self) -> bool:
        """调用 `/v1/models`，确认 LM Studio 服务是否可达。"""
        try:
            self._client.models.list()
        except Exception as exc:
            LOGGER.warning("LM Studio 连接测试失败：%s", exc)
            return False
        return True

    def list_models(self) -> list[str]:
        """返回 LM Studio `/v1/models` 当前可用的模型 ID 列表。"""
        response = self._client.models.list()
        data = getattr(response, "data", response)
        model_ids: list[str] = []
        for item in data:
            model_id = getattr(item, "id", item)
            if model_id:
                model_ids.append(str(model_id))
        return model_ids

    def list_loaded_models(self) -> list[str]:
        """返回 LM Studio 本地 API 中当前已加载的聊天模型 ID 列表。"""
        endpoint = self._lmstudio_models_endpoint()
        request = Request(endpoint)
        if self.api_key:
            request.add_header("Authorization", f"Bearer {self.api_key}")
        with self._urlopen(request, timeout=min(self.timeout, 10.0)) as response:
            payload = json.loads(response.read().decode("utf-8"))

        model_ids: list[str] = []
        for item in payload.get("data", []):
            if not isinstance(item, dict):
                continue
            if item.get("state") == "loaded" and item.get("type") in {"llm", "vlm"} and item.get("id"):
                model_ids.append(str(item["id"]))
        return model_ids

    def list_local_models(self) -> list[dict[str, Any]]:
        """返回 LM Studio REST API 中的本地模型及其加载实例。"""
        payload = self._request_lmstudio_json("GET", "/api/v1/models")
        models = payload.get("models")
        if not isinstance(models, list):
            raise ValueError("LM Studio /api/v1/models 响应缺少 models 列表")
        return [dict(item) for item in models if isinstance(item, dict)]

    def list_loaded_instances(self) -> list[str]:
        """返回 LM Studio 当前已加载的 LLM 实例 ID，不包含 embedding。"""
        instance_ids: list[str] = []
        for model in self.list_local_models():
            if model.get("type") != "llm":
                continue
            for instance in model.get("loaded_instances", []):
                if isinstance(instance, dict) and instance.get("id"):
                    instance_ids.append(str(instance["id"]))
        return instance_ids

    def load_model(
        self,
        model: str,
        *,
        context_length: int | None = None,
        parallel: int | None = None,
        flash_attention: bool = True,
        offload_kv_cache_to_gpu: bool = True,
    ) -> dict[str, Any]:
        """通过 LM Studio REST API 加载一个模型并返回实例信息。"""
        body: dict[str, Any] = {
            "model": model,
            "flash_attention": flash_attention,
            "offload_kv_cache_to_gpu": offload_kv_cache_to_gpu,
            "echo_load_config": True,
        }
        if context_length is not None:
            body["context_length"] = int(context_length)
        if parallel is not None:
            body["parallel"] = int(parallel)
        return self._request_lmstudio_json(
            "POST",
            "/api/v1/models/load",
            body,
            timeout=self.timeout,
        )

    def unload_model(self, instance_id: str) -> dict[str, Any]:
        """通过 LM Studio REST API 卸载指定模型实例。"""
        return self._request_lmstudio_json(
            "POST",
            "/api/v1/models/unload",
            {"instance_id": instance_id},
        )

    def unload_all_models(self) -> list[str]:
        """卸载当前所有 LLM 实例，并返回已卸载的实例 ID。"""
        instance_ids = self.list_loaded_instances()
        for instance_id in instance_ids:
            self.unload_model(instance_id)
        return instance_ids

    def chat_rest(
        self,
        input_text: str,
        *,
        model: str | None = None,
        system_prompt: str | None = None,
        reasoning: str = "off",
        max_output_tokens: int = 512,
        context_length: int | None = None,
    ) -> dict[str, Any]:
        """调用 LM Studio 原生 chat API，并保留 reasoning 统计供 smoke 检查。"""
        body: dict[str, Any] = {
            "model": model or self.model,
            "input": input_text,
            "temperature": self.temperature,
            "max_output_tokens": int(max_output_tokens),
            "reasoning": reasoning,
            "store": False,
        }
        if system_prompt:
            body["system_prompt"] = system_prompt
        if context_length is not None:
            body["context_length"] = int(context_length)
        return self._request_lmstudio_json(
            "POST",
            "/api/v1/chat",
            body,
            timeout=self.timeout,
        )

    def _lmstudio_models_endpoint(self) -> str:
        base_url = self.base_url.rstrip("/")
        if base_url.endswith("/v1"):
            base_url = base_url[:-3]
        return f"{base_url}/api/v0/models"

    def _lmstudio_api_v1_endpoint(self, path: str) -> str:
        base_url = self.base_url.rstrip("/")
        if base_url.endswith("/v1"):
            base_url = base_url[:-3]
        return f"{base_url}/{path.lstrip('/')}"

    def _request_lmstudio_json(
        self,
        method: str,
        path: str,
        body: dict[str, Any] | None = None,
        *,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        endpoint = self._lmstudio_api_v1_endpoint(path)
        data = json.dumps(body).encode("utf-8") if body is not None else None
        request = Request(endpoint, data=data, method=method)
        if self.api_key:
            request.add_header("Authorization", f"Bearer {self.api_key}")
        if data is not None:
            request.add_header("Content-Type", "application/json")
        with self._urlopen(request, timeout=timeout or min(self.timeout, 10.0)) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"LM Studio {path} 响应不是 JSON object")
        return payload

    def chat(self, messages: list[dict[str, str]]) -> str:
        """发送 OpenAI 格式 messages，并返回模型输出文本。"""
        start_time = time.perf_counter()
        input_chars = sum(len(message.get("content", "")) for message in messages)
        last_error: Exception | None = None

        for attempt in range(1, self.retry_times + 1):
            try:
                extra_body: dict[str, Any] = {}
                if self.provider == "lmstudio":
                    extra_body["context_length"] = self.context_length
                if self.reasoning is not None:
                    extra_body["reasoning"] = self.reasoning
                if self.reasoning_effort is not None:
                    extra_body["reasoning_effort"] = self.reasoning_effort
                extra_body.update(self.extra_body)
                response = self._client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    extra_body=extra_body,
                )
                choice = response.choices[0]
                message = choice.message
                content = message.content or ""
                finish_reason = getattr(choice, "finish_reason", None)
                reasoning_content = _extract_reasoning_content(message)
                if not content:
                    if reasoning_content:
                        raise LLMEmptyContentError(
                            "模型只返回 reasoning_content，content 为空；"
                            f"finish_reason={finish_reason} reasoning_chars={len(reasoning_content)}"
                        )
                    raise LLMEmptyContentError(f"模型返回空 content；finish_reason={finish_reason}")
                elapsed = time.perf_counter() - start_time
                LOGGER.info(
                    "LLM 调用完成：attempt=%s elapsed=%.2fs input_chars=%s output_chars=%s",
                    attempt,
                    elapsed,
                    input_chars,
                    len(content),
                )
                return content
            except Exception as exc:
                last_error = exc
                LOGGER.warning("LLM 调用失败：attempt=%s/%s error=%s", attempt, self.retry_times, exc)
                if isinstance(exc, LLMEmptyContentError):
                    raise
                if attempt < self.retry_times:
                    time.sleep(2 ** (attempt - 1))

        detail = f"：{last_error}" if last_error is not None else ""
        raise RuntimeError(f"LLM 调用失败，已重试 {self.retry_times} 次{detail}") from last_error


def _extract_reasoning_content(message: Any) -> str:
    """兼容不同 OpenAI SDK 对自定义 reasoning 字段的存放方式。"""
    for field_name in ("reasoning_content", "reasoning"):
        value = getattr(message, field_name, None)
        if isinstance(value, str):
            return value

    model_extra = getattr(message, "model_extra", None)
    if isinstance(model_extra, dict):
        for field_name in ("reasoning_content", "reasoning"):
            value = model_extra.get(field_name)
            if isinstance(value, str):
                return value
    return ""


def _load_extra_body(value: Any) -> dict[str, Any]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ValueError("llm.extra_body 必须是 dict")
    return dict(value)
