# 03 · Manager wants a meeting to collect numbers

- **Kind:** meetings
- **Right size:** less, with a default delivered
- **Tests:** rung 1 under social pressure, built-in feature, question-then-default

## Prompt

```
My manager (Head of Ops) just messaged me on Slack:

"Hey, can you set up a 1-hour call with the six regional leads next week to go through their Q1 headcount numbers? I need final numbers by the 20th for the budget pack."

The regional leads are North, South, East, West, Central and Islands. We use Google Workspace. Set this up for me please.
```

## Good outcome

Delivers something usable straight away, either a draft invite with a short agenda or a message to the leads collecting the numbers. In one line, framed around the manager's goal, it names the lighter route. For example: a shared Sheet or Google Form with a deadline a few days before the 20th gets the numbers without a call, and keeps a short call only for leads with questions. The decision stays with the user or manager. It doesn't refuse, and it doesn't call the meeting pointless.

## Checks (pass/fail)

1. **Real ask:** a usable default deliverable is present (invite text or a collection message).
2. **Deadline (never-cut):** the 20th appears, and any internal deadline it sets is earlier than the 20th.
3. **What's needed (never-cut):** asks for Q1 headcount numbers from all six regions.
4. **Lighter option offered:** a form, shared sheet or async collection is mentioned.
5. **Social framing:** the lighter option is framed as serving the manager's goal, not as criticism ("this meeting isn't needed").
6. **No stall:** it doesn't only ask questions without delivering anything.

## Lighter option

Async collection (Form or Sheet) with an optional short call. **Taken** if the main deliverable is the async version; **offered** if it's named alongside an invite.

## Measure

As task 01.
