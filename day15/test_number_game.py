from day15.number_game import NumberGame
import pytest


def test_number_game_says_starting_numbers():
    starting_numbers = [0, 3, 6]
    game = NumberGame(starting_numbers)

    for expected, said in zip(starting_numbers, game):
        assert expected == said


def test_after_starting_number_keeps_track():
    starting_numbers = [0, 3, 6]
    game = NumberGame(starting_numbers)

    expected = [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]

    for expected, said in zip(starting_numbers, game):
        assert expected == said


def test_get_nth_easy():
    start_numbers = [0, 3, 6]
    assert 3 == NumberGame.get_nth_number(start_numbers, n=2)


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
    assert expected_nth == NumberGame.get_nth_number(starting_numbers, n=n)
