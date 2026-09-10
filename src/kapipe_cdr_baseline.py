"""Adapter for evaluating the KAPipe CDR baseline."""

from __future__ import annotations

import json
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence


logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KAPIPE_SOURCE_DIR = (
    PROJECT_ROOT / "reference code from related work" / "kapipe-main" / "kapipe-main"
)
DEFAULT_KAPIPE_MODEL_ROOT = PROJECT_ROOT / "reference code from related work" / "kapipe-model"

_TOKEN_RE = re.compile(r"\w+|[^\w\s]", flags=re.UNICODE)


@dataclass(frozen=True)
class KapipeSnapshotPaths:

    ner: Path
    ed_retrieval: Path
    ed_reranking: Path
    docre: Path

    def as_dict(self) -> dict[str, Path]:

        return {
            "ner": self.ner,
            "ed_retrieval": self.ed_retrieval,
            "ed_reranking": self.ed_reranking,
            "docre": self.docre,
        }


REQUIRED_SNAPSHOT_FILES: dict[str, tuple[str, ...]] = {
    "ner": ("component_config.json", "entity_types.vocab.txt", "model.pt"),
    "ed_retrieval": (
        "component_config.json",
        "entity_dict.json",
        "entity_vectors.npy",
        "model.pt",
    ),
    "ed_reranking": ("component_config.json", "entity_dict.json", "model.pt"),
    "docre": ("component_config.json", "relations.vocab.txt", "model.pt"),
}


def default_snapshot_paths(model_root: Path | str = DEFAULT_KAPIPE_MODEL_ROOT) -> KapipeSnapshotPaths:

    root = Path(model_root)
    return KapipeSnapshotPaths(
        ner=(
            root
            / "ner"
            / "biaffine_ner"
            / "biaffine_ner_model_scibertuncased_cdr"
            / "raiden163a"
        ),
        ed_retrieval=(
            root
            / "ed_retrieval"
            / "blink_bi_encoder"
            / "blink_bi_encoder_model_scibertuncased_cdr"
            / "raiden512a"
        ),
        ed_reranking=(
            root
            / "ed_reranking"
            / "blink_cross_encoder"
            / "blink_cross_encoder_model_scibertuncased_cdr"
            / "raiden907a"
        ),
        docre=(
            root
            / "docre"
            / "atlop"
            / "atlop_model_scibertcased_cdr_overlap"
            / "raiden158a"
        ),
    )


def validate_snapshot_paths(snapshot_paths: KapipeSnapshotPaths) -> dict[str, list[Path]]:

    missing: dict[str, list[Path]] = {}
    for component_name, directory in snapshot_paths.as_dict().items():
        component_missing: list[Path] = []
        if not directory.is_dir():
            component_missing.append(directory)
        for filename in REQUIRED_SNAPSHOT_FILES[component_name]:
            path = directory / filename
            if not path.is_file():
                component_missing.append(path)
        if component_missing:
            missing[component_name] = component_missing
    return missing


def format_missing_snapshot_paths(missing: Mapping[str, Sequence[Path]]) -> str:

    lines = ["KAPipe CDR snapshot 文件不完整："]
    for component_name, paths in missing.items():
        lines.append(f"- {component_name}")
        lines.extend(f"  - {path}" for path in paths)
    return "\n".join(lines)


def ensure_kapipe_on_path(kapipe_source_dir: Path | str = DEFAULT_KAPIPE_SOURCE_DIR) -> Path:

    source_dir = Path(kapipe_source_dir).resolve()
    if not source_dir.is_dir():
        raise FileNotFoundError(f"找不到 KAPipe 源码目录：{source_dir}")
    source_text = str(source_dir)
    if source_text not in sys.path:
        sys.path.insert(0, source_text)
    return source_dir


def tokenize_for_kapipe(text: str) -> str:

    return " ".join(_TOKEN_RE.findall(text))


def sample_to_kapipe_document(sample: Mapping[str, Any]) -> dict[str, Any]:

    if "id" not in sample:
        raise ValueError("样本缺少 id 字段")
    text = str(sample.get("text", "")).strip()
    if not text:
        raise ValueError(f"样本 {sample.get('id')} 缺少 text 字段")
    return {
        "doc_key": str(sample["id"]),
        "sentences": [tokenize_for_kapipe(text)],
    }


def prediction_from_kapipe_document(
    document: Mapping[str, Any],
    sample_id: Any | None = None,
    relation_label: str = "CID",
) -> dict[str, Any]:

    triples: list[dict[str, Any]] = []
    for relation in _as_list(document.get("relations")):
        if not isinstance(relation, Mapping):
            continue
        if str(relation.get("relation", "")) != relation_label:
            continue
        cause_span = _entity_span(document=document, entity_index=relation.get("arg1"))
        effect_span = _entity_span(document=document, entity_index=relation.get("arg2"))
        if not cause_span or not effect_span:
            logger.warning("跳过无法映射 span 的 KAPipe relation：%s", relation)
            continue
        triples.append(
            {
                "cause": {"span": cause_span},
                "effect": {"span": effect_span},
                "source_relation": relation_label,
            }
        )

    return {
        "id": document.get("doc_key") if sample_id is None else sample_id,
        "has_causal": bool(triples),
        "triples": triples,
        "source": "kapipe_cdr",
    }


def build_kapipe_cdr_pipeline(
    kapipe_source_dir: Path | str = DEFAULT_KAPIPE_SOURCE_DIR,
    snapshot_paths: KapipeSnapshotPaths | None = None,
    device: str = "cpu",
    use_cross_encoder: bool = True,
) -> Any:

    paths = snapshot_paths or default_snapshot_paths()
    missing = validate_snapshot_paths(paths)
    if missing:
        raise FileNotFoundError(format_missing_snapshot_paths(missing))

    ensure_kapipe_on_path(kapipe_source_dir)
    try:
        from kapipe.docre import ATLOP
        from kapipe.ed_retrieval import BlinkBiEncoder
        from kapipe.ed_reranking import BlinkCrossEncoder
        from kapipe.ed_reranking import IdenticalEntityReranker
        from kapipe.ner import BiaffineNER
        from kapipe.passage_retrieval.anns import ApproximateNearestNeighborSearch
        from kapipe.pipelines import TripleExtractionPipeline
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            f"无法导入 KAPipe 依赖：{exc.name}。"
            "请先在 Master_thesis 环境安装缺失依赖后重试。"
        ) from exc

    ner = BiaffineNER.from_snapshot(snapshot_path=str(paths.ner), device=device)
    ed_retrieval = BlinkBiEncoder.from_snapshot(
        snapshot_path=str(paths.ed_retrieval),
        device=device,
    )
    ed_retrieval.anns = ApproximateNearestNeighborSearch(gpu_id=-1)
    ed_retrieval.make_index(use_precomputed_entity_vectors=True)

    if use_cross_encoder:
        ed_reranking = BlinkCrossEncoder.from_snapshot(
            snapshot_path=str(paths.ed_reranking),
            device=device,
        )
    else:
        ed_reranking = IdenticalEntityReranker()

    docre = ATLOP.from_snapshot(snapshot_path=str(paths.docre), device=device)
    return TripleExtractionPipeline(
        ner=ner,
        ed_retrieval=ed_retrieval,
        ed_reranking=ed_reranking,
        docre=docre,
    )


def run_kapipe_cdr_baseline(
    samples: Sequence[Mapping[str, Any]],
    pipeline: Any,
    dataset: str,
    retrieval_size: int = 10,
    primary_metric: str | None = None,
) -> dict[str, Any]:

    from src.evaluator import Evaluator

    evaluator = Evaluator(dataset=dataset, primary_metric=primary_metric)
    predictions: list[dict[str, Any]] = []
    kapipe_documents: list[dict[str, Any]] = []

    for sample in samples:
        document = sample_to_kapipe_document(sample)
        output_document = pipeline.extract_triples(
            document=document,
            retrieval_size=retrieval_size,
        )
        prediction = prediction_from_kapipe_document(
            document=output_document,
            sample_id=sample.get("id"),
        )
        evaluator.update(prediction=prediction, gold=dict(sample))
        predictions.append(prediction)
        kapipe_documents.append(output_document)

    return {
        "dataset": dataset,
        "n_samples": len(samples),
        "retrieval_size": retrieval_size,
        "predictions": predictions,
        "kapipe_documents": kapipe_documents,
        "report": evaluator.report(),
        "formatted_report": evaluator.format_report(title=f"KAPipe CDR baseline: {dataset}"),
    }


def save_run_outputs(result: Mapping[str, Any], output_dir: Path | str, run_name: str) -> dict[str, Path]:

    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)

    paths = {
        "predictions": directory / f"{run_name}.predictions.jsonl",
        "kapipe_documents": directory / f"{run_name}.kapipe_documents.json",
        "report_json": directory / f"{run_name}.report.json",
        "report_md": directory / f"{run_name}.report.md",
    }
    _write_jsonl(paths["predictions"], _as_list(result.get("predictions")))
    _write_json(paths["kapipe_documents"], _as_list(result.get("kapipe_documents")))
    _write_json(paths["report_json"], result.get("report", {}))
    paths["report_md"].write_text(str(result.get("formatted_report", "")), encoding="utf-8")
    return paths


def _entity_span(document: Mapping[str, Any], entity_index: Any) -> str:
    if not isinstance(entity_index, int):
        return ""
    entities = _as_list(document.get("entities"))
    if entity_index < 0 or entity_index >= len(entities):
        return ""
    entity = entities[entity_index]
    if not isinstance(entity, Mapping):
        return ""

    mentions = _as_list(document.get("mentions"))
    for mention_index in _as_list(entity.get("mention_indices")):
        if not isinstance(mention_index, int):
            continue
        if mention_index < 0 or mention_index >= len(mentions):
            continue
        mention = mentions[mention_index]
        if isinstance(mention, Mapping):
            name = str(mention.get("name", "")).strip()
            if name:
                return name

    for name in _as_list(entity.get("mention_names")):
        text = str(name).strip()
        if text:
            return text
    return str(entity.get("entity_id", "")).strip()


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False))
            file.write("\n")
