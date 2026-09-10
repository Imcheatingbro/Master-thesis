"""Serve a fine-tuned CNC model through a local OpenAI-compatible API."""

from __future__ import annotations

import argparse
import logging
import threading
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger(__name__)
API_OWNER = "unsloth-cnc-single-pass-v1"
DECISION_PREFIX = '{"has_causal":'


@dataclass
class _Runtime:

    model: Any
    tokenizer: Any
    torch: Any
    model_id: str
    lock: threading.Lock


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="启动 CNC Unsloth 推理 API")
    parser.add_argument("--model-path", type=Path, required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--max-seq-length", type=int, default=2048)
    parser.add_argument(
        "--chat-template",
        choices=("gemma-4", "qwen3"),
        default="gemma-4",
        help="选择与训练完全一致的 chat template。",
    )
    parser.add_argument(
        "--allow-base",
        action="store_true",
        help="允许 model-path 指向无 adapter 的本地 base，用于同路径 baseline。",
    )
    parser.add_argument(
        "--load-in-4bit",
        action="store_true",
        help="以 bitsandbytes 4-bit 加载 base model；12B QLoRA 推理必须启用。",
    )
    return parser.parse_args()


def _load_runtime(
    model_path: Path,
    model_id: str,
    max_seq_length: int,
    load_in_4bit: bool = False,
    chat_template: str = "gemma-4",
    allow_base: bool = False,
) -> _Runtime:
    if not allow_base and not (model_path / "adapter_model.safetensors").is_file():
        raise FileNotFoundError(f"未找到最终 LoRA：{model_path}")

    import unsloth
    import torch
    from unsloth import FastLanguageModel, FastModel
    from unsloth.chat_templates import get_chat_template

    if chat_template == "qwen3":
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=str(model_path),
            max_seq_length=max_seq_length,
            dtype=torch.bfloat16,
            load_in_4bit=load_in_4bit,
            full_finetuning=False,
            trust_remote_code=True,
            text_only=True,
        )
        if not getattr(tokenizer, "chat_template", None):
            raise RuntimeError("Qwen3 tokenizer 缺少原生 chat template。")
        FastLanguageModel.for_inference(model)
    else:
        model, tokenizer = FastModel.from_pretrained(
            model_name=str(model_path),
            max_seq_length=max_seq_length,
            dtype=torch.bfloat16,
            load_in_4bit=load_in_4bit,
            full_finetuning=False,
            trust_remote_code=False,
        )
        tokenizer = get_chat_template(tokenizer, chat_template="gemma-4")
        FastModel.for_inference(model)
    LOGGER.info("已加载模型：%s (%s, template=%s)", model_id, model_path, chat_template)
    return _Runtime(
        model=model,
        tokenizer=tokenizer,
        torch=torch,
        model_id=model_id,
        lock=threading.Lock(),
    )


def _text_tokenizer(tokenizer: Any) -> Any:
    return tokenizer.tokenizer if hasattr(tokenizer, "tokenizer") else tokenizer


def _eos_token_ids(tokenizer: Any) -> list[int]:
    text_tokenizer = _text_tokenizer(tokenizer)
    token_ids = {text_tokenizer.eos_token_id}
    turn_id = text_tokenizer.convert_tokens_to_ids("<turn|>")
    if isinstance(turn_id, int) and turn_id >= 0 and turn_id != text_tokenizer.unk_token_id:
        token_ids.add(turn_id)
    im_end_id = text_tokenizer.convert_tokens_to_ids("<|im_end|>")
    if isinstance(im_end_id, int) and im_end_id >= 0 and im_end_id != text_tokenizer.unk_token_id:
        token_ids.add(im_end_id)
    return sorted(token_id for token_id in token_ids if isinstance(token_id, int))


def _prepare_model_inputs(
    tokenizer: Any,
    messages: list[dict[str, str]],
    assistant_prefix: str = "",
) -> Any:
    text_tokenizer = _text_tokenizer(tokenizer)
    rendered = text_tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=False,
        enable_thinking=False,
    )
    bos_token = getattr(text_tokenizer, "bos_token", None)
    if isinstance(bos_token, str) and bos_token:
        rendered = rendered.removeprefix(bos_token)
    rendered += assistant_prefix
    if hasattr(tokenizer, "tokenizer"):
        return tokenizer(text=[rendered], return_tensors="pt", add_special_tokens=False)
    return tokenizer([rendered], return_tensors="pt", add_special_tokens=False)


def _decision_margin(runtime: _Runtime, messages: list[dict[str, str]]) -> tuple[float, int]:
    inputs = _prepare_model_inputs(
        runtime.tokenizer,
        messages,
        assistant_prefix=DECISION_PREFIX,
    ).to("cuda")
    text_tokenizer = _text_tokenizer(runtime.tokenizer)
    true_ids = text_tokenizer("true", add_special_tokens=False)["input_ids"]
    false_ids = text_tokenizer("false", add_special_tokens=False)["input_ids"]
    if len(true_ids) != 1 or len(false_ids) != 1:
        raise RuntimeError(f"true/false 必须各为单 token：true={true_ids}, false={false_ids}")
    outputs = runtime.model(**inputs, logits_to_keep=1)
    logits = outputs.logits[0, -1]
    margin = float((logits[true_ids[0]] - logits[false_ids[0]]).float().item())
    return margin, int(inputs["input_ids"].shape[-1])


def _decode_generated_content(
    runtime: _Runtime,
    inputs: Any,
    assistant_prefix: str,
    max_tokens: int,
    temperature: float,
) -> tuple[str, int, str]:
    text_tokenizer = _text_tokenizer(runtime.tokenizer)
    prompt_tokens = int(inputs["input_ids"].shape[-1])
    generation_kwargs: dict[str, Any] = {
        "max_new_tokens": max_tokens,
        "do_sample": temperature > 0,
        "use_cache": True,
        "eos_token_id": _eos_token_ids(runtime.tokenizer),
        "pad_token_id": text_tokenizer.pad_token_id,
    }
    if temperature > 0:
        generation_kwargs["temperature"] = temperature
    output_ids = runtime.model.generate(**inputs, **generation_kwargs)
    continuation_ids = output_ids[0, prompt_tokens:]
    generated_tokens = int(continuation_ids.shape[-1])
    continuation = text_tokenizer.decode(continuation_ids, skip_special_tokens=True)
    continuation = continuation.split("<turn|>", maxsplit=1)[0].strip()
    content = assistant_prefix + continuation
    finish_reason = "length" if generated_tokens >= max_tokens else "stop"
    return content, generated_tokens, finish_reason


def _generate(
    runtime: _Runtime,
    messages: list[dict[str, str]],
    temperature: float,
    max_tokens: int,
) -> tuple[str, int, int, str]:
    with runtime.lock, runtime.torch.inference_mode():
        inputs = _prepare_model_inputs(runtime.tokenizer, messages).to("cuda")
        prompt_tokens = int(inputs["input_ids"].shape[-1])
        content, completion_tokens, finish_reason = _decode_generated_content(
            runtime,
            inputs,
            assistant_prefix="",
            max_tokens=max_tokens,
            temperature=temperature,
        )
    return content, prompt_tokens, completion_tokens, finish_reason


def _create_app(runtime: _Runtime) -> Any:
    from fastapi import Body, FastAPI, HTTPException

    app = FastAPI(title="CNC Unsloth API")

    def _request_messages(payload: dict[str, Any]) -> list[dict[str, str]]:
        if payload.get("model") != runtime.model_id:
            raise HTTPException(status_code=400, detail="请求的 model 与已加载模型不一致")
        raw_messages = payload.get("messages")
        if not isinstance(raw_messages, list) or not raw_messages:
            raise HTTPException(status_code=422, detail="messages 必须是非空列表")
        messages: list[dict[str, str]] = []
        for message in raw_messages:
            if not isinstance(message, dict) or not isinstance(message.get("content"), str):
                raise HTTPException(status_code=422, detail="当前服务只接受字符串 content")
            messages.append({"role": str(message.get("role", "user")), "content": message["content"]})
        return messages

    @app.get("/v1/models")
    def list_models() -> dict[str, Any]:
        return {
            "object": "list",
            "data": [{"id": runtime.model_id, "object": "model", "owned_by": API_OWNER}],
        }

    @app.post("/v1/chat/completions")
    def create_chat_completion(payload: dict[str, Any] = Body(...)) -> dict[str, Any]:
        messages = _request_messages(payload)

        temperature = float(payload.get("temperature", 0.0))
        max_tokens = int(payload.get("max_tokens", 512))
        if max_tokens <= 0:
            raise HTTPException(status_code=422, detail="max_tokens 必须大于 0")
        try:
            content, prompt_tokens, completion_tokens, finish_reason = _generate(
                runtime,
                messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        except Exception as exc:
            LOGGER.exception("生成失败")
            raise HTTPException(
                status_code=500,
                detail=f"{type(exc).__name__}: {exc}",
            ) from exc
        LOGGER.info("生成完成：prompt=%s completion=%s", prompt_tokens, completion_tokens)
        return {
            "id": f"chatcmpl-{uuid.uuid4().hex}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": runtime.model_id,
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": content},
                    "finish_reason": finish_reason,
                }
            ],
            "usage": {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens,
            },
        }

    @app.post("/v1/cnc/decision-score")
    def score_causal_decision(payload: dict[str, Any] = Body(...)) -> dict[str, Any]:
        messages = _request_messages(payload)
        try:
            with runtime.lock, runtime.torch.inference_mode():
                margin, prompt_tokens = _decision_margin(runtime, messages)
        except Exception as exc:
            LOGGER.exception("决策评分失败")
            raise HTTPException(
                status_code=500,
                detail=f"{type(exc).__name__}: {exc}",
            ) from exc
        return {
            "model": runtime.model_id,
            "margin": margin,
            "prompt_tokens": prompt_tokens,
        }

    return app


def main() -> None:
    args = _parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    runtime = _load_runtime(
        args.model_path.resolve(),
        args.model_id,
        args.max_seq_length,
        load_in_4bit=args.load_in_4bit,
        chat_template=args.chat_template,
        allow_base=args.allow_base,
    )
    app = _create_app(runtime)

    import uvicorn

    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
