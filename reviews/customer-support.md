# Review: customer-support

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `33eeda1e8fd856455b05479d13a0f85b5f803744`
Source: `./vendor/customer-support` — copy of `anthropics/knowledge-work-plugins` / `customer-support` at `33eeda1e8fd856455b05479d13a0f85b5f803744`
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: `LICENSE` in the plugin folder (repository root is also Apache-2.0).
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 5 skill(s), 0 command(s), 0 agent(s), 4 MCP server(s), 0 script file(s).
- [x] **Capability** — network. Runs: 4 remote MCP server(s), added only on request: mcp.api.getguru.com, mcp.atlassian.com, mcp.intercom.com, mcp.notion.com.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing (no hooks).
- [x] **MCP servers** — After our change: intercom (`mcp.intercom.com`), guru (`mcp.api.getguru.com`), atlassian (`mcp.atlassian.com`), notion (`mcp.notion.com`) — each on the vendor's own domain. Removed: slack (Anthropic's OAuth client id), hubspot (`/anthropic` path), google calendar and gmail (empty URLs).
- [x] **Secrets** — none in files; each server authenticates with its own OAuth.
- [x] **Text read** — Manifest, `.mcp.json` and CONNECTORS.md read in full; the 5 skills scanned and spot-read.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — Skills draft responses and articles; sending them goes through the connected service and needs your approval.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
