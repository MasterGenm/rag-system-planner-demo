# Sample Planner To Artifact Handoff

## Purpose

Show how the proposed skill should behave after the split into `planner` and `artifact-maintenance`.

## Example Case

Use the ranking failure walkthrough already present in the scaffold:

- `artifacts/rag-wiki-template/sources/2026-04-09-rag-qa-logs-corpus-source-extract.md`
- `artifacts/rag-wiki-template/wiki/case-notes/developer-docs-auth-ranking-drift.md`
- `artifacts/rag-wiki-template/wiki/failure-modes/good-recall-weak-ranking.md`
- `artifacts/rag-wiki-template/wiki/evaluations/hard-case-trace-review.md`
- `artifacts/rag-wiki-template/queries/developer-docs-auth-ranking-diagnostic.md`

## Handoff Flow

1. `planner` reads the workspace before using static references.
2. `planner` classifies the issue as `Good Recall, Weak Ranking`.
3. `planner` recommends bounded fixes such as first-relevant-rank inspection and structure-aware chunking.
4. `artifact-maintenance` stores the raw extract, updates the case note and failure page, and preserves the user-facing memo.
5. A later `planner` session starts from those durable artifacts instead of re-deriving the same lesson.

## Why This Example Exists

This is the practical meaning of the new two-layer skill contract: planner makes the judgment, artifact-maintenance preserves the reusable result.
