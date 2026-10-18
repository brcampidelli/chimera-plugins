# Review: twilio-developer-kit

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `8aba46fb65dc8d9a20f4b301a68352064b4159a5`
Source: github `twilio/ai` at `8aba46fb65dc8d9a20f4b301a68352064b4159a5` (not copied here)
License: MIT

## Checklist

- [x] **License read at the pinned sha** — MIT: root `LICENSE` (Copyright 2026 Twilio).
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 57 skill(s), 0 command(s), 0 agent(s), 1 MCP server(s), 0 script file(s).
- [x] **Capability** — network. Runs: 1 remote MCP server(s), added only on request: mcp.twilio.com.
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing (no hooks).
- [x] **MCP servers** — twilio-docs — `https://mcp.twilio.com/docs` (Twilio's domain, documentation search only).
- [x] **Secrets** — Skills reference `TWILIO_ACCOUNT_SID` / `TWILIO_AUTH_TOKEN` by name only.
- [x] **Text read** — Manifest and `mcp.json` read; the 57 skills (twilio/ and sendgrid/) scanned and spot-read (WhatsApp senders, messaging, verify).
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — 4 findings: `npm install -g twilio-cli` / `ngrok` without version, `@latest` in the CLI reference. No `curl | sh`, no reader-directed text.
- [x] **Irreversible actions** — **Sends SMS/WhatsApp/calls that cost money and reach real people** when the agent runs the CLI or SDK; approval applies; never from bots/cron.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
