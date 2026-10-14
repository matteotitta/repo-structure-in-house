# PulseAnalytics — win/loss analysis (canonical, locked example)

> **Note on this file:** PulseAnalytics is a fictional B2B SaaS analytics platform used as the running example throughout this quickstart. The patterns below are illustrative. Quotes are masked per `.claude/rules/pii-redaction.md` (end-customer names → `[CLIENT]`) and every pattern carries a verbatim quote + speaker per `.claude/rules/evidence-bound-outputs.md`. **Replace this file with your own win/loss output.** Keep the structure; replace the content.

---

## Method

- **Sample:** 11 won + 9 lost deals, Q1–Q2 2026 sales calls (Granola transcripts). 2 churned accounts included in the loss set.
- **Mode:** comparison (won vs lost), aggregated to patterns.
- **Confidence:** High = 3+ deals, Medium = 2, Low = single mention. Patterns below the line are noted as Low and not acted on yet.

## Why we win (patterns across the won set)

**Product — "live in two weeks" lands as the deciding factor.** [High, 7/11]
> "We'd scoped a Looker build at a quarter of eng time. You were showing me my own pipeline attribution in the second week." — buyer, VP Marketing ([CLIENT])

**Messaging — the Monday-review framing is the hook that gets the first call.** [High, 6/11]
> "The 'stop stitching the Monday review' line is literally my Sunday night. That's why I booked." — buyer, Head of Demand Gen ([CLIENT])

**GTM — the templated demo on the buyer's own data closes faster than a generic walkthrough.** [Medium, 4/11]
> "Once you ran it on our Salesforce instead of a sandbox, the room went quiet. That was the moment." — buyer, VP Marketing ([CLIENT-2])

**Competition — we win vs Bizible/Dreamdata on "answers, not raw attribution."** [Medium, 4/11]
> "Dreamdata gave us the attribution; it didn't tell us what to do Monday. You did." — buyer, Demand Gen Lead ([CLIENT])

## Why we lose (patterns across the lost set)

**Pricing — per-tracked-revenue pricing spooks the smaller end of the ICP.** [High, 5/9]
> "At our revenue the volume tier put you above what I could expense without a board line. Came back to spreadsheets." — buyer, Marketing Lead ([CLIENT])

**Customer context — no exec sponsor → deal stalls after a strong champion call.** [High, 4/9]
> "I loved it. My CFO asked 'why not just have the data team do it' and I didn't have the answer ready." — champion, Head of Marketing ([CLIENT])

**Competition — lose to "live without it" more than to a named rival.** [Medium, 3/9]
> "Honestly we didn't pick anyone. We decided last-touch in HubSpot is good enough for now." — buyer, VP Marketing ([CLIENT-2])

**Product — enterprise prospects want session-level data we don't do.** [Low, 2/9]
> "We needed product-usage cohorts in the same view. That's Amplitude territory for us." — buyer, VP Growth ([CLIENT])

## Marketing handoff

- **→ positioning:** the "no data team required" differentiator is doing the heaviest lifting in wins — promote it above "implementation speed." Add an explicit "why not just have the data team build it" rebuttal (it's the #1 loss objection from the economic buyer).
- **→ product-messaging:** bake the verbatim "stop stitching the Monday review" + "answers, not raw attribution" language into the messaging library — buyers repeat it back unprompted.
- **→ icp-research:** sharpen the anti-ICP. Sub-$1M-ARR and enterprises needing session-level data both show up in losses — the current ICP floor is right; add "needs product-analytics depth" to anti-ICP.
- **→ pricing (future):** the volume-tier objection at the low end of the ICP recurs — flag for a pricing review, not a messaging fix.

---

## Refresh cadence

Monthly while deal volume is high. Refresh sooner on a churn spike or a named competitor appearing repeatedly in losses.

Last refreshed: 2026-05-17 (V1 example seed)
Owner: VP Marketing
