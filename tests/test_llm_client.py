"""SPEC_02：LM Studio 客户端封装的单元测试。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.llm_client import LLMClient


class FakeModels:
    """用于测试 ping 的假 models API。"""

    def __init__(self, should_fail: bool = False, model_ids: list[str] | None = None) -> None:
        self.should_fail = should_fail
        self.model_ids = model_ids or ["qwen/qwen3-14b"]

    def list(self) -> SimpleNamespace:
        if self.should_fail:
            raise OSError("连接失败")
        return SimpleNamespace(data=[SimpleNamespace(id=model_id) for model_id in self.model_ids])


class FakeChatCompletions:
    """用于测试 chat 重试逻辑的假 completions API。"""

    def __init__(
        self,
        failures_before_success: int,
        response_message: SimpleNamespace | None = None,
        finish_reason: str = "stop",
    ) -> None:
        self.failures_before_success = failures_before_success
        self.response_message = response_message
        self.finish_reason = finish_reason
        self.calls = 0
        self.last_kwargs: dict[str, object] | None = None

    def create(self, **kwargs: object) -> SimpleNamespace:
        self.calls += 1
        self.last_kwargs = kwargs
        if self.calls <= self.failures_before_success:
            raise TimeoutError("临时超时")
        return SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=self.response_message
                    or SimpleNamespace(content=f"ok:{kwargs['model']}:{kwargs['temperature']}"),
                    finish_reason=self.finish_reason,
                )
            ]
        )


class FakeOpenAI:
    """模拟 OpenAI SDK 客户端对象。"""

    def __init__(
        self,
        failures_before_success: int = 0,
        ping_fail: bool = False,
        model_ids: list[str] | None = None,
        response_message: SimpleNamespace | None = None,
        finish_reason: str = "stop",
    ) -> None:
        self.models = FakeModels(should_fail=ping_fail, model_ids=model_ids)
        self.chat = SimpleNamespace(
            completions=FakeChatCompletions(
                failures_before_success,
                response_message=response_message,
                finish_reason=finish_reason,
            )
        )


class FakeHTTPResponse:
    """模拟 LM Studio 本地 HTTP API 响应。"""

    def __init__(self, payload: dict[str, object]) -> None:
        self.payload = payload

    def __enter__(self) -> "FakeHTTPResponse":
        return self

    def __exit__(self, *_: object) -> None:
        return None

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


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
  context_length: 8192
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
    assert client.context_length == 8192
    assert client.extra_body == {"cache_prompt": False}


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


def test_list_models_returns_model_ids_from_models_endpoint(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    client = LLMClient(
        config_path=config_path,
        openai_client=FakeOpenAI(model_ids=["qwen/qwen3-14b", "oneke"]),
    )

    assert client.list_models() == ["qwen/qwen3-14b", "oneke"]


def test_list_loaded_models_returns_only_loaded_chat_models_and_sends_api_token(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    calls: list[tuple[str, str | None, float]] = []

    def fake_urlopen(request: object, timeout: float) -> FakeHTTPResponse:
        calls.append(
            (
                getattr(request, "full_url"),
                request.get_header("Authorization"),
                timeout,
            )
        )
        return FakeHTTPResponse(
            {
                "data": [
                    {"id": "qwen/qwen3-14b", "type": "llm", "state": "loaded"},
                    {"id": "qwen3.5-9b.gguf", "type": "vlm", "state": "loaded"},
                    {"id": "oneke", "type": "llm", "state": "not-loaded"},
                    {"id": "text-embedding", "type": "embeddings", "state": "loaded"},
                ]
            }
        )

    client = LLMClient(
        config_path=config_path,
        api_key="real-token",
        openai_client=FakeOpenAI(),
        urlopen_func=fake_urlopen,
    )

    assert client.list_loaded_models() == ["qwen/qwen3-14b", "qwen3.5-9b.gguf"]
    assert calls == [("http://127.0.0.1:1234/api/v0/models", "Bearer real-token", 10.0)]


def test_lmstudio_model_management_and_no_reasoning_chat(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    calls: list[dict[str, object]] = []
    responses = iter(
        [
            {
                "models": [
                    {
                        "type": "llm",
                        "key": "qwen/qwen3.6-35b-a3b",
                        "loaded_instances": [{"id": "qwen-loaded"}],
                    },
                    {
                        "type": "embedding",
                        "key": "bge-small",
                        "loaded_instances": [{"id": "bge-loaded"}],
                    },
                ]
            },
            {"instance_id": "qwen/qwen3.6-35b-a3b", "status": "loaded"},
            {
                "model_instance_id": "qwen/qwen3.6-35b-a3b",
                "output": [{"type": "message", "content": '{"has_causal":true,"triples":[]}'}],
                "stats": {"reasoning_output_tokens": 0},
            },
            {"instance_id": "qwen-loaded"},
        ]
    )

    def fake_urlopen(request: object, timeout: float) -> FakeHTTPResponse:
        request_data = getattr(request, "data", None)
        calls.append(
            {
                "url": getattr(request, "full_url"),
                "method": getattr(request, "method"),
                "authorization": request.get_header("Authorization"),
                "content_type": request.get_header("Content-type"),
                "body": json.loads(request_data.decode("utf-8")) if request_data else None,
                "timeout": timeout,
            }
        )
        return FakeHTTPResponse(next(responses))

    client = LLMClient(
        config_path=config_path,
        api_key="real-token",
        timeout=900,
        openai_client=FakeOpenAI(),
        urlopen_func=fake_urlopen,
    )

    assert client.list_loaded_instances() == ["qwen-loaded"]
    load_result = client.load_model(
        "qwen/qwen3.6-35b-a3b",
        context_length=16384,
        parallel=1,
    )
    smoke_result = client.chat_rest(
        "Heavy rain caused flooding.",
        model=load_result["instance_id"],
        system_prompt="Output JSON only.",
        context_length=16384,
    )
    unload_result = client.unload_model("qwen-loaded")

    assert smoke_result["stats"]["reasoning_output_tokens"] == 0
    assert unload_result == {"instance_id": "qwen-loaded"}
    assert calls == [
        {
            "url": "http://127.0.0.1:1234/api/v1/models",
            "method": "GET",
            "authorization": "Bearer real-token",
            "content_type": None,
            "body": None,
            "timeout": 10.0,
        },
        {
            "url": "http://127.0.0.1:1234/api/v1/models/load",
            "method": "POST",
            "authorization": "Bearer real-token",
            "content_type": "application/json",
            "body": {
                "model": "qwen/qwen3.6-35b-a3b",
                "flash_attention": True,
                "offload_kv_cache_to_gpu": True,
                "echo_load_config": True,
                "context_length": 16384,
                "parallel": 1,
            },
            "timeout": 900.0,
        },
        {
            "url": "http://127.0.0.1:1234/api/v1/chat",
            "method": "POST",
            "authorization": "Bearer real-token",
            "content_type": "application/json",
            "body": {
                "model": "qwen/qwen3.6-35b-a3b",
                "input": "Heavy rain caused flooding.",
                "temperature": 0.0,
                "max_output_tokens": 512,
                "reasoning": "off",
                "store": False,
                "system_prompt": "Output JSON only.",
                "context_length": 16384,
            },
            "timeout": 900.0,
        },
        {
            "url": "http://127.0.0.1:1234/api/v1/models/unload",
            "method": "POST",
            "authorization": "Bearer real-token",
            "content_type": "application/json",
            "body": {"instance_id": "qwen-loaded"},
            "timeout": 10.0,
        },
    ]


def test_chat_retries_transient_failures_and_returns_text(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    fake_client = FakeOpenAI(failures_before_success=2)
    client = LLMClient(config_path=config_path, openai_client=fake_client)
    monkeypatch.setattr("src.llm_client.time.sleep", lambda _: None)

    result = client.chat([{"role": "user", "content": "hello"}])

    assert result == "ok:qwen/qwen3-14b:0.0"
    assert fake_client.chat.completions.calls == 3
    assert fake_client.chat.completions.last_kwargs is not None
    assert fake_client.chat.completions.last_kwargs["extra_body"] == {
        "context_length": 8192,
        "cache_prompt": False,
    }


def test_chat_passes_reasoning_option_when_configured(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    fake_client = FakeOpenAI()
    client = LLMClient(config_path=config_path, openai_client=fake_client, reasoning="off")

    client.chat([{"role": "user", "content": "hello"}])

    assert fake_client.chat.completions.last_kwargs is not None
    assert fake_client.chat.completions.last_kwargs["extra_body"] == {
        "context_length": 8192,
        "reasoning": "off",
        "cache_prompt": False,
    }


def test_chat_passes_configured_extra_body_without_mutating_messages(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    fake_client = FakeOpenAI()
    client = LLMClient(
        config_path=config_path,
        openai_client=fake_client,
        extra_body={"chat_template_kwargs": {"enable_thinking": False}},
    )
    messages = [{"role": "user", "content": "Heavy rain caused flooding."}]

    client.chat(messages)

    assert fake_client.chat.completions.last_kwargs is not None
    assert fake_client.chat.completions.last_kwargs["messages"] == messages
    assert fake_client.chat.completions.last_kwargs["extra_body"] == {
        "context_length": 8192,
        "cache_prompt": False,
        "chat_template_kwargs": {"enable_thinking": False},
    }


def test_lmstudio_extra_body_can_explicitly_override_prompt_cache_default(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    fake_client = FakeOpenAI()
    client = LLMClient(
        config_path=config_path,
        openai_client=fake_client,
        extra_body={"cache_prompt": True},
    )

    client.chat([{"role": "user", "content": "hello"}])

    assert fake_client.chat.completions.last_kwargs is not None
    assert fake_client.chat.completions.last_kwargs["extra_body"] == {
        "context_length": 8192,
        "cache_prompt": True,
    }


def test_chat_omits_lmstudio_context_length_for_deepseek_and_passes_reasoning_options(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    fake_client = FakeOpenAI()
    client = LLMClient(
        config_path=config_path,
        provider="deepseek",
        base_url="https://api.deepseek.com",
        model="deepseek-v4-pro",
        api_key="deepseek-token",
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
        openai_client=fake_client,
    )

    client.chat([{"role": "user", "content": "extract JSON"}])

    assert fake_client.chat.completions.last_kwargs is not None
    assert fake_client.chat.completions.last_kwargs["model"] == "deepseek-v4-pro"
    assert fake_client.chat.completions.last_kwargs["extra_body"] == {
        "thinking": {"type": "enabled"},
        "reasoning_effort": "high",
    }


def test_chat_supports_generic_openai_compatible_server_without_vendor_fields(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    fake_client = FakeOpenAI()
    client = LLMClient(
        config_path=config_path,
        provider="openai_compatible",
        base_url="http://127.0.0.1:8000/v1",
        model="qwen3-8b-cnc-qlora-best",
        api_key="llamafactory-local",
        openai_client=fake_client,
    )

    client.chat([{"role": "user", "content": "extract JSON"}])

    assert fake_client.chat.completions.last_kwargs is not None
    assert fake_client.chat.completions.last_kwargs["model"] == "qwen3-8b-cnc-qlora-best"
    assert fake_client.chat.completions.last_kwargs["extra_body"] == {}


def test_chat_reports_reasoning_only_response_as_empty_content(tmp_path: Path) -> None:
    config_path = tmp_path / "llm.yaml"
    write_config(config_path)
    fake_client = FakeOpenAI(
        response_message=SimpleNamespace(content="", reasoning_content="Thinking Process: ..."),
        finish_reason="length",
    )
    client = LLMClient(config_path=config_path, openai_client=fake_client, retry_times=3)

    with pytest.raises(RuntimeError, match="reasoning_content"):
        client.chat([{"role": "user", "content": "extract JSON"}])
    assert fake_client.chat.completions.calls == 1
