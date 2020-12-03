from day03.right_cyclical_array import RightCyclicalArray
from unittest.mock import MagicMock


def test_check_items():
    input_array = MagicMock()
    input_array.shape = (3, 4)

    array = RightCyclicalArray(input_array)

    array[0, 0]
    input_array.__getitem__.assert_called_with((0, 0))

    array[10, 2]
    input_array.__getitem__.assert_called_with((1, 2))
