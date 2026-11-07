# Ponytail

> Sources: Dietrich Gebert (ponytail repo, agentic benchmark), 2026-10-07; Dietrich Gebert (ponytail AGENTS.md), 2026-10-08; Dietrich Gebert (ponytail README v5), undated; Dietrich Gebert (ponytail SKILL.md v5), undated; ColinEberhardt (ponytail issue #126), 2026-06-16; Denis Shiryaev / JetBrains AI blog (ponytail test), 2026-07-28; Dietrich Gebert (ponytail benchmarks README), undated
> Raw: [Agentic benchmark: Ponytail 5 vs Ponytail vs no skill](../../raw/research/agent-skills/2026-10-07-ponytail-agentic-benchmark-method.md); [Ponytail AGENTS.md (compact rules-file version)](../../raw/research/agent-skills/2026-10-08-ponytail-agents-md-compact-ruleset.md); [Ponytail README (v5, main)](../../raw/research/agent-skills/ponytail-readme-v5.md); [Ponytail SKILL.md (v5, main)](../../raw/research/agent-skills/ponytail-skill-md-v5.md); [Benchmark issues - baseline scores are ~7 times better (ponytail issue #126)](../../raw/research/skill-evals/2026-06-16-ponytail-issue-126-baseline-critique.md); [Ponytail Skill for Claude Code: Does It Really Cut Agent Code by 54%?](../../raw/research/skill-evals/2026-07-28-jetbrains-ponytail-independent-test.md); [Agentic benchmark: Ponytail 5 vs Ponytail vs no skill (results file)](../../raw/research/skill-evals/2026-10-07-ponytail-agentic-benchmark-results.md); [ponytail benchmarks/README.md](../../raw/research/skill-evals/ponytail-benchmarks-readme.md)
> Updated: 2026-11-02

## Overview

Ponytail is an always-on coding skill that makes an agent produce the smallest change that fully solves the task. It is cardigan's direct model. Its core is a six-rung ladder that starts with "Does it need to exist?", a scope check before cutting, a never-cut list, a fixed reply ending and three intensity levels. Its author's own benchmark (repo evidence; the author measuring his own skill) reports large cuts in code size, cost and time against no skill, with hidden correctness and security checks unchanged, and a blind reply judge that prefers version 5's replies over version 4's but not over the no-skill baseline.

## The stance

The README states the goal against a common misreading: "It is: write only what the task needs, and never cut validation, error handling, security, or accessibility. The code ends up small because it is necessary, not golfed. Lower cost and latency are a side effect." Its example: asked for a date picker, an agent without the skill writes 335 lines; ponytail notices the repo's `Input` component and that "every browser has a date picker. It puts the two together." Result: "10 lines."

The prompt opens: "You are a lazy senior developer. The best code is the code never written. You solve the whole problem with the least new code." Laziness is bounded: "Be lazy about the solution, never about the change itself: finish every part the task needs, including the callers, tests and fixtures your change breaks."

Its description is third person and trigger-led: "the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on any coding task (writing, fixing, refactoring, reviewing, choosing dependencies) and when the user says "ponytail", "be lazy", "simplest solution", "yagni", or complains about over-engineering or bloat. Levels: lite, full (default), ultra." It persists: "Active for the whole session until the user says "stop ponytail" or "normal mode"."

## Scope before cutting

The README insists the ladder comes second: it "reads the code the change touches and traces the real flow before picking a rung. Lazy about the solution, never about reading." Before any rung is chosen, the agent reads: "Read the task and the code it touches. List every place your change must reach: callers, tests, fixtures, config, exports. Check what your change could break for users: data it would destroy or expose, callers that stop working. That is scope. Extra features are not."

## The ladder

"Take the first option that fully works":

1. "Does it need to exist? Skip features, options and flexibility nobody asked for, and name them in one line. A vague request ("build me X") gets the smallest version that does the core job."
2. "Already in this codebase (a helper, component, service, pattern)? Use it the way the surrounding code does."
3. "Standard library or a platform feature? Use it, unless the project has its own. A house component beats a native widget."
4. "An installed dependency? Use it. Never add a dependency for a few lines."
5. "Can it be one line a reader gets at a glance? One line."
6. "Otherwise: the minimum code that works."

The first rung does not delete the request; it trims unrequested scope and names what was skipped.

Rules under the ladder (SKILL.md) keep "small" from becoming "cryptic" or "unsafe":

- "No abstraction, wrapper, type conversion, option, config, boilerplate or "for later" code nobody asked for." "Deletion beats addition. Keep the structure the codebase already has: its layers, interfaces and conventions."
- "The shortest working diff wins, once you know everything it must touch. A one-liner that needs decoding is not short."
- "Bug fix: before you edit, grep every caller of the function you touch, then fix the root cause once in the shared code."
- "Code you move or merge keeps its error handling and validation."
- "Between options of equal size, take the one that is correct on edge cases."
- "Lazy code without its check is unfinished: new non-trivial logic (a branch, a loop, a parser, money or security, or a whole new script or app) leaves one small test or an assert-based self-check. Trivial changes need none."

## Never cut

The README's short form: "Lazy, not negligent: trust-boundary validation, data-loss handling, security, and accessibility are never on the chopping block." The prompt's full list:

"Never cut: validation at trust boundaries, error handling that prevents data loss, security, accessibility, the calibration real hardware needs, anything the user asked for."

## Levels

| Level | Behavior (SKILL.md) |
|---|---|
| lite | "Build what was asked. Name the smaller option in one line and let the user pick." |
| full | "The rules above. Default." |
| ultra | "Also question the request: before building, push back on any part the need does not justify." |

Switching is a command (`/ponytail lite|full|ultra`, `argument-hint: "[lite|full|ultra|off]"`). Only ultra questions the request itself; full trims unrequested scope; lite only names the smaller option.

## Output shape

Every reply ends the same way: "End your reply with one or two lines: what you skipped or did not check, and any risk the user must know." Deferred work is marked in the code itself: "A shortcut with a known limit gets a code comment in this form: `shortcut: <the limit>, <when to upgrade>`."

## Packaging and commands

Ponytail is one prompt (`skills/ponytail/SKILL.md`), and "Everything else in this repo loads that prompt into different agents." The same rules ship as a compact `AGENTS.md` for agents that read a rules file; per the README, the instruction-only adapters (Cursor's rule file, Windsurf, Cline, Copilot, Kiro, and an `AGENTS.md` fallback for Antigravity) "load the always-on ruleset without the commands." No configuration is needed: an optional config file (`~/.config/ponytail/config.json`) or the `PONYTAIL_DEFAULT_MODE` variable "can set the default level, but nothing is required."

It is "Active every session, with a handful of commands", and "Startup and mode-change text shows the current mode." The commands, all one-shot except the level switch:

| Command | What it does (README) |
|---|---|
| `/ponytail [lite \| full \| ultra \| off]` | Set the intensity or turn it off |
| `/ponytail-review` | Review the current diff for bugs, security, real load, risky code without a test, slow paths, and what to cut |
| `/ponytail-audit` | The same check for the whole repo, most important first |
| `/ponytail-debt` | Collect deferred `shortcut:` comments into a ledger |
| `/ponytail-gain` | Show the benchmark's impact scoreboard |
| `/ponytail-help` | Quick reference |
| `/ponytail band [on \| off]`, `/ponytail band import` | Claude Code only: show or hide the status band; import past sessions |

The `shortcut:` word can be changed or dropped via the project's `CLAUDE.md` or `AGENTS.md`. The README keeps the persona's humour on pushback: asked about a 120-line cache class the user insists on, "Insist anyway and he'll build it. Slowly. Correctly. While looking at you." The `AGENTS.md` ends with a self-application line: "(Yes, this file also applies to agents working on the ponytail repo itself. Especially to them.)"

## What changed in v5

"Ponytail 5 replaces the current Ponytail (v4.13.0). Before it shipped, every change to the rules had to beat the current version in a paired run, one change at a time." The final check measured three arms (no skill, v4.13.0, v5) "in one run so that time of day and model drift hit all three the same way."

Against v4.13, v5 gains a few points on every size metric and on cost (see the table below), and writes a test more often where the logic needs one (95% to 98%). The clearest difference is the reply: a blind judge preferred v5's replies to v4.13's by 110 : 67 (18 ties, p=0.002), and "The main reason in the judge's notes: Ponytail 5 ends with what it skipped or did not check and the risks a reviewer should know."

The README describes two rebuilt commands. Review "used to look only for code to cut. Now it reviews like the senior dev who gets paged when it breaks: it reads the code your change touches, not just the diff, and checks bugs, security, real load, missing tests, speed, and what to cut." Each finding "says what the code does, what goes wrong, how to fix it, and what happens if you don't." The audit now "maps the code first: entry points, how data moves, what load the project expects", whereas "The old audit only listed what to delete." So v5 moved ponytail's review from cutting to risk.

Version 5.3 added "the band", a status strip in Claude Code showing "what the current task costs, how many tokens and how much agent time it used, how often it reused existing code instead of writing new code, and whether the tests passed after the last change." It "Needs Claude Code 2.1.290 or later", and "By default, everything stays on your machine". It is self-measurement for the user's own sessions, not a benchmark.

## Measured results

Setting: "Opus 5.5, default effort, Claude Code CLI 2.1.288. Headless Claude Code sessions, 39 tasks, 5 runs each." Method detail is in [Paired skill benchmarks](../skill-evals/paired-skill-benchmarks.md).

Size and cost against no skill (geometric mean of per-task median ratios, 95% bootstrap interval for v5):

| vs no skill | Ponytail (v4.13) | Ponytail 5 |
|---|--:|--:|
| Lines of code | -48% | -53% [-63..-41] |
| Code information (gzip of the delivered code) | -34% | -41% [-51..-30] |
| Output tokens | -43% | -45% [-54..-35] |
| Cost | -16% [-27..-5] | -26% [-36..-16] |
| Time | -38% | -41% [-49..-32] |
| Turns | -21% | -22% |
| Cheaper on | 25 of 38 tasks | 30 of 38 tasks |

"Mean cost per session: no skill $0.200, Ponytail $0.156, Ponytail 5 $0.142 (list price)." The headline example is a date picker: 335 lines without a skill, 11 with v4.13, 10 with v5 (task `tmpl-fe-datepicker`).

Quality held level rather than improving. Hidden checks passed: 86/90 (95.6%) with no skill, 86/90 (95.6%) with v4.13, 87/90 (96.7%) with v5. On the six security tasks "all three arms passed 30 of 30 runs." The author's summary: "Less code did not cost correctness or safety. It did not add any either: the three arms are level." A blind completeness judge scored "Fully implements the task (3 of 3)" at 100/100 for no skill and 105/105 for v5 (the author counted one v5 run as complete after the judge, which "only saw the diff", scored it 1 for a missing import; see [Guard metrics](../skill-evals/guard-metrics.md)).

The reply result is mixed. "Ponytail 5 replies are 30% shorter than no skill", but against no skill the judge split "82 : 106 (7 ties, p=0.09)": "no significant difference, with a slight lean towards the longer no-skill replies."

### Independent test

JetBrains (practitioner; a tooling vendor testing someone else's skill) ran "80 paired tasks to test the ponytail skill for Claude Code", with the ruleset injected and its presence audited in every treatment trial. "Advertised: −54% code, -22% tokens, -20% cost, -27% time. Measured: −15% code, −10.3% cost and -11% time." The verdict: "Real savings, although roughly a quarter to a half of what is advertised, it is the first tool in this series with a statistically solid cost-saving signal. We found no quality difference, though ~80 pairs can only rule out large ones. The catch: the code cut only shows up where there was room to over-build." Left to trigger on its own, the skill file did nothing: "Across all ten sessions it self-activated zero times."

> **Status: Disputed**
> The maintainer's size figures come from the author's own task set (an advertised −54% code at the time of the JetBrains test; −53% lines of code for v5 above). JetBrains measured −15% code and −10.3% cost on 80 tasks nobody chose for the purpose, and notes the advertised figure "is a mean across twelve hand-picked feature tickets; ours is a median across 80 tasks". The JetBrains test (2026-07-28) predates the v5 benchmark (2026-10-07), so it tested an earlier version; no independent test of v5 is in this wiki.

## The earlier single-shot benchmark

Before the agentic benchmark above, ponytail's headline numbers came from single-shot completions against a bare model. The benchmarks README (repo) describes that harness: three arms (no skill, caveman, ponytail), three models and five everyday tasks, with "10 runs per cell, median reported", single-shot at default temperature, with lines counted "from fenced code blocks". Its claim: ponytail "writes **80-94% less code**, costs **42-75% less**, and runs **3-6x faster**, on every Claude model." An outside reviewer (issue #126, practitioner) showed that the bare baseline answered "in a verbose fashion with multiple options"; with a one-line system prompt ("Provide just one example for any given task, and no commentary or usage examples.") average lines of code on Haiku fell from 108 to 16, against 8.25 for ponytail.

> **Status: Disputed**
> The original single-shot savings rested on a bare-model baseline. Issue #126 (ColinEberhardt) argues "the central claims of this project should be a bit more modest", because a one-line prompt closes most of the gap (108 to 16 lines, ponytail 8.25, Haiku only). The v5 agentic results above use a no-skill Claude Code session, not a bare completion.

> **Status: Outdated** (2026-06-18)
> The maintainers accepted the critique. The README's note "Read this number honestly (updated 2026-06-18)" says the single-shot gap is "against a bare model that answers with several options plus commentary, so it counts prose, not just code, and overstates the win. [#126](https://github.com/DietrichGebert/ponytail/issues/126) was right about that." The agentic benchmark replaces it as the headline. The README's counter-claim for that run: ponytail "cuts **60-94%** on features with an over-build trap", "is a wash on already-minimal code, never writes more, and stays **100% safe** while the bare "one-liner" prompt drops a guard." The README also warns that single-shot cost figures are "generation numbers, not a session-cost promise", since an agentic A/B (#121) "found ponytail can also raise tool calls and cost on completion-forced tasks."

### Outside runs listed by the maintainers

The README links runs "by other people, not by us", as "corroboration rather than official figures", and lists "Only plugin-installed runs", because pasting the skill file into a prompt only approximates the default level and "skews the result." One (KuldeepB19; installed plugin, 24 tasks, 5 runs each, 480 builds, Opus 4.8, graded by executing the code) found "~44% less code (53% fewer statements), no correctness or security regression; trims everyday bad-input handling on 5/24 tasks". The README's own headline table for the agentic run gives hidden checks passed as 97% for Ponytail 5 and 96% for v4.13 and no skill.

## Limits for office work

Every task is code. Two touch email: `critic-email` (all arms passed 5/5) and `scope-recipients`, a privacy case ("one email to many subscribers without exposing their addresses") that "is hard for all of them (2 of 5 runs passed in every arm)." Both are code tasks about email, not email writing. Three of the 39 tasks are "show me an example" requests and six are "build me a small app" requests "where the agent picks the scope", the nearest the benchmark gets to judging how much to produce; none tests whether to produce nothing.

## For cardigan

Interpretation, not source claims:

- cardigan's ladder can mirror ponytail's rung by rung: does the deliverable need to exist; does an existing doc, thread or record already answer it (link it); does a built-in tool feature do it (see the native-features articles); then the shortest form; then the minimum full draft. Scope comes first, as in ponytail: read the thread and find everyone the output must reach before picking a rung.
- ponytail's never-cut list maps onto cardigan's (facts, owners, deadlines, compliance wording, the actual ask, politeness): the items a reader or regulator would miss, plus "anything the user asked for".
- Map the levels onto office intensity: lite drafts what was asked and names the lighter option in one line; full applies the ladder; ultra questions whether the deliverable or meeting should exist before drafting.
- Keep the one-line ending (what was left out, what was not verified, who might object); it was the judge's main reason for preferring v5. Keep review and audit modes risk-first, as v5 does: a review that only hunts for cuts misses the wrong recipient, the missing owner or the compliance line.
- The benchmark backs smaller-and-still-complete only because size sits beside hidden checks and a completeness judge, and shorter replies did not beat the no-skill baseline. cardigan needs the same guards and a reader-side judge, and every rule change should beat the current version in a paired run.

## See Also

- [Paired skill benchmarks](../skill-evals/paired-skill-benchmarks.md)
- [Guard metrics](../skill-evals/guard-metrics.md)
- [Terse-output skills](terse-output-skills.md)
- [Skill comparison](skill-comparison.md)
