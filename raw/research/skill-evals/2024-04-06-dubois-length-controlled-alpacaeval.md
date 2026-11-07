# Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators

> Source: https://arxiv.org/abs/2404.04475 (HTML v2: https://arxiv.org/html/2404.04475v2)
> Collected: 2026-10-31
> Published: 2024-04-06
> Author: Yann Dubois, Balázs Galambosi, Percy Liang, Tatsunori B. Hashimoto (Stanford)
> Type: study

## Excerpts

> Even simple, known confounders such as preference for longer outputs remain in existing automated evaluation metrics.

> Despite being highly correlated with human preferences, AlpacaEval is known to favor models that generate longer outputs.

> To achieve this, we first fit a generalized linear model to predict the biased auto-annotator's preferences based on the mediators we want to control for (length difference) and other relevant features.

> Length-controlling not only improves the robustness of the metric to manipulations in model verbosity, we also find that it increases the Spearman correlation with LMSYS Chatbot Arena from 0.94 to 0.98.

> they often do so by exploiting spurious correlations such as the length of the output, the presence of lists, or various position biases

> then we zero out the "length of output" term to obtain counterfactual estimates of AlpacaEval win rate.

> Decreasing length gameability: We call a metric length gameable if simply prompting the model to be more or less verbose significantly affects the metric outcome.

> First, we would like evaluations that prioritize the content rather than the style of the answer. Second, the benchmark should not be too dependent on the prompting strategy as users usually think of evaluations of models rather than the entire system, which includes the prompt.

> The baseline model (gpt4_1106_preview) fluctuates from 22.9% to 64.3% by varying the verbosity instruction in the prompt.

> In contrast, the length-controlled AlpacaEval has significantly lower gameability (gpt4_1106_preview's win rates now only fluctuate from 41.9% to 51.6%), and rankings are generally stable to verbosity prompts. Quantitatively, the normalized standard deviation across the three verbosity prompts decreases from 25% to 10% from the length control.

## Collector's note

Shows that an LLM-judged win rate can swing from 22.9% to 64.3% purely by telling the same model to be concise vs verbose, and corrects for it with a regression that zeroes out the length term. For cardigan this cuts both ways: a raw pairwise win rate will be biased against the shorter cardigan arm, so report win rate alongside length and ideally a length-adjusted or "same content, different length" comparison; and a judge that is told to reward brevity could be gamed the other way.
