# Directionality Confusion

## Symptom

系统会混淆带方向性的关系，例如 ownership、dependency、caller-callee 或 parent-child。

## Likely Causes

- embeddings 把有方向的关系压扁成对称相似性
- chunk text 对关系方向的强调不够强
- prompts 过度信任那些语义相近、但方向相反的证据

## Investigation Order

1. 先识别真正关键的 directional claim
2. 检查 retrieved evidence 是否保留了“谁对谁做了什么”
3. 检查 metadata 或 schema 是否能显式编码方向
4. 只有做到这一步后，才考虑更重的 graph representations

## Common False Diagnoses

- 真正的问题是 directional semantics，却误判成通用 retrieval 问题
- 在关系编码还没理清前，就先上更大的模型

## Related Pages

- [Hierarchy Loss](hierarchy-loss.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- fareedkhan `14-rag-failures` taxonomy
