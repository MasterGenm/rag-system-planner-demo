# Developer Docs Auth Ranking Drift

## Context

这个 developer documentation benchmark 案例来自外部数据集 `rag-qa-logs-corpus-data`。

## Symptom

系统在回答 API key 认证问题时给出了 partial 且 unfaithful 的答案，尽管 retrieved set 里实际上存在相关的认证 chunks。

## Observed

- `QA000050 / run_49 / SC0004` 被标记为 `partial`、`unfaithful`，并且 `hallucination_flag=1`
- `recall_at_10=1.0`，但 `recall_at_5=0.0`
- 前五个 retrieved chunks 全都被标记为 irrelevant
- relevant chunks 只出现在 rank 6 到 rank 8
- 虽然 top 结果不相关，但它们和 relevant 结果在语义上看起来都很接近，因为都提到了 endpoints、responses 和 authentication，且都来自 developer docs 语境

## Inferred

- 这更接近 `Good Recall, Weak Ranking`，而不是缺证据
- ranking 和 reranking 需要更清楚地区分“认证专用证据”和“泛 endpoint 邻域证据”
- chunk title 或 heading-path metadata 很可能没有被充分利用

## Unknown

- 仅仅改进 heading-aware chunking，是否就能把 relevant chunks 推进 top 3
- 不改 chunking、只加强 reranker 是否足够
- answer synthesis 是否把 ranking miss 放大成了 hallucination

## Durable Lessons

- 除了 `recall_at_k`，还要追踪 `first relevant rank`
- 在改架构之前，先复盘那些 `recall_at_10` 很健康、但 `recall_at_5` 为零的案例
- 在加更重的 orchestration 之前，先测试 structure-aware metadata 和 chunk boundaries

## Related Pages

- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Section-Aware Chunking](../patterns/section-aware-chunking.md)

## Source Trail

- [2026-04-09 RAG QA Logs Corpus Source Extract](../../sources/2026-04-09-rag-qa-logs-corpus-source-extract.md)
