"""Utils - a working product."""
__author__ = "730579443"

def all(list1: list[int], num1: int) -> bool:
    """Given a list of ints and a singualr int, will return true or false depending on whether the ints in the list are the same as the singular int."""
    # Do the stuff
    if len(list1) == 0:
        return False
    num_idx: int = 0

    while num_idx < len(list1):
        if list1[num_idx] != num1:
            return False
        num_idx += 1
    return True
print(all([1, 1, 1], 1))

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = input[0]
    max_idx: int = 1

    while max_idx < len(input):
        if input[max_idx] > max_num:
            max_num = input[max_idx]
        max_idx += 1
    return max_num
print(max([2, 2, 35]))


def is_equal(lista: list[int], listb: list[int]) -> bool:
    lengtha: int = len(lista)
    lengthb: int = len(listb)
    equal_idx: int = 0

    if lengtha != lengthb:
        return False
    
    while equal_idx < lengtha and equal_idx < lengthb:
        if lista[equal_idx] != listb[equal_idx]:
            return False
        equal_idx += 1

    if (lengtha == (equal_idx)) and (lengthb == (equal_idx)):
        return True
    else:
        return False
    
print(is_equal([1, 0, 1], [1, 0, 1]))
print(is_equal([1, 1, 0], [1, 0, 1]))