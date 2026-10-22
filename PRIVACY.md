# Privacy: the VibeQM plugin and vibeqm-check

The VibeQM plugin (`plugins/vibeqm/`) and the tool it runs, `vibeqm-check`, collect
nothing about you or your code.

- **Nothing is sent to us.** There is no account, no telemetry and no server of ours.
  The checks run on your machine and the results stay there.
- **The skills read your repository through your own coding agent.** What your agent
  reads is handled by that agent's provider under its own terms (for Claude Code,
  Anthropic's); the plugin adds no other destination.
- **One optional outside call, with your login.** If the GitHub CLI (`gh`) is logged
  in, `vibeqm-check` asks GitHub, read-only and with your own login, for the
  repository's CI runs and merged pull requests. Pass `--offline` to turn it off.
- **Nothing changes without your yes.** The skills write files only after you agree,
  and never commit or push unless you ask.
- **Installing it.** The skills run `npx vibeqm-check`, which downloads the package
  from the npm registry; npm's own terms apply to that download.

Questions: open an issue at https://github.com/vibeqm/vqm/issues.
