"""Summing the elements of a list using different loops."""
__author__ = "730579443"


def w_sum(vals: list[float]) -> float:
    """Calculate the sum of floats in a list."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculate the sum of floats in a list using a for loop."""
    idx: int = 0
    sum: float = 0.0
    for numbers in vals:
        sum += vals[idx]
        idx += 1
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculate the sum of floats in a list using range function."""
    idx: int = 0
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
        idx += 1
    return sum
