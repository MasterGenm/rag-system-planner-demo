# Artifact Operation Checklists

Use these checklists after reading `artifact-maintenance-contract.md`.

## `ingest`

1. Read `index.md`, relevant hubs, and candidate canonical pages.
2. Read the new source and navigate before deep-reading if it is large.
3. Confirm whether this is a re-ingest update or a genuinely new page.
4. Store or confirm the source record.
5. Update the smallest fitting canonical pages.
6. Refresh navigation only if it materially changed.
7. Append to `log.md` only if the workspace changed.

Completion check:

- source preserved
- changed pages listed
- evidence trail visible
- remaining gaps stated

## `query`

1. Read `index.md`.
2. Read relevant canonical pages before re-deriving an answer.
3. Verify important claims against `sources/` when needed.
4. Write the answer with explicit uncertainty.
5. Save to `queries/` if reusable.
6. Promote to `wiki/` only if the result crossed the artifact update threshold.
7. Append to `log.md` only if a durable artifact was saved or updated.

Completion check:

- answer grounded in workspace
- evidence used listed
- durable destination stated
- uncertainty preserved

## `lint`

1. Define the lint scope.
2. Inspect the relevant hubs, canonical pages, and linked sources.
3. Record duplicates, unsupported claims, stale relationships, weak navigation, or taxonomy drift.
4. Clean up only the scoped issues you actually verified.
5. If navigation changed, refresh the affected hub or index page.
6. Save the lint result and append to `log.md` if cleanup happened.

Completion check:

- findings tied to files
- severity stated
- fixes recommended or applied
- any cleanup explicitly listed

## `index`

1. Read `index.md`, relevant hubs, and recently changed pages.
2. Keep the root index short.
3. Let folder hubs absorb taxonomy growth.
4. Relink promoted or newly important pages.
5. Check that links still resolve.
6. Append to `log.md` if navigation changed.

Completion check:

- root index still thin
- hub ownership remains clear
- links resolve
- changed navigation summarized
