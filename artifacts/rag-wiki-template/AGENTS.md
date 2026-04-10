# RAG Wiki Artifact Schema

This workspace stores durable RAG planning knowledge.

## Mission

Turn raw RAG evidence into reusable operational knowledge.

## Layers

1. `sources/` stores raw evidence and should stay immutable-by-default.
2. `wiki/` stores synthesized knowledge and is the canonical durable layer.
3. `queries/` stores saved outputs worth keeping when they are not yet canonical.

## Workspace Invariants

- Do not rewrite raw evidence as if it were original analysis.
- Use targeted reading before deep synthesis on large files or long notes.
- Prefer updating an existing page over creating near-duplicates.
- Keep a visible trail to evidence when making important claims.
- Save recurring conclusions into `wiki/`, not just `queries/`.
- Treat source staleness as a real condition. If a source changes or confidence drops, refresh the relationship or mark it as stale instead of silently carrying the old conclusion forward.
- Keep the index short and navigable.
- Use folder `README.md` files as the primary navigation hubs for large taxonomies.
- Append only completed operations to the log.
- If a finding is reusable as a pattern, failure mode, stack boundary, evaluation rule, or recurring case lesson, write it back into the workspace in the same session.

## Operations

### Ingest

Use when new evidence appears in `sources/`.

1. Read `index.md`.
2. Read the relevant folder hubs and candidate canonical pages before creating anything new.
3. Navigate before deep-reading large sources when possible.
4. Update or create the right wiki pages.
5. Preserve a visible source trail for important claims.
6. Update `index.md` or folder hubs only if navigation changed.
7. Append to `log.md` only when the operation actually changed the workspace.

### Query

Use when answering a RAG architecture or diagnosis question.

1. Read `index.md`.
2. Read the relevant wiki pages first.
3. Use `sources/` to verify claims when needed.
4. Save durable answers to `queries/` or fold them into `wiki/`.
5. If the answer became reusable, update the smallest fitting canonical page instead of creating a duplicate.

### Lint

Check for:

- orphan pages
- duplicate pages
- root-index bloat
- stale stack decisions
- stale source relationships
- unsupported claims
- missing evaluation or observability coverage
- taxonomy drift

Record explicit findings with affected files and recommended fixes. Do not claim the workspace is "clean" without listing what was checked.

### Index

Use after major ingest, cleanup, or taxonomy changes.

1. Keep the root index thin.
2. Refresh folder `README.md` hubs when their taxonomies changed.
3. Avoid duplicating content only for navigation.
4. Check that links still resolve after navigation changes.

## Templates

Use the templates under `templates/` when the operation would benefit from a durable run artifact:

- `ingest-note-template.md`
- `lint-report-template.md`
- `index-refresh-note-template.md`
- `maintenance-run-template.md`

## Promotion Guide

- `wiki/patterns/`: reusable retrieval and architecture patterns
- `wiki/failure-modes/`: recurring diagnostic classes
- `wiki/evaluations/`: hard-case sets, metric recipes, trace review rules, observability signals
- `wiki/stack-decisions/`: recurring architecture and tool boundaries
- `wiki/case-notes/`: project-specific history that may still matter later
