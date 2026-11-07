# Baseline and task design

> Sources: Anthropic Engineering ("Demystifying evals for AI agents"), 2026-01-09; ColinEberhardt (ponytail issue #126), 2026-06-16; Denis Shiryaev / JetBrains AI blog (ponytail test), 2026-07-28; Hamel Husain and Shreya Shankar (AI evals FAQ), 2026-09-18; Dietrich Gebert (ponytail benchmarks README), undated
> Raw: [Demystifying evals for AI agents](../../raw/research/skill-evals/2026-01-09-anthropic-demystifying-evals-for-ai-agents.md); [Benchmark issues - baseline scores are ~7 times better (ponytail issue #126)](../../raw/research/skill-evals/2026-06-16-ponytail-issue-126-baseline-critique.md); [Ponytail Skill for Claude Code: Does It Really Cut Agent Code by 54%?](../../raw/research/skill-evals/2026-07-28-jetbrains-ponytail-independent-test.md); [AI Evals: Everything You Need to Know](../../raw/research/skill-evals/2026-09-18-husain-shankar-ai-evals-faq.md); [ponytail benchmarks/README.md](../../raw/research/skill-evals/ponytail-benchmarks-readme.md)
> Updated: 2026-11-02

## Overview

What a skill is compared against, and on which tasks, decides most of what an eval can show. A trivial one-line instruction is the control a brevity skill has to beat: ponytail's issue #126 showed most of its first measured saving came from a chatty bare baseline. Anthropic's agent-evals guide (official-docs) adds two design rules to the paired setup in [Paired skill benchmarks](paired-skill-benchmarks.md): test both the cases where a behaviour should happen and where it should not, so the eval does not reward doing it everywhere; and start every trial from a clean environment, because leftovers from earlier trials can leak answers.

## A trivial control arm

A bare model is a weak baseline for a brevity skill. An outside critique of ponytail's original single-shot benchmark (practitioner; GitHub issue #126) found that "the model often responds in a verbose fashion with multiple options" because "the test case lacks a system prompt that is consistent with the types of prompt used by coding harnesses". Adding one line, "Provide just one example for any given task, and no commentary or usage examples.", "makes quite an impact on the results". Average lines of code on Haiku, all tests except one:

- Baseline (108)
- Baseline – "one example" system prompt (16)
- Ponytail (8.25)

The author's conclusion: "the central claims of this project should be a bit more modest." Most of the measured saving was the bare baseline being chatty, which a one-line instruction removes. Husain and Shankar's evals FAQ (practitioner) puts it as a general rule: "Many teams discover their LLM doesn't meet preferences they never actually specified - like wanting short responses, specific formatting, or step-by-step reasoning. Fix these obvious gaps first before building complex evaluation infrastructure." Ponytail's maintainers accepted the critique (README, "updated 2026-06-18": the single-shot gap "counts prose, not just code, and overstates the win") and moved their headline to an agentic run against a no-skill Claude Code session. They also make a counter-claim about the trivial arm: in that run ponytail "stays **100% safe** while the bare "one-liner" prompt drops a guard." A one-line instruction can match a skill on length while losing what the skill protects, so the control arm needs the same guards. Caveman's own concise-instruction arm makes the same point (see [Paired skill benchmarks](paired-skill-benchmarks.md#the-concise-control)).

## Two-sided tasks

"Test both the cases where a behavior should occur and where it shouldn't. One-sided evals create one-sided optimization. For instance, if you only test whether the agent searches when it should, you might end up with an agent that searches for almost everything. Try to avoid class-imbalanced evals."

## Clean, isolated trials

"Each trial should be "isolated" by starting from a clean environment." The guide gives a leak it saw: "in some internal evals we observed Claude gaining an unfair advantage on some tasks by examining the git history from previous trials."

### Audit that the skill reached the model, and only there

JetBrains' ponytail test (practitioner) audits both arms: "Every with-ponytail trial is audited afterwards to confirm the ruleset actually reached the model; every baseline trial is audited to confirm it did not." It calls this "the direct descendant of the contamination bug ponytail found in its own benchmark", and it "came back clean: 100% of treatment trials, 0% of baselines." Its other finding shows why the treatment side needs checking too: the plain skill file "self-activated zero times" across ten sessions.

## Unambiguous tasks

"A good task is one where two domain experts would independently reach the same pass/fail verdict. [...] Ambiguity in task specifications becomes noise in metrics."

The same issue shows what an ambiguous task does: the debounce test "fails often for all the test targets (baseline, caveman, ponytail) due to an ambiguous test case", because answers reasonably assumed a browser page ("referencing `document`").

## For cardigan

Interpretation, not source claims:

- Give cardigan's evals a third arm with a one-line instruction ("keep it short" or "be brief") in a realistic system prompt. cardigan earns credit only for what that line cannot do: dropping the deliverable, linking instead of restating, keeping the never-cut items.
- Score the "be brief" arm on the never-cut checks too: if it matches cardigan on length but drops a deadline or an owner, that is cardigan's real advantage.
- cardigan's task set must include tasks where cutting is wrong: a document that genuinely needs detail, a sensitive message that needs its softening, a request where the full deliverable is the right answer. An eval of only bloated requests rewards a skill that always cuts.
- Balance the set roughly between "less is right" and the full thing is right, and score both directions.
- Run each trial in a fresh session with no user memory, project instructions or earlier drafts visible, and check the transcript to confirm nothing leaked between arms.
- Audit every trial's transcript: cardigan present in its arm, absent from the baseline and the "be brief" arm.
- Before scoring, check that two people would agree on what a good answer to each task is; drop or rewrite tasks where they would not.

## See Also

- [Paired skill benchmarks](paired-skill-benchmarks.md)
- [Rubric design](rubric-design.md)
- [Length as a gamed metric](length-goodhart.md)
