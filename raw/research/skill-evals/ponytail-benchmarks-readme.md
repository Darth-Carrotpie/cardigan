# ponytail — benchmarks/README.md

> Source: https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/README.md
> Collected: 2026-10-31
> Published: Unknown
> Author: DietrichGebert (ponytail maintainers), MIT License
> Type: repo

## Excerpts

> The headline benchmark is the [agentic benchmark](agentic/): a headless Claude Code session per task, the same agent with and without the skill, scored on what it leaves behind. 39 tasks, Opus 5.5, 5 runs each, Ponytail 5, the previous Ponytail (v4.13) and no skill in one interleaved run.

> | vs no skill | lines of code | output tokens | cost | time | hidden checks passed |
> |---|--:|--:|--:|--:|--:|
> | **Ponytail 5** | **-53%** | **-45%** | **-26%** | **-41%** | **97%** |
> | Ponytail (v4.13) | -48% | -43% | -16% | -38% | 96% |
> | no skill | | | | | 96% |

> Three arms (no skill, [caveman](https://github.com/JuliusBrussee/caveman), ponytail), three models, five everyday tasks, **10 runs per cell, median reported**. Code LOC is counted from fenced code blocks; tokens, cost, and latency come straight from the API.

> Tasks: email validator, JS debounce, CSV sum, React countdown, FastAPI rate-limit (see `promptfooconfig.yaml`). Single-shot completions, default temperature.

> Versus baseline, ponytail writes **80-94% less code**, costs **42-75% less**, and runs **3-6x faster**, on every Claude model.

> **Read this number honestly (updated 2026-06-18).** The gap above is single-shot, against a bare model that answers with several options plus commentary, so it counts prose, not just code, and overstates the win. [#126](https://github.com/DietrichGebert/ponytail/issues/126) was right about that. The [agentic benchmark](agentic/) re-runs the comparison as a *real Claude Code session on a real public repo*: ponytail cuts **60-94%** on features with an over-build trap (custom component vs native input), is a wash on already-minimal code, never writes more, and stays **100% safe** while the bare "one-liner" prompt drops a guard.

> Run by other people, not by us, on their own harnesses and machines. Linked for transparency: the numbers are theirs, may shift between runs, and are corroboration rather than official figures. Only plugin-installed runs are listed, since pasting `SKILL.md` into a prompt is a rough approximation of `full` and skews the result.

> | [KuldeepB19](https://kuldeepb19.github.io/ponytail-benchmark/) | Installed plugin, 24 tasks, no-skill vs Lite/Full/Ultra, 5 runs each (480 builds), Opus 4.8, graded by executing the code | ~44% less code (53% fewer statements), no correctness or security regression; trims everyday bad-input handling on 5/24 tasks | 2026-06-24 |

> | `loc.js` | `loc` | Measurement - always passes, records line count |
> | `correctness.js` | `correct` | Gate - fails if generated code doesn't work |

> A broken one-liner that scores great on LOC will fail on correctness.

> **Note:** The React countdown and FastAPI rate-limit checks are keyword/structural only (no runtime execution), so they verify plausible structure rather than full correctness. The email, debounce, and CSV checks execute the code.

> Cost reflects single-shot calls (one prompt, one completion), not real multi-turn agent sessions. [...] a measured agentic A/B ([#121](https://github.com/DietrichGebert/ponytail/issues/121)) found ponytail can also raise tool calls and cost on completion-forced tasks. Treat these as generation numbers, not a session-cost promise.

## Collector's note

ponytail's benchmark has two generations: a promptfoo single-shot harness (5 tasks × 3 models × 10 runs, median, LOC metric paired with a correctness gate) and a newer agentic harness (39 tasks × 5 runs, Opus 5.5). The maintainers themselves concede the single-shot number overstated the win because the baseline was chatty. For cardigan, the "measurement metric + hard gate" pairing (length recorded, never-cut items as a pass/fail gate) is directly reusable, as is the warning that baseline framing can inflate a brevity effect.
