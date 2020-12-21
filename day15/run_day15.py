import time
from day15.number_game import get_nth_number
from helpers import get_data


def main():
    start_numbers = [int(num) for num in get_data(day=15).split(",")]

    number_2020 = get_nth_number(start_numbers, 2020)

    print(f"The 2020th number is {number_2020}")

    start = time.time()
    number_300000000 = get_nth_number(start_numbers, 30000000)
    duration = time.time() - start
    print(f"The 30000000th number is {number_300000000}")
    print(f"This took {duration}.")


if __name__ == "__main__":
    main()