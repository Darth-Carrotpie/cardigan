# notion-meeting-intelligence (OpenAI Codex curated skills)

> Source: https://github.com/openai/skills/blob/main/skills/.curated/notion-meeting-intelligence/SKILL.md (also https://github.com/openai/skills/blob/main/skills/.curated/notion-meeting-intelligence/evaluations/README.md and https://github.com/openai/skills/blob/main/skills/.curated/notion-meeting-intelligence/evaluations/decision-meeting-prep.json)
> Collected: 2026-10-31
> Published: 2026-02-02 (last commit to the skill folder; the openai/skills repo is now marked deprecated in favour of openai/plugins)
> Author: Notion Labs (MIT), distributed in OpenAI's Codex skills catalog
> Type: repo

## Excerpts

https://github.com/openai/skills/blob/main/skills/.curated/notion-meeting-intelligence/SKILL.md:

> ---
> name: notion-meeting-intelligence
> description: Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.
> metadata:
>   short-description: Prep meetings with Notion context and tailored agendas
> ---

> 1) Confirm meeting goal, attendees, date/time, and decisions needed.
> 2) Gather context: search with `Notion:notion-search`, then fetch with `Notion:notion-fetch` (prior notes, specs, OKRs, decisions).
> 3) Pick the right template via `reference/template-selection-guide.md` (status, decision, planning, retro, 1:1, brainstorming).
> 4) Draft agenda/pre-read in Notion with `Notion:notion-create-pages`, embedding source links and owner/timeboxes.
> 5) Enrich with Codex research (industry insights, benchmarks, risks) and update the page with `Notion:notion-update-page` as plans change.

> - Status/update → status template.
> - Decision/approval → decision template.
> [...]
> - Add concise Codex research where helpful: market/industry facts, benchmarks, risks, best practices.
> - Keep claims cited with source links; separate fact from opinion.

https://github.com/openai/skills/blob/main/skills/.curated/notion-meeting-intelligence/evaluations/README.md:

> These evaluations ensure the Meeting Intelligence skill:
> - Gathers context from Notion workspace
> - Enriches with Codex research appropriately
> - Creates both internal pre-reads and external agendas
> - Distinguishes between Notion facts and Codex insights
> - Works consistently across Haiku, Sonnet, and Opus

> 1. Enable the `meeting-intelligence` skill
> 2. Submit the query from the evaluation file
> 3. Verify the skill searches Notion first (not Codex research)
> 4. Check that TWO documents are created (internal + external)

https://github.com/openai/skills/blob/main/skills/.curated/notion-meeting-intelligence/evaluations/decision-meeting-prep.json:

> "query": "Prep for tomorrow's meeting where we need to decide on our database migration approach. Create both an internal pre-read for the team and an agenda for the meeting.",

> "success_criteria": [
>     "TWO documents are created (internal pre-read + external agenda), not just one",
>     "Internal pre-read is comprehensive with: Notion context + Codex insights + detailed pros/cons + recommendation",
>     [...]
>     "Codex enrichment is present and adds value (decision frameworks, migration best practices, risk patterns)",
>     [...]
>     "Documents are cross-linked (pre-read mentions agenda, agenda mentions pre-read)",

## Collector's note

A model-invoked meeting-prep skill for Codex that pulls Notion context, chooses one of six meeting templates, and writes agenda and pre-read pages. Unusually, it ships evaluation scenarios in the Anthropic-recommended JSON shape (query, expected_behavior, success_criteria), run manually across models. Those criteria reward *more* output ("TWO documents ... not just one", "comprehensive", enrichment "is present"), and nothing checks whether the meeting, the second document, or the research is needed, so it is a useful counter-example for how cardigan's own evals should be written. No quantitative results are published.
