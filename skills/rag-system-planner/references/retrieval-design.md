# Retrieval Design

在选择 orchestration framework 之前，先把 retrieval 设计好。很多糟糕的 RAG 系统失败，不是因为缺框架，而是因为它们先做了框架 plumbing，而不是先把 retrieval 质量打牢。

## Chunking

按文档结构设计 chunking，不要按任意 token 数硬切。

### Good Defaults

- 尽量保留 section boundaries
- 每个 chunk 都带上 metadata
- 只有在能改善上下文连续性时才使用 overlap

### When To Use Smaller Chunks

- 事实查找
- 稠密技术文档
- 问题跨度很窄

### When To Use Larger Chunks

- 叙事型文档
- 上下文跨越多个段落的法律或政策文本
- 以总结为导向的检索

### Section-Aware Defaults

对于结构化文档，先按 section 切，再按 paragraph 切。

优先：

- 以 document title 和 heading path 作为前缀
- 使用能保留局部推理链的适中 chunk size
- 保留 section 或 page anchors，让 citations 保持可检查

不要默认“越小越好”。过度切碎会破坏解释性上下文，尤其是在 issue threads 或长篇技术文档里。

对于 issue 类语料：

- 保留 issue title 作为强前缀
- 按段落组或子小节切正文
- 不要把调试叙事撕成过小碎片

## Metadata

如果你需要以下能力，就要尽早设计 metadata：

- source citations
- 时间过滤
- tenant isolation
- document type filtering
- 版本感知

糟糕的 metadata，经常会伪装成糟糕的 retrieval。

## Retrieval Strategy

先从简单 baseline 开始：

1. dense retrieval
2. 必要时加 metadata filtering
3. top-k retrieval

只有当 baseline 失败时，才增加复杂度：

- hybrid retrieval：适用于关键词敏感的查询
- query rewriting：适用于用户输入模糊的场景
- multi-query retrieval：适用于 recall 是主要问题的场景
- reranking：适用于初始 candidate set 噪声较大的场景
- parent-child retrieval：适用于 passage 需要更大 source context 的场景

对每一层新增能力，都要说明：

- 为什么 baseline 不够
- 这层能力改善什么
- 它在 latency、complexity 或 operations 上的代价是什么
- 你现在有意不加什么

## Adaptive Retrieval Funnels

只有当不同 query family 真的需要不同 retrieval 行为时，才使用 adaptive multi-stage retrieval funnel。

合理信号包括：

- 会话型或指代型查询，需要 rewrite 成 standalone query
- 存在 semantic gap，HyDE 或 hypothetical answer 能改善 first-stage recall
- 查询家族混杂：有些关键词重、有些偏语义、有些需要 hybrid retrieval
- 高价值问题确实需要“先扩 recall，再做 reranking，再做轻量蒸馏”才能显著改善答案质量

把它视为一种有边界的 retrieval upgrade，而不是引入大型 agentic workflow 的借口。

如果你推荐 adaptive funnel，要说明：

- 哪些 query family 会触发 rewrite、HyDE、keyword、dense 或 hybrid path
- 默认路径是什么
- 每个 stage 记录什么，才能保证失败仍然可调试
- 每一层额外 stage 带来的 latency 和 cost 开销
- 哪个固定 retrieval slice 或 hard-case set 能证明 funnel 比简单 baseline 更好

不要在以下情况下先上 retrieval supervisor 或 HyDE：

- corpus 很小，failure mode 还未明确
- baseline dense 或 hybrid retrieval 还没有被测过
- 团队无法解释哪些问题应该绕过额外 stage
- 这层设计只是让 demo 看起来更高级，却没有清楚的 retrieval gain

## Reranking

把 reranking 当成“排序修复”，而不是“召回修复”。

以下情况下可以加 reranking：

- 正确证据已经在 candidate pool 里，但前几名排序错了
- recall 尚可，但 top-rank precision 偏弱
- 前排结果相关但不够精确，无法支撑事实密集型问题或 citations
- query 很细粒度，而多个 candidate chunks 又共享同一个大主题

以下情况下先不要加 reranking：

- 相关证据根本没进 candidate pool
- chunking、metadata、filters 或 query formulation 仍然明显有问题
- corpus 很小，而 baseline retrieval 已经足够精确
- latency budget 很紧，不足以支撑 second-stage model

使用标准两阶段模式：

1. first-stage retrieval：收集 candidate set
2. second-stage reranking：只在 top-N candidates 上做 rerank

Cross-encoder 很适合 second stage，因为它通常太贵，不适合全库检索。

在规划 reranking 时，要说明：

- 你会如何确认 candidate recall 已经足够
- 有多少 candidates 会进入 reranker
- reranker 会消耗多少 latency budget
- 如果 reranker 有效，应该改善哪个 metric

输入整形很重要。不要只把裸 chunk text 喂给 reranker；当结构承载语义时，应把结构一并喂进去。

优先加入这些前缀：

- section 或 chapter titles
- document path 或 source title
- page anchors 或 subsection ids

这些信息经常能帮助 reranker 区分“同主题 chunk”和“真正回答问题的 chunk”。

## Chunking Versus Reranking

使用这个判断规则：

- 如果相关证据没有进入 candidate pool，先检查 chunking、metadata、filters 和 retrieval strategy。
- 如果相关证据已经在 candidate pool 中，但排序不对，先检查 reranking。
- 如果 retrieved chunks 大体相关，但太粗，无法回答精确问题，那么先做 section-aware chunking，再考虑更大的架构变化。
- 如果 chunks 本身不错、排序也对，但答案仍然弱，那么去检查 prompt assembly 或 generation。

不要把 reranking 当成修复明显坏掉的 chunking 的替代品；也不要在真实问题是 ranking precision 时，先重写 chunking。

## Graph RAG And Structural Retrieval

只有当问题在结构上足够难，而不是仅仅语义模糊时，才考虑 graph-structured retrieval。

合理信号包括：

- 需要显式 traversing intermediate entities 的 multi-hop 链路
- 层级或 parent-child lineage 问题
- 对方向性敏感的查询，例如 ownership 或 dependency arrows
- “最新事实”这种时间顺序比相似度更重要的问题
- common-neighbor 或 intersection 查询
- negation、absence 或 set-difference 问题
- influence、bottleneck 或 centrality 问题

以下情况下不要急着跳到 Graph RAG：

- 任务本质上仍然是 citation-heavy document QA
- dense 或 hybrid retrieval 还没有 baseline
- graph extraction 质量弱，或维护代价太高
- 团队无法解释哪些 query family 应该走 traversal，而不是 plain retrieval

如果你推荐 Graph RAG，要说明：

- entities 和 relations 从哪里来
- graph extraction 或人工整理如何验证
- 哪些 query family 路由到 graph traversal
- graph path 必须在什么固定 hard case 上打败更简单的向量检索 baseline
- 你会观察哪些 graph-specific failure modes，例如 stale edges 或 entity resolution 错误

## Web Fallback And External Search

只有当问题真的需要新鲜证据或 corpus 外证据时，才使用 external search。

合理信号包括：

- 对时间高度敏感，而内部文档明确过时
- 比较型问题需要把内部知识和近期公开事件结合起来
- 内部 corpus 存在明确覆盖缺口，且这个缺口无法合理补齐

不要把 web fallback 当成内部 retrieval 弱的替代品。如果内部文档本该答出来，就先修内部路径。

如果你加 web fallback，要说明：

- 哪些 query family 允许离开 corpus
- 外部证据如何引用，并如何与内部证据区分
- 适用什么 freshness 或 source-trust 规则
- 用什么 fallback cap 或 routing rule 防止不必要的外部调用

## Multimodal And Scan-Heavy Corpora

当证据存在于图表、截图、扫描页面或表格里时，不要强行把一切都塞进纯文本设计。

- 当 text chunks、OCR text 和 image/region assets 承担不同检索角色时，应保持区分
- 把 OCR confidence 当成 metadata，而不是隐藏实现细节
- 保留 page anchors、section ids 和 asset ids，让 citations 可追溯
- 只有当视觉语义不重要时，才用 text-only baseline
- 如果 image understanding 确实重要，就规划明确的模态路由或并行检索分支

当多模态证据可能改变 retrieval 设计时，读取 `references/multimodal-retrieval.md`。

## Fallback And Abstention

为弱证据场景做好设计：

- 当 retrieval 返回很少或没有支持时怎么办
- 在什么条件下应该 abstain，而不是强行回答
- 如何把低置信度证据暴露给用户或后续 workflow

## Generation Boundary

把 retrieval 问题和 generation 问题区分开：

- retrieved chunks 里缺证据，是 retrieval 问题
- 证据不错但综合很差，是 generation 或 prompt 问题
- 答案不错但 citation 很弱，通常是 assembly 问题

## Recommendation Pattern

明确说明：

1. chunking plan
2. metadata plan
3. retrieval plan
4. reranking plan（如果需要）
5. citation strategy
6. 当证据弱时的 fallback 或 abstention strategy
7. 现在不加什么，以及原因
