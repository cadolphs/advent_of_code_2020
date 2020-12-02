from itertools import combinations
from typing import Iterable
from operator import mul
from functools import reduce


def product(items: Iterable[int], start=1) -> int:
    return reduce(mul, items, start)


def expense_check(expenses: Iterable[int], num_numbers=2) -> int:
    for combination in combinations(expenses, num_numbers):
        if sum(combination) == 2020:
            return product(combination)
    raise InvalidInputException(f"No {num_numbers} numbers add up to 2020.")


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