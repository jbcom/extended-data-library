#!/usr/bin/env python3
"""Example: Basic AWS Connector usage.

This example demonstrates how to use the AWS connector to interact with
AWS Organizations and S3.

Requirements:
    pip install vendor-connectors[aws]

Environment Variables:
    AWS_ACCESS_KEY_ID: AWS access key
    AWS_SECRET_ACCESS_KEY: AWS secret key
    AWS_DEFAULT_REGION: AWS region (optional, defaults to us-east-1)
"""

from __future__ import annotations

import os
import sys


def main() -> int:
    """Demonstrate AWS connector usage."""
    # Check for required environment variables
    if not os.getenv("AWS_ACCESS_KEY_ID"):
        return 1

    try:
        from vendor_connectors import AWSConnector, AWSConnectorFull
    except ImportError:
        return 1

    # Basic connector - just session management
    AWSConnector()

    # Full connector with all operations
    full_connector = AWSConnectorFull()

    # List S3 buckets
    try:
        buckets = full_connector.list_buckets()
        for _bucket in buckets[:5]:  # Show first 5
            pass
        if len(buckets) > 5:
            pass
    except Exception:
        pass

    # List organization accounts (if using Organizations)
    try:
        accounts = full_connector.get_accounts()
        for _account in accounts[:5]:
            pass
        if len(accounts) > 5:
            pass
    except Exception:
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
