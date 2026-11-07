# Office workflow skills

> Sources: Anthropic (anthropics/skills, doc-coauthoring), 2025-12-04; Notion Labs (OpenAI Codex skills catalog, notion-meeting-intelligence), 2026-02-02; Anthropic (knowledge-work-plugins), 2026-03-13; Anthropic (anthropics/skills, internal-comms), 2026-04-20; Anthropic (anthropics/skills, discernment-nudge), 2026-08-17; Alireza Rezvani (claude-skills, inbox-triage), 2026-10-30
> Raw: [Anthropic skills: doc-coauthoring](../../raw/research/agent-skills/2025-12-04-anthropic-doc-coauthoring-skill.md); [notion-meeting-intelligence](../../raw/research/agent-skills/2026-02-02-openai-notion-meeting-intelligence-skill.md); [Anthropic knowledge-work-plugins: status-report and stakeholder-update](../../raw/research/agent-skills/2026-03-13-anthropic-knowledge-work-plugins-status-skills.md); [Anthropic skills: internal-comms](../../raw/research/agent-skills/2026-04-20-anthropic-internal-comms-skill.md); [Anthropic skills: discernment-nudge](../../raw/research/agent-skills/2026-08-17-anthropic-discernment-nudge-skill.md); [inbox-triage (alirezarezvani/claude-skills)](../../raw/research/agent-skills/2026-10-30-inbox-triage-drafts-only-skill.md)
> Updated: 2026-10-31

## Overview

Published agent skills for office work are mostly workflow and template skills: once a document is requested, they structure how it gets drafted. Anthropic's doc-coauthoring skill (repo; the skill file itself) runs a three-stage workflow for specs, proposals and decision docs and ends with a test by a context-free reader. Its process tends to add steps, and its only subtraction step comes late. Notion's meeting-prep skill for Codex writes agendas and pre-reads, and its shipped evals reward more output rather than less. Anthropic's status-report and stakeholder-update skills fill fixed templates however much happened. Anthropic's internal-comms skill is a small router to house formats, including a strict three-line status update. The exception is Anthropic's discernment-nudge, an add-on whose main content is when to stay silent. A community inbox-triage skill makes a real per-email "draft or not" call, but produces a full report every run.

## Doc co-authoring: a three-stage workflow

The skill triggers "when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content." Its stages are:

1. "**Context Gathering**: User provides all relevant context while Claude asks clarifying questions"
2. "**Refinement & Structure**: Iteratively build each section through brainstorming and editing"
3. "**Reader Testing**: Test the doc with a fresh Claude (no context) to catch blind spots before others read it"

Context gathering opens with five questions, including "Who's the primary audience?" and "What's the desired impact when someone reads this?". Each section then gets clarifying questions and "5-20 options will be brainstormed", which the user trims ("keep/remove/combine"). A user who does not know the structure gets "3-5 sections appropriate for the doc type."

Subtraction appears twice. A quality check fires late: "After 3 consecutive iterations with no substantial changes, ask if anything can be removed without losing important information." And depth goes out of the main text: "Use appendices to provide depth without bloating the main doc". In the excerpts, no step asks whether the document should exist; the audience and impact questions come closest. Users can step out ("Ask if they want to skip this and write freeform").

## Reader testing

The last stage is a reusable self-check. The skill tells Claude to "Generate 5-10 questions that readers would realistically ask", then "invoke a sub-agent with just the document content and the question", summarise "what Reader Claude got right/wrong", and run a further sub-agent check "for ambiguity, false assumptions, contradictions." The stop rule: "When Reader Claude consistently answers questions correctly and doesn't surface new gaps or ambiguities, the doc is ready." No evals or results ship with the skill.

## Meeting prep: agenda and pre-read

The notion-meeting-intelligence skill (repo; by Notion Labs, distributed in OpenAI's Codex skills catalog, which is marked deprecated) is for "drafting agendas/pre-reads, and tailoring materials to attendees." Its first step is a gate in form only: "Confirm meeting goal, attendees, date/time, and decisions needed." It then searches Notion, picks one of six templates "(status, decision, planning, retro, 1:1, brainstorming)", drafts the pages "embedding source links and owner/timeboxes", and enriches them with research. Two rules discipline the content: "Add concise Codex research where helpful" and "Keep claims cited with source links; separate fact from opinion."

### Its evals reward more

Unusually, the skill ships evaluation scenarios. The README says they check that it "Creates both internal pre-reads and external agendas", "Distinguishes between Notion facts and Codex insights" and "Works consistently across Haiku, Sonnet, and Opus"; the procedure is manual ("Verify the skill searches Notion first (not Codex research)"). The sample scenario's query does ask for two documents ("Create both an internal pre-read for the team and an agenda for the meeting."), so "TWO documents are created (internal pre-read + external agenda), not just one" follows the user's ask. But other criteria reward volume: the pre-read must be "comprehensive with: Notion context + Codex insights + detailed pros/cons + recommendation", and "Codex enrichment is present and adds value". No criterion checks whether the research, or the meeting, is needed, and no results are published. See [Guard metrics](../skill-evals/guard-metrics.md).

## Status reports and stakeholder updates

Anthropic's knowledge-work-plugins (repo) are role bundles: "Each plugin bundles the skills, connectors, slash commands, and sub-agents for a specific job function", built for Claude Cowork and "also compatible with" Claude Code. The README expects customisation: "The real power comes when you customize them for your company".

The status-report skill takes an `argument-hint` of "[weekly | monthly | quarterly] [project or team]", so it doubles as a slash command. It fills one template with eight headings: Executive Summary ("3-4 sentence overview"), Overall Status (green/yellow/red), Key Metrics, Accomplishments This Period, In Progress, Risks and Issues, Decisions Needed, Next Period Priorities. Brevity is a tip, not a structure: "**Lead with the headline** — Busy leaders read the first 3 lines. Make them count." Two other tips carry substance: "**Be honest about risks** — Surfacing issues early builds trust. Surprises erode it." and "For each decision needed, provide context and a recommendation."

The stakeholder-update skill multiplies audiences: it covers "translating the same progress into exec-brief, engineering-detail, or customer-facing versions." Its executive version has a length cap ("Keep it under 300 words.") and a BLUF rule: "Lead with the conclusion, not the journey. Executives want "we shipped X and it moved Y metric" not "we had 14 standups and resolved 23 tickets."" The only rule found in either skill about not producing something sits in a standup-facilitation section: "Cancel standup if there is nothing to sync on. Respect people's time." No evals ship for these skills.

## Internal comms: a router to house formats

Anthropic's internal-comms skill (repo) is a short router. Its description reads "A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use", written in the first person, which Anthropic's own authoring guide advises against (see [Skill authoring guidance](skill-authoring-guidance.md)). It picks one of four guideline files by type (3P updates, company newsletter, FAQ answers, general comms). Its only gate is format: "If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format."

The 3P format is the tightest office template surveyed. "3P updates stand for "Progress, Plans, Problems."" They should be "very succinct and to-the-point: think something you can read in 30-60sec or less", in a fixed shape ("The format is always the same, very strict formatting."): a header line with a team name and dates, then one line each for Progress, Plans and Problems. "Each section should be no more than 1-3 sentences: clear, to the point. It should be data-driven, and generally include metrics where possible." The header asks for an emoji: "Pick an emoji that is fun and captures the vibe of the team and update." The gathering step pulls the other way: "Try to gather as much context as you can".

The general-comms file asks before drafting: "Ask the user about their target audience", "Understand the communication's purpose", "Clarify the desired tone (formal, casual, urgent, informational)". Its principles are short: "Be clear and concise", "Use active voice", "Put the most important information first". No evals ship with the skill.

## Discernment nudge: silence as the default

Anthropic's discernment-nudge (repo) attaches to replies, not documents. Its description, which carries the whole trigger and skip logic, tells the model to "invoke this skill BEFORE finalizing your reply" after a substantive answer or draft (advice, plans, proposals, emails, estimates, analysis), and then, if it applies, to "append 2-3 short follow-up questions", each tied to something specific in the reply. It caps itself: "Do this at most once per conversation."

Most of the body is about not adding output. "Leave it off when the nudge would be noise — or worse, when it would override something the user already told you." "Silence is the right default". Skip cases include a user who asked for the quick version ("A nudge overrides that preference, which lands as paternalistic. Respect the ask; give them what they asked for and stop.") and a user who supplied the material ("they have the source and they're the judge of whether you matched it."; "If you're unsure your summary is faithful, say so in the answer."). Repeating the nudge "turns a light suggestion into nagging."

The output shape is fixed and small: "Two or three prompts, never more. Keep each under ~120 characters so it reads at a glance." The answer comes first ("Always answer the question completely first. The nudge comes after, and it should be easy to skip."), introduced by the exact line "A few things worth a second look:", with no trailing offer: "Don't add anything after the nudge — no "let me know if you'd like me to dig into any of these." The nudge is the closer." It does not question whether the drafted plan or email should exist, and no evals ship with it.

## Inbox triage: drafts it never sends

The inbox-triage skill (repo; Alireza Rezvani's claude-skills, version 1.0.0) "Classifies recent mail with the inbox-setup knowledge base, drafts replies it never sends (checked by draft_safety_validator.py) and reports." It runs "on a recurring schedule (1–3x daily) or on demand", depends on a separate setup skill's knowledge base, and keeps intake light: "Default invocations skip both questions and run with KB-default preferences."

The never-send rule is enforced by code, not by prompt: a validator script (`scripts/draft_safety_validator.py`) "enforces it post-run. Any send-shaped tool call in the action log fails validation."

It is the one surveyed office skill that decides per item whether to produce anything. Each email lands in one of four categories (TAKE IT, WORTH CONSIDERING, PASS, FLAG FOR REVIEW); PASS gets a "Brief "why" (1–3 sentences); draft polite decline", and FLAG FOR REVIEW gets "Surface fully; NO draft (user decides response shape)". It does not draft for "Clearly no-response emails (newsletters, automation, FYI)", "Threads where user already replied", or "Blocked senders (unless new info changes the calculus)". For low-priority mail it does not even read the thread: "skip thread reads entirely — context cost not worth it." Its tie-breaker: "When unsure, flag for review. A wrong auto-draft is worse than no draft."

The run-level output does not get the same treatment. Every run produces a six-section report (overview, stats, action needed, quick reference, detailed cards, footer), and "Even with zero new emails" it still generates a "minimal report: "No new actionable emails since last run"". It avoids one duplicate: "drafts are already in email client for user to read there", so the report has no draft previews. Its proposed learning signal is behavioural: "Drafts sent as-is vs. edited vs. deleted → tone calibration signal" and "PASS recommendations user overrides → framework adjustment signal". No benchmark is published.

## For cardigan

Interpretation, not source claims:

- Put the existence gate at the start, where these skills already collect the inputs: no nameable impact for a doc (doc-coauthoring's "desired impact") or no "decisions needed" for a meeting means cardigan proposes no doc, or an async update instead of an agenda, before any brainstorm or template.
- Apply inbox-triage's per-item "whether" call one level up: no draft for FYI mail, threads the user already answered, or when unsure; and an empty run or a status period with nothing decision-relevant gets one line or nothing, not a six-section report or eight template headings.
- discernment-nudge is the closest structural model for cardigan: always in context through its description, silence by default, explicit skip conditions, a frequency cap, a small fixed output shape, no trailing offer. Overriding a user's request for the quick version reads as paternalistic, so that preference is a social rule, not only a length rule.
- Use the user's house format (such as 3P) rather than a cardigan template, treating its caps as a ceiling; keep the strong template rules (headline first, honest risks, a recommendation with each decision) and post one update once rather than several audience versions.
- Draft, never send, and enforce it in code where the host allows (inbox-triage's validator). Evals should be the inverse of Notion's (credit one sufficient document, penalise unrequested enrichment, include cases where the right output is nothing), use a context-free reader test for high-stakes documents, and track drafts sent as-is vs edited vs deleted.

## See Also

- [Reviewing a draft](../review-practice/reviewing-drafts.md)
- [Proportional review](../review-practice/proportional-review.md)
