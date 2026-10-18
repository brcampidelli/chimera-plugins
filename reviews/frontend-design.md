# Review: frontend-design

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `ea10b213686c90bb1984b2016937310e05336cf3`
Source: `./vendor/frontend-design` — copy of `anthropics/claude-plugins-official` / `plugins/frontend-design` at `ea10b213686c90bb1984b2016937310e05336cf3`
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: `LICENSE` in the plugin folder and `skills/frontend-design/LICENSE.txt` (Apache-2.0 text without the appendix).
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 1 skill(s), 0 command(s), 0 agent(s), 0 MCP server(s), 0 script file(s).
- [x] **Capability** — instructions only. Runs: instructions only (skills/commands/agents in Markdown).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing.
- [x] **MCP servers** — none.
- [x] **Secrets** — none.
- [x] **Text read** — Manifest read; SKILL.md scanned and spot-read.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — none.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
