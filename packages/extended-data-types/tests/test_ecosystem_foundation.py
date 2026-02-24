"""Tests for the ecosystem foundation."""

from __future__ import annotations

import sys

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
    if sys.version_info < (3, 10):
        return  # MCP not supported on < 3.10

    from extended_data_types.mcp_server.server import get_library_functions

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
    if sys.version_info >= (3, 10):
        assert mcp_server_main is not None


def test_package_discovery_basic():
    """Basic test for package discovery."""
    discovery = EcosystemPackageDiscovery(base_path=None)
    assert discovery.base_path is not None


def test_release_coordinator_basic():
    """Basic test for release coordinator."""
    coordinator = ReleaseCoordinator()
    assert coordinator.config is not None


def test_status_monitor_basic():
    """Basic test for ecosystem status monitor."""
    monitor = EcosystemStatusMonitor()
    status = monitor.get_ecosystem_status()
    assert "package_count" in status
    assert "health" in status
