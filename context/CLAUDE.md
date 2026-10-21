# context/ — what Claude reads first

Every skill reads these folders before it writes anything. Fill them in this order:
ICP, competitors, voice, positioning, messaging.

Win-loss, founder POV, brand kit, funnel and goals come from the free [context plugin](https://github.com/matteotitta/claude-marketing-context) when you want them.

| Folder | What goes here | Skill that fills it |
|---|---|---|
| [`icp/`](./icp/) | Who you sell to: buyer and champion, pains in their words, who not to sell to. | `/icp-research` |
| [`competitors/`](./competitors/) | One file per competitor, plus a short summary across them. | `/competitor-research` |
| [`positioning/`](./positioning/) | The category you compete in, your alternatives, what's different, who cares. | `/positioning` |
| [`messaging/`](./messaging/) | Value props, proof points per persona, the words to use and avoid. | `/messaging` |
| [`brand/`](./brand/) | Your tone of voice: how you sound, the words to use and avoid. | `/tov-guidelines` |
| [`docs/`](./docs/) | Anything else Claude should know: company facts, briefs, transcripts. | `no skill: add files by hand` |

Keep one current file per topic (for example `positioning.md`) and date the research behind it (`1026-competitor-acme.md`).
See [`../example/pulse-analytics/context`](../example/pulse-analytics/context) for a filled-in version.
