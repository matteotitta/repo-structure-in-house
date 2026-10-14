---
name: brand-kit
description: >-
  Extracts a company's visual identity from screenshots (best) or its website (fallback) and writes a
  DESIGN.md brand file: machine-readable tokens for colours, typography, spacing, corner radius and logo
  usage, plus short prose explaining how and when to use each, and a list of do's and don'ts. Any later
  page, deck, carousel or ad can read the tokens instead of guessing. Triggers: "brand kit", "brand
  guidelines", "extract our brand", "design tokens", "colours and fonts from", "visual identity",
  "DESIGN.md". Not for tone of voice (use /tov-guidelines) or messaging (use /messaging).
version: '1.0.0'
license: MIT
---

# Brand kit

Turn what a brand looks like into a file other work can rely on. The tokens at the top are the source of truth: when a later page needs the primary colour, it reads the hex value from here instead of approximating it from a description. The prose underneath explains why each choice exists and how to use it.

## When to use it

- Building the context folder, before any visual output.
- When the team keeps producing off-brand pages, decks or ads.
- When a brand guide exists as a PDF nobody opens, and you want it in a form AI tools can read.

Don't use it for voice (`/tov-guidelines`), for messaging (`/messaging`), or to design a new identity from scratch unless that's explicitly what the user asked for.

## Inputs

**Required:** one visual source and the company name. The visual source is either:
- 3 to 5 screenshots: homepage, about, pricing, a feature page. This gives the highest fidelity.
- a website URL, where you capture screenshots yourself if you can.
- a brand PDF.

**Optional:** the website URL alongside screenshots (to read exact hex codes and font names from the CSS), a Figma file, logo files, an existing brand guide.

**Decide the job first:** apply the brand as it is (most common), fill in only the missing pieces, or create a new identity (only when asked).

**Paths.** Write to `context/brand/MMYY-brand-kit.md`. Agency or consultant? Swap `context/` for `clients/<client>/context/` throughout.

**Tools.** Your own vision on screenshots does most of the work. Page fetching or Firecrawl can read CSS for exact values. A browser automation tool can take screenshots from a URL if you have one.

## Steps

1. **Capture.** Get the screenshots, including pages that show icons, illustrations and photos in context, not just the logo.
2. **Analyse.** Colours (primary, secondary, accent, background, text), fonts and sizes, spacing rhythm, corner radius, buttons and cards, imagery style.
3. **Cross-check** against the CSS if you have the URL. When the CSS and the screenshot disagree, trust the screenshot.
4. **Score confidence** 0 to 5 on every token, and note where it came from.
5. **Write the tokens.** A YAML block at the top of the file:
   - `colors`: at least a `primary`, plus secondary, accent, background, surface, text, muted. Hex values.
   - `typography`: heading and body font families, weights, a size scale.
   - `spacing`: a base unit and scale.
   - `rounded`: corner radius values.
   - `logo`: which file to use on light and dark backgrounds, minimum size, clear space.
   - Refer to other tokens as `{colors.primary}` rather than repeating the hex.
6. **Write the prose sections,** in this order:
   - overview and mood
   - logo usage
   - colours, with what each is for
   - typography
   - layout and spacing
   - shapes
   - imagery
   - do's and don'ts
7. **Make the do's and don'ts quantitative.** Accent colour on no more than about 10% of a screen. No more than two font weights per screen. One primary action per screen. Name the brand's one signature element and limit it to one use per surface.
8. **Check the file.**
   - every `{token}` reference resolves
   - a primary colour exists
   - text and background pairs meet WCAG AA contrast
   - every colour token is used somewhere
9. **Mark gaps** as `[NEEDS VERIFICATION]` with your best estimate.

## What good looks like

- Every hex value was seen in a screenshot or the CSS. Nothing is guessed.
- Font names are confirmed, or described by shape with likely candidates flagged.
- Logo rules only describe files that exist.
- A designer, or an AI building a landing page, could produce an on-brand page from this file alone.
- The do's and don'ts are specific to this brand, not generic design advice.

## Mistakes to avoid

- Inventing an icon set or illustration style the brand doesn't have. "No icon set" is a valid finding.
- Approximating colours from a description ("a warm red") instead of extracting the value.
- Describing the brand in adjectives with no tokens.
- Letting the signature element creep into every section.

## Chain

Step 7 of the suggested chain: `/company-context` → `/icp-research` → `/competitor-research` → `/win-loss` → `/expert-pov` → `/tov-guidelines` → **brand-kit** → `/positioning` → `/messaging` → `/funnel-strategy` → `/goals`.
