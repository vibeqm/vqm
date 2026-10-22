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
| Skills for coding agents, and the plugin for Claude Code | [`plugins/vibeqm/`](plugins/vibeqm/) |

## The VibeQM plugin for Claude Code

Four skills over `vibeqm-check`, so your agent does the practice with you:

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

The skills read your repository and change nothing until you say yes; they never
commit or push unless you ask. They are plain `SKILL.md` folders, so any agent that
reads skills can use them: copy the folders in
[`plugins/vibeqm/skills/`](plugins/vibeqm/skills/) into that agent's skills folder.

More arrives here as it is published, starting with the current setup for each
coding agent.

Assessments made with this material are self-assessments, performed by AI and owned
by the team that runs them.

MIT licensed.
