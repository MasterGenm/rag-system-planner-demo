# Sample RAG Case Note

## Context

Internal support knowledge base with product docs, runbooks, and incident writeups.

## Observed Problem

Relevant evidence often appears in the retrieval pool, but final answers cite nearby sections instead of the precise troubleshooting step.

## Durable Findings

- chunking should preserve section path metadata
- citation quality is a separate problem from gross recall
- reranking should be tested only after candidate quality is confirmed

## Related Wiki Pages

- `wiki/patterns/section-aware-chunking.md`
- `wiki/failure-modes/good-recall-weak-ranking.md`
