# Sample Real Walkthroughs

## Purpose

Show that the proposed artifact scaffold is not only a blank template. It already contains two real diagnostic walkthroughs based on external or local evaluation evidence.

## Walkthrough 1: Good Recall, Weak Ranking

Dataset-backed files:

- `artifacts/rag-wiki-template/sources/2026-04-09-rag-qa-logs-corpus-source-extract.md`
- `artifacts/rag-wiki-template/wiki/case-notes/developer-docs-auth-ranking-drift.md`
- `artifacts/rag-wiki-template/queries/developer-docs-auth-ranking-diagnostic.md`

Why it matters:

- the retrieved set contains relevant authentication chunks
- the top-ranked region is dominated by semantically adjacent but less relevant endpoint material
- the failure is closer to ranking drift than missing evidence

## Walkthrough 2: Scattered Evidence

Retrieval-eval-backed files:

- `artifacts/rag-wiki-template/sources/2026-04-09-open-support-copilot-retrieval-eval-extract.md`
- `artifacts/rag-wiki-template/wiki/case-notes/architecture-comparison-evidence-collapse.md`
- `artifacts/rag-wiki-template/queries/architecture-comparison-scattered-evidence-diagnostic.md`

Why it matters:

- the comparison question requires evidence from both Chroma and Qdrant
- retrieval collapses toward one evidence neighborhood instead of covering both sides
- the failure is better explained by evidence breadth and cutoff than by a pure ranking mistake

## Why These Examples Matter

Together they show two different diagnosis paths:

- candidate set is good enough but ranking is weak
- topic match exists but evidence breadth is too narrow for the question type

That makes the scaffold more credible as a real `rag-system-planner` v2 proposal rather than a prompt-only rewrite.
