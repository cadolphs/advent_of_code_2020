import numpy as np


def parse_map(map_string: str) -> np.ndarray:
    lines = map_string.split("\n")
    num_row = len(lines)
    num_cols = len(lines[0])

    arr = np.zeros((num_row, num_cols), dtype=bool)

    for i, row in enumerate(lines):
        arr[i] = row_to_array(row)

    return arr.T


def row_to_array(row):
    return np.array([entry == "#" for entry in row])
