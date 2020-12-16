from day14.bitmask import IndexBitMask
from day14.memory import FloatingMemory


def test_sets_all():
    mem = FloatingMemory()
    mask = IndexBitMask("10X")

    mem.mask = mask

    mem[2] = 42

    # 2 is 0b10, so mask generates 110 and 111 = 6 and 7

    assert {(6, 42), (7, 42)} == set(mem.items())
