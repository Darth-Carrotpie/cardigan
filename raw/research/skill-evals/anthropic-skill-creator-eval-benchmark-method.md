# skill-creator (SKILL.md, agents/grader.md, agents/comparator.md, agents/analyzer.md)

> Source: https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md (also https://github.com/anthropics/skills/blob/main/skills/skill-creator/agents/grader.md, https://github.com/anthropics/skills/blob/main/skills/skill-creator/agents/comparator.md and https://github.com/anthropics/skills/blob/main/skills/skill-creator/agents/analyzer.md; read from the locally installed plugin copy, anthropic-plugin-directory/skill-creator a7ba5b93db0c, whose wording matches the public files)
> Collected: 2026-10-31
> Published: Unknown
> Author: Anthropic, Apache License 2.0
> Type: official-docs

## Excerpts

From https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md:

> Should we set up test cases to verify the skill works? Skills with objectively verifiable outputs (file transforms, data extraction, code generation, fixed workflow steps) benefit from test cases. Skills with subjective outputs (writing style, art) often don't need them. Suggest the appropriate default based on the skill type, but let the user decide.

> For each test case, spawn two subagents in the same turn — one with the skill, one without. This is important: don't spawn the with-skill runs first and then come back for baselines later. Launch everything at once so it all finishes around the same time.

> - **Creating a new skill**: no skill at all. Same prompt, no skill path, save to `without_skill/outputs/`.
> - **Improving an existing skill**: the old version. Before editing, snapshot the skill (`cp -r <skill-path> <workspace>/skill-snapshot/`), then point the baseline subagent at the snapshot. Save to `old_skill/outputs/`.

> Good assertions are objectively verifiable and have descriptive names — they should read clearly in the benchmark viewer so someone glancing at the results immediately understands what each one checks. Subjective skills (writing style, design quality) are better evaluated qualitatively — don't force assertions onto things that need human judgment.

> For assertions that can be checked programmatically, write and run a script rather than eyeballing it — scripts are faster, more reliable, and can be reused across iterations.

> This produces `benchmark.json` and `benchmark.md` with pass_rate, time, and tokens for each configuration, with mean ± stddev and the delta.

> things like assertions that always pass regardless of skill (non-discriminating), high-variance evals (possibly flaky), and time/token tradeoffs.

> For situations where you want a more rigorous comparison between two versions of a skill (e.g., the user asks "is the new version actually better?"), there's a blind comparison system. [...] The basic idea is: give two outputs to an independent agent without telling it which is which, and let it judge quality. Then analyze why the winner won.

> This is less rigorous than independent subagents (you wrote the skill and you're also running it, so you have full context), but it's a useful sanity check — and the human review step compensates.

From https://github.com/anthropics/skills/blob/main/skills/skill-creator/agents/grader.md:

> You have two jobs: grade the outputs, and critique the evals themselves. A passing grade on a weak assertion is worse than useless — it creates false confidence. When you notice an assertion that's trivially satisfied, or an important outcome that no assertion checks, say so.

> - **PASS**: Clear evidence the expectation is true AND the evidence reflects genuine task completion, not just surface-level compliance
> - **FAIL**: No evidence, or evidence contradicts the expectation, or the evidence is superficial (e.g., correct filename but empty/wrong content)

> Think about what makes an assertion *discriminating*: it passes when the skill genuinely succeeds and fails when it doesn't.

From https://github.com/anthropics/skills/blob/main/skills/skill-creator/agents/comparator.md:

> You receive two outputs labeled A and B, but you do NOT know which skill produced which. This prevents bias toward a particular skill or approach.

> - **Stay blind**: DO NOT try to infer which skill produced which output. Judge purely on output quality.

From https://github.com/anthropics/skills/blob/main/skills/skill-creator/agents/analyzer.md:

> - Does it **always pass** in both configurations? (may not differentiate skill value)
> - Does it **always fail** in both configurations? (may be broken or beyond capability)
> - Does it **always pass with skill but fail without**? (skill clearly adds value here)
> - Does it **always fail with skill but pass without**? (skill may be hurting)
> - Is it **highly variable**? (flaky expectation or non-deterministic behavior)

## Collector's note

Anthropic's own skill-eval workflow: with-skill and baseline runs launched simultaneously per test case, assertions (scripted where possible) graded with text/passed/evidence, aggregated as pass rate, time and tokens with mean ± stddev and delta, then an analyst pass for non-discriminating or flaky assertions, plus an optional blind A/B comparator. It openly flags that self-run evals by the skill's author are less rigorous. For cardigan this is the natural harness shape: per-task assertions for never-cut items and the real ask, a discrimination check that drops assertions passing in both arms, and blind A/B for the subjective "is this better" question.
