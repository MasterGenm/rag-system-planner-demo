# 2026-04-09 Open Support Copilot Retrieval Eval Extract

## Dataset

- local project: `E:\dt\open-support-copilot`
- evaluation slice: `tests/retrieval_eval`
- purpose: use a labeled retrieval audit as a real scattered-evidence demo for `rag-system-planner-v2-lab`

## Relevant Files

- `E:\dt\open-support-copilot\tests\retrieval_eval\README.md`
- `E:\dt\open-support-copilot\tests\retrieval_eval\gold_set.v1.json`
- `E:\dt\open-support-copilot\tests\retrieval_eval\results\chroma-retrieval-eval.md`
- `E:\dt\open-support-copilot\tests\retrieval_eval\results\qdrant-retrieval-eval.md`
- `E:\dt\open-support-copilot\tests\retrieval_eval\results\chroma-retrieval-eval.json`
- `E:\dt\open-support-copilot\tests\retrieval_eval\results\qdrant-retrieval-eval.json`

## Selected Walkthrough Example

- `id`: `architecture-01`
- question: `Should a support copilot over framework docs and GitHub issues stay on Chroma or move to Qdrant as filtering needs and update frequency grow?`
- why this case matters: the gold answer explicitly requires evidence from both sides of the comparison

## Gold Evidence

```text
https://docs.trychroma.com/reference/where-filter
https://docs.trychroma.com/docs/querying-collections/metadata-filtering
https://qdrant.tech/documentation/concepts/filtering/
https://qdrant.tech/documentation/faq/qdrant-fundamentals/
```

## Chroma Retrieval Summary

- `Recall@5 = 0.5000`
- matched URLs:
  - `https://docs.trychroma.com/reference/where-filter`
  - `https://docs.trychroma.com/docs/querying-collections/metadata-filtering`
- missing from top 5:
  - `https://qdrant.tech/documentation/concepts/filtering/`
  - `https://qdrant.tech/documentation/faq/qdrant-fundamentals/`

Top retrieved URLs:

```text
1. https://docs.trychroma.com/reference/overview
2. https://docs.trychroma.com/reference/where-filter
3. https://github.com/chroma-core/chroma/issues/6104
4. https://docs.trychroma.com/docs/querying-collections/metadata-filtering
5. https://docs.trychroma.com/docs/querying-collections/query-and-get
```

## Qdrant Retrieval Summary

- `Recall@5 = 0.2500`
- matched URLs:
  - `https://docs.trychroma.com/reference/where-filter`
- missing from top 5:
  - `https://docs.trychroma.com/docs/querying-collections/metadata-filtering`
  - `https://qdrant.tech/documentation/concepts/filtering/`
  - `https://qdrant.tech/documentation/faq/qdrant-fundamentals/`

Top retrieved URLs visible in the audit:

```text
1. https://docs.trychroma.com/reference/overview
2. https://docs.trychroma.com/reference/where-filter
```

## Initial Read

This is not just a generic bad result. The comparison query requires evidence breadth across two product families, but retrieval collapses around the Chroma side of the neighborhood and never surfaces enough Qdrant evidence to support a balanced answer.

## Related Pages

- [Scattered Evidence Cutoff](../wiki/failure-modes/scattered-evidence-cutoff.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Source Trail

- local retrieval-eval files inspected on 2026-04-09
