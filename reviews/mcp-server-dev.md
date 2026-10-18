# Review: mcp-server-dev

Reviewer: Claude Opus 5.5 (AI agent) — not a human review
Human sign-off: pending (no maintainer has signed this review yet)
Date: 2026-10-17
Reviewed sha: `ea10b213686c90bb1984b2016937310e05336cf3`
Source: `./vendor/mcp-server-dev` — copy of `anthropics/claude-plugins-official` / `plugins/mcp-server-dev` at `ea10b213686c90bb1984b2016937310e05336cf3`
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: `LICENSE` in the plugin folder.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 3 skill(s), 0 command(s), 0 agent(s), 0 MCP server(s), 0 script file(s).
- [x] **Capability** — instructions only. Runs: instructions only (skills/commands/agents in Markdown).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing.
- [x] **MCP servers** — none.
- [x] **Secrets** — Guides tell the user to keep OAuth secrets in environment variables.
- [x] **Text read** — Manifest read; the 3 SKILL.md and 16 reference files scanned and spot-read (scaffolding guides).
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — Upstream had `npm create cloudflare@latest` in a deploy guide — **rewritten** to `@<version>` with a link to Cloudflare's C3 page (see MODIFICATIONS.md). Clean after the change.
- [x] **Irreversible actions** — none by the plugin.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
