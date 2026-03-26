# Observability Design

Observability is not optional for diagnosis mode. You cannot reliably improve a RAG system if you cannot see what it retrieved, how long each stage took, and what evidence was available to the model.

## Minimum Signals

Track at least:

- Query text or normalized query form
- Retrieved document or chunk identifiers
- Retrieval scores
- Metadata filters used
- Reranking decisions if present
- Prompt assembly metadata
- Model response latency
- Token usage if relevant
- Returned citations

## Minimum Dashboards

Have visibility into:

- Retrieval latency
- Generation latency
- End-to-end latency
- Empty or low-confidence retrieval rate
- Citation failure rate
- Error rate by stage

## LangSmith Vs Phoenix

### LangSmith

Prefer when:

- The system already uses LangChain heavily
- You want polished tracing and experiment workflows
- Hosted tooling is acceptable

### Phoenix

Prefer when:

- You want an open-source observability option
- You need flexible tracing and evaluations without committing to LangChain
- You want a framework-neutral monitoring story

## Common Gaps

- Logging only the final answer
- Not storing retrieved chunk identifiers
- Not logging filter conditions
- No separation between retrieval and generation latency
- No trace linking bad answers to missing evidence

## Recommendation Pattern

Always specify:

1. What to trace
2. What to aggregate
3. What to alert on
4. Which tool fits the chosen stack
