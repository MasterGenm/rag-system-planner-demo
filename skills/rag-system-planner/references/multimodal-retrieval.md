# Multimodal Retrieval

当 corpus 中包含 scans、screenshots、diagrams、tables，或其他无法安全压缩成纯文本检索的证据时，使用这份文件。

## Decide Whether Multimodal Retrieval Is Really Needed

在以下情况下，text-only retrieval 仍然可能够用：

- OCR 质量高
- 重要证据大多仍是 prose
- page-level citations 已足够
- 图片更多是装饰性的，而不是语义必需的

当出现以下情况时，应该规划明确的 multimodal retrieval：

- diagrams 或 screenshots 本身就包含答案
- 用户需要 image-aware citations
- OCR 会丢掉关键布局或标签
- tables、charts 或 visual states 承载关键意义

## Evidence Units

保持可检索单元显式分离：

- text chunks
- OCR blocks
- image 或 region assets
- 当表格结构本身重要时，再加入 table extracts

如果它们服务不同的 retrieval paths，就不要把它们模糊地混进一个无差别存储层。

## Metadata Requirements

保留足够的 metadata，才能让答案保持 grounded：

- document id
- page number
- section id
- asset id 或 region id
- modality
- 如果适用，保留 OCR confidence
- 如果可用，保留 caption 或邻近文本锚点

## Retrieval Patterns

优先使用与任务匹配的最轻模式：

1. 带 OCR 支持的 text-first baseline
2. 按 query type 做 routed retrieval
3. 并行的 text 和 image retrieval，再做 merged ranking

只有当视觉证据在测量上真的重要时，才超出 text-first。

## Routing Guidance

以下情况下使用 modality-aware routing：

- 问题明确提到 diagram、screenshot、UI state、label 或 visual layout
- 支持工作流依赖 image-specific troubleshooting
- 扫描页面 OCR 很弱，需要 image context

保持 routing 可解释。用户或工程师应能说清系统为什么搜 text、images，或同时搜两者。

## Fallback Behavior

为弱视觉证据场景做好设计：

- 当 images 价值低时，fallback 到 text evidence
- 当 OCR confidence 很低，且没有 grounded image path 时，选择 abstain
- 暴露 low-confidence evidence，而不是伪装成确定结论

## Evaluation Changes

按模态拆分 evaluation：

- text-only questions
- image-dependent questions
- scan-heavy questions
- mixed text-image questions

检查：

- 各模态的 retrieval hit rate
- 按 page 或 asset 统计的 citation correctness
- 弱 OCR 条件下的 groundedness
- 当 routing 走错分支时的 failure rate

## Observability Signals

至少 trace：

- 选择了哪条 modality path
- retrieved asset ids 和 chunk ids
- OCR confidence
- 各分支的 retrieval scores
- merged ranking decisions
- 最终 citation anchors

## Recommendation Pattern

明确说明：

1. 为什么 multimodal retrieval 值得或不值得做
2. 可上线的最小 baseline 是什么
3. routing strategy 是什么
4. fallback behavior 是什么
5. 哪些额外复杂度被有意延后
