# Meeting notes and recaps

> Sources: Rachel Coldicutt / Careful Industries, 2025-11-20; Microsoft Learn, 2026-08-05; Google (Google Meet Help), undated; Slack (Help Center), undated
> Raw: [Nine risks caused by AI notetakers](../../raw/research/native-features/2025-11-20-careful-industries-nine-risks-ai-notetakers.md); [Manage the Meeting Recaps app for your organization in Microsoft Teams](../../raw/research/native-features/2026-08-05-teams-meeting-recaps-app-licensing.md); ["Take notes for me" in Google Meet](../../raw/research/native-features/google-meet-take-notes-for-me.md); [Guide to AI features in Slack](../../raw/research/native-features/slack-ai-features-guide.md)
> Updated: 2026-10-31

## Overview

Built-in AI notetakers and recap views promise to replace hand-typed minutes, the follow-up recap email and the message asking someone to fill you in. Vendor documentation shows the replacement is real but conditional: Google Meet writes notes into a Doc attached to the calendar event, but only on the organiser's eligible edition and with a warning that summaries can be incomplete or inaccurate; Microsoft Teams builds recaps only from recorded or transcribed meetings and gates the AI versions behind add-on licences. A practitioner risk review argues they shift work rather than remove it: someone still has to check the transcript, recording raises consent and data-protection duties, and always-on capture can chill candour. Its lower-risk alternative is a short agreed list of actions and headlines rather than comprehensive notes.

| Manual deliverable | Native feature (tool) | Plan/licence caveat |
|---|---|---|
| Hand-typed minutes and follow-up recap email | "Take notes for me" notes Doc, attached to the event and emailed to invitees (Google Meet) | Organiser needs an eligible Workspace edition or Google AI plan; one language per meeting; recommended for 15 minutes to 8 hours |
| Asking to be filled in when joining late | "Summary so far" (Google Meet) | Same as above |
| Recap email for people who missed the meeting | Meeting Recaps app: intelligent text, video and audio recap (Microsoft Teams) | Text recap needs Teams Premium or Copilot; audio and video recap need Copilot; meeting must be recorded or transcribed; previous 30 days only |
| Manual notes from a huddle (quick call) | AI huddle notes (Slack AI) | Depends on Slack plan, role and admin restrictions (collector reads the plan table as Pro and up; not in the excerpts) |
| Hand-typed minutes, recap email | AI notetakers in general (risk review, no specific tool) | Not applicable; the caveats are accuracy, consent and data handling |

## Google Meet: "Take notes for me"

Google's help page (official-docs, undated) promises to "Automatically capture meeting notes organized in Google Docs and share with your team." Latecomers can "catch up during the meeting with "Summary so far"". The output lands where people already look: the notes are "saved in the meeting organizer's Google Drive in the "Google Meet" folder", "The notes document is automatically attached to the Google Calendar event", and "The people you share notes with will receive an email with access to the generated notes doc after the meeting." That last step is the recap email, sent by the tool.

Limits from the same page:

- Licence: "This feature requires an eligible Google Workspace edition or Google AI plan." and "The meeting organizer must have the Workspace edition that includes "Take notes for me.""
- Language: "This feature supports one language at a time. Multiple languages spoken in the same meeting aren't currently supported."
- Length: "recommended for meetings of 15 minutes to a maximum of 8 hours."
- Accuracy: "Sometimes, the meeting summary can be incomplete, inaccurate, or not generated."
- Consent: "Google Meet informs all meeting participants that notes are being taken", and "Your administrator may require all participants to provide explicit consent".

## Microsoft Teams: Meeting Recaps app

Microsoft's admin documentation (official-docs) describes a hub where users can "find, filter, and catch up on their recent meetings". It "supports multiple recap modalities, including intelligent text recap, video recap, and audio recap", and "Audio recap can combine content from multiple meetings into a single podcast-style summary".

The conditions matter more than the features:

- Input: "Only recorded or transcribed meetings appear in the Meeting Recaps app."
- Window: it "displays recaps for meetings that occurred within the previous 30 days."
- Licence: "AI-generated recap experiences, including audio recap and video recap, require a Microsoft Copilot license." and "Intelligent text recap requires a Teams Premium or Microsoft Copilot license." Without Copilot, users "can still access meeting transcripts that they have permission to view."
- Discovery: "The app is preinstalled in Teams but isn't pinned by default." Desktop and web only; "Mobile support is coming soon."

The collector also notes community reports that licence behaviour may not match the documentation; that is the collector's summary, not Microsoft's text.

## Slack: huddle notes

Slack's AI guide (official-docs, undated) lists "using AI to take notes during a huddle." Availability depends on "your Slack plan, your role (member or guest), and whether your admins have restricted access."

## Risks of AI notetakers

Rachel Coldicutt (practitioner; Careful Industries, 2025) lists nine risks. Among them: "Low-quality and/or incorrect outputs, due to transcription errors", "Discriminatory outcomes for people with protected characteristics", "Declining quality of workplace culture", "Increased day-to-day workload", "Over-collection of personal data" and "Inappropriately sharing confidential, proprietary or sensitive information".

On accuracy her verdict is blunt: "AI transcription tools are not currently mature or reliable enough", so teams "rely on someone checking the full transcript to ensure full accuracy". That checking is the workload the tool was meant to remove.

> **Status: Disputed**
> Google's Meet help (official-docs) presents auto-notes as ready to share: "Automatically capture meeting notes organized in Google Docs and share with your team", emailed to invitees after the meeting. Coldicutt (2025, practitioner) says "AI transcription tools are not currently mature or reliable enough" and that teams "rely on someone checking the full transcript". The vendor page partly concedes the point ("Sometimes, the meeting summary can be incomplete, inaccurate, or not generated"); neither side offers measured error rates.

On culture, people were "unhappy or uncomfortable when automated notetaking was deployed as standard". Her rule: "Best practice is to treat transcription in the same way as an audio-visual recording," and "Create a clear consent process".

She does not idealise the manual version: "human-created meeting summaries may well contain mistakes and biases". The alternative she points to is agreeing shared actions and headline summaries "rather than taking comprehensive notes".

## For cardigan

Interpretation, not source claims:

- The laziest safe recap is often a short agreed action list (owner, action, date), not a full transcript or a long summary. That keeps the never-cut items and drops the rest.
- cardigan recommends turning on auto-notes only with a consent step, and treats the transcript like a recording: not forwarded widely, not pasted into email.
- An AI summary is a draft to check, not a finished deliverable; when cardigan relays one, decisions, owners and numbers get a human check first.
- When the organiser has Meet's notes on, cardigan does not write a separate recap email: the notes Doc is already attached and mailed. It adds only what the notes cannot know (decisions the user wants to confirm, the ask) after checking the summary.
- Before telling someone the recap is in Teams, cardigan checks the conditions it can know: was the meeting recorded or transcribed, does the reader have the licence, is it within 30 days. If not, a short written action list is still needed.
- Fewer meetings beats better minutes; the notetaker question comes after asking whether the meeting needs to happen at all (see [Meeting purges](../office-waste/meeting-purges.md)).

## See Also

- [Workslop](../office-waste/workslop.md)
- [Meeting purges](../office-waste/meeting-purges.md)
- [Recipient check](../review-practice/recipient-check.md)
