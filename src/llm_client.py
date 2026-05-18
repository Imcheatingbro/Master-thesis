"""SPEC_02：封装 LM Studio 兼容 OpenAI Chat Completion API 的客户端。"""

from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import Any

import yaml
from openai import OpenAI


LOGGER = logging.getLogger(__name__)
DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "llm.yaml"


class LLMClient:
    """读取本地配置并调用 LM Studio Chat Completion API。"""

    def __init__(
        self,
        config_path: Path | str = DEFAULT_CONFIG_PATH,
        openai_client: Any | None = None,
        **overrides: Any,
    ) -> None:
        config = self._load_config(Path(config_path))
        config.update({key: value for key, value in overrides.items() if value is not None})

        self.base_url = str(config["base_url"])
        self.model = str(config["model"])
        self.api_key = str(config["api_key"])
        self.temperature = float(config["temperature"])
        self.max_tokens = int(config["max_tokens"])
        self.timeout = float(config["timeout"])
        self.retry_times = int(config["retry_times"])
        self._client = openai_client or OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
            timeout=self.timeout,
        )

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

    def chat(self, messages: list[dict[str, str]]) -> str:
        """发送 OpenAI 格式 messages，并返回模型输出文本。"""
        start_time = time.perf_counter()
        input_chars = sum(len(message.get("content", "")) for message in messages)
        last_error: Exception | None = None

        for attempt in range(1, self.retry_times + 1):
            try:
                response = self._client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )
                content = response.choices[0].message.content or ""
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
                if attempt < self.retry_times:
                    time.sleep(2 ** (attempt - 1))

        raise RuntimeError(f"LLM 调用失败，已重试 {self.retry_times} 次") from last_error
