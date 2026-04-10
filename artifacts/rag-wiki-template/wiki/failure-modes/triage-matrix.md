# Failure Triage Matrix

## Summary

Use this page to move from vague symptom language to the smallest diagnostic class that explains the failure.

## Triage Matrix

### Evidence Composition

- pages: [Multi-Hop Reasoning Gap](multi-hop-reasoning-gap.md), [Scattered Evidence Cutoff](scattered-evidence-cutoff.md), [Aggregation And Counting](aggregation-and-counting.md), [Intersection Blindness](intersection-blindness.md), [Causal Synthesis Failure](causal-synthesis-failure.md)
- common signals: partial facts appear in traces, but the answer never composes them; relevant evidence is spread across many chunks; totals or causal constraints are wrong even when local evidence looks decent
- first checks: inspect candidate coverage before architecture changes; review top-k cutoff and packing; test whether deterministic aggregation or structured decomposition resolves the miss

### Semantic Precision

- pages: [Entity Ambiguity](entity-ambiguity.md), [Synonymy And Jargon Gap](synonymy-and-jargon-gap.md), [Implicit Hallucination](implicit-hallucination.md), [Negation And Absence](negation-and-absence.md)
- common signals: the answer uses the wrong entity, misses domain aliases, invents unsupported relationships, or fails on exclusion-style queries
- first checks: inspect metadata for entity type or namespace; add alias coverage tests; separate unsupported synthesis from retrieval misses; add targeted negation cases to evaluation

### Structural Reasoning

- pages: [Hierarchy Loss](hierarchy-loss.md), [Directionality Confusion](directionality-confusion.md), [Centrality Vs Title Bias](centrality-vs-title-bias.md)
- common signals: chunks look individually relevant but lose parent context, reverse who-did-what, or overweight obvious titles over actual bottlenecks
- first checks: verify section and parent context in chunks; inspect whether relations preserve direction; test reranking or metadata that encodes structure before reaching for graph machinery

### Temporal Truth

- pages: [Contradictory Facts And Recency](contradictory-facts-and-recency.md), [Temporal Sequence Breakdown](temporal-sequence-breakdown.md)
- common signals: old and new truth states are blended, the answer cites the wrong version, or process steps are returned in the wrong order
- first checks: inspect timestamps and version metadata; check whether retrieval or ranking preserves recency and policy precedence; add timeline-sensitive hard cases before redesigning the stack

## Escalation Guardrails

- upgrade to graph or agentic workflows only after you can show that simpler chunking, metadata, reranking, or packing fixes are insufficient
- prefer new evaluations and traces before new infrastructure
- when a failure spans multiple classes, diagnose the lowest-level break first: coverage before reasoning, reasoning before orchestration

## Related Pages

- [Failure Modes](README.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` taxonomy
- `production-grade-agentic-system` evaluation and observability themes
