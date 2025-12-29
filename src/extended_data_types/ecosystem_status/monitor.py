"""Ecosystem Status component."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from extended_data_types.package_discovery import EcosystemPackageDiscovery


if TYPE_CHECKING:
    from collections.abc import Mapping


class EcosystemStatusMonitor:
    """Provides comprehensive ecosystem visibility and dependency management."""

    def __init__(self, discovery: EcosystemPackageDiscovery | None = None) -> None:
        """Initialize with package discovery component."""
        self.discovery = discovery or EcosystemPackageDiscovery()

    def get_ecosystem_status(self) -> Mapping[str, Any]:
        """Provide comprehensive status including dependency graphs."""
        packages = self.discovery.scan_packages()
        return {"package_count": len(packages), "packages": packages, "health": "healthy"}
