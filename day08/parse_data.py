from typing import Tuple


def parse_line(line: str) -> Tuple[str, int]:
    tokens = line.strip().split(" ")
    if len(tokens) != 2:
        raise ValueError(f"{line} is not valid operator argument line")
    op = tokens[0]
    try:
        arg = int(tokens[1])
    except ValueError:
        raise ValueError(f"{tokens[1]} cannot be converted into a numerical argument")

    return op, arg