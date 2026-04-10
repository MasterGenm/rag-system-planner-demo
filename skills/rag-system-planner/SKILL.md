---
name: rag-system-planner
description: Plan, diagnose, and steadily document retrieval-augmented generation systems with bounded complexity. Use for greenfield RAG design, retrieval failure diagnosis, evaluation planning, and maintaining durable RAG knowledge artifacts that capture recurring failure modes, stack decisions, and case notes over time.
---

# RAG System Planner

## Overview

Design new RAG systems and diagnose existing ones without defaulting to unnecessary complexity.
This skill is artifact-aware: when a conclusion is likely to matter again, preserve it in durable workspace artifacts instead of letting it disappear into chat history.

Keep the workflow framework-neutral. Prefer the simplest architecture that meets the user's goals. Escalate to hybrid, graph, or agentic patterns only when the failure mode or workflow clearly requires it.

Read `references/artifact-workflow.md` for the persistent workspace model.
Read `references/artifact-maintenance-contract.md` for the execution contract that governs maintenance work.
Read `references/artifact-operation-checklists.md` for the shortest deterministic runbook for each maintenance operation.
Read `references/reference-to-artifact-map.md` when deciding what kind of durable page to create.

## Two-Layer Model

This skill has two explicit layers:

- `planner`
  - make bounded-complexity judgments for greenfield design, diagnosis, and comparison
- `artifact-maintenance`
  - preserve and organize durable sources, evaluations, failure pages, case notes, and workspace structure

Planner is the reasoning layer.
Artifact-maintenance is the compounding knowledge layer that planner should consult and update when reusable findings appear.

## Workflow Selection

Choose the primary layer first:

- `planner`
  - the user wants design, diagnosis, prioritization, or a recommendation
- `artifact-maintenance`
  - the user wants ingest, workspace updates, linting, or durable knowledge cleanup

Within `planner`, choose one of these modes:

- `greenfield`
  - the user is designing a new RAG system or replacing most of an old one
- `diagnosis`
  - the user already has a RAG system and wants to improve recall, latency, groundedness, observability, or operational reliability
- `comparison`
  - the user primarily wants a bounded option comparison instead of a full design or diagnosis

If the request mixes layers, start in `planner`, then hand off to `artifact-maintenance` before finishing whenever the artifact update threshold is met.

## Planner First Step

Before reasoning from scratch:

1. Inspect the artifact workspace if one exists.
2. Read `index.md` and the most relevant hubs, evaluation pages, failure pages, or stack-decision pages.
3. In diagnosis mode, start from `wiki/failure-modes/triage-matrix.md` if the workspace has one.
4. Prefer targeted reading over blind full-document synthesis on large sources.

## Comparison Requests

If the user is primarily comparing options instead of asking for a full greenfield design or diagnosis, keep the reasoning inside the current workflow but return a lighter decision memo.

Use these sections:

1. Decision context
2. Options compared
3. Recommendation
4. Why this fits
5. Not chosen because
6. What would change the decision

## Artifact Update Threshold

Do not leave these only in chat.
Update durable artifacts when the answer contains any of the following:

- a reusable failure mode
- a recurring retrieval or architecture pattern
- a stack boundary or `not now` decision
- a reusable evaluation heuristic or hard-case rule
- a case note likely to matter again

## Intake

Use `references/intake-checklist.md` whenever requirements are missing or vague.

Collect only the details needed to make architecture decisions:

- data type and source
- scale and update frequency
- interaction pattern
- quality priorities
- cost and latency constraints
- deployment constraints
- existing stack and migration constraints
- evaluation and observability expectations

If the user cannot answer everything, proceed with a short assumptions section instead of blocking.

## Greenfield Workflow

1. Clarify the problem, users, data modalities, and constraints.
2. Perform the planner first step and workspace knowledge check.
3. Read `references/retrieval-design.md` to shape chunking, metadata, retrieval, reranking, and citation flow.
4. Read `references/multimodal-retrieval.md` if the corpus contains scans, screenshots, diagrams, tables, or other non-text evidence.
5. Read `references/embedding-choice.md` when embedding selection is not obvious.
6. Read `references/vector-db-choice.md` when storage, filtering, hybrid search, or operations tradeoffs matter.
7. Read `references/agent-framework-choice.md` only if the user wants agent behavior, tool use, or orchestration.
8. Read `references/eval-design.md` to define offline and online validation.
9. Read `references/observability-design.md` to define tracing, monitoring, and failure analysis.
10. Produce a solution package with assumptions, stack choices, architecture, evaluation, observability, rollout phases, and explicit `not now` decisions for complexity that is intentionally deferred.
11. If the artifact update threshold is met, hand off durable patterns or decisions to `artifact-maintenance`.
12. If a structured final document would help, run `scripts/render_rag_plan.py`.

## Diagnosis Workflow

1. Summarize symptoms in concrete terms: low recall, irrelevant retrieval, hallucinations, latency, cost, missing citations, or poor agent behavior.
2. Perform the planner first step and workspace knowledge check.
3. Read `references/diagnosis-playbook.md` first.
4. Start from `wiki/failure-modes/triage-matrix.md` when an artifact workspace exists and classify the symptom into the smallest plausible failure family.
5. Read the closest concrete failure page before broadening the scope.
6. Label each hypothesis as `observed`, `inferred`, or `unknown`. Do not let missing evidence silently turn into a root-cause claim.
7. Read `references/retrieval-design.md` if the issue may come from chunking, metadata, retrieval, reranking, or prompt assembly.
8. Read `references/multimodal-retrieval.md` if scans, screenshots, diagrams, tables, OCR quality, or modality routing may be involved.
9. Read `references/embedding-choice.md` if representation quality or multilingual behavior is suspect.
10. Read `references/vector-db-choice.md` if filtering, indexing, hybrid search, persistence, or scale appear to be the bottleneck.
11. Read `references/eval-design.md` to identify missing benchmarks and datasets.
12. Read `references/observability-design.md` to identify missing traces or runtime signals.
13. Produce a diagnostic report with likely causes, missing evidence, investigation order, and a prioritized remediation path. In `Recommended changes`, prefer a `now`, `next`, `later` ordering and favor reversible fixes before expensive redesign.
14. If the artifact update threshold is met, hand off reusable failure notes, investigation heuristics, or stack decisions to `artifact-maintenance`.
15. If a structured final document would help, run `scripts/render_rag_diagnostic.py`.

## Artifact-Maintenance Workflow

Use this layer when the primary goal is to maintain the persistent workspace or when planner has produced durable findings that must be preserved.

Before any maintenance operation:

1. Read `references/artifact-maintenance-contract.md`.
2. Follow the matching runbook in `references/artifact-operation-checklists.md`.
3. Keep the operation scoped. Maintenance preserves and organizes knowledge; it does not become an unconstrained redesign pass.

Use one of these operations:

- `ingest`
  - convert raw evidence into durable pages
- `query`
  - answer from the workspace and save durable results when appropriate
- `lint`
  - detect duplicates, unsupported claims, stale pages, weak navigation, and taxonomy drift
- `index`
  - refresh or repair workspace entry points and hubs

## Output Contract

### Greenfield Output

Return a complete solution package with these sections:

1. Problem summary
2. Assumptions and constraints
3. Recommended stack
4. Architecture and data flow
5. Retrieval design
6. Agent integration guidance
7. Evaluation plan
8. Observability plan
9. Risks and tradeoffs
10. Phased rollout plan
11. Durable artifact summary

Within `Recommended stack` and `Risks and tradeoffs`, explain why the chosen level of complexity fits and what is intentionally not being added yet.
Within `Retrieval design`, include modality routing and fallback behavior when the corpus is not text-only.
Within `Durable artifact summary`, say what durable pages were created or updated, or why the result stays chat-only.

### Comparison Output

Return a lighter decision memo with these sections:

1. Decision context
2. Options compared
3. Recommendation
4. Why this fits
5. Not chosen because
6. What would change the decision

Within `Recommendation`, keep the answer bounded and say what complexity is intentionally deferred.
Within `What would change the decision`, name the missing evidence, evaluation result, or workload change that would justify escalation.

### Diagnosis Output

Return a diagnostic report with these sections:

1. Symptom summary
2. Working hypotheses
3. Missing evidence
4. Investigation order
5. Recommended changes
6. Evaluation additions
7. Observability additions
8. Risks and expected impact
9. Durable artifact summary

Within `Working hypotheses`, label what is observed versus inferred.
Within `Recommended changes`, order actions as `now`, `next`, and `later` when the sequence matters.
Within `Evaluation additions`, specify whether the next validation should focus on `single passage`, `multi passage`, or `no answer` style checks when that distinction matters, and say which failure family the evaluation is meant to confirm or falsify.
Within `Durable artifact summary`, say what durable pages were created or updated, or why the result stays chat-only.
Do not speculate past missing evidence.

## Minimal Reading Sets

- `greenfield` minimum:
  - `references/intake-checklist.md`
  - `references/retrieval-design.md`
  - `references/eval-design.md`
- `diagnosis` minimum:
  - `references/diagnosis-playbook.md`
  - `references/retrieval-design.md`
  - `references/observability-design.md`
  - `wiki/failure-modes/triage-matrix.md` when an artifact workspace exists

Read beyond these only when the request or failure mode clearly requires it.

- `references/intake-checklist.md`
  Read when the task lacks requirements or when you need a structured interview.
- `references/embedding-choice.md`
  Read when choosing or challenging the embedding layer.
- `references/vector-db-choice.md`
  Read when comparing storage, filtering, indexing, scale, or retrieval operations.
- `references/retrieval-design.md`
  Read for chunking, metadata, hybrid retrieval, reranking, and citation design.
- `references/multimodal-retrieval.md`
  Read when the corpus or failure mode depends on scans, screenshots, diagrams, tables, or cross-modal routing.
- `references/agent-framework-choice.md`
  Read only when the user needs tool use, agents, or orchestration.
- `references/eval-design.md`
  Read when planning measurement, benchmarks, or regression checks.
- `references/observability-design.md`
  Read when planning traces, logs, dashboards, or runtime monitoring.
- `references/diagnosis-playbook.md`
  Read first in diagnosis mode.
- `references/artifact-workflow.md`
  Read when the task should preserve durable RAG knowledge instead of ending in chat.
- `references/artifact-maintenance-contract.md`
  Read when the task includes ingest, query, lint, index, or durable artifact updates.
- `references/artifact-operation-checklists.md`
  Read when a short deterministic maintenance runbook is needed.
- `references/reference-to-artifact-map.md`
  Read when deciding whether a conclusion belongs in a pattern page, failure page, evaluation page, stack decision, or case note.

## Scripts

- `scripts/render_rag_plan.py`
  Render a consistent Markdown solution package from structured JSON input.
- `scripts/render_rag_diagnostic.py`
  Render a consistent Markdown diagnostic report from structured JSON input.

Use the scripts for formatting only. Do not move architecture judgment into Python.

## Principles

- Stay framework-neutral until the user's constraints justify a recommendation.
- Do not introduce an agent framework if a plain retrieval pipeline is enough.
- Do not enable agentic RAG unless the task has explicit decomposition needs, real branch conditions, and measurable benefit over simpler retrieval upgrades.
- Prefer fewer moving parts for small or stable corpora.
- Prefer a minimal viable baseline, then justify each extra layer you add.
- Distinguish retrieval failures from generation failures.
- Distinguish missing observability from actual model quality problems.
- In diagnosis mode, prioritize instrumentation, evidence collection, and reversible changes before expensive redesign.
- When recommending complexity, state what it buys and what it costs.
- State when a recommendation is an inference rather than evidence.
- Do not claim benchmark numbers that were not actually measured.
- Do not let repeated conclusions die in conversation when they are likely to matter again.
