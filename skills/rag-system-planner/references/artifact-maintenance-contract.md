# Artifact-Maintenance Contract

`artifact-maintenance` 的职责是保存证据、结构和可复用的 RAG 知识。
它不会自行重构架构。

## Shared Rules

- 输入尽量使用 workspace-relative 路径。
- `sources/` 是原始证据，默认应保持不可变。
- 面对大型 source 时，先导航，再深入阅读。当可以有目标地读取时，不要从盲目 dump 中做综合。
- durable writes 必须保留可见的 `source` 或 `derived_from` 链路。
- 优先更新一个 canonical page，而不是创建近似重复页。
- `queries/` 用于保存“有用但尚未 canonical”的输出。
- 把 source staleness 当成真实状态。如果 source 变化了，应刷新关系或标记为 stale，而不是默默假设它仍然有效。
- 只有真实操作完成时，才向 `log.md` 追加记录。
- 把 index 和 hub 刷新视为 maintenance 的一部分，而不是可选清理。

## Planner Handoff Payload

当 planner hand off 给 artifact-maintenance 时，payload 应明确包含这些字段：

- question 或 symptom
- `observed`、`inferred` 和 `unknown` claims
- evidence touched
- primary target artifact type
- secondary targets（如果有）
- 这次写入是 `canonical` 还是 `query-only`

当结构化 handoff 有帮助时，使用 `templates/artifact-handoff-template.md`。

## `ingest`

### Use When

新的原始证据应该被转化为 durable workspace knowledge。

### Required Inputs

- 新的 source material
- workspace path
- 可能的 target artifact types 或 canonical pages
- 可选的 planner handoff payload

### Required Reads

1. `index.md`
2. 相关 folder hubs
3. 相关 canonical pages
4. source 本身

### Allowed Writes

- `sources/`
- 对应的 `wiki/` 页面
- 如果导航变化了，则可写 `index.md` 或 folder hubs
- `log.md`

### Required Outputs

- 已存储或已确认的 source record
- 被更新或创建的 durable pages 列表
- 简洁的 ingest summary
- 可见的 evidence trail

### Invariants

- 不要发明 source facts
- 当已有页面可以承载结论时，不要创建重复的 canonical page
- 保留 provenance
- 写入范围必须以你实际读过的证据为边界
- 把 re-ingest 当作一次 update pass，除非有充分理由创建新页面

### Stop And Return Gaps When

- source 缺失，或其完整度不足以支撑目标 claims
- canonical target 含糊不清，无法被合理证明
- evidence trail 无法被干净地保留下来

## `query`

### Use When

应该优先由 workspace 回答问题，并且这次结果可能值得保存。

### Required Inputs

- user question
- 当前 workspace
- 可选的 planner diagnosis context

### Required Reads

1. `index.md`
2. 先读相关 canonical pages
3. 仅当需要核验 claim 时再读 `sources/`

### Allowed Writes

- `queries/`
- 当达到 artifact update threshold 时，更新 canonical `wiki/` pages
- `log.md`

### Required Outputs

- 面向用户的 memo 或 answer
- 使用过的 evidence
- 创建或更新的 durable pages
- 剩余 uncertainty

### Invariants

- 先从 workspace 回答
- 不要把 `unknown` 压平为事实
- 对可复用结论要保存，不要只留在 chat 里
- 如果答案仍然太临时，就留在 `queries/`，不要强行 canonicalize

### Stop And Return Gaps When

- workspace 还不足以支持 grounded answer
- 答案依赖于那些实际上并未被审阅的证据

## `lint`

### Use When

当复用可靠性存疑，或 workspace 可能已经变得不一致时。

### Required Inputs

- workspace scope
- 可选的 focus area，例如 taxonomy、provenance、stale pages 或 navigation

### Required Reads

1. `index.md`
2. folder hubs
3. 候选 canonical pages
4. 已链接 sources
5. 必要时再看最近的 queries

### Allowed Writes

- lint report artifact
- 有边界的 cleanup edits
- 如果修导航是 run 的一部分，则可写 `index.md` 或 folder hubs
- `log.md`

### Required Outputs

- 明确 findings
- severity
- affected files
- recommended fixes
- 如果做了清理，还要列出 cleaned pages

### Invariants

- 只报告 evidence-backed issues
- 不要以 lint 为名进行大范围重写
- 区分 stale evidence 和 missing evidence
- 如果发生 cleanup，要明确说明具体改了什么

### Stop And Return Gaps When

- scope 过大，无法被可信地审阅
- 所声称的问题无法绑定到具体文件或证据

## `index`

### Use When

当大规模 ingest、cleanup 或 taxonomy 变化可能削弱导航时。

### Required Inputs

- ingest 或 cleanup 之后的当前 workspace
- 最近变更过的 durable pages

### Required Reads

1. `index.md`
2. folder `README.md` hubs
3. 最近变更过的 durable pages

### Allowed Writes

- `index.md`
- folder hubs
- `log.md`

### Required Outputs

- 已刷新的根导航
- 如有需要，已刷新的 hub pages
- 一段简短说明，说明什么被移动、被提升或被重新链接

### Invariants

- 保持 root index 轻薄
- 让 hubs 承担大 taxonomy 的所有权
- 不要只为了导航而复制内容
- 修改后链接必须仍然可解析

### Stop And Return Gaps When

- 导航修改会遮蔽 canonical entry points
- 无法保证 link integrity

## Completion Rule

只有当一次 artifact-maintenance run 明确说明了以下内容时，它才算完成：

- 执行了哪种 operation
- 审阅了哪些页面
- 改动了哪些页面
- 使用了哪些证据
- provenance 或 staleness status
- 剩余 gaps
