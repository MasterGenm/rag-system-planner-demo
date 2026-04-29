"""Tests for deterministic benchmark scoring."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCORE_RUN_PATH = ROOT / "benchmarks" / "score_run.py"


@pytest.fixture()
def score_run_module(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("score_run_under_test", SCORE_RUN_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "RUNS_DIR", tmp_path / "runs")
    return module


def write_output(run_dir: Path, case_id: str, payload: dict) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / f"{case_id}.json").write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
        newline="\n",
    )


def test_self_test_run_scores_full_marks(score_run_module):
    records, average, log_path = score_run_module.run_score(ROOT / "benchmarks" / "_self_test_run")

    assert len(records) == 17
    assert average == 10.0
    assert all(record["total"] == 10 for record in records)
    assert log_path.exists()
    assert len(log_path.read_text(encoding="utf-8").strip().splitlines()) == 17


def test_threshold_failure_returns_nonzero(score_run_module, capsys):
    result = score_run_module.main(
        ["--runs", str(ROOT / "benchmarks" / "_self_test_run"), "--threshold", "11"]
    )
    captured = capsys.readouterr()

    assert result == 1
    assert "Average score: 10.00" in captured.out


def test_must_avoid_trigger_zeroes_escalation_dimension(score_run_module, tmp_path):
    run_dir = tmp_path / "bad_run"
    write_output(
        run_dir,
        "BCH-0005",
        {
            "mode": "diagnosis",
            "failure_family": "retrieval",
            "evidence_labels": ["observed", "unknown"],
            "next_action_class": "investigate_chunking",
            "recommendations": ["Upgrade to graph_rag now."],
        },
    )

    scenario = score_run_module.load_scenarios()["BCH-0005"]
    output = score_run_module.load_outputs(run_dir)["BCH-0005"]
    record = score_run_module.score_case("BCH-0005", scenario, output)

    assert record["scores"]["escalation_restraint"] == 0
    assert record["total"] == 8


def test_must_avoid_with_exception_allowed_and_declared_scores_two(score_run_module):
    scenario = score_run_module.load_scenarios()["BCH-0017"]
    output = {
        "mode": "comparison",
        "failure_family": "not_applicable",
        "evidence_labels": ["observed"],
        "next_action_class": "compare_vector_store",
        "recommendations": ["Use graph_rag only as a bounded_experiment."],
    }

    record = score_run_module.score_case("BCH-0017", scenario, output)

    assert record["scores"]["escalation_restraint"] == 2
    assert record["total"] == 10


def test_must_avoid_with_exception_allowed_but_undeclared_scores_zero(score_run_module):
    scenario = score_run_module.load_scenarios()["BCH-0017"]
    output = {
        "mode": "comparison",
        "failure_family": "not_applicable",
        "evidence_labels": ["observed"],
        "next_action_class": "compare_vector_store",
        "recommendations": ["Use graph_rag for regulated document intelligence."],
    }

    record = score_run_module.score_case("BCH-0017", scenario, output)

    assert record["scores"]["escalation_restraint"] == 0
    assert record["total"] == 8


def test_must_avoid_with_exception_disallowed_but_declared_scores_one(score_run_module):
    scenario = score_run_module.load_scenarios()["BCH-0005"]
    output = {
        "mode": "diagnosis",
        "failure_family": "retrieval",
        "evidence_labels": ["observed", "unknown"],
        "next_action_class": "investigate_chunking",
        "recommendations": ["Use graph_rag as a bounded_experiment."],
    }

    record = score_run_module.score_case("BCH-0005", scenario, output)

    assert record["scores"]["escalation_restraint"] == 1
    assert record["total"] == 9


def test_partial_evidence_labels_score_one(score_run_module):
    scenario = score_run_module.load_scenarios()["BCH-0005"]
    output = {
        "mode": "diagnosis",
        "failure_family": "retrieval",
        "evidence_labels": ["observed"],
        "next_action_class": "investigate_chunking",
    }

    record = score_run_module.score_case("BCH-0005", scenario, output)

    assert record["scores"]["evidence_labels"] == 1


def test_next_action_valid_but_different_family_scores_one(score_run_module):
    scenario = score_run_module.load_scenarios()["BCH-0005"]
    output = {
        "mode": "diagnosis",
        "failure_family": "retrieval",
        "evidence_labels": ["observed", "unknown"],
        "next_action_class": "tighten_answer_policy",
    }

    record = score_run_module.score_case("BCH-0005", scenario, output)

    assert record["scores"]["next_action_class"] == 1


def test_missing_output_scores_zero_for_required_dimensions(score_run_module):
    scenario = score_run_module.load_scenarios()["BCH-0005"]

    record = score_run_module.score_case("BCH-0005", scenario, None)

    assert record["scores"]["mode"] == 0
    assert record["scores"]["failure_family"] == 0
    assert record["scores"]["evidence_labels"] == 0
    assert record["scores"]["next_action_class"] == 0
