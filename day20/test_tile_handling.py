import numpy as np
import pytest
from tile_handling import Tile

@pytest.fixture
def input_str():
    return ("Tile 2311:\n"
            "..##.#..#.\n"
            "##..#.....\n"
            "#...##..#.\n"
            "####.#...#\n"
            "##.##.###.\n"
            "##...#.###\n"
            ".#.#.#..##\n"
            "..#....#..\n"
            "###...#.#.\n"
            "..###..###")


def test_simple_loading(input_str):
    expected_array = np.array([[0,0,1,1,0,1,0,0,1,0],
                               [1,1,0,0,1,0,0,0,0,0],
                               [1,0,0,0,1,1,0,0,1,0],
                               [1,1,1,1,0,1,0,0,0,1],
                               [1,1,0,1,1,0,1,1,1,0],
                               [1,1,0,0,0,1,0,1,1,1],
                               [0,1,0,1,0,1,0,0,1,1],
                               [0,0,1,0,0,0,0,1,0,0],
                               [1,1,1,0,0,0,1,0,1,0],
                               [0,0,1,1,1,0,0,1,1,1]], dtype=bool)

    expected_id = 2311

    tile = Tile.from_str(input_str)
    assert tile.id == expected_id
    assert np.alltrue(tile.data == expected_array)


def test_border(input_str):
    tile = Tile.from_str(input_str)
    expected_top = np.array([0,0,1,1,0,1,0,0,1,0])
    expected_bottom = np.array([1,1,1,0,0,1,1,1,0,0])
    expected_left = np.array([0,1,0,0,1,1,1,1,1,0])
    expected_right = np.array([0,0,0,1,0,1,1,0,0,1])

    assert np.alltrue(expected_top == tile.border(side=0, direction=0))
    assert np.alltrue(expected_right == tile.border(side=1, direction=0))
    assert np.alltrue(expected_bottom == tile.border(side=2, direction=0))
    assert np.alltrue(expected_left == tile.border(side=3, direction=0))

    assert np.alltrue(expected_top[::-1] == tile.border(side=0, direction=1))
    assert np.alltrue(expected_right[::-1] == tile.border(side=1, direction=1))
    assert np.alltrue(expected_bottom[::-1] == tile.border(side=2, direction=1))
    assert np.alltrue(expected_left[::-1] == tile.border(side=3, direction=1))