from typing import List, Set, Tuple


def neighbors(point: Tuple[int, int, int]) -> Set[Tuple[int, int, int]]:
    x, y, z = point
    return {(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z-1), (x, y, z+1)}