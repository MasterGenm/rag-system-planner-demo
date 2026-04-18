# Scattered Evidence Cutoff

## Symptom

答案依赖很多小块证据，但 top-k cutoff 或过弱的 context packing 把其中一些关键碎片漏掉了。

## Likely Causes

- 对当前证据分布来说，top-k 太小
- retrieval 虽然取回了正确 topic area，但邻域覆盖不够宽
- context assembly 把排名较低、但仍然必要的 chunks 丢掉了

## Investigation Order

1. 检查缺失证据是否刚好卡在当前 cutoff 下面
2. 检查 retrieved chunks 覆盖的是 breadth，还是只有局部 density
3. 在讨论 graph 或 agents 之前，先改进 neighborhood expansion 或 context assembly

## Common False Diagnoses

- 主要问题明明是 cutoff 和 packing，却把整个 retriever 判死刑
- 在没有量化简单 breadth expansion 效果前，就升级到 graph retrieval

## Related Pages

- [Section-Aware Chunking](../patterns/section-aware-chunking.md)
- [Good Recall, Weak Ranking](good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Architecture Comparison Evidence Collapse](../case-notes/architecture-comparison-evidence-collapse.md)

## Source Trail

- `14-rag-failures` 里的 scattered evidence taxonomy
- [2026-04-09 Open Support Copilot Retrieval Eval Extract](../../sources/2026-04-09-open-support-copilot-retrieval-eval-extract.md)
