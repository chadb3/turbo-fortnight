"""
Tests for mathops.py.

Run locally with:
    pytest

This is the same command the GitHub Actions workflow runs automatically
every time code is pushed.
"""

import pytest

from mathops import add, subtract, multiply, divide, is_prime, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-2, -3) == -5
    assert add(999,1)=1000;


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-2, -2) == 0


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-3, 3) == -9
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(5, 0)


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (0, False),
        (-5, False),
    ],
)
def test_is_prime(number, expected):
    assert is_prime(number) == expected


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)
