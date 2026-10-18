# Review: playwright

Reviewer: Claude Opus 5.5 (AI agent) — not a human review
Human sign-off: pending (no maintainer has signed this review yet)
Date: 2026-10-17
Reviewed sha: `ours`
Source: `./plugins/playwright` — written for this repository
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0 (ours). Package `@playwright/mcp` is Apache-2.0 (microsoft/playwright-mcp, 38,289 stars on 2026-10-17).
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 0 skill(s), 0 command(s), 0 agent(s), 1 MCP server(s), 0 script file(s).
- [x] **Capability** — starts process. Runs: 1 local MCP server(s) via npx, added only on request.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing.
- [x] **MCP servers** — local — `npx -y @playwright/mcp@0.0.83 --isolated` (version published 2026-09-28, ≥2 weeks old when pinned).
- [x] **Secrets** — none.
- [x] **Text read** — Everything.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean (README mention of '@latest' acknowledged).
- [x] **Irreversible actions** — The browser can submit forms on real sites; approvals apply.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
