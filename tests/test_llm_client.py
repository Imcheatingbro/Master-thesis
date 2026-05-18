"""SPEC_02：LM Studio 客户端封装的单元测试。"""

from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.llm_client import LLMClient


class FakeModels:
    """用于测试 ping 的假 models API。"""

    def __init__(self, should_fail: bool = False) -> None:
        self.should_fail = should_fail

    def list(self) -> list[str]:
        if self.should_fail:
            raise OSError("连接失败")
        return ["qwen/qwen3-14b"]


class FakeChatCompletions:
    """用于测试 chat 重试逻辑的假 completions API。"""

    def __init__(self, failures_before_success: int) -> None:
        self.failures_before_success = failures_before_success
        self.calls = 0

    def create(self, **kwargs: object) -> SimpleNamespace:
        self.calls += 1
        if self.calls <= self.failures_before_success:
            raise TimeoutError("临时超时")
        return SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content=f"ok:{kwargs['model']}:{kwargs['temperature']}")
                )
            ]
        )


class FakeOpenAI:
    """模拟 OpenAI SDK 客户端对象。"""

    def __init__(self, failures_before_success: int = 0, ping_fail: bool = False) -> None:
        self.models = FakeModels(should_fail=ping_fail)
        self.chat = SimpleNamespace(completions=FakeChatCompletions(failures_before_success))


def write_config(path: Path) -> None:
    """写入最小测试配置。"""
    path.write_text(
        """
llm:
  base_url: "http://127.0.0.1:1234/v1"
  model: "qwen/qwen3-14b"
  api_key: "lm-studio"
  temperature: 0.0
  max_tokens: 2048
  timeout: 120
  retry_times: 3
""".lstrip(),
        encoding="utf-8",
    )


def test_client_loads_config_and_allows_overrides(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)

    client = LLMClient(config_path=config_path, model="override-model", temperature=0.2)

    assert client.base_url == "http://127.0.0.1:1234/v1"
    assert client.model == "override-model"
    assert client.temperature == 0.2
    assert client.max_tokens == 2048


def test_ping_returns_true_when_models_endpoint_is_reachable(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    client = LLMClient(config_path=config_path, openai_client=FakeOpenAI())

    assert client.ping() is True


def test_ping_returns_false_when_models_endpoint_fails(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    client = LLMClient(config_path=config_path, openai_client=FakeOpenAI(ping_fail=True))

    assert client.ping() is False


def test_chat_retries_transient_failures_and_returns_text(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    fake_client = FakeOpenAI(failures_before_success=2)
    client = LLMClient(config_path=config_path, openai_client=fake_client)
    monkeypatch.setattr("src.llm_client.time.sleep", lambda _: None)

    result = client.chat([{"role": "user", "content": "hello"}])

    assert result == "ok:qwen/qwen3-14b:0.0"
    assert fake_client.chat.completions.calls == 3
