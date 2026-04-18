# Reference To Artifact Map

用这份文件判断：静态 guidance 应该如何被提升进 durable artifact workspace。

## Mapping

- `intake-checklist.md`
  当某些 durable project facts 很可能再次重要时，把它们提升到 `wiki/case-notes/`。
- `retrieval-design.md`
  把可复用的 chunking、metadata、retrieval、reranking、citation 和 abstention guidance 提升到 `wiki/patterns/`。
- `diagnosis-playbook.md`
  把会重复出现的 symptom classes 和 investigation ladders 提升到 `wiki/failure-modes/`。
  在 active diagnosis 中，先从 `wiki/failure-modes/triage-matrix.md` 进入，再把持久结论提升进某一个 canonical failure page。
- `eval-design.md`
  把 hard-case definitions、metric recipes 和 review procedures 提升到 `wiki/evaluations/`。
- `observability-design.md`
  把 trace requirements、stage-level latency guidance 和 debugging signals 提升到 `wiki/evaluations/` 或相关 case note。
- `embedding-choice.md`
  把会重复出现的 representation boundary 提升到 `wiki/stack-decisions/`。
- `vector-db-choice.md`
  把 durable 的 storage 与 filtering 权衡提升到 `wiki/stack-decisions/`。
- `agent-framework-choice.md`
  把升级边界和 `not now` 决策提升到 `wiki/stack-decisions/`。
- `multimodal-retrieval.md`
  把 modality-routing patterns 提升到 `wiki/patterns/`；把会反复出现的 OCR 或 screenshot failure classes 提升到 `wiki/failure-modes/`。

## Promotion Heuristic

按“主要复用价值”选择目标位置：

- `patterns/`：用于可复用的构建方式
- `failure-modes/`：用于可复用的调试方式
- `evaluations/`：用于可复用的测量和 tracing 方式
- `stack-decisions/`：用于会重复出现的架构边界
- `case-notes/`：用于项目特定的历史和证据

如果 artifact 仍然太临时、太 scoped，就先保存到 `queries/`，以后再提升。

## Planner Handoff Targeting

当 planner hand off 给 artifact-maintenance 时，先选一个 primary destination：

- `patterns/`：当经验是可复用的构建规则或检索规则
- `failure-modes/`：当经验是可复用的调试类别或 investigation ladder
- `evaluations/`：当经验是测量、trace 或 review 规则
- `stack-decisions/`：当经验是重复出现的架构边界或 `not now` 决策
- `case-notes/`：当经验绑定在一个项目、一个 incident 或一组 source
- `queries/`：当结果有用，但还不够稳定，不适合 canonicalize

如果一个结果看起来能落进多个页面类型，优先更新“最小且可复用”的 canonical page，把额外的项目细节放进 case note 或 query memo。

## Handoff Payload

planner handoff 至少应显式包含这些字段：

- question 或 symptom
- `observed`、`inferred` 和 `unknown` claims
- evidence touched
- primary target artifact type
- secondary targets（如果有）
- 写入是 `canonical` 还是 `query-only`
