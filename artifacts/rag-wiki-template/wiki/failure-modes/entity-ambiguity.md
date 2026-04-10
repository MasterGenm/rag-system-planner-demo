# Entity Ambiguity

## Symptom

The system retrieves evidence for the wrong entity because names overlap across domains, products, people, or concepts.

## Likely Causes

- metadata lacks entity type or disambiguating context
- retrieval relies too heavily on raw lexical overlap
- the query omits intent or entity type

## Investigation Order

1. inspect whether the candidate set mixes multiple entities with the same surface name
2. check whether metadata carries entity type, domain, or namespace
3. test whether query rewriting or entity normalization improves disambiguation
4. then decide whether a stronger ontology or graph layer is needed

## Common False Diagnoses

- blaming embeddings globally when the real issue is missing entity resolution
- assuming hallucination when the model is faithfully using the wrong entity evidence

## Related Pages

- [Synonymy And Jargon Gap](synonymy-and-jargon-gap.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- fareedkhan 14-rag-failures taxonomy
