# Agent Framework Choice

只有当任务确实需要 tool use、branching workflows 或 stateful multi-step behavior，而 plain retrieval pipeline 处理不干净时，才引入 orchestration 或 agent framework。

## First Question

用户真的需要 orchestration 或 agent framework 吗？

如果系统只是：

- 检索文档
- 生成 grounded answers
- 返回 citations

那么 plain RAG pipeline 往往就够了。

## Escalation Ladder

按这个顺序增加复杂度，并在简单层已经足够时立刻停下：

1. Plain retrieval 加 grounded answer generation
2. retrieval 升级，例如更好的 metadata、hybrid retrieval、reranking 或 query rewrite
3. Graph retrieval 或 graph-shaped orchestration；前提是 failure mode 在结构上复杂或分支很多
4. 只有当不同角色真的能提升结果时，才做 specialist multi-agent coordination

不要把 graph retrieval 和 graph orchestration 混为一谈。

- Graph retrieval 解决的是结构化知识访问
- Graph orchestration 解决的是结构化控制流

有些系统只需要其中之一。

## Agentic RAG Enablement Rule

只有当以下大多数条件同时成立时，才启用 agentic RAG：

- 任务必须被显式分解成多个 retrieval 或 reasoning steps
- 不同步骤确实需要不同的 tools、data sources 或 specialist roles
- workflow 存在真实分支点，例如 continue、rewrite、route、fallback、abstain 或 handoff
- state 必须跨步骤累计，而不是在一次回答后立即丢弃
- 产品能够承受新增 latency、cost 和 observability burden
- 固定 hard-case set 已证明，更简单的 retrieval 升级还不够

如果以下大多数条件成立，就不要启用 agentic RAG：

- 大多数 query 仍然是直接的 document QA
- 当前 baseline retrieval quality 还没有被刻画清楚
- 真正的问题是 chunking、metadata、filtering 或 reranking，而不是 workflow complexity
- 所谓的 agent loop 只是给一条 retrieval 路径多包了几层 prompt
- 没有 trace review、retry cap 或显式 failure policy

当你推荐 agentic RAG 时，必须说清：

- 精确的 subtask boundaries
- role 或 tool boundaries
- branch conditions
- loop cap 或 stop condition
- 哪个 evaluation signal 能证明这层控制逻辑配得上它的成本

## LangChain

适合在这些情况下使用：

- 你需要广泛的 ecosystem integrations
- 你需要灵活的 chains、tools 和 agent patterns
- 团队更看重大型社区和快速原型能力

代价：

- 很容易快速走向抽象过度
- 在简单 RAG 系统里，容易诱发过度工程化

## LangGraph

适合在这些情况下使用：

- workflow 存在明确分支，例如 query routing、query rewrite、web fallback 或 human review
- 团队需要对 retries、loops 或 tool transitions 有 stateful control
- 你要的是 graph-shaped control flow，而不是单个 agent loop
- 系统必须解释：为什么它留在 vector store path、为什么要 rewrite query、或为什么 fallback 到 web

代价：

- 即使真正瓶颈仍然只是 plain retrieval quality，它也会引入 orchestration complexity
- looping behaviors 如果没有 hard stopping criteria 和 observability，就会很难 debug
- LLM grading steps 可能看起来很高级，但实际只增加 latency 和脆弱的 judge 行为

只有当你同时能说清以下内容时，才使用它：

- branch points
- stopping conditions
- 最大 retry 或 loop count
- 哪个 evaluation signal 能证明 graph 比简单 pipeline 更好

不要为了让 RAG demo 看起来高级，就加 graph orchestration。

只有当 plain retrieval pipeline 已经显示出某个具体弱点，而且这些分支确实针对它时，query routing、rewrite nodes、web fallback 和 grading loops 才有理由存在。

## LlamaIndex

适合在这些情况下使用：

- document ingestion 和 retrieval 是核心
- 团队希望使用一个以 RAG 为中心的 abstraction layer
- 你想让 indexing 和 query workflow 成为一等概念

代价：

- 如果系统核心是 retrieval 之外的 agent orchestration，它不一定最合适

## CrewAI

适合在这些情况下使用：

- 设计真的需要 role-based multi-agent coordination
- 你需要明确的 agent responsibility boundaries
- workflow 已经不止是 retrieval 加 answer generation

代价：

- 对很多 RAG 产品来说复杂度过高
- 增加更多需要观察和调试的 moving parts

## Grading Loops And Self-Critique

把 LLM grading loops 当成可选 control layer，而不是 RAG 系统的默认形态。

最合理的使用场景：

- 你需要在返回答案前做明确 groundedness checks
- workflow 必须在“retry retrieval”“rewrite query”和“abstain”之间做选择
- 系统风险足够高，值得接受额外 latency

以下情况下通常不值得：

- retrieval baseline 仍然明显偏弱
- corpus 很小，而更简单的 abstention rule 已经足够
- 团队无法检查 traces，也无法比较 loop-on 和 loop-off 的差别

如果你加入 grading loops，必须要求：

- bounded retries
- 明确的 loop exit conditions
- 写清楚的 fallback path
- 把 retrieval quality 和 judge quality 分开评测

## Retrieval Supervisors And Policy Agents

把 retrieval supervisors、policy agents 和 reflective controllers 当成可选 control layer，而不是 RAG 系统的默认身份。

最合理的使用场景：

- workflow 必须在 vector、keyword、hybrid、graph 或 web 路径之间做选择
- 存在明确的 continuation decisions，例如继续、重写、切换、放弃
- 控制器确实能稳定提高结果，而不是仅仅“更像 agent”

如果推荐这层控制逻辑，必须明确：

- 它究竟控制什么
- 它不能控制什么
- 如何被测量
- 如果关闭它，会退回到什么简单 baseline

## Recommendation Pattern

当你推荐某个 agent framework 时，明确说明：

1. 为什么 plain retrieval pipeline 不够
2. 哪个 workflow 特性迫使你引入 orchestration
3. 要保持哪些 branch boundaries
4. 哪些 complexity 明确不加入
