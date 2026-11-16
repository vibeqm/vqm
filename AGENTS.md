# AGENTS.md — vqm

Notes for AI coding agents (and people) working on this repository: the public
companion to the Vibe Quality Model (VibeQM): the framework, the Level 2 templates and
the VibeQM plugin.

- `framework/` is written by the maintainer's export script from the model's working
  copies (a new framework version arrives as one export commit); never edit those files
  by hand. Changes to the model go through an issue ("model feedback").
- The four skills in `plugins/vibeqm/skills/` pin one `vibeqm-check@<version>`; when the
  pin or a skill changes, bump `version` in the three plugin manifests and in
  `.claude-plugin/marketplace.json` together, and record the pin in `package.json`
  (then `npm install --package-lock-only`), so the dependency scan covers it
  (`make check` refuses a mismatch).
- Templates in `templates/level-2/` are starter files with blanks; vibeqm-check bundles a
  copy, so a template change is made here first and then synced there.
- Wording: "assessment" and "self-assessed", never "appraisal", "certified" or
  "certification"; the short name is "VibeQM".
- Build and check: `make check` (the repository checks, then markdownlint). Enable the
  committed hooks once per clone: `git config core.hooksPath .githooks`.
- Workflow (the same as `CONTRIBUTING.md`): `main` is protected for everyone, the
  maintainer included, so never push to it. Work on a branch named for the change, run
  `make check`, push the branch, and open a pull request with `gh pr create` using the
  template (what, why, how tested). Wait for CI (`check`, `security`,
  `self-assessment`) to pass and every review thread to be resolved; merge with a merge
  commit (`gh pr merge --merge --delete-branch`) only after the person confirms in the
  session. Tag a release on `main` after the merge, never before. The ruleset lives on
  GitHub; its settings are recorded in `.github/rulesets/protect-main.json` (update the
  file when the ruleset changes).
  On the maintainer's machine every push is peer reviewed by a model from another company
  and leaves a record in `reviews/push/`: commit that record to the same branch and push
  again (a push that only adds review records is not reviewed again) before opening or
  merging the pull request. Fetch `origin` first, so a new branch is compared with the
  current `main`.
- Development and production: see `docs/DEV_AND_PRODUCTION.md`. Merging to `main`
  publishes to everyone who installs the plugin, so the agent merges a pull request or
  pushes a release tag only after the person confirms in the session.
- Keep this file under 200 lines.
