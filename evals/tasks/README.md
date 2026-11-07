# Eval tasks

Twelve realistic office tasks. Each file contains the exact **prompt** the agent receives, what a **good outcome** looks like, pass/fail **checks** (never-cut items are marked), the **lighter option** if one exists, and what to **measure**.

The set is two-sided, per [baseline design](../../wiki/skill-evals/baseline-design.md): 7 tasks where less is right, 1 where short-but-complete is right, and 4 where the full or careful deliverable is right. A skill that only shrinks output fails the last group.

| # | Task | Kind | Right size | Main thing tested |
|---|---|---|---|---|
| 01 | [All-staff FYI, "draft a reply"](01-fyi-announcement.md) | email | less: no reply | needs to exist?, recipients |
| 02 | [Client asks what the thread already answers](02-client-answer-in-thread.md) | email | short, complete | read fully, exact facts |
| 03 | [Manager wants a meeting to collect numbers](03-manager-meeting-to-collect-numbers.md) | meetings | less + default | pushback framing, built-in form |
| 04 | ["Write up the minutes" from a transcript](04-minutes-from-transcript.md) | meetings | less | owners and deadlines |
| 05 | [Weekly status report from raw notes](05-weekly-status-report.md) | reports | less | BLUF, noise, privacy |
| 06 | [Deck the director explicitly asked for](06-deck-director-insisted.md) | decks | full, as asked | no relitigating |
| 07 | [Eight per-person copies of one sheet](07-per-person-sheet-copies.md) | spreadsheets | less | built-in feature |
| 08 | [Saying no to a junior's proposal](08-decline-junior-proposal.md) | chat, team mgmt | short but warm | politeness downward |
| 09 | [Board decision memo](09-board-decision-memo.md) | docs | full | don't over-cut |
| 10 | [Apology to an unhappy client](10-client-outage-apology.md) | email | full, careful | accountability, exact terms |
| 11 | [The expenses question, fourth time](11-expenses-question-again.md) | chat | less | already exists, fix at source |
| 12 | ["Create a project plan" for a small migration](12-small-migration-plan.md) | planning | less | no unrequested artifacts |

## Arms (Phase 2 baseline)

- **A, no skill:** the prompt as written.
- **B, "keep it short":** the same prompt with one line added: `Keep it short.` (see [DECISIONS.md](../../DECISIONS.md)).

3 runs per task per arm, each in a fresh, isolated session, with a transcript audit confirming no skill was loaded in either arm.

## Grading

- Every check is pass/fail, with a one-line critique. Word counts and slide counts are measured with code.
- A run **passes** when every check passes. A never-cut item counts as kept for a task only if it passes in all 3 runs (pass^3).
- Per run, also record: deliverable words, total words, output tokens, time, lighter option offered (Y/N), lighter option taken (Y/N).
- Checks are frozen after a pilot read of a few outputs, before scored grading starts ([rubric design](../../wiki/skill-evals/rubric-design.md)).
