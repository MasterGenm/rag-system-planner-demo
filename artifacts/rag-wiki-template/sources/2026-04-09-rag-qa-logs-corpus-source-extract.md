# 2026-04-09 RAG QA Logs Corpus Source Extract

## Dataset

- Kaggle-facing concept: `RAG QA Logs & Corpus Data`
- mirror used for access: <https://huggingface.co/datasets/tarekmasryo/rag-qa-logs-corpus-data>
- reason the mirror was used: Kaggle auth is not configured on this machine

## Relevant Files

- `data/scenarios.csv`
- `data/eval_runs.csv`
- `data/rag_retrieval_events.csv`
- `data/rag_corpus_chunks.csv`

## Why This Dataset Matters

This dataset is useful for bounded-complexity RAG diagnosis because it combines:

- question and gold-answer scenarios
- per-run outcome labels such as `correctness_label`, `faithfulness_label`, and `hallucination_flag`
- ranked retrieval traces with `is_relevant`
- chunk-level corpus text for qualitative inspection

## Selected Walkthrough Example

- `example_id`: `QA000050`
- `run_id`: `run_49`
- `scenario_id`: `SC0004`

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

- `C04776` rank 1, irrelevant
  `Developer integration guide — Endpoint and Response`
- `C01347` rank 6, relevant
  `API reference: Response endpoint (2021)` with authentication patterns
- `C01230` rank 7, relevant
  `Service-to-service auth and endpoint — engineering guide 2019`
- `C04548` rank 8, relevant
  `API reference: Authentication endpoint (2019)`

## Initial Read

The corpus appears to contain relevant authentication evidence, but the top of the ranked list is dominated by semantically similar endpoint or response chunks before the truly relevant authentication chunks surface.

## Related Pages

- [Good Recall, Weak Ranking](../wiki/failure-modes/good-recall-weak-ranking.md)
- [Hard-Case And Trace Review](../wiki/evaluations/hard-case-trace-review.md)

## Source Trail

- Hugging Face dataset API and data files accessed on 2026-04-09
