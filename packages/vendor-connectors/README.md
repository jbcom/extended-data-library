# Vendor Connectors

*Universal vendor connectors with transparent secret management.*

[![CI Status](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml/badge.svg)](https://github.com/jbcom/extended-data-library/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/vendor-connectors.svg)](https://pypi.org/project/vendor-connectors/)
[![Python versions](https://img.shields.io/pypi/pyversions/vendor-connectors.svg)](https://pypi.org/project/vendor-connectors/)

Vendor Connectors provides standardized access to cloud providers, third-party services, and AI APIs. Each connector offers three interfaces: a direct Python API, LangChain-compatible tools for AI agents, and MCP servers for Claude Desktop and similar clients.

## Connectors

### AI/Agent
- **Anthropic** - Claude AI message generation, token counting, and model selection
- **Cursor** - Cursor Background Agent API for AI coding agent management

### Cloud Providers
- **AWS** - Boto3-based client with role assumption and retry logic
- **Google Cloud** - Workspace and Cloud Platform APIs with lazy credential loading

### Services
- **GitHub** - Repository management, GraphQL queries, and file operations
- **Slack** - Bot and app integrations with rate limiting
- **Vault** - HashiCorp Vault with Token and AppRole auth
- **Zoom** - Meeting and user management
- **Meshy** - AI 3D asset generation (text-to-3D, rigging, animation, retexture)

---

## Installation

```bash
pip install vendor-connectors
```

### Optional Extras

```bash
pip install vendor-connectors[webhooks]      # Meshy webhooks
pip install vendor-connectors[meshy-crewai]  # CrewAI-specific features
pip install vendor-connectors[meshy-mcp]     # Meshy MCP server
pip install vendor-connectors[all]           # Everything
```

## Quick Start

### Using VendorConnectors (Recommended)

```python
from vendor_connectors import VendorConnectors

vc = VendorConnectors()

# Cloud providers
s3 = vc.get_aws_client("s3")
google = vc.get_google_client()

# Services
github = vc.get_github_client(github_owner="myorg")
slack = vc.get_slack_client()
vault = vc.get_vault_client()

# AI
claude = vc.get_anthropic_client()
cursor = vc.get_cursor_client()
```

### Using Individual Connectors

```python
from vendor_connectors import AWSConnector, GithubConnector

aws = AWSConnector(execution_role_arn="arn:aws:iam::123456789012:role/MyRole")
s3 = aws.get_aws_client("s3")

github = GithubConnector(
    github_owner="myorg",
    github_repo="myrepo",
    github_token=os.getenv("GITHUB_TOKEN")
)
```

### Three Interfaces Per Connector

Every connector follows the same pattern:

```python
# 1. Direct Python API
from vendor_connectors.meshy import text3d

# 2. LangChain Tools (works with LangChain, CrewAI, LangGraph)
from vendor_connectors.meshy.tools import get_tools

# 3. MCP Server (for Claude Desktop, Cline, etc.)
from vendor_connectors.meshy.mcp import run_server
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Anthropic Claude API key |
| `CURSOR_API_KEY` | Cursor Background Agent API key |
| `AWS_*` | Standard AWS credentials |
| `EXECUTION_ROLE_ARN` | AWS role to assume |
| `GITHUB_TOKEN` | GitHub personal access token |
| `GOOGLE_SERVICE_ACCOUNT` | Google service account JSON |
| `SLACK_TOKEN` / `SLACK_BOT_TOKEN` | Slack tokens |
| `VAULT_ADDR` / `VAULT_TOKEN` | Vault connection |
| `MESHY_API_KEY` | Meshy AI API key |

---

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](https://github.com/jbcom/extended-data-library/blob/main/CONTRIBUTING.md) for more information.

## Project Links

- [**PyPI**](https://pypi.org/project/vendor-connectors/)
- [**GitHub**](https://github.com/jbcom/extended-data-library/tree/main/packages/vendor-connectors)
- [**Documentation**](https://extendeddata.dev)
- [**Changelog**](https://github.com/jbcom/extended-data-library/blob/main/packages/vendor-connectors/CHANGELOG.md)
