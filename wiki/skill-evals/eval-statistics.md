# Eval statistics

> Sources: Anthropic (companion post to Evan Miller, "Adding Error Bars to Evals"), 2024-11-19; Anthropic Engineering ("Demystifying evals for AI agents"), 2026-01-09; Denis Shiryaev / JetBrains AI blog (ponytail test), 2026-07-28; Anthropic (Claude Platform docs, Define success criteria and build evaluations), undated
> Raw: [A statistical approach to model evaluations](../../raw/research/skill-evals/2024-11-19-anthropic-statistical-approach-to-model-evals.md); [Demystifying evals for AI agents](../../raw/research/skill-evals/2026-01-09-anthropic-demystifying-evals-for-ai-agents.md); [Ponytail Skill for Claude Code: Does It Really Cut Agent Code by 54%?](../../raw/research/skill-evals/2026-07-28-jetbrains-ponytail-independent-test.md); [Define success criteria and build evaluations](../../raw/research/skill-evals/anthropic-docs-define-success-criteria-build-evals.md)
> Updated: 2026-11-02

## Overview

An eval score is an estimate, and with a small task set its error is large. Anthropic's statistics post (study; companion to Evan Miller's paper) gives five rules: report a confidence interval, cluster standard errors when items are not independent, average repeated samples per question before computing the error, compare two models with paired per-question differences, and run a power calculation before spending on a small eval. Together they explain why a skill benchmark with a dozen tasks can only detect large effects.

## Confidence intervals

"A 95% confidence interval can be calculated from the SEM by adding and subtracting 1.96 × SEM from the mean score." A bare score without this interval says nothing about whether a difference is real.

## Clustering

Items that share a unit (questions about the same passage, say) are not independent: "When the inclusion of questions is non-independent, we recommend clustering standard errors on the unit of randomization (for example, passage of text)". The correction is large: "clustered standard errors on popular evals can be over three times as large as naive standard errors. Ignoring question clustering may lead researchers to inadvertently detect a difference in model capabilities when in fact none exists."

Repeat runs are handled the same way. For evals with chain-of-thought, "we recommend resampling answers from the same model several times, and using the question-level averages as the question scores fed into the Central Limit Theorem." Repeat runs of one task reduce noise in that task's score; they do not add independent tasks.

## Paired differences

"a two-sample test ignores the hidden structure inside eval data. Since the question list is shared across models, conducting a paired-differences test lets us eliminate the variance in question difficulty and focus on the variance in responses." The gain is real because models tend to find the same questions hard: "the correlation of question scores on popular evals between frontier models to be substantial—between 0.3 and 0.7 on a scale of −1 to +1. [...] Paired-difference analysis thus represents a "free" variance reduction technique".

## Trials and reliability

Anthropic's agent-evals guide (official-docs) calls each attempt a trial: "Because model outputs vary between runs, we run multiple trials to produce more consistent results." For behaviour that must hold every time it suggests pass^k: "pass^k measures the probability that all k trials succeed. [...] If your agent has a 75% per-trial success rate and you run 3 trials, the probability of passing all three is (0.75)³ ≈ 42%."

## Sample size and power

"If an eval doesn't have very many questions, confidence intervals associated with any statistical tests will tend to be wide. This means that models will need to have a large underlying difference in capabilities in order to register a statistically significant result—and that small differences will likely go undetected." A power calculation can show in advance "that an eval with a limited number of available questions is not worth running on a particular pair of models."

Anthropic's platform docs (official-docs) lean the same way on volume: "Prioritize volume over quality: More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals." The agent-evals guide adds the practical side: "20-50 simple tasks drawn from real failures is a great start", because early on "each change to the system often has a clear, noticeable impact, and this large effect size means small sample sizes suffice. More mature agents may need larger, more difficult evals to detect smaller effects".

## Null results, medians and equivalence

JetBrains' ponytail test (practitioner) shows how to report a null result. On quality: "Nine tasks scored slightly worse, six slightly better, 65 identical — statistically indistinguishable. That is a null result, not a clean bill of health: this run was never powered to prove equivalence". Proving no harm needs a different design: "a non-inferiority design with a pre-declared margin, and — for a 5-point shift in pass rate at 80% power around this benchmark's ~40% baseline — on the order of several hundred paired tasks per arm rather than 80." Its summary: "We found no quality difference, though ~80 pairs can only rule out large ones."

It also warns about summary statistics on skewed data. Ponytail's advertised "−54% is a mean across twelve hand-picked feature tickets; ours is a median across 80 tasks nobody chose for this purpose. Means and medians on skewed data are different animals". And about slicing after the fact: for the finding that the code cut "only shows up where there was room to over-build", the authors concede "we chose these thresholds after seeing the data, and grouping by the baseline's own output can stretch a gradient like this on its own."

## For cardigan

Interpretation, not source claims:

- With about a dozen office tasks and three runs each, the unit is the task: average the three runs into one per-task score, and never treat the 36 outputs as 36 independent observations.
- Compare cardigan with each control arm by paired per-task differences, and report an interval, not a bare "X% shorter".
- For never-cut items, use an all-runs bar (pass^3 over three runs): a fact kept in two runs out of three is a fact dropped one time in three.
- Report a finding of no detectable quality loss as a null result with its limits, never as proof that quality is unchanged; at about a dozen tasks only large harm is ruled out.
- Report medians of per-task ratios, not means, and declare any subgroup split before seeing the data.
- Decide before running what effect size the task set can detect. A small eval can show that cardigan cuts length a lot; it cannot show that quality is unchanged.

## See Also

- [Paired skill benchmarks](paired-skill-benchmarks.md)
- [Guard metrics](guard-metrics.md)
