# Benchmark 场景集

本目录把 `rag-system-planner` 的判断协议转成可回归的 benchmark seed。

当前目标不是评测最终语言质量，而是评测 planner 是否能做出稳定、克制、可证据化的判断。

## 目录结构

- `scenarios/`：固定场景，每个文件一个 case。
- `scenarios/_index.csv`：场景索引，便于快速检查覆盖矩阵。
- `_check_coverage.py`：覆盖检查脚本。

## 单个场景结构

```json
{
  "case_id": "BCH-0001",
  "mode": "diagnosis",
  "input": {},
  "expected": {
    "mode": "diagnosis",
    "failure_family": "ranking",
    "evidence_labels_must_appear": ["observed", "unknown"],
    "must_avoid": ["graph_rag"],
    "next_action_class": "inspect_ranking"
  },
  "rationale": "中文说明为什么这个场景属于该类别。"
}
```

## Mode

- `greenfield`：新系统规划。
- `diagnosis`：已有系统排障。
- `comparison`：方案比较或是否升级的决策。

## Failure Family

`failure_family` 只对 `diagnosis` 场景有覆盖要求。

- `retrieval`：候选证据没有进入候选集，或被 filter、chunking、OCR、metadata 问题阻断。
- `ranking`：证据已经进入候选集，但排序、重排、citation anchor 或 context packing 不足。
- `generation`：证据存在，但答案层 unsupported、未 abstain、或 citation assembly 放大错误。
- `observability`：缺少 traces、stage timings、retrieved ids 等信号，无法可靠定位根因。
- `not_applicable`：用于 `greenfield` 和 `comparison` 场景。

## next_action_class 枚举

- `investigate_chunking`
- `fix_metadata_filters`
- `inspect_ranking`
- `tighten_answer_policy`
- `add_observability`
- `build_eval_set`
- `compare_vector_store`
- `defer_agentic_upgrade`
- `define_metadata_baseline`

## 覆盖要求

- `greenfield` 至少 4 个。
- `diagnosis` 至少 8 个。
- `comparison` 至少 3 个。
- diagnosis 下的 `retrieval`、`ranking`、`generation`、`observability` 各至少 2 个。
- 至少 1 个场景要求避免过早升级到 graph 或 multi-agent。
- 至少 1 个场景要求同时出现 `observed` 与 `unknown`。
