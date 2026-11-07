# Benchmark issues - baseline scores are ~7 times better (ponytail issue #126)

> Source: https://github.com/DietrichGebert/ponytail/issues/126
> Collected: 2026-10-31
> Published: 2026-06-16
> Author: ColinEberhardt (GitHub issue on DietrichGebert/ponytail)
> Type: practitioner

## Excerpts

> Hi, firstly, thanks for including a benchmark - most projects of this type don't have anything of the sort.

> 1. With the baseline test case, the model often responds in a verbose fashion with multiple options. This is because the test case lacks a system prompt that is consistent with the types of prompt used by coding harnesses
> 2. The debounce tests fails often for all the test targets (baseline, caveman, ponytail) due to an ambiguous test case. The response often expects the presence of a DOM (i.e. referencing `document`), which is entirely reasonable based on the test case.

> Fixing (1), by adding the simple system prompt `Provide just one example for any given task, and no commentary or usage examples.`, makes quite an impact on the results:
>
> Average LOC, running all tests (minus debounce) on haiku only:
>
>  - Baseline (108)
>  - Baseline – "one example" system prompt (16)
>  - Ponytail (8.25)
>
> As a result, the central claims of this project should be a bit more modest.

## Collector's note

A short external critique of ponytail's original single-shot benchmark: the no-skill baseline lacked a realistic system prompt, so much of the measured "saving" was the baseline being chatty; a one-line "be concise" prompt closed most of the gap (108 → 16 vs ponytail 8.25 LOC, Haiku only). The maintainers later accepted this in their README. For cardigan, this argues for a third arm — a one-line "be brief" prompt — so the skill is credited only for what a trivial instruction cannot achieve, and for checking that tasks are unambiguous.
