# Anthropic skills: internal-comms

> Source: https://github.com/anthropics/skills/blob/main/skills/internal-comms/SKILL.md (also https://github.com/anthropics/skills/blob/main/skills/internal-comms/examples/3p-updates.md and https://github.com/anthropics/skills/blob/main/skills/internal-comms/examples/general-comms.md)
> Collected: 2026-10-31
> Published: 2026-04-20 (last commit to the skill folder)
> Author: Anthropic
> Type: repo

## Excerpts

https://github.com/anthropics/skills/blob/main/skills/internal-comms/SKILL.md (Apache-2.0):

> ---
> name: internal-comms
> description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).
> license: Complete terms in LICENSE.txt
> ---

> To write any internal communication:
>
> 1. **Identify the communication type** from the request
> 2. **Load the appropriate guideline file** from the `examples/` directory:
>     - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
>     - `examples/company-newsletter.md` - For company-wide newsletters
>     - `examples/faq-answers.md` - For answering frequently asked questions
>     - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
> 3. **Follow the specific instructions** in that file for formatting, tone, and content gathering
>
> If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

https://github.com/anthropics/skills/blob/main/skills/internal-comms/examples/3p-updates.md:

> You are being asked to write a 3P update. 3P updates stand for "Progress, Plans, Problems." The main audience is for executives, leadership, other teammates, etc. They're meant to be very succinct and to-the-point: think something you can read in 30-60sec or less. They're also for people with some, but not a lot of context on what the team does.

> Try to gather as much context as you can, focusing on the things that covered the time period you're writing for:

> The format is always the same, very strict formatting. Never use any formatting other than this. Pick an emoji that is fun and captures the vibe of the team and update.
>
> [pick an emoji] [Team Name] (Dates Covered, usually a week)
> Progress: [1-3 sentences of content]
> Plans: [1-3 sentences of content]
> Problems: [1-3 sentences of content]
>
> Each section should be no more than 1-3 sentences: clear, to the point. It should be data-driven, and generally include metrics where possible.

https://github.com/anthropics/skills/blob/main/skills/internal-comms/examples/general-comms.md:

> Before proceeding:
> 1. Ask the user about their target audience
> 2. Understand the communication's purpose
> 3. Clarify the desired tone (formal, casual, urgent, informational)
> 4. Confirm any specific formatting requirements
>
> Use these general principles:
> - Be clear and concise
> - Use active voice
> - Put the most important information first

## Collector's note

A very short model-invoked router skill (~30 lines) that picks one of four format files by communication type; the 3P format caps each section at 1–3 sentences and a 30–60 second read. It governs format and length once a communication is requested; the only gate is "ask for clarification" when the type does not match. The description is written partly in first person ("help me write"), which Anthropic's own best-practices doc advises against. No evals or benchmarks ship with it; the repo itself shows no self-measurement beyond stars.
