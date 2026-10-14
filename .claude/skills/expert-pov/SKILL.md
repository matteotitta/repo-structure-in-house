---
name: expert-pov
description: >-
  Draws out a founder's or expert's point of view: what they believe about their market that others
  don't, the hot takes they'd defend, the stories behind them, and their taste. Generates interview
  questions, works from answers, a live call or existing content, and ends with ranked One Big Idea
  candidates for thought leadership and positioning. Triggers: "expert POV", "founder POV", "one big
  idea", "OBI", "contrarian beliefs", "what makes our founder different", "thought leadership
  foundation", "founder interview questions". Feeds /positioning and /tov-guidelines. Not for writing
  posts or articles, and not for brand voice rules (use /tov-guidelines).
version: '1.0.0'
license: MIT
---

# Expert POV

Authority comes from a distinct point of view, not from expertise alone. This skill surfaces what the founder (or another expert) actually believes, including the views that cut against the market, and turns them into a small set of ideas they can own for years.

## When to use it

- Building the context folder, before positioning, when the founder's voice is part of how the company sells.
- Before starting a thought leadership program on LinkedIn, a newsletter or a podcast.
- When content sounds like everyone else in the category.

Don't use it to write the content itself, or to set brand voice rules (`/tov-guidelines`).

## Inputs

**Required:** the founder's or expert's name, and the company's industry or category.

**Recommended:** `context/company/` and `context/competitors/` (so you know what the market already says), and existing content: LinkedIn posts, podcast or interview transcripts, talks, essays.

**Collection method.** Agree one up front: async (the founder answers written questions), live (an interview you transcribe), or content mining (you work from what they've already published). Mixing is fine.

**Paths.** Write to `context/expert-pov/MMYY-expert-pov.md`. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

**Tools.** For content mining, web search with a site filter on their LinkedIn or blog works. Exa helps if you have it.

## Steps

1. **Generate questions.** 25 to 30 questions across six areas:
   - market beliefs (where the category is going)
   - contrarian views (what most people get wrong)
   - craft (how they do the work, and why that way)
   - origin (why they started, the moment it clicked)
   - customer truths (what buyers misunderstand)
   - taste (what they admire, what they refuse to do)

   Tailor them to the industry. *Produces:* a question set the founder can answer in about 45 minutes.
2. **Collect the input** by the agreed method. For content mining, gather at least 10 pieces.
3. **Extract the POV.** From the answers or content, pull:
   - **beliefs**, stated plainly
   - **hot takes**, which a reasonable person could disagree with
   - **origin stories**, with the concrete moment
   - **taste signals**

   Quote the founder's own words for each.
4. **Classify the founder's archetype** from their origin story, citing their words:
   - **problem**: they lived the pain
   - **insight**: they saw something others missed
   - **vision**: they disagree with where the market is heading

   The archetype shapes which ideas will sound authentic in their mouth.
5. **Cluster into themes.** Group related beliefs. Drop anything every competitor would also say.
6. **Draft One Big Idea candidates.** 3 to 5 single-sentence ideas the founder could build a body of work around. Each one names a belief, the tension it resolves and who it's for.
7. **Score each candidate** on four questions:
   - Is it distinct from competitors?
   - Is it true to the founder?
   - Does it matter to the ICP?
   - Could they write 100 posts on it?
8. **Develop the top candidate** with its supporting beliefs, three proof points or stories, and five content angles.
9. **Review with the user.** Approve, iterate on the idea, or go back for more themes.

## Output shape

1. Summary: the recommended One Big Idea in one sentence, and the archetype.
2. Beliefs, hot takes and origin stories, each with a quote and source.
3. Themes.
4. Candidate table with scores and one line of reasoning each.
5. The developed top idea.
6. Gaps and follow-up questions.
7. The question set, so it can be reused.

## What good looks like

- Every belief traces to the founder's own words, not your summary of their industry.
- At least one hot take would make a competitor uncomfortable.
- The top idea passes the 100-posts test without straining.
- The ideas fit the archetype. A problem founder leading with a grand vision rings false.
- Nothing here could appear unchanged on a competitor's blog.

## Mistakes to avoid

- Writing beliefs the founder never said.
- Contrarian for its own sake. A hot take has to be something they'd defend on a call.
- Ten ideas instead of one. The point is focus.
- Generic themes like "customer obsession" or "AI is changing everything".

## Chain

Step 5 of the suggested chain: `/company-context` → `/icp-research` → `/competitor-research` → `/win-loss` → **expert-pov** → `/tov-guidelines` → `/brand-kit` → `/positioning` → `/messaging` → `/funnel-strategy` → `/goals`.
