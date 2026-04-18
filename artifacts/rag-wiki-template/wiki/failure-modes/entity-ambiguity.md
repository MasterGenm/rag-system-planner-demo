# Entity Ambiguity

## Symptom

系统因为名字在不同 domain、产品、人物或概念之间重叠，而取回了错误实体的证据。

## Likely Causes

- metadata 缺少 entity type 或消歧语境
- retrieval 过度依赖表层 lexical overlap
- query 没有写清 intent 或 entity type

## Investigation Order

1. 检查 candidate set 是否混入了多个同名实体
2. 检查 metadata 是否携带 entity type、domain 或 namespace
3. 测试 query rewriting 或 entity normalization 是否能改善消歧
4. 然后再决定是否真的需要更强的 ontology 或 graph layer

## Common False Diagnoses

- 真正的问题是缺少 entity resolution，却把锅全甩给 embeddings
- 模型其实忠实地使用了错误实体证据，却误判成 hallucination

## Related Pages

- [Synonymy And Jargon Gap](synonymy-and-jargon-gap.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- fareedkhan `14-rag-failures` taxonomy
