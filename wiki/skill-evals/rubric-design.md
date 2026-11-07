# Rubric design

> Sources: Shreya Shankar et al. (UC Berkeley, Université de Montréal), 2024-04-18; Hwanjun Song et al. (KAIST, AWS AI Labs), 2024-07-01; Eugene Yan, 2024-08-18; Hamel Husain, 2024-10-29; Anthropic Engineering ("Demystifying evals for AI agents"), 2026-01-09; Hamel Husain and Shreya Shankar (AI evals FAQ), 2026-09-18; Anthropic (Claude Platform docs, Define success criteria and build evaluations), undated; Anthropic (skill-creator SKILL.md and agents), undated
> Raw: [Who Validates the Validators?](../../raw/research/skill-evals/2024-04-18-shankar-who-validates-the-validators.md); [FineSurE: Fine-grained Summarization Evaluation using LLMs](../../raw/research/skill-evals/2024-07-01-song-finesure-keyfact-summarization-eval.md); [Evaluating the Effectiveness of LLM-Evaluators](../../raw/research/skill-evals/2024-08-18-eugene-yan-evaluating-llm-evaluators.md); [Using LLM-as-a-Judge For Evaluation: A Complete Guide](../../raw/research/skill-evals/2024-10-29-hamel-husain-llm-as-judge-critique-shadowing.md); [Demystifying evals for AI agents](../../raw/research/skill-evals/2026-01-09-anthropic-demystifying-evals-for-ai-agents.md); [AI Evals: Everything You Need to Know](../../raw/research/skill-evals/2026-09-18-husain-shankar-ai-evals-faq.md); [Define success criteria and build evaluations](../../raw/research/skill-evals/anthropic-docs-define-success-criteria-build-evals.md); [skill-creator: SKILL.md, grader, comparator, analyzer](../../raw/research/skill-evals/anthropic-skill-creator-eval-benchmark-method.md)
> Updated: 2026-11-02

## Overview

A rubric turns the question of whether an output is good into checks a grader can apply the same way every time. Shankar et al. (study; a qualitative user study with nine industry practitioners) found that criteria cannot be fully fixed before looking at outputs: grading outputs is how people discover what they care about. They call this criteria drift. They also found that some criteria, such as a word limit, are hard for humans to grade, and that LLM-based graders "simply inherit all the problems of the LLMs they evaluate, requiring further human validation." FineSurE (Song et al., study) shows the alternative to a single quality score: a list of key facts per input, scored for completeness and conciseness as percentages. Hamel Husain (practitioner) argues for pass/fail verdicts with written critiques instead of 1-5 scales, and for validating any LLM judge against a domain expert's labels before trusting it.

## Criteria drift

"We observed a "catch-22" situation: to grade outputs, people need to externalize and define their evaluation criteria; however, the process of grading outputs helps them to define that very criteria. We dub this phenomenon criteria drift, and it implies that it is impossible to completely determine evaluation criteria prior to human judging of LLM outputs." The drift continued after a first pass: "Even when participants graded first, we observed that they still refined their criteria upon further grading, even going back to change previous grades."

Drift changes both "definitions of existing criteria, and changes to the overall set of criteria". Some criteria also depend on what the model happens to produce: "some criteria appears dependent on the specific LLM outputs observed (rather than independent criteria that can be defined a priori)", which raises "serious questions for approaches that assume the independence of evaluation from observation of model outputs."

## What humans grade badly

Participants struggled because "some criteria are difficult for humans to grade (e.g., under a target word count)". Their trust in a grader also depended on its kind: "Participants' perceptions of alignment and needs varied based on the evaluator type (i.e., code-based vs. LLM-based)."

## Choosing the grading format

Eugene Yan's survey of LLM-evaluator papers (practitioner) separates three formats that "are not interchangeable":

- **Direct scoring** "evaluates a single response without needing an alternative for comparison". It suits "objective assessments such as measuring faithfulness to a source text or detecting policy violations such as toxicity."
- **Pairwise comparison** "chooses the better of two responses or declares a tie". It is "typically used—and more reliable—for subjective evals such as persuasiveness, tone, coherence, etc.", and "Studies show that pairwise comparisons lead to more stable results and smaller differences between LLM judgments and human annotations relative to direct scoring."
- **Reference-based** checks compare against a reference. The pyramid approach "first extracts semantic content units (SCUs) from the reference summary. The evaluator then checks if these SCUs are present in the generated summary."

Some questions fit only one format: "assessing faithfulness or instruction-following, don't fit the pairwise comparison paradigm. For example, a response is either faithful to the provided context or it is not".

### Binary outputs and how to measure agreement

Yan prefers binary verdicts: "where possible, I have my evaluators return binary outputs. This improves model performance while making it easier to apply classification metrics." He is "skeptical of correlation metrics. They don't account for chance agreement and thus could be overoptimistic (though Cohen's $\kappa$ is an exception)." The gap is visible in one study he cites: "Cohen's $\kappa$ between human and LLM judgments showed fair agreement of 0.3 - 0.5, while Kendall's $\tau$ and Spearman's $\rho$ was higher at 0.8 - 0.9."

## Pass/fail with a critique

Husain's guide (practitioner) rejects multi-dimension scales: "Arbitrary Scoring Systems: Using uncalibrated scales (like 1-5) across multiple dimensions, where the difference between scores is unclear and subjective. What makes something a 3 versus a 4? Nobody knows". His blunter version: "If your evaluations consist of a bunch of metrics that LLMs score on a 1-5 scale (or any other scale), you're doing it wrong."

His method, which he calls "Critique Shadowing", gives one domain expert one question: "Did the AI achieve the desired outcome?" The answer is "a clear pass or fail decision", plus "a critique that explains their reasoning." The critique has to carry weight: it "should be detailed enough so that you can use it in a few-shot prompt for a LLM judge", detailed enough "that a new employee could understand it. Being too terse is a common mistake."

How many examples: "I start with around 30 examples and keep going until I do not see any new failure modes." Like Shankar et al.'s criteria drift, he puts the data first: "You cannot write a good judge prompt until you've seen the data."

### Per-fact checks instead of scales

Husain and Shankar's evals FAQ (practitioner; distilled from teaching "5,000+ engineers and PMs", and flagged by the authors as "sharp opinions about what works in most cases. They are not universal truths.") gives the reasons against Likert scales: "the difference between adjacent points (like 3 vs 4) is subjective and inconsistent across annotators, detecting statistical differences requires larger sample sizes, and annotators often default to middle values to avoid making hard decisions."

Progress can still be tracked, by splitting a quality into binary parts: "instead of rating factual accuracy 1-5, you could track "4 out of 5 expected facts included" as separate binary checks." Composites are out for the same reason: "I discourage complicated weighted scores for the same reason I discourage Likert scales for LLM judges. If your dashboard reports a composite score that jumps from 3.2 to 3.7 week over week, it's easy to feel good about the increase without knowing what improved for users." So are off-the-shelf scores: generic metrics such as "helpfulness, coherence, quality" "measure abstract qualities that may not matter for your use case. Good scores on them don't mean your system works."

Cost points the same way: "Simple assertions and reference-based checks (comparing against known correct answers) are cheap to build and maintain. LLM-as-Judge evaluators require 100+ labeled examples, ongoing weekly maintenance, and coordination between developers, PMs, and domain experts."

### Validating the judge against the expert

The LLM judge prompt is iterated until it agrees with the expert; in his example "It took us only three iterations to achieve > 90% agreement between the LLM and Phillip." Agreement alone can mislead: "Raw agreement can be misleading when classes are imbalanced. Treat the human labels as ground truth and report the judge's True Positive Rate and True Negative Rate separately." The final number comes from data the prompt never saw: "Test set: Keep these examples hidden until you finish revising the prompt. Freeze the prompt, run the judge on the test set once, and use the result as your final estimate of the judge's performance."

The FAQ defines the two rates: "True positive rate (TPR), also called recall, measures how many actual failures the evaluator catches. [...] True negative rate (TNR) measures how many good outputs the evaluator correctly passes." Its short rule: "validate against human labels, separate training, development, and test examples, and measure TPR and TNR."

## Grader choice and per-dimension judges

Anthropic's agent-evals guide (official-docs) ranks graders: "We recommend choosing deterministic graders where possible, LLM graders where necessary or for additional flexibility, and using human graders judiciously for additional validation." Rubrics must be specific, because "vague rubrics produce inconsistent judgments."

For LLM judges it adds three habits. Calibrate them: "LLM-as-judge graders should be closely calibrated with human experts". Let them abstain: "To avoid hallucinations, give the LLM a way out, like providing an instruction to return "Unknown" when it doesn't have enough information." And split the work: "create clear, structured rubrics to grade each dimension of a task, and then grade each dimension with an isolated LLM-as-judge rather than using one to grade all dimensions." Multi-part tasks get partial credit ("For tasks with multiple components, build in partial credit."), and outcomes can be multidimensional, as in its example of a support agent: a state check (ticket resolved), a transcript constraint (under ten turns) and an LLM rubric for tone. None of this replaces reading: "You won't know if your graders are working well unless you read the transcripts and grades from many trials."

## Concrete rubrics (official docs)

Anthropic's platform docs (official-docs) ask for criteria that are "Specific" ("Instead of "good performance," specify "accurate sentiment classification."") and "Measurable", and note that "Most use cases need multidimensional evaluation along several success criteria." Their grading order matches the agent-evals guide: code-based grading is "Fastest and most reliable", LLM-based grading should be tested "to ensure reliability first, then scale", and human grading is "slow and expensive. Avoid if possible."

Their model rubric is a hard rule with an automatic fail: "The answer should always mention 'Acme Inc.' in the first sentence. If it does not, the answer is automatically graded as 'incorrect.'" Grader output should be constrained ("instruct the LLM to output only 'correct' or 'incorrect', or to judge from a scale of 1–5"), and the grader should think first: "Use a grader model with thinking on, so that it reasons before it produces an evaluation score."

> **Status: Disputed**
> Anthropic's platform docs offer "a scale of 1–5" as an acceptable constrained grader output. Husain says "If your evaluations consist of a bunch of metrics that LLMs score on a 1-5 scale (or any other scale), you're doing it wrong", Husain and Shankar's FAQ prefers separate binary checks, and Eugene Yan returns binary outputs "where possible". All of these are practitioner or documentation advice rather than head-to-head tests.

## Discriminating assertions

Anthropic's skill-creator grader (official-docs) has "two jobs: grade the outputs, and critique the evals themselves. A passing grade on a weak assertion is worse than useless — it creates false confidence." A pass needs "Clear evidence the expectation is true AND the evidence reflects genuine task completion, not just surface-level compliance"; a fail includes evidence that "is superficial (e.g., correct filename but empty/wrong content)". The goal is an assertion that is "*discriminating*: it passes when the skill genuinely succeeds and fails when it doesn't." Good assertions "are objectively verifiable and have descriptive names", and subjective qualities stay with people: "don't force assertions onto things that need human judgment."

## Key-fact checklists

The same guide names the pattern directly: "coverage checks define key facts a good answer must include".


FineSurE (Song et al., study; KAIST and AWS AI Labs) replaces a single Likert score for a summary with checks against a list of key facts. The motivation: "Traditional methods like ROUGE do not correlate well with human judgment, while recently proposed LLM-based metrics provide only summary-level assessment using Likert-scale scores."

"A keyfact refers to a concise sentence conveying a single key information, comprising at most 2-3 entities", and "The keyfact list can be generated automatically or by humans." An LLM then does two tasks, fact checking and keyfact alignment, which yield three percentages:

- **Faithfulness**: the share of output sentences that are factually correct.
- **Completeness**: "The summarizer ensures the inclusion of all keyfacts from the input text in the output summary." Scored as the share of key facts the output covers.
- **Conciseness**: "The summarizer refrains from incorporating information outside the keyfacts in the output, maintaining a succinct and focused summary." Scored as the share of output sentences that carry a key fact.

Their worked example: "the faithfulness score is 33%, since only one out of the three summary sentences is factually correct; the completeness score is 75%, since three out of the four keyfacts align with the summary; and the conciseness score is 66%, since two out of the three sentences are related to the keyfacts." The authors present percentages as "a more detailed assessment than Likert-scale scoring."

## For cardigan

Interpretation, not source claims:

- FineSurE's three scores fit cardigan almost directly: a short, human-written key-fact list per task (owners, deadlines, amounts, the ask, compliance wording) gives completeness; the share of sentences that carry a key fact gives conciseness; both sit beside raw length.
- Use direct binary checks for the objective items (each never-cut fact present, the ask answered, no unrequested section) and keep pairwise judging for the subjective question of which version a busy colleague would rather receive.
- Write each per-task criterion as a concrete auto-fail rule (for example, the reply must state the deadline given in the thread), and have the grader reason before its verdict.
- Track key-fact retention as N of M facts kept, each fact a separate binary check, and report the parts rather than one weighted cardigan score.
- Grade each criterion (real ask answered, never-cut items kept, lighter option taken where it fits) as pass/fail with a short written critique, not on a 1-5 scale. Have a human label a small calibration set first, then report the judge's true positive and true negative rates on a held-out set.
- Grade each criterion with its own judge call, allow "Unknown", and read a sample of transcripts with their grades before trusting any aggregate.
- Write cardigan's per-task criteria after reading a pilot batch of outputs, then freeze them before the scored runs. Re-opening criteria after seeing which arm won turns them into a fit to the result.
- Check numeric criteria (word counts, number of asks, presence of a date) with code, not with a human or LLM reader.
- Expect the never-cut list to grow during the pilot: grading real drafts will show facts and politeness moves that no list written in advance included.

## See Also

- [Guard metrics](guard-metrics.md)
- [LLM judge bias](llm-judge-bias.md)
