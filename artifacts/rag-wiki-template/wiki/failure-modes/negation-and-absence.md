# Negation And Absence

## Symptom

系统在处理“不允许什么”“不存在什么”或“可以安全排除什么”这类问题时表现很差。

## Likely Causes

- retrieval 更偏爱那些显式提到“存在项”或“风险项”的文本
- prompts 不擅长证明 absence
- evaluation 很少包含 negation-sensitive cases

## Investigation Order

1. 定义与问题相关的完整 candidate set
2. 检查系统是否能把 excluded items 和 allowed items 区分开
3. 检查答案是否在没有真实 exclusion logic 的前提下擅自推断“安全”
4. 把这类 absence-sensitive 任务当成 hard cases，而不是普通 semantic retrieval

## Common False Diagnoses

- 把 absence 问题误当成普通 recall
- 误以为更多相似文档就能证明一个 negative claim

## Related Pages

- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Implicit Hallucination](implicit-hallucination.md)

## Source Trail

- fareedkhan `14-rag-failures` taxonomy
