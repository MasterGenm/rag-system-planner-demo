# 示例：真实诊断路径

## 目的

说明这套工件脚手架不是空模板。它已经包含两条基于外部或本地评测证据的真实诊断路径。

## 路径 1：召回够用，但排序偏弱

来自数据集的文件：

- `artifacts/rag-wiki-template/sources/2026-04-09-rag-qa-logs-corpus-source-extract.md`
- `artifacts/rag-wiki-template/wiki/case-notes/developer-docs-auth-ranking-drift.md`
- `artifacts/rag-wiki-template/queries/developer-docs-auth-ranking-diagnostic.md`

为什么重要：

- 候选集中已经包含相关的认证片段
- 排在最前面的区域被语义相邻但相关性更弱的接口材料占据
- 这个问题更像排序漂移，而不是证据缺失

## 路径 2：证据分散

来自检索评测的文件：

- `artifacts/rag-wiki-template/sources/2026-04-09-open-support-copilot-retrieval-eval-extract.md`
- `artifacts/rag-wiki-template/wiki/case-notes/architecture-comparison-evidence-collapse.md`
- `artifacts/rag-wiki-template/queries/architecture-comparison-scattered-evidence-diagnostic.md`

为什么重要：

- 比较问题需要同时覆盖 Chroma 和 Qdrant 两边的证据
- 检索结果却收敛到单侧证据邻域，没能形成双边覆盖
- 这个失败更适合用“证据广度不足”和“截断”来解释，而不是单纯排序错误

## 这些示例说明了什么

这两条路径分别代表两种常见诊断场景：

- 候选集已经够用，但排序弱
- 主题命中了，但证据广度不够支撑问题类型

这让这套脚手架更像 `rag-system-planner` 的真实延伸，而不是只改了提示词的版本。
