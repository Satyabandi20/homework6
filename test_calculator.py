"""
This module contains unit tests for the calculator module.
"""

from calculator import add, subtract

def test_addition():
    """Test that the addition function works."""
    assert add(2, 2) == 4

def test_subtraction():
    """Test that the subtraction function works."""
    assert subtract(2, 2) == 0
