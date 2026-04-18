# Sample Support Incident

## 日期

2026-04-09

## System

一个面向产品文档、runbooks 和 incident 历史的内部 support RAG assistant。

## 观察

- retrieved candidates 往往能覆盖正确的文档族
- 答案有时会引用前一节或后一节，而不是精确的步骤
- 由于 chunk ids 和 citation anchors 不是总被记录，工程师无法稳定判断问题到底在 chunking、ranking 还是 answer assembly

## 初步假设

系统很可能是在可接受的 candidate recall 之上，又叠加了 citation precision 问题。
