"""Convert CNC fine-tuning targets to the triples-only output schema."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import logging
import shutil
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = PROJECT_ROOT / "Data" / "CNC_sft_gemma_v2"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "Data" / "CNC_sft_gemma_v3_triples_only"
DEFAULT_PROMPT_PATH = PROJECT_ROOT / "prompts" / "cnc_gemma_v4_triples_only.txt"
SPLITS = ("train", "validation", "test")


def main(args: argparse.Namespace) -> None:
    audit = prepare_triples_only_data(args.source_dir, args.output_dir, args.prompt_path)
    LOGGER.info("triples-only 数据已生成：%s", args.output_dir.resolve())
    LOGGER.info("数据分布：%s", audit["distribution"])


def prepare_triples_only_data(
    source_dir: Path,
    output_dir: Path,
    prompt_path: Path,
) -> dict[str, Any]:
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    prompt_path = prompt_path.resolve()
    if output_dir.exists():
        raise FileExistsError(f"拒绝覆盖已有数据：{output_dir}")
    if not prompt_path.is_file():
        raise FileNotFoundError(prompt_path)

    prompt = prompt_path.read_text(encoding="utf-8").strip()
    source_rows: dict[str, list[dict[str, Any]]] = {}
    output_rows: dict[str, list[dict[str, Any]]] = {}
    for split in SPLITS:
        source_path = source_dir / f"{split}.jsonl"
        if not source_path.is_file():
            raise FileNotFoundError(source_path)
        source_rows[split] = _read_jsonl(source_path)
        output_rows[split] = [_convert_row(row, prompt) for row in source_rows[split]]

    checks = _audit_rows(source_rows, output_rows, prompt)
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise RuntimeError(f"triples-only 数据审计失败：{', '.join(failed)}")

    output_dir.mkdir(parents=True)
    for split in SPLITS:
        _write_jsonl(output_dir / f"{split}.jsonl", output_rows[split])
    shutil.copyfile(source_dir / "dataset_info.json", output_dir / "dataset_info.json")

    audit = {
        "strategy": "仅替换 system Prompt，并从 assistant JSON 删除冗余 has_causal 字段",
        "source_dir": str(source_dir),
        "output_dir": str(output_dir),
        "prompt_path": str(prompt_path),
        "prompt_sha256": _sha256(prompt_path),
        "distribution": {
            split: {
                "samples": len(rows),
                "positive": sum(bool(row["relations"]) for row in rows),
                "negative": sum(not row["relations"] for row in rows),
                "relations": sum(len(row["relations"]) for row in rows),
            }
            for split, rows in output_rows.items()
        },
        "checks": checks,
        "source_hashes": {
            f"{split}.jsonl": _sha256(source_dir / f"{split}.jsonl")
            for split in SPLITS
        },
        "output_hashes": {
            f"{split}.jsonl": _sha256(output_dir / f"{split}.jsonl")
            for split in SPLITS
        },
    }
    _write_json(output_dir / "audit.json", audit)
    return audit


def _convert_row(row: dict[str, Any], prompt: str) -> dict[str, Any]:
    messages = row["messages"]
    if [message["role"] for message in messages] != ["system", "user", "assistant"]:
        raise ValueError(f"消息角色错误：id={row['id']}")
    source_target = json.loads(messages[-1]["content"])
    if bool(source_target["has_causal"]) != bool(source_target["triples"]):
        raise ValueError(f"源标签不一致：id={row['id']}")

    converted = copy.deepcopy(row)
    converted["messages"][0]["content"] = prompt
    converted["messages"][-1]["content"] = json.dumps(
        {"triples": source_target["triples"]},
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return converted


def _audit_rows(
    source_rows: dict[str, list[dict[str, Any]]],
    output_rows: dict[str, list[dict[str, Any]]],
    prompt: str,
) -> dict[str, bool]:
    ids = {split: {row["id"] for row in rows} for split, rows in source_rows.items()}
    documents = {
        split: {row["doc_id"] for row in rows}
        for split, rows in source_rows.items()
    }
    pairs = [
        (source, output)
        for split in SPLITS
        for source, output in zip(source_rows[split], output_rows[split])
    ]
    return {
        "split_sizes_preserved": all(
            len(source_rows[split]) == len(output_rows[split]) for split in SPLITS
        ),
        "row_order_and_ids_preserved": all(
            [row["id"] for row in source_rows[split]]
            == [row["id"] for row in output_rows[split]]
            for split in SPLITS
        ),
        "non_message_fields_preserved": all(
            {key: value for key, value in source.items() if key != "messages"}
            == {key: value for key, value in output.items() if key != "messages"}
            for source, output in pairs
        ),
        "user_messages_preserved": all(
            source["messages"][1] == output["messages"][1]
            for source, output in pairs
        ),
        "system_prompt_replaced": all(
            output["messages"][0] == {"role": "system", "content": prompt}
            for _source, output in pairs
        ),
        "assistant_is_triples_only": all(
            set(json.loads(output["messages"][-1]["content"])) == {"triples"}
            for _source, output in pairs
        ),
        "assistant_triples_preserved": all(
            json.loads(source["messages"][-1]["content"])["triples"]
            == json.loads(output["messages"][-1]["content"])["triples"]
            for source, output in pairs
        ),
        "split_ids_and_documents_disjoint": _pairwise_disjoint(ids)
        and _pairwise_disjoint(documents),
    }


def _pairwise_disjoint(values: dict[str, set[Any]]) -> bool:
    return not (
        values["train"] & values["validation"]
        or values["train"] & values["test"]
        or values["validation"] & values["test"]
    )


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="准备 CNC triples-only SFT 数据")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--prompt-path", type=Path, default=DEFAULT_PROMPT_PATH)
    main(parser.parse_args())
