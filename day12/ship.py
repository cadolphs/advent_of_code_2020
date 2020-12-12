from abc import ABC, abstractmethod
from dataclasses import dataclass
from day12.parsing import parse_line


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def l1_norm(self):
        return abs(self.x) + abs(self.y)

    def rotate(self, direction: str, degrees: int):
        if (degrees % 90) != 0:
            raise ValueError("Only multiples of 90 allowed.")
        if direction not in "LR":
            raise ValueError("Direction must be L or R.")

        dir_index_east = DirectionIndices["E"]

        num_steps = degrees // 90
        step_direction = 1 if direction == "R" else -1

        new_index_east = (dir_index_east + num_steps * step_direction) % 4

        dir_x = Directions[new_index_east]

        if dir_x == "E":
            # (E/N)
            return Vector(self.x, self.y)
        elif dir_x == "N":
            # (N/W)
            return Vector(-self.y, self.x)
        elif dir_x == "W":
            # (W/S)
            return Vector(-self.x, -self.y)
        elif dir_x == "S":
            # (S/E)
            return Vector(self.y, -self.x)

        assert False, "We should never get here."


Direction = dict(
    N=Vector(0, 1),
    E=Vector(1, 0),
    S=Vector(0, -1),
    W=Vector(-1, 0),
)

DirLookup = {value: key for key, value in Direction.items()}

Directions = ["N", "E", "S", "W"]
DirectionIndices = dict(zip(Directions, range(4)))


class AbstractShip(ABC):
    def __init__(self):
        self._pos = Vector(0, 0)
        self._dir = "E"
        self._post_init()

    # Override in child-classes if desired
    def _post_init(self):
        pass

    # Override in child-classes
    def _extra_info(self):
        return ""

    @property
    def pos(self):
        return self._pos

    def __str__(self):
        extra_info = self._extra_info()
        return f"Located at ({self._pos.x}, {self._pos.y}).{extra_info}"

    def execute(self, action):
        dir, amount = parse_line(action)
        """Again, in _general_ these sorts of type codes can be a code smell
        and might benefit from refactoring to use classes and polymorphism.
        Here I see little value in that. The benefit of using classes is that it makes
        the architecture more extensible. That's why I did it for the computer
        exercise, as I expect more Instruction types to pop up in the future.
        Here I don't expect a ton of new directions to pop up in the future!"""
        if dir in "LR":
            self.turn(dir, amount)
        elif dir in Directions:
            self.move_by(dir, amount)
        elif dir == "F":
            self.forward(amount)

    def get_manhatten_from_origin(self):
        return self._pos.l1_norm()

    @abstractmethod
    def forward(self, count: int):
        pass

    @abstractmethod
    def move_by(self, direction: str, count: int):
        pass

    @abstractmethod
    def turn(self, direction: str, degrees: int):
        pass


class Ship(AbstractShip):
    def _post_init(self):
        self._dir = "E"

    def _extra_info(self):
        return f" Facing ({self._dir}."

    @property
    def dir(self):
        return self._dir

    def forward(self, count: int):
        self.move_by(count=count, direction=self._dir)

    def move_by(self, direction: str, count: int):
        self._pos += Direction[direction] * count

    def turn(self, direction: str, degrees: int):
        dir_vec = Direction[self._dir]
        new_dir_vec = dir_vec.rotate(direction, degrees)
        self._dir = DirLookup[new_dir_vec]


class ShipAndWaypoint(AbstractShip):
    @property
    def waypoint(self):
        return self._waypoint

    def _post_init(self):
        self._waypoint = Vector(10, 1)

    def _extra_info(self):
        return f" Waypoint is {(self._waypoint.x, self.waypoint.y)} from Ship."

    def forward(self, count: int):
        self._pos += count * self._waypoint

    def turn(self, direction: str, degrees: int):
        self._waypoint = self._waypoint.rotate(direction, degrees)

    def move_by(self, direction: str, count: int):
        self._waypoint += Direction[direction] * count
