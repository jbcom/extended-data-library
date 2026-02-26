"""Tests for the ecosystem foundation."""

from __future__ import annotations

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


@given(st.sampled_from(extended_data_types.__all__))
@settings(max_examples=50, deadline=None)
def test_property_1_mcp_doc_completeness(name):
    """**Feature: ecosystem-foundation, Property 1: MCP Server Function Documentation Completeness**"""
    from extended_data_types.mcp_server.server import _get_library_functions as get_library_functions

    funcs = get_library_functions()
    attr = getattr(extended_data_types, name)
    if callable(attr):
        assert name in funcs


def test_ecosystem_foundation_imports():
    """Verify that all ecosystem foundation components are correctly exported."""
    assert EcosystemPackageDiscovery is not None
    assert ReleaseCoordinator is not None
    assert EcosystemStatusMonitor is not None
    assert DevelopmentIntegration is not None
    assert mcp_server_main is not None


def test_package_discovery_basic():
    """Basic test for package discovery."""
    discovery = EcosystemPackageDiscovery(base_path=None)
    assert discovery.base_path is not None


def test_release_coordinator_basic():
    """Basic test for release coordinator."""
    coordinator = ReleaseCoordinator()
    # The coordinator auto-discovers the repo root via get_tld()
    assert coordinator._repo_root is not None
    # Validate release readiness returns structured result
    readiness = coordinator.validate_release_readiness()
    assert "ready" in readiness
    assert "versions" in readiness
    assert "errors" in readiness


def test_status_monitor_basic():
    """Basic test for ecosystem status monitor."""
    monitor = EcosystemStatusMonitor()
    status = monitor.get_ecosystem_status()
    assert "package_count" in status
    assert "health" in status
