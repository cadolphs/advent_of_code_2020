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

    def border(self, side: int, direction: int) -> np.ndarray:
        """Return the border of the tile as a 1d vector with the given side, as seen from the given direction.

        From the standard orientation, this means
        side:
          0 - top
          1 - right
          2 - bottom
          3 - left
        direction:
          0 - rotate tile so side is at the right
          1 - rotate tile so side is at the left
        """
        res = None
        if side == 0:
            res = self.data[0, :]
        elif side == 1:
            res = self.data[:, -1]
        elif side == 2:
            res = self.data[-1, ::-1]
        elif side == 3:
            res = self.data[::-1, 0]
        if direction == 1:
            res = res[::-1]
        return res

    def matches(self, other: "Tile", side: int, other_side: int, alignment=1):
        assert alignment in {-1, 1}
        return np.alltrue(self.border(side, 0) == other.border(other_side, 1)[::alignment])


def parse_tile(lines: List[str]) -> np.ndarray:
    num_row = len(lines)
    num_cols = len(lines[0])

    arr = np.zeros((num_row, num_cols), dtype=bool)

    for i, row in enumerate(lines):
        arr[i] = row_to_array(row)

    return arr


def parse_input(input_str: str) -> List[Tile]:
    return [Tile.from_str(block) for block in input_str.split('\n\n')]


def row_to_array(row):
    return np.array([entry == "#" for entry in row])