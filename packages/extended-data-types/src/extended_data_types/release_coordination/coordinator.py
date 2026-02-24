"""Release Coordination component for release-please based workflows."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import extended_data_types


RELEASE_PLEASE_CONFIG = "release-please-config.json"
RELEASE_PLEASE_MANIFEST = ".release-please-manifest.json"


class ReleaseCoordinator:
    """Coordinates releases using the release-please workflow.

    Reads release-please-config.json and .release-please-manifest.json
    from the repository root to provide version and package information.
    """

    def __init__(self, repo_root: Path | None = None) -> None:
        """Initialize with the repository root directory.

        Args:
            repo_root: Path to the repository root. If None, uses get_tld()
                to discover the Git repository root automatically.

        Raises:
            RuntimeError: If no repository root can be determined.
        """
        if repo_root is None:
            tld = extended_data_types.get_tld()
            if tld is None:
                msg = "Cannot determine repository root. Pass repo_root explicitly or run from within a Git repository."
                raise RuntimeError(msg)
            self._repo_root = tld
        else:
            self._repo_root = repo_root

    def _read_json_file(self, filename: str) -> dict[str, Any]:
        """Read and parse a JSON file from the repository root.

        Args:
            filename: Name of the JSON file relative to repo root.

        Returns:
            Parsed JSON content as a dictionary.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file content cannot be parsed as JSON.
        """
        content = extended_data_types.read_file(filename, tld=self._repo_root)
        if content is None:
            msg = f"{filename} not found at {self._repo_root}"
            raise FileNotFoundError(msg)
        if not isinstance(content, (str, bytes, bytearray, memoryview)):
            msg = f"Unexpected content type from {filename}: {type(content)}"
            raise TypeError(msg)
        result = extended_data_types.decode_json(content)
        if not isinstance(result, dict):
            msg = f"{filename} must contain a JSON object, got {type(result).__name__}"
            raise TypeError(msg)
        return result

    def get_config(self) -> dict[str, Any]:
        """Read the release-please-config.json file.

        Returns:
            The full release-please configuration dictionary.

        Raises:
            FileNotFoundError: If release-please-config.json does not exist.
            ValueError: If the file is not valid JSON or not a JSON object.
        """
        return self._read_json_file(RELEASE_PLEASE_CONFIG)

    def get_manifest(self) -> dict[str, str]:
        """Read the .release-please-manifest.json file.

        Returns:
            Dictionary mapping package paths to their current version strings.

        Raises:
            FileNotFoundError: If .release-please-manifest.json does not exist.
            ValueError: If the file is not valid JSON or not a JSON object.
        """
        return self._read_json_file(RELEASE_PLEASE_MANIFEST)

    def get_packages(self) -> dict[str, dict[str, Any]]:
        """Get the packages defined in release-please-config.json.

        Returns:
            Dictionary mapping package paths to their configuration.
            For example::

                {
                    "packages/extended-data-types": {
                        "component": "edt",
                        "release-type": "python",
                        "changelog-path": "CHANGELOG.md"
                    }
                }

        Raises:
            FileNotFoundError: If release-please-config.json does not exist.
            ValueError: If the config is missing the "packages" key.
        """
        config = self.get_config()
        packages = config.get("packages")
        if packages is None:
            msg = "release-please-config.json is missing the 'packages' key"
            raise ValueError(msg)
        return packages

    def get_current_versions(self) -> dict[str, str]:
        """Get current versions for all packages from the manifest.

        Returns:
            Dictionary mapping package paths to version strings.
            For example::

                {
                    "packages/extended-data-types": "6.0.0",
                    "packages/lifecyclelogging": "2.0.0"
                }

        Raises:
            FileNotFoundError: If .release-please-manifest.json does not exist.
        """
        return self.get_manifest()

    def validate_release_readiness(self) -> dict[str, Any]:
        """Validate that release-please configuration is consistent.

        Checks that:
        - The manifest file exists and is valid JSON.
        - The config file exists and contains a packages key.
        - Every package in the config has a corresponding entry in the manifest.

        Returns:
            Dictionary with validation results::

                {
                    "ready": bool,
                    "versions": {"packages/foo": "1.0.0", ...},
                    "errors": ["...", ...],
                    "packages": {"packages/foo": {"component": "...", ...}, ...}
                }
        """
        errors: list[str] = []

        # Validate manifest
        try:
            manifest = self.get_manifest()
        except (FileNotFoundError, ValueError, TypeError) as exc:
            errors.append(f"Manifest error: {exc}")
            manifest = {}

        # Validate config and packages
        packages: dict[str, dict[str, Any]] = {}
        try:
            packages = self.get_packages()
        except (FileNotFoundError, ValueError, TypeError) as exc:
            errors.append(f"Config error: {exc}")

        # Check that every configured package has a manifest entry
        for package_path in packages:
            if package_path not in manifest:
                errors.append(f"Package '{package_path}' is in config but missing from manifest")

        return {
            "ready": len(errors) == 0,
            "versions": manifest,
            "errors": errors,
            "packages": packages,
        }
