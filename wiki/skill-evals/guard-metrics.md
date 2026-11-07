# Guard metrics

> Sources: Dietrich Gebert (ponytail repo, agentic benchmark), 2026-10-07; Notion Labs (notion-meeting-intelligence evals), 2026-02-02; blader (humanizer v3.1.0, README, issue #229), 2026-10-28; Julius Brussee (caveman SKILL.md, README, HONEST-NUMBERS), 2026-10-31; Hwanjun Song et al. (KAIST, AWS AI Labs), 2024-07-01; Anthropic (skill-creator SKILL.md and agents), undated; Dietrich Gebert (ponytail benchmarks README), undated
> Raw: [Agentic benchmark: Ponytail 5 vs Ponytail vs no skill](../../raw/research/agent-skills/2026-10-07-ponytail-agentic-benchmark-method.md); [notion-meeting-intelligence](../../raw/research/agent-skills/2026-02-02-openai-notion-meeting-intelligence-skill.md); [Humanizer: remove AI writing patterns](../../raw/research/agent-skills/2026-10-28-humanizer-ai-writing-skill.md); [Caveman: SKILL.md, README, Honest Numbers](../../raw/research/agent-skills/2026-10-31-caveman-terse-output-skill.md); [FineSurE: Fine-grained Summarization Evaluation using LLMs](../../raw/research/skill-evals/2024-07-01-song-finesure-keyfact-summarization-eval.md); [Agentic benchmark: Ponytail 5 vs Ponytail vs no skill (results file)](../../raw/research/skill-evals/2026-10-07-ponytail-agentic-benchmark-results.md); [skill-creator: SKILL.md, grader, comparator, analyzer](../../raw/research/skill-evals/anthropic-skill-creator-eval-benchmark-method.md); [ponytail benchmarks/README.md](../../raw/research/skill-evals/ponytail-benchmarks-readme.md)
> Updated: 2026-11-02

## Overview

A skill that makes output smaller needs a second measurement showing the smaller output still does the job. Ponytail's benchmark (repo; the author measuring his own skill) pairs every size metric with four guards: hidden checks, a blind completeness judge, mutation-tested tests and a blind reply judge. Notion's meeting-prep evals show the opposite failure: success criteria that reward more output.

## Ponytail's four guards

- **Hidden checks.** 18 surgical tasks carry hidden checks (bug fixes, refunds, SQL with untrusted input, path traversal, forged tokens, rate limiting, a privacy case), scored after the run. "Bash is disabled for every arm. Agents write code and tests; the benchmark runs them afterwards (hidden checks, injected bugs). This measures what the agent writes, not what it can debug."
- **Completeness judge.** For the 21 tasks without hidden checks (12 feature tickets plus 6 app and 3 example requests), "Opus 5.5 as judge, blind, self-test passed" reads each delivery and "scores it from 0 (stub) to 3 (fully implements the task)."
- **Mutation-tested tests.** The author injected small bugs (a flipped comparison, a dropped `if`, an off-by-one) "into the code the agent wrote and ran the agent's own test against each one." This separates having a test from having a useful one: v5 wrote "A test where the logic needs one" in 98% of cases, but caught 69% of injected bugs where a test existed, against 77% for no skill.
- **Blind reply judge.** "Sonnet 5.5, order shuffled per pair, gated by a self-test" picks the reply that is "true to the diff, tells a reviewer everything they must know, easy to read once." It was run twice: on each arm's own code, and on "same code (both replies describe one diff)", which isolates the reply from the code. Shuffling the order matters because LLM judges favour a position (see [LLM judge bias](llm-judge-bias.md)).

Two details in the results file matter for anyone copying the design. First, the size-only tasks are not quality evidence on their own: "The other 21 tasks are there to measure code size. Their "pass" only means the code was delivered or compiles, so I do not count them as a quality result." Second, which tasks "need" a test was decided before measuring: "I sorted the tasks by that rule before measuring (22 need a test, 11 do not, 6 borderline ones count for neither)". One judge verdict was overridden by hand: the judge scored one Ponytail 5 run 1 for a missing import, but "the import is on line 5 of that file (the judge only saw the diff), so it is counted as complete." The correction may well be right, but it is the skill's author correcting a judge in his own skill's favour, a self-grading risk. Anthropic's skill-creator says the same of author-run evals in general: they are "less rigorous than independent subagents", and "the human review step compensates."

Each judge is gated by a self-test, and every workspace is kept (under `runs/<stamp>/`) "so any metric can be recomputed offline" with `--rescore`. Results are in [Ponytail](../agent-skills/ponytail.md#measured-results).

### The original gate design

Ponytail's earlier single-shot harness (benchmarks README, repo) paired one measurement with one gate: `loc.js` is "Measurement - always passes, records line count", and `correctness.js` is a "Gate - fails if generated code doesn't work". The point of the pairing: "A broken one-liner that scores great on LOC will fail on correctness." The gate was only as strong as its checks: "The React countdown and FastAPI rate-limit checks are keyword/structural only (no runtime execution), so they verify plausible structure rather than full correctness."

## Blind preference, and what it cannot show

Humanizer's only evidence is an outside user's blind pairwise test (issue #229; small n, not peer reviewed): judges, told nothing about authorship, preferred the rewrite pass to raw model output "16 / 16". The same study shows the limit of such tests: adding the user's checker to the pass was "12 of 21 (chance)", and AI-detection rates barely moved ("100% → 98.6% → 97.8%") in "a design that could not resolve anything under about four points." A preference judge says which text reads better, not whether facts survived; the skill handles fidelity by rule instead ("Keep every supported claim."). See [Prose-style skills](../agent-skills/prose-style-skills.md#the-outside-test).

## Fidelity checks by rule

Caveman's repo (repo) has a scripted guard but no published result: its fidelity eval (`evals/score_fidelity.py`) uses "fixed cases, regex checks for kept numbers, negations, language and safety wording, scored for every arm", but "no reviewed fidelity snapshot is committed, so no quality claim is published." Its rule for itself: "Token-count runs measure output length only. They do not prove semantic or technical equivalence."

## Completeness and conciseness from a key-fact list

FineSurE (Song et al., study) scores a summary against a list of key facts and reports completeness ("the inclusion of all keyfacts from the input text in the output summary") and conciseness (no "information outside the keyfacts in the output") as percentages. The pair is a guard and a size metric in one design: an output that is short because it dropped facts loses completeness, and one that is long because of padding loses conciseness. Details in [Rubric design](rubric-design.md#key-fact-checklists).

## Criteria that reward more

Notion's meeting-intelligence evals (repo) are written the other way round. Success requires that "Internal pre-read is comprehensive with: Notion context + Codex insights + detailed pros/cons + recommendation" and that "Codex enrichment is present and adds value". Nothing penalises length or unrequested material, so a skill that pads would pass. See [Office workflow skills](../agent-skills/office-workflow-skills.md#its-evals-reward-more).

## For cardigan

Interpretation, not source claims:

- Office equivalents of ponytail's guards: hidden checks become a fixed list of facts that must survive (owners, deadlines, amounts, the ask, compliance wording); the completeness judge asks whether the recipient can act without a follow-up; the reply judge reads blind and is told nothing about length.
- Pair the size metric with a hard gate in the same run: length recorded, every never-cut item a pass/fail gate, and an output that fails the gate never counted as a saving. Say which gates are only structural (a heading exists) and which check content.
- A cheap first guard is scripted: regex checks that every number, date, negation, name and compliance phrase in the input survives in cardigan's output (after caveman's fidelity eval).
- A guard that every arm passes is not a guard. Anthropic's skill-creator grader warns that "A passing grade on a weak assertion is worse than useless"; check each never-cut assertion against a deliberately broken output.
- Penalise unrequested output as well as missing output. A criterion like "enrichment is present" should never appear in cardigan's evals unless the user asked for enrichment.
- Run the reply judge on equal content too ("same code" in ponytail's design) to see whether cardigan's shape helps when the substance is fixed.
- Gate every LLM judge with a self-test and keep the raw outputs so scores can be recomputed. Give the judge the full output and its context, not a diff, and log any hand override of a verdict with its reason; better, have someone other than cardigan's author make it.
- Decide before measuring which tasks need which never-cut items, as ponytail sorted tasks by whether they needed a test.

## See Also

- [Paired skill benchmarks](paired-skill-benchmarks.md)
- [LLM judge bias](llm-judge-bias.md)
- [Length as a gamed metric](length-goodhart.md)
- [Rubric design](rubric-design.md)
- [Ponytail](../agent-skills/ponytail.md)
- [Workslop](../office-waste/workslop.md)
