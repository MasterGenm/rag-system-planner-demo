# rag-system-planner

 RAG 规划与诊断 skill，重点是控制升级复杂度。

<p align="center">
  <a href="#核心问题">问题</a> ·
  <a href="#这个-skill-到底做什么">作用</a> ·
  <a href="#它是怎么工作的">工作方式</a> ·
  <a href="#仓库里包含什么">内容</a> ·
  <a href="#安装">安装</a> ·
  <a href="#仓库结构">结构</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenAI_Codex_CLI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Codex CLI">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/Kiro-232F3E?style=flat-square&logo=amazon&logoColor=white" alt="Kiro">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square" alt="OpenClaw">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square" alt="OpenCode">
  <img src="https://img.shields.io/badge/Language-English%20%7C%20中文-blue?style=flat-square" alt="Languages">
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

## 这个 skill 到底做什么

这个 skill 帮团队回答一个很实际的问题：

**这个 RAG 系统下一步到底该修什么，哪些升级现在还不该做？**

它适合处理：

- RAG 架构取舍
- retrieval 故障诊断
- eval / observability 设计
- 判断 plain RAG 何时该保持简单，何时才值得升级到 hybrid / graph / agentic workflow

它不是一个“默认推荐更复杂架构”的 skill。它最重要的价值，是把决策顺序拉回到更稳的轨道上。

| 团队常见做法 | 这个 planner 会强迫团队先做什么 |
|---|---|
| 先改基础设施 | 先说清失败模式：retrieval、ranking、generation 还是 observability |
| 因为某个工具听起来更生产级就提前升级 | 先保住最小 baseline，再明确 tradeoff |
| 从 plain RAG 直接跳到 graph / agentic RAG | 只有分支条件和工作流需求真实存在时才升级 |

## 它是怎么工作的

<img width="778" height="760" alt="流程描述" src="https://github.com/user-attachments/assets/c8a9cc3a-7bac-4c8a-addd-0cd09c9632ae" />


这个 skill 有两种主模式。

### 1. 绿地模式

用于设计一个新 RAG 系统，或替换一个旧系统的大部分结构。

它会：

- 先澄清问题、用户和约束
- 默认先处理 retrieval 设计
- 只在需要时补读额外 reference
- 最后产出完整方案包

### 2. 诊断模式

用于系统已经存在，但出现了召回差、排序差、幻觉、高延迟、缺引用、难调试等问题。

它会：

- 从症状开始，而不是从猜测开始
- 给每条假设贴上 `observed / inferred / unknown`
- 跳到最相关的排障 reference
- 最后给出有优先级的修复路径

### 3. 比较型请求

如果用户主要在比较选项，这个 skill 不会额外开第三条主流程。它会留在当前模式里，改用一个更轻的决策备忘录输出：

1. 决策背景
2. 比较的选项
3. 推荐结论
4. 为什么适合
5. 为什么不选别的
6. 什么条件会改变当前结论

## 仓库里包含什么

核心 skill 在 [`skills/rag-system-planner`](skills/rag-system-planner)。

### 核心文件

- `SKILL.md`
  触发 description 和主工作流说明。
- `agents/openai.yaml`
  skill 列表和 UI metadata。

### References

- `intake-checklist.md`
  需求不清时先问什么。
- `retrieval-design.md`
  chunking、metadata、retrieval strategy、reranking、graph retrieval、web fallback、abstention。
- `embedding-choice.md`
  hosted / local、multilingual、tradeoff。
- `vector-db-choice.md`
  FAISS、Chroma、Qdrant、Milvus 以及存储权衡。
- `multimodal-retrieval.md`
  OCR、截图、图表、表格等非纯文本证据。
- `agent-framework-choice.md`
  什么时候 LangGraph / tool use / bounded agentic RAG 才真的值得上。
- `eval-design.md`
  offline eval、judge-based eval、graph / agentic eval、dataset design。
- `observability-design.md`
  tracing、logs、runtime signals、minimum dashboards。
- `diagnosis-playbook.md`
  symptom-driven 排障和 triage 顺序。

### Scripts

- `render_rag_plan.py`
  把结构化绿地方案渲染成 Markdown。
- `render_rag_diagnostic.py`
  把结构化诊断报告渲染成 Markdown。

这些脚本只负责格式化输出，不负责做架构判断。

## 安装

这个仓库提供一个核心 `SKILL.md`，再加上 `Cursor` / `Kiro` 这类需要规则或 steering 文件的轻量适配。

### Claude Code

```bash
mkdir -p ~/.claude/skills/rag-system-planner
curl -o ~/.claude/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner/main/skills/rag-system-planner/SKILL.md
```

### OpenAI Codex CLI

```bash
mkdir -p ~/.codex/skills/rag-system-planner
curl -o ~/.codex/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner/main/skills/rag-system-planner/SKILL.md
```

### Cursor

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/rag-system-planner.mdc \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner/main/cursor/rules/rag-system-planner.mdc
```

### Kiro

```bash
mkdir -p .kiro/steering
curl -o .kiro/steering/rag-system-planner.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner/main/kiro/steering/rag-system-planner.md

mkdir -p .kiro/skills/rag-system-planner
curl -o .kiro/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner/main/skills/rag-system-planner/SKILL.md
```

### OpenClaw

```bash
mkdir -p ~/.openclaw/skills/rag-system-planner
curl -o ~/.openclaw/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner/main/skills/rag-system-planner/SKILL.md
```

### OpenCode

```bash
mkdir -p ~/.config/opencode/skills/rag-system-planner
curl -o ~/.config/opencode/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner/main/skills/rag-system-planner/SKILL.md
```

### Google Antigravity

```bash
mkdir -p ~/.gemini/antigravity/skills/rag-system-planner
curl -o ~/.gemini/antigravity/skills/rag-system-planner/SKILL.md \
  https://raw.githubusercontent.com/MasterGenm/rag-system-planner/main/skills/rag-system-planner/SKILL.md
```

## 仓库结构

```text
rag-system-planner/
├─ README.md
├─ README.zh-CN.md
├─ LICENSE
├─ .gitignore
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
      └─ scripts/
```

## 总结

`rag-system-planner` 是一个 **bounded-complexity RAG planner**。

它最适合帮助团队判断：

- 真正的失败模式是什么
- 下一步该修哪一层
- 哪些升级现在应该延后
- 规划 RAG 什么时候该保持简单，什么时候才值得受控升级
