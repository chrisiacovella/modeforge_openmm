"""
Unit and regression test for the modelforge_openmm package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import modelforge_openmm


def test_modelforge_openmm_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "modelforge_openmm" in sys.modules
