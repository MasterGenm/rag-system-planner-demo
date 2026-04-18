# Failure Triage Matrix

## Summary

用这页把模糊的 symptom 描述，收敛到能够解释问题的最小 diagnosis 类别。

## Triage Matrix

### Evidence Composition

- pages: [Multi-Hop Reasoning Gap](multi-hop-reasoning-gap.md), [Scattered Evidence Cutoff](scattered-evidence-cutoff.md), [Aggregation And Counting](aggregation-and-counting.md), [Intersection Blindness](intersection-blindness.md), [Causal Synthesis Failure](causal-synthesis-failure.md)
- common signals：traces 里已经出现了局部事实，但答案从未把它们组合起来；相关证据分散在许多 chunks 里；即使局部证据看起来不错，totals 或 causal constraints 仍然错
- first checks：先检查 candidate coverage，再谈架构变化；复盘 top-k cutoff 和 packing；测试 deterministic aggregation 或 structured decomposition 是否能修复这个 miss

### Semantic Precision

- pages: [Entity Ambiguity](entity-ambiguity.md), [Synonymy And Jargon Gap](synonymy-and-jargon-gap.md), [Implicit Hallucination](implicit-hallucination.md), [Negation And Absence](negation-and-absence.md)
- common signals：答案用了错误实体、漏掉了 domain aliases、发明了 unsupported relationships，或者在 exclusion-style queries 上失败
- first checks：检查 metadata 是否包含 entity type 或 namespace；加入 alias coverage tests；把 unsupported synthesis 和 retrieval misses 分开；在 evaluation 里加入定向的 negation cases

### Structural Reasoning

- pages: [Hierarchy Loss](hierarchy-loss.md), [Directionality Confusion](directionality-confusion.md), [Centrality Vs Title Bias](centrality-vs-title-bias.md)
- common signals：chunks 单看都相关，但丢了 parent context、颠倒了 who-did-what，或把显眼 title 看得比真实 bottleneck 更重
- first checks：核验 chunks 是否保留了 section 与 parent context；检查关系是否保留方向；在动 graph machinery 前，先测试能编码结构的 reranking 或 metadata

### Temporal Truth

- pages: [Contradictory Facts And Recency](contradictory-facts-and-recency.md), [Temporal Sequence Breakdown](temporal-sequence-breakdown.md)
- common signals：新旧 truth states 被混合，答案引用了错误版本，或者流程步骤顺序被答反了
- first checks：检查 timestamps 和 version metadata；检查 retrieval 或 ranking 是否保留 recency 与 policy precedence；在重构 stack 前，先加入对 timeline 敏感的 hard cases

## Escalation Guardrails

- 只有当你能证明更简单的 chunking、metadata、reranking 或 packing 修复都不够时，才升级到 graph 或 agentic workflows
- 优先补新的 evaluations 和 traces，而不是先上新基础设施
- 当一个 failure 横跨多个类别时，先诊断最低层的 break：coverage 先于 reasoning，reasoning 先于 orchestration

## Related Pages

- [Failure Modes](README.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` taxonomy
- `production-grade-agentic-system` 里的 evaluation 与 observability 主题
