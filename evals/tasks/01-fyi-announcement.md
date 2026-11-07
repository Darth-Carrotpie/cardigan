# 01 · All-staff FYI, "draft a reply"

- **Kind:** email
- **Right size:** less (no reply is needed)
- **Tests:** rung 1 (does it need to exist?), recipient check

## Prompt

```
Draft a reply to this email for me.

From: Marta Lind (Facilities) <facilities@northwind.example>
To: all-london@northwind.example
Subject: Office closed Friday 13 November – electrical works

Hi all,

The London office will be closed on Friday 13 November for scheduled electrical works. Please work from home that day.

Building access cards will not work between 07:00 Friday and 06:00 Monday. If you need to collect anything from your desk, please do so by 18:00 on Thursday 12 November.

Questions to facilities@northwind.example.

Thanks,
Marta
Facilities
```

## Good outcome

Tells the user that no reply is needed: it's an all-staff announcement, and a reply to `all-london` would start a reply-all chain. It may offer something useful instead, such as a calendar block for Friday or a reminder to collect things by Thursday 18:00. If it drafts anything, it's one line to facilities only.

## Checks (pass/fail)

1. **Real ask:** tells the user whether a reply is needed, and says it isn't.
2. **Recipient (never-cut):** no draft is addressed to `all-london`.
3. **Facts (never-cut):** any date or time it mentions is correct (Fri 13 Nov; Thu 12 Nov 18:00; 07:00 Fri to 06:00 Mon).

## Lighter option

No reply. **Taken** if the response recommends not replying, even if it also offers an optional one-liner.

## Measure

Words in the deliverable, total words, output tokens, time, checks passed, lighter option offered / taken.
