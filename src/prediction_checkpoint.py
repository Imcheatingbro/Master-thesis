"""Checkpoint management for long-running prediction jobs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable


class PredictionCheckpointError(RuntimeError):
    pass


class PredictionCheckpoint:

    FORMAT_VERSION = 1

    def __init__(
        self,
        *,
        directory: Path | str,
        run_name: str,
        signature_payload: dict[str, Any],
        sample_ids: Iterable[Any],
    ) -> None:
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.run_name = str(run_name)
        self.signature_payload = _json_roundtrip(signature_payload)
        self.signature = _stable_digest(self.signature_payload)
        self.sample_id_keys = [_sample_id_key(sample_id) for sample_id in sample_ids]
        if len(set(self.sample_id_keys)) != len(self.sample_id_keys):
            raise PredictionCheckpointError("当前评测样本包含重复 id，无法安全断点续跑。")
        self.expected_id_keys = set(self.sample_id_keys)

        slug = _safe_filename_part(self.run_name)
        stem = f"{slug}_{self.signature[:16]}"
        self.predictions_path = self.directory / f"{stem}.jsonl"
        self.manifest_path = self.directory / f"{stem}.manifest.json"
        self._predictions: dict[str, dict[str, Any]] = {}

        self._load_or_create_manifest()
        self._load_predictions()

    def __len__(self) -> int:
        return len(self._predictions)

    @property
    def remaining_count(self) -> int:
        return len(self.sample_id_keys) - len(self._predictions)

    def get(self, sample_id: Any) -> dict[str, Any] | None:
        prediction = self._predictions.get(_sample_id_key(sample_id))
        return _json_roundtrip(prediction) if prediction is not None else None

    def append(self, sample_id: Any, prediction: dict[str, Any]) -> None:
        key = _sample_id_key(sample_id)
        if key not in self.expected_id_keys:
            raise PredictionCheckpointError(f"Checkpoint 收到未知 sample id：{sample_id!r}")
        normalized_prediction = _json_roundtrip(prediction)
        existing = self._predictions.get(key)
        if existing is not None:
            if existing != normalized_prediction:
                raise PredictionCheckpointError(
                    f"Sample id {sample_id!r} 已存在不同预测，拒绝覆盖 checkpoint。"
                )
            return

        row = {"sample_id": sample_id, "prediction": normalized_prediction}
        serialized = json.dumps(row, ensure_ascii=False, sort_keys=True)
        with self.predictions_path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(serialized + "\n")
            handle.flush()
        self._predictions[key] = normalized_prediction
        self.mark_status("in_progress")

    def mark_status(
        self,
        status: str,
        *,
        error: str | None = None,
        report_path: str | None = None,
    ) -> None:
        manifest = self._manifest_payload(status=status)
        if error:
            manifest["error"] = str(error)
        if report_path:
            manifest["report_path"] = str(report_path)
        _write_json_atomic(self.manifest_path, manifest)

    def _load_or_create_manifest(self) -> None:
        if not self.manifest_path.exists():
            _write_json_atomic(self.manifest_path, self._manifest_payload(status="created"))
            return

        try:
            manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise PredictionCheckpointError(
                f"无法读取 checkpoint manifest：{self.manifest_path}"
            ) from exc
        if manifest.get("format_version") != self.FORMAT_VERSION:
            raise PredictionCheckpointError("Checkpoint format_version 与当前代码不一致。")
        if manifest.get("signature") != self.signature:
            raise PredictionCheckpointError("Checkpoint 运行签名与当前配置不一致。")
        if int(manifest.get("sample_count", -1)) != len(self.sample_id_keys):
            raise PredictionCheckpointError("Checkpoint 样本数量与当前数据不一致。")

    def _load_predictions(self) -> None:
        if not self.predictions_path.exists():
            return
        try:
            lines = self.predictions_path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            raise PredictionCheckpointError(
                f"无法读取 checkpoint predictions：{self.predictions_path}"
            ) from exc
        for line_number, line in enumerate(lines, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                key = _sample_id_key(row["sample_id"])
                prediction = _json_roundtrip(row["prediction"])
            except (KeyError, TypeError, json.JSONDecodeError) as exc:
                raise PredictionCheckpointError(
                    f"Checkpoint 第 {line_number} 行损坏：{self.predictions_path}"
                ) from exc
            if key not in self.expected_id_keys:
                raise PredictionCheckpointError(
                    f"Checkpoint 第 {line_number} 行包含当前数据不存在的 sample id。"
                )
            if key in self._predictions:
                raise PredictionCheckpointError(
                    f"Checkpoint 第 {line_number} 行包含重复 sample id。"
                )
            self._predictions[key] = prediction
        self.mark_status("ready_to_resume" if self._predictions else "created")

    def _manifest_payload(self, *, status: str) -> dict[str, Any]:
        return {
            "format_version": self.FORMAT_VERSION,
            "run_name": self.run_name,
            "signature": self.signature,
            "signature_payload": self.signature_payload,
            "sample_count": len(self.sample_id_keys),
            "completed_samples": len(self._predictions),
            "remaining_samples": self.remaining_count,
            "status": str(status),
            "predictions_path": str(self.predictions_path),
        }


def _stable_digest(payload: Any) -> str:
    serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def _sample_id_key(sample_id: Any) -> str:
    return json.dumps(sample_id, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _safe_filename_part(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value)).strip("-._")
    return normalized or "run"


def _json_roundtrip(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False, sort_keys=True))


def _write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    temporary_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary_path.replace(path)
