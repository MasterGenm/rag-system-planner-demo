# When Not To Use Agentic RAG

## Summary

Do not add agentic orchestration when a simpler retrieval pipeline has not yet been proven insufficient.

## Signals That Simpler Fixes Come First

- no retrieval traces
- no hard-case evaluation set
- weak chunking or metadata design
- poor citation behavior that can be explained without orchestration

## What Agentic RAG Buys

- branching workflows
- tool use
- decomposition across steps

## What It Costs

- latency
- debugging complexity
- observability burden
- more failure surfaces

## Related Pages

- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)

## Source Trail

- bounded-complexity principle from rag-system-planner
