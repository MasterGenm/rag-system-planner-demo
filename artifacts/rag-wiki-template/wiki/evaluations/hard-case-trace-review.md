# Hard-Case And Trace Review

## Purpose

Pair hard-case evaluation with trace review so teams can tell whether a failure came from retrieval, ranking, generation, or missing observability.

## Evaluation Dimensions

- citation correctness
- evidence grounding
- answer correctness
- context recall
- abstention behavior
- stage-level latency

## Trace Signals To Capture

- retrieved chunk ids
- retrieval scores
- applied filters
- reranker decisions
- citation anchors
- retrieval latency
- generation latency
- total latency

## Hard-Case Types

- multi-hop evidence
- scattered evidence across many chunks
- negation and absence
- temporal ordering
- citation drift despite good candidate recall
- comparison questions where one side of the evidence is missing from retrieval

## Review Questions

- was the right evidence present in the candidate pool?
- did ranking surface the right evidence?
- did the answer cite the correct span or only a nearby one?
- did missing traces block diagnosis?

## Related Pages

- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)
- [Scattered Evidence Cutoff](../failure-modes/scattered-evidence-cutoff.md)
- [Support KB Citation Drift](../case-notes/support-kb-citation-drift.md)

## Source Trail

- eval and telemetry ideas drawn from local reference projects
