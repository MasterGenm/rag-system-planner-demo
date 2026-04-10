# Scattered Evidence Cutoff

## Symptom

The answer depends on many small pieces of evidence, but top-k cutoff or weak context packing leaves some of the crucial pieces out.

## Likely Causes

- top-k is too small for the evidence distribution
- retrieval returns the right topic area but not enough of the neighborhood
- context assembly drops lower-ranked but still necessary chunks

## Investigation Order

1. inspect whether missing evidence sits just below the current cutoff
2. check whether retrieved chunks cover breadth or only local density
3. improve neighborhood expansion or context assembly before discussing graph or agents

## Common False Diagnoses

- calling the whole retriever bad when the main issue is cutoff and packing
- escalating to graph retrieval without measuring how much simple breadth expansion helps

## Related Pages

- [Section-Aware Chunking](../patterns/section-aware-chunking.md)
- [Good Recall, Weak Ranking](good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Architecture Comparison Evidence Collapse](../case-notes/architecture-comparison-evidence-collapse.md)

## Source Trail

- `14-rag-failures` scattered evidence taxonomy
- [2026-04-09 Open Support Copilot Retrieval Eval Extract](../../sources/2026-04-09-open-support-copilot-retrieval-eval-extract.md)
