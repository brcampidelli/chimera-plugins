# What changed from the upstream copy

Upstream: https://github.com/openai/plugins at commit `0722921d5542fc593105c27bd52630babd8b8c2a`, path `plugins/posthog`.
License: MIT — the upstream license text is in this folder and still governs the copied files.

Ported from the Codex (.codex-plugin) layout to the Claude Code plugin layout by the chimera-plugins maintainers on 2026-10-17.

- added .claude-plugin/plugin.json (facts from the Codex manifest)
- added LICENSE at the plugin root: a copy of skills/posthog/LICENSE.txt (MIT, PostHog); the upstream plugin root has no license file, so our one glue file (.claude-plugin/plugin.json) is contributed under the same MIT terms; .mcp.json is the upstream file, unchanged (a server URL)
- left out .codex-plugin/, .app.json, assets/ (logos, screenshots) and skills/posthog/agents/openai.yaml (Codex-only metadata)

Every other file is byte-for-byte the upstream file (git blob sha verified when copied).
