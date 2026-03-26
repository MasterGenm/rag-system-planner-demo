# Retrieval Design

Design retrieval before choosing an orchestration framework. Many poor RAG systems fail because they start with framework plumbing instead of retrieval quality.

## Chunking

Choose chunking based on document structure, not arbitrary token counts.

### Good Defaults

- Preserve section boundaries when possible
- Keep metadata attached to every chunk
- Use overlap only when it improves context continuity

### When To Use Smaller Chunks

- Fact lookup
- Dense technical documentation
- Narrow question spans

### When To Use Larger Chunks

- Narrative documents
- Legal or policy text where context spans paragraphs
- Summarization-oriented retrieval

### Section-Aware Defaults

For structured docs, split by section first and by paragraph second.

Prefer:

- document title plus heading path as a prefix
- moderate chunk sizes that preserve local reasoning
- section or page anchors that keep citations inspectable

Do not assume smaller is always better. Over-splitting can destroy explanatory context, especially in issue threads or long-form technical docs.

For issue-like corpora:

- keep the issue title as a strong prefix
- split the body by paragraph groups or subsections
- avoid shredding the debugging narrative into tiny fragments

## Metadata

Always design metadata early if you need:

- Source citations
- Time filtering
- Tenant isolation
- Document type filtering
- Version awareness

Poor metadata often looks like poor retrieval.

## Retrieval Strategy

Start with a simple baseline:

1. Dense retrieval
2. Metadata filtering where relevant
3. Top-k retrieval

Add complexity only if the baseline fails:

- Hybrid retrieval for keyword-sensitive queries
- Query rewriting for vague user input
- Multi-query retrieval when recall is the main problem
- Reranking when the initial candidate set is noisy
- Parent-child retrieval when passages need larger source context

For each added layer, say:

- why the baseline is not enough
- what the extra layer improves
- what it costs in latency, complexity, or operations
- what you are deliberately not adding yet

## Adaptive Retrieval Funnels

Use an adaptive multi-stage retrieval funnel only when query families genuinely need different retrieval behavior.

Good signals include:

- conversational or referential queries that need standalone rewrite
- semantic gaps where HyDE or a hypothetical answer can improve first-stage recall
- mixed query families where some requests are keyword-heavy, some semantic, and some need hybrid retrieval
- high-value questions where broad recall followed by reranking and light distillation materially improves answer quality

Treat this as a bounded retrieval upgrade, not as an excuse to introduce a large agentic workflow by default.

If you recommend an adaptive funnel, state:

- which query families trigger rewrite, HyDE, keyword, dense, or hybrid paths
- what the default path is when no special trigger fires
- what is logged at each stage so failures remain debuggable
- what latency and cost overhead each extra stage adds
- what fixed retrieval slice or hard-case set proves the funnel is better than a simpler baseline

Do not add a retrieval supervisor or HyDE first when:

- the corpus is small and the failure mode is not yet characterized
- baseline dense or hybrid retrieval has not been measured
- the team cannot explain which questions should bypass the extra stage
- the extra layer only makes a demo look more sophisticated without a clear retrieval gain

## Reranking

Treat reranking as a ranking fix, not a recall fix.

Add reranking when:

- The right evidence already appears in the candidate pool, but the top few results are misordered
- Recall is acceptable but top-rank precision is weak
- The top results are related but not precise enough for fact-heavy questions or citations
- The query is fine-grained and multiple candidate chunks share the same broad topic

Do not add reranking yet when:

- Relevant evidence is missing from the candidate pool entirely
- Chunking, metadata, filters, or query formulation are still clearly broken
- The corpus is tiny and baseline retrieval is already precise enough
- Latency budget is so tight that a second-stage model is hard to justify

Use the standard two-stage pattern:

1. First-stage retrieval to gather a candidate set
2. Second-stage reranking over only the top-N candidates

Cross-encoders fit naturally in the second stage because they are usually too expensive for full-corpus retrieval.

When planning reranking, state:

- how you will confirm that candidate recall is already good enough
- how many candidates enter the reranker
- what latency budget the reranker consumes
- what metric should improve if the reranker is working

Input shaping matters. Do not feed only naked chunk text when structure carries meaning.

Prefer prefixes such as:

- section or chapter titles
- document path or source title
- page anchors or subsection ids

These often help the reranker separate "same topic" chunks from the chunk that answers the exact question.

## Chunking Versus Reranking

Use this decision rule:

- If relevant evidence is missing from the candidate pool, inspect chunking, metadata, filters, and retrieval strategy first.
- If relevant evidence is already present in the candidate pool but misordered, inspect reranking first.
- If retrieved chunks are broadly relevant but too coarse to answer precise questions, use section-aware chunking before reaching for larger architecture changes.
- If the chunks are good and well-ranked but the answer is still weak, inspect prompt assembly or generation instead.

Do not use reranking as a substitute for obviously broken chunking, and do not rewrite chunking first when the real problem is ranking precision.

## Graph RAG And Structural Retrieval

Consider graph-structured retrieval only when the problem is structurally hard, not merely semantically fuzzy.

Good signals include:

- multi-hop chains where intermediate entities must be traversed explicitly
- hierarchy or parent-child lineage questions
- directionality-sensitive queries such as ownership or dependency arrows
- temporal latest-truth questions where ordering matters more than similarity
- common-neighbor or intersection queries
- negation, absence, or set-difference questions
- influence, bottleneck, or centrality questions over a network

Do not jump to Graph RAG when:

- the task is still mostly citation-heavy document QA
- dense or hybrid retrieval has not been baselined yet
- graph extraction quality is weak or too expensive to maintain
- the team cannot explain which queries should use traversal instead of plain retrieval

If you recommend Graph RAG, state:

- where entities and relations come from
- how graph extraction or curation will be validated
- which query families route to graph traversal
- what simpler baseline the graph path must beat on fixed hard cases
- what graph-specific failure modes you will observe, such as stale edges or wrong entity resolution

## Web Fallback And External Search

Use external search only when the problem truly needs fresh or out-of-corpus evidence.

Good signals include:

- time-sensitive questions where internal documents are known to be stale
- comparative questions that mix internal knowledge with recent public events
- explicit coverage gaps that the internal corpus cannot reasonably fill

Do not treat web fallback as a substitute for weak internal retrieval. If internal documents should have answered the question, fix the internal path first.

If you add web fallback, state:

- which query families are allowed to leave the corpus
- how external evidence is cited and separated from internal evidence
- what freshness or source-trust rules apply
- what fallback cap or routing rule prevents unnecessary external calls

## Multimodal And Scan-Heavy Corpora

If evidence lives in diagrams, screenshots, scanned pages, or tables, do not force everything into a plain text-only design.

- Keep text chunks, OCR text, and image or region assets distinct when they play different retrieval roles
- Treat OCR confidence as metadata, not as a hidden implementation detail
- Preserve page anchors, section ids, and asset ids so citations stay traceable
- Use a text-only baseline only when visual semantics are not materially required
- If image understanding matters, plan explicit modality routing or parallel retrieval branches

Read `references/multimodal-retrieval.md` when multimodal evidence may change retrieval design.

## Fallback And Abstention

Design for weak-evidence cases:

- what to do when retrieval returns little or no support
- when to abstain instead of forcing an answer
- how to surface low-confidence evidence to the user or downstream workflow

## Generation Boundary

Separate retrieval problems from generation problems:

- Missing evidence in retrieved chunks is a retrieval issue
- Good evidence but poor synthesis is a generation or prompt issue
- Good answer quality but weak citations is often an assembly issue

## Recommendation Pattern

State:

1. Chunking plan
2. Metadata plan
3. Retrieval plan
4. Reranking plan if needed
5. Citation strategy
6. Fallback or abstention strategy if evidence is weak
7. What you are not adding yet and why
