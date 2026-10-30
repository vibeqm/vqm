# The Vibe Quality Model (VibeQM): specification v0.4.6

Version 0.4.6, 2026-10-30. Part of the Vibe Quality Model: [vibeqm.com](https://vibeqm.com).

The definition of the model: the five levels, the autonomy each one earns, the
evidence rules and what each level requires. The assessor procedure
([ASSESSOR.md](ASSESSOR.md)) turns it into checks; the documentation standard
([DOC_STANDARD.md](DOC_STANDARD.md)) lists the records.

## 1. The purpose, and the rule that follows

**Purpose: take vibe coding from ad-hoc to professional, with quality that
employers and customers can trust.** The model works through the agent: its rules
files, checks and prompts instruct the AI to follow professional practice and keep
the records, so the developer's everyday work changes little.

**The rule that follows: a team earns more AI autonomy by proving quality.** Each level is defined by the
evidence a team can produce, and each level states the autonomy that evidence earns
(§3). The popular autonomy ladders (Shapiro's five levels end at a "dark factory"
where nobody reviews AI code; Yegge's stages count parallel agents, "Welcome to
Gas Town", January 2026) treat autonomy
as the goal. VibeQM treats it as the reward.

## 2. The five levels

One set of names for every book and document. Each name says how far the
AI's work is guarded by the team's process. No slang.

| Level | Name | What is true | Evidence gate to claim it |
|:--|:--|:--|:--|
| 1 | **Unguided** | Prompt, accept, ship what runs. Quality depends on luck and on one person's attention | None. Everyone starts here |
| 2 | **Guarded** | Every project has the basics: written requirements, a rules file, version control, peer review, verification and a security review on every change, development kept apart from production, limited agent permissions, and a human owner for every change | Every item of §6 Level 2 is met, with evidence |
| 3 | **Standardized** | One shared standard across projects, enforced by the system and audited: managed and traceable requirements with diagrams, risk-based peer review, verification and validation before every deployment through at least three environments, current platforms and dependencies, release, incident and backup practices, pinned models, provenance, a lessons log, training | Every item of §6 Level 3 is met, with evidence, and an audit shows the standard is followed |
| 4 | **Measured** | The four VibeQM numbers, DORA's four delivery metrics and one signal from outside the team are tracked against limits, with baselines for each model family; service-level objectives hold in production; low-risk self-merging is checked before every merge and stops automatically at a breach | Every item of §6 Level 4 is met, with a history of acting on the numbers |
| 5 | **Self-Improving** | Every escaped defect and incident gets a root-cause analysis and becomes a new rule, check, skill or permission; improvements and new tools are tried against the numbers before adoption | Every item of §6 Level 5 is met; each lessons entry links to the change it made |

The gate column summarizes. §6 lists every required artifact and practice, and
[ASSESSOR.md](ASSESSOR.md) §2 lists the checks; a level is met only when all of its items are met.

**The unit of a claim**. Level 2 is claimed for one repository. Level 3 and
above are claimed for a team or an organization: the claim lists its repositories,
each of which meets the lower levels, and the shared standard is read in the
repository that owns it. A solo developer is a team of one: they claim Level 3 and
above for the repositories they list (one is enough), and the standard lives in one of
them.

**Staged rule.** A level is claimed only when every lower level is also met. A team
with a lessons loop (5) but no measurements (4) is at Level 3.

**Autonomy follows evidence.** When a gate stops being met, the autonomy earned at
that level and above (§3) is suspended until it is met again.

## 3. Autonomy earned at each level

| Level | The AI may | A person must |
|:--|:--|:--|
| 1 Unguided | Nothing is earned yet: treat everything the AI writes as a draft (autonomy ladder: L1, coding intern) | Read every change before it lands. Most teams at this level give the AI far more freedom; that gap is the risk this level names |
| 2 Guarded | Edit code on a separate branch while a person supervises the session; run the checks (autonomy ladder: L2, junior developer) | Own and approve every change, after the checks pass and a peer review |
| 3 Standardized | Take a task from start to a finished, proposed change on its own (for example, from an issue to a pull request) (autonomy ladder: L3, developer) | Approve every merge; high-risk changes get both a human and an AI peer review |
| 4 Measured | Merge low-risk changes itself, after the checks and an automated AI peer review, while all the Level 4 numbers stay within their limits. A hook checks the change and the numbers before every self-merge and cuts this permission off automatically at a breach, until the numbers recover or a named person overrides it with a lessons entry (§7) (autonomy ladder: part of L4, engineering team) | Approve every standard- and high-risk merge |
| 5 Self-Improving | Merge low- and standard-risk changes itself under a written **performance agreement**, with an **AI peer** (a model from a different company) reviewing every change against it and a **kill switch** that suspends the developer AI the moment it breaches the agreement; and propose changes to its own rules, checks and skills (autonomy ladder: L5, governed) | Own the performance agreement and approve any change to it; give every high-risk change a human peer review; restore autonomy after a kill switch fires (a named person, with a lessons entry); approve anything irreversible and every change to the AI's own rules |

The steps in parentheses are the closest match on Dan Shapiro's widely shared
autonomy ladder (L0 autocomplete to L5 "dark factory", January 2026), shown so
readers can compare. The match is approximate: his levels describe one
developer's way of working, VibeQM's describe a team's evidence.

**Level 5 is a governed L5**. Nobody reviews each low- or standard-risk
change by hand, but the work is not unsupervised:

- **The performance agreement** is written and owned by named people. It states the
  limits on the Level 4 numbers, what the developer AI may merge (low and standard
  risk), the review criteria (for example: no weakened tests, every change traced
  to a requirement, security review clean), and what triggers the kill switch.
- **The AI peer**, a model from a different company, reviews every change the
  developer AI makes against the agreement.
- **The kill switch** fires when the AI peer finds a breach or a Level 4 limit is
  crossed: it suspends the developer AI's self-merging and autonomous work, reverts
  or quarantines the offending change if it has not been deployed, and alerts the
  owners. Autonomy returns only when a named person has reviewed the breach,
  recorded a lessons entry and restored it.
- The kill switch is tested like every other check: a planted breach must fire it
  (§4 rule 2).
- People still own the agreement, give every high-risk change a human peer review,
  and approve anything that can't be undone. That is what separates a governed L5
  from a dark factory, where nobody is accountable.

**Owner and approver are different roles**. Every change names a human
**owner**, accountable for it, at every level, including changes the AI merges
itself at Level 4. The **approver** is whoever approves the merge; at Levels 2 and 3
that is always a person.

**At every level,** anything that can't be undone needs a person's approval at the
moment it happens. The test: if the team can't undo the action with a
rollback it has actually practiced, it can't be undone. For example: deleting data,
deploying to production, publishing a package or a release, rewriting shared history,
deleting tags or branches, sending messages outside the team, spending money,
creating or rotating credentials, or changing the agent's own permissions. The list
is examples; the test decides.

## 4. Evidence rules

1. **The agent's word is not evidence.** Only records the system produced count:
   check logs, test output, commit history, review records. From Level 4, the
   records that grant autonomy (review verdicts, gate-proof records, self-merge
   approvals) are written by a hook or CI and kept where the agent's working session
   can't write them: a CI attestation, a signed commit, or a path the agent's
   permissions block. Each names the change it covers by its hash. The same
   applies from Level 3 to the reviewer's planted-fault record (§7).
2. **A check counts only after it has been seen to fail.** For automated checks:
   a planted fault or mutation testing, with a record; at Level 2, a real failure
   that blocked a change and was then fixed counts too. For process gates
   that can't be triggered on cue: one real change the gate stopped or corrected.
3. **Peer review must be independent**. Two kinds count:
   - **Human peer review:** a person other than the change's author reviews it.
   - **AI peer review:** a model from a **different company** than the one that
     wrote the change reviews it, in a separate session.
   A model reviewing its own work is not a peer review. The provenance record names
   the reviewer.
4. **Risk decides the review.** Every change falls in a risk class (§5), and the
   class sets the minimum peer review.
5. **Traces over documents.** A document proves a standard exists; only traces
   (history, logs, defects caught) prove it is followed.

## 5. Risk classes

| Class | Examples | Minimum before it lands |
|:--|:--|:--|
| Low | Documentation, comments, styling, new tests that leave existing tests unchanged | Automated checks, plus the level's peer review (every change gets one from Level 2); the class is what makes a change eligible for the AI's self-merge at Level 4 |
| Standard | Everything not listed as low or high | Automated checks, plus a human **or** AI peer review |
| High | Login and permissions, payments, personal data, deleting data, security settings, deployment and infrastructure, new dependencies and agent plug-ins, the AI's own rules and permissions, any change that weakens or deletes a test | Automated checks plus a peer review (Level 2); from Level 3, a human **and** an AI peer review plus a threat model |

From Level 2, every change, whatever its class, gets at least one peer review (§6), and by the staged rule that holds at every higher level: the AI's self-merges at Levels 4 and 5 always follow an AI peer review. A level's autonomy adds to this minimum and never removes from it.

**Classes are audited.** The assessor re-sorts a sample of at least 20 changes. If
more than one in ten was classed lower than it should have been, the risk-class
audit fails and Level 4 self-merging is suspended.

## 6. What each level requires

Each level requires everything in the levels below it.

**Applicability.** Some items assume a live production service: three
environments and promotion through them, verification and validation per production
release, runbooks, monitoring, incident response, backups, service-level objectives
and DORA's delivery numbers. They apply where the product has a live production
service. For other products (a library, a command-line tool, a mobile app, a static
site, a publishing pipeline) the standard states each item's equivalent: production
is the published release, staging a pre-release channel or a test install,
deployment frequency the release or publish frequency. An item with no meaningful
equivalent (service-level objectives for a library) is marked not applicable, with
the reason. Both are recorded as tailoring. An equivalent must be as strict as the
item it replaces: it changes the form of the item, not whether it is met.

### Level 1 — Unguided

Nothing is required.

### Level 2 — Guarded (the basics, for every project)

**Artifacts**

- A rules file specific to the repository, and a README.
- Written requirements with acceptance criteria (an issue tracker, or a short file);
  an issue tracker or backlog, so every change traces to a request. (The decision log
  and the plan are Level 3 artifacts, ; the Level 2 templates create short
  versions as a head start.)
- Version control with branches; tagged releases (until the first release, a note
  that nothing is released yet).
- Dependency manifests with lockfiles.
- CI configuration with blocking checks; linter, formatter and test-suite
  configuration.
- Secret-scanning configuration; no secrets in the repository.
- Agent deny rules.
- A short note, or a section of the rules file, naming the development and the
  production environment (or saying nothing is live yet).
- A record of each blocking check seen to fail.

**Practices**

- **Requirements first.** Every change starts from a written requirement or issue
  with acceptance criteria. When a requirement is ambiguous, the agent **asks the
  person clarifying questions with multiple options, the recommended option first**,
  before writing code, and the answer is recorded.
- **Peer review before merge.** Every change gets a human or an AI peer review
  (§4 rule 3). The unit is the push or the pull request, not the commit: one review
  at each push to the shared branch, or on each pull request, covers every commit
  since the last reviewed one, and nothing reaches staging or production unreviewed.
- **Verification on every change.** Tests, linter and static analysis run, and a
  failure blocks the change.
- **Security review before every push.** An AI security review of the change (for
  example Claude Code's `/security-review`), secret scanning, and a dependency
  vulnerability scan that blocks on critical findings.
- **Development separated from production.** There is a development environment and
  a production environment, and the agent publishes to production only after the
  person confirms, in the rules file or, better, in the agent's settings. A testing or
  staging environment is recommended, not required, at this level.
- The agent works on a branch; changes reach the main branch only through a merge
  path that can refuse them: pull requests with branch protection, or, for one
  person, the accepted equivalent: a committed blocking hook, the bypass
  (`--no-verify`) denied in the agent's settings, recorded as tailoring.
- Small changes: median 400 changed lines or fewer, unless the standard states
  another limit. A change is a commit on the main branch, merge commits left out, so
  a squash-merged pull request is one change. A high-risk change (§5) stays within that limit; split it if not.
- The agent can't force-push, skip checks, delete outside the project or read
  secrets.
- Every change names a human owner.
- Every blocking check has been seen to fail.

### Level 3 — Standardized (one enforced standard across projects)

**Artifacts** (every document starts with front matter: id, version, status, date)

- One written standard, readable by people and agents.
- **Requirements with traceability:** each requirement linked to its design, its
  tests and the changes that implement it. Non-functional requirements (performance,
  security, accessibility, reliability) stated and tested.
- **Requirement visualizations:** workflow and architecture diagrams kept in the
  repository (for example in Mermaid) and updated with every change that alters
  them.
- **Decision records with options:** significant decisions record the options
  considered, the recommendation and the choice.
- Plan, risk register, quality plan with self-assessment, tailoring record.
- Provenance record: which model and version wrote and which reviewer reviewed each
  change.
- Critical-rules table, risk-class definitions, model register, gate proof record,
  data boundary.
- Lessons log, and a blameless postmortem for every incident.
- Environment definitions for development, testing/staging and production, as code;
  the deployment pipeline configuration.
- A verification and validation record for each production release.
- A software inventory (SBOM): every library, runtime, database, operating system and
  container base image the product uses, with its version; the update policy (§10).
- Runbooks for deploy, rollback and incident response; backup and restore records.
- A training record: the team trained on the standard and the AI tools.

**Practices**

- **Requirements management.** Traceability maintained; changes to requirements
  controlled and recorded; diagrams kept current; clarifying questions with options
  recorded in the decision records.
- **Peer review by risk.** Standard-risk changes get a human or AI peer review;
  high-risk changes get both, plus a threat model. A review checklist is used. Risk
  classes are audited (§5).
- **Verification and validation before every production deployment.**
  *Verification*, built right: tests, peer review, static analysis, security review.
  *Validation*, the right thing built: acceptance tests against the requirements, run
  in staging, signed off by the owner.
- **At least three environments:** development, testing/staging (production-like)
  and production. Changes are promoted through them by the pipeline; nothing changes
  production directly; production data stays out of development unless masked. The
  agent never holds production access or production credentials: only the pipeline
  deploys.
- **Platform and dependency currency** (§10): libraries, runtimes, databases,
  operating systems and container images on current stable releases within the
  policy's windows; automated update proposals; images rebuilt on a schedule; no
  end-of-life software.
- **Security engineering:** threat models for high-risk changes; static analysis
  (SAST), dependency and container scanning in CI; secrets in a secret manager.
- **Release management:** versioned releases, changelog and release notes, a
  rollback the team has actually tried.
- **Operations:** monitoring, logging and alerting in production; a defined incident
  response; backups with tested restores.
- **Standard and audit:** an audit that can fail runs at least monthly, unless the
  standard states another cadence, and shows every project follows the standard.
- **Critical rules enforced** by hooks, blocking checks or permissions (§7).
- Pinned models; rules files within the size limit and reviewed; agent plug-ins and
  tools pinned and added as high-risk changes; parallel agents on separate branches;
  a license check on new code; a lessons entry for every escaped defect.

### Level 4 — Measured

**Artifacts**

- The four VibeQM numbers (§8): escaped defects, security findings, review time with
  review yield, churn; and the revert count as the cross-check on escaped defects.
- DORA's four delivery metrics (§8): deployment frequency, lead time for
  changes, change failure rate, time to restore service. DORA renamed the last
  "failed deployment recovery time" in 2023 and added a fifth, deployment rework
  rate, in 2024; VibeQM keeps the four classic metrics and accepts DORA's current
  definitions.
- Dependency freshness: patch latency and how far behind current versions the
  product is.
- Service-level objectives for production, with their measurements.
- **One signal of quality from outside the team**: written by people
  outside the team, such as defects users report, support requests, externally raised
  issues or customer acceptance results (for a book, reader errata and returns), with
  its source and a baseline. Incidents the team records itself don't count, and it is
  never a quality score the team computes.
- Baselines for each model family, limits, the warm-up or revalidation record for the
  last model switch, the automatic-stop check, and records linking numbers to process changes.

**Practices**

- The numbers are reviewed monthly, where the limits are set and recalibrated;
  baselines restart when the model family changes, with the warm-up rule, and are
  revalidated at a version change (§7).
- The automatic stop is checked before every self-merge and cuts off self-merging
  at a breach (§7).
- Process decisions are made from the data, and at least one recorded process change
  was triggered by a number.

### Level 5 — Self-Improving

**Artifacts**

- A lessons log in which each entry names the rule, check, skill or permission it
  changed and links to the commit.
- Approval records for every change to the AI's own rules, checks and permissions.
- Recurrence data by kind of defect, before and after each lesson.

**Practices**

- **Root-cause analysis** of every escaped defect and incident (for example "5
  whys"), then the strongest fix: trap, then permission, then skill, then rule.
- **Improvement proposals evaluated with the numbers** before adoption; new tools and
  models trialed against the baselines before adoption.
- **A periodic review of the process** against the standard.
- The AI proposes rule changes; a person approves. Rules and checks that no longer
  prevent anything are pruned. Mistakes of the same kind stop recurring.

## 7. Enforced rules

From Level 3:

- Every rule in the standard is marked **critical** or **advisory**. A critical
  rule is one whose breach would cause a defect, a security problem or lost work.
  The critical rules must cover at least every category in the high-risk class
  (§5), plus defenses against prompt injection.
- Critical rules are enforced by the system: a **hook**, an automated check that
  blocks the merge, or a permission the agent doesn't have. They may also appear in
  the rules file; appearing only there is not enough.
- Rules files stay within a size limit the standard states (default 200 lines).
- **The AI peer reviewer is a model like any other**. It is in the model
  register, its model and version are pinned, and a change of reviewer model or
  version is recorded and tried on recent changes before it takes over. Where a
  vendor offers no fixed version, the report declares it as a limit.
- **The AI peer reviewer has been seen to fail** (§4 rule 2). Its model and
  version have a record of catching a planted-fault set: at least five known-bad
  changes across standard and high risk, including a weakened test and a
  prompt-injection case, planted by a person or the harness, never by the agent
  under review. The set is rotated, and re-run when the reviewer model or version
  changes. A reviewer without a passing record doesn't count as a peer review; its
  changes go to a person until it passes.
  Rules that duplicate an enforced check, or no longer prevent anything, are
  removed. Every change to a rules file is reviewed like code.

From Level 4:

- Baselines belong to a model family (was a model version): the models one
  company offers under one name, such as Claude, GPT or Gemini. When the family
  changes, the baselines restart, and numbers from different families are not mixed.
- **Warm-up after a change of family**: until the new baseline has 50 merged
  changes or 30 days of data, whichever comes later, the previous limits apply,
  each moved 20% toward stricter (an escaped-defect limit of 10 becomes 8; a
  review-yield floor of 10% becomes 12%). The warm-up ends at 90 days at the latest;
  a thinner baseline is then accepted and noted in the report.
- **Revalidation after a version change inside the family**: the baseline
  continues, but the next 20 merged changes run under the warm-up limits (the current
  limits moved 20% toward stricter). If the numbers hold, the baseline carries on and
  the version change is noted in it; if a limit is crossed, the baseline restarts
  with the full warm-up. The revalidation is recorded like a warm-up. Frontier models
  change version every few months, so a restart at every version would keep a team
  in warm-up for most of the year.
- **The self-merge stop (§3) is checked at every merge**. Before each
  self-merge, a hook checks the change (its size, deleted or weakened tests, the
  re-sorted risk class, the reviewer's verdict, the security scan) and the numbers
  that can be read on the day (escaped defects and reverts over the last 30 days). A
  breach stops self-merging at once. It clears when the numbers are back within
  their limits, or when a named person records an override with a lessons entry.
  Numbers that only mean something over a month (DORA's, service-level objectives)
  are read at the monthly review: a breach found there stops self-merging from that
  date, and the report discloses the window in between.
- A change of the AI peer reviewer's model family restarts the baselines that
  depend on review (review yield, the self-merge reviews), with the warm-up rule; a
  version change inside its family revalidates them.

## 8. The Level 4 numbers

| Number | Definition | Typical source |
|:--|:--|:--|
| Escaped defects | Bugs found after a change reached the main branch, counted when the fix lands and linked to the change that caused it; per 100 merged changes, monthly | Issue tracker, or fix commits that name the change they fix |
| Outside signal | One signal written by people outside the team: user-reported defects, support requests, customer acceptance results | Support desk, public issue tracker, store reviews and returns, acceptance records |
| Reverts | Merged changes reverted or rolled back, per 100 merged changes; a cross-check on escaped defects | Version-control and deployment history |
| Security findings | New findings of medium severity or higher in code on the main branch, monthly, plus the count still open | Scanners, dependency checker, human reports |
| Review time and review yield | Median time from proposal to approval, **paired with** the share of reviews that caught something. For a solo developer: time from the AI's proposal to the owner's approval | Pull-request history, review records |
| Churn | Share of added lines changed or deleted again within 30 days | Version-control history |
| Deployment frequency (DORA) | How often the team deploys to production | Deployment pipeline |
| Lead time for changes (DORA) | Time from a change being committed to running in production | Version control and pipeline |
| Change failure rate (DORA) | Share of deployments that cause a failure needing a fix or rollback | Deployment and incident records |
| Time to restore service (DORA) | Time to recover from a failure in production | Incident records |
| Dependency freshness | Patch latency against the update policy (§10), and versions behind current | Software inventory, update tool |
| Service-level objectives | Agreed targets for availability, latency or errors in production, and their measurement | Monitoring |

Each number has a written definition, a source, a baseline for each model family
(§7), and a limit. A merged change, in the per-100 counts, is a commit on the main branch,
merge commits left out, as in §6 Level 2. A project may tailor a definition with a record.

**The numbers are diagnostics, not targets**. A number that becomes a
target stops measuring what it was meant to (Goodhart's law). Read each one with its
adversarial reading: a high review yield can mean careless first drafts rather than
sharp reviews; low churn can mean code nobody dares to improve rather than code done
right. A limit that has moved toward comfort since its baseline needs a recorded
reason.

**Escaped defects and the outside signal are read with their cross-checks**. A falling escaped-defect count can mean a quieter issue tracker
rather than better code, so it is read with change failure rate and the revert
count. Falling user reports can mean users gave up. If escaped defects fall while
change failure rate and reverts don't, or the outside signal worsens, a person
records why; without that record, the numbers earn no autonomy that month.

## 9. Further AI risks

| Risk | Rule | From level |
|:--|:--|:--|
| Code and data sent to AI companies | A written **data boundary**: which code and data may go to which AI company, and under what terms. Secrets and personal data never do | 2 (secrets and personal data); 3 (written boundary) |
| Agent plug-ins and tools | Plug-ins, tool servers (MCP) and skills from outside the team are treated as dependencies: pinned, reviewed, and added only as high-risk changes | 3 |
| Several agents in parallel | Each agent works on its own branch; every change goes through the same checks; no two agents change the same area at once without a person deciding the order | 3 |
| Licensing of AI-generated code | A check for code copied from sources under incompatible licenses | 3 |
| Rolling back AI changes | Every change can be reverted on its own, and the team has tried a rollback | 3 |

## 10. Update policy

"Up to date" means **current stable releases within a stated window**, for every
piece of software the product uses: libraries, runtimes, databases, operating
systems and container base images. The policy is written down and states at least:

- **Security patches:** critical within 14 days, high within 30 days (defaults; a
  project may set stricter ones).
- **Other updates:** on a stated schedule, for example monthly.
- **No end-of-life software:** anything past its vendor's support end is replaced.
- **How updates are verified:** every update goes through the same verification and
  validation as any other change (§6 Level 3).

"Latest the moment it ships" is not required: a new release can break production,
and a window gives time to verify it.

## 11. Before AI

Before AI agents wrote code, software organizations already managed quality with
process-maturity models (levels climbed in order), quality-management standards
(documented, audited process), statistical quality methods (measurement against
limits, root causes) and DORA's delivery metrics. All of them assume that people do
the work. VibeQM is built for the case where an AI agent does most of it; the
industry's established basics appear at Levels 2 and 3 (§6). **No text from any
other model is used.**

Related work: the AI Codebase Maturity Model (ACMM, arXiv
2604.09388), AASD-OMM (Hacettepe University, Feb 2026), DORA's 2025 AI Capabilities
Model.

## 12. Practice areas

1. **Requirements** — requirements first, clarifying questions with options,
   acceptance criteria, traceability, non-functional requirements, diagrams.
2. **Context** — rules files, specs, what the agent may read and touch.
3. **Change control** — version control, branches, small changes, risk classes,
   release management, parallel agents, rollback.
4. **Verification and validation** — tests, human and AI peer review, static
   analysis, planted faults, acceptance in staging before production.
5. **Environments and deployment** — development, testing/staging and production;
   promotion by pipeline; no direct production changes.
6. **Provenance and model management** — which model wrote and reviewed each change;
   pinning; trials before switching; portability.
7. **Security and supply chain** — security review before push, scanning, threat
   models, secrets, data boundary, agent plug-ins, licensing, platform and
   dependency currency.
8. **Agent permissions and safety** — least access, sandboxes, irreversible actions,
   prompt injection.
9. **Operations** — monitoring, incident response, postmortems, backups.
10. **Measurement** — the VibeQM and DORA numbers, freshness, service-level objectives.
11. **Learning** — lessons log, root-cause analysis, improvement trials, process
    review.
12. **Human ownership and training** — an owner for every change, cognitive debt,
    training on the standard and tools.

## 13. Assessment, self-assessment and scorecard rules

- **Assessments are done by AI** following [ASSESSOR.md](ASSESSOR.md). They are called "VibeQM
  assessments".
- The self-assessment returns a level, the autonomy it earns (§3), and the evidence
  still missing for the next level.
- A scorecard reads **"VibeQM vX.Y.Z self-assessed: Level N, DATE, ASSESSOR"**, naming
  the framework version it was assessed against. A VibeQM level is never
  presented as equivalent to a level in any other model. It adds a progress profile for the next
  level: "VibeQM v0.4.6 self-assessed: Level 2, DATE, ASSESSOR; Level 3: 20 of 27
  items open". The profile leads the result at every level, Level 1
  included, on the tool's screen and on the site: most repositories start at Level
  1 and most teams spend a long time inside Level 3, so progress is shown, not
  hidden. The result also says who the open items wait on (the
  agent alone, an answer from the person, a setting on the code host, or use) and
  the autonomy the next level earns (§3).
- **In place**. A gate whose practice is set up and recorded but measured
  over use (peer review counts after 20 reviewed changes) is reported in
  place, with how far along it is ("counts after 20 reviewed pushes, 3 so far"). It
  counts as not met for the level; the result says when it will count. Where vibeqm-check runs on every push or on a schedule, it may add
  "last checked DATE" from its latest passing run. That date says when the
  fact checks last passed; it never makes the claim continuously valid, because the
  fact checks cover only part of the gates.
- A claim keeps the version it was assessed against. When the framework changes, new
  claims are assessed against the current version; existing claims stay valid until
  their own expiry, and say which version they were assessed against.
- Two AI models from different companies assess independently, each writing its own
  report. When they disagree, the lower level stands.
- A named person countersigns every report and records whether the two agree.
- Reports state what they cover and which checks the assessor could not see; those
  stay unmet until proof is supplied.
- A result is valid for one year. A Level 4 or 5 result also ends when
  the team changes the model family it uses for the main work, because the
  baselines and the performance agreement belong to that family.
  A Level 2 or 3 result survives the change: no Level 2 gate depends on the model,
  and Level 3's model-bound gates (Models pinned, Reviewer proven) already re-run at
  a change; the team reruns the fact checks within two weeks of the switch and
  updates the rules file if the new agent needs different instructions.
- The records an assessment relies on are kept at least as long as its result is
  valid, somewhere a rebase, a squash or a CI log expiry can't erase them.
- The assessor is tested on reference repositories before assessments are offered
  to others. The set includes at least one repository whose true level is
  low and whose content tries to talk the assessor into a higher one; the assessor's
  record of resisting it is kept like the reviewer's planted-fault record.
