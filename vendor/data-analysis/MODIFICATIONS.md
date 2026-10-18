# What changed from the upstream copy

Upstream: https://github.com/anthropics/knowledge-work-plugins at commit `33eeda1e8fd856455b05479d13a0f85b5f803744`, path `data`.
License: Apache-2.0 — the upstream license text is in this folder and still governs the copied files.

Modified by the chimera-plugins maintainers on 2026-10-17.

- .mcp.json: removed servers whose 'url' is an empty string (Chimera and Claude Code refuse a server with neither command nor url)
- .claude-plugin/plugin.json: name 'data' renamed to 'data-analysis' (the generic name collides with Anthropic's own 'data' plugin when both marketplaces are added); folder renamed to match

Every other file is byte-for-byte the upstream file (git blob sha verified when copied).
