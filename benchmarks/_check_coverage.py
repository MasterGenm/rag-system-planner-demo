"""Check benchmark scenario coverage for the RAG planner skill."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
SCENARIO_DIR = ROOT / "scenarios"
INDEX_PATH = SCENARIO_DIR / "_index.csv"

MODE_MINIMUMS = {
    "greenfield": 4,
    "diagnosis": 8,
    "comparison": 3,
}

DIAGNOSIS_FAMILY_MINIMUMS = {
    "retrieval": 2,
    "ranking": 2,
    "generation": 2,
    "observability": 2,
}

NEXT_ACTION_CLASSES = {
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


def load_scenarios() -> list[dict]:
    scenarios = []
    for path in sorted(SCENARIO_DIR.glob("BCH-*.json")):
        with path.open(encoding="utf-8") as handle:
            payload = json.load(handle)
        payload["_path"] = path
        scenarios.append(payload)
    return scenarios


def load_index() -> dict[str, dict[str, str]]:
    with INDEX_PATH.open(encoding="utf-8", newline="") as handle:
        return {row["id"]: row for row in csv.DictReader(handle)}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    scenarios = load_scenarios()
    index_rows = load_index()

    require(15 <= len(scenarios) <= 20, f"expected 15-20 scenarios, found {len(scenarios)}", errors)

    mode_counts = Counter()
    diagnosis_family_counts = Counter()
    has_escalation_guardrail = False
    has_observed_and_unknown = False

    seen_ids: set[str] = set()
    for scenario in scenarios:
        case_id = scenario.get("case_id")
        mode = scenario.get("mode")
        expected = scenario.get("expected", {})
        family = expected.get("failure_family")
        next_action = expected.get("next_action_class")

        require(isinstance(case_id, str), f"{scenario['_path'].name}: case_id must be a string", errors)
        require(case_id not in seen_ids, f"{case_id}: duplicate case_id", errors)
        seen_ids.add(case_id)

        require(mode in MODE_MINIMUMS, f"{case_id}: invalid mode {mode!r}", errors)
        require(expected.get("mode") == mode, f"{case_id}: expected.mode must match mode", errors)
        require(isinstance(scenario.get("input"), dict), f"{case_id}: input must be an object", errors)
        require(next_action in NEXT_ACTION_CLASSES, f"{case_id}: invalid next_action_class {next_action!r}", errors)

        index_row = index_rows.get(case_id)
        require(index_row is not None, f"{case_id}: missing from _index.csv", errors)
        if index_row is not None:
            require(index_row["mode"] == mode, f"{case_id}: _index.csv mode mismatch", errors)
            require(index_row["failure_family"] == family, f"{case_id}: _index.csv family mismatch", errors)

        mode_counts[mode] += 1
        if mode == "diagnosis":
            diagnosis_family_counts[family] += 1

        must_avoid = expected.get("must_avoid", [])
        if "graph_rag" in must_avoid or "multi_agent_rewrite" in must_avoid:
            has_escalation_guardrail = True

        labels = set(expected.get("evidence_labels_must_appear", []))
        if {"observed", "unknown"}.issubset(labels):
            has_observed_and_unknown = True

    for mode, minimum in MODE_MINIMUMS.items():
        require(mode_counts[mode] >= minimum, f"mode {mode} has {mode_counts[mode]}, expected >= {minimum}", errors)

    for family, minimum in DIAGNOSIS_FAMILY_MINIMUMS.items():
        require(
            diagnosis_family_counts[family] >= minimum,
            f"diagnosis family {family} has {diagnosis_family_counts[family]}, expected >= {minimum}",
            errors,
        )

    require(has_escalation_guardrail, "no scenario checks premature graph or multi-agent escalation", errors)
    require(has_observed_and_unknown, "no scenario requires both observed and unknown labels", errors)

    print("Mode coverage")
    for mode in MODE_MINIMUMS:
        print(f"- {mode}: {mode_counts[mode]}")

    print("Diagnosis family coverage")
    for family in DIAGNOSIS_FAMILY_MINIMUMS:
        print(f"- {family}: {diagnosis_family_counts[family]}")

    if errors:
        print("Coverage check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
