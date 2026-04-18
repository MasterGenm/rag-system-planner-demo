# Section-Aware Chunking

## Summary

先按 section boundaries 切结构化文档，只有不够用时才退回 paragraph-level splitting。

## 什么时候该用

- 有 headings 和嵌套结构的文档
- runbooks
- 产品文档
- policy pages

## 什么时候不该用

- 没有结构、很短而平的 notes
- OCR 占比很重、结构本身就不可靠的证据

## Tradeoffs

- 通常能提升 citation quality 和 semantic coherence
- 可能需要更丰富的 metadata，以及保留 heading path

## Related Pages

- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)

## Source Trail

- 当前 `rag-system-planner` 在 retrieval design 上的指导
