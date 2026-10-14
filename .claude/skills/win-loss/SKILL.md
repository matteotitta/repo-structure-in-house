---
name: win-loss
description: >-
  Analyses sales call transcripts (and churn or renewal calls) to find why deals are won, lost, kept or
  churned. Reads each call across six dimensions (product, messaging, sales process, pricing,
  competition, customer context), pulls verbatim quotes with the speaker named, counts how often each
  pattern appears, and writes findings with recommendations. Works with any recorder export or pasted
  text. Triggers: "win/loss analysis", "why do we lose", "why do we win", "analyse these sales calls",
  "lost deals", "churn analysis", "objection patterns". Feeds /positioning and /messaging. Not for
  general meeting summaries or competitor research (use /competitor-research).
version: '1.0.0'
license: MIT
---

# Win-loss

Turn sales calls into evidence about why people buy and why they don't. The quotes are the main product; the summary is secondary. Every pattern you report has to trace back to something a person said on a call.

## When to use it

- After 5 or more closed deals with recordings or notes.
- Before positioning or messaging work, to replace opinions about objections with evidence.
- When win rate drops, or a competitor starts showing up in losses.
- Monthly, as a standing review for a team with steady deal flow.

Don't use it for one-off meeting notes, for researching competitors from the outside (`/competitor-research`), or for picking an ICP on its own (feed the findings into `/icp-research`).

## Inputs

**Required:** transcripts, each with the customer (or a code name) and the outcome: win, loss, retention or churn. If the outcome isn't given, ask. Only infer it when the call itself states it.

**Optional:** deal size and stage, competitor names to watch for, `context/icp/` and `context/competitors/` for cross-referencing.

**Paths.** Write to `context/win-loss/MMYY-win-loss.md`. Keep a short `context/win-loss/win-loss-strategy.md` across runs: decisions made, definitions agreed, things to stop doing. Read it first on every run. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

**Tools.** None needed beyond the transcripts. If a call recorder or CRM is connected, pull from it; otherwise the user pastes or uploads files.

## Before you analyse

- **Normalise the format.** Recorder exports, subtitle files, JSON and pasted text all become one shape: speaker-attributed turns, with timestamps where they exist.
- **Redact personal data.** Mask end-customer names, emails, phone and account numbers. Keep roles, company type and deal context.
- **Bind every claim to a quote.** A finding without a quote and a named speaker role doesn't ship.

## The six dimensions

| Dimension | Win signals | Loss signals |
|---|---|---|
| Product | "Exactly what we need" | "It doesn't do X" |
| Messaging | "Now I see why this matters" | "What does it actually do?" |
| Sales process | "You understood our problem" | "The demo missed our use case" |
| Pricing | "Fair for what we get" | "Over budget", "too expensive" |
| Competition | "Chose you over Y" | "Going with Y" |
| Customer context | "We need this by Q2" | "No rush, maybe next year" |

## Steps

1. **Read the strategy file** if one exists, and apply its locked definitions.
2. **Process each call.** Classify the outcome, tag speakers (buyer, champion, rep), and pull quotes against the six dimensions. *Produces:* a per-call evidence table.
3. **Aggregate by outcome.** Group wins, losses, retention and churn. Count how many calls support each pattern ("4 of 7 losses").
4. **Rank patterns.** Three or more mentions is a pattern. Two is emerging. One is a single mention, labelled as unconfirmed.
5. **Cross-reference** by segment, deal size or competitor where the data allows. Look across at least three cuts, not just competitor.
6. **Separate product gaps from sales execution.** They go to different teams.
7. **Write insights.** For each: the pattern, the evidence with frequency and quotes, the confidence, and what to do about it.
8. **Update the strategy file** with new decisions and definitions.
9. **Hand off** to `/positioning` and `/messaging`.

## Output shape

Open with a 3-line TLDR and the sample size, stated once. Then: an executive summary, top win drivers, top loss drivers, objection themes with suggested responses, competitor mentions, a per-dimension breakdown, recommendations split into product, messaging and sales, and an appendix of quotes by call.

Confidence: high is 3 or more consistent calls, medium is 2 or strong indirect signals, low is a single mention.

## What good looks like

- Every finding has a frequency and at least one verbatim quote with a speaker role.
- Patterns are described as "associated with", not "caused by".
- Small samples are flagged clearly. Under 5 wins and 5 losses, findings are directional.
- Dimensions with no data say "not discussed in transcripts".
- A seller could use the objection section on their next call.

## Mistakes to avoid

- Summarising what buyers said instead of quoting them.
- Treating one memorable call as a pattern.
- Mixing up what the rep said with what the buyer said.
- Reading cause into correlation ("long cycles lose deals").
- Keeping customer names or emails in the saved file.

## Chain

Step 4 of the suggested chain: `/company-context` → `/icp-research` → `/competitor-research` → **win-loss** → `/expert-pov` → `/tov-guidelines` → `/brand-kit` → `/positioning` → `/messaging` → `/funnel-strategy` → `/goals`.
