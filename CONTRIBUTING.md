# Contributing to the Vibe Quality Model

Thank you for helping. The Vibe Quality Model (VibeQM) gets better when people run it
on real repositories and tell us where it is wrong. You can help without writing any
code.

## The most useful thing you can do

Run the assessment on a repository you know well, then tell us whether the result was
fair:

```text
npx vibeqm-check
```

or, with the plugin installed, say *assess this repository with VibeQM*. If the level
is lower than your practice deserves, or higher, open a
[model feedback issue](https://github.com/vibeqm/vqm/issues/new?template=model-feedback.yml).
"This gate is wrong because…" is a welcome issue.

## Where each kind of change goes

| You want to change | How |
|:--|:--|
| **The model**: a level, a gate, a rule in `framework/` | Open an issue. The files in `framework/` are generated from the model's working copy at each release, so a pull request that edits them would be overwritten. A change the author accepts is recorded with its reason and ships in the next version, with credit in the issue. |
| **The templates** in `templates/` | Pull requests welcome. |
| **The skills** in `plugins/vibeqm/skills/` | Pull requests welcome. Keep the texts agent-neutral: they are shared by Claude Code, Codex, Copilot CLI and the other agents. |
| **Support for another agent** (where it reads skills, how to install) | Open an [agent support report](https://github.com/vibeqm/vqm/issues/new?template=agent-support.yml) with what you tested, or a pull request to the README's agent table. |
| **The self-assessment tool** (`vibeqm-check`) | Its own repository: [vibeqm/vibeqm-check](https://github.com/vibeqm/vibeqm-check/issues). |
| A question or an idea that isn't a change yet | [Discussions](https://github.com/vibeqm/vqm/discussions). |

## Pull requests

- One change per pull request, with a line saying why.
- Test a template change the way the project does: copy the templates into a fresh
  repository and run `npx vibeqm-check`. It must pass only what the files really
  provide. Say in the pull request what you ran and what it reported.
- Test a skill change by running the skill in at least one agent, and name the agent
  and its version.
- Don't paste text from other maturity models or standards. VibeQM uses no text from
  any other model.
- Describe a VibeQM assessment as what it is: a self-assessment performed by AI. No
  official body stands behind a level, so keep wording that suggests one out of the
  text.

## Starter issues

Issues labelled [good first issue](https://github.com/vibeqm/vqm/labels/good%20first%20issue)
need no knowledge of the codebase. Issues labelled
[help wanted](https://github.com/vibeqm/vqm/labels/help%20wanted) are bigger.

## License

By contributing you agree that your contribution is licensed under the
[MIT License](LICENSE), like the rest of this repository.
