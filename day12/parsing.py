from typing import Tuple


def parse_line(line: str) -> Tuple[str, int]:
    try:
        direction = line[0]
        amount = int(line[1:])
    except (IndexError, ValueError):
        raise ValueError(f"{line} is not a valid input.")
    return direction, amount
