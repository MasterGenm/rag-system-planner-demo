# Evaluation Design

Define evaluation before claiming a RAG system works. Use both retrieval and answer-level checks.

## Offline Evaluation

### Retrieval Metrics

Use when you can create labeled query-document pairs.

Common metrics:

- Recall@k
- MRR
- nDCG
- Hit rate

### Answer Metrics

Use when answers are the product surface.

Check:

- Groundedness
- Citation correctness
- Completeness
- Conciseness
- Task success for workflow-specific outputs

## Judge-Based Evaluation

Use LLM-as-a-judge for local pairwise comparisons, workflow-quality checks, or trace reviews, but do not let judge scores become the only proof that a system works.

Pair judge-based evaluation with at least one of:

- labeled retrieval slices
- fixed gold answers
- manual audit of a representative subset
- business-facing success checks when the system is already deployed

Keep the judge stable while comparing variants:

- same judge model
- same scoring prompt
- same candidate set or trace slice

Do not claim production readiness from notebook-local judge scores alone.

## Agentic And Graph Evaluation

If the system adds routing, rewrite loops, fallback tools, graph traversal, or multi-agent control, evaluate more than final-answer quality.

Check:

- routing correctness
- tool selection correctness
- retry and loop termination behavior
- fallback rate and abstention behavior
- latency and cost overhead per extra control layer
- graph-specific success on multi-hop, hierarchy, temporal, or negation cases when graph retrieval is used

## Tutorial-Bias And Single-Case Bias

Do not let a dramatic notebook walkthrough or a single hard query become the main proof that a system works.

One impressive case can be useful for demos, but it is not enough for architecture claims.

Require at least:

- a small fixed scenario set rather than one hero query
- a stable baseline to compare against
- repeated runs or manual audit when stochastic components matter
- explicit statement of what the showcased case does not prove

## Dataset Design

Create a small but representative evaluation set before over-optimizing architecture.

Include:

- Easy cases
- Ambiguous cases
- Long-tail domain cases
- Failure-prone cases
- Multilingual or multimodal cases if relevant

## Online Evaluation

Track:

- User success or abandonment
- Citation usage
- Follow-up question rate
- Latency percentiles
- Regeneration or retry rate

## Common Mistakes

- Measuring answer quality without measuring retrieval quality
- Using only synthetic evaluation data
- Ignoring hard negative examples
- Changing embeddings or chunking without re-baselining
- Treating LLM-as-a-judge traces as a substitute for retrieval ground truth
- Adding agentic branches without measuring whether the branch improved anything

## Recommendation Pattern

For every architecture recommendation, include:

1. What must be measured offline
2. What must be observed online
3. What threshold would justify iteration
