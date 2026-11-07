# Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents

> Source: https://arxiv.org/abs/2603.26233
> Collected: 2026-10-31
> Published: 2026-03-27
> Author: Nicholas Edwards, Sebastian Schuster (University of Vienna)
> Type: study

## Excerpts

> As Large Language Model (LLM) agents are increasingly deployed in open-ended domains like software engineering, they frequently encounter underspecified instructions that lack crucial context. While human developers naturally resolve underspecification by asking clarifying questions, current agents are largely optimized for autonomous execution.

> We propose an uncertainty-aware multi-agent scaffold that decouples underspecification detection from code execution. Across both proprietary and open-weight frontier LLMs, our scaffold achieves a 69.40% task resolve rate, significantly outperforming a standard single-agent setup and closing the performance gap with agents operating on fully specified instructions.

> Furthermore, we find that the multi-agent system exhibits well-calibrated information-seeking behavior, conserving queries on simple tasks while proactively seeking information on more complex issues.

From alphaXiv's generated overview on the v2 page (https://www.alphaxiv.org/abs/2603.26233v2); this wording is not in the paper text itself:

> An agent that asks questions for every minor detail (overclarification) becomes a burden to the user,

> while an agent that never asks (underclarification) remains prone to error.

> refraining from asking when it determines the task is straightforward

> only intervening when the ambiguity is likely to impede success

## Collector's note

An empirical study on an underspecified variant of SWE-bench Verified (v1 27 Mar 2026; v3 7 Sep 2026). Splitting "is this underspecified?" from execution raised resolve rates to near the fully-specified ceiling, with the agent asking only when the ambiguity would block success. Secondary write-ups say one model over-asked (87% ask rate) without benefit. The domain is coding, not office work, but cardigan can borrow the rule directly: ask only when a wrong guess would derail the deliverable, otherwise proceed on a stated assumption. That matches the "question in one line, still deliver a default" design.
