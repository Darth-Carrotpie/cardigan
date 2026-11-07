# Anthropic skills: discernment-nudge

> Source: https://github.com/anthropics/skills/blob/main/skills/discernment-nudge/SKILL.md
> Collected: 2026-10-31
> Published: 2026-08-17 (last commit to the skill folder)
> Author: Anthropic
> Type: repo

## Excerpts

Frontmatter (Apache-2.0):

> description: >
>   After you give a substantive answer or draft that the user may act on
>   — advice or recommendations, drafted artifacts such as goals, plans,
>   pitches, proposals, or emails, estimates or projections, analysis or
>   interpretation of data, factual claims they may rely on, or a
>   multi-step argument — invoke this skill BEFORE finalizing your reply
>   and then, if it applies, append 2-3 short follow-up questions, each
>   tied to something specific in what you just produced, that help the
>   user check key facts, probe the reasoning or assumptions, and notice
>   missing context. Do this at most once per conversation. Skip it when
>   the user asked a trivial how-to or simple lookup, wants a purely
>   educational explanation, asked you only to format, convert, or
>   assemble a file from content they provided, is writing code they will
>   run, is doing creative writing or casual chat, or already asked you
>   to double-check, cite, or review — the skill file explains these
>   boundaries and the exact output format.

Body:

> Leave it off when the nudge would be noise — or worse, when it would override something the user already told you. Silence is the right default; only add the nudge when there's something concrete worth reflecting on *and* the user hasn't already signaled they've got verification covered.
>
> **Once per conversation.** Offer the nudge at most once in a conversation. If you have already offered it on an earlier turn, stay silent on later turns even when the new answer would otherwise qualify — the user has already been invited to reflect, and repeating it turns a light suggestion into nagging.

> - **The user asked for the quick version, or said they'll do their own checking.** "Just the headline," "skip the caveats," "quick version — I'll do my own research." They've explicitly opted out of the scaffolding. A nudge overrides that preference, which lands as paternalistic. Respect the ask; give them what they asked for and stop.

> - **The user gave you the material.** Summarizing, reformatting, or extracting action items from their own document, thread, or notes — they have the source and they're the judge of whether you matched it. [...] If you're unsure your summary is faithful, say so in the answer.

> Phrase each one as something the user could ask you verbatim — first person, conversational, question form. Two or three prompts, never more. Keep each under ~120 characters so it reads at a glance.

> Always answer the question completely first. The nudge comes after, and it should be easy to skip.
> [...]
> Use that exact lead-in line — "A few things worth a second look:" — followed by the prompts as plain bullets. No blockquote, no heading, no extra framing; it should read as a light suggestion, not a boxed warning. Plain text only — no HTML, no headings, no emoji.
>
> Don't add anything after the nudge — no "let me know if you'd like me to dig into any of these." The nudge is the closer.

## Collector's note

An Anthropic skill that is effectively always-on through its description (model-invoked "BEFORE finalizing your reply") yet defaults to silence: a long list of skip conditions, a once-per-conversation cap, a fixed 2–3 bullet format, and a ban on trailing offers. It is the clearest surveyed example of a skill whose main content is *when not to add output*, and of a description that carries the full trigger and skip logic (~1,000 characters). It governs an add-on to the reply, not the deliverable itself, and it does not question whether the drafted plan or email should exist. No evals are published in the repo.
