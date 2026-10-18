# Review: posthog

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `0722921d5542fc593105c27bd52630babd8b8c2a`
Source: `./ports/posthog` — port of `openai/plugins` / `plugins/posthog` at `0722921d5542fc593105c27bd52630babd8b8c2a`
License: MIT

## Checklist

- [x] **License read at the pinned sha** — MIT: `skills/posthog/LICENSE.txt` (Copyright PostHog, Inc.). The plugin root upstream has no license file — see PORT.md for how the glue file is licensed.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 1 skill(s), 0 command(s), 0 agent(s), 1 MCP server(s), 0 script file(s).
- [x] **Capability** — network. Runs: 1 remote MCP server(s), added only on request: mcp.posthog.com.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing.
- [x] **MCP servers** — posthog — `https://mcp.posthog.com/mcp` (PostHog's domain).
- [x] **Secrets** — none.
- [x] **Text read** — `.mcp.json` and LICENSE read; SKILL.md scanned and spot-read.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — The server can toggle feature flags and edit experiments — writes need approval.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
