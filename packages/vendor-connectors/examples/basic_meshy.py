#!/usr/bin/env python3
"""Example: Meshy AI 3D Generation.

This example demonstrates how to use the Meshy connector for AI-powered
3D asset generation.

Requirements:
    pip install vendor-connectors[meshy]

Environment Variables:
    MESHY_API_KEY: Your Meshy API key (get one at https://meshy.ai)
"""

from __future__ import annotations

import os
import sys
import time


def main() -> int:
    """Demonstrate Meshy AI 3D generation."""
    # Check for required environment variables
    if not os.getenv("MESHY_API_KEY"):
        return 1

    # Import Meshy modules
    from vendor_connectors.meshy import text3d

    # Generate a simple 3D model
    prompt = "a medieval sword with ornate handle"

    try:
        # Start the generation (preview mode for faster results)
        result = text3d.generate(
            prompt=prompt,
            art_style="realistic",
            mode="preview",  # Use 'refine' for higher quality
        )

        # Poll for completion
        while result.status in ("PENDING", "IN_PROGRESS"):
            time.sleep(5)
            result = text3d.get(result.id)

        if result.status == "SUCCEEDED" or hasattr(result, "task_error"):
            pass

    except Exception:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
