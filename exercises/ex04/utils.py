"""List utility functions."""

__author__ = "730400224"


# TODO: Implement your functions here.

def all(list: list[int], number: int) -> bool:
    """Return True is item is found in List, False otherwise."""
    i: int = 0
    j: int = 0
    while i < len(list):
        item: int = list[i]
        if item == number:
            j += 1
        i += 1
    if len(list) == 0:
        return False
    elif j == len(list):
        return True
    else:
        return False


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Return True is lists are equal, False otherwise."""
    if len(list_1) != len(list_2):
        return False
    else:
        i: int = 0
        j: int = 0
        while i < len(list_1):
            item1: int = list_1[i]
            item2: int = list_2[i]
            if item1 == item2:
                j += 1
            i += 1
        if j == len(list_1):
            return True
        elif j == len(list_2) or j == len(list_1):
            return False
        else:
            return False