# Sample End-To-End Flow

## Raw Evidence

- `artifacts/rag-wiki-template/sources/sample-support-incident.md`

## Planner Step

- `planner` reads the workspace, classifies the issue, and decides the bounded remediation path

## Durable Pages Created

- `artifacts/rag-wiki-template/wiki/case-notes/support-kb-citation-drift.md`
- `artifacts/rag-wiki-template/wiki/failure-modes/good-recall-weak-ranking.md`
- `artifacts/rag-wiki-template/wiki/evaluations/hard-case-trace-review.md`

## Artifact-Maintenance Step

- `artifact-maintenance` writes or updates the durable pages above and preserves the evidence trail

## User-Facing Memo

- `artifacts/rag-wiki-template/queries/sample-diagnostic-note.md`

## Why This Example Exists

It demonstrates that v2 is not just a better answer format. It is a workflow where planner makes the judgment and artifact-maintenance preserves the durable result before producing a user-facing memo.
