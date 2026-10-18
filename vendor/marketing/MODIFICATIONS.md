# What changed from the upstream copy

Upstream: https://github.com/anthropics/knowledge-work-plugins at commit `33eeda1e8fd856455b05479d13a0f85b5f803744`, path `marketing`.
License: Apache-2.0 — the upstream license text is in this folder and still governs the copied files.

Modified by the chimera-plugins maintainers on 2026-10-17.

- .mcp.json: removed servers whose 'url' is an empty string (Chimera and Claude Code refuse a server with neither command nor url)
- .mcp.json: removed 'slack' — its entry carries Anthropic's registered OAuth client id, which is not ours to reuse
- .mcp.json: removed servers whose endpoint path is specific to Anthropic ('/anthropic'), not verified for other clients
- CONNECTORS.md and skills still mention the removed connectors; they are documentation, unchanged

Every other file is byte-for-byte the upstream file (git blob sha verified when copied).
