# Caveman: why many token when few do trick (SKILL.md, README, Honest Numbers)

> Source: https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md (also https://github.com/JuliusBrussee/caveman/blob/main/README.md and https://github.com/JuliusBrussee/caveman/blob/main/docs/HONEST-NUMBERS.md)
> Collected: 2026-10-31
> Published: 2026-10-31 (last push; ~116k stars at collection)
> Author: Julius Brussee
> Type: repo

## Excerpts

SKILL.md frontmatter and core (Apache-2.0):

> ---
> name: caveman
> description: >
>   Terse caveman voice: answer first, fluff gone, every technical fact kept.
>   Use for /caveman, "caveman mode", "talk like caveman", "be brief", "less
>   tokens". Stays on until "stop caveman" or "normal mode".
> ---
>
> # caveman
>
> Respond terse like smart caveman. All technical substance stay. Only fluff die.
>
> Caveman is a voice, not broken grammar. Reader pays per token and reads in a terminal. Every word earns its place. Every fact survives.

> ## Persistence
>
> Every response, whole session, until user says "stop caveman" or "normal mode". Unsure if still on? It is. Confirm the switch-off in one line.

> ## Why
>
> 1. Every output token is billed and read. Filler costs twice.
> 2. Code, commands, paths, numbers, errors are the payload. One changed character breaks them.
> 3. Ceremony is expensive, grammar is cheap. "Sure, I'd be happy to help" is ten tokens. "the" is one.
> 4. A dropped negation costs more than every token saved. Clarity beats compression.

> ### 1. Answer first
>
> Answer, then reason, then next step. Pattern: `[thing] [action] [reason]. [next step].`
> [...]
> ### 2. Kill ceremony
>
> No greeting, hedging, pleasantries, recap, or closer. No "Sure!", "Let me", "I'll now", "Hope this helps". No just/really/basically/actually/simply.
> [...]
> ### 4. Articles optional, meaning never
>
> Drop a/an/the when the sentence still reads in one pass. Fragments fine. Never drop not/never/no/only/except. Numbers and units exact.
> [...]
> ### 5. One idea per sentence
>
> ASD-STE100 is the floor: 20 words max, active voice, imperative for instructions, one term per thing, pronoun only with an obvious referent. Compression and clarity conflict? Clarity wins.
> [...]
> ### 9. Never perform caveman
>
> No "caveman mode on", no "me think", no "Caveman:" prefix, no normal answer plus caveman copy. No decorative tables or emoji. Never add a word to sound caveman. Caveman phrasing not shorter than plain? Use plain.

> ## When to break the rules
>
> Plain prose, then resume:
>
> 1. Security warning.
> 2. Irreversible action. Confirm in full sentences first.
> 3. Step order a fragment could scramble.
> 4. User confused or repeats the question.
> 5. Anything persisted outside chat: code, comments, commits, docs, issues, PRs, tickets, memory files, third-party messages. `/caveman-compress` exempt.
> 6. Harness asks for a status line or confirmation. Give it. Harness decides *when* you speak, caveman decides *how*.
> 7. You ask the user a question or offer options. Full sentences, so the answer comes back right first time.
>
> ## Pre-send check
>
> 1. First sentence announces what you will do? Delete.
> 2. Last sentence recaps or offers help? Delete.
> 3. Every not/never/no/only present? Every code span, path, number, error verbatim?
> 4. Any sentence with two readings? Make it a full sentence.

README, levels and commands:

> | Skill | Same answer | Tokens |
> |---|---|---:|
> | `/caveman` | New object ref each render, so React re-renders. Wrap the prop in `useMemo`. | 20 |
> | `/ultracave` | Inline object prop, new ref, re-render. `useMemo`. | 14 |
> | `/megacave` | 新參照致重繪。`useMemo`。 | **13** |

> | `/caveman` · `/ultracave` · `/megacave` | The voice, the grunt, the 文言文. `/caveman status` shows the mode, `/caveman off` stops it |
> | `/caveman-commit` | One-line Conventional Commit |
> | `/caveman-review` | One finding per line: `L42: 🔴 null deref. Guard it.` |
> | `/caveman-compress <file>` | Shrinks memory files and backs up the original |
> | `/caveman-stats` | Real token usage for this Claude Code session |

README, self-measurement:

> Ten dev questions on claude-opus-5-5:
>
> | Instruction | Output tokens |
> |---|---:|
> | None | 6,983 |
> | `Answer concisely.` | 4,334 |
> | `/caveman` | 4,119 |
> | `/ultracave` | **2,693** |
>
> "Be concise" is the real baseline; new models already know it. On top of it, `/caveman` cuts 3% more at the median and `/ultracave` 35% more. Measured on the 3.1.0 rules, not yet re-run. The rules cost about 1,160 tokens of input, and if you pay per request (GitHub Copilot), shorter answers save nothing.

> Two findings shaped caveman. Adobe: cavemanning *your* prompt makes answers worse, so caveman never touches your prompt. JetBrains: agent sessions are mostly code and tool calls, which the voice leaves alone.

docs/HONEST-NUMBERS.md:

> Caveman save tokens sometimes. Caveman cost tokens sometimes. This page say which is which, with the real numbers. No marketing. If caveman lose for your workload, this page tell you to turn it off.

> | Output reduction vs a plain `Answer concisely.` control | caveman 3%, ultracave 35%, megacave 9% at the median (n=10, single run, output length only, tiktoken o200k approximation; measured on the 3.1.0 skill text, not re-run since the 3.2.0 rule changes) | `evals/llm_run.py` on claude-opus-5-5 with host settings isolated; `evals/measure.py` | [...] |

> Token-count runs measure output length only. They do not prove semantic or technical equivalence. Publish a reduction only with committed raw pairs and separate quality review. A fidelity eval now exists (`evals/score_fidelity.py`: fixed cases, regex checks for kept numbers, negations, language and safety wording, scored for every arm), but no reviewed fidelity snapshot is committed, so no quality claim is published.

> - **LemonCrow** ([#727](https://github.com/JuliusBrussee/caveman/issues/727)): 20 engineering prompts × 5 reps × 3 runs (300 runs per arm), `claude-opus-4-8`, July 2026 `skills/caveman/SKILL.md` as the only extra system instruction. Billed output −44.1%. Total cost +0.06%. Initial cached context +1,532 tokens per run.
> [...]
> Common thread: output shrink, but an agent run's bill is mostly input and cache re-reads, which an output-style rule cannot touch.

> Earlier stats releases applied a fixed 65% output ratio without a committed reviewed result. Current reports ignore those historical `est_saved_*` fields while preserving the original history rows.

## Collector's note

Caveman is an always-on (session-persistent) output-voice skill with three intensity variants as separate skills (`/caveman`, `/ultracave`, `/megacave` classical Chinese) plus one-shot commands; the repo has since grown into a token-saving product (proxy, model router, telemetry). It governs how replies are phrased, not what gets produced, and explicitly exempts anything persisted outside chat (docs, tickets, third-party messages), which is the territory cardigan targets. Its self-measurement is notable for retreating from an early "65%" claim to a "Honest Numbers" page that uses a "Answer concisely." control arm (3% at median for the default level, n=10) and lists outside A/Bs where cost was flat. The "be concise is the real baseline" point is directly relevant to how cardigan should choose its control arm.
