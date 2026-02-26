"""Tests for the ecosystem foundation."""

from __future__ import annotations

from pathlib import Path

import pytest

from hypothesis import given, settings
from hypothesis import strategies as st

import extended_data_types

from extended_data_types import (
    DevelopmentIntegration,
    EcosystemPackageDiscovery,
    EcosystemStatusMonitor,
    ReleaseCoordinator,
    mcp_server_main,
)
from extended_data_types.ecosystem_status.monitor import _parse_dep_spec


# ---------------------------------------------------------------------------
# Property-based tests
# ---------------------------------------------------------------------------


@given(st.sampled_from(extended_data_types.__all__))
@settings(max_examples=50, deadline=None)
def test_property_1_mcp_doc_completeness(name: str) -> None:
    """**Feature: ecosystem-foundation, Property 1: MCP Server Function Documentation Completeness**"""
    from extended_data_types.mcp_server.server import (
        _get_library_functions as get_library_functions,
    )

    funcs = get_library_functions()
    attr = getattr(extended_data_types, name)
    if callable(attr):
        assert name in funcs


# ---------------------------------------------------------------------------
# Import tests
# ---------------------------------------------------------------------------


def test_ecosystem_foundation_imports() -> None:
    """Verify that all ecosystem foundation components are correctly exported."""
    assert EcosystemPackageDiscovery is not None
    assert ReleaseCoordinator is not None
    assert EcosystemStatusMonitor is not None
    assert DevelopmentIntegration is not None
    assert mcp_server_main is not None


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def sample_project(tmp_path: Path) -> Path:
    """Create a sample Python project with ecosystem-compliant structure."""
    project = tmp_path / "sample-project"
    project.mkdir()

    # pyproject.toml with hatchling
    (project / "pyproject.toml").write_text(
        '[build-system]\nrequires = ["hatchling"]\nbuild-backend = "hatchling.build"\n\n'
        '[project]\nname = "sample-project"\nversion = "1.0.0"\n'
        'description = "A sample project"\n'
        'dependencies = ["requests>=2.0", "extended-data-types>=6.0"]\n\n'
        "[tool.ruff]\nline-length = 88\n\n"
        "[tool.mypy]\nstrict = true\n"
    )

    # src layout
    src = project / "src" / "sample_project"
    src.mkdir(parents=True)
    (src / "__init__.py").write_text("")

    # tests dir
    (project / "tests").mkdir()

    return project


@pytest.fixture()
def non_compliant_project(tmp_path: Path) -> Path:
    """Create a project that violates ecosystem conventions."""
    project = tmp_path / "bad-project"
    project.mkdir()

    # pyproject.toml with setuptools (not hatchling)
    (project / "pyproject.toml").write_text(
        '[build-system]\nrequires = ["setuptools"]\nbuild-backend = "setuptools.build_meta"\n\n'
        '[project]\nname = "bad-project"\nversion = "0.1.0"\n'
    )

    return project


@pytest.fixture()
def ecosystem_dir(tmp_path: Path) -> Path:
    """Create a directory simulating ~/src with multiple packages."""
    base = tmp_path / "ecosystem"
    base.mkdir()

    # Package A: depends on nothing
    pkg_a = base / "package-a"
    pkg_a.mkdir()
    (pkg_a / "pyproject.toml").write_text(
        '[project]\nname = "package-a"\nversion = "1.0.0"\ndependencies = ["requests"]\n'
    )

    # Package B: depends on package-a
    pkg_b = base / "package-b"
    pkg_b.mkdir()
    (pkg_b / "pyproject.toml").write_text(
        '[project]\nname = "package-b"\nversion = "2.0.0"\ndependencies = ["package-a>=1.0"]\n'
    )

    # Package C: depends on package-a with different version spec
    pkg_c = base / "package-c"
    pkg_c.mkdir()
    (pkg_c / "pyproject.toml").write_text(
        '[project]\nname = "package-c"\nversion = "3.0.0"\ndependencies = ["package-a>=1.0,<2.0"]\n'
    )

    # Non-package directory (no pyproject.toml)
    (base / "not-a-package").mkdir()

    return base


@pytest.fixture()
def release_dir(tmp_path: Path) -> Path:
    """Create a directory with release-please config files."""
    repo = tmp_path / "repo"
    repo.mkdir()

    # release-please-config.json
    (repo / "release-please-config.json").write_text(
        "{\n"
        '  "packages": {\n'
        '    "packages/foo": {"component": "foo", "release-type": "python"},\n'
        '    "packages/bar": {"component": "bar", "release-type": "python"}\n'
        "  }\n"
        "}\n"
    )

    # .release-please-manifest.json
    (repo / ".release-please-manifest.json").write_text('{"packages/foo": "1.0.0", "packages/bar": "2.0.0"}\n')

    return repo


# ---------------------------------------------------------------------------
# EcosystemPackageDiscovery tests
# ---------------------------------------------------------------------------


class TestEcosystemPackageDiscovery:
    """Tests for EcosystemPackageDiscovery."""

    def test_default_base_path(self) -> None:
        """Default base_path is ~/src."""
        discovery = EcosystemPackageDiscovery()
        assert discovery.base_path == Path.home() / "src"

    def test_custom_base_path(self, tmp_path: Path) -> None:
        """Custom base_path is accepted."""
        discovery = EcosystemPackageDiscovery(base_path=tmp_path)
        assert discovery.base_path == tmp_path

    def test_scan_empty_directory(self, tmp_path: Path) -> None:
        """Empty directory returns empty list."""
        discovery = EcosystemPackageDiscovery(base_path=tmp_path)
        assert discovery.scan_packages() == []

    def test_scan_nonexistent_directory(self, tmp_path: Path) -> None:
        """Nonexistent base path returns empty list."""
        discovery = EcosystemPackageDiscovery(base_path=tmp_path / "nonexistent")
        assert discovery.scan_packages() == []

    def test_scan_finds_packages(self, ecosystem_dir: Path) -> None:
        """Directories with pyproject.toml are discovered as packages."""
        discovery = EcosystemPackageDiscovery(base_path=ecosystem_dir)
        packages = discovery.scan_packages()
        names = {p["name"] for p in packages}
        assert "package-a" in names
        assert "package-b" in names
        assert "package-c" in names
        assert "not-a-package" not in names

    def test_scan_returns_correct_fields(self, ecosystem_dir: Path) -> None:
        """Scanned packages have expected fields."""
        discovery = EcosystemPackageDiscovery(base_path=ecosystem_dir)
        packages = discovery.scan_packages()
        for pkg in packages:
            assert "name" in pkg
            assert "path" in pkg
            assert "is_git" in pkg
            assert "repo_name" in pkg

    def test_get_package_dependencies(self, ecosystem_dir: Path) -> None:
        """Dependencies are correctly parsed from pyproject.toml."""
        discovery = EcosystemPackageDiscovery(base_path=ecosystem_dir)
        deps = discovery.get_package_dependencies(ecosystem_dir / "package-b")
        assert deps["name"] == "package-b"
        assert deps["version"] == "2.0.0"
        assert "package-a>=1.0" in deps["dependencies"]

    def test_get_dependencies_missing_pyproject(self, tmp_path: Path) -> None:
        """Missing pyproject.toml returns empty dict."""
        discovery = EcosystemPackageDiscovery(base_path=tmp_path)
        assert discovery.get_package_dependencies(tmp_path / "nonexistent") == {}


# ---------------------------------------------------------------------------
# ReleaseCoordinator tests
# ---------------------------------------------------------------------------


class TestReleaseCoordinator:
    """Tests for ReleaseCoordinator."""

    def test_auto_discover_repo_root(self) -> None:
        """Auto-discovers repo root via get_tld() and can read config."""
        coordinator = ReleaseCoordinator()
        # Verify it found a valid root by successfully reading config
        config = coordinator.get_config()
        assert isinstance(config, dict)

    def test_explicit_repo_root(self, release_dir: Path) -> None:
        """Accepts explicit repo root and reads config from it."""
        coordinator = ReleaseCoordinator(repo_root=release_dir)
        config = coordinator.get_config()
        assert "packages" in config

    def test_get_config(self, release_dir: Path) -> None:
        """Reads release-please-config.json."""
        coordinator = ReleaseCoordinator(repo_root=release_dir)
        config = coordinator.get_config()
        assert "packages" in config

    def test_get_manifest(self, release_dir: Path) -> None:
        """Reads .release-please-manifest.json."""
        coordinator = ReleaseCoordinator(repo_root=release_dir)
        manifest = coordinator.get_manifest()
        assert "packages/foo" in manifest
        assert manifest["packages/foo"] == "1.0.0"

    def test_get_packages(self, release_dir: Path) -> None:
        """Extracts packages from config."""
        coordinator = ReleaseCoordinator(repo_root=release_dir)
        packages = coordinator.get_packages()
        assert "packages/foo" in packages
        assert packages["packages/foo"]["component"] == "foo"

    def test_get_current_versions(self, release_dir: Path) -> None:
        """Returns version mapping from manifest."""
        coordinator = ReleaseCoordinator(repo_root=release_dir)
        versions = coordinator.get_current_versions()
        assert versions["packages/foo"] == "1.0.0"
        assert versions["packages/bar"] == "2.0.0"

    def test_validate_release_readiness_valid(self, release_dir: Path) -> None:
        """Valid config reports ready."""
        coordinator = ReleaseCoordinator(repo_root=release_dir)
        result = coordinator.validate_release_readiness()
        assert result["ready"] is True
        assert result["errors"] == []
        assert "packages/foo" in result["versions"]

    def test_validate_release_readiness_missing_manifest_entry(self, tmp_path: Path) -> None:
        """Missing manifest entry is reported as error."""
        repo = tmp_path / "bad-repo"
        repo.mkdir()
        (repo / "release-please-config.json").write_text(
            '{"packages": {"packages/foo": {"component": "foo"}, "packages/bar": {"component": "bar"}}}'
        )
        (repo / ".release-please-manifest.json").write_text('{"packages/foo": "1.0.0"}')

        coordinator = ReleaseCoordinator(repo_root=repo)
        result = coordinator.validate_release_readiness()
        assert result["ready"] is False
        assert any("bar" in e for e in result["errors"])

    def test_validate_release_readiness_missing_config(self, tmp_path: Path) -> None:
        """Missing config file is reported as error."""
        repo = tmp_path / "empty-repo"
        repo.mkdir()
        (repo / ".release-please-manifest.json").write_text("{}")

        coordinator = ReleaseCoordinator(repo_root=repo)
        result = coordinator.validate_release_readiness()
        assert result["ready"] is False
        assert any("config" in e.lower() for e in result["errors"])

    def test_validate_readiness_returns_structured_result(self) -> None:
        """Readiness result has all expected keys (live repo test)."""
        coordinator = ReleaseCoordinator()
        readiness = coordinator.validate_release_readiness()
        assert "ready" in readiness
        assert "versions" in readiness
        assert "errors" in readiness
        assert "packages" in readiness


# ---------------------------------------------------------------------------
# EcosystemStatusMonitor tests
# ---------------------------------------------------------------------------


class TestEcosystemStatusMonitor:
    """Tests for EcosystemStatusMonitor."""

    def test_default_discovery(self) -> None:
        """Creates default discovery if none provided."""
        monitor = EcosystemStatusMonitor()
        assert monitor.discovery is not None

    def test_custom_discovery(self, ecosystem_dir: Path) -> None:
        """Accepts custom discovery instance."""
        discovery = EcosystemPackageDiscovery(base_path=ecosystem_dir)
        monitor = EcosystemStatusMonitor(discovery=discovery)
        assert monitor.discovery is discovery

    def test_get_ecosystem_status_structure(self, ecosystem_dir: Path) -> None:
        """Status result has all expected keys."""
        discovery = EcosystemPackageDiscovery(base_path=ecosystem_dir)
        monitor = EcosystemStatusMonitor(discovery=discovery)
        status = monitor.get_ecosystem_status()
        assert "package_count" in status
        assert "packages" in status
        assert "dependency_graph" in status
        assert "version_consistency" in status
        assert "health" in status

    def test_package_count(self, ecosystem_dir: Path) -> None:
        """Package count matches discovered packages."""
        discovery = EcosystemPackageDiscovery(base_path=ecosystem_dir)
        monitor = EcosystemStatusMonitor(discovery=discovery)
        status = monitor.get_ecosystem_status()
        assert status["package_count"] == 3

    def test_dependency_graph(self, ecosystem_dir: Path) -> None:
        """Dependency graph maps packages to ecosystem deps."""
        discovery = EcosystemPackageDiscovery(base_path=ecosystem_dir)
        monitor = EcosystemStatusMonitor(discovery=discovery)
        graph = monitor.get_dependency_graph()
        assert isinstance(graph, dict)
        # package-b and package-c depend on package-a
        assert "package-b" in graph, "package-b should be in dependency graph"
        assert "package-a" in graph["package-b"]
        assert "package-c" in graph, "package-c should be in dependency graph"
        assert "package-a" in graph["package-c"]

    def test_version_consistency_consistent(self, tmp_path: Path) -> None:
        """Consistent versions across packages."""
        base = tmp_path / "consistent"
        base.mkdir()
        for name in ("pkg-x", "pkg-y"):
            d = base / name
            d.mkdir()
            (d / "pyproject.toml").write_text(
                f'[project]\nname = "{name}"\nversion = "1.0.0"\ndependencies = ["shared-lib>=1.0"]\n'
            )
        discovery = EcosystemPackageDiscovery(base_path=base)
        monitor = EcosystemStatusMonitor(discovery=discovery)
        result = monitor.check_version_consistency()
        assert result["consistent"] is True
        assert result["inconsistencies"] == []

    def test_version_consistency_inconsistent(self, ecosystem_dir: Path) -> None:
        """Inconsistent version specs are detected."""
        discovery = EcosystemPackageDiscovery(base_path=ecosystem_dir)
        monitor = EcosystemStatusMonitor(discovery=discovery)
        result = monitor.check_version_consistency()
        # package-b uses "package-a>=1.0" and package-c uses "package-a>=1.0,<2.0"
        assert result["consistent"] is False
        assert len(result["inconsistencies"]) > 0
        dep_names = [i["dependency"] for i in result["inconsistencies"]]
        assert "package-a" in dep_names

    def test_health_healthy(self, tmp_path: Path) -> None:
        """Health is 'healthy' when all versions present and consistent."""
        base = tmp_path / "healthy"
        base.mkdir()
        d = base / "solo"
        d.mkdir()
        (d / "pyproject.toml").write_text('[project]\nname = "solo"\nversion = "1.0.0"\ndependencies = []\n')
        discovery = EcosystemPackageDiscovery(base_path=base)
        monitor = EcosystemStatusMonitor(discovery=discovery)
        status = monitor.get_ecosystem_status()
        assert status["health"] == "healthy"

    def test_health_unknown_empty(self, tmp_path: Path) -> None:
        """Health is 'unknown' when no packages found."""
        discovery = EcosystemPackageDiscovery(base_path=tmp_path)
        monitor = EcosystemStatusMonitor(discovery=discovery)
        status = monitor.get_ecosystem_status()
        assert status["health"] == "unknown"

    def test_ecosystem_status_is_idempotent(self, ecosystem_dir: Path) -> None:
        """Repeated calls return consistent results (caching works)."""
        discovery = EcosystemPackageDiscovery(base_path=ecosystem_dir)
        monitor = EcosystemStatusMonitor(discovery=discovery)
        first = monitor.get_ecosystem_status()
        second = monitor.get_ecosystem_status()
        assert first == second


# ---------------------------------------------------------------------------
# _parse_dep_spec tests
# ---------------------------------------------------------------------------


class TestParseDepSpec:
    """Tests for the dependency spec parser."""

    @pytest.mark.parametrize(
        "dep,expected_name,expected_spec",
        [
            ("requests>=2.0", "requests", ">=2.0"),
            ("some-package>=1.0,<2.0", "some-package", ">=1.0,<2.0"),
            ("my_package[extra]>=1.0", "my-package", ">=1.0"),
            ("Simple", "simple", ""),
            ("A.B-C_D", "a-b-c-d", ""),
        ],
    )
    def test_parse_dep_spec(self, dep: str, expected_name: str, expected_spec: str) -> None:
        """Dependency strings are parsed correctly."""
        name, spec = _parse_dep_spec(dep)
        assert name == expected_name
        assert spec == expected_spec


# ---------------------------------------------------------------------------
# DevelopmentIntegration tests
# ---------------------------------------------------------------------------


class TestDevelopmentIntegration:
    """Tests for DevelopmentIntegration."""

    def test_validate_compliant_project(self, sample_project: Path) -> None:
        """Compliant project passes all checks."""
        di = DevelopmentIntegration()
        result = di.validate_project_structure(sample_project)
        assert result["valid"] is True
        assert result["issues"] == []

    def test_validate_non_compliant_project(self, non_compliant_project: Path) -> None:
        """Non-compliant project fails checks for missing build-system and tests."""
        di = DevelopmentIntegration()
        result = di.validate_project_structure(non_compliant_project)
        assert result["valid"] is False
        issues_text = " ".join(result["issues"]).lower()
        assert "build" in issues_text or "test" in issues_text

    def test_configure_development_environment(self, sample_project: Path) -> None:
        """Compliant project has all configs detected."""
        di = DevelopmentIntegration()
        result = di.configure_development_environment(sample_project)
        assert result["configured"] is True
        assert result["configs"]["pyproject_toml"]["found"] is True
        assert result["configs"]["ruff"]["found"] is True
        assert result["configs"]["mypy"]["found"] is True

    def test_configure_missing_tools(self, non_compliant_project: Path) -> None:
        """Missing tool configs are reported with specifics."""
        di = DevelopmentIntegration()
        result = di.configure_development_environment(non_compliant_project)
        assert result["configured"] is False
        issues_text = " ".join(result["issues"]).lower()
        assert "ruff" in issues_text or "mypy" in issues_text or "missing" in issues_text

    def test_get_project_info(self, sample_project: Path) -> None:
        """Project info is correctly extracted from pyproject.toml."""
        di = DevelopmentIntegration()
        info = di.get_project_info(sample_project)
        assert info["name"] == "sample-project"
        assert info["version"] == "1.0.0"
        assert info["build_backend"] == "hatchling.build"
        assert "requests>=2.0" in info["dependencies"]

    def test_get_project_info_missing(self, tmp_path: Path) -> None:
        """Missing pyproject.toml returns empty dict."""
        di = DevelopmentIntegration()
        assert di.get_project_info(tmp_path / "nonexistent") == {}

    def test_missing_init_detection(self, tmp_path: Path) -> None:
        """Missing __init__.py in src packages is detected."""
        project = tmp_path / "no-init"
        project.mkdir()
        (project / "pyproject.toml").write_text(
            '[build-system]\nrequires = ["hatchling"]\nbuild-backend = "hatchling.build"\n\n'
            '[project]\nname = "no-init"\nversion = "0.1.0"\n'
        )
        src = project / "src" / "my_package"
        src.mkdir(parents=True)
        # No __init__.py
        (project / "tests").mkdir()

        di = DevelopmentIntegration()
        result = di.validate_project_structure(project)
        assert result["valid"] is False
        assert "__init__.py in src packages" in result["issues"]

    def test_ruff_config_in_separate_file(self, tmp_path: Path) -> None:
        """Ruff config in ruff.toml is detected."""
        project = tmp_path / "ruff-file"
        project.mkdir()
        (project / "pyproject.toml").write_text('[project]\nname = "test"\nversion = "0.1.0"\n')
        (project / "ruff.toml").write_text("line-length = 88\n")

        di = DevelopmentIntegration()
        result = di.configure_development_environment(project)
        assert result["configs"]["ruff"]["found"] is True
        assert result["configs"]["ruff"]["source"] == "ruff.toml"

    def test_mypy_config_in_ini_file(self, tmp_path: Path) -> None:
        """Mypy config in mypy.ini is detected."""
        project = tmp_path / "mypy-ini"
        project.mkdir()
        (project / "pyproject.toml").write_text('[project]\nname = "test"\nversion = "0.1.0"\n')
        (project / "mypy.ini").write_text("[mypy]\nstrict = true\n")

        di = DevelopmentIntegration()
        result = di.configure_development_environment(project)
        assert result["configs"]["mypy"]["found"] is True
        assert result["configs"]["mypy"]["source"] == "mypy.ini"
