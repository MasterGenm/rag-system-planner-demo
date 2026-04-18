# Synonymy And Jargon Gap

## Symptom

query 和 source material 指向的是同一件事，但双方使用了不同名字、缩写、别名或业务/技术术语，导致 retrieval 和 answer assembly 没能把它们对上。

## Likely Causes

- 缺少 alias mapping 或 ontology support
- metadata 没有做 terminology normalization
- query rewriting 保留了原词，但没有保留 concept equivalence

## Investigation Order

1. 检查用户措辞和 source 措辞是否指向同一个 underlying entity
2. 检查 alias 是否其实存在于 corpus 里，只是从未被 normalize
3. 在修改整个架构之前，先加入 terminology normalization

## Common False Diagnoses

- 误以为 embeddings 单独就一定能跨过术语鸿沟
- 实际失败点是 vocabulary alignment，却去怪 chunking

## Related Pages

- [Entity Ambiguity](entity-ambiguity.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- `14-rag-failures` 里的 synonymy / jargon taxonomy
