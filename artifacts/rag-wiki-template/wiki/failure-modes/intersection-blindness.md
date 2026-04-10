# Intersection Blindness

## Symptom

The system can retrieve facts about A and facts about B, but it misses the hidden connection that comes from their common neighbor or shared dependency.

## Likely Causes

- retrieval is limited to direct similarity instead of relational overlap
- the answerer does not test for shared intermediate entities
- evidence review is too local and misses cross-candidate intersection

## Investigation Order

1. inspect whether the question depends on a shared intermediate node or concept
2. verify that evidence for both sides was present but never intersected
3. add intersection-style reasoning before jumping to a full graph stack

## Common False Diagnoses

- assuming the corpus is missing evidence when the evidence is present but not joined
- moving immediately to graph RAG without testing smaller compositional fixes

## Related Pages

- [Multi-Hop Reasoning Gap](multi-hop-reasoning-gap.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- `14-rag-failures` intersection taxonomy
