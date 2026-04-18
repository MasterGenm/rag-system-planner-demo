# RAG Wiki Artifact Schema

这个 workspace 用来保存 durable 的 RAG 规划知识。

## 任务

把原始 RAG 证据转成可复用的运维型知识。

## 分层

1. `sources/` 保存原始证据，默认保持不可变。
2. `wiki/` 保存综合后的知识，是 canonical 的 durable 层。
3. `queries/` 保存那些值得保留、但还没升级为 canonical 的输出。

## Workspace 不变式

- 不要把原始证据改写成仿佛是原生分析。
- 面对大文件或长笔记时，先做目标导读，再做深入综合。
- 优先更新已有页面，而不是创建近似重复页。
- 做重要判断时，要保留清晰可见的证据链。
- 重复出现的结论要写进 `wiki/`，不要只留在 `queries/`。
- 把 source staleness 当成真实状态处理。如果 source 变了，或者信心下降了，要刷新关系或标记为 stale，不要默认旧结论仍然有效。
- 保持索引精简且可导航。
- 大型 taxonomy 里，把各目录下的 `README.md` 当成主导航 hub。
- 只把已完成的操作追加到 log。
- 如果某个发现可以复用为 pattern、failure mode、stack boundary、evaluation rule 或 recurring case lesson，就要在同一个 session 里把它写回 workspace。

## 操作

### Ingest

当 `sources/` 里出现新证据时使用。

1. 读 `index.md`。
2. 在创建新页面前，先读相关目录 hub 和候选 canonical pages。
3. 面对大 source 时，尽量先导航，再深读。
4. 更新或创建正确的 wiki 页面。
5. 对重要判断保留清晰可见的 source trail。
6. 只有导航变了时，才更新 `index.md` 或 hub 页面。
7. 只有这次操作确实改变了 workspace，才往 `log.md` 里追加记录。

### Query

当你在回答一个 RAG 架构或 diagnosis 问题时使用。

1. 读 `index.md`。
2. 先读相关 wiki 页面。
3. 需要核验时，再用 `sources/` 回查证据。
4. 把有 durable 价值的答案保存到 `queries/`，或折叠回 `wiki/`。
5. 如果这个答案已经可复用，就更新最贴切的 canonical page，而不是再建一个重复页。

### Lint

检查这些问题：

- orphan pages
- duplicate pages
- root index 过胖
- stale stack decisions
- stale source relationships
- unsupported claims
- 缺少 evaluation 或 observability 覆盖
- taxonomy drift

记录时要给出明确 findings、受影响文件和推荐修复。不要在没有列出检查范围时就声称 workspace 是“干净的”。

### Index

在大规模 ingest、清理或 taxonomy 变动之后使用。

1. 保持根 index 精简。
2. 某个 taxonomy 变了时，刷新对应目录的 `README.md` hub。
3. 不要只为了导航而重复复制内容。
4. 导航改动后，确认链接仍然有效。

## 模板

当某次操作适合沉淀成 durable run artifact 时，使用 `templates/` 下的模板：

- `ingest-note-template.md`
- `lint-report-template.md`
- `index-refresh-note-template.md`
- `maintenance-run-template.md`

## 升级指引

- `wiki/patterns/`：可复用的 retrieval 与 architecture patterns
- `wiki/failure-modes/`：重复出现的 diagnosis 类别
- `wiki/evaluations/`：hard-case 集、metric 配方、trace review 规则、observability signals
- `wiki/stack-decisions/`：会反复出现的架构和工具边界
- `wiki/case-notes/`：项目级历史，后续仍可能有用
