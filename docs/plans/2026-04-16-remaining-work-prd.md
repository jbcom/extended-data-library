# Remaining Work PRD

Status: Draft
Date: 2026-04-16
Scope: `jbcom/extended-data-library`
Owner: Maintainers

## Executive Summary

As of 2026-04-16, the monorepo is operational and materially more stable than
it was before the recent cleanup push. `main` is clean, there are no open pull
requests, there are no open GitHub issues, the docs site is live, package
release automation is working, and the repo no longer depends on the removed
control-center/agentic scaffolding for day-to-day work.

The remaining work is not a single blocking product bug. It is a set of
maintainer-facing cleanup and hardening tracks that still matter because they
affect public trust, repository clarity, contributor ergonomics, and the long-
term cost of operating the monorepo.

This PRD defines the remaining work required to finish the repository cleanup
phase and move the monorepo from “stable and usable” to “coherent, maintainable,
and intentionally operated.”

## Current State Snapshot

As of 2026-04-16:

- GitHub open pull requests: `0`
- GitHub open issues: `0`
- Default branch: `main`
- GitHub repo homepage: unset
- GitHub repo description: still `Extended Data Types` with a trailing space
  instead of a monorepo description
- Unmerged remote branches with no open PR attached: `37`
- Root instruction surface: `AGENTS.md` is current and tracked
- Public docs host: `https://extended-data.dev`

Observed remaining debt:

- Historical package changelogs still contain public references to
  `jbcom-control-center`, `control-center`, `agentic-control`, and related
  legacy provenance.
- Editor and internal state files are still tracked:
  - `memory-bank/activeContext.md`
  - `src/.gemini/settings.json`
  - `docs/.gemini/settings.json`
- `.gitignore` still contains old “Ruler Generated Files” entries that conflict
  with the repo’s current intentional state, including ignoring `/AGENTS.md`
  even though `AGENTS.md` is now a real tracked instruction file.
- The remote branch namespace still contains large amounts of abandoned
  `cursor/*`, `copilot/*`, `repo-sync/*`, `sync/*`, `release/*`, and similar
  residue.
- Some connector and documentation surfaces still imply broader support or more
  polished integration coverage than the repo has explicitly classified.

## Problem Statement

The repository has passed the “make it work” phase, but it has not fully passed
the “make it coherent” phase.

Today, the monorepo still sends mixed signals:

- GitHub metadata still describes one package rather than the monorepo.
- Historical changelogs still reference the old control-center lineage.
- Internal editor state is checked into the repo.
- Old branch residue makes it hard to tell which work is live.
- Connector surfaces are broadly useful, but the support level for each
  connector is not clearly tiered.

None of these are individually catastrophic. Together, they keep the repository
from looking intentionally maintained end-to-end.

## Goals

1. Make the monorepo’s public identity consistent across GitHub, docs, package
   metadata, and contributor guidance.
2. Remove tracked internal/editor state and align ignore rules with the current
   repository model.
3. Resolve legacy provenance leakage in public changelog and historical release
   surfaces where it still confuses users.
4. Clean up abandoned remote branch residue and document a branch lifecycle
   policy that prevents the same buildup.
5. Classify connector support levels and tighten the documentation around what
   is fully supported versus merely present.
6. Convert the remaining work into a finite sequence of mergeable cleanup PRs
   rather than leaving it as indefinite “later” debt.

## Non-Goals

- Creating new packages or new product lines.
- Major breaking API redesigns in stable packages.
- Rebuilding the docs site architecture again.
- Replacing release-please with a different release system.
- Large connector feature expansion unless explicitly required by the support-
  tier audit.

## Users and Stakeholders

- Maintainers who cut releases, review PRs, and operate the repo.
- Contributors who need clear repo instructions and predictable workflows.
- Package consumers who rely on README, changelog, docs, and PyPI metadata as
  the primary trust surface.
- Docs users who expect the GitHub repo and docs site to describe the same
  system.
- Automation and integration users who need clarity about which connector
  surfaces are stable, optional, or experimental.

## Workstreams

### Workstream 1: Monorepo Identity and GitHub Metadata

#### Problem

The repository is now a monorepo, but GitHub’s top-level metadata still looks
like a single-package repository.

#### Requirements

- Update the GitHub repository description from `Extended Data Types` with a
  trailing space to a monorepo description that reflects all maintained
  packages.
- Set the GitHub repository homepage to `https://extended-data.dev`.
- Verify that root README positioning matches the GitHub description and docs
  site headline.
- Confirm that package-level documentation links and root-level docs links all
  agree on the canonical domain.

#### Acceptance Criteria

- GitHub repo description accurately describes the monorepo.
- GitHub homepage points to `https://extended-data.dev`.
- Root README language matches the monorepo description.
- No active public docs or metadata surfaces describe the repo as only
  “Extended Data Types.”

#### Notes

This work includes GitHub settings, so not all of it is fixable by commit
alone.

### Workstream 2: Repository Hygiene and Tracked State Cleanup

#### Problem

Internal/editor state is still tracked, and `.gitignore` still reflects the
removed Ruler/control-center era more than the current repository model.

#### In-Scope Paths

- `memory-bank/activeContext.md`
- `src/.gemini/settings.json`
- `docs/.gemini/settings.json`
- `.gitignore` legacy “Ruler Generated Files” block

#### Requirements

- Decide whether any tracked `.gemini` settings are intentionally required. If
  not, remove them from git tracking and keep them ignored.
- Remove `memory-bank/activeContext.md` from git tracking unless there is a
  current maintainership requirement to keep it versioned.
- Simplify `.gitignore` to reflect the current repo model.
- Remove ignore rules that are only remnants of removed tooling.
- Stop ignoring intentional tracked files like `/AGENTS.md`.

#### Acceptance Criteria

- No editor state, model state, or memory-bank state is tracked unless it is
  explicitly justified in repo docs.
- `.gitignore` is understandable without needing historical context.
- Intentional instruction files are tracked normally and are not simultaneously
  treated as generated garbage.

### Workstream 3: Historical Changelog and Provenance Cleanup

#### Problem

Public changelogs for maintained packages still contain large numbers of old
references to:

- `jbcom-control-center`
- `control-center`
- `agentic-control`
- old ecosystem sync workflows
- old Ruler-era provenance

This history is technically real, but it creates avoidable confusion for users
trying to understand the current monorepo.

#### Affected Surfaces

- `packages/extended-data-types/CHANGELOG.md`
- `packages/lifecyclelogging/CHANGELOG.md`
- `packages/directed-inputs-class/CHANGELOG.md`

#### Required Decision

Choose one policy and apply it consistently:

1. Rewrite historical URLs and old repo names in package changelogs so the
   public record reflects the current monorepo.
2. Preserve raw historical entries but add a standard note explaining that
   earlier changes were imported from the old control-center lineage.

#### Recommendation

Prefer policy `2` unless there is a strong reason to rewrite historical release
records. An explanatory note preserves provenance while reducing confusion.

#### Acceptance Criteria

- There is one explicit changelog provenance policy.
- Maintained package changelogs no longer surprise readers with unexplained old
  repo names.
- Public changelog surfaces describe the relationship between historical and
  current monorepo releases clearly.

### Workstream 4: Remote Branch Hygiene and Branch Lifecycle Policy

#### Problem

There are `37` unmerged remote branches with no open pull request attached.
Most are abandoned automation or bot branches from earlier cleanup periods.

Examples include:

- `cursor/*`
- `copilot/*`
- `repo-sync/*`
- `sync/*`
- `release/*`
- `renovate/configure`
- `add-claude-github-actions-*`
- `feat-implement-mcp-server-*`

#### Requirements

- Audit all unmerged remote branches.
- Classify each branch as one of:
  - delete immediately
  - archive/tag before delete
  - keep intentionally
- Delete abandoned remote branches in batches with reviewable rationale.
- Document the branch lifecycle policy in maintainer docs:
  - when branches should be deleted
  - when automation branches may remain
  - how long stale branches are tolerated

#### Acceptance Criteria

- All remote branches with no purpose are deleted.
- Remaining non-`main` remote branches have an intentional owner or reason.
- Maintainer docs describe how branch cleanup is handled going forward.

### Workstream 5: Documentation and Contributor Surface Alignment

#### Problem

The repo-level docs are much cleaner than before, but there is still drift
between the root README, maintainer instructions, and package docs in a few
small but important places.

#### Requirements

- Align root README development guidance with `AGENTS.md` where the guidance is
  user-visible and non-agent-specific.
- Add an explicit maintainer-facing roadmap/cleanup note that points to this
  PRD or its successor.
- Review package README “Project Links” and “Contributing” sections for
  consistency in wording and target links.
- Confirm that all maintained public docs surfaces use the same support-floor
  language for each package.

#### Acceptance Criteria

- Root README, package READMEs, and maintainer docs do not contradict each
  other on core workflow details.
- Contributors can find one current roadmap document without needing PR history.

### Workstream 6: Connector Support-Tier Audit

#### Problem

The connector package is broad and useful, but the repo does not yet clearly
signal which integrations are:

- core and actively maintained
- maintained but optional
- present but more provisional

There are also a few surfaces that hint at future functionality, such as the
`days_since_activity` argument in
`packages/vendor-connectors/src/vendor_connectors/google/services.py`, whose
docstring explicitly says the threshold is not implemented yet.

#### Requirements

- Audit every connector family:
  - AWS
  - Google
  - GitHub
  - Slack
  - Vault
  - Zoom
  - Anthropic
  - Cursor
  - Meshy
  - SecretSync Go package surface
- Define a support-tier model and document it.
- Ensure package README and docs site reflect those support tiers.
- Identify any arguments, examples, or public methods that imply functionality
  not actually guaranteed.

#### Acceptance Criteria

- Every connector family has an explicit support tier.
- The README and docs site state support expectations clearly.
- No public argument or docstring says “not implemented yet” without a tracked
  decision to either implement or remove it.

### Workstream 7: Release and Public Surface Hardening

#### Problem

Release automation works, but the public-facing integrity of releases still
depends heavily on convention rather than documented policy.

#### Requirements

- Document which files are authoritative for releases:
  - package `pyproject.toml`
  - release-please config
  - package changelogs
  - docs site package pages
- Verify that release-oriented docs are consistent for all maintained packages,
  not just `extended-data-types` and `secretssync`.
- Add a maintainer checklist for post-release verification:
  - PyPI package published
  - GitHub release present
  - docs links point at current package pages
  - SecretSync install path still works

#### Acceptance Criteria

- There is one documented release-verification checklist.
- Release surfaces across packages are reviewed using the same standard.

## Prioritization

### P0: Immediate Cleanup and Clarity

- Workstream 1: monorepo identity and GitHub metadata
- Workstream 2: repository hygiene and tracked state cleanup
- Workstream 4: remote branch hygiene and lifecycle policy

Reason: these are low-risk, high-clarity changes that reduce confusion now.

### P1: Public Historical Surface Cleanup

- Workstream 3: changelog and provenance cleanup
- Workstream 5: docs and contributor surface alignment

Reason: these improve public coherence but require slightly more editorial
judgment.

### P2: Product-Surface Classification

- Workstream 6: connector support-tier audit
- Workstream 7: release and public-surface hardening

Reason: these are important, but they require maintainers to make explicit
support-policy decisions rather than simply fixing residue.

## Proposed Execution Plan

### Phase 1: Repo and GitHub Cleanup

Single focused PRs:

1. GitHub metadata + root README alignment
2. tracked state removal + `.gitignore` cleanup
3. branch cleanup policy + branch deletions

### Phase 2: Historical Surface Cleanup

Single or split PRs:

4. package changelog provenance policy and cleanup
5. docs/readme consistency pass across maintained packages

### Phase 3: Support Classification

Single or split PRs:

6. connector support-tier audit
7. release verification checklist and maintainership docs

## Success Metrics

The cleanup phase is complete when:

- GitHub repo metadata accurately represents the monorepo.
- No internal/editor state files are tracked without explicit justification.
- `.gitignore` no longer contains contradictory removed-tooling residue.
- Stale remote branches are cleaned up and branch policy is documented.
- Public changelog history is explained consistently.
- Connector support levels are documented explicitly.
- Maintainers can point to one current roadmap and one current release checklist.

## Risks and Tradeoffs

### Changelog Rewriting Risk

Rewriting historical changelog content can make old release references less
authentic. Preserving history without explanation, however, keeps confusing
users. This is why a provenance note may be the safer default.

### Branch Cleanup Risk

Deleting old remote branches is easy to do incorrectly if any abandoned branch
still contains work somebody cares about. Cleanup should happen in reviewed
batches with a recorded keep/delete decision.

### Connector Audit Scope Risk

If support tiers are defined too aggressively, maintainers may commit to more
than they can reliably support. If they are defined too loosely, users still
won’t know what to trust.

## Dependencies

### In-Repo

- Maintainer docs
- package READMEs
- package changelogs
- `.gitignore`

### Out-of-Repo

- GitHub repository description
- GitHub homepage URL
- remote branch deletion permissions

## Open Questions

1. Should historical changelog entries be rewritten or only annotated?
2. Should `docs/.gemini/settings.json` and `src/.gemini/settings.json` exist at
   all in version control?
3. Is `memory-bank/activeContext.md` still needed as a tracked repository file?
4. Which connector families are officially “core” versus “best-effort”?
5. Should branch cleanup be manual policy, scheduled automation, or both?

## Appendix: Evidence Collected During Audit

- GitHub open issues: `0`
- GitHub open PRs: `0`
- Unmerged remote branches without open PRs: `37`
- GitHub homepage URL: unset
- GitHub repo description: `Extended Data Types` with a trailing space
- Tracked internal/editor state:
  - `docs/.gemini/settings.json`
  - `memory-bank/activeContext.md`
  - `src/.gemini/settings.json`
- Intentional tracked instruction file currently contradicted by `.gitignore`:
  - `AGENTS.md`
- Explicit public “not implemented yet” wording found in:
  - `packages/vendor-connectors/src/vendor_connectors/google/services.py`
