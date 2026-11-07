# FineSurE: Fine-grained Summarization Evaluation using LLMs

> Source: https://arxiv.org/abs/2407.00908 (HTML v1: https://arxiv.org/html/2407.00908v1)
> Collected: 2026-10-31
> Published: 2024-07-01
> Author: Hwanjun Song, Hang Su, Igor Shalyminov, Jason Cai, Saab Mansour (KAIST, AWS AI Labs; ACL 2024)
> Type: study

## Excerpts

> Traditional methods like ROUGE do not correlate well with human judgment, while recently proposed LLM-based metrics provide only summary-level assessment using Likert-scale scores.

> It also employs completeness and conciseness criteria, in addition to faithfulness, enabling multi-dimensional assessment.

> Figure 1: FineSurE framework: the given summary is evaluated by conducting the two tasks of fact checking and keyfact alignment. In this specific example, the faithfulness score is 33%, since only one out of the three summary sentences is factually correct; the completeness score is 75%, since three out of the four keyfacts align with the summary; and the conciseness score is 66%, since two out of the three sentences are related to the keyfacts.

> A keyfact refers to a concise sentence conveying a single key information, comprising at most 2-3 entities, also referred to as a semantic content unit Bhandari et al. (2020). The keyfact list can be generated automatically or by humans.

> We aim to evaluate summaries using this framework along three vital criteria: the faithfulness of minimizing factuality errors, the completeness of encompassing the majority of keyfacts, and the conciseness of avoiding unnecessary details.

> We leverage the outcomes from both procedures to calculate precise percentage scores, offering a more detailed assessment than Likert-scale scoring.

> Completeness: The summarizer ensures the inclusion of all keyfacts from the input text in the output summary.

> Conciseness: The summarizer refrains from incorporating information outside the keyfacts in the output, maintaining a succinct and focused summary.

## Collector's note

An LLM-based evaluator that scores summaries by aligning output sentences to a keyfact list, yielding completeness (share of keyfacts covered) and conciseness (share of sentences that carry a keyfact) as percentages rather than Likert scores. This is a ready-made template for measuring "brevity without losing content" in cardigan: write a short human-authored keyfact list per task (including the never-cut items), score completeness per output, and report conciseness alongside raw length so that shorter-but-incomplete outputs are visibly penalised.
