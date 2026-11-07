# Async-first communication

> Sources: Matt Mullenweg, 2020-04-10; Longqi Yang et al. / Microsoft, 2020-07-30; Berkeley Haas Newsroom on Yang, Holtz et al., 2021-09-09; Amir Salihefendic / Doist, 2022-05-17; Jason Fried / 37signals, undated; GitLab Inc., undated
> Raw: [Distributed Work's Five Levels of Autonomy](../../raw/research/practices/2020-04-10-mullenweg-five-levels-of-autonomy.md); [What the heck is asynchronous communication anyway?](../../raw/research/practices/2022-05-17-doist-what-is-asynchronous-communication.md); [When everyone works remotely, communication and collaboration suffer](../../raw/research/practices/2021-09-09-yang-holtz-remote-work-collaboration-microsoft.md); [How we communicate](../../raw/research/practices/37signals-how-we-communicate.md); [GitLab Communication (The GitLab Handbook)](../../raw/research/practices/gitlab-handbook-communication.md); [How Work From Home Affects Collaboration](../../raw/research/office-waste/2020-07-30-yang-wfh-collaboration-natural-experiment-arxiv.md)
> Updated: 2026-10-31

## Overview

Async-first means written, non-immediate communication is the default and real-time meetings are the exception. Distributed-company leaders describe it as a maturity step beyond simply moving office habits online. Its admitted cost is slower decisions.

## Mullenweg's levels of autonomy

Matt Mullenweg (practitioner; Automattic CEO) describes a maturity model for distributed companies:

- At the bottom, a job "cannot be done unless you're physically there", and then remote work with "no deliberate effort to make things remote-friendly."
- Level 2 tries to "recreate what they were doing in the office in a "remote" setting", where "everything is still synchronous, your day is full of interruptions."
- At level 3 "you're really starting to benefit from being remote-first, or distributed", and "you realize just how crucial written communication is for your success." Meetings often have "a Google Doc up with the other meeting participants."
- Higher levels judge output, not presence ("You evaluate people's work on what they produce, not how or when they produce it"), and "Real-time meetings are respected and taken seriously, almost always have agendas."

He names the tradeoff openly: "better — perhaps slower, but more deliberate — decision-making."

## 37signals: async most of the time

Jason Fried's communication guide for 37signals (practitioner; Basecamp's own principles, undated) states the default as "Real-time sometimes, asynchronous most of the time." Several lines push against reflexive urgency: "The expectation of immediate response is toxic." "Communication shouldn't require schedule synchronization." "'Now' is often the wrong time to say what just popped into your head." "Urgency is overrated, ASAP is poison." And on placement: "Where you put something, and what you call it, matters."

The guide also guards against over-cutting: "Poor communication creates more work." "Communication is lossy, especially verbal communication." "Ask if things are clear." Its summary of the goal: "Saying the right thing at the right time in the right way with the fewest side effects."

## Doist: async as culture, with stated costs

Amir Salihefendic (practitioner; Doist CEO) defines the term simply: "asynchronous communication is when you send a message without expecting an immediate response." He insists it "isn't primarily about tools" but "about team culture and habits", and claims that under it "Deep work becomes the default" and "Documentation and greater transparency become automatic." His rule: "Synchronous communication should be the exception, not the rule." Two supporting habits: "Set reasonable, team-wide expectations for acceptable response times" and treat writing as a core skill.

He is open about the costs: "As with most things in life, async culture has pros and cons." The main one: "It's hard to build rapport and personal relationships with only written communication." Changing an existing company is "an uphill battle that challenges the status quo." Which situations Doist keeps synchronous (1-on-1s, sensitive feedback, crises) is recorded only in the collector's paraphrase of the page, not in quoted text.

## GitLab: async as the starting point

GitLab's handbook (official-docs) writes the default into policy: "we use asynchronous communication as a starting point", and "Sometimes synchronous communication is the better option, but do not default to it." It also removes the always-on expectation: "You are not expected to be available all the time." "There is no expectation to respond to messages outside of your planned working hours."

## Evidence from a natural experiment

The strongest evidence in this area is a Microsoft study, known here through two sources: the authors' 2020 arXiv preprint (study) and a university press summary of the later Nature Human Behaviour paper (the published paper was paywalled).

The preprint states the design in the authors' own words: "We use difference-in-differences (DiD), a causal identification strategy commonly used in the social sciences," "to control for unobserved confounding factors and estimate the causal effect of WFH." It compares employees who already worked from home before COVID-19 with those who did not ("measuring the difference in changes between those who WFH prior to COVID-19 and those who did not"). The causal result runs against the naive one: "The change attributable to WFH specifically is in the opposite direction: less time on collaboration and more focus time." The authors stress the method: "a simple analysis would have resulted in the wrong conclusion." The channel shifted too: "instant messages were used more, whereas scheduled meetings were used less."

The press page for the published version describes "a new study of over 61,000 Microsoft employees", because "Measuring the causal effects of remote work has historically been difficult". Remote work led people to "spend more time using asynchronous forms of communication" and "caused the number of hours people spent in meetings to decrease by about 5%." It also found that "your colleagues' remote work status affects your own work habits", and the authors caution: "It's important to be thoughtful about how these policies are implemented."

The headline finding that remote work made collaboration more siloed across groups appears in both raw notes only in the collectors' paraphrase, not in the quoted excerpts, so it is recorded here as unverified. The study measured forced remote work, not a chosen async-first policy, and fewer meetings came with more instant messages, not less communication.

## For cardigan

Interpretation, not source claims:

- Recreating the office online names the anti-pattern cardigan targets: a status meeting or call that exists only because it existed in the office. The meetings that remain get an agenda, which cardigan can draft.
- When cardigan suggests a written alternative to a meeting, it states the cost (a slower answer) when the decision is urgent, not hides it.
- A doc-instead-of-a-meeting suggestion fits known collaborators best. With new or cross-group contacts, cardigan should be slower to replace the one live conversation (interpretation of the study's caution; the siloing result is not verified here).
- Rapport is where written-only fails by its own advocates' account. For relationship-heavy or sensitive situations, cardigan should not push a written message over a call.
- Dropping meetings shifts volume to chat (the preprint). An async-first suggestion from cardigan should reduce total communication, for example one written update instead of a meeting, not one meeting traded for many messages.
- Not sending now is a valid output. When a thought can wait for a batch, a thread or the next agenda, cardigan can hold it rather than fire a message (37signals: now is often the wrong time).

## See Also

- [Message overload](../office-waste/message-overload.md)
- [Single source of truth](single-source-of-truth.md)
- [Meeting purges](../office-waste/meeting-purges.md)
- [Writing culture](writing-culture.md)
- [Bottom Line Up Front (BLUF)](bluf.md)
