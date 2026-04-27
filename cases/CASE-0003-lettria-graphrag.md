---
title: Lettria GraphRAG
case_id: CASE-0003
case_source: https://qdrant.tech/blog/case-study-lettria-v2/
case_type: retrospective_application
source_published_at: 2025-06-17
retrieved_at: 2026-04-27
estimated_failure_family: ranking
last_validated_at: 2026-04-27
derived_from: [https://qdrant.tech/blog/case-study-lettria-v2/]
owner: <owner>
stale_after_days: 365
---

## 背景

Lettria 面向金融、航空航天、制药、法律等高准确性行业做复杂文档智能。语料包含监管文档、复杂 PDF、表格、图表和专业术语；业务要求不仅是答案正确，还包括可解释性、lineage、auditability 和可追踪引用链。

## 输入证据

本段只记录背景与 symptom，用于独立判断；此时不使用原文后续 GraphRAG action、Qdrant/Neo4j pipeline 或 outcome。

- 出处段落：`Why Complex Document Intelligence Needs More Than Just Vector Search`，原文 lines 117-121。
- 原文短摘：`more explainable outputs`。
- 证据说明：Lettria 的客户场景是 regulated industries，要求 precision、auditability、accuracy；原文指出复杂 PDF、tables、diagrams、charts 等结构化/半结构化材料需要比普通 vector-only RAG 更强的文档理解。
- 出处段落：`Why Traditional RAG Fell Short in High-Stakes Use Cases`，原文 lines 122-124。
- 原文短摘：`around 70% accuracy`。
- 证据说明：传统 vector search 在复杂监管和专业文档上约 70% accuracy，不满足 precision non-negotiable 的场景；同时 LLM 输出的理解和审计存在明显困难。

## Skill 给出的判断

- mode: diagnosis
- failure_family: ranking
- evidence_labels: [observed, inferred, unknown]
- next_action_class: inspect_ranking
- must_avoid 触发：[graph_rag, multi_agent_rewrite]
- 判断中识别到的次要 failure 信号：retrieval 表示结构化证据可能未进入候选集；observability 表示 lineage/auditability 是强约束；generation 不是首要，因为当前 symptom 更像 evidence selection 与 traceability 不足。

独立判断理由：

- observed: vector-only RAG 在高风险复杂文档上 accuracy 不够，且审计输出困难。
- observed: 文档包含 tables、diagrams、专业术语和监管上下文，结构信号对证据选择重要。
- inferred: 首要调查应是候选集是否包含正确证据、结构 metadata 是否保留、ranking 是否把可审计证据排到前面，而不是立即生产化 GraphRAG。
- unknown: 当前 evidence 未展示 vector baseline 的 query slices、top-k misses、reranker inputs、metadata filters 或 graph extraction quality，因此不能直接判定 GraphRAG 是必要路径。

推荐调查顺序：

- Now: 对 high-stakes query set 做 vector/hybrid/rerank baseline，记录 retrieved ids、scores、metadata、lineage anchors。
- Next: 检查 ranking 是否能优先返回带表格、图表、术语和出处 lineage 的证据块。
- Later: 只有当结构 traversal query family 被 baseline 稳定证明无法覆盖时，再设计 GraphRAG route 和 graph extraction validation。

## 原作者实际采取的行动

原作者最终选择了 GraphRAG 路径，并把 Qdrant vector search 与 Neo4j knowledge graph 组合。

- 出处段落：`Building the document understanding and extraction pipeline`，原文 lines 129-138。
- 行动记录：Lettria 将 complex PDFs 转成 dense vector embeddings 和 semantic triples，保留 lineage metadata，并用 vector search seed points 扩展 Neo4j contextual subgraph。
- 出处段落：`The ingest transaction mechanism`，原文 lines 139-146。
- 行动记录：团队实现 Neo4j/Qdrant 一致写入机制，避免图数据库和向量库状态不一致。
- 出处段落：`Consistent querying and indexing through payload flattening`，原文 lines 176-181。
- 行动记录：团队 flatten payload，并为常用 filter 字段添加 payload indexes，同时拆分 hot/cold vectors 控制内存与延迟。

## 后续观察到的结果

- 出处段落：`Outcome: >20% accuracy improvement`，原文 lines 182-188。
- 结果记录：Graph-enhanced RAG 相比 pure vector solutions 在 finance、aerospace、pharmaceuticals、legal 等 verticals 获得 20-25% accuracy uplift。
- 结果记录：系统提供 document ingestion 到 query response 的 explainability 和 lineage tracking，并在 1-2 秒 query latency 下被客户接受为 audit-grade accuracy。
- 出处段落：`Scaling to >100M vectors at <200ms P95 retrieval`，原文 lines 179-181。
- 结果记录：Qdrant deployment 扩展到超过 100M vectors，并在 production-like load tests 下维持 P95 retrieval latency 低于 200ms。

## 一致性分析

- 与原作者判断一致的点：Skill 正确识别这不是普通 prompt 问题，而是 ranking/retrieval/lineage 的证据选择问题。
- 与原作者判断一致的点：Skill 要求先保留 lineage anchors、metadata、retrieved ids 和可审计证据，这与 Lettria 最终系统强调 lineage 和 auditability 一致。
- 不一致的点：Skill 的 `must_avoid: graph_rag` 会把 GraphRAG 视为默认应延后的复杂升级；原作者最终证明，在 regulated complex-document 场景中 GraphRAG 的成本是合理的，并带来 20-25% accuracy uplift。
- 不一致的点：Skill 的 next_action 是先做 bounded ranking inspection，而原作者实际采用了 vector + graph dual representation、ontology generation、graph expansion 和一致写入机制。
- 不一致是否揭示 Skill 的盲区：是。Lettria 场景具备高准确性要求、监管文档、表格/图表、专业术语、可解释性、lineage 和 audit-grade 输出要求，这些特征让 GraphRAG 不再只是炫技升级，而是满足业务约束的结构化检索路径。

## 学到的教训

此 case 揭示 Skill 的克制升级原则在哪些语境下需要补充例外条件：当场景同时具备高风险行业、复杂半结构化文档、强 lineage/auditability 要求、vector-only baseline 明确不足、并且团队能验证 graph extraction 与双写一致性时，`must_avoid: graph_rag` 应从硬性避免变成语境化延后。这个观察只记录在 case 中，本批次不修改 Skill。
