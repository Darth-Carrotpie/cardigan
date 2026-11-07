# Using LLM-as-a-Judge For Evaluation: A Complete Guide

> Source: https://hamel.dev/blog/posts/llm-judge/
> Collected: 2026-10-31
> Published: 2024-10-29
> Author: Hamel Husain
> Type: practitioner

## Excerpts

> Arbitrary Scoring Systems: Using uncalibrated scales (like 1-5) across multiple dimensions, where the difference between scores is unclear and subjective. What makes something a 3 versus a 4? Nobody knows, and different evaluators often interpret these scales differently.

> The solution is to use a technique that I call "Critique Shadowing".

> The domain expert's job is to focus on one thing: "Did the AI achieve the desired outcome?" No complex scoring scales or multiple metrics. Just a clear pass or fail decision. In addition to the pass/fail decision, the domain expert should write a critique that explains their reasoning.

> Most importantly, the critique should be detailed enough so that you can use it in a few-shot prompt for a LLM judge. In other words, it should be detailed enough that a new employee could understand it. Being too terse is a common mistake.

> If your evaluations consist of a bunch of metrics that LLMs score on a 1-5 scale (or any other scale), you're doing it wrong.

> My heuristic is that I start with around 30 examples and keep going until I do not see any new failure modes.

> You cannot write a good judge prompt until you've seen the data.

> Raw agreement can be misleading when classes are imbalanced. Treat the human labels as ground truth and report the judge's True Positive Rate and True Negative Rate separately.

> It took us only three iterations to achieve > 90% agreement between the LLM and Phillip.

> You should calculate the error on unseen data only to make sure your aren't getting biased results.

> Test set: Keep these examples hidden until you finish revising the prompt. Freeze the prompt, run the judge on the test set once, and use the result as your final estimate of the judge's performance.

## Collector's note

Practitioner method for building an LLM judge: one principal domain expert labels outputs pass/fail with written critiques, those critiques become few-shot examples, and the judge prompt is iterated until it agrees with the expert (>90% in his example), then checked once on a held-out set. For cardigan: grade each criterion (real ask answered, never-cut items kept, lighter option taken) as binary with a critique rather than 1–5, have a human label a small calibration set first, and report judge TPR/TNR rather than raw agreement.
