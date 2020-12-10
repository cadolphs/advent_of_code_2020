from day09.rolling_numbers import NumberRoller
import numpy as np


def test_build_initial_matrix():
    preamble = [1, 2, 3, 4, 5]

    roller = NumberRoller(preamble)

    mat = roller.get_sum_matrix()

    # There is a more elegant way to do this but this is a test.
    expected = np.empty((5, 5))
    for i in range(1, 6):
        for j in range(1, 6):
            expected[i - 1, j - 1] = i + j if i != j else -1

    assert np.all(expected == mat)


def test_is_valid_number():
    preamble = [1, 2, 3, 4, 5]
    roller = NumberRoller(preamble)

    valids = [3, 4, 5, 6, 7, 8, 9]
    invalids = [1, 2, 10, 11]

    for valid in valids:
        assert roller.is_valid_number(valid)

    for invalid in invalids:
        assert not roller.is_valid_number(invalid)


def test_update_number():
    roller = NumberRoller([1, 2, 3, 4, 5])

    roller.update_number(7)

    # Compute expected matrix "by hand"
    another_roller = NumberRoller([2, 3, 4, 5, 7])
    expected = another_roller.get_sum_matrix()

    assert np.all(expected == roller._sum_matrix)
