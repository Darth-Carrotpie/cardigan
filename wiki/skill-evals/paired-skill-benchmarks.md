# Paired skill benchmarks

> Sources: Denis Shiryaev / JetBrains AI blog, 2026-07-06; Dietrich Gebert (ponytail repo, agentic benchmark), 2026-10-07; Julius Brussee (caveman SKILL.md, README, HONEST-NUMBERS), 2026-10-31; Anthropic (Claude Platform docs, Skill authoring best practices), undated; Anthropic (statistical approach to model evals), 2024-11-19; ColinEberhardt (ponytail issue #126), 2026-06-16; Denis Shiryaev / JetBrains AI blog (ponytail test), 2026-07-28; Anthropic (skill-creator SKILL.md and agents), undated
> Raw: [Does Speaking to Agents Like Cavemen Really Save 65% of Tokens? We Test](../../raw/research/agent-skills/2026-07-06-jetbrains-caveman-paired-ab-test.md); [Agentic benchmark: Ponytail 5 vs Ponytail vs no skill](../../raw/research/agent-skills/2026-10-07-ponytail-agentic-benchmark-method.md); [Caveman: SKILL.md, README, Honest Numbers](../../raw/research/agent-skills/2026-10-31-caveman-terse-output-skill.md); [Skill authoring best practices](../../raw/research/agent-skills/anthropic-skill-authoring-best-practices.md); [A statistical approach to model evaluations](../../raw/research/skill-evals/2024-11-19-anthropic-statistical-approach-to-model-evals.md); [Benchmark issues - baseline scores are ~7 times better (ponytail issue #126)](../../raw/research/skill-evals/2026-06-16-ponytail-issue-126-baseline-critique.md); [Ponytail Skill for Claude Code: Does It Really Cut Agent Code by 54%?](../../raw/research/skill-evals/2026-07-28-jetbrains-ponytail-independent-test.md); [skill-creator: SKILL.md, grader, comparator, analyzer](../../raw/research/skill-evals/anthropic-skill-creator-eval-benchmark-method.md)
> Updated: 2026-11-02

## Overview

To tell whether an agent skill changes anything, run the same tasks with and without it, paired task by task, and test the per-task differences. JetBrains' independent test of the Caveman skill (practitioner) is a worked example: an external task suite with auto-graders, a forced-activation arm to get a ceiling, several runs, and a sign test. Its main lesson is that small runs mislead; JetBrains' later test of ponytail (practitioner) repeats it and adds an escalation ladder, fixed endpoints and an audit that the skill actually reached the model. Ponytail's own benchmark (repo; the author testing his skill) adds a third arm, the previous version, plus strict isolation and per-task ratio statistics. Caveman's own "Honest Numbers" page adds the most important control: a plain "Answer concisely." arm. Anthropic's skill-authoring guide (official-docs) asks for the same starting point, a measured no-skill baseline, but ships no runner.

## Design

The setup pairs every task: "Same tasks, same model, same settings, same budget per arm; excluded tasks excluded from both arms." Arm A is "no-skill: stock Claude Code"; Arm B is the skill installed plus one line forcing activation. The harness provides "Docker-sandboxed trials, task-level verifiers, paired runs", and each task "is auto-graded by its own tests on a 0-1 scale".

Forced activation answers a narrower question than normal use. Because the skill normally waits for the user's trigger phrase, forcing it makes "every number below is the skill's best case". This separates *does the skill work when on* from *does it turn on*.

## Three arms and isolation

Ponytail's benchmark runs "Ponytail 5, Ponytail (v4.13.0) and the same agent without any skill, measured in one run so that time of day and model drift hit all three the same way." The arms "alternate task by task", with "5 per task and arm, 585 sessions." Every rule change before release also "had to beat the current version in a paired run, one change at a time."

Isolation is explicit. The skill is loaded with `--plugin-dir`, "the same way a user gets it. The no-skill arm loads nothing." The author "checked the session transcript of a finished cell to prove what was injected." Each session "runs in a fresh temp folder outside any git repo", with CLAUDE.md loading and auto memory switched off and only the plugin under test. The shell is off ("Bash is disabled for every arm"), so the benchmark "measures what the agent writes, not what it can debug."

The task mix spans fixed and open scope: "12 feature tickets in a real FastAPI + React repo", 18 surgical tasks with hidden checks, and "6 "build me a small app" requests and 3 "show me an example" requests, where the agent picks the scope."

## The concise control

A no-skill baseline flatters any brevity skill. Caveman's README measured four arms on ten questions (6,983 output tokens with no instruction, 4,334 with "Answer concisely.", 4,119 with `/caveman`) and concluded that "be concise" is the real baseline: "new models already know it." Against that control the default level saved 3% at the median. Ponytail's first benchmark hit the same issue: in issue #126 a one-line system prompt cut the bare baseline from 108 to 16 lines against ponytail's 8.25 (see [Baseline and task design](baseline-design.md#a-trivial-control-arm)). Its HONEST-NUMBERS page also states a publishing rule: "Publish a reduction only with committed raw pairs and separate quality review."

What gets counted matters as much. Output tokens are not cost: an outside run on the same page found "Billed output −44.1%. Total cost +0.06%.", because "an agent run's bill is mostly input and cache re-reads, which an output-style rule cannot touch." The skill's own text is an input cost too ("The rules cost about 1,160 tokens of input").

## The JetBrains ponytail protocol

JetBrains' second independent test, of ponytail (practitioner; 80 paired tasks), states its protocol as rules:

- **Escalate before paying.** "Never trust k=1. Escalation ladder: a free transcript audit, then a 10-task smoke, then the same 10 at k=3, then the full 80."
- **Pair, and drop failures from both arms.** "Per-task comparison between arms; any task that errored in either arm is dropped from both."
- **Robust tests.** "Sign test for quality, per-task medians plus Wilcoxon for everything else, because one long-context session can bill 25× normal and wreck a mean."
- **Fix endpoints first.** "Endpoints fixed before the paid runs: reward, code written, output tokens, fresh input tokens, cost, turns, wall-clock." One metric was added later, and the post says so: "Total tokens was added afterwards".
- **Audit adoption.** "Every with-ponytail trial is audited afterwards to confirm the ruleset actually reached the model; every baseline trial is audited to confirm it did not." The result was "100% of treatment trials, 0% of baselines", so that "ponytail saved nothing" can never be confused with "ponytail never ran."

The activation gap was total for the plain skill file: "Across all ten sessions it self-activated zero times. Not rarely. Never. [...] Copy the SKILL.md into a skills folder and you will very likely measure nothing."

Results are in [Ponytail](../agent-skills/ponytail.md#independent-test): "Advertised: −54% code, -22% tokens, -20% cost, -27% time. Measured: −15% code, −10.3% cost and -11% time."

## Baseline first (official guidance)

Anthropic's authoring guide makes the baseline step mandatory: "Create evaluations BEFORE writing extensive documentation.", "Build three scenarios that test these gaps.", "Measure Claude's performance without the Skill." Its minimum ("At least three evaluations created", "Tested with Haiku, Sonnet, and Opus") is far below the benchmarks above, and "There is not currently a built-in way to run these evaluations." See [Skill authoring guidance](../agent-skills/skill-authoring-guidance.md#evaluations-first).

> **Status: Disputed**
> The authoring guide makes evaluations the first step for every skill ("Create evaluations BEFORE writing extensive documentation."). Anthropic's skill-creator is softer for skills like cardigan: "Skills with subjective outputs (writing style, art) often don't need them", and "Subjective skills (writing style, design quality) are better evaluated qualitatively — don't force assertions onto things that need human judgment." It still recommends test cases for "objectively verifiable outputs" and leaves the choice to the user.

## Anthropic's skill-creator workflow

Anthropic's skill-creator skill (official-docs; a published skill that builds and tests other skills) turns the paired design into a routine. Arms run together: "For each test case, spawn two subagents in the same turn — one with the skill, one without." It insists: "don't spawn the with-skill runs first and then come back for baselines later." The baseline depends on the job: for a new skill, "no skill at all"; for an improvement, "the old version", snapshotted before editing.

Assertions are scripted where possible ("write and run a script rather than eyeballing it"), and the run produces "pass_rate, time, and tokens for each configuration, with mean ± stddev and the delta." An analyst pass then looks for "assertions that always pass regardless of skill (non-discriminating), high-variance evals (possibly flaky), and time/token tradeoffs", sorting each assertion by whether it always passes in both arms, always fails in both, passes only with the skill, fails only with the skill, or is "highly variable". For "is the new version actually better?" there is a blind comparator: "give two outputs to an independent agent without telling it which is which, and let it judge quality. Then analyze why the winner won."

It is candid about who runs the eval. When the skill's author also runs it, the process "is less rigorous than independent subagents (you wrote the skill and you're also running it, so you have full context), but it's a useful sanity check — and the human review step compensates."

## Statistics and noise

Both studies compare per task, not per arm. Ponytail: "For each task I take the median of the 5 runs, divide arm by baseline, and report the geometric mean of those ratios over the tasks, with a 95% bootstrap interval. "Better on X of Y tasks" is a sign test over the tasks." JetBrains compares quality with a sign test on per-task outcomes ("Sign test over the 18 non-ties: p = 0.82"). Two noise traps showed up:

- **Small runs.** "The eye-catching -29.5% from the first small run did not replicate"; the authors' rule: "Never trust a k=1 eval."
- **Small runs again.** In the ponytail test, "Our ten-task smoke run said ponytail cut code by 3% and made things 9.6% more expensive, with mean task scores collapsing from 0.51 to 0.31. Had we published that, we would have written a very different and completely wrong article."
- **Single outliers in totals.** Arm totals showed the skill arm more expensive, but "The entire inversion came from a single trial"; per-task comparisons were not fooled.

The general case for per-task pairing comes from Anthropic's statistics post (study): a paired-differences test removes "the variance in question difficulty", and repeat runs should be averaged per question before computing error, because clustered standard errors "can be over three times as large as naive standard errors." See [Eval statistics](eval-statistics.md).

## For cardigan

Interpretation, not source claims:

- cardigan's eval needs a paired design over a fixed office-task set (emails, meeting requests, status asks), several runs per task, and per-task comparisons rather than arm totals. A first small run is a smoke test, not a result.
- Follow the escalation ladder (transcript audit, small smoke, smoke at three runs, full set) and fix the endpoints before the scored runs; audit every trial to prove cardigan loaded in its arm and not in the others.
- Include a "be concise" control arm (for office tasks, something like "keep it short"), so cardigan's effect is measured beyond what one sentence of instruction already buys.
- Report total cost and reader-side outcomes, not only output tokens; cardigan's own prompt length is part of the bill.
- Drop or rewrite any assertion that passes in every arm; it measures nothing about cardigan. Watch for assertions that pass only without cardigan: those are where it hurts.
- Use three arms where possible (no skill, current cardigan, candidate change); isolate each session from user memory and project instructions, and check the transcript to prove what was loaded.
- Separate the trigger question (does cardigan apply on office tasks?) from the effect question (when it applies, is the output smaller and still complete?).

## See Also

- [Terse-output skills](../agent-skills/terse-output-skills.md)
- [Ponytail](../agent-skills/ponytail.md)
- [Guard metrics](guard-metrics.md)
- [Eval statistics](eval-statistics.md)
- [Baseline and task design](baseline-design.md)
- [Skill authoring guidance](../agent-skills/skill-authoring-guidance.md)
