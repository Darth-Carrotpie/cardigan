# Skill authoring guidance

> Sources: Anthropic (Claude Platform docs, Skill authoring best practices), undated; Anthropic (Claude Code docs, Extend Claude with skills), undated; Anthropic (skill-creator SKILL.md and agents), undated
> Raw: [Skill authoring best practices](../../raw/research/agent-skills/anthropic-skill-authoring-best-practices.md); [Extend Claude with skills (Claude Code docs)](../../raw/research/agent-skills/claude-code-skills-docs-lifecycle-and-invocation.md); [skill-creator: SKILL.md, grader, comparator, analyzer](../../raw/research/skill-evals/anthropic-skill-creator-eval-benchmark-method.md)
> Updated: 2026-11-02

## Overview

Anthropic's official guidance (official-docs) on writing Agent Skills comes down to three rules: keep the skill short because it shares the context window, write a description that lets the model pick the skill from many, and build evaluations against a no-skill baseline before writing much. The platform doc does not address always-on skills specifically; the Claude Code docs fill part of the gap: an invoked skill stays in context across turns, and after compaction only its first 5,000 tokens come back.

## Concise, because context is shared

"Good Skills are concise, well-structured, and tested with real usage." The reason: "The context window is a public good." Loading is staged: "At startup, only the metadata (name and description) from all Skills is pre-loaded." The full SKILL.md is read "only when the Skill becomes relevant", and other files "only as needed." Once loaded, though, "every token competes with conversation history and other context."

The default assumption is "Claude is already very smart", so "Only add context Claude doesn't already have", tested by questions such as "Does this paragraph justify its token cost?" Specificity should scale with risk: "Match the level of specificity to the task's fragility and variability." And: "Don't present multiple approaches unless necessary".

Structure limits: keep the SKILL.md body under 500 lines "for optimal performance", split into separate files near that limit, and "Keep references one level deep from `SKILL.md`".

## The description does the selecting

The `description` field has hard limits ("Maximum 1,024 characters", "Cannot contain XML tags") and one job: it "Should describe what the Skill does and when to use it". It matters because "Claude uses it to choose the right Skill from potentially 100+ available Skills." Point of view is fixed: always third person, because "The description is injected into the system prompt, and inconsistent point-of-view can cause discovery problems." Anthropic's own internal-comms skill breaks this rule with a first-person description ("help me write"); see [Office workflow skills](office-workflow-skills.md#internal-comms-a-router-to-house-formats).

## In Claude Code: lifecycle and invocation

The Claude Code docs (official-docs) add host behaviour. A loaded skill is not a one-off: its rendered content "enters the conversation as a single message and stays there across later turns", hence "every line is a recurring token cost". The docs draw the authoring consequence: "Claude Code does not re-read the skill file on later turns, so write guidance that should apply throughout a task as standing instructions rather than one-time steps." Style follows: "State what to do rather than narrating how or why".

Compaction trims long skills. Claude Code "re-attaches the most recent invocation of each skill after the summary, keeping the first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens", filled from the most recent skill, so "older skills can be dropped entirely after compaction if you have invoked many in one session."

The listing has its own limit, separate from the platform's 1,024-character description field: the combined description and `when_to_use` text "is truncated at 1,536 characters in the skill listing to reduce context usage", so "Put the key use case first". The size rule is the same: under 500 lines.

Two switches set who can start a skill. With `disable-model-invocation: true`, "Claude can't invoke the skill on its own", meant for side effects ("You don't want Claude deciding to deploy because your code looks ready."); the description is then not in context. With `user-invocable: false`, "Only Claude can invoke the skill", for background knowledge; the description is always in context. An `argument-hint` shows expected arguments in autocomplete, which is how skills such as ponytail and status-report double as commands.

## Evaluations first

"Create evaluations BEFORE writing extensive documentation." The loop:

1. Run Claude on representative tasks without a skill and document failures.
2. "Build three scenarios that test these gaps."
3. "Measure Claude's performance without the Skill."
4. "Create just enough content to address the gaps and pass evaluations."
5. Iterate against the baseline.

"There is not currently a built-in way to run these evaluations", yet "Evaluations are your source of truth for measuring Skill effectiveness." The doc asks for testing on three model sizes, with a different question for each (for Opus: "Does the Skill avoid over-explaining?"), and suggests a two-instance loop: "Work with one instance of Claude ("Claude A") to create a Skill that is used by other instances ("Claude B")." The checklist minimum is "At least three evaluations created" and "Tested with Haiku, Sonnet, and Opus". See [Paired skill benchmarks](../skill-evals/paired-skill-benchmarks.md).

> **Status: Disputed**
> Anthropic's own skill-creator does not make evaluations universal: "Skills with subjective outputs (writing style, art) often don't need them", while skills with "objectively verifiable outputs" benefit from test cases, and the user decides. See [Paired skill benchmarks](../skill-evals/paired-skill-benchmarks.md#baseline-first-official-guidance).

## For cardigan

Interpretation, not source claims:

- cardigan's description must carry its triggers (office deliverables: email, chat, meetings, docs, decks, status, planning) within 1,024 characters, in the third person, key use case first.
- Keep SKILL.md short (ponytail is the size benchmark) and push office-specific detail (per-deliverable rules, native-feature lists) into one level of reference files.
- Write the body as standing instructions (it persists across turns) and put the load-bearing rules (the ladder, never-cut list, output shape) early, so they survive the 5,000-token re-attachment after compaction.
- Any cardigan command with side effects (sending, posting, cancelling a meeting) belongs behind `disable-model-invocation: true` or an explicit user confirmation; the always-on part stays model-invoked.
- Write evals before rules: run the model on office tasks with no skill, record where it over-produces, write only the rules that fix those failures, and test on small and large models (a small model may need more explicit "whether" rules; a large one may over-apply them).

## See Also

- [Ponytail](ponytail.md)
- [Paired skill benchmarks](../skill-evals/paired-skill-benchmarks.md)
- [Skill comparison](skill-comparison.md)
