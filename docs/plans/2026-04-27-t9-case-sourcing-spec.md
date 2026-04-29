# T9 案例素材调研与制作子规格

> 父规格：[2026-04-26-implementation-spec.md](2026-04-26-implementation-spec.md) 第 3 节 T9
> 本文档把 T9 从"等待发起人提供素材"细化为"基于公开 postmortem 的回顾性应用案例"路径。
> 本文档对父规格 T9 节的反目标全部继承。

---

## 0. 给执行方 AI 的元说明（必读）

### 0.1 你是谁、做什么

你被指派为 T9 的执行方。

T9 在父规格中设定的"前置：发起人提供原始材料"已经被替换为：**基于公开 postmortem 的回顾性应用案例**。这不是降低标准，而是承认目前仓库尚未投入真实生产使用、不能凭空编造案例。

你的任务有两阶段：

- **阶段一（本批次执行）**：调研公开来源，形成 5–8 篇候选短列表。
- **阶段二（后续批次执行）**：等发起人从短列表挑选 3 篇后，按规定结构写出 3 个 case 文件 + 索引。

**本次启动只执行阶段一。阶段二需等发起人新指令。不得跨阶段推进。**

### 0.2 不可逾越的红线

1. **不要在阶段一写任何 case 文件**。仅产出短列表。
2. **不要自行决定最终选哪 3 篇**。case selection 是判断，必须由发起人做。
3. **不要伪装成"我们用 Skill 帮 XXX 公司做了诊断"**。所有 case 文件必须明写 `case_type: retrospective_application`。
4. **不要用 LLM 总结改写代替原文摘录**。case 中的 symptom / action / outcome 段必须可追溯到原文段落。
5. **不要采用付费墙文章**，即使能找到镜像或盗版。
6. **不要采用纯 marketing 软文**（厂商客户成功故事中没有诊断细节的那类）。
7. **不要采用 GitHub issue / Reddit / HackerNews / Twitter 线程**作为主要源（可作为反向找原文的索引）。
8. **不要 `git push`，不要建议 push**，不要引入远端模拟器。所有 commit 保留本地。

### 0.3 中英文约定

- 文档：中文为主，技术术语保留英文。
- 字段名 / 文件名 / commit message：英文。
- frontmatter 字段值：URL / 日期等保留原始形式。

---

## 1. 任务本质澄清

T9 要的不是"RAG 数据集"，是"RAG 系统真实复盘叙事"。两者的差异：

| 维度 | RAG 数据集（Kaggle / KILT / BEIR / HotpotQA 等） | RAG postmortem（本任务需要的） |
|------|---------|---------|
| 内容形态 | query + docs + 期望答案 | 人写的复盘文章 |
| 是否含 diagnosis | 否 | 是（核心） |
| 是否含 action taken | 否 | 是（核心） |
| 是否含 outcome | 否 | 是（核心） |
| 是否可做 T9 case | ❌ | ✅ |

如果你在调研中找到的全部是数据集，**调研路径就跑偏了**，应回到 §2 的源池重新检索。

---

## 2. 源池分级

### A 级（优先在这几类里找）

- **向量数据库厂商博客的 case study**：Pinecone、Weaviate、Qdrant、Chroma、Milvus
  - 注意区分"客户成功故事软文"和"真实工程复盘"。判断标准见 §3。
- **AI 公司官方 cookbook 中的"问题→修复"案例**：Anthropic Cookbook、OpenAI Cookbook、Cohere Cookbook、Voyage AI 博客
- **评测 / 可观测性厂商的客户案例**：Arize AI、LangSmith（LangChain Blog）、Phoenix（Arize Phoenix）
  - 这些通常带 before/after 指标对比

### B 级（信号好但需要严格筛选）

- **LangChain / LlamaIndex / Haystack 的 use-case 博客**：多数是宣传，少数是真复盘
- **工程师个人或公司技术博客**：Substack、Medium、Hashnode、dev.to、公司 Engineering Blog
  - 关键词建议：
    - `"RAG postmortem"`
    - `"RAG lessons learned"`
    - `"we built a RAG system" + "what we learned"`
    - `"fixing RAG retrieval"`
    - `"debugging RAG"`
    - `"RAG in production" + 厂商名`
- **arXiv industry track case study**：少见但偶有高质量

### C 级（跳过）

- HackerNews / Reddit / Twitter / 推特线程：可作为反向找原文的索引，不作主要源
- 厂商 case study 中"匿名 Fortune 500 客户"类文章：细节被洗
- 纯学术 benchmark 论文：结构不对
- GitHub issue：信息片段化、缺 outcome
- 视频 / 播客转录：信噪比太低

---

## 3. 候选筛选 checklist

每个候选都要逐项过。任意一项缺失 → **不进入**短列表。

| 必备项 | 说明 |
|------|------|
| ✅ 公开可访问 URL | 不要付费墙、不要内部链接 |
| ✅ 发布时间 ≤ 24 个月 | 避免技术堆栈过时（例如仍在用 OpenAI ada-002 的早期文章） |
| ✅ 明确的 RAG 系统场景描述 | 不是泛谈，是具体业务上下文 |
| ✅ 明确的 symptom 描述 | "answer 不准"不够，要有具体例子 |
| ✅ 至少一段 diagnosis 推理 | 作者写了"我们怀疑是 X，验证后发现是 Y" |
| ✅ 明确的 action taken | 改了什么具体的东西 |
| ✅ outcome / measured result | **最关键**——前后对比、指标、定性观察都行，但必须有 |

---

## 4. 最终 3 篇必须满足的多样性要求

短列表（5–8 篇）不强制覆盖，但要保证发起人从中选出 3 篇时**有可能满足**以下三项：

- ≥ 1 篇属于 **retrieval / ranking** family（chunking、metadata、filter、reranker 类失败）
- ≥ 1 篇属于 **generation / observability** family（prompt assembly、citation、缺 trace 类失败）
- ≥ 1 篇是**潜在反例**：原作者最终选择了 graph RAG / multi-agent 重写。这一篇用来测试 Skill 是否会触发 `must_avoid: graph_rag` 与原作者不一致——一致性差异本身就是有价值的 case

短列表中至少要含 1 篇候选标注为"潜在反例"，否则要补找直到满足。

---

## 5. 执行步骤

```
Step 1: 调研（本批次）
   - 在 §2 的 A/B 级源池中检索
   - 用 §3 checklist 过每个候选
   - 形成 5-8 篇候选

Step 2: 输出短列表（本批次）
   - 按 §6 格式输出
   - 提交 commit
   - 写完成报告

【人工决策点】发起人从短列表挑 3 篇并新指令

Step 3: 写 case 文件（后续批次，等新指令）
   - 按 §7 结构写 3 个 case 文件
   - 写 cases/README.md 索引
   - 字段一致性自检

Step 4: 全量回归与提交（后续批次）
```

**本次启动只执行 Step 1–2。** Step 3–4 等发起人新指令再执行。

---

## 6. Step 2 短列表输出格式

短列表落成单一 Markdown 文件：`docs/plans/2026-04-27-t9-candidate-shortlist.md`

文件结构：

```markdown
# T9 候选短列表

> 调研完成时间：<YYYY-MM-DD>
> 调研者：<执行方 AI 标识>
> 候选数量：<N>（要求 5 ≤ N ≤ 8）
> 是否含潜在反例：是 / 否

## 候选 1

- 标题：<原文标题>
- URL：<完整 URL>
- 发布时间：<YYYY-MM>
- 来源类型：A 级 / B 级
- 来源具体类别：<例如 Pinecone Blog / Anthropic Cookbook / 工程师个人博客>
- RAG 场景：<一句话>
- 主要 failure 信号：<一句话>
- diagnosis 是否完整：✅ / ⚠️ / ❌
- action 是否明确：✅ / ⚠️ / ❌
- outcome 是否可量化：✅ / ⚠️ / ❌
- 推测对应 failure_family：retrieval / ranking / generation / observability
- 是否潜在反例（原作者选择 graph_rag / multi_agent）：是 / 否
- 摘要：<2-3 句话，覆盖 problem → diagnosis → action → outcome>

## 候选 2
...

## 调研路径与决策记录

- 检索关键词列表：
- 跳过的来源类型与理由：
- checklist 不通过的候选数量与典型不通过原因：
- 是否遇到付费墙或访问受限：
```

### 6.1 短列表必含字段一致性自检

每条候选必须包含 §6 模板中列出的 12 个字段。提交前自检：任何一条缺字段 → 不要提交，回去补。

---

## 7. Step 4 case 文件结构（后续批次用，本次启动不要写）

文件路径：`cases/2026-04-27-<slug>.md`

```markdown
---
case_id: CASE-0001
case_source: <原文 URL>
case_type: retrospective_application
source_published_at: <YYYY-MM-DD>
retrieved_at: <YYYY-MM-DD>
estimated_failure_family: retrieval | ranking | generation | observability
---

## 背景
<脱敏后的业务场景，一段>

## 输入证据
<从原文摘录的 symptom 与上下文，标明出处段落>

## Skill 给出的判断
- mode: diagnosis
- failure_family: <Skill 判定>
- evidence_labels: [observed, inferred, unknown]
- next_action_class: <枚举>
- must_avoid 触发：<列表 / 无>

## 原作者实际采取的行动
<原文中 action 段的摘录与转述>

## 后续观察到的结果
<原文中 outcome 段的摘录与转述，含指标>

## 一致性分析
- 与原作者判断一致的点：
- 不一致的点：
- 不一致是否揭示 Skill 的盲区：

## 学到的教训
<诚实记录：Skill 在此 case 表现好 / 不好 / 部分好；为什么>
```

`cases/README.md` 必含：
- case 索引表
- 明确声明：**v0.1 cases 全部为 `retrospective_application` 类型；`production_use` 类型留待 v0.2**

---

## 8. 反目标（重申）

- 不要把"软文式 case study"当作真实 postmortem。Pinecone / Weaviate 客户故事中"提升 X% 召回率"但没有诊断细节的文章不入选。
- 不要在 Step 4 自行决定哪 3 篇。
- 不要拿付费墙文章。
- 不要采用 GitHub issue / Reddit / HackerNews 作为主要源。
- 不要为凑数而把不满足 §3 checklist 的候选放进短列表。**短列表 5–8 是上限，不是必达。** 如果筛完只有 3 篇真正合格，照实写 3 篇并在"调研路径与决策记录"段说明，不要灌水。
- 不要修改任何代码或既有文档。本批次仅产出 `docs/plans/2026-04-27-t9-candidate-shortlist.md` 一个文件。

---

## 9. 验收标准

### Step 1–2（本批次）

```bash
test -f docs/plans/2026-04-27-t9-candidate-shortlist.md
grep -c "^## 候选 " docs/plans/2026-04-27-t9-candidate-shortlist.md   # 在 [3, 8] 区间
grep -q "调研路径与决策记录" docs/plans/2026-04-27-t9-candidate-shortlist.md
```

并行人工检查（执行方 AI 自检）：
- 至少 1 个候选标注 `是否潜在反例: 是`
- 所有候选的 URL 实际可访问（执行方 AI 应在调研时已访问过原文，不要靠搜索摘要）
- 所有候选的 §3 checklist 7 项必备全部 ✅

### Step 3–4（后续批次，本次不验收）

由后续指令明确。

---

## 10. 终止条件

如果遇到以下任一情况，**停止动手**，回到发起人确认：

1. A/B 级源池检索完后合格候选不足 3 篇（即使放宽到 24 个月仍然不足）。
2. 找不到任何一篇标注为"潜在反例"的候选。
3. 发现某篇高质量候选实际是付费墙 / 受限访问。
4. 发起人在短列表完成前下达新指令。

不要"自行决定继续"。
