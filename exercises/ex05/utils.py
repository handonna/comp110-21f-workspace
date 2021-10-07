"""List utility functions part 2."""

__author__ = "730400224"

# Define your functions below


def only_evens(list1: list[int]) -> list:
    """Return list containing only even elements of the input list."""
    i: int = 0
    list2: list[int] = []
    while i < len(list1):
        if list1[i] % 2 == 0:
            list2.append(list1[i])
        i += 1
    return list2


def sub(list1: list[int], start: int, stop: int) -> list:
    """Given a list of ints, start index, and end index, generate list between indexes. """
    list2: list[int] = []
    i: int = 0
    if i == len(list1): 
        return list2
    elif start > len(list1): 
        return list2
    elif stop <= i:
        return list2
    else: 
        while  start < stop:
            start < len(list1)
            list2.append(list1[start])
            start += 1
        return list2


def concat(list1: list[int], list2: list[int]) -> list:
    """Given two lists of ints, makes new list with elements of first list followed by elements of second list."""
    listnew: list[int] = []
    k: int = 0
    p: int = 0
    while k < len(list1):
        if k < len(list1):
            listnew.append(list1[k]) 
        k += 1
    while p < len(list2):
        if p < len(list2):
            listnew.append(list2[p])
        p += 1
    return listnew