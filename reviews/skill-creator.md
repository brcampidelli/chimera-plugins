# Review: skill-creator

Reviewer: Claude Opus 5.5 (agent), preparing for Bruno Campidelli — human sign-off pending before publication
Date: 2026-10-17
Reviewed sha: `ea10b213686c90bb1984b2016937310e05336cf3`
Source: `./vendor/skill-creator` — copy of `anthropics/claude-plugins-official` / `plugins/skill-creator` at `ea10b213686c90bb1984b2016937310e05336cf3`
License: Apache-2.0

## Checklist

- [x] **License read at the pinned sha** — Apache-2.0: plugin `LICENSE` and `skills/skill-creator/LICENSE.txt` (Apache-2.0).
- [x] **Validated** — `chimera plugin validate` from Chimera `main` @ `ae5eef5a` (0.69.0 is not on PyPI yet; 0.68.1 has no `plugin` command): valid. Components: 1 skill(s), 0 command(s), 0 agent(s), 0 MCP server(s), 10 script file(s).
- [x] **Capability** — scripts (a skill may ask to run them). Runs: 10 script file(s) a skill may ask to run (with your approval).
- [x] **Hooks / bin** — what is lost because Chimera never runs them: nothing (no hooks).
- [x] **MCP servers** — none.
- [x] **Secrets** — none.
- [x] **Text read** — Manifest read; SKILL.md, the 3 agent prompts and references scanned and spot-read; the Python scripts grepped for network, subprocess and file-system use: `run_eval.py` and `improve_description.py` spawn the `claude` CLI (`claude -p`) to run evals, `eval-viewer/generate_review.py` serves a local HTML page; no network calls to third parties found. `viewer.html` loads fonts from Google Fonts and SheetJS from its CDN when opened.
- [x] **Supply chain and reader-directed text** (`scripts/check.py` rules) — clean.
- [x] **Irreversible actions** — The skill may ask the agent to run its Python scripts (eval runs cost model tokens). Chimera asks before running them.

## Re-review

A new sha (or any change to the files above) needs a new review: update `Reviewed sha`, re-run
`python scripts/check.py` (or `--scan <checkout>` for a github entry) and `chimera plugin validate`.
