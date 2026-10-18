# Review: whatsapp-cloud

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `ours`
Source: `./plugins/whatsapp-cloud` — written for this repository
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0 (ours). Written from the author's knowledge of Meta's public WhatsApp Cloud API documentation; no third-party text was copied or paraphrased from a restricted source.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 4 skill(s), 1 command(s), 0 agent(s), 0 MCP server(s), 0 script file(s).
- [x] **Capability** — instructions only. Runs: instructions only (skills/commands/agents in Markdown).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing (no hooks).
- [x] **MCP servers** — none (Meta publishes no official MCP server for WhatsApp).
- [x] **Secrets** — Tells the agent to keep the System User token and app secret in a secret store.
- [x] **Text read** — Everything (written for this repository).
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — Instructions say an agent asks before sending and never sends from an unattended job without a per-campaign approval; the command is read-only.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
