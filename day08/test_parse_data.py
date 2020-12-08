from day08.parse_data import parse_line
import pytest


def test_nothing():
    assert ("nop", 0) == parse_line("nop +0")


def test_error():
    with pytest.raises(ValueError):
        parse_line("nop +0 -1")