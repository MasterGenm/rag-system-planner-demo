# Support KB RAG Plan

## Problem Summary
Design a bounded RAG baseline.

## Assumptions And Constraints
- Medium corpus
- Daily updates

## Recommended Stack
- Python retrieval service
- Section-aware chunks

## Architecture And Data Flow
- Ingest docs
- Index chunks

## Retrieval Design
### Chunking
- Use headings
- Keep anchors
### Citation
#### Anchors
- source title
- section path

## Agent Integration Guidance
Keep orchestration out until branching is proven.

## Evaluation Plan
- Recall@5
- Citation correctness

## Observability Plan
- retrieved chunk ids
- stage latency

## Risks And Tradeoffs
### now
- Missing trace coverage
### later
- Premature agentic workflow

## Phased Rollout Plan
### Phase 0
- Collect hard cases
### Phase 1
- Ship plain retrieval with citations
### Phase 2
- Add reranking if top rank precision is weak
### Phase 5
- Review stale artifacts
