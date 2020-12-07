from helpers import get_data
from typing import List


def unique_letters_in_strings(strings: List[str]) -> int:
    return len(set("".join(strings)))


def all_shared_letters_in_strings(strings: List[str]) -> int:
    if not strings:
        return 0
    start_set = set(strings[0])
    return len(start_set.intersection(*(set(string) for string in strings[1:])))


def split_input_to_blocks(data: str) -> List[str]:
    return data.split("\n\n")


def split_block_to_lines(block: str) -> List[str]:
    return block.split("\n")


def data_to_block_as_lines(data: str) -> List[List[str]]:
    return [split_block_to_lines(block) for block in split_input_to_blocks(data)]


def sum_all_unique(data):
    return sum(
        unique_letters_in_strings(lines) for lines in data_to_block_as_lines(data)
    )


def sum_all_present(data):
    return sum(
        all_shared_letters_in_strings(lines) for lines in data_to_block_as_lines(data)
    )


def main():
    data = get_data(day=6)

    ans = sum_all_unique(data)

    print(f"The answer is {ans}.")

    ans = sum_all_present(data)
    print(f"Achtually, it is {ans}.")


if __name__ == "__main__":
    main()
