# Releases

## Versioning

All packages use **Semantic Versioning (SemVer)**: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

## Conventional Commits

Commits drive automatic version bumps via **release-please**:

```
feat(scope): new feature       - minor bump (x.Y.0)
fix(scope): bug fix            - patch bump (x.y.Z)
feat(scope)!: breaking change  - major bump (X.0.0)
```

### Package Scopes

| Scope | Package | Tag Prefix |
|-------|---------|------------|
| `edt` | extended-data-types | `edt-v` |
| `logging` | lifecyclelogging | `logging-v` |
| `dic` or `inputs` | directed-inputs-class | `inputs-v` |
| `connectors` | vendor-connectors | `connectors-v` |
| `secretssync` | secretssync | `secretssync-v` |

## Release Process

```
Push to main with conventional commit
        |
CI runs tests & lint
        |
release-please analyzes commits
        |
Release PR created/updated (version bumps + changelogs)
        |
Release PR merged
        |
Tags created automatically
        |
Publish jobs triggered (PyPI / GoReleaser)
```

### Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `release.yml` | Push to main | release-please PR management + package publishing |
| `automerge.yml` | PR opened by bots | Auto-approve + squash-merge dependabot/release-please PRs |
| `cd.yml` | Push to main | Documentation deployment to GitHub Pages |

### Configuration Files

| File | Purpose |
|------|---------|
| `release-please-config.json` | Package definitions, release types, changelog config |
| `.release-please-manifest.json` | Current version tracking for each package |

## Dependabot

Dependabot creates grouped PRs (one per ecosystem) that are automatically merged by the automerge workflow. Merge commits include `[skip actions]` to prevent cascading workflow runs.

## What NOT to Do

- **Never** manually edit version numbers in `pyproject.toml` or the manifest
- **Never** create tags by hand (release-please manages tags)
- **Never** skip CI for releases
- **Never** merge release PRs with the "merge" strategy (always squash)

## Checking Release Status

```bash
# Check recent releases
gh release list --limit 5

# Check open release PRs
gh pr list --label "autorelease: pending"

# Check CI status
gh run list --limit 3

# View release-please manifest
cat .release-please-manifest.json
```
