from day05.day05 import compute_checksum, translate_problem_input, translate_string
import pytest


def test_translate_string():
    zero_letter = "F"
    one_letter = "B"

    test_string = "FBBFFBF"
    expected = "0110010"

    assert expected == translate_string(test_string, zero_letter, one_letter)


@pytest.mark.parametrize(
    "test_input, expected, seat_id",
    [
        ("FBFBBFFRLR", (44, 5), 357),
        ("BFFFBBFRRR", (70, 7), 567),
        ("FFFBBBFRRR", (14, 7), 119),
        ("BBFFBBFRLL", (102, 4), 820),
    ],
)
def test_problem_input(test_input, expected, seat_id):
    assert expected == translate_problem_input(test_input)
    assert seat_id == compute_checksum(expected)
