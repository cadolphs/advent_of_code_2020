from expense_check import expense_check, InvalidInputException
import pytest

# Let's start with tests. But usefully and proactively,
# And just in a way that exposes a good interface, maybe.

# We expect that we have a list of integers and we'll find
# the product of two numbers that add up to 2020.

# We assume that there _is_ such a pair.


def test_only_two_numbers_works():
    test_list = [1010, 1010]
    expected_result = 1010 ** 2

    result = expense_check(test_list)

    assert expected_result == result


def test_numbers_that_donot_work():
    test_list = [1, 2]
    with pytest.raises(InvalidInputException):
        expense_check(test_list)


# This test will fail first because `expense_check` doesn't exist.
# I will implement it. And then I will have to write the algo.

# I don't think TDD will be useful for the algo itself, really...

# Just using iterators ;)

# Okay so what's next? Now it's about three lists. Simple refactoring...
# Add argument for number of checks.


def test_three_numbers():
    test_list = [2000, 15, 5]
    expected_result = 2000 * 15 * 5

    result = expense_check(test_list, num_numbers=3)

    assert expected_result == result