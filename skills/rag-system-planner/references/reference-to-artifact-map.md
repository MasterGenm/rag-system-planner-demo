# Reference To Artifact Map

Use this file to decide how static guidance should be promoted into the durable artifact workspace.

## Mapping

- `intake-checklist.md`
  Promote durable project facts into `wiki/case-notes/` when they are likely to matter again.
- `retrieval-design.md`
  Promote reusable chunking, metadata, retrieval, reranking, citation, and abstention guidance into `wiki/patterns/`.
- `diagnosis-playbook.md`
  Promote recurring symptom classes and investigation ladders into `wiki/failure-modes/`.
  In active diagnosis, use `wiki/failure-modes/triage-matrix.md` as the entry point and then promote lasting conclusions into one canonical failure page.
- `eval-design.md`
  Promote hard-case definitions, metric recipes, and review procedures into `wiki/evaluations/`.
- `observability-design.md`
  Promote trace requirements, stage-level latency guidance, and debugging signals into `wiki/evaluations/` or a related case note.
- `embedding-choice.md`
  Promote recurring representation boundaries into `wiki/stack-decisions/`.
- `vector-db-choice.md`
  Promote durable storage and filtering tradeoffs into `wiki/stack-decisions/`.
- `agent-framework-choice.md`
  Promote upgrade boundaries and "not now" decisions into `wiki/stack-decisions/`.
- `multimodal-retrieval.md`
  Promote modality-routing patterns into `wiki/patterns/` and recurring OCR or screenshot failure classes into `wiki/failure-modes/`.

## Promotion Heuristic

Choose the destination by the primary reuse value:

- use `patterns/` for reusable ways of building
- use `failure-modes/` for reusable ways of debugging
- use `evaluations/` for reusable ways of measuring and tracing
- use `stack-decisions/` for recurring architecture boundaries
- use `case-notes/` for project-specific history and evidence

If the artifact is still too temporary or scoped, save it under `queries/` first and promote it later.

## Planner Handoff Targeting

When planner hands work to artifact-maintenance, choose one primary destination first:

- `patterns/` when the lesson is a reusable build or retrieval rule
- `failure-modes/` when the lesson is a reusable debugging class or investigation ladder
- `evaluations/` when the lesson is a measurement, trace, or review rule
- `stack-decisions/` when the lesson is a recurring architecture boundary or "not now" choice
- `case-notes/` when the lesson is tied to one project, one incident, or one source bundle
- `queries/` when the result is useful but not yet stable enough to canonize

If more than one page type could fit, update the smallest reusable canonical page and keep extra project-specific detail in a case note or query memo.

## Handoff Payload

The planner handoff should make these fields explicit:

- question or symptom
- `observed`, `inferred`, and `unknown` claims
- evidence touched
- primary target artifact type
- secondary targets if any
- whether the write is `canonical` or `query-only`
