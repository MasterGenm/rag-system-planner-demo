# Intersection Blindness

## Symptom

系统能分别取回关于 A 和关于 B 的事实，但看不到来自共同邻居或共享依赖的那条隐藏连接。

## Likely Causes

- retrieval 被限制在直接相似性上，而没有看 relational overlap
- answerer 没有检查 shared intermediate entities
- evidence review 太局部，漏掉了 cross-candidate intersection

## Investigation Order

1. 检查这个问题是否依赖 shared intermediate node 或 concept
2. 核验双方证据是否其实都在，但从未被 intersect 起来
3. 在跳到完整 graph stack 之前，先加入 intersection-style reasoning

## Common False Diagnoses

- 证据其实存在、只是没被 join，却误以为 corpus 缺证据
- 不测试更小的 compositional fixes，就直接跳到 graph RAG

## Related Pages

- [Multi-Hop Reasoning Gap](multi-hop-reasoning-gap.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` 里的 intersection taxonomy
