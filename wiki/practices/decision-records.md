# Decision records

> Sources: Michael Nygard, 2011-11-15; GitLab Inc., undated
> Raw: [Documenting Architecture Decisions](../../raw/research/practices/2011-11-15-nygard-documenting-architecture-decisions.md); [GitLab Communication (The GitLab Handbook)](../../raw/research/practices/gitlab-handbook-communication.md)
> Updated: 2026-10-31

## Overview

A decision record is a short, standalone note of one decision: its context, the decision, its status and its consequences. Michael Nygard's Architecture Decision Records (ADRs) come from software, but the format carries over to any office decision log. Its central claim is that the rationale is the part later readers most need.

## Why record the why

Nygard (practitioner, Cognitect) starts from a common problem: "One of the hardest things to track during the life of a project is the motivation behind certain decisions." A newcomer who lacks "the rationale or consequences" can only accept the decision blindly or reverse it blindly, and "It's better to avoid either blind acceptance or blind reversal."

## The format

- **Title.** "These documents have names that are short noun phrases."
- **Context.** "the forces at play, including technological, political, social, and project local."
- **Decision.** "It is stated in full sentences, with active voice."
- **Status.** For example, proposed before stakeholders agree, then accepted (the status values appear here only in the collector's paraphrase).
- **Consequences.** "the resulting context, after applying the decision."

Length: "The whole document should be one or two pages long." Tone: "We will write each ADR as if it is a conversation with a future developer."

## The same rule elsewhere

GitLab's handbook (official-docs) compresses the point into four words of advice: "say why, not just what."

## For cardigan

Interpretation, not source claims:

- For a request to write up what was decided, cardigan's default output is a five-part record (title, context, decision, status, consequences), not full meeting minutes.
- The rationale is on the never-cut list in spirit: a decision written without its reason forces later readers into blind acceptance or blind reversal.
- One decision per record matches the one-topic rule for messages; several decisions from one meeting become several short records or rows in a log.
- One or two pages is the ceiling, not the target; many office decisions fit in a few lines.

## See Also

- [Single source of truth](single-source-of-truth.md)
- [Short messages](short-messages.md)
- [Approvals](../native-features/approvals.md)
