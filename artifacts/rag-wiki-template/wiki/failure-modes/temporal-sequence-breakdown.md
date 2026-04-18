# Temporal Sequence Breakdown

## Symptom

系统取回了相关事件，但把它们的顺序打乱了，导致最终答案在 timeline 或 causal sequence 上出错。

## Likely Causes

- ranking 优化的是 relevance，而不是 sequence
- event chain 信息没有在 metadata 里被清楚保留
- answer assembly 没有强制 chronological order

## Investigation Order

1. 检查这个问题是否本质上需要有序的 event reasoning
2. 检查 candidate set 是否包含了正确事件，但没有形成稳定顺序
3. 在加 graph 或 agentic complexity 前，先保住 temporal anchors

## Common False Diagnoses

- 实际问题是 ordering，却误判成普通 hallucination
- 只加 retrieval breadth，却不加 temporal organization

## Related Pages

- [Contradictory Facts And Recency](contradictory-facts-and-recency.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` 里的 temporal sequence taxonomy
