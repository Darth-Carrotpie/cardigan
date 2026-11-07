# Repeat replies

> Sources: Google (Gmail Help), undated; Slack (resources page), undated
> Raw: [Create a template in Gmail](../../raw/research/native-features/gmail-templates-and-auto-reply-filters.md); [Four simple ways to save time with Workflow Builder](../../raw/research/native-features/slack-workflow-builder-save-time.md)
> Updated: 2026-10-31

## Overview

The same answer typed again (an FAQ reply, an intake acknowledgement, a standard decline) is a deliverable a tool can hold. Mail clients store it as a template, and a filter can send it automatically to a predictable class of message. Chat tools go a step earlier: an intake form makes the requester supply the facts up front, so the follow-up questions never need asking, and an automated welcome message replaces the repeated onboarding explanation. The evidence is vendor help and marketing pages, which describe how the features work, not whether they save time.

| Manual deliverable | Native feature (tool) | Plan/licence caveat |
|---|---|---|
| Retyping a standard email reply | Templates (Gmail) | Desktop only (Gmail on a computer); must be enabled first; deleted templates can't be recovered |
| Manually answering a predictable class of incoming mail | Filter with "Send template" auto-reply (Gmail) | Same as templates; needs a filter set up |
| Follow-up questions on ad-hoc requests (budget? brief?) | Intake form attached to a channel (Slack Workflow Builder) | Not stated on the page; the collector reports it is a paid-plan feature that admins can restrict |
| Re-explaining a project to each new teammate | Automated onboarding welcome message (Slack Workflow Builder) | As above |
| Pasting the same answer to repetitive questions in chat | Workflow reply (Slack Workflow Builder) | As above |

## Gmail: templates and template auto-replies

Google's help page (official-docs, undated) says the feature is off until switched on ("Next to "Templates," click Enable") and desktop-bound: "You can only turn on and use message templates from Gmail on your computer." A draft becomes reusable via "Save draft as template [...] Save as new template". Deletion is final: "After you delete a template, you can't recover it."

Automation needs one more step: "To send your message template as an automatic reply, you must create a filter." The filter action is "Send template".

The collector adds that Gmail has no native shared team templates; that is the collector's note, not the page's text.

## Slack: intake forms and automated answers

Slack's own resources page (vendor-data; marketing, undated, no author) lists the chat-side swaps. Requests: "attach intake forms to a channel and standardize how teammates ask for help or share feedback." with the payoff "No more follow-ups like, "Is there budget for this?" or "Do you have a creative brief?"" Onboarding: "With an onboarding workflow, you can quickly get teammates up to speed on a project", and "These automated welcome messages are handy for sharing kickoff docs, roles and responsibilities". Repeated answers: "Say goodbye to the copying and pasting the same answer to repetitive questions".

The page does not state plan limits; the collector's note says Workflow Builder is paid-plan and admin-restrictable, which is not verified from this source.

## For cardigan

Interpretation, not source claims:

- The second time a user asks for the same reply, cardigan drafts it once more and offers to save it as a template; the third time, it suggests a filter with an auto-reply if the incoming messages are predictable.
- A template or auto-reply still has to carry the facts the sender needs (next step, timeline, contact). Cutting effort does not mean cutting the ask or politeness.
- When a user keeps asking requesters the same follow-up questions, the fix is upstream: cardigan suggests an intake form that asks them once, at request time, instead of drafting the follow-up.
- Auto-replies suit acknowledgements and FAQs, not anything needing judgment; cardigan does not propose them for complaints, negotiations or anything with compliance wording that varies by case.

## See Also

- [Inbox triage](../practices/inbox-triage.md)
- [Single source of truth](../practices/single-source-of-truth.md)
- [Status updates and standups](status-and-standups.md)
