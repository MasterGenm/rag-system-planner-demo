# When Not To Use Agentic RAG

## Summary

如果更简单的 retrieval pipeline 还没有被证明确实不够，就不要引入 agentic orchestration。

## 哪些信号说明应该先修简单层

- 没有 retrieval traces
- 没有 hard-case evaluation set
- chunking 或 metadata 设计明显偏弱
- citation 行为很差，而且这种问题在不加 orchestration 的前提下就能解释清楚

## Agentic RAG 能买来什么

- branching workflows
- tool use
- 跨多个步骤的 decomposition

## 它的代价是什么

- latency
- 调试复杂度
- observability 负担
- 更多 failure surface

## Related Pages

- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)

## Source Trail

- 来自 `rag-system-planner` 的 bounded-complexity 原则
