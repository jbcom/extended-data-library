"""Package Discovery component."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import extended_data_types


class EcosystemPackageDiscovery:
    """Discovers and tracks jbcom Python packages in ~/src directory."""

    def __init__(self, base_path: Path | None = None) -> None:
        """Initialize package discovery with base scanning path."""
        if base_path is None:
            self.base_path = Path.home() / "src"
        else:
            self.base_path = base_path

    def scan_packages(self) -> list[dict[str, Any]]:
        """Scan for Python packages using existing get_parent_repository."""
        if not self.base_path.exists():
            return []

        packages = []
        for item in self.base_path.iterdir():
            if item.is_dir():
                pyproject = item / "pyproject.toml"
                if pyproject.exists():
                    repo = extended_data_types.get_parent_repository(item)
                    packages.append(
                        {
                            "name": item.name,
                            "path": str(item),
                            "is_git": repo is not None,
                            "repo_name": extended_data_types.get_repository_name(repo) if repo else None,
                        }
                    )
        return packages

    def get_package_dependencies(self, package_path: Path) -> dict[str, Any]:
        """Parse pyproject.toml to extract extended-data-types dependencies."""
        pyproject_path = package_path / "pyproject.toml"
        if not pyproject_path.exists():
            return {}

        try:
            content = extended_data_types.read_file(pyproject_path)
            assert isinstance(content, (str, bytes, bytearray, memoryview))
            data = extended_data_types.decode_toml(content)
            project = data.get("project", {})
            return {
                "name": project.get("name"),
                "version": project.get("version"),
                "dependencies": project.get("dependencies", []),
                "optional_dependencies": project.get("optional-dependencies", {}),
            }
        except (OSError, ValueError):
            return {}
