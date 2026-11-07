# Question, then default

> Sources: Nicholas Edwards, Sebastian Schuster (University of Vienna), 2026-03-27; Jeff Bezos / Amazon, undated (2016 letter to shareholders); Alison Wood Brooks, Francesca Gino, Maurice E. Schweitzer, undated (Management Science, 2015); Anthropic (anthropics/skills, discernment-nudge), 2026-08-17
> Raw: [Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents](../../raw/research/pushback/2026-03-27-ask-or-assume-clarification-coding-agents.md); [2016 Letter to Shareholders](../../raw/research/pushback/amazon-2016-shareholder-letter-disagree-and-commit.md); [Smart People Ask for (My) Advice: Seeking Advice Boosts Perceptions of Competence](../../raw/research/pushback/brooks-gino-schweitzer-seeking-advice-boosts-competence.md); [Anthropic skills: discernment-nudge](../../raw/research/agent-skills/2026-08-17-anthropic-discernment-nudge-skill.md)
> Updated: 2026-10-31

## Overview

When a request is underspecified, an assistant can ask or proceed on an assumption. Asking about everything burdens the requester; never asking produces wrong work. Evidence from coding agents favours a calibrated middle: detect whether the ambiguity actually matters, ask only then, and otherwise proceed. Asking the right question also does not make the asker look weak: substantive questions on hard tasks raise perceived competence. For cardigan this becomes one rule: ask a question only when a wrong guess would derail the deliverable, and otherwise deliver a sensible default with the assumption stated.

## Calibrated asking in agents

Edwards and Schuster (study; an arXiv preprint testing agents on software-engineering tasks with underspecified instructions) start from the gap between people and agents: "While human developers naturally resolve underspecification by asking clarifying questions, current agents are largely optimized for autonomous execution."

Their fix separates two jobs: "We propose an uncertainty-aware multi-agent scaffold that decouples underspecification detection from code execution." The result: "our scaffold achieves a 69.40% task resolve rate, significantly outperforming a standard single-agent setup and closing the performance gap with agents operating on fully specified instructions."

The asking was selective, not constant: "the multi-agent system exhibits well-calibrated information-seeking behavior, conserving queries on simple tasks while proactively seeking information on more complex issues."

The domain is coding agents, not office work, and the claims rest on the authors' abstract; the transfer to office requests is interpretation.

## Asking does not look weak

People hold back questions out of a misplaced fear. Brooks, Gino and Schweitzer (study; experiments published in Management Science) write: "We find that people are reticent to seek advice for fear of appearing incompetent. This fear, however, is misplaced." The finding: "We demonstrate that individuals perceive those who seek advice as more competent than those who do not."

The gain has conditions: "This effect is moderated by task difficulty, advisor egocentrism, and advisor expertise." Specifically, advice-seekers look more competent "when the task is difficult rather than when it is easy, when people seek advice from them personally rather than when they seek advice from others and when people seek advice from experts rather than from nonexperts or not at all."

## Deciding with partial information

A management rule points the same way. Jeff Bezos (practitioner; Amazon's 2016 shareholder letter) argues that "most decisions should probably be made with somewhere around 70% of the information you wish you had." Waiting for every clarification is itself a cost. See [Disagree and commit](disagree-and-commit.md).

## Questions after the answer

Anthropic's discernment-nudge agent skill (repo) handles the other end of a reply: optional follow-up questions that help the user check what was produced. It puts the work first ("Always answer the question completely first. The nudge comes after, and it should be easy to skip."), limits itself to "Two or three prompts, never more" and "at most once per conversation", and treats "Silence is the right default". A user who asked for the quick version is not nudged, because that "lands as paternalistic". See [Office workflow skills](../agent-skills/office-workflow-skills.md#discernment-nudge-silence-as-the-default).

## For cardigan

Interpretation, not source claims:

- Decide *whether to ask* as a separate step before producing anything. Ask only when the missing fact (purpose, audience, format, deadline) would change the deliverable substantially.
- On simple or low-stakes requests, do not ask. Deliver the light default and state the assumption in one line (*Assumed this is for the team, not the board; say if not*).
- When cardigan does ask, it still delivers a default alongside the question, so a slow reply does not block the work. The question goes to the requester directly and is about something substantive (purpose, audience), which is when asking reads as competence (Brooks and colleagues); questions about trivia get no such credit.
- Evals should score both failure modes: over-asking on simple requests and silently guessing on ambiguous high-stakes ones.

## See Also

- [Saying no](saying-no.md)
- [Speaking up (employee voice)](speaking-up.md)
- [Keep promises, don't exceed them](keep-not-exceed.md)
- [Disagree and commit](disagree-and-commit.md)
- [Office workflow skills](../agent-skills/office-workflow-skills.md)
