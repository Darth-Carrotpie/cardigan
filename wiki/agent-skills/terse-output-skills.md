# Terse-output skills

> Sources: Denis Shiryaev / JetBrains AI blog, 2026-07-06; Julius Brussee (caveman SKILL.md, README, HONEST-NUMBERS), 2026-10-31
> Raw: [Does Speaking to Agents Like Cavemen Really Save 65% of Tokens? We Test](../../raw/research/agent-skills/2026-07-06-jetbrains-caveman-paired-ab-test.md); [Caveman: SKILL.md, README, Honest Numbers](../../raw/research/agent-skills/2026-10-31-caveman-terse-output-skill.md)
> Updated: 2026-10-31

## Overview

Terse-output skills compress how an agent phrases its replies. The best known is Caveman, which advertised large token savings. An independent paired A/B by JetBrains (practitioner; a tooling vendor testing someone else's skill) measured far less on agentic coding tasks: "Advertised saving: 65%. Measured saving: 8.5%.", with no detectable change in task quality. The reason is structural: a voice rule only shrinks the prose part of the output. Caveman's own repo has since retreated to an "Honest Numbers" page that measures against a plain "Answer concisely." control and finds little extra saving at the default level. Caveman explicitly exempts docs, tickets and third-party messages, the territory cardigan covers.

## Caveman: the rules

Caveman (repo; SKILL.md, README and the HONEST-NUMBERS page by Julius Brussee) is a "Terse caveman voice: answer first, fluff gone, every technical fact kept." It is session-persistent: "Every response, whole session, until user says "stop caveman" or "normal mode". Unsure if still on? It is." Its premise: "Caveman is a voice, not broken grammar. Reader pays per token and reads in a terminal. Every word earns its place. Every fact survives."

Core rules: "Answer, then reason, then next step."; "No greeting, hedging, pleasantries, recap, or closer."; "Drop a/an/the when the sentence still reads in one pass." but "Never drop not/never/no/only/except. Numbers and units exact." The floor is plain-language style: "ASD-STE100 is the floor: 20 words max, active voice", and "Compression and clarity conflict? Clarity wins." It forbids performing the voice: "Never add a word to sound caveman. Caveman phrasing not shorter than plain? Use plain." The stated reason for the negation rule: "A dropped negation costs more than every token saved. Clarity beats compression."

### When it switches off

Caveman breaks its own rules, in plain prose, for a "Security warning.", an "Irreversible action. Confirm in full sentences first.", a confused user, and "Anything persisted outside chat: code, comments, commits, docs, issues, PRs, tickets, memory files, third-party messages." Questions to the user also get full sentences, "so the answer comes back right first time." A pre-send check deletes framing: "First sentence announces what you will do? Delete." and "Last sentence recaps or offers help? Delete."

### Levels and commands

Intensity is a set of separate skills. The README's example answer costs 20 tokens with `/caveman`, 14 with `/ultracave` and 13 with `/megacave` (classical Chinese). One-shot commands cover commits, one-line review findings, compressing memory files and session token stats; `/caveman status` shows the mode and `/caveman off` stops it.

## Caveman's own numbers

The README now measures against a concise control, not against nothing. On ten dev questions output tokens were 6,983 with no instruction, 4,334 with "Answer concisely.", 4,119 with `/caveman` and 2,693 with `/ultracave`. The author calls "be concise" the real baseline: "new models already know it." On top of that control, `/caveman` cuts 3% more at the median and `/ultracave` 35% more. HONEST-NUMBERS states the limits: "n=10, single run, output length only", and "Token-count runs measure output length only. They do not prove semantic or technical equivalence." The rules themselves "cost about 1,160 tokens of input", and "if you pay per request (GitHub Copilot), shorter answers save nothing."

Outside runs collected on the same page point the same way. One (LemonCrow, 300 runs per arm) found "Billed output −44.1%. Total cost +0.06%." The page's summary: "an agent run's bill is mostly input and cache re-reads, which an output-style rule cannot touch."

> **Status: Outdated** (2026-10-31)
> The advertised 65% saving no longer stands. HONEST-NUMBERS says "Earlier stats releases applied a fixed 65% output ratio without a committed reviewed result", and current reports ignore those fields. JetBrains measured 8.5% (below); the repo's own concise-control figure for the default level is 3%.

## The independent A/B

JetBrains ran Caveman on Claude Code against stock Claude Code on an external suite: "SkillsBench (benchflow/skillsbench): 86 of 87 tasks", each auto-graded 0-1. The model was "claude-sonnet-5, reasoning effort low (--effort low)", with "3 runs, about 240 billed trials, about USD 106 total." The skill arm was forced on, because "Caveman is user-activated. It triggers on phrases like "caveman mode" or "be brief"." Forcing makes "every number below is the skill's best case": in normal use "the realized saving can only be equal or lower than the roughly 10% ceiling measured here."

Results:

- **Tokens.** "at scale the saving converges to -8.5% (592k to 542k output tokens over 82 paired tasks)."
- **Quality.** "Sign test over the 18 non-ties: p = 0.82, far from any significant difference. Average task score was 0.326 for baseline vs. 0.311 for the skill arm".
- **Cost.** Per task the skill arm was cheaper, but the raw totals "showed the skill arm 11.6% more expensive: USD 40.60 vs. USD 36.39. The entire inversion came from a single trial".

## Why the saving is small

"Agentic output is different: code, diffs, tool invocations, and exact error strings dominate the token stream, and Caveman correctly leaves all of it verbatim. Only the narration between tool calls gets compressed, and there is not much of it." The verdict: "use it if you like it. It is fun, and it costs you nothing measurable in quality. Just do not expect huge savings on daily agentic tasks: a high-single-digit percentage is the realistic ceiling." Method lessons (small runs that did not replicate, forced activation as a ceiling) are in [Paired skill benchmarks](../skill-evals/paired-skill-benchmarks.md).

## For cardigan

Interpretation, not source claims:

- Caveman's exemptions (docs, tickets, "third-party messages", anything irreversible) are exactly cardigan's ground: office output is read by other people, so cardigan cannot borrow a terminal voice. Its keep-rules still transfer: never drop a negation, numbers and units exact, clarity beats compression.
- The control arm for cardigan's evals is "be concise", not no instruction; modern models already shorten on request, so cardigan must beat that.
- Phrasing rules move only the prose share of output. In office work prose is most of the output, so a voice rule would bite harder there than in coding, but the bigger lever is the one Caveman never pulls: not producing the deliverable at all.
- Skill triggered and skill effective are separate questions. An always-on skill like cardigan avoids the activation gap, but its evals should still check that the rules fired.
- Terseness and quality can be neutral to each other on graded tasks; cardigan should claim savings only where they are measured with a quality guard beside them.

## See Also

- [Paired skill benchmarks](../skill-evals/paired-skill-benchmarks.md)
- [Short messages](../practices/short-messages.md)
- [Skill comparison](skill-comparison.md)
