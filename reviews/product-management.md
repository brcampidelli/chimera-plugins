# Review: product-management

Reviewer: Claude Opus 5.5 (AI agent) — not a human review
Human sign-off: pending (no maintainer has signed this review yet)
Date: 2026-10-17
Reviewed sha: `33eeda1e8fd856455b05479d13a0f85b5f803744`
Source: `./vendor/product-management` — copy of `anthropics/knowledge-work-plugins` / `product-management` at `33eeda1e8fd856455b05479d13a0f85b5f803744`
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: `LICENSE` in the plugin folder.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 8 skill(s), 1 command(s), 0 agent(s), 13 MCP server(s), 0 script file(s).
- [x] **Capability** — network. Runs: 13 remote MCP server(s), added only on request: api.fireflies.ai, app.pendo.io, mcp.amplitude.com, mcp.asana.com, mcp.atlassian.com, mcp.clickup.com, mcp.eu.amplitude.com, mcp.figma.com, mcp.intercom.com, mcp.linear.app, mcp.monday.com, mcp.notion.com, mcp.similarweb.com.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing.
- [x] **MCP servers** — After our change: linear, asana, monday, clickup, atlassian, notion, figma, amplitude (+EU), pendo (`app.pendo.io`), intercom, fireflies (`api.fireflies.ai`), similarweb — vendor domains. Removed: slack, google calendar, gmail.
- [x] **Secrets** — none in files.
- [x] **Text read** — Manifest, `.mcp.json` and CONNECTORS.md read in full; the command and 8 skills scanned and spot-read.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — Creating tickets in a tracker is a write through the connected server; approval applies.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
