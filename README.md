# rag-system-planner

面向 AI Agent 的可复用工作流 Skill：帮助团队在 RAG 系统设计和故障诊断中做出有约束的决策——确定真正的失败模式、明确下一步该修什么、以及哪些升级现在不该做。

不是一段 prompt，而是一套包含决策框架、失败分诊矩阵、结构化输出合同和跨会话知识积累的可执行工作流资产。

> **A reusable Agent Skill demo for RAG system planning and diagnosis.** Packages domain expertise — structured decision frameworks, a 14-mode failure triage matrix, and standardized output contracts — into a cross-platform Agent Skill. Helps teams decide what to fix next in their RAG systems and what upgrades to defer. Adaptable to Claude Code, Cursor, Codex CLI, and 3+ other AI agent platforms.

<p align="center">
  <a href="#核心问题">问题</a> ·
  <a href="#工作方式">工作方式</a> ·
  <a href="#示例诊断模式">示例</a> ·
  <a href="#典型使用场景">场景</a> ·
  <a href="#核心能力">能力</a> ·
  <a href="#安装">安装</a> ·
  <a href="#agent-skill-设计理念">设计理念</a>
</p>

<p align="center">
  <a href="https://github.com/MasterGenm/rag-system-planner-demo/actions/workflows/ci.yml"><img src="https://github.com/MasterGenm/rag-system-planner-demo/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/MasterGenm/rag-system-planner-demo/releases"><img src="https://img.shields.io/github/v/release/MasterGenm/rag-system-planner-demo?style=flat-square" alt="Release"></a>
  <a href="https://github.com/MasterGenm/rag-system-planner-demo/blob/main/CHANGELOG.md"><img src="https://img.shields.io/badge/changelog-keep_a_changelog-blue?style=flat-square" alt="Changelog"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenAI_Codex_CLI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Codex CLI">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/Kiro-232F3E?style=flat-square&logo=amazon&logoColor=white" alt="Kiro">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square" alt="OpenClaw">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square" alt="OpenCode">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

---

## 核心问题

很多 RAG 团队的问题，不是不会搭系统，而是太容易在错误的时机升级错误的层。

常见情况是：

- 还没确认当前瓶颈，就先换向量库
- 真问题是排序，却先去重做 chunking
- 真问题是缺评测和可观测性，却先怪模型不够强
- plain RAG 还没稳定，就急着升级到 graph / agentic RAG

`rag-system-planner` 的作用，就是把这些分叉口变成更清楚、更有顺序、也更不容易拍脑袋的决策。

| 团队常见做法 | 这个 planner 会强迫团队先做什么 |
| --- | --- |
| 先改基础设施 | 先说清失败模式：retrieval、ranking、generation 还是 observability |
| 因为某个工具"听起来更生产级"就提前升级 | 先保住最小 baseline，再明确 tradeoff |
| 从 plain RAG 直接跳到 graph / agentic RAG | 只有分支条件和工作流需求真实存在时才升级 |

## 工作方式

<img width="2048" height="2048" alt="流程展示v2" src="https://github.com/user-attachments/assets/50c1dff3-7570-489b-93c2-7887cd3d6f2f" />

这个 skill 有两种主模式和一种轻量输出。

### 1. 新系统规划（Greenfield）

用于设计一个新 RAG 系统，或替换一个旧系统的大部分结构。先澄清问题和约束，默认先处理 retrieval 设计，只在需要时补读额外 reference，最后产出完整方案包。

### 2. 诊断模式（Diagnosis）

用于系统已经存在，但出现了召回差、排序差、幻觉、高延迟、缺引用、难调试等问题。从症状开始而不是从猜测开始，给每条假设贴上 `observed / inferred / unknown`，最后给出有优先级的修复路径。

### 3. 比较型请求（Comparison）

用户主要在比较选项时，不开第三条主流程，改用一个更轻的决策备忘录输出：决策背景、比较选项、推荐结论、为什么适合、为什么不选别的、什么条件会改变结论。

## 示例：诊断模式

**输入**：

> 我们的支持知识库 RAG 系统，用户反馈"搜得到相关文档，但经常答不到点上"。正确证据偶尔已经进入候选集，但不在排序最靠前的结果中。引用经常指向相邻段落而不是精确证据段。加了更多检索阶段之后延迟明显上升。

**输出**（结构化诊断报告摘要）：

| 假设 | 状态 | 说明 |
|------|------|------|
| 排名最前结果的精度弱于候选召回 | observed | Top-ranked 结果不准 |
| 切块可能过粗，细粒度问题不容易精确命中 | inferred | 待验证 |
| 团队把排序问题误判成"整个架构不够高级" | inferred | 待验证 |
| embedding 是否是当前最主要瓶颈 | unknown | 缺数据 |

**推荐改动**：

- **现在**：增加追踪（chunk ids、scores、filters、引用锚点）；建一个引用密集型困难样例集；调整切块粒度和分节感知元数据
- **下一步**：如果候选召回足够而 Top-1 精度差，引入重排实验；对关键词密集型查询单独测试混合检索
- **以后**：只有在基线检索加排序调整仍然无效时，才讨论更高复杂度路线

完整示例见 [`examples/sample-rag-diagnostic.md`](examples/sample-rag-diagnostic.md)，更多示例见 [`examples/`](examples/)。

## 典型使用场景

**场景 1：新系统规划** — 团队要给内部知识库做 RAG。输入需求和约束，Skill 输出一份包含检索设计、评测计划、可观测性方案和分阶段上线路径的完整方案包，并明确标注"现在不加什么以及为什么"。

**场景 2：线上召回排障** — 用户反馈"搜得到文档但答不到点上"。Skill 从症状出发做分诊，把每条假设标记为 observed / inferred / unknown，输出有优先级的修复路径（now / next / later），而不是一份泛泛的架构升级方案。

**场景 3：选型决策** — 团队纠结 Qdrant vs Chroma、要不要上 reranking。Skill 输出一份 decision memo，不只说推荐什么，还说"什么条件会改变这个结论"。

**场景 4：控制升级冲动** — 团队想从 plain RAG 跳到 Graph RAG / Agentic RAG。Skill 检查升级前提条件是否成立，大多数情况下结论是"先把 baseline 检索和评测做好"。

**场景 5：跨会话知识积累** — 上次诊断发现的失败模式、有效的 chunking 策略、选型结论，被持久化到 artifact workspace，下次会话不需要重新发现。

## 核心能力

| 模块 | 一句话说明 | 何时触发 |
| --- | --- | --- |
| **需求澄清** | 在需求不完整时，只收集会影响架构决策的最小关键信息 | 用户只说"做个 RAG"或上下文不完整时 |
| **新系统规划** | 为新系统或大规模重构输出最小可行且可扩展的 RAG 方案 | 新系统设计、旧系统重搭、要定 baseline 时 |
| **诊断分诊** | 从症状出发做排障，而不是从工具偏好出发 | recall 差、hallucination、latency、citation 弱、难调试时 |
| **选型比较** | 把选型问题压缩成可执行的 decision memo | Qdrant vs Chroma、reranking 要不要上、LangGraph 值不值 |

<details>
<summary>辅助能力</summary>

| 模块 | 一句话说明 | 何时触发 | 主要参考文件 |
| --- | --- | --- | --- |
| **检索设计** | 优先处理 chunking、metadata、retrieval、reranking 和 citation flow | 怀疑问题在召回、排序、chunking、filter、citation 时 | `references/retrieval-design.md` |
| **升级边界检查** | 检查系统是否真的满足升级到 hybrid / graph / agentic 的条件 | 团队想升级复杂度，但条件是否成立还不清楚时 | `references/agent-framework-choice.md` |
| **评测设计** | 设计能证明系统是否真的变好的评测 | 缺离线评测、hard cases、judge 设计、回归集时 | `references/eval-design.md` |
| **可观测性设计** | 定义 trace、日志、dashboard 和 stage-level signals | 无法定位 retrieval / generation / latency 问题时 | `references/observability-design.md` |
| **输出渲染** | 把结构化结论渲染成团队可读的 Markdown 交付文档 | 需要把 plan 或 diagnostic 发给团队时 | `scripts/render_rag_plan.py` |

</details>

<details>
<summary>症状 / 需求 → 该打开哪份 reference</summary>

| 用户问题 / 典型症状 | 优先参考 | 最终应返回什么 |
| --- | --- | --- |
| recall 很差，正确证据经常不在候选集里 | `references/diagnosis-playbook.md` | RAG Diagnostic |
| 相关证据在候选集里，但 top-ranked 结果不准 | `references/retrieval-design.md` | RAG Diagnostic 或 Comparison Memo |
| hallucination 高，答案看起来像编的 | `references/diagnosis-playbook.md` | RAG Diagnostic |
| latency 很高，不知道是 retrieval 还是 orchestration 太重 | `references/observability-design.md` | RAG Diagnostic |
| 回答里缺 citation，或者 citation 不可检查 | `references/retrieval-design.md` | RAG Diagnostic |
| 语料里有 PDF、表格、截图、图像证据 | `references/multimodal-retrieval.md` | RAG Plan 或 RAG Diagnostic |
| embedding 应该怎么选 | `references/embedding-choice.md` | Comparison Memo 或 RAG Plan |
| FAISS / Chroma / Qdrant / Milvus 应该怎么选 | `references/vector-db-choice.md` | Comparison Memo |
| 到底值不值得上 agentic RAG | `references/agent-framework-choice.md` | Comparison Memo |
| eval 该怎么做 | `references/eval-design.md` | RAG Plan 或 Comparison Memo |
| observability 该怎么做 | `references/observability-design.md` | RAG Plan 或 RAG Diagnostic |

</details>

## 交付产物

仓库提供两个 renderer 脚本：

- `scripts/render_rag_plan.py` — 把结构化 greenfield 方案渲染成 Markdown
- `scripts/render_rag_diagnostic.py` — 把结构化诊断报告渲染成 Markdown

它们只负责格式化输出，不负责做架构判断。架构判断来自 `SKILL.md` + `references/`，交付格式来自 renderer。

示例输出：[`examples/sample-rag-plan.md`](examples/sample-rag-plan.md)、[`examples/sample-rag-diagnostic.md`](examples/sample-rag-diagnostic.md)

## 安装

核心 skill 在 [`skills/rag-system-planner`](skills/rag-system-planner)。

### Claude Code

```bash
mkdir -p ~/.claude/skills/rag-system-planner
curl -o ~/.claude/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/skills/rag-system-planner/SKILL.md
```

### Cursor

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/rag-system-planner.mdc \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/cursor/rules/rag-system-planner.mdc
```

<details>
<summary>其他平台</summary>

### OpenAI Codex CLI

```bash
mkdir -p ~/.codex/skills/rag-system-planner
curl -o ~/.codex/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/skills/rag-system-planner/SKILL.md
```

### Kiro

```bash
mkdir -p .kiro/steering
curl -o .kiro/steering/rag-system-planner.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/kiro/steering/rag-system-planner.md

mkdir -p .kiro/skills/rag-system-planner
curl -o .kiro/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/skills/rag-system-planner/SKILL.md
```

### OpenClaw

```bash
mkdir -p ~/.openclaw/skills/rag-system-planner
curl -o ~/.openclaw/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/skills/rag-system-planner/SKILL.md
```

### OpenCode

```bash
mkdir -p ~/.config/opencode/skills/rag-system-planner
curl -o ~/.config/opencode/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/skills/rag-system-planner/SKILL.md
```

### Google Antigravity

```bash
mkdir -p ~/.gemini/antigravity/skills/rag-system-planner
curl -o ~/.gemini/antigravity/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/skills/rag-system-planner/SKILL.md
```

</details>

## Agent Skill 设计理念

这个项目不是一段 prompt。它是一次对 **Agent Skill 方法论** 的实践：把一个复杂的工作任务（RAG 系统规划和诊断）抽象成可复用、可执行、可评估的工作流资产。

| Agent Skill 特征 | 在本项目中的体现 |
|-----------------|----------------|
| **任务场景与触发条件** | SKILL.md frontmatter 定义触发描述；三种模式（greenfield / diagnosis / comparison）各有明确的进入条件 |
| **结构化执行步骤** | 两条主 workflow 有清晰的步骤序列，包括最小阅读集、workspace 状态检查、按需加载 reference |
| **决策逻辑而非固定路径** | 升级边界检查、failure triage matrix、evidence label 系统（observed / inferred / unknown）——教 AI 怎么判断，而不是给固定指令 |
| **标准化输出合同** | 三种输出格式有固定 section 结构（Output Contract），附带 Python 渲染脚本保证一致性 |
| **知识积累机制** | artifact workflow 把可复用结论持久化到 workspace，下次会话不需要重新发现 |
| **跨平台可移植** | 同一套逻辑适配 Claude Code / Cursor / Kiro / Codex CLI 等 6+ 平台 |

这是一个**知识密集型 Skill**——核心价值是决策框架和领域知识的结构化，而非通过本地代理服务增加运行时能力。两种 Skill 范式并列存在，各有适用场景。

## Internship Relevance

| 能力维度 | 在项目中的体现 |
|---------|--------------|
| 从真实问题抽象可复用工作流 | 把"RAG 该修什么"这个复杂判断拆成三条结构化流程，每条有明确的输入、步骤和输出合同 |
| 设计可执行的决策框架 | 14 种失败模式的分诊矩阵（4 个诊断族），升级边界检查，evidence label 系统 |
| 定义结构化输出合同 | 三种标准化产出格式，渲染脚本保证一致性 |
| 跨平台 Skill 适配 | 同一套逻辑适配 6+ 个 Agent 平台，展示对 Agent Skill 生态的理解 |
| 知识积累架构设计 | artifact workflow 实现跨会话 RAG 经验沉淀（sources → wiki → queries 三层） |

### 还没做到的

- 没有运行时服务或自动化集成——目前是纯知识层 Skill
- 缺少 Skill 自身的自动化质量评测（如对 renderer 输出的回归测试）
- 缺少用户反馈闭环和使用数据收集

## 仓库结构

```text
rag-system-planner/
├── README.md
├── LICENSE
├── examples/                          # 工作流示例和渲染器输出示例
├── artifacts/rag-wiki-template/       # 可持久化的 RAG 知识工作区模板
├── cursor/rules/                      # Cursor 适配
├── kiro/steering/                     # Kiro 适配
└── skills/rag-system-planner/
    ├── SKILL.md                       # 核心：触发条件 + 决策框架 + 工作流
    ├── agents/openai.yaml             # OpenAI 平台适配
    ├── references/                    # 按需加载的领域知识库
    │   ├── intake-checklist.md
    │   ├── retrieval-design.md
    │   ├── embedding-choice.md
    │   ├── vector-db-choice.md
    │   ├── multimodal-retrieval.md
    │   ├── agent-framework-choice.md
    │   ├── eval-design.md
    │   ├── observability-design.md
    │   ├── diagnosis-playbook.md
    │   ├── artifact-workflow.md
    │   ├── artifact-maintenance-contract.md
    │   ├── artifact-operation-checklists.md
    │   └── reference-to-artifact-map.md
    ├── scripts/
    │   ├── render_rag_plan.py         # greenfield 方案渲染器
    │   └── render_rag_diagnostic.py   # 诊断报告渲染器
    └── templates/                     # 结构化输出模板
```

## 局限性与后续方向

| 当前局限 | 后续可能方向 |
|---------|------------|
| 纯知识层 Skill，没有运行时服务 | 如果需要自动化集成（如自动拉取 trace 数据），可以加轻量 proxy，但要避免过度工程化 |
| renderer 脚本没有测试 | 加 2-3 个 pytest 用例，验证关键输入的渲染结果 |
| 失败模式库基于有限的案例归纳 | 随着真实场景积累，持续扩展 failure mode 覆盖 |
| 缺少 Skill 自身的评测机制 | 设计一组标准化的 RAG 场景描述，验证 Skill 输出的一致性和决策质量 |
| 没有用户反馈数据 | 如果有真实团队使用，收集使用数据反哺 triage matrix 和 reference 内容 |

## License

MIT
