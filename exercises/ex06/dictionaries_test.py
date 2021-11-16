"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730400224"


def test_invert_edge_words() -> None:
    """Edge case, encounter more than one of same key."""
    dictionary: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(dictionary) == KeyError


def test_invert_random_letters() -> None:
    """Use case, random letters."""
    dictionary: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(dictionary) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_invert_random_words() -> None:
    """Use case, random words."""
    dictionary: dict[str, str] = {'apple': 'orange', 'banana': 'pear'}
    assert invert(dictionary) == {'orange': 'apple', 'pear': 'banana'}


def test_favorite_color_edge() -> None:
    """Edge case, two colors appear same amount of times."""
    dictionary: dict[str, str] = {'Jones': 'Blue', 'Steve': 'Blue', 'Eric': 'Red', 'Anna': 'Red'}
    assert favorite_color(dictionary) == 'Blue'


def test_favorite_color_random_colors() -> None:
    """Use case, random colors and names."""
    dictionary: dict[str, str] = {'Bob': 'Blue', 'Steve': 'Red', 'Eric': 'Blue'}
    assert favorite_color(dictionary) == 'Blue'


def test_favorite_color_random_colors_again() -> None:
    """Use case, random colors and names."""
    dictionary: dict[str, str] = {'Jared': 'Green', 'Lilly': 'Purple', 'Joe': 'Green'}
    assert favorite_color(dictionary) == 'Green'


def test_count_edge() -> None:
    """Edge Case, all items only appear once."""
    given_list: list[str] = ['a', 'b', 'c', 'd']
    assert count(given_list) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}


def test_count_random_list() -> None:
    """Use Case, using letters."""
    given_list: list[str] = ['a', 'b', 'c', 'a', 'b', 'd']
    assert count(given_list) == {'a': 2, 'b': 2, 'c': 1, 'd': 1}


def test_count_random_list_again() -> None:
    """Use Case, using words."""
    given_list: list[str] = ['apple', 'banana', 'apple', 'orange']
    assert count(given_list) == {'apple': 2, 'banana': 1, 'orange': 1}