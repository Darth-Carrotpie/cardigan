# A statistical approach to model evaluations

> Source: https://www.anthropic.com/research/statistical-approach-to-model-evals
> Collected: 2026-10-31
> Published: 2024-11-19
> Author: Anthropic (companion post to Evan Miller, "Adding Error Bars to Evals", arXiv:2411.00640)
> Type: study

## Excerpts

> A 95% confidence interval can be calculated from the SEM by adding and subtracting 1.96 × SEM from the mean score.

> When the inclusion of questions is non-independent, we recommend clustering standard errors on the unit of randomization (for example, passage of text), and we provide applicable formulas in our paper.

> In practice, we have found that clustered standard errors on popular evals can be over three times as large as naive standard errors. Ignoring question clustering may lead researchers to inadvertently detect a difference in model capabilities when in fact none exists.

> If an eval uses chain-of-thought reasoning, we recommend resampling answers from the same model several times, and using the question-level averages as the question scores fed into the Central Limit Theorem. We note that the Inspect framework correctly computes standard errors in this way via its epochs parameter.

> However, a two-sample test ignores the hidden structure inside eval data. Since the question list is shared across models, conducting a paired-differences test lets us eliminate the variance in question difficulty and focus on the variance in responses.

> In practice, we find the correlation of question scores on popular evals between frontier models to be substantial—between 0.3 and 0.7 on a scale of −1 to +1. [...] Paired-difference analysis thus represents a "free" variance reduction technique that is very well suited for AI model evals.

> If an eval doesn't have very many questions, confidence intervals associated with any statistical tests will tend to be wide. This means that models will need to have a large underlying difference in capabilities in order to register a statistically significant result—and that small differences will likely go undetected.

> Researchers might use the power formula to conclude that an eval with a limited number of available questions is not worth running on a particular pair of models.

## Collector's note

Five reporting recommendations: SEM-based CIs, clustered standard errors, resampling to reduce within-question variance, paired differences, and power analysis. For cardigan's ~12 tasks × 3 runs: the 3 runs per task are a cluster (average them to a per-task score, don't treat 36 outputs as independent), compare arms with paired per-task differences, and expect only large effects to be detectable — report CIs rather than a bare "X% shorter".
