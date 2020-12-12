from helpers import get_data
from day12.ship import Ship, ShipAndWaypoint


def main():
    commands = get_data(day=12).split("\n")
    ship = Ship()
    for command in commands:
        ship.execute(command)

    print(ship)
    print(f"Distance from origin is {ship.get_manhatten_from_origin()}")

    # And again for the waypoint ship
    ship = ShipAndWaypoint()
    for command in commands:
        ship.execute(command)

    print(ship)
    print(f"Distance from origin is {ship.get_manhatten_from_origin()}")


if __name__ == "__main__":
    main()
