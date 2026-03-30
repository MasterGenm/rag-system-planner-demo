# RAG System Planner Productized Shell Design

Goal: turn `rag-system-planner` from a strong skill repo into a more legible, installable, and showable product package without changing its core theme or replacing its planning logic.

Scope:
- keep the project as a bounded-complexity RAG planner
- do not add finance features or unrelated capabilities
- do not overwrite the original root `README.md` or original skill files
- create a separate packaging layer inside the repo

Current strengths:
- clear problem framing around premature complexity in RAG
- strong `greenfield` and `diagnosis` workflows, plus lightweight comparison mode
- high-quality references for retrieval, eval, observability, vector store choice, and diagnosis
- explicit output contracts for both planning and diagnosis
- existing renderers that already create deliverable Markdown artifacts

Current product-shell gaps:
- weak first-screen value communication
- no front-loaded examples of outputs
- no explicit "what should I ask this?" prompt surface
- installation is complete but not conversion-oriented
- symptom-to-reference routing exists implicitly, not as a fast navigation asset

Approaches considered:

1. In-place rewrite of the current repo surface
- Pros: single source of truth, simplest repo shape
- Cons: violates the user's preference to avoid overwriting the existing project surface

2. Parallel productized wrapper inside the same repo
- Pros: preserves the original project, creates a showcase-ready shell, easy to compare old vs new packaging
- Cons: duplicates some packaging-facing files and needs a distribution snapshot

3. Separate new repo folder with a full copied fork
- Pros: maximal separation
- Cons: heavier duplication and weaker linkage to the original implementation

Recommended approach: 2.

Implementation design:
- Add `productized-shell/` as a self-contained packaging layer
- Put the new product homepage in `productized-shell/README.md`
- Add `examples/` with structured sample inputs and rendered Markdown outputs
- Add `docs/` for trigger navigation and installation/integration guidance
- Add `distribution/` as a ready-to-copy bundle of the current skill plus adapter files
- Keep the original root README and original skill untouched

Success criteria:
- a new visitor can understand the value proposition in under 10 seconds
- a new visitor can see example prompts and example outputs without reading the skill internals
- a new visitor can find the right mode from symptoms or task type
- a new visitor can install the skill into a target agent with one clear path first, then platform-specific variants
- the packaging still presents the project as a bounded-complexity RAG planner rather than a general RAG toolkit
