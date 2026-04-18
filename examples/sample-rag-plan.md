# 支持知识库 RAG 方案

## 问题概述

为内部支持知识库设计一个复杂度受控的 RAG 系统，语料包括产品文档、运行手册、常见问题、事故复盘和部分截图型证据。目标优先级是引用质量、可调试性和逐步演进，而不是一开始就做复杂编排。

## 假设与约束

- 当前语料规模为中等，日更
- 团队希望先上线 plain RAG 基线
- 需要 metadata 过滤和可检查引用
- 允许后续渐进式增加重排或多模态检索

## 推荐方案栈

- Python 检索服务
- 基于章节的切块
- 带丰富元数据的索引
- `Qdrant` 作为偏生产的默认向量存储
- 通用文本 embedding 先作为基线

## 架构与数据流

1. 文档进入摄取流水线，按章节和段落组切块
2. 每个 chunk 带上文档 id、标题路径、更新时间、文档类型等元数据
3. 服务阶段先做稠密检索加元数据过滤
4. 回答层只消费带引用锚点的证据
5. 对证据不足的情况显式拒答

## 检索设计

### 切块方案

- 对结构化文档优先按章节拆分
- 保留标题和 heading path
- 避免把 issue narrative 或排障过程切得过碎

### 元数据方案

- `document_id`
- `section_path`
- `doc_type`
- `updated_at`
- `product_area`

### 引用策略

- 返回 source title + section anchor
- 对截图或 PDF 页面保留 page / asset anchor

### 当前不引入的复杂度

- 暂不上图检索
- 暂不上 agent framework
- 暂不上多层 grading loop

## 评测方案

- 建一个固定困难样例集
- 离线测 `Recall@k`、citation 正确率、groundedness
- 对每次检索设计变更做回归检查

## 可观测性方案

- 追踪 query、retrieved chunk ids、scores、filters、latency
- 区分检索延迟、生成延迟和总延迟
- 仪表板至少看空检索比例和引用失败率

## 分阶段上线计划

### 第 1 阶段

- 上线 plain retrieval 基线 + 引用 + 最小可观测性

### 第 2 阶段

- 如果候选召回足够但 Top-1 精度弱，再加重排

### 第 3 阶段

- 如果视觉证据真的影响答案质量，再引入复杂度受控的多模态检索
