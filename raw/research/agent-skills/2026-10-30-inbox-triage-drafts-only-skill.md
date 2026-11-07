# inbox-triage (alirezarezvani/claude-skills, productivity/email)

> Source: https://github.com/alirezarezvani/claude-skills/blob/main/productivity/email/skills/inbox-triage/SKILL.md
> Collected: 2026-10-31
> Published: 2026-10-30 (last commit to the skill folder; repo ~29k stars)
> Author: Alireza Rezvani
> Type: repo

## Excerpts

Frontmatter (MIT):

> ---
> name: inbox-triage
> description: "Use when the user wants their inbox processed ('triage my inbox', 'check my email'). Classifies recent mail with the inbox-setup knowledge base, drafts replies it never sends (checked by draft_safety_validator.py) and reports."
> license: MIT
> metadata:
>   source_spec: "megaprompts/07-inbox-triage-megaprompt.md"
>   build_pattern: "Path B (direct conversion)"
>   paired_with: "inbox-setup (consumes the 7-file KB it produces)"
>   version: 1.0.0
> ---

> Run on a recurring schedule (1–3x daily) or on demand. Classify recent emails, research new senders, generate decision recommendations, draft replies (**NEVER SEND**), deliver a clean report, and update the knowledge base with what was learned this run.

> The `scripts/draft_safety_validator.py` enforces it post-run. Any send-shaped tool call in the action log fails validation.

> **Stop condition:** Max 2 questions. Default invocations skip both questions and run with KB-default preferences. The skill is optimized for fast recurring execution; intake is the exception, not the norm.

> For **lowest-priority** category (newsletters / automation / spam): skip thread reads entirely — context cost not worth it.

> | Category | When | Output |
> |---|---|---|
> | **TAKE IT** | Meets criteria | Recommend engaging; draft reply (Step 6) |
> | **WORTH CONSIDERING** | Has potential, needs user judgment | Surface key context; draft for user to edit |
> | **PASS** | Doesn't meet criteria | Brief "why" (1–3 sentences); draft polite decline |
> | **FLAG FOR REVIEW** | Unusual; needs direct user decision | Surface fully; NO draft (user decides response shape) |

> **Do NOT draft for:**
> - Clearly no-response emails (newsletters, automation, FYI)
> - Threads where user already replied
> - Blocked senders (unless new info changes the calculus)

> **Sections (in order):**
>
> 1. **Overview** — 2–3 sentences. What happened? Anything urgent?
> 2. **Stats** — Counts: processed, drafts created, action needed, skipped.
> 3. **Action Needed** — Overdue items, decisions, drafts to review, deadlines.
> 4. **Quick Reference** — One line per email, alphabetical by sender. `**Sender** — one-sentence summary + recommendation`.
> 5. **Detailed Cards** — Opportunities, active threads, flags. [...] **NO draft text previews** (drafts are already in email client for user to read there).
> 6. **Footer** — Generation timestamp + KB update summary.

> **Learning patterns to observe over runs:**
>
> - Drafts sent as-is vs. edited vs. deleted → tone calibration signal
> - PASS recommendations user overrides → framework adjustment signal

> Even with zero new emails:
>
> 1. Check `tracker.md` for items due today or overdue
> 2. Generate minimal report: "No new actionable emails since last run"

> 3. **Accuracy over speed.** When unsure, flag for review. A wrong auto-draft is worse than no draft.

## Collector's note

A command-style, scheduled email-triage skill that depends on a separate `inbox-setup` interview skill (7-file knowledge base) and ships Python scripts, including a deterministic post-run validator that fails any send-shaped tool call. It does make a per-email "whether" call (draft / no draft / flag; "A wrong auto-draft is worse than no draft"), which is closer to cardigan's question than any writing-style skill, but its own output is a six-section report produced every run, even on an empty inbox. Self-measurement is limited to the safety validator and a proposed learning signal (drafts sent as-is vs edited vs deleted); no published benchmark or A/B.
