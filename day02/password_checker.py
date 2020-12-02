from collections import namedtuple
from typing import Iterable
from itertools import tee

InputLine = namedtuple("InputLine", ("low", "high", "letter", "password"))


def is_password_valid(low: int, high: int, letter: str, password: str) -> bool:
    return low <= password.count(letter) <= high


def is_password_valid_v2(low: int, high: int, letter: str, password: str) -> bool:
    return (password[low - 1] == letter) ^ (password[high - 1] == letter)


def parse_input_line(line: str) -> InputLine:
    tokens = line.split(" ")

    low_high = tokens[0].split("-")
    letter = tokens[1][:-1]
    password = tokens[2]

    low, high = int(low_high[0]), int(low_high[1])

    return InputLine(low, high, letter, password)


def count_valid(inputs: Iterable[InputLine], checker=is_password_valid) -> int:
    return sum(1 for input in inputs if checker(*input))


def main():
    from helpers.data_access import get_data

    data = get_data(day=2).split("\n")
    inputs = (parse_input_line(line) for line in data)

    inputs_1, inputs_2 = tee(inputs)
    count = count_valid(inputs_1)

    print(f"There are {count} valid passwords.")

    count_v2 = count_valid(inputs_2, checker=is_password_valid_v2)
    print(f"Actually there's {count_v2} valid passwords.")


if __name__ == "__main__":
    main()
