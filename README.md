# rag-system-planner

RAG 规划与诊断 skill，重点是控制升级复杂度，并把会重复出现的判断沉淀成 durable artifacts，而不是只留在聊天里。

<p align="center">
  <a href="#核心问题">核心问题</a> ·
  <a href="#现在这个-skill-是什么">现在这个 skill 是什么</a> ·
  <a href="#两层模型">两层模型</a> ·
  <a href="#主要工作流">主要工作流</a> ·
  <a href="#从哪里开始">从哪里开始</a> ·
  <a href="#仓库里有什么">仓库里有什么</a> ·
  <a href="#安装">安装</a>
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

- 还没确认瓶颈，就先换向量库
- 真问题是排序，却先重做 chunking
- 真问题是缺评测和可观测性，却先怪模型不够强
- plain RAG 还没稳定，就急着升级到 graph / agentic RAG

`rag-system-planner` 的目标，是把这些分叉口变成更清楚、更有顺序、也更不容易拍脑袋的决策。

| 团队常见做法 | 这个 skill 会强迫团队先做什么 |
| --- | --- |
| 先改基础设施 | 先说清失败模式：retrieval、ranking、generation 还是 observability |
| 因为某个工具“听起来更生产级”就提前升级 | 先保住最小 baseline，再明确 tradeoff |
| 从 plain RAG 直接跳到 graph / agentic RAG | 只有分支条件和工作流需求真实存在时才升级 |

## 现在这个 skill 是什么

这个 skill 现在不只是一个一次性的 RAG 顾问 prompt。

它已经是一个 **artifact-aware 的 RAG planner**：

- 会做 `greenfield` 规划
- 会做 `diagnosis` 分诊
- 会做轻量 `comparison`
- 会把值得复用的结论写回 durable artifacts

适合处理的场景：

- RAG 架构取舍
- retrieval 故障诊断
- eval / observability 设计
- 判断 plain RAG 何时该保持简单，何时才值得升级到 hybrid / graph / agentic workflow
- 把 recurring failure modes、stack decisions、case notes、evaluation heuristics 沉淀成工作区资产

核心 skill 在 [skills/rag-system-planner/SKILL.md](skills/rag-system-planner/SKILL.md)。

## 两层模型

现在的 skill 明确分成两层：

### 1. `planner`

负责有边界的判断：

- `greenfield`
- `diagnosis`
- `comparison`

### 2. `artifact-maintenance`

负责 durable workspace 的维护：

- `ingest`
- `query`
- `lint`
- `index`

一句话说：

- `planner` 负责判断下一步该做什么
- `artifact-maintenance` 负责把这些会再次出现的判断保存下来

如果你只想得到一份方案或诊断，停在 `planner` 也可以。
如果你希望团队以后不再重复推理同一件事，就需要 `artifact-maintenance`。

## 主要工作流

### 1. Greenfield

用于设计一个新 RAG 系统，或替换一个旧系统的大部分结构。

输出重点：

- assumptions and constraints
- recommended stack
- retrieval design
- evaluation plan
- observability plan
- phased rollout
- durable artifact summary

### 2. Diagnosis

用于系统已经存在，但出现了召回差、排序差、幻觉、高延迟、缺引用、难调试等问题。

这个流程现在是 **triage-first**：

1. 先描述症状
2. 先读已有 workspace
3. 从 failure taxonomy 的 triage matrix 开始
4. 落到最接近的 canonical failure page
5. 给每条假设贴上 `observed / inferred / unknown`
6. 再补 retrieval / eval / observability 的静态 references

### 3. Comparison

用于比较几个 bounded 选项，而不是重做整个系统设计。

默认输出一个轻量 decision memo：

1. Decision context
2. Options compared
3. Recommendation
4. Why this fits
5. Not chosen because
6. What would change the decision

### 4. Artifact-Maintenance

当结论值得复用时，不要只把它留在 chat 里。

这一层负责：

- 把原始证据收进 `sources/`
- 把 recurring knowledge 收进 `wiki/`
- 把暂时有用但还不够 canonical 的结果放进 `queries/`
- 刷新 `index.md`、hub pages 和 `log.md`

## 从哪里开始

按你想做的事选入口。

### 只想直接用 skill

从这里开始：

- [skills/rag-system-planner/SKILL.md](skills/rag-system-planner/SKILL.md)
- [skills/rag-system-planner/references/diagnosis-playbook.md](skills/rag-system-planner/references/diagnosis-playbook.md)
- [skills/rag-system-planner/references/retrieval-design.md](skills/rag-system-planner/references/retrieval-design.md)

### 想理解 durable artifact 模型

从这里开始：

- [skills/rag-system-planner/references/artifact-workflow.md](skills/rag-system-planner/references/artifact-workflow.md)
- [skills/rag-system-planner/references/artifact-maintenance-contract.md](skills/rag-system-planner/references/artifact-maintenance-contract.md)
- [artifacts/rag-wiki-template/README.md](artifacts/rag-wiki-template/README.md)
- [artifacts/rag-wiki-template/ADOPTION.md](artifacts/rag-wiki-template/ADOPTION.md)
- [artifacts/rag-wiki-template/AGENTS.md](artifacts/rag-wiki-template/AGENTS.md)
- [artifacts/rag-wiki-template/index.md](artifacts/rag-wiki-template/index.md)

### 想先看真实示例

从这里开始：

- [examples/README.md](examples/README.md)
- [examples/sample-rag-end-to-end.md](examples/sample-rag-end-to-end.md)
- [examples/sample-rag-planner-handoff.md](examples/sample-rag-planner-handoff.md)
- [examples/sample-rag-real-walkthroughs.md](examples/sample-rag-real-walkthroughs.md)
- [artifacts/rag-wiki-template/wiki/failure-modes/triage-matrix.md](artifacts/rag-wiki-template/wiki/failure-modes/triage-matrix.md)

## 仓库里有什么

### Skill

- [skills/rag-system-planner/SKILL.md](skills/rag-system-planner/SKILL.md)
- [skills/rag-system-planner/agents/openai.yaml](skills/rag-system-planner/agents/openai.yaml)

### References

静态参考主要分成两类：

- 判断层
  - [intake-checklist.md](skills/rag-system-planner/references/intake-checklist.md)
  - [retrieval-design.md](skills/rag-system-planner/references/retrieval-design.md)
  - [embedding-choice.md](skills/rag-system-planner/references/embedding-choice.md)
  - [vector-db-choice.md](skills/rag-system-planner/references/vector-db-choice.md)
  - [multimodal-retrieval.md](skills/rag-system-planner/references/multimodal-retrieval.md)
  - [agent-framework-choice.md](skills/rag-system-planner/references/agent-framework-choice.md)
  - [eval-design.md](skills/rag-system-planner/references/eval-design.md)
  - [observability-design.md](skills/rag-system-planner/references/observability-design.md)
  - [diagnosis-playbook.md](skills/rag-system-planner/references/diagnosis-playbook.md)
- durable artifact 层
  - [artifact-workflow.md](skills/rag-system-planner/references/artifact-workflow.md)
  - [artifact-maintenance-contract.md](skills/rag-system-planner/references/artifact-maintenance-contract.md)
  - [artifact-operation-checklists.md](skills/rag-system-planner/references/artifact-operation-checklists.md)
  - [reference-to-artifact-map.md](skills/rag-system-planner/references/reference-to-artifact-map.md)

### Templates

phase 1 已经带上了最小模板集：

- [skills/rag-system-planner/templates](skills/rag-system-planner/templates)
- [artifacts/rag-wiki-template/templates](artifacts/rag-wiki-template/templates)

### Artifact Scaffold

[artifacts/rag-wiki-template](artifacts/rag-wiki-template) 是一个可复制的 durable workspace。

它包含：

- `sources/`
  原始证据
- `wiki/`
  failure modes、patterns、evaluations、stack decisions、case notes
- `queries/`
  暂时有用但未必 canonical 的 memo
- `index.md`
  根导航
- `log.md`
  维护日志

### Examples

完整列表见 [examples/README.md](examples/README.md)。

重点例子：

- [sample-rag-plan.md](examples/sample-rag-plan.md)
- [sample-rag-diagnostic.md](examples/sample-rag-diagnostic.md)
- [sample-rag-end-to-end.md](examples/sample-rag-end-to-end.md)
- [sample-rag-planner-handoff.md](examples/sample-rag-planner-handoff.md)
- [sample-rag-real-walkthroughs.md](examples/sample-rag-real-walkthroughs.md)

## 明确不做什么

当前主线还不做这些：

- `health / drift / repair`
- optional mirror 语义
- memory engine 绑定
- vector DB / graph DB 的 repo 级强绑定
- helper scripts for sync / drift / repair
- 把这个仓库直接扩成完整 document engine

这些内容仍然只放在本地 workbench 里探索，不是正式主线的一部分。

## 渲染脚本

仓库里仍然保留两个 renderer：

- `scripts/render_rag_plan.py`
- `scripts/render_rag_diagnostic.py`

它们只负责把已经形成的结构化结论渲染成 Markdown，不负责替你做架构判断。

## 安装

这个仓库提供一个核心 `SKILL.md`，再加上 `Cursor` / `Kiro` 这类需要规则或 steering 文件的轻量适配。

### Claude Code

```bash
mkdir -p ~/.claude/skills/rag-system-planner
curl -o ~/.claude/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/skills/rag-system-planner/SKILL.md
```

### OpenAI Codex CLI

```bash
mkdir -p ~/.codex/skills/rag-system-planner
curl -o ~/.codex/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/skills/rag-system-planner/SKILL.md
```

### Cursor

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/rag-system-planner.mdc \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner-demo/main/cursor/rules/rag-system-planner.mdc
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

## 仓库结构

```text
rag-system-planner/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ artifacts/
│  └─ rag-wiki-template/
├─ examples/
├─ cursor/
│  └─ rules/
│     └─ rag-system-planner.mdc
├─ kiro/
│  └─ steering/
│     └─ rag-system-planner.md
└─ skills/
   └─ rag-system-planner/
      ├─ SKILL.md
      ├─ agents/
      │  └─ openai.yaml
      ├─ references/
      ├─ templates/
      └─ scripts/
```

## 总结

`rag-system-planner` 现在是一个 **artifact-aware, bounded-complexity RAG planner**。

它最适合帮助团队判断：

- 真正的失败模式是什么
- 下一步该修哪一层
- 哪些升级现在应该延后
- 哪些结论值得沉淀成 durable artifacts

如果你只想做一次性分析，从 [skills/rag-system-planner/SKILL.md](skills/rag-system-planner/SKILL.md) 开始。
如果你想让团队逐步积累自己的 RAG case law，就从 [artifacts/rag-wiki-template](artifacts/rag-wiki-template) 和 [examples/README.md](examples/README.md) 开始。
