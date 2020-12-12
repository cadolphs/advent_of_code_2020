from abc import ABC, abstractmethod
import numpy as np
from itertools import product

FLOOR = 0
EMPTY = 1
OCCUPIED = 2

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


class AbstractSeatingPlan(ABC):
    def __init__(self, array):
        # Could add validation here, like does it only contain 0, 1, 2.
        self._array = array

    def num_occupied(self):
        return np.sum(self._array == OCCUPIED)

    def __eq__(self, other):
        try:
            return np.array_equal(self._array, other._array)
        except AttributeError:
            return False

    def __str__(self):
        return str((self._array[1:-1, 1:-1].astype(int))).translate(
            str.maketrans("012", ".L#", " []")
        )

    @classmethod
    def from_string(cls, data: str) -> "SeatingPlan":
        lines = data.split("\n")
        N = len(lines)
        M = len(lines[0])
        array = np.zeros((N + 2, M + 2))

        for i, line in enumerate(lines):
            array[i + 1, 1:-1] = cls.parse_line(line)

        return cls(array)

    @staticmethod
    def parse_line(line: str):
        line_as_numbers = line.translate(
            str.maketrans(".L#", f"{FLOOR}{EMPTY}{OCCUPIED}", "")
        )
        return np.array([int(c) for c in line_as_numbers])

    def step_until_stable(self):
        current = self
        while (new_plan := current.step()) != current:
            current = new_plan

        return current

    # Implement this in child class:
    @abstractmethod
    def step(self):
        pass


class SeatingPlan(AbstractSeatingPlan):
    def step(self):

        central_view = self._array[1:-1, 1:-1]
        views = [
            self._array[0:-2, 1:-1],
            self._array[2:, 1:-1],
            self._array[1:-1, 0:-2],
            self._array[1:-1, 2:],
            self._array[0:-2, 0:-2],
            self._array[0:-2, 2:],
            self._array[2:, 2:],
            self._array[2:, 0:-2],
        ]

        new_array = np.array(self._array)

        # Logical array for seats that are occupied and four or more adjacent seats are occupied:
        num_adj_occupied = sum(view == OCCUPIED for view in views)

        occupied_seats_to_flip = (central_view == OCCUPIED) & (num_adj_occupied >= 4)
        empty_seats_to_flip = (central_view == EMPTY) & (num_adj_occupied == 0)

        (new_array[1:-1, 1:-1])[occupied_seats_to_flip] = EMPTY
        (new_array[1:-1, 1:-1])[empty_seats_to_flip] = OCCUPIED

        return SeatingPlan(new_array)


class SeatingPlan2(AbstractSeatingPlan):
    def step(self):
        new_array = np.array(self._array)

        for pos in product(range(self._array.shape[0]), range(self._array.shape[1])):
            new_array[pos] = self._update_pos(pos)

        return SeatingPlan2(new_array)

    def _update_pos(self, pos):
        val = self._array[pos]
        if val == FLOOR:
            return FLOOR
        elif val == EMPTY:
            return (
                OCCUPIED
                if all(
                    self._count_visible_in_direction(direction, pos, OCCUPIED) == 0
                    for direction in directions
                )
                else EMPTY
            )
        elif val == OCCUPIED:
            occ = 0
            for i, direction in enumerate(directions):
                occ += self._count_visible_in_direction(direction, pos, OCCUPIED)

                if occ >= 5:
                    return EMPTY
                # if current occupied plus all remaining potentials is less than 5, cant' possibly make it
                if occ + 7 - i < 5:
                    return OCCUPIED
            return OCCUPIED
        raise ValueError()

    def _count_visible(self, pos, val):
        # All right, this is the annoying part.

        return sum(
            self._count_visible_in_direction(direction, pos, val)
            for direction in directions
        )

    def _count_visible_in_direction(self, direction, pos, val):
        def _is_valid(pos):
            return (
                0 <= pos[0] < self._array.shape[0]
                and 0 <= pos[1] < self._array.shape[1]
            )

        while _is_valid(pos := (pos[0] + direction[0], pos[1] + direction[1])):
            if self._array[pos] == val:
                return 1
            elif self._array[pos] != FLOOR:
                # It's not the type of seat we want but it's not the floor either
                return 0
        return 0
