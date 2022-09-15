"""EX04 - Utils."""

__author__ = "730604615"


def all(list_int: list[int], num: int) -> bool:
    """Given a list and an int, return True if the int is present in every index."""
    if len(list_int) == 0:
        return False
    else:
        i: int = 0
        while i < len(list_int):
            if list_int[i] != num:
                return False
            else:
                i += 1
        return True


def max(input: list[int]) -> int:
    """Given a list of ints, return the maximum int value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        max_int: int = input[i]
        while i < len(input):
            if input[i] > max_int:
                max_int = input[i]
            i += 1
        return max_int


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Given 2 lists of ints, return True if they are deeply equal to each other."""
    if len(list_one) == 0 and len(list_two) == 0:
        return True
    elif len(list_one) == 0 or len(list_two) == 0:
        return False
    elif len(list_one) != len(list_two):
        return False
    else:
        i: int = 0
        j: int = 0
        while i < len(list_one) and j < len(list_two):
            if list_one[i] == list_two[j]:
                i += 1
                j += 1
            else:
                return False
        return True