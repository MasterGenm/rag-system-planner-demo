# Centrality Vs Title Bias

## Symptom

系统会优先选出最显眼、头衔最高的角色，而不是实际证据网络里最重要的 connector、influencer 或 bottleneck。

## Likely Causes

- answering 过度依赖表层头衔或显著性词汇
- 系统没有机制去检查 relationship topology
- retrieval 只围绕局部描述展开，漏掉了 communication 或 dependency structure

## Investigation Order

1. 检查答案是不是选了头衔最高的人，而不是真正的桥接节点
2. 核验这类证据是否需要 topology-aware analysis，而不是 title matching
3. 在讨论完整 graph upgrade 前，先测试更小的 structural features

## Common False Diagnoses

- 把 topology 问题误当成普通 ranking 问题
- 在没有确认任务类型前，就默认上 agentic 或 graph 系统

## Related Pages

- [Intersection Blindness](intersection-blindness.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- `14-rag-failures` 里的 centrality taxonomy
