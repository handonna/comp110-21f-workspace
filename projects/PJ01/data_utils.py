"""Utility functions."""

__author__ = "730400224"

# Define your functions below
from csv import DictReader

  
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce column based table with first N rows of data."""
    result: dict[str, list[str]] = {}
    if N >= len(table):
        N == len(table)
    for row in table:
        empty: list[str] = []
        for i in range(0, N):
            value: str = table[row][i]
            empty.append(value)
        result[row] = empty

    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Define new table with speciifc subsets."""
    result: dict[str, list[str]] = {}
    for row in names:
        result[row] = table[row]
    return result


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """New table from two tables combined."""
    result: dict[str, list[str]] = {}
    for column1 in dict1:
        result[column1] = dict1[column1]
    for column2 in dict2:
        if column2 in result:
            for item in dict2[column2]:
                result[column2].append(item)
        result[column2] = dict2[column2]
    return result


def count(values: list[str]) -> dict[str, int]:
    """"Number of times value is in output list."""
    frequency: dict[str, int] = {}
    for i in values:
        if i in frequency.keys():
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency


def add(total1: int, total2: int) -> int:
    """Return addition of two integers."""
    total = total1 + total2
    return total
