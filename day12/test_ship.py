from hypothesis.core import execute_explicit_examples
from day12.ship import Ship, Vector
from hypothesis import given
from hypothesis.strategies import integers, sampled_from


def test_forward():
    ship = Ship()
    ship.forward(5)

    assert ship.pos == Vector(5, 0)


def test_move_by():
    ship = Ship()
    ship.move_by("N", 4)
    assert ship.pos == Vector(0, 4)
    ship.move_by("W", 10)
    assert ship.pos == Vector(-10, 4)
    ship.move_by("E", 20)
    assert ship.pos == Vector(10, 4)
    ship.move_by("S", 4)
    assert ship.pos == Vector(10, 0)


def test_turn():
    ship = Ship()
    assert ship.dir == "E"

    ship.turn("L", 90)
    assert ship.dir == "N"

    ship.turn("R", 180)
    assert ship.dir == "S"

    ship.turn("L", 1080)
    assert ship.dir == "S"

    ship.turn("R", 270)
    assert ship.dir == "E"


@given(
    integers(min_value=0),
    integers(min_value=0),
    sampled_from(["N", "S"]),
    sampled_from(["E", "W"]),
)
def test_manhattan(move_1, move_2, dir_1, dir_2):
    ship = Ship()
    ship.move_by(dir_1, move_1)
    ship.move_by(dir_2, move_2)

    expected = abs(move_1) + abs(move_2)
    assert expected == ship.get_manhatten_from_origin()


def test_execute():
    ship = Ship()
    ship.execute("F10")
    assert ship.pos == Vector(10, 0)
    ship.execute("L90")
    ship.execute("F5")
    assert ship.pos == Vector(10, 5)
    ship.execute("S3")
    assert ship.pos == Vector(10, 2)
    # Small test but really should be good enough.
