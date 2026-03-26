# Diagnosis Playbook

Use this file first in diagnosis mode. Start from symptoms, then narrow the problem area before suggesting fixes.

## Evidence Labels

Label statements explicitly:

- `observed`: supported by the user's description or available traces
- `inferred`: plausible interpretation, but not yet proven
- `unknown`: cannot be claimed until more evidence is collected

Do not treat a missing trace as proof of a component failure.

## Symptom To Cause Map

### Low Recall

Likely causes:

- Weak embeddings
- Bad chunk size or boundaries
- Missing metadata
- Missing hybrid retrieval
- Poor query rewriting
- Wrong filters

### High Hallucination Rate

Likely causes:

- Retrieval returns weak or irrelevant evidence
- Prompt does not force grounded answering
- Citation assembly is broken
- The system answers when it should abstain

### High Latency

Likely causes:

- Overly complex retrieval stack
- Large reranking stage
- Slow vector storage operations
- Excessive agent loops
- Missing caching

### Good Retrieval But Weak Answers

Likely causes:

- Prompt assembly issues
- Context packing issues
- Generation model is too weak for the task
- Citations or evidence are not exposed clearly to the generator

### Hard To Debug

Likely causes:

- Missing traces
- Missing retrieval logs
- No evaluation baseline
- No stage-level latency breakdown

## Investigation Order

1. Confirm the symptom with an example
2. Label what is observed, inferred, and unknown
3. Check whether the failure is retrieval or generation
4. Check whether the system logs enough evidence
5. Review chunking, metadata, filters, and top-k behavior
6. Review embeddings and vector storage choices
7. Review reranking and prompt assembly
8. Review evaluation coverage
9. Consider architecture upgrades only after the simpler layers are evidence-limited

## Default Triage Ladder

When the failure mode is not yet clear, use this default sequence:

1. Symptom confirmation
2. Evidence sufficiency
3. Retrieval baseline review
4. Embedding or vector-store review
5. Reranking and prompt review
6. Architecture upgrade discussion

## Remediation Pattern

Recommend changes in priority order:

1. Instrumentation gaps
2. Retrieval baseline fixes
3. Ranking and reranking fixes
4. Prompt and answer policy fixes
5. Architecture upgrades

Do not start with the most complex redesign unless the baseline is clearly exhausted.

## Actionability Pattern

Structure remediation as:

- `Now`: reversible changes or evidence-restoring actions with the highest information gain
- `Next`: targeted improvements once the evidence path is visible
- `Later`: expensive redesigns or architecture changes that require confirmed bottlenecks

For each action, state:

1. the symptom it targets
2. the expected signal or metric change
3. what would falsify the hypothesis

## When To Stop Speculating

Pause root-cause claims and prioritize instrumentation when:

- only final answers are logged
- retrieved chunk ids or scores are missing
- stage-level timings are unavailable
- the system mixes text, scans, or images but modality-specific traces are missing
