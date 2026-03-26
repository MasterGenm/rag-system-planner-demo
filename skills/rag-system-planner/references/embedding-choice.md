# Embedding Choice

Choose embeddings based on data modality, language coverage, latency budget, and operating constraints.

## Decision Rules

### Start Simple

Default to a strong general-purpose text embedding model unless one of these forces a different choice:

- Multilingual retrieval
- Domain-specific vocabulary
- Multimodal retrieval
- Strict local-only deployment
- Extremely high throughput requirements

### Hosted Vs Local

Use hosted embeddings when:

- Fast setup matters
- Managed operations are preferred
- Network access is acceptable
- Model iteration speed matters more than strict cost control

Use local embeddings when:

- Data cannot leave the environment
- Cost predictability matters at scale
- Offline or edge operation is required
- You already operate GPU inference locally

## By Use Case

### General Text RAG

Prefer strong text embeddings with:

- Good semantic search quality
- Stable sentence or passage retrieval
- Reasonable context length handling

### Multilingual RAG

Prefer models with explicit multilingual support. Do not assume an English-first model will perform well on mixed-language corpora.

### Domain-Specific RAG

If the corpus is legal, biomedical, financial, or code-heavy, test whether a domain-tuned embedding model improves retrieval enough to justify the extra complexity.

### Multimodal RAG

If retrieval must bridge text and images, use modality-aware embeddings or parallel pipelines instead of forcing everything into a text-only representation.

## Tradeoffs

- Better retrieval quality often increases latency or cost.
- Larger embedding dimensions increase storage and search cost.
- Changing embeddings usually requires full or partial re-indexing.
- Cross-lingual and multimodal support adds evaluation burden.

## Recommendation Pattern

When recommending embeddings, state:

1. Why the modality and language profile matter
2. Whether hosted or local is the better fit
3. Whether to start general-purpose or domain-specific
4. What evaluation must confirm the choice
