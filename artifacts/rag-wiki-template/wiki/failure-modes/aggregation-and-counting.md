# Aggregation And Counting

## Symptom

The system misses totals, counts, or rollups because evidence is scattered across many chunks or duplicated under different names.

## Likely Causes

- entity normalization is weak
- retrieval returns examples but not the full set needed for counting
- answer assembly is not designed for exact aggregation tasks

## Investigation Order

1. define what exact set must be counted
2. inspect whether retrieved evidence covers the full set or only samples
3. check whether aliases or duplicate entities distort counting
4. decide whether counting should be delegated to a deterministic post-step

## Common False Diagnoses

- assuming the model is bad at reasoning when the pipeline never assembled the full set
- overexpanding retrieval without normalizing duplicate entities

## Related Pages

- [Scattered Evidence Cutoff](scattered-evidence-cutoff.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- fareedkhan 14-rag-failures taxonomy
