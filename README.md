# The Vibe Quality Model: companion repository

The Vibe Quality Model (VibeQM) is a quality-first maturity model for software written
with AI agents: a team earns more AI autonomy by proving quality. This repository
holds the material that goes with it. Start at [vibeqm.com](https://vibeqm.com).

| What | Where |
|:--|:--|
| The specification: levels, autonomy, evidence rules, what each level requires | [`framework/VQM_SPEC.md`](framework/VQM_SPEC.md) |
| The assessor procedure an AI agent follows (also at [vibeqm.com/assessor](https://vibeqm.com/assessor)) | [`framework/ASSESSOR.md`](framework/ASSESSOR.md) |
| The documentation standard: which records, where | [`framework/DOC_STANDARD.md`](framework/DOC_STANDARD.md) |
| Templates for the records each level asks for | [`templates/`](templates/) |
| The self-assessment tool | [`vibeqm-check`](https://www.npmjs.com/package/vibeqm-check): run `npx vibeqm-check` in your repository |
| The plugin for Claude Code, Codex and GitHub Copilot CLI (four skills any agent can read) | [`plugins/vibeqm/`](plugins/vibeqm/) |

## The VibeQM plugin for Claude Code, Codex and GitHub Copilot CLI

Four skills over `vibeqm-check`, so your agent does the practice with you (in Codex the names are `$assess`, `$init`, `$fix-gates` and `$judgment`):

| Skill | What it does |
|:--|:--|
| `/vibeqm:assess` | Runs the checks and explains the level, the open gates and what closes them |
| `/vibeqm:init` | Shows the Level 2 template files, creates them after you say yes, and fills their blanks from your repository |
| `/vibeqm:fix-gates` | Closes the next level's open gates one at a time, asking before each change |
| `/vibeqm:judgment` | Answers the assessor's judgment questions: is the evidence real practice or only paperwork? |

Install it in Claude Code:

```
/plugin marketplace add vibeqm/vqm
/plugin install vibeqm@vibeqm
```

(On Claude Code 2.1.275 or later, one line does both:
`/plugin install vibeqm --marketplace vibeqm/vqm`.)

Install it in Codex (CLI 0.147 or later; the same plugin folder carries a portable
[Agent Plugins](https://agent-plugins.org) manifest and a Codex catalog):

```
codex plugin marketplace add vibeqm/vqm
codex plugin add vibeqm@vibeqm
```

Install it in GitHub Copilot CLI:

```
copilot plugin marketplace add vibeqm/vqm
copilot plugin install vibeqm@vibeqm
```

None of these installs needs a directory listing or an account with us: each command
reads this repository.

### Other agents

The skills are plain `SKILL.md` folders. Copy the four folders in
[`plugins/vibeqm/skills/`](plugins/vibeqm/skills/) into the folder your agent reads:

| Agent | Folder in your repository |
|:--|:--|
| OpenCode, Qwen Code, Pi, Oh My Pi, DeepSeek Harness (and Codex, Copilot CLI) | `.agents/skills/` |
| OpenClaw | `.agents/skills/` in its workspace (`agents.defaults.workspace`) |
| Cline | `.cline/skills/` |
| Claude Code without the plugin | `.claude/skills/` |

Tested on 2026-11-03 in OpenCode, Qwen Code, Pi, Oh My Pi, DeepSeek Harness, Cline and
Copilot CLI (each listed the four skills and read the command the assess skill runs) and
OpenClaw (`openclaw skills list` shows the four as ready). Any other agent that can run a shell command can use the tool
directly: `npx vibeqm-check`.

The skills read your repository and change nothing until you say yes; they never
commit or push unless you ask.

**What leaves your machine.** Nothing goes to us: no account, no telemetry, no server
of ours. Two outside calls are made on your side: `npx` downloads `vibeqm-check` from
the npm registry, and, if the GitHub CLI (`gh`) is logged in, `vibeqm-check` asks
GitHub, read-only and with your own login, for the repository's CI runs and merged
pull requests (`--offline` turns that off). The checks read your git history,
including commit authors' names and emails, on your machine. See
[`PRIVACY.md`](PRIVACY.md). 

More arrives here as it is published, starting with the current setup for each
coding agent.

Assessments made with this material are self-assessments, performed by AI and owned
by the team that runs them.

MIT licensed.
