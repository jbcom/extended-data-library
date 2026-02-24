"""Ecosystem Status component."""

from __future__ import annotations

import re

from pathlib import Path
from typing import TYPE_CHECKING, Any

from extended_data_types.package_discovery import EcosystemPackageDiscovery


if TYPE_CHECKING:
    from collections.abc import Mapping


# Pattern to extract package name and version specifier from a dependency string.
# Matches forms like "some-package>=1.0,<2.0" or "some-package[extra]>=1.0".
_DEP_PATTERN = re.compile(r"^([A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?)(\[.*?\])?\s*(.*)")


def _parse_dep_spec(dep: str) -> tuple[str, str]:
    """Extract the normalized package name and version specifier from a dependency string.

    Args:
        dep: A PEP 508 dependency string, e.g. ``"requests>=2.0,<3.0"``.

    Returns:
        A tuple of (normalized_name, version_specifier). The name is lowercased
        with hyphens and underscores normalized to hyphens. The version specifier
        is the raw constraint string (may be empty).
    """
    match = _DEP_PATTERN.match(dep.strip())
    if not match:
        return dep.strip().lower(), ""
    name = re.sub(r"[-_.]+", "-", match.group(1)).lower()
    version_spec = match.group(4).strip()
    return name, version_spec


class EcosystemStatusMonitor:
    """Provides comprehensive ecosystem visibility and dependency management.

    Builds on ``EcosystemPackageDiscovery`` to deliver rich status information
    including per-package versions, inter-package dependency graphs, and
    cross-package version-consistency checks.
    """

    def __init__(self, discovery: EcosystemPackageDiscovery | None = None) -> None:
        """Initialize with package discovery component.

        Args:
            discovery: An existing discovery instance. If ``None``, a new
                ``EcosystemPackageDiscovery`` with default settings is created.
        """
        self.discovery = discovery or EcosystemPackageDiscovery()
        self._cached_ecosystem_names: set[str] | None = None

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get_package_details(
        self,
        package_info: dict[str, Any],
        ecosystem_names: set[str] | None = None,
    ) -> dict[str, Any]:
        """Enrich a scanned package entry with version and dependency metadata.

        Args:
            package_info: A single dict as returned by
                ``EcosystemPackageDiscovery.scan_packages()``.
            ecosystem_names: Pre-computed ecosystem names to avoid redundant
                scanning. If ``None``, names are fetched via
                ``_get_ecosystem_package_names()``.

        Returns:
            A dict containing the original fields plus ``version``,
            ``dependencies``, and ``ecosystem_dependencies``.
        """
        path_value = package_info.get("path")
        if not path_value:
            return {**package_info, "version": None, "dependencies": [], "ecosystem_dependencies": []}

        package_path = Path(path_value)
        dep_info = self.discovery.get_package_dependencies(package_path)

        version: str | None = dep_info.get("version")
        raw_deps: list[str] = dep_info.get("dependencies", [])

        if ecosystem_names is None:
            ecosystem_names = self._get_ecosystem_package_names()
        ecosystem_deps: list[str] = []
        for dep in raw_deps:
            dep_name, _ = _parse_dep_spec(dep)
            if dep_name in ecosystem_names:
                ecosystem_deps.append(dep)

        return {
            **package_info,
            "version": version,
            "dependencies": raw_deps,
            "ecosystem_dependencies": ecosystem_deps,
        }

    def _get_ecosystem_package_names(self) -> set[str]:
        """Return normalized names of all packages discovered in the ecosystem.

        Results are cached for the lifetime of the monitor instance to avoid
        repeated filesystem scans.

        Returns:
            A set of lowercased, hyphen-normalized package names.
        """
        if self._cached_ecosystem_names is not None:
            return self._cached_ecosystem_names

        packages = self.discovery.scan_packages()
        names: set[str] = set()
        for pkg in packages:
            path_value = pkg.get("path")
            if not path_value:
                continue
            package_path = Path(path_value)
            dep_info = self.discovery.get_package_dependencies(package_path)
            pkg_name = dep_info.get("name")
            if pkg_name:
                names.add(re.sub(r"[-_.]+", "-", pkg_name).lower())
        self._cached_ecosystem_names = names
        return names

    def _assess_health(
        self,
        package_details: list[dict[str, Any]],
        consistency: dict[str, Any],
    ) -> str:
        """Determine an overall health assessment for the ecosystem.

        Args:
            package_details: Enriched package info dicts.
            consistency: Output of ``check_version_consistency()``.

        Returns:
            One of ``"healthy"``, ``"degraded"``, or ``"unhealthy"``.
        """
        if not package_details:
            return "unknown"

        has_inconsistencies = bool(consistency.get("inconsistencies"))
        missing_versions = any(p.get("version") is None for p in package_details)

        if has_inconsistencies:
            return "degraded"
        if missing_versions:
            return "degraded"
        return "healthy"

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get_ecosystem_status(self) -> Mapping[str, Any]:
        """Provide comprehensive ecosystem status including dependency information.

        Returns:
            A mapping containing:
            - ``package_count``: Total number of discovered packages.
            - ``packages``: List of enriched package dicts (with version,
              dependencies, and ecosystem_dependencies).
            - ``dependency_graph``: Output of ``get_dependency_graph()``.
            - ``version_consistency``: Output of ``check_version_consistency()``.
            - ``health``: Overall health assessment string.
        """
        packages = self.discovery.scan_packages()
        eco_names = self._get_ecosystem_package_names()
        details = [self._get_package_details(pkg, eco_names) for pkg in packages]
        dep_graph = self.get_dependency_graph()
        consistency = self.check_version_consistency()
        health = self._assess_health(details, consistency)

        return {
            "package_count": len(details),
            "packages": details,
            "dependency_graph": dep_graph,
            "version_consistency": consistency,
            "health": health,
        }

    def get_dependency_graph(self) -> dict[str, list[str]]:
        """Build a mapping of each package to its ecosystem dependencies.

        Only dependencies that reference *other packages within the ecosystem*
        are included. External dependencies are omitted.

        Returns:
            A dict mapping normalized package names to lists of ecosystem
            package names they depend on.  For example::

                {
                    "lifecyclelogging": ["extended-data-types"],
                    "vendor-connectors": ["extended-data-types", "lifecyclelogging"],
                }
        """
        packages = self.discovery.scan_packages()
        ecosystem_names = self._get_ecosystem_package_names()
        graph: dict[str, list[str]] = {}

        for pkg in packages:
            path_value = pkg.get("path")
            if not path_value:
                continue
            package_path = Path(path_value)
            dep_info = self.discovery.get_package_dependencies(package_path)
            pkg_name = dep_info.get("name")
            if not pkg_name:
                continue

            normalized_name = re.sub(r"[-_.]+", "-", pkg_name).lower()
            raw_deps: list[str] = dep_info.get("dependencies", [])
            eco_deps: list[str] = []

            for dep in raw_deps:
                dep_name, _ = _parse_dep_spec(dep)
                if dep_name in ecosystem_names and dep_name != normalized_name:
                    eco_deps.append(dep_name)

            graph[normalized_name] = eco_deps

        return graph

    def check_version_consistency(self) -> dict[str, Any]:
        """Check whether cross-package dependency version specifiers are consistent.

        When multiple packages depend on the same ecosystem package, this method
        verifies that they all request the same version constraint. Mismatches
        are reported as inconsistencies.

        Returns:
            A dict with:
            - ``consistent`` (bool): ``True`` when no mismatches are found.
            - ``inconsistencies`` (list[dict]): Each entry describes a dependency
              whose version specifier differs across consumers. Fields:
              ``dependency``, ``specifications`` (list of
              ``{"package": ..., "version_spec": ...}``).
        """
        packages = self.discovery.scan_packages()
        ecosystem_names = self._get_ecosystem_package_names()

        # Collect version specs keyed by (consumer_name, dependency_name).
        dep_specs: dict[str, list[dict[str, str]]] = {}

        for pkg in packages:
            path_value = pkg.get("path")
            if not path_value:
                continue
            package_path = Path(path_value)
            dep_info = self.discovery.get_package_dependencies(package_path)
            pkg_name = dep_info.get("name")
            if not pkg_name:
                continue

            normalized_name = re.sub(r"[-_.]+", "-", pkg_name).lower()
            raw_deps: list[str] = dep_info.get("dependencies", [])

            for dep in raw_deps:
                dep_name, version_spec = _parse_dep_spec(dep)
                if dep_name not in ecosystem_names or dep_name == normalized_name:
                    continue
                dep_specs.setdefault(dep_name, []).append({"package": normalized_name, "version_spec": version_spec})

        inconsistencies: list[dict[str, Any]] = []
        for dep_name, specs in dep_specs.items():
            unique_versions = {s["version_spec"] for s in specs}
            if len(unique_versions) > 1:
                inconsistencies.append({"dependency": dep_name, "specifications": specs})

        return {
            "consistent": len(inconsistencies) == 0,
            "inconsistencies": inconsistencies,
        }
