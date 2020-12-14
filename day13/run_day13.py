from day13.extended_gcd import solve_congruences
from typing import Iterable, List, Tuple
from operator import itemgetter
from helpers import get_data


def wait_time_for(from_time: int, interval: int) -> int:
    # from_time_past_last_departure = from_time % interval
    # time_to_next_departure = -from_time_past_last_departure % interval
    # We see how the above can be simplified
    return (-from_time) % interval


def find_interval_with_smallest_wait_time_for(
    from_time: int, intervals: Iterable[int]
) -> int:
    return min(
        ((interval, wait_time_for(from_time, interval)) for interval in intervals),
        key=itemgetter(1),
    )


def parse_input(data: str) -> Tuple[int, List[int]]:
    lines = data.split("\n")
    from_time = int(lines[0])
    bus_ids = list(extract_bus_ids(lines[1]))
    return from_time, bus_ids


def parse_input_with_positions(data: str) -> Tuple[int, List[Tuple[int, int]]]:
    lines = data.split("\n")
    from_time = int(lines[0])
    id_and_pos = list(extract_bus_ids_with_pos(lines[1]))

    return from_time, id_and_pos


def extract_bus_ids(line: str):
    for entry in line.split(","):
        if entry != "x":
            yield int(entry)


def extract_bus_ids_with_pos(line: str):
    for i, entry in enumerate(line.split(",")):
        if entry != "x":
            yield (int(entry), i)


def main():
    from_time, intervals = parse_input(get_data(day=13))

    best_id, wait_time = find_interval_with_smallest_wait_time_for(from_time, intervals)

    print(f"Take bus {best_id} to wait just {wait_time} minutes.")
    print(f"Puzzle solution: {best_id * wait_time}")

    _, ids_with_pos = parse_input_with_positions(get_data(day=13))

    congruences = [(-pos, bus_id) for bus_id, pos in ids_with_pos]
    t = solve_congruences(congruences)
    print(f"At time {t} the buses will all beautifully line up.")


if __name__ == "__main__":
    main()
