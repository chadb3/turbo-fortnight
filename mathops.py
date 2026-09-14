"""
mathops.py

A handful of small, self-contained math functions. Each one is simple enough
to reason about by hand, which makes it easy to write a test that checks its
behavior with confidence.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b.

    Raises:
        ValueError: if b is zero, since division by zero is undefined.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def factorial(n):
    """Return n! (n factorial) for a non-negative integer n.

    Raises:
        ValueError: if n is negative, since factorial is undefined there.
    """
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
