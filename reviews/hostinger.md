# Review: hostinger

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `ours`
Source: `./plugins/hostinger` — written for this repository
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0 (ours). Package `hostinger-api-mcp` is MIT (hostinger/api-mcp-server, 163 stars on 2026-10-17). The marketplace plugin `hostinger/claude-plugin` has no license; nothing was read from it for this plugin.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 0 skill(s), 0 command(s), 0 agent(s), 2 MCP server(s), 0 script file(s).
- [x] **Capability** — starts process. Runs: 2 local MCP server(s) via npx, added only on request.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing.
- [x] **MCP servers** — local — `npx -y --package=hostinger-api-mcp@2.7.0 hostinger-vps-mcp` and `… hostinger-dns-mcp` (2.7.0 published 2026-10-01; 3.1.0 of 2026-10-16 is too new to pin).
- [x] **Secrets** — `${user_config.hostinger_api_token}` (sensitive, optional) → env `HOSTINGER_API_TOKEN`; empty means OAuth in the browser.
- [x] **Text read** — Everything.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — **VPS restart, snapshot restore, firewall and DNS changes affect production.** Approval per action; never from bots/cron. Billing and purchase binaries deliberately excluded.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
