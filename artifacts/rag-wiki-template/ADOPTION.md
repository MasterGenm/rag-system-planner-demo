# Artifact Scaffold Adoption Guide

Use this guide when you want to go from zero to your first durable RAG artifact.

This is a phase 2 onboarding document.
It does not add new behavior to the skill.
It only turns the existing phase 1 workspace into a clearer first-session path.

## When To Use This Scaffold

Use [rag-wiki-template](./README.md) when at least one of these is true:

- you expect the same failure modes or stack decisions to come up again
- you want diagnosis work to accumulate instead of restarting from chat
- you want a place to keep raw evidence, reusable conclusions, and saved memos together
- you want later planner runs to start from maintained artifacts instead of rediscovering the same lesson

If you only need a one-off answer, you can stop at [../../skills/rag-system-planner/SKILL.md](../../skills/rag-system-planner/SKILL.md) and stay chat-only.

## First Session Path

Follow this order:

1. Read [AGENTS.md](AGENTS.md).
2. Read [index.md](index.md).
3. Read the relevant hub page under `wiki/`.
4. Add one real source file to `sources/`.
5. Choose one small maintenance path: `ingest` or `query`.
6. Create one durable artifact.
7. Append a short completed entry to [log.md](log.md).

Do not try to populate the whole scaffold in one session.
The goal is one real source, one real judgment, and one durable page.

## What Goes Where

- `sources/`
  Raw evidence. Keep it immutable-by-default.
- `wiki/`
  Reusable knowledge. Put recurring patterns, failure modes, evaluations, stack decisions, and case notes here.
- `queries/`
  Saved answers that are useful but not yet stable or broad enough to become canonical pages.
- `index.md`
  Thin root navigation.
- `log.md`
  Completed maintenance operations only.

## Step 1: Add The First Source

Add one raw input to [sources/](sources/).

Good first sources:

- an incident note
- a retrieval trace excerpt
- an eval output
- a design or architecture note

Use a date-prefixed filename when practical.
Do not rewrite the source into analysis before storing it.

## Step 2: Choose The First Workstream

Use `query` when you are answering a specific question and the result may or may not become canonical.

Start from:

- [templates/query-note-template.md](templates/query-note-template.md)

Use `ingest` when you already know the source contains reusable knowledge that should update the workspace.

Start from:

- [templates/ingest-note-template.md](templates/ingest-note-template.md)

Use `lint` or `index` only after real content exists.

Start from:

- [templates/lint-report-template.md](templates/lint-report-template.md)
- [templates/index-refresh-note-template.md](templates/index-refresh-note-template.md)

## Step 3: Read Before You Write

Before creating a new durable page:

1. Read [wiki/failure-modes/README.md](wiki/failure-modes/README.md) if the issue is diagnostic.
2. Read [wiki/failure-modes/triage-matrix.md](wiki/failure-modes/triage-matrix.md) when the symptom is still fuzzy.
3. Read [wiki/evaluations/README.md](wiki/evaluations/README.md) if the main lesson is about measurement or trace review.
4. Prefer updating one existing canonical page over creating a near-duplicate.

## Step 4: Create The First Durable Artifact

Use [templates/page-template.md](templates/page-template.md) when you need a new canonical page in `wiki/`.

Good first durable artifacts:

- one case note tied to one incident
- one failure page update tied to recurring evidence
- one evaluation page update tied to a reusable review rule

Promotion rule:

- keep temporary or narrow results in `queries/`
- move reusable conclusions into `wiki/`

Always keep a visible source trail.

## Step 5: Record The Operation

After a real maintenance pass completes:

1. add a short entry to [log.md](log.md)
2. update [index.md](index.md) or a hub page only if navigation changed

Use [templates/maintenance-run-template.md](templates/maintenance-run-template.md) when you want a compact record of:

- what changed
- what evidence was used
- what still remains open

## Recommended First Durable Artifact

The best default first run is:

1. put one source into `sources/`
2. create one ingest note
3. update or create one canonical page in `wiki/`
4. append one log entry

If the first interaction is mainly question-answering, the best default is:

1. save the answer in `queries/`
2. promote it into `wiki/` only if it becomes reusable

## Example Reading Order

For the shortest onboarding path, read these in order:

1. [../../examples/sample-rag-end-to-end.md](../../examples/sample-rag-end-to-end.md)
2. [../../examples/sample-rag-planner-handoff.md](../../examples/sample-rag-planner-handoff.md)
3. [../../examples/sample-rag-real-walkthroughs.md](../../examples/sample-rag-real-walkthroughs.md)
4. [../../examples/sample-rag-artifact-maintenance-ops.md](../../examples/sample-rag-artifact-maintenance-ops.md)

After that, use these as shape references:

- [../../examples/sample-rag-case-note.md](../../examples/sample-rag-case-note.md)
- [../../examples/sample-rag-pattern-page.md](../../examples/sample-rag-pattern-page.md)
- [../../examples/sample-rag-wiki-index.md](../../examples/sample-rag-wiki-index.md)

Keep these out of the main adoption path:

- [../../examples/sample-rag-plan.md](../../examples/sample-rag-plan.md)
- [../../examples/sample-rag-diagnostic.md](../../examples/sample-rag-diagnostic.md)

Those are useful final outputs, but they do not teach the durable workflow as directly.

## First Evaluation Path

After the first source and first durable page exist, use this shorter path for an initial evaluation-oriented pass:

1. Read [wiki/evaluations/README.md](wiki/evaluations/README.md).
2. Read [wiki/evaluations/hard-case-trace-review.md](wiki/evaluations/hard-case-trace-review.md).
3. Save the first reusable evaluation conclusion in `wiki/evaluations/` or `queries/`, depending on how stable it is.

## Success Criteria

This guide worked if, after one session, you can point to:

- one raw source in `sources/`
- one saved memo in `queries/` or one canonical page in `wiki/`
- one updated navigation surface if needed
- one completed line in `log.md`

At that point, later planner runs can start from the workspace instead of starting from zero.
