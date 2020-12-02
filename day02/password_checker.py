from collections import namedtuple
from typing import Iterable

InputLine = namedtuple("InputLine", ("low", "high", "letter", "password"))


def is_password_valid(low: int, high: int, letter: str, password: str) -> bool:
    return low <= password.count(letter) <= high


def parse_input_line(line: str) -> InputLine:
    tokens = line.split(" ")

    low_high = tokens[0].split("-")
    letter = tokens[1][:-1]
    password = tokens[2]

    low, high = int(low_high[0]), int(low_high[1])

    return InputLine(low, high, letter, password)


def count_valid(inputs: Iterable[InputLine]) -> int:
    return sum(1 for input in inputs if is_password_valid(*input))


def main():
    from helpers.data_access import get_data

    data = get_data(day=2).split("\n")
    inputs = (parse_input_line(line) for line in data)

    count = count_valid(inputs)

    print(f"There are {count} valid passwords.")


if __name__ == "__main__":
    main()
