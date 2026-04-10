# Temporal Sequence Breakdown

## Symptom

The system retrieves relevant events but scrambles their order, so the final answer gets the timeline or causal sequence wrong.

## Likely Causes

- ranking is optimized for relevance instead of sequence
- event chain information is not preserved clearly in metadata
- answer assembly does not enforce chronological order

## Investigation Order

1. inspect whether the question fundamentally requires ordered event reasoning
2. check whether the candidate set contained the right events but not in a stable sequence
3. preserve temporal anchors before adding graph or agentic complexity

## Common False Diagnoses

- calling the problem generic hallucination when the issue is ordering
- adding more retrieval breadth without adding temporal organization

## Related Pages

- [Contradictory Facts And Recency](contradictory-facts-and-recency.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` temporal sequence taxonomy
