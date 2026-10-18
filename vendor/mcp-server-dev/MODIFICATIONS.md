# What changed from the upstream copy

Upstream: https://github.com/anthropics/claude-plugins-official at commit `ea10b213686c90bb1984b2016937310e05336cf3`, path `plugins/mcp-server-dev`.
License: Apache-2.0 — the upstream license text is in this folder and still governs the copied files.

Modified by the chimera-plugins maintainers on 2026-10-17.

- skills/build-mcp-server/references/deploy-cloudflare-workers.md: `npm create cloudflare@latest` replaced by `npm create cloudflare@<version>` with a link to Cloudflare's C3 page (repository rule: no unpinned installs)

Every other file is byte-for-byte the upstream file (git blob sha verified when copied).
