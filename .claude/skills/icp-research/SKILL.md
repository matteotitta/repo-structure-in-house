---
name: icp-research
description: >-
  Builds an ideal customer profile from evidence: case studies, testimonials, customer logos, solutions
  pages, reviews and any sales notes you have. Produces market sizing layers, firmographic segments, a
  champion and an economic buyer persona, a negative ICP, intent signals, customer proof points and a
  voice-of-customer section in the buyers' own words, every claim sourced. Triggers: "ICP research",
  "ideal customer profile", "who are our customers", "customer segments", "buyer personas", "who should
  we target". Run after /company-context. Not for competitor analysis (use /competitor-research) or call
  transcript patterns (use /win-loss).
version: '1.0.0'
license: MIT
---

# ICP research

Work out who actually buys, who signs, who uses it and who isn't a fit, from what customers have said and done in public and in your own records. The output is the ICP file every later skill reads before it writes a word.

## When to use it

- Building the context folder, right after `/company-context`.
- Before positioning or messaging work, when nobody can say who the best customers are in one sentence.
- When sales keeps chasing deals that don't close and you suspect the target is too broad.

Don't use it to analyse sales calls (`/win-loss`) or competitors (`/competitor-research`).

## Inputs

**Required:** the company website URL. If it's missing, ask.

**Recommended:** `context/company/` from `/company-context`; links to case studies and testimonials; a customer list or CRM export (strip names and emails first); sales notes on wins and objections; any existing ICP document to check against.

If a recommended input is missing, run from what you have and list what's missing in the data gaps section.

**Paths.** Write to `context/icp/MMYY-icp.md`. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

**Tools.** Web search and page fetching are enough. Exa or Firecrawl help if you have them. Review sites (G2, Capterra) and the company's LinkedIn page are useful public sources.

## Steps

1. **Find the evidence pages.** Customers, case studies, testimonials, solutions or industry pages, pricing, integrations, review sites.
   *Produces:* a source list with URLs and access dates.
2. **Extract raw data per customer.** Company name, industry, size, region, role of the person quoted, the problem they described, the outcome they reported, tools they mention.
   *Produces:* a customer evidence table.
3. **Normalise the attributes.** Put size, industry and region into consistent bands so you can count them.
4. **Find the segments.** Count which industries, sizes and regions repeat. A segment needs several customers behind it, not one logo.
   *Produces:* 2 to 4 candidate segments with counts.
5. **Size the market in layers.** Total market, the part you can serve, the part you can realistically win, and the ICP as the best slice of that. Show the maths and mark estimates. Each layer must be smaller than the one above.
6. **Build two personas.** The champion (who feels the pain and pushes for the purchase) and the economic buyer (who signs). Cover goals, pains, triggers, objections and how each one judges success. They must read differently.
7. **Write the negative ICP.** Who looks like a fit but isn't, and the signals that disqualify them.
8. **List intent signals and buying triggers.** Observable events that show a company is ready: a new hire, funding, a tool change, a regulation, a growth milestone.
9. **Collect proof points.** Named customers with outcomes and URLs. Only customers referenced in public or in data the user gave you.
10. **Synthesise voice of customer.** Exact phrases customers use for their problem and their outcome. Quote, don't paraphrase.
11. **Recommend the priority segment.** Rank the segments and say why the first one wins.
12. **List data gaps** and what would fill them (interviews, CRM fields, win-loss).

## Output shape

Open with a 3-line TLDR and a short block of open questions. Then:

1. Header: date, website, confidence score 1 to 5.
2. Market sizing layers with the maths.
3. Firmographics: industry, size, region, tech stack patterns.
4. Personas: champion, economic buyer, and users or influencers if relevant.
5. Negative ICP.
6. Customer proof points.
7. Voice of customer.
8. Segment definitions, ranked, with intent signals.
9. Recommendations.
10. Data gaps.
11. Sources with URLs, dates and confidence.

Sort roles as champion, economic buyer, user, influencer. Sort sizes from largest to smallest.

## What good looks like

- Every customer named is public or came from the user's own data.
- Quotes are verbatim and attributed to a role.
- The champion and the economic buyer have different pains and different success measures.
- The negative ICP excludes real companies someone might chase.
- Segment claims show their count ("6 of 14 case studies"). Small samples are flagged once, not repeated in every section.
- The confidence score matches the evidence: mostly high-confidence sources score 4 or 5, mostly estimates score 1 or 2.

## Mistakes to avoid

- Inventing customer names or composite quotes.
- Personas built from imagination ("Marketing Mary, 34, loves podcasts").
- Market sizing that grows as it narrows, or a top-down number with no maths.
- Calling one big logo a segment.
- Writing the same caveat in every section. Say it once and point to it.

## Chain

Step 2 of the suggested chain: `/company-context` → **icp-research** → `/competitor-research` → `/win-loss` → `/expert-pov` → `/tov-guidelines` → `/brand-kit` → `/positioning` → `/messaging` → `/funnel-strategy` → `/goals`.
