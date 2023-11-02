"""Test my zip function."""
__author__ = "730579443"

from lessons.zip import zip

# Write 3 unit tests for zip
# One Edge case
# Two use cases
def test_empty_dict() -> None:
    """zip([]) should return 0"""
    keys = []
    values = []
    result = zip(keys, values)
    assert result == {}


def test_one_element() -> None:
    """Zip(["Hello"], [1]) should return "Hello": 1"""
    keys = ["Hello"]
    values = [1]
    result = zip(keys, values)
    assert result == {"Hello": 1}


def test_multiple_elements() -> None:
    """Zip(["Hello", "Hola", "Bonjour"], [1, 5, 8]) should return {"Hello": 1, "Hola": 5, "Bonjour": 8}"""
    keys = ["Hello", "Hola", "Bonjour"]
    values = [1, 5, 8]
    result = zip(keys, values)
    assert result == {"Hello": 1, "Hola": 5, "Bonjour": 8}