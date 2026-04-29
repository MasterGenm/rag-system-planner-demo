# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog 1.1.0,
and this project adheres to Semantic Versioning.

## [Unreleased]

## [0.1.1] - 2026-04-29

### Changed

- (Skill) `skills/rag-system-planner/SKILL.md`: added "语境化升级豁免" subsection with 5 trigger conditions and bounded-experiment boundary, derived from CASE-0003 and CASE-0001 findings recorded in v0.1.0.
- (Skill) `cursor/rules/rag-system-planner.mdc`: added a single-line pointer to the SKILL.md exception clause.
- (benchmarks) `benchmarks/score_run.py`: `score_escalation_restraint` now recognizes `expected.allow_escalation_exception` and contextual exception declarations (`bounded_experiment` / `escalation_exception_declared` / `语境化延后`).
- (benchmarks) `benchmarks/rubric.md`: documented the new exception-aware scoring branch.

### Added

- (benchmarks) `benchmarks/scenarios/BCH-0017.json`: regulated-domain comparison scenario where the 5 exception conditions are all satisfied; covers the new exception path.
- (benchmarks) `benchmarks/_self_test_run/BCH-0017.json`: full-mark self-test output for BCH-0017.
- (tests) `tests/test_score_run.py`: three new tests for exception-aware scoring branches.

### Notes

- v0.0 -> v0.1.0 -> v0.1.1 闭环：v0.1.0 通过 CASE-0003 与 CASE-0001 揭示的反例已在本版本吸收。CASE-0002 揭示的 "Skill 单一 failure_family 输出需要配套记录次要 failure signals" 留待 v0.2。
- v0.1.0 的 16 个 benchmark 场景与 self-test 输出未变更，向后兼容；新评分逻辑通过 `expected.allow_escalation_exception` 字段缺省值（False）保持 v0.1.0 结果不变。

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
