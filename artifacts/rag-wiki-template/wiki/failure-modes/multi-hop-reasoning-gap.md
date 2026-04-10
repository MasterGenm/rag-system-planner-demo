# Multi-Hop Reasoning Gap

## Symptom

The system retrieves relevant facts, but it fails to connect them into the reasoning chain needed to answer the question.

## Likely Causes

- chunks containing linked facts are retrieved separately and never composed
- top-k retrieval surfaces isolated fragments without a bridge
- the answer layer lacks an explicit way to chain evidence across steps

## Investigation Order

1. verify that the intermediate facts are both present in the candidate pool
2. inspect whether the answer required an `A -> B -> C` chain that was never assembled
3. check whether the system needs structured decomposition before any architecture upgrade discussion

## Common False Diagnoses

- blaming the base model when the missing step is evidence composition
- jumping straight to graph or agentic RAG before confirming candidate coverage

## Related Pages

- [Good Recall, Weak Ranking](good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` multi-hop reasoning taxonomy
