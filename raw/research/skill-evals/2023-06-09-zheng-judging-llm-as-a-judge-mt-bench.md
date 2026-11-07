# Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

> Source: https://arxiv.org/abs/2306.05685 (HTML v4: https://arxiv.org/html/2306.05685v4)
> Collected: 2026-10-31
> Published: 2023-06-09
> Author: Lianmin Zheng, Wei-Lin Chiang, Ying Sheng et al. (LMSYS; NeurIPS 2023 Datasets and Benchmarks)
> Type: study

## Excerpts

> Our results reveal that strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans.

> the pairwise comparison may lack scalability when the number of players increases, given that the number of possible pairs grows quadratically; single answer grading may be unable to discern subtle differences between specific pairs, and its results may become unstable, as absolute scores are likely to fluctuate more than relative pairwise results if the judge model changes.

> Position bias is when an LLM exhibits a propensity to favor certain positions over others.

> As in Table 2, we found all of them exhibit strong position bias. Most LLM judges favor the first position. Claude-v1 also shows a name bias which makes it favors "Assistant A", as illustrated by the "rename" prompt. The position bias can be very significant. Only GPT-4 outputs consistent results in more than 60% of cases.

> Verbosity bias is when an LLM judge favors longer, verbose responses, even if they are not as clear, high-quality, or accurate as shorter alternatives.

> We define the attack is successful if an LLM judge thinks the new response is better than the old response. [...] demonstrating that all LLMs may be prone to verbosity bias though GPT-4 defends significantly better than others.

> GPT-4 favors itself with a 10% higher win rate; Claude-v1 favors itself with a 25% higher win rate. However, they also favor other models and GPT-3.5 does not favor itself.

> Due to limited data and small differences, our study cannot determine whether the models exhibit a self-enhancement bias.

> A conservative approach is to call a judge twice by swapping the order of two answers and only declare a win when an answer is preferred in both orders. If the results are inconsistent after swapping, we can call it a tie.

> the few-shot judge can significantly increase the consistency of GPT-4 from 65.0% to 77.5%. However, high consistency may not imply high accuracy and we are not sure whether the few-shot examples will introduce new biases.

> we propose a reference-guided method, in which we first generate LLM judge's answer independently, and then display it as a reference answer in the judge prompt. [...] we see a significant improvement in failure rate (from 70% to 15%) over the default prompt.

> As shown in Table 10, position bias is more noticeable on open questions like writing and stem/humanity knowledge questions. [...] the position bias is more noticeable for models with close performance and can almost disappear when the performance of the two models differs a lot.

## Collector's note

The foundational LLM-judge bias paper: MT-Bench (80 multi-turn questions) and Chatbot Arena votes, with GPT-4/GPT-3.5/Claude-v1 as judges. Documents position bias, verbosity bias (a "repetitive list" attack fooled Claude-v1 and GPT-3.5 91.3% of the time, GPT-4 8.7%, on 23 answers), and inconclusive self-enhancement. For cardigan, verbosity bias works directly against a brevity skill in pairwise judging, and position bias is strongest on open writing tasks between close outputs — exactly cardigan's case — so every pairwise judgment should be run in both orders, with inconsistent results counted as ties.
