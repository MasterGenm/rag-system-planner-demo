# Artifact Scaffold Adoption Guide

当你想从零开始落下第一份 durable RAG artifact 时，使用这份指南。

这是一份 phase 2 onboarding 文档。
它不会给 skill 增加新行为。
它只是把现有的 phase 1 workspace 变成一条更清晰的首轮使用路径。

## 什么时候该用这个 Scaffold

当至少满足以下一条时，使用 [rag-wiki-template](./README.md)：

- 你预期同一类 failure mode 或 stack decision 以后还会反复出现
- 你希望 diagnosis 工作可以持续积累，而不是每次都从聊天重新开始
- 你想把原始证据、可复用结论和已保存 memo 放在同一个地方
- 你希望后续 planner 运行能直接从维护过的 artifacts 起步，而不是重新发现同一条经验

如果你只需要一次性答案，可以停在 [../../skills/rag-system-planner/SKILL.md](../../skills/rag-system-planner/SKILL.md)，保持 chat-only。

## 首次使用路径

按这个顺序走：

1. 读 [AGENTS.md](AGENTS.md)。
2. 读 [index.md](index.md)。
3. 读 `wiki/` 下面相关的 hub 页面。
4. 往 `sources/` 里放一份真实 source 文件。
5. 选择一条小范围 maintenance 路径：`ingest` 或 `query`。
6. 创建一份 durable artifact。
7. 在 [log.md](log.md) 里追加一条简短的已完成记录。

不要试图在一次 session 里把整个 scaffold 全部填满。
目标是一份真实 source、一个真实判断、以及一页 durable 页面。

## 各目录放什么

- `sources/`
  原始证据。默认按不可变处理。
- `wiki/`
  可复用知识。把 recurring patterns、failure modes、evaluations、stack decisions 和 case notes 放在这里。
- `queries/`
  有保存价值，但还不够稳定或不够通用、暂时不能升级为 canonical page 的答案。
- `index.md`
  精简的根导航页。
- `log.md`
  只记录已完成的 maintenance 操作。

## 第一步：加入第一份 Source

往 [sources/](sources/) 里加入一份原始输入。

好的第一份 source 往往是：

- 一份 incident note
- 一段 retrieval trace 摘录
- 一份 eval 输出
- 一份设计或架构说明

合适时优先使用日期前缀文件名。
在存进去之前，不要先把 source 改写成分析结论。

## 第二步：选择第一条工作流

当你在回答一个具体问题，而且结果可能会、也可能不会升级为 canonical 时，使用 `query`。

从这里开始：

- [templates/query-note-template.md](templates/query-note-template.md)

当你已经知道某份 source 里包含可复用知识、应该回写到 workspace 时，使用 `ingest`。

从这里开始：

- [templates/ingest-note-template.md](templates/ingest-note-template.md)

只有在工作区已经有真实内容之后，再使用 `lint` 或 `index`。

从这里开始：

- [templates/lint-report-template.md](templates/lint-report-template.md)
- [templates/index-refresh-note-template.md](templates/index-refresh-note-template.md)

## 第三步：先读后写

在新建 durable 页面之前：

1. 如果问题是诊断型的，先读 [wiki/failure-modes/README.md](wiki/failure-modes/README.md)。
2. 如果症状还很模糊，先读 [wiki/failure-modes/triage-matrix.md](wiki/failure-modes/triage-matrix.md)。
3. 如果主要经验和测量、trace review 有关，先读 [wiki/evaluations/README.md](wiki/evaluations/README.md)。
4. 优先更新已有 canonical page，而不是创建一个近似重复页。

## 第四步：创建第一份 Durable Artifact

如果你需要在 `wiki/` 里创建新的 canonical page，使用 [templates/page-template.md](templates/page-template.md)。

好的第一份 durable artifact 往往是：

- 一份与单个 incident 绑定的 case note
- 一次由重复证据支撑的 failure page 更新
- 一次由可复用 review 规则支撑的 evaluation page 更新

升级规则：

- 临时的、范围窄的结果先放在 `queries/`
- 可复用结论再升级进 `wiki/`

始终保留一条清晰可见的 source trail。

## 第五步：记录这次操作

一次真实 maintenance pass 完成后：

1. 在 [log.md](log.md) 里加一条简短记录
2. 只有导航真的变了时，才更新 [index.md](index.md) 或 hub 页面

当你需要一份简洁的操作记录时，使用 [templates/maintenance-run-template.md](templates/maintenance-run-template.md)，记录：

- 这次改了什么
- 用了哪些证据
- 还有哪些缺口没补上

## 推荐的第一份 Durable Artifact

默认最好的第一轮是：

1. 把一份 source 放进 `sources/`
2. 创建一份 ingest note
3. 在 `wiki/` 里更新或创建一页 canonical page
4. 追加一条 log 记录

如果第一次交互本质上是问答，那么默认最好的方式是：

1. 先把答案存进 `queries/`
2. 只有当它开始变得可复用时，再升级进 `wiki/`

## 示例阅读顺序

想走最短 onboarding 路径，按这个顺序读：

1. [../../examples/sample-rag-end-to-end.md](../../examples/sample-rag-end-to-end.md)
2. [../../examples/sample-rag-planner-handoff.md](../../examples/sample-rag-planner-handoff.md)
3. [../../examples/sample-rag-real-walkthroughs.md](../../examples/sample-rag-real-walkthroughs.md)
4. [../../examples/sample-rag-artifact-maintenance-ops.md](../../examples/sample-rag-artifact-maintenance-ops.md)

然后再把这些作为形态参考：

- [../../examples/sample-rag-case-note.md](../../examples/sample-rag-case-note.md)
- [../../examples/sample-rag-pattern-page.md](../../examples/sample-rag-pattern-page.md)
- [../../examples/sample-rag-wiki-index.md](../../examples/sample-rag-wiki-index.md)

这两份不要放进主 adoption 路径：

- [../../examples/sample-rag-plan.md](../../examples/sample-rag-plan.md)
- [../../examples/sample-rag-diagnostic.md](../../examples/sample-rag-diagnostic.md)

它们是有用的最终输出，但不如前面的材料那样直接展示 durable workflow。

## 第一条 Evaluation 路径

当第一份 source 和第一份 durable page 都已经存在后，用这条更短的 evaluation 路径开始：

1. 读 [wiki/evaluations/README.md](wiki/evaluations/README.md)。
2. 读 [wiki/evaluations/hard-case-trace-review.md](wiki/evaluations/hard-case-trace-review.md)。
3. 把第一条可复用的 evaluation 结论保存到 `wiki/evaluations/` 或 `queries/`，取决于它目前有多稳定。

## 成功标准

如果一轮 session 结束后，你能指向这些东西，这份指南就算生效：

- `sources/` 里的一份原始 source
- `queries/` 里的一份已保存 memo，或 `wiki/` 里的一页 canonical page
- 一处更新过的导航面，如果确实需要
- `log.md` 里一条完成记录

到这一步，后续 planner 运行就可以从 workspace 起步，而不是从零开始。
