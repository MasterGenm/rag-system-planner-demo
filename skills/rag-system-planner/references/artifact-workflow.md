# Artifact Workflow

Use this reference for the durable workspace lifecycle.
For exact operation requirements, read `artifact-maintenance-contract.md`.
For the shortest runbooks, read `artifact-operation-checklists.md`.

## Core Model

Represent durable RAG knowledge in three layers:

1. `sources/`
   Raw evidence such as specs, traces, evaluation outputs, incident notes, and architecture writeups.
2. `wiki/`
   Synthesized operational knowledge such as patterns, failure modes, evaluation notes, stack decisions, and case notes.
3. `queries/`
   Saved one-off memos or comparisons worth keeping, which may later be promoted into `wiki/`.

## Lifecycle

1. Planner reads the workspace before reasoning from scratch.
2. Planner makes a bounded judgment.
3. Planner hands off durable findings when the artifact update threshold is met.
4. Artifact-maintenance runs `ingest`, `query`, `lint`, or `index`.
5. Later planner sessions start from the maintained workspace instead of rediscovering the same lesson.

## Shared Rules

- Inputs should be workspace-relative whenever possible.
- `sources/` is raw evidence and should stay immutable-by-default.
- For large inputs, navigate before reading deeply. Do not synthesize from a blind dump when targeted reading is possible.
- Important claims in `wiki/` or `queries/` should show a visible evidence trail.
- Prefer updating one canonical page over creating near-duplicates.
- Treat source staleness as a real state. If a source changes, the relationship should be refreshed or marked stale rather than silently assumed current.
- `index.md` and `log.md` are part of the maintenance contract, not optional cleanup.

## Not Now

This workbench does not yet implement MinerU-style tooling such as automatic ingest trackers, stale-source detection, or deep-reading helpers.
The immediate goal is to make the maintenance contract sharp enough that those tools can be added later without changing the conceptual model.
