from day09.sequence_finder import RangeFinder


def test_range_finder_immediately():
    numbers = [10, 32]
    finder = RangeFinder(numbers, 42)

    assert (0, 1) == finder.find_range()


def test_range_finder_purely_by_increasing():
    numbers = [1, 2, 3]
    finder = RangeFinder(numbers, 6)

    assert (0, 2) == finder.find_range()


def test_range_finder_bumping_left_once():
    numbers = [1, 2, 3]
    finder = RangeFinder(numbers, 5)

    assert (1, 2) == finder.find_range()


def test_range_finder_bumping_left_a_few_times():
    numbers = [1, 2, 3, 4]
    finder = RangeFinder(numbers, 7)

    assert (2, 3) == finder.find_range()


def test_range_back_and_forth():
    numbers = [5, 4, 3, 2, 1, 4]
    finder = RangeFinder(numbers, 6)

    assert (2, 4) == finder.find_range()


def test_puzzle_input():
    numbers = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        57,
    ]

    low, high = RangeFinder.find_number_in_range(numbers, 127)
    assert 15 == min(numbers[low : high + 1])
    assert 47 == max(numbers[low : high + 1])
