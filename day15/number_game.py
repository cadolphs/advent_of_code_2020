from typing import DefaultDict, Iterable
from day15.tracked_number import TrackedNumber


class NumberGame:
    def __init__(self, starting_numbers: Iterable[int]):
        self._starting_numbers = starting_numbers
        self._numbers = DefaultDict(TrackedNumber)
        self._last_said_number = None

    def __iter__(self):
        for turn, number in enumerate(self._starting_numbers, start=1):
            self._numbers[number].say(turn)

            yield number
        self._turn = len(self._starting_numbers)
        self._last_said_number = self._starting_numbers[-1]

        while True:
            self._turn += 1
            number_to_say = self._numbers[self._last_said_number].get_number_to_say()
            self._numbers[number_to_say].say(turn=self._turn)
            self._last_said_number = number_to_say
            yield number_to_say

    @classmethod
    def get_nth_number(cls, starting_numbers: Iterable[int], n: int) -> int:
        game = iter(cls(starting_numbers=starting_numbers))
        # Skip first n-1
        for _ in range(n - 1):
            next(game)
        return next(game)
