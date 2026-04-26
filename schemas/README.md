# 输入 JSON Schema

本目录定义 renderer 可接受的 JSON 输入结构。

Schema 只约束当前 renderer 已经支持的字段，不为未来字段预留扩展块。所有顶层未知字段都会被拒绝。

## plan_input.schema.json

用于 `render_rag_plan.py`。

| 字段 | 必填 | 类型 | 语义 |
| --- | --- | --- | --- |
| `title` | 否 | `string` | 文档标题；缺省时 renderer 使用 `RAG Solution Package`。 |
| `problem_summary` | 否 | `string` | 问题概述。 |
| `assumptions` | 否 | `array<string>` | 假设和约束。 |
| `recommended_stack` | 否 | `array<string>` | 推荐技术栈或组件选择。 |
| `architecture` | 否 | `string \| array<string> \| object` | 架构和数据流说明。 |
| `retrieval_design` | 否 | `string \| array<string> \| object` | 检索设计说明。 |
| `agent_guidance` | 否 | `string \| array<string> \| object` | agent 集成边界和建议。 |
| `evaluation` | 否 | `string \| array<string> \| object` | 评测方案。 |
| `observability` | 否 | `string \| array<string> \| object` | 可观测性方案。 |
| `risks` | 否 | `string \| array<string> \| object` | 风险与权衡。 |
| `rollout` | 否 | `object` | 分阶段上线计划；键只能是 `Phase 0..5`、`now`、`next`、`later`，值必须是 `array<string>`。 |

## diagnostic_input.schema.json

用于 `render_rag_diagnostic.py`。

| 字段 | 必填 | 类型 | 语义 |
| --- | --- | --- | --- |
| `title` | 否 | `string` | 文档标题；缺省时 renderer 使用 `RAG Diagnostic Report`。 |
| `symptoms` | 否 | `array<string>` | 症状概述。 |
| `hypotheses` | 否 | `object` | 工作假设；键只能是 `observed`、`inferred`、`unknown`，值必须是 `array<string>`。 |
| `missing_evidence` | 否 | `array<string>` | 缺失证据。 |
| `investigation_order` | 否 | `array<string>` | 排查顺序。 |
| `recommended_changes` | 否 | `object` | 推荐改动；键只能是 `now`、`next`、`later`，值必须是 `array<string>`。 |
| `evaluation_additions` | 否 | `array<string>` | 需要补充的评测。 |
| `observability_additions` | 否 | `array<string>` | 需要补充的可观测性信号。 |
| `risks` | 否 | `array<string> \| object` | 风险与预期影响。 |

## 设计边界

- Schema 使用 JSON Schema draft 2020-12。
- Schema 不校验 URI、日期或业务格式。
- Schema 只负责输入结构，不负责判断 RAG 架构建议是否正确。
