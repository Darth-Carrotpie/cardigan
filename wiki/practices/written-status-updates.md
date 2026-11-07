# Written status updates

> Sources: Jason Fried / 37signals, 2021-12-20; Tim Hickle / The Parasocial Worker, 2023-03-28; Khan Academy engineering, undated; Anthropic (knowledge-work-plugins), 2026-03-13; Anthropic (anthropics/skills, internal-comms), 2026-04-20
> Raw: [Khan/snippets (README)](../../raw/research/practices/khan-academy-weekly-snippets-readme.md); [What's in a Heartbeat?](../../raw/research/office-waste/2021-12-20-jason-fried-whats-in-a-heartbeat.md); [A Quick and Easy Slack Hack to Augment My Team's Daily Standup](../../raw/research/native-features/2023-03-28-slack-standup-workflow-practitioner.md); [Anthropic knowledge-work-plugins: status-report and stakeholder-update](../../raw/research/agent-skills/2026-03-13-anthropic-knowledge-work-plugins-status-skills.md); [Anthropic skills: internal-comms](../../raw/research/agent-skills/2026-04-20-anthropic-internal-comms-skill.md)
> Updated: 2026-10-31

## Overview

A short written update can replace a status meeting. Two operator models set the size and cadence: Khan Academy's open-source "snippets" tool, a clone of a Google internal system, asks for about four short bullets a week in a plain textbox; Basecamp's "Heartbeats" are one longer written summary per team every six-week cycle, posted where the whole company can read them. Both are the organisations' own accounts, with no independent evidence of readership.

## Weekly snippets

The README (repo; Khan Academy's own tool documentation) defines the form: "A weekly snippet is an (ideally) brief description of what you did the last week." It sets the size by the input box: "the snippet-entry textbox is sized for 4 bullet-point entries, each 80 characters or less."

It lists several purposes, the first being to replace a meeting: "Instead of a weekly standup or other meeting where everyone shares what they've done in the last week". Others: "Managers can read snippets of their direct reports to make better use of 1-on-1 meetings", and colleagues can spot where they can help ("serendipidous helping", spelled so in the README).

The tool deliberately has no structure: "Filling out a snippet involves writing into a textbox: no fields or text editors or other barriers to productivity."

## Heartbeats: low frequency, open to all

Jason Fried (practitioner; 37signals CEO describing his own company) ties the practice to Basecamp's meeting habits: "We're famous for having very few meetings at Basecamp." What replaces them is "Writing. Long-form, complete-thought, considered writing." The status form is the Heartbeat: "A Heartbeat summarizes all the work the team did over the last 6-week cycle." It is "published to a message board in a Basecamp project called "What Works"", and "Everyone in the company can see this project, and can read every Heartbeat." Its stated purpose goes beyond reporting: "It's a way to celebrate progress, recognize contributions, and detail the sheer quantity of work".

The two models differ in cadence and length (weekly bullets vs. a per-cycle summary) but share the shape: written once, posted in one place, read when needed rather than presented live.

## In the chat tool

Chat tools ship the weekly-or-daily prompt as a built-in workflow. Tim Hickle (practitioner) used Slack's standup template to move "the bulk of the communication" in his team's standup into an async message, while keeping a shorter live standup rather than cancelling it. See [Status updates and standups](../native-features/status-and-standups.md) for the native features and their caveats.

## Agent-skill templates go the other way

Anthropic's status-report agent skill (repo) fills a fixed eight-heading leadership template (summary, green/yellow/red status, metrics, accomplishments, in progress, risks, decisions needed, next priorities) whatever the period held, and its stakeholder-update skill can turn the same progress into "exec-brief, engineering-detail, or customer-facing versions". Both share the practitioners' order ("Lead with the conclusion, not the journey") and cap the executive version ("Keep it under 300 words."), but not their small, fixed size. See [Office workflow skills](../agent-skills/office-workflow-skills.md#status-reports-and-stakeholder-updates).

Anthropic's internal-comms skill (repo) carries a compact counter-model, the "3P" update ("Progress, Plans, Problems"): a header line, then "no more than 1-3 sentences" per section, sized as "something you can read in 30-60sec or less". It is the agent-skill version of a snippet.

## For cardigan

Interpretation, not source claims:

- Default weekly-update template: up to four bullets, each one line. Longer status reports need a reason (a decision needed, a risk, a changed deadline).
- When a user asks to prepare for or run a status standup, cardigan can offer written snippets as the replacement, with the meeting kept only for discussion items.
- A changed deadline or a blocker goes first in the bullets, never buried (see [BLUF](bluf.md)).
- Cadence follows the work cycle, not the calendar habit. When nothing decision-relevant changes week to week, cardigan can propose a less frequent written summary (per cycle or milestone) over a weekly one.
- Post once where everyone can find it (a channel, a project board) rather than sending the same update to several audiences.
- No form fields: a plain textbox convention suggests cardigan should not invent elaborate status templates.

## See Also

- [Status updates and standups](../native-features/status-and-standups.md)
- [One-on-ones](one-on-ones.md)
- [Meeting purges](../office-waste/meeting-purges.md)
- [Async-first communication](async-first.md)
- [Bottom Line Up Front (BLUF)](bluf.md)
- [Office workflow skills](../agent-skills/office-workflow-skills.md)
