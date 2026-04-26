"""Deterministically score benchmark run outputs."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
import json
from pathlib import Path
import sys
from uuid import uuid4


ROOT = Path(__file__).resolve().parent
SCENARIO_DIR = ROOT / "scenarios"
RUNS_DIR = ROOT / "runs"

VALID_ACTIONS = {
    "investigate_chunking",
    "fix_metadata_filters",
    "inspect_ranking",
    "tighten_answer_policy",
    "add_observability",
    "build_eval_set",
    "compare_vector_store",
    "defer_agentic_upgrade",
    "define_metadata_baseline",
}

ACTION_FAMILIES = {
    "investigate_chunking": "retrieval_baseline",
    "fix_metadata_filters": "retrieval_baseline",
    "define_metadata_baseline": "retrieval_baseline",
    "inspect_ranking": "ranking",
    "tighten_answer_policy": "generation",
    "add_observability": "observability",
    "build_eval_set": "evaluation",
    "compare_vector_store": "comparison",
    "defer_agentic_upgrade": "comparison",
}

CLOSE_FAMILIES = {
    "retrieval": {"ranking"},
    "ranking": {"retrieval", "generation"},
    "generation": {"ranking"},
    "observability": set(),
    "not_applicable": set(),
}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return payload


def load_scenarios() -> dict[str, dict]:
    scenarios: dict[str, dict] = {}
    for path in sorted(SCENARIO_DIR.glob("BCH-*.json")):
        payload = load_json(path)
        scenarios[payload["case_id"]] = payload
    return scenarios


def load_outputs(run_dir: Path) -> dict[str, dict]:
    outputs: dict[str, dict] = {}
    for path in sorted(run_dir.glob("*.json")):
        try:
            outputs[path.stem] = load_json(path)
        except (json.JSONDecodeError, ValueError) as exc:
            outputs[path.stem] = {"_load_error": str(exc)}
    return outputs


def collect_strings(value) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        strings: list[str] = []
        for item in value:
            strings.extend(collect_strings(item))
        return strings
    if isinstance(value, dict):
        strings = []
        for key, item in value.items():
            strings.extend(collect_strings(key))
            strings.extend(collect_strings(item))
        return strings
    return []


def score_mode(output: dict, expected: dict) -> int:
    return 2 if output.get("mode") == expected.get("mode") else 0


def score_failure_family(output: dict, expected: dict) -> int:
    actual = output.get("failure_family")
    wanted = expected.get("failure_family")
    if actual == wanted:
        return 2
    if actual in CLOSE_FAMILIES.get(wanted, set()):
        return 1
    return 0


def score_evidence_labels(output: dict, expected: dict) -> int:
    required = set(expected.get("evidence_labels_must_appear", []))
    if not required:
        return 2

    actual = output.get("evidence_labels")
    if not isinstance(actual, list):
        return 0

    labels = {str(label) for label in actual}
    if not labels or labels == {"inferred"}:
        return 0
    if required.issubset(labels):
        return 2
    if required.intersection(labels):
        return 1
    return 0


def score_escalation_restraint(output: dict, expected: dict) -> int:
    blocked = [str(item).lower() for item in expected.get("must_avoid", [])]
    if not blocked:
        return 2

    output_text = "\n".join(collect_strings(output)).lower()
    return 0 if any(item in output_text for item in blocked) else 2


def score_next_action(output: dict, expected: dict) -> int:
    actual = output.get("next_action_class")
    wanted = expected.get("next_action_class")
    if actual not in VALID_ACTIONS:
        return 0
    if ACTION_FAMILIES.get(actual) == ACTION_FAMILIES.get(wanted):
        return 2
    return 1


def score_case(case_id: str, scenario: dict, output: dict | None) -> dict:
    expected = scenario["expected"]
    output = output or {}

    scores = {
        "mode": score_mode(output, expected),
        "failure_family": score_failure_family(output, expected),
        "evidence_labels": score_evidence_labels(output, expected),
        "escalation_restraint": score_escalation_restraint(output, expected),
        "next_action_class": score_next_action(output, expected),
    }
    total = sum(scores.values())
    return {
        "case_id": case_id,
        "scores": scores,
        "total": total,
        "missing_output": output == {},
        "load_error": output.get("_load_error") if output else None,
    }


def write_run_log(records: list[dict], average: float, run_dir: Path) -> Path:
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    path = RUNS_DIR / f"{timestamp}-{uuid4().hex[:8]}.jsonl"
    payloads = []
    for record in records:
        payloads.append(
            {
                "timestamp": timestamp,
                "run_dir": str(run_dir),
                "case_id": record["case_id"],
                "scores": record["scores"],
                "total": record["total"],
                "average": average,
            }
        )
    path.write_text(
        "\n".join(json.dumps(payload, sort_keys=True) for payload in payloads) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return path


def run_score(run_dir: Path) -> tuple[list[dict], float, Path]:
    scenarios = load_scenarios()
    outputs = load_outputs(run_dir)
    records = [
        score_case(case_id, scenario, outputs.get(case_id))
        for case_id, scenario in sorted(scenarios.items())
    ]
    average = sum(record["total"] for record in records) / len(records) if records else 0.0
    log_path = write_run_log(records, average, run_dir)
    return records, average, log_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score RAG planner benchmark outputs.")
    parser.add_argument("--runs", required=True, help="Directory containing <case_id>.json model outputs.")
    parser.add_argument("--threshold", type=float, default=7.0, help="Minimum average score.")
    args = parser.parse_args(argv)

    run_dir = Path(args.runs)
    if not run_dir.exists() or not run_dir.is_dir():
        raise SystemExit(f"Run directory not found: {run_dir}")

    records, average, log_path = run_score(run_dir)
    for record in records:
        scores = record["scores"]
        details = " ".join(f"{name}={value}" for name, value in scores.items())
        print(f"{record['case_id']}: total={record['total']} {details}")
        if record["load_error"]:
            print(f"{record['case_id']}: load_error={record['load_error']}", file=sys.stderr)

    print(f"Average score: {average:.2f}")
    print(f"Run log: {log_path}")

    return 0 if average >= args.threshold else 1


if __name__ == "__main__":
    raise SystemExit(main())
