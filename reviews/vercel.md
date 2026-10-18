# Review: vercel

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `137e9f44a243a939c5eaea30e4dff96aee744f64`
Source: github `vercel/vercel-plugin` at `137e9f44a243a939c5eaea30e4dff96aee744f64` (not copied here)
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: root `LICENSE` holds the short Apache-2.0 header (Copyright 2026 Vercel, Inc.); GitHub reports NOASSERTION because it is not the full text; the manifest says Apache-2.0.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 43 skill(s), 5 command(s), 3 agent(s), 1 MCP server(s), hooks, 80 script file(s).
- [x] **Capability** — hooks (inert in Chimera), network, scripts (a skill may ask to run them). Runs: 1 remote MCP server(s), added only on request: mcp.vercel.com; hooks present — never run by Chimera; 80 script file(s) a skill may ask to run (with your approval).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: the hooks (telemetry, CLAUDE.md injection, skill auto-injection by file pattern) never run in Chimera. Skills still load by description; auto-injection by file pattern is lost; the telemetry not running is a gain.
- [x] **MCP servers** — vercel — `https://mcp.vercel.com` (Vercel's domain, OAuth). The server can deploy and change projects.
- [x] **Secrets** — none in files.
- [x] **Text read** — Manifest, `.mcp.json`, `hooks/hooks.json`, the 3 agents and 4 commands read; the 43 skills scanned with `scripts/check.py --scan` and spot-read; hook scripts grepped for network use: `posttooluse-skill-telemetry.mjs`, `setup-telemetry.mjs` and `skill-telemetry.mjs` send skill-usage telemetry; `inject-claude-md.mjs` injects text at session start.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — 75 findings at this sha, all of the same two kinds: `@latest` in Vercel CLI / Workflow / AI SDK install instructions and `npm i -g vercel` in the CLI skill; no `curl | sh`, no reader-directed text. Not in this repository (github+sha source), so CI does not scan it — this review is the record.
- [x] **Irreversible actions** — **Deploys change production.** Every deploy, env change and domain action needs approval; never from bots/cron.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
