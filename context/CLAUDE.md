# context/ — what Claude reads first

Every skill reads these folders before it writes anything. Fill them in this order:
company facts, ICP, competitors, win-loss, expert POV, brand and voice, positioning, messaging, funnel, goals.

| Folder | What goes here | Skill that fills it |
|---|---|---|
| [`icp/`](./icp/) | Who you sell to: buyer and champion, pains in their words, who not to sell to. | `/icp-research` |
| [`competitors/`](./competitors/) | One file per competitor, plus a short summary across them. | `/competitor-research` |
| [`positioning/`](./positioning/) | The category you compete in, your alternatives, what's different, who cares. | `/positioning` |
| [`messaging/`](./messaging/) | Value props, proof points per persona, the words to use and avoid. | `/messaging` |
| [`brand/`](./brand/) | Brand kit (colours, type, logo use) and your tone of voice. | `/brand-kit and /tov-guidelines` |
| [`expert-pov/`](./expert-pov/) | What the founder or expert believes about the market, in their words. | `/expert-pov` |
| [`win-loss/`](./win-loss/) | Why deals close, stall and churn, quoted from real calls. | `/win-loss` |
| [`goals/`](./goals/) | Targets, KPIs, baselines, monthly pacing, and the funnel they run through. | `/funnel-strategy then /goals` |
| [`docs/`](./docs/) | Anything else Claude should know: company facts, briefs, transcripts, rules. | `/company-context` |

Keep one current file per topic (for example `positioning.md`) and date the research behind it (`1026-competitor-acme.md`).
See [`../example/pulse-analytics/context`](../example/pulse-analytics/context) for a filled-in version.
