# Sample Diagnostic Note

## Question

Why does the support assistant often cite nearby sections instead of the exact troubleshooting step?

## Short Answer

The problem appears to be closer to citation precision and ranking granularity than to gross retrieval failure. The next step is to improve section-aware chunking and add trace review for chunk ids, scores, and citation anchors before escalating architecture complexity.

## Evidence

- [Sample Support Incident](../sources/sample-support-incident.md)
- [Good Recall, Weak Ranking](../wiki/failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Follow-ups

- test heading-path metadata
- separate citation correctness from candidate recall in evals
- add stage-level trace coverage
