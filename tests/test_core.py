import pytest

from server.core import compute_operation


def test_add():
    """
    Test addition operation.
    """
    assert compute_operation("add", 1, 2) == 3


def test_subtract():
    """
    Test subtraction operation.
    """
    assert compute_operation("subtract", 5, 3) == 2


def test_multiply():
    """
    Test multiplication operation.
    """
    assert compute_operation("multiply", 2, 3) == 6


def test_divide():
    """
    Test division operation.
    """
    assert compute_operation("divide", 6, 2) == 3


def test_divide_by_zero():
    """
    Test that division by zero raises a ValueError.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        compute_operation("divide", 1, 0)


def test_unknown_operation():
    """
    Test that an unknown operation raises a ValueError.
    """
    with pytest.raises(ValueError, match="Unknown operation"):
        compute_operation("unknown", 1, 1)
