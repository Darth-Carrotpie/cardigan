# Anthropic skills: doc-coauthoring

> Source: https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md
> Collected: 2026-10-31
> Published: 2025-12-04 (last commit to the skill folder)
> Author: Anthropic
> Type: repo

## Excerpts

> description: Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

> 1. **Context Gathering**: User provides all relevant context while Claude asks clarifying questions
> 2. **Refinement & Structure**: Iteratively build each section through brainstorming and editing
> 3. **Reader Testing**: Test the doc with a fresh Claude (no context) to catch blind spots before others read it

> 1. What type of document is this? (e.g., technical spec, decision doc, proposal)
> 2. Who's the primary audience?
> 3. What's the desired impact when someone reads this?
> 4. Is there a template or specific format to follow?
> 5. Any other constraints or context to know?

> 1. Clarifying questions will be asked about what to include
> 2. 5-20 options will be brainstormed
> 3. User will indicate what to keep/remove/combine

> If user doesn't know what sections they need:
> Based on the type of document and template, suggest 3-5 sections appropriate for the doc type.

> ### Quality Checking
>
> After 3 consecutive iterations with no substantial changes, ask if anything can be removed without losing important information.

> Generate 5-10 questions that readers would realistically ask.
> [...]
> For each question, invoke a sub-agent with just the document content and the question.
>
> Summarize what Reader Claude got right/wrong for each question.
> [...]
> Invoke sub-agent to check for ambiguity, false assumptions, contradictions.

> When Reader Claude consistently answers questions correctly and doesn't surface new gaps or ambiguities, the doc is ready.

> - Use appendices to provide depth without bloating the main doc

> - If user wants to skip a stage: Ask if they want to skip this and write freeform

## Collector's note

A long, command-like workflow skill (offered, then opt-in) for drafting specs, proposals and decision docs in three stages, ending in "Reader Testing": a context-free subagent answers predicted reader questions from the doc alone. That reader test is a reusable, per-document self-check pattern cardigan could borrow (e.g. "can a reader act on this in one read?"). The skill tends to add process (5–10 questions per section, 5–20 brainstorm options), and its only subtraction step is asking "if anything can be removed" after three stable iterations. It never asks whether the doc is needed at all. No repo-level evals or benchmarks.
