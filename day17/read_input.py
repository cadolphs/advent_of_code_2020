from typing import Set, Tuple
from conway import center_frame


def read_input(input_str: str) -> Set[Tuple[int, int, int]]:
    points = set()
    lines = input_str.splitlines()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                points.add((col, -row, 0))

    return center_frame(points)