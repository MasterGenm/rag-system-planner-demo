# Contradictory Facts And Recency

## Symptom

系统从不同时间或不同版本取回了相互冲突的事实，却无法判断哪一个才应该支配最终答案。

## Likely Causes

- timestamps 或 version metadata 缺失，或者没有被充分使用
- ranking 没有把 recency 或 policy precedence 计入
- 新旧证据被当成同等 truth candidates

## Investigation Order

1. 检查冲突证据是否来自不同时间段或不同版本
2. 核验 retriever 和 ranker 是否保留了 recency 或 policy priority
3. 在重构整个 stack 之前，先把 version resolution 和通用 retrieval quality 区分开

## Common False Diagnoses

- 在模型其实是在平均冲突 truth states 时，就误判成 hallucination
- 问题明明是 time-aware resolution，却盲目加更多 retrieval

## Related Pages

- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` 里的 contradictory facts / latest-truth taxonomy
