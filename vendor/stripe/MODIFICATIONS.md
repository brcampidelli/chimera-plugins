# What changed from the upstream copy

Upstream: https://github.com/stripe/ai at commit `c1f5b0826f3f33d7e1cc7eff5e5e6cd42749808b`, path `providers/claude/plugin`.
License: MIT — the upstream license text is in this folder and still governs the copied files.

Modified by the chimera-plugins maintainers on 2026-10-17.

- skills/stripe-best-practices/SKILL.md: `npm i -g @stripe/cli` replaced by a link to https://docs.stripe.com/stripe-cli (repository rule: no unpinned global installs)
- scripts/cli.mjs: the two hook messages that suggested `npm i -g @stripe/cli` / `@stripe/cli@latest` now link to https://docs.stripe.com/stripe-cli (hooks are inert in Chimera; changed so the copy passes the same rule)

Every other file is byte-for-byte the upstream file (git blob sha verified when copied).
