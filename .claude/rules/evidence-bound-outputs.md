# Rule — evidence-bound outputs (quote, or lower confidence)

When producing any output from a transcript or call recording (e.g., `/win-loss-analysis`), every claim, score, or recommendation cites a verbatim (or near-verbatim) quote with speaker attribution — or it lowers its confidence. No invented evidence.

If the output isn't derived from a transcript, this rule is silent.

## The rule

1. **Every claim carries its quote.** A win/loss reason, an extracted theme, a score — each is backed by a verbatim quote from the transcript, with the speaker named.
2. **Attribute the speaker.** "The buyer said…", "The rep responded…". A quote with no speaker is half-evidence — the same words mean opposite things from a buyer vs. a rep.
3. **Add the locator when available.** Timestamp (`[12:34]`) or turn number, if the transcript carries them. Optional.
4. **No quote → lower the confidence, don't invent.** If the transcript doesn't support a claim, mark it `[INFERRED]` or `[ESTIMATED]`, or drop it. Never manufacture a plausible-sounding quote, paraphrase as if verbatim, or assume a business fact (deal size, competitor, outcome) the transcript doesn't state.

## Citation shape

```
> "verbatim quote from the transcript"
— Speaker (role) [timestamp if available]
```

Inline form for tight outputs:

> Strong on pain — the buyer named a quantified cost: "we're losing about 15 hours a week to this" (buyer, [08:12]).

## Near-verbatim is allowed; fabrication is not

Auto-transcripts garble words. Lightly cleaning a quote for a dropped word is fine — flag it `(cleaned)` if the change is more than trivial. Banned: paraphrasing into the buyer's mouth, compressing three sentences into one "quote," or inventing a quote that captures the "gist." Lower confidence beats invented evidence, always.

## How to check

Before any transcript-derived output ships: every factual claim has a verbatim/near-verbatim quote with a named speaker; no quote is paraphrased-as-verbatim; claims the transcript can't support are marked `[INFERRED]` / `[ESTIMATED]`, or dropped.

## Owner

Whoever owns the win-loss / transcript work.

## Refresh cadence

Reviewed each quarterly maintenance pass.
