# Support KB Citation Drift

## Context

一个包含结构化产品文档、runbooks 和 incident writeups 的 support knowledge base。

## Symptom

相关证据往往已经进入 candidate pool，但最终答案引用的却是错误的相邻章节，或一个范围过宽的 chunk。

## Observed

- candidate recall 往往可以接受
- citation anchors 过粗
- stage-level traces 不完整

## Inferred

- section boundaries 和 heading-path metadata 偏弱
- ranking 质量和 citation assembly 被混在一起判断了

## Unknown

- 单独加强 reranking 是否就足够
- answer assembly 是否在丢弃精确 evidence spans

## Durable Lessons

- citation quality 应该有自己独立的 evaluation track
- 在更重的架构变更之前，先测试 section-aware chunking
- trace review 必须把 candidate quality 和 answer assembly quality 分开

## Related Pages

- [Section-Aware Chunking](../patterns/section-aware-chunking.md)
- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- [Sample Support Incident](../../sources/sample-support-incident.md)
