# Vector Database Choice

Use this guide to compare storage and retrieval options. Favor operational simplicity unless the workload clearly needs something more complex.

## Quick Guidance

### FAISS

Use when:

- You want a lightweight local index
- Metadata filtering is limited or handled elsewhere
- The corpus is relatively static
- You care more about raw similarity search than database features

Avoid as the default when:

- You need rich filtering
- You need a managed service
- You expect operational scaling, multi-tenant isolation, or strong persistence guarantees

### Chroma

Use when:

- You want fast local development
- You want a simple developer experience
- The system is small to medium and operational complexity should stay low

Avoid as the default when:

- You need advanced filtering or high-scale production behavior
- You already know you need stronger operational controls

### Qdrant

Use when:

- You need a production-grade vector store
- Filtering and hybrid retrieval matter
- You want a strong balance of performance and operational features
- The system will evolve beyond a prototype

Avoid only when:

- The workload is tiny and local-only
- Operational overhead must be nearly zero

### Milvus

Use when:

- The workload is already beyond "simple product RAG" and the team expects heavier operational scale
- You want a vector database with stronger enterprise-style deployment modes and a richer storage or indexing surface
- Hybrid retrieval, collection schema design, and distributed deployment are part of the real requirements
- The team is already comfortable operating Docker or Kubernetes-style infrastructure

Avoid as the default when:

- The project is still proving product value or retrieval quality
- The team mostly needs a simple self-hosted developer experience
- Operational discipline is weak and database complexity would dominate the project
- The same problem could be solved with `Chroma` or `Qdrant` plus better retrieval design

### Managed Vector Databases

Use when:

- You want managed scaling and backups
- The team does not want to operate the database
- Vendor lock-in is acceptable

## Dual-Store Vector Plus Graph

Use a dual-store design such as `Qdrant + Neo4j` only when the workload clearly mixes:

- semantic document lookup
- structural traversal over entities and relations

This is justified when different query families truly need different retrieval primitives.

Require:

- a written routing rule for which questions hit vector search, graph traversal, or both
- shared identifiers or anchors that let graph evidence and document evidence be cited together
- separate freshness and consistency expectations for vector and graph stores
- fixed hard cases showing that the dual-store path beats a simpler vector-only baseline

Avoid as the default when:

- graph extraction quality is still uncertain
- the team mainly has document QA needs
- operating two data stores would dominate project complexity

## Decision Criteria

Compare options on:

- Corpus size
- Update frequency
- Metadata filtering requirements
- Hybrid search requirements
- Persistence and backup needs
- Multi-tenant requirements
- Operational skill and budget
- Deployment model and cluster complexity tolerance

## Default Recommendation Pattern

- Prototype or notebook workflow: `Chroma` or `FAISS`
- Production RAG with filtering and growth expectations: `Qdrant`
- Self-hosted enterprise-style deployment with heavier scale and ops tolerance: `Milvus`
- Managed enterprise environment: managed vector database if ops avoidance matters more than portability
