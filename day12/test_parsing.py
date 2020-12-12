from day12.parsing import parse_line
from hypothesis import given
import hypothesis.strategies as some


@given(some.sampled_from("LRNESWF"), some.integers(min_value=0))
def test_parse_line(dir, amount):
    line = f"{dir}{amount}"
    assert (dir, amount) == parse_line(line)
