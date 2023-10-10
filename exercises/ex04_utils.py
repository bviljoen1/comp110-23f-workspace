"""Utils - a working product."""
__author__ = "730579443"

def all(list1: list[int], num1: int) -> bool:
    """Given a list of ints and a singualr int, will return true or false depending on whether the ints in the list are the same as the singular int."""
    # Will check if the list exists, and whether every integer in the list is equal to the singular search integer.
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
    """Given a list of integers, it will return the integer of highest value."""
    # Will make sure the list isn't empty, then is going to initialize the max to be the first integer. then check if integer 2 is bigger than the first, if so then the second integer becomes the new maximum and the loop repeats until the list runs out of values.
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
    """Given two lists, the is_equal function will first check that they're the same length. If theyre not it returns False. After this it will make surethey're both set to the same index (equal_idx...)it will go through each index, comparing each list at that index, if at any point the two lists aren't equal it will exit and return false. if it gets through every index and they're all the same it will exit the while loop and return True."""
    # Will check lengths are same then index each integer, then will return True or False depending on the outcome of the previous test.
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