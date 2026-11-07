# Meeting purges

> Sources: JR Minkel / Scientific American Mind, 2006-06-01; Longqi Yang et al. / Microsoft, 2020-07-30; Daniella Genovese / Fox Business, 2023-01-06; Andrea Hsu / NPR, 2023-02-15; Sheryl Estrada / Fortune, 2023-07-14; Claire Zillman / Fortune, 2026-02-01; Rebecca Hinds / Asana, undated; Jason Fried / 37signals, undated; GitLab Inc., undated; Khan Academy engineering, undated; Slack (features page), undated; Slack (resources page), undated
> Raw: [Shopify deleted 322,000 hours of meetings](../../raw/research/practices/2023-02-15-npr-shopify-deleted-322000-hours-of-meetings.md); [How we communicate](../../raw/research/practices/37signals-how-we-communicate.md); [GitLab Communication (The GitLab Handbook)](../../raw/research/practices/gitlab-handbook-communication.md); [Khan/snippets (README)](../../raw/research/practices/khan-academy-weekly-snippets-readme.md); [Meetings Are Great](../../raw/research/office-waste/2006-06-01-scientific-american-meetings-are-great.md); [How Work From Home Affects Collaboration](../../raw/research/office-waste/2020-07-30-yang-wfh-collaboration-natural-experiment-arxiv.md); [E-commerce giant cancels 76,500 hours of meetings in new year](../../raw/research/office-waste/2023-01-06-shopify-calendar-purge-memo-fox-business.md); [Shopify's CFO explains how its new meeting cost calculator works](../../raw/research/office-waste/2023-07-14-shopify-meeting-purge-results-fortune.md); [In the age of AI, better meetings might be your company's secret weapon](../../raw/research/office-waste/2026-02-01-fortune-better-meetings-secret-weapon-hinds.md); [Meetings are broken. It's time for a meeting doomsday.](../../raw/research/office-waste/meetings-are-broken-time-for-a-meeting-doomsday-asana.md); [Stay aligned and free up time with clips](../../raw/research/native-features/slack-clips.md); [Four simple ways to save time with Workflow Builder](../../raw/research/native-features/slack-workflow-builder-save-time.md)
> Updated: 2026-10-31

## Overview

A meeting purge deletes recurring meetings in bulk and makes people re-add only the ones they can justify. Shopify's January 2023 purge is the best-known case; Asana runs the same move as a "Meeting Doomsday" with a 48-hour wait and an explicit test (does this meeting beat async?). The reported savings are company claims, not independent measurement. Meeting researchers argue the target should be bad meetings, not meetings as such, and older survey evidence suggests a meeting's value depends on how much the attendee's work depends on others. The main failure modes are creep-back and displacement into chat.

## Shopify's purge

COO Kaz Nejatian's memo, as quoted by Fox Business (journalism) in January 2023, framed it as "useful subtraction; freeing ourselves from an absurd amount of meeting time", with lines such as "No one joined Shopify to sit in meetings." and "meetings are a bug along that journey". The memo called re-adding meetings a "no judgment zone". Fox's headline put the cut at 76,500 hours.

NPR's report (journalism) one month in describes the mechanics. "A bot went into everyone's calendars and purged all recurring meetings with three or more people, giving them that time back." Employees then had to "wait two weeks before adding anything back to their calendars and to be "really, really critical" about what they bring back", and keep Wednesdays free.

The reported outcomes are the company's own claims, made in interviews, not independent measurement:

- "We deleted 322,000 hours of meetings," said Nejatian to NPR, in "a company of about 10,000 employees, all remote."
- "Nejatian says 85% of employees are complying with their "No Meetings Wednesdays" policy."
- Saying no became acceptable: "People have been saying 'no' to meetings from me, and I'm the COO of the company. And that's great."

The headline numbers move between reports: 76,500 hours in the January Fox headline, 322,000 hours in NPR's February interview, and a Fortune headline in July about how the company will cut 474,000 events in 2023, a projection rather than a result. Fortune's interview with CFO Jeff Hoffmeister (journalism) gives the rationale ("Time is money, and it should be spent on helping our merchants succeed and not on unnecessary meetings") and a personal observation ("Yes, I've seen the number of meetings on my calendar decrease."), and admits "There is no hard and fast rule for the number of people included in meetings." The measured before/after reduction appears in that raw note only in the collector's paraphrase, so it is not quoted here. Shopify followed the one-time wipe with ongoing friction: the Fortune headline is about its new meeting cost calculator.

For context, NPR cites Microsoft data that "the amount of time the average Teams user spent in meetings more than tripled between February 2020 and February 2022".

> **Status: Disputed**
> Shopify's leadership presents the bulk purge as "useful subtraction" that gives time back (NPR, 2023-02-15, quoting the company memo and COO). Organizational psychologist Steven Rogelberg, quoted in the same article, holds that "meetings are not in and of themselves the problem. Bad meetings are." He lists the failure modes: "the agenda items are all recycled, there are way more people than necessary in attendance, one person dominates, and they stretch on and on", and NPR reports he "is not a fan of the Shopify-style meeting purge." A 2006 Scientific American Mind report on his earlier research (journalism, summarising a survey study) adds that meeting dissatisfaction depends on the attendee: people with little need for others' input "do indeed tend to be generally dissatisfied with meetings", unlike those "whose work depends on interaction with others". The disagreement is about the remedy (delete vs. fix, uniformly vs. per attendee), not about whether meeting load has grown.

## Asana's Meeting Doomsday

Rebecca Hinds (practitioner; head of Asana's Work Innovation Lab, writing about her own company's experiment, undated, originally in Inc.) describes a repeatable version: "have your team delete all their recurring meetings from their calendars." Then "sit with their newly cleansed calendars for 48 hours" and "repopulate their calendars, but only with those meetings that are valuable". The re-add test is one question:

> Did the meeting help advance your work forward more quickly than you would have been able to do asynchronously?

Her reported result: "participants saved an average of 11 hours per month", or "each individual saving 17 workdays over the course of a year." No counts of meetings deleted or re-added and no negative results are reported. Her diagnosis of why meetings needed cutting is decay, not original uselessness: "most of these meetings were once productive but had grown in size or scope and needed to be reevaluated." Many survivors came back smaller: "shorter, unconventional lengths (like 15 minutes)", and "less frequent".

She also names the social barrier: "Employees often feel that if they delete meetings, other attendees will take it as a personal affront."

In a 2026 Fortune interview (journalism), Hinds says "As knowledge workers, we spend 85 to 90% of our time collaborating," and "There's no activity that we spend more time on than meetings, and yet they're highly, highly dysfunctional." She criticises meetings that "orient around showing productivity through meetings, as opposed to actually designing the meeting to move things forward." The article mentions a company that "wiped recurring meetings from employees' calendars overnight," (Dropbox, per the collector's paraphrase). Per the same paraphrase, Hinds treats sending an AI notetaker as "a sign to me that the meeting has not been intentionally designed." The point that purged meetings creep back unless people feel free to decline is recorded only in the collector's note.

## Who meetings help

The Scientific American Mind piece (journalism, 2006; a news summary, not the paper) is the main counterweight here. Workers "whose work depends on interaction with others" are the ones for whom meetings are not a net cost, and the article quotes the view that "I think it's a social norm to complain about your meetings". Complaints about meetings are therefore weak evidence that a particular meeting is waste. The sample size and design are recorded only in the collector's note.

## Where cut meetings go

Cutting meetings does not delete the communication they carried. Microsoft's natural-experiment preprint (study; difference-in-differences on Microsoft employees) found that under work-from-home "instant messages were used more, whereas scheduled meetings were used less." See [Async-first communication](../practices/async-first.md) and [Meeting-free days](meeting-free-days.md), where displaced meetings pile onto other days.

## Meetings as a last resort

Async-first companies set the default before any purge is needed. 37signals' guide (practitioner): "Meetings are the last resort, not the first option." See [Async-first communication](../practices/async-first.md).

GitLab's handbook (official-docs) explains why: "Meetings are incredibly expensive since they require synchronous time." It requires that every meeting "has an agenda and is available for everyone to edit", so that "Team members can add thoughts to an agenda in advance of a meeting and understand what was discussed if they cannot attend." It prefers text to video: "written notes are more efficient to read and offer greater opportunities for async engagement".

Written status is the usual replacement for a status meeting. Khan Academy's snippets tool (repo) exists "Instead of a weekly standup or other meeting where everyone shares what they've done in the last week"; Basecamp uses a written summary once per six-week cycle. See [Written status updates](../practices/written-status-updates.md).

Chat tools now package the replacements. Slack's clips page (vendor-data) says "post an audio or video clip instead" of gathering everyone for a walkthrough, and its Workflow Builder page claims "you can cancel status update meetings and move them into Slack" with a standup workflow. See [Status updates and standups](../native-features/status-and-standups.md) for the native swaps and their plan caveats.

## Fixing instead of deleting

Rogelberg's alternative is to repair the meeting: "Meetings can be incredibly engaging, satisfying sources of inspiration and good decision making when they are conducted effectively." His failure list doubles as a checklist: fresh agenda items, only the people needed, balanced participation, a firm end. Asana's survivors (shorter, less frequent) show the fix and the purge working together. Short, frequent one-on-ones are the recurring meeting with the strongest case for keeping; see [One-on-ones](../practices/one-on-ones.md).

## For cardigan

Interpretation, not source claims:

- Recurring meetings are the first thing cardigan questions, with Asana's test as the default prompt: would this beat doing it async? If not, propose cancelling; if yes, propose the smallest version (fewer people, 15 minutes, lower cadence).
- Cancel, shrink and make-optional are all on the ladder. A meeting's value differs by attendee (Rogelberg via SA Mind), so *make it optional for you and send notes* is often better than cancelling for everyone.
- A cut meeting must not turn into a dozen chat messages. When cardigan replaces a meeting, it replaces it with one artifact (agenda doc, written update, decision record), not a thread.
- Company savings figures (322,000 hours, 76,500 hours, 11 hours per month) are self-reported and inconsistent across reports; cardigan's docs and evals should not cite them as measured savings.
- Deleting or declining a meeting is socially costly ("personal affront"; permission has to come from the top). cardigan offers a polite decline-with-alternative and a blame-free framing, never a bare decline, and leaves one-on-ones alone unless asked.

## See Also

- [Meeting-free days](meeting-free-days.md)
- [Written status updates](../practices/written-status-updates.md)
- [Status updates and standups](../native-features/status-and-standups.md)
- [Async-first communication](../practices/async-first.md)
- [One-on-ones](../practices/one-on-ones.md)
