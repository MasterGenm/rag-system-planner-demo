# 运行日志 JSONL 规范

## 目的

Run log 是 CLI 在执行 `plan` 或 `diagnose` 时追加写入的运行记录，用于后续复现、审计和批量评估一次渲染调用。

## 触发

仅当调用 `cli.rag_planner` 的 `plan` 或 `diagnose` 子命令并显式传入 `--run-log <file>` 时，CLI 会向指定文件追加一行记录。

`validate` 子命令不产生 run log。

## 格式

Run log 文件格式为 JSONL：

- 每行是一个完整 JSON 对象。
- 文件编码为 UTF-8。
- 行结尾为 `\n`。
- 文件不应包含 BOM。

## 字段表

| 字段名 | 类型 | 是否必填 | 取值约束 | 示例 | 用途说明 |
|---|---|---|---|---|---|
| `run_id` | string | 是 | UUID v4 字符串 | `"<uuid4>"` | 标识一次 CLI 运行。 |
| `timestamp` | string | 是 | UTC ISO-8601 时间字符串 | `"<ISO-8601-UTC>"` | 记录运行发生时间。 |
| `mode` | string | 是 | 只能是 `plan` 或 `diagnose` | `"<plan-or-diagnose>"` | 标识本次运行使用的 CLI 模式。 |
| `input_sha256` | string | 是 | 输入 JSON 文本的 SHA-256，64 位十六进制字符串 | `"<64-hex>"` | 在不保存输入正文的前提下标识输入内容。 |
| `input_path` | string | 是 | 输入文件路径，或 stdin 输入时的 `stdin` | `"<input-path-or-stdin>"` | 标识输入来源。 |
| `output_sha256` | string | 是 | 输出 Markdown 文本的 SHA-256，64 位十六进制字符串 | `"<64-hex>"` | 在不保存输出正文的前提下标识输出内容。 |
| `output_path` | string | 是 | 输出文件路径，或 stdout 输出时的 `stdout` | `"<output-path-or-stdout>"` | 标识输出去向。 |
| `schema_version` | string | 是 | 当前 schema 契约版本 | `"<schema-version>"` | 标识校验输入时使用的 schema 契约版本。 |
| `cli_version` | string | 是 | 当前 CLI 版本字符串 | `"<cli-version>"` | 标识生成记录的 CLI 版本。 |

## 示例

```json
{"cli_version":"<cli-version>","input_path":"<input-path-or-stdin>","input_sha256":"<64-hex>","mode":"<plan-or-diagnose>","output_path":"<output-path-or-stdout>","output_sha256":"<64-hex>","run_id":"<uuid4>","schema_version":"<schema-version>","timestamp":"<ISO-8601-UTC>"}
```

## 保留与轮转

本仓库不规定 run log 的保留期、轮转周期、归档方式或删除策略。

这些策略由调用方根据自身的审计、存储和合规要求决定。

## 隐私边界

Run log 不保存输入 JSON 正文。

Run log 不保存输出 Markdown 正文。

Run log 不保存调用者身份、IP 地址或主机名。
