# Hard-Case And Trace Review

## Purpose

把 hard-case evaluation 和 trace review 绑在一起，这样团队才能区分 failure 到底来自 retrieval、ranking、generation，还是 observability 缺口。

## Evaluation Dimensions

- citation correctness
- evidence grounding
- answer correctness
- context recall
- abstention behavior
- stage-level latency

## 需要采集的 Trace Signals

- retrieved chunk ids
- retrieval scores
- applied filters
- reranker decisions
- citation anchors
- retrieval latency
- generation latency
- total latency

## Hard-Case 类型

- multi-hop evidence
- 分散在许多 chunks 里的 scattered evidence
- negation 与 absence
- temporal ordering
- candidate recall 看起来不错、但 citation 发生 drift 的案例
- comparison 问题里，某一边证据根本没进 retrieval 的案例

## Review Questions

- 正确证据有没有进入 candidate pool？
- ranking 有没有把正确证据抬上来？
- 答案引用的是精确 span，还是只是一个附近的段落？
- 缺失的 traces 有没有直接阻碍 diagnosis？

## Related Pages

- [Good Recall, Weak Ranking](../failure-modes/good-recall-weak-ranking.md)
- [Scattered Evidence Cutoff](../failure-modes/scattered-evidence-cutoff.md)
- [Support KB Citation Drift](../case-notes/support-kb-citation-drift.md)

## Source Trail

- 评测与 telemetry 思路来自本地参考项目
