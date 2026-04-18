# 示例：规划层到工件层的交接

## 目的

展示 `rag-system-planner` 在拆分成 `planner` 和 `artifact-maintenance` 之后，应该如何协作。

## 示例案例

直接使用脚手架中已经存在的排序失败演练：

- `artifacts/rag-wiki-template/sources/2026-04-09-rag-qa-logs-corpus-source-extract.md`
- `artifacts/rag-wiki-template/wiki/case-notes/developer-docs-auth-ranking-drift.md`
- `artifacts/rag-wiki-template/wiki/failure-modes/good-recall-weak-ranking.md`
- `artifacts/rag-wiki-template/wiki/evaluations/hard-case-trace-review.md`
- `artifacts/rag-wiki-template/queries/developer-docs-auth-ranking-diagnostic.md`

## 交接流程

1. `planner` 先读工作区，再看静态参考文档。
2. `planner` 将问题归类为 `Good Recall, Weak Ranking`。
3. `planner` 给出有边界的修复建议，例如先看首个相关结果排名和结构感知切块。
4. `artifact-maintenance` 保存原始摘录，更新案例记录和失败模式页面，并保留面向用户的备忘录。
5. 后续新的 `planner` 会话直接从这些持久化工件出发，而不是重新推导同一条结论。

## 这个示例为什么存在

它展示了新的双层 skill 合同的实际含义：`planner` 负责判断，`artifact-maintenance` 负责保留可复用结果。
