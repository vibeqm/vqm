#!/usr/bin/env python3
"""The checks `make check` runs on this repository (VibeQM Level 2).

- every JSON manifest parses;
- the plugin's version is the same in its three manifests and the Claude Code catalog;
- the four skills pin the same vibeqm-check version, and each has a name and description;
Exit 1 with one line per problem.
"""
import json, re, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
problems = []

manifests = [
    ".claude-plugin/marketplace.json",
    ".agents/plugins/marketplace.json",
    "plugins/vibeqm/plugin.json",
    "plugins/vibeqm/.claude-plugin/plugin.json",
    "plugins/vibeqm/.codex-plugin/plugin.json",
]
data = {}
for m in manifests:
    try:
        data[m] = json.loads((root / m).read_text())
    except Exception as e:  # noqa: BLE001 — any failure is a problem to report
        problems.append(f"{m}: not valid JSON ({e})")

versions = {m: data[m].get("version") for m in manifests[2:] if m in data}
cat = data.get(".claude-plugin/marketplace.json", {})
entry = next((p for p in cat.get("plugins", []) if p.get("name") == "vibeqm"), None)
if entry is None:
    problems.append(".claude-plugin/marketplace.json: no vibeqm plugin entry")
else:
    versions[".claude-plugin/marketplace.json"] = entry.get("version")
for m, v in versions.items():
    if not isinstance(v, str) or not v.strip():
        problems.append(f"{m}: no version")
if len(set(versions.values())) > 1:
    problems.append(f"plugin versions differ: {versions}")

pins = {}
for skill in sorted((root / "plugins/vibeqm/skills").glob("*/SKILL.md")):
    text = skill.read_text()
    rel = skill.relative_to(root)
    front = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not front or not re.search(r"^name:\s*\S", front.group(1), re.M) or not re.search(r"^description:\s*\S", front.group(1), re.M):
        problems.append(f"{rel}: front matter needs name and description")
    found = set(re.findall(r"vibeqm-check@(\d+\.\d+\.\d+)", text))
    if not found:
        problems.append(f"{rel}: no vibeqm-check@<version> pin")
    pins[str(rel)] = found
allpins = set().union(*pins.values()) if pins else set()
if len(allpins) > 1:
    problems.append(f"skills pin different vibeqm-check versions: {sorted(allpins)}")
if len(pins) != 4:
    problems.append(f"expected 4 skills, found {len(pins)}")

for problem in problems:
    print(f"✗ {problem}")
if problems:
    sys.exit(1)
print(f"✓ manifests valid, plugin {next(iter(set(versions.values())), '?')}, skills pinned to vibeqm-check@{next(iter(allpins), '?')}")
