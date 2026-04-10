# Sample Decision Memo

## Decision Context

The team wants to move from plain retrieval to agentic RAG because answers are often weak.

## Options Compared

- improve chunking and metadata
- add reranking
- add agentic orchestration

## Recommendation

Improve chunking and metadata first, then test reranking before discussing agentic orchestration.

## Why This Fits

The system lacks retrieval traces and a hard-case evaluation set, so jumping to agentic behavior would add complexity before the baseline is evidence-limited.

## What Would Change The Decision

The decision would change if retrieval and ranking were already instrumented, tuned, and still inadequate for real branching workflows.
