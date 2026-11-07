# Agentic benchmark: Ponytail 5 vs Ponytail vs no skill

> Source: https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-10-07-agentic.md
> Collected: 2026-10-31
> Published: 2026-10-07
> Author: DietrichGebert (ponytail maintainers), MIT License
> Type: repo

## Excerpts

> Ponytail 5 replaces the current Ponytail (v4.13.0). Before it shipped, every change to the rules had to beat the current version in a paired run, one change at a time. This file is the final check: Ponytail 5, Ponytail (v4.13.0) and the same agent without any skill, measured in one run so that time of day and model drift hit all three the same way.

> The skill is loaded with `--plugin-dir`, the same way a user gets it. The no-skill arm loads nothing. For every arm I checked the session transcript of a finished cell to prove what was injected.

> **Runs:** 5 per task and arm, 585 sessions. The three arms alternate task by task.

> **Isolation:** every session runs in a fresh temp folder outside any git repo, with `CLAUDE.md` loading and auto memory switched off, and only the plugin under test. (An earlier version of the harness ran some tasks inside the Ponytail repo. Claude Code then showed the model the repo's recent commit messages. That is fixed, and none of the numbers here come from that setup.)

> **Statistics.** For each task I take the median of the 5 runs, divide arm by baseline, and report the geometric mean of those ratios over the tasks, with a 95% bootstrap interval. "Better on X of Y tasks" is a sign test over the tasks.

> | Lines of code | -48% | **-53%** [-63..-41] |
> | Code information (gzip of the delivered code) | -34% | **-41%** [-51..-30] |
> [...]
> | Cost | -16% [-27..-5] | **-26%** [-36..-16] |

> The other 21 tasks are there to measure code size. Their "pass" only means the code was delivered or compiles, so I do not count them as a quality result.

> Whether the shorter code on these 21 tasks still does the whole job is checked by the completeness judge (`benchmarks/agentic/complete.py`, Opus 5.5 as judge, blind, self-test passed). It reads what each run delivered and scores it from 0 (stub) to 3 (fully implements the task).

> The judge scored one Ponytail 5 run 1 for a missing `col` import; the import is on line 5 of that file (the judge only saw the diff), so it is counted as complete.

> I sorted the tasks by that rule before measuring (22 need a test, 11 do not, 6 borderline ones count for neither), then checked what each agent left behind.

> A blind judge (Sonnet 5.5, order shuffled per pair, gated by a self-test) picked the reply that serves a busy developer better: true to the diff, tells a reviewer everything they must know, easy to read once.

> | Ponytail 5 vs Ponytail (v4.13) | **110 : 67** (18 ties, p=0.002) | **131 : 89** (12 ties, p=0.006) |
> | Ponytail 5 vs no skill | 82 : 106 (7 ties, p=0.09) | 99 : 118 (15 ties, p=0.22) |

> Ponytail 5 replies are 30% shorter than no skill. Against no skill the judge found no significant difference, with a slight lean towards the longer no-skill replies.

> Every workspace is kept under `runs/<stamp>/`, so any metric can be recomputed offline with `--rescore`.

## Collector's note

Maintainer-run, three-arm interleaved benchmark (39 tasks × 5 runs × 3 arms = 585 sessions), per-task medians, geometric-mean ratios with bootstrap CIs, sign tests, plus a blind shuffled-order pairwise judge for replies and a 0–3 completeness judge. Notably the judge leaned (non-significantly) toward the longer no-skill replies, and one judge error was hand-overridden by the author, which is a self-grading risk. For cardigan: interleave arms, isolate sessions from repo/memory context, pre-classify which tasks "need" an item before measuring, add a "same content, different wording" control for the pairwise judge, and keep raw outputs for rescoring.
