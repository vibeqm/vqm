# How development is kept apart from production

**Development** is a working copy of this repository: changes are made and checked
there (`make check`, the committed hooks) before they leave the machine.

**Production** is the `main` branch on GitHub (vibeqm/vqm): every plugin install and
update (`/plugin marketplace add vibeqm/vqm`, `codex plugin marketplace add vibeqm/vqm`,
`agy plugin install https://github.com/vibeqm/vqm`) reads it directly, so a merge to
`main` goes live for everyone.

- `main` is protected by a GitHub ruleset that binds everyone, the maintainer included:
  changes arrive only as pull requests, CI must pass, and force-pushes and deletion are
  refused. Its settings are recorded in `.github/rulesets/protect-main.json`.
- A merge to `main` publishes, so the agent merges only after the person confirms in the
  session (`AGENTS.md`); pushing a release tag and `gh release` stop for the person's
  confirmation in `.claude/settings.json`.
- Every pull request and push runs the checks again on GitHub (`.github/workflows/check.yml`) and, on the
  maintainer's machine, an AI peer review by a model from another company
  (`reviews/push/`).
- Each plugin version is tagged (`v0.1.8` and later).
