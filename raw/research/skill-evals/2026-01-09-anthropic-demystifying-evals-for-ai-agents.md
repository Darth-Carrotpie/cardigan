# Demystifying evals for AI agents

> Source: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
> Collected: 2026-10-31
> Published: 2026-01-09
> Author: Anthropic Engineering
> Type: official-docs

## Excerpts

> Each attempt at a task is a trial. Because model outputs vary between runs, we run multiple trials to produce more consistent results.

> pass^k measures the probability that all k trials succeed. [...] If your agent has a 75% per-trial success rate and you run 3 trials, the probability of passing all three is (0.75)³ ≈ 42%. This metric especially matters for customer-facing agents where users expect reliable behavior every time.

> We see teams delay building evals because they think they need hundreds of tasks. In reality, 20-50 simple tasks drawn from real failures is a great start. After all, in early agent development, each change to the system often has a clear, noticeable impact, and this large effect size means small sample sizes suffice. More mature agents may need larger, more difficult evals to detect smaller effects

> A good task is one where two domain experts would independently reach the same pass/fail verdict. [...] Ambiguity in task specifications becomes noise in metrics. The same applies to criteria for model-based graders: vague rubrics produce inconsistent judgments.

> Test both the cases where a behavior should occur and where it shouldn't. One-sided evals create one-sided optimization. For instance, if you only test whether the agent searches when it should, you might end up with an agent that searches for almost everything. Try to avoid class-imbalanced evals.

> Each trial should be "isolated" by starting from a clean environment. [...] For example, in some internal evals we observed Claude gaining an unfair advantage on some tasks by examining the git history from previous trials.

> We recommend choosing deterministic graders where possible, LLM graders where necessary or for additional flexibility, and using human graders judiciously for additional validation.

> For tasks with multiple components, build in partial credit.

> LLM-as-judge graders should be closely calibrated with human experts [...] To avoid hallucinations, give the LLM a way out, like providing an instruction to return "Unknown" when it doesn't have enough information. It can also help to create clear, structured rubrics to grade each dimension of a task, and then grade each dimension with an isolated LLM-as-judge rather than using one to grade all dimensions.

> You won't know if your graders are working well unless you read the transcripts and grades from many trials.

> coverage checks define key facts a good answer must include

> Success for conversational agents can be multidimensional: is the ticket resolved (state check), did it finish in <10 turns (transcript constraint), and was the tone appropriate (LLM rubric)?

## Collector's note

Anthropic's general guide to agent evals: trials vs tasks, pass@k vs pass^k, grader hierarchy (code > LLM > human), isolated per-dimension LLM judges with an "Unknown" escape, two-sided evals, clean environments, and reading transcripts. For cardigan: include tasks where brevity should NOT apply (e.g. a document that legitimately needs detail) so the skill is not rewarded for always cutting; use a key-facts coverage check per task; grade each criterion with a separate judge call; and consider pass^3 (all three runs pass never-cut items) as the reliability bar.
