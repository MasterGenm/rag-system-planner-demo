# Intake Checklist

Use this checklist when requirements are incomplete. Ask only for the fields that change architecture decisions.

## Greenfield Intake

### Product Goal

- What does the system need to answer or produce?
- Who are the users?
- Is this simple Q&A, multi-turn chat, or agent-assisted work?

### Data

- What data types are involved: text, PDF, web pages, images, audio, tables, or mixed?
- How many documents or records exist now?
- How often does the corpus change?
- Are metadata filters important?

### Constraints

- What matters most: recall, precision, latency, cost, or traceability?
- What are the deployment constraints: local, cloud, CPU, GPU, or compliance boundaries?
- Is there an existing stack that should be reused?

### Output Expectations

- Are citations required?
- Is tool use required?
- Is human review in the loop?
- Is offline evaluation required before launch?

## Diagnosis Intake

- What symptom is visible right now?
- When did it start?
- Is the problem retrieval quality, answer quality, latency, stability, or observability?
- What stack is already in place?
- What evidence exists: logs, traces, labeled examples, dashboards, evaluation runs?
- What has already been tried?

## Minimal Assumption Rules

If the user cannot answer everything, proceed with explicit assumptions.

Good assumptions:

- "Assume a medium-size corpus with daily updates."
- "Assume citation quality matters more than raw latency."
- "Assume Python-based orchestration is acceptable."

Bad assumptions:

- "Assume the user wants agents."
- "Assume the most complex architecture is appropriate."

## Required Vs Optional

### Usually Required

- Task type: greenfield or diagnosis
- Data type
- Approximate scale
- Primary optimization target

### Usually Optional

- Exact model name
- Exact cloud vendor
- Exact benchmark target

If a field is optional, do not stop progress waiting for it.
