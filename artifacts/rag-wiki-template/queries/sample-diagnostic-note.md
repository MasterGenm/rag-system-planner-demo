# Sample Diagnostic Note

## Question

为什么 support assistant 经常引用相邻章节，而不是精确的排障步骤？

## 简短回答

这个问题更接近 citation precision 和 ranking granularity，而不是明显的 retrieval failure。下一步应该先改进 section-aware chunking，并补上针对 chunk ids、scores 和 citation anchors 的 trace review，再考虑升级架构复杂度。

## Evidence

- [Sample Support Incident](../sources/sample-support-incident.md)
- [Good Recall, Weak Ranking](../wiki/failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Follow-ups

- 测试 heading-path metadata
- 在 eval 中把 citation correctness 和 candidate recall 分开
- 补上 stage-level trace coverage
