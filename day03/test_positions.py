from day03.positions import positions


def test_positions_generator():
    pos = positions(start=(0, 0), direction=(3, 1), max_row=2)

    expected = [(0, 0), (3, 1)]

    assert expected == list(pos)

    pos = positions(start=(0, 0), direction=(3, 1), max_row=3)
    expected = [(0, 0), (3, 1), (6, 2)]

    assert expected == list(pos)
