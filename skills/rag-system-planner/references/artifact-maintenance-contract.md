# Artifact-Maintenance Contract

`artifact-maintenance` exists to preserve evidence, structure, and reusable RAG knowledge.
It does not redesign architecture on its own.

## Shared Rules

- Inputs should be workspace-relative whenever possible.
- `sources/` is raw evidence and should stay immutable-by-default.
- For large sources, navigate before reading deeply. Do not synthesize from a blind dump when targeted reading is possible.
- Durable writes should keep a visible `source` or `derived_from` trail.
- Prefer updating one canonical page over creating near-duplicate pages.
- `queries/` is for saved outputs that are useful but not yet canonical.
- Treat source staleness as a real state. If a source changes, refresh the relationship or mark it as stale instead of silently assuming it is current.
- Append to `log.md` only when a real operation completed.
- Treat index and hub refresh as part of maintenance, not optional cleanup.

## Planner Handoff Payload

When planner hands off to artifact-maintenance, the payload should make these fields explicit:

- question or symptom
- `observed`, `inferred`, and `unknown` claims
- evidence touched
- primary target artifact type
- secondary targets if any
- whether the write is `canonical` or `query-only`

Use `templates/artifact-handoff-template.md` when a structured handoff helps.

## `ingest`

### Use When

New raw evidence should become durable workspace knowledge.

### Required Inputs

- new source material
- workspace path
- likely target artifact types or canonical pages
- optional planner handoff payload

### Required Reads

1. `index.md`
2. relevant folder hubs
3. related canonical pages
4. the source itself

### Allowed Writes

- `sources/`
- matching `wiki/` pages
- `index.md` or folder hubs if navigation changed
- `log.md`

### Required Outputs

- stored or confirmed source record
- list of durable pages updated or created
- concise ingest summary
- visible evidence trail

### Invariants

- do not invent source facts
- do not create a duplicate canonical page when an existing page fits
- preserve provenance
- keep writes scoped to the evidence actually reviewed
- treat re-ingest as an update pass unless there is a good reason to create a new page

### Stop And Return Gaps When

- the source is missing or too incomplete to support the intended claims
- the canonical target is ambiguous and cannot be justified
- the evidence trail cannot be preserved cleanly

## `query`

### Use When

The workspace should answer first and the result may need to be saved.

### Required Inputs

- user question
- current workspace
- optional planner diagnosis context

### Required Reads

1. `index.md`
2. relevant canonical pages first
3. `sources/` only when claim verification is needed

### Allowed Writes

- `queries/`
- canonical `wiki/` pages when the artifact update threshold is met
- `log.md`

### Required Outputs

- user-facing memo or answer
- evidence used
- durable pages created or updated
- remaining uncertainty

### Invariants

- answer from workspace first
- do not flatten `unknown` into fact
- save reusable conclusions instead of leaving them only in chat
- if the answer is still too temporary, keep it in `queries/` instead of forcing canonization

### Stop And Return Gaps When

- the workspace does not support a grounded answer
- the answer depends on evidence that was not actually reviewed

## `lint`

### Use When

Reuse reliability is in doubt or the workspace may have become inconsistent.

### Required Inputs

- workspace scope
- optional focus area such as taxonomy, provenance, stale pages, or navigation

### Required Reads

1. `index.md`
2. folder hubs
3. candidate canonical pages
4. linked sources
5. recent queries when needed

### Allowed Writes

- a lint report artifact
- targeted cleanup edits
- `index.md` or folder hubs if navigation repair is part of the run
- `log.md`

### Required Outputs

- explicit findings
- severity
- affected files
- recommended fixes
- pages cleaned if any

### Invariants

- report evidence-backed issues only
- do not perform broad rewrites under the label of lint
- distinguish stale evidence from missing evidence
- if cleanup happened, say exactly what changed

### Stop And Return Gaps When

- the scope is too broad to inspect credibly
- the claimed issue cannot be tied to specific files or evidence

## `index`

### Use When

Major ingest, cleanup, or taxonomy changes may have weakened navigation.

### Required Inputs

- current workspace after ingest or cleanup
- recently changed durable pages

### Required Reads

1. `index.md`
2. folder `README.md` hubs
3. recently changed durable pages

### Allowed Writes

- `index.md`
- folder hubs
- `log.md`

### Required Outputs

- refreshed root navigation
- refreshed hub pages if needed
- short note on what moved, was promoted, or was relinked

### Invariants

- keep the root index thin
- let hubs own large taxonomies
- avoid duplicating content only for navigation
- links should resolve after changes

### Stop And Return Gaps When

- navigation changes would obscure canonical entry points
- link integrity cannot be preserved

## Completion Rule

An artifact-maintenance run is complete only when it states:

- which operation ran
- which pages were reviewed
- which pages changed
- what evidence was used
- provenance or staleness status
- remaining gaps
