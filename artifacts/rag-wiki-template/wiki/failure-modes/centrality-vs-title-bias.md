# Centrality Vs Title Bias

## Symptom

The system identifies the most obvious or highest-status actor instead of the most important connector, influencer, or bottleneck in the actual evidence network.

## Likely Causes

- answering overweights surface titles or prominence words
- there is no mechanism to inspect relationship topology
- retrieval is local to descriptions and misses communication or dependency structure

## Investigation Order

1. inspect whether the answer chose the highest title rather than the true bridge node
2. verify whether the evidence needed topology-aware analysis rather than title matching
3. test smaller structural features before discussing a full graph upgrade

## Common False Diagnoses

- treating a topology problem as a generic ranking problem
- defaulting to agentic or graph systems without first confirming the task type

## Related Pages

- [Intersection Blindness](intersection-blindness.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- `14-rag-failures` centrality taxonomy
