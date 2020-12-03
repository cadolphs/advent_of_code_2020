import numpy as np

from day03.map_parser import parse_map


def test_simple_parse():
    map_str = ".#.\n..#\n##."

    arr = parse_map(map_str)

    expected = np.array(
        [[False, True, False], [False, False, True], [True, True, False]]
    ).T

    assert np.all(expected == arr)