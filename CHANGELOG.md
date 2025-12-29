# CHANGELOG

<!-- version list -->

## v5.4.0 (2025-12-29)

### Bug Fixes

- Avoid broken pipe with large diffs
  ([`bc640ed`](https://github.com/extended-data-library/core/commit/bc640ede20a2847266840c56a63a36ddeb07eb70))

- Ecosystem-reviewer gracefully handles missing Jules API key
  ([`5138544`](https://github.com/extended-data-library/core/commit/5138544eba5027d4d595eb1390b499dd8f82d348))

- Use direct Ollama API for more reliable reviews
  ([`cbe67e0`](https://github.com/extended-data-library/core/commit/cbe67e04ba66241a3e81d90ec87cff5efd726e17))

- **ci**: Disable build in semantic-release action, build in CI
  ([#22](https://github.com/extended-data-library/core/pull/22),
  [`8526635`](https://github.com/extended-data-library/core/commit/85266353077bb8ef8b8b67bc7fe7f2c01ed01ad5))

- **ci**: Fix invalid package name and implement MCP server core
  ([#24](https://github.com/extended-data-library/core/pull/24),
  [`d235959`](https://github.com/extended-data-library/core/commit/d235959bc830ab9ec9d69b3d2e01902d7bfa2227))

- **ci**: Fix lint errors and add mcp to test dependencies
  ([#26](https://github.com/extended-data-library/core/pull/26),
  [`60a0e04`](https://github.com/extended-data-library/core/commit/60a0e0408a729b1d2d1368c78ab75ca6d35fcb13))

- **ci**: Fix python 3.9 compatibility for MCP server and CI
  ([#27](https://github.com/extended-data-library/core/pull/27),
  [`07a5b30`](https://github.com/extended-data-library/core/commit/07a5b30ab6bcfc8cc7aa672496b62cc99c0bb7e6))

- **ci**: Fix ruff formatting in tests/test_mcp_server.py
  ([#28](https://github.com/extended-data-library/core/pull/28),
  [`50d7d9b`](https://github.com/extended-data-library/core/commit/50d7d9b61b162e7ea5141b2344161d083fe1e4b8))

- **ci**: Rebuild packages after version bump and add jbcom branding to docs
  ([#16](https://github.com/extended-data-library/core/pull/16),
  [`273034a`](https://github.com/extended-data-library/core/commit/273034a8c6d0d940c266aca8b2831eefa7444ea7))

- **ci**: Use CI_GITHUB_TOKEN to bypass branch protection for releases
  ([#17](https://github.com/extended-data-library/core/pull/17),
  [`5651842`](https://github.com/extended-data-library/core/commit/565184205f8f8af657f70ca9149c65f295558468))

- **ci**: Use github.token instead of CI_GITHUB_TOKEN
  ([#20](https://github.com/extended-data-library/core/pull/20),
  [`00abfaf`](https://github.com/extended-data-library/core/commit/00abfaff2fe28e65caad5abab6560eeef4959d91))

- **ci**: Use softprops/action-gh-release for more reliable artifact uploads
  ([#22](https://github.com/extended-data-library/core/pull/22),
  [`8526635`](https://github.com/extended-data-library/core/commit/85266353077bb8ef8b8b67bc7fe7f2c01ed01ad5))

### Chores

- Remove deprecated claude-code.yml (replaced by ecosystem-reviewer)
  ([`37d21de`](https://github.com/extended-data-library/core/commit/37d21dec1d0a0853591be998ef2adac1af352361))

- Remove deprecated ollama-pr-review.yml (replaced by ecosystem-reviewer)
  ([`a77e544`](https://github.com/extended-data-library/core/commit/a77e5440b596a871eeabeb768215a252ca7248f5))

- Remove deprecated pr-review.yml (replaced by ecosystem-reviewer)
  ([`c6d904c`](https://github.com/extended-data-library/core/commit/c6d904c6a29d6badb2815b1c0909d494d68cf7b6))

- Remove docs workflow - migrated to centralized docs at extendeddata.dev
  ([#23](https://github.com/extended-data-library/core/pull/23),
  [`73f1fb2`](https://github.com/extended-data-library/core/commit/73f1fb2de82a08ec6ba0b1250710d78c543dc8b4))

- Remove ecosystem workflow (moved to control-center)
  ([`712e463`](https://github.com/extended-data-library/core/commit/712e463ecb61e1d0eb3d3bf4478e9073f127588e))

- Remove ecosystem workflow (moved to control-center)
  ([`39bf3ee`](https://github.com/extended-data-library/core/commit/39bf3ee6046f1c2a733bf15c744730c386f56c0a))

- Remove ecosystem workflow (moved to control-center)
  ([`e49de59`](https://github.com/extended-data-library/core/commit/e49de59ae02fdc93720dfe473923d2a0953e9806))

- Remove ecosystem workflow (moved to control-center)
  ([`f178902`](https://github.com/extended-data-library/core/commit/f178902f5adba6aaeba91fc16a2f44c1175bdca4))

- Remove ecosystem workflow (moved to control-center)
  ([`c34529c`](https://github.com/extended-data-library/core/commit/c34529c2fb4a7e7efd7c782eef9e8d0ceebfff89))

- Remove ecosystem workflow (moved to control-center)
  ([`246bdaa`](https://github.com/extended-data-library/core/commit/246bdaa46627c9bf36deb4233c6e8d4d930221e2))

- Remove redundant workflow (handled by control-center ecosystem)
  ([`7d7dc3a`](https://github.com/extended-data-library/core/commit/7d7dc3a4e278f942274a57a8e06fdc691625428a))

- Remove redundant workflow (handled by control-center ecosystem)
  ([`49bfcac`](https://github.com/extended-data-library/core/commit/49bfcac5f9823dbc8aa4a7433449de0b8d975325))

- Remove redundant workflow (handled by control-center ecosystem)
  ([`43fe030`](https://github.com/extended-data-library/core/commit/43fe030b2adb47250de9408da13318eb8cd74efe))

- Remove redundant workflow (handled by control-center ecosystem)
  ([`958c604`](https://github.com/extended-data-library/core/commit/958c6045e228122e2714577d6c1596ca59f2a1d5))

- Sync .github/actions/agentic-ci-resolution/action.yml from control-center
  ([`c646b8b`](https://github.com/extended-data-library/core/commit/c646b8b9a605f5747daabe09d31e8869ade7d7f5))

- Sync .github/actions/agentic-issue-triage/action.yml from control-center
  ([`e891493`](https://github.com/extended-data-library/core/commit/e89149307956a34e181e22d727df8bb1b0057760))

- Sync .github/actions/agentic-pr-review/action.yml from control-center
  ([`646be7e`](https://github.com/extended-data-library/core/commit/646be7e3401cdd26f628cafd390ed051e1ff3972))

- Sync ecosystem-curator.yml from control-center
  ([`24c88eb`](https://github.com/extended-data-library/core/commit/24c88eb8fc2673e688ec5aec9d3fc1404754a33b))

- Sync ecosystem-delegator.yml from control-center
  ([`fa45c0d`](https://github.com/extended-data-library/core/commit/fa45c0d7df63156d45583d4342ddedbf9b4838d4))

- Sync ecosystem-fixer.yml from control-center
  ([`5ac463a`](https://github.com/extended-data-library/core/commit/5ac463a208dbd9fd5fa155c265f4e8999b9e9c42))

- Sync ecosystem-harvester.yml from control-center
  ([`aaeee74`](https://github.com/extended-data-library/core/commit/aaeee74f8614d56a4f2a51618af6c08520aa0c9c))

- Sync ecosystem-reviewer.yml from control-center
  ([`03b4296`](https://github.com/extended-data-library/core/commit/03b4296ab614b7f0cf1208313db453cc342437fe))

- Sync ecosystem-sage.yml from control-center
  ([`4839b59`](https://github.com/extended-data-library/core/commit/4839b59eb71a5ddafc1fbdaed7bcb364cc5a9ff1))

- Sync scripts/ecosystem-curator.mjs from control-center
  ([`5269537`](https://github.com/extended-data-library/core/commit/5269537ac7903ee05ee3e6a909a7a10835152934))

- Sync scripts/ecosystem-harvester.mjs from control-center
  ([`3fe715e`](https://github.com/extended-data-library/core/commit/3fe715e3491b40e6c5989c97ead8f3ec0606d39d))

- Sync scripts/ecosystem-sage.mjs from control-center
  ([`1167a75`](https://github.com/extended-data-library/core/commit/1167a7508fed80b8d3f963b36a704ac5aad6d360))

### Documentation

- Final status report for 1.0 stabilization effort
  ([#19](https://github.com/extended-data-library/core/pull/19),
  [`dc85598`](https://github.com/extended-data-library/core/commit/dc85598cd42d1c4920c03780bca315cf497852e8))

- Update status with branch protection blocker analysis
  ([#21](https://github.com/extended-data-library/core/pull/21),
  [`b6527e2`](https://github.com/extended-data-library/core/commit/b6527e2af411f9acb81bac9b9c83030c6eabd2f9))

- **enterprise**: Align with multi-org documentation strategy and branding
  ([`d2c4dfb`](https://github.com/extended-data-library/core/commit/d2c4dfba9a29377384d1395abeb95d4753963f54))

- **enterprise**: Align with multi-org documentation strategy and branding
  ([`9bd8061`](https://github.com/extended-data-library/core/commit/9bd806161f713ea2176ec06f77dbb2139a10bce9))

### Features

- **ci**: Implement official python-semantic-release GitHub Action
  ([#21](https://github.com/extended-data-library/core/pull/21),
  [`b6527e2`](https://github.com/extended-data-library/core/commit/b6527e2af411f9acb81bac9b9c83030c6eabd2f9))

- **ci**: Overhaul release workflow with robust token handling
  ([#19](https://github.com/extended-data-library/core/pull/19),
  [`dc85598`](https://github.com/extended-data-library/core/commit/dc85598cd42d1c4920c03780bca315cf497852e8))

- **ecosystem**: Initialize foundation components and mcp server
  ([#25](https://github.com/extended-data-library/core/pull/25),
  [`ebe7062`](https://github.com/extended-data-library/core/commit/ebe7062777b00b1998c6828a8f2b2d1bfb9be323))


## v5.3.1 (2025-12-24)

### Bug Fixes

- **ci**: Skip AI reviews for dependabot PRs to prevent secret failures
  ([#11](https://github.com/extended-data-library/core/pull/11),
  [`5fbf897`](https://github.com/extended-data-library/core/commit/5fbf897abbcf86102c9dca40bb143fae313390fa))

### Chores

- Sync ruler configuration ([#11](https://github.com/extended-data-library/core/pull/11),
  [`5fbf897`](https://github.com/extended-data-library/core/commit/5fbf897abbcf86102c9dca40bb143fae313390fa))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`c92f1e7`](https://github.com/extended-data-library/core/commit/c92f1e71e6b906677b697a6ee39589281214ef37))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`3d59c98`](https://github.com/extended-data-library/core/commit/3d59c98bc860f354900b2581168e90ccb512aa9c))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`620a8b1`](https://github.com/extended-data-library/core/commit/620a8b189a9f83d2349e2f451db377acc7d2eaa7))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`76c02af`](https://github.com/extended-data-library/core/commit/76c02af6d3aa571c61c2c3ab1d1ce13445e929a8))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`60d4c07`](https://github.com/extended-data-library/core/commit/60d4c07f6dc4f8afe7c011c991863e8a0689445e))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`cfcfaf7`](https://github.com/extended-data-library/core/commit/cfcfaf77026914163832aa2e35dc55c91caa0652))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`d9ce62e`](https://github.com/extended-data-library/core/commit/d9ce62e42d1e1e52552a7dbfabd310f742de2edf))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`a94db7c`](https://github.com/extended-data-library/core/commit/a94db7c934c1cb561a5e17ec7f8193933b58954b))

- **sync**: Synced local '.github/settings.yml' with remote
  'repository-files/always-sync/.github/settings.yml'
  ([`0d22734`](https://github.com/extended-data-library/core/commit/0d227342a7c4d6e7d854d07df915e1877b09a88e))

### Continuous Integration

- Bump actions/checkout from 4 to 6 ([#13](https://github.com/extended-data-library/core/pull/13),
  [`00b2206`](https://github.com/extended-data-library/core/commit/00b22066298132b59f77c7537b64768bae7d0235))

- Bump actions/download-artifact from 4 to 7
  ([#11](https://github.com/extended-data-library/core/pull/11),
  [`5fbf897`](https://github.com/extended-data-library/core/commit/5fbf897abbcf86102c9dca40bb143fae313390fa))

- Bump actions/setup-python from 5 to 6 ([#9](https://github.com/extended-data-library/core/pull/9),
  [`40f6644`](https://github.com/extended-data-library/core/commit/40f6644a74c5bb0377f9b59c47f2342f9a37a722))

- Bump actions/upload-pages-artifact from 3 to 4
  ([#12](https://github.com/extended-data-library/core/pull/12),
  [`47a290e`](https://github.com/extended-data-library/core/commit/47a290ed4f4e749ca1022c28ebb4461243e36078))

### Documentation

- Fix documentation placeholders and improve deploy workflow
  ([#15](https://github.com/extended-data-library/core/pull/15),
  [`5577d94`](https://github.com/extended-data-library/core/commit/5577d94c3c7b2872f04bb78dc7ea9938e21bbb3f))

- Update memory bank for fix/issue-6 ([#15](https://github.com/extended-data-library/core/pull/15),
  [`5577d94`](https://github.com/extended-data-library/core/commit/5577d94c3c7b2872f04bb78dc7ea9938e21bbb3f))


## v5.3.0 (2025-12-23)

### Bug Fixes

- **edt**: Remove inappropriate ecosystem-specific imports from public API
  ([#64](https://github.com/jbcom/python-extended-data-types/pull/64),
  [`57f8fbd`](https://github.com/jbcom/python-extended-data-types/commit/57f8fbd5ed8110dfac2c73cd870e576f133d9780))

### Chores

- Centralize AI agent instructions with Ruler
  ([#64](https://github.com/jbcom/python-extended-data-types/pull/64),
  [`57f8fbd`](https://github.com/jbcom/python-extended-data-types/commit/57f8fbd5ed8110dfac2c73cd870e576f133d9780))

- Initial .cursor/environment.json from jbcom-control-center
  ([`c2ac3ef`](https://github.com/jbcom/python-extended-data-types/commit/c2ac3ef28190e5a20b7efae3f69da1dd9d7727f2))

- Initial .github/workflows/docs.yml from jbcom-control-center
  ([`67d3796`](https://github.com/jbcom/python-extended-data-types/commit/67d379668c04b81b519f1bfe7ff2cdff1d1d79c6))

- Initial docs/.nojekyll from jbcom-control-center
  ([`094bc9f`](https://github.com/jbcom/python-extended-data-types/commit/094bc9ff977bef878d355d5c32d277bcccc98a37))

- Initial docs/_static/custom.css from jbcom-control-center
  ([`7342c5d`](https://github.com/jbcom/python-extended-data-types/commit/7342c5da4b38fdeb658aa6c49f5ef40c116afc21))

- Initial docs/_templates/.gitkeep from jbcom-control-center
  ([`8a8b7f3`](https://github.com/jbcom/python-extended-data-types/commit/8a8b7f36445918bc703348325f0c55dc37073a0c))

- Initial docs/api/index.rst from jbcom-control-center
  ([`6ea4586`](https://github.com/jbcom/python-extended-data-types/commit/6ea45861f59b28a546f8fa7053031ea462e9cb77))

- Initial docs/api/modules.rst from jbcom-control-center
  ([`124f796`](https://github.com/jbcom/python-extended-data-types/commit/124f796b952d45f6cb1f49c06effb80537ffc301))

- Initial docs/conf.py from jbcom-control-center
  ([`74d8605`](https://github.com/jbcom/python-extended-data-types/commit/74d8605ba6685bb854dd0566aa3879e2838b4415))

- Initial docs/development/contributing.md from jbcom-control-center
  ([`7fbd1a6`](https://github.com/jbcom/python-extended-data-types/commit/7fbd1a639b42092ba51a8c8a75b28d74edb430c6))

- Initial docs/getting-started/installation.md from jbcom-control-center
  ([`0de6c35`](https://github.com/jbcom/python-extended-data-types/commit/0de6c35b5a788c1ee5264752c91f45497bb581f5))

- Initial docs/getting-started/quickstart.md from jbcom-control-center
  ([`96a506e`](https://github.com/jbcom/python-extended-data-types/commit/96a506eada27a93c7345c0044d72dc3c5d6508a3))

- Initial docs/index.rst from jbcom-control-center
  ([`3d0f397`](https://github.com/jbcom/python-extended-data-types/commit/3d0f397a5e92a642c982161b65c3490ffbd06007))

- Initial docs/Makefile from jbcom-control-center
  ([`0a62e9f`](https://github.com/jbcom/python-extended-data-types/commit/0a62e9fd6a24472f3cc19c4d26bc79e65f4130b3))

- Simplify dependabot config - direct push mode (no PRs)
  ([`6f19604`](https://github.com/jbcom/python-extended-data-types/commit/6f196048d70c0352e85ca71569c4350db7d66c3b))

- Sync .cursor/rules/00-fundamentals.mdc from jbcom-control-center
  ([`afae361`](https://github.com/jbcom/python-extended-data-types/commit/afae36116e26ca15d3c46466f6a85ccb921033d8))

- Sync .cursor/rules/00-fundamentals.mdc from jbcom-control-center
  ([`b5c57b4`](https://github.com/jbcom/python-extended-data-types/commit/b5c57b47a646c512e8a314937f3973134d5ec41b))

- Sync .cursor/rules/01-pr-workflow.mdc from jbcom-control-center
  ([`3eb5e04`](https://github.com/jbcom/python-extended-data-types/commit/3eb5e0470a734a0262c56ac316d7dcd2fa94ef03))

- Sync .cursor/rules/02-memory-bank.mdc from jbcom-control-center
  ([`d7b41bd`](https://github.com/jbcom/python-extended-data-types/commit/d7b41bd8041ec74cf9d9228af9aa99a70c3d1924))

- Sync .cursor/rules/02-memory-bank.mdc from jbcom-control-center
  ([`5de60e9`](https://github.com/jbcom/python-extended-data-types/commit/5de60e90f3dd0394a633e89e0f5cd48dc5e9baf2))

- Sync .cursor/rules/ci.mdc from jbcom-control-center
  ([`bd96b19`](https://github.com/jbcom/python-extended-data-types/commit/bd96b19ad582bd6477f718be41d748a6914c39b7))

- Sync .cursor/rules/python.mdc from jbcom-control-center
  ([`dc6c6f1`](https://github.com/jbcom/python-extended-data-types/commit/dc6c6f1e16d1b4ea2ed140ee16b323f7295479a7))

- Sync .cursor/rules/releases.mdc from jbcom-control-center
  ([`d8c1ee4`](https://github.com/jbcom/python-extended-data-types/commit/d8c1ee4ad2a0b3e27cd9ba647ce625e2370d6953))

- Sync .cursor/rules/releases.mdc from jbcom-control-center
  ([`dddecc9`](https://github.com/jbcom/python-extended-data-types/commit/dddecc99e247dd6733a8ec2470b1b6d12c15d5b7))

- Sync .github/workflows/claude-code.yml from jbcom-control-center
  ([`02b71a2`](https://github.com/jbcom/python-extended-data-types/commit/02b71a2944200bbc9631a354aab398ae4a7ec326))

- Sync .github/workflows/claude-code.yml from jbcom-control-center
  ([`72e2e67`](https://github.com/jbcom/python-extended-data-types/commit/72e2e67441de46f6d9b4ad10e521542b28c1144b))

- Sync files from jbcom/.github ([#4](https://github.com/jbcom/python-extended-data-types/pull/4),
  [`d4132f5`](https://github.com/jbcom/python-extended-data-types/commit/d4132f51df75f010a0f864b7458e1bfffde9f20a))

- Sync settings.yml from control-center
  ([`42a8811`](https://github.com/jbcom/python-extended-data-types/commit/42a8811bcb9184527c50f035914fa7ed6781d8e5))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`0978536`](https://github.com/jbcom/python-extended-data-types/commit/0978536a0742d38237415fb287eb00c55a5e463f))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`1eb6e76`](https://github.com/jbcom/python-extended-data-types/commit/1eb6e7692398c2ac677b77aaeec949c9bbb5dc0d))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`374215a`](https://github.com/jbcom/python-extended-data-types/commit/374215aea8dd9a3ea5a8479bce7ebfbe202f32ec))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`803145e`](https://github.com/jbcom/python-extended-data-types/commit/803145ec9a2e267bd94c4c50ed84e49aeab3e32e))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`eced1b6`](https://github.com/jbcom/python-extended-data-types/commit/eced1b61761642be7d143beb1d19fb9756408b77))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`340e5d0`](https://github.com/jbcom/python-extended-data-types/commit/340e5d008392855d5d1e807d4bb533117221af90))

- **init**: Created local '.cursor/Dockerfile' from remote
  'repository-files/initial-only/.cursor/Dockerfile'
  ([`0183b10`](https://github.com/jbcom/python-extended-data-types/commit/0183b1081796ea981ccf4602b363b64c14f859ab))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`6385103`](https://github.com/jbcom/python-extended-data-types/commit/638510338be0353c62bff5c330e3b07b0d13ba54))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`0fda5c0`](https://github.com/jbcom/python-extended-data-types/commit/0fda5c0ab7419773371b000a9c2b89ec8ccedaab))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`465b343`](https://github.com/jbcom/python-extended-data-types/commit/465b343ea4e276275dbb666a4c25f60d430515c0))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`10bf6c8`](https://github.com/jbcom/python-extended-data-types/commit/10bf6c8655f79fe66d88a29f8edf5109e9645959))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`41290ee`](https://github.com/jbcom/python-extended-data-types/commit/41290eeb09acb23efd302f6112fbe67eca351d03))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`e7d36b5`](https://github.com/jbcom/python-extended-data-types/commit/e7d36b52ba6d089601ec211af74cde60b8d9dcdb))

- **init**: Created local '.cursor/environment.json' from remote
  'repository-files/initial-only/.cursor/environment.json'
  ([`a37730f`](https://github.com/jbcom/python-extended-data-types/commit/a37730f5f333b3b3c003bd0cecb517db2cd0ad35))

- **init**: Created local 'CLAUDE.md' from remote 'repository-files/initial-only/CLAUDE.md'
  ([`5c909a9`](https://github.com/jbcom/python-extended-data-types/commit/5c909a976817528783844f09fe585a3d83babdc7))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`fcc5379`](https://github.com/jbcom/python-extended-data-types/commit/fcc537916ae5e9ff9e1ecf0118d1ac2a80530c17))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`620ff0c`](https://github.com/jbcom/python-extended-data-types/commit/620ff0c56b0f83991693ec502ba54a0cbe09397f))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`fb4cb59`](https://github.com/jbcom/python-extended-data-types/commit/fb4cb595d68d8df2d368deab26af63215020fd89))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`9eadd53`](https://github.com/jbcom/python-extended-data-types/commit/9eadd53a9524319f6b56075881ea48206e37a392))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`597cb2e`](https://github.com/jbcom/python-extended-data-types/commit/597cb2e53cf42dfe2b9b823cb5cbc1cd9620bb61))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`0437777`](https://github.com/jbcom/python-extended-data-types/commit/0437777b6772242b7decc0ead6ab5a21d79b77e3))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`18c083b`](https://github.com/jbcom/python-extended-data-types/commit/18c083b09bb80b30cb24a7a24d9fbae1c419ed43))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`e7ace5e`](https://github.com/jbcom/python-extended-data-types/commit/e7ace5e6b2e0dcc3d033bc4feace55e751d60295))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`9c3ce68`](https://github.com/jbcom/python-extended-data-types/commit/9c3ce68307517b3b9bf65fa1573952cfb743089f))

- **sync**: Synced local '.cursor/' with remote 'repository-files/always-sync/.cursor/'
  ([`a24bf19`](https://github.com/jbcom/python-extended-data-types/commit/a24bf1986bc7b94830331e02c592f82315818cd7))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`18698a0`](https://github.com/jbcom/python-extended-data-types/commit/18698a017695699cb20ff23298fc934f2b78ccc9))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`5fe9ca6`](https://github.com/jbcom/python-extended-data-types/commit/5fe9ca629d854b65ad821e442a24297c195cff69))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`913c2d9`](https://github.com/jbcom/python-extended-data-types/commit/913c2d965ac30b9a9c5fe9e217f4918f1f22d0b0))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`3ab52c5`](https://github.com/jbcom/python-extended-data-types/commit/3ab52c5b7517ea69c6f1f0ea1056e3792173b430))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`c1bff9d`](https://github.com/jbcom/python-extended-data-types/commit/c1bff9d447698338b75cb7e02266d80e9980e941))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`d3e8412`](https://github.com/jbcom/python-extended-data-types/commit/d3e8412bd8fbecd80b70c869bfb3cdce33424353))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`847a1d5`](https://github.com/jbcom/python-extended-data-types/commit/847a1d5372f8a2294e7bab312c1b3bb9aec3906b))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`efec59e`](https://github.com/jbcom/python-extended-data-types/commit/efec59e77efdb544ef53356602c5b6cf314c5e9e))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`aa31dea`](https://github.com/jbcom/python-extended-data-types/commit/aa31dea2fa3514f9a540450ea3688bf9c3126b2a))

- **sync**: Synced local '.cursor/' with remote 'repository-files/python/.cursor/'
  ([`dae598c`](https://github.com/jbcom/python-extended-data-types/commit/dae598c8bed85874c36b304c50ff4020db7aa07d))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`8609e09`](https://github.com/jbcom/python-extended-data-types/commit/8609e09a327448939ad45e6bb499c71f77544427))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`216c982`](https://github.com/jbcom/python-extended-data-types/commit/216c982302f5c9641b70317a67b64fa4a9757670))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`cc0b8db`](https://github.com/jbcom/python-extended-data-types/commit/cc0b8dbd443463b15678c05e2800a27d933f5935))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`d5fbfb9`](https://github.com/jbcom/python-extended-data-types/commit/d5fbfb99f45305633172b12c92faf8a8684366d8))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`88311af`](https://github.com/jbcom/python-extended-data-types/commit/88311afbc91f004b8ee0c2a6c0912b560a6ea867))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`30363fb`](https://github.com/jbcom/python-extended-data-types/commit/30363fbb64acfead40ab718695d740e61ba1b70b))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`30f30c3`](https://github.com/jbcom/python-extended-data-types/commit/30f30c3bb04a953f2671276d664c5ac4d24b04e1))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/always-sync/.github/copilot-instructions.md'
  ([`9b9d01e`](https://github.com/jbcom/python-extended-data-types/commit/9b9d01e4c680dc1db0952d91a7419407fbb0bb06))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`39e83ec`](https://github.com/jbcom/python-extended-data-types/commit/39e83ec7f6783d1a4c4763f04ab6d89c07719e35))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`ff70e2a`](https://github.com/jbcom/python-extended-data-types/commit/ff70e2afe59c466e81b6243a0d04e1bc9abab908))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`c06aa95`](https://github.com/jbcom/python-extended-data-types/commit/c06aa95eda90835d28f41640e48e88ac31e30469))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`e1fc219`](https://github.com/jbcom/python-extended-data-types/commit/e1fc219188bbb6e5874b9e83c4f0f2d2d86e8c7a))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`d65390b`](https://github.com/jbcom/python-extended-data-types/commit/d65390b29be4879a64b700b33fa1639b3e149fdf))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`11119f3`](https://github.com/jbcom/python-extended-data-types/commit/11119f369b0c5dc9610eebab914f88f42aa1f59f))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`88afea3`](https://github.com/jbcom/python-extended-data-types/commit/88afea3f682b40e8421036f4214c4c26688438cd))

- **sync**: Synced local '.github/copilot-instructions.md' with remote
  'repository-files/python/.github/copilot-instructions.md'
  ([`7342ee6`](https://github.com/jbcom/python-extended-data-types/commit/7342ee62c4ca6f30946fe10738dfd612b22fbc55))

- **sync**: Synced local '.github/workflows/' with remote
  'repository-files/always-sync/.github/workflows/'
  ([`edfa9d1`](https://github.com/jbcom/python-extended-data-types/commit/edfa9d11990a1a64836636d16adbead73b3ffb5d))

- **sync**: Synced local '.github/workflows/' with remote
  'repository-files/always-sync/.github/workflows/'
  ([`9428030`](https://github.com/jbcom/python-extended-data-types/commit/9428030571dba79e0452996a2266b3877512e096))

- **sync**: Synced local '.github/workflows/' with remote
  'repository-files/always-sync/.github/workflows/'
  ([`ca53334`](https://github.com/jbcom/python-extended-data-types/commit/ca5333424a727b6b1402d83c9235f92ac43ee61e))

- **sync**: Synced local '.github/workflows/' with remote
  'repository-files/always-sync/.github/workflows/'
  ([`3b2006c`](https://github.com/jbcom/python-extended-data-types/commit/3b2006c2e9eee699cba5796e7fc9905e3db4fb43))

### Features

- **edt**: Add comprehensive ecosystem foundation specification
  ([#64](https://github.com/jbcom/python-extended-data-types/pull/64),
  [`57f8fbd`](https://github.com/jbcom/python-extended-data-types/commit/57f8fbd5ed8110dfac2c73cd870e576f133d9780))

- **edt**: Ecosystem foundation and Ruler AI agent setup
  ([#64](https://github.com/jbcom/python-extended-data-types/pull/64),
  [`57f8fbd`](https://github.com/jbcom/python-extended-data-types/commit/57f8fbd5ed8110dfac2c73cd870e576f133d9780))

- **settings**: Add ecosystem-specific settings with Ruff linter
  ([`c19a4f4`](https://github.com/jbcom/python-extended-data-types/commit/c19a4f46581622f61d8d72798983819d346a1814))


## v5.2.1 (2025-12-07)

### Bug Fixes

- Restore working Dockerfile with Go 1.25.3 and correct process-compose install
  ([`5bbafb9`](https://github.com/jbcom/extended-data-types/commit/5bbafb9e0473c3dd0423fd024ff5e24f5a3b413d))


## v5.2.0 (2025-12-07)

### Bug Fixes

- Add all mypy error codes for wrapt.ObjectProxy across Python versions
  ([#35](https://github.com/jbcom/extended-data-types/pull/35),
  [`5cf3c04`](https://github.com/jbcom/extended-data-types/commit/5cf3c0432722d482fe4e794008c463c23236f40f))

- Add all mypy error codes for wrapt.ObjectProxy across Python versions
  ([#36](https://github.com/jbcom/extended-data-types/pull/36),
  [`8801df8`](https://github.com/jbcom/extended-data-types/commit/8801df8882261842132bd9451036c25d3b4e00c6))

- Add ruamel.yaml dependency and bump to 5.1.2
  ([`36d88d5`](https://github.com/jbcom/extended-data-types/commit/36d88d5ae260434e2c7feb71fe2a24829244296f))

- Correct mypy type ignore comment for wrapt.ObjectProxy
  ([#34](https://github.com/jbcom/extended-data-types/pull/34),
  [`c3515c8`](https://github.com/jbcom/extended-data-types/commit/c3515c8d3618d0a86ea95f6f275a7398165cadb9))

- Use absolute imports throughout package
  ([#59](https://github.com/jbcom/extended-data-types/pull/59),
  [`fbacc7f`](https://github.com/jbcom/extended-data-types/commit/fbacc7f3bae78123c0609ab30f75e432e972bc58))

- Use mypy override for wrapt.ObjectProxy instead of inline ignores
  ([#36](https://github.com/jbcom/extended-data-types/pull/36),
  [`8801df8`](https://github.com/jbcom/extended-data-types/commit/8801df8882261842132bd9451036c25d3b4e00c6))

- Use TypeAlias for Python 3.9 mypy compatibility and fix ruff linting
  ([#35](https://github.com/jbcom/extended-data-types/pull/35),
  [`5cf3c04`](https://github.com/jbcom/extended-data-types/commit/5cf3c0432722d482fe4e794008c463c23236f40f))

- Use typing_extensions.TypeAlias and string literal for Python 3.9
  ([#35](https://github.com/jbcom/extended-data-types/pull/35),
  [`5cf3c04`](https://github.com/jbcom/extended-data-types/commit/5cf3c0432722d482fe4e794008c463c23236f40f))

### Chores

- Bump version to 5.1.1 ([#37](https://github.com/jbcom/extended-data-types/pull/37),
  [`bb42013`](https://github.com/jbcom/extended-data-types/commit/bb42013b74b77fb6221a3229f577915db429b8b6))

### Code Style

- Apply pre-commit formatting to set_version.py
  ([`74dab09`](https://github.com/jbcom/extended-data-types/commit/74dab0960695d59351724d0e14a109ce02825780))

### Documentation

- Clarify float support and exception handling in number transformations
  ([#45](https://github.com/jbcom/extended-data-types/pull/45),
  [`400c975`](https://github.com/jbcom/extended-data-types/commit/400c9755d16c7887e5c6fda7275dbf0d4140f1ff))

### Features

- Add release workflow and PR creation ([#41](https://github.com/jbcom/extended-data-types/pull/41),
  [`3fd24cb`](https://github.com/jbcom/extended-data-types/commit/3fd24cb0e9ba91924623d7b353b78e3a39a09f28))

- Add string and number transformation utilities
  ([#45](https://github.com/jbcom/extended-data-types/pull/45),
  [`400c975`](https://github.com/jbcom/extended-data-types/commit/400c9755d16c7887e5c6fda7275dbf0d4140f1ff))

- Improve export_utils with better format handling
  ([#45](https://github.com/jbcom/extended-data-types/pull/45),
  [`400c975`](https://github.com/jbcom/extended-data-types/commit/400c9755d16c7887e5c6fda7275dbf0d4140f1ff))

- Migrate from monorepo to standalone package
  ([`c4f24df`](https://github.com/jbcom/extended-data-types/commit/c4f24dfa10729a683390849c8ec83a8ee7d485cb))

- Update docs/conf.py version in sync with CalVer releases
  ([`74dab09`](https://github.com/jbcom/extended-data-types/commit/74dab0960695d59351724d0e14a109ce02825780))

### Refactoring

- Improve string, list, and map utilities
  ([#45](https://github.com/jbcom/extended-data-types/pull/45),
  [`400c975`](https://github.com/jbcom/extended-data-types/commit/400c9755d16c7887e5c6fda7275dbf0d4140f1ff))

- Use absolute imports and add future annotations
  ([`f2568eb`](https://github.com/jbcom/extended-data-types/commit/f2568eb60460ba58faeaa6e9fc02d923452fcd22))

### Testing

- Add comprehensive tests for transformation utilities
  ([#45](https://github.com/jbcom/extended-data-types/pull/45),
  [`400c975`](https://github.com/jbcom/extended-data-types/commit/400c9755d16c7887e5c6fda7275dbf0d4140f1ff))


## v202511.8.0 (2025-12-01)

### Features

- Consolidate control center into unified control surface
  ([#295](https://github.com/jbcom/jbcom-control-center/pull/295),
  [`2c207ca`](https://github.com/jbcom/jbcom-control-center/commit/2c207caf5129184d178bfbff81945eb74988d629))


## v202511.7.1 (2025-12-01)

### Bug Fixes

- Update default model to claude-4-opus for Cursor compatibility
  ([#290](https://github.com/jbcom/jbcom-control-center/pull/290),
  [`9b81310`](https://github.com/jbcom/jbcom-control-center/commit/9b8131073c73107bd07c078801897acc5bbe8370))


## v202511.7.0 (2025-12-01)

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


## v202511.4.0 (2025-11-28)

### Features

- Add FSC fleet coordination support
  ([`7a046b6`](https://github.com/jbcom/jbcom-control-center/commit/7a046b6578cd2216542e893d61ecd501d8305a8c))


## v202511.3.0 (2025-11-28)

- Initial Release
