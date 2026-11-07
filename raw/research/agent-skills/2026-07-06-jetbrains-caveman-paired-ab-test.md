# Does Speaking to Agents Like Cavemen Really Save 65% of Tokens? We Test

> Source: https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/
> Collected: 2026-10-31
> Published: 2026-07-06
> Author: Denis Shiryaev (JetBrains AI blog)
> Type: practitioner

## Excerpts

> A paired A/B benchmark of the token-compression skill Caveman on Claude Code, run on SkillsBench: does it actually save tokens, and does it degrade AI agent output quality?
>
> Advertised saving: 65%. Measured saving: 8.5%.

> | Setup | |
> |---|---|
> | Harness | Harbor 0.17: Docker-sandboxed trials, task-level verifiers, paired runs. |
> | Agent | Claude Code 2.1.200, headless, bypassPermissions. |
> | Model | claude-sonnet-5, reasoning effort low (--effort low). |
> | Benchmark | SkillsBench (benchflow/skillsbench): 86 of 87 tasks. Each task is auto-graded by its own tests on a 0-1 scale, where 1 means solved and partial credit is possible. |
> | Arm A | no-skill: stock Claude Code. |
> | Arm B | with-skill-forced: Caveman installed via Harbor --skill plus one instruction line forcing activation: "Use caveman mode…" |
> | Pairing | Same tasks, same model, same settings, same budget per arm; excluded tasks excluded from both arms. |
> | Volume | 3 runs, about 240 billed trials, about USD 106 total. |

(Table layout reconstructed by collector from the page's two-column setup table; cell text verbatim.)

> Why "forced" matters: Caveman is user-activated. It triggers on phrases like "caveman mode" or "be brief". We forced it on in every reply, which means every number below is the skill's best case. In normal use, where the agent must decide to activate it on its own, the realized saving can only be equal or lower than the roughly 10% ceiling measured here.

> Advertised savings come from chat-style prose answers. Agentic output is different: code, diffs, tool invocations, and exact error strings dominate the token stream, and Caveman correctly leaves all of it verbatim. Only the narration between tool calls gets compressed, and there is not much of it.

> The eye-catching -29.5% from the first small run did not replicate; at scale the saving converges to -8.5% (592k to 542k output tokens over 82 paired tasks). The advertised -65% is off-chart.

> Per-task paired outcomes, full run. Sign test over the 18 non-ties: p = 0.82, far from any significant difference. Average task score was 0.326 for baseline vs. 0.311 for the skill arm, a -0.015 gap on a 0-1 scale.

> Cost tracks the roughly 8.5% token saving, so the skill arm should come out roughly 10% cheaper, and per task, it does. But the raw arm totals in our full run showed the skill arm 11.6% more expensive: USD 40.60 vs. USD 36.39. The entire inversion came from a single trial [...]

> Recommendation: use it if you like it. It is fun, and it costs you nothing measurable in quality. Just do not expect huge savings on daily agentic tasks: a high-single-digit percentage is the realistic ceiling.

> Methodology bonus: our first 10-task run "showed" a -30% token saving. It dissolved as sample size grew. Never trust a k=1 eval.

## Collector's note

Independent paired A/B of a popular brevity skill by a tooling vendor, using an external task suite with auto-graders, a forced-activation arm (to get a ceiling), and a sign test on per-task outcomes. Headline: -8.5% output tokens, no detectable quality change (8 better / 10 worse / 64 tied, p = 0.82), and cost savings erased by single-trial variance. Lessons for cardigan's own evaluation: separate "skill triggered" from "skill effective", report small-sample results as noise until they replicate, and expect that a style rule only moves the part of output that is prose. This is a coding benchmark; no office-task equivalent was found.
