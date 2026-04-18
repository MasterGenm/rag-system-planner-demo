# Aggregation And Counting

## Symptom

系统在 totals、counts 或 rollups 上出错，因为证据分散在许多 chunks 里，或者以不同名称重复出现。

## Likely Causes

- entity normalization 偏弱
- retrieval 只返回了示例，而没有收齐计数所需的完整集合
- answer assembly 并不是为精确 aggregation 任务设计的

## Investigation Order

1. 明确定义到底要统计哪一个精确集合
2. 检查 retrieved evidence 覆盖的是完整集合，还是只是一些 sample
3. 检查 aliases 或 duplicate entities 是否扭曲了计数
4. 判断 counting 是否应该委托给一个 deterministic post-step

## Common False Diagnoses

- 在 pipeline 根本没把完整集合拼齐时，就断定模型推理差
- 在不做 duplicate entity normalization 的情况下，盲目扩张 retrieval

## Related Pages

- [Scattered Evidence Cutoff](scattered-evidence-cutoff.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- fareedkhan `14-rag-failures` taxonomy
