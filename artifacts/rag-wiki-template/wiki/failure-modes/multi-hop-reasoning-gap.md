# Multi-Hop Reasoning Gap

## Symptom

系统确实取回了相关事实，但没能把它们连成回答问题所需的 reasoning chain。

## Likely Causes

- 包含相关事实的 chunks 被分别取回，却从未被组合起来
- top-k retrieval 只露出彼此孤立的片段，没有 bridge
- answer layer 缺少跨步骤串联证据的显式机制

## Investigation Order

1. 先确认中间事实确实都已经在 candidate pool 里
2. 检查答案是否依赖一个从未被真正组装出来的 `A -> B -> C` 链
3. 在讨论架构升级前，先检查系统是否需要 structured decomposition

## Common False Diagnoses

- 缺的是 evidence composition，却先去怪基础模型
- candidate coverage 还没确认，就直接跳到 graph 或 agentic RAG

## Related Pages

- [Good Recall, Weak Ranking](good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` 里的 multi-hop reasoning taxonomy
