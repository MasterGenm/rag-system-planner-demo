# 示例：端到端流程

## 原始证据

- `artifacts/rag-wiki-template/sources/sample-support-incident.md`

## 规划层步骤

- `planner` 先读工作区，分类问题，并决定有边界的修复路径

## 生成的持久页面

- `artifacts/rag-wiki-template/wiki/case-notes/support-kb-citation-drift.md`
- `artifacts/rag-wiki-template/wiki/failure-modes/good-recall-weak-ranking.md`
- `artifacts/rag-wiki-template/wiki/evaluations/hard-case-trace-review.md`

## 工件维护步骤

- `artifact-maintenance` 写入或更新上述持久页面，并保留证据链

## 面向用户的备忘录

- `artifacts/rag-wiki-template/queries/sample-diagnostic-note.md`

## 这个示例为什么存在

它说明这套方案不只是更好的回答格式，而是一条工作流：`planner` 先做判断，`artifact-maintenance` 先保留可复用结果，再产出面向用户的备忘录。
