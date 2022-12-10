"""Dictionary related utility functions."""

__author__ = "730604615"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv of a 'table'."""
    result: list[dict[str, str]] = list()
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
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


def head(row_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if n >= len(row_table):
        return row_table
    else:
        for row in row_table:
            count: int = 0
            row_list: list[str] = []
            while count < n:
                row_list.append(row_table[row][count])
                count += 1
            result[row] = row_list
    return result


def select(row_table: dict[str, list[str]], list_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for col in list_names:
        result[col] = row_table[col]
    return result


def concat(col_table1: dict[str, list[str]], col_table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines 2 different column-based tables."""
    result: dict[str, list[str]] = {}
    for col in col_table1:
        result[col] = col_table1[col]
    for col in col_table2:
        if col in result:
            result[col] += col_table2[col]
        else:
            result[col] = col_table2[col]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Given list[str], returns a dict displaying the # of each unique value."""
    result: dict[str, int] = {}
    for i in values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result