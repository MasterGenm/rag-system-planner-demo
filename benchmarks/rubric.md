# Benchmark Rubric

本 rubric 用于 deterministic scoring。
它评测的是 planner 输出是否符合结构化判断协议，不评测文字是否优美。

每个 case 总分 10 分，包含 5 个维度，每个维度 0/1/2 分。

## 输入输出约定

`score_run.py` 读取一个 runs 目录。
目录中每个输出文件使用 `<case_id>.json` 命名，例如：

```json
{
  "mode": "diagnosis",
  "failure_family": "ranking",
  "evidence_labels": ["observed", "inferred", "unknown"],
  "next_action_class": "inspect_ranking",
  "recommendations": ["Audit first relevant rank before changing architecture."]
}
```

允许输出包含额外字段。
scorer 只读取本 rubric 中定义的字段，并扫描所有字符串值以检查 `must_avoid`。

## 评分维度

| 维度 | 0 分 | 1 分 | 2 分 |
|------|------|------|------|
| Mode 选择 | `mode` 错误或缺失 | 不适用 | `mode` 正确 |
| Failure family 选择 | `failure_family` 错误或缺失 | 与 expected 接近 | 与 expected 相同 |
| 证据标签使用 | 缺失、为空，或全部是 `inferred` | 出现部分 required labels | 出现全部 required labels |
| 升级克制 | 输出触发 expected.must_avoid 中任一项，且未声明有效豁免 | 触发 must_avoid 且声明豁免，但场景不允许豁免 | 未触发 expected.must_avoid；或场景允许豁免且输出声明豁免 |
| 下一步动作分类 | `next_action_class` 不在枚举内或缺失 | 枚举内但与 expected 不同族 | 与 expected 同族 |

## Failure Family 接近关系

用于给 1 分：

- `retrieval` 与 `ranking` 接近
- `ranking` 与 `retrieval`、`generation` 接近
- `generation` 与 `ranking` 接近
- `observability` 不与其它 family 接近
- `not_applicable` 不与其它 family 接近

## Evidence Labels

如果场景没有要求 `evidence_labels_must_appear`，该维度直接给 2 分。

如果场景要求标签：

- 输出缺失 `evidence_labels`、为空，或只有 `inferred`，给 0 分。
- 输出包含部分 required labels，给 1 分。
- 输出包含全部 required labels，给 2 分。

因此，对要求同时出现 `observed` 和 `unknown` 的场景，只有两者都出现才给 2 分。

## Must Avoid

`must_avoid` 用于测试升级克制。

scorer 会把输出 JSON 中所有字符串值收集起来，做大小写不敏感的子串检查。
如果出现 expected.must_avoid 中任一项，则默认视为触发升级克制风险。

### v0.1.1 起：语境化豁免

当场景的 `expected.allow_escalation_exception` 为真时，命中 must_avoid 的输出如果显式声明了豁免，评分维度给 2 分。豁免声明关键词为以下任一项：

- `escalation_exception_declared`
- `bounded_experiment`
- `语境化延后`

当 `expected.allow_escalation_exception` 缺省或为假时，命中 must_avoid 仍然违反默认克制；如果输出同时声明豁免，给 1 分作为部分理解，否则给 0 分。

## Next Action Class

有效枚举与 `benchmarks/README.md` 保持一致：

- `investigate_chunking`
- `fix_metadata_filters`
- `inspect_ranking`
- `tighten_answer_policy`
- `add_observability`
- `build_eval_set`
- `compare_vector_store`
- `defer_agentic_upgrade`
- `define_metadata_baseline`

Action family:

- `retrieval_baseline`: `investigate_chunking`, `fix_metadata_filters`, `define_metadata_baseline`
- `ranking`: `inspect_ranking`
- `generation`: `tighten_answer_policy`
- `observability`: `add_observability`
- `evaluation`: `build_eval_set`
- `comparison`: `compare_vector_store`, `defer_agentic_upgrade`

如果输出 action 与 expected action 属于同一个 action family，给 2 分。
如果输出 action 在枚举内但属于不同 action family，给 1 分。
如果输出 action 缺失或不在枚举内，给 0 分。

## 反目标

本 rubric 不包含以下项：

- 行文流畅度
- 语言自然度
- 表达风格
- 观点是否讨喜

这些项不能稳定机评，不进入当前 P0 benchmark。
