# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog 1.1.0,
and this project adheres to Semantic Versioning.

## [Unreleased]

## [0.1.0] - 2026-04-27

### Added

- (T1) Renderer regression suite: pytest coverage for `render_rag_plan.py` and `render_rag_diagnostic.py`, fixtures, and CLI behaviors.
- (T2) Input JSON Schemas (`plan_input.schema.json`, `diagnostic_input.schema.json`) with draft 2020-12 validation tests.
- (T3) Benchmark scenario seed set: 16 cases covering greenfield/diagnosis/comparison modes and the four diagnosis failure families, plus coverage checker.
- (T4) Deterministic scorer with 5 dimensions and rubric (`benchmarks/rubric.md`, `benchmarks/score_run.py`), self-test fixture run, and tests.
- (T5) Thin CLI runner `cli.rag_planner` with `plan` / `diagnose` / `validate` subcommands, schema validation, JSON run log, and CLI tests; registered as `rag-planner` console script via `pyproject.toml`.
- (T6) Telemetry contract document with 10-field minimum set and failure-family mapping (`docs/telemetry-contract.md`).
- (T7) Run log JSONL contract document aligned with the implemented record fields (`docs/run-log-format.md`).
- (T8) Minimal GitHub Actions CI workflow running tests, schema validation, coverage check, and scorer self-test.
- (T9) Three retrospective application cases (CASE-0001 Court Logic, CASE-0002 Stackademic RAG Done Right, CASE-0003 Lettria GraphRAG) and case index, with v0.1 boundary statement.
- (T10) Freshness metadata on long-lived documents, freshness policy (`docs/freshness-policy.md`), and stdlib-only `scripts/check_freshness.py` with tests.

### Changed

- (T1) `render_rag_plan.py` and `render_rag_diagnostic.py`: added `newline="\n"` to `Path.write_text` for cross-platform output consistency. No section ordering or rendering contract change.
- (T5) `pyproject.toml`: added minimal `[project]` metadata and `[project.scripts]` entry for the `rag-planner` console script.

### Notes

- All v0.1 retrospective cases are `case_type: retrospective_application`. `production_use` cases are deferred to v0.2.
- The `<owner>` placeholder in freshness frontmatter must be replaced with the GitHub handle before push (see release checklist).
- CI workflow exists locally; remote GitHub Actions verification is performed by the maintainer at push time.
