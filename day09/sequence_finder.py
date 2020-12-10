from typing import Sequence


class RangeFinder:
    def __init__(self, numbers: Sequence[int], number: int):
        self.number = number
        self._numbers = numbers

        self.left = 0
        self.right = 1

        self._sum = numbers[0] + numbers[1]

    @property
    def sum(self):
        return self._sum

    def find_range(self):
        while self._sum != self.number:
            if self._sum < self.number:
                self._increment_right()
            else:
                self._increment_left()

        return (self.left, self.right)

    def _increment_right(self):
        self.right += 1
        self._sum += self._numbers[self.right]

    def _increment_left(self):
        self._sum -= self._numbers[self.left]
        self.left += 1
        if self.left == self.right:
            self._reset_range()

    def _reset_range(self):
        self.right = self.left + 1
        self._sum = self._numbers[self.left] + self._numbers[self.right]

    @staticmethod
    def find_number_in_range(range, number):
        return RangeFinder(range, number).find_range()