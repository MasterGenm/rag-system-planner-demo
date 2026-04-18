# Causal Synthesis Failure

## Symptom

系统会重复正向或描述性证据，但漏掉那些真正会改变答案的隐藏冲突、约束或因果不兼容关系。

## Likely Causes

- retrieval 过度偏向 semantic similarity，而低估了 constraint logic
- answerer 没有检查 retrieved properties 是否能共存
- review step 缺少 causal 或 rule-based reasoning

## Investigation Order

1. 检查答案是否只是在总结表层的正向证据
2. 检查关键约束或冲突条件是否其实已经被取回、但被忽略了
3. 在升级复杂度前，先加入显式的 contradiction 或 compatibility review

## Common False Diagnoses

- 在证据其实已存在、只是没有被 reconcile 时，就误判成 retriever 失败
- 不去补更好的 synthesis check，反而直接加更多 retrieval stages

## Related Pages

- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Support KB Citation Drift](../case-notes/support-kb-citation-drift.md)

## Source Trail

- `14-rag-failures` 里的 causal synthesis taxonomy
