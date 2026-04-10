# Negation And Absence

## Symptom

The system struggles with questions about what is not allowed, not present, or safely excluded.

## Likely Causes

- retrieval favors explicit mentions of risky or present items
- prompts are weak at proving absence
- evaluation rarely includes negation-sensitive cases

## Investigation Order

1. define the full candidate set relevant to the question
2. inspect whether the system can separate excluded items from allowed items
3. check whether the answer is inferring safety without a real exclusion logic
4. treat absence-sensitive tasks as hard cases, not ordinary semantic retrieval

## Common False Diagnoses

- treating absence as ordinary recall
- assuming more similar documents can prove a negative claim

## Related Pages

- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)
- [Implicit Hallucination](implicit-hallucination.md)

## Source Trail

- fareedkhan 14-rag-failures taxonomy
