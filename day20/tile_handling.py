import re
from typing import List
import numpy as np


class Tile:
    __slots__ = ["id", "data"]

    def __init__(self, id, data):
        self.id = id
        self.data = data

    @classmethod
    def from_str(cls, tile_str: str) -> "Tile":
        lines = tile_str.splitlines()

        # read header
        ans = re.findall(r"\d+", lines[0])[0]
        id = int(ans)

        data = parse_tile(lines[1:])
        return cls(id, data)


def parse_tile(lines: List[str]) -> np.ndarray:
    num_row = len(lines)
    num_cols = len(lines[0])

    arr = np.zeros((num_row, num_cols), dtype=bool)

    for i, row in enumerate(lines):
        arr[i] = row_to_array(row)

    return arr


def row_to_array(row):
    return np.array([entry == "#" for entry in row])