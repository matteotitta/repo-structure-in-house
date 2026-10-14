---
name: goals
description: >-
  Turns a target someone has already committed to (a board plan, an annual plan, a contract) into a
  plan the team can measure: KPIs in three tiers with a guardrail for each, a baseline from real data,
  monthly pacing with lag and seasonality, and two or three channels chosen from how your ICP actually
  searches and buys. Writes context/goals/MMYY-scope.md and context/goals/measurement.md. It never
  invents the target. Triggers: "set our goals", "what are our KPIs", "revenue target and pacing",
  "which channels and what targets", "write the scope file", "are we on track". Run after
  /funnel-strategy. Not for designing funnel stages (use /funnel-strategy).
version: '1.0.0'
license: MIT
---

# Goals

Every later piece of marketing work should start from `context/goals/`. This skill fills it. It takes a number someone has already committed to and works out what to measure, where you stand today, how fast you need to move each month, and which channels will carry it, so anyone can tell by the 10th of the month whether you're on track.

**It never invents the target.** No committed number, no run: ask for it.

## When to use it

- The last step of the context folder, after `/funnel-strategy`.
- A new financial year, a new plan or a new contract.
- When someone asks "what are we actually trying to hit, and through which channels?"

Don't use it to design funnel stages (`/funnel-strategy`), or for traction goals before the product has any repeatable way to win customers.

## Two modes

Ask once, then proceed.

| | Company mode | Engagement mode |
|---|---|---|
| Who | In-house marketer, founder, head of marketing | Consultant or agency, per client |
| Target from | Board plan, annual plan, revenue target | Contract, statement of work, signed proposal |
| Baseline from | Your CRM, last 12 months | The client's CRM, analytics and reports |

## Inputs

**Required:** the target, with a date and its source.

**Recommended:**
- a CRM export for the last 12 months (strip names and emails first; keep aggregates only)
- `context/goals/MMYY-funnel.md` from `/funnel-strategy`, for the stages and conversion rates
- `context/icp/`, for where buyers search, compare and decide
- analytics or ad reports, for traffic and channel numbers

Missing inputs don't stop the run. Mark each gap `[TBD: collect X]` and say what would fill it.

**Paths.** Write `context/goals/MMYY-scope.md` and `context/goals/measurement.md`. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

## Steps

1. **Pin the target.** Quote it with its source: "£450k new revenue by 31 Aug 2027 (FY plan, slide 4)". Keep ranges and scenarios as given. Ask how much risk the business will accept and how fast it needs results. That caps how aggressive the pacing can be.
2. **Choose one focus** for this period: pipeline, new customers, activation, retention, expansion or a launch. A team that pushes every number at once moves none of them.
3. **Set KPIs in three tiers,** three per tier at most:
   - **Outcome:** the target itself.
   - **Drivers:** the two or three numbers on the focus that lead to the outcome, taken from the funnel (qualified opportunities and win rate for pipeline; activation rate for activation).
   - **Activity:** what the team controls week to week, one per channel.
4. **Give every driver and activity KPI a guardrail:** the number that must not get worse while you push it. Lead volume versus lead quality. Send volume versus unsubscribes. Discounting versus win rate.
5. **Set baselines.** Today's number for every KPI, from its real source, with the count it rests on. Fewer than 20 deals, or under six months of history, is a direction, not a fact: say so next to the number. A new channel has no baseline. Give it a test budget, not a target.
6. **Find the gap and pace it.** The gap is the target minus where today's run rate lands. Work it back through the funnel's conversion rates to the volume needed each month. Pace with:
   - the sales cycle lag (pipeline leads revenue by one typical cycle)
   - seasonality from the company's own history
   - a ramp for new channels
   - low, medium and high scenarios

   Don't put the gap-closing work in the last month, where it can't land in time.
7. **Pick channels from ICP behaviour.** From `context/icp/`, list where buyers search, compare and decide. Shortlist two or three channels. Give each one job, one metric and the activity KPI it owns, and name the constraint likely to cap it (budget, people, content, sales capacity). Every channel must trace to a line in the ICP file, not to habit.
8. **Write `measurement.md`.** One entry per KPI and guardrail: the source, the exact counting rule, the cadence and the owner. A KPI with no possible source moves to open questions.
9. **Hand off** in three lines: the target and the gap, the focus and its drivers, the channels.

## Output shape

`MMYY-scope.md`:
1. Target with source, and the gap.
2. Focus.
3. KPI table: tier, KPI, guardrail, baseline (with count), target.
4. Monthly pacing table with low, medium and high.
5. Channels: job, metric, constraint, ICP evidence.
6. Open questions.

`measurement.md`: KPI, source, counting rule, cadence, owner.

## What good looks like

- The target is quoted, not estimated.
- Every KPI has a guardrail, a baseline and a source.
- Small samples are flagged once.
- Pacing respects lag and seasonality instead of a flat line to the target.
- Nobody has to ask how a number is counted.

## Mistakes to avoid

- Inventing or "suggesting" the target.
- Rates as outcomes. The outcome is a total, such as revenue or customers.
- KPIs with no guardrail, which get gamed.
- Channels picked because the team already uses them, not because buyers do.
- Personal data in the saved files.

## Chain

The final step of the suggested chain: `/company-context` → `/icp-research` → `/competitor-research` → `/win-loss` → `/expert-pov` → `/tov-guidelines` → `/brand-kit` → `/positioning` → `/messaging` → `/funnel-strategy` → **goals**.
