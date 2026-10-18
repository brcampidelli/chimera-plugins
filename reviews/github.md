# Review: github

Reviewer: Claude Opus 5.5 (AI agent) — not a human review
Human sign-off: pending (no maintainer has signed this review yet)
Date: 2026-10-17
Reviewed sha: `ours`
Source: `./plugins/github` — written for this repository
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0 (ours). The server is github/github-mcp-server (MIT, 33,702 stars on 2026-10-17); its endpoints are facts from its public docs.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 0 skill(s), 0 command(s), 0 agent(s), 2 MCP server(s), 0 script file(s).
- [x] **Capability** — network. Runs: 2 remote MCP server(s), added only on request: api.githubcopilot.com.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing.
- [x] **MCP servers** — github-readonly — `https://api.githubcopilot.com/mcp/readonly`; github — `https://api.githubcopilot.com/mcp/` (GitHub's domain, per the github-mcp-server README).
- [x] **Secrets** — `${user_config.github_token}` (sensitive) → `Authorization: Bearer` header to api.githubcopilot.com only.
- [x] **Text read** — Everything.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — The read-write server can open/close issues, comment and edit; add it only when needed; approvals apply.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
