# Developer Docs Auth Ranking Drift

## Context

Developer documentation benchmark case taken from the `rag-qa-logs-corpus-data` external dataset.

## Symptom

The system answers the API-key authentication question with a partial and unfaithful response even though relevant authentication chunks exist in the retrieved set.

## Observed

- `QA000050 / run_49 / SC0004` is labeled `partial`, `unfaithful`, with `hallucination_flag=1`
- `recall_at_10=1.0` but `recall_at_5=0.0`
- the first five retrieved chunks are all labeled irrelevant
- relevant chunks appear only at ranks 6 through 8
- the irrelevant top result and the relevant results all look semantically close because they mention endpoints, responses, and authentication in overlapping developer-doc language

## Inferred

- this is closer to `Good Recall, Weak Ranking` than to missing evidence
- ranking and reranking need tighter separation between authentication-specific evidence and generic endpoint-adjacent evidence
- chunk titles or heading-path metadata are probably underused

## Unknown

- whether better heading-aware chunking alone would move the relevant chunks into top 3
- whether a stronger reranker would be enough without changing chunking
- whether answer synthesis is amplifying the ranking miss into hallucination

## Durable Lessons

- track `first relevant rank` alongside `recall_at_k`
- review cases where `recall_at_10` is healthy but `recall_at_5` is zero before changing architecture
- test structure-aware metadata and chunk boundaries before adding heavier orchestration

## Related Pages

- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Section-Aware Chunking](../patterns/section-aware-chunking.md)

## Source Trail

- [2026-04-09 RAG QA Logs Corpus Source Extract](../../sources/2026-04-09-rag-qa-logs-corpus-source-extract.md)
