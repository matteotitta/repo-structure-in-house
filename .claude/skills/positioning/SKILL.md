---
name: positioning
description: >-
  Develops B2B SaaS positioning from your ICP, competitor and win-loss evidence. Maps what buyers compare
  you to, chooses between leading with a category or a problem, picks a primary and secondary anchor and
  up to three defensible differentiators, lays out 2 to 4 worked positioning options with a comparison
  canvas so you can decide, then locks the chosen one and tests it (clarity ladder, guarantee test).
  Triggers: "positioning", "how do we position", "what category are we in", "how do we differentiate
  from", "our homepage is confusing", "positioning options". Run before /messaging. Not for taglines or
  a messaging library (use /messaging).
version: '1.0.0'
license: MIT
---

# Positioning

Decide what you are, who it's for, what they'd use instead, and why you're the better choice, in words a buyer understands in five seconds. The method follows the public April Dunford school: start from the competitive alternatives buyers actually consider, and build out from there.

## When to use it

- The homepage doesn't explain what you do, or demos start with "so what is it exactly?".
- You're choosing between going broad and niching down.
- A new product, a new segment, or a competitor that moved.

Don't use it for taglines, value props or a full messaging library (`/messaging`, which runs after this), or for research you haven't done yet.

## Inputs

**Required:** company name, a short description and the website URL.

**Recommended:** `context/icp/`, `context/competitors/`, `context/win-loss/` and `context/expert-pov/`. Positioning without ICP and competitor evidence is opinion. If those are missing, say so, run what you can, and offer `/icp-research` and `/competitor-research` first.

**Paths.** Write to `context/positioning/MMYY-positioning.md`. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

## Steps

1. **Read the current state.** Fetch the homepage, pricing and about pages. Run the five-second test: do the headline and sub-headline say what it is and who it's for? Note the category, differentiation and ICP the site claims today.
2. **Map the alternatives.** What would a buyer do if you didn't exist?
   - do it manually
   - keep a legacy tool
   - buy a direct competitor
   - stretch an adjacent tool
   - do nothing
   - build it with a general AI assistant

   Rank them by how often they show up in deals.
3. **Map the anchors.** What could the positioning hang on?
   - an activity
   - a product category
   - a use case
   - a problem
   - a persona
   - a competitive alternative ("the X alternative for Y")

   Score the promising combinations on clarity, differentiation and relevance to the ICP.
4. **Make the binary choice.** Category-led (buyers already know the category and you win inside it) or problem-led (the category is new, crowded or wrong, so you lead with the pain). Use an activity anchor only when no software category fits.
5. **Lay out the options.** Take the top 2 to 4 combinations (3 by default) and work each one up:
   - primary and secondary anchor
   - a hero headline and sub-headline
   - the value in three parts: category, problem, differentiation
   - who it's for
   - the bet it makes
   - the risks

   Each option must change the anchor or the binary choice. No rewording of the same bet.
6. **Build the comparison canvas.** One column per option, rows for clarity, differentiation, ICP relevance, proof available, competitive exposure and risk. Mark each cell's confidence: verified, inferred, estimated or unknown. Recommend one and name the trade-off each option forces. The user decides.
7. **Lock the chosen option.** Up to three differentiators, each one a thing you'd guarantee with money on the line (pass, partial or fail). Name the primary competitive alternative and the market focus, with simple TAM maths (average deal size × customers needed).
8. **Run the clarity ladder.** Compress the position to one word, one phrase, one sentence and one paragraph. If a level fails, go back to the anchors.
9. **Write the positioning statement** in the form that fits the anchor:
   - Use case: "We help [persona] [do the job] without [friction], by [approach]."
   - Category: "We are a [category] that [differentiator], unlike [alternative] which [weakness]."
   - Alternative: "We're the [leader] alternative that [upgrade], for [persona] who [unmet need]."
   - Activity: "We help [persona] [do activity], replacing [manual process] with [mechanism]."
10. **Map the implications.** What changes for messaging, for the ICP, and which channel leads with which facet (homepage: primary anchor; comparison pages: the alternative; case studies: proof that matches the anchor).
11. **Hand off** to `/messaging`.

## Output shape

Open with a TLDR (the one-sentence position) and one block of open decisions. Then: current state, alternatives, the options with the canvas, the committed position (anchors, differentiators with guarantee verdicts, statement, clarity ladder), implications, and sources. Each caveat is stated once.

## What good looks like

- A stranger reads the hero and knows what it is and who it's for in five seconds.
- No more than three differentiators, each one provable.
- The comparison set matches the buyer. Compare to other vendors only when buyers already use the category.
- The options are real choices, not three phrasings of one idea.
- The TAM maths is realistic, not hopeful.

## Mistakes to avoid

- "The platform for X" with nothing else.
- "AI-powered" as the main differentiator.
- Inventing a category nobody searches for.
- Choosing the position before mapping the alternatives.
- Differentiators you couldn't prove to a sceptical buyer.

## Chain

Part of the free five-skill chain: `/icp-research` → `/competitor-research` → `/tov-guidelines` → **positioning** → `/messaging`. The other six context skills (company context, win-loss, founder POV, brand kit, funnel and goals) are in the paid context plugin ($19.99, link in the README).
