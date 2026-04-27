---
last_validated_at: 2026-04-27
derived_from: [docs/plans/2026-04-26-implementation-spec.md]
owner: <owner>
stale_after_days: 180
---

# 新鲜度政策

## 政策目的

本政策用于减少长期文档腐烂，让 Skill、规则文件和回顾性 case 明确记录何时验证、依据什么验证、由谁维护，以及多久后需要复核。

## 适用范围

当前 freshness 检查覆盖 6 个目标文件：

- `skills/rag-system-planner/SKILL.md`
- `cursor/rules/rag-system-planner.mdc`
- `docs/freshness-policy.md`
- `cases/CASE-0001-court-logic.md`
- `cases/CASE-0002-stackademic-rag-done-right.md`
- `cases/CASE-0003-lettria-graphrag.md`

未来扩展原则：

- 只给长期有效、会被后续任务复用的文档添加 freshness metadata。
- 不给测试 fixture、临时报告、PR 模板、短期计划草稿添加 freshness metadata。
- 新增长期 case 或长期规则文档时，应同步加入 freshness 检查目标列表。

## 字段语义

`last_validated_at` 表示该文件最近一次被人工或自动流程确认仍然可信的日期，格式为 `YYYY-MM-DD`。

`derived_from` 表示该文件当前内容的依据来源，可以是仓库内文件路径，也可以是公开来源 URL。

`owner` 表示负责后续复核的人或团队。本批次统一使用 `<owner>` 占位，不编造 GitHub handle。

`stale_after_days` 表示从 `last_validated_at` 起经过多少天后该文件进入 stale 状态。

## 分档策略

180 天档用于 Skill、规则和 policy 文档。

理由：

- 这些文件会影响后续判断协议、工具行为和维护规则。
- RAG 工程实践、评测方式和复杂度边界变化较快，应半年复核一次。

365 天档用于 retrospective application case。

理由：

- case 是历史材料，事实本身不会快速变化。
- case 仍可能因为链接失效、来源更新或 Skill 解释框架变化而需要年度复核。

## owner 占位处理

`owner` 字段当前统一写为 `<owner>`。

实际 GitHub handle 或维护团队名称由发起人在后续统一替换。

在 `<owner>` 替换前，freshness 检查只验证日期与过期状态，不把占位值视为错误。

## 触发与处理

当前不把 freshness 检查接入 CI。

是否将 `python scripts/check_freshness.py --as-of <YYYY-MM-DD>` 纳入自动检查，由发起人后续决定。

当文件状态为 `stale` 时，处理方式是重新阅读 `derived_from` 中列出的来源，确认内容是否仍然准确；若准确则更新 `last_validated_at`，若不准确则先修正文档再更新日期。
