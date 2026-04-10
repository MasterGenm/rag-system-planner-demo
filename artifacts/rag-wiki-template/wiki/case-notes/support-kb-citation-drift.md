# Support KB Citation Drift

## Context

Support knowledge base with structured product docs, runbooks, and incident writeups.

## Symptom

Relevant evidence often appears in the candidate pool, but the final answer cites the wrong adjacent section or an over-broad chunk.

## Observed

- candidate recall is often acceptable
- citation anchors are coarse
- stage-level traces are incomplete

## Inferred

- section boundaries and heading-path metadata are too weak
- ranking quality and citation assembly are being conflated

## Unknown

- whether reranking alone would fix the issue
- whether answer assembly is dropping precise evidence spans

## Durable Lessons

- citation quality deserves its own evaluation track
- section-aware chunking should be tested before heavier architecture changes
- trace review must separate candidate quality from answer assembly quality

## Related Pages

- [Section-Aware Chunking](../patterns/section-aware-chunking.md)
- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- [Sample Support Incident](../../sources/sample-support-incident.md)
