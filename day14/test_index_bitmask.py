from day14.bitmask import IndexBitMask


def test_ones_override_with_1():
    mask = IndexBitMask("0001")

    result = mask.apply(0b10)

    expected = [0b11]

    assert expected == result


def test_zeros_leave_stuff():
    mask = IndexBitMask("0000")

    assert [0b11011] == mask.apply(0b11011)


def test_x_floats():
    mask = IndexBitMask("10X")

    result = mask.apply(0b010)

    expected = {0b110, 0b111}

    assert expected == set(result)


def test_larger_x():
    mask = IndexBitMask("XX")
    result = mask.apply(0b11)  # Doesn't really matter
    expected = set(range(4))

    assert expected == set(result)