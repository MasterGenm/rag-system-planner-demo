---
title: Court Logic capstone
case_id: CASE-0001
case_source: https://medium.com/@pliu27/we-built-an-ai-that-argues-like-the-supreme-court-heres-what-we-learned-80a6823bd134
case_type: retrospective_application
source_published_at: 2026-04-20
retrieved_at: 2026-04-27
estimated_failure_family: retrieval
last_validated_at: 2026-04-27
derived_from: [https://medium.com/@pliu27/we-built-an-ai-that-argues-like-the-supreme-court-heres-what-we-learned-80a6823bd134]
owner: <owner>
stale_after_days: 365
---

## 背景

Court Logic 是 UC Berkeley MIDS capstone 项目，目标是把 2021-2025 年完成的美国最高法院意见书转成可检索语料，让系统围绕用户提交的法律问题模拟不同法官联盟的辩论与结构化判决意见。原文说明系统依赖 Court Listener API、结构化 JSON、per-justice FAISS store、coalition-level index 和 curated gold standard dataset。

## 输入证据

本段只记录背景与 symptom，用于独立判断；此时不使用原文后续 ablation、GraphRAG 比较或最终 outcome。

- 出处段落：`Building the Data Pipeline: Five Years of Judicial Opinion`，原文 lines 55-60。
- 原文短摘：`grounded in real judicial writing`。
- 证据说明：系统必须从真实司法意见书中检索支持性法律论证；语料是长篇、结构化、跨段落推理文本。原文在同一段说明使用 `RecursiveCharacterTextSplitter`，并指出 chunking 是关键决策。
- 出处段落：`Evaluation: How Do You Grade a Fake Supreme Court?`，原文 lines 104-110。
- 证据说明：系统用 outcome accuracy、key-point coverage、LLM-as-a-judge、RAGAS context precision/recall 等指标评估，baseline symptom 包含 outcome accuracy 15.4%，说明问题不是单纯 UI 或响应格式问题，而是检索上下文是否支撑法律推理的问题。

## Skill 给出的判断

- mode: diagnosis
- failure_family: retrieval
- evidence_labels: [observed, inferred, unknown]
- next_action_class: investigate_chunking
- must_avoid 触发：[graph_rag, multi_agent_rewrite]
- 判断中识别到的次要 failure 信号：observability 已有一定基础，因为原文提到 gold standard、RAGAS 和多轮 evaluation；generation 质量可能受上下文连续性影响，但当前 evidence 不足以把主因判成 generation。

独立判断理由：

- observed: 语料是司法意见书，答案质量依赖多段法律推理；baseline outcome accuracy 为 15.4%。
- observed: 系统已经显式把 chunking 作为关键 pipeline step。
- inferred: 法律推理容易被过小 chunk 切断，首要调查应是 chunk size、overlap、section-aware boundaries 和 retrieved context continuity。
- unknown: 当前 evidence 尚未展示 retrieved chunk ids、per-query misses、top-k 分布或 chunk-level failure examples，因此不能断言 embedding 或 reranker 是根因。

推荐调查顺序：

- Now: 固定 evaluation set，做 chunk size/overlap 与 section-aware splitting ablation。
- Next: 检查 retrieved context 是否覆盖完整 legal reasoning chain，而不只覆盖单句 precedent。
- Later: 在 chunking baseline 明确后，再比较 graph retrieval 或 coalition architecture 的收益。

## 原作者实际采取的行动

原作者后续做了系统化 evaluation 与 chunking ablation。

- 出处段落：`The Chunking Ablation That Changed Everything`，原文 lines 111-119。
- 行动记录：团队固定其他参数，系统性改变 chunk size 与 overlap，并比较 outcome accuracy、key-point coverage 和 LLM judge 分数。
- 行动记录：团队同时保留 RAGAS 对 retrieval pipeline 的独立评估，避免只看最终生成文本。
- 行动记录：原作者还测试了 GraphRAG，但把它作为 challenger，而不是直接替换 standard RAG。

## 后续观察到的结果

- 出处段落：`Evaluation` 与 `The Chunking Ablation That Changed Everything`，原文 lines 110-119。
- 结果记录：22 次 evaluation run 后，outcome accuracy 从 15.4% 提升到 46.2%，key-point coverage 从 0.115 提升到 0.564。
- 结果记录：chunk size 2000、overlap 300 是最佳配置；这说明 legal reasoning 的上下文连续性比更小 chunk 更重要。
- 出处段落：`Graph RAG: A Promising Challenger`，原文 lines 120-124。
- 结果记录：GraphRAG 在 k=15 时达到 38.5% outcome accuracy，接近但没有超过 standard RAG 的最佳 46.2%；k 的增加也不是单调收益。

## 一致性分析

- 与原作者判断一致的点：Skill 在只看 baseline symptom 与 chunking/legal context 时，把主因指向 retrieval/chunking，和原作者后续 ablation 的最强发现一致。
- 与原作者判断一致的点：Skill 建议先做 chunking ablation，再谈 GraphRAG；原作者实际结果也显示 GraphRAG 有潜力但不是最优结果。
- 不一致的点：Skill 的 `must_avoid: graph_rag` 比原作者更保守。原作者确实测试了 GraphRAG，并发现它在较少 retrieved passages 下有一定 targeted reasoning chain 优势。
- 不一致是否揭示 Skill 的盲区：部分揭示。Skill 对 GraphRAG 的默认克制是合理的，但应该允许在 evaluation 对照实验中把 GraphRAG 作为 bounded challenger，而不是把任何 GraphRAG 实验都视为过早升级。

## 学到的教训

这个 case 中 Skill 表现较好：它会优先调查 chunking/context continuity，而不是直接要求更复杂架构。真正有价值的补充是把 `must_avoid` 表述得更细：避免过早生产化 GraphRAG，但允许在固定 hard-case set 上做 bounded experiment。
