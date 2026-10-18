# Review: data

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `33eeda1e8fd856455b05479d13a0f85b5f803744`
Source: `./vendor/data` — copy of `anthropics/knowledge-work-plugins` / `data` at `33eeda1e8fd856455b05479d13a0f85b5f803744`
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: `LICENSE` in the plugin folder.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 10 skill(s), 0 command(s), 0 agent(s), 6 MCP server(s), 1 script file(s).
- [x] **Capability** — network, scripts (a skill may ask to run them). Runs: 6 remote MCP server(s), added only on request: api.definite.app, app.hex.tech, bigquery.googleapis.com, mcp.amplitude.com, mcp.atlassian.com, mcp.eu.amplitude.com; 1 script file(s) a skill may ask to run (with your approval).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing.
- [x] **MCP servers** — After our change: bigquery (`bigquery.googleapis.com`), hex, amplitude (+EU), atlassian, definite (`api.definite.app`). Removed: snowflake and databricks (empty URLs). Note: the plugin name `data` is generic and collides with Anthropic's own `data` plugin if both marketplaces are added.
- [x] **Secrets** — none in files.
- [x] **Text read** — Manifest and `.mcp.json` read in full; skills and references scanned and spot-read; `scripts/package_data_skill.py` checked (zips a generated skill folder; stdlib only, no network).
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — SQL can write if the connected database allows it — use read-only credentials.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
