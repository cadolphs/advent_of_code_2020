from day06.day06 import (
    all_shared_letters_in_strings,
    split_block_to_lines,
    split_input_to_blocks,
    sum_all_unique,
    unique_letters_in_strings,
)


def test_single_string():
    test_string = "abcdefg"

    assert len(test_string) == unique_letters_in_strings([test_string])


def test_two_disjoint_strings():
    test_strings = ["abc", "def"]
    assert 6 == unique_letters_in_strings(test_strings)


def test_two_identical_strings():
    test_strings = ["abc"] * 3
    assert 3 == unique_letters_in_strings(test_strings)


def test_split_input_to_blocks():
    test = "foo\n\nbar\nbaz\n\nbla"

    blocks = split_input_to_blocks(test)

    expected = ["foo", "bar\nbaz", "bla"]
    assert expected == blocks


def test_split_block_into_lines():
    test = "bar\nbaz"
    lines = split_block_to_lines(test)
    expected = ["bar", "baz"]

    assert expected == lines


def test_puzzle_example():
    test = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"

    expected = 11
    result = sum_all_unique(test)

    assert expected == result


def test_all_shared_single_string():
    test = "abc"
    expected = 3
    assert expected == all_shared_letters_in_strings([test])


def test_all_shared_letters_disjoint():
    test = ["abc", "def"]
    expected = 0

    assert expected == all_shared_letters_in_strings(test)


def test_some_overlap():
    test = ["abc", "bcde", "be"]
    expected = 1

    assert expected == all_shared_letters_in_strings(test)