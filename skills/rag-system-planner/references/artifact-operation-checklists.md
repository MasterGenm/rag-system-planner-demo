# Artifact Operation Checklists

在读取 `artifact-maintenance-contract.md` 之后，再使用这些 checklist。

## `ingest`

1. 读取 `index.md`、相关 hub 和候选 canonical pages。
2. 读取新的 source；如果它很大，先导航，再深入阅读。
3. 确认这是一次 re-ingest update，还是一个真正的新页面。
4. 保存或确认 source record。
5. 更新最小且最匹配的 canonical pages。
6. 只有在导航确实发生变化时才刷新导航。
7. 只有 workspace 发生了真实变化时，才追加到 `log.md`。

完成检查（Completion check）：

- source 已保留
- 变更页面已列出
- evidence trail 可见
- 剩余 gaps 已说明

## `query`

1. 读取 `index.md`。
2. 在重新推导答案之前，先读相关 canonical pages。
3. 当需要核验 claim 时，再去对照 `sources/`。
4. 带着明确的不确定性写出答案。
5. 如果结果可复用，就保存到 `queries/`。
6. 只有当结果跨过 artifact update threshold 时，才晋升到 `wiki/`。
7. 只有当 durable artifact 被保存或更新时，才向 `log.md` 追加记录。

完成检查（Completion check）：

- 答案以 workspace 为依据
- 使用过的 evidence 已列出
- durable destination 已说明
- 不确定性得到保留

## `lint`

1. 定义 lint scope。
2. 检查相关 hub、canonical pages 和已链接的 sources。
3. 记录 duplicates、unsupported claims、stale relationships、weak navigation 或 taxonomy drift。
4. 只清理那些你实际验证过的 scoped issues。
5. 如果导航发生变化，刷新受影响的 hub 或 index page。
6. 如果发生了清理动作，就保存 lint result，并追加到 `log.md`。

完成检查（Completion check）：

- findings 绑定到了具体文件
- severity 已说明
- fixes 已推荐或已应用
- 所有 cleanup 都被明确列出

## `index`

1. 读取 `index.md`、相关 hub，以及最近变动的页面。
2. 保持 root index 简短。
3. 让 folder hubs 承担 taxonomy 增长。
4. 重新链接那些被晋升或新变得重要的页面。
5. 检查链接仍然可解析。
6. 如果导航发生变化，就追加到 `log.md`。

完成检查（Completion check）：

- root index 仍然轻薄
- hub ownership 依然清晰
- 链接可以解析
- 变动后的导航已被总结
