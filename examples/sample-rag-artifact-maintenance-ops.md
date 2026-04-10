# Sample Artifact-Maintenance Operations

## Purpose

Show what a scoped maintenance loop looks like after the execution contract lands.

## Example Sequence

1. `ingest`
   - read `artifacts/rag-wiki-template/index.md`
   - read the incoming source extract
   - update the matching canonical failure or case-note page
   - preserve the source trail
2. `lint`
   - inspect the touched pages for unsupported claims, stale relationships, or duplicate conclusions
   - record explicit findings or cleanup
3. `index`
   - refresh `index.md` or the relevant folder hub only if navigation changed
   - keep the root index thin

## Why This Matters

This example makes the proposal operational.
The artifact layer is no longer just "save useful notes". It becomes a repeatable maintenance loop with scoped writes, explicit evidence use, and navigation hygiene.
