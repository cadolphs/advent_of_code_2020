from day03.positions import positions
from day03.right_cyclical_array import RightCyclicalArray
from day03.map_parser import parse_map
from day03.run_day03 import count_trees


def test_counting():
    map_str = ".#.\n..#\n##."
    arr = parse_map(map_str)
    tree_map = RightCyclicalArray(arr)

    poss = positions((0, 0), (3, 1), 3)

    # Positions will be (0,0), (1,3), (2,6)
    # No tree at (0,0)
    # No tree at (1,3) == (1,0)
    # One tree at (2, 6) == (2, 0)

    assert 1 == count_trees(tree_map, poss)