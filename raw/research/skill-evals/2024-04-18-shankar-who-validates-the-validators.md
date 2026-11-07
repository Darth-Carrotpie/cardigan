# Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences

> Source: https://arxiv.org/abs/2404.12272 (HTML v1: https://arxiv.org/html/2404.12272v1)
> Collected: 2026-10-31
> Published: 2024-04-18
> Author: Shreya Shankar, J.D. Zamfirescu-Pereira, Björn Hartmann, Aditya G. Parameswaran, Ian Arawjo (UC Berkeley, Université de Montréal)
> Type: study

## Excerpts

> Yet LLM-generated evaluators simply inherit all the problems of the LLMs they evaluate, requiring further human validation.

> In particular, we identify a phenomenon we dub criteria drift: users need criteria to grade outputs, but grading outputs helps users define criteria. What is more, some criteria appears dependent on the specific LLM outputs observed (rather than independent criteria that can be defined a priori), raising serious questions for approaches that assume the independence of evaluation from observation of model outputs.

> We observed a "catch-22" situation: to grade outputs, people need to externalize and define their evaluation criteria; however, the process of grading outputs helps them to define that very criteria. We dub this phenomenon criteria drift, and it implies that it is impossible to completely determine evaluation criteria prior to human judging of LLM outputs. Even when participants graded first, we observed that they still refined their criteria upon further grading, even going back to change previous grades.

> then ran a qualitative user study with nine (9) industry practitioners that use LLMs in production contexts.

> Participants struggled to align assertions with their preferences due to two main challenges in grading: (i) some criteria are difficult for humans to grade (e.g., under a target word count), and (ii) as they grade more LLM outputs, we observe a criteria drift phenomenon, in which criteria change as participants grade more LLM outputs (both definitions of existing criteria, and changes to the overall set of criteria).

> Participants' perceptions of alignment and needs varied based on the evaluator type (i.e., code-based vs. LLM-based).

## Collector's note

HCI study (EvalGen in ChainForge, 9 practitioners, NER-on-tweets task) on aligning LLM-generated assertions with human grades; coins "criteria drift". This sits in tension with pre-registering criteria (JetBrains): cardigan should look at a pilot batch of outputs to settle per-task criteria, then freeze them before the scored 3-run comparison, and note that numeric criteria like word limits are better checked by code than by humans or LLMs.
