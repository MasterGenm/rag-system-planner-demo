# Diagnosis Playbook

在 diagnosis 模式中先读取这份文件。先从 symptoms 开始，再逐步缩小问题区域，然后才给出 fixes。

## Evidence Labels

对所有判断明确打标：

- `observed`：得到用户描述或现有 traces 支持
- `inferred`：合理推断，但尚未被证实
- `unknown`：在收集更多证据之前，不能声称成立

不要把缺失 trace 当成某个组件失败的证据。

## Symptom To Cause Map

### Low Recall

可能原因：

- embedding 偏弱
- chunk size 或边界设计差
- metadata 缺失
- 缺少 hybrid retrieval
- query rewriting 差
- filters 错误

### High Hallucination Rate

可能原因：

- retrieval 返回了弱证据或无关证据
- prompt 没有强制 grounded answering
- citation assembly 出错
- 系统在应该 abstain 的时候仍然继续回答

### High Latency

可能原因：

- retrieval stack 过于复杂
- reranking stage 过大
- vector storage operations 过慢
- agent loops 过多
- 缺少缓存

### Good Retrieval But Weak Answers

可能原因：

- prompt assembly 有问题
- context packing 有问题
- generation model 对这个任务太弱
- citations 或 evidence 没有被清晰暴露给 generator

### Hard To Debug

可能原因：

- 缺少 traces
- 缺少 retrieval logs
- 没有 evaluation baseline
- 没有 stage-level latency breakdown

## Investigation Order

1. 用一个具体示例确认 symptom
2. 标记哪些是 observed、inferred 和 unknown
3. 判断失败是 retrieval 侧还是 generation 侧
4. 检查系统是否记录了足够的 evidence
5. 审查 chunking、metadata、filters 和 top-k 行为
6. 审查 embeddings 和 vector storage 选择
7. 审查 reranking 和 prompt assembly
8. 审查 evaluation 覆盖
9. 只有当更简单层已经 evidence-limited 时，才考虑 architecture upgrades

## Default Triage Ladder

当 failure mode 还不清楚时，使用这个默认顺序：

1. 症状确认
2. 证据充分性检查
3. retrieval baseline 审查
4. embedding 或 vector-store 审查
5. reranking 和 prompt 审查
6. architecture upgrade 讨论

## Remediation Pattern

按优先级推荐修改：

1. instrumentation gaps
2. retrieval baseline fixes
3. ranking 和 reranking fixes
4. prompt 和 answer policy fixes
5. architecture upgrades

除非 baseline 已经明确穷尽，否则不要从最复杂的重构开始。

## Actionability Pattern

把 remediation 组织成：

- `Now`：信息增益最高、且可逆的修改，或恢复证据链的动作
- `Next`：当证据路径变清晰后，再做的定向改进
- `Later`：需要已确认瓶颈支撑的高成本重构或架构变化

对每个 action，都说明：

1. 它针对的 symptom 是什么
2. 预期改变的 signal 或 metric 是什么
3. 什么结果会证伪这个 hypothesis

## When To Stop Speculating

当出现以下情况时，暂停 root-cause claims，优先补 instrumentation：

- 只记录了最终答案
- 缺少 retrieved chunk ids 或 scores
- 缺少 stage-level timings
- 系统混合了 text、scans 或 images，但缺少 modality-specific traces
