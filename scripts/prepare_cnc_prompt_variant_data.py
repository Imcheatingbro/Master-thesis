"""Copy CNC fine-tuning splits while replacing only the system prompt."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = PROJECT_ROOT / "Data" / "CNC_sft"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "Data" / "CNC_sft_gemma_v1"
DEFAULT_PROMPT_PATH = PROJECT_ROOT / "prompts" / "cnc_gemma_v1.txt"
SPLITS = ("train", "validation", "test")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Copy CNC SFT splits while replacing only the system prompt")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--system-prompt", type=Path, default=DEFAULT_PROMPT_PATH)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    audit = prepare_prompt_variant(args.source_dir, args.output_dir, args.system_prompt)
    print(f"Prompt-variant CNC SFT data created: {args.output_dir}")
    print(json.dumps(audit["distribution"], ensure_ascii=False, indent=2))
    print(f"Audit checks passed: {all(audit['checks'].values())}")


def prepare_prompt_variant(source_dir: Path, output_dir: Path, system_prompt_path: Path) -> dict[str, Any]:
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    system_prompt_path = system_prompt_path.resolve()
    if output_dir == source_dir or source_dir in output_dir.parents and output_dir.name == source_dir.name:
        raise ValueError("Output directory must differ from the source directory")
    if output_dir.exists():
        raise FileExistsError(f"Output directory already exists: {output_dir}")
    if not system_prompt_path.is_file():
        raise FileNotFoundError(f"System prompt not found: {system_prompt_path}")

    prompt = system_prompt_path.read_text(encoding="utf-8").strip()
    source_rows: dict[str, list[dict[str, Any]]] = {}
    output_rows: dict[str, list[dict[str, Any]]] = {}
    for split in SPLITS:
        source_path = source_dir / f"{split}.jsonl"
        if not source_path.is_file():
            raise FileNotFoundError(f"Source split not found: {source_path}")
        rows = _read_jsonl(source_path)
        source_rows[split] = rows
        output_rows[split] = [_replace_system_prompt(row, prompt) for row in rows]

    checks = _audit_rows(source_rows, output_rows, prompt)
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise RuntimeError(f"Prompt-variant audit failed: {', '.join(failed)}")

    output_dir.mkdir(parents=True)
    for split in SPLITS:
        _write_jsonl(output_dir / f"{split}.jsonl", output_rows[split])
    shutil.copyfile(source_dir / "dataset_info.json", output_dir / "dataset_info.json")

    audit = {
        "strategy": "copy the existing audited CNC SFT splits and replace only messages[0].content",
        "source_dir": _portable_path(source_dir),
        "output_dir": _portable_path(output_dir),
        "system_prompt": {
            "path": _portable_path(system_prompt_path),
            "sha256": _sha256(system_prompt_path),
        },
        "distribution": {
            split: {
                "samples": len(rows),
                "positive": sum(bool(row.get("relations")) for row in rows),
                "negative": sum(not row.get("relations") for row in rows),
                "relations": sum(len(row.get("relations", [])) for row in rows),
            }
            for split, rows in source_rows.items()
        },
        "source_hashes": {f"{split}.jsonl": _sha256(source_dir / f"{split}.jsonl") for split in SPLITS},
        "output_hashes": {f"{split}.jsonl": _sha256(output_dir / f"{split}.jsonl") for split in SPLITS},
        "checks": checks,
        "notes": [
            "IDs, document assignments, text, labels, Gold spans, user messages, and assistant answers are unchanged.",
            "Only the system prompt differs from Data/CNC_sft.",
            "No validation or test example is added to training.",
        ],
    }
    (output_dir / "audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return audit


def _replace_system_prompt(row: dict[str, Any], prompt: str) -> dict[str, Any]:
    messages = row.get("messages")
    if not isinstance(messages, list) or len(messages) != 3:
        raise ValueError(f"Invalid messages for id={row.get('id')}")
    if [message.get("role") for message in messages] != ["system", "user", "assistant"]:
        raise ValueError(f"Unexpected message roles for id={row.get('id')}")
    copied = copy.deepcopy(row)
    copied["messages"][0]["content"] = prompt
    return copied


def _audit_rows(
    source_rows: dict[str, list[dict[str, Any]]],
    output_rows: dict[str, list[dict[str, Any]]],
    prompt: str,
) -> dict[str, bool]:
    ids = {split: {row["id"] for row in rows} for split, rows in source_rows.items()}
    docs = {split: {row["doc_id"] for row in rows} for split, rows in source_rows.items()}
    return {
        "split_sizes_preserved": all(len(source_rows[split]) == len(output_rows[split]) for split in SPLITS),
        "row_order_and_ids_preserved": all(
            [row["id"] for row in source_rows[split]] == [row["id"] for row in output_rows[split]]
            for split in SPLITS
        ),
        "non_message_fields_preserved": all(
            _without_messages(source) == _without_messages(output)
            for split in SPLITS
            for source, output in zip(source_rows[split], output_rows[split])
        ),
        "user_and_assistant_messages_preserved": all(
            source["messages"][1:] == output["messages"][1:]
            for split in SPLITS
            for source, output in zip(source_rows[split], output_rows[split])
        ),
        "system_prompt_replaced_exactly": all(
            output["messages"][0] == {"role": "system", "content": prompt}
            for split in SPLITS
            for output in output_rows[split]
        ),
        "ids_document_disjoint": _pairwise_disjoint(ids) and _pairwise_disjoint(docs),
    }


def _without_messages(row: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in row.items() if key != "messages"}


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


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _portable_path(path: Path) -> str:
    try:
        return path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


if __name__ == "__main__":
    main()
