# Contradictory Facts And Recency

## Symptom

The system retrieves conflicting facts from different times or versions and fails to resolve which one should govern the answer.

## Likely Causes

- timestamps or version metadata are missing or underused
- ranking does not account for recency or policy precedence
- old and new evidence are treated as equal truth candidates

## Investigation Order

1. inspect whether contradictory evidence is coming from different time periods or versions
2. verify whether the retriever and ranker preserve recency or policy priority
3. separate version resolution from generic retrieval quality before redesigning the stack

## Common False Diagnoses

- assuming the model is hallucinating when it is actually averaging conflicting truth states
- adding more retrieval when the issue is time-aware resolution

## Related Pages

- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` contradictory facts and latest-truth taxonomy
