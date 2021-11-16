"""Practice with dictionaries."""

__author__ = "730400224"

# Define your functions below


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Return dictionary that inverts keys and values."""
    inverted: dict[str, str] = {}
    for key in dictionary:
        inverted[dictionary[key]] = key
    return inverted


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns color that appears most frequently."""
    colors: list[str] = []
    numbers: list[int] = []
    colors_2: list[str] = []
    k: int = 0
    j: int = 0
    for key in dictionary:
        colors.append(dictionary[key])
    for color in colors:
        i: int = 0
        for color_2 in colors_2:
            if color == colors_2:
                i += 1
        numbers.append(i)
    maximum: int = max(numbers)
    for number in numbers:
        if number == maximum:
            j = k
        k += 1
    return colors[j]


def count(given_list: list[str]) -> dict[str, int]:
    """Key is unique value and each value associated is the count of times that value appeared in list."""
    result: dict[str, int] = {}
    for item in given_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return (result)