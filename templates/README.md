# Templates

Starting points for the records the Vibe Quality Model asks for. Each one is
small: copy it, fill it from your repository as it is, and let your agent keep it
current. Every `<...>` is a placeholder. A copied template that still has its
placeholders is not evidence of anything.

## Level 2 (Guarded)

Copy the contents of `level-2/` into the root of your repository, then fill the
placeholders. The table says what each file is for and the check that keeps it
honest. The gate names are the ones `vqm-check` reports.

| File | Gate it serves | The check that keeps it honest |
|:--|:--|:--|
| `AGENTS.md` | Agent rules file; Development apart from production | Under 100 lines; every section says something true of this repository; the build command really is the one that runs |
| `.claude/settings.json` | Agent permissions; Development apart from production | The agent can't force-push, skip the checks, delete outside the project or read secrets, and publish commands stop for a person. Other tools: see their own permission settings |
| `.github/workflows/checks.yml` | Checks before merge; Verification on every change; Security review before push | Your build, tests and linter run in the `verify` job (it checks nothing until you uncomment or write them), and both jobs are required checks on the main branch |
| `.github/dependabot.yml` | Security review before push | One entry per package manager the project uses |
| `.github/ISSUE_TEMPLATE/change-request.md` | Requirements first | Every change traces to a request with acceptance criteria |
| `.github/pull_request_template.md` | Peer review on every change; Owner per change | Every pull request names its requirement, owner, risk class and reviewer |
| `.gitignore` | Configuration basics | `.env` files never reach the repository |
| `VibeQM/README.md` | The index | Every row points to a file that exists |
| `VibeQM/requirements/REQUIREMENTS.md` | Requirements first | Every requirement has acceptance criteria and a way to verify it; clarifying questions and their answers are recorded |
| `VibeQM/decisions/DECISIONS.md` | Decision log (light) | Every decision is dated and names who decided |
| `VibeQM/plan/PROJECT_PLAN.md` | Plan (light) | Every milestone says what evidence closes it |
| `VibeQM/tailoring/TAILORING.md` | Version control + merge path (the solo-work exception) | Every change to the standard has a reason and an approver |
| `vqm-proof.json` | Proof for what `vqm-check` can't see | Each entry is vouched for by a named person, and expires after a year |

## What files can't do

Level 2 also needs a few things no template can supply:

- **Branch protection.** On the code host, make the `checks.yml` jobs required on
  the main branch, so a failing check blocks the merge. A solo project may push to
  the main branch instead, with a blocking pre-push hook and a tailoring record.
- **A release tag**, pushed to the host (for example `v0.1.0`).
- **Peer review of every push or pull request**, by a person or by an AI model
  from a different company than the one that wrote the change. A pull request
  review on the host counts. So does a push-review record: a file under
  `reviews/push/` whose first line is `<!-- push review · <from>..<to> -->`, with a
  line naming the model, ending `VERDICT: PASS`. Review counts once 20 changes have
  followed the first reviewed one.
- **A check seen to fail.** Plant a fault (a failing test, a lint error) and watch
  the check refuse it, then fix it. A failed-then-passed run on the main branch is
  found automatically; otherwise record it in `vqm-proof.json`.
- **Small changes**: a median of 400 changed lines or fewer per commit on the main
  branch.

Run `npx vqm-check` in your repository to see which gates are open and what each
one needs.
