# What changed from the upstream copy

Upstream: https://github.com/cursor/plugins at commit `1b800800583ee8ff7f2676caf7a5cb7f0804be85`, path `thermos`.
License: MIT — the upstream license text is in this folder and still governs the copied files.

Ported from the Cursor (.cursor-plugin) layout to the Claude Code plugin layout by the chimera-plugins maintainers on 2026-10-17.

- added .claude-plugin/plugin.json (facts from the Cursor manifest; dropped Cursor-only 'logo', 'category', 'tags')
- left out .cursor-plugin/ and assets/logo.png
- skills/ and agents/ copied byte for byte; their text names Cursor's subagent types ('shell', 'explore') — in Chimera/Claude Code use the equivalent built-in agents

Every other file is byte-for-byte the upstream file (git blob sha verified when copied).
