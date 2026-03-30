# 支持知识库 RAG 方案

## 问题概述

为内部支持知识库设计一个 bounded-complexity RAG 系统，语料包括产品文档、运行手册、FAQ、事故复盘和部分截图型证据。目标优先级是引用质量、可调试性和逐步演进，而不是一开始就做复杂 orchestration。

## 假设与约束

- 当前语料规模为中等，日更
- 团队希望先上线 plain RAG baseline
- 需要 metadata filtering 和可检查 citation
- 允许后续渐进式增加 reranking 或 multimodal retrieval

## 推荐方案栈

- Python 检索服务
- 基于章节的 chunking
- 带丰富 metadata 的索引
- `Qdrant` 作为偏生产的默认向量存储
- 通用 text embedding 先作为 baseline

## 架构与数据流

1. 文档进入 ingestion pipeline，按 section 和段落组切块  
2. 每个 chunk 带上文档 id、标题路径、更新时间、文档类型等 metadata  
3. serving 时先做 dense retrieval + metadata filtering  
4. 回答层只消费带 citation anchor 的 evidence  
5. 对证据不足的情况显式 abstain

## 检索设计

### 切块方案

- 对结构化文档优先按 section 拆分
- 保留标题和 heading path
- 避免把 issue narrative 或排障过程切得过碎

### Metadata 方案

- `document_id`
- `section_path`
- `doc_type`
- `updated_at`
- `product_area`

### 引用策略

- 返回 source title + section anchor
- 对截图或 PDF 页面保留 page / asset anchor

### 当前不引入的复杂度

- 暂不上 graph retrieval
- 暂不上 agent framework
- 暂不上多层 grading loop

## 评测方案

- 建一个固定困难样例集（hard-case set）
- 离线测 `Recall@k`、citation correctness、groundedness
- 对每次 retrieval 设计变更做回归检查

## 可观测性方案

- trace query、retrieved chunk ids、scores、filters、latency
- 区分 retrieval latency / generation latency / total latency
- dashboard 至少看 empty retrieval rate 和 citation failure rate

## 分阶段上线计划

### 第 1 阶段

- 上线 plain retrieval baseline + citations + minimum observability

### 第 2 阶段

- 如果 candidate recall 足够但 top precision 弱，再加 reranking

### 第 3 阶段

- 如果视觉证据真的影响答案质量，再引入 bounded multimodal retrieval
