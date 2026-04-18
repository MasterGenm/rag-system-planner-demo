# Evaluation Design

在声称一个 RAG 系统可用之前，先定义 evaluation。既要测 retrieval，也要测 answer 层。

## Offline Evaluation

### Retrieval Metrics

当你能构造带标签的 query-document pairs 时使用。

常见指标：

- Recall@k
- MRR
- nDCG
- Hit rate

### Answer Metrics

当“答案本身”就是产品表面时使用。

检查：

- Groundedness
- Citation correctness
- Completeness
- Conciseness
- 针对特定 workflow 输出的 task success

## Judge-Based Evaluation

把 LLM-as-a-judge 用在局部 pairwise comparison、workflow 质量检查或 trace review 上，但不要让 judge score 成为系统可用的唯一证据。

Judge-based evaluation 至少要和以下之一配对：

- 带标签的 retrieval slices
- 固定 gold answers
- 对代表性子集做 manual audit
- 当系统已部署时，再加面向业务的成功检查

在比较 variants 时，保持 judge 稳定：

- same judge model
- same scoring prompt
- same candidate set 或 trace slice

不要仅凭 notebook 本地的 judge scores 就声称系统已经具备 production readiness。

## Agentic And Graph Evaluation

如果系统引入 routing、rewrite loops、fallback tools、graph traversal 或 multi-agent control，就不能只看最终答案质量。

需要检查：

- routing correctness
- tool selection correctness
- retry 和 loop termination behavior
- fallback rate 和 abstention behavior
- 每增加一层 control layer 带来的 latency 和 cost overhead
- 当使用 graph retrieval 时，在 multi-hop、hierarchy、temporal 或 negation cases 上的 graph-specific success

## Tutorial-Bias And Single-Case Bias

不要让一个戏剧化的 notebook walkthrough，或一条特别难的 query，变成系统可用的主要证据。

一个精彩案例对 demo 有价值，但不足以支撑架构结论。

至少要求：

- 一个小而固定的 scenario set，而不是单个 hero query
- 一个稳定 baseline 用于比较
- 当系统含随机成分时，要做 repeated runs 或 manual audit
- 明确说明这个 showcase case 不能证明什么

## Dataset Design

在过度优化架构之前，先构建一个小但具有代表性的 evaluation set。

应包含：

- Easy cases
- Ambiguous cases
- Long-tail domain cases
- Failure-prone cases
- 若相关，还要加入 multilingual 或 multimodal cases

## Online Evaluation

持续追踪：

- User success 或 abandonment
- Citation usage
- Follow-up question rate
- Latency percentiles
- Regeneration 或 retry rate

## Common Mistakes

- 只测 answer quality，不测 retrieval quality
- 只用 synthetic evaluation data
- 忽略 hard negative examples
- 改了 embeddings 或 chunking，却不重做 baseline
- 把 LLM-as-a-judge traces 当成 retrieval ground truth 的替代品
- 加了 agentic branches，却不测这个 branch 到底有没有改善任何东西

## Recommendation Pattern

对每一个架构建议，都要包含：

1. 必须做哪些 offline measurement
2. 必须观察哪些 online signals
3. 达到什么 threshold 才值得继续迭代
