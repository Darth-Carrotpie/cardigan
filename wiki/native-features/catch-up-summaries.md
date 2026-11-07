# Catch-up summaries

> Sources: Google (Gmail Help), undated; Slack (Help Center), undated
> Raw: [Collaborate with Gemini in Gmail](../../raw/research/native-features/gemini-in-gmail.md); [Guide to AI features in Slack](../../raw/research/native-features/slack-ai-features-guide.md)
> Updated: 2026-10-31

## Overview

The catch-up email for someone joining a long thread, the digest of what someone missed in a channel, and the dig through old messages to find an answer can be self-served: the reader's own mail or chat client can summarise the thread or channel, or answer a question with citations. Vendor help pages describe the features and tie them to plan, role and admin settings; Google's page also warns that output may be inaccurate, while Slack's answers cite their source messages.

| Manual deliverable | Native feature (tool) | Plan/licence caveat |
|---|---|---|
| Catch-up summary of a long email thread | Thread summary in bullet points (Gemini in Gmail) | "requires an eligible Google Workspace or Google AI plan"; Google warns outputs may be inaccurate |
| Digest of what someone missed in chat channels | Daily recaps and on-demand channel/thread summaries (Slack AI) | Depends on Slack plan, member or guest role and admin restrictions; some features need the Slack AI add-on on legacy plans; custom date range desktop only |
| Answering a question about a past decision from memory | AI search answers with citations to source messages (Slack AI) | Same as above; answers only include information available to the asker |
| Digging through the inbox for a reservation, flight or package | Ask Gemini about emails in your inbox (Gemini in Gmail) | Same plan requirement; not processed if more than 10,000 threads match |

## Gmail: Gemini summaries and lookups

Google's help page (official-docs, undated) lists what Gemini does in Gmail: "Synthesize long email threads into concise bullet points." and "Gemini can get information on reservations, flights, packages, and other emails sent to your inbox." It also drafts: "Create new emails or refine existing drafts for tone and clarity."

The limits, from the same page:

- Plan: "This feature requires an eligible Google Workspace or Google AI plan."
- Scale: "If there are more than 10,000 email threads that match your criteria, the request is not processed by Gemini."
- Accuracy: "Gemini features may suggest inaccurate or inappropriate information." and "Don't rely on Gemini features as medical, legal, financial or other professional advice."

## Slack: recaps, summaries and cited answers

Slack's help guide (official-docs, undated) offers to "Get caught up after some time away from Slack with a customized summary of your unread channels." and "You'll get a new recap every morning with what you missed from the previous day." On demand, "You can summarize just your unread messages, the last seven days, or a custom date range (desktop only)." and "Summaries can take longer to generate for larger time frames or message histories."

Search answers point back to their evidence: "Answers include citations that refer to the source messages or files that informed them." and "Slack AI will automatically apply the right search filters to natural language queries". Access follows permissions: "AI-generated responses only include information available to you".

Availability varies: "The AI features available to you depend on your Slack plan, your role (member or guest), and whether your admins have restricted access." and "If you're on the legacy version of Business+ or the Enterprise Grid plan without the Slack AI add-on, you'll only have access to the Pro features listed above."

## For cardigan

Interpretation, not source claims:

- cardigan does not write missed-messages digests for a team whose chat tool already produces daily recaps; if a digest is still wanted, it covers only decisions and asks, with links.
- When the recipient's client can summarise the thread, cardigan does not write a catch-up summary by default; it writes only the ask and what changed, and points to the thread.
- That shortcut holds only if the recipient has the feature. For external recipients, or when the plan is unknown, cardigan keeps the two-line summary on forwards (see [Threads and forwarding](../practices/threads-and-forwarding.md)).
- An AI summary never carries the decision, owner or deadline on its own: cardigan states those in the user's words, because the summariser may miss or distort them.
- Legal, financial or compliance threads get a human-written summary, matching Google's own warning.

## See Also

- [Threads and forwarding](../practices/threads-and-forwarding.md)
- [Meeting notes and recaps](meeting-notes-and-recaps.md)
- [Message overload](../office-waste/message-overload.md)
