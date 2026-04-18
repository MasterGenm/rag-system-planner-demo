# Vector Database Choice

用这份指南比较 storage 和 retrieval 选项。除非 workload 明确要求更复杂的能力，否则优先 operational simplicity。

## Quick Guidance

### FAISS

以下情况适合：

- 你想要一个轻量的本地索引
- metadata filtering 很有限，或在其他层处理
- corpus 相对静态
- 你更在意原始相似度搜索，而不是数据库能力

以下情况不要把它当默认：

- 你需要丰富 filtering
- 你需要 managed service
- 你预期会遇到 operational scaling、multi-tenant isolation 或强 persistence guarantees

### Chroma

以下情况适合：

- 你需要快速本地开发
- 你需要简单的 developer experience
- 系统规模小到中等，且你希望运维复杂度保持低位

以下情况不要把它当默认：

- 你需要高级 filtering 或高规模 production 行为
- 你已经明确知道需要更强的 operational controls

### Qdrant

以下情况适合：

- 你需要 production-grade vector store
- filtering 和 hybrid retrieval 很重要
- 你想在性能和运维能力之间取得强平衡
- 系统会继续从 prototype 演化

只有在以下情况下才不必默认用它：

- workload 很小，而且只在本地运行
- operational overhead 必须几乎为零

### Milvus

以下情况适合：

- workload 已经明显超出“简单产品型 RAG”，团队预期会有更重的运维规模
- 你需要 enterprise-style deployment mode 和更丰富的 storage/indexing surface
- hybrid retrieval、collection schema design 和 distributed deployment 是真实需求
- 团队已经习惯运维 Docker 或 Kubernetes 风格的基础设施

以下情况不要把它当默认：

- 项目还在证明产品价值或 retrieval 质量
- 团队主要需要简单的 self-hosted developer experience
- 运维纪律较弱，数据库复杂度会反过来主导项目
- 同样的问题完全可以用 `Chroma` 或 `Qdrant` 加更好的 retrieval design 解决

### Managed Vector Databases

以下情况适合：

- 你需要 managed scaling 和 backups
- 团队不想自己运维数据库
- 可以接受 vendor lock-in

## Dual-Store Vector Plus Graph

只有当 workload 明确同时混合了以下两种需求时，才使用双存储设计，例如 `Qdrant + Neo4j`：

- semantic document lookup
- entities 和 relations 上的 structural traversal

这只有在不同 query family 真的需要不同 retrieval primitive 时才合理。

必须具备：

- 一份清楚的 routing rule，说明哪些问题打 vector search、哪些打 graph traversal、哪些同时打
- 共享 identifiers 或 anchors，让 graph evidence 和 document evidence 能一起被引用
- 向量层和图层分别独立定义 freshness 与 consistency 预期
- 固定 hard cases 证明 dual-store 路径确实打败了简单的 vector-only baseline

以下情况不要把它当默认：

- graph extraction quality 还不确定
- 团队的主要需求仍然是 document QA
- 运维两个数据存储的复杂度会吞掉项目本身

## Decision Criteria

比较不同方案时，看这些维度：

- Corpus size
- Update frequency
- Metadata filtering requirements
- Hybrid search requirements
- Persistence 和 backup 需求
- Multi-tenant requirements
- Operational skill 和预算
- Deployment model 以及 cluster complexity tolerance

## Default Recommendation Pattern

- Prototype 或 notebook workflow：`Chroma` 或 `FAISS`
- 需要 filtering、并且预期会增长的 production RAG：`Qdrant`
- 更重的自托管企业部署，且团队能承受更高 ops 复杂度：`Milvus`
- 企业环境且 ops avoidance 比 portability 更重要：managed vector database
