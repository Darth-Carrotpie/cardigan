# Status updates and standups

> Sources: Tim Hickle / The Parasocial Worker, 2023-03-28; Slack (features page), undated; Slack (resources page), undated; Anthropic (knowledge-work-plugins), 2026-03-13
> Raw: [A Quick and Easy Slack Hack to Augment My Team's Daily Standup](../../raw/research/native-features/2023-03-28-slack-standup-workflow-practitioner.md); [Stay aligned and free up time with clips](../../raw/research/native-features/slack-clips.md); [Four simple ways to save time with Workflow Builder](../../raw/research/native-features/slack-workflow-builder-save-time.md); [Anthropic knowledge-work-plugins: status-report and stakeholder-update](../../raw/research/agent-skills/2026-03-13-anthropic-knowledge-work-plugins-status-skills.md)
> Updated: 2026-10-31

## Overview

The live status round (daily standup, weekly status meeting) can move into a built-in chat workflow: a scheduled prompt collects each person's update as a message, and people read it before or instead of meeting. The evidence is one manager's practitioner account of Slack's standup template; its benefits are anticipated, not measured, and it shrinks the meeting rather than removing it. The same move applies to walkthrough and show-and-tell meetings: a recorded clip with a transcript, which Slack's marketing page (vendor data) offers on every plan.

| Manual deliverable | Native feature (tool) | Plan/licence caveat |
|---|---|---|
| Spoken round of updates in a daily standup or status meeting | Standup workflow with scheduled prompts and forms (Slack Workflow Builder) | Not stated in either source; the collector reports Workflow Builder is paid-plan and admin-restrictable |
| Walkthrough meeting or long written explainer | Audio, video and screen-recording clips with captions and transcript (Slack) | All plans, free included, per Slack |

## Async standup, shorter meeting

Tim Hickle (practitioner; a manager describing his own team) sets the goal: "We want to take the bulk of the communication that happens during our existing standups and turn it into an asynchronous Slack message." He did not have to build anything: "Slack has already set up a template for it in its workflow builder," and the team "could leverage Slack forms".

His diagnosis of the live round: "people are too busy worrying about what they're going to say!" and "there was little or no discussion or engagement". The fix is reading ahead: "By sharing our updates asynchronously ahead of time, our team can review others' standup notes beforehand".

The meeting survives in smaller form. The stated aim is "replacing the bulk of our standup with async communication", not all of it, and the leftover time is social: "We can spend the first 5 minutes of a 15-minute standup on small talk". The claimed upside ("could supercharge the efficacy of your team's daily touch-base") is a hope, not a result.

Slack's own resources page (vendor-data; marketing, undated) goes further: "With a standup workflow, you can cancel status update meetings and move them into Slack." The mechanism is a schedule: "Automated prompts remind teammates to provide quick updates each day or week".

> **Status: Disputed**
> Slack's marketing (vendor-data) says a standup workflow lets you "cancel status update meetings and move them into Slack". Hickle (practitioner), using the same template, keeps a shorter live standup and aims at "replacing the bulk of our standup", not all of it. A third, conditional view comes from Anthropic's stakeholder-update agent skill (repo): "Keep it to 15 minutes" and "Cancel standup if there is nothing to sync on." None offers measured results.

## Walkthroughs: a clip instead of a meeting

Slack's clips page (vendor-data; marketing, undated) pitches the swap directly: "Record and send audio or video clips for a convenient way to share information without needing to meet." and "Rather than trying to get everyone together at the same time, post an audio or video clip instead." For demos: "Share your screen in a video clip—perfect for walking someone through a project." Viewers can "follow along with captions or quickly skim the transcript".

The page claims a "reduction in scheduled meetings among teams that use clips"; that is vendor data, and the size of the effect is not reproduced here. Availability is the broadest of any feature in this wiki: "All Slack plans—including paid and free versions—offer unlimited use of audio and video clips."

## For cardigan

Interpretation, not source claims:

- When a user asks to run, prep or "fix" a standup, the first rung is the chat tool's built-in standup workflow, not a hand-built status template or a new bot.
- Default to shrinking, not deleting: async updates plus a short live slot for blockers and social contact. Removing the meeting entirely is a separate decision the team makes.
- The update itself follows the [written status updates](../practices/written-status-updates.md) shape: a few one-line bullets, blockers and changed deadlines first.
- For a one-way walkthrough (a demo, an explanation of a new process), cardigan suggests a short screen clip over a meeting or a long doc, plus a two-line written summary with the ask, since not everyone will watch it.
- Evals should not credit the swap as proven time-saving; the standup source is a single anticipatory account and the clips figure is vendor marketing.

## See Also

- [Written status updates](../practices/written-status-updates.md)
- [Meeting purges](../office-waste/meeting-purges.md)
- [Async-first communication](../practices/async-first.md)
- [Office workflow skills](../agent-skills/office-workflow-skills.md)
