# Review: pr-review-toolkit

Reviewer: Claude Opus 5.5 (AI agent) — not a human review
Human sign-off: pending (no maintainer has signed this review yet)
Date: 2026-10-17
Reviewed sha: `ea10b213686c90bb1984b2016937310e05336cf3`
Source: `./vendor/pr-review-toolkit` — copy of `anthropics/claude-plugins-official` / `plugins/pr-review-toolkit` at `ea10b213686c90bb1984b2016937310e05336cf3`
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: `LICENSE` in the upstream plugin folder.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 0 skill(s), 1 command(s), 6 agent(s), 0 MCP server(s), 0 script file(s).
- [x] **Capability** — instructions only. Runs: instructions only (skills/commands/agents in Markdown).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing (no hooks).
- [x] **MCP servers** — none.
- [x] **Secrets** — none.
- [x] **Text read** — Manifest and README read; the 6 agent prompts and the command scanned and spot-read.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — 1 finding, acknowledged: `agents/silent-failure-hunter.md` matches the 'conceal' pattern — false positive (it lists 'without informing the user' as a bug to look for).
- [x] **Irreversible actions** — read-only review; no irreversible action.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
