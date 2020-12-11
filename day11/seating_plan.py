import numpy as np

FLOOR = 0
EMPTY = 1
OCCUPIED = 2


class SeatingPlan:
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
        return str(self._array[1:-1, 1:-1]).translate(str.maketrans("012", ".L#"))

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

    def step_until_stable(self):
        current = self
        while (new_plan := current.step()) != current:
            current = new_plan

        return current
