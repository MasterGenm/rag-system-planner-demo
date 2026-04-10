# Hierarchy Loss

## Symptom

A leaf-level chunk is retrieved, but the answer loses the parent or root context needed to interpret it correctly.

## Likely Causes

- chunking strips heading path or parent hierarchy
- retrieval favors local snippets without structural lineage
- context packing keeps leaf evidence but drops the governing container

## Investigation Order

1. inspect whether the cited evidence depends on a parent section or enclosing system
2. check whether heading path metadata survives ingestion and retrieval
3. preserve hierarchy before moving to more complex orchestration

## Common False Diagnoses

- blaming the base model for missing context that was removed upstream
- assuming more semantic similarity will restore lost hierarchy

## Related Pages

- [Section-Aware Chunking](../patterns/section-aware-chunking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- `14-rag-failures` hierarchy taxonomy
