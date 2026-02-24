"""Development Integration component for ecosystem project validation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import extended_data_types


class DevelopmentIntegration:
    """Validates and inspects Python projects for ecosystem compliance.

    Checks that projects follow the extended-data-types ecosystem conventions:
    hatchling build backend, src layout, tests directory, and proper config.
    """

    def __init__(self, project_template_path: Path | None = None) -> None:
        """Initialize with optional project template path.

        Args:
            project_template_path: Path to template files for project generation.
        """
        self.project_template_path = project_template_path

    def configure_development_environment(self, project_path: Path) -> dict[str, Any]:
        """Validate that a project has the expected config files.

        Checks for pyproject.toml, ruff configuration (pyproject.toml,
        ruff.toml, or .ruff.toml), and mypy configuration (pyproject.toml,
        mypy.ini, or .mypy.ini).

        Args:
            project_path: Root path of the project.

        Returns:
            Dict with per-config validation results and overall status.
        """
        project_path = Path(project_path)
        configs: dict[str, dict[str, Any]] = {}

        # Check pyproject.toml
        pyproject = project_path / "pyproject.toml"
        configs["pyproject_toml"] = {
            "found": pyproject.is_file(),
            "path": str(pyproject),
        }

        # Load tool sections from pyproject.toml (reused for ruff/mypy checks)
        tools: dict[str, Any] = {}
        if pyproject.is_file():
            tools = self._load_tool_section(pyproject)

        # Check ruff config
        configs["ruff"] = self._find_ruff_config(project_path, tools)

        # Check mypy config
        configs["mypy"] = self._find_mypy_config(project_path, tools)

        all_found = all(cfg.get("found", False) for cfg in configs.values())
        issues: list[str] = []
        if not configs["pyproject_toml"]["found"]:
            issues.append("pyproject.toml not found")
        if not configs["ruff"]["found"]:
            issues.append("No ruff configuration found")
        if not configs["mypy"]["found"]:
            issues.append("No mypy configuration found")

        return {
            "configured": all_found,
            "configs": configs,
            "issues": issues,
        }

    def validate_project_structure(self, project_path: Path) -> dict[str, Any]:
        """Check that a project follows ecosystem conventions.

        Validates:
        - pyproject.toml exists with hatchling build backend
        - src/ layout is used
        - tests/ directory exists
        - Proper __init__.py files in src packages

        Args:
            project_path: Root path of the project to validate.

        Returns:
            Dict with validation results including passed checks and issues.
        """
        project_path = Path(project_path)
        checks: list[dict[str, Any]] = []

        # Check pyproject.toml exists
        pyproject = project_path / "pyproject.toml"
        checks.append(
            {
                "name": "pyproject.toml exists",
                "passed": pyproject.is_file(),
            }
        )

        # Check build backend if pyproject.toml exists
        if pyproject.is_file():
            info = self.get_project_info(project_path)
            build_backend = info.get("build_backend", "")
            checks.append(
                {
                    "name": "hatchling build backend",
                    "passed": "hatchling" in build_backend,
                }
            )

        # Check src layout
        src_dir = project_path / "src"
        has_src = src_dir.is_dir()
        checks.append(
            {
                "name": "src/ layout",
                "passed": has_src,
            }
        )

        # Check tests directory
        tests_dir = project_path / "tests"
        checks.append(
            {
                "name": "tests/ directory",
                "passed": tests_dir.is_dir(),
            }
        )

        # Check __init__.py files in src packages
        if has_src:
            missing_inits = self._find_packages_missing_init(src_dir)
            checks.append(
                {
                    "name": "__init__.py in src packages",
                    "passed": len(missing_inits) == 0,
                    "details": missing_inits or None,
                }
            )

        issues = [c["name"] for c in checks if not c["passed"]]
        return {
            "valid": len(issues) == 0,
            "checks": checks,
            "issues": issues,
        }

    def get_project_info(self, project_path: Path) -> dict[str, Any]:
        """Read pyproject.toml and return project metadata.

        Args:
            project_path: Root path of the project.

        Returns:
            Dict with project name, version, dependencies, and build backend.
            Returns an empty dict if pyproject.toml cannot be read.
        """
        project_path = Path(project_path)
        pyproject = project_path / "pyproject.toml"
        if not pyproject.exists():
            return {}

        try:
            content = extended_data_types.read_file(pyproject)
            if not isinstance(content, (str, bytes, bytearray, memoryview)):
                return {}
            data = extended_data_types.decode_toml(content)
        except (OSError, ValueError):
            return {}

        project = data.get("project", {})
        build_system = data.get("build-system", {})

        return {
            "name": project.get("name", ""),
            "version": project.get("version", ""),
            "description": project.get("description", ""),
            "dependencies": project.get("dependencies", []),
            "optional_dependencies": project.get("optional-dependencies", {}),
            "build_backend": build_system.get("build-backend", ""),
            "build_requires": build_system.get("requires", []),
            "python_requires": project.get("requires-python", ""),
        }

    def _load_tool_section(self, pyproject_path: Path) -> dict[str, Any]:
        """Load the [tool] section from a pyproject.toml file.

        Args:
            pyproject_path: Path to pyproject.toml.

        Returns:
            The tool section as a dict, or empty dict on failure.
        """
        try:
            content = extended_data_types.read_file(pyproject_path)
            if not isinstance(content, (str, bytes, bytearray, memoryview)):
                return {}
            data = extended_data_types.decode_toml(content)
            return dict(data.get("tool", {}))
        except (OSError, ValueError):
            return {}

    def _find_ruff_config(self, project_path: Path, tools: dict[str, Any]) -> dict[str, Any]:
        """Locate ruff configuration across standard locations.

        Args:
            project_path: Root directory of the project.
            tools: Pre-loaded [tool] section from pyproject.toml.

        Returns:
            Status dict with found flag and source location.
        """
        if "ruff" in tools:
            return {
                "found": True,
                "source": "pyproject.toml [tool.ruff]",
            }
        for filename in ("ruff.toml", ".ruff.toml"):
            candidate = project_path / filename
            if candidate.is_file():
                return {"found": True, "source": filename}
        return {"found": False, "source": None}

    def _find_mypy_config(self, project_path: Path, tools: dict[str, Any]) -> dict[str, Any]:
        """Locate mypy configuration across standard locations.

        Args:
            project_path: Root directory of the project.
            tools: Pre-loaded [tool] section from pyproject.toml.

        Returns:
            Status dict with found flag and source location.
        """
        if "mypy" in tools:
            return {
                "found": True,
                "source": "pyproject.toml [tool.mypy]",
            }
        for filename in ("mypy.ini", ".mypy.ini", "setup.cfg"):
            candidate = project_path / filename
            if candidate.is_file():
                if filename == "setup.cfg":
                    # Only count setup.cfg if it has a [mypy] section
                    try:
                        content = extended_data_types.read_file(candidate)
                        if isinstance(content, str) and "[mypy]" in content:
                            return {"found": True, "source": "setup.cfg [mypy]"}
                    except OSError:
                        continue
                else:
                    return {"found": True, "source": filename}
        return {"found": False, "source": None}

    def _find_packages_missing_init(self, src_dir: Path) -> list[str]:
        """Find package directories under src/ that lack __init__.py.

        Args:
            src_dir: The src/ directory to inspect.

        Returns:
            List of directory names missing __init__.py.
        """
        missing: list[str] = []
        for item in sorted(src_dir.iterdir()):
            if item.is_dir() and not item.name.startswith((".", "_")) and not (item / "__init__.py").is_file():
                missing.append(item.name)
        return missing
