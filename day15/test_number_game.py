from day15.number_game import get_nth_number
import pytest


def test_get_nth_easy():
    start_numbers = [0, 3, 6]
    assert 3 == get_nth_number(start_numbers, n=2)


def test_another_test():
    # 0, 3, 6 | 0, 3, 3, 1
    start_numbers = [0, 3, 6]
    assert 0 == get_nth_number(start_numbers, n=4)
    assert 3 == get_nth_number(start_numbers, n=5)
    assert 3 == get_nth_number(start_numbers, n=6)
    assert 1 == get_nth_number(start_numbers, n=7)


@pytest.mark.parametrize(
    ("starting_numbers", "n", "expected_nth"),
    [
        ([0, 3, 6], 2020, 436),
        ([1, 3, 2], 2020, 1),
        ([2, 1, 3], 2020, 10),
        ([1, 2, 3], 2020, 27),
        ([2, 3, 1], 2020, 78),
        ([3, 2, 1], 2020, 438),
        ([3, 1, 2], 2020, 1836),
    ],
)
def test_example_input(starting_numbers, n, expected_nth):
    assert expected_nth == get_nth_number(starting_numbers, n=n)
