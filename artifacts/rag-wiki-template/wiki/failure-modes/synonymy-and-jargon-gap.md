# Synonymy And Jargon Gap

## Symptom

The query and the source material refer to the same thing using different names, acronyms, aliases, or business and technical terms, so retrieval and answer assembly fail to connect them.

## Likely Causes

- alias mapping or ontology support is missing
- metadata does not normalize terminology
- query rewriting preserves wording but not concept equivalence

## Investigation Order

1. inspect whether the user wording and source wording point to the same underlying entity
2. check whether aliases exist in the corpus but were never normalized
3. add terminology normalization before changing the whole architecture

## Common False Diagnoses

- assuming embeddings alone should always bridge terminology gaps
- blaming chunking when the failure is vocabulary alignment

## Related Pages

- [Entity Ambiguity](entity-ambiguity.md)
- [Hard-Case And Trace Review](../evaluations/hard-case-trace-review.md)

## Source Trail

- `14-rag-failures` synonymy and jargon taxonomy
