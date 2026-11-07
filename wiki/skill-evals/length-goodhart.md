# Length as a gamed metric

> Sources: Prasann Singhal, Tanya Goyal, Jiacheng Xu, Greg Durrett (UT Austin), 2023-10-05; Yann Dubois, Balázs Galambosi, Percy Liang, Tatsunori B. Hashimoto (Stanford), 2024-04-06
> Raw: [A Long Way to Go: Investigating Length Correlations in RLHF](../../raw/research/skill-evals/2023-10-05-singhal-length-correlations-in-rlhf.md); [Length-Controlled AlpacaEval](../../raw/research/skill-evals/2024-04-06-dubois-length-controlled-alpacaeval.md)
> Updated: 2026-10-31

## Overview

Length is easy to measure and easy to move, so any score that correlates with length tends to end up measuring length. Singhal et al. (study) showed this for RLHF: learned reward scores track response length so closely that a reward based on length alone reproduces most of the measured improvement. Dubois et al. (study) showed it for LLM-judged win rates: telling the same model to be more or less verbose moved its win rate from 22.9% to 64.3%, and a regression that removes the length term cut that swing sharply. The direction in both is that longer looks better; a brevity skill faces the mirror case, where "shorter" is the tempting single number and a raw judged win rate is biased against it.

## Reward tracks length

"RLHF also often drives models to produce longer outputs." Across three settings the authors find "improvements in reward to largely be driven by increasing response length, instead of other features. Indeed, we find that even a purely length-based reward reproduces most downstream RLHF improvements over supervised fine-tuned models." Their Figure 1 shows that "reward scores are strongly correlated with length."

The source of the bias is the scorer, not the optimiser: "we identify the dominant source of these biases to be reward models, which, by studying training dynamics, we find are non-robust and easily influenced by length biases in preference data." The open question they pose is "to what extent length is a meaningful feature vs. a spurious correlation that PPO optimizes for."

## Judged win rates are length-gameable

Dubois et al. (study; Stanford, on the AlpacaEval benchmark) show the same confounder in LLM-judged evaluation: "Even simple, known confounders such as preference for longer outputs remain in existing automated evaluation metrics." AlpacaEval, "Despite being highly correlated with human preferences", "is known to favor models that generate longer outputs." Judges exploit "spurious correlations such as the length of the output, the presence of lists, or various position biases".

They define the failure: "We call a metric length gameable if simply prompting the model to be more or less verbose significantly affects the metric outcome." It is large. With only the verbosity instruction changed, "The baseline model (gpt4_1106_preview) fluctuates from 22.9% to 64.3%".

### The length-controlled fix

They "fit a generalized linear model to predict the biased auto-annotator's preferences based on the mediators we want to control for (length difference) and other relevant features", then "zero out the "length of output" term to obtain counterfactual estimates of AlpacaEval win rate." With length controlled, the same model's win rates "now only fluctuate from 41.9% to 51.6%", and "the normalized standard deviation across the three verbosity prompts decreases from 25% to 10%". The adjusted metric also tracks human rankings better: Spearman correlation with Chatbot Arena rises "from 0.94 to 0.98."

Their stated goals are ones a brevity eval shares: "evaluations that prioritize the content rather than the style of the answer", and a benchmark that is not "too dependent on the prompting strategy".

## For cardigan

Interpretation, not source claims:

- "Shorter" must never count as a win on its own in cardigan's evals. Report length beside independent content checks (facts kept, ask answered), so a skill that just truncates is caught.
- The lesson runs both ways: a judge or score that rewards length will undervalue cardigan, and one told to reward brevity can be gamed by cutting content.
- A raw pairwise win rate against a longer arm is biased against cardigan. Report it next to the length difference, and where possible compare outputs with the same content at different lengths, or adjust for length as Dubois et al. do.
- A "be brief" one-line control arm tests length gameability directly: if a verbosity instruction alone moves the score as much as cardigan does, the score is measuring length.
- When cardigan's rules are tuned against an eval, check that gains on the score are not just changes in length.

## See Also

- [Guard metrics](guard-metrics.md)
- [LLM judge bias](llm-judge-bias.md)
