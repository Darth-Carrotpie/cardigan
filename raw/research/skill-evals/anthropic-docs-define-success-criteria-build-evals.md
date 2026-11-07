# Define success criteria and build evaluations

> Source: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
> Collected: 2026-10-31
> Published: Unknown
> Author: Anthropic (Claude Platform docs)
> Type: official-docs

## Excerpts

> Define measurable success criteria for your LLM application and build evaluations to test it, from exact match checks to LLM-based grading.

> Specific: Clearly define what you want to achieve. Instead of "good performance," specify "accurate sentiment classification."

> Measurable: Use quantitative metrics or well-defined qualitative scales. Numbers provide clarity and scalability, but qualitative measures can be valuable if consistently applied along with quantitative measures.

> Most use cases need multidimensional evaluation along several success criteria.

> Be task-specific: Design evals that mirror your real-world task distribution. Don't forget to factor in edge cases!

> Automate when possible: Structure questions to allow for automated grading (for example, multiple-choice, string match, code-graded, LLM-graded).

> Prioritize volume over quality: More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals.

> Code-based grading: Fastest and most reliable, extremely scalable, but also lacks nuance for more complex judgments that require less rule-based rigidity. [...]
> Human grading: Most flexible and high quality, but slow and expensive. Avoid if possible.
> LLM-based grading: Fast and flexible, scalable and suitable for complex judgment. Test to ensure reliability first, then scale.

> Have detailed, clear rubrics: "The answer should always mention 'Acme Inc.' in the first sentence. If it does not, the answer is automatically graded as 'incorrect.'"

> A given use case, or even a specific success criterion for that use case, might require several rubrics for holistic evaluation.

> Be empirical or specific: For example, instruct the LLM to output only 'correct' or 'incorrect', or to judge from a scale of 1–5. Purely qualitative evaluations are hard to assess quickly and at scale.

> Encourage reasoning: Use a grader model with thinking on, so that it reasons before it produces an evaluation score. This increases evaluation performance, particularly for tasks requiring complex judgment.

## Collector's note

Anthropic's official "develop tests" page: SMART-style success criteria, multidimensional evaluation, grading-method hierarchy (code > LLM > human), and LLM-grader tips (concrete rubrics, constrained output, reasoning first). Its "volume over quality" advice is in tension with cardigan's small 10–12-task design, and its ROUGE/cosine examples are criticised elsewhere (Husain/Shankar FAQ). For cardigan: write each per-task criterion as a concrete, auto-fail-style rule ("must state the deadline of 14 Nov") and have the grader reason before verdict.
