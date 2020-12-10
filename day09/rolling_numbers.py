from typing import Iterable, Sequence
import numpy as np


class NumberRoller:
    def __init__(self, preamble: Sequence[int]):
        self._numbers = np.array(preamble)
        self._sum_matrix = self.get_sum_matrix()

    def get_sum_matrix(self):
        rep_1, rep_2 = np.meshgrid(self._numbers, self._numbers)

        equals = rep_1 == rep_2
        result = rep_1 + rep_2
        result[equals] = -1

        return result

    def is_valid_number(self, number: int) -> bool:
        return np.any(number == self._sum_matrix)

    def update_number(self, number: int):
        self._update_numbers_array(number)
        self._update_sum_matrix(number)

    def find_first_invalid_number(self, numbers: Iterable[int]) -> int:
        for next_number in numbers:
            if self.is_valid_number(next_number):
                self.update_number(next_number)
            else:
                return next_number
        raise ValueError("Did not find an invalid number!")

    def _update_numbers_array(self, number: int):
        self._numbers = np.roll(self._numbers, -1)
        self._numbers[-1] = number

    def _update_sum_matrix(self, number: int):
        new_mat = np.roll(self._sum_matrix, shift=-1, axis=(0, 1))

        new_vals = self._numbers + number
        new_vals[self._numbers == number] = -1

        new_mat[-1, :] = new_vals
        new_mat[:, -1] = new_vals

        self._sum_matrix = new_mat
