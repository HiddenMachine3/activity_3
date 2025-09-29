"""
Tests for the calculator functions.
"""
from funcs import add, sub, mult


def test_add():
    """Test the add function."""
    assert add(1, 2) == 3

def test_sub():
    """Test the sub function."""
    assert sub(1, 2) == -1

def test_mult():
    """Test the mult function."""
    assert mult(1, 2) == 2
