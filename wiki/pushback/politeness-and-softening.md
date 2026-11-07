# Politeness and softening

> Sources: Cristian Danescu-Niculescu-Mizil, Moritz Sudhof, Dan Jurafsky, Jure Leskovec, Christopher Potts (ACL), 2013-06-25; Erin Meyer / INSEAD Knowledge, 2015-04-06; Megan Breen / INTHEBLACK (reporting Jen Overbeck), 2026-02-02; Michael Zipursky / Consulting Success (interview with Charles H. Green), undated; Hardik Pandya (stop-slop skill), 2026-03-17
> Raw: [A Computational Approach to Politeness with Application to Social Factors](../../raw/research/pushback/2013-06-25-computational-approach-politeness-power.md); [The Most Productive Ways to Disagree Across Cultures](../../raw/research/pushback/2015-04-06-meyer-productive-ways-to-disagree-across-cultures.md); [What your work emails say about how others perceive you](../../raw/research/pushback/2026-02-02-overbeck-email-language-perceived-power.md); [How to Become the Trusted Advisor to Consulting Clients with Charles Green: Podcast #196](../../raw/research/pushback/charles-green-trusted-advisor-consulting-success-podcast.md); [Stop Slop](../../raw/research/agent-skills/2026-03-17-stop-slop-skill.md)
> Updated: 2026-10-31

## Overview

How much softening a request or a disagreement needs depends on who is writing to whom. Politeness research identifies the markers that do the softening (indirection, deference, impersonalization, modality) and finds that lower-status writers use them more and drop them once they gain status. Culture adds a second axis: in some cultures open disagreement debates an idea, in others it costs the other person face, especially when aimed at someone senior. A terse or blunt message carries different risk going up the hierarchy than going down, and across cultures.

## The markers

Danescu-Niculescu-Mizil and colleagues (study; peer-reviewed computational linguistics, ACL) built "a new corpus of requests annotated for politeness" and a classifier based on politeness theory. Their features operationalise "key components of politeness theory, such as indirection, deference, impersonalization and modality." These are the parts of a message a trimming pass is most likely to remove.

## Politeness falls as power rises

Applied to online communities, the classifier shows a link between politeness and status: "polite Wikipedia editors are more likely to achieve high status through elections, but, once elevated, they become less polite." The same pattern holds elsewhere: "We see a similar negative correlation between politeness and power on Stack Exchange, where users at the top of the reputation scale are less polite than those at the bottom." The evidence is correlational and drawn from two online communities, not offices.

## Culture and seniority

Erin Meyer (practitioner; INSEAD professor and author of The Culture Map, writing for INSEAD Knowledge) describes how disagreement norms differ. In some cultures disagreement is about ideas: "When I say "I disagree," I am debating Erin's position, not disapproving of her." In others, face comes first: "In China, protecting another person's face is more important than stating what you believe is correct." Seniority sharpens this: "In Japan for example, disagreeing with someone with white hair or rank is taboo", and more generally "both your seniority and your age may impact the willingness of others to disagree openly".

Word choice carries the signal: "In confrontation-avoiding cultures, people are more likely to use words like "sort of" or "partially"." Speakers there also avoid strong words such as *absolutely* or *totally*. Even in a culture comfortable with debate there are limits: "I would not recommend telling your French client "you are totally wrong"."

She recommends changing the channel as well as the words:

- Anonymous input: "Putting ideas on a board anonymously then debating them with the group can facilitate disagreement".
- Private pre-meetings: "conduct meetings before the main meeting, something especially important in East Asian cultures".
- Naming your own style: "Sometimes, just a few words of explanation framing your behaviour can make all the difference".

Charles H. Green (practitioner; client-advisory coach) gives the same advice for disagreeing with clients: "Do it one-on-one privately", with humble framing such as "'I can be wrong about this but it occurs to me,'". See [Speaking up](speaking-up.md).

## Keep irritation out

Softening also means leaving emotion out. Trade-press coverage of Jen Overbeck's research (journalism; INTHEBLACK) reports that "expressing negative emotions correlates with being perceived as less powerful", while "using analytical language is positively associated with perceived power and prestige." A pushback that explains its reasoning reads stronger than one that sounds annoyed. See [Short messages](../practices/short-messages.md) for the same research on length.

## AI style rules that strip softeners

Popular prose-cleanup skills for AI agents tell the model to remove exactly these markers. Stop-slop (repo) tells the model to trust readers: "State facts directly. Skip softening, justification, hand-holding."

> **Status: Disputed**
> Stop-slop's rule to "Skip softening" (practitioner style rules for prose) conflicts with the studies above, which treat softeners as markers of politeness and find them falling as power rises. See [Prose-style skills](../agent-skills/prose-style-skills.md#softening-a-style-rule-against-the-evidence).

## For cardigan

Interpretation, not source claims:

- Brevity and politeness markers are separate dials. cardigan cuts padding but keeps the markers (a *could you*, a *would it help if*, a thanks) when the user writes upward to a manager or client.
- Users writing downward can be terser, but that is exactly where Zorn finds short messages are read most negatively (see [Short messages](../practices/short-messages.md)), so a lower politeness level is not a licence for curtness.
- Pushback is a face-threatening act by nature; it needs more softening than a routine reply of the same length.
- A one-line question in a group thread is not culture-neutral. With senior or confrontation-avoiding recipients cardigan softens the qualifiers, moves the question to a private message, or skips it and just delivers the lighter default with an offer (after Meyer).

## See Also

- [Short messages](../practices/short-messages.md)
- [Speaking up (employee voice)](speaking-up.md)
- [Saying no](saying-no.md)
- [Prose-style skills](../agent-skills/prose-style-skills.md)
