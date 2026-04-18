# Hierarchy Loss

## Symptom

系统确实取回了 leaf-level chunk，但答案丢掉了正确解释它所需要的 parent 或 root context。

## Likely Causes

- chunking 把 heading path 或 parent hierarchy 剥掉了
- retrieval 只偏爱局部片段，而没有保留结构血缘
- context packing 保留了 leaf evidence，却丢掉了上位容器

## Investigation Order

1. 检查被引用的证据是否依赖 parent section 或更大的 enclosing system
2. 检查 heading path metadata 是否在 ingestion 和 retrieval 过程中幸存
3. 在升级到更复杂 orchestration 之前，先保住 hierarchy

## Common False Diagnoses

- 上游已经把 context 丢掉了，却去怪基础模型
- 误以为增加 semantic similarity 就能恢复丢失的 hierarchy

## Related Pages

- [Section-Aware Chunking](../patterns/section-aware-chunking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- `14-rag-failures` 里的 hierarchy taxonomy
