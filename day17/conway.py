from itertools import chain, product
from typing import List, Set, Tuple


def add_tuples(x, y):
    return tuple(xi + yi for xi, yi in zip(x,y))


def neighbors(point: Tuple[int, ...]) -> Set[Tuple[int, ...]]:
    dim = len(point)
    return {add_tuples(point, delta) for delta in product((-1, 0, 1), repeat=dim)} - {point}


def all_neighbors(points: Set[Tuple[int,...]]) -> Set[Tuple[int, ...]]:
    return set(chain.from_iterable(neighbors(point) for point in points))


def cubes_that_remain_active(live_points: Set[Tuple[int, int, int]]) -> Set[Tuple[int, int, int]]:
    return {cube for cube in live_points if (2 <= len(neighbors(cube).intersection(live_points)) <= 3)}


def update_game(live_points: Set[Tuple[int, ...]]) -> Set[Tuple[int, ...]]:
    inactive_neighbors = all_neighbors(live_points).difference(live_points)

    newly_active_cubes = {cube for cube in inactive_neighbors if len(neighbors(cube).intersection(live_points)) == 3}

    return center_frame(cubes_that_remain_active(live_points).union(newly_active_cubes))


def update_n_steps(live_points: Set[Tuple[int, int, int]], n: int) -> Set[Tuple[int, int, int]]:
    if n < 1:
        raise ValueError("Can't run less than 1 steps")

    for _ in range(n):
        live_points = update_game(live_points)

    return live_points


def center_frame(points: Set[Tuple[int, ...]]) -> Set[Tuple[int, ...]]:
    dim = len(next(iter(points)))
    deltas = [0] * dim
    for pos in range(dim):
        min_val = min(point[pos] for point in points)
        max_val = max(point[pos] for point in points)

        deltas[pos] = -(min_val + max_val) // 2

    return {add_tuples(point, deltas) for point in points}
