# Support KB Diagnostic

## Symptom Summary
- Answers miss precise citation
- Latency increased

## Working Hypotheses
### observed
- Relevant chunks appear after rank 5
### inferred
- Ranking drift
### unknown
- Embedding weakness

## Missing Evidence
- Stage timings

## Investigation Order
- Audit first relevant rank
- Inspect citation anchors

## Recommended Changes
### now
- Add retrieval traces
### next
- Test reranking
### later
- Consider graph only after baseline fixes fail

## Evaluation Additions
- First relevant rank
- Citation correctness

## Observability Additions
- chunk ids
- scores

## Risks And Expected Impact
### now
- Overfitting to one trace
### later
#### Escalation
- Unjustified agentic workflow
