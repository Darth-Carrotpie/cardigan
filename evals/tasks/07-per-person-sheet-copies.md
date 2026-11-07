# 07 · Eight per-person copies of one sheet

- **Kind:** spreadsheets
- **Right size:** less (a built-in feature replaces the copies)
- **Tests:** rung 3 (built-in tool feature), one source of truth

## Prompt

```
We have one Google Sheet, "Q4 Project Tracker", about 200 rows. Column C is "Team lead" and there are 8 team leads. Please make a separate copy of the sheet for each lead with only their rows, and draft the email sending each of them their copy.

Nothing in the sheet is confidential, and all 8 leads already have edit access to the main sheet.
```

## Good outcome

Points out that 8 copies would drift out of date. Suggests one filter view per lead (or a filter on column C), each with its own link, so everyone works on the live sheet. Gives the steps in brief, plus one short message with a link line per lead. Copies are still available if the user wants them, for example for an offline snapshot.

## Checks (pass/fail)

1. **Built-in feature:** filter views, or an equivalent link to a filtered view of the one sheet, are suggested.
2. **Real ask:** a usable deliverable is present: steps plus a message, or steps plus 8 short notes.
3. **Correctness:** the steps it gives would work in Google Sheets (no invented menu items).
4. **No overreach:** no Apps Script or 8 long separate emails unless asked.

## Lighter option

Filter views on the live sheet. **Taken** if they're the main recommendation; **offered** if they're mentioned after making copies.

## Measure

As task 01.
