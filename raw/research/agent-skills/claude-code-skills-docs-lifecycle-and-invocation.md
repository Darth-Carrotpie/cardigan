# Extend Claude with skills (Claude Code docs)

> Source: https://code.claude.com/docs/en/skills
> Collected: 2026-10-31
> Published: Unknown
> Author: Anthropic
> Type: official-docs

## Excerpts

> Keep the body itself concise. Once a skill loads, its content [stays in context across turns](#skill-content-lifecycle), so every line is a recurring token cost. State what to do rather than narrating how or why, and apply the same conciseness test you would for [CLAUDE.md content].

> | `description` | Recommended | What the skill does and when to use it. Claude uses this to decide when to apply the skill. If omitted, uses the first non-empty line of the markdown content. Put the key use case first: the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage. [...] |
> | `when_to_use` | No | Additional context for when Claude should invoke the skill, such as trigger phrases or example requests. Appended to `description` in the skill listing and counts toward the 1,536-character cap. |
> | `argument-hint` | No | Hint shown during autocomplete to indicate expected arguments. Example: `[issue-number]` or `[filename] [format]`. |

> * **`disable-model-invocation: true`**: Claude can't invoke the skill on its own. Use this for workflows with side effects or that you want to control timing, like `/commit`, `/deploy`, or `/send-slack-message`. You don't want Claude deciding to deploy because your code looks ready.
>
> * **`user-invocable: false`**: Only Claude can invoke the skill. Use this for background knowledge that isn't actionable as a command.

> | `disable-model-invocation: true` | Yes | Not on its own | Description not in context, full skill loads when invoked |
> | `user-invocable: false` | No | Yes | Description always in context, full skill loads when invoked |

> > Keep `SKILL.md` under 500 lines. Move detailed reference material to separate files.

> ### Skill content lifecycle
>
> When you or Claude invoke a skill, the rendered `SKILL.md` content enters the conversation as a single message and stays there across later turns. [...] Claude Code does not re-read the skill file on later turns, so write guidance that should apply throughout a task as standing instructions rather than one-time steps.

> [Auto-compaction] carries invoked skills forward within a token budget. When the conversation is summarized to free context, Claude Code re-attaches the most recent invocation of each skill after the summary, keeping the first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens. Claude Code fills this budget starting from the most recently invoked skill, so older skills can be dropped entirely after compaction if you have invoked many in one session.

## Collector's note

The Claude Code-specific skills reference, which adds host behaviour the platform best-practices page does not cover. Relevant to an always-on skill like cardigan: once invoked, the body persists across turns and should be written as standing instructions; after compaction only the first 5,000 tokens of each skill are re-attached (shared 25,000-token budget, most recent first); the listing truncates description + `when_to_use` at 1,536 characters, so the key trigger must come first. It also documents the invocation switches (`disable-model-invocation`, `user-invocable`) that determine whether a skill is model-triggered, a slash command, or both.
