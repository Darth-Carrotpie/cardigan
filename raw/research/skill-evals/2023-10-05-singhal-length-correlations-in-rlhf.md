# A Long Way to Go: Investigating Length Correlations in RLHF

> Source: https://arxiv.org/abs/2310.03716 (HTML v2: https://arxiv.org/html/2310.03716v2)
> Collected: 2026-10-31
> Published: 2023-10-05
> Author: Prasann Singhal, Tanya Goyal, Jiacheng Xu, Greg Durrett (UT Austin)
> Type: study

## Excerpts

> RLHF also often drives models to produce longer outputs. This paper demonstrates, on three diverse settings, that optimizing for response length is, much more than previously thought, a significant factor behind RLHF.

> Studying the strategies RL optimization uses to maximize reward, we find improvements in reward to largely be driven by increasing response length, instead of other features. Indeed, we find that even a purely length-based reward reproduces most downstream RLHF improvements over supervised fine-tuned models.

> Testing a comprehensive set of length-countering interventions, we identify the dominant source of these biases to be reward models, which, by studying training dynamics, we find are non-robust and easily influenced by length biases in preference data.

> Figure 1: Log-scaled heatmap of lengths of SFT outputs vs. learned reward model scores for WebGPT (left). The graph shows that reward scores are strongly correlated with length. RLHF with these consistently leads to longer outputs (right).

> In this paper, we study this phenomenon in depth to understand its underlying causes, and to what extent length is a meaningful feature vs. a spurious correlation that PPO optimizes for.

## Collector's note

Goodhart case study in the opposite direction from cardigan: learned preference scores are so length-correlated that a pure length reward reproduces most RLHF "improvement". The lesson transfers symmetrically — any single scalar that correlates with length (shorter or longer) will be optimised for length rather than quality. cardigan's evals should never let "shorter" count as a win on its own; length must be reported next to independent content checks (key facts retained, ask answered) so a skill that just truncates is caught.
