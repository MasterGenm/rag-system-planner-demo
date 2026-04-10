# Directionality Confusion

## Symptom

The system confuses directional relationships, such as ownership, dependency, caller-callee, or parent-child.

## Likely Causes

- embeddings collapse directional relations into symmetric similarity
- chunk text does not emphasize relation direction strongly enough
- prompts over-trust semantically similar but directionally inverted evidence

## Investigation Order

1. identify the exact directional claim that matters
2. inspect whether retrieved evidence preserves who did what to whom
3. check whether metadata or schema can encode direction explicitly
4. only then consider heavier graph representations

## Common False Diagnoses

- calling it a generic retrieval problem when the real issue is directional semantics
- trying bigger models before clarifying relation encoding

## Related Pages

- [Hierarchy Loss](hierarchy-loss.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- fareedkhan 14-rag-failures taxonomy
