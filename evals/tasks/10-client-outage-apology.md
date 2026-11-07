# 10 · Apology to an unhappy client after an outage

- **Kind:** email
- **Right size:** full and careful (warmth and specifics are the point)
- **Tests:** politeness and accountability as never-cut items, exact facts, contractual wording

## Prompt

```
Draft the email to Karen Osei, Ops Director at Brightline Logistics, about Tuesday's outage. She was not happy when I called her yesterday. I'm her account manager.

Facts:
- Outage: Tuesday 3 November, 09:12 to 11:26 CET (2 hours 14 minutes).
- Cause: a database failover failed during planned maintenance on our side.
- Impact: Brightline's shipment updates were queued during the outage and processed once we recovered. No data was lost.
- This breaches our 99.9% monthly uptime commitment. Under section 7.2 of the SLA they get a service credit of 10% of the November fee, applied automatically to the next invoice.
- What we're changing: failover is now tested weekly, and planned maintenance moves to weekends.
```

## Good outcome

A sincere apology at the top that owns the failure, with no blame-shifting. Then what happened with exact times, the impact (queued updates, no data lost), the credit (10% of November, section 7.2, automatic on the next invoice), what is changing, and an offer of a call. About 120 to 250 words. It shouldn't be a three-liner, and it shouldn't wrap the facts in padding either.

## Checks (pass/fail)

1. **Apology and ownership (never-cut):** an explicit apology, and the cause is owned ("on our side"), not deflected.
2. **Times (never-cut):** 3 November, 09:12 to 11:26 CET, 2 hours 14 minutes, all correct if stated.
3. **Impact (never-cut):** no data lost; updates queued and then processed.
4. **Credit (never-cut):** 10% of the November fee, section 7.2 of the SLA, applied automatically to the next invoice.
5. **Prevention:** weekly failover tests and weekend maintenance.
6. **Next step:** offers a call or a named contact.
7. **Tone (judge):** an unhappy ops director would read it as taking the problem seriously.

## Lighter option

None. A terse acknowledgement is the failure this task looks for.

## Measure

As task 01.
