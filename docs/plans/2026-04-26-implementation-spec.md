# rag-system-planner-demo 落地实施规格

> 配套文档：[2026-04-26-productionization-review.md](2026-04-26-productionization-review.md)
> 本文档把 review 中的方向，拆成跨平台 AI 可独立执行的任务规格。

---

## 0. 给执行方 AI 的元说明（必读）

### 0.1 你是谁、做什么

你是被指派来推进 `rag-system-planner-demo` 仓库生产化的一名工程协作者。
你不是被指派来重新设计这个仓库，也不是被指派来评审方向。
方向已经在 `2026-04-26-productionization-review.md` 中决定。
你的工作是按本文件中的任务，逐项交付。

### 0.2 不可逾越的红线

以下行为属于"偏题"，禁止：

1. **不重写两个 renderer**（`render_rag_plan.py` / `render_rag_diagnostic.py`）。它们已经够用，只允许小修 bug，不允许重构、改风格、改 ORDER_PRIORITY。
2. **不引入新框架**。不要引入 LangChain / LlamaIndex / 向量数据库 SDK / orchestration 库。本仓库是规划/诊断的 Skill，不是 RAG 运行时。
3. **不加在线服务**。不要写 FastAPI、不要写 Web UI、不要建 Docker。CLI 即可。
4. **不要把 Skill 文档拆散成更多页**。在评测体系建立前，禁止扩充 failure taxonomy / 增加新 mode / 增加新 reference 页。
5. **不要并行启动多个任务**。逐个交付、逐个验收。每个任务有独立 PR-粒度的产出。
6. **不要替换已有依赖最小集**。仅允许新增 `pytest`、`jsonschema` 这两个开发依赖。其它新依赖必须先在 issue 中讨论。
7. **不要写不可机评的"软指标"**。所有验收标准必须是命令行能运行出 pass/fail 的检查。

### 0.3 通用工作流

每个任务执行前：

1. 阅读 `2026-04-26-productionization-review.md` 的"Project Context"和"Current Diagnosis"段。
2. 阅读本文件的对应任务节。
3. 阅读任务节中"必读上下文"列出的所有文件。
4. 仅修改任务节"产物"中列出的文件。其它文件不得改动。
5. 完成后，按"验收命令"中列出的命令本地复跑，全部通过才算完成。

### 0.4 中英文约定

- 所有 Markdown 文档：**中文**为主，技术术语保留英文。
- 所有代码、JSON 字段、文件名、命令：**英文**。
- 所有 commit message：英文，遵循 Conventional Commits（`feat:`/`test:`/`docs:`/`chore:`）。

---

## 1. 仓库当前状态快照（2026-04-26）

```
rag-system-planner-demo/
├── LICENSE
├── README.md
├── cursor/rules/rag-system-planner.mdc       # Cursor 规则副本
├── skills/rag-system-planner/
│   ├── SKILL.md                              # 核心 Skill 定义
│   ├── examples/                             # 既有示例
│   └── scripts/
│       ├── render_rag_plan.py                # 渲染规划 Markdown
│       └── render_rag_diagnostic.py          # 渲染诊断 Markdown
└── docs/plans/
    ├── 2026-04-26-productionization-review.md  # 方向文档
    └── 2026-04-26-implementation-spec.md       # 本文件
```

执行方 AI 在动手前，必须先用 `ls` 或等价工具确认这棵树仍然成立；如果出现新文件，先停下来询问发起人。

---

## 2. 任务总览

| ID  | 名称 | 依赖 | 预估规模 | 优先级 |
|-----|------|------|----------|--------|
| T1  | 渲染器 pytest 回归套件 | — | 0.5d | P0 |
| T2  | 输入 JSON Schema 定义 | T1 | 0.5d | P0 |
| T3  | Benchmark 场景集（15–20） | T2 | 1.5d | P0 |
| T4  | Rubric 定义与机评脚本 | T3 | 1d | P0 |
| T5  | 薄 CLI Runner | T2 | 1d | P1 |
| T6  | 遥测合约文档 | — | 0.5d | P1 |
| T7  | 运行日志 JSONL 规范 | T5 | 0.5d | P1 |
| T8  | 最小 CI | T1, T4 | 0.5d | P1 |
| T9  | Pilot Cases（2–3 个真实案例） | T5, T7 | 1d | P2 |
| T10 | 新鲜度元数据 | — | 0.5d | P2 |
| T11 | v0.1 发布纪律 | T1–T10 | 0.5d | P2 |

**执行顺序**：T1 → T2 → T3 → T4 → T8（CI 提前接 T1+T4）→ T5 → T7 → T6 → T9 → T10 → T11

---

## 3. 任务详细规格

### T1 — 渲染器 pytest 回归套件

**目标**：让 `render_rag_plan.py` 与 `render_rag_diagnostic.py` 拥有可机器执行的回归测试，防止后续修改静默退化。

**必读上下文**：
- [skills/rag-system-planner/scripts/render_rag_plan.py](../../skills/rag-system-planner/scripts/render_rag_plan.py)
- [skills/rag-system-planner/scripts/render_rag_diagnostic.py](../../skills/rag-system-planner/scripts/render_rag_diagnostic.py)

**产物**（仅允许新增/修改这些文件）：
- `tests/__init__.py`（空文件）
- `tests/conftest.py`（添加 `sys.path` 注入，使 `scripts/` 可导入）
- `tests/test_render_rag_plan.py`
- `tests/test_render_rag_diagnostic.py`
- `tests/fixtures/plan_minimal.json`
- `tests/fixtures/plan_full.json`
- `tests/fixtures/diagnostic_minimal.json`
- `tests/fixtures/diagnostic_full.json`
- `tests/fixtures/expected/plan_minimal.md`
- `tests/fixtures/expected/plan_full.md`
- `tests/fixtures/expected/diagnostic_minimal.md`
- `tests/fixtures/expected/diagnostic_full.md`
- `pyproject.toml`（仅允许新增 `[tool.pytest.ini_options]` 与 dev 依赖段）

**测试覆盖必须包含**：

1. happy path：完整 payload → Markdown 输出与 `expected/*.md` 字符串相等。
2. minimal payload：只含 `title` 一个键 → 仅输出标题，不抛异常。
3. 缺失字段：缺 `recommended_stack` / `recommended_changes` 等 → 该 section 完全不渲染（不出现空标题）。
4. 嵌套 dict：`rollout` 里嵌套 dict → 多级 heading 正确，heading 层级不超过 6。
5. 排序：`rollout` 中乱序的 `Phase 2 / Phase 0 / Phase 1` → 按 `ORDER_PRIORITY` 重排。
6. 排序：`hypotheses` 中 `unknown / observed / inferred` → 按 `ORDER_PRIORITY` 重排为 observed / inferred / unknown。
7. 错误：非 dict 顶层（如 `[]` 或 `"x"`）→ `SystemExit`。
8. 错误：非法 JSON → `SystemExit`，错误消息含 "Invalid JSON"。
9. 错误：`--input` 指向不存在文件 → `SystemExit`，错误消息含 "Input file not found"。
10. CLI：`--output` 写入磁盘，文件以单个 `\n` 结尾，UTF-8 无 BOM。

**验收命令**：

```bash
pytest -q
```

必须 100% 通过，且 `pytest --collect-only` 报告测试数 ≥ 14。

**反目标**：
- 不要为提高覆盖率而 mock 内部函数。测试应当通过 stdin/参数从外部驱动。
- 不要修改 renderer 源码。如果发现 bug，独立提一个"已发现 bug"的笔记到 PR 描述里，由发起人决定是否修。

---

### T2 — 输入 JSON Schema 定义

**目标**：把当前 renderer 隐含的输入约定，固化为可校验的 JSON Schema（draft 2020-12）。

**必读上下文**：T1 的 fixtures、两个 renderer 顶部的 docstring。

**产物**：
- `schemas/plan_input.schema.json`
- `schemas/diagnostic_input.schema.json`
- `schemas/README.md`（说明每个字段的语义、必填/可选、取值约束，**中文**）
- `tests/test_schema_validation.py`

**Schema 必须包含的字段约束**（不要超出此范围）：

`plan_input.schema.json`：
- `title`（string，可选，默认 `"RAG Solution Package"`）
- `problem_summary`（string）
- `assumptions`（array<string>）
- `recommended_stack`（array<string>）
- `architecture`（string | array<string> | object）
- `retrieval_design`（同上）
- `agent_guidance`（同上）
- `evaluation`（同上）
- `observability`（同上）
- `risks`（同上）
- `rollout`（object，键为 `Phase 0..5` / `now` / `next` / `later`，值为 array<string>）
- `additionalProperties: false`（所有顶层未列出的键都拒绝）

`diagnostic_input.schema.json`：
- `title`（string，可选）
- `symptoms`（array<string>）
- `hypotheses`（object，键限定为 `observed` / `inferred` / `unknown`，值为 array<string>）
- `missing_evidence`（array<string>）
- `investigation_order`（array<string>）
- `recommended_changes`（object，键限定为 `now` / `next` / `later`）
- `evaluation_additions`（array<string>）
- `observability_additions`（array<string>）
- `risks`（array<string> 或 object）
- `additionalProperties: false`

**验收命令**：

```bash
pytest tests/test_schema_validation.py -q
python -c "import json, jsonschema; jsonschema.Draft202012Validator.check_schema(json.load(open('schemas/plan_input.schema.json')))"
python -c "import json, jsonschema; jsonschema.Draft202012Validator.check_schema(json.load(open('schemas/diagnostic_input.schema.json')))"
```

T1 的 4 个 fixture JSON 必须全部通过对应 schema 的校验，且至少 3 个故意构造的非法样例（多余字段、错类型、错枚举）被拒绝。

**反目标**：
- 不要给 schema 加 `format: uri` / `format: date-time` 等运行时校验，这里只约束结构。
- 不要为"未来可能有的字段"预留 `extensions` 块。

---

### T3 — Benchmark 场景集

**目标**：建立 15–20 个稳定场景，覆盖 3 个 mode × 4 个 failure family，作为后续判断质量的基准。

**必读上下文**：
- `skills/rag-system-planner/SKILL.md`（核心契约 / failure taxonomy / triage matrix）
- T2 的两个 schema

**产物**：
- `benchmarks/scenarios/<id>.json`（共 15–20 个文件）
- `benchmarks/scenarios/_index.csv`（id, mode, failure_family, source）
- `benchmarks/README.md`（说明场景结构与覆盖矩阵）

**单个场景文件结构**：

```json
{
  "case_id": "BCH-0001",
  "mode": "diagnosis",
  "input": { "...": "符合 schema 的输入" },
  "expected": {
    "mode": "diagnosis",
    "failure_family": "retrieval",
    "evidence_labels_must_appear": ["observed", "unknown"],
    "must_avoid": ["graph_rag", "multi_agent_rewrite"],
    "next_action_class": "investigate_chunking"
  },
  "rationale": "中文写一句为什么这是该 family"
}
```

**覆盖矩阵硬性要求**：

- mode 维度：`greenfield` ≥ 4，`diagnosis` ≥ 8，`comparison` ≥ 3
- failure family 维度（仅适用于 diagnosis）：`retrieval` / `ranking` / `generation` / `observability` 各 ≥ 2
- 至少 1 例 expected `must_avoid` 包含"过早升级到 graph 或 multi-agent"，用来测试克制性
- 至少 1 例 expected `evidence_labels_must_appear` 同时含 `observed` 与 `unknown`，用来测试证据诚实度

**验收命令**：

```bash
python benchmarks/_check_coverage.py
```

`_check_coverage.py` 也由本任务交付，输出覆盖矩阵；任意一格为 0 则退出码非零。

**反目标**：
- 场景内容不要凭空编造企业名称、人名。用泛化描述（"一家电商客服 RAG"）。
- 不要把 `expected.next_action_class` 写成自由文本，必须从有限枚举集（在 `benchmarks/README.md` 中列出）中选。

---

### T4 — Rubric 定义与机评脚本

**目标**：把"判断质量好不好"这件事变成可机评的脚本。

**必读上下文**：T3 的全部产物。

**产物**：
- `benchmarks/rubric.md`（中文，定义 5 个评分维度）
- `benchmarks/score_run.py`（机评入口）
- `tests/test_score_run.py`

**5 个评分维度**（每维度 0/1/2 三档）：

| 维度 | 0 分 | 1 分 | 2 分 |
|------|------|------|------|
| Mode 选择 | 错 | — | 对 |
| Failure family 选择 | 错 | 接近 | 对 |
| 证据标签使用 | 缺失或全 inferred | 部分使用 | 含 observed + unknown |
| 升级克制 | 触发 must_avoid | — | 未触发 |
| 下一步动作分类 | 不属枚举 | 枚举内但与 expected 不同族 | 与 expected 同族 |

总分 0–10。

**`score_run.py` 行为**：

- 输入：一个目录，里面是模型对每个 `case_id` 的输出（JSON 文件，文件名 = case_id）
- 输出：stdout 打印每个 case 的得分明细 + 总均分；同时写 `benchmarks/runs/<timestamp>.jsonl`
- 退出码：均分 < 阈值（默认 7.0，可 `--threshold` 覆盖）→ 非零

**验收命令**：

```bash
pytest tests/test_score_run.py -q
python benchmarks/score_run.py --runs benchmarks/_self_test_run --threshold 0
```

`_self_test_run/` 由本任务提供，是一份"故意全对"的示例输出，用于自检脚本本身没坏。

**反目标**：
- 不要在 rubric 里引入"行文流畅度""语言自然度"等无法机评的项。
- 不要让 `score_run.py` 调任何 LLM。这是 deterministic scorer。

---

### T5 — 薄 CLI Runner

**目标**：提供唯一的可复现执行入口，串起 schema 校验 → mode 选择 → renderer 调用。

**必读上下文**：两个 renderer、T2 的 schema。

**产物**：
- `cli/__init__.py`
- `cli/rag_planner.py`
- `tests/test_cli.py`
- `pyproject.toml`：在 `[project.scripts]` 注册 `rag-planner = "cli.rag_planner:main"`

**子命令规格**：

```
rag-planner plan      --input <file|->  [--output <file>]  [--run-log <file>]
rag-planner diagnose  --input <file|->  [--output <file>]  [--run-log <file>]
rag-planner validate  --input <file|->  --mode {plan|diagnose}
```

**行为**：

- `plan` / `diagnose`：先用对应 schema 校验输入；校验失败 → 退出码 2 + stderr 列出错误路径。校验通过 → 调用对应 renderer → stdout 输出 Markdown（或写到 `--output`）；同时如果给了 `--run-log`，追加一行 JSONL（格式见 T7）。
- `validate`：仅校验，不渲染。
- `--input -` 表示从 stdin 读。

**验收命令**：

```bash
pytest tests/test_cli.py -q
echo '{"title":"x"}' | python -m cli.rag_planner plan --input -
echo '{"title":"x","unknown_key":1}' | python -m cli.rag_planner validate --input - --mode plan ; test $? -eq 2
```

**反目标**：
- 不要做交互式提问。不要 `input()`。
- 不要做颜色/进度条。stdout 必须是干净的 Markdown，方便 pipe。

---

### T6 — 遥测合约文档

**目标**：明确写出"做诊断之前，调用方至少要采到哪些字段"。

**产物**：
- `docs/telemetry-contract.md`（中文）

**文档必须包含**：

1. 字段表（必填 / 可选 / 类型 / 示例 / 用途）
2. 最小字段集：`query_text`、`normalized_query`、`retrieved_doc_ids`、`retrieval_scores`、`metadata_filters`、`rerank_decisions`、`prompt_assembly`、`stage_latencies_ms`、`citations_returned`、`artifact_writes`
3. 每个字段一条"为什么需要它"的诊断用途说明
4. 一个 mermaid 图：trace 字段如何对应到 triage matrix 的 4 个 failure family
5. 明确指出：本仓库不实现采集，只规定契约

**验收命令**：

```bash
test -f docs/telemetry-contract.md
grep -c "^## " docs/telemetry-contract.md  # 至少 5 个二级标题
```

**反目标**：
- 不要绑定具体厂商（不写 LangSmith / Phoenix / Datadog 的 SDK 调用）。
- 不要伪造数据点示例（用 `<doc_42>` 而不是真实 URL）。

---

### T7 — 运行日志 JSONL 规范

**目标**：CLI 的每次执行都能落盘成可重放的运行记录。

**产物**：
- `docs/run-log-format.md`（中文规范）
- T5 中 `--run-log` 实现的具体字段

**单行 JSON 必填字段**：

```json
{
  "run_id": "uuid4",
  "timestamp": "ISO-8601 UTC",
  "mode": "plan|diagnose",
  "input_sha256": "...",
  "input_path": "...|stdin",
  "output_sha256": "...",
  "output_path": "...|stdout",
  "schema_version": "1",
  "cli_version": "x.y.z"
}
```

**验收命令**：

```bash
echo '{"title":"x"}' | python -m cli.rag_planner plan --input - --run-log /tmp/r.jsonl
python -c "import json; [json.loads(l) for l in open('/tmp/r.jsonl')]"
```

**反目标**：
- 不要在 run log 里写完整的 input/output 内容（只写 sha256 和路径）。
- 不要在 run log 里写用户身份、机器名等可识别信息。

---

### T8 — 最小 CI

**目标**：让 push / PR 自动跑 T1 + T2 + T4 的检查。

**产物**：
- `.github/workflows/ci.yml`

**workflow 必须**：

- 触发：`push` 到任意分支，`pull_request` 到 `main`
- Python 3.11
- 步骤：装依赖 → `pytest -q` → 校验所有 schema → 跑 `benchmarks/_check_coverage.py` → 跑 `benchmarks/score_run.py --runs benchmarks/_self_test_run --threshold 0`
- 任一步失败 → CI 红

**验收命令**：

```bash
yamllint .github/workflows/ci.yml || true   # 仅可读性参考
```

发起人在远端验证 CI 实际运行。

**反目标**：
- 不要加部署、发布、coverage 上传、benchmark 报告 PR 评论等"看起来很专业"的步骤。当前阶段只要绿/红信号。

---

### T9 — Pilot Cases

**目标**：记录 2–3 个真实使用案例，证明 Skill 在真实场景中起到作用（或没起到作用，并诚实记录）。

**前置**：发起人提供原始材料（评测截图、trace 片段、决策结果）。如果没有，本任务挂起，不得编造。

**产物**：
- `cases/2026-MM-DD-<slug>.md`，每个文件含：
  - 背景
  - 输入证据（脱敏）
  - Skill 给出的判断
  - 实际采取的行动
  - 后续观察到的结果
  - 学到的教训
- `cases/README.md`（索引）

**验收命令**：

```bash
test -d cases && ls cases/*.md | wc -l  # 至少 2
```

**反目标**：
- 不要写"成功故事"。诚实记录"判断对了"和"判断错了"两类。
- 不要在 case 中放可识别公司/个人信息。

---

### T10 — 新鲜度元数据

**目标**：让长期文档（Skill、failure taxonomy、case）带上腐烂信号。

**产物**：
- 给以下文件追加 YAML frontmatter：
  - `skills/rag-system-planner/SKILL.md`
  - `cursor/rules/rag-system-planner.mdc`
  - 每个 `cases/*.md`
- `docs/freshness-policy.md`（中文政策）
- `scripts/check_freshness.py`：扫描所有带 frontmatter 的文件，超过 `stale_after_days` 的列出来；超期 → 退出码非零

**frontmatter 字段**：

```yaml
---
last_validated_at: 2026-04-26
derived_from: [外部来源链接或仓库内文件]
owner: <github-handle>
stale_after_days: 180
---
```

**验收命令**：

```bash
python scripts/check_freshness.py --as-of 2026-04-26
```

**反目标**：
- 不要给短命文件（PR 模板、测试 fixture）加 frontmatter。
- 不要让 `stale_after_days` 全部一刀切（Skill 可以 180，case 可以 365）。

---

### T11 — v0.1 发布纪律

**前置**：T1–T10 全部完成且 CI 绿。

**产物**：
- `CHANGELOG.md`（Keep a Changelog 风格）
- 一次 git tag：`v0.1.0`
- `docs/release-checklist.md`：勾选项清单（CI 绿 / 所有 schema 校验通过 / freshness 检查通过 / pilot cases ≥ 2 / case-study 写完）

**验收命令**：

```bash
git tag --list | grep -q '^v0.1.0$'
test -f CHANGELOG.md && grep -q '^## \[0.1.0\]' CHANGELOG.md
```

**反目标**：
- 不要发布到 PyPI。
- 不要 GitHub Release Notes 写自夸语句，事实陈述即可。

---

## 4. 跨任务的统一规范

### 4.1 Python 风格

- Python ≥ 3.11
- 标准库优先；额外依赖只允许 `pytest`、`jsonschema`
- 不引入 mypy / ruff / black 配置（后续如果加，单独开任务）
- 每个新文件顶部一行简短 docstring，不写 ASCII 艺术、不写大段注释

### 4.2 文件命名

- Python：`snake_case.py`
- JSON Schema：`<thing>.schema.json`
- Markdown 文档：`kebab-case.md`，`docs/plans/` 下用 `YYYY-MM-DD-<slug>.md`

### 4.3 提交粒度

每个任务一个 commit（或一组 commit + 一个合并 commit）。commit 标题前缀：

- T1 / T3 → `test:`
- T2 / T7 → `feat(schema):` / `feat(runlog):`
- T5 → `feat(cli):`
- T6 / T9 / T10 → `docs:`
- T8 → `ci:`
- T11 → `chore(release):`

### 4.4 PR 描述模板

每个 PR 描述必须含：

```
## 对应任务
T<N>

## 验收命令本地输出
<粘贴验收命令的输出>

## 偏离规格的地方
<如无写"无"；若有，必须解释为什么>
```

---

## 5. 整体验收（执行完 T1–T11 后）

```bash
pytest -q
python benchmarks/_check_coverage.py
python benchmarks/score_run.py --runs benchmarks/_self_test_run --threshold 0
python scripts/check_freshness.py --as-of <today>
git tag --list | grep -q '^v0.1.0$'
```

全部通过且 CI 绿，则视为本规格完成。

---

## 6. 与 review 文档的对应关系

| review 中的 Highest-Leverage Change | 本规格中的任务 |
|------|------|
| 1. Goldens And Regression Harness | T3, T4 |
| 2. Incident/Evidence Bundle Schema | T2 |
| 3. Thin CLI Runner | T5 |
| 4. Telemetry Contract | T6 |
| 5. Small Real Pilot | T9 |
| 6. Freshness And Release Discipline | T10, T11 |

回归保护（review 中 Weeks 2-3）= T1 + T8。

---

## 7. 终止条件

如果在执行过程中发现以下任一情况，**停止动手**，回到发起人确认：

1. 任务规格与现有代码出现不兼容（例如 renderer 的实际输入约定与 T2 schema 冲突）
2. 验收命令在本地无法跑通且原因不明
3. 任务之间出现你认为应该并行/合并/拆分的强烈理由
4. 发起人提供的真实案例（T9）涉及不能脱敏的信息

不要"自行决定继续"。
