# cardigan

*She reads the whole thread, replies with one line, and it's enough.*

cardigan is an always-on agent skill for everyday office work: email, chat, meetings, documents, decks, spreadsheets, reports, status updates and planning. It decides **what** to produce, which is often less than asked for: a one-line reply, a link to something that already exists, a calendar poll instead of a scheduling thread, or nothing at all. It never cuts facts, owners, deadlines, compliance wording, the actual ask, or basic politeness. How the prose reads is out of scope; pair cardigan with a terse-prose or anti-slop skill for that.

The idea and the mechanics come from [ponytail](https://github.com/DietrichGebert/ponytail) (MIT) by Dietrich Gebert, the "lazy senior developer" coding skill: a ladder with early exit, read fully then be lazy, a never-cut list, a fixed reply ending, and intensity levels. cardigan carries that over to the office, in the person of the veteran colleague in the cardigan who has survived every reply-all storm.

**Status:** in development. Research (Phase 1) is done. The skill itself is not written yet.

## Install

Not released yet. When it is, `skills/cardigan/SKILL.md` will install as a Claude Code skill, like ponytail.

## The ladder and levels (draft, being decided)

Stop at the first rung that holds:

1. Does this deliverable need to exist? (A meeting that could be an email, an email that needs no reply, a report nobody reads.)
2. Does it already exist? (A past deck, template or answer in your Drive, Notion or mail.)
3. Can a built-in tool feature do it? (A calendar poll, a Sheets filter view, a mail rule, an approvals app.)
4. Does it belong to an existing process or owner? (A form, a ticket queue, a person.)
5. Can it be one line or a link?
6. Only then: the shortest deliverable that answers the real ask.

Levels: **lite** (deliver what was asked, name the lighter option in one line), **full** (default: the ladder), **ultra** (also question the request first). The rungs, wording and levels are being decided in Phase 3. See [DECISIONS.md](DECISIONS.md).

## How the knowledge base works

cardigan's rules are drawn from research kept in an LLM wiki (Karpathy's pattern, via the [karpathy-llm-wiki](.claude/skills/karpathy-llm-wiki/SKILL.md) project skill):

- `raw/research/<area>/` holds immutable source notes, one per source: verbatim excerpts, URL and dates.
- `wiki/` holds compiled topic articles. Each one cites its raw notes, flags disputed or outdated claims, and ends with a "For cardigan" section. Start at [wiki/index.md](wiki/index.md); [wiki/log.md](wiki/log.md) records every operation.
- **Ingest** adds a source to `raw/`, then merges it into the wiki. **Query** answers from the wiki with citations. **Lint** checks the index, links, and that every number and quote is present in its raw note (`check_evidence.py`).

The current wiki has 50 articles in 7 topics (office waste, practices, review practice, pushback, native tool features, agent skills, skill evals), built from 117 sources.

## Renewing the research

[RESEARCH.md](RESEARCH.md) lists the research questions, scope, every search query, rejected sources, known gaps and a step-by-step renewal procedure. [`tools/verify_excerpts.py`](tools/verify_excerpts.py) checks that new notes quote their sources verbatim before they are compiled.

## Evals

As in ponytail, the same agent runs a set of realistic office tasks (`evals/tasks/`) with and without the skill, 3 runs each. Each run is graded on per-task pass/fail checks: real ask answered, never-cut items kept, lighter option taken where one existed, plus length, time and tokens. Reports go to `evals/results/`.

**Latest result:** none yet. The baseline run (Phase 2) is next.

## License

To be decided. Ponytail itself is MIT.
