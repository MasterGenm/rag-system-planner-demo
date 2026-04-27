# Cases

## v0.1 阶段说明

本目录的 case 全部为 `retrospective_application` 类型，即基于公开 postmortem 对 Skill 判断协议进行回顾性应用。

`production_use` 类型的 case 需要仓库被真实生产使用后产生，留待 v0.2。

## 索引

| case_id | 标题 | 来源 | failure_family | 类型 |
|---|---|---|---|---|
| CASE-0001 | Court Logic capstone | medium.com | retrieval | 基础 |
| CASE-0002 | RAG Done Right | blog.stackademic.com | generation | 多 failure 叠加 |
| CASE-0003 | Lettria GraphRAG | qdrant.tech | ranking | 潜在反例 |

## 阅读建议

按 case_id 升序阅读：从 Skill 应能精准判断的基础 case，过渡到多 failure 叠加 case，最后到 Skill 与原作者判断不一致的反例。
