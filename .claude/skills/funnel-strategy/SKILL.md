---
name: funnel-strategy
description: >-
  Works out a company's go-to-market motion (product-led, sales-led or hybrid) from its website and
  pricing, then maps the funnel stage by stage: a definition, strategy, leading inputs the team controls,
  lagging outputs with targets, cadence and owner for each stage, MQL, SQL and PQL criteria, post-sale
  stages, closed-lost re-entry paths and backward funnel maths from a revenue target. Triggers: "funnel
  strategy", "funnel stages", "pipeline stages", "PLG vs SLG", "lead qualification criteria", "map our
  sales process", "how do leads flow". Feeds /goals. Not for setting the target itself (use /goals).
version: '1.0.0'
license: MIT
---

# Funnel strategy

Map how a buyer moves from first touch to renewal, in the shape this company actually sells. The motion decides the stages: a product-led company and a sales-led company should not share a funnel. Every stage separates what the team does (inputs) from what it measures (outputs), and the maths runs backwards from the revenue target.

## When to use it

- Building the context folder, after positioning and messaging, before `/goals`.
- Setting up or cleaning up CRM stages.
- When marketing and sales disagree on what a qualified lead is.

Don't use it to set the revenue target (`/goals` takes a target someone has already committed to) or to design individual campaigns.

## Inputs

**Required:** the company website URL.

**Recommended:** `context/company/` (deal size, team size, funding sharpen the motion call), `context/icp/` (buying triggers shape qualification), the real CRM stages if they exist (they override anything inferred), pricing or average deal size.

**Paths.** Write to `context/goals/MMYY-funnel.md`, next to the scope file `/goals` will write. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

**Tools.** Page fetching and web search. Exa helps with company research if you have it.

## Steps

1. **Read the signals.** Homepage CTA ("Start free" vs "Book a demo"), pricing (self-serve checkout vs "Contact sales"), free trial or freemium, docs and API in the navigation, average deal size, sales team size.
2. **Call the motion.**
   - **Product-led:** signals point to self-serve.
   - **Sales-led:** they point to demos and sales.
   - **Hybrid:** both are strong.
   - **Unclear:** ask the user.

   State it with your two or three strongest signals and a confidence level.
3. **Pick the stage set** for that motion only. Don't mix product-led stages into a sales-led funnel. Hybrid runs two tracks with a rule for when a product user gets routed to sales.
4. **Define each pre-sale stage:**
   - a definition for this company
   - the strategy
   - **inputs**: leading activities the team controls, with a frequency ("3 LinkedIn posts a week")
   - **outputs**: lagging results with a target ("500 visitors a month")
   - cadence and owner

   Never put a metric in the inputs.
5. **Set qualification criteria.** 3 to 5 measurable signals each for MQL (marketing to sales), SQL (confirmed by sales) and, for product-led or hybrid, PQL (product usage). "Good fit" isn't a criterion; "50+ employees and visited pricing twice" is.
6. **Map closed-lost re-entry.** Loss reason, which stage they re-enter, the trigger and the timing.
7. **Map post-sale stages** in the same format: onboarding (the path to first value), retention, expansion, churn prevention. Match the motion: product-led is in-app, sales-led is account-manager driven.
8. **Run the backward maths** if there's a revenue target. Revenue to deals, deals to opportunities, then SQLs, MQLs, leads and traffic, using real conversion rates where you have them and marked estimates where you don't. Check whether current volumes can get there.
9. **Draw the journey** as a simple text diagram from first touch to expansion.
10. **List gaps and recommendations,** then hand off to `/goals`.

## Output shape

1. Motion assessment table: signal, what you saw, what it points to.
2. Pre-sale stages, each in the same format.
3. Qualification criteria.
4. Post-sale stages.
5. Closed-lost re-entry table.
6. Journey diagram.
7. Backward maths (if a target exists).
8. Gaps and recommendations.
9. Sources with URLs and confidence.

## What good looks like

- The motion is backed by at least three signals.
- Every input has a frequency, every output a target, every stage a cadence and an owner.
- Inputs and outputs never swap places.
- Qualification criteria are thresholds someone could put into a CRM.
- Post-sale matches pre-sale. A product-led company doesn't suddenly get a customer-success-led renewal motion.

## Mistakes to avoid

- Inventing stages the company doesn't run, instead of asking for the real ones.
- Assuming the motion from the category ("it's dev tools, so it's product-led").
- Making up conversion rates or KPI targets without marking them as estimates.
- One funnel template forced onto every company.

## Chain

Step 10 of the suggested chain: `/company-context` → `/icp-research` → `/competitor-research` → `/win-loss` → `/expert-pov` → `/tov-guidelines` → `/brand-kit` → `/positioning` → `/messaging` → **funnel-strategy** → `/goals`.
