# Good Recall, Weak Ranking

## Symptom

相关证据已经进入 candidate set，但 top-ranked 结果依然很弱，或者和问题对不准。

## Likely Causes

- reranking 缺失或偏弱
- chunk boundaries 太粗
- metadata 不足以区分近似重复证据

## Investigation Order

1. 先确认正确证据已经在 candidate pool 里
2. 检查 chunk granularity 和 citation anchors
3. 检查 ranking 或 reranking 行为
4. 做完这些后，再讨论更大的架构变动

## Common False Diagnoses

- candidate set 已经不错时，还去怪 embeddings
- ranking 还没修，就先升级到 agentic RAG

## Related Pages

- [Section-Aware Chunking](../patterns/section-aware-chunking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Developer Docs Auth Ranking Drift](../case-notes/developer-docs-auth-ranking-drift.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- 当前 `rag-system-planner` 的 diagnosis 与 retrieval heuristics
- [2026-04-09 RAG QA Logs Corpus Source Extract](../../sources/2026-04-09-rag-qa-logs-corpus-source-extract.md)
