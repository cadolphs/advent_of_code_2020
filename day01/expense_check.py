from itertools import combinations
from typing import Iterable, Tuple
from operator import mul
from functools import reduce


def product(items: Iterable[int], start=1) -> int:
    return reduce(mul, items, start)


def expense_check(expenses: Iterable[int], num_numbers=2) -> int:
    for combination in combinations(expenses, num_numbers):
        if sum(combination) == 2020:
            return product(combination)
    raise InvalidInputException(f"No {num_numbers} numbers add up to 2020.")


def check_pair(items: Iterable[int], sum_goal=2020) -> Tuple[int, int]:
    item_set = set(items)
    item_compliment = {sum_goal - item for item in item_set}

    matches = item_set.intersection(item_compliment)

    some_match = matches.pop()
    return (some_match, sum_goal - some_match)


class InvalidInputException(Exception):
    pass


def main():
    from helpers.data_access import get_data

    data = get_data(day=1).split("\n")

    result = expense_check((int(entry) for entry in data))

    print(f"Expense check result is {result}")

    result_b = expense_check((int(entry) for entry in data), num_numbers=3)

    print(f"Extended xpense check result is {result_b}")


if __name__ == "__main__":
    main()