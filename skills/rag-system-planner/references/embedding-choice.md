# Embedding Choice

按数据模态、语言覆盖、延迟预算和运维约束来选择 embeddings。

## Decision Rules

### Start Simple

默认先选一个强的通用文本 embedding model，除非下面这些条件迫使你换用其他方案：

- multilingual retrieval
- domain-specific vocabulary
- multimodal retrieval
- 严格的 local-only deployment
- 极高吞吐需求

### Hosted Vs Local

以下情况优先 hosted embeddings：

- 快速接入最重要
- 团队更希望使用 managed operations
- 可以接受 network access
- 模型迭代速度比严格成本控制更重要

以下情况优先 local embeddings：

- 数据不能离开当前环境
- 大规模下成本可预测性更重要
- 需要 offline 或 edge operation
- 团队已经本地运维 GPU inference

## By Use Case

### General Text RAG

优先选择具备以下特征的强文本 embedding：

- semantic search 质量稳定
- sentence 或 passage retrieval 表现良好
- 对上下文长度的处理足够稳

### Multilingual RAG

优先选择明确支持 multilingual 的模型。不要假设一个 English-first 模型在 mixed-language corpus 上也能表现良好。

### Domain-Specific RAG

如果语料是 legal、biomedical、financial 或 code-heavy，先测试 domain-tuned embedding model 是否真的提升 retrieval，提升不足则不要引入额外复杂度。

### Multimodal RAG

如果 retrieval 必须在 text 和 image 之间建立桥梁，就使用 modality-aware embeddings 或 parallel pipelines，而不是把一切都硬塞进纯文本表示。

## Tradeoffs

- 更好的 retrieval quality 往往意味着更高 latency 或 cost。
- 更大的 embedding dimensions 会增加 storage 和 search 成本。
- 切换 embeddings 往往意味着全量或部分 re-indexing。
- cross-lingual 和 multimodal 支持会增加 evaluation burden。

## Recommendation Pattern

在推荐 embeddings 时，明确说明：

1. 为什么当前的 modality 和 language profile 重要
2. hosted 还是 local 更合适
3. 应该先从通用模型起步，还是直接用 domain-specific 模型
4. 需要用什么 evaluation 来确认这个选择
