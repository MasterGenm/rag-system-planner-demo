---
name: rag-system-planner
description: 以受控复杂度规划、诊断并持续沉淀 retrieval-augmented generation（RAG）系统。适用于 greenfield RAG 设计、检索故障诊断、评测规划，以及维护能够长期保存 failure modes、stack decisions 和 case notes 的 durable RAG 工件。
last_validated_at: 2026-04-29
derived_from: [skills/rag-system-planner/scripts/render_rag_plan.py, skills/rag-system-planner/scripts/render_rag_diagnostic.py, skills/rag-system-planner/references/diagnosis-playbook.md, skills/rag-system-planner/references/retrieval-design.md, skills/rag-system-planner/references/observability-design.md]
owner: MasterGenm
stale_after_days: 180
---

# RAG System Planner

## 概览

在不默认引入不必要复杂度的前提下，设计新的 RAG 系统，并诊断已有系统。
这个 skill 是 artifact-aware 的：当某个结论很可能再次重要时，应把它保存在 durable workspace artifacts 中，而不是让它消失在聊天记录里。

保持 workflow 与具体框架无关。优先选择能够满足用户目标的最简单架构。只有当 failure mode 或 workflow 明确要求时，才升级到 hybrid、graph 或 agentic 模式。

持久化工作区模型见 `references/artifact-workflow.md`。
维护工作的执行合同见 `references/artifact-maintenance-contract.md`。
每种维护操作的最短确定性 runbook 见 `references/artifact-operation-checklists.md`。
当你要判断该创建哪类 durable 页面时，读取 `references/reference-to-artifact-map.md`。

## 双层模型（Two-Layer Model）

这个 skill 明确分成两层：

- `planner`
  - 为 greenfield 设计、diagnosis 和 comparison 做复杂度受控的判断
- `artifact-maintenance`
  - 保存并整理 durable 的 sources、evaluations、failure pages、case notes 和 workspace 结构

Planner 是推理层。
Artifact-maintenance 是知识复利层；当出现可复用结论时，planner 应先查询它，并在需要时更新它。

## Workflow 选择

先选主层：

- `planner`
  - 用户要的是设计、诊断、优先级判断或建议
- `artifact-maintenance`
  - 用户要的是 ingest、workspace 更新、lint，或者 durable knowledge 清理

在 `planner` 内部，再选一种模式：

- `greenfield`
  - 用户正在设计一个新的 RAG 系统，或准备替换旧系统的大部分结构
- `diagnosis`
  - 用户已经有一个 RAG 系统，想提升 recall、latency、groundedness、observability 或 operational reliability
- `comparison`
  - 用户主要想做一个有边界的方案比较，而不是完整设计或完整诊断

如果请求同时跨越两层，先从 `planner` 开始；当达到 artifact update threshold 时，再在结束前 hand off 给 `artifact-maintenance`。

## Planner 的第一步（Planner First Step）

不要一上来就从零推理：

1. 如果存在 artifact workspace，先检查它。
2. 读取 `index.md` 和最相关的 hub、evaluation page、failure page 或 stack-decision page。
3. 在 diagnosis 模式下，如果 workspace 中存在 `wiki/failure-modes/triage-matrix.md`，先从它开始。
4. 面对大 source 时，优先有目标地导航与阅读，不要对整份长文档做盲目综合。

### Workspace 状态规则（Workspace State Rules）

根据 workspace 的真实状态调整第一步：

- 不存在 workspace
  - 跳过 workspace 阅读
  - 直接读取最小静态 references，不要假装已有 artifact knowledge
  - 如果达到了 artifact update threshold，要明确建议先创建哪一个 durable artifact
- workspace 已存在，但还很薄
  - 读取 `index.md`，再读一个相关 hub 或页面
  - 优先做一个有边界的 `ingest` 或 `query`，而不是大范围维护
- workspace 中已经有相关 canonical pages
  - 优先引用并扩展这些页面
  - 优先更新现有页面，而不是创建近似重复页

## 比较型请求（Comparison Requests）

如果用户主要在比较选项，而不是要完整 greenfield 设计或完整 diagnosis，就保留在当前 workflow 中，但返回一个更轻的 decision memo。

使用这些 section：

1. Decision context
2. Options compared
3. Recommendation
4. Why this fits
5. Not chosen because
6. What would change the decision

## Artifact 更新阈值（Artifact Update Threshold）

以下内容不要只留在 chat 里。
只要答案里出现了这些内容，就应该更新 durable artifacts：

- 可复用的 failure mode
- 会重复出现的 retrieval 或 architecture pattern
- stack boundary 或 `not now` 决策
- 可复用的 evaluation heuristic 或 hard-case rule
- 未来大概率还会用到的 case note

## Intake

当需求缺失或表述含糊时，使用 `references/intake-checklist.md`。

只收集那些会影响架构决策的信息：

- 数据类型和来源
- 规模与更新频率
- 交互模式
- 质量优先级
- 成本与延迟约束
- 部署约束
- 现有技术栈和迁移约束
- 评测与可观测性预期

如果用户答不全，不要阻塞；改用一个简短的 assumptions section 继续往下做。

## Greenfield Workflow

1. 澄清问题、用户、数据模态和约束。
2. 执行 planner first step 和 workspace knowledge check。
3. 读取 `references/retrieval-design.md`，确定 chunking、metadata、retrieval、reranking 和 citation flow。
4. 如果语料包含扫描件、截图、图表、表格或其他非文本证据，读取 `references/multimodal-retrieval.md`。
5. 如果 embedding 选择并不显然，读取 `references/embedding-choice.md`。
6. 当存储、过滤、hybrid search 或运维权衡变得重要时，读取 `references/vector-db-choice.md`。
7. 只有当用户明确需要 agent behavior、tool use 或 orchestration 时，才读取 `references/agent-framework-choice.md`。
8. 读取 `references/eval-design.md`，定义 offline 和 online 验证。
9. 读取 `references/observability-design.md`，定义 tracing、monitoring 和 failure analysis。
10. 产出一个 solution package，包含 assumptions、stack choices、architecture、evaluation、observability、rollout phases，以及明确的 `not now` 决策，说明哪些复杂度是有意延后的。
11. 如果达到了 artifact update threshold，就把 durable patterns 或 decisions hand off 给 `artifact-maintenance`。
12. 如果结构化最终文档有帮助，运行 `scripts/render_rag_plan.py`。

## Diagnosis Workflow

1. 用具体术语总结症状：低 recall、检索不相关、幻觉、高延迟、高成本、缺 citation 或 agent 行为差。
2. 执行 planner first step 和 workspace knowledge check。
3. 先读取 `references/diagnosis-playbook.md`。
4. 当存在 artifact workspace 时，从 `wiki/failure-modes/triage-matrix.md` 开始，把症状归入“最小 plausible failure family”。
5. 在扩大阅读范围之前，先读最接近的具体 failure page。
6. 把每个 hypothesis 标记成 `observed`、`inferred` 或 `unknown`。不要让缺失证据悄悄变成 root-cause claim。
7. 如果问题可能来自 chunking、metadata、retrieval、reranking 或 prompt assembly，读取 `references/retrieval-design.md`。
8. 如果问题涉及扫描件、截图、图表、表格、OCR 质量或模态路由，读取 `references/multimodal-retrieval.md`。
9. 如果怀疑表示质量或多语言行为有问题，读取 `references/embedding-choice.md`。
10. 如果 filtering、indexing、hybrid search、persistence 或 scale 看起来是瓶颈，读取 `references/vector-db-choice.md`。
11. 读取 `references/eval-design.md`，找出缺失的 benchmark 和 dataset。
12. 读取 `references/observability-design.md`，找出缺失的 traces 或 runtime signals。
13. 产出一个 diagnostic report，包含 likely causes、missing evidence、investigation order 和按优先级排序的 remediation path。在 `Recommended changes` 中，优先使用 `now`、`next`、`later` 的排序，并且先做可逆修改，再做高成本重构。
14. 如果达到了 artifact update threshold，把可复用的 failure notes、investigation heuristics 或 stack decisions hand off 给 `artifact-maintenance`。
15. 如果结构化最终文档有帮助，运行 `scripts/render_rag_diagnostic.py`。

## Artifact-Maintenance Workflow

当主要目标是维护持久化 workspace，或者 planner 已经产出了必须保存的 durable findings 时，使用这一层。

在执行任何维护操作之前：

1. 读取 `references/artifact-maintenance-contract.md`。
2. 按照 `references/artifact-operation-checklists.md` 中匹配的 runbook 执行。
3. 保持操作有边界。Maintenance 的职责是保存和整理知识，不是借机做无限制重构。

使用以下操作之一：

- `ingest`
  - 把原始证据转成 durable pages
- `query`
  - 从 workspace 回答问题，并在合适时保存 durable 结果
- `lint`
  - 检测重复项、缺证据断言、过时页面、弱导航和 taxonomy drift
- `index`
  - 刷新或修复 workspace 的入口页和 hub 页

## 输出合同（Output Contract）

### Greenfield 输出

返回一个完整的 solution package，包含这些 section：

1. Problem summary
2. Assumptions and constraints
3. Recommended stack
4. Architecture and data flow
5. Retrieval design
6. Agent integration guidance
7. Evaluation plan
8. Observability plan
9. Risks and tradeoffs
10. Phased rollout plan
11. Durable artifact summary

在 `Recommended stack` 和 `Risks and tradeoffs` 中，解释为什么当前复杂度级别合适，以及哪些东西是有意不加入的。
在 `Retrieval design` 中，如果语料不只是文本，要包含模态路由和 fallback behavior。
在 `Durable artifact summary` 中，说明创建或更新了哪些 durable pages；如果没有写入 durable 页面，也要说清为什么结果保持为 chat-only。

### Comparison 输出

返回一个更轻的 decision memo，包含这些 section：

1. Decision context
2. Options compared
3. Recommendation
4. Why this fits
5. Not chosen because
6. What would change the decision

在 `Recommendation` 中，保持结论有边界，并说明当前有意延后的复杂度。
在 `What would change the decision` 中，点明哪类缺失证据、评测结果或 workload 变化会成为升级理由。

### Diagnosis 输出

返回一个 diagnostic report，包含这些 section：

1. Symptom summary
2. Working hypotheses
3. Missing evidence
4. Investigation order
5. Recommended changes
6. Evaluation additions
7. Observability additions
8. Risks and expected impact
9. Durable artifact summary

在 `Working hypotheses` 中，标明哪些是 observed，哪些是 inferred。
在 `Recommended changes` 中，当顺序重要时，用 `now`、`next`、`later` 排序。
在 `Evaluation additions` 中，当区分很重要时，明确下一轮验证应该聚焦 `single passage`、`multi passage` 还是 `no answer` 风格的检查，并说明它要确认或证伪的是哪一个 failure family。
在 `Durable artifact summary` 中，说明创建或更新了哪些 durable pages；如果没有写入 durable 页面，也要说清为什么结果保持为 chat-only。
不要在缺失证据之外做过度推测。

## 最小阅读集（Minimal Reading Sets）

- `greenfield` 最小集：
  - `references/intake-checklist.md`
  - `references/retrieval-design.md`
  - `references/eval-design.md`
- `diagnosis` 最小集：
  - `references/diagnosis-playbook.md`
  - `references/retrieval-design.md`
  - `references/observability-design.md`
  - 当存在 artifact workspace 时，再加 `wiki/failure-modes/triage-matrix.md`

只有当请求内容或 failure mode 明确要求时，才读取超出这些范围的文档。

- `references/intake-checklist.md`
  当任务缺少需求信息，或你需要一个结构化访谈时读取。
- `references/embedding-choice.md`
  当你要选择或质疑 embedding 层时读取。
- `references/vector-db-choice.md`
  当你要比较存储、过滤、索引、规模或检索运维时读取。
- `references/retrieval-design.md`
  当你要处理 chunking、metadata、hybrid retrieval、reranking 和 citation design 时读取。
- `references/multimodal-retrieval.md`
  当语料或 failure mode 涉及扫描件、截图、图表、表格或跨模态路由时读取。
- `references/agent-framework-choice.md`
  只有当用户需要 tool use、agents 或 orchestration 时才读取。
- `references/eval-design.md`
  当你在规划 measurement、benchmarks 或 regression checks 时读取。
- `references/observability-design.md`
  当你在规划 traces、logs、dashboards 或 runtime monitoring 时读取。
- `references/diagnosis-playbook.md`
  在 diagnosis 模式中先读它。
- `references/artifact-workflow.md`
  当任务应该把 durable RAG knowledge 保存下来，而不是只停在 chat 中时读取。
- `references/artifact-maintenance-contract.md`
  当任务包含 ingest、query、lint、index 或 durable artifact updates 时读取。
- `references/artifact-operation-checklists.md`
  当你需要一份最短、确定性的 maintenance runbook 时读取。
- `references/reference-to-artifact-map.md`
  当你要判断一个结论应该写进 pattern page、failure page、evaluation page、stack decision 还是 case note 时读取。

## 脚本（Scripts）

- `scripts/render_rag_plan.py`
  从结构化 JSON 输入渲染出一致的 Markdown solution package。
- `scripts/render_rag_diagnostic.py`
  从结构化 JSON 输入渲染出一致的 Markdown diagnostic report。

脚本只负责格式化，不负责做架构判断。不要把 architecture judgment 挪进 Python。

## 原则（Principles）

- 在用户约束足以支撑推荐之前，保持框架中立。
- 如果 plain retrieval pipeline 已经够用，就不要引入 agent framework。
- 除非任务有明确的分解需求、真实分支条件，并且比更简单的 retrieval 升级能带来可测收益，否则不要启用 agentic RAG。
- 对小型或稳定语料，优先更少的 moving parts。
- 先建立 minimal viable baseline，再为每一层新增复杂度给出理由。
- 区分 retrieval failure 和 generation failure。
- 区分 missing observability 和真实的 model quality problem。
- 在 diagnosis 模式下，先做 instrumentation、evidence collection 和可逆修改，再做高成本重构。
- 当你推荐复杂度时，要说清它带来什么，也要说清它的代价。
- 明确指出哪些推荐是 inference，而不是 evidence。
- 不要声称那些并未真实测量过的 benchmark numbers。
- 当某个结论很可能再次重要时，不要让它死在对话里。

## 语境化升级豁免（Contextual Escalation Exception）

默认情况下，向 GraphRAG、multi-agent rewrite 等高复杂度架构的升级应被推迟。

仅当下列 5 项条件全部被实测证据证实时，可将 `must_avoid: graph_rag` 或 `must_avoid: multi_agent_rewrite` 从硬性避免放宽为语境化延后，并允许进入固定 hard-case set 上的 bounded experiment：

1. 场景属于高风险或受监管行业，例如金融、法律、医疗、航空航天。
2. 语料包含表格、图表、专业术语等复杂半结构化结构。
3. 业务输出对 lineage 与 auditability 有明确硬性要求。
4. vector-only baseline 已被实测验证不足，并附具体数字或可观察的失败模式。
5. 团队具备 graph extraction、双写一致性、payload 索引等工程能力的可验证证据。

即使 5 项条件全部满足，也不直接建议生产化升级；豁免的含义是允许进入受控对照实验阶段。

### Bounded Experiment 边界

当不满足上述 5 项中的任意一项时，仍可对升级方案进行 bounded experiment 来收集证据，但必须满足：

- 在固定 hard-case set 上对照。
- 与 baseline 同时跑，不替换 baseline。
- 实验产出明确的 win/loss/inconclusive 判定。

bounded experiment 不是升级承诺，是证据收集。
