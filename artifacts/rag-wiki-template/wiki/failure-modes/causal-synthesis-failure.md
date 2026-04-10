# Causal Synthesis Failure

## Symptom

The system repeats positive or descriptive evidence, but misses hidden conflicts, constraints, or causal incompatibilities that change the answer.

## Likely Causes

- retrieval overweights semantic similarity and underweights constraint logic
- the answerer never checks whether the retrieved properties can coexist
- causal or rule-based reasoning is missing from the review step

## Investigation Order

1. inspect whether the answer only summarized surface-positive evidence
2. check whether key constraints or conflict conditions were retrieved but ignored
3. add explicit contradiction or compatibility review before escalating complexity

## Common False Diagnoses

- assuming the retriever failed when the evidence was present but not reconciled
- adding more retrieval stages instead of adding a better synthesis check

## Related Pages

- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Support KB Citation Drift](../case-notes/support-kb-citation-drift.md)

## Source Trail

- `14-rag-failures` causal synthesis taxonomy
