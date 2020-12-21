import numpy as np
from typing import Iterable
from numba import njit, jit


@njit()
def get_nth_number(starting_numbers: Iterable[int], n: int) -> int:
    if n <= len(starting_numbers):
        return starting_numbers[n - 1]

    size_of_array = max(max(starting_numbers), n) + 2
    memory = np.zeros(size_of_array, dtype=np.int32)

    num_starts = len(starting_numbers)
    for turn in range(1, num_starts):
        memory[starting_numbers[turn - 1]] = turn

    last_said_number = starting_numbers[-1]

    for turn in range(len(starting_numbers) + 1, n + 1):
        last_seen = memory[last_said_number]
        if last_seen == 0:
            number_to_say = 0
        else:
            number_to_say = turn - last_seen - 1

        memory[last_said_number] = turn - 1
        last_said_number = number_to_say

    return last_said_number
