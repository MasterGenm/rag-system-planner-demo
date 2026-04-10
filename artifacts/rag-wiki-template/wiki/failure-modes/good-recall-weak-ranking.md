# Good Recall, Weak Ranking

## Symptom

Relevant evidence appears in the candidate set, but top-ranked results are weak or poorly aligned to the question.

## Likely Causes

- reranking is missing or weak
- chunk boundaries are too coarse
- metadata is insufficient to separate near-duplicate evidence

## Investigation Order

1. verify the right evidence is present in the candidate pool
2. inspect chunk granularity and citation anchors
3. inspect ranking or reranking behavior
4. only then consider larger architecture changes

## Common False Diagnoses

- blaming embeddings when the candidate set is already good
- escalating to agentic RAG before fixing ranking

## Related Pages

- [Section-Aware Chunking](../patterns/section-aware-chunking.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Developer Docs Auth Ranking Drift](../case-notes/developer-docs-auth-ranking-drift.md)
- [When Not To Use Agentic RAG](../stack-decisions/when-not-to-use-agentic-rag.md)

## Source Trail

- current rag-system-planner diagnosis and retrieval heuristics
- [2026-04-09 RAG QA Logs Corpus Source Extract](../../sources/2026-04-09-rag-qa-logs-corpus-source-extract.md)
