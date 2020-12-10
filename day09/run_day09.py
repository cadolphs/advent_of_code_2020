from day09.sequence_finder import RangeFinder
from day09.rolling_numbers import NumberRoller
from helpers import get_data


def main():
    data = get_data(day=9).split("\n")
    numbers = [int(line) for line in data]

    preamble = numbers[:25]

    roller = NumberRoller(preamble)

    first_invalid = roller.find_first_invalid_number(numbers[25:])

    print(f"First invalid number is {first_invalid}")

    low, high = RangeFinder.find_number_in_range(numbers, first_invalid)
    check_range = numbers[low : high + 1]
    smallest, largest = min(check_range), max(check_range)

    answer = smallest + largest

    print(f"Checking the smallest plus largest in range gives {answer}")


if __name__ == "__main__":
    main()
