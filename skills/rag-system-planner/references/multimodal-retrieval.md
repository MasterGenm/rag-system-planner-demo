# Multimodal Retrieval

Use this file when the corpus includes scans, screenshots, diagrams, tables, or other evidence that is not safely reducible to plain text retrieval.

## Decide Whether Multimodal Retrieval Is Really Needed

Text-only retrieval may still be enough when:

- OCR quality is high
- the important evidence is mostly prose
- page-level citations are acceptable
- images are decorative rather than semantically necessary

Plan explicit multimodal retrieval when:

- diagrams or screenshots contain the answer
- the user needs image-aware citations
- OCR loses important layout or labels
- tables, charts, or visual states carry key meaning

## Evidence Units

Keep retrievable units explicit:

- text chunks
- OCR blocks
- image or region assets
- table extracts when table structure matters

Do not blur them into one undifferentiated store if they serve different retrieval paths.

## Metadata Requirements

Preserve enough metadata to keep answers grounded:

- document id
- page number
- section id
- asset id or region id
- modality
- OCR confidence when applicable
- caption or nearby text anchors when available

## Retrieval Patterns

Prefer the lightest pattern that matches the task:

1. text-first baseline with OCR support
2. routed retrieval based on query type
3. parallel text and image retrieval with merged ranking

Only move beyond text-first when visual evidence measurably matters.

## Routing Guidance

Use modality-aware routing when:

- the question refers to a diagram, screenshot, UI state, label, or visual layout
- support workflows depend on image-specific troubleshooting
- scanned pages have weak OCR and need image context

Keep the routing explainable. A user or engineer should be able to tell why the system searched text, images, or both.

## Fallback Behavior

Plan for weak visual evidence:

- fall back to text evidence when images are low value
- abstain when OCR confidence is weak and no grounded image path exists
- expose low-confidence evidence rather than pretending certainty

## Evaluation Changes

Split evaluation by modality:

- text-only questions
- image-dependent questions
- scan-heavy questions
- mixed text-image questions

Check:

- retrieval hit rate by modality
- citation correctness by page or asset
- groundedness under weak OCR conditions
- failure rate when routing chooses the wrong branch

## Observability Signals

Trace at least:

- chosen modality path
- retrieved asset ids and chunk ids
- OCR confidence
- branch-specific retrieval scores
- merged ranking decisions
- final citation anchors

## Recommendation Pattern

State:

1. why multimodal retrieval is or is not justified
2. the minimal baseline to launch
3. the routing strategy
4. the fallback behavior
5. what extra complexity is intentionally deferred
