# Review: sentry

Reviewer: Claude Opus 5.5 (AI agent) — not a human review
Human sign-off: pending (no maintainer has signed this review yet)
Date: 2026-10-17
Reviewed sha: `0d42f6a5b013580110ea55c00f699782c03a99b0`
Source: github `getsentry/plugin-claude` at `0d42f6a5b013580110ea55c00f699782c03a99b0` (not copied here)
License: MIT

## Checklist

- [x] **License read at the pinned sha** — MIT: root `LICENSE` (Copyright 2025 Sentry).
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 8 skill(s), 0 command(s), 0 agent(s), 1 MCP server(s), 0 script file(s).
- [x] **Capability** — network. Runs: 1 remote MCP server(s), added only on request: mcp.sentry.dev.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing (no hooks).
- [x] **MCP servers** — sentry — `https://mcp.sentry.dev/mcp?utm_source=plugin` (Sentry's domain; the query string is a referral tag).
- [x] **Secrets** — none in files.
- [x] **Text read** — Manifest (MCP server declared inline) read in full; the 8 SKILL.md and references scanned and spot-read.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — Not scanned by this repo's CI (the source is a pinned commit in another repository). Findings at the pinned sha (`scripts/check.py --scan` on a checkout): 19: 15× `@latest` in setup docs for Sentry's own wizard/CLI (`@sentry/wizard@latest`, `@sentry/cli@latest`), 4× 'conceal' — false positives (`Do not tell the user to "go check your dashboard"`). No `curl | sh`.
- [x] **Irreversible actions** — Resolving or assigning issues is a write; approval applies.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
