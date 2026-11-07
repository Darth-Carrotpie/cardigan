# Stop Slop

> Source: https://github.com/hardikpandya/stop-slop/blob/main/SKILL.md (also https://github.com/hardikpandya/stop-slop/blob/main/README.md)
> Collected: 2026-10-31
> Published: 2026-03-17 (last commit; ~18.5k stars at collection)
> Author: Hardik Pandya
> Type: repo

## Excerpts

https://github.com/hardikpandya/stop-slop/blob/main/SKILL.md (MIT):

> ---
> name: stop-slop
> description: Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells.
> metadata:
>   trigger: Writing prose, editing drafts, reviewing content for AI patterns
>   author: Hardik Pandya (https://hvpandya.com)
> ---
>
> # Stop Slop
>
> Eliminate predictable AI writing patterns from prose.
>
> ## Core Rules
>
> 1. **Cut filler phrases.** Remove throat-clearing openers, emphasis crutches, and all adverbs. See [references/phrases.md](references/phrases.md).
>
> 2. **Break formulaic structures.** Avoid binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency. See [references/structures.md](references/structures.md).
>
> 3. **Use active voice.** Every sentence needs a human subject doing something. No passive constructions. No inanimate objects performing human actions ("the complaint becomes a fix").
>
> 4. **Be specific.** No vague declaratives ("The reasons are structural"). Name the specific thing. No lazy extremes ("every," "always," "never") doing vague work.
>
> 5. **Put the reader in the room.** No narrator-from-a-distance voice. "You" beats "People." Specifics beat abstractions.
>
> 6. **Vary rhythm.** Mix sentence lengths. Two items beat three. End paragraphs differently. No em dashes.
>
> 7. **Trust readers.** State facts directly. Skip softening, justification, hand-holding.
>
> 8. **Cut quotables.** If it sounds like a pull-quote, rewrite it.
>
> ## Quick Checks
>
> Before delivering prose:
>
> - Any adverbs? Kill them.
> - Any passive voice? Find the actor, make them the subject.
> [...]
> - Vague declarative ("The implications are significant")? Name the specific implication.
> - Narrator-from-a-distance ("Nobody designed this")? Put the reader in the scene.
> - Meta-joiners ("The rest of this essay...")? Delete. Let the essay move.
>
> ## Scoring
>
> Rate 1-10 on each dimension:
>
> | Dimension | Question |
> |-----------|----------|
> | Directness | Statements or announcements? |
> | Rhythm | Varied or metronomic? |
> | Trust | Respects reader intelligence? |
> | Authenticity | Sounds human? |
> | Density | Anything cuttable? |
>
> Below 35/50: revise.

https://github.com/hardikpandya/stop-slop/blob/main/README.md:

> AI writing has patterns. Predictable phrases, structures, rhythms. This skill teaches Claude (or any LLM) to catch and remove them.

> ```
> stop-slop/
> ├── SKILL.md              # Core instructions
> ├── references/
> │   ├── phrases.md        # Phrases to remove
> │   ├── structures.md     # Structural patterns to avoid
> │   └── examples.md       # Before/after transformations
> ```

> **API calls:** Include `SKILL.md` in your system prompt. Reference files load on demand.

## Collector's note

A short (~60-line) model-invoked prose-editing skill with progressive disclosure into three reference files; no levels, no commands, no persistence instructions. It governs sentence-level style only. Its only self-measurement is an in-prompt self-scoring rubric (5 dimensions, revise below 35/50); the repo publishes no benchmark, A/B, or before/after statistics, so popularity (stars) is the only external signal. It never asks whether the text should be written, or whether it could be shorter as a whole; "Density: anything cuttable?" is the closest rule.
