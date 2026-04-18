# 2026-04-09 Open Support Copilot Retrieval Eval Extract

## Dataset

- 本地项目：`E:\dt\open-support-copilot`
- evaluation slice：`tests/retrieval_eval`
- 用途：把一份带标签的 retrieval audit 当作 `rag-system-planner` 的真实 scattered-evidence 示例

## Relevant Files

- `E:\dt\open-support-copilot\tests\retrieval_eval\README.md`
- `E:\dt\open-support-copilot\tests\retrieval_eval\gold_set.v1.json`
- `E:\dt\open-support-copilot\tests\retrieval_eval\results\chroma-retrieval-eval.md`
- `E:\dt\open-support-copilot\tests\retrieval_eval\results\qdrant-retrieval-eval.md`
- `E:\dt\open-support-copilot\tests\retrieval_eval\results\chroma-retrieval-eval.json`
- `E:\dt\open-support-copilot\tests\retrieval_eval\results\qdrant-retrieval-eval.json`

## Selected Walkthrough Example

- `id`：`architecture-01`
- question：`Should a support copilot over framework docs and GitHub issues stay on Chroma or move to Qdrant as filtering needs and update frequency grow?`
- 这个案例重要的原因：gold answer 明确要求比较双方的证据都要出现

## Gold Evidence

```text
https://docs.trychroma.com/reference/where-filter
https://docs.trychroma.com/docs/querying-collections/metadata-filtering
https://qdrant.tech/documentation/concepts/filtering/
https://qdrant.tech/documentation/faq/qdrant-fundamentals/
```

## Chroma Retrieval Summary

- `Recall@5 = 0.5000`
- matched URLs：
  - `https://docs.trychroma.com/reference/where-filter`
  - `https://docs.trychroma.com/docs/querying-collections/metadata-filtering`
- top 5 里缺失：
  - `https://qdrant.tech/documentation/concepts/filtering/`
  - `https://qdrant.tech/documentation/faq/qdrant-fundamentals/`

Top retrieved URLs：

```text
1. https://docs.trychroma.com/reference/overview
2. https://docs.trychroma.com/reference/where-filter
3. https://github.com/chroma-core/chroma/issues/6104
4. https://docs.trychroma.com/docs/querying-collections/metadata-filtering
5. https://docs.trychroma.com/docs/querying-collections/query-and-get
```

## Qdrant Retrieval Summary

- `Recall@5 = 0.2500`
- matched URLs：
  - `https://docs.trychroma.com/reference/where-filter`
- top 5 里缺失：
  - `https://docs.trychroma.com/docs/querying-collections/metadata-filtering`
  - `https://qdrant.tech/documentation/concepts/filtering/`
  - `https://qdrant.tech/documentation/faq/qdrant-fundamentals/`

审计里可见的 Top retrieved URLs：

```text
1. https://docs.trychroma.com/reference/overview
2. https://docs.trychroma.com/reference/where-filter
```

## Initial Read

这不只是一个泛泛的坏结果。这个 comparison query 需要跨两个 product family 收齐证据，但 retrieval 一直围绕 `Chroma` 一侧塌缩，从来没有把足够多的 `Qdrant` 证据抬出来，因此无法支撑平衡答案。

## Related Pages

- [Scattered Evidence Cutoff](../wiki/failure-modes/scattered-evidence-cutoff.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Source Trail

- 本地 retrieval-eval 文件于 2026-04-09 被检查
