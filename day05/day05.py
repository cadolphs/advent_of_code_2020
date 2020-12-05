from typing import Tuple
from helpers import get_data


def translate_string(text: str, zero_letter: str, one_letter: str) -> str:
    return text.translate(
        str.maketrans(
            {
                zero_letter: "0",
                one_letter: "1",
            }
        )
    )


def translate_and_decode_string(text: str, zero_letter: str, one_letter: str) -> int:
    try:
        return int(translate_string(text, zero_letter, one_letter), base=2)
    except ValueError:
        raise ValueError(
            f"Cannot decode string {text} with {zero_letter} as 0 and {one_letter} as 1"
        )


def translate_problem_input(text: str) -> Tuple[int, int]:
    try:
        row_string, col_string = text[:7], text[7:]
    except IndexError:
        raise ValueError("Invalid problem input; not a string of length 10.")

    row_number = translate_and_decode_string(row_string, "F", "B")
    col_number = translate_and_decode_string(col_string, "L", "R")

    return (row_number, col_number)


def compute_checksum(seat: Tuple[int, int]) -> int:
    return seat[0] * 8 + seat[1]


def main():
    data = get_data(day=5).split("\n")

    max_id = max(
        compute_checksum(translate_problem_input(boarding_pass))
        for boarding_pass in data
    )

    print(f"Highest seat ID is {max_id}")


if __name__ == "__main__":
    main()
