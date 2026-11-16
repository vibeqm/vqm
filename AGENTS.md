# AGENTS.md — vqm

Notes for AI coding agents (and people) working on this repository: the public
companion to the Vibe Quality Model (VibeQM): the framework, the Level 2 templates and
the VibeQM plugin.

- `framework/` is written by the maintainer's export script from the model's working
  copies (a new framework version arrives as one export commit); never edit those files
  by hand. Changes to the model go through an issue ("model feedback").
- The four skills in `plugins/vibeqm/skills/` pin one `vibeqm-check@<version>`; when the
  pin or a skill changes, bump `version` in the three plugin manifests and in
  `.claude-plugin/marketplace.json` together (`make check` refuses a mismatch).
- Templates in `templates/level-2/` are starter files with blanks; vibeqm-check bundles a
  copy, so a template change is made here first and then synced there.
- Wording: "assessment" and "self-assessed", never "appraisal", "certified" or
  "certification"; the short name is "VibeQM".
- Build and check: `make check` (the repository checks, then markdownlint). Enable the
  committed hooks once per clone: `git config core.hooksPath .githooks`.
- `main` is protected for everyone, the maintainer included: every change arrives as a
  pull request from a branch, and merges after CI passes (no force-push, no deletion).
- Development and production: see `docs/DEV_AND_PRODUCTION.md`. Merging to `main`
  publishes to everyone who installs the plugin, so the agent merges a pull request or
  pushes a release tag only after the person confirms in the session.
- Keep this file under 200 lines.
