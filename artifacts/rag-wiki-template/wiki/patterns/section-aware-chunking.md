# Section-Aware Chunking

## Summary

Chunk structured documents by section boundaries before falling back to paragraph-level splitting.

## When To Use

- docs with headings and nested structure
- runbooks
- product documentation
- policy pages

## When Not To Use

- tiny flat notes with no structure
- OCR-heavy evidence where structure is unreliable

## Tradeoffs

- usually improves citation quality and semantic coherence
- may require richer metadata and heading-path retention

## Related Pages

- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)

## Source Trail

- current rag-system-planner guidance on retrieval design
