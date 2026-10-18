# What changed from the upstream copy

Upstream: https://github.com/resend/resend-skills at commit `b2ae7b1798b70134faf679f35fc05b4331462988`, path `.`.
License: MIT — the upstream license text is in this folder and still governs the copied files.

Modified by the chimera-plugins maintainers on 2026-10-17.

- skills/agent-email-inbox/references/webhook-setup.md: replaced a `curl … | sh` Tailscale install line with a pointer to Tailscale's official download page (repository rule: no download piped into a shell)

Only the Claude Code plugin is copied: .claude-plugin/plugin.json, skills/, README.md, LICENSE. Left out: other harnesses' manifests (.cursor-plugin, .grok-plugin, root plugin.json/mcp.json), the repo's marketplace.json, CI workflows, skill-evals, AGENTS.md, CLAUDE.md (a symlink upstream) and the logo (a trademark).

Every other file is byte-for-byte the upstream file (git blob sha verified when copied).
