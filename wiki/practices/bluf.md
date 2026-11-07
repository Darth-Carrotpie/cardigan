# Bottom Line Up Front (BLUF)

> Sources: Merlin Mann, 2005-09-19; Matthew Ström-Awn, 2020-05-17; Microsoft WorkLab, 2025-06-17; Bryan A. Garner / ABA Journal, 2026-01-27; Jason Fried / 37signals, undated; Barbara Minto / Minto Books International, undated; surendranb (writing-skills, business-writing), 2026-08-14; blader (humanizer v3.1.0, README, issue #229), 2026-10-28
> Raw: [Writing sensible email messages](../../raw/research/practices/2005-09-19-merlin-mann-writing-sensible-email-messages.md); [Should the bottom line be up front? Only with context](../../raw/research/practices/2026-01-27-garner-bluf-only-with-context.md); [How we communicate](../../raw/research/practices/37signals-how-we-communicate.md); [Bottom Line Up Front: write to make decisions faster](../../raw/research/practices/stroem-bluf-write-to-make-decisions-faster.md); [Bottom Line Up Front (review-practice copy, dated)](../../raw/research/review-practice/2020-05-17-strom-bottom-line-up-front.md); [Breaking Down the Infinite Workday](../../raw/research/office-waste/2025-06-17-microsoft-wti-breaking-down-infinite-workday.md); [The Minto Pyramid Principle: Concept / Course](../../raw/research/review-practice/minto-pyramid-principle-concept-and-course.md); [writing-skills: business-writing (BLUF)](../../raw/research/agent-skills/2026-08-14-writing-skills-business-writing-bluf.md); [Humanizer: remove AI writing patterns](../../raw/research/agent-skills/2026-10-28-humanizer-ai-writing-skill.md)
> Updated: 2026-10-31

## Overview

Put the ask, the decision or the deadline in the first lines of a message so the reader can act without reading further. Practitioner sources agree on the core move for asks and status: say what you want and by when, at the top. The bottom line is the decision or ask, not a summary. For analysis, a legal-writing authority argues the problem must come before the answer.

## Ask and deadline first

Merlin Mann (practitioner, 43 Folders) frames every business email as one of three types: "Providing information [...] Requesting information [...] Requesting action". The reader should be able to tell which type it is: "don't bury the lede." Any request goes "near the top of the message" with a clear statement of "when you will need it."

He names the failure this prevents, a changed deadline lost in a long status update:

> how many minutes have you wasted panning through a sloppy "project update" email only to completely miss the changed deadline or work request buried in the penultimate paragraph?

His working assumption is harsh: "assume that no one will ever read more than the first sentence of anything you write." Before writing at all, he wants two answers: "Why am I writing this? What exactly do I want the result of this message to be?" When an old thread is revived, context goes "right at the opening."

Twenty years later, Microsoft's telemetry (vendor-data, 2025) gives the assumption a number: "The average worker receives 117 emails daily—most of them skimmed in under 60 seconds." See [Message overload](../office-waste/message-overload.md).

37signals' guide (practitioner) adds the companion rule: "If you want an answer, you have to ask a question." An update with an implied ask is not an ask.

## The bottom line is a decision, not a summary

Matthew Ström-Awn's essay (practitioner) traces BLUF to US Army correspondence rules (Army Regulation 25-50 per the dated copy's byline; the regulation itself was not fetched), quoting a requirement of "putting the main point at the beginning of the correspondence (bottom line up front)". He defines the bottom line narrowly: its purpose "is to capture the decisive moment of your argument," and "The bottom line is not a summary." The payoff is speed: putting it first "allows your reader to make a decision much faster."

The military sources he quotes are less absolute than the acronym suggests. A second guide he quotes (an Air Force handbook, per the byline) says "get your bottom line up front (most of the time)", and the Army rule pairs it with active voice: "Army writing will be concise, organized, and to the point." He also quotes a memo complaining about long papers (attributed to Churchill in the collector's note): "Nearly all of them are far too long", and "the discipline of setting out the real points concisely will prove an aid to clear thinking."

He also names the risks. "Being direct and getting straight to the point isn't always the right approach. If you know your audience is already skeptical, putting the bottom line up front may cause the reader to ignore everything that comes after it." A short opening carries weight: "Without context, any ambiguity is subject to misinterpretation." And the relationship matters: "If you typically communicate in a more conversational style, your colleagues might interpret your brevity as sudden coldness. If you're already at a disadvantage due to office politics, gender bias, or cultural stereotypes, BLUF might not be the right approach."

## The governing thought answers the reader's question

Barbara Minto's Pyramid Principle (practitioner; her own site, describing a course "based on a similar course she developed and taught for several years at McKinsey & Company") gives BLUF a structure underneath. Thinking "ends in a single pyramid of ideas, at many levels, obeying logical rules, and held together by a single thought", and "Communicating the thinking requires only that you guide the reader down the pyramid." The first step is to "identify the reader's question", then organise "the points needed to answer that question". Minto claims it fits "email, 1-page memo, multi-page report, or formal slide presentation."

Her test for supporting points is that a grouping must produce an insight, not a label: check that "when you say "There are three reasons for making this change," there are in fact only three reasons", and that "you have drawn the appropriate insight from having identified them. ("There are three reasons" is not an appropriate insight!)" Recommendations should be presented "so that they provoke action and lead to change."

## BLUF as an agent rule

A business-writing agent skill (repo; surendranb's writing-skills) turns the practice into checkable steps: `one sentence: the verdict or the ask` → `2–4 supporting facts with numbers` → `one sentence: what you need or what happens next` → `delete everything else`, verified by "The first sentence contains the point" and "One explicit ask, stated as a verb + deadline". It shares Mann's assumption ("Executives read the first sentence; if it does not contain the answer, the rest may never be read") and none of Ström-Awn's or Garner's caveats. The humanizer skill (repo) applies the same order to replies: "Lead with the decision and keep only the reasoning that would change whether the reader agrees: usually one fact they lack and any link they need to act", because "In a reply the reader already has the context, so rebuilding it adds nothing and buries the point." See [Prose-style skills](../agent-skills/prose-style-skills.md#business-writing-bluf-as-a-skill).

## When the answer needs the problem first

Bryan Garner (practitioner; legal-writing authority, ABA Journal column) accepts BLUF where the bottom line is a discrete call: "In the military world, "bottom line up front" is genuinely helpful." But "the usefulness of BLUF depends on understanding what the true bottom line is", and in legal analysis it "can short-circuit the essential work of problem-framing" and "can produce empty, conclusory openings that rush to "We win."" His alternative: "the wiser priority is not "bottom line up front" but "problem first, answer next."" Because "Only when the problem is clearly in view does any bottom line become truly comprehensible."

> **Status: Disputed**
> Mann (43 Folders, 2005) puts the request at the top and assumes "no one will ever read more than the first sentence". Garner (ABA Journal, 2026) argues that for analytical writing the order should be "problem first, answer next", because a bottom line without its problem is not comprehensible. Both are practitioner views. They conflict mainly in scope: Mann writes about routine business email, Garner about memos and briefs.

## For cardigan

Interpretation, not source claims:

- When cardigan drafts a message, the first line carries the ask or decision plus its deadline. A TL;DR that restates content is not a bottom line, and a buried deadline is a defect, not a style choice.
- *What result do I want from this message?* and *what question is the reader asking?* (Minto) are cheap pre-draft gates, and classifying the message (inform / request info / request action) picks its shape. No answer to the gates may mean the right output is nothing.
- BLUF for asks, decisions and status. For analysis, for a skeptical reader, or when the reader does not yet share the problem, cardigan opens with a one-line problem statement and then the answer. If the user normally writes conversationally, a sudden BLUF can read as cold, so cardigan keeps the user's usual register around the bottom line.
- BLUF moves facts; it never deletes them. Because readers may stop after the first line (Ström-Awn's warning), anything they must not miss (a caveat, a compliance condition, a deadline) belongs in or right next to that line.
- Leading with the ask is not dropping the greeting or the reason. Short, impersonal messages from someone with more power are the ones most often misread as negative (see [Short messages](short-messages.md#brevity-and-tone)), so the courtesy clause stays.

## See Also

- [Short messages](short-messages.md)
- [Threads and forwarding](threads-and-forwarding.md)
- [Writing for skimmers](writing-for-skimmers.md)
- [Message overload](../office-waste/message-overload.md)
- [Prose-style skills](../agent-skills/prose-style-skills.md)
