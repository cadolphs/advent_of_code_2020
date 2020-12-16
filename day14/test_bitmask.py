from day14.bitmask import BitMask


def test_setting_single_bit_to_1():

    bitmask = BitMask("XXXX1")

    my_int = 2
    assert 3 == bitmask.apply(my_int)

    bitmask = BitMask("1XXXX")
    my_int = 2
    assert 18 == bitmask.apply(my_int)


def test_setting_single_but_to_0():
    bitmask = BitMask("XXX0X")

    assert 1 == bitmask.apply(3)


def test_general_setting():
    bitmask = BitMask("XXX01")
    assert 1 == bitmask.apply(2)


def test_repr():
    bitmask = BitMask("X11X001")
    assert repr(bitmask) == 'BitMask("X11X001")'