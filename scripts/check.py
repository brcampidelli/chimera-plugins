#!/usr/bin/env python3
"""Repository policy check for chimera-plugins. Standard library only; reads files, runs nothing.

What it enforces (CONTRIBUTING.md explains each rule):

1. Every marketplace entry has a pinned source: a ``./`` path inside this repository, ``github``
   with a 40-hex ``sha``, or ``archive`` with ``https://`` and a 64-hex ``sha256``. Nothing else.
2. Every entry has ``catalog/<name>.json`` and ``reviews/<name>.md``; the review names the sha it
   reviewed, and for a github entry that sha equals the marketplace sha.
3. Every folder under ``vendor/`` and ``ports/`` has ``UPSTREAM.json`` (repo, path, sha, license,
   copied_at), a license file, an SPDX id on the allowlist, and a line in ``NOTICE``.
4. Catalog files use the 26 canonical category ids from ``categories.yaml`` (shared with the
   skills and connectors catalogs), at most 3 secondary categories, and GitHub stars only
   with the date they were read.
5. Text files carry no ``curl | sh``, no unpinned ``npm -g`` / ``npx``, no ``@latest``, and no
   sentence addressed to an AI reader or reviewer ("ignore previous instructions", "note to the
   AI", ...). A finding that a human has looked at is acknowledged in ``scripts/acknowledged.json``
   with the reason; the check fails on anything else.

``--scan DIR`` runs only rule 5 over any directory (used when reviewing a github entry before its
sha goes into the marketplace). Exit status 1 on any error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LICENSE_ALLOWLIST = frozenset({
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MPL-2.0", "CC0-1.0",
})
LICENSE_FILES = ("LICENSE", "LICENSE.txt", "LICENSE.md", "COPYING")
SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")
REPO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{0,38}/[A-Za-z0-9._-]{1,100}$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
BANNED_SOURCES = ("composiohq/", "voltagent/", "clawhub")
TEXT_SUFFIXES = frozenset({
    ".md", ".mdc", ".txt", ".json", ".yaml", ".yml", ".toml", ".sh", ".bash", ".ps1", ".py",
    ".js", ".mjs", ".cjs", ".ts", ".html", ".xml", ".cfg", ".ini", "",
})
MAX_TEXT_BYTES = 2_000_000


@dataclass(frozen=True)
class Rule:
    id: str
    pattern: re.Pattern[str]
    message: str


# Supply-chain shapes. They match documentation as well as code on purpose: a skill that tells the
# agent to run `curl ... | sh` is the same risk as a script that does it.
SUPPLY_RULES = (
    Rule("curl-pipe-shell", re.compile(r"\b(?:curl|wget)\b[^\n|]*\|\s*(?:sudo\s+)?(?:ba|z)?sh\b", re.I),
         "download piped into a shell"),
    Rule("iwr-iex", re.compile(r"\b(?:iwr|invoke-webrequest|irm|invoke-restmethod)\b[^\n|]*\|\s*iex\b", re.I),
         "download piped into Invoke-Expression"),
    Rule("at-latest", re.compile(r"@latest\b"), "'@latest' is not a pinned version"),
    Rule("npm-global-unpinned",
         re.compile(r"\bnpm\s+(?:install|i)\s+(?:-g|--global)\s+(?:@[\w.-]+/)?[\w.-]+(?![\w.-]*@\d)(?=\s|$|[`'\"])", re.I),
         "global npm install without an exact version"),
)

# Sentences addressed to a model or a reviewer rather than to the person reading the docs. Skills
# legitimately speak to the agent ("You are a reviewer..."), so these target override, concealment
# and exfiltration shapes, not second-person prose.
READER_RULES = (
    Rule("override", re.compile(r"\b(?:ignore|disregard|forget)\s+(?:all\s+|any\s+)?(?:the\s+)?(?:previous|prior|above|earlier|preceding|other)\s+(?:instructions|rules|prompts?|guidelines)", re.I),
         "asks the reader to drop earlier instructions"),
    Rule("addressed-to-ai", re.compile(r"\b(?:note|message|instructions?)\s+(?:to|for)\s+(?:the\s+|any\s+)?(?:ai|llm|language model|model|assistant|agent|reviewer|scanner)s?\b", re.I),
         "text addressed to an AI or a reviewer"),
    Rule("if-you-are-ai", re.compile(r"\bif\s+you\s+are\s+(?:an?\s+)?(?:ai|llm|language model|automated|bot|agent|assistant)\b", re.I),
         "conditional addressed to an AI reader"),
    Rule("conceal", re.compile(r"\b(?:do\s+not|don't|never)\s+(?:tell|inform|mention\s+(?:this\s+)?to|reveal\s+(?:this\s+)?to|show)\s+(?:the\s+)?user\b|\bwithout\s+(?:telling|informing|asking)\s+the\s+user\b", re.I),
         "asks to hide something from the user"),
    Rule("exfiltrate", re.compile(r"\b(?:send|post|upload|exfiltrate)\s+(?:the\s+|all\s+|any\s+)?(?:contents?\s+of\s+)?(?:~/\.ssh|\.env|env(?:ironment)?\s+variables|secrets?|credentials|api\s+keys?|tokens?)\s+to\b", re.I),
         "sends secrets somewhere"),
    Rule("hidden-unicode", re.compile("[​‌‍⁠‪-‮⁦-⁩﻿]"),
         "invisible or bidirectional-formatting character"),
)


@dataclass
class Report:
    errors: list[str]
    notes: list[str]

    def error(self, message: str) -> None:
        self.errors.append(message)

    def note(self, message: str) -> None:
        self.notes.append(message)


def load_json(path: Path, report: Report) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        report.error(f"{rel(path)}: missing")
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        report.error(f"{rel(path)}: not valid JSON ({exc})")
    return None


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


# ---------------------------------------------------------------------------------------- scanning

def iter_text_files(base: Path):
    for path in sorted(base.rglob("*")):
        if path.is_symlink():
            yield path, None
            continue
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if path.stat().st_size > MAX_TEXT_BYTES:
            continue
        try:
            yield path, path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue


def scan_text(base: Path, acknowledged: dict[str, dict[str, str]], report: Report, label_root: Path) -> int:
    """Rule 5 over ``base``. Returns the number of unacknowledged findings."""
    findings = 0
    for path, text in iter_text_files(base):
        key = path.relative_to(label_root).as_posix()
        if text is None:
            report.error(f"{key}: symbolic link (not allowed in this repository)")
            findings += 1
            continue
        if key.startswith("scripts/check.py") or key == "scripts/acknowledged.json":
            continue  # the rules themselves contain the patterns
        allowed = acknowledged.get(key, {})
        # Reviews and change notices quote findings on purpose; they still may not hide characters.
        rules = (READER_RULES[-1],) if is_record(key) else (*SUPPLY_RULES, *READER_RULES)
        for rule in rules:
            for match in rule.pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                if rule.id in allowed:
                    report.note(f"{key}:{line}: {rule.id} (acknowledged: {allowed[rule.id]})")
                    continue
                snippet = match.group(0).strip().replace("\n", " ")[:80]
                report.error(f"{key}:{line}: {rule.message} [{rule.id}] -> {snippet!r}")
                findings += 1
        if path.name == ".mcp.json" or path.name == "mcp.json":
            findings += check_mcp(path, text, key, report)
    return findings


def is_record(key: str) -> bool:
    """Files that describe findings rather than instruct anyone: reviews and change notices."""
    name = key.rsplit("/", 1)[-1]
    return key.startswith("reviews/") or name in ("UPSTREAM.json", "MODIFICATIONS.md", "PORT.md")


NPX_PINNED = re.compile(r"^(?:@[\w.-]+/)?[\w.-]+@\d+\.\d+\.\d+(?:[-+][\w.]+)?$")


def check_mcp(path: Path, text: str, key: str, report: Report) -> int:
    """A local MCP server must name an exact package version; a remote one must be https."""
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        report.error(f"{key}: not valid JSON")
        return 1
    servers = data.get("mcpServers", data) if isinstance(data, dict) else {}
    bad = 0
    for name, spec in (servers.items() if isinstance(servers, dict) else []):
        if not isinstance(spec, dict):
            continue
        url = spec.get("url")
        if isinstance(url, str) and url and not url.startswith("https://"):
            report.error(f"{key}: server {name!r} url is not https")
            bad += 1
        command = spec.get("command")
        args = [a for a in spec.get("args", []) if isinstance(a, str)]
        if command in ("npx", "bunx", "pnpx", "uvx", "pipx"):
            # `npx --package=pkg@1.2.3 bin` / `npx -p pkg@1.2.3 bin` name the package explicitly;
            # otherwise the first positional argument is the package.
            explicit = [a.split("=", 1)[1] for a in args if a.startswith("--package=")]
            explicit += [args[i + 1] for i, a in enumerate(args[:-1]) if a in ("-p", "--package")]
            packages = explicit or [a for a in args if not a.startswith("-")]
            if not packages:
                report.error(f"{key}: server {name!r} runs {command} with no package")
                bad += 1
            elif command in ("npx", "bunx", "pnpx") and not NPX_PINNED.match(packages[0]):
                report.error(f"{key}: server {name!r} runs {packages[0]!r} without an exact version")
                bad += 1
            elif command in ("uvx", "pipx") and "==" not in packages[0] and "@" not in packages[0]:
                report.error(f"{key}: server {name!r} runs {packages[0]!r} without an exact version")
                bad += 1
        if command == "docker" and not any("@sha256:" in a for a in args):
            report.error(f"{key}: server {name!r} runs a docker image without a digest")
            bad += 1
    return bad


# -------------------------------------------------------------------------------------- repo rules

CATEGORY_LINE = re.compile(r"^\s*-\s*\{\s*id:\s*([a-z0-9-]+)\s*,", re.M)


def check_categories(report: Report) -> set[str]:
    """The 26 canonical ids, from categories.yaml — the same file the skills and connectors
    catalogs carry, so the app filters all three together. Parsed with a regex (stdlib only); the
    file's format is one ``- {id: x, pt: "..."}`` per line."""
    path = ROOT / "categories.yaml"
    if not path.is_file():
        report.error("categories.yaml: missing")
        return set()
    found = CATEGORY_LINE.findall(path.read_text(encoding="utf-8"))
    ids = set(found)
    if len(found) != len(ids):
        report.error("categories.yaml: duplicate id")
    if len(ids) != 26:
        report.error(f"categories.yaml: expected the 26 canonical categories, found {len(ids)}")
    return ids


def check_source(name: str, source: object, report: Report) -> tuple[str, str | None, Path | None]:
    """Returns (kind, sha, local_dir)."""
    if isinstance(source, str):
        if not source.startswith("./") or ".." in source.split("/") or "\\" in source:
            report.error(f"{name}: local source must be './path' inside the repo, got {source!r}")
            return "bad", None, None
        local = (ROOT / source[2:]).resolve()
        if not local.is_dir() or ROOT not in local.parents:
            report.error(f"{name}: local source {source!r} is not a folder in this repository")
            return "bad", None, None
        if local.parent.name not in ("plugins", "vendor", "ports") or local.parent.parent != ROOT:
            report.error(f"{name}: local source must live in plugins/, vendor/ or ports/")
        return "local", None, local
    if not isinstance(source, dict):
        report.error(f"{name}: source must be a './path' or an object")
        return "bad", None, None
    kind = source.get("source")
    if kind == "github":
        repo, sha = source.get("repo"), source.get("sha")
        if not isinstance(repo, str) or not REPO.match(repo):
            report.error(f"{name}: github source needs repo 'owner/name'")
            return "bad", None, None
        if any(repo.lower().startswith(b) or b in repo.lower() for b in BANNED_SOURCES):
            report.error(f"{name}: {repo} is on the banned-source list")
        if not isinstance(sha, str) or not SHA1.match(sha):
            report.error(f"{name}: github source needs a full 40-hex lowercase 'sha' (no branches, no tags)")
            return "bad", None, None
        if "ref" in source:
            report.error(f"{name}: drop 'ref' — the sha alone pins the tree")
        return "github", sha, None
    if kind == "archive":
        url, digest = source.get("url"), source.get("sha256")
        if not isinstance(url, str) or not url.startswith("https://"):
            report.error(f"{name}: archive needs an https:// url")
        if not isinstance(digest, str) or not SHA256.match(digest):
            report.error(f"{name}: archive needs a 64-hex sha256")
        return "archive", digest if isinstance(digest, str) else None, None
    report.error(f"{name}: source type {kind!r} is not allowed (only local, github+sha, archive+sha256)")
    return "bad", None, None


def check_upstream(folder: Path, notice: str, report: Report) -> str | None:
    """vendor/ and ports/ items. Returns the upstream sha."""
    where = rel(folder)
    data = load_json(folder / "UPSTREAM.json", report)
    if not isinstance(data, dict):
        return None
    for key in ("repo", "path", "sha", "license", "copied_at"):
        if key not in data:
            report.error(f"{where}/UPSTREAM.json: missing '{key}'")
    repo, sha, spdx = data.get("repo"), data.get("sha"), data.get("license")
    if not isinstance(repo, str) or not REPO.match(repo):
        report.error(f"{where}/UPSTREAM.json: 'repo' is owner/name")
    elif any(b in repo.lower() for b in BANNED_SOURCES):
        report.error(f"{where}/UPSTREAM.json: {repo} is on the banned-source list")
    if not isinstance(sha, str) or not SHA1.match(sha):
        report.error(f"{where}/UPSTREAM.json: 'sha' is a full 40-hex commit")
    if spdx not in LICENSE_ALLOWLIST:
        report.error(f"{where}/UPSTREAM.json: license {spdx!r} is not on the allowlist {sorted(LICENSE_ALLOWLIST)}")
    if not isinstance(data.get("copied_at"), str) or not DATE.match(data["copied_at"]):
        report.error(f"{where}/UPSTREAM.json: 'copied_at' is YYYY-MM-DD")
    if data.get("modified") and not data.get("changes"):
        report.error(f"{where}/UPSTREAM.json: modified copies list their 'changes'")
    if not any((folder / name).is_file() for name in LICENSE_FILES):
        report.error(f"{where}: no LICENSE file (the upstream license text travels with the copy)")
    if where not in notice:
        report.error(f"NOTICE: no entry for {where}")
    return sha if isinstance(sha, str) else None


def check_catalog(name: str, entry: dict, categories: set[str], report: Report) -> None:
    path = ROOT / "catalog" / f"{name}.json"
    data = load_json(path, report)
    if not isinstance(data, dict):
        return
    where = rel(path)
    if data.get("id") != name:
        report.error(f"{where}: 'id' must be {name!r}")
    primary = data.get("category")
    if primary not in categories:
        report.error(f"{where}: category {primary!r} is not one of the 26 ids")
    secondary = data.get("secondary", [])
    if not isinstance(secondary, list) or len(secondary) > 3:
        report.error(f"{where}: 'secondary' is a list of at most 3 ids")
    else:
        for item in secondary:
            if item not in categories or item == primary:
                report.error(f"{where}: secondary {item!r} is not a valid id distinct from the primary")
    if entry.get("category") != primary:
        report.error(f"{name}: marketplace category {entry.get('category')!r} differs from catalog {primary!r}")
    if not isinstance(data.get("tags", []), list):
        report.error(f"{where}: 'tags' is a list")
    if not isinstance(data.get("featured", False), bool):
        report.error(f"{where}: 'featured' is true or false")
    for banned in ("installs", "install_count", "downloads", "rating"):
        if banned in data:
            report.error(f"{where}: '{banned}' is not published — no install counts or invented numbers")
    stars = data.get("stars")
    if stars is not None:
        if not (isinstance(stars, dict) and isinstance(stars.get("count"), int)
                and isinstance(stars.get("read_at"), str) and DATE.match(stars["read_at"])
                and isinstance(stars.get("repo"), str) and REPO.match(stars["repo"])):
            report.error(f"{where}: 'stars' is {{repo, count, read_at: YYYY-MM-DD}}")
    upstream_repo = data.get("upstream")
    if upstream_repo and stars is None:
        report.error(f"{where}: an item whose upstream is a GitHub repository shows its stars with the date read")


def check_review(name: str, expected_sha: str | None, report: Report) -> None:
    path = ROOT / "reviews" / f"{name}.md"
    if not path.is_file():
        report.error(f"reviews/{name}.md: missing (every entry has a review)")
        return
    text = path.read_text(encoding="utf-8")
    for field in ("Reviewer:", "Date:", "Reviewed sha:"):
        if field not in text:
            report.error(f"reviews/{name}.md: missing '{field}'")
    match = re.search(r"Reviewed sha:\s*`?([0-9a-f]{40}|ours)`?", text)
    if not match:
        report.error(f"reviews/{name}.md: 'Reviewed sha:' is a 40-hex sha or 'ours'")
    elif expected_sha and match.group(1) != expected_sha:
        report.error(f"reviews/{name}.md: reviewed {match.group(1)[:12]} but the source is {expected_sha[:12]} — a new sha needs a new review")
    if "- [ ]" in text:
        report.error(f"reviews/{name}.md: unanswered checklist item")


def check_repo(report: Report) -> None:
    categories = check_categories(report)
    acknowledged_raw = load_json(ROOT / "scripts" / "acknowledged.json", report)
    acknowledged = acknowledged_raw if isinstance(acknowledged_raw, dict) else {}
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8") if (ROOT / "NOTICE").is_file() else ""
    if not notice:
        report.error("NOTICE: missing")
    market = load_json(ROOT / ".claude-plugin" / "marketplace.json", report)
    if not isinstance(market, dict):
        return
    entries = market.get("plugins", [])
    names: set[str] = set()
    local_dirs: set[Path] = set()
    for entry in entries if isinstance(entries, list) else []:
        name = entry.get("name") if isinstance(entry, dict) else None
        if not isinstance(name, str) or not name:
            report.error("marketplace: an entry without a name")
            continue
        if name in names:
            report.error(f"marketplace: duplicate {name}")
        names.add(name)
        if entry.get("license") not in LICENSE_ALLOWLIST:
            report.error(f"{name}: marketplace 'license' {entry.get('license')!r} is not on the allowlist")
        kind, sha, local = check_source(name, entry.get("source"), report)
        if local is not None:
            local_dirs.add(local)
            if local.parent.name in ("vendor", "ports"):
                sha = check_upstream(local, notice, report)
                upstream = load_json(local / "UPSTREAM.json", Report([], []))
                if isinstance(upstream, dict) and upstream.get("license") != entry.get("license"):
                    report.error(f"{name}: marketplace license differs from UPSTREAM.json")
            else:
                sha = None
                manifest = load_json(local / ".claude-plugin" / "plugin.json", report)
                if isinstance(manifest, dict) and manifest.get("license") != "Apache-2.0":
                    report.error(f"{name}: our own plugins are Apache-2.0")
        check_catalog(name, entry, categories, report)
        check_review(name, sha, report)
    for group in ("plugins", "vendor", "ports"):
        base = ROOT / group
        for folder in sorted(p for p in base.iterdir() if p.is_dir()) if base.is_dir() else []:
            if folder.resolve() not in local_dirs:
                report.error(f"{rel(folder)}: folder is not listed in marketplace.json")
    for orphan in sorted((ROOT / "catalog").glob("*.json")):
        if orphan.stem not in names and True:
            report.error(f"{rel(orphan)}: no marketplace entry with this name")
    for orphan in sorted((ROOT / "reviews").glob("*.md")):
        if orphan.stem not in names and orphan.stem != "TEMPLATE":
            report.error(f"{rel(orphan)}: no marketplace entry with this name")
    scan_text(ROOT, acknowledged, report, ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--scan", type=Path, help="only run the text rules over this directory")
    parser.add_argument("--quiet", action="store_true", help="do not print acknowledged findings")
    args = parser.parse_args()
    report = Report([], [])
    if args.scan:
        base = args.scan.resolve()
        scan_text(base, {}, report, base)
    else:
        check_repo(report)
    if not args.quiet:
        for note in report.notes:
            print(f"note  {note}")
    for message in report.errors:
        print(f"ERROR {message}")
    print(f"{len(report.errors)} error(s), {len(report.notes)} acknowledged finding(s)")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
