# Anthropic knowledge-work-plugins: status-report and stakeholder-update skills

> Source: https://github.com/anthropics/knowledge-work-plugins/blob/main/operations/skills/status-report/SKILL.md (also https://github.com/anthropics/knowledge-work-plugins/blob/main/README.md and https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/stakeholder-update/SKILL.md)
> Collected: 2026-10-31
> Published: 2026-03-13 (last commit to both skill folders)
> Author: Anthropic
> Type: repo

## Excerpts

https://github.com/anthropics/knowledge-work-plugins/blob/main/README.md (Apache-2.0):

> Plugins that turn Claude into a specialist for your role, team, and company. Built for [Claude Cowork](https://claude.com/product/cowork), also compatible with [Claude Code](https://claude.com/product/claude-code).

> Each plugin bundles the skills, connectors, slash commands, and sub-agents for a specific job function. Out of the box, they give Claude a strong starting point for helping anyone in that role. The real power comes when you customize them for your company — your tools, your terminology, your processes — so Claude works like it was built for your team.

https://github.com/anthropics/knowledge-work-plugins/blob/main/operations/skills/status-report/SKILL.md:

> ---
> name: status-report
> description: Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health with green/yellow/red status, surfacing risks and decisions that need stakeholder attention, or turning a pile of project tracker activity into a readable narrative.
> argument-hint: "[weekly | monthly | quarterly] [project or team]"
> ---

> ### Executive Summary
> [3-4 sentence overview — what's on track, what needs attention, key wins]
>
> ### Overall Status: 🟢 On Track / 🟡 At Risk / 🔴 Off Track
>
> ### Key Metrics
> [...]
> ### Accomplishments This Period
> [...]
> ### In Progress
> [...]
> ### Risks and Issues
> [...]
> ### Decisions Needed
> [...]
> ### Next Period Priorities

> 1. **Lead with the headline** — Busy leaders read the first 3 lines. Make them count.
> 2. **Be honest about risks** — Surfacing issues early builds trust. Surprises erode it.
> 3. **Make decisions easy** — For each decision needed, provide context and a recommendation.

https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/stakeholder-update/SKILL.md:

> description: Generate a stakeholder update tailored to audience and cadence. Use when writing a weekly or monthly status for leadership, announcing a launch, escalating a risk or blocker, or translating the same progress into exec-brief, engineering-detail, or customer-facing versions.

> **For executives**: TL;DR, status color (G/Y/R), key progress tied to goals, decisions made, risks with mitigation, specific asks, and next milestones. Keep it under 300 words.

> - Lead with the conclusion, not the journey. Executives want "we shipped X and it moved Y metric" not "we had 14 standups and resolved 23 tickets."

> - Keep it to 15 minutes. If discussions emerge, take them offline.
> - Focus on blockers — this is the highest-value part of standup
> - Track blockers and follow up on resolution
> - Cancel standup if there is nothing to sync on. Respect people's time.

## Collector's note

Anthropic's official office-work plugin marketplace (11 role plugins, built for Cowork, also usable in Claude Code); skills double as slash commands with `argument-hint`. These two skills are template generators: status-report fixes eight sections (summary, RAG status, KPI table, wins, in-progress table, risks, decisions, priorities) regardless of how much happened, and stakeholder-update can produce several audience versions of the same progress. Brevity appears as tips ("Lead with the headline", "under 300 words"); the one "whether" rule found is buried in a facilitation section ("Cancel standup if there is nothing to sync on"). No evals or benchmarks ship in the repo for these skills.
