---
name: company-context
description: >-
  Researches a company from its website and public sources and writes a company profile: what it sells,
  who buys it, traction, funding, team, hiring, tech stack, key people, red flags and the gaps you still
  need to fill, every claim tagged with a source and a confidence level. Use it as the first file in a
  marketing context folder, or to prep a discovery call or qualify a prospect. Triggers: "company
  research", "company background", "company context for", "qualify this prospect", "discovery call
  prep", "account brief", or a company URL handed over for research. Not for competitor analysis (use
  /competitor-research) or customer profiles (use /icp-research).
version: '1.0.0'
license: MIT
---

# Company context

Build a sourced profile of one company: what it does, how big it is, how it's growing, who runs it and what's missing. It's the root file of the context folder. Every other skill in this plugin reads it first, so a wrong number here spreads everywhere. Accuracy beats completeness.

## When to use it

- Starting the context folder for your own company or a client.
- Prepping a discovery or sales call with a prospect.
- Checking whether a prospect is worth pursuing before you spend time on them.

Don't use it for competitor deep dives (`/competitor-research`), customer personas (`/icp-research`) or a quick "what does this company do" question you can answer in one line.

## Inputs

**Required:** a website URL, LinkedIn company page or company name. If the name is ambiguous (two companies called "Atlas"), ask for the URL before you start.

**Optional:** the questions the user most wants answered, the date of an upcoming call, any internal notes or decks.

**Paths.** Write to `context/company/MMYY-company-context.md`. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

**Tools.** Plain web search and page fetching are enough. If you have Exa or Firecrawl connected, use them for cleaner extraction. No API key is required.

## Steps

1. **Confirm the company.** Name, URL, one-line description. Stop and ask if you're not sure it's the right one.
   *Produces:* a confirmed identity line.
2. **Read the website.** Homepage (what they claim and for whom), product and pricing pages, about page (story, founders), customers or case studies, careers page.
   *Produces:* raw notes with the URL of every fact.
3. **Search funding and size.** Funding rounds, investors, headcount, revenue estimates. Check press, the company's own announcements and public funding databases. Treat revenue estimates from aggregator sites as low confidence.
   *Produces:* a funding and size table.
4. **Collect traction signals.** Logo walls, named case studies, review counts on G2 or Capterra, recent launches, hiring volume by team.
   *Produces:* a traction list, each with a date.
5. **Map the people who matter.** Founders, marketing and sales leaders, recent senior hires and departures, from public sources only.
   *Produces:* a short people table with roles and source.
6. **Tag confidence on every claim.** `[VERIFIED]` for an official or primary source, `[INFERRED]` when two or more sources point the same way, `[ESTIMATED]` for your reasoning, `[UNAVAILABLE]` when you looked and found nothing. Say where you looked.
   *Produces:* tagged notes.
7. **Flag conflicts and red flags.** Sources that disagree, layoffs, long funding gaps, executive churn, a recent pivot, hidden pricing, a logo wall with no case studies.
   *Produces:* a red-flag list with evidence.
8. **Score fit, if the user is qualifying a prospect.** Five criteria scored 0 to 5: stage, size, industry, a marketing or growth leader in seat, and signals that match the user's ICP. Show the reasoning per criterion, not just the total.
   *Produces:* a fit score out of 25.
9. **Write 3 to 5 observations.** The things a reader should know before a call or before writing positioning. Each one tied to evidence.
10. **List the gaps.** What you couldn't find, and the question you'd ask the company to fill each one.
11. **Hand off.** Suggest the next step in the chain: `/icp-research`, then `/competitor-research`.

## Output shape

A single markdown file, in this order:

1. Header: company, URL, research date, overall confidence (1 to 5).
2. Summary in 3 sentences.
3. Snapshot table: category, founded, HQ, headcount, funding, revenue band, pricing model, each with confidence.
4. Product and who it's for, in their words, with URLs.
5. Traction signals, dated.
6. Team and key people.
7. Red flags.
8. Fit score (only if qualifying).
9. Key observations.
10. Data gaps and questions to ask.
11. Sources with URLs and access dates.

## What good looks like

- Revenue, customers, funding and team size are each answered or marked `[UNAVAILABLE: searched X, Y]`.
- At least half the claims are `[VERIFIED]`. Major claims have more than one source.
- No invented numbers. A blank with a note is better than a plausible guess.
- Observations are specific to this company. Swap in another company name and they should stop being true.
- Someone could walk into a call with only this file and ask better questions.

## Mistakes to avoid

- Treating an aggregator's revenue estimate as fact.
- Copying the homepage tagline as if it were the positioning. Note what they claim, then note what the evidence shows.
- Mixing up two companies with similar names.
- Reporting signals older than 12 months as current. Date everything.
- Padding the observations with generic advice ("they should invest in content").

## Chain

This is step 1 of the suggested context chain: **company-context** → `/icp-research` → `/competitor-research` → `/win-loss` → `/expert-pov` → `/tov-guidelines` → `/brand-kit` → `/positioning` → `/messaging` → `/funnel-strategy` → `/goals`.
