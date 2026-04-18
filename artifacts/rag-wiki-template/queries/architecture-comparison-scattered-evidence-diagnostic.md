# Architecture Comparison Scattered Evidence Diagnostic

## Question

为什么 `Chroma` 对 `Qdrant` 的架构比较总会塌缩成单边证据？

## 简短回答

这个案例更接近 `Scattered Evidence Cutoff`，而不是简单的 ranking 问题。答案需要同时覆盖 `Chroma` 和 `Qdrant` 两边的证据，但实际 retrieved set 一直集中在 `Chroma` 附近。下一步应该先测试证据广度策略，例如 query decomposition、按 source family 做 coverage 检查，以及更宽的 neighborhood expansion，然后再讨论更复杂的架构升级。

## Evidence

- [2026-04-09 Open Support Copilot Retrieval Eval Extract](../sources/2026-04-09-open-support-copilot-retrieval-eval-extract.md)
- [Architecture Comparison Evidence Collapse](../wiki/case-notes/architecture-comparison-evidence-collapse.md)
- [Scattered Evidence Cutoff](../wiki/failure-modes/scattered-evidence-cutoff.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Follow-ups

- 在 retrieval evaluation 里加入按比较双方分开的 coverage 检查
- 在最终综合之前，先测试拆解式 retrieval，例如 `Chroma filtering` 加 `Qdrant filtering`
- 对比按 product family 做 metadata filtering 与普通 semantic retrieval 的差异
- 当比较问题只取回了一边证据时，要求答案层 abstain 或明确降格表述
