"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730400224"


def test_only_evens_no_evens() -> None:
    """Edge Case, No evens are in the list and should result in empty list."""
    list1: list[int] = [1, 3, 5, 7]
    assert only_evens(list1) == []


def test_only_evens_some_evens() -> None:
    """Use Case, Some evens are in the list."""
    list1: list[int] = [10, 11, 12, 13, 14, 15]
    assert only_evens(list1) == [10, 12, 14]


def test_only_evens_some_evens_again() -> None:
    """Use Case, Some evens are in the list."""
    list1: list[int] = [60, 61, 62, 63, 64, 65, 66]
    assert only_evens(list1) == [60, 62, 64, 66]


def test_sub_length_of_list_is_zero() -> None:
    """Edge Case, given list has zero elements, should result in empty list."""
    list1: list[int] = []
    assert sub(list1, 2, 4) == []


def test_sub_random_numbers() -> None:
    """Use Case, subset of list using random numbers."""
    list1: list[int] = [0, 1, 2, 3, 4, 5]
    assert sub(list1, 1, 3) == [1, 2]


def test_sub_random_numbers_again() -> None:
    """Use Case, subset of list using random numbers."""
    list1: list[int] = [10, 20, 30, 40, 50]
    assert sub(list1, 1, 4) == [20, 30, 40]


def test_concat_one_list_is_empty() -> None:
    """Edge Case, one of the lists are empty."""
    list1: list[int] = [1, 2, 3, 4]
    list2: list[int] = []
    assert concat(list1, list2) == [1, 2, 3, 4]


def test_concat_random_numbers() -> None:
    """Use Case, concatenated list with random numbers."""
    list1: list[int] = [20, 21, 22, 23]
    list2: list[int] = [24, 25, 26, 27]
    assert concat(list1, list2) == [20, 21, 22, 23, 24, 25, 26, 27]


def test_concat_random_numbers_again() -> None:
    """Edge Case, concatenated list with random numbers."""
    list1: list[int] = [10, 20, 30, 40, 50]
    list2: list[int] = [60, 70, 80, 90, 100]
    assert concat(list1, list2) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]