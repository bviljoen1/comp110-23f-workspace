"""Dictionary test to test the dictionary file used in ex06."""
__author__ = "730579443"

# Writing unit tests for 5 funcitons defined in dictionary.py
import pytest
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# INVERT FUNCTION - 3 unit tests: 2 use cases, 1 edge case
def test_empty__invert_dict() -> None:
    """Invert([]) should return 0."""
    # Edge Case
    input_dict = {}
    result = invert(input_dict)
    assert result == {}


def test__invert_one_pair() -> None:
    """Invert(["General": "Kenobi"]) should return {"Kenobi": "General"}."""
    # Use Case
    input_dict = {'General': 'Kenobi'}
    result = invert(input_dict)
    assert result == {'Kenobi': 'General'}


def test_invert_multiple_pairs() -> None:
    """Invert(["Ben": "Viljoen", "Andrey": "Balabin"]) should return ["Viljoen": "Ben", "Balabin": "Andrey"]."""
    # Use Case
    input_dict = {'Ben': 'Viljoen', 'Andrey': 'Balabin'}
    result = invert(input_dict)
    assert result == {'Viljoen': 'Ben', 'Balabin': 'Andrey'}


# FAVORITE_COLOR - 3 unit tests: 2 use cases, 1 edge case
def test_empty_color_dict() -> None:
    """Favorite_color([]) should yield 0."""
    # Edge Case
    input_dict = {}
    result = favorite_color(input_dict)
    assert result == ""


def test_color_one_pair() -> None:
    """Favorite_color(["Ben": "blue"]) will return {"blue"}."""
    # Use Case
    input_dict = {'Ben': 'blue'}
    result = favorite_color(input_dict)
    assert result == 'blue'


def test_color_multiple_pair() -> None:
    """Favorite_color(["Marc": "yellow", "Ezri": "blue", "Kris": "blue"]) should return {"blue"}."""
    # Use Case
    input_dict = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}
    result = favorite_color(input_dict)
    assert result == 'blue'


# COUNT - 3 unit tests: 2 use cases, 1 edge case
def test_count_empty_list() -> None:
    """Count([]) will return 0."""
    # Edge case
    input_list = {}
    result = count(input_list)
    assert result == {}


def test_count_one_element() -> None:
    """Count(['apple']) should return {'apple': 1}."""
    # Use Case
    input_list = {'apple'}
    result = count(input_list)
    assert result == {'apple': 1}


def test_count_multiple_element() -> None:
     """Count(['apple', 'banana', 'apple', 'cherry', 'banana']) should return {'apple': 2, 'banana': 2, 'cherry': 1}."""
     # Use Case
     input_list = ['apple', 'banana', 'apple', 'cherry', 'banana']
     result = count(input_list)
     assert result == {'apple': 2, 'banana': 2, 'cherry': 1}


# ALPHABETIZER - 3 unit tests: 2 use cases, 1 edge case
def test_alphabetizer_empty_list() -> None:
    """Alphabetizer([]) should return 0."""
    # Edge case
    input_list = {}
    result = alphabetizer(input_list)
    assert result == {}


def test_alphabetizer_one_element() -> None:
    """Alphabetizer(['cat']) should return {c: ['cat']}."""
    # Use Case
    input_list = ['cat']
    result = alphabetizer(input_list)
    assert result == {'c': ['cat']}


def test_alphabetizer_multiple_elements() -> None:
    """Alphabetizer(['cat', 'apple']) should return {'c': ['cat'], 'a': ['apple']}."""
    # Use Case
    input_list = ['cat', 'apple']
    result = alphabetizer(input_list)
    assert result == {'c': ['cat'], 'a': ['apple']}


# UPDATE_ATTENDANCE - 3 unit tests: 2 use cases, 1 edge case
def test_attendance_empty_dict() -> None:
    """Update_attendance([]) should return 0."""
    # Edge case
    input_dict = {}
    result = update_attendance(input_dict, 'Monday', 'Alice')
    assert result == {'Monday': ["Alice"]}

def test_attendance_one_element() -> None:
    """Update_attendance(['Monday': ['Vrinda', 'Kaleb']], 'Monday', 'Alice') should return {'Monday': ['Vrinda', 'Kaleb', 'Alice']}."""
    # Use Case
    input_dict = {'Monday': ['Vrinda', 'Kaleb']}
    result = update_attendance(input_dict, 'Monday', 'Alice')
    assert result == {'Monday': ['Vrinda', 'Kaleb', 'Alice']}

def test_attendance_multiple_elements() -> None:
    """Update_attendance(['Monday': ['Vrinda', 'Kaleb', 'Alice'], 'Tuesday', 'Vrinda') should return {'Monday': ['Vrinda', 'Kaleb', 'Alice'], 'Tuesday': ['Vrinda']}."""
    # Use Case
    input_dict = {'Monday': ['Vrinda', 'Kaleb', 'Alice']}
    result = update_attendance(input_dict, 'Tuesday', 'Vrinda')
    assert result == {'Monday': ['Vrinda', 'Kaleb', 'Alice'], 'Tuesday': ['Vrinda']}