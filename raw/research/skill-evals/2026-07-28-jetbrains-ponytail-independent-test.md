# Ponytail Skill for Claude Code: Does It Really Cut Agent Code by 54%?

> Source: https://blog.jetbrains.com/ai/2026/07/ponytail-skill-claude-tested/
> Collected: 2026-10-31
> Published: 2026-07-28
> Author: Denis Shiryaev / JetBrains AI Blog
> Type: practitioner

## Excerpts

> We ran 80 paired tasks to test the ponytail skill for Claude Code. Advertised: −54% code, -22% tokens, -20% cost, -27% time. Measured: −15% code, −10.3% cost and -11% time.

> Real savings, although roughly a quarter to a half of what is advertised, it is the first tool in this series with a statistically solid cost-saving signal. We found no quality difference, though ~80 pairs can only rule out large ones. The catch: the code cut only shows up where there was room to over-build.

> Every with-ponytail trial is audited afterwards to confirm the ruleset actually reached the model; every baseline trial is audited to confirm it did not. That check is the direct descendant of the contamination bug ponytail found in its own benchmark, and it came back clean: 100% of treatment trials, 0% of baselines.

> Across all ten sessions it self-activated zero times. Not rarely. Never. [...] Copy the SKILL.md into a skills folder and you will very likely measure nothing.

> First, their −54% is a mean across twelve hand-picked feature tickets; ours is a median across 80 tasks nobody chose for this purpose. Means and medians on skewed data are different animals

> we chose these thresholds after seeing the data, and grouping by the baseline's own output can stretch a gradient like this on its own.

> Nine tasks scored slightly worse, six slightly better, 65 identical — statistically indistinguishable. That is a null result, not a clean bill of health: this run was never powered to prove equivalence

> Finding 6 — small samples lied to us, in both directions [...] Our ten-task smoke run said ponytail cut code by 3% and made things 9.6% more expensive, with mean task scores collapsing from 0.51 to 0.31. Had we published that, we would have written a very different and completely wrong article.

> Never trust k=1. Escalation ladder: a free transcript audit, then a 10-task smoke, then the same 10 at k=3, then the full 80.

> Paired analysis only. Per-task comparison between arms; any task that errored in either arm is dropped from both. Sign test for quality, per-task medians plus Wilcoxon for everything else, because one long-context session can bill 25× normal and wreck a mean.

> Endpoints fixed before the paid runs: reward, code written, output tokens, fresh input tokens, cost, turns, wall-clock. Total tokens was added afterwards, once we checked which metric ponytail's own benchmarks/agentic/run.py actually advertises.

> proving quality is genuinely unchanged would take a non-inferiority design with a pre-declared margin, and — for a 5-point shift in pass rate at 80% power around this benchmark's ~40% baseline — on the order of several hundred paired tasks per arm rather than 80.

> Adoption instrumented. Every trial audited for whether the ruleset reached the model — 100% in the treatment arm, 0% in the baseline — so "ponytail saved nothing" can never be confused with "ponytail never ran."

## Collector's note

Independent paired A/B (Harbor harness, claude-sonnet-5, SkillsBench 80 tasks, 251 billed trials) of ponytail v4.8.4 with its ruleset injected; quality from task verifiers, stats via sign test / Wilcoxon on per-task medians. Key findings: effect about a quarter to a half of advertised, concentrated where over-build room exists; plain SKILL.md never self-activated; a 10-task smoke gave the opposite conclusion. For cardigan: pre-register endpoints, audit that the skill actually loaded (and did not leak into baseline), use paired per-task tests, report medians, and treat "no quality difference" at n≈12 tasks × 3 runs as unable to rule out moderate harm.
