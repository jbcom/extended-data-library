# CHANGELOG

> **Note:** Historical links reference pre-monorepo repositories.

<!-- version list -->

## [2.1.0](https://github.com/jbcom/extended-data-library/compare/logging-v2.0.0...logging-v2.1.0) (2026-02-26)


### Features

* **docs:** switch to sphinx-autodoc2 for source-based API docs ([#74](https://github.com/jbcom/extended-data-library/issues/74)) ([6edc542](https://github.com/jbcom/extended-data-library/commit/6edc5426fd91ae39459d43ae26da8db4774287ed))

## [2.0.0](https://github.com/jbcom/extended-data-library/compare/logging-v1.0.0...logging-v2.0.0) (2026-02-24)


### ⚠ BREAKING CHANGES

* Repository restructured as monorepo. Import paths unchanged but package installation from source requires uv workspace.

### Features

* consolidate extended-data-library org into monorepo ([a6a0f63](https://github.com/jbcom/extended-data-library/commit/a6a0f63fe5a2cc4658b6ae59205890658ca66e16))


### Bug Fixes

* **ci:** remove semantic-release, add docs testing, fix CD ([#49](https://github.com/jbcom/extended-data-library/issues/49)) ([055eded](https://github.com/jbcom/extended-data-library/commit/055eded0026932058b522cd3f82a9524bb61204e))

## v0.3.0 (2025-12-23)

### Bug Fixes

- **build**: Remove broken symlinks and exclude .github from package
  ([#3](https://github.com/jbcom/python-lifecyclelogging/pull/3),
  [`f18232c`](https://github.com/jbcom/python-lifecyclelogging/commit/f18232c8152fea618086446221792eb71b321e5c))

- **docs**: Add missing sphinx-autodoc-typehints dependency
  ([#48](https://github.com/jbcom/python-lifecyclelogging/pull/48),
  [`94aef73`](https://github.com/jbcom/python-lifecyclelogging/commit/94aef7350471c6ca30b9e204465f0d7eeb1dd64c))

### Chores

- Implement Python standards compliance
  ([#3](https://github.com/jbcom/python-lifecyclelogging/pull/3),
  [`f18232c`](https://github.com/jbcom/python-lifecyclelogging/commit/f18232c8152fea618086446221792eb71b321e5c))

- Initial .cursor/environment.json from jbcom-control-center
  ([`fa71ab0`](https://github.com/jbcom/python-lifecyclelogging/commit/fa71ab0381082c8e5c541f872e879e542209ecca))

- Initial .github/workflows/docs.yml from jbcom-control-center
  ([`c07543e`](https://github.com/jbcom/python-lifecyclelogging/commit/c07543eb2510b3141264561b45a2a6f6b48dbca7))

- Initial docs/.nojekyll from jbcom-control-center
  ([`b7c8787`](https://github.com/jbcom/python-lifecyclelogging/commit/b7c87876598a70ed457a141f198a774ba2a86187))

- Initial docs/_static/custom.css from jbcom-control-center
  ([`f26f554`](https://github.com/jbcom/python-lifecyclelogging/commit/f26f554841431a828b280125ea3941fb4907072f))

- Initial docs/_templates/.gitkeep from jbcom-control-center
  ([`a07571c`](https://github.com/jbcom/python-lifecyclelogging/commit/a07571c142af683112b93502b60a7fc7d41854da))

- Initial docs/api/index.rst from jbcom-control-center
  ([`1703f5c`](https://github.com/jbcom/python-lifecyclelogging/commit/1703f5c13af1d6e56e9a0dda77343bad5f69f4cb))

- Initial docs/api/modules.rst from jbcom-control-center
  ([`2c1f17e`](https://github.com/jbcom/python-lifecyclelogging/commit/2c1f17e2cf4923592a9660edae3ae104f83570c9))

- Initial docs/conf.py from jbcom-control-center
  ([`cdb6141`](https://github.com/jbcom/python-lifecyclelogging/commit/cdb61413c0d09d3b01a59255ace50b54d0af1f87))

- Initial docs/development/contributing.md from jbcom-control-center
  ([`d2c3bc9`](https://github.com/jbcom/python-lifecyclelogging/commit/d2c3bc93970fdea007055b8acaa971039677d3aa))

- Initial docs/getting-started/installation.md from jbcom-control-center
  ([`38fd774`](https://github.com/jbcom/python-lifecyclelogging/commit/38fd77460cb4a47ac1d71b1894b6c788068a33d7))

- Initial docs/getting-started/quickstart.md from jbcom-control-center
  ([`ce488a8`](https://github.com/jbcom/python-lifecyclelogging/commit/ce488a815c98e53ec6e4da7dd8238ecc13254490))

- Initial docs/index.rst from jbcom-control-center
  ([`edf5d0e`](https://github.com/jbcom/python-lifecyclelogging/commit/edf5d0e9e3128d25f6ac4ed1088e171ecc2a245f))

- Initial docs/Makefile from jbcom-control-center
  ([`2cf9cf8`](https://github.com/jbcom/python-lifecyclelogging/commit/2cf9cf8f0dbc8f110f7b0e07e62256308957096a))

- Simplify dependabot config - direct push mode (no PRs)
  ([`28f1874`](https://github.com/jbcom/python-lifecyclelogging/commit/28f1874350a2b5cf829c034a1b8816b3a3ee5603))

- Sync .cursor/rules/00-fundamentals.mdc from jbcom-control-center
  ([`7632c73`](https://github.com/jbcom/python-lifecyclelogging/commit/7632c7389123289758674de75e42853fe017374d))

- Sync .cursor/rules/01-pr-workflow.mdc from jbcom-control-center
  ([`1e98f26`](https://github.com/jbcom/python-lifecyclelogging/commit/1e98f263cb93372c563334f3f24ad0133ba95efc))

- Sync .cursor/rules/02-memory-bank.mdc from jbcom-control-center
  ([`b11d2d5`](https://github.com/jbcom/python-lifecyclelogging/commit/b11d2d50fb9ae6b181ee86617478188c372b48cb))

- Sync .cursor/rules/ci.mdc from jbcom-control-center
  ([`0621e1d`](https://github.com/jbcom/python-lifecyclelogging/commit/0621e1d0d7086e9d7fd17480a9cba1ecc1894a1d))

- Sync .cursor/rules/python.mdc from jbcom-control-center
  ([`6f86eab`](https://github.com/jbcom/python-lifecyclelogging/commit/6f86eabbe38f6d65bd7e0e8ea9b75a413dff1b43))

- Sync .cursor/rules/python.mdc from jbcom-control-center
  ([`c326d5f`](https://github.com/jbcom/python-lifecyclelogging/commit/c326d5fbe43ce1c13c5165b69e6816b5611eb21f))

- Sync .cursor/rules/releases.mdc from jbcom-control-center
  ([`3e142b3`](https://github.com/jbcom/python-lifecyclelogging/commit/3e142b30307672f88f30aa6a9c693806109ceed8))

- Sync .github/workflows/claude-code.yml from jbcom-control-center
  ([`4125387`](https://github.com/jbcom/python-lifecyclelogging/commit/41253872cba1e429b65b53a63bbaf0c121726b1e))

- Sync .github/workflows/claude-code.yml from jbcom-control-center
  ([`a554724`](https://github.com/jbcom/python-lifecyclelogging/commit/a5547244930701ac4c7f0ed0a4bf86ce1d5c24db))

- Sync files from jbcom/.github ([#3](https://github.com/jbcom/python-lifecyclelogging/pull/3),
  [`f18232c`](https://github.com/jbcom/python-lifecyclelogging/commit/f18232c8152fea618086446221792eb71b321e5c))

- Sync settings.yml from control-center
  ([`3a11923`](https://github.com/jbcom/python-lifecyclelogging/commit/3a11923e8c6f3d5ff9209b42b8b2d6686ea6a4b6))

- Update pre-commit hooks to latest versions
  ([#3](https://github.com/jbcom/python-lifecyclelogging/pull/3),
  [`f18232c`](https://github.com/jbcom/python-lifecyclelogging/commit/f18232c8152fea618086446221792eb71b321e5c))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`8e7b053`](https://github.com/jbcom/python-lifecyclelogging/commit/8e7b053d10f5aad074d7b5e5149707d2c035316a))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`bbee5b5`](https://github.com/jbcom/python-lifecyclelogging/commit/bbee5b5bac6e020d9604838c2477e633e5eba426))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`1a4b64a`](https://github.com/jbcom/python-lifecyclelogging/commit/1a4b64afafea2c8281f7f9372fe7348d8c338f09))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`15ef52a`](https://github.com/jbcom/python-lifecyclelogging/commit/15ef52a91af1c41973e11f60fe60428dd7965fc9))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`a308089`](https://github.com/jbcom/python-lifecyclelogging/commit/a3080894f0c6bb3b17e8e2a8dbfc7d5b218c9d12))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`c14bdee`](https://github.com/jbcom/python-lifecyclelogging/commit/c14bdee85d45d911728538f92428705dc20f730a))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`d7fe3d1`](https://github.com/jbcom/python-lifecyclelogging/commit/d7fe3d1d78d1417f9c537e9a4b59e321a59117fb))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`3347378`](https://github.com/jbcom/python-lifecyclelogging/commit/33473781396813bd3bdeeb6e1f7e3100371fb52d))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`6c2f0a9`](https://github.com/jbcom/python-lifecyclelogging/commit/6c2f0a9806b268db864ad23bbf38cb666aee0fcd))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`8e0936a`](https://github.com/jbcom/python-lifecyclelogging/commit/8e0936af8ee6c97ed2acf7be046b9d8c318ea524))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`c80fe44`](https://github.com/jbcom/python-lifecyclelogging/commit/c80fe44a501bcbbe8efb102efeaf18b1075dc4cb))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`be40250`](https://github.com/jbcom/python-lifecyclelogging/commit/be40250e8e84eac16ab62c3e5b392ce0222a9c4d))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`6801994`](https://github.com/jbcom/python-lifecyclelogging/commit/68019943ba32df51dea554e775c720c518298a26))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`e2a7e4f`](https://github.com/jbcom/python-lifecyclelogging/commit/e2a7e4ff767c2c919282e4c1a6e3aed2011c8fdd))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`19ead44`](https://github.com/jbcom/python-lifecyclelogging/commit/19ead441bb569b87ef1980e9e9bb0360e1c7b3a3))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`c547cb2`](https://github.com/jbcom/python-lifecyclelogging/commit/c547cb225d325ea43a0cadee342d82a77818719a))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`c6bd353`](https://github.com/jbcom/python-lifecyclelogging/commit/c6bd353f5d4aa9027d11f5043baf33f8d8fd67e3))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`7fa25df`](https://github.com/jbcom/python-lifecyclelogging/commit/7fa25df8e3e3f68c4336848fca7e827a73a113c3))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`b454029`](https://github.com/jbcom/python-lifecyclelogging/commit/b454029362f10ee7827f320e84e8ad72e4667550))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`a117027`](https://github.com/jbcom/python-lifecyclelogging/commit/a117027cc0f77d754d05c0995f2255d7d9248778))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`0e67dcc`](https://github.com/jbcom/python-lifecyclelogging/commit/0e67dcc645c3e46bff732bf7b716390cc50d1402))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`b503981`](https://github.com/jbcom/python-lifecyclelogging/commit/b503981b6ea6e05ecb01ec4c6c4ca2c7d59b7687))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`34df44a`](https://github.com/jbcom/python-lifecyclelogging/commit/34df44a0dfe6aabd70d153ded789e5ef1055c1c9))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`f9e1d6c`](https://github.com/jbcom/python-lifecyclelogging/commit/f9e1d6c2acb8140e9dc89b7a31ce80ebc7bc387c))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`39872d8`](https://github.com/jbcom/python-lifecyclelogging/commit/39872d8a0d1e4f6c01aa8bed12eb787c8658c874))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`d12d5ce`](https://github.com/jbcom/python-lifecyclelogging/commit/d12d5cec40d47cf87aa8a50807dfbd8694e44af3))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`fdcbfd5`](https://github.com/jbcom/python-lifecyclelogging/commit/fdcbfd5a4d0fa15725319dbb86df4f74e206330e))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`1f47739`](https://github.com/jbcom/python-lifecyclelogging/commit/1f477391f5ea15ceae8164d8aa6430c84ee38bb2))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`47382f5`](https://github.com/jbcom/python-lifecyclelogging/commit/47382f52739d74d031c4e65c8df8094730575d4e))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`82f9136`](https://github.com/jbcom/python-lifecyclelogging/commit/82f9136758f83ea20749828d21675af2a2a528a6))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`795ece7`](https://github.com/jbcom/python-lifecyclelogging/commit/795ece7290c95bb41db629b79677d986d8c8e65d))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`92834c2`](https://github.com/jbcom/python-lifecyclelogging/commit/92834c2c7a9130dc7a592754dd96a177d1f0b1c2))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`9fe9744`](https://github.com/jbcom/python-lifecyclelogging/commit/9fe97446f6f3c6b4b50bf58b62db2ed6994df17e))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`52fd466`](https://github.com/jbcom/python-lifecyclelogging/commit/52fd46616cf352c793eecf5b408000cfc2894095))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`cb7b2ff`](https://github.com/jbcom/python-lifecyclelogging/commit/cb7b2ff40ffdbc210dfc74e941a88b336f9c31d6))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`3b7ac99`](https://github.com/jbcom/python-lifecyclelogging/commit/3b7ac994441ed9f9eb454ea20e7d456db8e8d959))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`3d464e6`](https://github.com/jbcom/python-lifecyclelogging/commit/3d464e689a4e8d44bb0714203be78c81c8ab3974))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`c0ceec1`](https://github.com/jbcom/python-lifecyclelogging/commit/c0ceec15b4e6ef4e55548782d8af1b0d348a8e35))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`dbc50b6`](https://github.com/jbcom/python-lifecyclelogging/commit/dbc50b6d2bf62657a6639ebbf11e3228de4149a7))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`88a306f`](https://github.com/jbcom/python-lifecyclelogging/commit/88a306f030e2c577281480e7ecde28671a64ec42))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`3d410e6`](https://github.com/jbcom/python-lifecyclelogging/commit/3d410e6a376b8b0051bac70ea9b2f01a5aba8e79))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`a8668e6`](https://github.com/jbcom/python-lifecyclelogging/commit/a8668e63ed45e94a380ddab343a9ebb970825048))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`fa361b7`](https://github.com/jbcom/python-lifecyclelogging/commit/fa361b732fec0b003d2d677b12eaaf3ffdbded9c))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`d73cb4d`](https://github.com/jbcom/python-lifecyclelogging/commit/d73cb4db0c1b95b73685af9f5e3ab476b99da2bc))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`b7b2a7e`](https://github.com/jbcom/python-lifecyclelogging/commit/b7b2a7eec5b9bf6236d77d5ea13feeced711f735))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`657a6d1`](https://github.com/jbcom/python-lifecyclelogging/commit/657a6d159b51a3ba3846ba12d10d06a770996611))

- **sync**: Synced local '.github/workflows/' with remote
  'repository-files/always-sync/.github/workflows/'
  ([`0e829f1`](https://github.com/jbcom/python-lifecyclelogging/commit/0e829f102a6746ae951d68fbe9a1bce9e5b7cb7f))

- **sync**: Synced local '.github/workflows/' with remote
  'repository-files/always-sync/.github/workflows/'
  ([`47e0e80`](https://github.com/jbcom/python-lifecyclelogging/commit/47e0e806ead9caa5579c07554606c2dc935ce8f0))

- **sync**: Synced local '.github/workflows/' with remote
  'repository-files/always-sync/.github/workflows/'
  ([`4858663`](https://github.com/jbcom/python-lifecyclelogging/commit/48586636539ce3d1b82b5b0338fd62dc98aaa262))

- **sync**: Synced local '.github/workflows/' with remote
  'repository-files/always-sync/.github/workflows/'
  ([`13e8b42`](https://github.com/jbcom/python-lifecyclelogging/commit/13e8b4207f5dacbdd2883d7dc0207cf24b981516))

### Features

- **settings**: Add ecosystem-specific settings with Ruff linter
  ([`34cc6b1`](https://github.com/jbcom/python-lifecyclelogging/commit/34cc6b13897d18a7e59660af20087dd38ac2b95e))


## v0.2.1 (2025-12-07)

### Bug Fixes

- Restore working Dockerfile with Go 1.25.3 and correct process-compose install
  ([`eef6fda`](https://github.com/jbcom/lifecyclelogging/commit/eef6fdaadd8f5ec7073b05d53933a511ee4fbb02))


## v0.2.0 (2025-12-07)

### Bug Fixes

- Properly sanitize only filename, not directory path
  ([#28](https://github.com/jbcom/lifecyclelogging/pull/28),
  [`0707a30`](https://github.com/jbcom/lifecyclelogging/commit/0707a30f528578adda7c562c7a9aa926464110ac))

- Resolve CI failures from linting and test issues
  ([#28](https://github.com/jbcom/lifecyclelogging/pull/28),
  [`0707a30`](https://github.com/jbcom/lifecyclelogging/commit/0707a30f528578adda7c562c7a9aa926464110ac))

- Use absolute imports and fix lint issues
  ([#46](https://github.com/jbcom/lifecyclelogging/pull/46),
  [`3ce738d`](https://github.com/jbcom/lifecyclelogging/commit/3ce738d0ecb133c8ed52283209cc25aced10e2c4))

### Chores

- Remove .DS_Store files and add to .gitignore
  ([#28](https://github.com/jbcom/lifecyclelogging/pull/28),
  [`0707a30`](https://github.com/jbcom/lifecyclelogging/commit/0707a30f528578adda7c562c7a9aa926464110ac))

- **config**: Migrate config renovate.json
  ([#27](https://github.com/jbcom/lifecyclelogging/pull/27),
  [`14618ed`](https://github.com/jbcom/lifecyclelogging/commit/14618edcc060b17fcdb91b5deb6c8a8b901309e9))

- **deps**: Update actions/checkout action to v6
  ([#31](https://github.com/jbcom/lifecyclelogging/pull/31),
  [`9e497d6`](https://github.com/jbcom/lifecyclelogging/commit/9e497d62b7ceb795df2314e75c3cca026676be9a))

- **deps**: Update actions/checkout action to v6
  ([#25](https://github.com/jbcom/lifecyclelogging/pull/25),
  [`d837604`](https://github.com/jbcom/lifecyclelogging/commit/d8376047f1382f7365b142dbdf972e1ddb83d7c4))

- **deps**: Update actions/checkout action to v6
  ([#26](https://github.com/jbcom/lifecyclelogging/pull/26),
  [`e11bddd`](https://github.com/jbcom/lifecyclelogging/commit/e11bdddfa73e78ba8cb43cbd2f405269750e559f))

- **deps**: Update actions/checkout to v6 ([#25](https://github.com/jbcom/lifecyclelogging/pull/25),
  [`d837604`](https://github.com/jbcom/lifecyclelogging/commit/d8376047f1382f7365b142dbdf972e1ddb83d7c4))

- **deps**: Update actions/download-artifact action to v6
  ([#32](https://github.com/jbcom/lifecyclelogging/pull/32),
  [`07246e3`](https://github.com/jbcom/lifecyclelogging/commit/07246e3e2c6fbb4415e358ae1997a6d7044cafa8))

### Code Style

- Format handlers.py with black ([#28](https://github.com/jbcom/lifecyclelogging/pull/28),
  [`0707a30`](https://github.com/jbcom/lifecyclelogging/commit/0707a30f528578adda7c562c7a9aa926464110ac))

### Documentation

- Add AI agent guidelines and fix workflow conflicts
  ([#28](https://github.com/jbcom/lifecyclelogging/pull/28),
  [`0707a30`](https://github.com/jbcom/lifecyclelogging/commit/0707a30f528578adda7c562c7a9aa926464110ac))

### Features

- Leverage extended-data-types 5.2.0 for improved data handling
  ([#28](https://github.com/jbcom/lifecyclelogging/pull/28),
  [`0707a30`](https://github.com/jbcom/lifecyclelogging/commit/0707a30f528578adda7c562c7a9aa926464110ac))

- Migrate from monorepo to standalone package
  ([`92645c9`](https://github.com/jbcom/lifecyclelogging/commit/92645c93d84c4169c853e0f0bf5fe8fddc564cac))

- Upgrade to extended-data-types 5.2.0 and unified CI workflow
  ([#28](https://github.com/jbcom/lifecyclelogging/pull/28),
  [`0707a30`](https://github.com/jbcom/lifecyclelogging/commit/0707a30f528578adda7c562c7a9aa926464110ac))

### Refactoring

- Use absolute imports and add future annotations
  ([`e413f71`](https://github.com/jbcom/lifecyclelogging/commit/e413f7190dd97adc24eda75f4634d414d863791b))


## v202511.8.0 (2025-12-01)

### Documentation

- Create handoff for documentation overhaul
  ([#298](https://github.com/jbcom/jbcom-control-center/pull/298),
  [`4481bd2`](https://github.com/jbcom/jbcom-control-center/commit/4481bd27d6cd665cecc678acf784395c9986d930))

### Features

- Consolidate control center into unified control surface
  ([#295](https://github.com/jbcom/jbcom-control-center/pull/295),
  [`2c207ca`](https://github.com/jbcom/jbcom-control-center/commit/2c207caf5129184d178bfbff81945eb74988d629))


## v202511.7.0 (2025-12-01)

### Bug Fixes

- Update default model to claude-4-opus for Cursor compatibility
  ([#290](https://github.com/jbcom/jbcom-control-center/pull/290),
  [`9b81310`](https://github.com/jbcom/jbcom-control-center/commit/9b8131073c73107bd07c078801897acc5bbe8370))

### Documentation

- Align instructions with SemVer ([#263](https://github.com/jbcom/jbcom-control-center/pull/263),
  [`1d3d830`](https://github.com/jbcom/jbcom-control-center/commit/1d3d83033aaf2d0b16b7355559dbda208ee20dd7))

- Fix test instructions + repository health audit
  ([#275](https://github.com/jbcom/jbcom-control-center/pull/275),
  [`f9617cb`](https://github.com/jbcom/jbcom-control-center/commit/f9617cb8db0216c0f1fc10310e441ef447373aba))

### Features

- Unified agentic-control package with intelligent multi-org token switching
  ([#285](https://github.com/jbcom/jbcom-control-center/pull/285),
  [`0baced8`](https://github.com/jbcom/jbcom-control-center/commit/0baced883a8ae0c6909e6a631d5de69c7c9d8e21))


## v202511.6.0 (2025-11-29)

### Documentation

- Add FSC Control Center counterparty awareness
  ([#220](https://github.com/jbcom/jbcom-control-center/pull/220),
  [`a0e9ff9`](https://github.com/jbcom/jbcom-control-center/commit/a0e9ff96aefd947266753fb8e8f460463eb8dc8f))

- Update orchestration with completion status
  ([`f0737b5`](https://github.com/jbcom/jbcom-control-center/commit/f0737b52b44300f8ba7d376fc1a32da2ee7035de))

- Update PR_PLAN with agent fleet assignments
  ([`80845b1`](https://github.com/jbcom/jbcom-control-center/commit/80845b1531f900a81786489ce77c030429d4c362))

- Update wiki and orchestration for architectural evolution
  ([`8ad2f99`](https://github.com/jbcom/jbcom-control-center/commit/8ad2f997f41dffb1910c07398a779d1d7c2a9302))

### Features

- Add python-terraform-bridge package
  ([#248](https://github.com/jbcom/jbcom-control-center/pull/248),
  [`2d3cd6f`](https://github.com/jbcom/jbcom-control-center/commit/2d3cd6f05502fe02c0a0178829d871a955ae6b35))


## v202511.5.0 (2025-11-29)

### Features

- Add AWS Secrets Manager create, update, delete operations
  ([#236](https://github.com/jbcom/jbcom-control-center/pull/236),
  [`76b8243`](https://github.com/jbcom/jbcom-control-center/commit/76b82433cc4ff8e2842e0ea2313fba4bfedbc19c))

- Add filtering and transformation to Google user/group listing
  ([#241](https://github.com/jbcom/jbcom-control-center/pull/241),
  [`33feb1c`](https://github.com/jbcom/jbcom-control-center/commit/33feb1ca1ba61df049879eaeb75e46b112542560))

- Add Slack usergroup and conversation listing
  ([#237](https://github.com/jbcom/jbcom-control-center/pull/237),
  [`ef1aea7`](https://github.com/jbcom/jbcom-control-center/commit/ef1aea7eb469df998e9d0fe93722b6af0af8267b))

- Add Vault AWS IAM role helpers ([#239](https://github.com/jbcom/jbcom-control-center/pull/239),
  [`bc7c8aa`](https://github.com/jbcom/jbcom-control-center/commit/bc7c8aa2c9b27dac2748e038ceff34a4b0f5572d))


## v202511.4.0 (2025-11-29)

### Features

- Add FSC fleet coordination support
  ([`7a046b6`](https://github.com/jbcom/jbcom-control-center/commit/7a046b6578cd2216542e893d61ecd501d8305a8c))


## v202511.3.0 (2025-11-28)

- Initial Release
