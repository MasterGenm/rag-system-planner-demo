# RAG 召回与引用诊断报告

## 症状概述

- 用户反馈“搜得到相关文档，但经常答不到点上”
- 正确证据偶尔在候选集里，但不在 top-ranked 结果中
- citation 经常指向相邻段落，而不是精确证据段
- 加了更多 retrieval stages 之后，延迟明显上升

## 工作假设

### 已观察到（Observed）

- top-rank precision 弱于 candidate recall
- citation anchor 粒度偏粗

### 推断中（Inferred）

- chunking 可能过粗，导致细粒度问题不容易被精确命中
- 团队可能把 ranking 问题误判成“整个架构不够高级”

### 仍未知（Unknown）

- embedding 是否是当前最主要瓶颈
- hybrid retrieval 对 hard keyword cases 的收益是否足够大

## 缺失证据

- 缺一个固定困难样例评测集（hard-case eval set）
- 缺 retrieval trace，无法区分“召回失败”还是“排序失败”
- 缺 stage-level latency breakdown

## 排查顺序

1. 先确认正确 chunk 是否已经出现在 candidate pool 中  
2. 再看 chunking、metadata 和 citation anchor  
3. 如果 candidate recall 已经够，再评估 reranking  
4. 最后才讨论是否需要更大范围架构升级

## 推荐改动

### 现在（Now）

- 增加 trace：chunk ids、scores、filters、citation anchors
- 建一个 citation-heavy hard-case set
- 调整 chunking 粒度和 section-aware metadata

### 下一步（Next）

- 如果 candidate recall 足够而 top precision 差，引入 reranking 实验
- 对 keyword-heavy 查询单独测试 hybrid retrieval

### 以后（Later）

- 只有在 baseline retrieval + ranking 调整仍然无效时，才讨论更高复杂度路线

## 评测补充

- `Recall@k`
- top-rank precision
- citation correctness
- 各配置版本的 latency 对比

## 可观测性补充

- retrieval trace
- per-stage latency
- empty retrieval rate
- citation failure rate

## 风险与预期影响

- 如果没有 hard-case eval，团队会继续根据个别案例反复重构
- 如果 chunking 不先修，直接加 reranking 只能改善排序，不能彻底解决 citation 质量问题
