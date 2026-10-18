# Review: superpowers

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `bb92a77741419a4ab5f06e711a283343f1ada0c3`
Source: github `obra/superpowers` at `bb92a77741419a4ab5f06e711a283343f1ada0c3` (not copied here)
License: MIT

## Checklist

- [x] **License read at the pinned sha** — MIT: root `LICENSE` (Copyright 2025 Jesse Vincent).
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 15 skill(s), 0 command(s), 0 agent(s), 0 MCP server(s), hooks, 16 script file(s).
- [x] **Capability** — hooks (inert in Chimera), scripts (a skill may ask to run them). Runs: hooks present — never run by Chimera; 16 script file(s) a skill may ask to run (with your approval).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: the SessionStart hook that forces the 'using-superpowers' skill into every session never runs in Chimera — the skills are available by description instead. That hook is also a 'dominates every turn' trigger, so losing it is acceptable.
- [x] **MCP servers** — none.
- [x] **Secrets** — none.
- [x] **Text read** — Manifest, `hooks/` (SessionStart hook injects the `using-superpowers` skill), read in full; the 15 SKILL.md scanned and spot-read; scripts scanned (brainstorming visual companion server, test helpers).
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — 1 finding: root `AGENTS.md` opens with 'If You Are an AI Agent' — contributor guidance asking agents not to open low-quality PRs to that repo. Benign and not a plugin component (Chimera does not load a plugin's AGENTS.md).
- [x] **Irreversible actions** — Skills push toward subagent-driven development and git worktrees; commits/pushes still go through approval.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
