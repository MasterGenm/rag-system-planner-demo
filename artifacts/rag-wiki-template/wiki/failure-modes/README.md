# Failure Modes

Use this folder for recurring RAG failure classes and their investigation order.

## How To Use This Section

- start here when the symptom is still fuzzy
- identify the closest failure class before recommending bigger architecture changes
- use [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md) to separate retrieval, ranking, generation, and observability issues
- link durable case evidence into the relevant failure page instead of repeating the same diagnosis in chat
- use [Failure Triage Matrix](triage-matrix.md) when you need a fast mapping from symptom to likely checks and bounded-complexity fixes

## Investigation Flow

1. Start with [Good Recall, Weak Ranking](good-recall-weak-ranking.md) if you suspect evidence exists but is not being surfaced well.
2. Move into `Evidence Composition` or `Semantic Precision` before proposing graph or agentic changes.
3. Escalate into `Structural Reasoning` only after you have checked chunking, aliases, ranking, and candidate coverage.
4. Treat `Temporal Truth` as its own class of failure. Stale or mixed-truth answers are not fixed by "more retrieval" alone.
5. Use [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md) as a guardrail before adding orchestration.

## Cross-Cutting

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

## Practical Starting Points

- begin with [Scattered Evidence Cutoff](scattered-evidence-cutoff.md) when details are split across too many chunks or top-k feels too thin
- begin with [Entity Ambiguity](entity-ambiguity.md) or [Synonymy And Jargon Gap](synonymy-and-jargon-gap.md) when naming mismatches dominate
- begin with [Contradictory Facts And Recency](contradictory-facts-and-recency.md) or [Temporal Sequence Breakdown](temporal-sequence-breakdown.md) when freshness, precedence, or ordering matter
- begin with [Hierarchy Loss](hierarchy-loss.md) when retrieved chunks feel locally correct but globally misframed

## Guardrails

- do not jump to graph or agentic RAG before ruling out coverage, ranking, metadata, and packing failures
- treat unsupported relationships as [Implicit Hallucination](implicit-hallucination.md) until you can show missing evidence instead of imagined evidence
- prefer updating one canonical page per failure class instead of creating near-duplicates
