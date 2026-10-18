# Review: cli-for-agent

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `1b800800583ee8ff7f2676caf7a5cb7f0804be85`
Source: `./ports/cli-for-agent` — port of `cursor/plugins` / `cli-for-agent` at `1b800800583ee8ff7f2676caf7a5cb7f0804be85`
License: MIT

## Checklist

- [x] **License read at the pinned sha** — MIT: `LICENSE` in the upstream folder.
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
