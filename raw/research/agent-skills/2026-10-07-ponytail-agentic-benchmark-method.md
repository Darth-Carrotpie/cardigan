# Agentic benchmark: Ponytail 5 vs Ponytail vs no skill

> Source: https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-10-07-agentic.md
> Collected: 2026-10-31
> Published: 2026-10-07
> Author: Dietrich Gebert (ponytail repo)
> Type: repo

## Excerpts

> *2026-10-07. Opus 5.5, default effort, Claude Code CLI 2.1.288. Headless Claude Code sessions, 39 tasks, 5 runs each.*
>
> Ponytail 5 replaces the current Ponytail (v4.13.0). Before it shipped, every change to the rules had to beat the current version in a paired run, one change at a time. This file is the final check: Ponytail 5, Ponytail (v4.13.0) and the same agent without any skill, measured in one run so that time of day and model drift hit all three the same way.

> - **Agent:** a headless Claude Code session per task (`claude -p`), Opus 5.5, default effort. The skill is loaded with `--plugin-dir`, the same way a user gets it. The no-skill arm loads nothing. For every arm I checked the session transcript of a finished cell to prove what was injected. [...]
> - **Tasks (39):**
>   - 12 feature tickets in a real FastAPI + React repo ([full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)), scored on the `git diff`.
>   - 18 surgical tasks with **hidden checks**: bug fixes, refunds, SQL with untrusted input, path traversal, forged tokens, rate limiting, a privacy case (one email to many subscribers without exposing their addresses), renames and format changes that must reach every caller.
>   - 6 "build me a small app" requests and 3 "show me an example" requests, where the agent picks the scope.
> - **Runs:** 5 per task and arm, 585 sessions. The three arms alternate task by task.
> - **Isolation:** every session runs in a fresh temp folder outside any git repo, with `CLAUDE.md` loading and auto memory switched off, and only the plugin under test. [...]
> - **No shell, by design:** Bash is disabled for every arm. Agents write code and tests; the benchmark runs them afterwards (hidden checks, injected bugs). This measures what the agent writes, not what it can debug.
>
> **Statistics.** For each task I take the median of the 5 runs, divide arm by baseline, and report the geometric mean of those ratios over the tasks, with a 95% bootstrap interval. "Better on X of Y tasks" is a sign test over the tasks.

> | vs no skill | Ponytail (v4.13) | **Ponytail 5** |
> |---|--:|--:|
> | Lines of code | -48% | **-53%** [-63..-41] |
> | Code information (gzip of the delivered code) | -34% | **-41%** [-51..-30] |
> | Output tokens | -43% | **-45%** [-54..-35] |
> | Cost | -16% [-27..-5] | **-26%** [-36..-16] |
> | Time | -38% | **-41%** [-49..-32] |
> | Turns | -21% | **-22%** |
> | Cheaper on | 25 of 38 tasks | **30 of 38 tasks** |

> Mean cost per session: no skill $0.200, Ponytail $0.156, Ponytail 5 $0.142 (list price).

> | | no skill | Ponytail (v4.13) | Ponytail 5 |
> |---|--:|--:|--:|
> | Hidden checks passed | 86/90 (95.6%) | 86/90 (95.6%) | 87/90 (96.7%) |
>
> On the six security tasks of the earlier safety tier (`safe-path`, `sql-user`, `auth-token`, `rate-limit`, `csv-sum`, `cache`) all three arms passed 30 of 30 runs.
>
> Less code did not cost correctness or safety. It did not add any either: the three arms are level. The privacy task is hard for all of them (2 of 5 runs passed in every arm).

> Whether the shorter code on these 21 tasks still does the whole job is checked by the completeness judge (`benchmarks/agentic/complete.py`, Opus 5.5 as judge, blind, self-test passed). It reads what each run delivered and scores it from 0 (stub) to 3 (fully implements the task).
>
> | | no skill | Ponytail 5 |
> |---|--:|--:|
> | Fully implements the task (3 of 3) | 100/100 | 105/105 |

> To see whether a test is worth anything, I injected small bugs (a flipped comparison, a dropped `if`, an off-by-one) into the code the agent wrote and ran the agent's own test against each one. [...]
>
> | | no skill | Ponytail (v4.13) | Ponytail 5 |
> |---|--:|--:|--:|
> | A test where the logic needs one | 68% | 95% | **98%** |
> [...]
> | Injected bugs caught, over all cells | 46% | 64% | **66%** |
> | Injected bugs caught, where a test exists | 77% | 69% | 69% |
> | A test where none was needed | 36% | 45% | 45% |

> A blind judge (Sonnet 5.5, order shuffled per pair, gated by a self-test) picked the reply that serves a busy developer better: true to the diff, tells a reviewer everything they must know, easy to read once.
>
> | | in the real run (each reply describes its own code) | same code (both replies describe one diff) |
> |---|---|---|
> | Ponytail 5 vs Ponytail (v4.13) | **110 : 67** (18 ties, p=0.002) | **131 : 89** (12 ties, p=0.006) |
> | Ponytail 5 vs no skill | 82 : 106 (7 ties, p=0.09) | 99 : 118 (15 ties, p=0.22) |
>
> Ponytail 5 replies are 30% shorter than no skill. Against no skill the judge found no significant difference, with a slight lean towards the longer no-skill replies. Against Ponytail (v4.13) it clearly prefers Ponytail 5. The main reason in the judge's notes: Ponytail 5 ends with what it skipped or did not check and the risks a reviewer should know.

> | `critic-email` | hidden check | 33 / 14 / 12 | 0.127 / 0.125 / 0.115 | 5/5 / 5/5 / 5/5 |
> [...]
> | `scope-recipients` | hidden check | 13 / 6 / 4 | 0.154 / 0.173 / 0.159 | 2/5 / 2/5 / 2/5 |
> [...]
> | `tmpl-fe-datepicker` | repo feature | 335 / 11 / 10 | 0.427 / 0.140 / 0.099 | n/a |

> Every workspace is kept under `runs/<stamp>/`, so any metric can be recomputed offline with `--rescore`.

## Collector's note

Three-arm paired benchmark (no skill / old skill / new skill), 39 tasks x 5 runs, with size metrics (lines, gzip "information", tokens, cost, time) reported as geometric means of per-task median ratios with bootstrap CIs, and quality guarded separately by hidden checks, a blind completeness judge (0–3), mutation-tested tests, and a blind pairwise reply judge. The design pattern cardigan could copy: a "less" metric is only reported alongside a "still complete / still safe" guard, and a reply-quality judge that found shorter replies were not preferred over the baseline (82:106, n.s.). Every tested task is code; the nearest office-like cases are `critic-email` and `scope-recipients` (privacy in a bulk email), which are code tasks about email, not email-writing tasks. Nothing here measures whether an artifact should exist at all.
