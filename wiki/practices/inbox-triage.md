# Inbox triage

> Sources: Merlin Mann, 2006-03-27; Tim Ferriss, 2008-01-22; David Allen / David Allen Company, 2020-05-29; Sonja Manning / First Round Review, 2022-12-20; Alireza Rezvani (claude-skills, inbox-triage), 2026-10-30
> Raw: [Inbox Zero: Processing to zero](../../raw/research/practices/2006-03-27-merlin-mann-inbox-zero-processing-to-zero.md); [The Holy Grail: How to Outsource the Inbox](../../raw/research/review-practice/2008-01-22-ferriss-outsource-the-inbox-processing-rules.md); [The Two-minute Rule](../../raw/research/practices/2020-05-29-david-allen-two-minute-rule.md); [How to be an Exceptional Chief of Staff](../../raw/research/review-practice/2022-12-20-first-round-exceptional-chief-of-staff.md); [inbox-triage (alirezarezvani/claude-skills)](../../raw/research/agent-skills/2026-10-30-inbox-triage-drafts-only-skill.md)
> Updated: 2026-10-31

## Overview

Triage decides what a message needs before anyone drafts a reply. Merlin Mann's Inbox Zero posts (practitioner) argue that you clear an inbox by processing, not by answering: delete or archive most mail, park the real work in a "pending" pile, and keep replies short. Tim Ferriss (practitioner) goes further and writes the triage down as standing rules that an assistant applies, so that only the few items needing a decision reach him.

## Process, don't answer

Mann's "dirty little secret" is that you get to zero not "by responding to each of those emails but by ruthlessly processing them." His blunt version: "you cheat. You don't answer them all. Not even most of them."

The order of work for a big backlog:

1. Delete the obvious junk and archive mailing lists, "all the while identifying, flagging, and relocating all the actual important stuff to a "pending" folder".
2. "Only when you're at zero do you return to "pending," concentrating on short responses and generation of to-dos."
3. Stale mail gets a last chance and is then deleted ("this is where I draw the line in the sand").

The guiding rule: "Give each message as much attention as it needs and not one iota more." His slogan is to think in shovels, not in teaspoons.

## Three triage questions

From the companion post ("What's the action here?"):

1. "What does this message mean to me, and why do I care?"
2. "What action, if any, does this message require of me?"
3. "What's the most elegant way to close out this message and the nested action it contains?"

Mann estimates that "Fifty percent or more of your mail may not make it past the first question: delete", and that most of the rest needs at most "a one- or two-line reply". These are his estimates from practice, not measured rates.

## Triage as written rules

Tim Ferriss (practitioner; one person's 2008 setup, with a rules document co-written by his executive assistant) treats triage as a fixed set of questions: "How you evaluate and handle (delete vs. archive vs. forward vs. respond) e-mail is just a series of questions you ask yourself". He writes the answers down in a "Processing Rules" document, and his assistants "add rules when I send them via e-mail with "ADD TO RULES" in the subject."

His claim, an estimate from his own inbox rather than a measurement: "99% of e-mail falls into predetermined categories of inquiries with set questions or responses". The assistant clears the inbox twice a day; "For the 1% of e-mail that might require my input for next actions" there is "a once-daily phone call of 4-10 minutes". When he travels, action items arrive "in numerical order" on voicemail, which he says "forces my assistant to be more prepared and more concise."

The rules show the smallest workable responses:

- **No reply.** Some senders are only labelled: "No need to respond or forward." Some notifications are archived or deleted because he sees them elsewhere anyway.
- **Filter, then flag.** "filter them first, respond to all you can, then mark the ones I should look at with the label "TIM" in Gmail".
- **A one-line acknowledgement.** He needs confirmation that a task was received, and "on it — will be done at Xpm" is enough; status updates are for "larger projects with milestones."
- **A stated authority limit.** "You can decide anything under $100. Use your judgment and report the decisions."

He accepts the cost openly: "it's necessary to let small bad things happen if you want to get huge good things done."

A startup chief of staff, Sonja Manning (practitioner; First Round Review), describes the same pattern in a later playbook: systems "for EAs to do call prep, create meeting notes, update snippets in Superhuman, and draft responses for everything from emails to LinkedIn messages", and "partial implementation, taking on the bulk of the work before sending it to the executive for their final flourish." Her test for what to hand off: "Ask yourself "Do I do this every day or week?" If the answer is yes, consider ways to systematize or offload those tasks."

## Triage rules as an agent skill

An open-source inbox-triage agent skill (repo; Alireza Rezvani's claude-skills) encodes the same pattern for an AI delegate. Each email is sorted into TAKE IT, WORTH CONSIDERING, PASS or FLAG FOR REVIEW, and the skill does not draft for "Clearly no-response emails (newsletters, automation, FYI)" or "Threads where user already replied". Like Ferriss's assistant it works from written standing preferences ("Default invocations skip both questions and run with KB-default preferences."), and like a cautious delegate it escalates instead of guessing: "When unsure, flag for review. A wrong auto-draft is worse than no draft." Unlike Ferriss's assistant it never acts on the user's behalf: a validator fails "Any send-shaped tool call in the action log". See [Office workflow skills](../agent-skills/office-workflow-skills.md#inbox-triage-drafts-it-never-sends).

## The two-minute rule

David Allen (practitioner; originator of Getting Things Done) states the rule on the official GTD site: "Anything you can do in less than two minutes, if you need to do it at all then do it right then." The payoff he claims: "I never have any backlog of two minute stuff because they're all done." The clause "if you need to do it at all" puts deletion before doing, which matches Mann's first triage question.

> **Status: Disputed**
> Allen (GTD site, 2020) says anything under two minutes should be done "right then". Mann (43 Folders, 2006) rejects this for big backlogs: "If you've got more than a few hundred messages in the backlog, I wouldn't even think about responding just yet (we'll agree to disagree in this instance, David Allen)", because even with the two-minute rule "you might be looking at hours and hours of response time". Both are practitioner positions; neither cites measurement. A reconciling reading is that the rule fits a steady flow of mail, while a large backlog needs culling first.

## For cardigan

Interpretation, not source claims:

- Before drafting, cardigan asks Mann's second question (what action, if any?). *None* is a legitimate output and probably the most common one; a to-do or calendar item can close a message better than a reply (Mann's "generation of to-dos").
- When a reply is needed, the default size is one or two lines; longer replies need a reason. A one-line acknowledgement with a time ("on it — will be done at Xpm") is a complete reply to a task request, and only what needs the user's decision is escalated, as a short numbered list.
- A quick, clearly scoped request gets answered right away and briefly rather than scheduled (Allen); when the user faces a large backlog, cardigan triages first and drafts later (Mann).
- Standing rules beat case-by-case judgment for recurring mail: when the user handles the same kind of message twice, cardigan can propose a rule (a filter, a template, an authority limit such as Ferriss's "anything under $100") instead of drafting the third reply.
- Deleting stale mail is a personal-inbox habit; cardigan should not apply it to messages that contain a real ask, owner or deadline.

## See Also

- [Short messages](short-messages.md)
- [Repeat replies](../native-features/repeat-replies.md)
- [Office workflow skills](../agent-skills/office-workflow-skills.md)
