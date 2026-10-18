# What changed from the upstream copy

Upstream: https://github.com/openai/plugins at commit `0722921d5542fc593105c27bd52630babd8b8c2a`, path `plugins/supabase`.
License: MIT — the upstream license text is in this folder and still governs the copied files.

Ported from the Codex (.codex-plugin) layout to the Claude Code plugin layout by the chimera-plugins maintainers on 2026-10-17.

- added .claude-plugin/plugin.json (written from the Codex manifest's facts: name, author, links, license)
- left out .codex-plugin/plugin.json and .app.json (a ChatGPT app id, not portable)
- left out assets/ (Supabase logos — trademarks)
- skills/, .mcp.json, LICENSE, README.md, CHANGELOG.md copied byte for byte

Every other file is byte-for-byte the upstream file (git blob sha verified when copied).
