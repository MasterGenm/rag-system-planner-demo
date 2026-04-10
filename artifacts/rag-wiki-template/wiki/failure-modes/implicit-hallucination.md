# Implicit Hallucination

## Symptom

The answer invents a relationship because two entities co-occur nearby, even though no explicit evidence supports the link.

## Likely Causes

- chunks are too broad and invite adjacency-based guessing
- prompts do not force explicit evidence linkage
- evaluation does not penalize unsupported relation inference sharply enough

## Investigation Order

1. identify the exact claim that appears unsupported
2. verify whether any retrieved chunk explicitly states the relation
3. inspect whether the model inferred the relation from mere co-occurrence
4. tighten citation and abstention policy before adding architectural complexity

## Common False Diagnoses

- calling it low recall when the needed relation was never in the corpus
- assuming more retrieval breadth will solve an evidence-policy failure

## Related Pages

- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Support KB Citation Drift](../case-notes/support-kb-citation-drift.md)

## Source Trail

- fareedkhan 14-rag-failures taxonomy
