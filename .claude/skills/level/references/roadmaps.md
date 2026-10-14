# Roadmaps — one transition at a time

Show ONLY the section matching the assessed level. Focus is everything. Each roadmap is 3-4 steps with time estimates, recalibrated to current Anthropic-native features. Times are rough.

---

## Tourist → Marked (L0→1): get grounded

**Unlocks:** Claude remembers your preferences and follows your rules — consistent output instead of generic answers every session.

1. **Create your CLAUDE.md** (10 min). The single most important file — read at the start of every session. Include: who you are, what you do, communication preferences, project context, output-quality rules. Onboard it like a new teammate.
2. **Set up a git project** (2 min). Dedicated folder, `git init`, CLAUDE.md at the root.
3. **Learn the core commands** (5 min). `/compact`, `/model`, `/cost`, `/help`, and `/clear`.
4. **Run a real task** (10 min). Not a toy — something you actually need. Watch it follow your CLAUDE.md.

*Tip:* the quality of your repo dictates the quality of your output. *Mistake:* a vague CLAUDE.md. "Be helpful" means nothing; "short paragraphs, data-backed claims, no jargon" means everything.

---

## Marked → Plugged (L1→2): connect your tools

**Unlocks:** Claude reads your actual Slack / Drive / Notion / Gmail. No more copy-pasting context.

1. **Pick your first MCP** (5 min). Start where your work lives (Drive, Notion, Slack, or Gmail). Prefer a **plugin** over raw config — plugins load as deferred tools (zero startup cost).
2. **Wire it** (5 min). Plugin install, or add to project-scoped `.mcp.json` (committing it means teammates inherit the same tools). Restart Claude Code.
3. **Test with a real task** (5 min). "Summarize the last 5 messages in #general", "action items from my last meeting notes".
4. **Get to 3+ MCPs across categories** (10 min). Plugged = 3+ wired. Cross-referencing two sources is where the magic starts.

*Tip:* fewer is better than many — too many MCPs bloat startup context. Prefer plugins (deferred) + project-scope over user-scope. *Mistake:* installing 15 MCPs on day one.

---

## Plugged → Skilled (L2→3): build your skills

**Unlocks:** repeatable workflows you trigger with one command instead of re-explaining every session.

1. **Find your most-repeated task** (5 min). What do you explain at least weekly with a consistent structure? That's skill #1.
2. **Create the skill** (10 min). `.claude/skills/{name}/SKILL.md` (or `.claude/commands/{name}.md`). Frontmatter + steps + output format + rules.
3. **Test and iterate** (5 min). Run it, see what's off, edit. Good skills get specific over time — add examples + edge cases.
4. **Build 2-3 more** (ongoing). Research / review / create is the core three. They compound: `/research` feeds `/create` feeds `/review`.

*Tip:* skills turn Claude into a teammate who never forgets the process. *Mistake:* never iterating — the first version is never the keeper.

---

## Skilled → Architect (L3→4): become a context architect

**Unlocks:** a knowledge system. Claude draws from accumulated patterns, profiles, and examples — output improves over time.

1. **Design the memory architecture** (20 min). Use the **memory tool** and/or a `memory/` tree (company / customers / patterns / examples). One topic per file.
2. **Connect it via CLAUDE.md** (10 min). CLAUDE.md becomes the index — navigation table mapping needs → file paths; a "before starting work" routing rule.
3. **Seed it** (30 min). Your top 5 patterns/frameworks; 3-5 reference outputs; a profile for your main project.
4. **Build the feedback loop** (ongoing). After each project, extract what worked into `patterns/`. Add rules. This is where compounding starts.

*Tip:* context quality = output quality. This is context engineering, not prompt engineering. *Mistake:* a memory dir CLAUDE.md never references — unrouted memory is dead weight.

---

## Architect → Conductor (L4→5): build systems, not skills

**Unlocks:** multi-phase workflows + a team feel. You become the architect, not the operator.

1. **Write multi-phase skills** (15 min). Add phases with approval gates (research → create → review).
2. **Chain skills** (10 min). Design skills that feed each other; reference each other in the files.
3. **Use subagents** (10 min). The Agent tool spins up specialists (Explore / Plan / general-purpose) running in parallel. Define roles in `.claude/agents/`. Default to **fresh** context; **fork** only for continuation-of-thought.
4. **Set up hooks as quality gates** (10 min). PreToolUse (block writes to `.env`), PostToolUse (auto-lint). Add **output styles** to shape voice. Hooks are guardrails, not infra.

*Tip:* L4→5 is where Claude Code stops feeling like a tool and starts feeling like a team. Build the orchestration layer, not just more skills.

---

## Conductor → Machinist (L5→6): programmatic pipelines

**Unlocks:** Claude as a programmable component — scripts call it, data pipes through, no human in the loop for routine work.

1. **Headless mode** (5 min). `claude -p "..."`, pipe data in (`cat data.csv | claude -p "..."`), JSON output for chaining. (Slash commands are interactive-only — in headless, pipe the prompt text.)
2. **First automation script** (15 min). A shell script that calls `claude -p` with `--allowedTools` for a routine task (a morning briefing that writes itself).
3. **Chain outputs programmatically** (10 min). JSON out → another tool → an API.
4. **Author a plugin / try the Agent SDK** (ongoing). Package skills as a distributable plugin; or build a real app on the Agent SDK. Wire into CI.

*Tip:* L6 is the practical ceiling for most use cases. Beyond here you're building infrastructure.

---

## Machinist → Hunter (L6→7): browser power

**Unlocks:** Claude controls a browser — scrape, screenshot, PDF, fill forms, crawl-and-synthesize research pipelines.

1. **Install browser tools** (5 min). A browser MCP (Chrome DevTools / Playwright / Puppeteer).
2. **Screenshot + PDF generation** (10 min). HTML → PNG → PDF skills for branded decks, carousels, one-pagers.
3. **Web-scraping workflows** (15 min). A `/research [company]` skill that scrapes site + news → structured brief.
4. **Research pipelines** (ongoing). Browser + MCPs: scrape → store in Notion → alert in Slack. On-demand competitive intel.

*Tip:* this is where Claude Code starts replacing paid SaaS (decks, design, scraping tools).

---

## Hunter → Ringleader (L7→8): multi-agent operations

**Unlocks:** multiple Claude instances in parallel, each a specialist. You're the tech lead.

1. **Parallel agents** (10 min). Use `/workflows` to fan out deterministic multi-agent work, or run multiple instances (tmux / separate windows). One researches, one writes, one reviews — simultaneously.
2. **Define agent roles** (15 min). Role-agents with their own context + instructions; an orchestrator that decomposes + routes. Pass work via shared files.
3. **Isolate with worktrees** (15 min). Git worktrees (or the Agent tool's `isolation: worktree`) so parallel agents don't collide. Orchestrator reviews + merges.
4. **Coordination patterns** (ongoing). Sequential pipeline / parallel fan-out / supervisor delegation / consensus voting — match the pattern to the problem.

*Tip:* multiple agents without coordination create chaos, not productivity. Discipline first.

---

## Ringleader → Nightshift (L8→9): always on

**Unlocks:** Claude runs whether you're at your desk or not. Scheduled tasks, monitoring, event triggers. Infrastructure.

1. **Scheduled automation** (15 min). `/schedule` or CronCreate for recurring remote agents; cron/launchd for local headless runs. Weekly reports, daily digests, periodic audits. (Headless = `-p` + plain text, not slash commands.)
2. **Persistent background agents** (15 min). Background tasks / pm2 / systemd for continuous runs. An agent watches a queue + processes items. Log rotation + restart policy.
3. **Monitoring + alerting** (15 min). Claude watches a data source + alerts on change (competitor pricing, a metric threshold).

*Tip:* L9 is where "using a tool" becomes "running a system." Most project-based work is happiest at 5-7; L9 is for continuous operations.

---

## Nightshift → Swarm (L9→10): swarm architecture

**Unlocks:** autonomous execution — agents that manage agents, systems that take a goal and work toward it.

1. **Autonomous loops** (advanced). Give Claude a spec + a test suite; it picks a task, implements, tests, commits if green, repeats. Safety: sandbox, clear modify-boundaries, review before pushing to main, max-iteration cap, kill switch.
2. **Multi-agent orchestration framework** (advanced). An orchestrator decomposes → specialists execute → a reviewer validates. Each agent has its own context, memory, skills (an orchestration layer-style control plane + wave-batch).
3. **Agent-to-agent coordination** (advanced). Shared task queue + results; git-based coordination (branches/PRs/merges); status files agents read + update.

*Tip:* L10 is experimental and high-maintenance. It's "build, monitor, iterate", not "set and forget." Very few people are here.
