# Artifact Workflow

当你需要理解 durable workspace 的生命周期时，使用这份 reference。
如果要看精确操作要求，读取 `artifact-maintenance-contract.md`。
如果只需要最短 runbook，读取 `artifact-operation-checklists.md`。

## 核心模型（Core Model）

把 durable 的 RAG 知识表示成三层：

1. `sources/`
   原始证据，例如 specs、traces、evaluation outputs、incident notes 和 architecture writeups。
2. `wiki/`
   综合后的操作性知识，例如 patterns、failure modes、evaluation notes、stack decisions 和 case notes。
3. `queries/`
   值得保存的一次性 memo 或 comparison，之后有机会再晋升到 `wiki/`。

## 生命周期（Lifecycle）

1. Planner 在从零推理之前先读 workspace。
2. Planner 做出一个有边界的判断。
3. 当达到 artifact update threshold 时，planner hand off durable findings。
4. Artifact-maintenance 执行 `ingest`、`query`、`lint` 或 `index`。
5. 后续的 planner 会话从已维护好的 workspace 出发，而不是重新发现同一条经验。

## 共享规则（Shared Rules）

- 输入尽量使用 workspace-relative 路径。
- `sources/` 是原始证据，默认应保持不可变。
- 对大 source，先导航，再深入阅读；当可以有目标地读取时，不要从盲目 dump 中做综合。
- `wiki/` 或 `queries/` 中的重要结论应带有可见的 evidence trail。
- 优先更新一个 canonical page，而不是创建近似重复页。
- 把 source staleness 当成真实状态。如果 source 变了，就刷新关系或把它标成 stale，不要悄悄假设它仍然有效。
- `index.md` 和 `log.md` 是维护合同的一部分，不是可选清理项。

## 现在先不做（Not Now）

这个 workbench 还没有实现 MinerU 风格的工具，例如自动 ingest trackers、stale-source detection 或 deep-reading helpers。
当前目标是先把 maintenance contract 做到足够清晰，这样以后再加这些工具时，不需要改变概念模型。
