# Reviewing a draft

> Sources: Craig Silverman / Poynter, 2012-01-10; Jon Sanger / Government Digital Service, 2013-07-31; Benjamin Mortimer / Government Digital Service, 2017-02-06; Hurley Write, 2024-02-27; Barbara Minto / Minto Books International, undated; Anthropic (doc-coauthoring skill), 2025-12-04
> Raw: [Copy editors' advice for the new year: 'Slow down'](../../raw/research/review-practice/2012-01-10-poynter-copy-editors-slow-down.md); [Editorial reviews and mainstream content](../../raw/research/review-practice/2013-07-31-govuk-editorial-reviews-2i-mainstream.md); [Talk more, queue less: faster updates for GOV.UK](../../raw/research/review-practice/2017-02-06-govuk-talk-more-queue-less-2i-review.md); [Optimizing Your Team's Editing and Review Process](../../raw/research/review-practice/2024-02-27-hurley-write-optimizing-editing-review.md); [The Minto Pyramid Principle: Concept / Course](../../raw/research/review-practice/minto-pyramid-principle-concept-and-course.md); [Anthropic skills: doc-coauthoring](../../raw/research/agent-skills/2025-12-04-anthropic-doc-coauthoring-skill.md)
> Updated: 2026-10-31

## Overview

How a reviewer should work on someone else's draft (or on their own): check it against the original request, read the whole thing before changing anything, raise big risks early, fix small things directly, and leave correct text alone, because editing can add errors as well as remove them. The evidence is practitioner advice from newsroom copy editors and from the UK Government Digital Service (GDS).

## Check against the original ask

GDS's "2i" (second pair of eyes) review, described by Jon Sanger (practitioner; Inside GOV.UK blog), starts from the request, not the draft: 2i "will go back and make sure that the original scope has been fulfilled", whether the request came from "a Zendesk ticket or a task in Pivotal".

## Read the whole piece first

Newsroom copy editors quoted by Craig Silverman (practitioner; Poynter's *Regret the Error* column) advise: "Slow down — just a little." The copy editor "should take a few minutes to read the story and digest what is being said before making any changes beyond fixing an obvious typo." Questions get noted but held: "read the whole story and make sure your question isn't addressed before posing it to the writer or assigning editor."

GDS applies the same rule to small edits: "2i has to read the whole content item thoroughly, even if only a tiny part of it was changed." Two reasons are given. A small change can break something else ("It's the butterfly effect of changing content"), and the item sits among others: "even an innocent looking update could duplicate, contradict or crossover with other content."

## Raise big problems early

Not every issue waits for the line edit. "Any "big-picture" issues regarding libel, fairness and the like should be raised as early as possible so that more reporting can be done, a senior editor can be consulted, or the story can be held until the concerns can be addressed."

GDS later moved part of its review before the writing starts, so that a colleague can "point out any problems with your plan" (Mortimer; see [Proportional review](proportional-review.md)). The logic matches the newsroom advice: a wrong approach is cheapest to fix before the draft exists.

## If it isn't broken, don't fix it

John McIntyre of The (Baltimore) Sun, quoted in the same piece, says "a good copy editor knows when to leave things alone", and "the copy editor should have a good reason why he or she made the change." The risk runs both ways: "Editors save writers from making mistakes. It happens all the time. But it's also true that the editing process can introduce errors." Hence: "inserting an error into a story is the cardinal sin of editing", so "make sure what you are "correcting" is actually incorrect."

A business-writing trainer, Hurley Write (practitioner, with a commercial interest), offers the positive version of the test. Reviewers who "slap the document on the table and pull out a red pen" waste time; instead, "Consider the goal for the document and its intended reader: the strategy should be to edit anywhere the document can be better aligned with its objectives and readers." See [Proportional review](proportional-review.md) for its "good enough" argument.

## Fix small things, send back big ones

GDS reviewers do not bounce every issue back. Small fixes are made directly, because "rejecting them from review and back to the content designer might be an unnecessary delay for everyone involved"; "2i will make any small adjustments needed and make sure they record any notes on what they've done. It's better than slowing down the velocity of the team." The limit is volume: "2i can easily see up to 50 or more items a day", so changes that are "too far-reaching or complicated" go back "with notes, questions or suggestions."

## Structural tests

Barbara Minto's Pyramid Principle course (practitioner) supplies review questions for the structure rather than the sentences: what is "the reader's question", does the document answer it, and does each grouping carry an insight, since "("There are three reasons" is not an appropriate insight!)". See [Bottom Line Up Front (BLUF)](../practices/bluf.md#the-governing-thought-answers-the-readers-question).

## Test with a reader who lacks the context

Anthropic's doc-coauthoring agent skill (repo) automates a cold read: it has the model "Generate 5-10 questions that readers would realistically ask", gives a sub-agent "just the document content and the question", and checks the answers, plus a pass "for ambiguity, false assumptions, contradictions." The doc is ready "When Reader Claude consistently answers questions correctly and doesn't surface new gaps or ambiguities". It is the machine version of handing a draft to a colleague who was not in the meeting. See [Office workflow skills](../agent-skills/office-workflow-skills.md#reader-testing).

## For cardigan

Interpretation, not source claims:

- Review starts from the ask: cardigan first checks that the draft does what was requested (the ticket, the email, the user's instruction) and answers the reader's question near the top, then reads all of it, and drops any question the text already answers. For high-stakes documents, a context-free reader check (only the draft plus the recipient's likely questions) catches what the author cannot see.
- Small, safe fixes (typos, a wrong date format, a missing link) are applied directly with a one-line note; only changes to substance or scope go back as questions.
- A one-line change to a shared doc still gets a read of the whole doc and a check for contradictions with other pages on the same subject.
- Every proposed change needs a reason the user would accept (wrong, unclear, risky, off-ask). Style preference alone is not a reason, and an unchanged paragraph is a valid review outcome. An edit that changes meaning is worse than no edit; evals should check that cardigan's edits never alter facts.
- Show-stoppers (legal, compliance, fairness, a wrong recipient) go first in the review, before line edits, so the user can stop or reroute early.

## See Also

- [Accuracy checklists](accuracy-checklists.md)
- [Proportional review](proportional-review.md)
- [Bottom Line Up Front (BLUF)](../practices/bluf.md)
- [Office workflow skills](../agent-skills/office-workflow-skills.md)
