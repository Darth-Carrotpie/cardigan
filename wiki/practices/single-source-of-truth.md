# Single source of truth

> Sources: GitLab Inc., undated; Jason Fried / 37signals, undated; Brie Wolfson, 2022-07-18
> Raw: [GitLab Communication (The GitLab Handbook)](../../raw/research/practices/gitlab-handbook-communication.md); [How we communicate](../../raw/research/practices/37signals-how-we-communicate.md); [What I Miss About Working at Stripe](../../raw/research/practices/2022-07-18-wolfson-what-i-miss-about-working-at-stripe.md)
> Updated: 2026-10-31

## Overview

Keep each fact in one findable place and point to it, instead of restating it in emails and chats. GitLab's handbook makes this an explicit rule: messages are not the source of truth, answers go into the handbook, and questions go to public channels so they are answered once. The same handbook warns that a bare link is not an answer: add context.

## Messages are not the record

GitLab's public handbook (official-docs; the company's own published policy) says: "The email or Slack message should not be the source of truth." For work items, "The issue description should be the **single source of truth**."

Answering once is the goal. When someone could not find an answer, "please immediately make a merge request to add it to the handbook in a place you have looked for it", "leading by example to ensure that question only needs to be answered once". Questions belong in the open: use "issues or public chat channels" (the handbook names a #questions channel) "instead of direct messages or one-on-one emails."

37signals' guide (practitioner) states the placement principle in one line: "Where you put something, and what you call it, matters." Stripe's former employee Brie Wolfson (practitioner) describes the broadcast version: "We were encouraged to write everything down and then share it to a Google Group".

## A link plus context

GitLab does not treat a link as a complete reply: "If you send a handbook link to someone as an answer to a question, consider adding some context". Its broader rule is "Use low-context communications by being explicit in your communications" and "Provide as much context as possible to avoid confusion."

## For cardigan

Interpretation, not source claims:

- When the answer already exists somewhere (a doc, a ticket, a wiki page), cardigan's default output is a link plus one line of context, not a restated answer.
- When the same question has come up before, the better output may be adding the answer to the shared doc and then linking it: answer once.
- Chat and email are not where decisions live; cardigan should point decisions and status to the system of record (ticket, doc, decision log).
- A bare link fails the never-cut test if the recipient needs to know which part matters or what to do; the context line carries the ask.

## See Also

- [Decision records](decision-records.md)
- [Writing culture](writing-culture.md)
- [Async-first communication](async-first.md)
- [Trackers and status tables](../native-features/trackers.md)
