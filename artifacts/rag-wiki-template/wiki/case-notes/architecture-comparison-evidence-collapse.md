# Architecture Comparison Evidence Collapse

## Context

这个架构比较案例来自 `open-support-copilot` 的 retrieval-eval slice。

## Symptom

问题在问 support copilot 应该继续留在 `Chroma` 还是迁移到 `Qdrant`，但 retrieved evidence 明显向 `Chroma` 一侧塌缩，导致 `Qdrant` 侧证据太少。

## Observed

- gold evidence 横跨 `Chroma` 与 `Qdrant` 双方，共四个 URL
- 在 `Chroma` backend 审计里，`Recall@5 = 0.5000`，而且命中的两个 URL 都是 `Chroma` 页面
- 在 `Qdrant` backend 审计里，`Recall@5 = 0.2500`，可见命中的 URL 仍然是 `Chroma` 页面
- 两个 backend 都没能为这个 query 提供平衡的 top-5 比较证据集

## Inferred

- 这个案例更符合 `Scattered Evidence Cutoff`，而不是单纯的 ranking miss
- retriever 一直停留在单个局部证据邻域里，没有把比较问题需要的双方证据都收齐
- 在任何更大的架构变更之前，retrieval breadth 和 query decomposition 更值得优先检查

## Unknown

- 如果不改 backend，只做拆解式 comparison query，是否能同时召回 `Chroma` 和 `Qdrant` 证据
- 按 product 或 source family 做 metadata filters，是否能改善 breadth
- 当双方证据都已出现后，reranking 是否还能进一步改进

## Durable Lessons

- comparison 问题需要 breadth checks，而不只是 topic relevance checks
- `Recall@k` 应该结合比较双方各自的 evidence coverage 一起看
- 当 comparison 的一边根本没进 retrieval 时，架构类答案应该 fail closed

## Related Pages

- [Scattered Evidence Cutoff](../failure-modes/scattered-evidence-cutoff.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Section-Aware Chunking](../patterns/section-aware-chunking.md)

## Source Trail

- [2026-04-09 Open Support Copilot Retrieval Eval Extract](../../sources/2026-04-09-open-support-copilot-retrieval-eval-extract.md)
