# AI Evals: Everything You Need to Know

> Source: https://hamel.dev/blog/posts/evals-faq/
> Collected: 2026-10-31
> Published: 2026-09-18
> Author: Hamel Husain, Shreya Shankar
> Type: practitioner

## Excerpts

> This document curates the most common questions Shreya and I received while teaching 5,000+ engineers and PMs AI Evals. Warning: These are sharp opinions about what works in most cases. They are not universal truths. Use your judgment.

> Binary evaluations force clearer thinking and more consistent labeling. Likert scales introduce significant challenges: the difference between adjacent points (like 3 vs 4) is subjective and inconsistent across annotators, detecting statistical differences requires larger sample sizes, and annotators often default to middle values to avoid making hard decisions.

> For tracking gradual improvements, consider measuring specific sub-components with their own binary checks rather than using a scale. For example, instead of rating factual accuracy 1-5, you could track "4 out of 5 expected facts included" as separate binary checks. This preserves the ability to measure progress while maintaining clear, objective criteria.

> I discourage complicated weighted scores for the same reason I discourage Likert scales for LLM judges. If your dashboard reports a composite score that jumps from 3.2 to 3.7 week over week, it's easy to feel good about the increase without knowing what improved for users.

> Many teams discover their LLM doesn't meet preferences they never actually specified - like wanting short responses, specific formatting, or step-by-step reasoning. Fix these obvious gaps first before building complex evaluation infrastructure.

> Simple assertions and reference-based checks (comparing against known correct answers) are cheap to build and maintain. LLM-as-Judge evaluators require 100+ labeled examples, ongoing weekly maintenance, and coordination between developers, PMs, and domain experts.

> True positive rate (TPR), also called recall, measures how many actual failures the evaluator catches. [...] True negative rate (TNR) measures how many good outputs the evaluator correctly passes.

> How to trust an LLM judge: validate against human labels, separate training, development, and test examples, and measure TPR and TNR.

> Generic evaluation metrics are everywhere. Eval libraries contain scores like helpfulness, coherence, quality, etc. promising easy evaluation. These metrics measure abstract qualities that may not matter for your use case. Good scores on them don't mean your system works.

> Generic metrics like similarity or verbosity won't catch this.

## Collector's note

Long FAQ distilled from teaching evals to 5,000+ practitioners; opinionated, not empirical. Most relevant: replace Likert ratings with per-fact binary checks ("4 out of 5 expected facts included"), avoid composite weighted scores, validate any LLM judge against human labels with TPR/TNR, and note that "wanting short responses" is often a one-line prompt fix. For cardigan this directly supports a key-fact checklist per task for information retention, and a "be brief" one-liner control arm.
