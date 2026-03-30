# RAG System Planner Productized Shell Implementation Plan

> For Claude: REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

Goal: create a productized wrapper for `rag-system-planner` that improves clarity, installation, triggerability, and showcase value without changing the core skill.

Architecture: keep the original repo surface intact and add a parallel `productized-shell/` directory that contains a rewritten product homepage, install docs, symptom maps, examples, and a distribution snapshot. Generate example outputs with the existing render scripts so the new shell highlights real deliverables rather than mock screenshots.

Tech Stack: Markdown, JSON, existing Python render scripts, repo-local distribution snapshot

---

### Task 1: Create design and plan artifacts

Files:
- Create: `docs/plans/2026-03-30-rag-system-planner-productized-shell-design.md`
- Create: `docs/plans/2026-03-30-rag-system-planner-productized-shell.md`

Steps:
1. Record the product-shell strategy and scope boundaries.
2. Capture the chosen parallel-wrapper approach.
3. Save both documents under `docs/plans/`.

### Task 2: Build the productized homepage shell

Files:
- Create: `productized-shell/README.md`

Steps:
1. Rewrite the first screen around value proposition, capability panels, and output visibility.
2. Add "what to ask" prompt examples.
3. Add links to rendered example outputs and installation docs.

### Task 3: Add trigger and integration documentation

Files:
- Create: `productized-shell/docs/symptom-to-reference-map.md`
- Create: `productized-shell/docs/install-and-integration.md`

Steps:
1. Turn implicit trigger logic into a visible navigation table.
2. Reorder installation from fastest path to platform-specific paths.
3. Keep the guidance aligned with the original skill boundaries.

### Task 4: Add structured example inputs

Files:
- Create: `productized-shell/examples/greenfield-plan.json`
- Create: `productized-shell/examples/diagnosis-report.json`
- Create: `productized-shell/examples/README.md`

Steps:
1. Create one realistic greenfield sample payload.
2. Create one realistic diagnosis sample payload.
3. Document how to regenerate the rendered Markdown outputs.

### Task 5: Generate rendered example outputs

Files:
- Create: `productized-shell/examples/greenfield-plan.md`
- Create: `productized-shell/examples/diagnosis-report.md`

Steps:
1. Run `render_rag_plan.py` against the greenfield JSON.
2. Run `render_rag_diagnostic.py` against the diagnosis JSON.
3. Confirm the outputs render as readable Markdown deliverables.

### Task 6: Create a distribution snapshot

Files:
- Create: `productized-shell/distribution/README.md`
- Copy: `skills/rag-system-planner/**`
- Copy: `cursor/rules/rag-system-planner.mdc`
- Copy: `kiro/steering/rag-system-planner.md`

Steps:
1. Copy the current skill contents into the distribution area.
2. Add a short note explaining that the bundle is a packaging snapshot of the original.
3. Use the productized homepage to point installers to this bundle first.

### Task 7: Verify the wrapper

Files:
- Review: `productized-shell/**`

Steps:
1. Confirm the example output links resolve.
2. Confirm the distribution tree exists.
3. Confirm the new shell does not overwrite the original project files.
