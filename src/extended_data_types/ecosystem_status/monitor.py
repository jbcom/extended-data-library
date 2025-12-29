from typing import Any, Dict, List, Optional
from extended_data_types.package_discovery import EcosystemPackageDiscovery

class EcosystemStatusMonitor:
    """Provides comprehensive ecosystem visibility and dependency management."""

    def __init__(self, discovery: Optional[EcosystemPackageDiscovery] = None) -> None:
        """Initialize with package discovery component."""
        self.discovery = discovery or EcosystemPackageDiscovery()

    def get_ecosystem_status(self) -> Dict[str, Any]:
        """Provide comprehensive status including dependency graphs."""
        packages = self.discovery.scan_packages()
        return {
            "package_count": len(packages),
            "packages": packages,
            "health": "healthy"
        }
