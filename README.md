![Repo structure for in-house marketers](.github/banner.png)

# Repo structure for in-house marketers

The folder layout that gives Claude Code your company's context before it writes anything. Fork it, fill `context/` with the 11 skills inside, and every draft after that starts from your ICP, your positioning and your voice. You stop re-explaining your product every session.

**[Use this template →](https://github.com/new?template_name=repo-structure-in-house&template_owner=matteotitta)**

Agency or consultant with several clients? Use [repo-structure-agency](https://github.com/matteotitta/repo-structure-agency) instead.

---

## Start in three steps

1. **Create your copy.** Click *Use this template* above, or run:
   ```bash
   gh repo create my-marketing --template matteotitta/repo-structure-in-house --private --clone
   ```
2. **Open it in Claude Code** and read the example first: `example/pulse-analytics/` is a made-up B2B SaaS company with every context file filled in.
3. **Fill your context in this order.** Each skill asks for what it needs and saves into the right folder:
   ```
   /company-context → /icp-research → /competitor-research → /win-loss → /expert-pov
   → /tov-guidelines → /brand-kit → /positioning → /messaging → /funnel-strategy → /goals
   ```
   `/win-loss` needs call transcripts and `/expert-pov` needs founder material. Skip either until you have them.

Web research works best with an [Exa](https://exa.ai) key in `.env` (copy `env` to `.env`). Without one, the skills fall back to plain web search.

---

## What's inside

```
repo-structure-in-house/
├── context/          what Claude reads first: icp, competitors, positioning, messaging,
│                     brand, expert-pov, win-loss, goals, docs
├── outputs/          what you ship, by lane: content, website, seo-aeo, social,
│                     product-marketing, sales, paid, lifecycle, outbound
│                     (each lane runs research → strategy → execution)
├── workflows/        recipes that chain several skills
├── library/taste/    work you admire, for "in the style of"
├── example/          PulseAnalytics, filled in. Read it, then delete it
├── latest.md         what changed recently (Claude reads it at the start)
├── history.md        one line per meaningful change
└── .claude/
    ├── skills/       the 11 context skills, plus /level
    └── rules/        four short house rules
```

Every folder has a one-page `CLAUDE.md` that says what goes there and which skill fills it.

**The idea:** `context/` is written once and kept current. `outputs/` is where work happens. Because every skill reads `context/` before it writes, a landing page, a launch plan and a LinkedIn post all come out sounding like the same company.

---

## Add skills for each lane

The 11 skills here build your context. When you're ready to ship work, add the plugin for that lane. Each one reads the same `context/` folder:

| Lane | Plugin |
|---|---|
| Product launches, stories, case studies | [claude-marketing-launch](https://github.com/matteotitta/claude-marketing-launch) |
| Website score, sitemap, wireframes, copy | [claude-marketing-website](https://github.com/matteotitta/claude-marketing-website) |
| AI-answer and search visibility | [claude-marketing-aeo](https://github.com/matteotitta/claude-marketing-aeo) |
| LinkedIn profile, posts, carousels | [claude-marketing-linkedin](https://github.com/matteotitta/claude-marketing-linkedin) |
| Content strategy, long-form, newsletter | [claude-marketing-content](https://github.com/matteotitta/claude-marketing-content) |

Want to build your own skills? Start from [gtm-skill-template](https://github.com/matteotitta/gtm-skill-template).

---

## What the full version adds

This is the free shape of the workspace students build in [Marketing Engineering University](https://maven.com/matteo-tittarelli/marketing-engineering-university-genesys-growth). The course version adds:

- the full skill library, with the reference material and output templates these free skills leave out
- agents, commands and hooks that chain the skills and check their own work
- live sessions where you build the system on your own company

The free version is enough to get your context right. That's the step most teams skip.

---

## Keep it alive

- Every file in `context/` has one owner.
- Re-run a context skill when something real changes: a new competitor, a pricing change, a new segment.
- Every 90 days, spend 30 minutes pruning. See [`.claude/rules/quarterly-maintenance.md`](.claude/rules/quarterly-maintenance.md).

[`HOW-TO-OPERATE.md`](HOW-TO-OPERATE.md) has seven habits for getting real work out of Claude Code.

---

Built by [Matteo Tittarelli](https://www.linkedin.com/in/matteotittarelli/) at [Genesys Growth](https://genesysgrowth.com). MIT licensed: fork it, change it, use it with clients.
