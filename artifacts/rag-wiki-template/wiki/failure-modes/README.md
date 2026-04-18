# Failure Modes

这个目录用于保存重复出现的 RAG failure 类别，以及它们的调查顺序。

## 怎么使用这一节

- 当症状还比较模糊时，从这里开始
- 在建议更大的架构改动之前，先锁定最接近的 failure class
- 用 [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md) 区分 retrieval、ranking、generation 和 observability 问题
- 把 durable 的 case evidence 链接到对应 failure 页面，而不是反复在聊天里重复同一份 diagnosis
- 当你需要把症状快速映射到可能检查项和 bounded-complexity 修复动作时，使用 [Failure Triage Matrix](triage-matrix.md)

## 调查流

1. 如果你怀疑证据其实存在、只是没被正确抬出来，就从 [Good Recall, Weak Ranking](good-recall-weak-ranking.md) 开始。
2. 在提议 graph 或 agentic 方案之前，先在 `Evidence Composition` 或 `Semantic Precision` 里缩小范围。
3. 只有在已经检查过 chunking、别名、ranking 和 candidate coverage 之后，才升级到 `Structural Reasoning`。
4. 把 `Temporal Truth` 当成独立 failure 类。过时或混合 truth 的答案，不能靠“多做一点 retrieval”直接修好。
5. 在增加 orchestration 之前，用 [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md) 作为 guardrail。

## 跨类问题

- [Good Recall, Weak Ranking](good-recall-weak-ranking.md)

## Evidence Composition

- [Multi-Hop Reasoning Gap](multi-hop-reasoning-gap.md)
- [Scattered Evidence Cutoff](scattered-evidence-cutoff.md)
- [Aggregation And Counting](aggregation-and-counting.md)
- [Intersection Blindness](intersection-blindness.md)
- [Causal Synthesis Failure](causal-synthesis-failure.md)

## Semantic Precision

- [Entity Ambiguity](entity-ambiguity.md)
- [Synonymy And Jargon Gap](synonymy-and-jargon-gap.md)
- [Implicit Hallucination](implicit-hallucination.md)
- [Negation And Absence](negation-and-absence.md)

## Structural Reasoning

- [Hierarchy Loss](hierarchy-loss.md)
- [Directionality Confusion](directionality-confusion.md)
- [Centrality Vs Title Bias](centrality-vs-title-bias.md)

## Temporal Truth

- [Contradictory Facts And Recency](contradictory-facts-and-recency.md)
- [Temporal Sequence Breakdown](temporal-sequence-breakdown.md)

## 实用起点

- 当细节分散在太多 chunks 里，或 top-k 看起来太薄时，从 [Scattered Evidence Cutoff](scattered-evidence-cutoff.md) 开始
- 当命名不一致占主导时，从 [Entity Ambiguity](entity-ambiguity.md) 或 [Synonymy And Jargon Gap](synonymy-and-jargon-gap.md) 开始
- 当 freshness、优先级或顺序很重要时，从 [Contradictory Facts And Recency](contradictory-facts-and-recency.md) 或 [Temporal Sequence Breakdown](temporal-sequence-breakdown.md) 开始
- 当 retrieved chunks 局部正确、但整体语境错位时，从 [Hierarchy Loss](hierarchy-loss.md) 开始

## Guardrails

- 在排除 coverage、ranking、metadata 和 packing failure 之前，不要直接跳到 graph 或 agentic RAG
- 在你能证明是缺证据、而不是凭空想象之前，把 unsupported relationship 当成 [Implicit Hallucination](implicit-hallucination.md)
- 每一类 failure 优先维护一页 canonical page，而不是建一堆近似重复页
