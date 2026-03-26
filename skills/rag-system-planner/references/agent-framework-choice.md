# Agent Framework Choice

Only add an orchestration or agent framework when the task requires tool use, branching workflows, or stateful multi-step behavior that a plain retrieval pipeline cannot handle cleanly.

## First Question

Does the user really need an orchestration or agent framework?

If the system is:

- Retrieve documents
- Produce grounded answers
- Return citations

then a plain RAG pipeline is often enough.

## Escalation Ladder

Escalate complexity in this order, and stop as soon as the simpler layer is enough:

1. Plain retrieval plus grounded answer generation
2. Retrieval upgrades such as better metadata, hybrid retrieval, reranking, or query rewrite
3. Graph retrieval or graph-shaped orchestration when the failure mode is structural or branch-heavy
4. Specialist multi-agent coordination only when distinct roles truly improve the outcome

Do not confuse graph retrieval with graph orchestration.

- Graph retrieval is about structured knowledge access
- Graph orchestration is about structured control flow

Some systems need one but not the other.

## Agentic RAG Enablement Rule

Enable agentic RAG only when most of the following are true:

- the task must be explicitly decomposed into multiple retrieval or reasoning steps
- different steps genuinely need different tools, data sources, or specialist roles
- the workflow has real branch points such as continue, rewrite, route, fallback, abstain, or handoff
- state must accumulate across steps instead of being disposable after one answer
- the product can afford the added latency, cost, and observability burden
- a fixed hard-case set shows that simpler retrieval upgrades are not enough

Do not enable agentic RAG when most of the following are true:

- most queries are still straightforward document QA
- the current baseline retrieval quality is not yet characterized
- the real problem is chunking, metadata, filtering, or reranking rather than workflow complexity
- the proposed agent loop mainly wraps one retrieval path in extra prompts
- there is no trace review, retry cap, or explicit failure policy

When you recommend agentic RAG, name:

- the exact subtask boundaries
- the role or tool boundaries
- the branch conditions
- the loop cap or stop condition
- the evaluation signal that proves the extra control layer earns its cost

## LangChain

Use when:

- You want broad ecosystem integrations
- You need flexible chains, tools, and agent patterns
- The team values a large community and fast prototyping

Tradeoffs:

- Can become abstract quickly
- May invite over-engineering in simple RAG systems

## LangGraph

Use when:

- The workflow has explicit branches such as query routing, query rewrite, web fallback, or human review
- The team needs stateful control over retries, loops, or tool transitions
- You want graph-shaped control flow instead of a single agent loop
- The system must explain why it stayed in the vector store path, rewrote the query, or fell back to the web

Tradeoffs:

- Adds orchestration complexity even when the real bottleneck is still plain retrieval quality
- Looping behaviors need hard stopping criteria and observability, or the system becomes hard to debug
- LLM grading steps can look sophisticated while adding latency and fragile judge behavior

Use it only when you can also name:

- the branch points
- the stopping conditions
- the maximum retry or loop count
- the evaluation signal that proves the graph is better than a simpler pipeline

Do not add graph orchestration just to make a RAG demo look advanced.

Query routing, rewrite nodes, web fallback, and grading loops are justified only when a plain retrieval pipeline has already shown a concrete weakness that these branches address.

## LlamaIndex

Use when:

- Document ingestion and retrieval are central
- The team wants a RAG-focused abstraction layer
- You want indexing and query workflows to be first-class concepts

Tradeoffs:

- Less ideal if the system is mostly about agent orchestration beyond retrieval

## CrewAI

Use when:

- The design truly requires role-based multi-agent coordination
- You need explicit agent responsibility boundaries
- The workflow is more than retrieval plus answer generation

Tradeoffs:

- Too much complexity for many RAG products
- Adds more moving parts to observe and debug

## Grading Loops And Self-Critique

Treat LLM grading loops as an optional control layer, not as the default shape of a RAG system.

They are most justified when:

- you need explicit groundedness checks before returning an answer
- the workflow must decide between "retry retrieval", "rewrite the query", and "abstain"
- the system is high risk enough that extra latency is acceptable

They are often not justified when:

- the retrieval baseline is still obviously weak
- the corpus is small and a simpler abstention rule would suffice
- the team cannot inspect traces or compare loop-on versus loop-off behavior

If you add grading loops, require:

- bounded retries
- clear loop exit conditions
- a written fallback path
- separate evaluation for retrieval quality versus judge quality

## Retrieval Supervisors And Policy Agents

Treat retrieval supervisors, policy agents, and reflective controllers as optional control layers, not as the default identity of a RAG system.

They are most justified when:

- the workflow must choose between vector, keyword, hybrid, graph, or web paths
- there are explicit continuation decisions such as continue research, revise the plan, or stop
- the team can point to fixed hard cases that a simpler pipeline misses

They are often not justified when:

- one strong retrieval path already handles most queries
- the policy layer mostly wraps the same retrieval call in extra prompts
- the project lacks trace review, loop caps, or scenario-based evaluation

If you recommend a supervisor layer, require:

- explicit branch criteria
- maximum iteration count
- a degraded-mode path when the controller fails
- separate measurement of controller benefit versus controller overhead

## Recommendation Pattern

- No agent framework for straightforward grounded Q&A
- `LlamaIndex` when document-centric RAG dominates
- `LangChain` when tool calling and broad orchestration dominate
- `LangGraph` when graph-shaped routing, rewrite, fallback, or bounded grading loops are a real requirement
- `CrewAI` only when multi-agent coordination is part of the core product

When a user asks for "agentic RAG", decompose that request into:

- retrieval complexity
- workflow branching complexity
- safety and fallback requirements
- evaluation burden introduced by the extra control loop

Do not recommend a fully agentic path unless those burdens are justified by the task.
