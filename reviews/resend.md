# Review: resend

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `b2ae7b1798b70134faf679f35fc05b4331462988`
Source: `./vendor/resend` — copy of `resend/resend-skills` / `.` at `b2ae7b1798b70134faf679f35fc05b4331462988`
License: MIT

## Checklist

- [x] **License read at the pinned sha** — MIT: repository-root `LICENSE` (copied).
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 5 skill(s), 0 command(s), 0 agent(s), 1 MCP server(s), 1 script file(s).
- [x] **Capability** — network, scripts (a skill may ask to run them). Runs: 1 remote MCP server(s), added only on request: mcp.resend.com; 1 script file(s) a skill may ask to run (with your approval).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing (no hooks).
- [x] **MCP servers** — resend — `https://mcp.resend.com/mcp` (Resend's domain).
- [x] **Secrets** — `RESEND_API_KEY` by name only.
- [x] **Text read** — Manifest read; SKILL.md files and references scanned and spot-read; `fetch-all-templates.mjs` read (lists templates through the Resend SDK with `RESEND_API_KEY`).
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — Upstream had a `curl … | sh` (Tailscale install) in `agent-email-inbox/references/webhook-setup.md` — **rewritten** (see MODIFICATIONS.md). Remaining in the copy: `npm install -g resend-cli` (×3) and `@latest` in React Email scaffolding docs (×7) — acknowledged in `scripts/acknowledged.json` as Resend's own tooling (same open question as stripe: rewrite with pinned versions or keep).
- [x] **Irreversible actions** — **Sends email to real people.** Every send/broadcast needs approval; never from bots/cron without a per-campaign approval.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
