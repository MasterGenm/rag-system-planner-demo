# Implicit Hallucination

## Symptom

答案因为两个实体在附近共同出现，就凭空发明了一段关系，尽管没有任何显式证据支持这条链接。

## Likely Causes

- chunks 太宽，诱发了基于相邻共现的猜测
- prompts 没有强制显式 evidence linkage
- evaluation 对 unsupported relation inference 的惩罚不够强

## Investigation Order

1. 识别那条看起来 unsupported 的精确 claim
2. 核验是否有任何 retrieved chunk 明确写出了这段关系
3. 检查模型是否只是从共现关系里自行推断了连接
4. 在增加架构复杂度之前，先收紧 citation 和 abstention policy

## Common False Diagnoses

- 需要的关系压根不在 corpus 里，却误判成 low recall
- evidence-policy failure 却被误以为可以靠更多 retrieval breadth 修好

## Related Pages

- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Support KB Citation Drift](../case-notes/support-kb-citation-drift.md)

## Source Trail

- fareedkhan `14-rag-failures` taxonomy
