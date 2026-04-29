# v0.1.0 发布检查清单

## 用法

本清单由发起人在 `git push` 之前逐项勾选。

执行方 AI 不勾选、不替发起人决定 push 时机。

## 代码与测试

- [ ] `pytest -q` 全绿
- [ ] `python benchmarks/_check_coverage.py` 退出 0
- [ ] `python benchmarks/score_run.py --runs benchmarks/_self_test_run --threshold 0` 退出 0
- [ ] `python scripts/check_freshness.py --as-of <today>` 退出 0
- [ ] schema 文件通过 draft 2020-12 校验

## 文档

- [ ] `CHANGELOG.md` 含 v0.1.0 条目且日期正确
- [ ] `cases/README.md` 含 v0.1 阶段说明（`retrospective_application` 边界）
- [ ] `docs/freshness-policy.md` 存在且与 `check_freshness.py` 行为一致

## 元数据

- [ ] 所有 frontmatter 中的 `<owner>` 已替换为真实 GitHub handle（涉及文件：`SKILL.md` / cursor mdc / `docs/freshness-policy.md` / 三个 case 文件）

## 发布动作

- [ ] 本地 git tag `v0.1.0` 已存在
- [ ] 远端推送：`git push origin main && git push origin v0.1.0`
- [ ] 远端 GitHub Actions 工作流首次执行结果检查（绿/红）
- [ ] 如远端 CI 红：在远端 issue 中记录失败步骤，**不立即修复**，由发起人决定下一步

## v0.2 规划入口

- [ ] 在仓库 README 或 ROADMAP（如新增）中标注：CASE-0001 / CASE-0002 / CASE-0003 揭示的 Skill 协议改进观察留待 v0.2 评估吸收
- [ ] 标注：`production_use` 类型 case 留待 v0.2
