# LLM judge bias

> Sources: Peiyi Wang et al. (Peking University, HKU, Tencent Cloud AI), 2023-05-29; Lianmin Zheng et al. (LMSYS), 2023-06-09; Yann Dubois et al. (Stanford), 2024-04-06; Arjun Panickssery, Samuel R. Bowman, Shi Feng, 2024-04-15; Eugene Yan, 2024-08-18
> Raw: [Large Language Models are not Fair Evaluators](../../raw/research/skill-evals/2023-05-29-wang-llms-are-not-fair-evaluators.md); [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](../../raw/research/skill-evals/2023-06-09-zheng-judging-llm-as-a-judge-mt-bench.md); [Length-Controlled AlpacaEval](../../raw/research/skill-evals/2024-04-06-dubois-length-controlled-alpacaeval.md); [LLM Evaluators Recognize and Favor Their Own Generations](../../raw/research/skill-evals/2024-04-15-panickssery-llm-evaluators-favor-own-generations.md); [Evaluating the Effectiveness of LLM-Evaluators](../../raw/research/skill-evals/2024-08-18-eugene-yan-evaluating-llm-evaluators.md)
> Updated: 2026-10-31

## Overview

An LLM used as a judge can agree with people about as often as people agree with each other, but it has systematic biases that can decide a comparison on their own. Two studies set out the main ones. Position bias: the order in which two answers are shown changes which one wins (Wang et al.; Zheng et al.). Verbosity bias: judges favour longer answers even when they are not better (Zheng et al.). Self-preference: judges may favour their own model's output; Zheng et al. could not confirm it, but Panickssery et al. found it on summarization and linked it to the judge recognising its own text. The standard fixes are to score both orders and call disagreements a tie, make the judge reason before its verdict, and give it a reference answer. For a brevity skill, verbosity bias is the one that matters most, because it pushes every pairwise verdict towards the longer arm.

## How well judges agree with people

Zheng et al. (study; MT-Bench questions and Chatbot Arena votes) found that "strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans."

They also weigh the two judging formats. Pairwise comparison "may lack scalability when the number of players increases", while single-answer grading "may be unable to discern subtle differences between specific pairs, and its results may become unstable, as absolute scores are likely to fluctuate more than relative pairwise results if the judge model changes."

## Position bias

Wang et al. (study) "uncover a systematic bias in the evaluation paradigm of adopting large language models (LLMs), e.g., GPT-4, as a referee". The ranking of two candidate answers "can be easily hacked by simply altering their order of appearance in the context." Their example: "Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator."

Zheng et al. found the same across judges: "all of them exhibit strong position bias. Most LLM judges favor the first position." One judge also had a name bias: "Claude-v1 also shows a name bias which makes it favors "Assistant A"". "Only GPT-4 outputs consistent results in more than 60% of cases."

The bias is worst exactly where a brevity skill is tested: "position bias is more noticeable on open questions like writing and stem/humanity knowledge questions", and "more noticeable for models with close performance and can almost disappear when the performance of the two models differs a lot."

## Verbosity bias

"Verbosity bias is when an LLM judge favors longer, verbose responses, even if they are not as clear, high-quality, or accurate as shorter alternatives." Zheng et al. tested it by padding answers (an attack counted as successful "if an LLM judge thinks the new response is better than the old response") and concluded that "all LLMs may be prone to verbosity bias though GPT-4 defends significantly better than others."

The bias survives in benchmark use: Dubois et al. (study) found that an LLM-judged win rate swung from 22.9% to 64.3% when only the verbosity instruction to the same model changed, and correct for it by regressing out the length difference. See [Length as a gamed metric](length-goodhart.md).

Eugene Yan's survey (practitioner) restates the padding test from the MT-Bench work: the verbose distractors were MT-Bench answers that gpt-4 rephrased "without adding new information" and appended to the originals, and "Both claude-v1 and gpt-3.5 preferred the longer response more than 90% of the time". Another paper he cites "found that gpt-4 favored responses that provided more examples", which suggests "biases such as a bias towards giving higher scores and verbosity bias." Pairwise preferences also "vary significantly, even with semantically equivalent instructions."

## Judges miss defects

A judge that passes good outputs may still miss bad ones. In one study Yan summarises, "While the LLM-evaluator identified >95% of consistent summaries (high precision for good summaries), it only identified 30 - 60% of the inconsistent summaries (low recall for defects)." For a brevity skill, the defect that matters is a dropped fact, which is exactly the kind of miss a lenient judge lets through.

## Self-enhancement

Zheng et al. measured a lean towards a judge's own model ("GPT-4 favors itself with a 10% higher win rate; Claude-v1 favors itself with a 25% higher win rate"), but "they also favor other models and GPT-3.5 does not favor itself." Their conclusion is cautious: "Due to limited data and small differences, our study cannot determine whether the models exhibit a self-enhancement bias."

> **Status: Disputed**
> Zheng et al. (2023) could not determine whether self-enhancement exists. Panickssery, Bowman and Feng (2024, study) report it on two summarization tasks: "LLMs (GPT-3.5 Turbo, GPT-4, and Llama 2) disproportionately favor summaries written by themselves over those by other LLMs and from humans." The two used different tasks and designs, so the disagreement may be about where the bias shows rather than whether it exists.

Panickssery et al. define self-preference as "where an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality", and tie it to self-recognition. Out of the box, "All three LLMs we evaluate achieve over 50% accuracy at distinguishing their own outputs from other sources using simple prompts without fine-tuning. GPT-4 is 73.5% accurate distinguishing itself from two other LLMs and humans." Fine-tuning "leads to near-perfect self-recognition", and they find "a linear correlation between self-recognition capability and the strength of self-preference bias", a causal link that "resists straightforward confounders." The underlying worry: when one model is both evaluator and evaluatee, "the neutrality of the evaluator is in question".

## Fixes

- **Both orders, tie on disagreement.** Zheng et al.: "A conservative approach is to call a judge twice by swapping the order of two answers and only declare a win when an answer is preferred in both orders. If the results are inconsistent after swapping, we can call it a tie." Wang et al.'s version averages instead: "we evaluate each candidate in both positions across two runs and compute the final score as the average of the two runs."
- **Evidence before score.** Wang et al.: "We prompt the model to generate evaluation evidence before assigning scores", with an ensemble over several such runs "to further stabilize the evaluation."
- **Humans for hard cases.** Wang et al. use an entropy measure over orderings to flag difficult examples and seek "human assistance when needed."
- **Few-shot examples.** These "can significantly increase the consistency of GPT-4 from 65.0% to 77.5%. However, high consistency may not imply high accuracy and we are not sure whether the few-shot examples will introduce new biases."
- **Reference answer.** In the reference-guided method the judge first answers the question itself, then sees that answer as a reference; Zheng et al. report "a significant improvement in failure rate (from 70% to 15%) over the default prompt."

## For cardigan

Interpretation, not source claims:

- Every pairwise judgment in cardigan's evals (cardigan vs no skill, cardigan vs a "be brief" control) should run in both orders, with a win only when both orders agree; flipped verdicts count as ties.
- Expect verbosity bias against cardigan in any open comparison of which output is better. Do not read a loss or a tie on reader preference as proof that the shorter output is worse until the content checks agree.
- cardigan's tasks (open writing, two arms often close in quality) are where position bias is strongest, so order effects are not a minor correction here.
- Ask the judge for its reasons before its verdict, and give it a reference: for office tasks, the list of facts and the ask the output must carry.
- A judge saying "nothing important was cut" is weak evidence on its own; check its recall on outputs with a fact deliberately removed, and spot-check with a human.
- Both arms of a cardigan eval come from the same model, so self-preference does not favour one arm directly. But a style the judge recognises (a terse register, a fixed ending) can unblind it; cross-check verdicts with a judge from another model family or a human sample.
- Random order per pair (as in ponytail's reply judge) balances position bias across many pairs but does not remove it from any single verdict; both-order scoring does.

## See Also

- [Guard metrics](guard-metrics.md)
- [Paired skill benchmarks](paired-skill-benchmarks.md)
- [Length as a gamed metric](length-goodhart.md)
