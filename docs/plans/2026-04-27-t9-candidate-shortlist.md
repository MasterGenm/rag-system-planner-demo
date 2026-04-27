# T9 候选短列表

> 调研完成时间：2026-04-27
> 调研者：Codex
> 候选数量：7（要求 5 <= N <= 8）
> 是否含潜在反例：是

## 候选 1

- 标题：How Arize Skills Improved RAG Recall from 39% to 75% in 8 Hours
- URL：https://arize.com/blog/how-arize-skills-improved-rag-recall-from-39-to-75-in-8-hours/
- 发布时间：2026-04
- 来源类型：A 级
- 来源具体类别：Arize AI Blog / 评测与可观测性厂商工程复盘
- RAG 场景：基于 OpenSearch、LangGraph 和 GPT-4o-mini 的 self-rag 项目，通过评测闭环持续改进检索质量。
- 主要 failure 信号：Recall@5 初始只有 39%，意味着 61% 查询的正确文档没有进入 top 5。
- diagnosis 是否完整：✅
- action 是否明确：✅
- outcome 是否可量化：✅
- 推测对应 failure_family：retrieval
- 是否潜在反例（原作者选择 graph_rag / multi_agent）：否
- 摘要：文章把问题定位为检索质量上限，而不是生成提示词问题。作者用 Arize experiment、失败模式分析和自动 backlog 扩展驱动索引、chunking、mapping、query expansion、reranking 等改动。8 小时后 Recall@5 从 39% 提升到 75%，适合检验 Skill 是否优先定位 retrieval/ranking 而不是盲目调 prompt。

## 候选 2

- 标题：GraphRAG: How Lettria Unlocked 20% Accuracy Gains with Qdrant and Neo4j
- URL：https://qdrant.tech/blog/case-study-lettria-v2/
- 发布时间：2025-06
- 来源类型：A 级
- 来源具体类别：Qdrant Blog / 向量数据库厂商 case study
- RAG 场景：Lettria 在金融、航空航天、制药、法律等高准确性文档智能场景中，将 Qdrant vector search 与 Neo4j knowledge graph 组合成 GraphRAG。
- 主要 failure 信号：传统 vector-only RAG 在复杂监管文档、表格、图表和专业术语场景中约 70% accuracy，不满足高风险行业要求。
- diagnosis 是否完整：✅
- action 是否明确：✅
- outcome 是否可量化：✅
- 推测对应 failure_family：ranking
- 是否潜在反例（原作者选择 graph_rag / multi_agent）：是
- 摘要：原文判断单纯向量检索无法满足复杂文档的可解释性、lineage 和准确性要求。Lettria 采用 GraphRAG，并补齐 Neo4j/Qdrant 一致写入、payload flattening、payload indexing、冷热向量分层等工程措施。结果是相比纯向量方案提升 20-25% accuracy，并保持 1-2 秒查询延迟，是测试 `must_avoid: graph_rag` 是否过度保守的关键反例候选。

## 候选 3

- 标题：From Patterns to Progress: How We Drove Trust in RAG Without Retraining the Model
- URL：https://www.needl.ai/blog/from-patterns-to-progress-how-we-drove-trust-in-rag-without-retraining-the-model
- 发布时间：2025-05
- 来源类型：B 级
- 来源具体类别：公司技术博客 / enterprise search 产品复盘
- RAG 场景：企业搜索 RAG 系统面对财报、公告、监管材料等开放式问题，需要给出可追溯、可信的回答。
- 主要 failure 信号：missing citations、incomplete answers、wrong references 和 retrieval gap 破坏用户信任。
- diagnosis 是否完整：✅
- action 是否明确：✅
- outcome 是否可量化：⚠️
- 推测对应 failure_family：observability
- 是否潜在反例（原作者选择 graph_rag / multi_agent）：否
- 摘要：作者把问题诊断为 trust/auditability 缺口，而不是模型本身完全失效。团队建立约 200 条真实任务查询、失败标签、live usage review、用户信任反馈和 QA set，把散乱反馈转成结构化诊断输入。结果偏定性，但清楚展示了 citations、traceability 和 human review 对 RAG 诊断的价值。

## 候选 4

- 标题：We Built an AI That Argues Like the Supreme Court — Here’s What We Learned
- URL：https://medium.com/@pliu27/we-built-an-ai-that-argues-like-the-supreme-court-heres-what-we-learned-80a6823bd134
- 发布时间：2026-04
- 来源类型：B 级
- 来源具体类别：工程师个人博客 / capstone project 复盘
- RAG 场景：Court Logic 用 RAG 检索司法意见和先例，模拟美国最高法院的判决推理与观点生成。
- 主要 failure 信号：baseline outcome accuracy 只有 15.4%，legal reasoning 被小 chunk 切碎后无法支撑连贯推理。
- diagnosis 是否完整：✅
- action 是否明确：✅
- outcome 是否可量化：✅
- 推测对应 failure_family：retrieval
- 是否潜在反例（原作者选择 graph_rag / multi_agent）：否
- 摘要：团队把 RAG 质量拆成 outcome accuracy、key-point coverage、LLM judge、RAGAS context precision/recall 等维度，并做 837 条测试记录、22 次 evaluation run。chunk size/overlap ablation 显示 2000/300 配置将 outcome accuracy 从 15.4% 提升到 46.2%，GraphRAG 也接近但未超过最佳 standard RAG。该候选适合测试 Skill 是否能识别 chunking/context continuity，而不是只看 retrieval recall。

## 候选 5

- 标题：RAG Done Right: Architecting Reliable Retrieval-Augmented Generation Systems
- URL：https://blog.stackademic.com/building-a-robust-rag-system-a-comprehensive-architecture-guide-cb27fda02e0b
- 发布时间：2025-12
- 来源类型：B 级
- 来源具体类别：工程师个人博客 / Stackademic 生产复盘
- RAG 场景：客户支持 AI 从 naive RAG 演进为多组件 production RAG，用于回答 API、政策、销售数据等业务问题。
- 主要 failure 信号：系统编造已废弃 API feature、引用不存在文档，并在 refund policy 查询中检索到 shipping policy 后生成错误答案。
- diagnosis 是否完整：✅
- action 是否明确：✅
- outcome 是否可量化：✅
- 推测对应 failure_family：generation
- 是否潜在反例（原作者选择 graph_rag / multi_agent）：否
- 摘要：作者把失败归因于 naive retrieval、缺少 query construction、缺少 routing、缺少 metrics 和 faithfulness check。后续引入 query construction、hybrid search、routing、reranking、evaluation gates 和 unsupported-claim 检查。文中给出 SQL query construction success rate 从 45% 到 92%、naive RAG 约 60% 可用等量化信号。

## 候选 6

- 标题：Building Chip: How We Built AI Customer Support in 2 Days
- URL：https://medium.com/brandcast-insider/building-chip-how-we-built-ai-customer-support-in-2-days-cdb63efe5e83
- 发布时间：2025-10
- 来源类型：B 级
- 来源具体类别：公司产品工程博客 / AI support assistant 复盘
- RAG 场景：BrandCast/FamilyCast 的 AI support assistant 结合 Stripe/account tools 与 1000+ help articles RAG，为真实客户回答 billing、account 和 product 问题。
- 主要 failure 信号：单纯 prompt/context 方案会 hallucinate，尤其是涉及实时账单和账户事实时。
- diagnosis 是否完整：✅
- action 是否明确：✅
- outcome 是否可量化：✅
- 推测对应 failure_family：generation
- 是否潜在反例（原作者选择 graph_rag / multi_agent）：否
- 摘要：作者先定义 accuracy、no hallucinations、human escalation 等需求，再比较 prompt-only 与 function calling/tool-backed answers。最终用 Vertex AI、13 个工具、RAG Engine、sources 和 escalation rules 组成系统。文章给出 $0.003 per conversation、<3s response time、function calling 后账单事实 100% accurate 等结果，适合测试 Skill 是否把实时工具调用与 RAG 证据边界区分开。

## 候选 7

- 标题：RAG or Fine-Tuned? How We Helped a Customer Make the Right AI Call
- URL：https://medium.com/@abunworaset/rag-or-fine-tuned-how-we-helped-a-customer-make-the-right-ai-call-a66901b2fdc3
- 发布时间：2025-06
- 来源类型：B 级
- 来源具体类别：咨询/工程师个人博客 / customer assistant 架构决策复盘
- RAG 场景：零售客户希望构建能回答产品、政策、促销和退换货问题的 AI assistant。
- 主要 failure 信号：fine-tuned bot 语气好但 hallucinate outdated return policy；RAG bot 准确但语气生硬，并需要 chunking/search tuning。
- diagnosis 是否完整：✅
- action 是否明确：✅
- outcome 是否可量化：⚠️
- 推测对应 failure_family：retrieval
- 是否潜在反例（原作者选择 graph_rag / multi_agent）：否
- 摘要：作者先把需求拆成 tone-sensitive 与 factual/dynamic 两类，再分别测试 fine-tune 与 RAG 原型。诊断结果是单一路线都不够：fine-tune 解决 brand voice，RAG 解决 live policy/source grounding。最终实现 hybrid approach：fine-tuned tone + RAG over live docs，并训练客户团队维护 KB 与 performance feedback loop。

## 调研路径与决策记录

- 检索关键词列表：
  - `"RAG postmortem" retrieval ranking production lessons learned outcome 2024`
  - `"RAG lessons learned" production retrieval reranking outcome 2025`
  - `"RAG" "missing citations" "wrong references" "outcome"`
  - `"RAGAS" "retrieval" "outcome accuracy" "context precision"`
  - `"GraphRAG" "case study" "outcome" "2025" "accuracy"`
  - `site:qdrant.tech/blog "RAG" "case study" "accuracy" "2025"`
  - `site:pinecone.io/customers "RAG" "retrieval" "accuracy"`
  - `site:weaviate.io/blog "RAG" "recall" "case study" "2025"`
- 覆盖的源池类型：
  - A 级：向量数据库厂商博客 / case study，评测与可观测性厂商博客。
  - B 级：公司技术博客，工程师个人博客，capstone/项目复盘。
- 跳过的来源类型与理由：
  - Reddit / HackerNews / Twitter / LinkedIn 线程：只作为索引线索，不作为主要源。
  - 纯教程或概念 guide：缺少真实 symptom、diagnosis、action、outcome 链条。
  - 纯学术 benchmark 或 survey：多数不具备人写 postmortem 叙事。
  - 厂商客户页但无明确发布时间：即使有结果指标，也无法严格证明满足 24 个月要求。
  - 软文式客户故事：只有收益指标，没有足够诊断细节时不进入短列表。
- checklist 不通过的候选数量与典型不通过原因：
  - 本轮明确筛掉 17 个候选或候选类型。
  - 典型原因包括：无发布时间、没有具体 symptom、没有 diagnosis 推理、只有 vendor benefit 而无 action 细节、没有 outcome、主要来源是社交讨论、内容是 benchmark 而非 postmortem。
- 是否遇到付费墙或访问受限：
  - 未将付费墙或访问受限内容纳入短列表。
  - Medium/Stackademic 候选均已实际打开原文正文；若后续人工访问遇到平台侧阅读限制，可优先选择 Arize、Qdrant、Needl 等非 Medium 候选。
- 人工自检记录：
  - 每个短列表候选 URL 均已实际访问原文，不依赖搜索摘要。
  - 每个短列表候选均通过 §3 的 7 项必备 checklist。
  - 短列表包含潜在反例：候选 2。
  - 多样性可覆盖 retrieval/ranking、generation/observability、潜在反例三类。
