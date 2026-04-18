# Observability Design

在 diagnosis 模式下，observability 不是可选项。如果你看不见系统检索了什么、每个 stage 花了多久、模型当时能看到什么证据，你就无法可靠地改进一个 RAG 系统。

## Minimum Signals

至少追踪：

- Query text 或规范化后的 query form
- Retrieved document 或 chunk identifiers
- Retrieval scores
- 使用过的 metadata filters
- 如果存在，记录 reranking decisions
- Prompt assembly metadata
- Model response latency
- 如果相关，再记录 token usage
- 返回给用户的 citations

## Minimum Dashboards

至少要能看见：

- Retrieval latency
- Generation latency
- End-to-end latency
- Empty 或 low-confidence retrieval rate
- Citation failure rate
- 分 stage 的错误率

## LangSmith Vs Phoenix

### LangSmith

以下情况优先：

- 系统已经大量使用 LangChain
- 你需要更成熟的 tracing 和 experiment workflow
- 可以接受 hosted tooling

### Phoenix

以下情况优先：

- 你想要开源 observability 方案
- 你需要灵活的 tracing 和 evaluation，但不想绑定 LangChain
- 你想保留一个 framework-neutral 的 monitoring 方案

## Common Gaps

- 只记录最终答案
- 不保存 retrieved chunk identifiers
- 不记录 filter conditions
- 不区分 retrieval latency 和 generation latency
- 没有把 bad answers 与 missing evidence 关联到同一条 trace 上

## Recommendation Pattern

始终明确说明：

1. 要 trace 什么
2. 要聚合什么
3. 要对什么做告警
4. 在当前 chosen stack 下，哪种工具更合适
