# Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)

> Source: https://eugeneyan.com/writing/llm-evaluators/
> Collected: 2026-10-31
> Published: 2024-08-18
> Author: Eugene Yan
> Type: practitioner

## Excerpts

> Direct scoring evaluates a single response without needing an alternative for comparison. This makes it more versatile than pairwise comparison. Because it scores output directly, it's more suitable for objective assessments such as measuring faithfulness to a source text or detecting policy violations such as toxicity.

> Pairwise comparison chooses the better of two responses or declares a tie. It's typically used—and more reliable—for subjective evals such as persuasiveness, tone, coherence, etc. Studies show that pairwise comparisons lead to more stable results and smaller differences between LLM judgments and human annotations relative to direct scoring.

> These three approaches are not interchangeable. Some evaluation tasks, such as assessing faithfulness or instruction-following, don't fit the pairwise comparison paradigm. For example, a response is either faithful to the provided context or it is not

> I tend to be skeptical of correlation metrics. They don't account for chance agreement and thus could be overoptimistic (though Cohen's $\kappa$ is an exception). [...] Thus, where possible, I have my evaluators return binary outputs. This improves model performance while making it easier to apply classification metrics.

> The pyramid approach first extracts semantic content units (SCUs) from the reference summary. The evaluator then checks if these SCUs are present in the generated summary.

> While the LLM-evaluator identified >95% of consistent summaries (high precision for good summaries), it only identified 30 - 60% of the inconsistent summaries (low recall for defects).

> The paper also found that gpt-4 favored responses that provided more examples. Overall, this suggests that gpt-4 as an evaluator has biases such as a bias towards giving higher scores and verbosity bias.

> Then, they show that pairwise preferences of LLMs vary significantly, even with semantically equivalent instructions.

> Second, verbosity bias, where LLM-evaluators favor longer, more verbose responses, even if they're not as clear, high-quality, or accurate as shorter alternatives. To generate these verbose distractors, the authors had gpt-4 rephrase some MT-Bench answers without adding new information and concatenated them to the original answers. Both claude-v1 and gpt-3.5 preferred the longer response more than 90% of the time

> Results: Cohen's $\kappa$ between human and LLM judgments showed fair agreement of 0.3 - 0.5, while Kendall's $\tau$ and Spearman's $\rho$ was higher at 0.8 - 0.9.

## Collector's note

A literature survey (dozens of papers) by a practitioner on when to use direct scoring vs pairwise vs reference-based LLM evaluators, and how to measure evaluator quality. Key points for cardigan: use direct binary checks for objective items (never-cut facts present, ask answered) and pairwise only for subjective "which would a busy colleague prefer"; a pyramid/SCU-style check maps onto key-fact retention; and LLM judges often have low recall for defects, so a judge saying "nothing important was cut" needs human spot-checks.
