# rag-system-planner-demo Productionization Review

## Document Purpose

This document turns the recent repo review into a concrete planning artifact.
It is intended for:

- follow-up review by other AI systems
- mentor or teammate critique
- turning the repo from a methodology-heavy demo into a pre-production Agent Skill project

It is not an implementation log.
It is a decision and prioritization document.

## Project Context

`rag-system-planner-demo` is currently strongest as a knowledge-dense Agent Skill for:

- RAG system planning
- RAG diagnosis
- bounded-complexity architectural decision support
- durable knowledge accumulation through `sources -> wiki -> queries`

Its core value is not that it implements an online RAG runtime.
Its real value is that it encodes expert workflow contracts:

- two-layer model: `planner` and `artifact-maintenance`
- three planning modes: `greenfield`, `diagnosis`, `comparison`
- evidence labeling: `observed`, `inferred`, `unknown`
- structured output contracts
- durable artifact lifecycle

This review is based on local repo inspection plus external production guidance from:

- OpenAI agent evals guidance
- OpenAI's in-house data agent write-up
- Anthropic's agent engineering guidance
- LangSmith evaluation workflow docs
- Arize Phoenix observability and evaluation docs

## Current Diagnosis

### Overall Judgment

The project is already strong as a methodology and workflow-design artifact.
It is still weak as a production-adjacent system.

The main gap is not lack of domain knowledge.
The main gap is lack of a closed loop:

`real input -> stable execution surface -> traces/logs -> evals/regression -> artifact updates -> adoption feedback`

### Current Strengths

- Clear expert workflow contracts in `SKILL.md`
- Strong bounded-complexity philosophy
- Reusable failure taxonomy and triage matrix
- Good artifact model for cross-session knowledge reuse
- Cross-platform packaging awareness
- Seed examples that already resemble case-based diagnosis

### Current Weaknesses

- No real runtime entrypoint
- No automated regression or benchmark harness
- No CI or test discipline
- No telemetry contract for real production diagnosis
- No usage feedback loop
- No freshness or release discipline around durable artifacts

## Evidence From The Repo

### Repo Self-Declared Gaps

The README already states:

- no runtime service or automation integration
- no automated quality evaluation for the skill itself
- no user feedback loop or usage data

It also suggests:

- adding `pytest` tests for renderer outputs
- designing a standard scenario set to validate consistency and decision quality

### Contract-Level Signals

The current `diagnosis` workflow already expects:

- benchmark and dataset discovery
- trace and runtime signal discovery
- `now / next / later` prioritization
- evidence-aware reasoning rather than speculation

The triage matrix also explicitly says:

- do not escalate to graph or agentic workflows before simpler retrieval fixes are disproven
- prioritize new evaluations and traces before new infrastructure

This is important because the repo already contains the right philosophy.
What is missing is operationalization.

## External Production Guidance Alignment

The productionization direction recommended here is aligned with current public guidance:

- OpenAI recommends starting with traces, then moving to datasets and eval runs for repeatability.
- OpenAI's internal data agent uses curated question-answer evals as continuous unit-test-like canaries.
- Anthropic recommends starting simple, measuring thoroughly, and only adding complexity when it demonstrably improves outcomes.
- LangSmith and Phoenix both center the workflow around datasets, evaluators, traces, online monitoring, and feedback loops.

This means the repo should not jump first to heavier orchestration or a polished product shell.
It should first become measurable and replayable.

## Three Productionization Paths

### Path 1: Eval-First Hardening

Turn the current workflow contracts into a benchmarked skill system.

Build:

- a fixed scenario set
- gold or rubric-backed expected behavior
- regression tests across workflow modes
- baseline comparison against a plain prompt without the skill

What gets evaluated:

- workflow mode selection
- correct failure-family classification
- correct use of `observed / inferred / unknown`
- whether the system avoids unjustified escalation
- whether recommendations stay reversible before costly changes

Why this path is strong:

- it directly validates the repo's most valuable asset: judgment quality
- it creates evidence for reliability
- it supports both hiring credibility and team adoption

Main risk:

- requires disciplined rubric design, not just sample collection

### Path 2: Case Library And Knowledge Ops

Turn existing examples and walkthroughs into a structured case library.

Each case should eventually have:

- `case_id`
- source system background
- symptom summary
- expected failure family
- evidence bundle
- attempted fix
- before/after metric or outcome
- reviewer
- artifact promotion state
- freshness metadata

Suggested lifecycle:

`raw -> analyzed -> benchmarked -> canonical -> stale`

Why this path is strong:

- makes the `sources / wiki / queries` model behave like a data flywheel
- creates reusable institutional memory
- supports future benchmark generation

Main risk:

- can become heavy documentation work if not tied to evaluation and adoption

### Path 3: Thin Workflow Product

Build a thin CLI or ChatOps-style wrapper around the current workflow.

Possible surface:

- `plan`
- `diagnose`
- `artifact-maintain`

Expected input:

- incident note
- retrieval trace slice
- eval report slice
- architecture note

Expected output:

- structured JSON
- Markdown memo
- optional artifact handoff payload

Why this path is useful:

- makes the repo actually runnable by teammates
- lowers trial friction

Main risk:

- if done too early, it creates a product-looking shell around unverified heuristics

## Recommended Direction

### Recommendation

Prioritize:

1. `Eval-first hardening`
2. `Case library and knowledge ops`
3. `Thin workflow product`

### Why This Order

The repo's strongest asset is not runtime.
It is the decision protocol.

If the decision protocol is not benchmarked:

- a CLI will only make the demo easier to run
- more examples will only make the repo larger
- more wrappers will not increase trust

The shortest credible bridge from methodology to production is:

`workflow contract -> benchmark -> regression -> case-backed adoption -> thin execution surface`

## Highest-Leverage Changes

### 1. Build Goldens And A Regression Harness

Target outcome:

- prove that the skill does not silently regress

Minimum scope:

- `15-20` stable scenarios
- coverage across `greenfield`, `diagnosis`, and `comparison`
- coverage across the 4 top-level failure families in the triage matrix
- a plain-prompt baseline for comparison

What to score:

- mode choice
- failure-family choice
- evidence-label correctness
- recommended next action quality
- escalation restraint

### 2. Define An Incident Or Evidence Bundle Schema

Target outcome:

- stable machine-consumable input surface

Minimum scope:

- incident metadata
- query or symptom
- evidence attachments
- retrieval trace fields
- latency fields
- artifact write intent

This should become the input contract for future CLI use and benchmark replay.

### 3. Add A Thin CLI Runner

Target outcome:

- one reproducible execution surface

Minimum scope:

- read structured input
- choose mode
- produce JSON output
- render Markdown output
- optionally emit a run log entry

Do not build a heavy service first.

### 4. Define A Telemetry Contract

Target outcome:

- make production diagnosis prerequisites explicit

Minimum fields:

- query text or normalized query
- retrieved chunk or doc ids
- retrieval scores
- metadata filters
- reranking decisions if present
- prompt assembly metadata
- stage latencies
- citations returned to the user
- artifact writes

Without this, the repo can describe diagnosis but cannot reliably support it.

### 5. Run A Small Real Pilot

Target outcome:

- prove real usefulness, not just theoretical quality

Minimum scope:

- `2-3` real cases
- each with raw evidence, memo, recommended action, and outcome
- at least one case where the skill prevents an unjustified architecture escalation

### 6. Add Freshness And Release Discipline

Target outcome:

- reduce decay in durable knowledge

Minimum scope:

- `last_validated_at`
- `derived_from`
- `owner`
- `stale_after_days`
- release tags like `v0.x`
- changelog
- release checklist

## 6 To 8 Week Roadmap

### Weeks 1-2

Focus:

- evaluation foundation

Deliverables:

- scenario schema
- first `15-20` benchmark cases
- baseline prompt setup
- rubric definitions

Success criteria:

- a reviewer can explain what counts as success or failure without reading the whole repo

### Weeks 2-3

Focus:

- regression protection

Deliverables:

- `pytest` tests for the two renderers
- snapshot or smoke tests for example outputs
- minimal CI

Success criteria:

- changes to the repo can be checked automatically

### Weeks 3-4

Focus:

- stable execution surface

Deliverables:

- incident/evidence bundle schema
- thin CLI runner
- JSON and Markdown outputs

Success criteria:

- a new machine or teammate can run a stable diagnosis flow with one command

### Weeks 4-5

Focus:

- observability prerequisites

Deliverables:

- telemetry contract doc
- trace-backed diagnosis example
- JSONL run log format

Success criteria:

- the repo can state exactly what telemetry is required before a diagnosis claim is trusted

### Weeks 5-6

Focus:

- real-world validation

Deliverables:

- `2-3` pilot cases
- before/after notes
- evidence of accepted or rejected recommendations

Success criteria:

- you can answer which recommendations were adopted and which were not

### Weeks 6-8

Focus:

- durability and release readiness

Deliverables:

- freshness metadata policy
- stale artifact checks
- first tagged release
- changelog
- case-study writeup

Success criteria:

- the repo looks maintainable, replayable, and reviewable rather than purely demonstrative

## What Not To Do First

Do not prioritize these first:

- adding more platform wrappers or badges
- adding many more reference pages
- adding more failure taxonomy pages before evaluation exists
- building a hosted service or polished frontend
- jumping to multi-agent, graph, or heavy orchestration
- integrating branded observability tools before internal metrics and goldens exist

These are not useless.
They are just lower leverage right now.

## Review Questions For Other Evaluators

If another AI or reviewer evaluates this direction, these are the most useful questions:

1. Is `Eval-first hardening` the right first productionization move for this repo?
2. Is the proposed benchmark shape sufficient, or does it miss critical skill behavior?
3. What is the minimum viable telemetry contract for trustworthy diagnosis?
4. What should the incident/evidence bundle schema include on day one?
5. Which of the current examples are strong enough to become benchmark seed cases?
6. What signals would prove that this skill is improving real team decisions rather than only producing neat memos?
7. What should be considered the first real adoption milestone?

## Final Recommendation

Treat this repo as an `expert workflow system` that needs:

- evaluation discipline
- replayability
- a stable execution surface
- a small but real adoption loop

Do not treat it as a half-finished product shell that needs more interface work first.

The shortest credible path forward is:

`benchmark the judgment -> protect it with regression -> connect it to real evidence bundles -> prove value on pilot cases -> only then expand the execution surface`
