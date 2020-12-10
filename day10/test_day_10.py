from day10.run_day_10 import (
    count_joltage_diffs,
    count_joltage_paths,
    make_joltage_chain,
)
import pytest


@pytest.fixture
def example_input():
    return [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


@pytest.fixture
def large_input():
    return [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]


def test_make_joltage_chain(example_input):
    joltages = make_joltage_chain(example_input)

    expected = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]

    assert expected == joltages


def test_count_diffs(example_input):
    joltages = make_joltage_chain(example_input)

    diff_counter = count_joltage_diffs(joltages)

    assert 7 == diff_counter[1]
    assert 5 == diff_counter[3]


def test_large_example(large_input):
    joltages = make_joltage_chain(large_input)
    diff_counter = count_joltage_diffs(joltages)

    assert 22 == diff_counter[1]
    assert 10 == diff_counter[3]


def test_small_path_counter(example_input):
    joltages = make_joltage_chain(example_input)

    assert 8 == count_joltage_paths(joltages)


def test_large_path_counter(large_input):
    joltages = make_joltage_chain(large_input)

    assert 19208 == count_joltage_paths(joltages)