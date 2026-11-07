# Database automations (Notion Help Center)

> Source: https://www.notion.com/help/database-automations
> Collected: 2026-10-31
> Published: Unknown
> Author: Notion
> Type: official-docs

## Excerpts

> Database automations are sequences of actions that happen any time a specific change to a database occurs.

> Automations can have one trigger or multiple triggers.

> `Page added` means your automation will be triggered when a new page is added to your database.

> `Edit property` will edit the properties of pages in the database you are currently in.

> `Send Slack notification to` will send a custom notification to the Slack channel you want.

> `Send mail to` will send an email from your Gmail account to one or more recipients.

> Database automations are available on **paid plans** on **all platforms**.

> Free Plan users can create **Slack notification** automations, but no other kinds of automations.

> **Database automations can't be triggered by other automations.**

> Unfortunately, guests can't create database automations.

> A recurring template automation will not trigger a database automation.

## Collector's note

Replaces manual "status changed, pinging the owner" messages, hand-maintained hand-off emails, and copy-updating properties: a trigger on a database change sends Slack/Gmail notifications or edits properties. Caveats: mostly paid-plan only (free plan gets Slack notifications only), guests can't create them, no automation chaining. For cardigan, the Notion rung before building any custom notification process.
