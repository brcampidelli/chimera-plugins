# Review: supabase

Reviewer: Claude Opus 5.5 (AI agent) — not a human review
Human sign-off: pending (no maintainer has signed this review yet)
Date: 2026-10-17
Reviewed sha: `0722921d5542fc593105c27bd52630babd8b8c2a`
Source: `./ports/supabase` — port of `openai/plugins` / `plugins/supabase` at `0722921d5542fc593105c27bd52630babd8b8c2a`
License: MIT

## Checklist

- [x] **License read at the pinned sha** — MIT: `LICENSE` in the upstream plugin folder (Copyright 2025 Supabase). openai/plugins has no root license; this folder's own LICENSE file is what makes the copy possible.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 2 skill(s), 0 command(s), 0 agent(s), 1 MCP server(s), 0 script file(s).
- [x] **Capability** — network. Runs: 1 remote MCP server(s), added only on request: mcp.supabase.com.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing (no hooks).
- [x] **MCP servers** — supabase — `https://mcp.supabase.com/mcp` (Supabase's domain, OAuth).
- [x] **Secrets** — none in files.
- [x] **Text read** — Codex manifest and `.mcp.json` read in full; both SKILL.md, README and CHANGELOGs scanned and spot-read; the 38 Postgres best-practice references scanned and spot-read (RLS, indexes, pooling).
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — **The MCP server runs SQL and migrations on your projects.** Writes need approval; use the server's read-only / project-scoped options for production.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
