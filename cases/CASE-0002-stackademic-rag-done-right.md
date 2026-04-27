---
title: RAG Done Right
case_id: CASE-0002
case_source: https://blog.stackademic.com/building-a-robust-rag-system-a-comprehensive-architecture-guide-cb27fda02e0b
case_type: retrospective_application
source_published_at: 2025-12-22
retrieved_at: 2026-04-27
estimated_failure_family: generation
---

## 背景

该文章回顾一个 customer support AI 从 weekend naive RAG 演进为 production-grade RAG 的过程。场景包含客户支持、API 文档、政策问答、结构化查询、关系查询、技术文档检索和 answer verification。系统已经进入生产环境，失败会影响客户沟通和业务成交。

## 输入证据

本段只记录背景与 symptom，用于独立判断；此时不使用原文后续 architecture、component fix 或最终结果段。

- 出处段落：`The Problem That Started Everything`，原文 lines 50-58。
- 原文短摘：`citing "documentation" that didn't exist`。
- 证据说明：客户支持 AI 自信地声称已废弃 API feature 仍可用，并引用不存在的文档；一次 enterprise escalation 最终暴露 AI 完全编造 capability，造成 $50K deal loss。
- 出处段落：`What Makes RAG So Hard`，原文 lines 63-70。
- 证据说明：原文进一步指出 bad retrieval 会让模型使用 irrelevant chunks 生成错误答案，并给出 refund policy 查询检索到 shipping policy 后生成虚构退款政策的 symptom。

## Skill 给出的判断

- mode: diagnosis
- failure_family: generation
- evidence_labels: [observed, inferred, unknown]
- next_action_class: tighten_answer_policy
- must_avoid 触发：无
- 判断中识别到的次要 failure 信号：retrieval/routing 明显可疑；observability 也不足，因为初始描述没有显示 retrieved ids、scores、route decision、faithfulness score 或 unsupported-claim trace。

独立判断理由：

- observed: 用户可见失败是 unsupported answer、虚构 capability 和不存在 citation。
- observed: refund policy 问题存在 wrong-context symptom，说明 retrieval/routing 是重要次要信号。
- inferred: 最早应阻止系统在证据不足时继续回答，并要求答案逐句绑定 retrieved context；否则 retrieval 修好前仍会输出高置信幻觉。
- unknown: 当前 evidence 还不足以判定是 chunking、hybrid search、routing classifier、reranker 还是 prompt assembly 的单一根因。

推荐调查顺序：

- Now: 添加 answer policy 和 faithfulness gate，要求 unsupported claims 被标记或拒答。
- Next: 记录 route decision、retrieved chunk ids、scores、context precision/recall，并把 refund-policy 类失败做成 regression query。
- Later: 根据 trace 决定是否引入 routing、hybrid search、semantic splitting 或 reranking。

## 原作者实际采取的行动

原作者没有选择 agentic rewrite，而是逐层补齐 production RAG 组件。

- 出处段落：`Component 1: Query Construction`，原文 lines 80-128。
- 行动记录：增加 query construction，把自然语言问题翻译成 SQL、graph query 或 vector search query；SQL query construction 通过 few-shot examples 提升。
- 出处段落：`Component 2: Routing`，原文 lines 129-218。
- 行动记录：增加 logical routing 与 LLM classifier，把不同查询路由到 relational、graph、vector 或 hybrid 路径。
- 出处段落：`Component 3: Indexing`，原文 lines 219-247。
- 行动记录：把固定 512-token chunking 改成按 section、paragraph、sentence 的 semantic splitting，避免把关键政策句子切断。
- 出处段落：`Groundedness and Hallucination Detection`，原文 lines 920-948。
- 行动记录：实现 groundedness/faithfulness check，检测答案中不受 context 支持的声明。

## 后续观察到的结果

- 出处段落：`Query Construction`，原文 lines 107-128。
- 结果记录：SQL query construction success rate 从 45% 提升到 92%；query construction 将 retrieval failures 从 30% 降到 5% 以下。
- 出处段落：`Routing`，原文 lines 213-218。
- 结果记录：query routing accuracy 从 60% 提升到 87%，平均 latency 为 50ms。
- 出处段落：`Indexing`，原文 lines 247-250。
- 结果记录：semantic splitting 使 retrieval quality 提升 23%，multi-representation indexing 进一步提升 retrieval accuracy。
- 出处段落：`What We Learned the Hard Way`，原文 lines 2227-2266。
- 结果记录：naive RAG 约 60% queries 可用；后续加入 retrieval precision、answer faithfulness、user satisfaction、500 test queries、precision/recall/faithfulness scoring 和 latency benchmarks。

## 一致性分析

- 与原作者判断一致的点：Skill 没有建议 `defer_agentic_upgrade` 或复杂 agent 重写，而是从 answer policy、trace、routing/retrieval evidence 逐步修。
- 与原作者判断一致的点：Skill 识别到 generation 是用户可见主失败，同时保留 retrieval/routing 作为次要 failure signal；原作者实际修复也同时覆盖 answer verification、routing、query construction 和 indexing。
- 不一致的点：Skill 如果只能选一个 `failure_family`，会把最早用户可见失败归到 generation；原作者复盘更强调 retrieval/indexing/routing 的根因链条。
- 不一致是否揭示 Skill 的盲区：不算严重盲区。这是多 failure family 叠加 case，单一 family 标签会损失信息；case 文件应保留 secondary signals，否则会误以为只需要 prompt/answer policy。

## 学到的教训

这个 case 说明 Skill 的单一 `failure_family` 输出需要配套记录次要 failure signals。面对 hallucination + bad retrieval + bad routing 的组合故障，最稳妥路径是先让答案不能无证据输出，同时补齐 trace 和 regression queries，再逐项修 retrieval pipeline。
