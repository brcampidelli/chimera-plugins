# Review: mercadopago

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `9815b7fe3769783ddafce0745d113351c8e69ab0`
Source: `./vendor/mercadopago` — copy of `mercadopago/mercadopago-claude-marketplace` / `plugins/mercadopago` at `9815b7fe3769783ddafce0745d113351c8e69ab0`
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: repository-root `LICENSE` and `NOTICE` (copied into the vendor folder); manifest says Apache-2.0.
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 4 skill(s), 4 command(s), 1 agent(s), 1 MCP server(s), hooks, 27 script file(s).
- [x] **Capability** — hooks (inert in Chimera), network, scripts (a skill may ask to run them). Runs: 1 remote MCP server(s), added only on request: mcp.mercadopago.com; hooks present — never run by Chimera; 27 script file(s) a skill may ask to run (with your approval).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: the credential-leak guard hook and the version notice never run in Chimera. Chimera's own secret scanning covers part of the guard.
- [x] **MCP servers** — mcp — `https://mcp.mercadopago.com/mcp` (Mercado Pago's domain) with two static headers (plugin version, invocation context); no secret in headers.
- [x] **Secrets** — none in files; the hook that would block credential leaks is inert, so the review skill's advice (never commit `APP_USR-` tokens) is what remains.
- [x] **Text read** — Manifest, `.mcp.json`, `hooks/hooks.json` and `hooks/check-version.sh` read in full; agent, commands and SKILL.md files scanned and spot-read; `validate_mp_credentials.py` header read (a PreToolUse guard that blocks writing live Mercado Pago credentials into files — inert in Chimera). The 27 `.mjs` validator/test scripts scanned and spot-read: local static checks of the user's integration; `api.qrserver.com` appears only as a forbidden pattern and in a negative test fixture.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — 1 finding, acknowledged: `npm install mercadopago@latest` in `mp-integrate/SKILL.md`, inside a step that requires explicit authorisation and an exact stable version.
- [x] **Irreversible actions** — **Money.** Test users and test cards are safe; anything on a production account needs approval. Never from bots/cron.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
