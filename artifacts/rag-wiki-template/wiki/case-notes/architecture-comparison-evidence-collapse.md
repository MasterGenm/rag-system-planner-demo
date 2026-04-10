# Architecture Comparison Evidence Collapse

## Context

Architecture comparison case taken from the `open-support-copilot` retrieval-eval slice.

## Symptom

The comparison answer asks whether a support copilot should stay on Chroma or move to Qdrant, but the retrieved evidence collapses toward the Chroma side and leaves too little Qdrant evidence in view.

## Observed

- gold evidence spans four URLs across both Chroma and Qdrant
- in the Chroma backend audit, `Recall@5 = 0.5000` and both matched URLs are Chroma-side pages
- in the Qdrant backend audit, `Recall@5 = 0.2500` and the visible matched URL is still a Chroma-side page
- neither backend surfaces a balanced top-5 comparison set for the query

## Inferred

- this fits `Scattered Evidence Cutoff` better than a pure ranking miss
- the retriever stays inside one local evidence neighborhood instead of gathering both sides required for a comparative answer
- retrieval breadth and query decomposition matter before any larger architecture change

## Unknown

- whether a decomposed comparison query would recover both Chroma and Qdrant evidence without changing the backend
- whether metadata filters by product or source family would improve breadth
- whether reranking would help once both sides are present

## Durable Lessons

- comparison questions need breadth checks, not just topical relevance checks
- `Recall@k` should be inspected against evidence coverage by comparison side
- architecture answers should fail closed when one side of the comparison is absent from retrieval

## Related Pages

- [Scattered Evidence Cutoff](../failure-modes/scattered-evidence-cutoff.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Section-Aware Chunking](../patterns/section-aware-chunking.md)

## Source Trail

- [2026-04-09 Open Support Copilot Retrieval Eval Extract](../../sources/2026-04-09-open-support-copilot-retrieval-eval-extract.md)
