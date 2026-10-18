# Review: stripe

Reviewer: Claude Opus 5.5 (AI agent) — not a human review
Human sign-off: pending (no maintainer has signed this review yet)
Date: 2026-10-17
Reviewed sha: `c1f5b0826f3f33d7e1cc7eff5e5e6cd42749808b`
Source: `./vendor/stripe` — copy of `stripe/ai` / `providers/claude/plugin` at `c1f5b0826f3f33d7e1cc7eff5e5e6cd42749808b`
License: MIT

## Checklist

- [x] **License read at the pinned sha** — MIT: repository-root `LICENSE` of stripe/ai (the plugin folder has none; copied into the vendor folder). The plugin manifest also says MIT.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 10 skill(s), 2 command(s), 1 agent(s), 1 MCP server(s), hooks, 10 script file(s).
- [x] **Capability** — hooks (inert in Chimera), network, scripts (a skill may ask to run them). Runs: 1 remote MCP server(s), added only on request: mcp.stripe.com; hooks present — never run by Chimera; 10 script file(s) a skill may ask to run (with your approval).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: the hooks (session-start CLI guidance, skill-usage telemetry, feedback prompts) never run in Chimera — the skills and MCP server still work; the telemetry not running is a gain.
- [x] **MCP servers** — stripe — `https://mcp.stripe.com` (Stripe's domain, OAuth).
- [x] **Secrets** — none in files.
- [x] **Text read** — Manifest, `.mcp.json` and `hooks/hooks.json` read in full; agent, commands and SKILL.md files scanned and spot-read; the `.mjs` hook scripts grepped for network/subprocess use: they call the local `stripe` CLI (`spawnSync`) to check install/login and to report skill usage to Stripe through the CLI (telemetry). References scanned.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — Upstream had `npm i -g @stripe/cli` in `skills/stripe-best-practices/SKILL.md` and two hook messages with `npm i -g @stripe/cli` / `@stripe/cli@latest` — **all rewritten** to a link to https://docs.stripe.com/stripe-cli (see MODIFICATIONS.md). Clean after the change. Not verified: `skills/stripe-directory/SKILL.md` sends the user to `https://stripe.directory`; who owns that domain was not checked against a Stripe primary source — confirm before publishing.
- [x] **Irreversible actions** — **Money.** The Stripe MCP server can create customers, prices, payment links and refunds. Every write needs approval; never from bots/cron. Prefer a restricted key / test mode.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
