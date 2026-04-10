# Architecture Comparison Scattered Evidence Diagnostic

## Question

Why does the Chroma-versus-Qdrant architecture comparison keep collapsing into one-sided evidence?

## Short Answer

This case is closer to scattered-evidence cutoff than to a simple ranking issue. The answer needs evidence from both Chroma and Qdrant, but the retrieved set stays concentrated in the Chroma neighborhood. The next move is to test evidence-breadth strategies such as query decomposition, source-family coverage checks, and broader neighborhood expansion before discussing a more complex architecture.

## Evidence

- [2026-04-09 Open Support Copilot Retrieval Eval Extract](../sources/2026-04-09-open-support-copilot-retrieval-eval-extract.md)
- [Architecture Comparison Evidence Collapse](../wiki/case-notes/architecture-comparison-evidence-collapse.md)
- [Scattered Evidence Cutoff](../wiki/failure-modes/scattered-evidence-cutoff.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Follow-ups

- add comparison-side coverage checks to retrieval evaluation
- test decomposed retrieval like `Chroma filtering` plus `Qdrant filtering` before final synthesis
- compare product-family metadata filtering against plain semantic retrieval
- require the answer layer to abstain or qualify when one side of a comparison is missing
