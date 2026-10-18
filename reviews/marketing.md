# Review: marketing

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `33eeda1e8fd856455b05479d13a0f85b5f803744`
Source: `./vendor/marketing` — copy of `anthropics/knowledge-work-plugins` / `marketing` at `33eeda1e8fd856455b05479d13a0f85b5f803744`
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: `LICENSE` in the plugin folder.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 8 skill(s), 0 command(s), 0 agent(s), 9 MCP server(s), 0 script file(s).
- [x] **Capability** — network. Runs: 9 remote MCP server(s), added only on request: api.ahrefs.com, mcp.amplitude.com, mcp.canva.com, mcp.eu.amplitude.com, mcp.figma.com, mcp.klaviyo.com, mcp.notion.com, mcp.similarweb.com, mcp.supermetrics.com.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing.
- [x] **MCP servers** — After our change: canva, figma, amplitude (+EU), notion, ahrefs (`api.ahrefs.com`), similarweb, klaviyo, supermetrics — each on the vendor's own domain. Removed: slack, hubspot (`/anthropic` path), google calendar, gmail (empty URLs).
- [x] **Secrets** — none in files.
- [x] **Text read** — Manifest, `.mcp.json` and CONNECTORS.md read in full; the 8 skills scanned and spot-read.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — Campaign/email drafts only; sending through Klaviyo etc. needs approval.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
