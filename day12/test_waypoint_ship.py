from day12.ship import ShipAndWaypoint, Vector


def test_forward():
    ship = ShipAndWaypoint()

    ship.forward(10)

    assert Vector(100, 10) == ship.pos


def test_move_by():
    ship = ShipAndWaypoint()
    ship.forward(10)
    ship.execute("N3")

    assert Vector(10, 4) == ship.waypoint


def test_turn():
    ship = ShipAndWaypoint()
    ship.forward(10)
    ship.execute("N3")
    ship.execute("R90")

    assert Vector(4, -10) == ship.waypoint