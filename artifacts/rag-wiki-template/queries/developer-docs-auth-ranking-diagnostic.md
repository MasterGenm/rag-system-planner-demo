# Developer Docs Auth Ranking Diagnostic

## Question

语料里明明有相关的认证 chunks，为什么 API key 认证问题还是答错了？

## 简短回答

这个案例更接近 ranking drift，而不是 recall failure。在 `QA000050 / run_49 / SC0004` 里，相关 chunks 确实进入了 top 10，但前五个排序结果全都不相关。下一步应该先审计 `first relevant rank`，测试 structure-aware chunking 或 metadata，再比较 reranking 行为，而不是立刻讨论更大的架构升级。

## Evidence

- [2026-04-09 RAG QA Logs Corpus Source Extract](../sources/2026-04-09-rag-qa-logs-corpus-source-extract.md)
- [Developer Docs Auth Ranking Drift](../wiki/case-notes/developer-docs-auth-ranking-drift.md)
- [Good Recall, Weak Ranking](../wiki/failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Follow-ups

- 在 hard-case review 里加入 `first relevant rank` 审计
- 对 developer docs 比较 `sliding_window_256_overlap` 和 `by_heading`
- 测试 title 或 heading-path metadata 对 ranking 的帮助
- 在讨论 graph 或 agentic 之前，把 diagnosis 限定在 bounded retrieval fixes 里
