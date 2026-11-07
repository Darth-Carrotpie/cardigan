# Scheduling

> Sources: Google (Google Calendar Help), undated; Google (Gmail Help), undated; Microsoft Support, undated
> Raw: [Create an appointment schedule](../../raw/research/native-features/google-calendar-appointment-schedules.md); [Collaborate with Gemini in Gmail](../../raw/research/native-features/gemini-in-gmail.md); [Find the best meeting time for everyone with Outlook Scheduling Poll](../../raw/research/native-features/outlook-scheduling-poll.md)
> Updated: 2026-10-31

## Overview

The email thread that asks which times work is a deliverable calendar tools replace. For one-person bookings (office hours, interviews, client calls), a booking page lets the other side pick a free slot. For a group, a scheduling poll lets attendees vote while the calendar holds the candidate slots. The evidence is vendor help pages; they describe the mechanics and the tier limits, not time saved.

| Manual deliverable | Native feature (tool) | Plan/licence caveat |
|---|---|---|
| Back-and-forth email to find a 1:1 slot | Appointment schedule with booking page (Google Calendar) | Booking page for "eligible Workspace accounts"; some features need Workspace or Google One; can't be created in the mobile apps; co-host calendars not checked by default |
| Multi-party email thread to agree a time | Scheduling poll with temporary calendar holds (Outlook) | Microsoft 365 Apps for business or enterprise plans; not for shared mailboxes, group calendars, delegates or Exchange On-Premises organisers |
| Proposing times in a reply | "Propose meeting times" from your calendar (Gemini in Gmail) | Eligible Workspace or Google AI plan; primary calendar only |

## Google Calendar: appointment schedules

Google's help page (official-docs, undated) describes the setup: "Select the appointment duration and your availability." Then "For eligible Workspace accounts, Calendar automatically generates a booking page." The page "is set up based on your weekday availability and doesn't show times when you're busy."

Controls that replace the usual negotiation rules:

- Conflicts: "To avoid schedule conflicts, select Check calendars for availability." For shared slots, "Include co-hosts' calendars in availability checks to prevent double-bookings." But "By default, appointment schedules do not check co-host availability."
- Lead time and load: "By default, there is a 4-hour minimum lead time to schedule an appointment." Owners can "Limit the number of appointments you accept in a single day" and "Add time between appointments on your calendar."
- Spam: "To avoid spam bookings, check the box next to Require email verification."
- Reminders: "You can send up to 5 reminders." but "You can't edit the text of the reminder emails."

Limits: "Some appointment schedule features require an eligible Google Workspace or Google One subscription." and "You can't create an appointment schedule in the Calendar app for Android or iPhone and iPad."

## Outlook: scheduling poll for groups

Microsoft's support page (official-docs, undated): "The scheduling poll feature is used to schedule meetings via polling." It reserves time while people vote: "When a new scheduling poll is created, temporary holds are placed on everyone's calendars to help reserve time." and "Holds are removed when the organizer chooses the final time for the event." Attendees "can vote on their preferred times" from the poll email, and the web page is "the only way that people outside of your organization can vote".

On size: "Currently, you can include up to 15-time options in a poll, however 3-5 options are recommended".

Limits: it is "available to users of Microsoft 365 Apps for business or enterprise plans". "Scheduling polls aren't supported with shared email accounts or group calendars." "Currently, calendar delegates cannot create new scheduling polls or vote on behalf of the main calendar owner." "This feature is not available to organizers with mailboxes on an Exchange On-Premises server."

## Gmail: proposed times in a draft

Google's Gemini in Gmail page (official-docs) lists "Propose meeting times based on your availability in Google Calendar." on an eligible plan, with the limit that "Gemini in Gmail can only give you information about events on your primary calendar."

## For cardigan

Interpretation, not source claims:

- For a recurring kind of one-to-one booking, cardigan's first suggestion is a booking link, not a list of proposed times. The reply becomes one line plus the link.
- A booking link to a senior person or an external client can read as offloading work onto them; cardigan offers two or three concrete times instead when the recipient outranks the user or the relationship is new (social rule over laziness).
- For three or more people, cardigan suggests a scheduling poll with a few options (Microsoft recommends 3-5) rather than an email asking everyone for availability.
- Assistants who schedule for an executive cannot use Outlook's poll as a delegate, so cardigan falls back to proposing times for them.
- When co-hosts are involved, cardigan reminds the user to turn on co-host availability checks, since the default does not check them.

## See Also

- [Meeting purges](../office-waste/meeting-purges.md)
- [Politeness and softening](../pushback/politeness-and-softening.md)
