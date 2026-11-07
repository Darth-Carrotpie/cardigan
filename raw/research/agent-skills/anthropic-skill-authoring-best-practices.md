# Skill authoring best practices (Claude Platform docs)

> Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
> Collected: 2026-10-31
> Published: Unknown
> Author: Anthropic
> Type: official-docs

## Excerpts

> Good Skills are concise, well-structured, and tested with real usage.

> The context window is a public good. Your Skill shares the context window with everything else Claude needs [...]
>
> Not every token in your Skill has an immediate cost. At startup, only the metadata (name and description) from all Skills is pre-loaded. Claude reads `SKILL.md` only when the Skill becomes relevant, and reads additional files only as needed. However, being concise in `SKILL.md` still matters: once Claude loads it, every token competes with conversation history and other context.
>
> **Default assumption:** Claude is already very smart
>
> Only add context Claude doesn't already have. Challenge each piece of information:
>
> * "Does Claude really need this explanation?"
> * "Can I assume Claude has this information?"
> * "Does this paragraph justify its token cost?"

> Match the level of specificity to the task's fragility and variability.

> `description`:
>
> * Must be non-empty
> * Maximum 1,024 characters
> * Cannot contain XML tags
> * Should describe what the Skill does and when to use it

> **Always write in third person**. The description is injected into the system prompt, and inconsistent point-of-view can cause discovery problems.
>
> * **Good:** "Processes Excel files and generates reports"
> * **Avoid:** "I can help you process Excel files"
> * **Avoid:** "You can use this to process Excel files"

> Each Skill has exactly one description field. The description is critical for skill selection: Claude uses it to choose the right Skill from potentially 100+ available Skills. Your description must provide enough detail for Claude to determine when to select this Skill, whereas the rest of `SKILL.md` provides the implementation details.

> * Keep the `SKILL.md` body under 500 lines for optimal performance.
> * Split content into separate files when approaching this limit.

> **Keep references one level deep from `SKILL.md`**. All reference files should link directly from `SKILL.md` to ensure Claude reads complete files when needed.

> **Create evaluations BEFORE writing extensive documentation.** This ensures your Skill solves real problems rather than documenting imagined ones.
>
> **Evaluation-driven development:**
>
> 1. **Identify gaps:** Run Claude on representative tasks without a Skill. Document specific failures or missing context.
> 2. **Create evaluations:** Build three scenarios that test these gaps.
> 3. **Establish baseline:** Measure Claude's performance without the Skill.
> 4. **Write minimal instructions:** Create just enough content to address the gaps and pass evaluations.
> 5. **Iterate:** Run evaluations, compare against baseline, and refine.

> There is not currently a built-in way to run these evaluations. You can create your own evaluation system. Evaluations are your source of truth for measuring Skill effectiveness.

> * **Claude Haiku** (fast, economical): Does the Skill provide enough guidance?
> * **Claude Sonnet** (balanced): Is the Skill clear and efficient?
> * **Claude Opus** (powerful reasoning): Does the Skill avoid over-explaining?

> Work with one instance of Claude ("Claude A") to create a Skill that is used by other instances ("Claude B"). Claude A helps you design and refine instructions, whereas Claude B tests them in real tasks.

> Don't present multiple approaches unless necessary:

> ### Testing
>
> * [ ] At least three evaluations created
> * [ ] Tested with Haiku, Sonnet, and Opus
> * [ ] Tested with real usage scenarios
> * [ ] Team feedback incorporated (if applicable)

## Collector's note

Anthropic's canonical authoring guide for Agent Skills. Key constraints for cardigan: description ≤1,024 characters, third person, "what it does and when to use it" with concrete trigger terms; SKILL.md body under 500 lines with one-level-deep reference files; assume the model already knows general knowledge. Its measurement guidance is evaluation-first: a no-skill baseline, at least three scenarios, testing on Haiku/Sonnet/Opus, and a "Claude A writes / Claude B tests" loop, with no built-in runner. Ponytail v5 (~52 lines) is well inside these limits; the doc does not address always-on skills specifically.
