# 2026-04-09 RAG QA Logs Corpus Source Extract

## Dataset

- 面向 Kaggle 的概念名：`RAG QA Logs & Corpus Data`
- 实际访问使用的镜像：<https://huggingface.co/datasets/tarekmasryo/rag-qa-logs-corpus-data>
- 使用镜像的原因：这台机器没有配置 Kaggle auth

## Relevant Files

- `data/scenarios.csv`
- `data/eval_runs.csv`
- `data/rag_retrieval_events.csv`
- `data/rag_corpus_chunks.csv`

## Why This Dataset Matters

这个数据集适合 bounded-complexity 的 RAG diagnosis，因为它把这些东西放在了一起：

- 问题与 gold-answer scenarios
- 按 run 给出的结果标签，例如 `correctness_label`、`faithfulness_label` 和 `hallucination_flag`
- 带 `is_relevant` 标记的 ranked retrieval traces
- 便于做定性检查的 chunk-level corpus text

## Selected Walkthrough Example

- `example_id`：`QA000050`
- `run_id`：`run_49`
- `scenario_id`：`SC0004`

## Scenario Row

```csv
scenario_id,domain,query,gold_answer,scenario_type,difficulty_level,use_case
SC0004,developer_docs,How do I authenticate using API keys?,API keys are passed as a bearer token in the Authorization header.,standard_qa,medium,rag_evaluation
```

## Eval Row

```csv
example_id,run_id,scenario_id,domain,task_type,correctness_label,faithfulness_label,hallucination_flag,retrieval_strategy,chunking_strategy,recall_at_5,recall_at_10,mrr_at_10,has_relevant_in_top5,has_relevant_in_top10
QA000050,run_49,SC0004,developer_docs,comparison,partial,unfaithful,1,bm25_then_rerank,sliding_window_256_overlap,0.0,1.0,0.1666666666666666,0,1
```

## Retrieval Trace Excerpt

```csv
rank,chunk_id,retrieval_score,is_relevant
1,C04776,0.90249216931254,0
2,C01739,0.7736046499973004,0
3,C01612,0.7219039811468517,0
4,C03167,0.5424263596278248,0
5,C03414,0.8240990719394974,0
6,C01347,0.7386831590271102,1
7,C01230,0.6387316148611839,1
8,C04548,0.7426596710277693,1
```

## Chunk Excerpts

- `C04776` rank 1，irrelevant
  `Developer integration guide бк Endpoint and Response`
- `C01347` rank 6，relevant
  `API reference: Response endpoint (2021)` with authentication patterns
- `C01230` rank 7，relevant
  `Service-to-service auth and endpoint бк engineering guide 2019`
- `C04548` rank 8，relevant
  `API reference: Authentication endpoint (2019)`

## Initial Read

语料里看起来确实有相关的认证证据，但排序列表顶部被语义相近的 endpoint 或 response chunks 占满了，真正相关的 authentication chunks 只能在更后面才出现。

## Related Pages

- [Good Recall, Weak Ranking](../wiki/failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Source Trail

- Hugging Face 数据集 API 与数据文件于 2026-04-09 被访问
