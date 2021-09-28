from conway import neighbors, update_game
from itertools import product
from read_input import read_input


def test_neighbors():
    res = neighbors((0,0,0))
    all_points = set(product((-1,0,1), repeat=3)) - {(0,0,0)}
    assert res == all_points
    assert len(all_points) == 26


def test_simple_step():
    live_points = {(0, 1, 0), (1, 0, 0), (-1,-1,0),(0,-1,0),(1,-1,0)}

    new_points = update_game(live_points)

    expected = {(-1,1,-1), (1,0,-1), (0,-1,-1),
                (-1,1,0),(1,1,0),(0,0,0),(1,0,0),(0,-1,0),
                (-1,1,1),(1,0,1),(0,-1,1)}

    assert len(new_points) == 11
    assert expected == new_points


def test_read_input():
    input_str = """.#.
..#
###"""

    points = read_input(input_str)
    expected = {(0, 1, 0), (1, 0, 0), (-1,-1,0),(0,-1,0),(1,-1,0)}

    assert expected == points