"""Combining two lists into a dictionary."""
__author__ = "730579443"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Gathering input from two lists to produce a dictionary."""
    if len(keys) != len(values) or len(keys) == 0:
        return {}
    
    hehe = {}
    for idx in range(len(keys)):
        hehe[keys[idx]] = values[idx]
    return hehe