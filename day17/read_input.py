from typing import Set, Tuple
from conway import center_frame


def read_input(input_str: str, dim=3) -> Set[Tuple[int,...]]:
    points = set()
    lines = input_str.splitlines()

    def pad_extra_dim(point):
        zeros = [0] * dim
        zeros[0] = point[0]
        zeros[1] = point[1]
        return tuple(zeros)

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                points.add(pad_extra_dim((col, -row)))

    return center_frame(points)