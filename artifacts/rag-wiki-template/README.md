# RAG Wiki Artifact Template

这是一个可直接复制的持久化 RAG 工作区模板。

## 用途

用这个工作区保存：

- `sources/` 里的原始证据
- `wiki/` 里的综合型 RAG 知识
- `queries/` 里的已保存答案与备忘录

## 从这里开始

1. 先读 `AGENTS.md`。
2. 再读 `index.md`。
3. 把第一份真实材料放进 `sources/`。
4. 当你要写 durable 的 ingest、lint 或 index-refresh 记录时，使用 `templates/` 里的模板。
5. 让 agent 执行 ingest、query、lint，或刷新工作区索引。

如果这是你第一次使用这个 scaffold，下一步读 [ADOPTION.md](ADOPTION.md)。
