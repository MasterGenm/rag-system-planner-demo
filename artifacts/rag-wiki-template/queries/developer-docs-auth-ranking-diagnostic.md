# Developer Docs Auth Ranking Diagnostic

## Question

Why did the API-key authentication answer fail even though the corpus contains relevant authentication chunks?

## Short Answer

This case is closer to ranking drift than recall failure. In `QA000050 / run_49 / SC0004`, the relevant chunks exist in the top 10, but the first five ranked chunks are all irrelevant. The next move is to audit first-relevant-rank, test structure-aware chunking or metadata, and compare reranking behavior before considering any larger architecture upgrade.

## Evidence

- [2026-04-09 RAG QA Logs Corpus Source Extract](../sources/2026-04-09-rag-qa-logs-corpus-source-extract.md)
- [Developer Docs Auth Ranking Drift](../wiki/case-notes/developer-docs-auth-ranking-drift.md)
- [Good Recall, Weak Ranking](../wiki/failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Follow-ups

- add a `first relevant rank` audit to hard-case review
- compare `sliding_window_256_overlap` against `by_heading` for developer docs
- test title or heading-path metadata in ranking
- keep the diagnosis inside bounded retrieval fixes before discussing graph or agentic changes
