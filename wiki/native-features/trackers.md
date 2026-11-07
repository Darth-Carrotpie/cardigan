# Trackers and status tables

> Sources: Google (Google Docs Help), undated; Google (Google Docs Editors Help), undated; Notion (Help Center), undated; Slack (Help Center), undated
> Raw: [Insert smart chips and building blocks in your Google Doc](../../raw/research/native-features/google-docs-smart-chips.md); [Sort & filter your data](../../raw/research/native-features/google-sheets-filter-views.md); [Database automations](../../raw/research/native-features/notion-database-automations.md); [Slack lists: Track project tasks](../../raw/research/native-features/slack-lists-track-project-tasks.md)
> Updated: 2026-10-31

## Overview

Hand-built status tables, pasted attendee lists, copied file links and per-person copies of a spreadsheet go stale the moment they are written. Docs and chat tools offer live elements instead: lists in the chat tool where the work is discussed, chips that point to a person, file or calendar event, dropdowns or building blocks that turn a doc into a simple tracker, saved filter views that give each reader their own link into one live sheet, and automations that send the "status changed" message when the tracker changes. The evidence is vendor help pages.

| Manual deliverable | Native feature (tool) | Plan/licence caveat |
|---|---|---|
| Separate tracker spreadsheet or "action items" email for a small project | Lists with a Project tracker template; turn any message into a task (Slack) | Plan availability not stated on the fetched page |
| Pasted names, file links and event details in a doc | People, file and calendar-event smart chips (Google Docs) | Mentioning someone doesn't give them access; share the doc separately |
| Hand-built status table in a doc | Dropdown chips and building blocks for tracking projects (Google Docs) | Not stated on the fetched page |
| Per-person copies of a sheet, or emailed filtered extracts | Saved filter view with its own shareable link (Google Sheets) | One filter view applied at a time; temporary views are not saved |
| "Status changed" pings to an owner, hand-off emails, updating fields by hand | Database automations: trigger on a change, send Slack notification or Gmail, edit properties (Notion) | Paid plans; free plan gets Slack-notification automations only; guests can't create them; automations can't trigger other automations |
| Asking a collaborator by email to fill in a field | Placeholder chip (Google Docs) | Not stated on the fetched page |

## Slack: lists

Slack's help page (official-docs, undated): "With lists, you can capture, track, and stay aligned on tasks — right where you're already working." Users can start from a template ("the Project tracker template is a great option"), where "Task, Status, Assignee, and Due Date are added for you". Conversation turns into work items directly: "You can turn any message into a task." Owners see their items: "When you assign someone a task in a list, they can view it in the Assigned to you section of the Lists page." and "You can enable notifications for items in a list you want to keep tabs on."

The page states no plan availability or limits; the collector's note adds that launch coverage tied lists to paid plans and that a university IT page calls them not a full project-management tool (collector's summary, not Slack's text).

## Google Docs: smart chips and building blocks

Google's help page (official-docs, undated) lists chips for details such as "Dates or Google Calendar events", and says "You can also insert placeholder chips, time trackers, and dropdowns" and "use building blocks to track projects, files, and more."

Chips replace pasting: to add a people chip you start typing a name or email address (or `@me` for yourself), and "To add a file smart chip, enter the file name or related keywords." "You can add a smart chip for a Calendar event to see information about the event". For a field someone else owns: "To add a smart chip that a collaborator can fill in, select "Placeholder chip.""

The access caveat: "When you mention another user in a smart chip, they don't automatically get access to your document." and "To grant access to another user, you must share your document."

## Google Sheets: filter views instead of copies

Google's Sheets help (official-docs, undated) separates a shared filter from a personal view. A plain filter is global: "When you add a filter, anyone with access to your spreadsheet will find the filter too." Filter views avoid that: "On a computer, you can filter data so the filtered data only applies to your view of the spreadsheet." and they "Let multiple people find different filter views at the same time."

A view can be temporary ("you can create a temporary filter view that only you can use. Your filter view won't be saved.") or saved ("To save your filter view, at the top right, click Save View."), and shared by link: "Apply the filter view [...] Copy the URL [...] Share the filter view link". Limits: "You can only apply one filter view at a time." and "You can't change the order of filter views."

## Notion: database automations

Notion's help page (official-docs, undated) defines them: "Database automations are sequences of actions that happen any time a specific change to a database occurs." and "Automations can have one trigger or multiple triggers." For example, "`Page added` means your automation will be triggered when a new page is added to your database." Actions include "`Send Slack notification to` will send a custom notification to the Slack channel you want.", "`Send mail to` will send an email from your Gmail account to one or more recipients." and "`Edit property` will edit the properties of pages in the database you are currently in."

Limits: "Database automations are available on **paid plans** on **all platforms**." and "Free Plan users can create **Slack notification** automations, but no other kinds of automations." Also "**Database automations can't be triggered by other automations.**", "Unfortunately, guests can't create database automations." and "A recurring template automation will not trigger a database automation."

## For cardigan

Interpretation, not source claims:

- For a small project already run in chat, cardigan suggests a chat list (task, owner, status, due date) over a separate spreadsheet or an action-items email; the owner and due date are never-cut fields either way.
- When a user asks for a status table or a doc that lists people, files and dates, cardigan uses the tool's live elements (chips, dropdowns, a tracker block) rather than typed text that goes stale.
- When a user asks for a per-person version of a sheet or an emailed extract, cardigan proposes a saved filter-view link over the live sheet instead of a copy, so there is one source and no versions to reconcile.
- When the user keeps telling people that a tracker item moved (done, your turn), cardigan suggests a tracker automation for that hand-off instead of drafting the message each time. On a free plan, that means a Slack notification only.
- A mention is not a share. When cardigan adds people to a doc, it reminds the user to share it, or the named owner may never see their task.

## See Also

- [Single source of truth](../practices/single-source-of-truth.md)
- [Status updates and standups](status-and-standups.md)
