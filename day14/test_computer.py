from day14.computer import Memory
from hypothesis import given
import hypothesis.strategies as some


@given(some.integers(min_value=0, max_value=2 ** 36 - 1))
def test_init_memory(index):
    mem = Memory()

    assert 0 == mem[index]


@given(
    some.integers(min_value=0, max_value=2 ** 36 - 1),
    some.integers(min_value=1, max_value=2 ** 36 - 1),
)
def test_set_and_unset_memory(index, val):
    mem = Memory()
    mem[index] = val

    assert mem[index] == val

    assert index in mem.keys()
    assert (index, val) in mem.items()

    mem[index] = 0

    assert 0 == len(list(mem.keys()))
