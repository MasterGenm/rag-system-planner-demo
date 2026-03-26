---
name: rag-system-planner
description: Plan and diagnose retrieval-augmented generation (RAG) systems with an emphasis on bounded complexity. Use for RAG architecture tradeoffs, retrieval failure diagnosis, evaluation and observability planning, and deciding whether to stay with plain RAG or escalate to hybrid, graph, or agentic workflows. Trigger for requests about recall, ranking, hallucinations, latency, citations, and premature upgrades.
---

# RAG System Planner

## Overview

Design new RAG systems and diagnose existing ones without hardcoding a single framework stack. Gather constraints, compare options, explain tradeoffs, and produce a complete solution package or diagnostic report.

Keep the workflow framework-neutral. Prefer the simplest architecture that meets the user's goals. Escalate to graph or agentic RAG only when the failure mode or workflow genuinely requires it. Label assumptions explicitly when the user has not provided enough details.
Avoid template-only advice. Tie each major recommendation to the actual scale, modality, update pattern, latency target, or workflow complexity in the request. Say what you are deliberately not adding yet when simplicity is the better trade.

## Workflow Selection

Choose one of these modes before making recommendations:

- `greenfield`: The user is designing a new RAG system or replacing most of an old one.
- `diagnosis`: The user already has a RAG system and wants to improve recall, latency, groundedness, observability, or operational reliability.

If the request mixes both, start in diagnosis mode, then end with a replacement or upgrade plan.

## Comparison Requests

If the user is primarily comparing options instead of asking for a full greenfield design or a full diagnosis, keep the reasoning inside the current workflow but return a lighter decision memo.

Use these sections:

1. Decision context
2. Options compared
3. Recommendation
4. Why this fits
5. Not chosen because
6. What would change the decision

## Intake

Use `references/intake-checklist.md` whenever requirements are missing or vague.

Collect only the details needed to make architecture decisions:

- Data type and source
- Scale and update frequency
- Interaction pattern
- Quality priorities
- Cost and latency constraints
- Deployment constraints
- Existing stack and migration constraints
- Evaluation and observability expectations

If the user cannot answer everything, proceed with a short assumptions section instead of blocking.

## Greenfield Workflow

1. Clarify the problem, users, data modalities, and constraints.
2. Read `references/retrieval-design.md` to shape chunking, metadata, retrieval, reranking, and citation flow.
3. Read `references/multimodal-retrieval.md` if the corpus contains scans, screenshots, diagrams, tables, or other non-text evidence.
4. Read `references/embedding-choice.md` when embedding selection is not obvious.
5. Read `references/vector-db-choice.md` when storage, filtering, hybrid search, or operations tradeoffs matter.
6. Read `references/agent-framework-choice.md` only if the user wants agent behavior, tool use, or orchestration.
7. Read `references/eval-design.md` to define offline and online validation.
8. Read `references/observability-design.md` to define tracing, monitoring, and failure analysis.
9. Produce a solution package with assumptions, stack choices, architecture, evaluation, observability, rollout phases, and explicit "not now" decisions for complexity you are intentionally deferring.
10. If a structured final document would help, run `scripts/render_rag_plan.py`.

## Diagnosis Workflow

1. Summarize symptoms in concrete terms: low recall, irrelevant retrieval, hallucinations, latency, cost, missing citations, or poor agent behavior.
2. Read `references/diagnosis-playbook.md` first.
3. Label each hypothesis as `observed`, `inferred`, or `unknown`. Do not let missing evidence silently turn into a root-cause claim.
4. Read `references/retrieval-design.md` if the issue may come from chunking, metadata, retrieval, reranking, or prompt assembly.
5. Read `references/multimodal-retrieval.md` if scans, screenshots, diagrams, tables, OCR quality, or modality routing may be involved.
6. Read `references/embedding-choice.md` if representation quality or multilingual behavior is suspect.
7. Read `references/vector-db-choice.md` if filtering, indexing, hybrid search, persistence, or scale appear to be the bottleneck.
8. Read `references/eval-design.md` to identify missing benchmarks and datasets.
9. Read `references/observability-design.md` to identify missing traces or runtime signals.
10. Produce a diagnostic report with likely causes, missing evidence, investigation order, and a prioritized remediation path. In `Recommended changes`, prefer a `now`, `next`, `later` ordering and favor reversible fixes before expensive redesign.
11. If a structured final document would help, run `scripts/render_rag_diagnostic.py`.

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

Within `Recommended stack` and `Risks and tradeoffs`, explain why the chosen level of complexity fits and what you are intentionally not adding yet.
Within `Retrieval design`, include modality routing and fallback behavior when the corpus is not text-only.

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

Within `Working hypotheses`, label what is observed versus inferred.
Within `Recommended changes`, order actions as `now`, `next`, and `later` when the sequence matters.
Do not speculate past missing evidence.

## Reference Map

## Minimal Reading Sets

- `greenfield` minimum:
  - `references/intake-checklist.md`
  - `references/retrieval-design.md`
  - `references/eval-design.md`
- `diagnosis` minimum:
  - `references/diagnosis-playbook.md`
  - `references/retrieval-design.md`
  - `references/observability-design.md`

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
