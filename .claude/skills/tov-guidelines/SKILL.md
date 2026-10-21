---
name: tov-guidelines
description: >-
  Extracts a company's tone of voice from its own content and turns it into rules a writer or an AI can
  follow. Phase 1 analyses 15 to 20 pages for sentence, paragraph, word and structure patterns with
  frequency counts; after the user reviews it, Phase 2 writes the guidelines: tone attributes with
  before and after examples, a We are / We are not table, tone by context, vocabulary to use and avoid,
  and open questions. Triggers: "tone of voice", "brand voice", "voice guidelines", "writing style
  guide", "extract voice from our website", "TOV". Not for visual identity (use /brand-kit) or messaging
  (use /messaging).
version: '1.0.0'
license: MIT
---

# TOV guidelines

Find out how a company actually writes, then write that down as rules specific enough that a new writer, or an AI, sounds like them on the first draft. Two phases with a review in between: first the evidence, then the guidelines.

## When to use it

- Building the context folder, before any copy or content work.
- Starting a content program, or onboarding writers or AI tools.
- When content has drifted, or the existing guide is more than six months old.

Don't use it for colours and fonts (`/brand-kit`), for what to say (`/messaging`), or when the user only wants a one-line description of the voice.

## Inputs

**Required:** the company website URL. It needs a homepage and at least 5 to 10 pages of real content. If it's thin, say so and flag the sample size in the output.

**Optional:** founder notes or transcripts, an existing style guide to update, `context/icp/` for the reader, `context/expert-pov/` for the founder's own voice.

**Paths.** Write `context/brand/MMYY-tov-analysis.md` (Phase 1) and `context/brand/MMYY-tov-guidelines.md` (Phase 2). Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

**Tools.** Page fetching for the site. Web search with a site filter helps collect founder posts. Exa or Firecrawl are fine if you have them.

## Phase 1: analysis

1. **Pick the pages.** Homepage, about or values, 3 to 5 blog posts, 2 to 3 case studies, pricing, FAQ, a landing page. Aim for 15 to 20.
2. **Sentence patterns:** average length, first or third person, questions, imperatives.
3. **Paragraph patterns:** length, how they open, where evidence sits.
4. **Word patterns:** the company's own terms, the customer's terms, words they avoid, how often they use modifiers.
5. **Structure patterns:** sentence or title case headers, CTA wording and placement, how they stack proof.
6. **Score frequency.**
   - High: 80% of pages or more.
   - Medium: 40 to 79%.
   - Low: under 40%.
   - Conflict: pages contradict each other.

   Show the count ("5 of 6 pages").
7. **Map voice by content type.** Person, formality and CTA style for homepage, blog, case study and pricing.
8. **Collect real examples** for each pattern. Use real sentences only, never invented ones.
9. **Flag inconsistencies and gaps**, with the questions you'd ask the founder.
10. **Review gate.** The user confirms the patterns, corrects anything wrong and answers the gap questions. Don't start Phase 2 without this.

## Phase 2: guidelines

1. **Apply the feedback** and resolve each inconsistency.
2. **Write the core guide:**
   - who reads it
   - 3 to 5 tone attributes, each with a before and after rewrite
   - vocabulary to use and avoid
   - structure templates for the main content types
3. **We are / We are not table.** 5 to 8 rows, each backed by Phase 1 evidence.
4. **Tone by context.** How the voice shifts for these contexts:
   - cold outreach
   - nurture email
   - objection handling
   - sales follow-up
   - support reply
   - case study
   - social post
5. **Tone by reader emotion.** How to write to someone frustrated, sceptical, excited or rushed.
6. **AI writing tells to avoid.** At least five patterns that would make this brand sound machine-written, shown with the brand's own fix. Examples: generic praise openers, three short parallel sentences, "it's not X, it's Y" contrasts, filler transitions, closing on "what do you think?".
7. **Optional sections**, only when they apply:
   - hard questions answered: security, pricing, a big competitor. Mark these draft until the founder approves.
   - product microcopy, for companies with a product UI.
   - AI assistant voice, for companies with a chatbot.
8. **Open questions.** At least three, each saying what it unblocks.
9. **Source every rule** to a page, or mark it "TBD, needs founder input".

## What good looks like

- At least 15 pages read, with findings in every pattern category.
- Frequencies are counts, never "usually" or "often".
- No adjective-only rules. "Friendly" isn't a guideline; "use 'you' in the first sentence of every page" is.
- Every example is real text from the site.
- A writer could pick the right tone for a support reply without asking anyone.

## Mistakes to avoid

- Writing the voice you wish they had instead of the one they have. Note the gap; don't paper over it.
- Skipping the review gate.
- Copying another company's style guide structure and filling it with adjectives.
- Rules so vague any brand could use them.

## Chain

Part of the free five-skill chain: `/icp-research` → `/competitor-research` → **tov-guidelines** → `/positioning` → `/messaging`. The other six context skills (company context, win-loss, founder POV, brand kit, funnel and goals) are free in the [context plugin](https://github.com/matteotitta/claude-marketing-context).
