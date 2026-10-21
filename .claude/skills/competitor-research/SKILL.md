---
name: competitor-research
description: >-
  Researches one B2B SaaS competitor across 13 dimensions (company, product, ICP, pricing, reviews,
  content, launches, search and AI visibility, tech stack, hiring, go-to-market, social, paid ads) and
  writes a sourced dossier with an executive summary, a threat level, strengths and weaknesses, and a
  data gaps section. Run it once per competitor, then compare. Triggers: "competitor analysis",
  "competitor research on", "what is [competitor] doing", "compare us to", "competitive landscape",
  "battlecard prep". Run after /company-context and /icp-research. Not for researching your own company
  (use /company-context).
version: '1.0.0'
license: MIT
---

# Competitor research

Build a dossier on one competitor that a marketer, a seller and a founder can each act on. The rule that governs everything: **no data point without a source.** Every claim carries a URL and an access date, or it's marked `[Not available]`.

## When to use it

- Building the context folder, after you know who your customer is.
- Before positioning, so you know what buyers compare you to.
- When a competitor shows up in deals more often, or launches something.

Don't use it for your own company (`/company-context`) or a single factual question ("what does X charge?"), which you can answer directly.

## Inputs

**Required:** the competitor's name and website. If the name is ambiguous, confirm before you start.

**Recommended:** `context/company/` and `context/icp/` (so you can judge the threat against your own buyer), any existing dossier to refresh, and the questions the user cares about most (pricing, outbound, a feature).

**Paths.** Write to `context/competitors/MMYY-<competitor-slug>.md`. With two or more dossiers done, add `context/competitors/MMYY-landscape.md`. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

**Tools.** Web search and page fetching cover most of it. Exa helps find similar companies and clean page text; Firecrawl helps with pricing and comparison pages. Paid SEO and tech-stack tools are optional: if you don't have one, say so in that dimension rather than guessing. On a large site, list the pages first and only read the ones that matter (product, pricing, positioning, customers).

## The 13 dimensions

1. **Company:** founding, funding, headcount, leadership.
2. **Product:** core offer, key features, what changed recently.
3. **ICP:** who they sell to, judged from their case studies and logos.
4. **Pricing:** model, tiers, entry price, what's gated behind sales.
5. **Reviews:** themes in G2, Capterra or Trustpilot praise and complaints, with counts.
6. **Content:** what they publish, how often, which topics.
7. **Launches:** what they've shipped in the last 12 months.
8. **Search and AI visibility:** the topics they rank or get cited for.
9. **Tech stack:** tools visible on the site, if you can see them.
10. **Hiring:** open roles by team, which signal where they're investing.
11. **Go-to-market:** self-serve, sales-led or both; channels; partnerships.
12. **LinkedIn and social:** founder and company activity, recurring themes.
13. **Paid advertising:** ads visible in public ad libraries, angles they test.

## Steps

1. **Confirm scope.** Name, URL, and what the user wants to learn. *Produces:* a one-line brief.
2. **Research each dimension** in the order above. Note the source and date for each finding. If a dimension needs a tool you don't have, write `[Not available: needs X]` and move on.
3. **Tag confidence.** `[VERIFIED]`, `[INFERRED]`, `[ESTIMATED]`, `[UNAVAILABLE]`. Aim for at least half verified.
4. **Assess strengths and weaknesses** against your ICP, not in the abstract.
5. **Set a threat level:** primary (same buyer, same problem, often in deals), enterprise tier (same problem, bigger buyer), direct ICP (same buyer, adjacent problem), watch (early or stealth), low, or defunct. Explain the call in two sentences.
6. **Write the executive summary** last, in 2 to 3 short paragraphs.
7. **List data gaps** with the action that would fill each one.
8. **If you have 2 or more dossiers,** write a landscape file: threat table, feature comparison, where each competitor is weak, and 3 to 5 recommendations. Cite the dossiers rather than repeating them.
9. **Hand off** to `/positioning`, which uses the competitor set as its list of alternatives.

## Output shape

Title the file `# Competitor research: [Name]`. Then: a recent-changes line (on a refresh), executive summary, threat level, a section per dimension with inline `(Source: X)` notes, strengths and weaknesses, data gaps, and a sources table at the end with URL, access date and confidence per dimension.

## What good looks like

- All 13 dimensions present, each either filled or marked with why it's empty.
- Major claims (funding, size, pricing) have more than one source.
- Review themes come with counts, not adjectives.
- The threat level would make sense to your sales team.
- A refresh updates the existing file and notes what changed, rather than creating a duplicate.

## Mistakes to avoid

- Copying their marketing claims as fact. Note the claim, then the evidence.
- Guessing pricing that's behind "contact sales".
- Reporting old news as current. Date every finding.
- A weakness list that's really a wish list ("their UX is bad") with no evidence.
- Restating every dossier inside the landscape file.

## Chain

Part of the free five-skill chain: `/icp-research` → **competitor-research** → `/tov-guidelines` → `/positioning` → `/messaging`. The other six context skills (company context, win-loss, founder POV, brand kit, funnel and goals) are free in the [context plugin](https://github.com/matteotitta/claude-marketing-context).
