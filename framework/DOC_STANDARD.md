# VibeQM documentation standard v0.4.3

Version 0.4.3, 2026-10-17. Part of the Vibe Quality Model: [vibeqm.com](https://vibeqm.com).

It answers: **which documents does a project keep,
where, in what shape, and how much of it can a project drop?** Process maturity
needs written process, in the same way the established maturity models ask organizations for
defined, documented processes. VibeQM keeps that need, and makes the documents small, versioned
with the code, and readable by AI agents as well as people.

## 1. Principles

1. **One home.** Project documentation lives in a single `VibeQM/` directory at the
   repo root. Nothing loose at the root except files the tools require
   (`README.md`, agent rules files such as `CLAUDE.md`/`AGENTS.md`, build files).
2. **Agents read it.** `VibeQM/README.md` is the index; agent rules files point
   to it so an agent knows where to read requirements and where to write decisions.
3. **One fact, one place.** Link, don't copy.
4. **Stable IDs.** `REQ-`, `DEC-`, `RSK-`, `IDEA-`, `TLR-` (tailoring) numbers are
   never reused or renumbered.
5. **Dated and attributed.** Every decision says who decided and when.
6. **Evidence over prose.** A document earns its place by being checked: a
   requirement has a verification method, a risk has a trigger, a gate has a
   record.
7. **Tailor, don't skip silently.** Any part of this standard can be dropped or
   changed, but the change is written down (§4).

## 2. Standard layout

```
VibeQM/
  README.md            index; what lives where; agents read first
  plan/                PROJECT_PLAN.md: scope, deliverables, schedule, milestones
  requirements/        REQUIREMENTS.md: IDs, acceptance criteria, verification
  decisions/           DECISIONS.md: dated decision log (DEC-NNN)
  risks/               RISKS.md: register (RSK-NNN)
  quality/             QUALITY_PLAN.md: VibeQM self-assessment, gates, metrics
  tailoring/           TAILORING.md: what this project changed from the standard (TLR-NNN)
  mockups/             UI, covers, diagrams
  research/            dated research; read-only once written
  ideas/               IDEAS.md: future products and backlog (IDEA-NNN)
  framework/           only in the repo that owns a framework/standard
```

## 3. Required documents by level

A project at a level must keep the documents marked for that level and below.
"Light" means a short version is enough (a few lines or a table).

| Document | L1 Unguided | L2 Guarded | L3 Standardized | L4 Measured | L5 Self-Improving |
|:--|:-:|:-:|:-:|:-:|:-:|
| `README.md` index | — | ✓ | ✓ | ✓ | ✓ |
| Agent rules file pointing to VibeQM | — | ✓ | ✓ | ✓ | ✓ |
| Requirements with acceptance criteria (issue tracker or file); clarifying questions and answers recorded | — | light | ✓ | ✓ | ✓ |
| Requirements traceability (requirement → design → tests → changes); non-functional requirements | — | — | ✓ | ✓ | ✓ |
| Workflow and architecture diagrams, kept current | — | — | ✓ | ✓ | ✓ |
| Decision log (from L3: options considered, recommendation, choice) | — | light | ✓ | ✓ | ✓ |
| Plan | — | light | ✓ | ✓ | ✓ |
| Note on how development is kept separate from production | — | light | — | — | — |
| Environment definitions (development, testing/staging, production) and pipeline configuration | — | — | ✓ | ✓ | ✓ |
| Verification and validation record for each production release | — | — | ✓ | ✓ | ✓ |
| Software inventory (SBOM) and update policy ([the specification](VQM_SPEC.md) §10) | — | — | ✓ | ✓ | ✓ |
| Release notes and changelog | — | — | ✓ | ✓ | ✓ |
| Runbooks (deploy, rollback, incident response); backup and restore records | — | — | ✓ | ✓ | ✓ |
| Postmortem for every incident (blameless) | — | — | ✓ | ✓ | ✓ |
| Training record (standard and AI tools) | — | — | ✓ | ✓ | ✓ |
| Risk register | — | — | ✓ | ✓ | ✓ |
| Quality plan + self-assessment | — | — | ✓ | ✓ | ✓ |
| Tailoring record | — | — | ✓ | ✓ | ✓ |
| Provenance record (model/version that wrote and reviewer that reviewed each change) | — | — | ✓ | ✓ | ✓ |
| Front matter (id, version, status, date) on each document | — | — | ✓ | ✓ | ✓ |
| Critical rules, each mapped to the hook, check or permission that enforces it | — | — | ✓ | ✓ | ✓ |
| Risk classes for changes; threat model for each high-risk change | — | — | ✓ | ✓ | ✓ |
| Model register: models and versions in use, and the checks run before each switch | — | — | ✓ | ✓ | ✓ |
| Data boundary: what code and data may go to which AI company | — | — | ✓ | ✓ | ✓ |
| Gate proof record: when each automated check was seen catching a planted fault; from L3, the AI peer reviewer's planted-fault set and results, kept where the agent's session can't write | — | light | ✓ | ✓ | ✓ |
| Lessons log: dated entries with what happened, why, and what will change | — | — | ✓ | ✓ | ✓ |
| Metric definitions, if tailored from [the specification](VQM_SPEC.md) §8 | — | — | — | ✓ | ✓ |
| Metrics (VibeQM, DORA, freshness, SLOs, the revert count and one signal from outside the team) with baselines and limits | — | — | — | ✓ | ✓ |
| Root-cause analysis per escaped defect and incident; lessons entries link the change | — | — | — | — | ✓ |
| Improvement trials and periodic process review | — | — | — | — | ✓ |

A solo developer at Level 2 can live with one page: a README, a rules file, and a
few lines of requirements and decisions.

## 4. Tailoring

A project may drop, merge, rename or extend any document, folder or template.
Each change is one row in `tailoring/TAILORING.md`:

| ID | Date | Standard item | Change | Reason | Approved by |
|:--|:--|:--|:--|:--|:--|

Rules:
- Tailoring never removes a document required by the level the project claims;
  drop the claim instead. The one exception: for a product with no live production
  service, a document for a service-bound item ([the specification](VQM_SPEC.md) §6) is replaced by the
  stated equivalent, or marked not applicable with the reason.
- Merging is fine (e.g. risks inside the plan for a small project) as long as the
  IDs and fields survive.
- Organizations can publish their own tailored standard; projects tailor from that.

## 5. Templates

Templates for the Level 2 documents are in [`templates/`](../templates/): fields, an example row, and the check that keeps it honest (for example,
"every REQ has a verification method").

From Level 3 every document starts with front matter that a script can read:

```yaml
---
id: requirements
version: 0.1
status: approved
date: 2026-10-05
---
```
