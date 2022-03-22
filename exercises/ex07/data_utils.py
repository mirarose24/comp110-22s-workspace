"""Dictionary related utility functions."""

__author__ = "730440093"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # open a handle to the data file 
    file_handle = open(filename, "r", encoding="utf8")  # "r" = read
    
    # prepare to read the data file as a csv rather than just strings
    csv_reader = DictReader(file_handle)

    # read each row of the csv line-by-line
    for row in csv_reader:
        result.append(row)
    
    # close the file when we're done, to free its resources.
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


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first 'n' rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        length: int = len(table[column])
        i: int = 0
        if n >= length:
            for row in table[column]:
                values.append(row)
        else:
            while i < n:
                row = table[column][i]
                values.append(row)
                i += 1
        result[column] = values
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table w only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table[column]
    return result


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table w two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for columns in dict_1:
        result[columns] = dict_1[columns]
    for columns in dict_2:
        if columns in result:
            result[columns] += dict_2[columns]
        else:
            result[columns] = dict_2[columns]
    return result 


def count(values: list[str]) -> dict[str, int]: 
    """Given a list of values, this function will produce a count of the number of times a unique key appeared in the input list."""
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result