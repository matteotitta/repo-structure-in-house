---
name: messaging
description: >-
  Builds a product messaging library from your positioning, your website and customer evidence: a
  description, the status quo and alternatives, pain points with their knock-on consequences,
  capabilities, functional, emotional and social benefits, branded features, the cost of doing nothing,
  common objections with responses, and core messaging blocks (tagline, elevator pitch, value props,
  proof, per-audience lines). Every claim sourced. Triggers: "product messaging", "messaging library",
  "messaging framework", "value props", "capabilities and benefits", "what are our differentiators in
  words". Run after /positioning. Not for choosing the position itself (use /positioning).
version: '1.0.0'
license: MIT
---

# Messaging

Turn the position into the words people will actually use: on the website, in sales calls, in emails and ads. The library links each pain to a capability, each capability to a benefit, and each benefit to proof, so any writer can pull a line and know it holds up.

## When to use it

- Right after `/positioning` is agreed.
- Before rewriting the website, a sales deck or a launch.
- When sales, marketing and product describe the product three different ways.

Don't use it to choose the position (`/positioning`), or for a single-feature question you can answer directly.

## Inputs

**Required:** the website URL and the exact product name. Confirm the name if it's ambiguous.

**Recommended:** read these first if they exist:
- `context/positioning/`, the primary input, which frames everything
- `context/icp/` for pains and voice of customer
- `context/competitors/` for the status quo and contrasts
- `context/win-loss/` for real objections
- `context/brand/` for tone of voice

Also useful: internal docs and customer quotes. If positioning is missing, say so and offer `/positioning` first.

**Paths.** Write to `context/messaging/MMYY-messaging.md`. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

**Tools.** Page fetching for the site; web search for reviews, testimonials and comparison pages. Exa or Firecrawl if you have them.

## Steps

1. **Validate inputs** and load the upstream context.
2. **Research.** Fetch at least five core pages (home, features, pricing, customers, about) with URLs and dates. Search reviews and testimonials. Record branded feature names exactly as the company writes them.
3. **Extract the ten components, in order:**
   1. **Description.** What it is, in one or two sentences, using the positioning.
   2. **Status quo and alternatives.** Doing it by hand, plus at least one named alternative.
   3. **Pain points.** Each with a consequence chain: the first-order problem, what it causes, what that costs the business.
   4. **Capabilities.** What the product does about each pain.
   5. **Functional benefits.** The outcome, each backed by a verbatim customer quote or marked "not available".
   6. **Emotional and social benefits.** Two of each: how the buyer feels, and how they look to their boss and team.
   7. **Features.** The branded names that deliver each capability.
   8. **Cost of inaction.** What not acting costs per week or month, in numbers where you can.
   9. **Objections.** 3 to 5, each with its root cause and a response that acknowledges, reframes and gives evidence.
   10. **Core messaging blocks.** A tagline of 7 words or fewer, a one-sentence elevator pitch, a 3-bullet value prop, a lead proof point, and one line per audience segment.
4. **Link it up.** Every pain points to a capability, every capability to a feature and a benefit.
5. **Verify.** Check each claim against its source. Quotes are verbatim. Tag confidence `[VERIFIED]`, `[INFERRED]`, `[ESTIMATED]` or `[UNAVAILABLE]`. For a client-facing library, aim for at least 60% verified and no more than 10% estimated.
6. **Write the data gaps** and how to fill each one.
7. **Hand off** to `/funnel-strategy`, and to any copy work.

## Output shape

Title it `# Product messaging library: [Product]`. Open with a TLDR and one block of open questions. Then the ten components in order, a data gaps section, and a source list with URLs and access dates.

## What good looks like

- All ten components present, or marked "not available" with a reason.
- No pain point stops at the first-order problem.
- The cost of inaction has a number, not an adjective.
- The tagline and pitch match the agreed position. If they don't, flag it rather than drifting.
- A seller could answer the top three objections using only this file.

## Mistakes to avoid

- Feature lists dressed up as benefits.
- Invented customer quotes or made-up metrics.
- Messaging that contradicts the positioning because a line sounded better.
- Buzzwords where a plain verb would do.
- Repeating the same caveat in every component. Say it once.

## Chain

Part of the free five-skill chain: `/icp-research` → `/competitor-research` → `/tov-guidelines` → `/positioning` → **messaging**. The other six context skills (company context, win-loss, founder POV, brand kit, funnel and goals) are free in the [context plugin](https://github.com/matteotitta/claude-marketing-context).
