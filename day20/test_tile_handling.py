import numpy as np

from tile_handling import Tile


def test_simple_loading():
    input_str = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###"""

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