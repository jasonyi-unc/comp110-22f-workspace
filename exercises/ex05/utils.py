"""EX05 - list utility functions."""

__author__ = "730604615"


def only_evens(user_list: list[int]) -> list[int]:
    """Given a list of ints, returns a new list of even elements."""
    evens_list: list[int] = list()
    for i in user_list:
        if i % 2 == 0:
            evens_list.append(i)
    return evens_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given 2 list of ints, return a new list that concatenates both lists."""
    concat_list: list[int] = list()
    for i in list_one:
        concat_list.append(i)
    for i in list_two:
        concat_list.append(i)
    return concat_list


def sub(user_list: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints and 2 ints, returns a new list based on the start index and end index."""
    sub_list: list[int] = list()
    i: int = 0
    j: int = 0
    if start < 0:
        j = end
    elif end > len(user_list):
        i = start
        j = len(user_list)
    else:
        i = start
        j = end
    while i < j:
        sub_list.append(user_list[i])
        i += 1
    return sub_list
