#!/usr/bin/env python3
"""Example: Basic Google Cloud Connector usage.

This example demonstrates how to use the Google Cloud connector to interact
with Google Workspace and Cloud Platform.

Requirements:
    pip install vendor-connectors[google]

Environment Variables:
    GOOGLE_SERVICE_ACCOUNT: JSON service account credentials
    GOOGLE_DOMAIN: Google Workspace domain (for Workspace operations)
"""

from __future__ import annotations

import os
import sys


def main() -> int:
    """Demonstrate Google connector usage."""
    # Check for required environment variables
    if not os.getenv("GOOGLE_SERVICE_ACCOUNT"):
        return 1

    try:
        from vendor_connectors import GoogleConnector, GoogleConnectorFull
    except ImportError:
        return 1

    # Basic connector
    GoogleConnector()

    # Full connector with all operations
    full_connector = GoogleConnectorFull()

    # List projects
    try:
        projects = full_connector.list_projects()
        for _project in projects[:5]:
            pass
        if len(projects) > 5:
            pass
    except Exception:
        pass

    # List workspace users (if domain configured)
    if os.getenv("GOOGLE_DOMAIN"):
        try:
            users = full_connector.list_users()
            for user in users[:5]:
                user.get("primaryEmail", "Unknown")
            if len(users) > 5:
                pass
        except Exception:
            pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
