# Intake Checklist

当需求不完整时，使用这份 checklist。只问那些会改变架构决策的字段。

## Greenfield Intake

### Product Goal

- 系统需要回答或产出什么？
- 用户是谁？
- 这是简单问答、多轮对话，还是 agent-assisted work？

### Data

- 涉及哪些数据类型：text、PDF、web pages、images、audio、tables，还是混合？
- 当前有多少文档或记录？
- corpus 多久变化一次？
- metadata filters 是否重要？

### Constraints

- 最重要的是什么：recall、precision、latency、cost，还是 traceability？
- 部署约束是什么：local、cloud、CPU、GPU，还是 compliance boundaries？
- 是否有必须复用的现有技术栈？

### Output Expectations

- 是否要求 citations？
- 是否要求 tool use？
- human review 是否在环？
- 是否要求上线前先做 offline evaluation？

## Diagnosis Intake

- 当前可见的 symptom 是什么？
- 什么时候开始的？
- 问题属于 retrieval quality、answer quality、latency、stability，还是 observability？
- 现在已经用了什么 stack？
- 现有证据有哪些：logs、traces、labeled examples、dashboards、evaluation runs？
- 已经尝试过什么？

## Minimal Assumption Rules

如果用户无法把所有问题都答清，就带着显式 assumptions 往下走。

好的 assumptions：

- “假设 corpus 规模中等，且每天更新。”
- “假设 citation quality 比极限 latency 更重要。”
- “假设基于 Python 的 orchestration 可以接受。”

坏的 assumptions：

- “假设用户想要 agents。”
- “假设最复杂的架构就是合适的。”

## Required Vs Optional

### Usually Required

- Task type：greenfield 还是 diagnosis
- Data type
- Approximate scale
- Primary optimization target

### Usually Optional

- Exact model name
- Exact cloud vendor
- Exact benchmark target

如果某个字段是 optional，就不要为了等它而停住进度。
